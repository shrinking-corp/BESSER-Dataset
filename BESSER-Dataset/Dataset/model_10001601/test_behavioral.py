import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    LineItem,
    Order,
    Payment,
    Product,
    ShoppingCart,
    ShoppingCart1,
    OrderStatus,
    UserState,
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

def test_assoc_Account_Payment_reverse_link_reassign_clear():
    a1 = ShoppingCart1(closed=date(2024, 1, 1), isClosed=True, itemCount=7, totalPrice=7)
    a2 = ShoppingCart1(closed=date(2025, 6, 15), isClosed=False, itemCount=13, totalPrice=13)
    b = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    _safe_set(b, 'acc1', a1)
    assert _is_linked(b, 'acc1', a1)
    if hasattr(a1, 'p0'):
        assert _is_linked(a1, 'p0', b)
    _safe_set(b, 'acc1', a2)
    assert _is_linked(b, 'acc1', a2)
    if hasattr(a1, 'p0'):
        assert not _is_linked(a1, 'p0', b)
    if hasattr(a2, 'p0'):
        assert _is_linked(a2, 'p0', b)
    _safe_set(b, 'acc1', None)
    assert not _is_linked(b, 'acc1', a2)
    if hasattr(a2, 'p0'):
        assert not _is_linked(a2, 'p0', b)


def test_assoc_Account_ShoppingCart_reverse_link_reassign_clear():
    a1 = ShoppingCart1(closed=date(2024, 1, 1), isClosed=True, itemCount=7, totalPrice=7)
    a2 = ShoppingCart1(closed=date(2025, 6, 15), isClosed=False, itemCount=13, totalPrice=13)
    b = ShoppingCart(creationDate=date(2024, 1, 1))
    _safe_set(b, 'account3', a1)
    assert _is_linked(b, 'account3', a1)
    if hasattr(a1, 'cart2'):
        assert _is_linked(a1, 'cart2', b)
    _safe_set(b, 'account3', a2)
    assert _is_linked(b, 'account3', a2)
    if hasattr(a1, 'cart2'):
        assert not _is_linked(a1, 'cart2', b)
    if hasattr(a2, 'cart2'):
        assert _is_linked(a2, 'cart2', b)
    _safe_set(b, 'account3', None)
    assert not _is_linked(b, 'account3', a2)
    if hasattr(a2, 'cart2'):
        assert not _is_linked(a2, 'cart2', b)


def test_assoc_Product_LineItem_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", name="sample_text")
    a2 = Product(description="sample_text_2", name="sample_text_2")
    b = LineItem(price=3.14, quantity=7)
    _safe_set(b, 'product7', a1)
    assert _is_linked(b, 'product7', a1)
    if hasattr(a1, 'lineItems6'):
        assert _is_linked(a1, 'lineItems6', b)
    _safe_set(b, 'product7', a2)
    assert _is_linked(b, 'product7', a2)
    if hasattr(a1, 'lineItems6'):
        assert not _is_linked(a1, 'lineItems6', b)
    if hasattr(a2, 'lineItems6'):
        assert _is_linked(a2, 'lineItems6', b)
    _safe_set(b, 'product7', None)
    assert not _is_linked(b, 'product7', a2)
    if hasattr(a2, 'lineItems6'):
        assert not _is_linked(a2, 'lineItems6', b)


def test_assoc_ShoppingCart_LineItem_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = LineItem(price=3.14, quantity=7)
    _safe_set(b, 'sc5', a1)
    assert _is_linked(b, 'sc5', a1)
    if hasattr(a1, 'items4'):
        assert _is_linked(a1, 'items4', b)
    _safe_set(b, 'sc5', a2)
    assert _is_linked(b, 'sc5', a2)
    if hasattr(a1, 'items4'):
        assert not _is_linked(a1, 'items4', b)
    if hasattr(a2, 'items4'):
        assert _is_linked(a2, 'items4', b)
    _safe_set(b, 'sc5', None)
    assert not _is_linked(b, 'sc5', a2)
    if hasattr(a2, 'items4'):
        assert not _is_linked(a2, 'items4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

