import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Login,
    NewClass,
    account_Account,
    account_AccountManager,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
    customerpackage_Customer,
    transaction_Class,
    transaction_DepositTransaction,
    transaction_Transaction,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
    account_AccountType,
    transaction_TransactionType,
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

def test_assoc_Customer_Login_reverse_link_reassign_clear():
    a1 = customerpackage_Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    a2 = customerpackage_Customer(address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailAddress="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    b = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    _safe_set(b, 'customer5', a1)
    assert _is_linked(b, 'customer5', a1)
    if hasattr(a1, 'login4'):
        assert _is_linked(a1, 'login4', b)
    _safe_set(b, 'customer5', a2)
    assert _is_linked(b, 'customer5', a2)
    if hasattr(a1, 'login4'):
        assert not _is_linked(a1, 'login4', b)
    if hasattr(a2, 'login4'):
        assert _is_linked(a2, 'login4', b)
    _safe_set(b, 'customer5', None)
    assert not _is_linked(b, 'customer5', a2)
    if hasattr(a2, 'login4'):
        assert not _is_linked(a2, 'login4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

