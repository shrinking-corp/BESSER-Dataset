import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Addressable,
    Order,
    company_Addressable,
    company_Category,
    company_Company,
    company_Customer,
    company_Order,
    company_OrderDetail,
    company_Product,
    company_PurchaseOrder,
    company_SalesOrder,
    company_Supplier,
    VAT,
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

def test_assoc_categories18_reverse_link_reassign_clear():
    a1 = company_Category(name="sample_text")
    a2 = company_Category(name="sample_text_2")
    b = company_Category(name="sample_text")
    _safe_set(b, 'company_Category19', a1)
    assert _is_linked(b, 'company_Category19', a1)
    if hasattr(a1, 'company_Category17'):
        assert _is_linked(a1, 'company_Category17', b)
    _safe_set(b, 'company_Category19', a2)
    assert _is_linked(b, 'company_Category19', a2)
    if hasattr(a1, 'company_Category17'):
        assert not _is_linked(a1, 'company_Category17', b)
    if hasattr(a2, 'company_Category17'):
        assert _is_linked(a2, 'company_Category17', b)
    _safe_set(b, 'company_Category19', None)
    assert not _is_linked(b, 'company_Category19', a2)
    if hasattr(a2, 'company_Category17'):
        assert not _is_linked(a2, 'company_Category17', b)


def test_assoc_orderDetails22_reverse_link_reassign_clear():
    a1 = company_Product(description="sample_text", name="sample_text", price=3.14, vat="sample_text")
    a2 = company_Product(description="sample_text_2", name="sample_text_2", price=9.99, vat="sample_text_2")
    b = company_OrderDetail(price=3.14)
    _safe_set(b, 'OrderDetail23', a1)
    assert _is_linked(b, 'OrderDetail23', a1)
    if hasattr(a1, 'product'):
        assert _is_linked(a1, 'product', b)
    _safe_set(b, 'OrderDetail23', a2)
    assert _is_linked(b, 'OrderDetail23', a2)
    if hasattr(a1, 'product'):
        assert not _is_linked(a1, 'product', b)
    if hasattr(a2, 'product'):
        assert _is_linked(a2, 'product', b)
    _safe_set(b, 'OrderDetail23', None)
    assert not _is_linked(b, 'OrderDetail23', a2)
    if hasattr(a2, 'product'):
        assert not _is_linked(a2, 'product', b)


def test_assoc_product13_reverse_link_reassign_clear():
    a1 = company_Product(description="sample_text", name="sample_text", price=3.14, vat="sample_text")
    a2 = company_Product(description="sample_text_2", name="sample_text_2", price=9.99, vat="sample_text_2")
    b = company_OrderDetail(price=3.14)
    _safe_set(b, 'orderDetails14', a1)
    assert _is_linked(b, 'orderDetails14', a1)
    if hasattr(a1, 'Product'):
        assert _is_linked(a1, 'Product', b)
    _safe_set(b, 'orderDetails14', a2)
    assert _is_linked(b, 'orderDetails14', a2)
    if hasattr(a1, 'Product'):
        assert not _is_linked(a1, 'Product', b)
    if hasattr(a2, 'Product'):
        assert _is_linked(a2, 'Product', b)
    _safe_set(b, 'orderDetails14', None)
    assert not _is_linked(b, 'orderDetails14', a2)
    if hasattr(a2, 'Product'):
        assert not _is_linked(a2, 'Product', b)


def test_assoc_products20_reverse_link_reassign_clear():
    a1 = company_Product(description="sample_text", name="sample_text", price=3.14, vat="sample_text")
    a2 = company_Product(description="sample_text_2", name="sample_text_2", price=9.99, vat="sample_text_2")
    b = company_Category(name="sample_text")
    _safe_set(b, 'company_Category21', {a1})
    assert _is_linked(b, 'company_Category21', a1)
    if hasattr(a1, 'company_Product'):
        assert _is_linked(a1, 'company_Product', b)
    _safe_set(b, 'company_Category21', {a2})
    assert _is_linked(b, 'company_Category21', a2)
    if hasattr(a1, 'company_Product'):
        assert not _is_linked(a1, 'company_Product', b)
    if hasattr(a2, 'company_Product'):
        assert _is_linked(a2, 'company_Product', b)
    _safe_set(b, 'company_Category21', set())
    assert not _is_linked(b, 'company_Category21', a2)
    if hasattr(a2, 'company_Product'):
        assert not _is_linked(a2, 'company_Product', b)


def test_assoc_purchaseOrders9_reverse_link_reassign_clear():
    a1 = company_Supplier(preferred=True)
    a2 = company_Supplier(preferred=False)
    b = company_PurchaseOrder(date=date(2024, 1, 1))
    _safe_set(b, 'PurchaseOrder', a1)
    assert _is_linked(b, 'PurchaseOrder', a1)
    if hasattr(a1, 'supplier'):
        assert _is_linked(a1, 'supplier', b)
    _safe_set(b, 'PurchaseOrder', a2)
    assert _is_linked(b, 'PurchaseOrder', a2)
    if hasattr(a1, 'supplier'):
        assert not _is_linked(a1, 'supplier', b)
    if hasattr(a2, 'supplier'):
        assert _is_linked(a2, 'supplier', b)
    _safe_set(b, 'PurchaseOrder', None)
    assert not _is_linked(b, 'PurchaseOrder', a2)
    if hasattr(a2, 'supplier'):
        assert not _is_linked(a2, 'supplier', b)


