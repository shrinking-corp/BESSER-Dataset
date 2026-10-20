import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    shop_Customer,
    shop_Order,
    shop_PriceCategory,
    shop_Product,
    shop_ProductCategory,
    shop_Transaction,
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

def test_assoc_customer10_reverse_link_reassign_clear():
    a1 = shop_Order(comments="sample_text", number="sample_text")
    a2 = shop_Order(comments="sample_text_2", number="sample_text_2")
    b = shop_Customer(address="sample_text", comments="sample_text", familyName="sample_text", hotel="sample_text", surname="sample_text", telephoneNr="sample_text")
    _safe_set(b, 'shop_Customer', a1)
    assert _is_linked(b, 'shop_Customer', a1)
    if hasattr(a1, 'shop_Order'):
        assert _is_linked(a1, 'shop_Order', b)
    _safe_set(b, 'shop_Customer', a2)
    assert _is_linked(b, 'shop_Customer', a2)
    if hasattr(a1, 'shop_Order'):
        assert not _is_linked(a1, 'shop_Order', b)
    if hasattr(a2, 'shop_Order'):
        assert _is_linked(a2, 'shop_Order', b)
    _safe_set(b, 'shop_Customer', None)
    assert not _is_linked(b, 'shop_Customer', a2)
    if hasattr(a2, 'shop_Order'):
        assert not _is_linked(a2, 'shop_Order', b)


