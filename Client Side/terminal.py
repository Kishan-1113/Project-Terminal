import os
import sys
import threading
import subprocess
import queue
import time
import uuid
import tkinter as tk
from tkinter import font as tkfont

import websocket


IS_WINDOWS = os.name == "nt"


class TerminalGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("MyTerm")
        self.root.geometry("900x550")
        self.root.configure(bg="black")

        self.mono = tkfont.Font(
            family="Consolas" if IS_WINDOWS else "Courier New",
            size=11
        )

        self.fg = "#e6e6e6"
        self.bg = "black"
        self.prompt_color = "#57d364"
        self.error_color = "#ff6b6b"

        self.output = tk.Text(
            root,
            bg=self.bg,
            fg=self.fg,
            insertbackground=self.fg,
            font=self.mono,
            wrap="word",
            state="disabled",
            padx=8,
            pady=6
        )

        self.output.pack(fill="both", expand=True)

        # Network status / ping indicator
        self.network_status = tk.Label(
            root,
            text="● Connecting...",
            bg=self.bg,
            fg="#57d364",
            font=self.mono
        )

        self.network_status.place(
            relx=1.0,
            rely=0.0,
            anchor="ne",
            x=-12,
            y=8
        )

        self.output.tag_config(
            "prompt",
            foreground=self.prompt_color
        )

        self.output.tag_config(
            "error",
            foreground=self.error_color
        )

        self.output.tag_config(
            "normal",
            foreground=self.fg
        )

        input_frame = tk.Frame(root, bg=self.bg)
        input_frame.pack(fill="x", side="bottom")

        self.prompt_label = tk.Label(
            input_frame,
            text=self._prompt_text(),
            bg=self.bg,
            fg=self.prompt_color,
            font=self.mono,
            anchor="w"
        )

        self.prompt_label.pack(
            side="left",
            padx=(8, 0),
            pady=6
        )

        self.entry = tk.Entry(
            input_frame,
            bg=self.bg,
            fg=self.fg,
            insertbackground=self.fg,
            font=self.mono,
            relief="flat"
        )

        self.entry.pack(
            fill="x",
            expand=True,
            side="left",
            padx=(4, 8),
            pady=6
        )

        self.entry.focus_set()

        self.history = []
        self.history_index = None

        self.current_process = None

        self.out_queue = queue.Queue()

        self.ws_url = os.environ.get(
            "GO_ENGINE_WS_URL",
            "ws://127.0.0.1:8080/ws"
        )

        self.ws = None
        self.ws_lock = threading.Lock()

        self.ws_connected = threading.Event()
        self.ws_stop = threading.Event()

        self.entry.bind("<Return>", self.on_enter)
        self.entry.bind("<Up>", self.on_history_up)
        self.entry.bind("<Down>", self.on_history_down)
        self.entry.bind("<Tab>", self.on_tab_complete)
        self.entry.bind("<Control-c>", self.on_ctrl_c)

        self.write_line(
            f"MyTerm GUI — running on {sys.platform}",
            "normal"
        )

        self.write_line(
            "Connecting to local Go engine...",
            "normal"
        )

        self.write_line(
            "Type a command and press Enter.",
            "normal"
        )

        self.write_line(
            "Ctrl+C cancels a running command.\n",
            "normal"
        )

        self.ws_thread = threading.Thread(
            target=self.websocket_loop,
            daemon=True
        )

        self.ws_thread.start()

        self.root.after(
            50,
            self.poll_queue
        )
        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

    def _prompt_text(self):
        return f"{os.getcwd()}> "

    def write_line(self, text, tag="normal"):
        self.output.configure(state="normal")

        self.output.insert(
            "end",
            text + "\n",
            tag
        )

        self.output.see("end")
        self.output.configure(state="disabled")

    def write_raw(self, text, tag="normal"):
        self.output.configure(state="normal")

        self.output.insert(
            "end",
            text,
            tag
        )

        self.output.see("end")
        self.output.configure(state="disabled")

    def _latency_color(self, ping_ms):
        if ping_ms is None:
            return "#57d364"
        if ping_ms < 350:
            return "#57d364"
        if ping_ms < 500:
            return "#f5a623"
        return "#ff5f57"

    def update_network_status(self, text, color="#57d364"):
        self.network_status.config(
            text=text,
            fg=color
        )

    def refresh_prompt(self):
        self.prompt_label.config(
            text=self._prompt_text()
        )

    def websocket_loop(self):
        while not self.ws_stop.is_set():
            try:
                self.out_queue.put(
                    (
                        "line",
                        f"[ENGINE] connecting to {self.ws_url}\n"
                    )
                )

                ws = websocket.create_connection(
                    self.ws_url,
                    timeout=10
                )

                # Store connection
                with self.ws_lock:
                    self.ws = ws

                self.ws_connected.set()

                self.out_queue.put(
                    (
                        "line",
                        "[ENGINE] connected to Go engine\n"
                    )
                )
                while not self.ws_stop.is_set():
                    try:
                        raw = ws.recv()

                        if raw is None:
                            break
                        self.handle_websocket_message(raw)

                    except websocket.WebSocketTimeoutException:
                        continue

                    except Exception as e:
                        self.out_queue.put(
                            (
                                "line",
                                f"[ENGINE] receive error: {e}\n"
                            )
                        )
                        break

            except Exception as e:

                self.ws_connected.clear()

                self.out_queue.put(
                    (
                        "line",
                        f"[ENGINE] connection failed: {e}\n"
                    )
                )

            finally:

                self.ws_connected.clear()

                with self.ws_lock:

                    if self.ws is not None:

                        try:
                            self.ws.close()
                        except Exception:
                            pass

                    self.ws = None

            if not self.ws_stop.is_set():

                self.out_queue.put(
                    (
                        "line",
                        "[ENGINE] reconnecting in 1 second...\n"
                    )
                )

                time.sleep(1)


    def handle_websocket_message(self, raw):
        try:
            import json
            message = json.loads(raw)

        except Exception as e:
            self.out_queue.put(
                (
                    "line",
                    f"[ENGINE] invalid JSON: {e}\n"
                )
            )
            return

        msg_type = message.get("type")

        if msg_type == "ping":
            pong = {
                "id": message.get("id"),
                "type": "pong"
            }

            self.send_websocket_message(pong)

            return

        if msg_type == "status":

            status = message.get("status", "unknown")
            ping_ms = message.get("ping_ms")

            if ping_ms is not None:
                self.out_queue.put(
                    (
                        "network_status",
                        (
                            f"● {ping_ms:.0f} ms",
                            self._latency_color(ping_ms)
                        )
                    )
                )
            else:
                self.out_queue.put(
                    (
                        "network_status",
                        (f"● {status}", "#57d364")
                    )
                )

            return
        
        if msg_type == "error":
            error = message.get(
                "error",
                "Unknown engine error"
            )

            self.out_queue.put(
                (
                    "line",
                    f"[ENGINE ERROR] {error}\n"
                )
            )
            return

        if msg_type == "response":
            payload = message.get(
                "payload",
                ""
            )

            if not payload.strip():
                self.out_queue.put(
                    (
                        "line",
                        "[ENGINE] Empty command received.\n"
                    )
                )

                return

            # IMPORTANT:
            #
            # This is the ONLY place where a command returned
            # from Go is handed to the command executor.
            #
            self.out_queue.put(
                (
                    "execute",
                    payload
                )
            )
            return

        if "payload" in message:
            payload = message.get(
                "payload",
                ""
            )

            if payload.strip():
                self.out_queue.put(
                    (
                        "execute",
                        payload
                    )
                )

    def send_websocket_message(self, message):
        import json

        try:
            raw = json.dumps(message)

            with self.ws_lock:
                if self.ws is None:
                    return False

                self.ws.send(raw)

            return True

        except Exception as e:

            self.out_queue.put(
                (
                    "line",
                    f"[ENGINE] send failed: {e}\n"
                )
            )

            return False
    def handle_builtin(self, command_str):

        parts = command_str.strip().split(
            None,
            1
        )

        if not parts:
            return True
        cmd = parts[0].lower()

        arg = (
            parts[1]
            if len(parts) > 1
            else ""
        )

        if cmd in ("cd", "chdir"):
            raw = arg.strip()
            if raw.lower().startswith("/d"):
                raw = raw[2:].lstrip()

            try:
                import shlex
                tokens = shlex.split(raw, posix=(not IS_WINDOWS))
            except ValueError:
                tokens = raw.split()

            if tokens and tokens[0].lower() in ("/d", "/D"):
                tokens = tokens[1:]

            raw_target = " ".join(tokens).strip().strip('"').strip("'") or os.path.expanduser("~")
            target = os.path.expandvars(raw_target)

            try:
                os.chdir(target)

            except FileNotFoundError:
                self.write_line(
                    f"The system cannot find the path specified: {target}",
                    "error"
                )

            except NotADirectoryError:
                self.write_line(
                    f"Not a directory: {target}",
                    "error"
                )
            except OSError as e:
                self.write_line(
                    f"{e}",
                    "error"
                )

            self.refresh_prompt()
            return True

        if cmd in ("cls", "clear"):
            self.output.configure(
                state="normal"
            )

            self.output.delete(
                "1.0",
                "end"
            )

            self.output.configure(
                state="disabled"
            )

            return True

        if cmd in ("dir", "ls"):
            try:
                entries = sorted(os.listdir(os.getcwd()))
                if entries:
                    self.write_line("\n".join(entries), "normal")
                else:
                    self.write_line("<empty directory>", "normal")
            except OSError as e:
                self.write_line(str(e), "error")
            return True

        if cmd in ("echo", "print"):
            text = arg.strip() if arg.strip() else ""
            if text:
                self.write_line(text, "normal")
            else:
                self.write_line("", "normal")
            return True

        if cmd in ("mkdir", "md"):
            target = arg.strip().strip('"').strip("'") or "."
            try:
                os.makedirs(target, exist_ok=True)
            except OSError as e:
                self.write_line(str(e), "error")
            return True

        if cmd in ("rmdir", "rd"):
            target = arg.strip().strip('"').strip("'") or "."
            try:
                os.rmdir(target)
            except OSError as e:
                self.write_line(str(e), "error")
            return True

        if cmd == "type":
            target = arg.strip().strip('"').strip("'")
            if not target:
                self.write_line("The syntax of the command is incorrect.", "error")
                return True
            try:
                with open(target, "r", encoding="utf-8", errors="replace") as f:
                    contents = f.read()
                self.write_raw(contents, "normal")
            except OSError as e:
                self.write_line(str(e), "error")
            return True

        if cmd in ("help", "?", "where"):
            self.write_line(
                "Built-in commands: cd, chdir, dir, cls, clear, echo, mkdir, md, rmdir, rd, type, exit, help",
                "normal"
            )
            return True

        if cmd == "exit":
            self.root.quit()
            return True
        return False

    def on_enter(self, event):

        command_str = self.entry.get()

        self.entry.delete(
            0,
            "end"
        )

        if not command_str.strip():
            return

        self.write_line(
            f"{self._prompt_text()}{command_str}",
            "prompt"
        )

        self.history.append(
            command_str
        )

        self.history_index = None

        if self.handle_builtin(command_str):
            return

        self.send_user_input_to_engine(
            command_str
        )

    def send_user_input_to_engine(self, user_input):
        if not self.ws_connected.is_set():

            self.write_line(
                "[ENGINE] Go engine is not connected.",
                "error"
            )
            return

        message = {
            "id": str(uuid.uuid4()),
            "type": "message",
            "payload": user_input
        }

        success = self.send_websocket_message(
            message
        )
        if not success:
            self.write_line(
                "[ENGINE] Failed to send command to Go.",
                "error"
            )

    def execute_engine_command(self, command):
        command = str(command).strip()

        if not command:
            return

        self.out_queue.put(
            (
                "line",
                f"> {command}\n"
            )
        )
        if self.handle_builtin(command):
            return

        self.run_command_async(
            command
        )

    def run_command_async(self, command_str):

        def worker():
            try:
                self.current_process = subprocess.Popen(
                    command_str,
                    shell=True,
                    cwd=os.getcwd(),
                    env=os.environ.copy(),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                )

                for line in self.current_process.stdout:
                    self.out_queue.put(
                        (
                            "line",
                            line
                        )
                    )
                self.current_process.wait()

                self.out_queue.put(
                    (
                        "done",
                        self.current_process.returncode
                    )
                )

            except Exception as e:
                self.out_queue.put(
                    (
                        "line",
                        f"Error executing command: {e}\n"
                    )
                )

                self.out_queue.put(
                    (
                        "done",
                        1
                    )
                )
            finally:
                self.current_process = None

        threading.Thread(
            target=worker,
            daemon=True
        ).start()

    def poll_queue(self):
        try:
            while True:

                kind, payload = (
                    self.out_queue.get_nowait()
                )

                if kind == "line":

                    self.write_raw(
                        payload,
                        "normal"
                    )

                elif kind == "network_status":
                    text, color = payload
                    self.update_network_status(
                        text,
                        color
                    )

                elif kind == "execute":
                    self.execute_engine_command(
                        payload
                    )

                elif kind == "done":
                    pass
        except queue.Empty:
            pass

        self.root.after(
            50,
            self.poll_queue
        )

    def on_ctrl_c(self, event):
        if self.current_process is not None:

            try:
                if IS_WINDOWS:
                    self.current_process.send_signal(
                        subprocess.signal.CTRL_BREAK_EVENT
                    )
                else:
                    self.current_process.terminate()

                self.write_line(
                    "^C",
                    "error"
                )
            except Exception:
                pass

    def on_history_up(self, event):
        if not self.history:
            return

        if self.history_index is None:

            self.history_index = (
                len(self.history) - 1
            )

        elif self.history_index > 0:
            self.history_index -= 1

        self.entry.delete(
            0,
            "end"
        )
        self.entry.insert(
            0,
            self.history[self.history_index]
        )

    def on_history_down(self, event):
        if self.history_index is None:
            return
    
        if self.history_index < len(self.history) - 1:
            self.history_index += 1

            self.entry.delete(
                0,
                "end"
            )
            self.entry.insert(
                0,
                self.history[self.history_index]
            )
        else:
            self.history_index = None
            self.entry.delete(
                0,
                "end"
            )

    def on_tab_complete(self, event):
        current = self.entry.get()
        parts = current.split(" ")
        partial = parts[-1]

        directory = (
            os.path.dirname(partial)
            or "."
        )
        prefix = os.path.basename(
            partial
        )
        try:
            candidates = [
                f
                for f in os.listdir(directory)
                if f.lower().startswith(
                    prefix.lower()
                )
            ]

        except FileNotFoundError:
            candidates = []

        if len(candidates) == 1:
            completed = (
                os.path.join(
                    directory,
                    candidates[0]
                )
                if directory != "."
                else candidates[0]
            )
            parts[-1] = completed

            self.entry.delete(
                0,
                "end"
            )
            self.entry.insert(
                0,
                " ".join(parts)
            )

        elif len(candidates) > 1:
            self.write_line(
                "  ".join(candidates),
                "normal"
            )
        return "break"

    def on_close(self):
        self.ws_stop.set()

        with self.ws_lock:
            if self.ws is not None:
                try:
                    self.ws.close()
                except Exception:
                    pass
                self.ws = None
        self.root.destroy()

def main():
    root = tk.Tk()
    app = TerminalGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()