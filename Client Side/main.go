//		Python terminal.py  <--local WebSocket-->  Go client engine  <--WebSocket-->  Remote server
//
//	  - Starts listening on a local WebSocket endpoint FIRST, THEN launches
//	    terminal.py as a subprocess -- this guarantees the local server is
//	    already accepting connections before Python's first connect attempt,
//	    so you never get a "connection refused" race on startup.
//	  - As soon as the GUI connects locally, the Go engine opens (and keeps
//	    open) a persistent WebSocket connection to the remote server,
//	    reconnecting with backoff if it drops.
//	  - Continuously measures round-trip latency to the remote server ("ping")
//	    and pushes it to the GUI so it can show network strength.
//	  - Forwards every message from the GUI to the remote server, and every
//	    response from the remote server back to the GUI, over the same
//	    persistent connections (no per-message reconnects).
//	  - When the GUI's local connection closes (GUI closed), the remote
//	    connection is torn down too, AND the python subprocess is terminated.
package main

import (
	"crypto/tls"
	_ "embed"
	"flag"
	"log"
	"math"
	"net"
	"net/http"
	"os"
	"os/exec"
	"sync"
	"time"

	"github.com/google/uuid"
	"github.com/gorilla/websocket"
)

// ---------- Wire protocol (GUI <-> Go client, same shape reused remotely) ----------

type WireMessage struct {
	ID      string  `json:"id,omitempty"`
	Type    string  `json:"type"` // "message" | "response" | "ping" | "pong" | "status" | "error"
	Payload string  `json:"payload,omitempty"`
	Error   string  `json:"error,omitempty"`
	PingMS  float64 `json:"ping_ms,omitempty"` // populated on "status" messages
	Status  string  `json:"status,omitempty"`  // "connected" | "disconnected" | "reconnecting"
}

const (
	remoteReadTimeout  = 60 * time.Second
	remotePingInterval = 5 * time.Second // how often we measure latency
	localPingInterval  = 5 * time.Second // how often we ping the local GUI
	writeWait          = 10 * time.Second
	reconnectMinDelay  = 1 * time.Second
	reconnectMaxDelay  = 30 * time.Second
	maxMessageSize     = 1 << 20 // 1 MB, matches the remote server's limit
	snapshotInterval   = 10 * time.Second
	pingStaleAfter     = 2 * localPingInterval // no pong within this long -> flag as unresponsive
)

// ---------- Connectivity logging ----------

// classifyLatency turns a round-trip time into a human-readable quality
// label so log lines and the GUI's status text mean something at a glance
// instead of just showing a raw number.
func classifyLatency(ms float64) string {
	switch {
	case ms <= 0:
		return "unknown"
	case ms < 50:
		return "excellent"
	case ms < 150:
		return "good"
	case ms < 400:
		return "fair"
	default:
		return "poor"
	}
}

// LinkHealth tracks the live status + latency of one hop (either
// local<->GUI or local<->remote) and logs every change immediately, so the
// console gives a real-time picture of connectivity without waiting for a
// periodic snapshot.
type LinkHealth struct {
	name string // e.g. "LOCAL<->GUI" or "LOCAL<->REMOTE"

	mu         sync.Mutex
	status     string // "connected" | "disconnected" | "reconnecting" | "unresponsive"
	pingMS     float64
	lastPingAt time.Time
}

func NewLinkHealth(name string) *LinkHealth {
	return &LinkHealth{name: name, status: "disconnected"}
}

func (h *LinkHealth) SetStatus(status string) {
	h.mu.Lock()
	changed := h.status != status
	h.status = status
	if status == "connected" && h.lastPingAt.IsZero() {
		// Give CheckStale a baseline from connection time, so a link that
		// NEVER answers a single ping (e.g. an old GUI build with no pong
		// handler) still gets flagged after pingStaleAfter -- not just
		// links that were fine once and then went quiet.
		h.lastPingAt = time.Now()
	}
	if status == "disconnected" {
		h.lastPingAt = time.Time{} // reset so the next connection gets a clean baseline
	}
	h.mu.Unlock()
	if changed {
		log.Printf("[%s] status changed -> %s", h.name, status)
	}
}

