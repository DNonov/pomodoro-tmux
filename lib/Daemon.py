import os, sys, time, atexit
from signal import SIGTERM

class Daemon():
    """
    Generic deamon class.

    Just subclass it and override run() method.
    """
    def __init__(self, pid_file, stdin="/dev/null", stdout="/dev/null", stderr="/dev/null"):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pid_file = pid_file

    def daemonize(self):
        """
        Do the UNIX double fork magic.
        """

        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)

        except OSError as e:
            sys.stderr.write("Fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                # exit second parent
                sys.exit(0)

        except OSError as e:
            sys.stderr.write("Fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # redirect standard file descriptores
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pid file
        atexit.register(self.delete_pid)
        pid = str(os.getpid())
        with open(self.pid_file, 'w+') as f:
            f.write("%s\n" % pid)

    def delete_pid(self):
        os.remove(self.pid_file)

    def start(self):
        """
        Start the deamon.
        """

        # Check for a pid file to see if the deamon already runs
        try:
            with open(self.pid_file, 'r') as pf:
                pid = int(pf.read().strip())

        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exists. Deamon already running?\n"
            sys.stderr.write(message % self.pid_file)
            sys.exit(1)

        # Start the deamon
        self.daemonize()
        self.run()

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            with open(self.pid_file, 'r') as pf:
                pid = int(pf.read().strip())

        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s already exists. Deamon already running?\n"
            sys.stderr.write(message % self.pid_file)
            return # not an error in a restart

        # Try to kill the deamon process
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)

        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pid_file):
                    os.remove(self.pid_file)
            else:
                print(str(err))
                sys.exit(1)

    def restart(self):
        """
        Restart the deamon
        """
        self.stop()
        self.start()

    def run(self):
        """
        You should override this method when you subclass Deamon.
        It will be called after the process has been daemonized by start() or
        restart()
        """
