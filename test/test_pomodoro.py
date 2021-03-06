import time

from lib.Pomodoro import Pomodoro
from lib.Alarm import Alarm

def test_if_end_of_work_is_setted_on_start():
    a = Alarm()
    p = Pomodoro(a)
    p.start_work()

    assert p.work_end_time_point is not None

def test_if_pomodoro_status_is_correct_after_start():
    a = Alarm()
    p = Pomodoro(a)
    p.start_work()

    assert p.status() == "Work: 24:59"

def test_if_rest_status_is_correct_after_start():
    a = Alarm()
    p = Pomodoro(a)
    p.start_rest()

    assert p.status() == "Rest: 04:59"

def test_if_reset_time_points_are_reset_after_start_rest_call():
    a = Alarm()
    p = Pomodoro(a)
    p.start_work()
    p.start_rest()

    assert p.work_start_time_point is None

def test_if_reset_time_points_are_reset_after_start_work_call():
    a = Alarm()
    p = Pomodoro(a)
    p.start_rest()
    p.start_work()

    assert p.rest_start_time_point is None

def test_if_status_return_no_active_session():
    a = Alarm()
    p = Pomodoro(a)

    assert p.status() == ""

def test_if_after_end_of_work_session_display_correct_message():
    a = Alarm()
    p = Pomodoro(a, work_time_seconds=1)
    p.start_work()

    time.sleep(1)

    assert p.status() == "Work session finished!"

def test_if_after_end_of_rest_session_display_correct_message():
    a = Alarm()
    p = Pomodoro(a, rest_time_seconds=1)
    p.start_rest()

    time.sleep(1)

    assert p.status() == "Rest session finished!"

def test_whole_pomodoro_with_work_and_rest_sessions():
    a = Alarm()
    p = Pomodoro(a, work_time_seconds=1, rest_time_seconds=1)

    p.start_work()
    time.sleep(1)
    assert p.status() == "Work session finished!"

    p.start_rest()
    time.sleep(1)
    assert p.status() == "Rest session finished!"

    p.start_work()
    time.sleep(1)
    assert p.status() == "Work session finished!"

def test_cannot_run_work_session_twice_without_run_rest_session():
    a = Alarm()
    p = Pomodoro(a, work_time_seconds=1, rest_time_seconds=1)

    p.start_work()
    time.sleep(2)
    p.start_work()
    time.sleep(1)
    assert p.status() == "Work session finished!"

def test_cannot_run_rest_session_twice_without_run_rest_session():
    a = Alarm()
    p = Pomodoro(a, work_time_seconds=1, rest_time_seconds=1)

    p.start_rest()
    time.sleep(2)
    p.start_rest()
    time.sleep(1)
    assert p.status() == "Rest session finished!"
