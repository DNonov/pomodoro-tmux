import os
from sys import platform

class Alarm():
    """
    Makes sound notification.

    This is functional only on linux systems with 'sox' installed.
    """
    def __init__(self):
        self.counter = 0
        self.linux_alarm_comand = 'play -nq -t alsa synth 0.1 sine 170'

    def notify(self):
        """ Creates sound notification """
        if platform == "linux" or platform == "linux2":
            if self.counter < 5:
                os.system(self.linux_alarm_comand)
                self.counter += 1

