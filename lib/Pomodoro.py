from datetime import datetime, timedelta

class Pomodoro():
    """
    Pomodoro class holds 4 time points. Which are required for constructing
    two sessions 'work' and 'rest'. There are three methods that will map
    directly to the server's urls.
    """
    def __init__(self, work_time_minutes=25, rest_time_minutes=5):
        self.work_start_time_point = None
        self.work_end_time_point = None
        self.rest_start_time_point = None
        self.rest_end_time_point = None
        self.last_active_session = None
        self.alarm_counter = 0

        self.work_time = timedelta(minutes=work_time_minutes)
        self.rest_time = timedelta(minutes=rest_time_minutes)

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
        self.alarm_counter = 0

    def start_rest(self):
        """ Start rest session. """

        self.rest_start_time_point = datetime.now()
        self.rest_end_time_point = \
            self.rest_start_time_point + self.rest_time

        self.reset_work_time_points()
        self.last_active_session = "rest"
        self.alarm_counter = 0

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
            return "No active session!"

        if self.last_active_session == "work":
            if self.alarm_counter < 5:
                print("\a")
                self.alarm_counter += 1
            return "Work session finished!"

        if self.last_active_session == "rest":
            if self.alarm_counter < 5:
                print("\a")
                self.alarm_counter += 1
            return "Rest session finished!"