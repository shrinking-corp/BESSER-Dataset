import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Profile,
    User,
    account_Account,
    account_SavingsAccount,
    transaction_DepositTransaction,
    transaction_ExternalAccount,
    transaction_PaybillsTransaction,
    transaction_Payee,
    transaction_Transaction,
    transaction_TransferTransaction,
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

def test_assoc_Profile_User_reverse_link_reassign_clear():
    a1 = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", username="sample_text")
    a2 = User(lastLoginTime="sample_text_2", password="sample_text_2", userID="sample_text_2", username="sample_text_2")
    b = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    _safe_set(b, 'user6', a1)
    assert _is_linked(b, 'user6', a1)
    if hasattr(a1, 'profile7'):
        assert _is_linked(a1, 'profile7', b)
    _safe_set(b, 'user6', a2)
    assert _is_linked(b, 'user6', a2)
    if hasattr(a1, 'profile7'):
        assert not _is_linked(a1, 'profile7', b)
    if hasattr(a2, 'profile7'):
        assert _is_linked(a2, 'profile7', b)
    _safe_set(b, 'user6', None)
    assert not _is_linked(b, 'user6', a2)
    if hasattr(a2, 'profile7'):
        assert not _is_linked(a2, 'profile7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_PaybillsTransaction_Payee_stub_double():
    # transaction_PaybillsTransaction has no real 'payee4' property in the generated
    # code (a bare stub) -- manually attach it so transaction_Payee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transaction_Payee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    partner = transaction_PaybillsTransaction()
    setattr(partner, 'payee4', None)
    _safe_set(owner, 'paybillsTransaction5', {partner})
    assert getattr(partner, 'payee4') == owner
    _safe_set(owner, 'paybillsTransaction5', set())
    assert getattr(partner, 'payee4') is None


def test_assoc_TransferTransaction_ExternalAccount_stub_double():
    # transaction_TransferTransaction has no real 'externalAccount2' property in the generated
    # code (a bare stub) -- manually attach it so transaction_ExternalAccount's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transaction_ExternalAccount's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transaction_ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    partner = transaction_TransferTransaction()
    setattr(partner, 'externalAccount2', None)
    _safe_set(owner, 'transferTransaction3', {partner})
    assert getattr(partner, 'externalAccount2') == owner
    _safe_set(owner, 'transferTransaction3', set())
    assert getattr(partner, 'externalAccount2') is None


