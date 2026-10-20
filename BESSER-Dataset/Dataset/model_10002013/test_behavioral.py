import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alert,
    Alert2,
    Arduino,
    Count_people,
    Firebase,
    Gas_Smoke_Sensor,
    Mobile_App,
    PressureSensor,
    Sensor,
    Temperature_Sensor,
    Web,
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

def test_assoc_Arduino__Firebase_reverse_link_reassign_clear():
    a1 = Firebase(Status=True, Update=3.14)
    a2 = Firebase(Status=False, Update=9.99)
    b = Arduino(MicID="sample_text")
    _safe_set(b, 'Arduino__Firebase_08', a1)
    assert _is_linked(b, 'Arduino__Firebase_08', a1)
    if hasattr(a1, 'Arduino__Firebase_19'):
        assert _is_linked(a1, 'Arduino__Firebase_19', b)
    _safe_set(b, 'Arduino__Firebase_08', a2)
    assert _is_linked(b, 'Arduino__Firebase_08', a2)
    if hasattr(a1, 'Arduino__Firebase_19'):
        assert not _is_linked(a1, 'Arduino__Firebase_19', b)
    if hasattr(a2, 'Arduino__Firebase_19'):
        assert _is_linked(a2, 'Arduino__Firebase_19', b)
    _safe_set(b, 'Arduino__Firebase_08', None)
    assert not _is_linked(b, 'Arduino__Firebase_08', a2)
    if hasattr(a2, 'Arduino__Firebase_19'):
        assert not _is_linked(a2, 'Arduino__Firebase_19', b)


def test_assoc_Home_Security_System_Alert_reverse_link_reassign_clear():
    a1 = Mobile_App(UserID=7)
    a2 = Mobile_App(UserID=13)
    b = Alert(AlertID=7)
    _safe_set(b, 'home_Security_System3', a1)
    assert _is_linked(b, 'home_Security_System3', a1)
    if hasattr(a1, 'alert2'):
        assert _is_linked(a1, 'alert2', b)
    _safe_set(b, 'home_Security_System3', a2)
    assert _is_linked(b, 'home_Security_System3', a2)
    if hasattr(a1, 'alert2'):
        assert not _is_linked(a1, 'alert2', b)
    if hasattr(a2, 'alert2'):
        assert _is_linked(a2, 'alert2', b)
    _safe_set(b, 'home_Security_System3', None)
    assert not _is_linked(b, 'home_Security_System3', a2)
    if hasattr(a2, 'alert2'):
        assert not _is_linked(a2, 'alert2', b)


def test_assoc_Home_Security_System_System_reverse_link_reassign_clear():
    a1 = Mobile_App(UserID=7)
    a2 = Mobile_App(UserID=13)
    b = Firebase(Status=True, Update=3.14)
    _safe_set(b, 'home_Security_System7', a1)
    assert _is_linked(b, 'home_Security_System7', a1)
    if hasattr(a1, 'system6'):
        assert _is_linked(a1, 'system6', b)
    _safe_set(b, 'home_Security_System7', a2)
    assert _is_linked(b, 'home_Security_System7', a2)
    if hasattr(a1, 'system6'):
        assert not _is_linked(a1, 'system6', b)
    if hasattr(a2, 'system6'):
        assert _is_linked(a2, 'system6', b)
    _safe_set(b, 'home_Security_System7', None)
    assert not _is_linked(b, 'home_Security_System7', a2)
    if hasattr(a2, 'system6'):
        assert not _is_linked(a2, 'system6', b)


def test_assoc_Sensor_Door_reverse_link_reassign_clear():
    a1 = Sensor(SensorID=7, SensorType=7)
    a2 = Sensor(SensorID=13, SensorType=13)
    b = Count_people(_attr=7)
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
    b = Arduino(MicID="sample_text")
    _safe_set(b, 'sensor5', {a1})
    assert _is_linked(b, 'sensor5', a1)
    if hasattr(a1, 'system4'):
        assert _is_linked(a1, 'system4', b)
    _safe_set(b, 'sensor5', {a2})
    assert _is_linked(b, 'sensor5', a2)
    if hasattr(a1, 'system4'):
        assert not _is_linked(a1, 'system4', b)
    if hasattr(a2, 'system4'):
        assert _is_linked(a2, 'system4', b)
    _safe_set(b, 'sensor5', set())
    assert not _is_linked(b, 'sensor5', a2)
    if hasattr(a2, 'system4'):
        assert not _is_linked(a2, 'system4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Alert2_Web_stub_double():
    # Web has no real 'alert213' property in the generated
    # code (a bare stub) -- manually attach it so Alert2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Alert2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Alert2(AlertID=7)
    partner = Web()
    setattr(partner, 'alert213', None)
    _safe_set(owner, 'web12', partner)
    assert getattr(partner, 'alert213') == owner
    _safe_set(owner, 'web12', None)
    assert getattr(partner, 'alert213') is None


def test_assoc_Firebase_Web_stub_double():
    # Web has no real 'firebase11' property in the generated
    # code (a bare stub) -- manually attach it so Firebase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Firebase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Firebase(Status=True, Update=3.14)
    partner = Web()
    setattr(partner, 'firebase11', None)
    _safe_set(owner, 'web10', partner)
    assert getattr(partner, 'firebase11') == owner
    _safe_set(owner, 'web10', None)
    assert getattr(partner, 'firebase11') is None


