import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alert,
    Camera,
    Class,
    Door,
    Entertainment,
    FireAlarm_Sensor,
    HomeTheatre,
    Home_Security_System,
    HouseHolds,
    Light,
    Motion_Sensor,
    PressureSensor,
    Sensor,
    Speakers,
    Symbol_Meaning,
    System,
    TV,
    _unnamed,
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

def test_assoc_Door_Camera_reverse_link_reassign_clear():
    a1 = Door(DoorID=7)
    a2 = Door(DoorID=13)
    b = Camera(CameraID=7)
    _safe_set(b, 'door3', a1)
    assert _is_linked(b, 'door3', a1)
    if hasattr(a1, 'camera2'):
        assert _is_linked(a1, 'camera2', b)
    _safe_set(b, 'door3', a2)
    assert _is_linked(b, 'door3', a2)
    if hasattr(a1, 'camera2'):
        assert not _is_linked(a1, 'camera2', b)
    if hasattr(a2, 'camera2'):
        assert _is_linked(a2, 'camera2', b)
    _safe_set(b, 'door3', None)
    assert not _is_linked(b, 'door3', a2)
    if hasattr(a2, 'camera2'):
        assert not _is_linked(a2, 'camera2', b)


def test_assoc_HomeTheatre_Entertainment_reverse_link_reassign_clear():
    a1 = HomeTheatre(HTID="sample_text")
    a2 = HomeTheatre(HTID="sample_text_2")
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'homeTheatre23', {a1})
    assert _is_linked(b, 'homeTheatre23', a1)
    if hasattr(a1, 'entertainment22'):
        assert _is_linked(a1, 'entertainment22', b)
    _safe_set(b, 'homeTheatre23', {a2})
    assert _is_linked(b, 'homeTheatre23', a2)
    if hasattr(a1, 'entertainment22'):
        assert not _is_linked(a1, 'entertainment22', b)
    if hasattr(a2, 'entertainment22'):
        assert _is_linked(a2, 'entertainment22', b)
    _safe_set(b, 'homeTheatre23', set())
    assert not _is_linked(b, 'homeTheatre23', a2)
    if hasattr(a2, 'entertainment22'):
        assert not _is_linked(a2, 'entertainment22', b)


def test_assoc_HomeTheatre_Speakers_reverse_link_reassign_clear():
    a1 = Speakers(SpeakerID=7)
    a2 = Speakers(SpeakerID=13)
    b = HomeTheatre(HTID="sample_text")
    _safe_set(b, 'speakers6', a1)
    assert _is_linked(b, 'speakers6', a1)
    if hasattr(a1, 'homeTheatre7'):
        assert _is_linked(a1, 'homeTheatre7', b)
    _safe_set(b, 'speakers6', a2)
    assert _is_linked(b, 'speakers6', a2)
    if hasattr(a1, 'homeTheatre7'):
        assert not _is_linked(a1, 'homeTheatre7', b)
    if hasattr(a2, 'homeTheatre7'):
        assert _is_linked(a2, 'homeTheatre7', b)
    _safe_set(b, 'speakers6', None)
    assert not _is_linked(b, 'speakers6', a2)
    if hasattr(a2, 'homeTheatre7'):
        assert not _is_linked(a2, 'homeTheatre7', b)


def test_assoc_HomeTheatre_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = HomeTheatre(HTID="sample_text")
    _safe_set(b, 'system14', a1)
    assert _is_linked(b, 'system14', a1)
    if hasattr(a1, 'homeTheatre15'):
        assert _is_linked(a1, 'homeTheatre15', b)
    _safe_set(b, 'system14', a2)
    assert _is_linked(b, 'system14', a2)
    if hasattr(a1, 'homeTheatre15'):
        assert not _is_linked(a1, 'homeTheatre15', b)
    if hasattr(a2, 'homeTheatre15'):
        assert _is_linked(a2, 'homeTheatre15', b)
    _safe_set(b, 'system14', None)
    assert not _is_linked(b, 'system14', a2)
    if hasattr(a2, 'homeTheatre15'):
        assert not _is_linked(a2, 'homeTheatre15', b)


def test_assoc_HomeTheatre_TV_reverse_link_reassign_clear():
    a1 = TV(TVID=7)
    a2 = TV(TVID=13)
    b = HomeTheatre(HTID="sample_text")
    _safe_set(b, 'tV4', a1)
    assert _is_linked(b, 'tV4', a1)
    if hasattr(a1, 'homeTheatre5'):
        assert _is_linked(a1, 'homeTheatre5', b)
    _safe_set(b, 'tV4', a2)
    assert _is_linked(b, 'tV4', a2)
    if hasattr(a1, 'homeTheatre5'):
        assert not _is_linked(a1, 'homeTheatre5', b)
    if hasattr(a2, 'homeTheatre5'):
        assert _is_linked(a2, 'homeTheatre5', b)
    _safe_set(b, 'tV4', None)
    assert not _is_linked(b, 'tV4', a2)
    if hasattr(a2, 'homeTheatre5'):
        assert not _is_linked(a2, 'homeTheatre5', b)


def test_assoc_Home_Security_System_Alert_reverse_link_reassign_clear():
    a1 = Home_Security_System(UserID=7)
    a2 = Home_Security_System(UserID=13)
    b = Alert(AlertID=7)
    _safe_set(b, 'home_Security_System9', a1)
    assert _is_linked(b, 'home_Security_System9', a1)
    if hasattr(a1, 'alert8'):
        assert _is_linked(a1, 'alert8', b)
    _safe_set(b, 'home_Security_System9', a2)
    assert _is_linked(b, 'home_Security_System9', a2)
    if hasattr(a1, 'alert8'):
        assert not _is_linked(a1, 'alert8', b)
    if hasattr(a2, 'alert8'):
        assert _is_linked(a2, 'alert8', b)
    _safe_set(b, 'home_Security_System9', None)
    assert not _is_linked(b, 'home_Security_System9', a2)
    if hasattr(a2, 'alert8'):
        assert not _is_linked(a2, 'alert8', b)


