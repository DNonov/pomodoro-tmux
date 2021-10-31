from datetime import datetime, timedelta

class Pomodoro():
    """
    Pomodoro class holds 4 time points. Which are required for constructing
    two sessions 'work' and 'rest'. There are three methods that will map
    directly to the server's urls.
    """
    def __init__(self, work_time_seconds = 1500, rest_time_seconds=300):
        self.work_start_time_point = None
        self.work_end_time_point = None

        self.rest_start_time_point = None
        self.rest_end_time_point = None

        self.last_active_session = None

        self.work_time = timedelta(seconds=work_time_seconds)
        self.rest_time = timedelta(seconds=rest_time_seconds)

    def reset_work_time_points(self):
        """ Reset work time points on the end of the rest session. """

        self.work_start_time_point = None
        self.work_end_time_point = None

    def reset_rest_time_points(self):
        """ Reset rest time points on the end of the work session. """

        self.rest_start_time_point = None
        self.rest_end_time_point = None

    def into_work_session(self, time):
        """ Check if current time is into the work session. """

        if self.work_start_time_point:
            if self.work_start_time_point < time < self.work_end_time_point:
                return True
        return False

    def into_rest_session(self, time):
        """ Check if current time is into the rest session. """

        if self.rest_start_time_point:
            if self.rest_start_time_point < time < self.rest_end_time_point:
                return True
        return False

    def start_work(self):
        """ Start work session. """

        self.work_start_time_point = datetime.now()
        self.work_end_time_point = \
            self.work_start_time_point + self.work_time

        self.reset_rest_time_points()
        self.last_active_session = "work"

    def start_rest(self):
        """ Start rest session. """

        self.rest_start_time_point = datetime.now()
        self.rest_end_time_point = \
            self.rest_start_time_point + self.rest_time

        self.reset_work_time_points()
        self.last_active_session = "rest"

    def status(self):
        """ Return the time remaining of a session. """

        time_now = datetime.now()

        if self.into_work_session(time_now):
            time = self.work_end_time_point - time_now
            return f"Work: {(time.seconds//60):02}:{(time.seconds % 60):02}"

        if self.into_rest_session(time_now):
            time =  self.rest_end_time_point - time_now
            return f"Rest: {(time.seconds//60):02}:{(time.seconds % 60):02}"

        if self.last_active_session is None:
            return ""

        if self.last_active_session == "work":
            return "Work session finished!"

        if self.last_active_session == "rest":
            return "Rest session finished!"
