from http.server import BaseHTTPRequestHandler
from lib.Pomodoro import Pomodoro
from lib.Alarm import Alarm

alarm = Alarm()
pomodoro = Pomodoro(alarm)

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
