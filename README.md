# MyTerm: Natural-Language Terminal Assistant

MyTerm lets a user describe a terminal task in natural language and receive the corresponding command in a terminal-style desktop interface. The intent model runs on a server, while commands run on the user's own computer.

The project separates the desktop interface and command execution from model inference. The Go client maintains the network connection and relays messages; the Go server exposes the remote WebSocket API and calls the Python model service over HTTP.

```text
User
  |
  v
Python/Tkinter terminal GUI -- local WebSocket --> Go desktop client
                                                     |
                                               persistent WebSocket
                                                     |
                                                     v
                                              Go server -- HTTP POST /predict --> Python intent model
                                                     ^
                                                     |
                        command response over the same connections
```

## Problem It Solves

A conventional terminal requires users to know command names, flags, and syntax. MyTerm aims to let users ask for terminal tasks in natural language, including supported Hinglish phrases, and translate those requests into commands from a curated registry.

The model does not run a shell remotely. It classifies the request into an intent, fills command parameters from quoted text when needed, and returns a command string. The desktop client receives that string and executes it on the user's machine. This keeps file access and command effects local, but means the client machine is the security boundary; see [Security](#security-and-limitations).

## Project Layout

```text
Terminal Project/
|-- README.md                         # This project manual
|-- Client Side/
|   |-- main.go                       # Local WebSocket relay and bundled GUI launcher
|   |-- terminal.py                   # Tkinter terminal UI and local command execution
|   |-- terminal.exe                  # Embedded Windows GUI executable
|   |-- go.mod
|   `-- README.md                     # Earlier client notes
`-- Server Side/
    |-- main.go                        # Remote WebSocket server and HTTP model client
    |-- Dockerfile                     # Go server image
    |-- docker-compose.yml             # Go server + Python model services
    |-- go.mod
    |-- python/
    |   |-- engine.py                  # Intent classifier and FastAPI model API
    |   |-- intents_new.py             # Example utterances grouped by intent
    |   |-- command_registry.py         # Approved command templates and required slots
    |   |-- requirements.txt
    |   `-- Dockerfile                  # Python model image and model-cache download
    `-- README.md                      # Earlier server notes
```

## Components And Technology

| Component | Technology | Purpose |
|---|---|---|
| Desktop terminal | Python, Tkinter | Displays terminal output, accepts typed or natural-language input, handles a small set of built-ins, and runs returned commands locally. |
| Desktop relay | Go, Gorilla WebSocket | Provides the GUI's local WebSocket endpoint, keeps a remote WebSocket open, forwards messages, reconnects after failures, and reports link status and latency. |
| Remote API | Go, Gorilla WebSocket | Accepts desktop sessions, handles request IDs and ping/pong messages, and invokes the model service for requests. |
| Intent service | Python, FastAPI, Sentence Transformers, PyTorch, NumPy | Encodes the request, finds its closest configured intent, extracts required values, and returns a registry command. |
| Semantic model | `intfloat/multilingual-e5-small` | Compares multilingual user phrases with example phrases, avoiding a requirement that users memorize exact command syntax. |
| Containers | Docker, Docker Compose | Run the Go API and Python model as separate services on a private Compose bridge network. |

Go is used for the long-lived network relays and concurrent request handling. Python is used for the model and the existing GUI. WebSockets suit the interactive terminal because one connection can carry many requests and responses without reconnecting for every command. HTTP is used between the Go server and Python model because inference is a request/response operation and can be containerized independently.

## Request Processing

1. The user enters a natural-language task in the Tkinter terminal. The GUI sends a JSON `message` with an ID and input text to the local Go client.
2. The client forwards it across its persistent WebSocket to the remote Go server. If the GUI did not provide an ID, the client assigns one.
3. The Go server sends `POST /predict` with `{"input":"..."}` to the Python service. The server applies a 30-second HTTP timeout.
4. The Python model encodes the query with the E5 `query:` prefix. At startup, it encodes intent examples using `passage:`, with normalized embeddings. It selects the highest similarity; scores below the current `0.75` threshold are rejected as unknown.
5. For a recognized intent, the model looks up its command template in `command_registry.py`. Required values are currently extracted from double-quoted input segments. Missing values or low confidence become an error response.
6. The Go server returns the command as a WebSocket `response`. The Go client relays it to the GUI, which executes it locally and renders standard output and standard error in the terminal window.

