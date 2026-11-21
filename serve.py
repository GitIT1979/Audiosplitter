"""Локальный сервер для AudioSplitter.

Зачем: с http://localhost браузер даёт доступ к папке библиотеки (File System Access),
а на file:// этот доступ часто блокируется. Запуск: python serve.py
"""
import os
import socket
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
URL = f"http://localhost:{PORT}/AudioSplitter.html"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


class Server(ThreadingHTTPServer):
    # побочные потоки не мешают выходу по Ctrl+C
    daemon_threads = True


def open_browser():
    webbrowser.open(URL)


def portBusy():
    # на Windows SO_REUSEADDR даёт привязаться и к занятому порту, поэтому проверяем соединением
    probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    probe.settimeout(0.3)
    try:
        return probe.connect_ex(("127.0.0.1", PORT)) == 0
    finally:
        probe.close()


if __name__ == "__main__":
    if portBusy():
        print(f"Порт {PORT} уже занят.")
        print(f"Похоже, сервер уже запущен — просто откройте {URL}")
        raise SystemExit(1)
    try:
        httpd = Server(("127.0.0.1", PORT), Handler)
    except OSError as error:
        print(f"Порт {PORT} не удалось занять: {error}")
        raise SystemExit(1)
    with httpd:
        print(f"AudioSplitter: {URL}")
        print("Остановить — Ctrl+C")
        threading.Timer(0.8, open_browser).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nОстановлено")
