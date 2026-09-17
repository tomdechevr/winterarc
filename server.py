#!/usr/bin/env python3
"""
Serveur local pour Winter Arc.

Lance ce script (double-clic, ou `python3 server.py` dans un terminal),
puis ouvre http://localhost:8420 si le navigateur ne s'ouvre pas tout seul.

Les données sont lues et écrites DIRECTEMENT dans les fichiers .json
présents dans ce même dossier :
  - transactions.json
  - goals.json
  - journal.json

Aucune dépendance externe : uniquement la bibliothèque standard de Python 3.
Laisse la fenêtre du terminal ouverte tant que tu utilises l'application.
"""
import json
import os
import socket
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8420
HOST = "0.0.0.0"  # écoute sur toutes les interfaces réseau, pas juste localhost
ROOT = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(ROOT, "index.html")


def get_lan_ip():
    """Devine l'adresse IP locale de cet appareil sur le réseau Wi-Fi."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

DATA_FILES = {
    "transactions.json": [],
    "goals.json": [],
    "journal.json": {},
}


def ensure_data_files():
    """Crée les fichiers .json à la racine s'ils n'existent pas encore."""
    for name, default in DATA_FILES.items():
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(default, f, ensure_ascii=False, indent=2)


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path, content_type):
        try:
            with open(path, "rb") as f:
                body = f.read()
        except FileNotFoundError:
            self.send_error(404, "Fichier introuvable")
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send_file(INDEX_FILE, "text/html; charset=utf-8")
            return
        if self.path.startswith("/api/") and self.path[5:] in DATA_FILES:
            name = self.path[5:]
            path = os.path.join(ROOT, name)
            if not os.path.exists(path):
                self._send_json(200, DATA_FILES[name])
                return
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, OSError):
                data = DATA_FILES[name]
            self._send_json(200, data)
            return
        self.send_error(404, "Introuvable")

    def do_PUT(self):
        if self.path.startswith("/api/") and self.path[5:] in DATA_FILES:
            name = self.path[5:]
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b""
            try:
                data = json.loads(raw.decode("utf-8")) if raw else DATA_FILES[name]
            except json.JSONDecodeError:
                self._send_json(400, {"ok": False, "error": "JSON invalide"})
                return
            path = os.path.join(ROOT, name)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self._send_json(200, {"ok": True})
            return
        self.send_error(404, "Introuvable")

    def log_message(self, format, *args):
        pass  # console silencieuse


def open_browser():
    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass


def main():
    ensure_data_files()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    lan_ip = get_lan_ip()
    print(f"Winter Arc est lancé sur le réseau.")
    print(f"  - Sur cet appareil    : http://localhost:{PORT}")
    print(f"  - Depuis un autre appareil du même réseau Wi-Fi : http://{lan_ip}:{PORT}")
    print("Laisse cette fenêtre ouverte tant que tu utilises l'application.")
    print("Ctrl+C pour arrêter le serveur.")
    threading.Timer(0.6, open_browser).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur.")
        server.shutdown()


if __name__ == "__main__":
    main()
