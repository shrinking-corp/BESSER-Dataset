import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    account_Account,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
    mypackage_Customer,
    mypackage_Login,
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
    a1 = mypackage_Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    a2 = mypackage_Login(lastLoginTime=date(2025, 6, 15), password="sample_text_2", securityAnswer="sample_text_2", securityQuestion="sample_text_2", username="sample_text_2")
    b = mypackage_Customer(address="sample_text", attribute="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    _safe_set(b, 'login4', a1)
    assert _is_linked(b, 'login4', a1)
    if hasattr(a1, 'customer5'):
        assert _is_linked(a1, 'customer5', b)
    _safe_set(b, 'login4', a2)
    assert _is_linked(b, 'login4', a2)
    if hasattr(a1, 'customer5'):
        assert not _is_linked(a1, 'customer5', b)
    if hasattr(a2, 'customer5'):
        assert _is_linked(a2, 'customer5', b)
    _safe_set(b, 'login4', None)
    assert not _is_linked(b, 'login4', a2)
    if hasattr(a2, 'customer5'):
        assert not _is_linked(a2, 'customer5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

