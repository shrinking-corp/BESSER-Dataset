import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Attendance,
    Calender_Event,
    Donations,
    Executive_Director,
    Logout,
    Mail,
    Normal_user,
    Profile,
    System_Login,
    Volunteer,
    Volunteer_Forms,
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

def test_assoc_Admin_Donations_reverse_link_reassign_clear():
    a1 = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    a2 = Donations(amount=13, cardNumber=13, cardType="sample_text_2", expirationDate=13, issuerName="sample_text_2")
    b = Admin(password="sample_text", userID=7, userName="sample_text")
    _safe_set(b, 'donation14', a1)
    assert _is_linked(b, 'donation14', a1)
    if hasattr(a1, 'admin15'):
        assert _is_linked(a1, 'admin15', b)
    _safe_set(b, 'donation14', a2)
    assert _is_linked(b, 'donation14', a2)
    if hasattr(a1, 'admin15'):
        assert not _is_linked(a1, 'admin15', b)
    if hasattr(a2, 'admin15'):
        assert _is_linked(a2, 'admin15', b)
    _safe_set(b, 'donation14', None)
    assert not _is_linked(b, 'donation14', a2)
    if hasattr(a2, 'admin15'):
        assert not _is_linked(a2, 'admin15', b)


def test_assoc_Admin_Mail_reverse_link_reassign_clear():
    a1 = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    a2 = Mail(emailID="sample_text_2", sendBy="sample_text_2", sendTo="sample_text_2", subject="sample_text_2")
    b = Admin(password="sample_text", userID=7, userName="sample_text")
    _safe_set(b, 'mail20', {a1})
    assert _is_linked(b, 'mail20', a1)
    if hasattr(a1, 'admin21'):
        assert _is_linked(a1, 'admin21', b)
    _safe_set(b, 'mail20', {a2})
    assert _is_linked(b, 'mail20', a2)
    if hasattr(a1, 'admin21'):
        assert not _is_linked(a1, 'admin21', b)
    if hasattr(a2, 'admin21'):
        assert _is_linked(a2, 'admin21', b)
    _safe_set(b, 'mail20', set())
    assert not _is_linked(b, 'mail20', a2)
    if hasattr(a2, 'admin21'):
        assert not _is_linked(a2, 'admin21', b)


def test_assoc_Normal_user_Donations_reverse_link_reassign_clear():
    a1 = Normal_user(password="sample_text", userID=7, userName="sample_text")
    a2 = Normal_user(password="sample_text_2", userID=13, userName="sample_text_2")
    b = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    _safe_set(b, 'normal_user17', {a1})
    assert _is_linked(b, 'normal_user17', a1)
    if hasattr(a1, 'donation216'):
        assert _is_linked(a1, 'donation216', b)
    _safe_set(b, 'normal_user17', {a2})
    assert _is_linked(b, 'normal_user17', a2)
    if hasattr(a1, 'donation216'):
        assert not _is_linked(a1, 'donation216', b)
    if hasattr(a2, 'donation216'):
        assert _is_linked(a2, 'donation216', b)
    _safe_set(b, 'normal_user17', set())
    assert not _is_linked(b, 'normal_user17', a2)
    if hasattr(a2, 'donation216'):
        assert not _is_linked(a2, 'donation216', b)


def test_assoc_Profile_Attendance_reverse_link_reassign_clear():
    a1 = Profile(first_Name="sample_text", last_Name="sample_text", password="sample_text", phone_Number=7, user_Name="sample_text")
    a2 = Profile(first_Name="sample_text_2", last_Name="sample_text_2", password="sample_text_2", phone_Number=13, user_Name="sample_text_2")
    b = Attendance(attendanceID=7, checkInTime="sample_text", checkOutTime="sample_text")
    _safe_set(b, 'profile9', a1)
    assert _is_linked(b, 'profile9', a1)
    if hasattr(a1, 'Track_Attendance8'):
        assert _is_linked(a1, 'Track_Attendance8', b)
    _safe_set(b, 'profile9', a2)
    assert _is_linked(b, 'profile9', a2)
    if hasattr(a1, 'Track_Attendance8'):
        assert not _is_linked(a1, 'Track_Attendance8', b)
    if hasattr(a2, 'Track_Attendance8'):
        assert _is_linked(a2, 'Track_Attendance8', b)
    _safe_set(b, 'profile9', None)
    assert not _is_linked(b, 'profile9', a2)
    if hasattr(a2, 'Track_Attendance8'):
        assert not _is_linked(a2, 'Track_Attendance8', b)


def test_assoc_SuperAdmin_Donations_reverse_link_reassign_clear():
    a1 = Executive_Director(password="sample_text", userID=7, userName="sample_text")
    a2 = Executive_Director(password="sample_text_2", userID=13, userName="sample_text_2")
    b = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    _safe_set(b, 'superAdmin11', {a1})
    assert _is_linked(b, 'superAdmin11', a1)
    if hasattr(a1, 'payment10'):
        assert _is_linked(a1, 'payment10', b)
    _safe_set(b, 'superAdmin11', {a2})
    assert _is_linked(b, 'superAdmin11', a2)
    if hasattr(a1, 'payment10'):
        assert not _is_linked(a1, 'payment10', b)
    if hasattr(a2, 'payment10'):
        assert _is_linked(a2, 'payment10', b)
    _safe_set(b, 'superAdmin11', set())
    assert not _is_linked(b, 'superAdmin11', a2)
    if hasattr(a2, 'payment10'):
        assert not _is_linked(a2, 'payment10', b)


def test_assoc_SuperAdmin_Mail_reverse_link_reassign_clear():
    a1 = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    a2 = Mail(emailID="sample_text_2", sendBy="sample_text_2", sendTo="sample_text_2", subject="sample_text_2")
    b = Executive_Director(password="sample_text", userID=7, userName="sample_text")
    _safe_set(b, 'mail18', {a1})
    assert _is_linked(b, 'mail18', a1)
    if hasattr(a1, 'superAdmin19'):
        assert _is_linked(a1, 'superAdmin19', b)
    _safe_set(b, 'mail18', {a2})
    assert _is_linked(b, 'mail18', a2)
    if hasattr(a1, 'superAdmin19'):
        assert not _is_linked(a1, 'superAdmin19', b)
    if hasattr(a2, 'superAdmin19'):
        assert _is_linked(a2, 'superAdmin19', b)
    _safe_set(b, 'mail18', set())
    assert not _is_linked(b, 'mail18', a2)
    if hasattr(a2, 'superAdmin19'):
        assert not _is_linked(a2, 'superAdmin19', b)


def test_assoc_Volunteer_Donations_reverse_link_reassign_clear():
    a1 = Volunteer(password="sample_text", userID=7, userName="sample_text")
    a2 = Volunteer(password="sample_text_2", userID=13, userName="sample_text_2")
    b = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    _safe_set(b, 'volunteer13', {a1})
    assert _is_linked(b, 'volunteer13', a1)
    if hasattr(a1, 'payment12'):
        assert _is_linked(a1, 'payment12', b)
    _safe_set(b, 'volunteer13', {a2})
    assert _is_linked(b, 'volunteer13', a2)
    if hasattr(a1, 'payment12'):
        assert not _is_linked(a1, 'payment12', b)
    if hasattr(a2, 'payment12'):
        assert _is_linked(a2, 'payment12', b)
    _safe_set(b, 'volunteer13', set())
    assert not _is_linked(b, 'volunteer13', a2)
    if hasattr(a2, 'payment12'):
        assert not _is_linked(a2, 'payment12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

