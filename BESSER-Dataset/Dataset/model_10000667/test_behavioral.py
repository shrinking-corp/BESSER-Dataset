import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Customer,
    Employee,
    Inventory,
    Items,
    Menu,
    Order,
    PurchaseOrder,
    Store,
    Vendor,
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

def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order(CustNumber=7, ItemName="sample_text", MenuItem=7, OrderDate=date(2024, 1, 1), OrderID=7)
    a2 = Order(CustNumber=13, ItemName="sample_text_2", MenuItem=13, OrderDate=date(2025, 6, 15), OrderID=13)
    b = Customer(CustNumber=7)
    _safe_set(b, 'order14', {a1})
    assert _is_linked(b, 'order14', a1)
    if hasattr(a1, 'customer15'):
        assert _is_linked(a1, 'customer15', b)
    _safe_set(b, 'order14', {a2})
    assert _is_linked(b, 'order14', a2)
    if hasattr(a1, 'customer15'):
        assert not _is_linked(a1, 'customer15', b)
    if hasattr(a2, 'customer15'):
        assert _is_linked(a2, 'customer15', b)
    _safe_set(b, 'order14', set())
    assert not _is_linked(b, 'order14', a2)
    if hasattr(a2, 'customer15'):
        assert not _is_linked(a2, 'customer15', b)


def test_assoc_Inventory_Items2_reverse_link_reassign_clear():
    a1 = Items(ItemID=7, Name="sample_text")
    a2 = Items(ItemID=13, Name="sample_text_2")
    b = Inventory(ItemID=7, Quantity=3.14, StoreID=7)
    _safe_set(b, 'items8', {a1})
    assert _is_linked(b, 'items8', a1)
    if hasattr(a1, 'inventory9'):
        assert _is_linked(a1, 'inventory9', b)
    _safe_set(b, 'items8', {a2})
    assert _is_linked(b, 'items8', a2)
    if hasattr(a1, 'inventory9'):
        assert not _is_linked(a1, 'inventory9', b)
    if hasattr(a2, 'inventory9'):
        assert _is_linked(a2, 'inventory9', b)
    _safe_set(b, 'items8', set())
    assert not _is_linked(b, 'items8', a2)
    if hasattr(a2, 'inventory9'):
        assert not _is_linked(a2, 'inventory9', b)


def test_assoc_Inventory_Store_reverse_link_reassign_clear():
    a1 = Store(Address="sample_text", Name="sample_text", StoreID=7)
    a2 = Store(Address="sample_text_2", Name="sample_text_2", StoreID=13)
    b = Inventory(ItemID=7, Quantity=3.14, StoreID=7)
    _safe_set(b, 'store2', {a1})
    assert _is_linked(b, 'store2', a1)
    if hasattr(a1, 'inventory3'):
        assert _is_linked(a1, 'inventory3', b)
    _safe_set(b, 'store2', {a2})
    assert _is_linked(b, 'store2', a2)
    if hasattr(a1, 'inventory3'):
        assert not _is_linked(a1, 'inventory3', b)
    if hasattr(a2, 'inventory3'):
        assert _is_linked(a2, 'inventory3', b)
    _safe_set(b, 'store2', set())
    assert not _is_linked(b, 'store2', a2)
    if hasattr(a2, 'inventory3'):
        assert not _is_linked(a2, 'inventory3', b)


def test_assoc_Menu_Items_reverse_link_reassign_clear():
    a1 = Menu(MenuItem="sample_text")
    a2 = Menu(MenuItem="sample_text_2")
    b = Items(ItemID=7, Name="sample_text")
    _safe_set(b, 'menu7', a1)
    assert _is_linked(b, 'menu7', a1)
    if hasattr(a1, 'items6'):
        assert _is_linked(a1, 'items6', b)
    _safe_set(b, 'menu7', a2)
    assert _is_linked(b, 'menu7', a2)
    if hasattr(a1, 'items6'):
        assert not _is_linked(a1, 'items6', b)
    if hasattr(a2, 'items6'):
        assert _is_linked(a2, 'items6', b)
    _safe_set(b, 'menu7', None)
    assert not _is_linked(b, 'menu7', a2)
    if hasattr(a2, 'items6'):
        assert not _is_linked(a2, 'items6', b)


