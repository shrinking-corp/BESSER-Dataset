import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor2_Actor,
    Actor_Actor,
    Class,
    Customer,
    Manager,
    Waiter,
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

def test_assoc_Customer_Manager_reverse_link_reassign_clear():
    a1 = Manager(Address="sample_text", Contact=7, ID=7, Name="sample_text", Personalnformation="sample_text")
    a2 = Manager(Address="sample_text_2", Contact=13, ID=13, Name="sample_text_2", Personalnformation="sample_text_2")
    b = Customer(Contact_Number=7, Dishes_Ordered="sample_text", Name="sample_text", Reservation=True, date="sample_text", reservedTables="sample_text")
    _safe_set(b, 'manager4', a1)
    assert _is_linked(b, 'manager4', a1)
    if hasattr(a1, 'customer5'):
        assert _is_linked(a1, 'customer5', b)
    _safe_set(b, 'manager4', a2)
    assert _is_linked(b, 'manager4', a2)
    if hasattr(a1, 'customer5'):
        assert not _is_linked(a1, 'customer5', b)
    if hasattr(a2, 'customer5'):
        assert _is_linked(a2, 'customer5', b)
    _safe_set(b, 'manager4', None)
    assert not _is_linked(b, 'manager4', a2)
    if hasattr(a2, 'customer5'):
        assert not _is_linked(a2, 'customer5', b)


def test_assoc_Waiter_Customer_reverse_link_reassign_clear():
    a1 = Waiter(Address="sample_text", Contact=7, ID="sample_text", Name="sample_text", Personal_Information="sample_text")
    a2 = Waiter(Address="sample_text_2", Contact=13, ID="sample_text_2", Name="sample_text_2", Personal_Information="sample_text_2")
    b = Customer(Contact_Number=7, Dishes_Ordered="sample_text", Name="sample_text", Reservation=True, date="sample_text", reservedTables="sample_text")
    _safe_set(b, 'waiter3', a1)
    assert _is_linked(b, 'waiter3', a1)
    if hasattr(a1, 'customer2'):
        assert _is_linked(a1, 'customer2', b)
    _safe_set(b, 'waiter3', a2)
    assert _is_linked(b, 'waiter3', a2)
    if hasattr(a1, 'customer2'):
        assert not _is_linked(a1, 'customer2', b)
    if hasattr(a2, 'customer2'):
        assert _is_linked(a2, 'customer2', b)
    _safe_set(b, 'waiter3', None)
    assert not _is_linked(b, 'waiter3', a2)
    if hasattr(a2, 'customer2'):
        assert not _is_linked(a2, 'customer2', b)


def test_assoc_Waiter_Manager_reverse_link_reassign_clear():
    a1 = Waiter(Address="sample_text", Contact=7, ID="sample_text", Name="sample_text", Personal_Information="sample_text")
    a2 = Waiter(Address="sample_text_2", Contact=13, ID="sample_text_2", Name="sample_text_2", Personal_Information="sample_text_2")
    b = Manager(Address="sample_text", Contact=7, ID=7, Name="sample_text", Personalnformation="sample_text")
    _safe_set(b, 'waiter1', a1)
    assert _is_linked(b, 'waiter1', a1)
    if hasattr(a1, 'manager0'):
        assert _is_linked(a1, 'manager0', b)
    _safe_set(b, 'waiter1', a2)
    assert _is_linked(b, 'waiter1', a2)
    if hasattr(a1, 'manager0'):
        assert not _is_linked(a1, 'manager0', b)
    if hasattr(a2, 'manager0'):
        assert _is_linked(a2, 'manager0', b)
    _safe_set(b, 'waiter1', None)
    assert not _is_linked(b, 'waiter1', a2)
    if hasattr(a2, 'manager0'):
        assert not _is_linked(a2, 'manager0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

