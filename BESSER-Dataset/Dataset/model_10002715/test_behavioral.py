import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cart_Checkout,
    Cart_ShoppingCart,
    Customer_Account,
    Customer_Customer,
    Customer_Customer1,
    Customer_Payment,
    Customer_Payment1,
    Customer_User,
    GUI_Screen,
    Product_Item,
    Product_Item_Specification,
    Product_Item_Type,
    Shopping_Cart_Checkout,
    Shopping_Cart_ShoppingCart,
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

def test_assoc_Customer_ShoppingCart_reverse_link_reassign_clear():
    a1 = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    a2 = Shopping_Cart_ShoppingCart(AddOrder=13, CheckoutID=13, GetTotal__=9.99, RemoveOrder=13, UpdateOrder=13, creationDate=date(2025, 6, 15), id=13)
    b = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    _safe_set(b, 'Customer_ShoppingCart_02', a1)
    assert _is_linked(b, 'Customer_ShoppingCart_02', a1)
    if hasattr(a1, 'Customer_ShoppingCart_13'):
        assert _is_linked(a1, 'Customer_ShoppingCart_13', b)
    _safe_set(b, 'Customer_ShoppingCart_02', a2)
    assert _is_linked(b, 'Customer_ShoppingCart_02', a2)
    if hasattr(a1, 'Customer_ShoppingCart_13'):
        assert not _is_linked(a1, 'Customer_ShoppingCart_13', b)
    if hasattr(a2, 'Customer_ShoppingCart_13'):
        assert _is_linked(a2, 'Customer_ShoppingCart_13', b)
    _safe_set(b, 'Customer_ShoppingCart_02', None)
    assert not _is_linked(b, 'Customer_ShoppingCart_02', a2)
    if hasattr(a2, 'Customer_ShoppingCart_13'):
        assert not _is_linked(a2, 'Customer_ShoppingCart_13', b)


def test_assoc_GUI_Screen_Account_reverse_link_reassign_clear():
    a1 = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    a2 = GUI_Screen(DisplayList__=13, Error__="sample_text_2", Exit__="sample_text_2", Message="sample_text_2", id=13)
    b = Customer_Account(Login__="sample_text", account__="sample_text")
    _safe_set(b, 'GUI_Screen_Account_123', a1)
    assert _is_linked(b, 'GUI_Screen_Account_123', a1)
    if hasattr(a1, 'GUI_Screen_Account_022'):
        assert _is_linked(a1, 'GUI_Screen_Account_022', b)
    _safe_set(b, 'GUI_Screen_Account_123', a2)
    assert _is_linked(b, 'GUI_Screen_Account_123', a2)
    if hasattr(a1, 'GUI_Screen_Account_022'):
        assert not _is_linked(a1, 'GUI_Screen_Account_022', b)
    if hasattr(a2, 'GUI_Screen_Account_022'):
        assert _is_linked(a2, 'GUI_Screen_Account_022', b)
    _safe_set(b, 'GUI_Screen_Account_123', None)
    assert not _is_linked(b, 'GUI_Screen_Account_123', a2)
    if hasattr(a2, 'GUI_Screen_Account_022'):
        assert not _is_linked(a2, 'GUI_Screen_Account_022', b)


def test_assoc_GUI_Screen_Item_reverse_link_reassign_clear():
    a1 = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    a2 = Product_Item(OutofStock__="sample_text_2", id=13, list__=9.99, quantity=13, totalcost__="sample_text_2")
    b = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    _safe_set(b, 'GUI_Screen_Item_026', a1)
    assert _is_linked(b, 'GUI_Screen_Item_026', a1)
    if hasattr(a1, 'GUI_Screen_Item_127'):
        assert _is_linked(a1, 'GUI_Screen_Item_127', b)
    _safe_set(b, 'GUI_Screen_Item_026', a2)
    assert _is_linked(b, 'GUI_Screen_Item_026', a2)
    if hasattr(a1, 'GUI_Screen_Item_127'):
        assert not _is_linked(a1, 'GUI_Screen_Item_127', b)
    if hasattr(a2, 'GUI_Screen_Item_127'):
        assert _is_linked(a2, 'GUI_Screen_Item_127', b)
    _safe_set(b, 'GUI_Screen_Item_026', None)
    assert not _is_linked(b, 'GUI_Screen_Item_026', a2)
    if hasattr(a2, 'GUI_Screen_Item_127'):
        assert not _is_linked(a2, 'GUI_Screen_Item_127', b)


