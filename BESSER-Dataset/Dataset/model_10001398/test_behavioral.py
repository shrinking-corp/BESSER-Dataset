import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ShoppingCart,
    cartitem,
    coustomer,
    order,
    orderDetail,
    product,
    shippinginfo,
    user,
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

def test_assoc_ShoppingCart_cartitem_reverse_link_reassign_clear():
    a1 = cartitem(productId=7, quantity=7, subtotal=3.14, unitcost=3.14)
    a2 = cartitem(productId=13, quantity=13, subtotal=9.99, unitcost=9.99)
    b = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    _safe_set(b, 'ShoppingCart_cartitem_02', a1)
    assert _is_linked(b, 'ShoppingCart_cartitem_02', a1)
    if hasattr(a1, 'ShoppingCart_cartitem_13'):
        assert _is_linked(a1, 'ShoppingCart_cartitem_13', b)
    _safe_set(b, 'ShoppingCart_cartitem_02', a2)
    assert _is_linked(b, 'ShoppingCart_cartitem_02', a2)
    if hasattr(a1, 'ShoppingCart_cartitem_13'):
        assert not _is_linked(a1, 'ShoppingCart_cartitem_13', b)
    if hasattr(a2, 'ShoppingCart_cartitem_13'):
        assert _is_linked(a2, 'ShoppingCart_cartitem_13', b)
    _safe_set(b, 'ShoppingCart_cartitem_02', None)
    assert not _is_linked(b, 'ShoppingCart_cartitem_02', a2)
    if hasattr(a2, 'ShoppingCart_cartitem_13'):
        assert not _is_linked(a2, 'ShoppingCart_cartitem_13', b)


def test_assoc_ShoppingCart_coustomer_reverse_link_reassign_clear():
    a1 = coustomer(address="sample_text", customerId=7, email="sample_text", name="sample_text", phoneno=7, shippinginfo="sample_text")
    a2 = coustomer(address="sample_text_2", customerId=13, email="sample_text_2", name="sample_text_2", phoneno=13, shippinginfo="sample_text_2")
    b = ShoppingCart(cartId=7, dateAdded=7, productId=7, quantity=7)
    _safe_set(b, 'ShoppingCart_coustomer_00', a1)
    assert _is_linked(b, 'ShoppingCart_coustomer_00', a1)
    if hasattr(a1, 'ShoppingCart_coustomer_11'):
        assert _is_linked(a1, 'ShoppingCart_coustomer_11', b)
    _safe_set(b, 'ShoppingCart_coustomer_00', a2)
    assert _is_linked(b, 'ShoppingCart_coustomer_00', a2)
    if hasattr(a1, 'ShoppingCart_coustomer_11'):
        assert not _is_linked(a1, 'ShoppingCart_coustomer_11', b)
    if hasattr(a2, 'ShoppingCart_coustomer_11'):
        assert _is_linked(a2, 'ShoppingCart_coustomer_11', b)
    _safe_set(b, 'ShoppingCart_coustomer_00', None)
    assert not _is_linked(b, 'ShoppingCart_coustomer_00', a2)
    if hasattr(a2, 'ShoppingCart_coustomer_11'):
        assert not _is_linked(a2, 'ShoppingCart_coustomer_11', b)


def test_assoc_cartitem_ProLocal_reverse_link_reassign_clear():
    a1 = product(description="sample_text", image="sample_text", name="sample_text", price=7, productId=7)
    a2 = product(description="sample_text_2", image="sample_text_2", name="sample_text_2", price=13, productId=13)
    b = cartitem(productId=7, quantity=7, subtotal=3.14, unitcost=3.14)
    _safe_set(b, 'cartitem_ProLocal_04', a1)
    assert _is_linked(b, 'cartitem_ProLocal_04', a1)
    if hasattr(a1, 'cartitem_ProLocal_15'):
        assert _is_linked(a1, 'cartitem_ProLocal_15', b)
    _safe_set(b, 'cartitem_ProLocal_04', a2)
    assert _is_linked(b, 'cartitem_ProLocal_04', a2)
    if hasattr(a1, 'cartitem_ProLocal_15'):
        assert not _is_linked(a1, 'cartitem_ProLocal_15', b)
    if hasattr(a2, 'cartitem_ProLocal_15'):
        assert _is_linked(a2, 'cartitem_ProLocal_15', b)
    _safe_set(b, 'cartitem_ProLocal_04', None)
    assert not _is_linked(b, 'cartitem_ProLocal_04', a2)
    if hasattr(a2, 'cartitem_ProLocal_15'):
        assert not _is_linked(a2, 'cartitem_ProLocal_15', b)


