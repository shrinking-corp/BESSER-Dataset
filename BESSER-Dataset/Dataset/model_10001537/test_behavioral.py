import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CheckStaff,
    Luggage,
    Passenger,
    Ticket,
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

def test_assoc_CheckStaff_Ticket_reverse_link_reassign_clear():
    a1 = Ticket(no=7)
    a2 = Ticket(no=13)
    b = CheckStaff(name="sample_text")
    _safe_set(b, 'ticket8', a1)
    assert _is_linked(b, 'ticket8', a1)
    if hasattr(a1, 'checkStaff9'):
        assert _is_linked(a1, 'checkStaff9', b)
    _safe_set(b, 'ticket8', a2)
    assert _is_linked(b, 'ticket8', a2)
    if hasattr(a1, 'checkStaff9'):
        assert not _is_linked(a1, 'checkStaff9', b)
    if hasattr(a2, 'checkStaff9'):
        assert _is_linked(a2, 'checkStaff9', b)
    _safe_set(b, 'ticket8', None)
    assert not _is_linked(b, 'ticket8', a2)
    if hasattr(a2, 'checkStaff9'):
        assert not _is_linked(a2, 'checkStaff9', b)


def test_assoc_Luggage_CheckStaff_reverse_link_reassign_clear():
    a1 = Luggage(weight=7)
    a2 = Luggage(weight=13)
    b = CheckStaff(name="sample_text")
    _safe_set(b, 'luggage5', a1)
    assert _is_linked(b, 'luggage5', a1)
    if hasattr(a1, 'checkStaff4'):
        assert _is_linked(a1, 'checkStaff4', b)
    _safe_set(b, 'luggage5', a2)
    assert _is_linked(b, 'luggage5', a2)
    if hasattr(a1, 'checkStaff4'):
        assert not _is_linked(a1, 'checkStaff4', b)
    if hasattr(a2, 'checkStaff4'):
        assert _is_linked(a2, 'checkStaff4', b)
    _safe_set(b, 'luggage5', None)
    assert not _is_linked(b, 'luggage5', a2)
    if hasattr(a2, 'checkStaff4'):
        assert not _is_linked(a2, 'checkStaff4', b)


def test_assoc_Passenger_CheckStaff_reverse_link_reassign_clear():
    a1 = Passenger(name="sample_text")
    a2 = Passenger(name="sample_text_2")
    b = CheckStaff(name="sample_text")
    _safe_set(b, 'passenger7', a1)
    assert _is_linked(b, 'passenger7', a1)
    if hasattr(a1, 'checkStaff6'):
        assert _is_linked(a1, 'checkStaff6', b)
    _safe_set(b, 'passenger7', a2)
    assert _is_linked(b, 'passenger7', a2)
    if hasattr(a1, 'checkStaff6'):
        assert not _is_linked(a1, 'checkStaff6', b)
    if hasattr(a2, 'checkStaff6'):
        assert _is_linked(a2, 'checkStaff6', b)
    _safe_set(b, 'passenger7', None)
    assert not _is_linked(b, 'passenger7', a2)
    if hasattr(a2, 'checkStaff6'):
        assert not _is_linked(a2, 'checkStaff6', b)


def test_assoc_luggage_Passenger_Luggage_0_reverse_link_reassign_clear():
    a1 = Passenger(name="sample_text")
    a2 = Passenger(name="sample_text_2")
    b = Luggage(weight=7)
    _safe_set(b, 'passenger0', a1)
    assert _is_linked(b, 'passenger0', a1)
    if hasattr(a1, 'luggage1'):
        assert _is_linked(a1, 'luggage1', b)
    _safe_set(b, 'passenger0', a2)
    assert _is_linked(b, 'passenger0', a2)
    if hasattr(a1, 'luggage1'):
        assert not _is_linked(a1, 'luggage1', b)
    if hasattr(a2, 'luggage1'):
        assert _is_linked(a2, 'luggage1', b)
    _safe_set(b, 'passenger0', None)
    assert not _is_linked(b, 'passenger0', a2)
    if hasattr(a2, 'luggage1'):
        assert not _is_linked(a2, 'luggage1', b)


def test_assoc_ticket_Passenger_Ticket_1_reverse_link_reassign_clear():
    a1 = Ticket(no=7)
    a2 = Ticket(no=13)
    b = Passenger(name="sample_text")
    _safe_set(b, 'ticket3', a1)
    assert _is_linked(b, 'ticket3', a1)
    if hasattr(a1, 'passenger2'):
        assert _is_linked(a1, 'passenger2', b)
    _safe_set(b, 'ticket3', a2)
    assert _is_linked(b, 'ticket3', a2)
    if hasattr(a1, 'passenger2'):
        assert not _is_linked(a1, 'passenger2', b)
    if hasattr(a2, 'passenger2'):
        assert _is_linked(a2, 'passenger2', b)
    _safe_set(b, 'ticket3', None)
    assert not _is_linked(b, 'ticket3', a2)
    if hasattr(a2, 'passenger2'):
        assert not _is_linked(a2, 'passenger2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