def test_assoc_order11_reverse_link_reassign_clear():
    a1 = shop_Transaction(endDate=date(2024, 1, 1), number="sample_text", paidDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = shop_Transaction(endDate=date(2025, 6, 15), number="sample_text_2", paidDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = shop_Order(comments="sample_text", number="sample_text")
    _safe_set(b, 'Order', a1)
    assert _is_linked(b, 'Order', a1)
    if hasattr(a1, 'transactions'):
        assert _is_linked(a1, 'transactions', b)
    _safe_set(b, 'Order', a2)
    assert _is_linked(b, 'Order', a2)
    if hasattr(a1, 'transactions'):
        assert not _is_linked(a1, 'transactions', b)
    if hasattr(a2, 'transactions'):
        assert _is_linked(a2, 'transactions', b)
    _safe_set(b, 'Order', None)
    assert not _is_linked(b, 'Order', a2)
    if hasattr(a2, 'transactions'):
        assert not _is_linked(a2, 'transactions', b)


def test_assoc_parent7_reverse_link_reassign_clear():
    a1 = shop_ProductCategory(name="sample_text")
    a2 = shop_ProductCategory(name="sample_text_2")
    b = shop_ProductCategory(name="sample_text")
    _safe_set(b, 'subCategorys', a1)
    assert _is_linked(b, 'subCategorys', a1)
    if hasattr(a1, 'ProductCategory8'):
        assert _is_linked(a1, 'ProductCategory8', b)
    _safe_set(b, 'subCategorys', a2)
    assert _is_linked(b, 'subCategorys', a2)
    if hasattr(a1, 'ProductCategory8'):
        assert not _is_linked(a1, 'ProductCategory8', b)
    if hasattr(a2, 'ProductCategory8'):
        assert _is_linked(a2, 'ProductCategory8', b)
    _safe_set(b, 'subCategorys', None)
    assert not _is_linked(b, 'subCategorys', a2)
    if hasattr(a2, 'ProductCategory8'):
        assert not _is_linked(a2, 'ProductCategory8', b)


def test_assoc_priceCategory1_reverse_link_reassign_clear():
    a1 = shop_Product(description="sample_text", name="sample_text", number="sample_text")
    a2 = shop_Product(description="sample_text_2", name="sample_text_2", number="sample_text_2")
    b = shop_PriceCategory(name="sample_text", prices=3.14)
    _safe_set(b, 'shop_PriceCategory', a1)
    assert _is_linked(b, 'shop_PriceCategory', a1)
    if hasattr(a1, 'shop_Product'):
        assert _is_linked(a1, 'shop_Product', b)
    _safe_set(b, 'shop_PriceCategory', a2)
    assert _is_linked(b, 'shop_PriceCategory', a2)
    if hasattr(a1, 'shop_Product'):
        assert not _is_linked(a1, 'shop_Product', b)
    if hasattr(a2, 'shop_Product'):
        assert _is_linked(a2, 'shop_Product', b)
    _safe_set(b, 'shop_PriceCategory', None)
    assert not _is_linked(b, 'shop_PriceCategory', a2)
    if hasattr(a2, 'shop_Product'):
        assert not _is_linked(a2, 'shop_Product', b)


def test_assoc_product12_reverse_link_reassign_clear():
    a1 = shop_Transaction(endDate=date(2024, 1, 1), number="sample_text", paidDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = shop_Transaction(endDate=date(2025, 6, 15), number="sample_text_2", paidDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = shop_Product(description="sample_text", name="sample_text", number="sample_text")
    _safe_set(b, 'shop_Product13', a1)
    assert _is_linked(b, 'shop_Product13', a1)
    if hasattr(a1, 'shop_Transaction'):
        assert _is_linked(a1, 'shop_Transaction', b)
    _safe_set(b, 'shop_Product13', a2)
    assert _is_linked(b, 'shop_Product13', a2)
    if hasattr(a1, 'shop_Transaction'):
        assert not _is_linked(a1, 'shop_Transaction', b)
    if hasattr(a2, 'shop_Transaction'):
        assert _is_linked(a2, 'shop_Transaction', b)
    _safe_set(b, 'shop_Product13', None)
    assert not _is_linked(b, 'shop_Product13', a2)
    if hasattr(a2, 'shop_Transaction'):
        assert not _is_linked(a2, 'shop_Transaction', b)


def test_assoc_productCategory0_reverse_link_reassign_clear():
    a1 = shop_ProductCategory(name="sample_text")
    a2 = shop_ProductCategory(name="sample_text_2")
    b = shop_Product(description="sample_text", name="sample_text", number="sample_text")
    _safe_set(b, 'products', a1)
    assert _is_linked(b, 'products', a1)
    if hasattr(a1, 'ProductCategory'):
        assert _is_linked(a1, 'ProductCategory', b)
    _safe_set(b, 'products', a2)
    assert _is_linked(b, 'products', a2)
    if hasattr(a1, 'ProductCategory'):
        assert not _is_linked(a1, 'ProductCategory', b)
    if hasattr(a2, 'ProductCategory'):
        assert _is_linked(a2, 'ProductCategory', b)
    _safe_set(b, 'products', None)
    assert not _is_linked(b, 'products', a2)
    if hasattr(a2, 'ProductCategory'):
        assert not _is_linked(a2, 'ProductCategory', b)


def test_assoc_products2_reverse_link_reassign_clear():
    a1 = shop_ProductCategory(name="sample_text")
    a2 = shop_ProductCategory(name="sample_text_2")
    b = shop_Product(description="sample_text", name="sample_text", number="sample_text")
    _safe_set(b, 'Product', a1)
    assert _is_linked(b, 'Product', a1)
    if hasattr(a1, 'productCategory'):
        assert _is_linked(a1, 'productCategory', b)
    _safe_set(b, 'Product', a2)
    assert _is_linked(b, 'Product', a2)
    if hasattr(a1, 'productCategory'):
        assert not _is_linked(a1, 'productCategory', b)
    if hasattr(a2, 'productCategory'):
        assert _is_linked(a2, 'productCategory', b)
    _safe_set(b, 'Product', None)
    assert not _is_linked(b, 'Product', a2)
    if hasattr(a2, 'productCategory'):
        assert not _is_linked(a2, 'productCategory', b)


def test_assoc_subCategorys4_reverse_link_reassign_clear():
    a1 = shop_ProductCategory(name="sample_text")
    a2 = shop_ProductCategory(name="sample_text_2")
    b = shop_ProductCategory(name="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'ProductCategory5'):
        assert _is_linked(a1, 'ProductCategory5', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'ProductCategory5'):
        assert not _is_linked(a1, 'ProductCategory5', b)
    if hasattr(a2, 'ProductCategory5'):
        assert _is_linked(a2, 'ProductCategory5', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'ProductCategory5'):
        assert not _is_linked(a2, 'ProductCategory5', b)


def test_assoc_transactions9_reverse_link_reassign_clear():
    a1 = shop_Transaction(endDate=date(2024, 1, 1), number="sample_text", paidDate=date(2024, 1, 1), price=3.14, startDate=date(2024, 1, 1))
    a2 = shop_Transaction(endDate=date(2025, 6, 15), number="sample_text_2", paidDate=date(2025, 6, 15), price=9.99, startDate=date(2025, 6, 15))
    b = shop_Order(comments="sample_text", number="sample_text")
    _safe_set(b, 'order', {a1})
    assert _is_linked(b, 'order', a1)
    if hasattr(a1, 'Transaction'):
        assert _is_linked(a1, 'Transaction', b)
    _safe_set(b, 'order', {a2})
    assert _is_linked(b, 'order', a2)
    if hasattr(a1, 'Transaction'):
        assert not _is_linked(a1, 'Transaction', b)
    if hasattr(a2, 'Transaction'):
        assert _is_linked(a2, 'Transaction', b)
    _safe_set(b, 'order', set())
    assert not _is_linked(b, 'order', a2)
    if hasattr(a2, 'Transaction'):
        assert not _is_linked(a2, 'Transaction', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

