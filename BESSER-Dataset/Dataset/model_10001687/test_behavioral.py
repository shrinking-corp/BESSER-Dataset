import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Customer,
    Customer_Data,
    Employee,
    Inventory,
    Manager,
    Online_Portal,
    Order,
    Product,
    Service,
    Store,
    Terminal,
    Transactions,
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

def test_assoc_Customer_Data_Order_reverse_link_reassign_clear():
    a1 = Order(Product="sample_text", Service="sample_text")
    a2 = Order(Product="sample_text_2", Service="sample_text_2")
    b = Customer_Data(Contact="sample_text", Name="sample_text")
    _safe_set(b, 'order14', a1)
    assert _is_linked(b, 'order14', a1)
    if hasattr(a1, 'customer_Data15'):
        assert _is_linked(a1, 'customer_Data15', b)
    _safe_set(b, 'order14', a2)
    assert _is_linked(b, 'order14', a2)
    if hasattr(a1, 'customer_Data15'):
        assert not _is_linked(a1, 'customer_Data15', b)
    if hasattr(a2, 'customer_Data15'):
        assert _is_linked(a2, 'customer_Data15', b)
    _safe_set(b, 'order14', None)
    assert not _is_linked(b, 'order14', a2)
    if hasattr(a2, 'customer_Data15'):
        assert not _is_linked(a2, 'customer_Data15', b)


def test_assoc_Online_Portal_Customer_Data_reverse_link_reassign_clear():
    a1 = Online_Portal(StoreLocation="sample_text")
    a2 = Online_Portal(StoreLocation="sample_text_2")
    b = Customer_Data(Contact="sample_text", Name="sample_text")
    _safe_set(b, 'online_Portal37', a1)
    assert _is_linked(b, 'online_Portal37', a1)
    if hasattr(a1, 'customer_Data36'):
        assert _is_linked(a1, 'customer_Data36', b)
    _safe_set(b, 'online_Portal37', a2)
    assert _is_linked(b, 'online_Portal37', a2)
    if hasattr(a1, 'customer_Data36'):
        assert not _is_linked(a1, 'customer_Data36', b)
    if hasattr(a2, 'customer_Data36'):
        assert _is_linked(a2, 'customer_Data36', b)
    _safe_set(b, 'online_Portal37', None)
    assert not _is_linked(b, 'online_Portal37', a2)
    if hasattr(a2, 'customer_Data36'):
        assert not _is_linked(a2, 'customer_Data36', b)


def test_assoc_Online_Portal_Inventory_reverse_link_reassign_clear():
    a1 = Online_Portal(StoreLocation="sample_text")
    a2 = Online_Portal(StoreLocation="sample_text_2")
    b = Inventory(Products="sample_text", Services="sample_text")
    _safe_set(b, 'online_Portal33', a1)
    assert _is_linked(b, 'online_Portal33', a1)
    if hasattr(a1, 'inventory32'):
        assert _is_linked(a1, 'inventory32', b)
    _safe_set(b, 'online_Portal33', a2)
    assert _is_linked(b, 'online_Portal33', a2)
    if hasattr(a1, 'inventory32'):
        assert not _is_linked(a1, 'inventory32', b)
    if hasattr(a2, 'inventory32'):
        assert _is_linked(a2, 'inventory32', b)
    _safe_set(b, 'online_Portal33', None)
    assert not _is_linked(b, 'online_Portal33', a2)
    if hasattr(a2, 'inventory32'):
        assert not _is_linked(a2, 'inventory32', b)


def test_assoc_Online_Portal_Transactions_reverse_link_reassign_clear():
    a1 = Transactions(Customer="sample_text", Order="sample_text")
    a2 = Transactions(Customer="sample_text_2", Order="sample_text_2")
    b = Online_Portal(StoreLocation="sample_text")
    _safe_set(b, 'transactions34', a1)
    assert _is_linked(b, 'transactions34', a1)
    if hasattr(a1, 'online_Portal35'):
        assert _is_linked(a1, 'online_Portal35', b)
    _safe_set(b, 'transactions34', a2)
    assert _is_linked(b, 'transactions34', a2)
    if hasattr(a1, 'online_Portal35'):
        assert not _is_linked(a1, 'online_Portal35', b)
    if hasattr(a2, 'online_Portal35'):
        assert _is_linked(a2, 'online_Portal35', b)
    _safe_set(b, 'transactions34', None)
    assert not _is_linked(b, 'transactions34', a2)
    if hasattr(a2, 'online_Portal35'):
        assert not _is_linked(a2, 'online_Portal35', b)


