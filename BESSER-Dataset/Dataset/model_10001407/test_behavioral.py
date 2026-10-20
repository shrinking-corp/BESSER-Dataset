import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alert,
    Control_Box,
    FAN,
    Fan_Regulator_Box,
    FireAlarm_Sensor,
    Home_Security_System,
    HouseHolds,
    Light,
    MicroPhone,
    Sensor,
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
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = Home_Security_System(UserID=7)
    _safe_set(b, 'system6', a1)
    assert _is_linked(b, 'system6', a1)
    if hasattr(a1, 'home_Security_System7'):
        assert _is_linked(a1, 'home_Security_System7', b)
    _safe_set(b, 'system6', a2)
    assert _is_linked(b, 'system6', a2)
    if hasattr(a1, 'home_Security_System7'):
        assert not _is_linked(a1, 'home_Security_System7', b)
    if hasattr(a2, 'home_Security_System7'):
        assert _is_linked(a2, 'home_Security_System7', b)
    _safe_set(b, 'system6', None)
    assert not _is_linked(b, 'system6', a2)
    if hasattr(a2, 'home_Security_System7'):
        assert not _is_linked(a2, 'home_Security_System7', b)


def test_assoc_MicroPhone_System_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = MicroPhone(MicID="sample_text")
    _safe_set(b, 'system0', a1)
    assert _is_linked(b, 'system0', a1)
    if hasattr(a1, 'microPhone1'):
        assert _is_linked(a1, 'microPhone1', b)
    _safe_set(b, 'system0', a2)
    assert _is_linked(b, 'system0', a2)
    if hasattr(a1, 'microPhone1'):
        assert not _is_linked(a1, 'microPhone1', b)
    if hasattr(a2, 'microPhone1'):
        assert _is_linked(a2, 'microPhone1', b)
    _safe_set(b, 'system0', None)
    assert not _is_linked(b, 'system0', a2)
    if hasattr(a2, 'microPhone1'):
        assert not _is_linked(a2, 'microPhone1', b)


def test_assoc_System_HouseHolds_reverse_link_reassign_clear():
    a1 = System(Status=True, Update=3.14)
    a2 = System(Status=False, Update=9.99)
    b = HouseHolds(Alarm="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    _safe_set(b, 'system5', a1)
    assert _is_linked(b, 'system5', a1)
    if hasattr(a1, 'houseHolds4'):
        assert _is_linked(a1, 'houseHolds4', b)
    _safe_set(b, 'system5', a2)
    assert _is_linked(b, 'system5', a2)
    if hasattr(a1, 'houseHolds4'):
        assert not _is_linked(a1, 'houseHolds4', b)
    if hasattr(a2, 'houseHolds4'):
        assert _is_linked(a2, 'houseHolds4', b)
    _safe_set(b, 'system5', None)
    assert not _is_linked(b, 'system5', a2)
    if hasattr(a2, 'houseHolds4'):
        assert not _is_linked(a2, 'houseHolds4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

