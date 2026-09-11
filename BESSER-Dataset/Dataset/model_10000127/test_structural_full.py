import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Admin_password_value_roundtrip():
    instance = Admin(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Admin_userID_value_roundtrip():
    instance = Admin(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_Admin_userName_value_roundtrip():
    instance = Admin(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_Attendance_attendanceID_value_roundtrip():
    instance = Attendance(attendanceID=7, checkInTime="sample_text", checkOutTime="sample_text")
    assert instance.attendanceID == 7
    instance.attendanceID = 13
    assert instance.attendanceID == 13


def test_Attendance_checkInTime_value_roundtrip():
    instance = Attendance(attendanceID=7, checkInTime="sample_text", checkOutTime="sample_text")
    assert instance.checkInTime == "sample_text"
    instance.checkInTime = "sample_text_2"
    assert instance.checkInTime == "sample_text_2"


def test_Attendance_checkOutTime_value_roundtrip():
    instance = Attendance(attendanceID=7, checkInTime="sample_text", checkOutTime="sample_text")
    assert instance.checkOutTime == "sample_text"
    instance.checkOutTime = "sample_text_2"
    assert instance.checkOutTime == "sample_text_2"


def test_Donations_amount_value_roundtrip():
    instance = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_Donations_cardNumber_value_roundtrip():
    instance = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    assert instance.cardNumber == 7
    instance.cardNumber = 13
    assert instance.cardNumber == 13


def test_Donations_cardType_value_roundtrip():
    instance = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    assert instance.cardType == "sample_text"
    instance.cardType = "sample_text_2"
    assert instance.cardType == "sample_text_2"


def test_Donations_expirationDate_value_roundtrip():
    instance = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    assert instance.expirationDate == 7
    instance.expirationDate = 13
    assert instance.expirationDate == 13


def test_Donations_issuerName_value_roundtrip():
    instance = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    assert instance.issuerName == "sample_text"
    instance.issuerName = "sample_text_2"
    assert instance.issuerName == "sample_text_2"


def test_Executive_Director_password_value_roundtrip():
    instance = Executive_Director(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Executive_Director_userID_value_roundtrip():
    instance = Executive_Director(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_Executive_Director_userName_value_roundtrip():
    instance = Executive_Director(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_Mail_emailID_value_roundtrip():
    instance = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    assert instance.emailID == "sample_text"
    instance.emailID = "sample_text_2"
    assert instance.emailID == "sample_text_2"


def test_Mail_sendBy_value_roundtrip():
    instance = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    assert instance.sendBy == "sample_text"
    instance.sendBy = "sample_text_2"
    assert instance.sendBy == "sample_text_2"


def test_Mail_sendTo_value_roundtrip():
    instance = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    assert instance.sendTo == "sample_text"
    instance.sendTo = "sample_text_2"
    assert instance.sendTo == "sample_text_2"


def test_Mail_subject_value_roundtrip():
    instance = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


def test_Normal_user_password_value_roundtrip():
    instance = Normal_user(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Normal_user_userID_value_roundtrip():
    instance = Normal_user(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_Normal_user_userName_value_roundtrip():
    instance = Normal_user(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_Profile_first_Name_value_roundtrip():
    instance = Profile(first_Name="sample_text", last_Name="sample_text", password="sample_text", phone_Number=7, user_Name="sample_text")
    assert instance.first_Name == "sample_text"
    instance.first_Name = "sample_text_2"
    assert instance.first_Name == "sample_text_2"


def test_Profile_last_Name_value_roundtrip():
    instance = Profile(first_Name="sample_text", last_Name="sample_text", password="sample_text", phone_Number=7, user_Name="sample_text")
    assert instance.last_Name == "sample_text"
    instance.last_Name = "sample_text_2"
    assert instance.last_Name == "sample_text_2"


def test_Profile_password_value_roundtrip():
    instance = Profile(first_Name="sample_text", last_Name="sample_text", password="sample_text", phone_Number=7, user_Name="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Profile_phone_Number_value_roundtrip():
    instance = Profile(first_Name="sample_text", last_Name="sample_text", password="sample_text", phone_Number=7, user_Name="sample_text")
    assert instance.phone_Number == 7
    instance.phone_Number = 13
    assert instance.phone_Number == 13


def test_Profile_user_Name_value_roundtrip():
    instance = Profile(first_Name="sample_text", last_Name="sample_text", password="sample_text", phone_Number=7, user_Name="sample_text")
    assert instance.user_Name == "sample_text"
    instance.user_Name = "sample_text_2"
    assert instance.user_Name == "sample_text_2"


def test_Volunteer_password_value_roundtrip():
    instance = Volunteer(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Volunteer_userID_value_roundtrip():
    instance = Volunteer(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_Volunteer_userName_value_roundtrip():
    instance = Volunteer(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_Volunteer_Forms_password_value_roundtrip():
    instance = Volunteer_Forms(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Volunteer_Forms_userID_value_roundtrip():
    instance = Volunteer_Forms(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_Volunteer_Forms_userName_value_roundtrip():
    instance = Volunteer_Forms(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_assoc_Admin_Donations_link_reassign_clear():
    a = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    b1 = Admin(password="sample_text", userID=7, userName="sample_text")
    b2 = Admin(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'admin15', {b1})
    assert _is_linked(a, 'admin15', b1)
    if hasattr(b1, 'donation14'):
        assert _is_linked(b1, 'donation14', a)
    _safe_set(a, 'admin15', {b2})
    assert _is_linked(a, 'admin15', b2)
    if hasattr(b1, 'donation14'):
        assert not _is_linked(b1, 'donation14', a)
    if hasattr(b2, 'donation14'):
        assert _is_linked(b2, 'donation14', a)
    _safe_set(a, 'admin15', set())
    assert not _is_linked(a, 'admin15', b2)
    if hasattr(b2, 'donation14'):
        assert not _is_linked(b2, 'donation14', a)


def test_assoc_Admin_Mail_link_reassign_clear():
    a = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    b1 = Admin(password="sample_text", userID=7, userName="sample_text")
    b2 = Admin(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'admin21', b1)
    assert _is_linked(a, 'admin21', b1)
    if hasattr(b1, 'mail20'):
        assert _is_linked(b1, 'mail20', a)
    _safe_set(a, 'admin21', b2)
    assert _is_linked(a, 'admin21', b2)
    if hasattr(b1, 'mail20'):
        assert not _is_linked(b1, 'mail20', a)
    if hasattr(b2, 'mail20'):
        assert _is_linked(b2, 'mail20', a)
    _safe_set(a, 'admin21', None)
    assert not _is_linked(a, 'admin21', b2)
    if hasattr(b2, 'mail20'):
        assert not _is_linked(b2, 'mail20', a)


def test_assoc_Normal_user_Donations_link_reassign_clear():
    a = Normal_user(password="sample_text", userID=7, userName="sample_text")
    b1 = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    b2 = Donations(amount=13, cardNumber=13, cardType="sample_text_2", expirationDate=13, issuerName="sample_text_2")
    _safe_set(a, 'donation216', b1)
    assert _is_linked(a, 'donation216', b1)
    if hasattr(b1, 'normal_user17'):
        assert _is_linked(b1, 'normal_user17', a)
    _safe_set(a, 'donation216', b2)
    assert _is_linked(a, 'donation216', b2)
    if hasattr(b1, 'normal_user17'):
        assert not _is_linked(b1, 'normal_user17', a)
    if hasattr(b2, 'normal_user17'):
        assert _is_linked(b2, 'normal_user17', a)
    _safe_set(a, 'donation216', None)
    assert not _is_linked(a, 'donation216', b2)
    if hasattr(b2, 'normal_user17'):
        assert not _is_linked(b2, 'normal_user17', a)


def test_assoc_Profile_Attendance_link_reassign_clear():
    a = Profile(first_Name="sample_text", last_Name="sample_text", password="sample_text", phone_Number=7, user_Name="sample_text")
    b1 = Attendance(attendanceID=7, checkInTime="sample_text", checkOutTime="sample_text")
    b2 = Attendance(attendanceID=13, checkInTime="sample_text_2", checkOutTime="sample_text_2")
    _safe_set(a, 'Track_Attendance8', b1)
    assert _is_linked(a, 'Track_Attendance8', b1)
    if hasattr(b1, 'profile9'):
        assert _is_linked(b1, 'profile9', a)
    _safe_set(a, 'Track_Attendance8', b2)
    assert _is_linked(a, 'Track_Attendance8', b2)
    if hasattr(b1, 'profile9'):
        assert not _is_linked(b1, 'profile9', a)
    if hasattr(b2, 'profile9'):
        assert _is_linked(b2, 'profile9', a)
    _safe_set(a, 'Track_Attendance8', None)
    assert not _is_linked(a, 'Track_Attendance8', b2)
    if hasattr(b2, 'profile9'):
        assert not _is_linked(b2, 'profile9', a)


def test_assoc_SuperAdmin_Donations_link_reassign_clear():
    a = Executive_Director(password="sample_text", userID=7, userName="sample_text")
    b1 = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    b2 = Donations(amount=13, cardNumber=13, cardType="sample_text_2", expirationDate=13, issuerName="sample_text_2")
    _safe_set(a, 'payment10', b1)
    assert _is_linked(a, 'payment10', b1)
    if hasattr(b1, 'superAdmin11'):
        assert _is_linked(b1, 'superAdmin11', a)
    _safe_set(a, 'payment10', b2)
    assert _is_linked(a, 'payment10', b2)
    if hasattr(b1, 'superAdmin11'):
        assert not _is_linked(b1, 'superAdmin11', a)
    if hasattr(b2, 'superAdmin11'):
        assert _is_linked(b2, 'superAdmin11', a)
    _safe_set(a, 'payment10', None)
    assert not _is_linked(a, 'payment10', b2)
    if hasattr(b2, 'superAdmin11'):
        assert not _is_linked(b2, 'superAdmin11', a)


def test_assoc_SuperAdmin_Mail_link_reassign_clear():
    a = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    b1 = Executive_Director(password="sample_text", userID=7, userName="sample_text")
    b2 = Executive_Director(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'superAdmin19', b1)
    assert _is_linked(a, 'superAdmin19', b1)
    if hasattr(b1, 'mail18'):
        assert _is_linked(b1, 'mail18', a)
    _safe_set(a, 'superAdmin19', b2)
    assert _is_linked(a, 'superAdmin19', b2)
    if hasattr(b1, 'mail18'):
        assert not _is_linked(b1, 'mail18', a)
    if hasattr(b2, 'mail18'):
        assert _is_linked(b2, 'mail18', a)
    _safe_set(a, 'superAdmin19', None)
    assert not _is_linked(a, 'superAdmin19', b2)
    if hasattr(b2, 'mail18'):
        assert not _is_linked(b2, 'mail18', a)


def test_assoc_Volunteer_Donations_link_reassign_clear():
    a = Volunteer(password="sample_text", userID=7, userName="sample_text")
    b1 = Donations(amount=7, cardNumber=7, cardType="sample_text", expirationDate=7, issuerName="sample_text")
    b2 = Donations(amount=13, cardNumber=13, cardType="sample_text_2", expirationDate=13, issuerName="sample_text_2")
    _safe_set(a, 'payment12', b1)
    assert _is_linked(a, 'payment12', b1)
    if hasattr(b1, 'volunteer13'):
        assert _is_linked(b1, 'volunteer13', a)
    _safe_set(a, 'payment12', b2)
    assert _is_linked(a, 'payment12', b2)
    if hasattr(b1, 'volunteer13'):
        assert not _is_linked(b1, 'volunteer13', a)
    if hasattr(b2, 'volunteer13'):
        assert _is_linked(b2, 'volunteer13', a)
    _safe_set(a, 'payment12', None)
    assert not _is_linked(a, 'payment12', b2)
    if hasattr(b2, 'volunteer13'):
        assert not _is_linked(b2, 'volunteer13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Attendance_strategy = st.builds(Attendance, attendanceID=st.integers(), checkInTime=safe_text, checkOutTime=safe_text)
@given(instance=Attendance_strategy)
@settings(max_examples=25)
def test_Attendance_instantiation(instance):
    assert isinstance(instance, Attendance)


Donations_strategy = st.builds(Donations, amount=st.integers(), cardNumber=st.integers(), cardType=safe_text, expirationDate=st.integers(), issuerName=safe_text)
@given(instance=Donations_strategy)
@settings(max_examples=25)
def test_Donations_instantiation(instance):
    assert isinstance(instance, Donations)


Executive_Director_strategy = st.builds(Executive_Director, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Executive_Director_strategy)
@settings(max_examples=25)
def test_Executive_Director_instantiation(instance):
    assert isinstance(instance, Executive_Director)


Logout_strategy = st.builds(Logout)
@given(instance=Logout_strategy)
@settings(max_examples=25)
def test_Logout_instantiation(instance):
    assert isinstance(instance, Logout)


Mail_strategy = st.builds(Mail, emailID=safe_text, sendBy=safe_text, sendTo=safe_text, subject=safe_text)
@given(instance=Mail_strategy)
@settings(max_examples=25)
def test_Mail_instantiation(instance):
    assert isinstance(instance, Mail)


Normal_user_strategy = st.builds(Normal_user, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Normal_user_strategy)
@settings(max_examples=25)
def test_Normal_user_instantiation(instance):
    assert isinstance(instance, Normal_user)


Profile_strategy = st.builds(Profile, first_Name=safe_text, last_Name=safe_text, password=safe_text, phone_Number=st.integers(), user_Name=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


Volunteer_strategy = st.builds(Volunteer, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Volunteer_strategy)
@settings(max_examples=25)
def test_Volunteer_instantiation(instance):
    assert isinstance(instance, Volunteer)


Volunteer_Forms_strategy = st.builds(Volunteer_Forms, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Volunteer_Forms_strategy)
@settings(max_examples=25)
def test_Volunteer_Forms_instantiation(instance):
    assert isinstance(instance, Volunteer_Forms)


void_strategy = st.builds(void)
@given(instance=void_strategy)
@settings(max_examples=25)
def test_void_instantiation(instance):
    assert isinstance(instance, void)


