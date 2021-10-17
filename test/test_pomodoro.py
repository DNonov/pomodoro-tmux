import time

from lib.Pomodoro import Pomodoro

def test_if_end_of_work_is_setted_on_start():
    p = Pomodoro()
    p.start_work()

    assert p.work_end_time_point is not None

def test_if_pomodoro_status_is_correct_after_start():
    p = Pomodoro()
    p.start_work()

    assert p.status() == "Work: 24:59"

def test_if_rest_status_is_correct_after_start():
    p = Pomodoro()
    p.start_rest()

    assert p.status() == "Rest: 04:59"

def test_if_reset_time_points_are_reset_after_start_rest_call():
    p = Pomodoro()
    p.start_work()
    p.start_rest()

    assert p.work_start_time_point is None

def test_if_reset_time_points_are_reset_after_start_work_call():
    p = Pomodoro()
    p.start_rest()
    p.start_work()

    assert p.rest_start_time_point is None

def test_if_status_return_no_active_session():
    p = Pomodoro()

    assert p.status() == ""

def test_if_after_end_of_work_session_display_correct_message():
    p = Pomodoro(work_time_seconds=1)
    p.start_work()

    time.sleep(1)

    assert p.status() == "Work session finished!"

def test_if_after_end_of_rest_session_display_correct_message():
    p = Pomodoro(rest_time_seconds=1)
    p.start_rest()

    time.sleep(1)

    assert p.status() == "Rest session finished!"

def test_whole_pomodoro_with_work_and_rest_sessions():
    p = Pomodoro(work_time_seconds=1, rest_time_seconds=1)

    p.start_work()
    time.sleep(1)
    assert p.status() == "Work session finished!"

    p.start_rest()
    time.sleep(1)
    assert p.status() == "Rest session finished!"

    p.start_work()
    time.sleep(1)
    assert p.status() == "Work session finished!"
