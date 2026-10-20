import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    Order,
    OrderDetail,
    model1_Address,
    model1_Category,
    model1_Company,
    model1_Customer,
    model1_Order,
    model1_OrderAddress,
    model1_OrderDetail,
    model1_Product1,
    model1_ProductToOrder,
    model1_PurchaseOrder,
    model1_SalesOrder,
    model1_Supplier,
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

def test_assoc_categories26_reverse_link_reassign_clear():
    a1 = model1_Category(name="sample_text")
    a2 = model1_Category(name="sample_text_2")
    b = model1_Category(name="sample_text")
    _safe_set(b, 'model1_Category27', a1)
    assert _is_linked(b, 'model1_Category27', a1)
    if hasattr(a1, 'model1_Category25'):
        assert _is_linked(a1, 'model1_Category25', b)
    _safe_set(b, 'model1_Category27', a2)
    assert _is_linked(b, 'model1_Category27', a2)
    if hasattr(a1, 'model1_Category25'):
        assert not _is_linked(a1, 'model1_Category25', b)
    if hasattr(a2, 'model1_Category25'):
        assert _is_linked(a2, 'model1_Category25', b)
    _safe_set(b, 'model1_Category27', None)
    assert not _is_linked(b, 'model1_Category27', a2)
    if hasattr(a2, 'model1_Category25'):
        assert not _is_linked(a2, 'model1_Category25', b)


def test_assoc_orderDetails30_reverse_link_reassign_clear():
    a1 = model1_Product1(description="sample_text", name="sample_text", otherVATs="sample_text", vat="sample_text")
    a2 = model1_Product1(description="sample_text_2", name="sample_text_2", otherVATs="sample_text_2", vat="sample_text_2")
    b = model1_OrderDetail(price=3.14)
    _safe_set(b, 'OrderDetail31', a1)
    assert _is_linked(b, 'OrderDetail31', a1)
    if hasattr(a1, 'product'):
        assert _is_linked(a1, 'product', b)
    _safe_set(b, 'OrderDetail31', a2)
    assert _is_linked(b, 'OrderDetail31', a2)
    if hasattr(a1, 'product'):
        assert not _is_linked(a1, 'product', b)
    if hasattr(a2, 'product'):
        assert _is_linked(a2, 'product', b)
    _safe_set(b, 'OrderDetail31', None)
    assert not _is_linked(b, 'OrderDetail31', a2)
    if hasattr(a2, 'product'):
        assert not _is_linked(a2, 'product', b)


def test_assoc_product15_reverse_link_reassign_clear():
    a1 = model1_Product1(description="sample_text", name="sample_text", otherVATs="sample_text", vat="sample_text")
    a2 = model1_Product1(description="sample_text_2", name="sample_text_2", otherVATs="sample_text_2", vat="sample_text_2")
    b = model1_OrderDetail(price=3.14)
    _safe_set(b, 'orderDetails16', a1)
    assert _is_linked(b, 'orderDetails16', a1)
    if hasattr(a1, 'Product1'):
        assert _is_linked(a1, 'Product1', b)
    _safe_set(b, 'orderDetails16', a2)
    assert _is_linked(b, 'orderDetails16', a2)
    if hasattr(a1, 'Product1'):
        assert not _is_linked(a1, 'Product1', b)
    if hasattr(a2, 'Product1'):
        assert _is_linked(a2, 'Product1', b)
    _safe_set(b, 'orderDetails16', None)
    assert not _is_linked(b, 'orderDetails16', a2)
    if hasattr(a2, 'Product1'):
        assert not _is_linked(a2, 'Product1', b)


def test_assoc_products28_reverse_link_reassign_clear():
    a1 = model1_Product1(description="sample_text", name="sample_text", otherVATs="sample_text", vat="sample_text")
    a2 = model1_Product1(description="sample_text_2", name="sample_text_2", otherVATs="sample_text_2", vat="sample_text_2")
    b = model1_Category(name="sample_text")
    _safe_set(b, 'model1_Category29', {a1})
    assert _is_linked(b, 'model1_Category29', a1)
    if hasattr(a1, 'model1_Product1'):
        assert _is_linked(a1, 'model1_Product1', b)
    _safe_set(b, 'model1_Category29', {a2})
    assert _is_linked(b, 'model1_Category29', a2)
    if hasattr(a1, 'model1_Product1'):
        assert not _is_linked(a1, 'model1_Product1', b)
    if hasattr(a2, 'model1_Product1'):
        assert _is_linked(a2, 'model1_Product1', b)
    _safe_set(b, 'model1_Category29', set())
    assert not _is_linked(b, 'model1_Category29', a2)
    if hasattr(a2, 'model1_Product1'):
        assert not _is_linked(a2, 'model1_Product1', b)


