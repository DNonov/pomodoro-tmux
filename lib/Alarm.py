import os

class Alarm():
    """
    Makes sound notification.

    This is functional only on linux systems with 'sox' installed.
    """
    def __init__(self):
        self.counter = 0
        self.alarm_comand = 'play -nq -t alsa synth 0.1 sine 170'

    def beep(self):
        """ Creates sound notification """
        if self.counter < 5:
            os.system(self.alarm_comand)
            self.counter += 1

