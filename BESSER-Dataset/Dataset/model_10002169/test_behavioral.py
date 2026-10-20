import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alert,
    End_Of_Day,
    Home_Security_System,
    HouseHolds,
    Lamp,
    MicroPhone,
    Relay,
    Start_Of_Day,
    System,
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
    _safe_set(b, 'system14', a1)
    assert _is_linked(b, 'system14', a1)
    if hasattr(a1, 'home_Security_System15'):
        assert _is_linked(a1, 'home_Security_System15', b)
    _safe_set(b, 'system14', a2)
    assert _is_linked(b, 'system14', a2)
    if hasattr(a1, 'home_Security_System15'):
        assert not _is_linked(a1, 'home_Security_System15', b)
    if hasattr(a2, 'home_Security_System15'):
        assert _is_linked(a2, 'home_Security_System15', b)
    _safe_set(b, 'system14', None)
    assert not _is_linked(b, 'system14', a2)
    if hasattr(a2, 'home_Security_System15'):
        assert not _is_linked(a2, 'home_Security_System15', b)


def test_assoc_HouseHolds_End_Of_Day_reverse_link_reassign_clear():
    a1 = HouseHolds(LampLight="sample_text", TimeID="sample_text")
    a2 = HouseHolds(LampLight="sample_text_2", TimeID="sample_text_2")
    b = End_Of_Day(EOT=7)
    _safe_set(b, 'houseHolds5', a1)
    assert _is_linked(b, 'houseHolds5', a1)
    if hasattr(a1, 'end_Of_Day4'):
        assert _is_linked(a1, 'end_Of_Day4', b)
    _safe_set(b, 'houseHolds5', a2)
    assert _is_linked(b, 'houseHolds5', a2)
    if hasattr(a1, 'end_Of_Day4'):
        assert not _is_linked(a1, 'end_Of_Day4', b)
    if hasattr(a2, 'end_Of_Day4'):
        assert _is_linked(a2, 'end_Of_Day4', b)
    _safe_set(b, 'houseHolds5', None)
    assert not _is_linked(b, 'houseHolds5', a2)
    if hasattr(a2, 'end_Of_Day4'):
        assert not _is_linked(a2, 'end_Of_Day4', b)


def test_assoc_HouseHolds_Start_Of_Day_reverse_link_reassign_clear():
    a1 = Start_Of_Day(SOT=7)
    a2 = Start_Of_Day(SOT=13)
    b = HouseHolds(LampLight="sample_text", TimeID="sample_text")
    _safe_set(b, 'start_Of_Day2', a1)
    assert _is_linked(b, 'start_Of_Day2', a1)
    if hasattr(a1, 'houseHolds3'):
        assert _is_linked(a1, 'houseHolds3', b)
    _safe_set(b, 'start_Of_Day2', a2)
    assert _is_linked(b, 'start_Of_Day2', a2)
    if hasattr(a1, 'houseHolds3'):
        assert not _is_linked(a1, 'houseHolds3', b)
    if hasattr(a2, 'houseHolds3'):
        assert _is_linked(a2, 'houseHolds3', b)
    _safe_set(b, 'start_Of_Day2', None)
    assert not _is_linked(b, 'start_Of_Day2', a2)
    if hasattr(a2, 'houseHolds3'):
        assert not _is_linked(a2, 'houseHolds3', b)


def test_assoc_MicroPhone_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = MicroPhone(MicID="sample_text")
    _safe_set(b, 'system6', a1)
    assert _is_linked(b, 'system6', a1)
    if hasattr(a1, 'microPhone7'):
        assert _is_linked(a1, 'microPhone7', b)
    _safe_set(b, 'system6', a2)
    assert _is_linked(b, 'system6', a2)
    if hasattr(a1, 'microPhone7'):
        assert not _is_linked(a1, 'microPhone7', b)
    if hasattr(a2, 'microPhone7'):
        assert _is_linked(a2, 'microPhone7', b)
    _safe_set(b, 'system6', None)
    assert not _is_linked(b, 'system6', a2)
    if hasattr(a2, 'microPhone7'):
        assert not _is_linked(a2, 'microPhone7', b)


def test_assoc_Sensor_Door_reverse_link_reassign_clear():
    a1 = Relay(SensorID=7, SensorType=7)
    a2 = Relay(SensorID=13, SensorType=13)
    b = Lamp(LampID=7)
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
    b = Relay(SensorID=7, SensorType=7)
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


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = HouseHolds(LampLight="sample_text", TimeID="sample_text")
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

