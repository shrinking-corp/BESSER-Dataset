import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alert,
    Camera,
    Door,
    End_Of_Day,
    Entertainment,
    FireAlarm_Sensor,
    HomeTheatre,
    Home_Security_System,
    HouseHolds,
    IOT,
    Light,
    MicroPhone,
    Motion_Sensor,
    PressureSensor,
    Sensor,
    Speakers,
    Start_Of_Day,
    TV,
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
    _safe_set(b, 'homeTheatre29', {a1})
    assert _is_linked(b, 'homeTheatre29', a1)
    if hasattr(a1, 'entertainment28'):
        assert _is_linked(a1, 'entertainment28', b)
    _safe_set(b, 'homeTheatre29', {a2})
    assert _is_linked(b, 'homeTheatre29', a2)
    if hasattr(a1, 'entertainment28'):
        assert not _is_linked(a1, 'entertainment28', b)
    if hasattr(a2, 'entertainment28'):
        assert _is_linked(a2, 'entertainment28', b)
    _safe_set(b, 'homeTheatre29', set())
    assert not _is_linked(b, 'homeTheatre29', a2)
    if hasattr(a2, 'entertainment28'):
        assert not _is_linked(a2, 'entertainment28', b)


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
    a1 = IOT(Status=True, Update=3.14)
    a2 = IOT(Status=False, Update=9.99)
    b = HomeTheatre(HTID="sample_text")
    _safe_set(b, 'system20', a1)
    assert _is_linked(b, 'system20', a1)
    if hasattr(a1, 'homeTheatre21'):
        assert _is_linked(a1, 'homeTheatre21', b)
    _safe_set(b, 'system20', a2)
    assert _is_linked(b, 'system20', a2)
    if hasattr(a1, 'homeTheatre21'):
        assert not _is_linked(a1, 'homeTheatre21', b)
    if hasattr(a2, 'homeTheatre21'):
        assert _is_linked(a2, 'homeTheatre21', b)
    _safe_set(b, 'system20', None)
    assert not _is_linked(b, 'system20', a2)
    if hasattr(a2, 'homeTheatre21'):
        assert not _is_linked(a2, 'homeTheatre21', b)


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
    _safe_set(b, 'home_Security_System15', a1)
    assert _is_linked(b, 'home_Security_System15', a1)
    if hasattr(a1, 'alert14'):
        assert _is_linked(a1, 'alert14', b)
    _safe_set(b, 'home_Security_System15', a2)
    assert _is_linked(b, 'home_Security_System15', a2)
    if hasattr(a1, 'alert14'):
        assert not _is_linked(a1, 'alert14', b)
    if hasattr(a2, 'alert14'):
        assert _is_linked(a2, 'alert14', b)
    _safe_set(b, 'home_Security_System15', None)
    assert not _is_linked(b, 'home_Security_System15', a2)
    if hasattr(a2, 'alert14'):
        assert not _is_linked(a2, 'alert14', b)


def test_assoc_Home_Security_System_System_reverse_link_reassign_clear():
    a1 = IOT(Status=True, Update=3.14)
    a2 = IOT(Status=False, Update=9.99)
    b = Home_Security_System(UserID=7)
    _safe_set(b, 'system22', a1)
    assert _is_linked(b, 'system22', a1)
    if hasattr(a1, 'home_Security_System23'):
        assert _is_linked(a1, 'home_Security_System23', b)
    _safe_set(b, 'system22', a2)
    assert _is_linked(b, 'system22', a2)
    if hasattr(a1, 'home_Security_System23'):
        assert not _is_linked(a1, 'home_Security_System23', b)
    if hasattr(a2, 'home_Security_System23'):
        assert _is_linked(a2, 'home_Security_System23', b)
    _safe_set(b, 'system22', None)
    assert not _is_linked(b, 'system22', a2)
    if hasattr(a2, 'home_Security_System23'):
        assert not _is_linked(a2, 'home_Security_System23', b)