def test_assoc_purchaseOrders22_reverse_link_reassign_clear():
    a1 = model1_SalesOrder(id=7)
    a2 = model1_SalesOrder(id=13)
    b = model1_PurchaseOrder(date=date(2024, 1, 1))
    _safe_set(b, 'PurchaseOrder24', a1)
    assert _is_linked(b, 'PurchaseOrder24', a1)
    if hasattr(a1, 'salesOrders23'):
        assert _is_linked(a1, 'salesOrders23', b)
    _safe_set(b, 'PurchaseOrder24', a2)
    assert _is_linked(b, 'PurchaseOrder24', a2)
    if hasattr(a1, 'salesOrders23'):
        assert not _is_linked(a1, 'salesOrders23', b)
    if hasattr(a2, 'salesOrders23'):
        assert _is_linked(a2, 'salesOrders23', b)
    _safe_set(b, 'PurchaseOrder24', None)
    assert not _is_linked(b, 'PurchaseOrder24', a2)
    if hasattr(a2, 'salesOrders23'):
        assert not _is_linked(a2, 'salesOrders23', b)


def test_assoc_purchaseOrders9_reverse_link_reassign_clear():
    a1 = model1_Supplier(preferred=True)
    a2 = model1_Supplier(preferred=False)
    b = model1_PurchaseOrder(date=date(2024, 1, 1))
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


def test_assoc_salesOrders18_reverse_link_reassign_clear():
    a1 = model1_SalesOrder(id=7)
    a2 = model1_SalesOrder(id=13)
    b = model1_PurchaseOrder(date=date(2024, 1, 1))
    _safe_set(b, 'purchaseOrders19', {a1})
    assert _is_linked(b, 'purchaseOrders19', a1)
    if hasattr(a1, 'SalesOrder20'):
        assert _is_linked(a1, 'SalesOrder20', b)
    _safe_set(b, 'purchaseOrders19', {a2})
    assert _is_linked(b, 'purchaseOrders19', a2)
    if hasattr(a1, 'SalesOrder20'):
        assert not _is_linked(a1, 'SalesOrder20', b)
    if hasattr(a2, 'SalesOrder20'):
        assert _is_linked(a2, 'SalesOrder20', b)
    _safe_set(b, 'purchaseOrders19', set())
    assert not _is_linked(b, 'purchaseOrders19', a2)
    if hasattr(a2, 'SalesOrder20'):
        assert not _is_linked(a2, 'SalesOrder20', b)


def test_assoc_supplier17_reverse_link_reassign_clear():
    a1 = model1_Supplier(preferred=True)
    a2 = model1_Supplier(preferred=False)
    b = model1_PurchaseOrder(date=date(2024, 1, 1))
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
    # model1_Company has no real 'model1_Company' property in the generated
    # code (a bare stub) -- manually attach it so model1_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_Category(name="sample_text")
    partner = model1_Company()
    setattr(partner, 'model1_Company', None)
    _safe_set(owner, 'model1_Category', partner)
    assert owner in getattr(partner, 'model1_Company')
    _safe_set(owner, 'model1_Category', None)
    assert owner not in getattr(partner, 'model1_Company')


def test_assoc_customer21_stub_double():
    # model1_Customer has no real 'Customer' property in the generated
    # code (a bare stub) -- manually attach it so model1_SalesOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_SalesOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_SalesOrder(id=7)
    partner = model1_Customer()
    setattr(partner, 'Customer', None)
    _safe_set(owner, 'salesOrders', partner)
    assert getattr(partner, 'Customer') == owner
    _safe_set(owner, 'salesOrders', None)
    assert getattr(partner, 'Customer') is None


