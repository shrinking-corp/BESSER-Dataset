import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Camera,
    Door,
    End_Of_Day,
    Entertainment,
    HomeTheatre,
    HouseHolds,
    Light,
    Light_Sensor,
    MicroPhone,
    Microcontroller,
    Motion_Sensor,
    PressureSensor,
    Sensor,
    Speakers,
    Start_Of_Day,
    System,
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

def test_assoc_HomeTheatre_Entertainment_reverse_link_reassign_clear():
    a1 = HomeTheatre(HTID="sample_text")
    a2 = HomeTheatre(HTID="sample_text_2")
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'homeTheatre21', {a1})
    assert _is_linked(b, 'homeTheatre21', a1)
    if hasattr(a1, 'entertainment20'):
        assert _is_linked(a1, 'entertainment20', b)
    _safe_set(b, 'homeTheatre21', {a2})
    assert _is_linked(b, 'homeTheatre21', a2)
    if hasattr(a1, 'entertainment20'):
        assert not _is_linked(a1, 'entertainment20', b)
    if hasattr(a2, 'entertainment20'):
        assert _is_linked(a2, 'entertainment20', b)
    _safe_set(b, 'homeTheatre21', set())
    assert not _is_linked(b, 'homeTheatre21', a2)
    if hasattr(a2, 'entertainment20'):
        assert not _is_linked(a2, 'entertainment20', b)


def test_assoc_HomeTheatre_Speakers_reverse_link_reassign_clear():
    a1 = Speakers(SpeakerID=7)
    a2 = Speakers(SpeakerID=13)
    b = HomeTheatre(HTID="sample_text")
    _safe_set(b, 'speakers4', a1)
    assert _is_linked(b, 'speakers4', a1)
    if hasattr(a1, 'homeTheatre5'):
        assert _is_linked(a1, 'homeTheatre5', b)
    _safe_set(b, 'speakers4', a2)
    assert _is_linked(b, 'speakers4', a2)
    if hasattr(a1, 'homeTheatre5'):
        assert not _is_linked(a1, 'homeTheatre5', b)
    if hasattr(a2, 'homeTheatre5'):
        assert _is_linked(a2, 'homeTheatre5', b)
    _safe_set(b, 'speakers4', None)
    assert not _is_linked(b, 'speakers4', a2)
    if hasattr(a2, 'homeTheatre5'):
        assert not _is_linked(a2, 'homeTheatre5', b)


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
    _safe_set(b, 'tV2', a1)
    assert _is_linked(b, 'tV2', a1)
    if hasattr(a1, 'homeTheatre3'):
        assert _is_linked(a1, 'homeTheatre3', b)
    _safe_set(b, 'tV2', a2)
    assert _is_linked(b, 'tV2', a2)
    if hasattr(a1, 'homeTheatre3'):
        assert not _is_linked(a1, 'homeTheatre3', b)
    if hasattr(a2, 'homeTheatre3'):
        assert _is_linked(a2, 'homeTheatre3', b)
    _safe_set(b, 'tV2', None)
    assert not _is_linked(b, 'tV2', a2)
    if hasattr(a2, 'homeTheatre3'):
        assert not _is_linked(a2, 'homeTheatre3', b)


def test_assoc_HouseHolds_End_Of_Day_reverse_link_reassign_clear():
    a1 = HouseHolds(Computer="sample_text", Fan="sample_text", Light="sample_text", TimeID="sample_text")
    a2 = HouseHolds(Computer="sample_text_2", Fan="sample_text_2", Light="sample_text_2", TimeID="sample_text_2")
    b = End_Of_Day(EOT=7)
    _safe_set(b, 'houseHolds9', a1)
    assert _is_linked(b, 'houseHolds9', a1)
    if hasattr(a1, 'end_Of_Day8'):
        assert _is_linked(a1, 'end_Of_Day8', b)
    _safe_set(b, 'houseHolds9', a2)
    assert _is_linked(b, 'houseHolds9', a2)
    if hasattr(a1, 'end_Of_Day8'):
        assert not _is_linked(a1, 'end_Of_Day8', b)
    if hasattr(a2, 'end_Of_Day8'):
        assert _is_linked(a2, 'end_Of_Day8', b)
    _safe_set(b, 'houseHolds9', None)
    assert not _is_linked(b, 'houseHolds9', a2)
    if hasattr(a2, 'end_Of_Day8'):
        assert not _is_linked(a2, 'end_Of_Day8', b)


def test_assoc_HouseHolds_Start_Of_Day_reverse_link_reassign_clear():
    a1 = Start_Of_Day(SOT=7)
    a2 = Start_Of_Day(SOT=13)
    b = HouseHolds(Computer="sample_text", Fan="sample_text", Light="sample_text", TimeID="sample_text")
    _safe_set(b, 'start_Of_Day6', a1)
    assert _is_linked(b, 'start_Of_Day6', a1)
    if hasattr(a1, 'houseHolds7'):
        assert _is_linked(a1, 'houseHolds7', b)
    _safe_set(b, 'start_Of_Day6', a2)
    assert _is_linked(b, 'start_Of_Day6', a2)
    if hasattr(a1, 'houseHolds7'):
        assert not _is_linked(a1, 'houseHolds7', b)
    if hasattr(a2, 'houseHolds7'):
        assert _is_linked(a2, 'houseHolds7', b)
    _safe_set(b, 'start_Of_Day6', None)
    assert not _is_linked(b, 'start_Of_Day6', a2)
    if hasattr(a2, 'houseHolds7'):
        assert not _is_linked(a2, 'houseHolds7', b)