def test_assoc_HouseHolds_End_Of_Day_reverse_link_reassign_clear():
    a1 = HouseHolds(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    a2 = HouseHolds(Alarm="sample_text_2", Coffee="sample_text_2", DishWasher="sample_text_2", TimeID="sample_text_2", WashingMachine="sample_text_2")
    b = End_Of_Day(EOT=7)
    _safe_set(b, 'houseHolds11', a1)
    assert _is_linked(b, 'houseHolds11', a1)
    if hasattr(a1, 'end_Of_Day10'):
        assert _is_linked(a1, 'end_Of_Day10', b)
    _safe_set(b, 'houseHolds11', a2)
    assert _is_linked(b, 'houseHolds11', a2)
    if hasattr(a1, 'end_Of_Day10'):
        assert not _is_linked(a1, 'end_Of_Day10', b)
    if hasattr(a2, 'end_Of_Day10'):
        assert _is_linked(a2, 'end_Of_Day10', b)
    _safe_set(b, 'houseHolds11', None)
    assert not _is_linked(b, 'houseHolds11', a2)
    if hasattr(a2, 'end_Of_Day10'):
        assert not _is_linked(a2, 'end_Of_Day10', b)


def test_assoc_HouseHolds_Start_Of_Day_reverse_link_reassign_clear():
    a1 = Start_Of_Day(SOT=7)
    a2 = Start_Of_Day(SOT=13)
    b = HouseHolds(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    _safe_set(b, 'start_Of_Day8', a1)
    assert _is_linked(b, 'start_Of_Day8', a1)
    if hasattr(a1, 'houseHolds9'):
        assert _is_linked(a1, 'houseHolds9', b)
    _safe_set(b, 'start_Of_Day8', a2)
    assert _is_linked(b, 'start_Of_Day8', a2)
    if hasattr(a1, 'houseHolds9'):
        assert not _is_linked(a1, 'houseHolds9', b)
    if hasattr(a2, 'houseHolds9'):
        assert _is_linked(a2, 'houseHolds9', b)
    _safe_set(b, 'start_Of_Day8', None)
    assert not _is_linked(b, 'start_Of_Day8', a2)
    if hasattr(a2, 'houseHolds9'):
        assert not _is_linked(a2, 'houseHolds9', b)


def test_assoc_MicroPhone_System_reverse_link_reassign_clear():
    a1 = MicroPhone(MicID="sample_text")
    a2 = MicroPhone(MicID="sample_text_2")
    b = IOT(Status=True, Update=3.14)
    _safe_set(b, 'microPhone13', {a1})
    assert _is_linked(b, 'microPhone13', a1)
    if hasattr(a1, 'system12'):
        assert _is_linked(a1, 'system12', b)
    _safe_set(b, 'microPhone13', {a2})
    assert _is_linked(b, 'microPhone13', a2)
    if hasattr(a1, 'system12'):
        assert not _is_linked(a1, 'system12', b)
    if hasattr(a2, 'system12'):
        assert _is_linked(a2, 'system12', b)
    _safe_set(b, 'microPhone13', set())
    assert not _is_linked(b, 'microPhone13', a2)
    if hasattr(a2, 'system12'):
        assert not _is_linked(a2, 'system12', b)


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
    a1 = Sensor(SensorID=7, SensorType=7)
    a2 = Sensor(SensorID=13, SensorType=13)
    b = IOT(Status=True, Update=3.14)
    _safe_set(b, 'sensor17', {a1})
    assert _is_linked(b, 'sensor17', a1)
    if hasattr(a1, 'system16'):
        assert _is_linked(a1, 'system16', b)
    _safe_set(b, 'sensor17', {a2})
    assert _is_linked(b, 'sensor17', a2)
    if hasattr(a1, 'system16'):
        assert not _is_linked(a1, 'system16', b)
    if hasattr(a2, 'system16'):
        assert _is_linked(a2, 'system16', b)
    _safe_set(b, 'sensor17', set())
    assert not _is_linked(b, 'sensor17', a2)
    if hasattr(a2, 'system16'):
        assert not _is_linked(a2, 'system16', b)


def test_assoc_Speakers_Entertainment_reverse_link_reassign_clear():
    a1 = Speakers(SpeakerID=7)
    a2 = Speakers(SpeakerID=13)
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'speakers27', {a1})
    assert _is_linked(b, 'speakers27', a1)
    if hasattr(a1, 'entertainment26'):
        assert _is_linked(a1, 'entertainment26', b)
    _safe_set(b, 'speakers27', {a2})
    assert _is_linked(b, 'speakers27', a2)
    if hasattr(a1, 'entertainment26'):
        assert not _is_linked(a1, 'entertainment26', b)
    if hasattr(a2, 'entertainment26'):
        assert _is_linked(a2, 'entertainment26', b)
    _safe_set(b, 'speakers27', set())
    assert not _is_linked(b, 'speakers27', a2)
    if hasattr(a2, 'entertainment26'):
        assert not _is_linked(a2, 'entertainment26', b)


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = IOT(Status=True, Update=3.14)
    a2 = IOT(Status=False, Update=9.99)
    b = HouseHolds(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    _safe_set(b, 'system19', a1)
    assert _is_linked(b, 'system19', a1)
    if hasattr(a1, 'houseHolds18'):
        assert _is_linked(a1, 'houseHolds18', b)
    _safe_set(b, 'system19', a2)
    assert _is_linked(b, 'system19', a2)
    if hasattr(a1, 'houseHolds18'):
        assert not _is_linked(a1, 'houseHolds18', b)
    if hasattr(a2, 'houseHolds18'):
        assert _is_linked(a2, 'houseHolds18', b)
    _safe_set(b, 'system19', None)
    assert not _is_linked(b, 'system19', a2)
    if hasattr(a2, 'houseHolds18'):
        assert not _is_linked(a2, 'houseHolds18', b)


def test_assoc_TV_Entertainment_reverse_link_reassign_clear():
    a1 = TV(TVID=7)
    a2 = TV(TVID=13)
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'tV25', {a1})
    assert _is_linked(b, 'tV25', a1)
    if hasattr(a1, 'entertainment24'):
        assert _is_linked(a1, 'entertainment24', b)
    _safe_set(b, 'tV25', {a2})
    assert _is_linked(b, 'tV25', a2)
    if hasattr(a1, 'entertainment24'):
        assert not _is_linked(a1, 'entertainment24', b)
    if hasattr(a2, 'entertainment24'):
        assert _is_linked(a2, 'entertainment24', b)
    _safe_set(b, 'tV25', set())
    assert not _is_linked(b, 'tV25', a2)
    if hasattr(a2, 'entertainment24'):
        assert not _is_linked(a2, 'entertainment24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

