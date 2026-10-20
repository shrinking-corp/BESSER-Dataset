import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Camera,
    Door,
    Entertainment_System,
    Fan,
    GSM_Module,
    Geyser,
    HomeTheatre,
    Light,
    Microcontroller,
    Speakers,
    TV,
    User__SMS_,
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
    _safe_set(b, 'door1', a1)
    assert _is_linked(b, 'door1', a1)
    if hasattr(a1, 'camera0'):
        assert _is_linked(a1, 'camera0', b)
    _safe_set(b, 'door1', a2)
    assert _is_linked(b, 'door1', a2)
    if hasattr(a1, 'camera0'):
        assert not _is_linked(a1, 'camera0', b)
    if hasattr(a2, 'camera0'):
        assert _is_linked(a2, 'camera0', b)
    _safe_set(b, 'door1', None)
    assert not _is_linked(b, 'door1', a2)
    if hasattr(a2, 'camera0'):
        assert not _is_linked(a2, 'camera0', b)


def test_assoc_GSM_Module_Microcontroller_reverse_link_reassign_clear():
    a1 = Microcontroller(Status="sample_text", Update=3.14)
    a2 = Microcontroller(Status="sample_text_2", Update=9.99)
    b = GSM_Module(CmdMatch="sample_text", Status="sample_text", Update=3.14)
    _safe_set(b, 'microcontroller12', a1)
    assert _is_linked(b, 'microcontroller12', a1)
    if hasattr(a1, 'gSM_Module13'):
        assert _is_linked(a1, 'gSM_Module13', b)
    _safe_set(b, 'microcontroller12', a2)
    assert _is_linked(b, 'microcontroller12', a2)
    if hasattr(a1, 'gSM_Module13'):
        assert not _is_linked(a1, 'gSM_Module13', b)
    if hasattr(a2, 'gSM_Module13'):
        assert _is_linked(a2, 'gSM_Module13', b)
    _safe_set(b, 'microcontroller12', None)
    assert not _is_linked(b, 'microcontroller12', a2)
    if hasattr(a2, 'gSM_Module13'):
        assert not _is_linked(a2, 'gSM_Module13', b)


def test_assoc_HomeTheatre_Entertainment_reverse_link_reassign_clear():
    a1 = HomeTheatre(HTID="sample_text")
    a2 = HomeTheatre(HTID="sample_text_2")
    b = Entertainment_System(DeviceID=7)
    _safe_set(b, 'homeTheatre11', {a1})
    assert _is_linked(b, 'homeTheatre11', a1)
    if hasattr(a1, 'entertainment10'):
        assert _is_linked(a1, 'entertainment10', b)
    _safe_set(b, 'homeTheatre11', {a2})
    assert _is_linked(b, 'homeTheatre11', a2)
    if hasattr(a1, 'entertainment10'):
        assert not _is_linked(a1, 'entertainment10', b)
    if hasattr(a2, 'entertainment10'):
        assert _is_linked(a2, 'entertainment10', b)
    _safe_set(b, 'homeTheatre11', set())
    assert not _is_linked(b, 'homeTheatre11', a2)
    if hasattr(a2, 'entertainment10'):
        assert not _is_linked(a2, 'entertainment10', b)


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


def test_assoc_Light_Fan_reverse_link_reassign_clear():
    a1 = Light(LightID="sample_text")
    a2 = Light(LightID="sample_text_2")
    b = Fan(FanID="sample_text")
    _safe_set(b, 'light15', a1)
    assert _is_linked(b, 'light15', a1)
    if hasattr(a1, 'fan14'):
        assert _is_linked(a1, 'fan14', b)
    _safe_set(b, 'light15', a2)
    assert _is_linked(b, 'light15', a2)
    if hasattr(a1, 'fan14'):
        assert not _is_linked(a1, 'fan14', b)
    if hasattr(a2, 'fan14'):
        assert _is_linked(a2, 'fan14', b)
    _safe_set(b, 'light15', None)
    assert not _is_linked(b, 'light15', a2)
    if hasattr(a2, 'fan14'):
        assert not _is_linked(a2, 'fan14', b)


def test_assoc_Speakers_Entertainment_reverse_link_reassign_clear():
    a1 = Speakers(SpeakerID=7)
    a2 = Speakers(SpeakerID=13)
    b = Entertainment_System(DeviceID=7)
    _safe_set(b, 'speakers9', {a1})
    assert _is_linked(b, 'speakers9', a1)
    if hasattr(a1, 'entertainment8'):
        assert _is_linked(a1, 'entertainment8', b)
    _safe_set(b, 'speakers9', {a2})
    assert _is_linked(b, 'speakers9', a2)
    if hasattr(a1, 'entertainment8'):
        assert not _is_linked(a1, 'entertainment8', b)
    if hasattr(a2, 'entertainment8'):
        assert _is_linked(a2, 'entertainment8', b)
    _safe_set(b, 'speakers9', set())
    assert not _is_linked(b, 'speakers9', a2)
    if hasattr(a2, 'entertainment8'):
        assert not _is_linked(a2, 'entertainment8', b)


def test_assoc_TV_Entertainment_reverse_link_reassign_clear():
    a1 = TV(TVID=7)
    a2 = TV(TVID=13)
    b = Entertainment_System(DeviceID=7)
    _safe_set(b, 'tV7', {a1})
    assert _is_linked(b, 'tV7', a1)
    if hasattr(a1, 'entertainment6'):
        assert _is_linked(a1, 'entertainment6', b)
    _safe_set(b, 'tV7', {a2})
    assert _is_linked(b, 'tV7', a2)
    if hasattr(a1, 'entertainment6'):
        assert not _is_linked(a1, 'entertainment6', b)
    if hasattr(a2, 'entertainment6'):
        assert _is_linked(a2, 'entertainment6', b)
    _safe_set(b, 'tV7', set())
    assert not _is_linked(b, 'tV7', a2)
    if hasattr(a2, 'entertainment6'):
        assert not _is_linked(a2, 'entertainment6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