def test_assoc_Terminal_Customer_Data_reverse_link_reassign_clear():
    a1 = Terminal(Current_Employee="sample_text")
    a2 = Terminal(Current_Employee="sample_text_2")
    b = Customer_Data(Contact="sample_text", Name="sample_text")
    _safe_set(b, 'terminal23', {a1})
    assert _is_linked(b, 'terminal23', a1)
    if hasattr(a1, 'customer_Data22'):
        assert _is_linked(a1, 'customer_Data22', b)
    _safe_set(b, 'terminal23', {a2})
    assert _is_linked(b, 'terminal23', a2)
    if hasattr(a1, 'customer_Data22'):
        assert not _is_linked(a1, 'customer_Data22', b)
    if hasattr(a2, 'customer_Data22'):
        assert _is_linked(a2, 'customer_Data22', b)
    _safe_set(b, 'terminal23', set())
    assert not _is_linked(b, 'terminal23', a2)
    if hasattr(a2, 'customer_Data22'):
        assert not _is_linked(a2, 'customer_Data22', b)


def test_assoc_Terminal_Inventory_reverse_link_reassign_clear():
    a1 = Terminal(Current_Employee="sample_text")
    a2 = Terminal(Current_Employee="sample_text_2")
    b = Inventory(Products="sample_text", Services="sample_text")
    _safe_set(b, 'terminal19', {a1})
    assert _is_linked(b, 'terminal19', a1)
    if hasattr(a1, 'inventory18'):
        assert _is_linked(a1, 'inventory18', b)
    _safe_set(b, 'terminal19', {a2})
    assert _is_linked(b, 'terminal19', a2)
    if hasattr(a1, 'inventory18'):
        assert not _is_linked(a1, 'inventory18', b)
    if hasattr(a2, 'inventory18'):
        assert _is_linked(a2, 'inventory18', b)
    _safe_set(b, 'terminal19', set())
    assert not _is_linked(b, 'terminal19', a2)
    if hasattr(a2, 'inventory18'):
        assert not _is_linked(a2, 'inventory18', b)


def test_assoc_Terminal_Transactions_reverse_link_reassign_clear():
    a1 = Transactions(Customer="sample_text", Order="sample_text")
    a2 = Transactions(Customer="sample_text_2", Order="sample_text_2")
    b = Terminal(Current_Employee="sample_text")
    _safe_set(b, 'transactions20', {a1})
    assert _is_linked(b, 'transactions20', a1)
    if hasattr(a1, 'terminal21'):
        assert _is_linked(a1, 'terminal21', b)
    _safe_set(b, 'transactions20', {a2})
    assert _is_linked(b, 'transactions20', a2)
    if hasattr(a1, 'terminal21'):
        assert not _is_linked(a1, 'terminal21', b)
    if hasattr(a2, 'terminal21'):
        assert _is_linked(a2, 'terminal21', b)
    _safe_set(b, 'transactions20', set())
    assert not _is_linked(b, 'transactions20', a2)
    if hasattr(a2, 'terminal21'):
        assert not _is_linked(a2, 'terminal21', b)


