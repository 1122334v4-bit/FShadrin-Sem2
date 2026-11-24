import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from app.filemanager import FileManager

DATA_DIR = os.environ.get("DATA_DIR", "/home/appuser/data")
PORT = int(os.environ.get("PORT", "8000"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"files": FileManager(DATA_DIR).list_dir()}, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    FileManager(DATA_DIR).write_file("hello.txt", "Файловый менеджер работает")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()