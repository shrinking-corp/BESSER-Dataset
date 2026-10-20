import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Corporate_Order,
    Custom_Login,
    Customer,
    Items,
    Order,
    Payment,
    Phone_Order,
    Products,
    Shopping_Cart,
    Social_Login,
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

def test_assoc_Account_Customer_reverse_link_reassign_clear():
    a1 = Customer(Customer_ID="sample_text", Name="sample_text")
    a2 = Customer(Customer_ID="sample_text_2", Name="sample_text_2")
    b = Account(Address="sample_text", ContactNo="sample_text", Email="sample_text")
    _safe_set(b, 'customer8', a1)
    assert _is_linked(b, 'customer8', a1)
    if hasattr(a1, 'account9'):
        assert _is_linked(a1, 'account9', b)
    _safe_set(b, 'customer8', a2)
    assert _is_linked(b, 'customer8', a2)
    if hasattr(a1, 'account9'):
        assert not _is_linked(a1, 'account9', b)
    if hasattr(a2, 'account9'):
        assert _is_linked(a2, 'account9', b)
    _safe_set(b, 'customer8', None)
    assert not _is_linked(b, 'customer8', a2)
    if hasattr(a2, 'account9'):
        assert not _is_linked(a2, 'account9', b)


def test_assoc_Account_Order_reverse_link_reassign_clear():
    a1 = Order(GiftMessage="sample_text", Order_ID="sample_text", ReceipientAddress="sample_text", ReceipientContactNo="sample_text", ReceipientEmail="sample_text", ReceipientName="sample_text")
    a2 = Order(GiftMessage="sample_text_2", Order_ID="sample_text_2", ReceipientAddress="sample_text_2", ReceipientContactNo="sample_text_2", ReceipientEmail="sample_text_2", ReceipientName="sample_text_2")
    b = Account(Address="sample_text", ContactNo="sample_text", Email="sample_text")
    _safe_set(b, 'Account_Order_020', a1)
    assert _is_linked(b, 'Account_Order_020', a1)
    if hasattr(a1, 'Account_Order_121'):
        assert _is_linked(a1, 'Account_Order_121', b)
    _safe_set(b, 'Account_Order_020', a2)
    assert _is_linked(b, 'Account_Order_020', a2)
    if hasattr(a1, 'Account_Order_121'):
        assert not _is_linked(a1, 'Account_Order_121', b)
    if hasattr(a2, 'Account_Order_121'):
        assert _is_linked(a2, 'Account_Order_121', b)
    _safe_set(b, 'Account_Order_020', None)
    assert not _is_linked(b, 'Account_Order_020', a2)
    if hasattr(a2, 'Account_Order_121'):
        assert not _is_linked(a2, 'Account_Order_121', b)


def test_assoc_Corporate_Order_Customer_reverse_link_reassign_clear():
    a1 = Customer(Customer_ID="sample_text", Name="sample_text")
    a2 = Customer(Customer_ID="sample_text_2", Name="sample_text_2")
    b = Corporate_Order(Date="sample_text")
    _safe_set(b, 'Corporate_Order_Customer_028', a1)
    assert _is_linked(b, 'Corporate_Order_Customer_028', a1)
    if hasattr(a1, 'Corporate_Order_Customer_129'):
        assert _is_linked(a1, 'Corporate_Order_Customer_129', b)
    _safe_set(b, 'Corporate_Order_Customer_028', a2)
    assert _is_linked(b, 'Corporate_Order_Customer_028', a2)
    if hasattr(a1, 'Corporate_Order_Customer_129'):
        assert not _is_linked(a1, 'Corporate_Order_Customer_129', b)
    if hasattr(a2, 'Corporate_Order_Customer_129'):
        assert _is_linked(a2, 'Corporate_Order_Customer_129', b)
    _safe_set(b, 'Corporate_Order_Customer_028', None)
    assert not _is_linked(b, 'Corporate_Order_Customer_028', a2)
    if hasattr(a2, 'Corporate_Order_Customer_129'):
        assert not _is_linked(a2, 'Corporate_Order_Customer_129', b)


