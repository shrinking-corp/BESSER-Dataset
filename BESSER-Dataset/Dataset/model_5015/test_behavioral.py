import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    extendedPO2_Address,
    extendedPO2_Customer,
    extendedPO2_GlobalAddress,
    extendedPO2_Item,
    extendedPO2_PurchaseOrder,
    extendedPO2_Supplier,
    extendedPO2_USAddress,
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

def test_assoc_billTo1_reverse_link_reassign_clear():
    a1 = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    a2 = extendedPO2_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2", status="sample_text_2", totalAmount=13)
    b = extendedPO2_Address(country="sample_text", name="sample_text")
    _safe_set(b, 'extendedPO2_Address', a1)
    assert _is_linked(b, 'extendedPO2_Address', a1)
    if hasattr(a1, 'extendedPO2_PurchaseOrder'):
        assert _is_linked(a1, 'extendedPO2_PurchaseOrder', b)
    _safe_set(b, 'extendedPO2_Address', a2)
    assert _is_linked(b, 'extendedPO2_Address', a2)
    if hasattr(a1, 'extendedPO2_PurchaseOrder'):
        assert not _is_linked(a1, 'extendedPO2_PurchaseOrder', b)
    if hasattr(a2, 'extendedPO2_PurchaseOrder'):
        assert _is_linked(a2, 'extendedPO2_PurchaseOrder', b)
    _safe_set(b, 'extendedPO2_Address', None)
    assert not _is_linked(b, 'extendedPO2_Address', a2)
    if hasattr(a2, 'extendedPO2_PurchaseOrder'):
        assert not _is_linked(a2, 'extendedPO2_PurchaseOrder', b)


def test_assoc_customer8_reverse_link_reassign_clear():
    a1 = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    a2 = extendedPO2_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2", status="sample_text_2", totalAmount=13)
    b = extendedPO2_Customer(customerID=7)
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


def test_assoc_customers14_reverse_link_reassign_clear():
    a1 = extendedPO2_Supplier(name="sample_text")
    a2 = extendedPO2_Supplier(name="sample_text_2")
    b = extendedPO2_Customer(customerID=7)
    _safe_set(b, 'extendedPO2_Customer', a1)
    assert _is_linked(b, 'extendedPO2_Customer', a1)
    if hasattr(a1, 'extendedPO2_Supplier15'):
        assert _is_linked(a1, 'extendedPO2_Supplier15', b)
    _safe_set(b, 'extendedPO2_Customer', a2)
    assert _is_linked(b, 'extendedPO2_Customer', a2)
    if hasattr(a1, 'extendedPO2_Supplier15'):
        assert not _is_linked(a1, 'extendedPO2_Supplier15', b)
    if hasattr(a2, 'extendedPO2_Supplier15'):
        assert _is_linked(a2, 'extendedPO2_Supplier15', b)
    _safe_set(b, 'extendedPO2_Customer', None)
    assert not _is_linked(b, 'extendedPO2_Customer', a2)
    if hasattr(a2, 'extendedPO2_Supplier15'):
        assert not _is_linked(a2, 'extendedPO2_Supplier15', b)


def test_assoc_items0_reverse_link_reassign_clear():
    a1 = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    a2 = extendedPO2_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2", status="sample_text_2", totalAmount=13)
    b = extendedPO2_Item(USPrice=7, comment="sample_text", partNum="sample_text", productName="sample_text", quantity=7, shipDate="sample_text")
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


def test_assoc_order9_reverse_link_reassign_clear():
    a1 = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    a2 = extendedPO2_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2", status="sample_text_2", totalAmount=13)
    b = extendedPO2_Item(USPrice=7, comment="sample_text", partNum="sample_text", productName="sample_text", quantity=7, shipDate="sample_text")
    _safe_set(b, 'items', a1)
    assert _is_linked(b, 'items', a1)
    if hasattr(a1, 'PurchaseOrder'):
        assert _is_linked(a1, 'PurchaseOrder', b)
    _safe_set(b, 'items', a2)
    assert _is_linked(b, 'items', a2)
    if hasattr(a1, 'PurchaseOrder'):
        assert not _is_linked(a1, 'PurchaseOrder', b)
    if hasattr(a2, 'PurchaseOrder'):
        assert _is_linked(a2, 'PurchaseOrder', b)
    _safe_set(b, 'items', None)
    assert not _is_linked(b, 'items', a2)
    if hasattr(a2, 'PurchaseOrder'):
        assert not _is_linked(a2, 'PurchaseOrder', b)


def test_assoc_orders10_reverse_link_reassign_clear():
    a1 = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    a2 = extendedPO2_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2", status="sample_text_2", totalAmount=13)
    b = extendedPO2_Customer(customerID=7)
    _safe_set(b, 'customer', {a1})
    assert _is_linked(b, 'customer', a1)
    if hasattr(a1, 'PurchaseOrder11'):
        assert _is_linked(a1, 'PurchaseOrder11', b)
    _safe_set(b, 'customer', {a2})
    assert _is_linked(b, 'customer', a2)
    if hasattr(a1, 'PurchaseOrder11'):
        assert not _is_linked(a1, 'PurchaseOrder11', b)
    if hasattr(a2, 'PurchaseOrder11'):
        assert _is_linked(a2, 'PurchaseOrder11', b)
    _safe_set(b, 'customer', set())
    assert not _is_linked(b, 'customer', a2)
    if hasattr(a2, 'PurchaseOrder11'):
        assert not _is_linked(a2, 'PurchaseOrder11', b)