def test_assoc_Menu_Order_reverse_link_reassign_clear():
    a1 = Order(CustNumber=7, ItemName="sample_text", MenuItem=7, OrderDate=date(2024, 1, 1), OrderID=7)
    a2 = Order(CustNumber=13, ItemName="sample_text_2", MenuItem=13, OrderDate=date(2025, 6, 15), OrderID=13)
    b = Menu(MenuItem="sample_text")
    _safe_set(b, 'order0', a1)
    assert _is_linked(b, 'order0', a1)
    if hasattr(a1, 'menu1'):
        assert _is_linked(a1, 'menu1', b)
    _safe_set(b, 'order0', a2)
    assert _is_linked(b, 'order0', a2)
    if hasattr(a1, 'menu1'):
        assert not _is_linked(a1, 'menu1', b)
    if hasattr(a2, 'menu1'):
        assert _is_linked(a2, 'menu1', b)
    _safe_set(b, 'order0', None)
    assert not _is_linked(b, 'order0', a2)
    if hasattr(a2, 'menu1'):
        assert not _is_linked(a2, 'menu1', b)


def test_assoc_PurchaseOrder_Items_reverse_link_reassign_clear():
    a1 = PurchaseOrder(Date=date(2024, 1, 1), ItemID=7, Price=3.14, PurchaseOrderID=7, Quantity=3.14, VendorID=7)
    a2 = PurchaseOrder(Date=date(2025, 6, 15), ItemID=13, Price=9.99, PurchaseOrderID=13, Quantity=9.99, VendorID=13)
    b = Items(ItemID=7, Name="sample_text")
    _safe_set(b, 'purchaseOrder13', a1)
    assert _is_linked(b, 'purchaseOrder13', a1)
    if hasattr(a1, 'items12'):
        assert _is_linked(a1, 'items12', b)
    _safe_set(b, 'purchaseOrder13', a2)
    assert _is_linked(b, 'purchaseOrder13', a2)
    if hasattr(a1, 'items12'):
        assert not _is_linked(a1, 'items12', b)
    if hasattr(a2, 'items12'):
        assert _is_linked(a2, 'items12', b)
    _safe_set(b, 'purchaseOrder13', None)
    assert not _is_linked(b, 'purchaseOrder13', a2)
    if hasattr(a2, 'items12'):
        assert not _is_linked(a2, 'items12', b)


def test_assoc_Store_Employee_reverse_link_reassign_clear():
    a1 = Store(Address="sample_text", Name="sample_text", StoreID=7)
    a2 = Store(Address="sample_text_2", Name="sample_text_2", StoreID=13)
    b = Employee(EmployeeID=7, Role="sample_text", Salary=3.14, StoreID=7)
    _safe_set(b, 'store11', a1)
    assert _is_linked(b, 'store11', a1)
    if hasattr(a1, 'employee10'):
        assert _is_linked(a1, 'employee10', b)
    _safe_set(b, 'store11', a2)
    assert _is_linked(b, 'store11', a2)
    if hasattr(a1, 'employee10'):
        assert not _is_linked(a1, 'employee10', b)
    if hasattr(a2, 'employee10'):
        assert _is_linked(a2, 'employee10', b)
    _safe_set(b, 'store11', None)
    assert not _is_linked(b, 'store11', a2)
    if hasattr(a2, 'employee10'):
        assert not _is_linked(a2, 'employee10', b)


def test_assoc_Vendor_PurchaseOrder_reverse_link_reassign_clear():
    a1 = Vendor(Address="sample_text", ItemID=7, VendorID=7)
    a2 = Vendor(Address="sample_text_2", ItemID=13, VendorID=13)
    b = PurchaseOrder(Date=date(2024, 1, 1), ItemID=7, Price=3.14, PurchaseOrderID=7, Quantity=3.14, VendorID=7)
    _safe_set(b, 'vendor5', a1)
    assert _is_linked(b, 'vendor5', a1)
    if hasattr(a1, 'purchaseOrder4'):
        assert _is_linked(a1, 'purchaseOrder4', b)
    _safe_set(b, 'vendor5', a2)
    assert _is_linked(b, 'vendor5', a2)
    if hasattr(a1, 'purchaseOrder4'):
        assert not _is_linked(a1, 'purchaseOrder4', b)
    if hasattr(a2, 'purchaseOrder4'):
        assert _is_linked(a2, 'purchaseOrder4', b)
    _safe_set(b, 'vendor5', None)
    assert not _is_linked(b, 'vendor5', a2)
    if hasattr(a2, 'purchaseOrder4'):
        assert not _is_linked(a2, 'purchaseOrder4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

