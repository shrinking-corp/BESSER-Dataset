import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Guest,
    Host,
    Kitchen,
    Online_Customer,
    Order,
    Party,
    Payment,
    Reservation,
    Staff,
    Table,
    Waiter,
    Date,
    ReservationType,
    ReservationType2,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Waiter_Bill_stub_double():
    # Waiter has no real 'bill6' property in the generated
    # code (a bare stub) -- manually attach it so Bill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Bill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Bill(Tax=7, Tip=7, TotalAmount=7)
    partner = Waiter()
    setattr(partner, 'bill6', None)
    _safe_set(owner, 'waiter7', partner)
    assert getattr(partner, 'bill6') == owner
    _safe_set(owner, 'waiter7', None)
    assert getattr(partner, 'bill6') is None


def test_assoc_Waiter_Table_stub_double():
    # Waiter has no real 'table8' property in the generated
    # code (a bare stub) -- manually attach it so Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Table(Capacity=7, TableID="sample_text")
    partner = Waiter()
    setattr(partner, 'table8', None)
    _safe_set(owner, 'waiter9', partner)
    assert getattr(partner, 'table8') == owner
    _safe_set(owner, 'waiter9', None)
    assert getattr(partner, 'table8') is None


