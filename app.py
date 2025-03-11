import os
from urllib.parse import urlparse
import http.server
import socketserver


PORT = int(os.environ.get('API_PORT'))
DIRECTORY = '/var/logs'

class SecureHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Parse query parameters
        parsed_url = urlparse(self.path)

        # Secure file path resolution
        safe_path = os.path.abspath(os.path.join(DIRECTORY, parsed_url.path.lstrip("/")))
        if not safe_path.startswith(DIRECTORY) or not os.path.exists(safe_path):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File Not Found")
            return

        # Serve file
        self.path = parsed_url.path
        super().do_GET()

with socketserver.TCPServer(("127.0.0.1", PORT), SecureHTTPRequestHandler) as httpd:
    host, port = httpd.server_address
    print(f"Serving {DIRECTORY} files at http://{host}:{port}")
    httpd.serve_forever()