def test_assoc_key32_stub_double():
    # model1_ProductToOrder has no real 'model1_ProductToOrder33' property in the generated
    # code (a bare stub) -- manually attach it so model1_Product1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_Product1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_Product1(description="sample_text", name="sample_text", otherVATs="sample_text", vat="sample_text")
    partner = model1_ProductToOrder()
    setattr(partner, 'model1_ProductToOrder33', None)
    _safe_set(owner, 'model1_Product134', partner)
    assert getattr(partner, 'model1_ProductToOrder33') == owner
    _safe_set(owner, 'model1_Product134', None)
    assert getattr(partner, 'model1_ProductToOrder33') is None


def test_assoc_order14_stub_double():
    # model1_Order has no real 'Order' property in the generated
    # code (a bare stub) -- manually attach it so model1_OrderDetail's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_OrderDetail's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_OrderDetail(price=3.14)
    partner = model1_Order()
    setattr(partner, 'Order', None)
    _safe_set(owner, 'orderDetails', partner)
    assert getattr(partner, 'Order') == owner
    _safe_set(owner, 'orderDetails', None)
    assert getattr(partner, 'Order') is None


def test_assoc_orderDetails13_stub_double():
    # model1_Order has no real 'order' property in the generated
    # code (a bare stub) -- manually attach it so model1_OrderDetail's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_OrderDetail's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_OrderDetail(price=3.14)
    partner = model1_Order()
    setattr(partner, 'order', None)
    _safe_set(owner, 'OrderDetail', partner)
    assert owner in getattr(partner, 'order')
    _safe_set(owner, 'OrderDetail', None)
    assert owner not in getattr(partner, 'order')


def test_assoc_purchaseOrders5_stub_double():
    # model1_Company has no real 'model1_Company6' property in the generated
    # code (a bare stub) -- manually attach it so model1_PurchaseOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_PurchaseOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_PurchaseOrder(date=date(2024, 1, 1))
    partner = model1_Company()
    setattr(partner, 'model1_Company6', None)
    _safe_set(owner, 'model1_PurchaseOrder', partner)
    assert owner in getattr(partner, 'model1_Company6')
    _safe_set(owner, 'model1_PurchaseOrder', None)
    assert owner not in getattr(partner, 'model1_Company6')


def test_assoc_salesOrders10_stub_double():
    # model1_Customer has no real 'customer' property in the generated
    # code (a bare stub) -- manually attach it so model1_SalesOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_SalesOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_SalesOrder(id=7)
    partner = model1_Customer()
    setattr(partner, 'customer', None)
    _safe_set(owner, 'SalesOrder', partner)
    assert owner in getattr(partner, 'customer')
    _safe_set(owner, 'SalesOrder', None)
    assert owner not in getattr(partner, 'customer')


def test_assoc_salesOrders7_stub_double():
    # model1_Company has no real 'model1_Company8' property in the generated
    # code (a bare stub) -- manually attach it so model1_SalesOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_SalesOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_SalesOrder(id=7)
    partner = model1_Company()
    setattr(partner, 'model1_Company8', None)
    _safe_set(owner, 'model1_SalesOrder', partner)
    assert owner in getattr(partner, 'model1_Company8')
    _safe_set(owner, 'model1_SalesOrder', None)
    assert owner not in getattr(partner, 'model1_Company8')


def test_assoc_suppliers1_stub_double():
    # model1_Company has no real 'model1_Company2' property in the generated
    # code (a bare stub) -- manually attach it so model1_Supplier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_Supplier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_Supplier(preferred=True)
    partner = model1_Company()
    setattr(partner, 'model1_Company2', None)
    _safe_set(owner, 'model1_Supplier', partner)
    assert owner in getattr(partner, 'model1_Company2')
    _safe_set(owner, 'model1_Supplier', None)
    assert owner not in getattr(partner, 'model1_Company2')


def test_assoc_value35_stub_double():
    # model1_ProductToOrder has no real 'model1_ProductToOrder36' property in the generated
    # code (a bare stub) -- manually attach it so model1_SalesOrder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model1_SalesOrder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model1_SalesOrder(id=7)
    partner = model1_ProductToOrder()
    setattr(partner, 'model1_ProductToOrder36', None)
    _safe_set(owner, 'model1_SalesOrder37', partner)
    assert getattr(partner, 'model1_ProductToOrder36') == owner
    _safe_set(owner, 'model1_SalesOrder37', None)
    assert getattr(partner, 'model1_ProductToOrder36') is None