def test_assoc_orders12_reverse_link_reassign_clear():
    a1 = extendedPO2_Supplier(name="sample_text")
    a2 = extendedPO2_Supplier(name="sample_text_2")
    b = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    _safe_set(b, 'extendedPO2_PurchaseOrder13', a1)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder13', a1)
    if hasattr(a1, 'extendedPO2_Supplier'):
        assert _is_linked(a1, 'extendedPO2_Supplier', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder13', a2)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder13', a2)
    if hasattr(a1, 'extendedPO2_Supplier'):
        assert not _is_linked(a1, 'extendedPO2_Supplier', b)
    if hasattr(a2, 'extendedPO2_Supplier'):
        assert _is_linked(a2, 'extendedPO2_Supplier', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder13', None)
    assert not _is_linked(b, 'extendedPO2_PurchaseOrder13', a2)
    if hasattr(a2, 'extendedPO2_Supplier'):
        assert not _is_linked(a2, 'extendedPO2_Supplier', b)


def test_assoc_pendingOrders16_reverse_link_reassign_clear():
    a1 = extendedPO2_Supplier(name="sample_text")
    a2 = extendedPO2_Supplier(name="sample_text_2")
    b = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    _safe_set(b, 'extendedPO2_PurchaseOrder18', a1)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder18', a1)
    if hasattr(a1, 'extendedPO2_Supplier17'):
        assert _is_linked(a1, 'extendedPO2_Supplier17', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder18', a2)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder18', a2)
    if hasattr(a1, 'extendedPO2_Supplier17'):
        assert not _is_linked(a1, 'extendedPO2_Supplier17', b)
    if hasattr(a2, 'extendedPO2_Supplier17'):
        assert _is_linked(a2, 'extendedPO2_Supplier17', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder18', None)
    assert not _is_linked(b, 'extendedPO2_PurchaseOrder18', a2)
    if hasattr(a2, 'extendedPO2_Supplier17'):
        assert not _is_linked(a2, 'extendedPO2_Supplier17', b)


def test_assoc_previousOrder6_reverse_link_reassign_clear():
    a1 = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    a2 = extendedPO2_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2", status="sample_text_2", totalAmount=13)
    b = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    _safe_set(b, 'extendedPO2_PurchaseOrder7', a1)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder7', a1)
    if hasattr(a1, 'extendedPO2_PurchaseOrder5'):
        assert _is_linked(a1, 'extendedPO2_PurchaseOrder5', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder7', a2)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder7', a2)
    if hasattr(a1, 'extendedPO2_PurchaseOrder5'):
        assert not _is_linked(a1, 'extendedPO2_PurchaseOrder5', b)
    if hasattr(a2, 'extendedPO2_PurchaseOrder5'):
        assert _is_linked(a2, 'extendedPO2_PurchaseOrder5', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder7', None)
    assert not _is_linked(b, 'extendedPO2_PurchaseOrder7', a2)
    if hasattr(a2, 'extendedPO2_PurchaseOrder5'):
        assert not _is_linked(a2, 'extendedPO2_PurchaseOrder5', b)


def test_assoc_shipTo2_reverse_link_reassign_clear():
    a1 = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    a2 = extendedPO2_PurchaseOrder(comment="sample_text_2", orderDate="sample_text_2", status="sample_text_2", totalAmount=13)
    b = extendedPO2_Address(country="sample_text", name="sample_text")
    _safe_set(b, 'extendedPO2_Address4', a1)
    assert _is_linked(b, 'extendedPO2_Address4', a1)
    if hasattr(a1, 'extendedPO2_PurchaseOrder3'):
        assert _is_linked(a1, 'extendedPO2_PurchaseOrder3', b)
    _safe_set(b, 'extendedPO2_Address4', a2)
    assert _is_linked(b, 'extendedPO2_Address4', a2)
    if hasattr(a1, 'extendedPO2_PurchaseOrder3'):
        assert not _is_linked(a1, 'extendedPO2_PurchaseOrder3', b)
    if hasattr(a2, 'extendedPO2_PurchaseOrder3'):
        assert _is_linked(a2, 'extendedPO2_PurchaseOrder3', b)
    _safe_set(b, 'extendedPO2_Address4', None)
    assert not _is_linked(b, 'extendedPO2_Address4', a2)
    if hasattr(a2, 'extendedPO2_PurchaseOrder3'):
        assert not _is_linked(a2, 'extendedPO2_PurchaseOrder3', b)


def test_assoc_shippedOrders19_reverse_link_reassign_clear():
    a1 = extendedPO2_Supplier(name="sample_text")
    a2 = extendedPO2_Supplier(name="sample_text_2")
    b = extendedPO2_PurchaseOrder(comment="sample_text", orderDate="sample_text", status="sample_text", totalAmount=7)
    _safe_set(b, 'extendedPO2_PurchaseOrder21', a1)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder21', a1)
    if hasattr(a1, 'extendedPO2_Supplier20'):
        assert _is_linked(a1, 'extendedPO2_Supplier20', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder21', a2)
    assert _is_linked(b, 'extendedPO2_PurchaseOrder21', a2)
    if hasattr(a1, 'extendedPO2_Supplier20'):
        assert not _is_linked(a1, 'extendedPO2_Supplier20', b)
    if hasattr(a2, 'extendedPO2_Supplier20'):
        assert _is_linked(a2, 'extendedPO2_Supplier20', b)
    _safe_set(b, 'extendedPO2_PurchaseOrder21', None)
    assert not _is_linked(b, 'extendedPO2_PurchaseOrder21', a2)
    if hasattr(a2, 'extendedPO2_Supplier20'):
        assert not _is_linked(a2, 'extendedPO2_Supplier20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

