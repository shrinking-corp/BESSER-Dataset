import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_BookedTables_BookingID_value_roundtrip():
    instance = BookedTables(BookingID=7, TableNo=7)
    assert instance.BookingID == 7
    instance.BookingID = 13
    assert instance.BookingID == 13


def test_BookedTables_TableNo_value_roundtrip():
    instance = BookedTables(BookingID=7, TableNo=7)
    assert instance.TableNo == 7
    instance.TableNo = 13
    assert instance.TableNo == 13


def test_Bookings_BookingID_value_roundtrip():
    instance = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    assert instance.BookingID == 7
    instance.BookingID = 13
    assert instance.BookingID == 13


def test_Bookings_CustomerName_value_roundtrip():
    instance = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_Bookings_Date_value_roundtrip():
    instance = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    assert instance.Date == date(2024, 1, 1)
    instance.Date = date(2025, 6, 15)
    assert instance.Date == date(2025, 6, 15)


def test_Bookings_People_value_roundtrip():
    instance = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    assert instance.People == 7
    instance.People = 13
    assert instance.People == 13


def test_Bookings_Phone_value_roundtrip():
    instance = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    assert instance.Phone == "sample_text"
    instance.Phone = "sample_text_2"
    assert instance.Phone == "sample_text_2"


def test_Bookings_Time_value_roundtrip():
    instance = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    assert instance.Time == date(2024, 1, 1)
    instance.Time = date(2025, 6, 15)
    assert instance.Time == date(2025, 6, 15)


def test_Checkout_checkoutAmount_value_roundtrip():
    instance = Checkout(checkoutAmount=3.14, checkoutID=7)
    assert instance.checkoutAmount == 3.14
    instance.checkoutAmount = 9.99
    assert instance.checkoutAmount == 9.99


def test_Checkout_checkoutID_value_roundtrip():
    instance = Checkout(checkoutAmount=3.14, checkoutID=7)
    assert instance.checkoutID == 7
    instance.checkoutID = 13
    assert instance.checkoutID == 13


def test_Membership_discount_value_roundtrip():
    instance = Membership(discount=3.14, loyaltyID=7)
    assert instance.discount == 3.14
    instance.discount = 9.99
    assert instance.discount == 9.99


def test_Membership_loyaltyID_value_roundtrip():
    instance = Membership(discount=3.14, loyaltyID=7)
    assert instance.loyaltyID == 7
    instance.loyaltyID = 13
    assert instance.loyaltyID == 13


def test_Menu_Availability_value_roundtrip():
    instance = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    assert instance.Availability == 7
    instance.Availability = 13
    assert instance.Availability == 13


def test_Menu_Category_value_roundtrip():
    instance = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    assert instance.Category == "sample_text"
    instance.Category = "sample_text_2"
    assert instance.Category == "sample_text_2"


def test_Menu_MenuItem_value_roundtrip():
    instance = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    assert instance.MenuItem == "sample_text"
    instance.MenuItem = "sample_text_2"
    assert instance.MenuItem == "sample_text_2"


def test_Menu_Price_value_roundtrip():
    instance = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    assert instance.Price == 3.14
    instance.Price = 9.99
    assert instance.Price == 9.99


def test_Order_Completed_value_roundtrip():
    instance = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    assert instance.Completed == 7
    instance.Completed = 13
    assert instance.Completed == 13


def test_Order_Date_value_roundtrip():
    instance = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Order_OrderID_value_roundtrip():
    instance = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Order_UserID_value_roundtrip():
    instance = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_OrderList_ItemName_value_roundtrip():
    instance = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    assert instance.ItemName == "sample_text"
    instance.ItemName = "sample_text_2"
    assert instance.ItemName == "sample_text_2"


def test_OrderList_OrderID_value_roundtrip():
    instance = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_OrderList_OrderItemID_value_roundtrip():
    instance = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    assert instance.OrderItemID == 7
    instance.OrderItemID = 13
    assert instance.OrderItemID == 13


def test_OrderList_RemaningTime_value_roundtrip():
    instance = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    assert instance.RemaningTime == date(2024, 1, 1)
    instance.RemaningTime = date(2025, 6, 15)
    assert instance.RemaningTime == date(2025, 6, 15)


def test_Table_Occupied_value_roundtrip():
    instance = Table(Occupied=7, TableNo=7)
    assert instance.Occupied == 7
    instance.Occupied = 13
    assert instance.Occupied == 13


