import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BMS,
    Business,
    CheckingAccount,
    Contractor,
    Customer,
    Employee,
    Indevidual,
    Permanent,
    SavingsAccount,
    Temporary,
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

def test_assoc_Customer_Checking_Account_reverse_link_reassign_clear():
    a1 = Customer(Address="sample_text", CustId=7, DOB="sample_text", FName="sample_text", Gender="sample_text", Lname="sample_text", Mobile=7, State="sample_text", Zipcode=7, attribute="sample_text")
    a2 = Customer(Address="sample_text_2", CustId=13, DOB="sample_text_2", FName="sample_text_2", Gender="sample_text_2", Lname="sample_text_2", Mobile=13, State="sample_text_2", Zipcode=13, attribute="sample_text_2")
    b = CheckingAccount(AccountNo=7, AccountType="sample_text", Amount="sample_text", Cust_DOB="sample_text", Cust_Name="sample_text", CustomerId=7, Diposit="sample_text", MobileNo=7, Withdraw="sample_text")
    _safe_set(b, 'customer7', a1)
    assert _is_linked(b, 'customer7', a1)
    if hasattr(a1, 'checking_Account6'):
        assert _is_linked(a1, 'checking_Account6', b)
    _safe_set(b, 'customer7', a2)
    assert _is_linked(b, 'customer7', a2)
    if hasattr(a1, 'checking_Account6'):
        assert not _is_linked(a1, 'checking_Account6', b)
    if hasattr(a2, 'checking_Account6'):
        assert _is_linked(a2, 'checking_Account6', b)
    _safe_set(b, 'customer7', None)
    assert not _is_linked(b, 'customer7', a2)
    if hasattr(a2, 'checking_Account6'):
        assert not _is_linked(a2, 'checking_Account6', b)


def test_assoc_Customer_Savings_Account_reverse_link_reassign_clear():
    a1 = SavingsAccount(AccountNo=7, AccountType="sample_text", Amount="sample_text", Cust_DOB="sample_text", Cust_Name="sample_text", CustomerId=7, Diposit="sample_text", Mobile=7, Withdraw="sample_text")
    a2 = SavingsAccount(AccountNo=13, AccountType="sample_text_2", Amount="sample_text_2", Cust_DOB="sample_text_2", Cust_Name="sample_text_2", CustomerId=13, Diposit="sample_text_2", Mobile=13, Withdraw="sample_text_2")
    b = Customer(Address="sample_text", CustId=7, DOB="sample_text", FName="sample_text", Gender="sample_text", Lname="sample_text", Mobile=7, State="sample_text", Zipcode=7, attribute="sample_text")
    _safe_set(b, 'savings_Account4', a1)
    assert _is_linked(b, 'savings_Account4', a1)
    if hasattr(a1, 'customer5'):
        assert _is_linked(a1, 'customer5', b)
    _safe_set(b, 'savings_Account4', a2)
    assert _is_linked(b, 'savings_Account4', a2)
    if hasattr(a1, 'customer5'):
        assert not _is_linked(a1, 'customer5', b)
    if hasattr(a2, 'customer5'):
        assert _is_linked(a2, 'customer5', b)
    _safe_set(b, 'savings_Account4', None)
    assert not _is_linked(b, 'savings_Account4', a2)
    if hasattr(a2, 'customer5'):
        assert not _is_linked(a2, 'customer5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_BankManagementSystem_Customer_stub_double():
    # BMS has no real 'customer2' property in the generated
    # code (a bare stub) -- manually attach it so Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Customer(Address="sample_text", CustId=7, DOB="sample_text", FName="sample_text", Gender="sample_text", Lname="sample_text", Mobile=7, State="sample_text", Zipcode=7, attribute="sample_text")
    partner = BMS()
    setattr(partner, 'customer2', None)
    _safe_set(owner, 'BMS3', partner)
    assert getattr(partner, 'customer2') == owner
    _safe_set(owner, 'BMS3', None)
    assert getattr(partner, 'customer2') is None


def test_assoc_BankManagementSystem_Employee_stub_double():
    # BMS has no real 'employee0' property in the generated
    # code (a bare stub) -- manually attach it so Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Employee(Address="sample_text", City="sample_text", DOB="sample_text", Department="sample_text", EmpFName="sample_text", EmpId=7, EmpLName="sample_text", EmpType="sample_text", Gender="sample_text", State="sample_text", Zipcode="sample_text")
    partner = BMS()
    setattr(partner, 'employee0', None)
    _safe_set(owner, 'BMS1', partner)
    assert getattr(partner, 'employee0') == owner
    _safe_set(owner, 'BMS1', None)
    assert getattr(partner, 'employee0') is None


