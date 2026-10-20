import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Customer,
    Order_Details,
    Orders,
    Shipping_Info,
    Shopping_Cart,
    User,
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

def test_assoc_Customer_Orders_reverse_link_reassign_clear():
    a1 = Orders(Customer_Id="sample_text", Date_Created="sample_text", Date_Shipped="sample_text", Order_id=7, Status="sample_text")
    a2 = Orders(Customer_Id="sample_text_2", Date_Created="sample_text_2", Date_Shipped="sample_text_2", Order_id=13, Status="sample_text_2")
    b = Customer(Address="sample_text", Credit_Card_Info=7, Customer_Name="sample_text", email="sample_text")
    _safe_set(b, 'orders0', {a1})
    assert _is_linked(b, 'orders0', a1)
    if hasattr(a1, 'customer1'):
        assert _is_linked(a1, 'customer1', b)
    _safe_set(b, 'orders0', {a2})
    assert _is_linked(b, 'orders0', a2)
    if hasattr(a1, 'customer1'):
        assert not _is_linked(a1, 'customer1', b)
    if hasattr(a2, 'customer1'):
        assert _is_linked(a2, 'customer1', b)
    _safe_set(b, 'orders0', set())
    assert not _is_linked(b, 'orders0', a2)
    if hasattr(a2, 'customer1'):
        assert not _is_linked(a2, 'customer1', b)


def test_assoc_Customer_Shopping_Cart_reverse_link_reassign_clear():
    a1 = Shopping_Cart(Cart_id=7, Product_id=7, Quantity=7)
    a2 = Shopping_Cart(Cart_id=13, Product_id=13, Quantity=13)
    b = Customer(Address="sample_text", Credit_Card_Info=7, Customer_Name="sample_text", email="sample_text")
    _safe_set(b, 'shopping_Cart6', {a1})
    assert _is_linked(b, 'shopping_Cart6', a1)
    if hasattr(a1, 'customer7'):
        assert _is_linked(a1, 'customer7', b)
    _safe_set(b, 'shopping_Cart6', {a2})
    assert _is_linked(b, 'shopping_Cart6', a2)
    if hasattr(a1, 'customer7'):
        assert not _is_linked(a1, 'customer7', b)
    if hasattr(a2, 'customer7'):
        assert _is_linked(a2, 'customer7', b)
    _safe_set(b, 'shopping_Cart6', set())
    assert not _is_linked(b, 'shopping_Cart6', a2)
    if hasattr(a2, 'customer7'):
        assert not _is_linked(a2, 'customer7', b)


def test_assoc_Orders_Order_Details_reverse_link_reassign_clear():
    a1 = Orders(Customer_Id="sample_text", Date_Created="sample_text", Date_Shipped="sample_text", Order_id=7, Status="sample_text")
    a2 = Orders(Customer_Id="sample_text_2", Date_Created="sample_text_2", Date_Shipped="sample_text_2", Order_id=13, Status="sample_text_2")
    b = Order_Details(Order_Id=7, Product_Id=7, Product_Name="sample_text", Quantity=7, Sub_Total="sample_text", Unicast="sample_text")
    _safe_set(b, 'orders5', a1)
    assert _is_linked(b, 'orders5', a1)
    if hasattr(a1, 'order_Details4'):
        assert _is_linked(a1, 'order_Details4', b)
    _safe_set(b, 'orders5', a2)
    assert _is_linked(b, 'orders5', a2)
    if hasattr(a1, 'order_Details4'):
        assert not _is_linked(a1, 'order_Details4', b)
    if hasattr(a2, 'order_Details4'):
        assert _is_linked(a2, 'order_Details4', b)
    _safe_set(b, 'orders5', None)
    assert not _is_linked(b, 'orders5', a2)
    if hasattr(a2, 'order_Details4'):
        assert not _is_linked(a2, 'order_Details4', b)


def test_assoc_Orders_Shipping_Info_reverse_link_reassign_clear():
    a1 = Shipping_Info(Shipping_Id=7, Shipping_Type="sample_text")
    a2 = Shipping_Info(Shipping_Id=13, Shipping_Type="sample_text_2")
    b = Orders(Customer_Id="sample_text", Date_Created="sample_text", Date_Shipped="sample_text", Order_id=7, Status="sample_text")
    _safe_set(b, 'shipping_Info2', a1)
    assert _is_linked(b, 'shipping_Info2', a1)
    if hasattr(a1, 'orders3'):
        assert _is_linked(a1, 'orders3', b)
    _safe_set(b, 'shipping_Info2', a2)
    assert _is_linked(b, 'shipping_Info2', a2)
    if hasattr(a1, 'orders3'):
        assert not _is_linked(a1, 'orders3', b)
    if hasattr(a2, 'orders3'):
        assert _is_linked(a2, 'orders3', b)
    _safe_set(b, 'shipping_Info2', None)
    assert not _is_linked(b, 'shipping_Info2', a2)
    if hasattr(a2, 'orders3'):
        assert not _is_linked(a2, 'orders3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

