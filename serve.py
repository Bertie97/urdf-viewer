from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8765"))

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.split("?")[0].endswith(("/", ".html")):
            self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

if __name__ == '__main__':
    print(f'URDF Viewer: http://127.0.0.1:{PORT}/')
    ThreadingHTTPServer(('127.0.0.1', PORT), Handler).serve_forever()
