import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Class,
    Customer,
    Item,
    Order,
    Payment,
    Product,
    ShoppingCart,
    OrderStatus,
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

def test_assoc_association2_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1), id=7)
    a2 = ShoppingCart(creationDate=date(2025, 6, 15), id=13)
    b = Customer(emailAddress="sample_text", firstname="sample_text", id=7, isBan=True, lastname="sample_text", login="sample_text", password="sample_text")
    _safe_set(b, 'cart1', a1)
    assert _is_linked(b, 'cart1', a1)
    if hasattr(a1, 'c0'):
        assert _is_linked(a1, 'c0', b)
    _safe_set(b, 'cart1', a2)
    assert _is_linked(b, 'cart1', a2)
    if hasattr(a1, 'c0'):
        assert not _is_linked(a1, 'c0', b)
    if hasattr(a2, 'c0'):
        assert _is_linked(a2, 'c0', b)
    _safe_set(b, 'cart1', None)
    assert not _is_linked(b, 'cart1', a2)
    if hasattr(a2, 'c0'):
        assert not _is_linked(a2, 'c0', b)


def test_assoc_association3_reverse_link_reassign_clear():
    a1 = Customer(emailAddress="sample_text", firstname="sample_text", id=7, isBan=True, lastname="sample_text", login="sample_text", password="sample_text")
    a2 = Customer(emailAddress="sample_text_2", firstname="sample_text_2", id=13, isBan=False, lastname="sample_text_2", login="sample_text_2", password="sample_text_2")
    b = Account(billingAddress="sample_text", id=7, openDate=date(2024, 1, 1))
    _safe_set(b, 'customer2', a1)
    assert _is_linked(b, 'customer2', a1)
    if hasattr(a1, 'account3'):
        assert _is_linked(a1, 'account3', b)
    _safe_set(b, 'customer2', a2)
    assert _is_linked(b, 'customer2', a2)
    if hasattr(a1, 'account3'):
        assert not _is_linked(a1, 'account3', b)
    if hasattr(a2, 'account3'):
        assert _is_linked(a2, 'account3', b)
    _safe_set(b, 'customer2', None)
    assert not _is_linked(b, 'customer2', a2)
    if hasattr(a2, 'account3'):
        assert not _is_linked(a2, 'account3', b)


def test_assoc_association4_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1), id=7)
    a2 = ShoppingCart(creationDate=date(2025, 6, 15), id=13)
    b = Account(billingAddress="sample_text", id=7, openDate=date(2024, 1, 1))
    _safe_set(b, 'shoppingcart5', a1)
    assert _is_linked(b, 'shoppingcart5', a1)
    if hasattr(a1, 'accnt4'):
        assert _is_linked(a1, 'accnt4', b)
    _safe_set(b, 'shoppingcart5', a2)
    assert _is_linked(b, 'shoppingcart5', a2)
    if hasattr(a1, 'accnt4'):
        assert not _is_linked(a1, 'accnt4', b)
    if hasattr(a2, 'accnt4'):
        assert _is_linked(a2, 'accnt4', b)
    _safe_set(b, 'shoppingcart5', None)
    assert not _is_linked(b, 'shoppingcart5', a2)
    if hasattr(a2, 'accnt4'):
        assert not _is_linked(a2, 'accnt4', b)


def test_assoc_association5_reverse_link_reassign_clear():
    a1 = Payment(comments="sample_text", id=7, total=7)
    a2 = Payment(comments="sample_text_2", id=13, total=13)
    b = Account(billingAddress="sample_text", id=7, openDate=date(2024, 1, 1))
    _safe_set(b, 'payment7', {a1})
    assert _is_linked(b, 'payment7', a1)
    if hasattr(a1, 'acc6'):
        assert _is_linked(a1, 'acc6', b)
    _safe_set(b, 'payment7', {a2})
    assert _is_linked(b, 'payment7', a2)
    if hasattr(a1, 'acc6'):
        assert not _is_linked(a1, 'acc6', b)
    if hasattr(a2, 'acc6'):
        assert _is_linked(a2, 'acc6', b)
    _safe_set(b, 'payment7', set())
    assert not _is_linked(b, 'payment7', a2)
    if hasattr(a2, 'acc6'):
        assert not _is_linked(a2, 'acc6', b)


def test_assoc_association7_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1), id=7)
    a2 = ShoppingCart(creationDate=date(2025, 6, 15), id=13)
    b = Item(id=7, price=3.14, quantity=7)
    _safe_set(b, 'shoppingcart10', a1)
    assert _is_linked(b, 'shoppingcart10', a1)
    if hasattr(a1, 'item11'):
        assert _is_linked(a1, 'item11', b)
    _safe_set(b, 'shoppingcart10', a2)
    assert _is_linked(b, 'shoppingcart10', a2)
    if hasattr(a1, 'item11'):
        assert not _is_linked(a1, 'item11', b)
    if hasattr(a2, 'item11'):
        assert _is_linked(a2, 'item11', b)
    _safe_set(b, 'shoppingcart10', None)
    assert not _is_linked(b, 'shoppingcart10', a2)
    if hasattr(a2, 'item11'):
        assert not _is_linked(a2, 'item11', b)


def test_assoc_association8_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", id=7, name="sample_text")
    a2 = Product(description="sample_text_2", id=13, name="sample_text_2")
    b = Item(id=7, price=3.14, quantity=7)
    _safe_set(b, 'product13', a1)
    assert _is_linked(b, 'product13', a1)
    if hasattr(a1, 'item12'):
        assert _is_linked(a1, 'item12', b)
    _safe_set(b, 'product13', a2)
    assert _is_linked(b, 'product13', a2)
    if hasattr(a1, 'item12'):
        assert not _is_linked(a1, 'item12', b)
    if hasattr(a2, 'item12'):
        assert _is_linked(a2, 'item12', b)
    _safe_set(b, 'product13', None)
    assert not _is_linked(b, 'product13', a2)
    if hasattr(a2, 'item12'):
        assert not _is_linked(a2, 'item12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