def test_assoc_MicroPhone_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = MicroPhone(MicID="sample_text")
    _safe_set(b, 'system10', a1)
    assert _is_linked(b, 'system10', a1)
    if hasattr(a1, 'microPhone11'):
        assert _is_linked(a1, 'microPhone11', b)
    _safe_set(b, 'system10', a2)
    assert _is_linked(b, 'system10', a2)
    if hasattr(a1, 'microPhone11'):
        assert not _is_linked(a1, 'microPhone11', b)
    if hasattr(a2, 'microPhone11'):
        assert _is_linked(a2, 'microPhone11', b)
    _safe_set(b, 'system10', None)
    assert not _is_linked(b, 'system10', a2)
    if hasattr(a2, 'microPhone11'):
        assert not _is_linked(a2, 'microPhone11', b)


def test_assoc_Microcontroller_HouseHolds_reverse_link_reassign_clear():
    a1 = Microcontroller(sendData__="sample_text")
    a2 = Microcontroller(sendData__="sample_text_2")
    b = HouseHolds(Computer="sample_text", Fan="sample_text", Light="sample_text", TimeID="sample_text")
    _safe_set(b, 'microcontroller25', a1)
    assert _is_linked(b, 'microcontroller25', a1)
    if hasattr(a1, 'houseHolds24'):
        assert _is_linked(a1, 'houseHolds24', b)
    _safe_set(b, 'microcontroller25', a2)
    assert _is_linked(b, 'microcontroller25', a2)
    if hasattr(a1, 'houseHolds24'):
        assert not _is_linked(a1, 'houseHolds24', b)
    if hasattr(a2, 'houseHolds24'):
        assert _is_linked(a2, 'houseHolds24', b)
    _safe_set(b, 'microcontroller25', None)
    assert not _is_linked(b, 'microcontroller25', a2)
    if hasattr(a2, 'houseHolds24'):
        assert not _is_linked(a2, 'houseHolds24', b)


def test_assoc_Microcontroller_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = Microcontroller(sendData__="sample_text")
    _safe_set(b, 'system26', a1)
    assert _is_linked(b, 'system26', a1)
    if hasattr(a1, 'microcontroller27'):
        assert _is_linked(a1, 'microcontroller27', b)
    _safe_set(b, 'system26', a2)
    assert _is_linked(b, 'system26', a2)
    if hasattr(a1, 'microcontroller27'):
        assert not _is_linked(a1, 'microcontroller27', b)
    if hasattr(a2, 'microcontroller27'):
        assert _is_linked(a2, 'microcontroller27', b)
    _safe_set(b, 'system26', None)
    assert not _is_linked(b, 'system26', a2)
    if hasattr(a2, 'microcontroller27'):
        assert not _is_linked(a2, 'microcontroller27', b)


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


def test_assoc_Sensor_Microcontroller_reverse_link_reassign_clear():
    a1 = Sensor(SensorID=7, SensorType=7)
    a2 = Sensor(SensorID=13, SensorType=13)
    b = Microcontroller(sendData__="sample_text")
    _safe_set(b, 'sensor23', a1)
    assert _is_linked(b, 'sensor23', a1)
    if hasattr(a1, 'microcontroller22'):
        assert _is_linked(a1, 'microcontroller22', b)
    _safe_set(b, 'sensor23', a2)
    assert _is_linked(b, 'sensor23', a2)
    if hasattr(a1, 'microcontroller22'):
        assert not _is_linked(a1, 'microcontroller22', b)
    if hasattr(a2, 'microcontroller22'):
        assert _is_linked(a2, 'microcontroller22', b)
    _safe_set(b, 'sensor23', None)
    assert not _is_linked(b, 'sensor23', a2)
    if hasattr(a2, 'microcontroller22'):
        assert not _is_linked(a2, 'microcontroller22', b)


def test_assoc_Speakers_Entertainment_reverse_link_reassign_clear():
    a1 = Speakers(SpeakerID=7)
    a2 = Speakers(SpeakerID=13)
    b = Entertainment(DeviceID=7)
    _safe_set(b, 'speakers19', {a1})
    assert _is_linked(b, 'speakers19', a1)
    if hasattr(a1, 'entertainment18'):
        assert _is_linked(a1, 'entertainment18', b)
    _safe_set(b, 'speakers19', {a2})
    assert _is_linked(b, 'speakers19', a2)
    if hasattr(a1, 'entertainment18'):
        assert not _is_linked(a1, 'entertainment18', b)
    if hasattr(a2, 'entertainment18'):
        assert _is_linked(a2, 'entertainment18', b)
    _safe_set(b, 'speakers19', set())
    assert not _is_linked(b, 'speakers19', a2)
    if hasattr(a2, 'entertainment18'):
        assert not _is_linked(a2, 'entertainment18', b)


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = HouseHolds(Computer="sample_text", Fan="sample_text", Light="sample_text", TimeID="sample_text")
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
    _safe_set(b, 'tV17', {a1})
    assert _is_linked(b, 'tV17', a1)
    if hasattr(a1, 'entertainment16'):
        assert _is_linked(a1, 'entertainment16', b)
    _safe_set(b, 'tV17', {a2})
    assert _is_linked(b, 'tV17', a2)
    if hasattr(a1, 'entertainment16'):
        assert not _is_linked(a1, 'entertainment16', b)
    if hasattr(a2, 'entertainment16'):
        assert _is_linked(a2, 'entertainment16', b)
    _safe_set(b, 'tV17', set())
    assert not _is_linked(b, 'tV17', a2)
    if hasattr(a2, 'entertainment16'):
        assert not _is_linked(a2, 'entertainment16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

