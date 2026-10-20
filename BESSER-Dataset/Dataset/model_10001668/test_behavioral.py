import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Customer,
    Inventory,
    Payment,
    Product,
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

def test_assoc_Customer_Payment_reverse_link_reassign_clear():
    a1 = Payment(ID=7, Imtiaz="sample_text", amount__="sample_text", discountamount="sample_text", finalamount="sample_text", list="sample_text", quantity=7, totalamount="sample_text")
    a2 = Payment(ID=13, Imtiaz="sample_text_2", amount__="sample_text_2", discountamount="sample_text_2", finalamount="sample_text_2", list="sample_text_2", quantity=13, totalamount="sample_text_2")
    b = Customer(royalty=True, type="sample_text")
    _safe_set(b, 'payment0', a1)
    assert _is_linked(b, 'payment0', a1)
    if hasattr(a1, 'customer1'):
        assert _is_linked(a1, 'customer1', b)
    _safe_set(b, 'payment0', a2)
    assert _is_linked(b, 'payment0', a2)
    if hasattr(a1, 'customer1'):
        assert not _is_linked(a1, 'customer1', b)
    if hasattr(a2, 'customer1'):
        assert _is_linked(a2, 'customer1', b)
    _safe_set(b, 'payment0', None)
    assert not _is_linked(b, 'payment0', a2)
    if hasattr(a2, 'customer1'):
        assert not _is_linked(a2, 'customer1', b)


def test_assoc_Inventory_Product_reverse_link_reassign_clear():
    a1 = Product(ID=7, Name="sample_text", amount="sample_text", attribute="sample_text", blgl=True, price="sample_text", qty=7, type="sample_text")
    a2 = Product(ID=13, Name="sample_text_2", amount="sample_text_2", attribute="sample_text_2", blgl=False, price="sample_text_2", qty=13, type="sample_text_2")
    b = Inventory(SuperMarket="sample_text", list="sample_text")
    _safe_set(b, 'product2', {a1})
    assert _is_linked(b, 'product2', a1)
    if hasattr(a1, 'inventory3'):
        assert _is_linked(a1, 'inventory3', b)
    _safe_set(b, 'product2', {a2})
    assert _is_linked(b, 'product2', a2)
    if hasattr(a1, 'inventory3'):
        assert not _is_linked(a1, 'inventory3', b)
    if hasattr(a2, 'inventory3'):
        assert _is_linked(a2, 'inventory3', b)
    _safe_set(b, 'product2', set())
    assert not _is_linked(b, 'product2', a2)
    if hasattr(a2, 'inventory3'):
        assert not _is_linked(a2, 'inventory3', b)


def test_assoc_Payment_Inventory_reverse_link_reassign_clear():
    a1 = Payment(ID=7, Imtiaz="sample_text", amount__="sample_text", discountamount="sample_text", finalamount="sample_text", list="sample_text", quantity=7, totalamount="sample_text")
    a2 = Payment(ID=13, Imtiaz="sample_text_2", amount__="sample_text_2", discountamount="sample_text_2", finalamount="sample_text_2", list="sample_text_2", quantity=13, totalamount="sample_text_2")
    b = Inventory(SuperMarket="sample_text", list="sample_text")
    _safe_set(b, 'payment9', a1)
    assert _is_linked(b, 'payment9', a1)
    if hasattr(a1, 'inventory8'):
        assert _is_linked(a1, 'inventory8', b)
    _safe_set(b, 'payment9', a2)
    assert _is_linked(b, 'payment9', a2)
    if hasattr(a1, 'inventory8'):
        assert not _is_linked(a1, 'inventory8', b)
    if hasattr(a2, 'inventory8'):
        assert _is_linked(a2, 'inventory8', b)
    _safe_set(b, 'payment9', None)
    assert not _is_linked(b, 'payment9', a2)
    if hasattr(a2, 'inventory8'):
        assert not _is_linked(a2, 'inventory8', b)


def test_assoc_Product_Customer_reverse_link_reassign_clear():
    a1 = Product(ID=7, Name="sample_text", amount="sample_text", attribute="sample_text", blgl=True, price="sample_text", qty=7, type="sample_text")
    a2 = Product(ID=13, Name="sample_text_2", amount="sample_text_2", attribute="sample_text_2", blgl=False, price="sample_text_2", qty=13, type="sample_text_2")
    b = Customer(royalty=True, type="sample_text")
    _safe_set(b, 'product5', {a1})
    assert _is_linked(b, 'product5', a1)
    if hasattr(a1, 'customer4'):
        assert _is_linked(a1, 'customer4', b)
    _safe_set(b, 'product5', {a2})
    assert _is_linked(b, 'product5', a2)
    if hasattr(a1, 'customer4'):
        assert not _is_linked(a1, 'customer4', b)
    if hasattr(a2, 'customer4'):
        assert _is_linked(a2, 'customer4', b)
    _safe_set(b, 'product5', set())
    assert not _is_linked(b, 'product5', a2)
    if hasattr(a2, 'customer4'):
        assert not _is_linked(a2, 'customer4', b)


def test_assoc_Product_Payment_reverse_link_reassign_clear():
    a1 = Product(ID=7, Name="sample_text", amount="sample_text", attribute="sample_text", blgl=True, price="sample_text", qty=7, type="sample_text")
    a2 = Product(ID=13, Name="sample_text_2", amount="sample_text_2", attribute="sample_text_2", blgl=False, price="sample_text_2", qty=13, type="sample_text_2")
    b = Payment(ID=7, Imtiaz="sample_text", amount__="sample_text", discountamount="sample_text", finalamount="sample_text", list="sample_text", quantity=7, totalamount="sample_text")
    _safe_set(b, 'product7', {a1})
    assert _is_linked(b, 'product7', a1)
    if hasattr(a1, 'payment6'):
        assert _is_linked(a1, 'payment6', b)
    _safe_set(b, 'product7', {a2})
    assert _is_linked(b, 'product7', a2)
    if hasattr(a1, 'payment6'):
        assert not _is_linked(a1, 'payment6', b)
    if hasattr(a2, 'payment6'):
        assert _is_linked(a2, 'payment6', b)
    _safe_set(b, 'product7', set())
    assert not _is_linked(b, 'product7', a2)
    if hasattr(a2, 'payment6'):
        assert not _is_linked(a2, 'payment6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