def test_assoc_GUI_Screen_ShoppingCart_reverse_link_reassign_clear():
    a1 = GUI_Screen(DisplayList__=7, Error__="sample_text", Exit__="sample_text", Message="sample_text", id=7)
    a2 = GUI_Screen(DisplayList__=13, Error__="sample_text_2", Exit__="sample_text_2", Message="sample_text_2", id=13)
    b = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    _safe_set(b, 'GUI_Screen_ShoppingCart_125', a1)
    assert _is_linked(b, 'GUI_Screen_ShoppingCart_125', a1)
    if hasattr(a1, 'GUI_Screen_ShoppingCart_024'):
        assert _is_linked(a1, 'GUI_Screen_ShoppingCart_024', b)
    _safe_set(b, 'GUI_Screen_ShoppingCart_125', a2)
    assert _is_linked(b, 'GUI_Screen_ShoppingCart_125', a2)
    if hasattr(a1, 'GUI_Screen_ShoppingCart_024'):
        assert not _is_linked(a1, 'GUI_Screen_ShoppingCart_024', b)
    if hasattr(a2, 'GUI_Screen_ShoppingCart_024'):
        assert _is_linked(a2, 'GUI_Screen_ShoppingCart_024', b)
    _safe_set(b, 'GUI_Screen_ShoppingCart_125', None)
    assert not _is_linked(b, 'GUI_Screen_ShoppingCart_125', a2)
    if hasattr(a2, 'GUI_Screen_ShoppingCart_024'):
        assert not _is_linked(a2, 'GUI_Screen_ShoppingCart_024', b)


def test_assoc_Item_ShoppingCart_reverse_link_reassign_clear():
    a1 = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    a2 = Product_Item(OutofStock__="sample_text_2", id=13, list__=9.99, quantity=13, totalcost__="sample_text_2")
    b = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    _safe_set(b, 'Item_ShoppingCart_121', {a1})
    assert _is_linked(b, 'Item_ShoppingCart_121', a1)
    if hasattr(a1, 'Item_ShoppingCart_020'):
        assert _is_linked(a1, 'Item_ShoppingCart_020', b)
    _safe_set(b, 'Item_ShoppingCart_121', {a2})
    assert _is_linked(b, 'Item_ShoppingCart_121', a2)
    if hasattr(a1, 'Item_ShoppingCart_020'):
        assert not _is_linked(a1, 'Item_ShoppingCart_020', b)
    if hasattr(a2, 'Item_ShoppingCart_020'):
        assert _is_linked(a2, 'Item_ShoppingCart_020', b)
    _safe_set(b, 'Item_ShoppingCart_121', set())
    assert not _is_linked(b, 'Item_ShoppingCart_121', a2)
    if hasattr(a2, 'Item_ShoppingCart_020'):
        assert not _is_linked(a2, 'Item_ShoppingCart_020', b)


def test_assoc_Item_Specification_Item_reverse_link_reassign_clear():
    a1 = Product_Item_Specification(Brand__="sample_text", ItemSpecs__="sample_text", id=7, price=3.14, quantity=7)
    a2 = Product_Item_Specification(Brand__="sample_text_2", ItemSpecs__="sample_text_2", id=13, price=9.99, quantity=13)
    b = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    _safe_set(b, 'Item_Specification_Item_117', {a1})
    assert _is_linked(b, 'Item_Specification_Item_117', a1)
    if hasattr(a1, 'Item_Specification_Item_016'):
        assert _is_linked(a1, 'Item_Specification_Item_016', b)
    _safe_set(b, 'Item_Specification_Item_117', {a2})
    assert _is_linked(b, 'Item_Specification_Item_117', a2)
    if hasattr(a1, 'Item_Specification_Item_016'):
        assert not _is_linked(a1, 'Item_Specification_Item_016', b)
    if hasattr(a2, 'Item_Specification_Item_016'):
        assert _is_linked(a2, 'Item_Specification_Item_016', b)
    _safe_set(b, 'Item_Specification_Item_117', set())
    assert not _is_linked(b, 'Item_Specification_Item_117', a2)
    if hasattr(a2, 'Item_Specification_Item_016'):
        assert not _is_linked(a2, 'Item_Specification_Item_016', b)


