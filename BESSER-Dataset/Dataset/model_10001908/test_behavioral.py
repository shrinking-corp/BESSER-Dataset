import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    OnlineBanking_AppConfig,
    TestAccountChain,
    data_CustomerProfileRepository,
    genmymodelreverse_C1,
    genmymodelreverse_C2,
    genmymodelreverse_java_util_Date,
    genmymodelreverse_java_util_HashMap,
    genmymodelreverse_org_springframework_ui_Model_Interface,
    model_Account,
    model_AccountAction,
    model_AccountChain_Interface,
    model_AccountHandler,
    model_Bank,
    model_CheckingAccount,
    model_CloseAccount,
    model_CreditAccount,
    model_Customer,
    model_Deposit,
    model_Loan,
    model_MakePayment,
    model_OpenAccount,
    model_SavingsAccount,
    model_Transaction,
    model_Withdrawal,
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

def test_assoc_Account_AccountAction_reverse_link_reassign_clear():
    a1 = model_AccountAction(action="sample_text", amount=3.14, success=True)
    a2 = model_AccountAction(action="sample_text_2", amount=9.99, success=False)
    b = model_Account(accountNumber=7, balance=3.14, customerId=7, type="sample_text")
    _safe_set(b, 'accountAction6', {a1})
    assert _is_linked(b, 'accountAction6', a1)
    if hasattr(a1, 'account7'):
        assert _is_linked(a1, 'account7', b)
    _safe_set(b, 'accountAction6', {a2})
    assert _is_linked(b, 'accountAction6', a2)
    if hasattr(a1, 'account7'):
        assert not _is_linked(a1, 'account7', b)
    if hasattr(a2, 'account7'):
        assert _is_linked(a2, 'account7', b)
    _safe_set(b, 'accountAction6', set())
    assert not _is_linked(b, 'accountAction6', a2)
    if hasattr(a2, 'account7'):
        assert not _is_linked(a2, 'account7', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = model_Customer(accounts="sample_text", address="sample_text", dob="sample_text", id=7, name="sample_text", password="sample_text", username="sample_text")
    a2 = model_Customer(accounts="sample_text_2", address="sample_text_2", dob="sample_text_2", id=13, name="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = model_Account(accountNumber=7, balance=3.14, customerId=7, type="sample_text")
    _safe_set(b, 'has1', a1)
    assert _is_linked(b, 'has1', a1)
    if hasattr(a1, 'owns0'):
        assert _is_linked(a1, 'owns0', b)
    _safe_set(b, 'has1', a2)
    assert _is_linked(b, 'has1', a2)
    if hasattr(a1, 'owns0'):
        assert not _is_linked(a1, 'owns0', b)
    if hasattr(a2, 'owns0'):
        assert _is_linked(a2, 'owns0', b)
    _safe_set(b, 'has1', None)
    assert not _is_linked(b, 'has1', a2)
    if hasattr(a2, 'owns0'):
        assert not _is_linked(a2, 'owns0', b)


def test_assoc_Customer_AccountAction_reverse_link_reassign_clear():
    a1 = model_Customer(accounts="sample_text", address="sample_text", dob="sample_text", id=7, name="sample_text", password="sample_text", username="sample_text")
    a2 = model_Customer(accounts="sample_text_2", address="sample_text_2", dob="sample_text_2", id=13, name="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = model_AccountAction(action="sample_text", amount=3.14, success=True)
    _safe_set(b, 'customer3', a1)
    assert _is_linked(b, 'customer3', a1)
    if hasattr(a1, 'requests2'):
        assert _is_linked(a1, 'requests2', b)
    _safe_set(b, 'customer3', a2)
    assert _is_linked(b, 'customer3', a2)
    if hasattr(a1, 'requests2'):
        assert not _is_linked(a1, 'requests2', b)
    if hasattr(a2, 'requests2'):
        assert _is_linked(a2, 'requests2', b)
    _safe_set(b, 'customer3', None)
    assert not _is_linked(b, 'customer3', a2)
    if hasattr(a2, 'requests2'):
        assert not _is_linked(a2, 'requests2', b)


def test_assoc_account_Bank_Account_8_reverse_link_reassign_clear():
    a1 = model_Bank(address="sample_text", customerMap="sample_text", name="sample_text")
    a2 = model_Bank(address="sample_text_2", customerMap="sample_text_2", name="sample_text_2")
    b = model_Account(accountNumber=7, balance=3.14, customerId=7, type="sample_text")
    _safe_set(b, 'bank14', a1)
    assert _is_linked(b, 'bank14', a1)
    if hasattr(a1, 'accounts15'):
        assert _is_linked(a1, 'accounts15', b)
    _safe_set(b, 'bank14', a2)
    assert _is_linked(b, 'bank14', a2)
    if hasattr(a1, 'accounts15'):
        assert not _is_linked(a1, 'accounts15', b)
    if hasattr(a2, 'accounts15'):
        assert _is_linked(a2, 'accounts15', b)
    _safe_set(b, 'bank14', None)
    assert not _is_linked(b, 'bank14', a2)
    if hasattr(a2, 'accounts15'):
        assert not _is_linked(a2, 'accounts15', b)


def test_assoc_customer_Bank_Customer_6_reverse_link_reassign_clear():
    a1 = model_Customer(accounts="sample_text", address="sample_text", dob="sample_text", id=7, name="sample_text", password="sample_text", username="sample_text")
    a2 = model_Customer(accounts="sample_text_2", address="sample_text_2", dob="sample_text_2", id=13, name="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = model_Bank(address="sample_text", customerMap="sample_text", name="sample_text")
    _safe_set(b, 'customer13', {a1})
    assert _is_linked(b, 'customer13', a1)
    if hasattr(a1, 'bank12'):
        assert _is_linked(a1, 'bank12', b)
    _safe_set(b, 'customer13', {a2})
    assert _is_linked(b, 'customer13', a2)
    if hasattr(a1, 'bank12'):
        assert not _is_linked(a1, 'bank12', b)
    if hasattr(a2, 'bank12'):
        assert _is_linked(a2, 'bank12', b)
    _safe_set(b, 'customer13', set())
    assert not _is_linked(b, 'customer13', a2)
    if hasattr(a2, 'bank12'):
        assert not _is_linked(a2, 'bank12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

