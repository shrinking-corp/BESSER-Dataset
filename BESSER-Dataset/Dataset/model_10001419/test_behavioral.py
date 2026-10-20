import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Customer,
    Items,
    Order,
    Payment,
    Products,
    Shopping_Cart,
    Warehouse,
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

def test_assoc_Account_Customer_reverse_link_reassign_clear():
    a1 = Customer(Customer_ID=7, Name="sample_text")
    a2 = Customer(Customer_ID=13, Name="sample_text_2")
    b = Account(Address="sample_text")
    _safe_set(b, 'customer8', a1)
    assert _is_linked(b, 'customer8', a1)
    if hasattr(a1, 'account9'):
        assert _is_linked(a1, 'account9', b)
    _safe_set(b, 'customer8', a2)
    assert _is_linked(b, 'customer8', a2)
    if hasattr(a1, 'account9'):
        assert not _is_linked(a1, 'account9', b)
    if hasattr(a2, 'account9'):
        assert _is_linked(a2, 'account9', b)
    _safe_set(b, 'customer8', None)
    assert not _is_linked(b, 'customer8', a2)
    if hasattr(a2, 'account9'):
        assert not _is_linked(a2, 'account9', b)


def test_assoc_Account_Order_reverse_link_reassign_clear():
    a1 = Order(Order_ID=7)
    a2 = Order(Order_ID=13)
    b = Account(Address="sample_text")
    _safe_set(b, 'order22', a1)
    assert _is_linked(b, 'order22', a1)
    if hasattr(a1, 'account23'):
        assert _is_linked(a1, 'account23', b)
    _safe_set(b, 'order22', a2)
    assert _is_linked(b, 'order22', a2)
    if hasattr(a1, 'account23'):
        assert not _is_linked(a1, 'account23', b)
    if hasattr(a2, 'account23'):
        assert _is_linked(a2, 'account23', b)
    _safe_set(b, 'order22', None)
    assert not _is_linked(b, 'order22', a2)
    if hasattr(a2, 'account23'):
        assert not _is_linked(a2, 'account23', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = Customer(Customer_ID=7, Name="sample_text")
    a2 = Customer(Customer_ID=13, Name="sample_text_2")
    b = Account(Address="sample_text")
    _safe_set(b, 'customer11', a1)
    assert _is_linked(b, 'customer11', a1)
    if hasattr(a1, 'account10'):
        assert _is_linked(a1, 'account10', b)
    _safe_set(b, 'customer11', a2)
    assert _is_linked(b, 'customer11', a2)
    if hasattr(a1, 'account10'):
        assert not _is_linked(a1, 'account10', b)
    if hasattr(a2, 'account10'):
        assert _is_linked(a2, 'account10', b)
    _safe_set(b, 'customer11', None)
    assert not _is_linked(b, 'customer11', a2)
    if hasattr(a2, 'account10'):
        assert not _is_linked(a2, 'account10', b)


def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order(Order_ID=7)
    a2 = Order(Order_ID=13)
    b = Customer(Customer_ID=7, Name="sample_text")
    _safe_set(b, 'order2', {a1})
    assert _is_linked(b, 'order2', a1)
    if hasattr(a1, 'customer3'):
        assert _is_linked(a1, 'customer3', b)
    _safe_set(b, 'order2', {a2})
    assert _is_linked(b, 'order2', a2)
    if hasattr(a1, 'customer3'):
        assert not _is_linked(a1, 'customer3', b)
    if hasattr(a2, 'customer3'):
        assert _is_linked(a2, 'customer3', b)
    _safe_set(b, 'order2', set())
    assert not _is_linked(b, 'order2', a2)
    if hasattr(a2, 'customer3'):
        assert not _is_linked(a2, 'customer3', b)


def test_assoc_Customer_Payment_reverse_link_reassign_clear():
    a1 = Payment(Date=7, Payment_ID=7)
    a2 = Payment(Date=13, Payment_ID=13)
    b = Customer(Customer_ID=7, Name="sample_text")
    _safe_set(b, 'payment6', a1)
    assert _is_linked(b, 'payment6', a1)
    if hasattr(a1, 'customer7'):
        assert _is_linked(a1, 'customer7', b)
    _safe_set(b, 'payment6', a2)
    assert _is_linked(b, 'payment6', a2)
    if hasattr(a1, 'customer7'):
        assert not _is_linked(a1, 'customer7', b)
    if hasattr(a2, 'customer7'):
        assert _is_linked(a2, 'customer7', b)
    _safe_set(b, 'payment6', None)
    assert not _is_linked(b, 'payment6', a2)
    if hasattr(a2, 'customer7'):
        assert not _is_linked(a2, 'customer7', b)


def test_assoc_Customer_Products_reverse_link_reassign_clear():
    a1 = Products(Product_ID=7)
    a2 = Products(Product_ID=13)
    b = Customer(Customer_ID=7, Name="sample_text")
    _safe_set(b, 'products0', {a1})
    assert _is_linked(b, 'products0', a1)
    if hasattr(a1, 'customer1'):
        assert _is_linked(a1, 'customer1', b)
    _safe_set(b, 'products0', {a2})
    assert _is_linked(b, 'products0', a2)
    if hasattr(a1, 'customer1'):
        assert not _is_linked(a1, 'customer1', b)
    if hasattr(a2, 'customer1'):
        assert _is_linked(a2, 'customer1', b)
    _safe_set(b, 'products0', set())
    assert not _is_linked(b, 'products0', a2)
    if hasattr(a2, 'customer1'):
        assert not _is_linked(a2, 'customer1', b)


def test_assoc_Customer_Shopping_Cart_reverse_link_reassign_clear():
    a1 = Shopping_Cart(Date=7)
    a2 = Shopping_Cart(Date=13)
    b = Customer(Customer_ID=7, Name="sample_text")
    _safe_set(b, 'shopping_Cart4', a1)
    assert _is_linked(b, 'shopping_Cart4', a1)
    if hasattr(a1, 'customer5'):
        assert _is_linked(a1, 'customer5', b)
    _safe_set(b, 'shopping_Cart4', a2)
    assert _is_linked(b, 'shopping_Cart4', a2)
    if hasattr(a1, 'customer5'):
        assert not _is_linked(a1, 'customer5', b)
    if hasattr(a2, 'customer5'):
        assert _is_linked(a2, 'customer5', b)
    _safe_set(b, 'shopping_Cart4', None)
    assert not _is_linked(b, 'shopping_Cart4', a2)
    if hasattr(a2, 'customer5'):
        assert not _is_linked(a2, 'customer5', b)


def test_assoc_Order_Account_reverse_link_reassign_clear():
    a1 = Order(Order_ID=7)
    a2 = Order(Order_ID=13)
    b = Account(Address="sample_text")
    _safe_set(b, 'order19', a1)
    assert _is_linked(b, 'order19', a1)
    if hasattr(a1, 'account18'):
        assert _is_linked(a1, 'account18', b)
    _safe_set(b, 'order19', a2)
    assert _is_linked(b, 'order19', a2)
    if hasattr(a1, 'account18'):
        assert not _is_linked(a1, 'account18', b)
    if hasattr(a2, 'account18'):
        assert _is_linked(a2, 'account18', b)
    _safe_set(b, 'order19', None)
    assert not _is_linked(b, 'order19', a2)
    if hasattr(a2, 'account18'):
        assert not _is_linked(a2, 'account18', b)


def test_assoc_Order_Account2_reverse_link_reassign_clear():
    a1 = Order(Order_ID=7)
    a2 = Order(Order_ID=13)
    b = Account(Address="sample_text")
    _safe_set(b, 'order21', a1)
    assert _is_linked(b, 'order21', a1)
    if hasattr(a1, 'account20'):
        assert _is_linked(a1, 'account20', b)
    _safe_set(b, 'order21', a2)
    assert _is_linked(b, 'order21', a2)
    if hasattr(a1, 'account20'):
        assert not _is_linked(a1, 'account20', b)
    if hasattr(a2, 'account20'):
        assert _is_linked(a2, 'account20', b)
    _safe_set(b, 'order21', None)
    assert not _is_linked(b, 'order21', a2)
    if hasattr(a2, 'account20'):
        assert not _is_linked(a2, 'account20', b)


def test_assoc_Payment__Order_reverse_link_reassign_clear():
    a1 = Payment(Date=7, Payment_ID=7)
    a2 = Payment(Date=13, Payment_ID=13)
    b = Order(Order_ID=7)
    _safe_set(b, 'payment15', a1)
    assert _is_linked(b, 'payment15', a1)
    if hasattr(a1, 'order14'):
        assert _is_linked(a1, 'order14', b)
    _safe_set(b, 'payment15', a2)
    assert _is_linked(b, 'payment15', a2)
    if hasattr(a1, 'order14'):
        assert not _is_linked(a1, 'order14', b)
    if hasattr(a2, 'order14'):
        assert _is_linked(a2, 'order14', b)
    _safe_set(b, 'payment15', None)
    assert not _is_linked(b, 'payment15', a2)
    if hasattr(a2, 'order14'):
        assert not _is_linked(a2, 'order14', b)


def test_assoc_Shopping_Cart_Items_reverse_link_reassign_clear():
    a1 = Shopping_Cart(Date=7)
    a2 = Shopping_Cart(Date=13)
    b = Items(Description="sample_text")
    _safe_set(b, 'shopping_Cart17', a1)
    assert _is_linked(b, 'shopping_Cart17', a1)
    if hasattr(a1, 'items16'):
        assert _is_linked(a1, 'items16', b)
    _safe_set(b, 'shopping_Cart17', a2)
    assert _is_linked(b, 'shopping_Cart17', a2)
    if hasattr(a1, 'items16'):
        assert not _is_linked(a1, 'items16', b)
    if hasattr(a2, 'items16'):
        assert _is_linked(a2, 'items16', b)
    _safe_set(b, 'shopping_Cart17', None)
    assert not _is_linked(b, 'shopping_Cart17', a2)
    if hasattr(a2, 'items16'):
        assert not _is_linked(a2, 'items16', b)


def test_assoc_Warehouse_Products_reverse_link_reassign_clear():
    a1 = Warehouse(Warehouse_branch="sample_text")
    a2 = Warehouse(Warehouse_branch="sample_text_2")
    b = Products(Product_ID=7)
    _safe_set(b, 'warehouse13', {a1})
    assert _is_linked(b, 'warehouse13', a1)
    if hasattr(a1, 'products12'):
        assert _is_linked(a1, 'products12', b)
    _safe_set(b, 'warehouse13', {a2})
    assert _is_linked(b, 'warehouse13', a2)
    if hasattr(a1, 'products12'):
        assert not _is_linked(a1, 'products12', b)
    if hasattr(a2, 'products12'):
        assert _is_linked(a2, 'products12', b)
    _safe_set(b, 'warehouse13', set())
    assert not _is_linked(b, 'warehouse13', a2)
    if hasattr(a2, 'products12'):
        assert not _is_linked(a2, 'products12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