func (h *LinkHealth) RecordLatency(ms float64) {
	h.mu.Lock()
	h.pingMS = ms
	h.lastPingAt = time.Now()
	changed := h.status != "connected"
	h.status = "connected"
	h.mu.Unlock()
	quality := classifyLatency(ms)
	if changed {
		log.Printf("[%s] status changed -> connected (latency: %.1fms, quality: %s)", h.name, ms, quality)
	} else {
		log.Printf("[%s] latency: %.1fms (quality: %s)", h.name, ms, quality)
	}
}

// CheckStale marks the link "unresponsive" if the last successful
// latency measurement is older than pingStaleAfter -- catches the case
// where the TCP connection looks alive but the other side has stopped
// answering pings (e.g. an old GUI build that doesn't reply to "ping").
func (h *LinkHealth) CheckStale() {
	h.mu.Lock()
	defer h.mu.Unlock()
	if h.status == "connected" && !h.lastPingAt.IsZero() && time.Since(h.lastPingAt) > pingStaleAfter {
		h.status = "unresponsive"
		log.Printf("[%s] status changed -> unresponsive (no ping reply for over %s)", h.name, pingStaleAfter)
	}
}

func (h *LinkHealth) Snapshot() (status string, pingMS float64) {
	h.mu.Lock()
	defer h.mu.Unlock()
	return h.status, h.pingMS
}

// ---------- Remote connection manager ----------

// RemoteLink owns the persistent WebSocket connection to the remote server.
// It reconnects automatically and reports latency + status upstream via
// the toGUI channel.
type RemoteLink struct {
	url             string
	insecureSkipTLS bool
	toGUI           chan<- WireMessage
	health          *LinkHealth

	mu   sync.Mutex
	conn *websocket.Conn

	fromGUI chan WireMessage // messages coming from the GUI to forward remotely

	pendingPingsMu sync.Mutex
	pendingPings   map[string]time.Time

	stop chan struct{}
}

func NewRemoteLink(url string, insecureSkipTLS bool, toGUI chan<- WireMessage, health *LinkHealth) *RemoteLink {
	return &RemoteLink{
		url:             url,
		insecureSkipTLS: insecureSkipTLS,
		toGUI:           toGUI,
		health:          health,
		fromGUI:         make(chan WireMessage, 64),
		pendingPings:    make(map[string]time.Time),
		stop:            make(chan struct{}),
	}
}

// Run keeps a connection alive to the remote server, reconnecting with
// exponential backoff, until Close() is called.
func (r *RemoteLink) Run() {
	dialer := websocket.DefaultDialer
	if r.insecureSkipTLS {
		// DEV ONLY: skips certificate verification, e.g. for a self-signed
		// cert while testing. Never ship this on for real deployments --
		// it defeats the point of wss:// (man-in-the-middle protection).
		d := *websocket.DefaultDialer
		d.TLSClientConfig = &tls.Config{InsecureSkipVerify: true} // #nosec G402 -- opt-in dev flag only
		dialer = &d
	}

	delay := reconnectMinDelay
	for {
		select {
		case <-r.stop:
			return
		default:
		}

		conn, _, err := dialer.Dial(r.url, nil)
		if err != nil {
			log.Printf("[LOCAL<->REMOTE] dial failed: %v (retrying in %s)", err, delay)
			r.health.SetStatus("disconnected")
			r.emitStatus("disconnected", 0)
			select {
			case <-time.After(delay):
			case <-r.stop:
				return
			}
			delay = time.Duration(math.Min(float64(delay)*2, float64(reconnectMaxDelay)))
			continue
		}

		delay = reconnectMinDelay
		log.Printf("[LOCAL<->REMOTE] connected to %s", r.url)
		r.mu.Lock()
		r.conn = conn
		r.mu.Unlock()
		r.health.SetStatus("connected")
		r.emitStatus("connected", 0)

		r.handleConnection(conn) // blocks until this connection dies

		r.mu.Lock()
		r.conn = nil
		r.mu.Unlock()

		select {
		case <-r.stop:
			return
		default:
			r.health.SetStatus("reconnecting")
			r.emitStatus("reconnecting", 0)
		}
	}
}

