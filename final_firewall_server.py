# www.theforage.com - Telstra Cyber Task 3
# Firewall Server Handler

from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define a custom request handler
class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/tomcatwar.jsp':
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Access to /tomcatwar.jsp is Forbidden')
        else:
            # For all other paths, serve the requested files
            super().do_GET()

# Create an HTTP server with the custom request handler
server = HTTPServer(('localhost', 8080), CustomRequestHandler)

# Start the server
server.serve_forever()