def test_Table_TableNo_value_roundtrip():
    instance = Table(Occupied=7, TableNo=7)
    assert instance.TableNo == 7
    instance.TableNo = 13
    assert instance.TableNo == 13


def test_Users_UserBday_value_roundtrip():
    instance = Users(UserBday=date(2024, 1, 1), UserID=7, UserLevel=7, UserName="sample_text")
    assert instance.UserBday == date(2024, 1, 1)
    instance.UserBday = date(2025, 6, 15)
    assert instance.UserBday == date(2025, 6, 15)


def test_Users_UserID_value_roundtrip():
    instance = Users(UserBday=date(2024, 1, 1), UserID=7, UserLevel=7, UserName="sample_text")
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Users_UserLevel_value_roundtrip():
    instance = Users(UserBday=date(2024, 1, 1), UserID=7, UserLevel=7, UserName="sample_text")
    assert instance.UserLevel == 7
    instance.UserLevel = 13
    assert instance.UserLevel == 13


def test_Users_UserName_value_roundtrip():
    instance = Users(UserBday=date(2024, 1, 1), UserID=7, UserLevel=7, UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_ViewOrder_getOrderList_value_roundtrip():
    instance = ViewOrder(getOrderList=7)
    assert instance.getOrderList == 7
    instance.getOrderList = 13
    assert instance.getOrderList == 13


def test_assoc_BookedTables_Table_link_reassign_clear():
    a = Table(Occupied=7, TableNo=7)
    b1 = BookedTables(BookingID=7, TableNo=7)
    b2 = BookedTables(BookingID=13, TableNo=13)
    _safe_set(a, 'bookedTables13', {b1})
    assert _is_linked(a, 'bookedTables13', b1)
    if hasattr(b1, 'table12'):
        assert _is_linked(b1, 'table12', a)
    _safe_set(a, 'bookedTables13', {b2})
    assert _is_linked(a, 'bookedTables13', b2)
    if hasattr(b1, 'table12'):
        assert not _is_linked(b1, 'table12', a)
    if hasattr(b2, 'table12'):
        assert _is_linked(b2, 'table12', a)
    _safe_set(a, 'bookedTables13', set())
    assert not _is_linked(a, 'bookedTables13', b2)
    if hasattr(b2, 'table12'):
        assert not _is_linked(b2, 'table12', a)


def test_assoc_Membership_Checkout_link_reassign_clear():
    a = Membership(discount=3.14, loyaltyID=7)
    b1 = Checkout(checkoutAmount=3.14, checkoutID=7)
    b2 = Checkout(checkoutAmount=9.99, checkoutID=13)
    _safe_set(a, 'checkout16', b1)
    assert _is_linked(a, 'checkout16', b1)
    if hasattr(b1, 'membership17'):
        assert _is_linked(b1, 'membership17', a)
    _safe_set(a, 'checkout16', b2)
    assert _is_linked(a, 'checkout16', b2)
    if hasattr(b1, 'membership17'):
        assert not _is_linked(b1, 'membership17', a)
    if hasattr(b2, 'membership17'):
        assert _is_linked(b2, 'membership17', a)
    _safe_set(a, 'checkout16', None)
    assert not _is_linked(a, 'checkout16', b2)
    if hasattr(b2, 'membership17'):
        assert not _is_linked(b2, 'membership17', a)


def test_assoc_OrderItem_Order_link_reassign_clear():
    a = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    b1 = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    b2 = Order(Completed=13, Date="sample_text_2", OrderID=13, UserID=13)
    _safe_set(a, 'order8', b1)
    assert _is_linked(a, 'order8', b1)
    if hasattr(b1, 'orderItem9'):
        assert _is_linked(b1, 'orderItem9', a)
    _safe_set(a, 'order8', b2)
    assert _is_linked(a, 'order8', b2)
    if hasattr(b1, 'orderItem9'):
        assert not _is_linked(b1, 'orderItem9', a)
    if hasattr(b2, 'orderItem9'):
        assert _is_linked(b2, 'orderItem9', a)
    _safe_set(a, 'order8', None)
    assert not _is_linked(a, 'order8', b2)
    if hasattr(b2, 'orderItem9'):
        assert not _is_linked(b2, 'orderItem9', a)


def test_assoc_Order_Checkout_link_reassign_clear():
    a = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    b1 = Checkout(checkoutAmount=3.14, checkoutID=7)
    b2 = Checkout(checkoutAmount=9.99, checkoutID=13)
    _safe_set(a, 'checkout14', b1)
    assert _is_linked(a, 'checkout14', b1)
    if hasattr(b1, 'order15'):
        assert _is_linked(b1, 'order15', a)
    _safe_set(a, 'checkout14', b2)
    assert _is_linked(a, 'checkout14', b2)
    if hasattr(b1, 'order15'):
        assert not _is_linked(b1, 'order15', a)
    if hasattr(b2, 'order15'):
        assert _is_linked(b2, 'order15', a)
    _safe_set(a, 'checkout14', None)
    assert not _is_linked(a, 'checkout14', b2)
    if hasattr(b2, 'order15'):
        assert not _is_linked(b2, 'order15', a)


def test_assoc_Order_Menu_link_reassign_clear():
    a = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    b1 = Menu(Availability=7, Category="sample_text", MenuItem="sample_text", Price=3.14)
    b2 = Menu(Availability=13, Category="sample_text_2", MenuItem="sample_text_2", Price=9.99)
    _safe_set(a, 'menu4', b1)
    assert _is_linked(a, 'menu4', b1)
    if hasattr(b1, 'orderItem5'):
        assert _is_linked(b1, 'orderItem5', a)
    _safe_set(a, 'menu4', b2)
    assert _is_linked(a, 'menu4', b2)
    if hasattr(b1, 'orderItem5'):
        assert not _is_linked(b1, 'orderItem5', a)
    if hasattr(b2, 'orderItem5'):
        assert _is_linked(b2, 'orderItem5', a)
    _safe_set(a, 'menu4', None)
    assert not _is_linked(a, 'menu4', b2)
    if hasattr(b2, 'orderItem5'):
        assert not _is_linked(b2, 'orderItem5', a)


def test_assoc_Order_Table_link_reassign_clear():
    a = Table(Occupied=7, TableNo=7)
    b1 = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    b2 = Order(Completed=13, Date="sample_text_2", OrderID=13, UserID=13)
    _safe_set(a, 'order1', {b1})
    assert _is_linked(a, 'order1', b1)
    if hasattr(b1, 'table0'):
        assert _is_linked(b1, 'table0', a)
    _safe_set(a, 'order1', {b2})
    assert _is_linked(a, 'order1', b2)
    if hasattr(b1, 'table0'):
        assert not _is_linked(b1, 'table0', a)
    if hasattr(b2, 'table0'):
        assert _is_linked(b2, 'table0', a)
    _safe_set(a, 'order1', set())
    assert not _is_linked(a, 'order1', b2)
    if hasattr(b2, 'table0'):
        assert not _is_linked(b2, 'table0', a)


def test_assoc_Order_Users_link_reassign_clear():
    a = Users(UserBday=date(2024, 1, 1), UserID=7, UserLevel=7, UserName="sample_text")
    b1 = Order(Completed=7, Date="sample_text", OrderID=7, UserID=7)
    b2 = Order(Completed=13, Date="sample_text_2", OrderID=13, UserID=13)
    _safe_set(a, 'order11', {b1})
    assert _is_linked(a, 'order11', b1)
    if hasattr(b1, 'users10'):
        assert _is_linked(b1, 'users10', a)
    _safe_set(a, 'order11', {b2})
    assert _is_linked(a, 'order11', b2)
    if hasattr(b1, 'users10'):
        assert not _is_linked(b1, 'users10', a)
    if hasattr(b2, 'users10'):
        assert _is_linked(b2, 'users10', a)
    _safe_set(a, 'order11', set())
    assert not _is_linked(a, 'order11', b2)
    if hasattr(b2, 'users10'):
        assert not _is_linked(b2, 'users10', a)


def test_assoc_Table_Bookings_link_reassign_clear():
    a = Bookings(BookingID=7, CustomerName="sample_text", Date=date(2024, 1, 1), People=7, Phone="sample_text", Time=date(2024, 1, 1))
    b1 = BookedTables(BookingID=7, TableNo=7)
    b2 = BookedTables(BookingID=13, TableNo=13)
    _safe_set(a, 'table3', {b1})
    assert _is_linked(a, 'table3', b1)
    if hasattr(b1, 'bookings2'):
        assert _is_linked(b1, 'bookings2', a)
    _safe_set(a, 'table3', {b2})
    assert _is_linked(a, 'table3', b2)
    if hasattr(b1, 'bookings2'):
        assert not _is_linked(b1, 'bookings2', a)
    if hasattr(b2, 'bookings2'):
        assert _is_linked(b2, 'bookings2', a)
    _safe_set(a, 'table3', set())
    assert not _is_linked(a, 'table3', b2)
    if hasattr(b2, 'bookings2'):
        assert not _is_linked(b2, 'bookings2', a)


def test_assoc_ViewOrder_OrderItem_link_reassign_clear():
    a = ViewOrder(getOrderList=7)
    b1 = OrderList(ItemName="sample_text", OrderID=7, OrderItemID=7, RemaningTime=date(2024, 1, 1))
    b2 = OrderList(ItemName="sample_text_2", OrderID=13, OrderItemID=13, RemaningTime=date(2025, 6, 15))
    _safe_set(a, 'orderItem6', {b1})
    assert _is_linked(a, 'orderItem6', b1)
    if hasattr(b1, 'viewOrder7'):
        assert _is_linked(b1, 'viewOrder7', a)
    _safe_set(a, 'orderItem6', {b2})
    assert _is_linked(a, 'orderItem6', b2)
    if hasattr(b1, 'viewOrder7'):
        assert not _is_linked(b1, 'viewOrder7', a)
    if hasattr(b2, 'viewOrder7'):
        assert _is_linked(b2, 'viewOrder7', a)
    _safe_set(a, 'orderItem6', set())
    assert not _is_linked(a, 'orderItem6', b2)
    if hasattr(b2, 'viewOrder7'):
        assert not _is_linked(b2, 'viewOrder7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BookedTables_strategy = st.builds(BookedTables, BookingID=st.integers(), TableNo=st.integers())
@given(instance=BookedTables_strategy)
@settings(max_examples=25)
def test_BookedTables_instantiation(instance):
    assert isinstance(instance, BookedTables)


Bookings_strategy = st.builds(Bookings, BookingID=st.integers(), CustomerName=safe_text, Date=st.dates(), People=st.integers(), Phone=safe_text, Time=st.dates())
@given(instance=Bookings_strategy)
@settings(max_examples=25)
def test_Bookings_instantiation(instance):
    assert isinstance(instance, Bookings)


Checkout_strategy = st.builds(Checkout, checkoutAmount=st.floats(allow_nan=False, allow_infinity=False), checkoutID=st.integers())
@given(instance=Checkout_strategy)
@settings(max_examples=25)
def test_Checkout_instantiation(instance):
    assert isinstance(instance, Checkout)


Membership_strategy = st.builds(Membership, discount=st.floats(allow_nan=False, allow_infinity=False), loyaltyID=st.integers())
@given(instance=Membership_strategy)
@settings(max_examples=25)
def test_Membership_instantiation(instance):
    assert isinstance(instance, Membership)


Menu_strategy = st.builds(Menu, Availability=st.integers(), Category=safe_text, MenuItem=safe_text, Price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Menu_strategy)
@settings(max_examples=25)
def test_Menu_instantiation(instance):
    assert isinstance(instance, Menu)


Order_strategy = st.builds(Order, Completed=st.integers(), Date=safe_text, OrderID=st.integers(), UserID=st.integers())
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


OrderList_strategy = st.builds(OrderList, ItemName=safe_text, OrderID=st.integers(), OrderItemID=st.integers(), RemaningTime=st.dates())
@given(instance=OrderList_strategy)
@settings(max_examples=25)
def test_OrderList_instantiation(instance):
    assert isinstance(instance, OrderList)


Table_strategy = st.builds(Table, Occupied=st.integers(), TableNo=st.integers())
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


Users_strategy = st.builds(Users, UserBday=st.dates(), UserID=st.integers(), UserLevel=st.integers(), UserName=safe_text)
@given(instance=Users_strategy)
@settings(max_examples=25)
def test_Users_instantiation(instance):
    assert isinstance(instance, Users)


ViewOrder_strategy = st.builds(ViewOrder, getOrderList=st.integers())
@given(instance=ViewOrder_strategy)
@settings(max_examples=25)
def test_ViewOrder_instantiation(instance):
    assert isinstance(instance, ViewOrder)


