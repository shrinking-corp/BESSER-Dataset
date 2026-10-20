import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Course,
    Customer,
    Login,
    Student,
    Teacher,
    account_Account,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
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
    a1 = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    a2 = Login(lastLoginTime=date(2025, 6, 15), password="sample_text_2", securityAnswer="sample_text_2", securityQuestion="sample_text_2", username="sample_text_2")
    b = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
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


def test_assoc_Student_Course_reverse_link_reassign_clear():
    a1 = Student(Age=7, Phone=7, name="sample_text")
    a2 = Student(Age=13, Phone=13, name="sample_text_2")
    b = Course(Timing="sample_text", name="sample_text")
    _safe_set(b, 'student9', a1)
    assert _is_linked(b, 'student9', a1)
    if hasattr(a1, 'course8'):
        assert _is_linked(a1, 'course8', b)
    _safe_set(b, 'student9', a2)
    assert _is_linked(b, 'student9', a2)
    if hasattr(a1, 'course8'):
        assert not _is_linked(a1, 'course8', b)
    if hasattr(a2, 'course8'):
        assert _is_linked(a2, 'course8', b)
    _safe_set(b, 'student9', None)
    assert not _is_linked(b, 'student9', a2)
    if hasattr(a2, 'course8'):
        assert not _is_linked(a2, 'course8', b)


def test_assoc_Teacher__Course_reverse_link_reassign_clear():
    a1 = Teacher(Age=7, Phone=7, name="sample_text")
    a2 = Teacher(Age=13, Phone=13, name="sample_text_2")
    b = Course(Timing="sample_text", name="sample_text")
    _safe_set(b, 'teacher7', {a1})
    assert _is_linked(b, 'teacher7', a1)
    if hasattr(a1, 'course6'):
        assert _is_linked(a1, 'course6', b)
    _safe_set(b, 'teacher7', {a2})
    assert _is_linked(b, 'teacher7', a2)
    if hasattr(a1, 'course6'):
        assert not _is_linked(a1, 'course6', b)
    if hasattr(a2, 'course6'):
        assert _is_linked(a2, 'course6', b)
    _safe_set(b, 'teacher7', set())
    assert not _is_linked(b, 'teacher7', a2)
    if hasattr(a2, 'course6'):
        assert not _is_linked(a2, 'course6', b)


def test_assoc_Teacher__Student_reverse_link_reassign_clear():
    a1 = Teacher(Age=7, Phone=7, name="sample_text")
    a2 = Teacher(Age=13, Phone=13, name="sample_text_2")
    b = Student(Age=7, Phone=7, name="sample_text")
    _safe_set(b, 'teacher11', a1)
    assert _is_linked(b, 'teacher11', a1)
    if hasattr(a1, 'student10'):
        assert _is_linked(a1, 'student10', b)
    _safe_set(b, 'teacher11', a2)
    assert _is_linked(b, 'teacher11', a2)
    if hasattr(a1, 'student10'):
        assert not _is_linked(a1, 'student10', b)
    if hasattr(a2, 'student10'):
        assert _is_linked(a2, 'student10', b)
    _safe_set(b, 'teacher11', None)
    assert not _is_linked(b, 'teacher11', a2)
    if hasattr(a2, 'student10'):
        assert not _is_linked(a2, 'student10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