func (r *RemoteLink) handleConnection(conn *websocket.Conn) {
	done := make(chan struct{})

	conn.SetReadDeadline(time.Now().Add(remoteReadTimeout))
	conn.SetPongHandler(func(string) error {
		conn.SetReadDeadline(time.Now().Add(remoteReadTimeout))
		return nil
	})

	// Reader: remote -> GUI
	go func() {
		defer close(done)
		for {
			var msg WireMessage
			if err := conn.ReadJSON(&msg); err != nil {
				log.Printf("[LOCAL<->REMOTE] read error: %v", err)
				return
			}
			if msg.Type == "pong" {
				r.recordPong(msg.ID)
				continue
			}
			log.Printf("[REMOTE -> GUI] type=%s id=%s payload=%q error=%q",
				msg.Type,
				msg.ID,
				msg.Payload,
				msg.Error,
			)
			r.toGUI <- msg
		}
	}()

	pingTicker := time.NewTicker(remotePingInterval)
	defer pingTicker.Stop()

	for {
		select {
		case <-done:
			conn.Close()
			return
		case <-r.stop:
			conn.Close()
			return
		case m := <-r.fromGUI:
			conn.SetWriteDeadline(time.Now().Add(writeWait))
			if err := conn.WriteJSON(m); err != nil {
				log.Printf("[LOCAL<->REMOTE] write error: %v", err)
				conn.Close()
				<-done
				return
			}
		case <-pingTicker.C:
			r.sendPing(conn)
		}
	}
}

func (r *RemoteLink) sendPing(conn *websocket.Conn) {
	id := uuid.NewString()
	r.pendingPingsMu.Lock()
	r.pendingPings[id] = time.Now()
	r.pendingPingsMu.Unlock()

	conn.SetWriteDeadline(time.Now().Add(writeWait))
	if err := conn.WriteJSON(WireMessage{ID: id, Type: "ping"}); err != nil {
		log.Printf("[LOCAL<->REMOTE] ping send error: %v", err)
	}
}

func (r *RemoteLink) recordPong(id string) {
	r.pendingPingsMu.Lock()
	start, ok := r.pendingPings[id]
	if ok {
		delete(r.pendingPings, id)
	}
	r.pendingPingsMu.Unlock()
	if !ok {
		return
	}
	rtt := time.Since(start)
	pingMS := float64(rtt.Microseconds()) / 1000.0
	r.health.RecordLatency(pingMS)
	r.emitStatus("connected", pingMS)
}

func (r *RemoteLink) emitStatus(status string, pingMS float64) {
	r.toGUI <- WireMessage{Type: "status", Status: status, PingMS: pingMS}
}

// Send queues a message to be forwarded to the remote server. Safe to call
// even while disconnected; it will be dropped if the buffer is currently
// full during a long outage rather than blocking forever.
func (r *RemoteLink) Send(m WireMessage) {
	log.Printf("[GUI -> REMOTE] type=%s id=%s payload=%q",
		m.Type,
		m.ID,
		m.Payload,
	)
	select {
	case r.fromGUI <- m:
	default:
		log.Printf("[LOCAL<->REMOTE] outbound buffer full, dropping message id=%s", m.ID)
	}
}

func (r *RemoteLink) Close() {
	close(r.stop)
	r.mu.Lock()
	if r.conn != nil {
		r.conn.Close()
	}
	r.mu.Unlock()
}

// ---------- Local WebSocket server (talks to the Python GUI) ----------

var upgrader = websocket.Upgrader{
	ReadBufferSize:  4096,
	WriteBufferSize: 4096,
	CheckOrigin:     func(r *http.Request) bool { return true },
}

type LocalServer struct {
	remoteURL       string
	insecureSkipTLS bool
}