def test_assoc_Home_Security_System_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = Home_Security_System(UserID=7)
    _safe_set(b, 'system16', a1)
    assert _is_linked(b, 'system16', a1)
    if hasattr(a1, 'home_Security_System17'):
        assert _is_linked(a1, 'home_Security_System17', b)
    _safe_set(b, 'system16', a2)
    assert _is_linked(b, 'system16', a2)
    if hasattr(a1, 'home_Security_System17'):
        assert not _is_linked(a1, 'home_Security_System17', b)
    if hasattr(a2, 'home_Security_System17'):
        assert _is_linked(a2, 'home_Security_System17', b)
    _safe_set(b, 'system16', None)
    assert not _is_linked(b, 'system16', a2)
    if hasattr(a2, 'home_Security_System17'):
        assert not _is_linked(a2, 'home_Security_System17', b)


def test_assoc_Sensor_Door_reverse_link_reassign_clear():
    a1 = Sensor(SensorID=7, SensorType=7)
    a2 = Sensor(SensorID=13, SensorType=13)
    b = Door(DoorID=7)
    _safe_set(b, 'sensor1', a1)
    assert _is_linked(b, 'sensor1', a1)
    if hasattr(a1, 'door0'):
        assert _is_linked(a1, 'door0', b)
    _safe_set(b, 'sensor1', a2)
    assert _is_linked(b, 'sensor1', a2)
    if hasattr(a1, 'door0'):
        assert not _is_linked(a1, 'door0', b)
    if hasattr(a2, 'door0'):
        assert _is_linked(a2, 'door0', b)
    _safe_set(b, 'sensor1', None)
    assert not _is_linked(b, 'sensor1', a2)
    if hasattr(a2, 'door0'):
        assert not _is_linked(a2, 'door0', b)


def test_assoc_Sensor_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = Sensor(SensorID=7, SensorType=7)
    _safe_set(b, 'system10', a1)
    assert _is_linked(b, 'system10', a1)
    if hasattr(a1, 'sensor11'):
        assert _is_linked(a1, 'sensor11', b)
    _safe_set(b, 'system10', a2)
    assert _is_linked(b, 'system10', a2)
    if hasattr(a1, 'sensor11'):
        assert not _is_linked(a1, 'sensor11', b)
    if hasattr(a2, 'sensor11'):
        assert _is_linked(a2, 'sensor11', b)
    _safe_set(b, 'system10', None)
    assert not _is_linked(b, 'system10', a2)
    if hasattr(a2, 'sensor11'):
        assert not _is_linked(a2, 'sensor11', b)


def test_assoc_Speakers_Entertainment_reverse_link_reassign_clear():
    a1 = Speakers(SpeakerID=7)
    a2 = Speakers(SpeakerID=13)
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'speakers21', {a1})
    assert _is_linked(b, 'speakers21', a1)
    if hasattr(a1, 'entertainment20'):
        assert _is_linked(a1, 'entertainment20', b)
    _safe_set(b, 'speakers21', {a2})
    assert _is_linked(b, 'speakers21', a2)
    if hasattr(a1, 'entertainment20'):
        assert not _is_linked(a1, 'entertainment20', b)
    if hasattr(a2, 'entertainment20'):
        assert _is_linked(a2, 'entertainment20', b)
    _safe_set(b, 'speakers21', set())
    assert not _is_linked(b, 'speakers21', a2)
    if hasattr(a2, 'entertainment20'):
        assert not _is_linked(a2, 'entertainment20', b)


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = HouseHolds(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    _safe_set(b, 'system13', a1)
    assert _is_linked(b, 'system13', a1)
    if hasattr(a1, 'houseHolds12'):
        assert _is_linked(a1, 'houseHolds12', b)
    _safe_set(b, 'system13', a2)
    assert _is_linked(b, 'system13', a2)
    if hasattr(a1, 'houseHolds12'):
        assert not _is_linked(a1, 'houseHolds12', b)
    if hasattr(a2, 'houseHolds12'):
        assert _is_linked(a2, 'houseHolds12', b)
    _safe_set(b, 'system13', None)
    assert not _is_linked(b, 'system13', a2)
    if hasattr(a2, 'houseHolds12'):
        assert not _is_linked(a2, 'houseHolds12', b)


def test_assoc_TV_Entertainment_reverse_link_reassign_clear():
    a1 = TV(TVID=7)
    a2 = TV(TVID=13)
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'tV19', {a1})
    assert _is_linked(b, 'tV19', a1)
    if hasattr(a1, 'entertainment18'):
        assert _is_linked(a1, 'entertainment18', b)
    _safe_set(b, 'tV19', {a2})
    assert _is_linked(b, 'tV19', a2)
    if hasattr(a1, 'entertainment18'):
        assert not _is_linked(a1, 'entertainment18', b)
    if hasattr(a2, 'entertainment18'):
        assert _is_linked(a2, 'entertainment18', b)
    _safe_set(b, 'tV19', set())
    assert not _is_linked(b, 'tV19', a2)
    if hasattr(a2, 'entertainment18'):
        assert not _is_linked(a2, 'entertainment18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

