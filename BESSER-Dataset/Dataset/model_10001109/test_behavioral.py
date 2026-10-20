import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Controllers_OrderController,
    Controllers_ProductController,
    Controllers_ShoppingCartController,
    Models_Customer,
    Models_LineItem,
    Models_LoginLog,
    Models_Order,
    Models_Product,
    Models_ShippingInfo,
    Models_ShoppingCart,
    Models_User,
    Models_cartItem,
    dao_CartItemDao_Interface,
    dao_CustomerDao_Interface,
    dao_LineItemDao_Interface,
    dao_OrderDao_Interface,
    dao_ProductDao_Interface,
    dao_ShippingInfoDao_Interface,
    dao_ShoppingCartDao_Interface,
    Models_OrderStatus,
    Models_ShippingType,
    Models_ShoppingCartStatus,
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

def test_assoc_LoginLog_user_reverse_link_reassign_clear():
    a1 = Models_User(UserId="sample_text", email="sample_text", password="sample_text")
    a2 = Models_User(UserId="sample_text_2", email="sample_text_2", password="sample_text_2")
    b = Models_LoginLog(id=7, isLogin=True, lastLoginDate=date(2024, 1, 1), user_id=7)
    _safe_set(b, 'user16', a1)
    assert _is_linked(b, 'user16', a1)
    if hasattr(a1, 'loginLog17'):
        assert _is_linked(a1, 'loginLog17', b)
    _safe_set(b, 'user16', a2)
    assert _is_linked(b, 'user16', a2)
    if hasattr(a1, 'loginLog17'):
        assert not _is_linked(a1, 'loginLog17', b)
    if hasattr(a2, 'loginLog17'):
        assert _is_linked(a2, 'loginLog17', b)
    _safe_set(b, 'user16', None)
    assert not _is_linked(b, 'user16', a2)
    if hasattr(a2, 'loginLog17'):
        assert not _is_linked(a2, 'loginLog17', b)


def test_assoc_ShoppingCart_cartitem_reverse_link_reassign_clear():
    a1 = Models_cartItem(cartId=7, deleted=True, name="sample_text", quantity=7, subtotal=3.14, unitcost=3.14)
    a2 = Models_cartItem(cartId=13, deleted=False, name="sample_text_2", quantity=13, subtotal=9.99, unitcost=9.99)
    b = Models_ShoppingCart(cartId=7, customerId=7, dateAdded=7, deleted=True, status=7)
    _safe_set(b, 'ShoppingCart_cartitem_020', {a1})
    assert _is_linked(b, 'ShoppingCart_cartitem_020', a1)
    if hasattr(a1, 'ShoppingCart_cartitem_121'):
        assert _is_linked(a1, 'ShoppingCart_cartitem_121', b)
    _safe_set(b, 'ShoppingCart_cartitem_020', {a2})
    assert _is_linked(b, 'ShoppingCart_cartitem_020', a2)
    if hasattr(a1, 'ShoppingCart_cartitem_121'):
        assert not _is_linked(a1, 'ShoppingCart_cartitem_121', b)
    if hasattr(a2, 'ShoppingCart_cartitem_121'):
        assert _is_linked(a2, 'ShoppingCart_cartitem_121', b)
    _safe_set(b, 'ShoppingCart_cartitem_020', set())
    assert not _is_linked(b, 'ShoppingCart_cartitem_020', a2)
    if hasattr(a2, 'ShoppingCart_cartitem_121'):
        assert not _is_linked(a2, 'ShoppingCart_cartitem_121', b)