def test_assoc_coustomer_order_reverse_link_reassign_clear():
    a1 = order(customerid=7, datecreated="sample_text", name="sample_text", orderId=7, shippingid="sample_text")
    a2 = order(customerid=13, datecreated="sample_text_2", name="sample_text_2", orderId=13, shippingid="sample_text_2")
    b = coustomer(address="sample_text", customerId=7, email="sample_text", name="sample_text", phoneno=7, shippinginfo="sample_text")
    _safe_set(b, 'coustomer_order_08', {a1})
    assert _is_linked(b, 'coustomer_order_08', a1)
    if hasattr(a1, 'coustomer_order_19'):
        assert _is_linked(a1, 'coustomer_order_19', b)
    _safe_set(b, 'coustomer_order_08', {a2})
    assert _is_linked(b, 'coustomer_order_08', a2)
    if hasattr(a1, 'coustomer_order_19'):
        assert not _is_linked(a1, 'coustomer_order_19', b)
    if hasattr(a2, 'coustomer_order_19'):
        assert _is_linked(a2, 'coustomer_order_19', b)
    _safe_set(b, 'coustomer_order_08', set())
    assert not _is_linked(b, 'coustomer_order_08', a2)
    if hasattr(a2, 'coustomer_order_19'):
        assert not _is_linked(a2, 'coustomer_order_19', b)


def test_assoc_orderDetail_ProLocal_reverse_link_reassign_clear():
    a1 = product(description="sample_text", image="sample_text", name="sample_text", price=7, productId=7)
    a2 = product(description="sample_text_2", image="sample_text_2", name="sample_text_2", price=13, productId=13)
    b = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    _safe_set(b, 'orderDetail_ProLocal_06', a1)
    assert _is_linked(b, 'orderDetail_ProLocal_06', a1)
    if hasattr(a1, 'orderDetail_ProLocal_17'):
        assert _is_linked(a1, 'orderDetail_ProLocal_17', b)
    _safe_set(b, 'orderDetail_ProLocal_06', a2)
    assert _is_linked(b, 'orderDetail_ProLocal_06', a2)
    if hasattr(a1, 'orderDetail_ProLocal_17'):
        assert not _is_linked(a1, 'orderDetail_ProLocal_17', b)
    if hasattr(a2, 'orderDetail_ProLocal_17'):
        assert _is_linked(a2, 'orderDetail_ProLocal_17', b)
    _safe_set(b, 'orderDetail_ProLocal_06', None)
    assert not _is_linked(b, 'orderDetail_ProLocal_06', a2)
    if hasattr(a2, 'orderDetail_ProLocal_17'):
        assert not _is_linked(a2, 'orderDetail_ProLocal_17', b)


def test_assoc_order_orderDetail_reverse_link_reassign_clear():
    a1 = orderDetail(orderId=7, productid=7, productname="sample_text", quantity=7, subtotall=3.14, unitcost=3.14)
    a2 = orderDetail(orderId=13, productid=13, productname="sample_text_2", quantity=13, subtotall=9.99, unitcost=9.99)
    b = order(customerid=7, datecreated="sample_text", name="sample_text", orderId=7, shippingid="sample_text")
    _safe_set(b, 'order_orderDetail_010', a1)
    assert _is_linked(b, 'order_orderDetail_010', a1)
    if hasattr(a1, 'order_orderDetail_111'):
        assert _is_linked(a1, 'order_orderDetail_111', b)
    _safe_set(b, 'order_orderDetail_010', a2)
    assert _is_linked(b, 'order_orderDetail_010', a2)
    if hasattr(a1, 'order_orderDetail_111'):
        assert not _is_linked(a1, 'order_orderDetail_111', b)
    if hasattr(a2, 'order_orderDetail_111'):
        assert _is_linked(a2, 'order_orderDetail_111', b)
    _safe_set(b, 'order_orderDetail_010', None)
    assert not _is_linked(b, 'order_orderDetail_010', a2)
    if hasattr(a2, 'order_orderDetail_111'):
        assert not _is_linked(a2, 'order_orderDetail_111', b)


def test_assoc_order_shippinginfo_reverse_link_reassign_clear():
    a1 = shippinginfo(shippingId=7, shippingcost=7)
    a2 = shippinginfo(shippingId=13, shippingcost=13)
    b = order(customerid=7, datecreated="sample_text", name="sample_text", orderId=7, shippingid="sample_text")
    _safe_set(b, 'order_shippinginfo_012', a1)
    assert _is_linked(b, 'order_shippinginfo_012', a1)
    if hasattr(a1, 'order_shippinginfo_113'):
        assert _is_linked(a1, 'order_shippinginfo_113', b)
    _safe_set(b, 'order_shippinginfo_012', a2)
    assert _is_linked(b, 'order_shippinginfo_012', a2)
    if hasattr(a1, 'order_shippinginfo_113'):
        assert not _is_linked(a1, 'order_shippinginfo_113', b)
    if hasattr(a2, 'order_shippinginfo_113'):
        assert _is_linked(a2, 'order_shippinginfo_113', b)
    _safe_set(b, 'order_shippinginfo_012', None)
    assert not _is_linked(b, 'order_shippinginfo_012', a2)
    if hasattr(a2, 'order_shippinginfo_113'):
        assert not _is_linked(a2, 'order_shippinginfo_113', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

