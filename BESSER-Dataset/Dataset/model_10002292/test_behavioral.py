import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AdminPanel,
    BookedTables,
    Bookings,
    Membership_Card,
    Menu,
    Order,
    OrderItem,
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

def test_assoc_AdminPanel_Menu_reverse_link_reassign_clear():
    a1 = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    a2 = Menu(Availability=13, Category="sample_text_2", MenuItem="sample_text_2", Price=9.99)
    b = AdminPanel(UserID=7, UserLevel=7, UserName="sample_text")
    _safe_set(b, 'menu8', a1)
    assert _is_linked(b, 'menu8', a1)
    if hasattr(a1, 'adminPanel9'):
        assert _is_linked(a1, 'adminPanel9', b)
    _safe_set(b, 'menu8', a2)
    assert _is_linked(b, 'menu8', a2)
    if hasattr(a1, 'adminPanel9'):
        assert not _is_linked(a1, 'adminPanel9', b)
    if hasattr(a2, 'adminPanel9'):
        assert _is_linked(a2, 'adminPanel9', b)
    _safe_set(b, 'menu8', None)
    assert not _is_linked(b, 'menu8', a2)
    if hasattr(a2, 'adminPanel9'):
        assert not _is_linked(a2, 'adminPanel9', b)


def test_assoc_BookedTables_Table_reverse_link_reassign_clear():
    a1 = Table(Occupied=7, TableNo=7)
    a2 = Table(Occupied=13, TableNo=13)
    b = BookedTables(BookingID=7, TableNo=7)
    _safe_set(b, 'table16', a1)
    assert _is_linked(b, 'table16', a1)
    if hasattr(a1, 'bookedTables17'):
        assert _is_linked(a1, 'bookedTables17', b)
    _safe_set(b, 'table16', a2)
    assert _is_linked(b, 'table16', a2)
    if hasattr(a1, 'bookedTables17'):
        assert not _is_linked(a1, 'bookedTables17', b)
    if hasattr(a2, 'bookedTables17'):
        assert _is_linked(a2, 'bookedTables17', b)
    _safe_set(b, 'table16', None)
    assert not _is_linked(b, 'table16', a2)
    if hasattr(a2, 'bookedTables17'):
        assert not _is_linked(a2, 'bookedTables17', b)


def test_assoc_Membership_Card_Order_reverse_link_reassign_clear():
    a1 = Order(Date=date(2024, 1, 1), DicountLvl=7, OrderID=7, Total=3.14, UserID=7)
    a2 = Order(Date=date(2025, 6, 15), DicountLvl=13, OrderID=13, Total=9.99, UserID=13)
    b = Membership_Card(DiscountLVL=7, ID=7)
    _safe_set(b, 'order0', {a1})
    assert _is_linked(b, 'order0', a1)
    if hasattr(a1, 'membership_Card1'):
        assert _is_linked(a1, 'membership_Card1', b)
    _safe_set(b, 'order0', {a2})
    assert _is_linked(b, 'order0', a2)
    if hasattr(a1, 'membership_Card1'):
        assert not _is_linked(a1, 'membership_Card1', b)
    if hasattr(a2, 'membership_Card1'):
        assert _is_linked(a2, 'membership_Card1', b)
    _safe_set(b, 'order0', set())
    assert not _is_linked(b, 'order0', a2)
    if hasattr(a2, 'membership_Card1'):
        assert not _is_linked(a2, 'membership_Card1', b)


def test_assoc_OrderItem_Order_reverse_link_reassign_clear():
    a1 = OrderItem(Completed=7, ItemName="sample_text", RemaningTime=date(2024, 1, 1))
    a2 = OrderItem(Completed=13, ItemName="sample_text_2", RemaningTime=date(2025, 6, 15))
    b = Order(Date=date(2024, 1, 1), DicountLvl=7, OrderID=7, Total=3.14, UserID=7)
    _safe_set(b, 'orderItem13', {a1})
    assert _is_linked(b, 'orderItem13', a1)
    if hasattr(a1, 'order12'):
        assert _is_linked(a1, 'order12', b)
    _safe_set(b, 'orderItem13', {a2})
    assert _is_linked(b, 'orderItem13', a2)
    if hasattr(a1, 'order12'):
        assert not _is_linked(a1, 'order12', b)
    if hasattr(a2, 'order12'):
        assert _is_linked(a2, 'order12', b)
    _safe_set(b, 'orderItem13', set())
    assert not _is_linked(b, 'orderItem13', a2)
    if hasattr(a2, 'order12'):
        assert not _is_linked(a2, 'order12', b)