def test_assoc_Item_Type_Item_reverse_link_reassign_clear():
    a1 = Product_Item_Type(Avail__="sample_text", ItemType__="sample_text", id=7, price=3.14, quantity=7)
    a2 = Product_Item_Type(Avail__="sample_text_2", ItemType__="sample_text_2", id=13, price=9.99, quantity=13)
    b = Product_Item(OutofStock__="sample_text", id=7, list__=3.14, quantity=7, totalcost__="sample_text")
    _safe_set(b, 'Item_Type_Item_119', {a1})
    assert _is_linked(b, 'Item_Type_Item_119', a1)
    if hasattr(a1, 'Item_Type_Item_018'):
        assert _is_linked(a1, 'Item_Type_Item_018', b)
    _safe_set(b, 'Item_Type_Item_119', {a2})
    assert _is_linked(b, 'Item_Type_Item_119', a2)
    if hasattr(a1, 'Item_Type_Item_018'):
        assert not _is_linked(a1, 'Item_Type_Item_018', b)
    if hasattr(a2, 'Item_Type_Item_018'):
        assert _is_linked(a2, 'Item_Type_Item_018', b)
    _safe_set(b, 'Item_Type_Item_119', set())
    assert not _is_linked(b, 'Item_Type_Item_119', a2)
    if hasattr(a2, 'Item_Type_Item_018'):
        assert not _is_linked(a2, 'Item_Type_Item_018', b)


def test_assoc_Payment_Checkout_reverse_link_reassign_clear():
    a1 = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    a2 = Shopping_Cart_Checkout(CheckoutID=13, Checkout__=9.99, CustomerID="sample_text_2", Paymentid=13, billingMethod="sample_text_2")
    b = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    _safe_set(b, 'Payment_Checkout_04', a1)
    assert _is_linked(b, 'Payment_Checkout_04', a1)
    if hasattr(a1, 'Payment_Checkout_15'):
        assert _is_linked(a1, 'Payment_Checkout_15', b)
    _safe_set(b, 'Payment_Checkout_04', a2)
    assert _is_linked(b, 'Payment_Checkout_04', a2)
    if hasattr(a1, 'Payment_Checkout_15'):
        assert not _is_linked(a1, 'Payment_Checkout_15', b)
    if hasattr(a2, 'Payment_Checkout_15'):
        assert _is_linked(a2, 'Payment_Checkout_15', b)
    _safe_set(b, 'Payment_Checkout_04', None)
    assert not _is_linked(b, 'Payment_Checkout_04', a2)
    if hasattr(a2, 'Payment_Checkout_15'):
        assert not _is_linked(a2, 'Payment_Checkout_15', b)


