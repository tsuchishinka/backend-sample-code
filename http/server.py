from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

HOST = "127.0.0.1"
PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        print(path)
        for name, value in self.headers.items():
            print(f"{name}: {value}")

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)

        print(body.decode("utf-8", errors="replace"))
        self.send_text("ffff")


server = HTTPServer((HOST, PORT), Handler)
print("起動")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("終了")
finally:
    server.server_close()
