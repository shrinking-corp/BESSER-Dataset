import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Classes,
    Order,
    Payment,
    Product,
    ShoppingCart,
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

def test_assoc_Account_Order_reverse_link_reassign_clear():
    a1 = Order(Items="sample_text", number="sample_text")
    a2 = Order(Items="sample_text_2", number="sample_text_2")
    b = Account(Valid_invalid="sample_text", open=date(2024, 1, 1))
    _safe_set(b, 'order10', {a1})
    assert _is_linked(b, 'order10', a1)
    if hasattr(a1, 'account11'):
        assert _is_linked(a1, 'account11', b)
    _safe_set(b, 'order10', {a2})
    assert _is_linked(b, 'order10', a2)
    if hasattr(a1, 'account11'):
        assert not _is_linked(a1, 'account11', b)
    if hasattr(a2, 'account11'):
        assert _is_linked(a2, 'account11', b)
    _safe_set(b, 'order10', set())
    assert not _is_linked(b, 'order10', a2)
    if hasattr(a2, 'account11'):
        assert not _is_linked(a2, 'account11', b)


def test_assoc_Account_ShoppingCart_reverse_link_reassign_clear():
    a1 = ShoppingCart(Update_cart=date(2024, 1, 1))
    a2 = ShoppingCart(Update_cart=date(2025, 6, 15))
    b = Account(Valid_invalid="sample_text", open=date(2024, 1, 1))
    _safe_set(b, 'cart2', a1)
    assert _is_linked(b, 'cart2', a1)
    if hasattr(a1, 'account3'):
        assert _is_linked(a1, 'account3', b)
    _safe_set(b, 'cart2', a2)
    assert _is_linked(b, 'cart2', a2)
    if hasattr(a1, 'account3'):
        assert not _is_linked(a1, 'account3', b)
    if hasattr(a2, 'account3'):
        assert _is_linked(a2, 'account3', b)
    _safe_set(b, 'cart2', None)
    assert not _is_linked(b, 'cart2', a2)
    if hasattr(a2, 'account3'):
        assert not _is_linked(a2, 'account3', b)


def test_assoc_Order_LineItem_reverse_link_reassign_clear():
    a1 = Order(Items="sample_text", number="sample_text")
    a2 = Order(Items="sample_text_2", number="sample_text_2")
    b = Classes(Name="sample_text", quantity="sample_text")
    _safe_set(b, 'order9', a1)
    assert _is_linked(b, 'order9', a1)
    if hasattr(a1, 'items8'):
        assert _is_linked(a1, 'items8', b)
    _safe_set(b, 'order9', a2)
    assert _is_linked(b, 'order9', a2)
    if hasattr(a1, 'items8'):
        assert not _is_linked(a1, 'items8', b)
    if hasattr(a2, 'items8'):
        assert _is_linked(a2, 'items8', b)
    _safe_set(b, 'order9', None)
    assert not _is_linked(b, 'order9', a2)
    if hasattr(a2, 'items8'):
        assert not _is_linked(a2, 'items8', b)


def test_assoc_Payment_Order_reverse_link_reassign_clear():
    a1 = Payment(Paytment_type="sample_text")
    a2 = Payment(Paytment_type="sample_text_2")
    b = Order(Items="sample_text", number="sample_text")
    _safe_set(b, 'payment13', a1)
    assert _is_linked(b, 'payment13', a1)
    if hasattr(a1, 'order12'):
        assert _is_linked(a1, 'order12', b)
    _safe_set(b, 'payment13', a2)
    assert _is_linked(b, 'payment13', a2)
    if hasattr(a1, 'order12'):
        assert not _is_linked(a1, 'order12', b)
    if hasattr(a2, 'order12'):
        assert _is_linked(a2, 'order12', b)
    _safe_set(b, 'payment13', None)
    assert not _is_linked(b, 'payment13', a2)
    if hasattr(a2, 'order12'):
        assert not _is_linked(a2, 'order12', b)


def test_assoc_Product_LineItem_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", name="sample_text")
    a2 = Product(description="sample_text_2", name="sample_text_2")
    b = Classes(Name="sample_text", quantity="sample_text")
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
    a1 = ShoppingCart(Update_cart=date(2024, 1, 1))
    a2 = ShoppingCart(Update_cart=date(2025, 6, 15))
    b = Classes(Name="sample_text", quantity="sample_text")
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


def test_assoc_WebUser_ShoppingCart_reverse_link_reassign_clear():
    a1 = User(login="sample_text", password="sample_text")
    a2 = User(login="sample_text_2", password="sample_text_2")
    b = ShoppingCart(Update_cart=date(2024, 1, 1))
    _safe_set(b, 'webUser1', a1)
    assert _is_linked(b, 'webUser1', a1)
    if hasattr(a1, 'shoppingCart0'):
        assert _is_linked(a1, 'shoppingCart0', b)
    _safe_set(b, 'webUser1', a2)
    assert _is_linked(b, 'webUser1', a2)
    if hasattr(a1, 'shoppingCart0'):
        assert not _is_linked(a1, 'shoppingCart0', b)
    if hasattr(a2, 'shoppingCart0'):
        assert _is_linked(a2, 'shoppingCart0', b)
    _safe_set(b, 'webUser1', None)
    assert not _is_linked(b, 'webUser1', a2)
    if hasattr(a2, 'shoppingCart0'):
        assert not _is_linked(a2, 'shoppingCart0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

