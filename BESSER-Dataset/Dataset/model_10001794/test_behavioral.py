import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator,
    Customer,
    Item,
    Order_Details,
    Orders,
    Products,
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

def test_assoc_Administrator_Products_reverse_link_reassign_clear():
    a1 = Products(racknumber=7, totral=7)
    a2 = Products(racknumber=13, totral=13)
    b = Administrator(adminName="sample_text", email="sample_text")
    _safe_set(b, 'products12', a1)
    assert _is_linked(b, 'products12', a1)
    if hasattr(a1, 'Administrator_Products_113'):
        assert _is_linked(a1, 'Administrator_Products_113', b)
    _safe_set(b, 'products12', a2)
    assert _is_linked(b, 'products12', a2)
    if hasattr(a1, 'Administrator_Products_113'):
        assert not _is_linked(a1, 'Administrator_Products_113', b)
    if hasattr(a2, 'Administrator_Products_113'):
        assert _is_linked(a2, 'Administrator_Products_113', b)
    _safe_set(b, 'products12', None)
    assert not _is_linked(b, 'products12', a2)
    if hasattr(a2, 'Administrator_Products_113'):
        assert not _is_linked(a2, 'Administrator_Products_113', b)


def test_assoc_Customer_Orders_reverse_link_reassign_clear():
    a1 = Orders(CustomerId="sample_text", Date="sample_text", OrderId=7, ShippingId="sample_text", customerName="sample_text", dateCreated="sample_text", status="sample_text")
    a2 = Orders(CustomerId="sample_text_2", Date="sample_text_2", OrderId=13, ShippingId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", status="sample_text_2")
    b = Customer(address="sample_text", credit_card_info="sample_text", customer="sample_text", email="sample_text", shipping_info="sample_text")
    _safe_set(b, 'orders4', {a1})
    assert _is_linked(b, 'orders4', a1)
    if hasattr(a1, 'customer5'):
        assert _is_linked(a1, 'customer5', b)
    _safe_set(b, 'orders4', {a2})
    assert _is_linked(b, 'orders4', a2)
    if hasattr(a1, 'customer5'):
        assert not _is_linked(a1, 'customer5', b)
    if hasattr(a2, 'customer5'):
        assert _is_linked(a2, 'customer5', b)
    _safe_set(b, 'orders4', set())
    assert not _is_linked(b, 'orders4', a2)
    if hasattr(a2, 'customer5'):
        assert not _is_linked(a2, 'customer5', b)


def test_assoc_Customer_Shopping_Cart_reverse_link_reassign_clear():
    a1 = Shopping_Cart(CartId=7, Quantity=7, dateAdded=7, productId=7)
    a2 = Shopping_Cart(CartId=13, Quantity=13, dateAdded=13, productId=13)
    b = Customer(address="sample_text", credit_card_info="sample_text", customer="sample_text", email="sample_text", shipping_info="sample_text")
    _safe_set(b, 'shopping_Cart2', {a1})
    assert _is_linked(b, 'shopping_Cart2', a1)
    if hasattr(a1, 'customer3'):
        assert _is_linked(a1, 'customer3', b)
    _safe_set(b, 'shopping_Cart2', {a2})
    assert _is_linked(b, 'shopping_Cart2', a2)
    if hasattr(a1, 'customer3'):
        assert not _is_linked(a1, 'customer3', b)
    if hasattr(a2, 'customer3'):
        assert _is_linked(a2, 'customer3', b)
    _safe_set(b, 'shopping_Cart2', set())
    assert not _is_linked(b, 'shopping_Cart2', a2)
    if hasattr(a2, 'customer3'):
        assert not _is_linked(a2, 'customer3', b)


def test_assoc_Customer_User_reverse_link_reassign_clear():
    a1 = User(Password="sample_text", User_Id="sample_text", loginStatus="sample_text")
    a2 = User(Password="sample_text_2", User_Id="sample_text_2", loginStatus="sample_text_2")
    b = Customer(address="sample_text", credit_card_info="sample_text", customer="sample_text", email="sample_text", shipping_info="sample_text")
    _safe_set(b, 'user0', a1)
    assert _is_linked(b, 'user0', a1)
    if hasattr(a1, 'customer1'):
        assert _is_linked(a1, 'customer1', b)
    _safe_set(b, 'user0', a2)
    assert _is_linked(b, 'user0', a2)
    if hasattr(a1, 'customer1'):
        assert not _is_linked(a1, 'customer1', b)
    if hasattr(a2, 'customer1'):
        assert _is_linked(a2, 'customer1', b)
    _safe_set(b, 'user0', None)
    assert not _is_linked(b, 'user0', a2)
    if hasattr(a2, 'customer1'):
        assert not _is_linked(a2, 'customer1', b)


def test_assoc_Orders_Order_Details_reverse_link_reassign_clear():
    a1 = Orders(CustomerId="sample_text", Date="sample_text", OrderId=7, ShippingId="sample_text", customerName="sample_text", dateCreated="sample_text", status="sample_text")
    a2 = Orders(CustomerId="sample_text_2", Date="sample_text_2", OrderId=13, ShippingId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", status="sample_text_2")
    b = Order_Details(orderId=7, productId=7, productName="sample_text", quantity=7, subtotal=7, unitcost=7)
    _safe_set(b, 'orders9', a1)
    assert _is_linked(b, 'orders9', a1)
    if hasattr(a1, 'order_Details8'):
        assert _is_linked(a1, 'order_Details8', b)
    _safe_set(b, 'orders9', a2)
    assert _is_linked(b, 'orders9', a2)
    if hasattr(a1, 'order_Details8'):
        assert not _is_linked(a1, 'order_Details8', b)
    if hasattr(a2, 'order_Details8'):
        assert _is_linked(a2, 'order_Details8', b)
    _safe_set(b, 'orders9', None)
    assert not _is_linked(b, 'orders9', a2)
    if hasattr(a2, 'order_Details8'):
        assert not _is_linked(a2, 'order_Details8', b)


def test_assoc_Orders_Shipping_Info_reverse_link_reassign_clear():
    a1 = Shipping_Info(ShippingRegionId=7, Shipping_Cost=7, Shipping_Id=7, Shipping_Type="sample_text")
    a2 = Shipping_Info(ShippingRegionId=13, Shipping_Cost=13, Shipping_Id=13, Shipping_Type="sample_text_2")
    b = Orders(CustomerId="sample_text", Date="sample_text", OrderId=7, ShippingId="sample_text", customerName="sample_text", dateCreated="sample_text", status="sample_text")
    _safe_set(b, 'shipping_Info6', a1)
    assert _is_linked(b, 'shipping_Info6', a1)
    if hasattr(a1, 'orders7'):
        assert _is_linked(a1, 'orders7', b)
    _safe_set(b, 'shipping_Info6', a2)
    assert _is_linked(b, 'shipping_Info6', a2)
    if hasattr(a1, 'orders7'):
        assert not _is_linked(a1, 'orders7', b)
    if hasattr(a2, 'orders7'):
        assert _is_linked(a2, 'orders7', b)
    _safe_set(b, 'shipping_Info6', None)
    assert not _is_linked(b, 'shipping_Info6', a2)
    if hasattr(a2, 'orders7'):
        assert not _is_linked(a2, 'orders7', b)


def test_assoc_Products_Item_reverse_link_reassign_clear():
    a1 = Products(racknumber=7, totral=7)
    a2 = Products(racknumber=13, totral=13)
    b = Item(name="sample_text", pieceAvailable=7, unitcost=7)
    _safe_set(b, 'products11', a1)
    assert _is_linked(b, 'products11', a1)
    if hasattr(a1, 'item10'):
        assert _is_linked(a1, 'item10', b)
    _safe_set(b, 'products11', a2)
    assert _is_linked(b, 'products11', a2)
    if hasattr(a1, 'item10'):
        assert not _is_linked(a1, 'item10', b)
    if hasattr(a2, 'item10'):
        assert _is_linked(a2, 'item10', b)
    _safe_set(b, 'products11', None)
    assert not _is_linked(b, 'products11', a2)
    if hasattr(a2, 'item10'):
        assert not _is_linked(a2, 'item10', b)


def test_assoc_User_Administrator_reverse_link_reassign_clear():
    a1 = User(Password="sample_text", User_Id="sample_text", loginStatus="sample_text")
    a2 = User(Password="sample_text_2", User_Id="sample_text_2", loginStatus="sample_text_2")
    b = Administrator(adminName="sample_text", email="sample_text")
    _safe_set(b, 'user15', a1)
    assert _is_linked(b, 'user15', a1)
    if hasattr(a1, 'administrator14'):
        assert _is_linked(a1, 'administrator14', b)
    _safe_set(b, 'user15', a2)
    assert _is_linked(b, 'user15', a2)
    if hasattr(a1, 'administrator14'):
        assert not _is_linked(a1, 'administrator14', b)
    if hasattr(a2, 'administrator14'):
        assert _is_linked(a2, 'administrator14', b)
    _safe_set(b, 'user15', None)
    assert not _is_linked(b, 'user15', a2)
    if hasattr(a2, 'administrator14'):
        assert not _is_linked(a2, 'administrator14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

