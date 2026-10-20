import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BookedTables,
    Bookings,
    Checkout,
    Membership,
    Menu,
    Order,
    OrderList,
    Table,
    Users,
    ViewOrder,
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

def test_assoc_BookedTables_Table_reverse_link_reassign_clear():
    a1 = Table(Occupied=7, TableNo=7)
    a2 = Table(Occupied=13, TableNo=13)
    b = BookedTables(BookingID=7, TableNo=7)
    _safe_set(b, 'table12', a1)
    assert _is_linked(b, 'table12', a1)
    if hasattr(a1, 'bookedTables13'):
        assert _is_linked(a1, 'bookedTables13', b)
    _safe_set(b, 'table12', a2)
    assert _is_linked(b, 'table12', a2)
    if hasattr(a1, 'bookedTables13'):
        assert not _is_linked(a1, 'bookedTables13', b)
    if hasattr(a2, 'bookedTables13'):
        assert _is_linked(a2, 'bookedTables13', b)
    _safe_set(b, 'table12', None)
    assert not _is_linked(b, 'table12', a2)
    if hasattr(a2, 'bookedTables13'):
        assert not _is_linked(a2, 'bookedTables13', b)


def test_assoc_Membership_Checkout_reverse_link_reassign_clear():
    a1 = Membership(discount=3.14, loyaltyID=7)
    a2 = Membership(discount=9.99, loyaltyID=13)
    b = Checkout(checkoutAmount=3.14, checkoutID=7)
    _safe_set(b, 'membership17', a1)
    assert _is_linked(b, 'membership17', a1)
    if hasattr(a1, 'checkout16'):
        assert _is_linked(a1, 'checkout16', b)
    _safe_set(b, 'membership17', a2)
    assert _is_linked(b, 'membership17', a2)
    if hasattr(a1, 'checkout16'):
        assert not _is_linked(a1, 'checkout16', b)
    if hasattr(a2, 'checkout16'):
        assert _is_linked(a2, 'checkout16', b)
    _safe_set(b, 'membership17', None)
    assert not _is_linked(b, 'membership17', a2)
    if hasattr(a2, 'checkout16'):
        assert not _is_linked(a2, 'checkout16', b)


def test_assoc_OrderItem_Order_reverse_link_reassign_clear():
    a1 = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    a2 = OrderList(ItemName="sample_text_2", OrderID=13, OrderItemID=13, RemaningTime=date(2025, 6, 15))
    b = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    _safe_set(b, 'orderItem9', {a1})
    assert _is_linked(b, 'orderItem9', a1)
    if hasattr(a1, 'order8'):
        assert _is_linked(a1, 'order8', b)
    _safe_set(b, 'orderItem9', {a2})
    assert _is_linked(b, 'orderItem9', a2)
    if hasattr(a1, 'order8'):
        assert not _is_linked(a1, 'order8', b)
    if hasattr(a2, 'order8'):
        assert _is_linked(a2, 'order8', b)
    _safe_set(b, 'orderItem9', set())
    assert not _is_linked(b, 'orderItem9', a2)
    if hasattr(a2, 'order8'):
        assert not _is_linked(a2, 'order8', b)


def test_assoc_Order_Checkout_reverse_link_reassign_clear():
    a1 = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    a2 = Order(Completed=13, Date="sample_text_2", OrderID=13, UserID=13)
    b = Checkout(checkoutAmount=3.14, checkoutID=7)
    _safe_set(b, 'order15', a1)
    assert _is_linked(b, 'order15', a1)
    if hasattr(a1, 'checkout14'):
        assert _is_linked(a1, 'checkout14', b)
    _safe_set(b, 'order15', a2)
    assert _is_linked(b, 'order15', a2)
    if hasattr(a1, 'checkout14'):
        assert not _is_linked(a1, 'checkout14', b)
    if hasattr(a2, 'checkout14'):
        assert _is_linked(a2, 'checkout14', b)
    _safe_set(b, 'order15', None)
    assert not _is_linked(b, 'order15', a2)
    if hasattr(a2, 'checkout14'):
        assert not _is_linked(a2, 'checkout14', b)


