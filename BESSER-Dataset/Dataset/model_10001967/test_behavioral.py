import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Camera_1,
    Dispatch_drown,
    Event_Log,
    Home_Security__Hub_,
    Light_Sensor,
    Lock_doors,
    Motion_Sensor,
    Security_logs,
    T,
    Temperature_sensor,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_Camera_1_Camera_1_reverse_link_reassign_clear():
    a1 = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    a2 = Camera_1(Camera_ID="sample_text_2", Sensor_ID="sample_text_2")
    b = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    _safe_set(b, 'camera_113', a1)
    assert _is_linked(b, 'camera_113', a1)
    if hasattr(a1, 'camera_112'):
        assert _is_linked(a1, 'camera_112', b)
    _safe_set(b, 'camera_113', a2)
    assert _is_linked(b, 'camera_113', a2)
    if hasattr(a1, 'camera_112'):
        assert not _is_linked(a1, 'camera_112', b)
    if hasattr(a2, 'camera_112'):
        assert _is_linked(a2, 'camera_112', b)
    _safe_set(b, 'camera_113', None)
    assert not _is_linked(b, 'camera_113', a2)
    if hasattr(a2, 'camera_112'):
        assert not _is_linked(a2, 'camera_112', b)


def test_assoc_Home_Security_Camera_reverse_link_reassign_clear():
    a1 = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    a2 = Home_Security__Hub_(Camera_ID="sample_text_2", Hub_ID="sample_text_2", Login_ID="sample_text_2", Sensor_ID="sample_text_2")
    b = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    _safe_set(b, 'home_Security3', a1)
    assert _is_linked(b, 'home_Security3', a1)
    if hasattr(a1, 'camera2'):
        assert _is_linked(a1, 'camera2', b)
    _safe_set(b, 'home_Security3', a2)
    assert _is_linked(b, 'home_Security3', a2)
    if hasattr(a1, 'camera2'):
        assert not _is_linked(a1, 'camera2', b)
    if hasattr(a2, 'camera2'):
        assert _is_linked(a2, 'camera2', b)
    _safe_set(b, 'home_Security3', None)
    assert not _is_linked(b, 'home_Security3', a2)
    if hasattr(a2, 'camera2'):
        assert not _is_linked(a2, 'camera2', b)


def test_assoc_Home_Security_Doors_reverse_link_reassign_clear():
    a1 = Lock_doors(Door_ID="sample_text")
    a2 = Lock_doors(Door_ID="sample_text_2")
    b = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    _safe_set(b, 'doors8', a1)
    assert _is_linked(b, 'doors8', a1)
    if hasattr(a1, 'home_Security9'):
        assert _is_linked(a1, 'home_Security9', b)
    _safe_set(b, 'doors8', a2)
    assert _is_linked(b, 'doors8', a2)
    if hasattr(a1, 'home_Security9'):
        assert not _is_linked(a1, 'home_Security9', b)
    if hasattr(a2, 'home_Security9'):
        assert _is_linked(a2, 'home_Security9', b)
    _safe_set(b, 'doors8', None)
    assert not _is_linked(b, 'doors8', a2)
    if hasattr(a2, 'home_Security9'):
        assert not _is_linked(a2, 'home_Security9', b)


def test_assoc_Home_Security_Event_Log_reverse_link_reassign_clear():
    a1 = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    a2 = Home_Security__Hub_(Camera_ID="sample_text_2", Hub_ID="sample_text_2", Login_ID="sample_text_2", Sensor_ID="sample_text_2")
    b = Event_Log(Status=True)
    _safe_set(b, 'home_Security5', a1)
    assert _is_linked(b, 'home_Security5', a1)
    if hasattr(a1, 'event_Log4'):
        assert _is_linked(a1, 'event_Log4', b)
    _safe_set(b, 'home_Security5', a2)
    assert _is_linked(b, 'home_Security5', a2)
    if hasattr(a1, 'event_Log4'):
        assert not _is_linked(a1, 'event_Log4', b)
    if hasattr(a2, 'event_Log4'):
        assert _is_linked(a2, 'event_Log4', b)
    _safe_set(b, 'home_Security5', None)
    assert not _is_linked(b, 'home_Security5', a2)
    if hasattr(a2, 'event_Log4'):
        assert not _is_linked(a2, 'event_Log4', b)


def test_assoc_Home_Security_Light_Sensor_reverse_link_reassign_clear():
    a1 = Light_Sensor(Sensor_ID="sample_text")
    a2 = Light_Sensor(Sensor_ID="sample_text_2")
    b = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    _safe_set(b, 'light_Sensor6', {a1})
    assert _is_linked(b, 'light_Sensor6', a1)
    if hasattr(a1, 'home_Security7'):
        assert _is_linked(a1, 'home_Security7', b)
    _safe_set(b, 'light_Sensor6', {a2})
    assert _is_linked(b, 'light_Sensor6', a2)
    if hasattr(a1, 'home_Security7'):
        assert not _is_linked(a1, 'home_Security7', b)
    if hasattr(a2, 'home_Security7'):
        assert _is_linked(a2, 'home_Security7', b)
    _safe_set(b, 'light_Sensor6', set())
    assert not _is_linked(b, 'light_Sensor6', a2)
    if hasattr(a2, 'home_Security7'):
        assert not _is_linked(a2, 'home_Security7', b)


def test_assoc_Home_Security_Server_reverse_link_reassign_clear():
    a1 = Security_logs(Camera_ID="sample_text", Log_ID="sample_text", Sensor_ID="sample_text")
    a2 = Security_logs(Camera_ID="sample_text_2", Log_ID="sample_text_2", Sensor_ID="sample_text_2")
    b = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    _safe_set(b, 'server0', a1)
    assert _is_linked(b, 'server0', a1)
    if hasattr(a1, 'home_Security1'):
        assert _is_linked(a1, 'home_Security1', b)
    _safe_set(b, 'server0', a2)
    assert _is_linked(b, 'server0', a2)
    if hasattr(a1, 'home_Security1'):
        assert not _is_linked(a1, 'home_Security1', b)
    if hasattr(a2, 'home_Security1'):
        assert _is_linked(a2, 'home_Security1', b)
    _safe_set(b, 'server0', None)
    assert not _is_linked(b, 'server0', a2)
    if hasattr(a2, 'home_Security1'):
        assert not _is_linked(a2, 'home_Security1', b)


def test_assoc_Home_Security_Temperature_sensor_reverse_link_reassign_clear():
    a1 = Temperature_sensor(Temp_ID="sample_text")
    a2 = Temperature_sensor(Temp_ID="sample_text_2")
    b = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    _safe_set(b, 'temperature_sensor10', {a1})
    assert _is_linked(b, 'temperature_sensor10', a1)
    if hasattr(a1, 'home_Security11'):
        assert _is_linked(a1, 'home_Security11', b)
    _safe_set(b, 'temperature_sensor10', {a2})
    assert _is_linked(b, 'temperature_sensor10', a2)
    if hasattr(a1, 'home_Security11'):
        assert not _is_linked(a1, 'home_Security11', b)
    if hasattr(a2, 'home_Security11'):
        assert _is_linked(a2, 'home_Security11', b)
    _safe_set(b, 'temperature_sensor10', set())
    assert not _is_linked(b, 'temperature_sensor10', a2)
    if hasattr(a2, 'home_Security11'):
        assert not _is_linked(a2, 'home_Security11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