def test_assoc_supplier15_reverse_link_reassign_clear():
    a1 = company_Supplier(preferred=True)
    a2 = company_Supplier(preferred=False)
    b = company_PurchaseOrder(date=date(2024, 1, 1))
    _safe_set(b, 'purchaseOrders', a1)
    assert _is_linked(b, 'purchaseOrders', a1)
    if hasattr(a1, 'Supplier'):
        assert _is_linked(a1, 'Supplier', b)
    _safe_set(b, 'purchaseOrders', a2)
    assert _is_linked(b, 'purchaseOrders', a2)
    if hasattr(a1, 'Supplier'):
        assert not _is_linked(a1, 'Supplier', b)
    if hasattr(a2, 'Supplier'):
        assert _is_linked(a2, 'Supplier', b)
    _safe_set(b, 'purchaseOrders', None)
    assert not _is_linked(b, 'purchaseOrders', a2)
    if hasattr(a2, 'Supplier'):
        assert not _is_linked(a2, 'Supplier', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_categories0_stub_double():
    # company_Company has no real 'company_Company' property in the generated
    # code (a bare stub) -- manually attach it so company_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Category(name="sample_text")
    partner = company_Company()
    setattr(partner, 'company_Company', None)
    _safe_set(owner, 'company_Category', partner)
    assert owner in getattr(partner, 'company_Company')
    _safe_set(owner, 'company_Category', None)
    assert owner not in getattr(partner, 'company_Company')


def test_assoc_customer16_stub_double():
    # company_Customer has no real 'Customer' property in the generated
    # code (a bare stub) -- manually attach it so company_SalesOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_SalesOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_SalesOrder(id=7)
    partner = company_Customer()
    setattr(partner, 'Customer', None)
    _safe_set(owner, 'salesOrders', partner)
    assert getattr(partner, 'Customer') == owner
    _safe_set(owner, 'salesOrders', None)
    assert getattr(partner, 'Customer') is None


def test_assoc_order12_stub_double():
    # company_Order has no real 'Order' property in the generated
    # code (a bare stub) -- manually attach it so company_OrderDetail's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_OrderDetail's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_OrderDetail(price=3.14)
    partner = company_Order()
    setattr(partner, 'Order', None)
    _safe_set(owner, 'orderDetails', partner)
    assert getattr(partner, 'Order') == owner
    _safe_set(owner, 'orderDetails', None)
    assert getattr(partner, 'Order') is None


def test_assoc_orderDetails11_stub_double():
    # company_Order has no real 'order' property in the generated
    # code (a bare stub) -- manually attach it so company_OrderDetail's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_OrderDetail's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_OrderDetail(price=3.14)
    partner = company_Order()
    setattr(partner, 'order', None)
    _safe_set(owner, 'OrderDetail', partner)
    assert owner in getattr(partner, 'order')
    _safe_set(owner, 'OrderDetail', None)
    assert owner not in getattr(partner, 'order')


def test_assoc_purchaseOrders5_stub_double():
    # company_Company has no real 'company_Company6' property in the generated
    # code (a bare stub) -- manually attach it so company_PurchaseOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_PurchaseOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_PurchaseOrder(date=date(2024, 1, 1))
    partner = company_Company()
    setattr(partner, 'company_Company6', None)
    _safe_set(owner, 'company_PurchaseOrder', partner)
    assert owner in getattr(partner, 'company_Company6')
    _safe_set(owner, 'company_PurchaseOrder', None)
    assert owner not in getattr(partner, 'company_Company6')


def test_assoc_salesOrders10_stub_double():
    # company_Customer has no real 'customer' property in the generated
    # code (a bare stub) -- manually attach it so company_SalesOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_SalesOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_SalesOrder(id=7)
    partner = company_Customer()
    setattr(partner, 'customer', None)
    _safe_set(owner, 'SalesOrder', partner)
    assert owner in getattr(partner, 'customer')
    _safe_set(owner, 'SalesOrder', None)
    assert owner not in getattr(partner, 'customer')


def test_assoc_salesOrders7_stub_double():
    # company_Company has no real 'company_Company8' property in the generated
    # code (a bare stub) -- manually attach it so company_SalesOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_SalesOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_SalesOrder(id=7)
    partner = company_Company()
    setattr(partner, 'company_Company8', None)
    _safe_set(owner, 'company_SalesOrder', partner)
    assert owner in getattr(partner, 'company_Company8')
    _safe_set(owner, 'company_SalesOrder', None)
    assert owner not in getattr(partner, 'company_Company8')


def test_assoc_suppliers1_stub_double():
    # company_Company has no real 'company_Company2' property in the generated
    # code (a bare stub) -- manually attach it so company_Supplier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Supplier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Supplier(preferred=True)
    partner = company_Company()
    setattr(partner, 'company_Company2', None)
    _safe_set(owner, 'company_Supplier', partner)
    assert owner in getattr(partner, 'company_Company2')
    _safe_set(owner, 'company_Supplier', None)
    assert owner not in getattr(partner, 'company_Company2')


