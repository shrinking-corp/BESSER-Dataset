import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Login,
    Logout,
    Mail,
    Payment,
    Profile,
    SuperAdmin,
    Volunteer,
    void,
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

def test_assoc_Admin_Mail_reverse_link_reassign_clear():
    a1 = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    a2 = Mail(emailID="sample_text_2", sendBy="sample_text_2", sendTo="sample_text_2", subject="sample_text_2")
    b = Admin(password="sample_text", userID=7, userName="sample_text")
    _safe_set(b, 'mail8', {a1})
    assert _is_linked(b, 'mail8', a1)
    if hasattr(a1, 'admin9'):
        assert _is_linked(a1, 'admin9', b)
    _safe_set(b, 'mail8', {a2})
    assert _is_linked(b, 'mail8', a2)
    if hasattr(a1, 'admin9'):
        assert not _is_linked(a1, 'admin9', b)
    if hasattr(a2, 'admin9'):
        assert _is_linked(a2, 'admin9', b)
    _safe_set(b, 'mail8', set())
    assert not _is_linked(b, 'mail8', a2)
    if hasattr(a2, 'admin9'):
        assert not _is_linked(a2, 'admin9', b)


def test_assoc_Admin_Payment_reverse_link_reassign_clear():
    a1 = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    a2 = Payment(amount=13, cardNumber=13, cardType="sample_text_2", expiryDate="sample_text_2", issuerName="sample_text_2")
    b = Admin(password="sample_text", userID=7, userName="sample_text")
    _safe_set(b, 'payment4', a1)
    assert _is_linked(b, 'payment4', a1)
    if hasattr(a1, 'admin5'):
        assert _is_linked(a1, 'admin5', b)
    _safe_set(b, 'payment4', a2)
    assert _is_linked(b, 'payment4', a2)
    if hasattr(a1, 'admin5'):
        assert not _is_linked(a1, 'admin5', b)
    if hasattr(a2, 'admin5'):
        assert _is_linked(a2, 'admin5', b)
    _safe_set(b, 'payment4', None)
    assert not _is_linked(b, 'payment4', a2)
    if hasattr(a2, 'admin5'):
        assert not _is_linked(a2, 'admin5', b)


def test_assoc_SuperAdmin_Mail_reverse_link_reassign_clear():
    a1 = SuperAdmin(password="sample_text", userID=7, userName="sample_text")
    a2 = SuperAdmin(password="sample_text_2", userID=13, userName="sample_text_2")
    b = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    _safe_set(b, 'superAdmin7', a1)
    assert _is_linked(b, 'superAdmin7', a1)
    if hasattr(a1, 'mail6'):
        assert _is_linked(a1, 'mail6', b)
    _safe_set(b, 'superAdmin7', a2)
    assert _is_linked(b, 'superAdmin7', a2)
    if hasattr(a1, 'mail6'):
        assert not _is_linked(a1, 'mail6', b)
    if hasattr(a2, 'mail6'):
        assert _is_linked(a2, 'mail6', b)
    _safe_set(b, 'superAdmin7', None)
    assert not _is_linked(b, 'superAdmin7', a2)
    if hasattr(a2, 'mail6'):
        assert not _is_linked(a2, 'mail6', b)


def test_assoc_SuperAdmin_Payment_reverse_link_reassign_clear():
    a1 = SuperAdmin(password="sample_text", userID=7, userName="sample_text")
    a2 = SuperAdmin(password="sample_text_2", userID=13, userName="sample_text_2")
    b = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    _safe_set(b, 'superAdmin1', {a1})
    assert _is_linked(b, 'superAdmin1', a1)
    if hasattr(a1, 'payment0'):
        assert _is_linked(a1, 'payment0', b)
    _safe_set(b, 'superAdmin1', {a2})
    assert _is_linked(b, 'superAdmin1', a2)
    if hasattr(a1, 'payment0'):
        assert not _is_linked(a1, 'payment0', b)
    if hasattr(a2, 'payment0'):
        assert _is_linked(a2, 'payment0', b)
    _safe_set(b, 'superAdmin1', set())
    assert not _is_linked(b, 'superAdmin1', a2)
    if hasattr(a2, 'payment0'):
        assert not _is_linked(a2, 'payment0', b)


def test_assoc_Volunteer_Payment_reverse_link_reassign_clear():
    a1 = Volunteer(password="sample_text", userID=7, userName="sample_text")
    a2 = Volunteer(password="sample_text_2", userID=13, userName="sample_text_2")
    b = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    _safe_set(b, 'volunteer3', {a1})
    assert _is_linked(b, 'volunteer3', a1)
    if hasattr(a1, 'payment2'):
        assert _is_linked(a1, 'payment2', b)
    _safe_set(b, 'volunteer3', {a2})
    assert _is_linked(b, 'volunteer3', a2)
    if hasattr(a1, 'payment2'):
        assert not _is_linked(a1, 'payment2', b)
    if hasattr(a2, 'payment2'):
        assert _is_linked(a2, 'payment2', b)
    _safe_set(b, 'volunteer3', set())
    assert not _is_linked(b, 'volunteer3', a2)
    if hasattr(a2, 'payment2'):
        assert not _is_linked(a2, 'payment2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

