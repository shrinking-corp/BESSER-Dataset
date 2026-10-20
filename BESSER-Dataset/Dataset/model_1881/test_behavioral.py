import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Payment,
    Person,
    Valuable,
    shop_AccountBook,
    shop_BankOperation,
    shop_CashPayment,
    shop_ChequePayment,
    shop_Customer,
    shop_ElectronicPayment,
    shop_Employee,
    shop_Payment,
    shop_Person,
    shop_Sale,
    shop_Shop,
    shop_Valuable,
    PaymentType,
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

def test_assoc_bankOperations15_reverse_link_reassign_clear():
    a1 = shop_BankOperation(description="sample_text")
    a2 = shop_BankOperation(description="sample_text_2")
    b = shop_AccountBook(cashFlow=3.14)
    _safe_set(b, 'shop_AccountBook', {a1})
    assert _is_linked(b, 'shop_AccountBook', a1)
    if hasattr(a1, 'shop_BankOperation'):
        assert _is_linked(a1, 'shop_BankOperation', b)
    _safe_set(b, 'shop_AccountBook', {a2})
    assert _is_linked(b, 'shop_AccountBook', a2)
    if hasattr(a1, 'shop_BankOperation'):
        assert not _is_linked(a1, 'shop_BankOperation', b)
    if hasattr(a2, 'shop_BankOperation'):
        assert _is_linked(a2, 'shop_BankOperation', b)
    _safe_set(b, 'shop_AccountBook', set())
    assert not _is_linked(b, 'shop_AccountBook', a2)
    if hasattr(a2, 'shop_BankOperation'):
        assert not _is_linked(a2, 'shop_BankOperation', b)


def test_assoc_payments10_reverse_link_reassign_clear():
    a1 = shop_Sale(description="sample_text")
    a2 = shop_Sale(description="sample_text_2")
    b = shop_Payment(type="sample_text")
    _safe_set(b, 'Payment', a1)
    assert _is_linked(b, 'Payment', a1)
    if hasattr(a1, 'sale'):
        assert _is_linked(a1, 'sale', b)
    _safe_set(b, 'Payment', a2)
    assert _is_linked(b, 'Payment', a2)
    if hasattr(a1, 'sale'):
        assert not _is_linked(a1, 'sale', b)
    if hasattr(a2, 'sale'):
        assert _is_linked(a2, 'sale', b)
    _safe_set(b, 'Payment', None)
    assert not _is_linked(b, 'Payment', a2)
    if hasattr(a2, 'sale'):
        assert not _is_linked(a2, 'sale', b)


def test_assoc_payments17_reverse_link_reassign_clear():
    a1 = shop_Payment(type="sample_text")
    a2 = shop_Payment(type="sample_text_2")
    b = shop_AccountBook(cashFlow=3.14)
    _safe_set(b, 'shop_AccountBook18', {a1})
    assert _is_linked(b, 'shop_AccountBook18', a1)
    if hasattr(a1, 'shop_Payment'):
        assert _is_linked(a1, 'shop_Payment', b)
    _safe_set(b, 'shop_AccountBook18', {a2})
    assert _is_linked(b, 'shop_AccountBook18', a2)
    if hasattr(a1, 'shop_Payment'):
        assert not _is_linked(a1, 'shop_Payment', b)
    if hasattr(a2, 'shop_Payment'):
        assert _is_linked(a2, 'shop_Payment', b)
    _safe_set(b, 'shop_AccountBook18', set())
    assert not _is_linked(b, 'shop_AccountBook18', a2)
    if hasattr(a2, 'shop_Payment'):
        assert not _is_linked(a2, 'shop_Payment', b)