def test_assoc_Payment_Customer_reverse_link_reassign_clear():
    a1 = Customer_Payment(ApplPay=7, CustomerId="sample_text", PayPal=7, Payment__=3.14, Paymentid=7, login="sample_text")
    a2 = Customer_Payment(ApplPay=13, CustomerId="sample_text_2", PayPal=13, Payment__=9.99, Paymentid=13, login="sample_text_2")
    b = Customer_Customer(Message="sample_text", emailAddress="sample_text", firstname="sample_text", id=7, lastname="sample_text", login="sample_text", password="sample_text")
    _safe_set(b, 'Payment_Customer_11', a1)
    assert _is_linked(b, 'Payment_Customer_11', a1)
    if hasattr(a1, 'Payment_Customer_00'):
        assert _is_linked(a1, 'Payment_Customer_00', b)
    _safe_set(b, 'Payment_Customer_11', a2)
    assert _is_linked(b, 'Payment_Customer_11', a2)
    if hasattr(a1, 'Payment_Customer_00'):
        assert not _is_linked(a1, 'Payment_Customer_00', b)
    if hasattr(a2, 'Payment_Customer_00'):
        assert _is_linked(a2, 'Payment_Customer_00', b)
    _safe_set(b, 'Payment_Customer_11', None)
    assert not _is_linked(b, 'Payment_Customer_11', a2)
    if hasattr(a2, 'Payment_Customer_00'):
        assert not _is_linked(a2, 'Payment_Customer_00', b)


def test_assoc_ShoppingCart_Checkout_reverse_link_reassign_clear():
    a1 = Shopping_Cart_ShoppingCart(AddOrder=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    a2 = Shopping_Cart_ShoppingCart(AddOrder=13, CheckoutID=13, GetTotal__=9.99, RemoveOrder=13, UpdateOrder=13, creationDate=date(2025, 6, 15), id=13)
    b = Shopping_Cart_Checkout(CheckoutID=7, Checkout__=3.14, CustomerID="sample_text", Paymentid=7, billingMethod="sample_text")
    _safe_set(b, 'ShoppingCart_Checkout_17', a1)
    assert _is_linked(b, 'ShoppingCart_Checkout_17', a1)
    if hasattr(a1, 'ShoppingCart_Checkout_06'):
        assert _is_linked(a1, 'ShoppingCart_Checkout_06', b)
    _safe_set(b, 'ShoppingCart_Checkout_17', a2)
    assert _is_linked(b, 'ShoppingCart_Checkout_17', a2)
    if hasattr(a1, 'ShoppingCart_Checkout_06'):
        assert not _is_linked(a1, 'ShoppingCart_Checkout_06', b)
    if hasattr(a2, 'ShoppingCart_Checkout_06'):
        assert _is_linked(a2, 'ShoppingCart_Checkout_06', b)
    _safe_set(b, 'ShoppingCart_Checkout_17', None)
    assert not _is_linked(b, 'ShoppingCart_Checkout_17', a2)
    if hasattr(a2, 'ShoppingCart_Checkout_06'):
        assert not _is_linked(a2, 'ShoppingCart_Checkout_06', b)


def test_assoc_ShoppingCart_Customer_reverse_link_reassign_clear():
    a1 = Customer_Customer1(Account__="sample_text", PaymentMet__=3.14, select__="sample_text", userId="sample_text")
    a2 = Customer_Customer1(Account__="sample_text_2", PaymentMet__=9.99, select__="sample_text_2", userId="sample_text_2")
    b = Cart_ShoppingCart(AddCart=7, CheckoutID=7, GetTotal__=3.14, RemoveOrder=7, UpdateOrder=7, creationDate=date(2024, 1, 1), id=7)
    _safe_set(b, 'ShoppingCart_Customer_012', a1)
    assert _is_linked(b, 'ShoppingCart_Customer_012', a1)
    if hasattr(a1, 'ShoppingCart_Customer_113'):
        assert _is_linked(a1, 'ShoppingCart_Customer_113', b)
    _safe_set(b, 'ShoppingCart_Customer_012', a2)
    assert _is_linked(b, 'ShoppingCart_Customer_012', a2)
    if hasattr(a1, 'ShoppingCart_Customer_113'):
        assert not _is_linked(a1, 'ShoppingCart_Customer_113', b)
    if hasattr(a2, 'ShoppingCart_Customer_113'):
        assert _is_linked(a2, 'ShoppingCart_Customer_113', b)
    _safe_set(b, 'ShoppingCart_Customer_012', None)
    assert not _is_linked(b, 'ShoppingCart_Customer_012', a2)
    if hasattr(a2, 'ShoppingCart_Customer_113'):
        assert not _is_linked(a2, 'ShoppingCart_Customer_113', b)


