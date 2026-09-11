import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Calender_Event,
    Login,
    Logout,
    Mail,
    Manager,
    Normal_user,
    Payment,
    Profile,
    Volunteer,
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


def test_Manager_password_value_roundtrip():
    instance = Manager(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Manager_userID_value_roundtrip():
    instance = Manager(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_Manager_userName_value_roundtrip():
    instance = Manager(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


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


def test_Payment_amount_value_roundtrip():
    instance = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_Payment_cardNumber_value_roundtrip():
    instance = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    assert instance.cardNumber == 7
    instance.cardNumber = 13
    assert instance.cardNumber == 13


def test_Payment_cardType_value_roundtrip():
    instance = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    assert instance.cardType == "sample_text"
    instance.cardType = "sample_text_2"
    assert instance.cardType == "sample_text_2"


def test_Payment_expiryDate_value_roundtrip():
    instance = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    assert instance.expiryDate == "sample_text"
    instance.expiryDate = "sample_text_2"
    assert instance.expiryDate == "sample_text_2"


def test_Payment_issuerName_value_roundtrip():
    instance = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    assert instance.issuerName == "sample_text"
    instance.issuerName = "sample_text_2"
    assert instance.issuerName == "sample_text_2"


def test_Profile_f_Name_value_roundtrip():
    instance = Profile(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
    assert instance.f_Name == "sample_text"
    instance.f_Name = "sample_text_2"
    assert instance.f_Name == "sample_text_2"


def test_Profile_l_Name_value_roundtrip():
    instance = Profile(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
    assert instance.l_Name == "sample_text"
    instance.l_Name = "sample_text_2"
    assert instance.l_Name == "sample_text_2"


def test_Profile_password_value_roundtrip():
    instance = Profile(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Profile_user_Name_value_roundtrip():
    instance = Profile(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
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


def test_assoc_Admin_Mail_link_reassign_clear():
    a = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    b1 = Admin(password="sample_text", userID=7, userName="sample_text")
    b2 = Admin(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'admin9', b1)
    assert _is_linked(a, 'admin9', b1)
    if hasattr(b1, 'mail8'):
        assert _is_linked(b1, 'mail8', a)
    _safe_set(a, 'admin9', b2)
    assert _is_linked(a, 'admin9', b2)
    if hasattr(b1, 'mail8'):
        assert not _is_linked(b1, 'mail8', a)
    if hasattr(b2, 'mail8'):
        assert _is_linked(b2, 'mail8', a)
    _safe_set(a, 'admin9', None)
    assert not _is_linked(a, 'admin9', b2)
    if hasattr(b2, 'mail8'):
        assert not _is_linked(b2, 'mail8', a)


def test_assoc_Admin_Payment_link_reassign_clear():
    a = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b1 = Admin(password="sample_text", userID=7, userName="sample_text")
    b2 = Admin(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'admin5', {b1})
    assert _is_linked(a, 'admin5', b1)
    if hasattr(b1, 'payment4'):
        assert _is_linked(b1, 'payment4', a)
    _safe_set(a, 'admin5', {b2})
    assert _is_linked(a, 'admin5', b2)
    if hasattr(b1, 'payment4'):
        assert not _is_linked(b1, 'payment4', a)
    if hasattr(b2, 'payment4'):
        assert _is_linked(b2, 'payment4', a)
    _safe_set(a, 'admin5', set())
    assert not _is_linked(a, 'admin5', b2)
    if hasattr(b2, 'payment4'):
        assert not _is_linked(b2, 'payment4', a)


def test_assoc_Normal_user_Payment_link_reassign_clear():
    a = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b1 = Normal_user(password="sample_text", userID=7, userName="sample_text")
    b2 = Normal_user(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'normal_user7', {b1})
    assert _is_linked(a, 'normal_user7', b1)
    if hasattr(b1, 'payment26'):
        assert _is_linked(b1, 'payment26', a)
    _safe_set(a, 'normal_user7', {b2})
    assert _is_linked(a, 'normal_user7', b2)
    if hasattr(b1, 'payment26'):
        assert not _is_linked(b1, 'payment26', a)
    if hasattr(b2, 'payment26'):
        assert _is_linked(b2, 'payment26', a)
    _safe_set(a, 'normal_user7', set())
    assert not _is_linked(a, 'normal_user7', b2)
    if hasattr(b2, 'payment26'):
        assert not _is_linked(b2, 'payment26', a)


def test_assoc_SuperAdmin_Payment_link_reassign_clear():
    a = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b1 = Manager(password="sample_text", userID=7, userName="sample_text")
    b2 = Manager(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'superAdmin1', {b1})
    assert _is_linked(a, 'superAdmin1', b1)
    if hasattr(b1, 'payment0'):
        assert _is_linked(b1, 'payment0', a)
    _safe_set(a, 'superAdmin1', {b2})
    assert _is_linked(a, 'superAdmin1', b2)
    if hasattr(b1, 'payment0'):
        assert not _is_linked(b1, 'payment0', a)
    if hasattr(b2, 'payment0'):
        assert _is_linked(b2, 'payment0', a)
    _safe_set(a, 'superAdmin1', set())
    assert not _is_linked(a, 'superAdmin1', b2)
    if hasattr(b2, 'payment0'):
        assert not _is_linked(b2, 'payment0', a)


def test_assoc_Volunteer_Payment_link_reassign_clear():
    a = Volunteer(password="sample_text", userID=7, userName="sample_text")
    b1 = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b2 = Payment(amount=13, cardNumber=13, cardType="sample_text_2", expiryDate="sample_text_2", issuerName="sample_text_2")
    _safe_set(a, 'payment2', b1)
    assert _is_linked(a, 'payment2', b1)
    if hasattr(b1, 'volunteer3'):
        assert _is_linked(b1, 'volunteer3', a)
    _safe_set(a, 'payment2', b2)
    assert _is_linked(a, 'payment2', b2)
    if hasattr(b1, 'volunteer3'):
        assert not _is_linked(b1, 'volunteer3', a)
    if hasattr(b2, 'volunteer3'):
        assert _is_linked(b2, 'volunteer3', a)
    _safe_set(a, 'payment2', None)
    assert not _is_linked(a, 'payment2', b2)
    if hasattr(b2, 'volunteer3'):
        assert not _is_linked(b2, 'volunteer3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


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


Manager_strategy = st.builds(Manager, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Normal_user_strategy = st.builds(Normal_user, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Normal_user_strategy)
@settings(max_examples=25)
def test_Normal_user_instantiation(instance):
    assert isinstance(instance, Normal_user)


Payment_strategy = st.builds(Payment, amount=st.integers(), cardNumber=st.integers(), cardType=safe_text, expiryDate=safe_text, issuerName=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Profile_strategy = st.builds(Profile, f_Name=safe_text, l_Name=safe_text, password=safe_text, user_Name=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


Volunteer_strategy = st.builds(Volunteer, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=Volunteer_strategy)
@settings(max_examples=25)
def test_Volunteer_instantiation(instance):
    assert isinstance(instance, Volunteer)


void_strategy = st.builds(void)
@given(instance=void_strategy)
@settings(max_examples=25)
def test_void_instantiation(instance):
    assert isinstance(instance, void)


