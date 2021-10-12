from lib.Pomodoro import Pomodoro
from datetime import datetime, timedelta

def test_if_end_of_work_is_setted_on_start():
    p = Pomodoro()
    p.start_work()

    assert p.work_end_time_point is not None

def test_check_pomodoro_status_right_after_start():
    p = Pomodoro()
    p.start_work()

    assert p.status() == "Work: 24:59"

def test_check_rest_status_right_after_start():
    p = Pomodoro()
    p.start_rest()

    assert p.status() == "Rest: 04:59"

def test_reset_time_points_after_call_start_rest():
    p = Pomodoro()
    p.start_work()
    p.start_rest()

    assert p.work_start_time_point is None

def test_reset_time_points_after_call_start_work():
    p = Pomodoro()
    p.start_rest()
    p.start_work()

    assert p.rest_start_time_point is None

def test_status_return_no_active_session():
    p = Pomodoro()

    assert p.status() == "No active session!"