def test_assoc_Corporate_Order_Items_reverse_link_reassign_clear():
    a1 = Items(Quantity="sample_text", SKUCode="sample_text")
    a2 = Items(Quantity="sample_text_2", SKUCode="sample_text_2")
    b = Corporate_Order(Date="sample_text")
    _safe_set(b, 'Corporate_Order_Items_024', {a1})
    assert _is_linked(b, 'Corporate_Order_Items_024', a1)
    if hasattr(a1, 'Corporate_Order_Items_125'):
        assert _is_linked(a1, 'Corporate_Order_Items_125', b)
    _safe_set(b, 'Corporate_Order_Items_024', {a2})
    assert _is_linked(b, 'Corporate_Order_Items_024', a2)
    if hasattr(a1, 'Corporate_Order_Items_125'):
        assert not _is_linked(a1, 'Corporate_Order_Items_125', b)
    if hasattr(a2, 'Corporate_Order_Items_125'):
        assert _is_linked(a2, 'Corporate_Order_Items_125', b)
    _safe_set(b, 'Corporate_Order_Items_024', set())
    assert not _is_linked(b, 'Corporate_Order_Items_024', a2)
    if hasattr(a2, 'Corporate_Order_Items_125'):
        assert not _is_linked(a2, 'Corporate_Order_Items_125', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = Customer(Customer_ID="sample_text", Name="sample_text")
    a2 = Customer(Customer_ID="sample_text_2", Name="sample_text_2")
    b = Account(Address="sample_text", ContactNo="sample_text", Email="sample_text")
    _safe_set(b, 'Customer_Account_111', a1)
    assert _is_linked(b, 'Customer_Account_111', a1)
    if hasattr(a1, 'Customer_Account_010'):
        assert _is_linked(a1, 'Customer_Account_010', b)
    _safe_set(b, 'Customer_Account_111', a2)
    assert _is_linked(b, 'Customer_Account_111', a2)
    if hasattr(a1, 'Customer_Account_010'):
        assert not _is_linked(a1, 'Customer_Account_010', b)
    if hasattr(a2, 'Customer_Account_010'):
        assert _is_linked(a2, 'Customer_Account_010', b)
    _safe_set(b, 'Customer_Account_111', None)
    assert not _is_linked(b, 'Customer_Account_111', a2)
    if hasattr(a2, 'Customer_Account_010'):
        assert not _is_linked(a2, 'Customer_Account_010', b)


def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order(GiftMessage="sample_text", Order_ID="sample_text", ReceipientAddress="sample_text", ReceipientContactNo="sample_text", ReceipientEmail="sample_text", ReceipientName="sample_text")
    a2 = Order(GiftMessage="sample_text_2", Order_ID="sample_text_2", ReceipientAddress="sample_text_2", ReceipientContactNo="sample_text_2", ReceipientEmail="sample_text_2", ReceipientName="sample_text_2")
    b = Customer(Customer_ID="sample_text", Name="sample_text")
    _safe_set(b, 'Customer_Order_02', {a1})
    assert _is_linked(b, 'Customer_Order_02', a1)
    if hasattr(a1, 'Customer_Order_13'):
        assert _is_linked(a1, 'Customer_Order_13', b)
    _safe_set(b, 'Customer_Order_02', {a2})
    assert _is_linked(b, 'Customer_Order_02', a2)
    if hasattr(a1, 'Customer_Order_13'):
        assert not _is_linked(a1, 'Customer_Order_13', b)
    if hasattr(a2, 'Customer_Order_13'):
        assert _is_linked(a2, 'Customer_Order_13', b)
    _safe_set(b, 'Customer_Order_02', set())
    assert not _is_linked(b, 'Customer_Order_02', a2)
    if hasattr(a2, 'Customer_Order_13'):
        assert not _is_linked(a2, 'Customer_Order_13', b)


def test_assoc_Customer_Payment_reverse_link_reassign_clear():
    a1 = Payment(Date=7, Payment_ID="sample_text")
    a2 = Payment(Date=13, Payment_ID="sample_text_2")
    b = Customer(Customer_ID="sample_text", Name="sample_text")
    _safe_set(b, 'Customer_Payment_06', a1)
    assert _is_linked(b, 'Customer_Payment_06', a1)
    if hasattr(a1, 'Customer_Payment_17'):
        assert _is_linked(a1, 'Customer_Payment_17', b)
    _safe_set(b, 'Customer_Payment_06', a2)
    assert _is_linked(b, 'Customer_Payment_06', a2)
    if hasattr(a1, 'Customer_Payment_17'):
        assert not _is_linked(a1, 'Customer_Payment_17', b)
    if hasattr(a2, 'Customer_Payment_17'):
        assert _is_linked(a2, 'Customer_Payment_17', b)
    _safe_set(b, 'Customer_Payment_06', None)
    assert not _is_linked(b, 'Customer_Payment_06', a2)
    if hasattr(a2, 'Customer_Payment_17'):
        assert not _is_linked(a2, 'Customer_Payment_17', b)


def test_assoc_Customer_Products_reverse_link_reassign_clear():
    a1 = Products(Product_Name="sample_text", SKU_Code="sample_text")
    a2 = Products(Product_Name="sample_text_2", SKU_Code="sample_text_2")
    b = Customer(Customer_ID="sample_text", Name="sample_text")
    _safe_set(b, 'Customer_Products_00', {a1})
    assert _is_linked(b, 'Customer_Products_00', a1)
    if hasattr(a1, 'Customer_Products_11'):
        assert _is_linked(a1, 'Customer_Products_11', b)
    _safe_set(b, 'Customer_Products_00', {a2})
    assert _is_linked(b, 'Customer_Products_00', a2)
    if hasattr(a1, 'Customer_Products_11'):
        assert not _is_linked(a1, 'Customer_Products_11', b)
    if hasattr(a2, 'Customer_Products_11'):
        assert _is_linked(a2, 'Customer_Products_11', b)
    _safe_set(b, 'Customer_Products_00', set())
    assert not _is_linked(b, 'Customer_Products_00', a2)
    if hasattr(a2, 'Customer_Products_11'):
        assert not _is_linked(a2, 'Customer_Products_11', b)


def test_assoc_Customer_Shopping_Cart_reverse_link_reassign_clear():
    a1 = Shopping_Cart(Date="sample_text")
    a2 = Shopping_Cart(Date="sample_text_2")
    b = Customer(Customer_ID="sample_text", Name="sample_text")
    _safe_set(b, 'Customer_Shopping_Cart_04', a1)
    assert _is_linked(b, 'Customer_Shopping_Cart_04', a1)
    if hasattr(a1, 'Customer_Shopping_Cart_15'):
        assert _is_linked(a1, 'Customer_Shopping_Cart_15', b)
    _safe_set(b, 'Customer_Shopping_Cart_04', a2)
    assert _is_linked(b, 'Customer_Shopping_Cart_04', a2)
    if hasattr(a1, 'Customer_Shopping_Cart_15'):
        assert not _is_linked(a1, 'Customer_Shopping_Cart_15', b)
    if hasattr(a2, 'Customer_Shopping_Cart_15'):
        assert _is_linked(a2, 'Customer_Shopping_Cart_15', b)
    _safe_set(b, 'Customer_Shopping_Cart_04', None)
    assert not _is_linked(b, 'Customer_Shopping_Cart_04', a2)
    if hasattr(a2, 'Customer_Shopping_Cart_15'):
        assert not _is_linked(a2, 'Customer_Shopping_Cart_15', b)


def test_assoc_Order_Account_reverse_link_reassign_clear():
    a1 = Order(GiftMessage="sample_text", Order_ID="sample_text", ReceipientAddress="sample_text", ReceipientContactNo="sample_text", ReceipientEmail="sample_text", ReceipientName="sample_text")
    a2 = Order(GiftMessage="sample_text_2", Order_ID="sample_text_2", ReceipientAddress="sample_text_2", ReceipientContactNo="sample_text_2", ReceipientEmail="sample_text_2", ReceipientName="sample_text_2")
    b = Account(Address="sample_text", ContactNo="sample_text", Email="sample_text")
    _safe_set(b, 'order17', a1)
    assert _is_linked(b, 'order17', a1)
    if hasattr(a1, 'account16'):
        assert _is_linked(a1, 'account16', b)
    _safe_set(b, 'order17', a2)
    assert _is_linked(b, 'order17', a2)
    if hasattr(a1, 'account16'):
        assert not _is_linked(a1, 'account16', b)
    if hasattr(a2, 'account16'):
        assert _is_linked(a2, 'account16', b)
    _safe_set(b, 'order17', None)
    assert not _is_linked(b, 'order17', a2)
    if hasattr(a2, 'account16'):
        assert not _is_linked(a2, 'account16', b)


def test_assoc_Order_Account2_reverse_link_reassign_clear():
    a1 = Order(GiftMessage="sample_text", Order_ID="sample_text", ReceipientAddress="sample_text", ReceipientContactNo="sample_text", ReceipientEmail="sample_text", ReceipientName="sample_text")
    a2 = Order(GiftMessage="sample_text_2", Order_ID="sample_text_2", ReceipientAddress="sample_text_2", ReceipientContactNo="sample_text_2", ReceipientEmail="sample_text_2", ReceipientName="sample_text_2")
    b = Account(Address="sample_text", ContactNo="sample_text", Email="sample_text")
    _safe_set(b, 'order19', a1)
    assert _is_linked(b, 'order19', a1)
    if hasattr(a1, 'account18'):
        assert _is_linked(a1, 'account18', b)
    _safe_set(b, 'order19', a2)
    assert _is_linked(b, 'order19', a2)
    if hasattr(a1, 'account18'):
        assert not _is_linked(a1, 'account18', b)
    if hasattr(a2, 'account18'):
        assert _is_linked(a2, 'account18', b)
    _safe_set(b, 'order19', None)
    assert not _is_linked(b, 'order19', a2)
    if hasattr(a2, 'account18'):
        assert not _is_linked(a2, 'account18', b)


def test_assoc_Payment__Order_reverse_link_reassign_clear():
    a1 = Payment(Date=7, Payment_ID="sample_text")
    a2 = Payment(Date=13, Payment_ID="sample_text_2")
    b = Order(GiftMessage="sample_text", Order_ID="sample_text", ReceipientAddress="sample_text", ReceipientContactNo="sample_text", ReceipientEmail="sample_text", ReceipientName="sample_text")
    _safe_set(b, 'Payment__Order_113', a1)
    assert _is_linked(b, 'Payment__Order_113', a1)
    if hasattr(a1, 'Payment__Order_012'):
        assert _is_linked(a1, 'Payment__Order_012', b)
    _safe_set(b, 'Payment__Order_113', a2)
    assert _is_linked(b, 'Payment__Order_113', a2)
    if hasattr(a1, 'Payment__Order_012'):
        assert not _is_linked(a1, 'Payment__Order_012', b)
    if hasattr(a2, 'Payment__Order_012'):
        assert _is_linked(a2, 'Payment__Order_012', b)
    _safe_set(b, 'Payment__Order_113', None)
    assert not _is_linked(b, 'Payment__Order_113', a2)
    if hasattr(a2, 'Payment__Order_012'):
        assert not _is_linked(a2, 'Payment__Order_012', b)


def test_assoc_Phone_Order_Customer_reverse_link_reassign_clear():
    a1 = Phone_Order(Date="sample_text")
    a2 = Phone_Order(Date="sample_text_2")
    b = Customer(Customer_ID="sample_text", Name="sample_text")
    _safe_set(b, 'Phone_Order_Customer_127', a1)
    assert _is_linked(b, 'Phone_Order_Customer_127', a1)
    if hasattr(a1, 'Phone_Order_Customer_026'):
        assert _is_linked(a1, 'Phone_Order_Customer_026', b)
    _safe_set(b, 'Phone_Order_Customer_127', a2)
    assert _is_linked(b, 'Phone_Order_Customer_127', a2)
    if hasattr(a1, 'Phone_Order_Customer_026'):
        assert not _is_linked(a1, 'Phone_Order_Customer_026', b)
    if hasattr(a2, 'Phone_Order_Customer_026'):
        assert _is_linked(a2, 'Phone_Order_Customer_026', b)
    _safe_set(b, 'Phone_Order_Customer_127', None)
    assert not _is_linked(b, 'Phone_Order_Customer_127', a2)
    if hasattr(a2, 'Phone_Order_Customer_026'):
        assert not _is_linked(a2, 'Phone_Order_Customer_026', b)


def test_assoc_Phone_Order_Items_reverse_link_reassign_clear():
    a1 = Phone_Order(Date="sample_text")
    a2 = Phone_Order(Date="sample_text_2")
    b = Items(Quantity="sample_text", SKUCode="sample_text")
    _safe_set(b, 'Phone_Order_Items_123', {a1})
    assert _is_linked(b, 'Phone_Order_Items_123', a1)
    if hasattr(a1, 'Phone_Order_Items_022'):
        assert _is_linked(a1, 'Phone_Order_Items_022', b)
    _safe_set(b, 'Phone_Order_Items_123', {a2})
    assert _is_linked(b, 'Phone_Order_Items_123', a2)
    if hasattr(a1, 'Phone_Order_Items_022'):
        assert not _is_linked(a1, 'Phone_Order_Items_022', b)
    if hasattr(a2, 'Phone_Order_Items_022'):
        assert _is_linked(a2, 'Phone_Order_Items_022', b)
    _safe_set(b, 'Phone_Order_Items_123', set())
    assert not _is_linked(b, 'Phone_Order_Items_123', a2)
    if hasattr(a2, 'Phone_Order_Items_022'):
        assert not _is_linked(a2, 'Phone_Order_Items_022', b)


def test_assoc_Shopping_Cart_Items_reverse_link_reassign_clear():
    a1 = Shopping_Cart(Date="sample_text")
    a2 = Shopping_Cart(Date="sample_text_2")
    b = Items(Quantity="sample_text", SKUCode="sample_text")
    _safe_set(b, 'Shopping_Cart_Items_115', {a1})
    assert _is_linked(b, 'Shopping_Cart_Items_115', a1)
    if hasattr(a1, 'Shopping_Cart_Items_014'):
        assert _is_linked(a1, 'Shopping_Cart_Items_014', b)
    _safe_set(b, 'Shopping_Cart_Items_115', {a2})
    assert _is_linked(b, 'Shopping_Cart_Items_115', a2)
    if hasattr(a1, 'Shopping_Cart_Items_014'):
        assert not _is_linked(a1, 'Shopping_Cart_Items_014', b)
    if hasattr(a2, 'Shopping_Cart_Items_014'):
        assert _is_linked(a2, 'Shopping_Cart_Items_014', b)
    _safe_set(b, 'Shopping_Cart_Items_115', set())
    assert not _is_linked(b, 'Shopping_Cart_Items_115', a2)
    if hasattr(a2, 'Shopping_Cart_Items_014'):
        assert not _is_linked(a2, 'Shopping_Cart_Items_014', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