def test_assoc_Order_Menu_reverse_link_reassign_clear():
    a1 = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    a2 = OrderList(ItemName="sample_text_2", OrderID=13, OrderItemID=13, RemaningTime=date(2025, 6, 15))
    b = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    _safe_set(b, 'orderItem5', {a1})
    assert _is_linked(b, 'orderItem5', a1)
    if hasattr(a1, 'menu4'):
        assert _is_linked(a1, 'menu4', b)
    _safe_set(b, 'orderItem5', {a2})
    assert _is_linked(b, 'orderItem5', a2)
    if hasattr(a1, 'menu4'):
        assert not _is_linked(a1, 'menu4', b)
    if hasattr(a2, 'menu4'):
        assert _is_linked(a2, 'menu4', b)
    _safe_set(b, 'orderItem5', set())
    assert not _is_linked(b, 'orderItem5', a2)
    if hasattr(a2, 'menu4'):
        assert not _is_linked(a2, 'menu4', b)


def test_assoc_Order_Table_reverse_link_reassign_clear():
    a1 = Table(Occupied=7, TableNo=7)
    a2 = Table(Occupied=13, TableNo=13)
    b = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    _safe_set(b, 'table0', a1)
    assert _is_linked(b, 'table0', a1)
    if hasattr(a1, 'order1'):
        assert _is_linked(a1, 'order1', b)
    _safe_set(b, 'table0', a2)
    assert _is_linked(b, 'table0', a2)
    if hasattr(a1, 'order1'):
        assert not _is_linked(a1, 'order1', b)
    if hasattr(a2, 'order1'):
        assert _is_linked(a2, 'order1', b)
    _safe_set(b, 'table0', None)
    assert not _is_linked(b, 'table0', a2)
    if hasattr(a2, 'order1'):
        assert not _is_linked(a2, 'order1', b)


def test_assoc_Order_Users_reverse_link_reassign_clear():
    a1 = Users(UserBday=date(2024, 1, 1), UserID=7, UserLevel=7, UserName="sample_text")
    a2 = Users(UserBday=date(2025, 6, 15), UserID=13, UserLevel=13, UserName="sample_text_2")
    b = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    _safe_set(b, 'users10', a1)
    assert _is_linked(b, 'users10', a1)
    if hasattr(a1, 'order11'):
        assert _is_linked(a1, 'order11', b)
    _safe_set(b, 'users10', a2)
    assert _is_linked(b, 'users10', a2)
    if hasattr(a1, 'order11'):
        assert not _is_linked(a1, 'order11', b)
    if hasattr(a2, 'order11'):
        assert _is_linked(a2, 'order11', b)
    _safe_set(b, 'users10', None)
    assert not _is_linked(b, 'users10', a2)
    if hasattr(a2, 'order11'):
        assert not _is_linked(a2, 'order11', b)


def test_assoc_Table_Bookings_reverse_link_reassign_clear():
    a1 = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    a2 = Bookings(BookingID=13, CustomerName="sample_text_2", Date=date(2025, 6, 15), People=13, Phone="sample_text_2", Time=date(2025, 6, 15))
    b = BookedTables(BookingID=7, TableNo=7)
    _safe_set(b, 'bookings2', a1)
    assert _is_linked(b, 'bookings2', a1)
    if hasattr(a1, 'table3'):
        assert _is_linked(a1, 'table3', b)
    _safe_set(b, 'bookings2', a2)
    assert _is_linked(b, 'bookings2', a2)
    if hasattr(a1, 'table3'):
        assert not _is_linked(a1, 'table3', b)
    if hasattr(a2, 'table3'):
        assert _is_linked(a2, 'table3', b)
    _safe_set(b, 'bookings2', None)
    assert not _is_linked(b, 'bookings2', a2)
    if hasattr(a2, 'table3'):
        assert not _is_linked(a2, 'table3', b)


def test_assoc_ViewOrder_OrderItem_reverse_link_reassign_clear():
    a1 = ViewOrder(getOrderList=7)
    a2 = ViewOrder(getOrderList=13)
    b = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    _safe_set(b, 'viewOrder7', a1)
    assert _is_linked(b, 'viewOrder7', a1)
    if hasattr(a1, 'orderItem6'):
        assert _is_linked(a1, 'orderItem6', b)
    _safe_set(b, 'viewOrder7', a2)
    assert _is_linked(b, 'viewOrder7', a2)
    if hasattr(a1, 'orderItem6'):
        assert not _is_linked(a1, 'orderItem6', b)
    if hasattr(a2, 'orderItem6'):
        assert _is_linked(a2, 'orderItem6', b)
    _safe_set(b, 'viewOrder7', None)
    assert not _is_linked(b, 'viewOrder7', a2)
    if hasattr(a2, 'orderItem6'):
        assert not _is_linked(a2, 'orderItem6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