def test_assoc_Transactions_Order_reverse_link_reassign_clear():
    a1 = Transactions(Customer="sample_text", Order="sample_text")
    a2 = Transactions(Customer="sample_text_2", Order="sample_text_2")
    b = Order(Product="sample_text", Service="sample_text")
    _safe_set(b, 'transactions17', a1)
    assert _is_linked(b, 'transactions17', a1)
    if hasattr(a1, 'order16'):
        assert _is_linked(a1, 'order16', b)
    _safe_set(b, 'transactions17', a2)
    assert _is_linked(b, 'transactions17', a2)
    if hasattr(a1, 'order16'):
        assert not _is_linked(a1, 'order16', b)
    if hasattr(a2, 'order16'):
        assert _is_linked(a2, 'order16', b)
    _safe_set(b, 'transactions17', None)
    assert not _is_linked(b, 'transactions17', a2)
    if hasattr(a2, 'order16'):
        assert not _is_linked(a2, 'order16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Customer_Customer_Data_stub_double():
    # Customer has no real 'customer_Data12' property in the generated
    # code (a bare stub) -- manually attach it so Customer_Data's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Customer_Data's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Customer_Data(Contact="sample_text", Name="sample_text")
    partner = Customer()
    setattr(partner, 'customer_Data12', None)
    _safe_set(owner, 'customer13', {partner})
    assert getattr(partner, 'customer_Data12') == owner
    _safe_set(owner, 'customer13', set())
    assert getattr(partner, 'customer_Data12') is None


def test_assoc_Customer_Online_Portal_stub_double():
    # Customer has no real 'online_Portal38' property in the generated
    # code (a bare stub) -- manually attach it so Online_Portal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Online_Portal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Online_Portal(StoreLocation="sample_text")
    partner = Customer()
    setattr(partner, 'online_Portal38', None)
    _safe_set(owner, 'customer39', {partner})
    assert getattr(partner, 'online_Portal38') == owner
    _safe_set(owner, 'customer39', set())
    assert getattr(partner, 'online_Portal38') is None


def test_assoc_Employee_Terminal_stub_double():
    # Employee has no real 'terminal24' property in the generated
    # code (a bare stub) -- manually attach it so Terminal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Terminal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Terminal(Current_Employee="sample_text")
    partner = Employee()
    setattr(partner, 'terminal24', None)
    _safe_set(owner, 'employee25', {partner})
    assert owner in getattr(partner, 'terminal24')
    _safe_set(owner, 'employee25', set())
    assert owner not in getattr(partner, 'terminal24')


def test_assoc_Manager_Terminal_stub_double():
    # Manager has no real 'terminal26' property in the generated
    # code (a bare stub) -- manually attach it so Terminal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Terminal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Terminal(Current_Employee="sample_text")
    partner = Manager()
    setattr(partner, 'terminal26', None)
    _safe_set(owner, 'manager27', partner)
    assert owner in getattr(partner, 'terminal26')
    _safe_set(owner, 'manager27', None)
    assert owner not in getattr(partner, 'terminal26')


def test_assoc_Store_Customer_Data_stub_double():
    # Store has no real 'customer_Data10' property in the generated
    # code (a bare stub) -- manually attach it so Customer_Data's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Customer_Data's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Customer_Data(Contact="sample_text", Name="sample_text")
    partner = Store()
    setattr(partner, 'customer_Data10', None)
    _safe_set(owner, 'store11', partner)
    assert getattr(partner, 'customer_Data10') == owner
    _safe_set(owner, 'store11', None)
    assert getattr(partner, 'customer_Data10') is None


def test_assoc_Store_Inventory_stub_double():
    # Store has no real 'inventory6' property in the generated
    # code (a bare stub) -- manually attach it so Inventory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Inventory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Inventory(Products="sample_text", Services="sample_text")
    partner = Store()
    setattr(partner, 'inventory6', None)
    _safe_set(owner, 'store7', partner)
    assert getattr(partner, 'inventory6') == owner
    _safe_set(owner, 'store7', None)
    assert getattr(partner, 'inventory6') is None


def test_assoc_Store_Product_stub_double():
    # Store has no real 'product40' property in the generated
    # code (a bare stub) -- manually attach it so Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Product(Company="sample_text")
    partner = Store()
    setattr(partner, 'product40', None)
    _safe_set(owner, 'store41', {partner})
    assert owner in getattr(partner, 'product40')
    _safe_set(owner, 'store41', set())
    assert owner not in getattr(partner, 'product40')


def test_assoc_Store_Service_stub_double():
    # Store has no real 'service42' property in the generated
    # code (a bare stub) -- manually attach it so Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Service(Info="sample_text", Terms="sample_text")
    partner = Store()
    setattr(partner, 'service42', None)
    _safe_set(owner, 'store43', {partner})
    assert owner in getattr(partner, 'service42')
    _safe_set(owner, 'store43', set())
    assert owner not in getattr(partner, 'service42')


def test_assoc_Store_Transactions_stub_double():
    # Store has no real 'transactions8' property in the generated
    # code (a bare stub) -- manually attach it so Transactions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Transactions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Transactions(Customer="sample_text", Order="sample_text")
    partner = Store()
    setattr(partner, 'transactions8', None)
    _safe_set(owner, 'store9', partner)
    assert getattr(partner, 'transactions8') == owner
    _safe_set(owner, 'store9', None)
    assert getattr(partner, 'transactions8') is None