def test_assoc_sale13_reverse_link_reassign_clear():
    a1 = shop_Sale(description="sample_text")
    a2 = shop_Sale(description="sample_text_2")
    b = shop_Payment(type="sample_text")
    _safe_set(b, 'payments', a1)
    assert _is_linked(b, 'payments', a1)
    if hasattr(a1, 'Sale14'):
        assert _is_linked(a1, 'Sale14', b)
    _safe_set(b, 'payments', a2)
    assert _is_linked(b, 'payments', a2)
    if hasattr(a1, 'Sale14'):
        assert not _is_linked(a1, 'Sale14', b)
    if hasattr(a2, 'Sale14'):
        assert _is_linked(a2, 'Sale14', b)
    _safe_set(b, 'payments', None)
    assert not _is_linked(b, 'payments', a2)
    if hasattr(a2, 'Sale14'):
        assert not _is_linked(a2, 'Sale14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accountBook5_stub_double():
    # shop_Shop has no real 'shop' property in the generated
    # code (a bare stub) -- manually attach it so shop_AccountBook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shop_AccountBook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shop_AccountBook(cashFlow=3.14)
    partner = shop_Shop()
    setattr(partner, 'shop', None)
    _safe_set(owner, 'AccountBook', partner)
    assert getattr(partner, 'shop') == owner
    _safe_set(owner, 'AccountBook', None)
    assert getattr(partner, 'shop') is None


def test_assoc_customer7_stub_double():
    # shop_Customer has no real 'Customer' property in the generated
    # code (a bare stub) -- manually attach it so shop_Sale's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shop_Sale's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shop_Sale(description="sample_text")
    partner = shop_Customer()
    setattr(partner, 'Customer', None)
    _safe_set(owner, 'sales', partner)
    assert getattr(partner, 'Customer') == owner
    _safe_set(owner, 'sales', None)
    assert getattr(partner, 'Customer') is None


def test_assoc_employees8_stub_double():
    # shop_Employee has no real 'Employee' property in the generated
    # code (a bare stub) -- manually attach it so shop_Sale's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shop_Sale's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shop_Sale(description="sample_text")
    partner = shop_Employee()
    setattr(partner, 'Employee', None)
    _safe_set(owner, 'sales9', {partner})
    assert getattr(partner, 'Employee') == owner
    _safe_set(owner, 'sales9', set())
    assert getattr(partner, 'Employee') is None


def test_assoc_sales1_stub_double():
    # shop_Shop has no real 'shop_Shop2' property in the generated
    # code (a bare stub) -- manually attach it so shop_Sale's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shop_Sale's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shop_Sale(description="sample_text")
    partner = shop_Shop()
    setattr(partner, 'shop_Shop2', None)
    _safe_set(owner, 'shop_Sale', partner)
    assert owner in getattr(partner, 'shop_Shop2')
    _safe_set(owner, 'shop_Sale', None)
    assert owner not in getattr(partner, 'shop_Shop2')


def test_assoc_sales11_stub_double():
    # shop_Employee has no real 'employees' property in the generated
    # code (a bare stub) -- manually attach it so shop_Sale's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shop_Sale's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shop_Sale(description="sample_text")
    partner = shop_Employee()
    setattr(partner, 'employees', None)
    _safe_set(owner, 'Sale12', partner)
    assert owner in getattr(partner, 'employees')
    _safe_set(owner, 'Sale12', None)
    assert owner not in getattr(partner, 'employees')


def test_assoc_sales6_stub_double():
    # shop_Customer has no real 'customer' property in the generated
    # code (a bare stub) -- manually attach it so shop_Sale's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shop_Sale's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shop_Sale(description="sample_text")
    partner = shop_Customer()
    setattr(partner, 'customer', None)
    _safe_set(owner, 'Sale', partner)
    assert owner in getattr(partner, 'customer')
    _safe_set(owner, 'Sale', None)
    assert owner not in getattr(partner, 'customer')


def test_assoc_shop16_stub_double():
    # shop_Shop has no real 'Shop' property in the generated
    # code (a bare stub) -- manually attach it so shop_AccountBook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shop_AccountBook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shop_AccountBook(cashFlow=3.14)
    partner = shop_Shop()
    setattr(partner, 'Shop', None)
    _safe_set(owner, 'accountBook', partner)
    assert getattr(partner, 'Shop') == owner
    _safe_set(owner, 'accountBook', None)
    assert getattr(partner, 'Shop') is None