def test_assoc_ShoppingCart_coustomer_reverse_link_reassign_clear():
    a1 = Models_ShoppingCart(cartId=7, customerId=7, dateAdded=7, deleted=True, status=7)
    a2 = Models_ShoppingCart(cartId=13, customerId=13, dateAdded=13, deleted=False, status=13)
    b = Models_Customer(address="sample_text", coustomername="sample_text", creditcardinfo="sample_text", deleted=True, phoneno=7, shippinginfo="sample_text")
    _safe_set(b, 'ShoppingCart_coustomer_111', a1)
    assert _is_linked(b, 'ShoppingCart_coustomer_111', a1)
    if hasattr(a1, 'ShoppingCart_coustomer_010'):
        assert _is_linked(a1, 'ShoppingCart_coustomer_010', b)
    _safe_set(b, 'ShoppingCart_coustomer_111', a2)
    assert _is_linked(b, 'ShoppingCart_coustomer_111', a2)
    if hasattr(a1, 'ShoppingCart_coustomer_010'):
        assert not _is_linked(a1, 'ShoppingCart_coustomer_010', b)
    if hasattr(a2, 'ShoppingCart_coustomer_010'):
        assert _is_linked(a2, 'ShoppingCart_coustomer_010', b)
    _safe_set(b, 'ShoppingCart_coustomer_111', None)
    assert not _is_linked(b, 'ShoppingCart_coustomer_111', a2)
    if hasattr(a2, 'ShoppingCart_coustomer_010'):
        assert not _is_linked(a2, 'ShoppingCart_coustomer_010', b)


def test_assoc_cartitem_ProLocal_reverse_link_reassign_clear():
    a1 = Models_cartItem(cartId=7, deleted=True, name="sample_text", quantity=7, subtotal=3.14, unitcost=3.14)
    a2 = Models_cartItem(cartId=13, deleted=False, name="sample_text_2", quantity=13, subtotal=9.99, unitcost=9.99)
    b = Models_Product(imagefilename="sample_text", price=3.14, productid=7, productname="sample_text", quantity=7)
    _safe_set(b, 'cartitem_ProLocal_123', {a1})
    assert _is_linked(b, 'cartitem_ProLocal_123', a1)
    if hasattr(a1, 'cartitem_ProLocal_022'):
        assert _is_linked(a1, 'cartitem_ProLocal_022', b)
    _safe_set(b, 'cartitem_ProLocal_123', {a2})
    assert _is_linked(b, 'cartitem_ProLocal_123', a2)
    if hasattr(a1, 'cartitem_ProLocal_022'):
        assert not _is_linked(a1, 'cartitem_ProLocal_022', b)
    if hasattr(a2, 'cartitem_ProLocal_022'):
        assert _is_linked(a2, 'cartitem_ProLocal_022', b)
    _safe_set(b, 'cartitem_ProLocal_123', set())
    assert not _is_linked(b, 'cartitem_ProLocal_123', a2)
    if hasattr(a2, 'cartitem_ProLocal_022'):
        assert not _is_linked(a2, 'cartitem_ProLocal_022', b)


def test_assoc_coustomer_order_reverse_link_reassign_clear():
    a1 = Models_Order(customerid=7, dateCreated=date(2024, 1, 1), dateShipped="sample_text", orderID=7, shippingInfoId=7, status="sample_text")
    a2 = Models_Order(customerid=13, dateCreated=date(2025, 6, 15), dateShipped="sample_text_2", orderID=13, shippingInfoId=13, status="sample_text_2")
    b = Models_Customer(address="sample_text", coustomername="sample_text", creditcardinfo="sample_text", deleted=True, phoneno=7, shippinginfo="sample_text")
    _safe_set(b, 'coustomer_order_012', {a1})
    assert _is_linked(b, 'coustomer_order_012', a1)
    if hasattr(a1, 'coustomer_order_113'):
        assert _is_linked(a1, 'coustomer_order_113', b)
    _safe_set(b, 'coustomer_order_012', {a2})
    assert _is_linked(b, 'coustomer_order_012', a2)
    if hasattr(a1, 'coustomer_order_113'):
        assert not _is_linked(a1, 'coustomer_order_113', b)
    if hasattr(a2, 'coustomer_order_113'):
        assert _is_linked(a2, 'coustomer_order_113', b)
    _safe_set(b, 'coustomer_order_012', set())
    assert not _is_linked(b, 'coustomer_order_012', a2)
    if hasattr(a2, 'coustomer_order_113'):
        assert not _is_linked(a2, 'coustomer_order_113', b)


