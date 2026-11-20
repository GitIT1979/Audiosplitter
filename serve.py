"""Локальный сервер для AudioSplitter.

Зачем: с http://localhost браузер даёт доступ к папке библиотеки (File System Access),
а на file:// этот доступ часто блокируется. Запуск: python serve.py
"""
import http.server
import os
import socketserver
import threading
import webbrowser

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
URL = f"http://localhost:{PORT}/AudioSplitter.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


def open_browser():
    webbrowser.open(URL)


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"AudioSplitter: {URL}")
        print("Остановить — Ctrl+C")
        threading.Timer(0.8, open_browser).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nОстановлено")