The semantic model chooses among configured intents; it does not freely generate arbitrary shell commands. However, the current slot extraction and shell execution behavior still require careful treatment (see [Security](#security-and-limitations)).

## Network Protocol

### Connections

- GUI to desktop Go client: `ws://127.0.0.1:9001/ws` by default. This is local to the desktop machine.
- Desktop Go client to remote Go server: `ws://<server-host>:8080/ws` by default in Compose. Use `wss://` when TLS is configured for a real deployment.
- Go server to Python model: `http://python-model:8000/predict` inside the Compose network. This is service-to-service HTTP and is not published to the host by Compose.

The desktop client opens its remote connection when a GUI WebSocket session connects. It keeps that connection for the session and reconnects with exponential delay from 1 second up to 30 seconds if the remote connection fails. Closing the GUI connection closes the associated remote connection.

### WebSocket Messages

Messages are JSON objects. Typical examples:

```json
{"id":"request-uuid","type":"message","payload":"create a folder named \"reports\""}
{"id":"request-uuid","type":"response","payload":"mkdir reports"}
{"id":"request-uuid","type":"error","error":"Couldn't confidently classify..."}
{"id":"ping-uuid","type":"ping"}
{"id":"ping-uuid","type":"pong"}
{"type":"status","status":"connected","ping_ms":12.4}
```

The client and server use application-level ping/pong messages to measure round-trip latency. The client measures both GUI-to-client and client-to-server links approximately every five seconds and logs a combined network snapshot every ten seconds. The server also sends WebSocket control-frame pings approximately every 54 seconds; its 60-second read deadline is refreshed by pong frames. Application pings are distinct from WebSocket control frames.

On the model boundary, Go sends `{"input":"..."}` to `/predict`; Python returns `{"output":"...","error":"..."}`. The Python health endpoint is `GET /healthz`; the Go server health endpoint is also `GET /healthz`.

## Run With Docker Compose

Docker Compose runs the remote backend only (Go API plus Python model). The desktop Go client and GUI run on the Windows host so commands are executed on that host, not inside a container.

Prerequisites:

- Docker Desktop with Docker Compose v2
- Go 1.22 or newer on the Windows desktop if running the client from source
- Network access during the first image build to download dependencies and the Hugging Face model

From the project root in PowerShell:

```powershell
docker compose -f "Server Side/docker-compose.yml" up --build
```

The first build can take a while: the Python image installs CPU-only PyTorch/model dependencies and downloads `intfloat/multilingual-e5-small` into its image cache. Later starts reuse built images. Compose waits for the Python service health check before starting the Go server.

In another PowerShell terminal, start the desktop client and point it at the Compose-published Go server:

```powershell
Set-Location "Client Side"
go run . -remote ws://127.0.0.1:8080/ws
```

The Go client binds its local GUI endpoint on `127.0.0.1:9001` and launches the bundled `terminal.exe`. Enter a supported natural-language request in the window. The client currently defaults to launching the bundled GUI; its optional `-gui` flag can select an external GUI executable.

Useful Compose commands, run from the project root:

```powershell
# Show service state and health
docker compose -f "Server Side/docker-compose.yml" ps

# Follow backend logs
docker compose -f "Server Side/docker-compose.yml" logs -f

# Stop and remove the containers and Compose network
docker compose -f "Server Side/docker-compose.yml" down
```

The Go API is published on host port `8080`. The Python model's port `8000` is exposed only to the private Compose network. To change the remote API port, update the `ports` mapping in `Server Side/docker-compose.yml` and use the corresponding host port in the client `-remote` URL.

## Run Without Docker

This path runs both backend processes on the host. In PowerShell, open three terminals.

### 1. Prepare Python And Download The Model

From the project root:

```powershell
Set-Location "Server Side"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r python/requirements.txt

$env:HF_HOME = Join-Path $PWD ".cache\huggingface"
$env:HF_HUB_OFFLINE = "0"
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='intfloat/multilingual-e5-small')"
$env:HF_HUB_OFFLINE = "1"
python -m uvicorn engine:app --app-dir python --host 127.0.0.1 --port 8000
```

Keep this terminal running. The Python process loads the model and builds example embeddings during startup.

### 2. Start The Go Server

In a second terminal, from the project root:

```powershell
Set-Location "Server Side"
go run . -addr :8080 -model-url http://127.0.0.1:8000
```

### 3. Start The Desktop Client

In a third terminal:

```powershell
Set-Location "Client Side"
go run . -local-addr 127.0.0.1:9001 -remote ws://127.0.0.1:8080/ws
```

Closing the GUI also shuts down the Go client process. Stop the Go server and Python model with `Ctrl+C` in their respective terminals.

## Configuration And Operations

- Go server: `-addr` sets its HTTP/WebSocket listen address; `-model-url` sets the Python service base URL.
- Go client: `-local-addr` sets the GUI-facing listen address; `-remote` sets the server WebSocket URL; `-insecure-skip-verify` disables TLS certificate verification for development only. Do not use that flag in production.
- Model matching: `classify()` in `Server Side/python/engine.py` currently uses a similarity threshold of `0.75`.
- Supported natural-language tasks are defined in `Server Side/python/intents_new.py`; their actual command templates and required slots are in `Server Side/python/command_registry.py`.
- Add or change an intent by keeping its intent key consistent between the example phrases and command registry. The model computes intent-example embeddings once when the Python process starts.
- Docker health endpoints are available at `http://localhost:8080/healthz` for Go and internally at `http://python-model:8000/healthz` for Python.

## Security And Limitations

- **Commands execute on the desktop host.** The GUI runs non-built-in returned commands with `subprocess.Popen(..., shell=True)`. Treat the model server and network as trusted, review changes to command templates, and do not expose the server publicly as-is.
- The `confirm` values in the registry are metadata only in the current code; the GUI does not implement a confirmation step before execution. Destructive or remote commands can therefore run as soon as returned by the model.
- The WebSocket upgrade handlers currently allow every origin and there is no authentication. Restrict origins and add authentication before deployment beyond a trusted network.
- Plain `ws://` and the internal Compose HTTP link are unencrypted. Use TLS (`wss://`) for remote traffic and secure the Python service/network appropriately when deploying across hosts.
- Model errors and malformed/unsupported requests are surfaced to the GUI, but intent classification and quoted-slot extraction are deliberately simple. Test intents and arguments, especially paths, names, and shell-special characters.
- The model service is CPU-only in the supplied Dockerfile. Latency and memory use depend on the host and model runtime.
- The desktop client embeds a Windows GUI executable (`terminal.exe`) and is currently intended to run on Windows. The GUI and command executor run with the user's operating-system permissions.

## Troubleshooting

- **Go server cannot reach the model:** With Compose, check `docker compose ... ps` and logs; the server must use `http://python-model:8000`, not `localhost`, because `localhost` inside the Go container refers to that container. Outside Compose, use `http://127.0.0.1:8000`.
- **Python model fails at startup:** Verify the model download completed and that `HF_HOME` points to the same cache used when downloading. In Docker, rebuild with network access if the image build did not complete the model snapshot download.
- **Client cannot connect:** Confirm the Go server is healthy on port `8080`, the `-remote` URL ends in `/ws`, and the local port `9001` is free.
- **Request reports unknown intent or missing info:** Use a phrasing represented in `intents_new.py`; provide required values in double quotes for the current slot extractor.

The component-level README files point back to this consolidated manual.
