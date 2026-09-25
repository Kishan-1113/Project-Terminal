// Server-side Go engine.
//
//   - Opens a WebSocket endpoint (/ws) that any number of clients can connect to.
//   - Communicates with the Python model through HTTP.
//   - Keeps WebSocket connections persistent with periodic ping/pong.
//   - Every message received from a client is forwarded to the Python model
//     through HTTP.
//   - The Python model returns the generated output through HTTP.
//   - The output is sent back to the same WebSocket client.
//
// IMPORTANT:
//   - WebSocket configuration is intentionally unchanged.
//   - Python is now an independent HTTP service.
//   - In Docker, use the Python service name, e.g.
//     http://python-model:8000
package main

import (
	"encoding/json"
	"flag"
	"log"
	"net/http"
	"strings"
	"time"

	"github.com/google/uuid"
	"github.com/gorilla/websocket"
)

// ---------- Wire protocol ----------

// ClientMessage is what a client sends over the WebSocket.
type ClientMessage struct {
	ID      string `json:"id,omitempty"`      // optional client-supplied id, echoed back
	Type    string `json:"type"`              // "message" | "ping"
	Payload string `json:"payload,omitempty"` // the actual text/data sent to the model
}

// ServerMessage is what the server sends back over the WebSocket.
type ServerMessage struct {
	ID      string `json:"id,omitempty"`
	Type    string `json:"type"` // "response" | "pong" | "error" | "info"
	Payload string `json:"payload,omitempty"`
	Error   string `json:"error,omitempty"`
}

// ---------- Model HTTP client ----------

// ModelClient communicates with the Python model through HTTP.
type ModelClient struct {
	baseURL    string
	httpClient *http.Client
}

type ModelRequest struct {
	Input string `json:"input"`
}

type ModelResponse struct {
	Output string `json:"output"`
	Error  string `json:"error,omitempty"`
}

func NewModelClient(baseURL string) *ModelClient {

	return &ModelClient{
		baseURL: strings.TrimRight(baseURL, "/"),

		httpClient: &http.Client{
			Timeout: modelTimeout,
		},
	}
}

// Ask sends input to the Python model through HTTP.
func (mc *ModelClient) Ask(input string) (string, error) {

	requestBody := ModelRequest{
		Input: input,
	}

	data, err := json.Marshal(requestBody)
	if err != nil {
		return "", err
	}

	req, err := http.NewRequest(
		http.MethodPost,
		mc.baseURL+"/predict",
		strings.NewReader(string(data)),
	)
	if err != nil {
		return "", err
	}

	req.Header.Set(
		"Content-Type",
		"application/json",
	)

	resp, err := mc.httpClient.Do(req)
	if err != nil {
		return "", err
	}

	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", &modelError{
			msg: "model returned HTTP status " + resp.Status,
		}
	}

	var result ModelResponse

	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return "", err
	}

	if result.Error != "" {
		return "", &modelError{
			msg: result.Error,
		}
	}

	return result.Output, nil
}

type modelError struct {
	msg string
}

func (e *modelError) Error() string {
	return e.msg
}

// ---------- WebSocket handling ----------

var upgrader = websocket.Upgrader{
	ReadBufferSize:  4096,
	WriteBufferSize: 4096,
	// Allow any origin. Tighten this in production (check r.Header.Get("Origin")).
	CheckOrigin: func(r *http.Request) bool { return true },
}

const (
	writeWait      = 10 * time.Second
	pongWait       = 60 * time.Second
	pingInterval   = (pongWait * 9) / 10
	modelTimeout   = 30 * time.Second
	maxMessageSize = 1 << 20 // 1 MB
)

type Hub struct {
	model *ModelClient
}

