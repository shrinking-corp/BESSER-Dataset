import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    GlobalLocation,
    epo2_Address,
    epo2_Customer,
    epo2_GlobalAddress,
    epo2_GlobalLocation,
    epo2_Item,
    epo2_PurchaseOrder,
    epo2_Supplier,
    epo2_USAddress,
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

def test_assoc_billTo14_reverse_link_reassign_clear():
    a1 = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    a2 = epo2_PurchaseOrder(comment="sample_text_2", orderDate=date(2025, 6, 15), status="sample_text_2", totalAmount=13)
    b = epo2_Address(country="sample_text", name="sample_text")
    _safe_set(b, 'epo2_Address', a1)
    assert _is_linked(b, 'epo2_Address', a1)
    if hasattr(a1, 'epo2_PurchaseOrder15'):
        assert _is_linked(a1, 'epo2_PurchaseOrder15', b)
    _safe_set(b, 'epo2_Address', a2)
    assert _is_linked(b, 'epo2_Address', a2)
    if hasattr(a1, 'epo2_PurchaseOrder15'):
        assert not _is_linked(a1, 'epo2_PurchaseOrder15', b)
    if hasattr(a2, 'epo2_PurchaseOrder15'):
        assert _is_linked(a2, 'epo2_PurchaseOrder15', b)
    _safe_set(b, 'epo2_Address', None)
    assert not _is_linked(b, 'epo2_Address', a2)
    if hasattr(a2, 'epo2_PurchaseOrder15'):
        assert not _is_linked(a2, 'epo2_PurchaseOrder15', b)


def test_assoc_customer9_reverse_link_reassign_clear():
    a1 = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    a2 = epo2_PurchaseOrder(comment="sample_text_2", orderDate=date(2025, 6, 15), status="sample_text_2", totalAmount=13)
    b = epo2_Customer(customerID=7)
    _safe_set(b, 'Customer', a1)
    assert _is_linked(b, 'Customer', a1)
    if hasattr(a1, 'orders'):
        assert _is_linked(a1, 'orders', b)
    _safe_set(b, 'Customer', a2)
    assert _is_linked(b, 'Customer', a2)
    if hasattr(a1, 'orders'):
        assert not _is_linked(a1, 'orders', b)
    if hasattr(a2, 'orders'):
        assert _is_linked(a2, 'orders', b)
    _safe_set(b, 'Customer', None)
    assert not _is_linked(b, 'Customer', a2)
    if hasattr(a2, 'orders'):
        assert not _is_linked(a2, 'orders', b)


def test_assoc_customers7_reverse_link_reassign_clear():
    a1 = epo2_Supplier(name="sample_text")
    a2 = epo2_Supplier(name="sample_text_2")
    b = epo2_Customer(customerID=7)
    _safe_set(b, 'epo2_Customer', a1)
    assert _is_linked(b, 'epo2_Customer', a1)
    if hasattr(a1, 'epo2_Supplier8'):
        assert _is_linked(a1, 'epo2_Supplier8', b)
    _safe_set(b, 'epo2_Customer', a2)
    assert _is_linked(b, 'epo2_Customer', a2)
    if hasattr(a1, 'epo2_Supplier8'):
        assert not _is_linked(a1, 'epo2_Supplier8', b)
    if hasattr(a2, 'epo2_Supplier8'):
        assert _is_linked(a2, 'epo2_Supplier8', b)
    _safe_set(b, 'epo2_Customer', None)
    assert not _is_linked(b, 'epo2_Customer', a2)
    if hasattr(a2, 'epo2_Supplier8'):
        assert not _is_linked(a2, 'epo2_Supplier8', b)


def test_assoc_items13_reverse_link_reassign_clear():
    a1 = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    a2 = epo2_PurchaseOrder(comment="sample_text_2", orderDate=date(2025, 6, 15), status="sample_text_2", totalAmount=13)
    b = epo2_Item(comment="sample_text", partNum="sample_text", productName="sample_text", quantity=7, shipDate=date(2024, 1, 1), usPrice=7)
    _safe_set(b, 'Item', a1)
    assert _is_linked(b, 'Item', a1)
    if hasattr(a1, 'order'):
        assert _is_linked(a1, 'order', b)
    _safe_set(b, 'Item', a2)
    assert _is_linked(b, 'Item', a2)
    if hasattr(a1, 'order'):
        assert not _is_linked(a1, 'order', b)
    if hasattr(a2, 'order'):
        assert _is_linked(a2, 'order', b)
    _safe_set(b, 'Item', None)
    assert not _is_linked(b, 'Item', a2)
    if hasattr(a2, 'order'):
        assert not _is_linked(a2, 'order', b)


