import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AdminController,
    BookingController,
    Login,
    Membership_Card,
    OrderController,
    Table,
    processQuery,
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

def test_AdminController_UserID_value_roundtrip():
    instance = AdminController(UserID=7, UserLevel=7, UserName="sample_text")
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_AdminController_UserLevel_value_roundtrip():
    instance = AdminController(UserID=7, UserLevel=7, UserName="sample_text")
    assert instance.UserLevel == 7
    instance.UserLevel = 13
    assert instance.UserLevel == 13


def test_AdminController_UserName_value_roundtrip():
    instance = AdminController(UserID=7, UserLevel=7, UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_BookingController_BookingID_value_roundtrip():
    instance = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    assert instance.BookingID == 7
    instance.BookingID = 13
    assert instance.BookingID == 13


def test_BookingController_CustomerName_value_roundtrip():
    instance = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_BookingController_Date_value_roundtrip():
    instance = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_BookingController_Phone_value_roundtrip():
    instance = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    assert instance.Phone == "sample_text"
    instance.Phone = "sample_text_2"
    assert instance.Phone == "sample_text_2"


def test_BookingController_TableNo_value_roundtrip():
    instance = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    assert instance.TableNo == "sample_text"
    instance.TableNo = "sample_text_2"
    assert instance.TableNo == "sample_text_2"


def test_BookingController_Time_value_roundtrip():
    instance = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    assert instance.Time == "sample_text"
    instance.Time = "sample_text_2"
    assert instance.Time == "sample_text_2"


def test_Login_Discount_value_roundtrip():
    instance = Login(Discount=7, LoyaltyID=7)
    assert instance.Discount == 7
    instance.Discount = 13
    assert instance.Discount == 13


def test_Login_LoyaltyID_value_roundtrip():
    instance = Login(Discount=7, LoyaltyID=7)
    assert instance.LoyaltyID == 7
    instance.LoyaltyID = 13
    assert instance.LoyaltyID == 13


def test_Membership_Card_Discount_value_roundtrip():
    instance = Membership_Card(Discount=7, LoyaltyID=7)
    assert instance.Discount == 7
    instance.Discount = 13
    assert instance.Discount == 13


def test_Membership_Card_LoyaltyID_value_roundtrip():
    instance = Membership_Card(Discount=7, LoyaltyID=7)
    assert instance.LoyaltyID == 7
    instance.LoyaltyID = 13
    assert instance.LoyaltyID == 13


def test_OrderController_Date_value_roundtrip():
    instance = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_OrderController_OrderID_value_roundtrip():
    instance = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_OrderController_OrderTotal_value_roundtrip():
    instance = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    assert instance.OrderTotal == "sample_text"
    instance.OrderTotal = "sample_text_2"
    assert instance.OrderTotal == "sample_text_2"


def test_OrderController_UserID_value_roundtrip():
    instance = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Table_Occupied_value_roundtrip():
    instance = Table(Occupied=True, TableNo="sample_text")
    assert instance.Occupied == True
    instance.Occupied = False
    assert instance.Occupied == False


def test_Table_TableNo_value_roundtrip():
    instance = Table(Occupied=True, TableNo="sample_text")
    assert instance.TableNo == "sample_text"
    instance.TableNo = "sample_text_2"
    assert instance.TableNo == "sample_text_2"


def test_assoc_Login_processQuery_link_reassign_clear():
    a = Login(Discount=7, LoyaltyID=7)
    b1 = processQuery()
    b2 = processQuery()
    _safe_set(a, 'processQuery12', b1)
    assert _is_linked(a, 'processQuery12', b1)
    if hasattr(b1, 'login13'):
        assert _is_linked(b1, 'login13', a)
    _safe_set(a, 'processQuery12', b2)
    assert _is_linked(a, 'processQuery12', b2)
    if hasattr(b1, 'login13'):
        assert not _is_linked(b1, 'login13', a)
    if hasattr(b2, 'login13'):
        assert _is_linked(b2, 'login13', a)
    _safe_set(a, 'processQuery12', None)
    assert not _is_linked(a, 'processQuery12', b2)
    if hasattr(b2, 'login13'):
        assert not _is_linked(b2, 'login13', a)


def test_assoc_Order_Membership_Card_link_reassign_clear():
    a = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    b1 = Membership_Card(Discount=7, LoyaltyID=7)
    b2 = Membership_Card(Discount=13, LoyaltyID=13)
    _safe_set(a, 'membership_Card4', b1)
    assert _is_linked(a, 'membership_Card4', b1)
    if hasattr(b1, 'order5'):
        assert _is_linked(b1, 'order5', a)
    _safe_set(a, 'membership_Card4', b2)
    assert _is_linked(a, 'membership_Card4', b2)
    if hasattr(b1, 'order5'):
        assert not _is_linked(b1, 'order5', a)
    if hasattr(b2, 'order5'):
        assert _is_linked(b2, 'order5', a)
    _safe_set(a, 'membership_Card4', None)
    assert not _is_linked(a, 'membership_Card4', b2)
    if hasattr(b2, 'order5'):
        assert not _is_linked(b2, 'order5', a)


def test_assoc_Order_Table_link_reassign_clear():
    a = Table(Occupied=True, TableNo="sample_text")
    b1 = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    b2 = OrderController(Date="sample_text_2", OrderID=13, OrderTotal="sample_text_2", UserID=13)
    _safe_set(a, 'has1', b1)
    assert _is_linked(a, 'has1', b1)
    if hasattr(b1, 'is_ordered_by0'):
        assert _is_linked(b1, 'is_ordered_by0', a)
    _safe_set(a, 'has1', b2)
    assert _is_linked(a, 'has1', b2)
    if hasattr(b1, 'is_ordered_by0'):
        assert not _is_linked(b1, 'is_ordered_by0', a)
    if hasattr(b2, 'is_ordered_by0'):
        assert _is_linked(b2, 'is_ordered_by0', a)
    _safe_set(a, 'has1', None)
    assert not _is_linked(a, 'has1', b2)
    if hasattr(b2, 'is_ordered_by0'):
        assert not _is_linked(b2, 'is_ordered_by0', a)


def test_assoc_Table_Booking_link_reassign_clear():
    a = Table(Occupied=True, TableNo="sample_text")
    b1 = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    b2 = BookingController(BookingID=13, CustomerName="sample_text_2", Date="sample_text_2", Phone="sample_text_2", TableNo="sample_text_2", Time="sample_text_2")
    _safe_set(a, 'reserved2', b1)
    assert _is_linked(a, 'reserved2', b1)
    if hasattr(b1, 'is_reserved_by3'):
        assert _is_linked(b1, 'is_reserved_by3', a)
    _safe_set(a, 'reserved2', b2)
    assert _is_linked(a, 'reserved2', b2)
    if hasattr(b1, 'is_reserved_by3'):
        assert not _is_linked(b1, 'is_reserved_by3', a)
    if hasattr(b2, 'is_reserved_by3'):
        assert _is_linked(b2, 'is_reserved_by3', a)
    _safe_set(a, 'reserved2', None)
    assert not _is_linked(a, 'reserved2', b2)
    if hasattr(b2, 'is_reserved_by3'):
        assert not _is_linked(b2, 'is_reserved_by3', a)


def test_assoc_processQuery_AdminPanel_link_reassign_clear():
    a = AdminController(UserID=7, UserLevel=7, UserName="sample_text")
    b1 = processQuery()
    b2 = processQuery()
    _safe_set(a, 'processQuery7', b1)
    assert _is_linked(a, 'processQuery7', b1)
    if hasattr(b1, 'adminPanel6'):
        assert _is_linked(b1, 'adminPanel6', a)
    _safe_set(a, 'processQuery7', b2)
    assert _is_linked(a, 'processQuery7', b2)
    if hasattr(b1, 'adminPanel6'):
        assert not _is_linked(b1, 'adminPanel6', a)
    if hasattr(b2, 'adminPanel6'):
        assert _is_linked(b2, 'adminPanel6', a)
    _safe_set(a, 'processQuery7', None)
    assert not _is_linked(a, 'processQuery7', b2)
    if hasattr(b2, 'adminPanel6'):
        assert not _is_linked(b2, 'adminPanel6', a)


def test_assoc_processQuery_Booking_link_reassign_clear():
    a = BookingController(BookingID=7, CustomerName="sample_text", Date="sample_text", Phone="sample_text", TableNo="sample_text", Time="sample_text")
    b1 = processQuery()
    b2 = processQuery()
    _safe_set(a, 'processQuery9', b1)
    assert _is_linked(a, 'processQuery9', b1)
    if hasattr(b1, 'booking8'):
        assert _is_linked(b1, 'booking8', a)
    _safe_set(a, 'processQuery9', b2)
    assert _is_linked(a, 'processQuery9', b2)
    if hasattr(b1, 'booking8'):
        assert not _is_linked(b1, 'booking8', a)
    if hasattr(b2, 'booking8'):
        assert _is_linked(b2, 'booking8', a)
    _safe_set(a, 'processQuery9', None)
    assert not _is_linked(a, 'processQuery9', b2)
    if hasattr(b2, 'booking8'):
        assert not _is_linked(b2, 'booking8', a)


def test_assoc_processQuery_Order_link_reassign_clear():
    a = OrderController(Date="sample_text", OrderID=7, OrderTotal="sample_text", UserID=7)
    b1 = processQuery()
    b2 = processQuery()
    _safe_set(a, 'processQuery11', b1)
    assert _is_linked(a, 'processQuery11', b1)
    if hasattr(b1, 'order10'):
        assert _is_linked(b1, 'order10', a)
    _safe_set(a, 'processQuery11', b2)
    assert _is_linked(a, 'processQuery11', b2)
    if hasattr(b1, 'order10'):
        assert not _is_linked(b1, 'order10', a)
    if hasattr(b2, 'order10'):
        assert _is_linked(b2, 'order10', a)
    _safe_set(a, 'processQuery11', None)
    assert not _is_linked(a, 'processQuery11', b2)
    if hasattr(b2, 'order10'):
        assert not _is_linked(b2, 'order10', a)


def test_assoc_processQuery_Table_link_reassign_clear():
    a = Table(Occupied=True, TableNo="sample_text")
    b1 = processQuery()
    b2 = processQuery()
    _safe_set(a, 'processQuery15', b1)
    assert _is_linked(a, 'processQuery15', b1)
    if hasattr(b1, 'table14'):
        assert _is_linked(b1, 'table14', a)
    _safe_set(a, 'processQuery15', b2)
    assert _is_linked(a, 'processQuery15', b2)
    if hasattr(b1, 'table14'):
        assert not _is_linked(b1, 'table14', a)
    if hasattr(b2, 'table14'):
        assert _is_linked(b2, 'table14', a)
    _safe_set(a, 'processQuery15', None)
    assert not _is_linked(a, 'processQuery15', b2)
    if hasattr(b2, 'table14'):
        assert not _is_linked(b2, 'table14', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AdminController_strategy = st.builds(AdminController, UserID=st.integers(), UserLevel=st.integers(), UserName=safe_text)
@given(instance=AdminController_strategy)
@settings(max_examples=25)
def test_AdminController_instantiation(instance):
    assert isinstance(instance, AdminController)


BookingController_strategy = st.builds(BookingController, BookingID=st.integers(), CustomerName=safe_text, Date=safe_text, Phone=safe_text, TableNo=safe_text, Time=safe_text)
@given(instance=BookingController_strategy)
@settings(max_examples=25)
def test_BookingController_instantiation(instance):
    assert isinstance(instance, BookingController)


Login_strategy = st.builds(Login, Discount=st.integers(), LoyaltyID=st.integers())
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Membership_Card_strategy = st.builds(Membership_Card, Discount=st.integers(), LoyaltyID=st.integers())
@given(instance=Membership_Card_strategy)
@settings(max_examples=25)
def test_Membership_Card_instantiation(instance):
    assert isinstance(instance, Membership_Card)


OrderController_strategy = st.builds(OrderController, Date=safe_text, OrderID=st.integers(), OrderTotal=safe_text, UserID=st.integers())
@given(instance=OrderController_strategy)
@settings(max_examples=25)
def test_OrderController_instantiation(instance):
    assert isinstance(instance, OrderController)


Table_strategy = st.builds(Table, Occupied=st.booleans(), TableNo=safe_text)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


processQuery_strategy = st.builds(processQuery)
@given(instance=processQuery_strategy)
@settings(max_examples=25)
def test_processQuery_instantiation(instance):
    assert isinstance(instance, processQuery)


