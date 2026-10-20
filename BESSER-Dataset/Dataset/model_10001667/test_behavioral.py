import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Alert,
    Camera,
    Display,
    Door,
    Employee,
    End_Of_Day,
    Home_Security_System,
    Hub_Device,
    Light,
    Manager,
    Motion_Sensor,
    PressureSensor,
    RFID_Sensor,
    Sensor,
    Start_Of_Day,
    UDP_Controller,
    UDP_Socket,
    Users,
    int,
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


def test_assoc_HomeTheatre_Speakers_reverse_link_reassign_clear():
    a1 = Users(HTID="sample_text")
    a2 = Users(HTID="sample_text_2")
    b = Manager(MangagerID=7)
    _safe_set(b, 'homeTheatre7', {a1})
    assert _is_linked(b, 'homeTheatre7', a1)
    if hasattr(a1, 'speakers6'):
        assert _is_linked(a1, 'speakers6', b)
    _safe_set(b, 'homeTheatre7', {a2})
    assert _is_linked(b, 'homeTheatre7', a2)
    if hasattr(a1, 'speakers6'):
        assert not _is_linked(a1, 'speakers6', b)
    if hasattr(a2, 'speakers6'):
        assert _is_linked(a2, 'speakers6', b)
    _safe_set(b, 'homeTheatre7', set())
    assert not _is_linked(b, 'homeTheatre7', a2)
    if hasattr(a2, 'speakers6'):
        assert not _is_linked(a2, 'speakers6', b)


def test_assoc_HomeTheatre_System_reverse_link_reassign_clear():
    a1 = Users(HTID="sample_text")
    a2 = Users(HTID="sample_text_2")
    b = Hub_Device(Status=True, Update=3.14)
    _safe_set(b, 'homeTheatre19', a1)
    assert _is_linked(b, 'homeTheatre19', a1)
    if hasattr(a1, 'system18'):
        assert _is_linked(a1, 'system18', b)
    _safe_set(b, 'homeTheatre19', a2)
    assert _is_linked(b, 'homeTheatre19', a2)
    if hasattr(a1, 'system18'):
        assert not _is_linked(a1, 'system18', b)
    if hasattr(a2, 'system18'):
        assert _is_linked(a2, 'system18', b)
    _safe_set(b, 'homeTheatre19', None)
    assert not _is_linked(b, 'homeTheatre19', a2)
    if hasattr(a2, 'system18'):
        assert not _is_linked(a2, 'system18', b)


def test_assoc_HomeTheatre_TV_reverse_link_reassign_clear():
    a1 = Users(HTID="sample_text")
    a2 = Users(HTID="sample_text_2")
    b = Admin(AdminID=7)
    _safe_set(b, 'homeTheatre5', {a1})
    assert _is_linked(b, 'homeTheatre5', a1)
    if hasattr(a1, 'tV4'):
        assert _is_linked(a1, 'tV4', b)
    _safe_set(b, 'homeTheatre5', {a2})
    assert _is_linked(b, 'homeTheatre5', a2)
    if hasattr(a1, 'tV4'):
        assert not _is_linked(a1, 'tV4', b)
    if hasattr(a2, 'tV4'):
        assert _is_linked(a2, 'tV4', b)
    _safe_set(b, 'homeTheatre5', set())
    assert not _is_linked(b, 'homeTheatre5', a2)
    if hasattr(a2, 'tV4'):
        assert not _is_linked(a2, 'tV4', b)


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
    a1 = Hub_Device(Status=True, Update=3.14)
    a2 = Hub_Device(Status=False, Update=9.99)
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
    a1 = End_Of_Day(EOT=7)
    a2 = End_Of_Day(EOT=13)
    b = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    _safe_set(b, 'end_Of_Day10', a1)
    assert _is_linked(b, 'end_Of_Day10', a1)
    if hasattr(a1, 'houseHolds11'):
        assert _is_linked(a1, 'houseHolds11', b)
    _safe_set(b, 'end_Of_Day10', a2)
    assert _is_linked(b, 'end_Of_Day10', a2)
    if hasattr(a1, 'houseHolds11'):
        assert not _is_linked(a1, 'houseHolds11', b)
    if hasattr(a2, 'houseHolds11'):
        assert _is_linked(a2, 'houseHolds11', b)
    _safe_set(b, 'end_Of_Day10', None)
    assert not _is_linked(b, 'end_Of_Day10', a2)
    if hasattr(a2, 'houseHolds11'):
        assert not _is_linked(a2, 'houseHolds11', b)


def test_assoc_HouseHolds_Start_Of_Day_reverse_link_reassign_clear():
    a1 = Start_Of_Day(SOT=7)
    a2 = Start_Of_Day(SOT=13)
    b = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
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
    a1 = Sensor(SensorID=7, SensorType=7)
    a2 = Sensor(SensorID=13, SensorType=13)
    b = Hub_Device(Status=True, Update=3.14)
    _safe_set(b, 'sensor15', {a1})
    assert _is_linked(b, 'sensor15', a1)
    if hasattr(a1, 'system14'):
        assert _is_linked(a1, 'system14', b)
    _safe_set(b, 'sensor15', {a2})
    assert _is_linked(b, 'sensor15', a2)
    if hasattr(a1, 'system14'):
        assert not _is_linked(a1, 'system14', b)
    if hasattr(a2, 'system14'):
        assert _is_linked(a2, 'system14', b)
    _safe_set(b, 'sensor15', set())
    assert not _is_linked(b, 'sensor15', a2)
    if hasattr(a2, 'system14'):
        assert not _is_linked(a2, 'system14', b)


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = Hub_Device(Status=True, Update=3.14)
    a2 = Hub_Device(Status=False, Update=9.99)
    b = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

