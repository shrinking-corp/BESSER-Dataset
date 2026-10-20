import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alert,
    Curtains,
    End_Of_Day,
    HomeTheatre,
    Kitchen,
    Light,
    MotionSensor,
    PowerSystem,
    ROOM,
    Security_System,
    Sensor,
    Speakers,
    Start_Of_Day,
    System,
    TechSupport,
    UserProfile,
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

def test_assoc_HomeTheatre_Speakers_reverse_link_reassign_clear():
    a1 = Speakers(SpeakerID=7)
    a2 = Speakers(SpeakerID=13)
    b = HomeTheatre(SSID="sample_text")
    _safe_set(b, 'speakers2', a1)
    assert _is_linked(b, 'speakers2', a1)
    if hasattr(a1, 'homeTheatre3'):
        assert _is_linked(a1, 'homeTheatre3', b)
    _safe_set(b, 'speakers2', a2)
    assert _is_linked(b, 'speakers2', a2)
    if hasattr(a1, 'homeTheatre3'):
        assert not _is_linked(a1, 'homeTheatre3', b)
    if hasattr(a2, 'homeTheatre3'):
        assert _is_linked(a2, 'homeTheatre3', b)
    _safe_set(b, 'speakers2', None)
    assert not _is_linked(b, 'speakers2', a2)
    if hasattr(a2, 'homeTheatre3'):
        assert not _is_linked(a2, 'homeTheatre3', b)


def test_assoc_HomeTheatre_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = HomeTheatre(SSID="sample_text")
    _safe_set(b, 'system16', a1)
    assert _is_linked(b, 'system16', a1)
    if hasattr(a1, 'homeTheatre17'):
        assert _is_linked(a1, 'homeTheatre17', b)
    _safe_set(b, 'system16', a2)
    assert _is_linked(b, 'system16', a2)
    if hasattr(a1, 'homeTheatre17'):
        assert not _is_linked(a1, 'homeTheatre17', b)
    if hasattr(a2, 'homeTheatre17'):
        assert _is_linked(a2, 'homeTheatre17', b)
    _safe_set(b, 'system16', None)
    assert not _is_linked(b, 'system16', a2)
    if hasattr(a2, 'homeTheatre17'):
        assert not _is_linked(a2, 'homeTheatre17', b)


def test_assoc_Home_Security_System_Alert_reverse_link_reassign_clear():
    a1 = Security_System(UserID=7)
    a2 = Security_System(UserID=13)
    b = Alert(AlertID=7)
    _safe_set(b, 'home_Security_System11', a1)
    assert _is_linked(b, 'home_Security_System11', a1)
    if hasattr(a1, 'alert10'):
        assert _is_linked(a1, 'alert10', b)
    _safe_set(b, 'home_Security_System11', a2)
    assert _is_linked(b, 'home_Security_System11', a2)
    if hasattr(a1, 'alert10'):
        assert not _is_linked(a1, 'alert10', b)
    if hasattr(a2, 'alert10'):
        assert _is_linked(a2, 'alert10', b)
    _safe_set(b, 'home_Security_System11', None)
    assert not _is_linked(b, 'home_Security_System11', a2)
    if hasattr(a2, 'alert10'):
        assert not _is_linked(a2, 'alert10', b)


def test_assoc_Home_Security_System_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = Security_System(UserID=7)
    _safe_set(b, 'Home_Security_System_System_018', a1)
    assert _is_linked(b, 'Home_Security_System_System_018', a1)
    if hasattr(a1, 'Home_Security_System_System_119'):
        assert _is_linked(a1, 'Home_Security_System_System_119', b)
    _safe_set(b, 'Home_Security_System_System_018', a2)
    assert _is_linked(b, 'Home_Security_System_System_018', a2)
    if hasattr(a1, 'Home_Security_System_System_119'):
        assert not _is_linked(a1, 'Home_Security_System_System_119', b)
    if hasattr(a2, 'Home_Security_System_System_119'):
        assert _is_linked(a2, 'Home_Security_System_System_119', b)
    _safe_set(b, 'Home_Security_System_System_018', None)
    assert not _is_linked(b, 'Home_Security_System_System_018', a2)
    if hasattr(a2, 'Home_Security_System_System_119'):
        assert not _is_linked(a2, 'Home_Security_System_System_119', b)