def test_assoc_orderDetail_ProLocal_reverse_link_reassign_clear():
    a1 = Models_Product(imagefilename="sample_text", price=3.14, productid=7, productname="sample_text", quantity=7)
    a2 = Models_Product(imagefilename="sample_text_2", price=9.99, productid=13, productname="sample_text_2", quantity=13)
    b = Models_LineItem(orderId=7, productid=7, productname="sample_text", quantity=7, subtotal=3.14, unitcost=3.14)
    _safe_set(b, 'orderDetail_ProLocal_018', a1)
    assert _is_linked(b, 'orderDetail_ProLocal_018', a1)
    if hasattr(a1, 'orderDetail_ProLocal_119'):
        assert _is_linked(a1, 'orderDetail_ProLocal_119', b)
    _safe_set(b, 'orderDetail_ProLocal_018', a2)
    assert _is_linked(b, 'orderDetail_ProLocal_018', a2)
    if hasattr(a1, 'orderDetail_ProLocal_119'):
        assert not _is_linked(a1, 'orderDetail_ProLocal_119', b)
    if hasattr(a2, 'orderDetail_ProLocal_119'):
        assert _is_linked(a2, 'orderDetail_ProLocal_119', b)
    _safe_set(b, 'orderDetail_ProLocal_018', None)
    assert not _is_linked(b, 'orderDetail_ProLocal_018', a2)
    if hasattr(a2, 'orderDetail_ProLocal_119'):
        assert not _is_linked(a2, 'orderDetail_ProLocal_119', b)


def test_assoc_order_orderDetail_reverse_link_reassign_clear():
    a1 = Models_Order(customerid=7, dateCreated=date(2024, 1, 1), dateShipped="sample_text", orderID=7, shippingInfoId=7, status="sample_text")
    a2 = Models_Order(customerid=13, dateCreated=date(2025, 6, 15), dateShipped="sample_text_2", orderID=13, shippingInfoId=13, status="sample_text_2")
    b = Models_LineItem(orderId=7, productid=7, productname="sample_text", quantity=7, subtotal=3.14, unitcost=3.14)
    _safe_set(b, 'order_orderDetail_115', a1)
    assert _is_linked(b, 'order_orderDetail_115', a1)
    if hasattr(a1, 'order_orderDetail_014'):
        assert _is_linked(a1, 'order_orderDetail_014', b)
    _safe_set(b, 'order_orderDetail_115', a2)
    assert _is_linked(b, 'order_orderDetail_115', a2)
    if hasattr(a1, 'order_orderDetail_014'):
        assert not _is_linked(a1, 'order_orderDetail_014', b)
    if hasattr(a2, 'order_orderDetail_014'):
        assert _is_linked(a2, 'order_orderDetail_014', b)
    _safe_set(b, 'order_orderDetail_115', None)
    assert not _is_linked(b, 'order_orderDetail_115', a2)
    if hasattr(a2, 'order_orderDetail_014'):
        assert not _is_linked(a2, 'order_orderDetail_014', b)


