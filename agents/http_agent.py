from http.server import BaseHTTPRequestHandler, HTTPServer
import asyncio

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from HTTP!")

async def start_http_server(port=8080):
    loop = asyncio.get_running_loop()

    server = HTTPServer(("0.0.0.0", port), HTTPHandler)

    # Run in a separate thread to avoid blocking asyncio
    await loop.run_in_executor(None, server.serve_forever)
