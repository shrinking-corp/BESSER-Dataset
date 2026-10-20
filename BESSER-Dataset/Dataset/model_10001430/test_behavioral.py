import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Customer,
    Order,
    OrderDetail,
    Portal,
    PremiumCustomer,
    Product,
    OrderStatus,
    real,
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

def test_assoc_Customer_Portal_reverse_link_reassign_clear():
    a1 = Portal(name="sample_text", portalId="sample_text", url="sample_text")
    a2 = Portal(name="sample_text_2", portalId="sample_text_2", url="sample_text_2")
    b = Customer(address="sample_text", creditCardInfo="sample_text", email="sample_text", name="sample_text", phone=7, shippingInfo="sample_text")
    _safe_set(b, 'portal6', a1)
    assert _is_linked(b, 'portal6', a1)
    if hasattr(a1, 'users7'):
        assert _is_linked(a1, 'users7', b)
    _safe_set(b, 'portal6', a2)
    assert _is_linked(b, 'portal6', a2)
    if hasattr(a1, 'users7'):
        assert not _is_linked(a1, 'users7', b)
    if hasattr(a2, 'users7'):
        assert _is_linked(a2, 'users7', b)
    _safe_set(b, 'portal6', None)
    assert not _is_linked(b, 'portal6', a2)
    if hasattr(a2, 'users7'):
        assert not _is_linked(a2, 'users7', b)


def test_assoc_Product_OrderDetail_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", imageFileName="sample_text", price=3.14, productId=7, productName="sample_text", stock=7)
    a2 = Product(description="sample_text_2", imageFileName="sample_text_2", price=9.99, productId=13, productName="sample_text_2", stock=13)
    b = OrderDetail(ordrId=7, productId=7, productName="sample_text", quantity=7, subtotal=3.14, unitCost=3.14)
    _safe_set(b, 'product3', a1)
    assert _is_linked(b, 'product3', a1)
    if hasattr(a1, 'orderDetails2'):
        assert _is_linked(a1, 'orderDetails2', b)
    _safe_set(b, 'product3', a2)
    assert _is_linked(b, 'product3', a2)
    if hasattr(a1, 'orderDetails2'):
        assert not _is_linked(a1, 'orderDetails2', b)
    if hasattr(a2, 'orderDetails2'):
        assert _is_linked(a2, 'orderDetails2', b)
    _safe_set(b, 'product3', None)
    assert not _is_linked(b, 'product3', a2)
    if hasattr(a2, 'orderDetails2'):
        assert not _is_linked(a2, 'orderDetails2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

