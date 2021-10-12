from http.server import BaseHTTPRequestHandler, HTTPServer
from lib.Pomodoro import Pomodoro
import time

host_name = "localhost"
server_port = 9876
pomodoro = Pomodoro()

class PomodoroServer(BaseHTTPRequestHandler):
    def response(self, payload):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f'{payload}', "utf-8"))

    def do_GET(self):
        if self.path == "/status":
            self.response(pomodoro.status())

        if self.path == "/start-work":
            pomodoro.start_work()
            self.response('Work started')

        if self.path == "/start-rest":
            pomodoro.start_rest()
            self.response("Rest started")

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), PomodoroServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped")