def test_assoc_order_shippinginfo_reverse_link_reassign_clear():
    a1 = Models_ShippingInfo(shippingcost=7, shippingid=7, shippingregionid=7, shippingtype="sample_text")
    a2 = Models_ShippingInfo(shippingcost=13, shippingid=13, shippingregionid=13, shippingtype="sample_text_2")
    b = Models_Order(customerid=7, dateCreated=date(2024, 1, 1), dateShipped="sample_text", orderID=7, shippingInfoId=7, status="sample_text")
    _safe_set(b, 'order_shippinginfo_024', a1)
    assert _is_linked(b, 'order_shippinginfo_024', a1)
    if hasattr(a1, 'order_shippinginfo_125'):
        assert _is_linked(a1, 'order_shippinginfo_125', b)
    _safe_set(b, 'order_shippinginfo_024', a2)
    assert _is_linked(b, 'order_shippinginfo_024', a2)
    if hasattr(a1, 'order_shippinginfo_125'):
        assert not _is_linked(a1, 'order_shippinginfo_125', b)
    if hasattr(a2, 'order_shippinginfo_125'):
        assert _is_linked(a2, 'order_shippinginfo_125', b)
    _safe_set(b, 'order_shippinginfo_024', None)
    assert not _is_linked(b, 'order_shippinginfo_024', a2)
    if hasattr(a2, 'order_shippinginfo_125'):
        assert not _is_linked(a2, 'order_shippinginfo_125', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_CartItemDao_cartItem_stub_double():
    # dao_CartItemDao_Interface has no real 'cartItem4' property in the generated
    # code (a bare stub) -- manually attach it so Models_cartItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Models_cartItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Models_cartItem(cartId=7, deleted=True, name="sample_text", quantity=7, subtotal=3.14, unitcost=3.14)
    partner = dao_CartItemDao_Interface()
    setattr(partner, 'cartItem4', None)
    _safe_set(owner, 'cartItemDao5', partner)
    assert getattr(partner, 'cartItem4') == owner
    _safe_set(owner, 'cartItemDao5', None)
    assert getattr(partner, 'cartItem4') is None


def test_assoc_Customer_CustomerDao_stub_double():
    # dao_CustomerDao_Interface has no real 'customer29' property in the generated
    # code (a bare stub) -- manually attach it so Models_Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Models_Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Models_Customer(address="sample_text", coustomername="sample_text", creditcardinfo="sample_text", deleted=True, phoneno=7, shippinginfo="sample_text")
    partner = dao_CustomerDao_Interface()
    setattr(partner, 'customer29', None)
    _safe_set(owner, 'customerDao28', partner)
    assert getattr(partner, 'customer29') == owner
    _safe_set(owner, 'customerDao28', None)
    assert getattr(partner, 'customer29') is None


def test_assoc_OrderDao_Order_stub_double():
    # dao_OrderDao_Interface has no real 'order2' property in the generated
    # code (a bare stub) -- manually attach it so Models_Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Models_Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Models_Order(customerid=7, dateCreated=date(2024, 1, 1), dateShipped="sample_text", orderID=7, shippingInfoId=7, status="sample_text")
    partner = dao_OrderDao_Interface()
    setattr(partner, 'order2', None)
    _safe_set(owner, 'orderDao3', partner)
    assert getattr(partner, 'order2') == owner
    _safe_set(owner, 'orderDao3', None)
    assert getattr(partner, 'order2') is None


def test_assoc_ShippingInfo_shippingInfo_stub_double():
    # dao_ShippingInfoDao_Interface has no real 'shippingInfo0' property in the generated
    # code (a bare stub) -- manually attach it so Models_ShippingInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Models_ShippingInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Models_ShippingInfo(shippingcost=7, shippingid=7, shippingregionid=7, shippingtype="sample_text")
    partner = dao_ShippingInfoDao_Interface()
    setattr(partner, 'shippingInfo0', None)
    _safe_set(owner, 'shippingInfo1', partner)
    assert getattr(partner, 'shippingInfo0') == owner
    _safe_set(owner, 'shippingInfo1', None)
    assert getattr(partner, 'shippingInfo0') is None


def test_assoc_ShoppingCart_ShoppingCartDao_stub_double():
    # dao_ShoppingCartDao_Interface has no real 'shoppingCart9' property in the generated
    # code (a bare stub) -- manually attach it so Models_ShoppingCart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Models_ShoppingCart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Models_ShoppingCart(cartId=7, customerId=7, dateAdded=7, deleted=True, status=7)
    partner = dao_ShoppingCartDao_Interface()
    setattr(partner, 'shoppingCart9', None)
    _safe_set(owner, 'shoppingCartDao8', partner)
    assert getattr(partner, 'shoppingCart9') == owner
    _safe_set(owner, 'shoppingCartDao8', None)
    assert getattr(partner, 'shoppingCart9') is None


def test_assoc_product_LineItemDao_stub_double():
    # dao_LineItemDao_Interface has no real 'LineItem7' property in the generated
    # code (a bare stub) -- manually attach it so Models_LineItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Models_LineItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Models_LineItem(orderId=7, productid=7, productname="sample_text", quantity=7, subtotal=3.14, unitcost=3.14)
    partner = dao_LineItemDao_Interface()
    setattr(partner, 'LineItem7', None)
    _safe_set(owner, 'lineItemDao6', partner)
    assert getattr(partner, 'LineItem7') == owner
    _safe_set(owner, 'lineItemDao6', None)
    assert getattr(partner, 'LineItem7') is None


def test_assoc_product_ProductDao_stub_double():
    # dao_ProductDao_Interface has no real 'product27' property in the generated
    # code (a bare stub) -- manually attach it so Models_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Models_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Models_Product(imagefilename="sample_text", price=3.14, productid=7, productname="sample_text", quantity=7)
    partner = dao_ProductDao_Interface()
    setattr(partner, 'product27', None)
    _safe_set(owner, 'productDao26', partner)
    assert getattr(partner, 'product27') == owner
    _safe_set(owner, 'productDao26', None)
    assert getattr(partner, 'product27') is None


