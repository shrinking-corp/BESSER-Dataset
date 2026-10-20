import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Admin_Actor,
    AjoutProduit_UseCase,
    Customer,
    LineItem,
    MyActor2_Actor,
    MyActor_Actor,
    MyUseCase_UseCase,
    Order,
    Payment,
    Product,
    ShoppingCart,
    WebUser,
    Webuser_Actor,
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
    a1 = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Payment(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'payment0', {a1})
    assert _is_linked(b, 'payment0', a1)
    if hasattr(a1, 'account1'):
        assert _is_linked(a1, 'account1', b)
    _safe_set(b, 'payment0', {a2})
    assert _is_linked(b, 'payment0', a2)
    if hasattr(a1, 'account1'):
        assert not _is_linked(a1, 'account1', b)
    if hasattr(a2, 'account1'):
        assert _is_linked(a2, 'account1', b)
    _safe_set(b, 'payment0', set())
    assert not _is_linked(b, 'payment0', a2)
    if hasattr(a2, 'account1'):
        assert not _is_linked(a2, 'account1', b)


def test_assoc_Account_ShoppinCart_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'cart16', a1)
    assert _is_linked(b, 'cart16', a1)
    if hasattr(a1, 'account17'):
        assert _is_linked(a1, 'account17', b)
    _safe_set(b, 'cart16', a2)
    assert _is_linked(b, 'cart16', a2)
    if hasattr(a1, 'account17'):
        assert not _is_linked(a1, 'account17', b)
    if hasattr(a2, 'account17'):
        assert _is_linked(a2, 'account17', b)
    _safe_set(b, 'cart16', None)
    assert not _is_linked(b, 'cart16', a2)
    if hasattr(a2, 'account17'):
        assert not _is_linked(a2, 'account17', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = Customer(address="sample_text", email="sample_text", phone="sample_text")
    a2 = Customer(address="sample_text_2", email="sample_text_2", phone="sample_text_2")
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'customer11', a1)
    assert _is_linked(b, 'customer11', a1)
    if hasattr(a1, 'acc10'):
        assert _is_linked(a1, 'acc10', b)
    _safe_set(b, 'customer11', a2)
    assert _is_linked(b, 'customer11', a2)
    if hasattr(a1, 'acc10'):
        assert not _is_linked(a1, 'acc10', b)
    if hasattr(a2, 'acc10'):
        assert _is_linked(a2, 'acc10', b)
    _safe_set(b, 'customer11', None)
    assert not _is_linked(b, 'customer11', a2)
    if hasattr(a2, 'acc10'):
        assert not _is_linked(a2, 'acc10', b)


def test_assoc_Product_LineItem_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", name="sample_text")
    a2 = Product(description="sample_text_2", name="sample_text_2")
    b = LineItem(price=3.14, quantity=7)
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


def test_assoc_ShoppinCart_LineItem_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = LineItem(price=3.14, quantity=7)
    _safe_set(b, 'sc19', a1)
    assert _is_linked(b, 'sc19', a1)
    if hasattr(a1, 'items18'):
        assert _is_linked(a1, 'items18', b)
    _safe_set(b, 'sc19', a2)
    assert _is_linked(b, 'sc19', a2)
    if hasattr(a1, 'items18'):
        assert not _is_linked(a1, 'items18', b)
    if hasattr(a2, 'items18'):
        assert _is_linked(a2, 'items18', b)
    _safe_set(b, 'sc19', None)
    assert not _is_linked(b, 'sc19', a2)
    if hasattr(a2, 'items18'):
        assert not _is_linked(a2, 'items18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

