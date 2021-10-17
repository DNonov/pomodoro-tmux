import sys, time
from http.server import HTTPServer

from lib.Daemon import Daemon
from lib.RequestHandler import RequestHandler

HOST_NAME = "localhost"
SERVER_PORT = 9876


class PomodoroDaemon(Daemon):
    def run(self):
        web_server = HTTPServer((HOST_NAME, SERVER_PORT), RequestHandler)
        web_server.serve_forever()


if __name__ == "__main__":
    daemon = PomodoroDaemon("/tmp/deamon-pomodoro.pid")

    if len(sys.argv) == 2:
        if "start" == sys.argv[1]:
            daemon.start()

        elif "stop" == sys.argv[1]:
            daemon.stop()

        elif "restart" == sys.argv[1]:
            daemon.restart()

        else:
            print("Unknown commant")
            sys.exit(2)
        sys.exit(0)

    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
