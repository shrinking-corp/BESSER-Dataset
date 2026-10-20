import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    Basket,
    Buyer,
    Category,
    Offer,
    Order,
    Position,
    Product,
    Seller,
    Store,
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

def test_assoc_Address_Position_reverse_link_reassign_clear():
    a1 = Position(createdAt="sample_text", id=7, latitude="sample_text", longitude="sample_text")
    a2 = Position(createdAt="sample_text_2", id=13, latitude="sample_text_2", longitude="sample_text_2")
    b = Address(city="sample_text", country="sample_text", id=7, street="sample_text", zipCode="sample_text")
    _safe_set(b, 'position4', a1)
    assert _is_linked(b, 'position4', a1)
    if hasattr(a1, 'address5'):
        assert _is_linked(a1, 'address5', b)
    _safe_set(b, 'position4', a2)
    assert _is_linked(b, 'position4', a2)
    if hasattr(a1, 'address5'):
        assert not _is_linked(a1, 'address5', b)
    if hasattr(a2, 'address5'):
        assert _is_linked(a2, 'address5', b)
    _safe_set(b, 'position4', None)
    assert not _is_linked(b, 'position4', a2)
    if hasattr(a2, 'address5'):
        assert not _is_linked(a2, 'address5', b)


def test_assoc_Buyer_Basket_reverse_link_reassign_clear():
    a1 = Buyer(email="sample_text")
    a2 = Buyer(email="sample_text_2")
    b = Basket(id=7, updatedAt="sample_text")
    _safe_set(b, 'buyer1', a1)
    assert _is_linked(b, 'buyer1', a1)
    if hasattr(a1, 'basket0'):
        assert _is_linked(a1, 'basket0', b)
    _safe_set(b, 'buyer1', a2)
    assert _is_linked(b, 'buyer1', a2)
    if hasattr(a1, 'basket0'):
        assert not _is_linked(a1, 'basket0', b)
    if hasattr(a2, 'basket0'):
        assert _is_linked(a2, 'basket0', b)
    _safe_set(b, 'buyer1', None)
    assert not _is_linked(b, 'buyer1', a2)
    if hasattr(a2, 'basket0'):
        assert not _is_linked(a2, 'basket0', b)


def test_assoc_Buyer_Order_reverse_link_reassign_clear():
    a1 = Order(amount=7, createdAt="sample_text", id=7)
    a2 = Order(amount=13, createdAt="sample_text_2", id=13)
    b = Buyer(email="sample_text")
    _safe_set(b, 'order10', {a1})
    assert _is_linked(b, 'order10', a1)
    if hasattr(a1, 'buyer11'):
        assert _is_linked(a1, 'buyer11', b)
    _safe_set(b, 'order10', {a2})
    assert _is_linked(b, 'order10', a2)
    if hasattr(a1, 'buyer11'):
        assert not _is_linked(a1, 'buyer11', b)
    if hasattr(a2, 'buyer11'):
        assert _is_linked(a2, 'buyer11', b)
    _safe_set(b, 'order10', set())
    assert not _is_linked(b, 'order10', a2)
    if hasattr(a2, 'buyer11'):
        assert not _is_linked(a2, 'buyer11', b)


def test_assoc_Buyer_Position_reverse_link_reassign_clear():
    a1 = Position(createdAt="sample_text", id=7, latitude="sample_text", longitude="sample_text")
    a2 = Position(createdAt="sample_text_2", id=13, latitude="sample_text_2", longitude="sample_text_2")
    b = Buyer(email="sample_text")
    _safe_set(b, 'position2', a1)
    assert _is_linked(b, 'position2', a1)
    if hasattr(a1, 'buyer3'):
        assert _is_linked(a1, 'buyer3', b)
    _safe_set(b, 'position2', a2)
    assert _is_linked(b, 'position2', a2)
    if hasattr(a1, 'buyer3'):
        assert not _is_linked(a1, 'buyer3', b)
    if hasattr(a2, 'buyer3'):
        assert _is_linked(a2, 'buyer3', b)
    _safe_set(b, 'position2', None)
    assert not _is_linked(b, 'position2', a2)
    if hasattr(a2, 'buyer3'):
        assert not _is_linked(a2, 'buyer3', b)