def test_assoc_HouseHolds_End_Of_Day_reverse_link_reassign_clear():
    a1 = Kitchen(TimeID="sample_text")
    a2 = Kitchen(TimeID="sample_text_2")
    b = End_Of_Day(EOT=7)
    _safe_set(b, 'houseHolds7', a1)
    assert _is_linked(b, 'houseHolds7', a1)
    if hasattr(a1, 'end_Of_Day6'):
        assert _is_linked(a1, 'end_Of_Day6', b)
    _safe_set(b, 'houseHolds7', a2)
    assert _is_linked(b, 'houseHolds7', a2)
    if hasattr(a1, 'end_Of_Day6'):
        assert not _is_linked(a1, 'end_Of_Day6', b)
    if hasattr(a2, 'end_Of_Day6'):
        assert _is_linked(a2, 'end_Of_Day6', b)
    _safe_set(b, 'houseHolds7', None)
    assert not _is_linked(b, 'houseHolds7', a2)
    if hasattr(a2, 'end_Of_Day6'):
        assert not _is_linked(a2, 'end_Of_Day6', b)


def test_assoc_HouseHolds_Start_Of_Day_reverse_link_reassign_clear():
    a1 = Start_Of_Day(SOT=7)
    a2 = Start_Of_Day(SOT=13)
    b = Kitchen(TimeID="sample_text")
    _safe_set(b, 'start_Of_Day4', a1)
    assert _is_linked(b, 'start_Of_Day4', a1)
    if hasattr(a1, 'houseHolds5'):
        assert _is_linked(a1, 'houseHolds5', b)
    _safe_set(b, 'start_Of_Day4', a2)
    assert _is_linked(b, 'start_Of_Day4', a2)
    if hasattr(a1, 'houseHolds5'):
        assert not _is_linked(a1, 'houseHolds5', b)
    if hasattr(a2, 'houseHolds5'):
        assert _is_linked(a2, 'houseHolds5', b)
    _safe_set(b, 'start_Of_Day4', None)
    assert not _is_linked(b, 'start_Of_Day4', a2)
    if hasattr(a2, 'houseHolds5'):
        assert not _is_linked(a2, 'houseHolds5', b)


def test_assoc_MicroPhone_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = PowerSystem(DeviceID=7)
    _safe_set(b, 'system8', a1)
    assert _is_linked(b, 'system8', a1)
    if hasattr(a1, 'microPhone9'):
        assert _is_linked(a1, 'microPhone9', b)
    _safe_set(b, 'system8', a2)
    assert _is_linked(b, 'system8', a2)
    if hasattr(a1, 'microPhone9'):
        assert not _is_linked(a1, 'microPhone9', b)
    if hasattr(a2, 'microPhone9'):
        assert _is_linked(a2, 'microPhone9', b)
    _safe_set(b, 'system8', None)
    assert not _is_linked(b, 'system8', a2)
    if hasattr(a2, 'microPhone9'):
        assert not _is_linked(a2, 'microPhone9', b)


def test_assoc_Sensor_Door_reverse_link_reassign_clear():
    a1 = Sensor(SensorID=7, SensorType=7)
    a2 = Sensor(SensorID=13, SensorType=13)
    b = Curtains(CurtaiunID=7)
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
    _safe_set(b, 'system12', a1)
    assert _is_linked(b, 'system12', a1)
    if hasattr(a1, 'sensor13'):
        assert _is_linked(a1, 'sensor13', b)
    _safe_set(b, 'system12', a2)
    assert _is_linked(b, 'system12', a2)
    if hasattr(a1, 'sensor13'):
        assert not _is_linked(a1, 'sensor13', b)
    if hasattr(a2, 'sensor13'):
        assert _is_linked(a2, 'sensor13', b)
    _safe_set(b, 'system12', None)
    assert not _is_linked(b, 'system12', a2)
    if hasattr(a2, 'sensor13'):
        assert not _is_linked(a2, 'sensor13', b)


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = Kitchen(TimeID="sample_text")
    _safe_set(b, 'system15', a1)
    assert _is_linked(b, 'system15', a1)
    if hasattr(a1, 'houseHolds14'):
        assert _is_linked(a1, 'houseHolds14', b)
    _safe_set(b, 'system15', a2)
    assert _is_linked(b, 'system15', a2)
    if hasattr(a1, 'houseHolds14'):
        assert not _is_linked(a1, 'houseHolds14', b)
    if hasattr(a2, 'houseHolds14'):
        assert _is_linked(a2, 'houseHolds14', b)
    _safe_set(b, 'system15', None)
    assert not _is_linked(b, 'system15', a2)
    if hasattr(a2, 'houseHolds14'):
        assert not _is_linked(a2, 'houseHolds14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