func (h *Hub) serveWs(w http.ResponseWriter, r *http.Request) {

	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Printf("upgrade error: %v", err)
		return
	}

	log.Printf("client connected: %s", conn.RemoteAddr())

	conn.SetReadLimit(maxMessageSize)

	conn.SetReadDeadline(
		time.Now().Add(pongWait),
	)

	conn.SetPongHandler(func(string) error {

		conn.SetReadDeadline(
			time.Now().Add(pongWait),
		)

		return nil
	})

	// writeCh serializes all writes to this connection: the read loop and
	// the pinger both want to write, and gorilla/websocket only allows one
	// writer at a time.
	writeCh := make(chan ServerMessage, 32)

	done := make(chan struct{})

	go h.writePump(
		conn,
		writeCh,
		done,
	)

	h.readPump(
		conn,
		writeCh,
		done,
	)
}

func (h *Hub) writePump(
	conn *websocket.Conn,
	writeCh <-chan ServerMessage,
	done <-chan struct{},
) {

	ticker := time.NewTicker(pingInterval)

	defer ticker.Stop()
	defer conn.Close()

	for {

		select {

		case msg, ok := <-writeCh:

			conn.SetWriteDeadline(
				time.Now().Add(writeWait),
			)

			if !ok {

				conn.WriteMessage(
					websocket.CloseMessage,
					[]byte{},
				)

				return
			}

			if err := conn.WriteJSON(msg); err != nil {

				log.Printf(
					"write error: %v",
					err,
				)

				return
			}

		case <-ticker.C:

			conn.SetWriteDeadline(
				time.Now().Add(writeWait),
			)

			if err := conn.WriteMessage(
				websocket.PingMessage,
				nil,
			); err != nil {
				return
			}

		case <-done:

			return
		}
	}
}

func (h *Hub) readPump(
	conn *websocket.Conn,
	writeCh chan<- ServerMessage,
	done chan<- struct{},
) {

	defer func() {

		close(done)

		log.Printf(
			"client disconnected: %s",
			conn.RemoteAddr(),
		)
	}()

	for {

		var msg ClientMessage

		if err := conn.ReadJSON(&msg); err != nil {

			if websocket.IsUnexpectedCloseError(
				err,
				websocket.CloseGoingAway,
				websocket.CloseNormalClosure,
			) {

				log.Printf(
					"read error: %v",
					err,
				)
			}

			return
		}

		switch msg.Type {

		case "ping":

			// Application-level ping.
			writeCh <- ServerMessage{
				ID:   msg.ID,
				Type: "pong",
			}

		case "message":

			reqID := msg.ID

			if reqID == "" {
				reqID = uuid.NewString()
			}

			go func(id, input string) {

				output, err := h.model.Ask(input)

				if err != nil {

					writeCh <- ServerMessage{
						ID:    id,
						Type:  "error",
						Error: err.Error(),
					}

					return
				}

				log.Printf(
					"generated output for id=%s: %s",
					id,
					output,
				)

				writeCh <- ServerMessage{
					ID:      id,
					Type:    "response",
					Payload: output,
				}

			}(reqID, msg.Payload)

		default:

			writeCh <- ServerMessage{
				ID:    msg.ID,
				Type:  "error",
				Error: "unknown message type: " + msg.Type,
			}
		}
	}
}

// ---------- main ----------

func main() {

	addr := flag.String(
		"addr",
		":8080",
		"listen address",
	)

	modelURL := flag.String(
		"model-url",
		"http://python-model:8000",
		"URL of the Python model service",
	)

	flag.Parse()

	model := NewModelClient(
		*modelURL,
	)

	hub := &Hub{
		model: model,
	}

	mux := http.NewServeMux()

	mux.HandleFunc(
		"/ws",
		hub.serveWs,
	)

	mux.HandleFunc(
		"/healthz",
		func(w http.ResponseWriter, r *http.Request) {

			w.WriteHeader(
				http.StatusOK,
			)

			w.Write(
				[]byte("ok"),
			)
		},
	)

	log.Printf(
		"server listening on %s (ws endpoint: /ws)",
		*addr,
	)

	log.Printf(
		"python model service: %s",
		*modelURL,
	)

	if err := http.ListenAndServe(
		*addr,
		mux,
	); err != nil {

		log.Fatalf(
			"server error: %v",
			err,
		)
	}
}
