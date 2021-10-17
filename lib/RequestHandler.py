from http.server import BaseHTTPRequestHandler, HTTPServer
from lib.Pomodoro import Pomodoro

pomodoro = Pomodoro()

class RequestHandler(BaseHTTPRequestHandler):
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
            self.response("Work started")

        if self.path == "/start-rest":
            pomodoro.start_rest()
            self.response("Rest started")
