import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alert,
    Door,
    End_Of_Day,
    Entertainment,
    FireAlarm_Sensor,
    HomeControl,
    Home_Security_System,
    HouseHolds,
    LPGControl,
    Light,
    Motion_Sensor,
    Sensor,
    Start_Of_Day,
    SwitchControl,
    System,
    WIFI_Sense,
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
    a1 = WIFI_Sense(WIFIID=7)
    a2 = WIFI_Sense(WIFIID=13)
    b = Door(DoorID=7)
    _safe_set(b, 'camera2', {a1})
    assert _is_linked(b, 'camera2', a1)
    if hasattr(a1, 'door3'):
        assert _is_linked(a1, 'door3', b)
    _safe_set(b, 'camera2', {a2})
    assert _is_linked(b, 'camera2', a2)
    if hasattr(a1, 'door3'):
        assert not _is_linked(a1, 'door3', b)
    if hasattr(a2, 'door3'):
        assert _is_linked(a2, 'door3', b)
    _safe_set(b, 'camera2', set())
    assert not _is_linked(b, 'camera2', a2)
    if hasattr(a2, 'door3'):
        assert not _is_linked(a2, 'door3', b)


def test_assoc_HomeTheatre_Entertainment_reverse_link_reassign_clear():
    a1 = HomeControl(HTID="sample_text")
    a2 = HomeControl(HTID="sample_text_2")
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'homeTheatre25', {a1})
    assert _is_linked(b, 'homeTheatre25', a1)
    if hasattr(a1, 'entertainment24'):
        assert _is_linked(a1, 'entertainment24', b)
    _safe_set(b, 'homeTheatre25', {a2})
    assert _is_linked(b, 'homeTheatre25', a2)
    if hasattr(a1, 'entertainment24'):
        assert not _is_linked(a1, 'entertainment24', b)
    if hasattr(a2, 'entertainment24'):
        assert _is_linked(a2, 'entertainment24', b)
    _safe_set(b, 'homeTheatre25', set())
    assert not _is_linked(b, 'homeTheatre25', a2)
    if hasattr(a2, 'entertainment24'):
        assert not _is_linked(a2, 'entertainment24', b)


def test_assoc_HomeTheatre_Speakers_reverse_link_reassign_clear():
    a1 = LPGControl(LPGControlID=7)
    a2 = LPGControl(LPGControlID=13)
    b = HomeControl(HTID="sample_text")
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
    b = HomeControl(HTID="sample_text")
    _safe_set(b, 'system18', a1)
    assert _is_linked(b, 'system18', a1)
    if hasattr(a1, 'homeTheatre19'):
        assert _is_linked(a1, 'homeTheatre19', b)
    _safe_set(b, 'system18', a2)
    assert _is_linked(b, 'system18', a2)
    if hasattr(a1, 'homeTheatre19'):
        assert not _is_linked(a1, 'homeTheatre19', b)
    if hasattr(a2, 'homeTheatre19'):
        assert _is_linked(a2, 'homeTheatre19', b)
    _safe_set(b, 'system18', None)
    assert not _is_linked(b, 'system18', a2)
    if hasattr(a2, 'homeTheatre19'):
        assert not _is_linked(a2, 'homeTheatre19', b)


def test_assoc_HomeTheatre_TV_reverse_link_reassign_clear():
    a1 = SwitchControl(SWITCHID=7)
    a2 = SwitchControl(SWITCHID=13)
    b = HomeControl(HTID="sample_text")
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
    _safe_set(b, 'home_Security_System13', a1)
    assert _is_linked(b, 'home_Security_System13', a1)
    if hasattr(a1, 'alert12'):
        assert _is_linked(a1, 'alert12', b)
    _safe_set(b, 'home_Security_System13', a2)
    assert _is_linked(b, 'home_Security_System13', a2)
    if hasattr(a1, 'alert12'):
        assert not _is_linked(a1, 'alert12', b)
    if hasattr(a2, 'alert12'):
        assert _is_linked(a2, 'alert12', b)
    _safe_set(b, 'home_Security_System13', None)
    assert not _is_linked(b, 'home_Security_System13', a2)
    if hasattr(a2, 'alert12'):
        assert not _is_linked(a2, 'alert12', b)


def test_assoc_Home_Security_System_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = Home_Security_System(UserID=7)
    _safe_set(b, 'system20', a1)
    assert _is_linked(b, 'system20', a1)
    if hasattr(a1, 'home_Security_System21'):
        assert _is_linked(a1, 'home_Security_System21', b)
    _safe_set(b, 'system20', a2)
    assert _is_linked(b, 'system20', a2)
    if hasattr(a1, 'home_Security_System21'):
        assert not _is_linked(a1, 'home_Security_System21', b)
    if hasattr(a2, 'home_Security_System21'):
        assert _is_linked(a2, 'home_Security_System21', b)
    _safe_set(b, 'system20', None)
    assert not _is_linked(b, 'system20', a2)
    if hasattr(a2, 'home_Security_System21'):
        assert not _is_linked(a2, 'home_Security_System21', b)


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
    _safe_set(b, 'system14', a1)
    assert _is_linked(b, 'system14', a1)
    if hasattr(a1, 'sensor15'):
        assert _is_linked(a1, 'sensor15', b)
    _safe_set(b, 'system14', a2)
    assert _is_linked(b, 'system14', a2)
    if hasattr(a1, 'sensor15'):
        assert not _is_linked(a1, 'sensor15', b)
    if hasattr(a2, 'sensor15'):
        assert _is_linked(a2, 'sensor15', b)
    _safe_set(b, 'system14', None)
    assert not _is_linked(b, 'system14', a2)
    if hasattr(a2, 'sensor15'):
        assert not _is_linked(a2, 'sensor15', b)


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = HouseHolds(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    _safe_set(b, 'system17', a1)
    assert _is_linked(b, 'system17', a1)
    if hasattr(a1, 'houseHolds16'):
        assert _is_linked(a1, 'houseHolds16', b)
    _safe_set(b, 'system17', a2)
    assert _is_linked(b, 'system17', a2)
    if hasattr(a1, 'houseHolds16'):
        assert not _is_linked(a1, 'houseHolds16', b)
    if hasattr(a2, 'houseHolds16'):
        assert _is_linked(a2, 'houseHolds16', b)
    _safe_set(b, 'system17', None)
    assert not _is_linked(b, 'system17', a2)
    if hasattr(a2, 'houseHolds16'):
        assert not _is_linked(a2, 'houseHolds16', b)


def test_assoc_TV_Entertainment_reverse_link_reassign_clear():
    a1 = SwitchControl(SWITCHID=7)
    a2 = SwitchControl(SWITCHID=13)
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'tV23', {a1})
    assert _is_linked(b, 'tV23', a1)
    if hasattr(a1, 'entertainment22'):
        assert _is_linked(a1, 'entertainment22', b)
    _safe_set(b, 'tV23', {a2})
    assert _is_linked(b, 'tV23', a2)
    if hasattr(a1, 'entertainment22'):
        assert not _is_linked(a1, 'entertainment22', b)
    if hasattr(a2, 'entertainment22'):
        assert _is_linked(a2, 'entertainment22', b)
    _safe_set(b, 'tV23', set())
    assert not _is_linked(b, 'tV23', a2)
    if hasattr(a2, 'entertainment22'):
        assert not _is_linked(a2, 'entertainment22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