func (s *LocalServer) serveGUI(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Printf("[LOCAL<->GUI] upgrade error: %v", err)
		return
	}
	conn.SetReadLimit(maxMessageSize)

	guiHealth := NewLinkHealth("LOCAL<->GUI")
	remoteHealth := NewLinkHealth("LOCAL<->REMOTE")
	guiHealth.SetStatus("connected") // TCP+WS handshake to the GUI just succeeded

	toGUI := make(chan WireMessage, 64)
	remote := NewRemoteLink(s.remoteURL, s.insecureSkipTLS, toGUI, remoteHealth)
	go remote.Run()

	guiDone := make(chan struct{})

	// Writer: anything destined for the GUI (remote responses, status/ping
	// updates) goes out here, serialized on a single goroutine.
	go func() {
		for {
			select {
			case msg, ok := <-toGUI:
				if !ok {
					return
				}
				conn.SetWriteDeadline(time.Now().Add(writeWait))
				if err := conn.WriteJSON(msg); err != nil {
					log.Printf("[LOCAL<->GUI] write error: %v", err)
					return
				}
			case <-guiDone:
				return
			}
		}
	}()

	// Pinger: periodically pings the LOCAL GUI connection (a separate,
	// independent measurement from the remote-link ping above) so we get
	// real latency/health data for the local hop too, not just an assumed
	// "it's on loopback so it must be fine". Requires the GUI to reply
	// with {"type":"pong",...} -- see terminal.py's on_message handler.
	pendingLocalPingsMu := sync.Mutex{}
	pendingLocalPings := make(map[string]time.Time)

	go func() {
		ticker := time.NewTicker(localPingInterval)
		staleTicker := time.NewTicker(localPingInterval)
		defer ticker.Stop()
		defer staleTicker.Stop()
		for {
			select {
			case <-guiDone:
				return
			case <-ticker.C:
				id := uuid.NewString()
				pendingLocalPingsMu.Lock()
				pendingLocalPings[id] = time.Now()
				pendingLocalPingsMu.Unlock()
				select {
				case toGUI <- WireMessage{ID: id, Type: "ping"}:
				default:
					log.Printf("[LOCAL<->GUI] outbound buffer full, skipping ping")
				}
			case <-staleTicker.C:
				guiHealth.CheckStale()
			}
		}
	}()

	// Combined snapshot: logs BOTH hops together on a fixed interval so
	// you always have a recent, at-a-glance line even if nothing changed
	// (the event-driven logs above only fire on transitions/measurements).
	go func() {
		ticker := time.NewTicker(snapshotInterval)
		defer ticker.Stop()
		for {
			select {
			case <-guiDone:
				return
			case <-ticker.C:
				gStatus, gPing := guiHealth.Snapshot()
				rStatus, rPing := remoteHealth.Snapshot()
				log.Printf(
					"[NETWORK SNAPSHOT] local<->gui: %s (%.1fms, %s) | local<->remote: %s (%.1fms, %s)",
					gStatus, gPing, classifyLatency(gPing),
					rStatus, rPing, classifyLatency(rPing),
				)
			}
		}
	}()

	log.Printf("[LOCAL<->GUI] python GUI connected")

	// Reader: everything the GUI sends gets forwarded to the remote server,
	// EXCEPT "pong" replies to our local pings, which we intercept here to
	// measure local-hop latency (mirrors how RemoteLink intercepts "pong"
	// from the remote server).
	for {
		var msg WireMessage
		if err := conn.ReadJSON(&msg); err != nil {
			log.Printf("[LOCAL<->GUI] read error / disconnected: %v", err)
			break
		}

		if msg.Type == "pong" {
			pendingLocalPingsMu.Lock()
			start, ok := pendingLocalPings[msg.ID]
			if ok {
				delete(pendingLocalPings, msg.ID)
			}
			pendingLocalPingsMu.Unlock()
			if ok {
				pingMS := float64(time.Since(start).Microseconds()) / 1000.0
				guiHealth.RecordLatency(pingMS)
			}
			continue
		}

		if msg.ID == "" {
			msg.ID = uuid.NewString()
		}
		remote.Send(msg)
	}

	close(guiDone)
	guiHealth.SetStatus("disconnected")
	remote.Close() // GUI closed -> tear down the remote connection too
	conn.Close()
	log.Printf("[LOCAL<->GUI] session ended, remote connection closed")
}