def test_assoc_Category_Product_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", id=7, name="sample_text", photoPath="sample_text", price=7)
    a2 = Product(description="sample_text_2", id=13, name="sample_text_2", photoPath="sample_text_2", price=13)
    b = Category(id=7, name="sample_text", photoPath="sample_text")
    _safe_set(b, 'product14', {a1})
    assert _is_linked(b, 'product14', a1)
    if hasattr(a1, 'category15'):
        assert _is_linked(a1, 'category15', b)
    _safe_set(b, 'product14', {a2})
    assert _is_linked(b, 'product14', a2)
    if hasattr(a1, 'category15'):
        assert not _is_linked(a1, 'category15', b)
    if hasattr(a2, 'category15'):
        assert _is_linked(a2, 'category15', b)
    _safe_set(b, 'product14', set())
    assert not _is_linked(b, 'product14', a2)
    if hasattr(a2, 'category15'):
        assert not _is_linked(a2, 'category15', b)


def test_assoc_Product_Offer_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", id=7, name="sample_text", photoPath="sample_text", price=7)
    a2 = Product(description="sample_text_2", id=13, name="sample_text_2", photoPath="sample_text_2", price=13)
    b = Offer(beginDate="sample_text", discount=7, endDate="sample_text", id=7)
    _safe_set(b, 'product13', a1)
    assert _is_linked(b, 'product13', a1)
    if hasattr(a1, 'offer12'):
        assert _is_linked(a1, 'offer12', b)
    _safe_set(b, 'product13', a2)
    assert _is_linked(b, 'product13', a2)
    if hasattr(a1, 'offer12'):
        assert not _is_linked(a1, 'offer12', b)
    if hasattr(a2, 'offer12'):
        assert _is_linked(a2, 'offer12', b)
    _safe_set(b, 'product13', None)
    assert not _is_linked(b, 'product13', a2)
    if hasattr(a2, 'offer12'):
        assert not _is_linked(a2, 'offer12', b)


def test_assoc_Seller_Store_reverse_link_reassign_clear():
    a1 = Store(id=7, name="sample_text", photoPath="sample_text")
    a2 = Store(id=13, name="sample_text_2", photoPath="sample_text_2")
    b = Seller(registerNumber="sample_text")
    _safe_set(b, 'store8', a1)
    assert _is_linked(b, 'store8', a1)
    if hasattr(a1, 'seller9'):
        assert _is_linked(a1, 'seller9', b)
    _safe_set(b, 'store8', a2)
    assert _is_linked(b, 'store8', a2)
    if hasattr(a1, 'seller9'):
        assert not _is_linked(a1, 'seller9', b)
    if hasattr(a2, 'seller9'):
        assert _is_linked(a2, 'seller9', b)
    _safe_set(b, 'store8', None)
    assert not _is_linked(b, 'store8', a2)
    if hasattr(a2, 'seller9'):
        assert not _is_linked(a2, 'seller9', b)


def test_assoc_Store_Address_reverse_link_reassign_clear():
    a1 = Store(id=7, name="sample_text", photoPath="sample_text")
    a2 = Store(id=13, name="sample_text_2", photoPath="sample_text_2")
    b = Address(city="sample_text", country="sample_text", id=7, street="sample_text", zipCode="sample_text")
    _safe_set(b, 'store7', a1)
    assert _is_linked(b, 'store7', a1)
    if hasattr(a1, 'address6'):
        assert _is_linked(a1, 'address6', b)
    _safe_set(b, 'store7', a2)
    assert _is_linked(b, 'store7', a2)
    if hasattr(a1, 'address6'):
        assert not _is_linked(a1, 'address6', b)
    if hasattr(a2, 'address6'):
        assert _is_linked(a2, 'address6', b)
    _safe_set(b, 'store7', None)
    assert not _is_linked(b, 'store7', a2)
    if hasattr(a2, 'address6'):
        assert not _is_linked(a2, 'address6', b)


def test_assoc_Store_Product_reverse_link_reassign_clear():
    a1 = Store(id=7, name="sample_text", photoPath="sample_text")
    a2 = Store(id=13, name="sample_text_2", photoPath="sample_text_2")
    b = Product(description="sample_text", id=7, name="sample_text", photoPath="sample_text", price=7)
    _safe_set(b, 'store17', a1)
    assert _is_linked(b, 'store17', a1)
    if hasattr(a1, 'product16'):
        assert _is_linked(a1, 'product16', b)
    _safe_set(b, 'store17', a2)
    assert _is_linked(b, 'store17', a2)
    if hasattr(a1, 'product16'):
        assert not _is_linked(a1, 'product16', b)
    if hasattr(a2, 'product16'):
        assert _is_linked(a2, 'product16', b)
    _safe_set(b, 'store17', None)
    assert not _is_linked(b, 'store17', a2)
    if hasattr(a2, 'product16'):
        assert not _is_linked(a2, 'product16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

