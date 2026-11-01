#!/usr/bin/env python3
"""Preview the already-built personal site using Python's standard library."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
DESTINATION = ROOT / "_site"
match = re.search(r"^baseurl:\s*([^\s#]*)", (ROOT / "_config.yml").read_text(), re.M)
BASEURL = match.group(1).strip("\"'").rstrip("/") if match else ""


class PreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path == "/" and BASEURL:
            self.send_response(302)
            self.send_header("Location", BASEURL + "/")
            self.end_headers()
            return
        super().do_GET()

    def translate_path(self, path):
        if path.startswith(BASEURL + "/"):
            path = path[len(BASEURL):]
        return super().translate_path(path)


if __name__ == "__main__":
    if not (DESTINATION / "index.html").is_file():
        raise SystemExit("Build the site first: bundle exec jekyll build --baseurl /al-folio")
    server = ThreadingHTTPServer(
        ("127.0.0.1", 4000), partial(PreviewHandler, directory=str(DESTINATION))
    )
    print(f"Preview: http://127.0.0.1:4000{BASEURL}/\nPress Ctrl+C to stop.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