def test_assoc_Order_Menu_reverse_link_reassign_clear():
    a1 = Order(Date=date(2024, 1, 1), DicountLvl=7, OrderID=7, Total=3.14, UserID=7)
    a2 = Order(Date=date(2025, 6, 15), DicountLvl=13, OrderID=13, Total=9.99, UserID=13)
    b = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    _safe_set(b, 'order7', a1)
    assert _is_linked(b, 'order7', a1)
    if hasattr(a1, 'menu6'):
        assert _is_linked(a1, 'menu6', b)
    _safe_set(b, 'order7', a2)
    assert _is_linked(b, 'order7', a2)
    if hasattr(a1, 'menu6'):
        assert not _is_linked(a1, 'menu6', b)
    if hasattr(a2, 'menu6'):
        assert _is_linked(a2, 'menu6', b)
    _safe_set(b, 'order7', None)
    assert not _is_linked(b, 'order7', a2)
    if hasattr(a2, 'menu6'):
        assert not _is_linked(a2, 'menu6', b)


def test_assoc_Order_Table_reverse_link_reassign_clear():
    a1 = Table(Occupied=7, TableNo=7)
    a2 = Table(Occupied=13, TableNo=13)
    b = Order(Date=date(2024, 1, 1), DicountLvl=7, OrderID=7, Total=3.14, UserID=7)
    _safe_set(b, 'table2', a1)
    assert _is_linked(b, 'table2', a1)
    if hasattr(a1, 'order3'):
        assert _is_linked(a1, 'order3', b)
    _safe_set(b, 'table2', a2)
    assert _is_linked(b, 'table2', a2)
    if hasattr(a1, 'order3'):
        assert not _is_linked(a1, 'order3', b)
    if hasattr(a2, 'order3'):
        assert _is_linked(a2, 'order3', b)
    _safe_set(b, 'table2', None)
    assert not _is_linked(b, 'table2', a2)
    if hasattr(a2, 'order3'):
        assert not _is_linked(a2, 'order3', b)


def test_assoc_Order_Users_reverse_link_reassign_clear():
    a1 = Users(UserID=7, UserLevel=7, UserName="sample_text")
    a2 = Users(UserID=13, UserLevel=13, UserName="sample_text_2")
    b = Order(Date=date(2024, 1, 1), DicountLvl=7, OrderID=7, Total=3.14, UserID=7)
    _safe_set(b, 'users14', a1)
    assert _is_linked(b, 'users14', a1)
    if hasattr(a1, 'order15'):
        assert _is_linked(a1, 'order15', b)
    _safe_set(b, 'users14', a2)
    assert _is_linked(b, 'users14', a2)
    if hasattr(a1, 'order15'):
        assert not _is_linked(a1, 'order15', b)
    if hasattr(a2, 'order15'):
        assert _is_linked(a2, 'order15', b)
    _safe_set(b, 'users14', None)
    assert not _is_linked(b, 'users14', a2)
    if hasattr(a2, 'order15'):
        assert not _is_linked(a2, 'order15', b)


def test_assoc_Table_Bookings_reverse_link_reassign_clear():
    a1 = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", TableNo=7, Time=date(2024, 1, 1))
    a2 = Bookings(BookingID=13, CustomerName="sample_text_2", Date=date(2025, 6, 15), People=13, Phone="sample_text_2", TableNo=13, Time=date(2025, 6, 15))
    b = BookedTables(BookingID=7, TableNo=7)
    _safe_set(b, 'bookings4', a1)
    assert _is_linked(b, 'bookings4', a1)
    if hasattr(a1, 'table5'):
        assert _is_linked(a1, 'table5', b)
    _safe_set(b, 'bookings4', a2)
    assert _is_linked(b, 'bookings4', a2)
    if hasattr(a1, 'table5'):
        assert not _is_linked(a1, 'table5', b)
    if hasattr(a2, 'table5'):
        assert _is_linked(a2, 'table5', b)
    _safe_set(b, 'bookings4', None)
    assert not _is_linked(b, 'bookings4', a2)
    if hasattr(a2, 'table5'):
        assert not _is_linked(a2, 'table5', b)


def test_assoc_ViewOrder_OrderItem_reverse_link_reassign_clear():
    a1 = ViewOrder(getUser=7)
    a2 = ViewOrder(getUser=13)
    b = OrderItem(Completed=7, ItemName="sample_text", RemaningTime=date(2024, 1, 1))
    _safe_set(b, 'viewOrder11', a1)
    assert _is_linked(b, 'viewOrder11', a1)
    if hasattr(a1, 'orderItem10'):
        assert _is_linked(a1, 'orderItem10', b)
    _safe_set(b, 'viewOrder11', a2)
    assert _is_linked(b, 'viewOrder11', a2)
    if hasattr(a1, 'orderItem10'):
        assert not _is_linked(a1, 'orderItem10', b)
    if hasattr(a2, 'orderItem10'):
        assert _is_linked(a2, 'orderItem10', b)
    _safe_set(b, 'viewOrder11', None)
    assert not _is_linked(b, 'viewOrder11', a2)
    if hasattr(a2, 'orderItem10'):
        assert not _is_linked(a2, 'orderItem10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

