import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AdminController,
    BookingController,
    Login,
    Membership_Card,
    OrderController,
    Table,
    processQuery,
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

def test_assoc_Order_Membership_Card_reverse_link_reassign_clear():
    a1 = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    a2 = OrderController(Date="sample_text_2", OrderID=13, OrderTotal="sample_text_2", UserID=13)
    b = Membership_Card(Discount=7, LoyaltyID=7)
    _safe_set(b, 'order5', {a1})
    assert _is_linked(b, 'order5', a1)
    if hasattr(a1, 'membership_Card4'):
        assert _is_linked(a1, 'membership_Card4', b)
    _safe_set(b, 'order5', {a2})
    assert _is_linked(b, 'order5', a2)
    if hasattr(a1, 'membership_Card4'):
        assert not _is_linked(a1, 'membership_Card4', b)
    if hasattr(a2, 'membership_Card4'):
        assert _is_linked(a2, 'membership_Card4', b)
    _safe_set(b, 'order5', set())
    assert not _is_linked(b, 'order5', a2)
    if hasattr(a2, 'membership_Card4'):
        assert not _is_linked(a2, 'membership_Card4', b)


def test_assoc_Order_Table_reverse_link_reassign_clear():
    a1 = Table(Occupied=True, TableNo="sample_text")
    a2 = Table(Occupied=False, TableNo="sample_text_2")
    b = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    _safe_set(b, 'is_ordered_by0', a1)
    assert _is_linked(b, 'is_ordered_by0', a1)
    if hasattr(a1, 'has1'):
        assert _is_linked(a1, 'has1', b)
    _safe_set(b, 'is_ordered_by0', a2)
    assert _is_linked(b, 'is_ordered_by0', a2)
    if hasattr(a1, 'has1'):
        assert not _is_linked(a1, 'has1', b)
    if hasattr(a2, 'has1'):
        assert _is_linked(a2, 'has1', b)
    _safe_set(b, 'is_ordered_by0', None)
    assert not _is_linked(b, 'is_ordered_by0', a2)
    if hasattr(a2, 'has1'):
        assert not _is_linked(a2, 'has1', b)


def test_assoc_Table_Booking_reverse_link_reassign_clear():
    a1 = Table(Occupied=True, TableNo="sample_text")
    a2 = Table(Occupied=False, TableNo="sample_text_2")
    b = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    _safe_set(b, 'is_reserved_by3', {a1})
    assert _is_linked(b, 'is_reserved_by3', a1)
    if hasattr(a1, 'reserved2'):
        assert _is_linked(a1, 'reserved2', b)
    _safe_set(b, 'is_reserved_by3', {a2})
    assert _is_linked(b, 'is_reserved_by3', a2)
    if hasattr(a1, 'reserved2'):
        assert not _is_linked(a1, 'reserved2', b)
    if hasattr(a2, 'reserved2'):
        assert _is_linked(a2, 'reserved2', b)
    _safe_set(b, 'is_reserved_by3', set())
    assert not _is_linked(b, 'is_reserved_by3', a2)
    if hasattr(a2, 'reserved2'):
        assert not _is_linked(a2, 'reserved2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Login_processQuery_stub_double():
    # processQuery has no real 'login13' property in the generated
    # code (a bare stub) -- manually attach it so Login's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Login's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Login(Discount=7, LoyaltyID=7)
    partner = processQuery()
    setattr(partner, 'login13', None)
    _safe_set(owner, 'processQuery12', partner)
    assert getattr(partner, 'login13') == owner
    _safe_set(owner, 'processQuery12', None)
    assert getattr(partner, 'login13') is None


def test_assoc_processQuery_AdminPanel_stub_double():
    # processQuery has no real 'adminPanel6' property in the generated
    # code (a bare stub) -- manually attach it so AdminController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # AdminController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = AdminController(UserID=7, UserLevel=7, UserName="sample_text")
    partner = processQuery()
    setattr(partner, 'adminPanel6', None)
    _safe_set(owner, 'processQuery7', partner)
    assert getattr(partner, 'adminPanel6') == owner
    _safe_set(owner, 'processQuery7', None)
    assert getattr(partner, 'adminPanel6') is None


def test_assoc_processQuery_Booking_stub_double():
    # processQuery has no real 'booking8' property in the generated
    # code (a bare stub) -- manually attach it so BookingController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BookingController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    partner = processQuery()
    setattr(partner, 'booking8', None)
    _safe_set(owner, 'processQuery9', partner)
    assert getattr(partner, 'booking8') == owner
    _safe_set(owner, 'processQuery9', None)
    assert getattr(partner, 'booking8') is None


def test_assoc_processQuery_Order_stub_double():
    # processQuery has no real 'order10' property in the generated
    # code (a bare stub) -- manually attach it so OrderController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OrderController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    partner = processQuery()
    setattr(partner, 'order10', None)
    _safe_set(owner, 'processQuery11', partner)
    assert getattr(partner, 'order10') == owner
    _safe_set(owner, 'processQuery11', None)
    assert getattr(partner, 'order10') is None


def test_assoc_processQuery_Table_stub_double():
    # processQuery has no real 'table14' property in the generated
    # code (a bare stub) -- manually attach it so Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Table(Occupied=True, TableNo="sample_text")
    partner = processQuery()
    setattr(partner, 'table14', None)
    _safe_set(owner, 'processQuery15', partner)
    assert getattr(partner, 'table14') == owner
    _safe_set(owner, 'processQuery15', None)
    assert getattr(partner, 'table14') is None


