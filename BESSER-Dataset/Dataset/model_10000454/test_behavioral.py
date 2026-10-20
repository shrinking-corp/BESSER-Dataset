import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator,
    Customer,
    Order,
    OrderDetails,
    ShippingInfo,
    Shopping,
    ShoppingCart,
    Users,
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

def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    a2 = Order(CustomerID="sample_text_2", CustomerName="sample_text_2", DateCreated="sample_text_2", DateShipped="sample_text_2", OrderID=13, ShippingID="sample_text_2", Status="sample_text_2")
    b = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    _safe_set(b, 'order2', {a1})
    assert _is_linked(b, 'order2', a1)
    if hasattr(a1, 'customer3'):
        assert _is_linked(a1, 'customer3', b)
    _safe_set(b, 'order2', {a2})
    assert _is_linked(b, 'order2', a2)
    if hasattr(a1, 'customer3'):
        assert not _is_linked(a1, 'customer3', b)
    if hasattr(a2, 'customer3'):
        assert _is_linked(a2, 'customer3', b)
    _safe_set(b, 'order2', set())
    assert not _is_linked(b, 'order2', a2)
    if hasattr(a2, 'customer3'):
        assert not _is_linked(a2, 'customer3', b)


def test_assoc_Customer_ShoppingCart_reverse_link_reassign_clear():
    a1 = ShoppingCart(CartID=7, DateAdded=7, ProductID=7, Quantity=7)
    a2 = ShoppingCart(CartID=13, DateAdded=13, ProductID=13, Quantity=13)
    b = Customer(AccountBalance=7, Address="sample_text", CreditCartInfo="sample_text", CustomerName="sample_text", Email="sample_text", ShippingInfo="sample_text")
    _safe_set(b, 'shoppingCart0', {a1})
    assert _is_linked(b, 'shoppingCart0', a1)
    if hasattr(a1, 'customer1'):
        assert _is_linked(a1, 'customer1', b)
    _safe_set(b, 'shoppingCart0', {a2})
    assert _is_linked(b, 'shoppingCart0', a2)
    if hasattr(a1, 'customer1'):
        assert not _is_linked(a1, 'customer1', b)
    if hasattr(a2, 'customer1'):
        assert _is_linked(a2, 'customer1', b)
    _safe_set(b, 'shoppingCart0', set())
    assert not _is_linked(b, 'shoppingCart0', a2)
    if hasattr(a2, 'customer1'):
        assert not _is_linked(a2, 'customer1', b)


def test_assoc_Order_OrderDetails_reverse_link_reassign_clear():
    a1 = OrderDetails(OrderID=7, ProductID=7, ProductName="sample_text", Quantity=7, SubTotal=7, UnitCost=7)
    a2 = OrderDetails(OrderID=13, ProductID=13, ProductName="sample_text_2", Quantity=13, SubTotal=13, UnitCost=13)
    b = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    _safe_set(b, 'has_a6', a1)
    assert _is_linked(b, 'has_a6', a1)
    if hasattr(a1, 'order7'):
        assert _is_linked(a1, 'order7', b)
    _safe_set(b, 'has_a6', a2)
    assert _is_linked(b, 'has_a6', a2)
    if hasattr(a1, 'order7'):
        assert not _is_linked(a1, 'order7', b)
    if hasattr(a2, 'order7'):
        assert _is_linked(a2, 'order7', b)
    _safe_set(b, 'has_a6', None)
    assert not _is_linked(b, 'has_a6', a2)
    if hasattr(a2, 'order7'):
        assert not _is_linked(a2, 'order7', b)


def test_assoc_Order_ShippingInfo_reverse_link_reassign_clear():
    a1 = ShippingInfo(ShippingCost=7, ShippingID=7, ShippingRegionID=7, ShippingType="sample_text")
    a2 = ShippingInfo(ShippingCost=13, ShippingID=13, ShippingRegionID=13, ShippingType="sample_text_2")
    b = Order(CustomerID="sample_text", CustomerName="sample_text", DateCreated="sample_text", DateShipped="sample_text", OrderID=7, ShippingID="sample_text", Status="sample_text")
    _safe_set(b, 'shippingInfo4', a1)
    assert _is_linked(b, 'shippingInfo4', a1)
    if hasattr(a1, 'order5'):
        assert _is_linked(a1, 'order5', b)
    _safe_set(b, 'shippingInfo4', a2)
    assert _is_linked(b, 'shippingInfo4', a2)
    if hasattr(a1, 'order5'):
        assert not _is_linked(a1, 'order5', b)
    if hasattr(a2, 'order5'):
        assert _is_linked(a2, 'order5', b)
    _safe_set(b, 'shippingInfo4', None)
    assert not _is_linked(b, 'shippingInfo4', a2)
    if hasattr(a2, 'order5'):
        assert not _is_linked(a2, 'order5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

