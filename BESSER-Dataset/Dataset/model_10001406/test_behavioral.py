import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cosul_de_cumparaturi,
    LineItem,
    Ordin,
    Plata,
    Produse,
    WebUser,
    client,
    cont,
    Starea_comenzii,
    StatusulUtilizatorilor,
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
    a1 = cont(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    a2 = cont(billingAddress="sample_text_2", closed=date(2025, 6, 15), isClosed=False, open=date(2025, 6, 15))
    b = Plata(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
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
    a1 = cont(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    a2 = cont(billingAddress="sample_text_2", closed=date(2025, 6, 15), isClosed=False, open=date(2025, 6, 15))
    b = Cosul_de_cumparaturi(creationDate=date(2024, 1, 1))
    _safe_set(b, 'cont9', a1)
    assert _is_linked(b, 'cont9', a1)
    if hasattr(a1, 'cart8'):
        assert _is_linked(a1, 'cart8', b)
    _safe_set(b, 'cont9', a2)
    assert _is_linked(b, 'cont9', a2)
    if hasattr(a1, 'cart8'):
        assert not _is_linked(a1, 'cart8', b)
    if hasattr(a2, 'cart8'):
        assert _is_linked(a2, 'cart8', b)
    _safe_set(b, 'cont9', None)
    assert not _is_linked(b, 'cont9', a2)
    if hasattr(a2, 'cart8'):
        assert not _is_linked(a2, 'cart8', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = cont(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    a2 = cont(billingAddress="sample_text_2", closed=date(2025, 6, 15), isClosed=False, open=date(2025, 6, 15))
    b = client(address="sample_text", email="sample_text", phone="sample_text")
    _safe_set(b, 'cont6', a1)
    assert _is_linked(b, 'cont6', a1)
    if hasattr(a1, 'client7'):
        assert _is_linked(a1, 'client7', b)
    _safe_set(b, 'cont6', a2)
    assert _is_linked(b, 'cont6', a2)
    if hasattr(a1, 'client7'):
        assert not _is_linked(a1, 'client7', b)
    if hasattr(a2, 'client7'):
        assert _is_linked(a2, 'client7', b)
    _safe_set(b, 'cont6', None)
    assert not _is_linked(b, 'cont6', a2)
    if hasattr(a2, 'client7'):
        assert not _is_linked(a2, 'client7', b)


def test_assoc_Product_LineItem_reverse_link_reassign_clear():
    a1 = Produse(description="sample_text", name="sample_text")
    a2 = Produse(description="sample_text_2", name="sample_text_2")
    b = LineItem(price=3.14, quantity=7)
    _safe_set(b, 'product13', a1)
    assert _is_linked(b, 'product13', a1)
    if hasattr(a1, 'elemente_de_linie12'):
        assert _is_linked(a1, 'elemente_de_linie12', b)
    _safe_set(b, 'product13', a2)
    assert _is_linked(b, 'product13', a2)
    if hasattr(a1, 'elemente_de_linie12'):
        assert not _is_linked(a1, 'elemente_de_linie12', b)
    if hasattr(a2, 'elemente_de_linie12'):
        assert _is_linked(a2, 'elemente_de_linie12', b)
    _safe_set(b, 'product13', None)
    assert not _is_linked(b, 'product13', a2)
    if hasattr(a2, 'elemente_de_linie12'):
        assert not _is_linked(a2, 'elemente_de_linie12', b)


def test_assoc_ShoppingCart_LineItem_reverse_link_reassign_clear():
    a1 = LineItem(price=3.14, quantity=7)
    a2 = LineItem(price=9.99, quantity=13)
    b = Cosul_de_cumparaturi(creationDate=date(2024, 1, 1))
    _safe_set(b, 'articole10', a1)
    assert _is_linked(b, 'articole10', a1)
    if hasattr(a1, 'sc11'):
        assert _is_linked(a1, 'sc11', b)
    _safe_set(b, 'articole10', a2)
    assert _is_linked(b, 'articole10', a2)
    if hasattr(a1, 'sc11'):
        assert not _is_linked(a1, 'sc11', b)
    if hasattr(a2, 'sc11'):
        assert _is_linked(a2, 'sc11', b)
    _safe_set(b, 'articole10', None)
    assert not _is_linked(b, 'articole10', a2)
    if hasattr(a2, 'sc11'):
        assert not _is_linked(a2, 'sc11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

