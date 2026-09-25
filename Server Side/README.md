# Go Engine: Server + Client, WebSocket bridge to a Python model/GUI

```
Python GUI  <--local WS-->  Go client engine  <--WS (persistent)-->  Go server  <--stdin/stdout-->  Python model
```

## Layout

```
go-engine/
├── server/
│   ├── main.go     # WebSocket server, multiplexes clients onto one Python model process
│   └── go.mod
├── client/
│   ├── main.go     # Local WS server for the GUI + persistent remote WS client with ping/reconnect
│   └── go.mod
├── python/
│   ├── model_server.py  # persistent model process (replace run_model() with real inference)
│   └── gui_client.py    # example tkinter GUI
└── README.md
```

## 1. Server side (`server/main.go`)

- Exposes `ws://<host>:8080/ws` — any number of clients can connect concurrently.
- On startup it spawns **one** long-lived Python subprocess (`python/model_server.py`)
  and keeps it alive for the server's whole lifetime — the model loads once, not
  per connection/request.
- Every message from a client is tagged with a request ID and written to the
  model's stdin as one JSON line; the model's stdout is read continuously and
  each response is routed back to the client that asked for it (safe with many
  concurrent clients hammering the same model process).
- Connections are kept open: a ticker sends WS ping control frames every ~54s
  and a 60s read deadline resets on every pong, so dead sockets are detected
  and cleaned up quickly instead of leaking.

Run it:

```bash
cd server
go build -o server .
./server -addr=:8080 -python=python3 -script=../python/model_server.py
```

Flags: `-addr` (listen address), `-python` (interpreter), `-script` (path to the model script).

## 2. Client side (`client/main.go`)

- Runs a small local WebSocket server, default `ws://127.0.0.1:9001/ws`, for the
  Python GUI to connect to.
- The instant the GUI's local WebSocket connects, the Go engine dials the
  **remote** server and keeps that connection open for as long as the GUI
  session lasts — not one connection per message.
- If the remote connection drops, it reconnects automatically with exponential
  backoff (1s → 2s → 4s ... capped at 30s) and reports `status: "reconnecting"`
  / `"disconnected"` to the GUI the whole time.
- Every ~5 seconds it sends an application-level `ping` to the remote server
  and times the matching `pong`, then pushes `{"type":"status","ping_ms":...}`
  to the GUI — this is your live "network strength" indicator.
- When the GUI closes its local socket, the Go engine tears down the remote
  connection too (no dangling sockets).

Run it:

```bash
cd client
go build -o client .
./client -local-addr=127.0.0.1:9001 -remote=ws://<server-host>:8080/ws
```

Flags: `-local-addr` (where the GUI connects), `-remote` (the remote server's WS URL).

## 3. Python model (`python/model_server.py`)

Speaks line-delimited JSON over stdin/stdout:

```
stdin:  {"id": "...", "input": "..."}
stdout: {"id": "...", "output": "..."}
```

Load your real model once at the top of the file (commented example included
for a HuggingFace/transformers model) and replace the body of `run_model()`
with a real inference call. Everything else (the loop, flushing, error
handling, request/response IDs) already works and is wired end-to-end.

## 4. Python GUI (`python/gui_client.py`)

A minimal tkinter example. `pip install websocket-client`, then run it. It:

- Connects to the local Go client engine the moment the window opens.
- Reconnects to the local engine if that connection drops, while the window
  stays open.
- Sends whatever you type as `{"type": "message", "payload": "..."}`.
- Renders `response` messages from the model, and shows connection status +
  live ping in the top bar.
- Closing the window closes the socket, which signals the Go client engine to
  tear down the remote connection.

## Wire protocol (shared shape used everywhere)

```json
{"id": "uuid", "type": "message", "payload": "text to send"}
{"id": "uuid", "type": "response", "payload": "text from model"}
{"type": "ping"}                                  // app-level ping
{"type": "pong"}
{"type": "status", "status": "connected", "ping_ms": 12.4}
{"type": "error", "error": "description"}
```

## Full run order

```bash
# 1. terminal 1 — the remote server (wherever it's deployed)
cd server && ./server -addr=:8080 -script=../python/model_server.py

# 2. terminal 2 — the client machine's Go engine (point -remote at the server's address)
cd client && ./client -remote=ws://<server-ip>:8080/ws

# 3. terminal 3 — the GUI
pip install websocket-client
python3 python/gui_client.py
```

This exact end-to-end flow (GUI → local Go engine → remote Go server → Python
model → back through the same two persistent WebSockets) was built and
verified in this environment: messages round-trip correctly, ping is measured
and reported every ~5s, and killing/restarting the remote server triggers
automatic backoff-reconnect without the GUI needing to do anything.

## Notes / things to harden for production

- `CheckOrigin` is currently permissive (`return true`) on both upgraders —
  restrict it once you know your deployment origins.
- Add TLS (`wss://`) termination in front of the server (e.g. nginx/Caddy, or
  `http.ListenAndServeTLS` directly) before exposing it over the open internet.
- Add auth (a token in the initial message, or an `Authorization` header
  checked in `serveWs`) before accepting client connections in production.
- The model timeout is 30s (`modelTimeout` in `server/main.go`) — raise it if
  your real model is slower.




  ┌─────────────┐   local WS    ┌──────────────────┐    remote WS      ┌──────────────┐   stdin/stdout   ┌──────────────┐
│ Python GUI  │◄─────────────►│ Go client engine │◄─────────────────►│  Go server   │◄────────────────►│ Python model │
│ (user's PC) │  127.0.0.1    │  (user's PC)     │   internet/LAN    │ (your infra) │   (same box)      │ (same box)   │
└─────────────┘               └──────────────────┘                    └──────────────┘                   └──────────────┘