// ---------- launching the bundled terminal GUI ----------

// terminal.exe is built by PyInstaller with Python and websocket-client
// included. The Go binary embeds that executable so the default launch path
// has no Python or pip dependency on the target machine.
//

var embeddedTerminalGUI []byte

func extractEmbeddedGUI() (string, string, error) {
	tmpDir, err := os.MkdirTemp("", "myterm-gui-")
	if err != nil {
		return "", "", err
	}
	guiPath := tmpDir + "\\terminal.exe"
	if err := os.WriteFile(guiPath, embeddedTerminalGUI, 0o700); err != nil {
		os.RemoveAll(tmpDir)
		return "", "", err
	}
	return guiPath, tmpDir, nil
}

func launchGUI(guiPath, localAddr string) (*exec.Cmd, error) {
	cmd := exec.Command(guiPath)

	cmd.Env = append(os.Environ(), "GO_ENGINE_WS_URL=ws://"+localAddr+"/ws")
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Start(); err != nil {
		return nil, err
	}

	return cmd, nil
}

// ---------- main ----------

func main() {
	localAddr := flag.String("local-addr", "127.0.0.1:9001", "address to serve the local GUI-facing websocket on")
	remoteURL := flag.String("remote", "ws://myamazingsiteonaws.xyz:8080/ws", "remote server websocket URL to connect to")
	insecureSkipTLS := flag.Bool("insecure-skip-verify", false, "DEV ONLY: skip TLS certificate verification for wss:// (self-signed certs)")

	// Replace double quotes with backticks for Windows paths
	guiExecutable := flag.String("gui", "", "optional external GUI executable for development; the bundled GUI is used by default")
	flag.Parse()

	// launchGUI := flag.Bool("launch-gui", true, "launch the python terminal GUI as a subprocess automatically")

	// Bind the listener FIRST, before touching Python at all, so the
	// server is guaranteed to be accepting connections the instant
	// terminal.py tries to dial in.
	ln, err := net.Listen("tcp", *localAddr)
	if err != nil {
		log.Fatalf("failed to bind local address %s: %v", *localAddr, err)
	}

	s := &LocalServer{remoteURL: *remoteURL, insecureSkipTLS: *insecureSkipTLS}
	mux := http.NewServeMux()
	mux.HandleFunc("/ws", s.serveGUI)

	log.Printf("go client engine listening on ws://%s/ws", *localAddr)
	log.Printf("will relay to remote server at %s", *remoteURL)

	var guiCmd *exec.Cmd
	var resolvedGUI string
	var guiTempDir string

	if *guiExecutable == "" {
		resolvedGUI, guiTempDir, err = extractEmbeddedGUI()
		if err != nil {
			log.Fatalf("failed to extract embedded terminal GUI: %v", err)
		}
	} else {
		resolvedGUI = *guiExecutable
	}

	guiCmd, err = launchGUI(resolvedGUI, *localAddr)

	if err != nil {
		log.Fatalf("failed to launch terminal GUI (%s): %v", resolvedGUI, err)
	}

	log.Printf("launched terminal GUI (%s), pid=%d", resolvedGUI, guiCmd.Process.Pid)

	// If the GUI window is closed, its process exits -- shut the whole
	// engine down with it rather than leaving an orphaned Go process.
	go func() {
		guiCmd.Wait()
		if guiTempDir != "" {
			os.RemoveAll(guiTempDir)
		}
		log.Printf("python terminal GUI exited, shutting down")
		os.Exit(0)
	}()

	if err := http.Serve(ln, mux); err != nil {
		log.Fatalf("server error: %v", err)
	}
}