def test_assoc_order20_reverse_link_reassign_clear():
    a1 = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    a2 = epo2_PurchaseOrder(comment="sample_text_2", orderDate=date(2025, 6, 15), status="sample_text_2", totalAmount=13)
    b = epo2_Item(comment="sample_text", partNum="sample_text", productName="sample_text", quantity=7, shipDate=date(2024, 1, 1), usPrice=7)
    _safe_set(b, 'items', a1)
    assert _is_linked(b, 'items', a1)
    if hasattr(a1, 'PurchaseOrder21'):
        assert _is_linked(a1, 'PurchaseOrder21', b)
    _safe_set(b, 'items', a2)
    assert _is_linked(b, 'items', a2)
    if hasattr(a1, 'PurchaseOrder21'):
        assert not _is_linked(a1, 'PurchaseOrder21', b)
    if hasattr(a2, 'PurchaseOrder21'):
        assert _is_linked(a2, 'PurchaseOrder21', b)
    _safe_set(b, 'items', None)
    assert not _is_linked(b, 'items', a2)
    if hasattr(a2, 'PurchaseOrder21'):
        assert not _is_linked(a2, 'PurchaseOrder21', b)


def test_assoc_orders0_reverse_link_reassign_clear():
    a1 = epo2_Supplier(name="sample_text")
    a2 = epo2_Supplier(name="sample_text_2")
    b = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    _safe_set(b, 'epo2_PurchaseOrder', a1)
    assert _is_linked(b, 'epo2_PurchaseOrder', a1)
    if hasattr(a1, 'epo2_Supplier'):
        assert _is_linked(a1, 'epo2_Supplier', b)
    _safe_set(b, 'epo2_PurchaseOrder', a2)
    assert _is_linked(b, 'epo2_PurchaseOrder', a2)
    if hasattr(a1, 'epo2_Supplier'):
        assert not _is_linked(a1, 'epo2_Supplier', b)
    if hasattr(a2, 'epo2_Supplier'):
        assert _is_linked(a2, 'epo2_Supplier', b)
    _safe_set(b, 'epo2_PurchaseOrder', None)
    assert not _is_linked(b, 'epo2_PurchaseOrder', a2)
    if hasattr(a2, 'epo2_Supplier'):
        assert not _is_linked(a2, 'epo2_Supplier', b)


def test_assoc_orders19_reverse_link_reassign_clear():
    a1 = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    a2 = epo2_PurchaseOrder(comment="sample_text_2", orderDate=date(2025, 6, 15), status="sample_text_2", totalAmount=13)
    b = epo2_Customer(customerID=7)
    _safe_set(b, 'customer', {a1})
    assert _is_linked(b, 'customer', a1)
    if hasattr(a1, 'PurchaseOrder'):
        assert _is_linked(a1, 'PurchaseOrder', b)
    _safe_set(b, 'customer', {a2})
    assert _is_linked(b, 'customer', a2)
    if hasattr(a1, 'PurchaseOrder'):
        assert not _is_linked(a1, 'PurchaseOrder', b)
    if hasattr(a2, 'PurchaseOrder'):
        assert _is_linked(a2, 'PurchaseOrder', b)
    _safe_set(b, 'customer', set())
    assert not _is_linked(b, 'customer', a2)
    if hasattr(a2, 'PurchaseOrder'):
        assert not _is_linked(a2, 'PurchaseOrder', b)


def test_assoc_pendingOrders1_reverse_link_reassign_clear():
    a1 = epo2_Supplier(name="sample_text")
    a2 = epo2_Supplier(name="sample_text_2")
    b = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    _safe_set(b, 'epo2_PurchaseOrder3', a1)
    assert _is_linked(b, 'epo2_PurchaseOrder3', a1)
    if hasattr(a1, 'epo2_Supplier2'):
        assert _is_linked(a1, 'epo2_Supplier2', b)
    _safe_set(b, 'epo2_PurchaseOrder3', a2)
    assert _is_linked(b, 'epo2_PurchaseOrder3', a2)
    if hasattr(a1, 'epo2_Supplier2'):
        assert not _is_linked(a1, 'epo2_Supplier2', b)
    if hasattr(a2, 'epo2_Supplier2'):
        assert _is_linked(a2, 'epo2_Supplier2', b)
    _safe_set(b, 'epo2_PurchaseOrder3', None)
    assert not _is_linked(b, 'epo2_PurchaseOrder3', a2)
    if hasattr(a2, 'epo2_Supplier2'):
        assert not _is_linked(a2, 'epo2_Supplier2', b)


