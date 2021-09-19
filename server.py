from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host_name = "localhost"
server_port = 9876

class PomodoroServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f'{}', "utf-8"))

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), PomodoroServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped")
