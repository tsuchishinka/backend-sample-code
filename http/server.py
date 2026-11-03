import json
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8000


def get_api_status(self):
    body = json.dumps({"status", "success"}, ensure_ascii=False).encode("utf-8")
    return 200, {"Content-Type": "application/json; charset=utf-8"}, body


def post_authorize(self):
    token = uuid.uuid4()
    headers = {
        "Content-Type": "application/json",
        "Set-Cookie": f"token={token}; Path=/; HttpOnly: SameSite=Lax",
    }
    body = b'{"status": "ok"}'

    return 200, headers, body


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        print(self.client_address)

        for name, value in self.headers.items():
            print(f"{name}: {value}")

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        print(body.decode("utf-8", errors="replace"))

        if self.path == "/api/status":
            status, headers, response_body = get_api_status()

        self.send_response_data(status, headers, response_body)

    def do_POST(self):
        print(self.path)
        print(self.client_address)

        for name, value in self.headers.items():
            print(f"{name}: {value}")

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        print(body.decode("utf-8", errors="replace"))

        if self.path == "/authorize":
            status, headers, response_body = post_authorize()

        self.send_response_data(status, headers, response_body)

    def send_response_data(self, status: int, headers: dict, body: bytes):
        self.send_response(status)
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer((HOST, PORT), Handler)
print("起動")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("終了")
finally:
    server.server_close()