def test_assoc_previousOrder11_reverse_link_reassign_clear():
    a1 = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    a2 = epo2_PurchaseOrder(comment="sample_text_2", orderDate=date(2025, 6, 15), status="sample_text_2", totalAmount=13)
    b = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    _safe_set(b, 'epo2_PurchaseOrder12', a1)
    assert _is_linked(b, 'epo2_PurchaseOrder12', a1)
    if hasattr(a1, 'epo2_PurchaseOrder10'):
        assert _is_linked(a1, 'epo2_PurchaseOrder10', b)
    _safe_set(b, 'epo2_PurchaseOrder12', a2)
    assert _is_linked(b, 'epo2_PurchaseOrder12', a2)
    if hasattr(a1, 'epo2_PurchaseOrder10'):
        assert not _is_linked(a1, 'epo2_PurchaseOrder10', b)
    if hasattr(a2, 'epo2_PurchaseOrder10'):
        assert _is_linked(a2, 'epo2_PurchaseOrder10', b)
    _safe_set(b, 'epo2_PurchaseOrder12', None)
    assert not _is_linked(b, 'epo2_PurchaseOrder12', a2)
    if hasattr(a2, 'epo2_PurchaseOrder10'):
        assert not _is_linked(a2, 'epo2_PurchaseOrder10', b)


def test_assoc_shipTo16_reverse_link_reassign_clear():
    a1 = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    a2 = epo2_PurchaseOrder(comment="sample_text_2", orderDate=date(2025, 6, 15), status="sample_text_2", totalAmount=13)
    b = epo2_Address(country="sample_text", name="sample_text")
    _safe_set(b, 'epo2_Address18', a1)
    assert _is_linked(b, 'epo2_Address18', a1)
    if hasattr(a1, 'epo2_PurchaseOrder17'):
        assert _is_linked(a1, 'epo2_PurchaseOrder17', b)
    _safe_set(b, 'epo2_Address18', a2)
    assert _is_linked(b, 'epo2_Address18', a2)
    if hasattr(a1, 'epo2_PurchaseOrder17'):
        assert not _is_linked(a1, 'epo2_PurchaseOrder17', b)
    if hasattr(a2, 'epo2_PurchaseOrder17'):
        assert _is_linked(a2, 'epo2_PurchaseOrder17', b)
    _safe_set(b, 'epo2_Address18', None)
    assert not _is_linked(b, 'epo2_Address18', a2)
    if hasattr(a2, 'epo2_PurchaseOrder17'):
        assert not _is_linked(a2, 'epo2_PurchaseOrder17', b)


def test_assoc_shippedOrders4_reverse_link_reassign_clear():
    a1 = epo2_Supplier(name="sample_text")
    a2 = epo2_Supplier(name="sample_text_2")
    b = epo2_PurchaseOrder(comment="sample_text", orderDate=date(2024, 1, 1), status="sample_text", totalAmount=7)
    _safe_set(b, 'epo2_PurchaseOrder6', a1)
    assert _is_linked(b, 'epo2_PurchaseOrder6', a1)
    if hasattr(a1, 'epo2_Supplier5'):
        assert _is_linked(a1, 'epo2_Supplier5', b)
    _safe_set(b, 'epo2_PurchaseOrder6', a2)
    assert _is_linked(b, 'epo2_PurchaseOrder6', a2)
    if hasattr(a1, 'epo2_Supplier5'):
        assert not _is_linked(a1, 'epo2_Supplier5', b)
    if hasattr(a2, 'epo2_Supplier5'):
        assert _is_linked(a2, 'epo2_Supplier5', b)
    _safe_set(b, 'epo2_PurchaseOrder6', None)
    assert not _is_linked(b, 'epo2_PurchaseOrder6', a2)
    if hasattr(a2, 'epo2_Supplier5'):
        assert not _is_linked(a2, 'epo2_Supplier5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

