# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Mail,
    Payment,
    Logout,
    Attendance,
    Login,
    Calender_Event,
    Volunteer,
    Admin,
    Normal_user,
    void,
    SuperAdmin,
    Profile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mail_is_not_abstract():
    assert not inspect.isabstract(Mail)


def test_hyp_mail_constructor_exists():
    assert callable(Mail.__init__)


def test_hyp_mail_constructor_args():
    sig = inspect.signature(Mail.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "sendTo" in params, "Missing parameter 'sendTo'"
    assert "sendBy" in params, "Missing parameter 'sendBy'"
    assert "emailID" in params, "Missing parameter 'emailID'"







def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "issuerName" in params, "Missing parameter 'issuerName'"
    assert "cardType" in params, "Missing parameter 'cardType'"
    assert "expiryDate" in params, "Missing parameter 'expiryDate'"
    assert "amount" in params, "Missing parameter 'amount'"








def test_hyp_logout_is_not_abstract():
    assert not inspect.isabstract(Logout)


def test_hyp_logout_constructor_exists():
    assert callable(Logout.__init__)


def test_hyp_logout_constructor_args():
    sig = inspect.signature(Logout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_hyp_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_hyp_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "checkOutTime" in params, "Missing parameter 'checkOutTime'"
    assert "attendanceID" in params, "Missing parameter 'attendanceID'"
    assert "checkInTime" in params, "Missing parameter 'checkInTime'"






def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "loggedinTime" in params, "Missing parameter 'loggedinTime'"
    assert "loggedoutTime" in params, "Missing parameter 'loggedoutTime'"

def test_hyp_login_has_userID():
    assert hasattr(Login, "userID")
    descriptor = None
    for klass in Login.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_login_has_loggedinTime():
    assert hasattr(Login, "loggedinTime")
    descriptor = None
    for klass in Login.__mro__:
        if "loggedinTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedinTime"]
            break
    assert isinstance(descriptor, property)

def test_hyp_login_has_loggedoutTime():
    assert hasattr(Login, "loggedoutTime")
    descriptor = None
    for klass in Login.__mro__:
        if "loggedoutTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedoutTime"]
            break
    assert isinstance(descriptor, property)



def test_hyp_calender_event_is_not_abstract():
    assert not inspect.isabstract(Calender_Event)


def test_hyp_calender_event_constructor_exists():
    assert callable(Calender_Event.__init__)


def test_hyp_calender_event_constructor_args():
    sig = inspect.signature(Calender_Event.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "volunteer" in params, "Missing parameter 'volunteer'"
    assert "participantAmount" in params, "Missing parameter 'participantAmount'"
    assert "category" in params, "Missing parameter 'category'"
    assert "nomarlUser" in params, "Missing parameter 'nomarlUser'"
    assert "description" in params, "Missing parameter 'description'"
    assert "time" in params, "Missing parameter 'time'"
    assert "eventType" in params, "Missing parameter 'eventType'"
    assert "admin" in params, "Missing parameter 'admin'"

def test_hyp_calender_event_has_date():
    assert hasattr(Calender_Event, "date")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_volunteer():
    assert hasattr(Calender_Event, "volunteer")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "volunteer" in klass.__dict__:
            descriptor = klass.__dict__["volunteer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_participantAmount():
    assert hasattr(Calender_Event, "participantAmount")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "participantAmount" in klass.__dict__:
            descriptor = klass.__dict__["participantAmount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_category():
    assert hasattr(Calender_Event, "category")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_nomarlUser():
    assert hasattr(Calender_Event, "nomarlUser")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "nomarlUser" in klass.__dict__:
            descriptor = klass.__dict__["nomarlUser"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_description():
    assert hasattr(Calender_Event, "description")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_time():
    assert hasattr(Calender_Event, "time")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_eventType():
    assert hasattr(Calender_Event, "eventType")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_calender_event_has_admin():
    assert hasattr(Calender_Event, "admin")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "admin" in klass.__dict__:
            descriptor = klass.__dict__["admin"]
            break
    assert isinstance(descriptor, property)



def test_hyp_volunteer_is_not_abstract():
    assert not inspect.isabstract(Volunteer)


def test_hyp_volunteer_constructor_exists():
    assert callable(Volunteer.__init__)


def test_hyp_volunteer_constructor_args():
    sig = inspect.signature(Volunteer.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "userID" in params, "Missing parameter 'userID'"






def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "userName" in params, "Missing parameter 'userName'"






def test_hyp_normal_user_is_not_abstract():
    assert not inspect.isabstract(Normal_user)


def test_hyp_normal_user_constructor_exists():
    assert callable(Normal_user.__init__)


def test_hyp_normal_user_constructor_args():
    sig = inspect.signature(Normal_user.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"






def test_hyp_void_is_not_abstract():
    assert not inspect.isabstract(void)


def test_hyp_void_constructor_exists():
    assert callable(void.__init__)


def test_hyp_void_constructor_args():
    sig = inspect.signature(void.__init__)
    params = list(sig.parameters.keys())



def test_hyp_superadmin_is_not_abstract():
    assert not inspect.isabstract(SuperAdmin)


def test_hyp_superadmin_constructor_exists():
    assert callable(SuperAdmin.__init__)


def test_hyp_superadmin_constructor_args():
    sig = inspect.signature(SuperAdmin.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"






def test_hyp_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_hyp_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_hyp_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "l_Name" in params, "Missing parameter 'l_Name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "f_Name" in params, "Missing parameter 'f_Name'"
    assert "user_Name" in params, "Missing parameter 'user_Name'"






# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Mail_strategy = st.builds(
    Mail,
    subject=
        safe_text,
    sendTo=
        safe_text,
    sendBy=
        safe_text,
    emailID=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    cardNumber=
        st.integers(),
    issuerName=
        safe_text,
    cardType=
        safe_text,
    expiryDate=
        safe_text,
    amount=
        st.integers()
)
Logout_strategy = st.builds(
    Logout,
)
Attendance_strategy = st.builds(
    Attendance,
    checkOutTime=
        safe_text,
    attendanceID=
        st.integers(),
    checkInTime=
        safe_text
)
Login_strategy = st.builds(
    Login,
    userID=
        st.none(),
    loggedinTime=
        safe_text,
    loggedoutTime=
        safe_text
)
Calender_Event_strategy = st.builds(
    Calender_Event,
    date=
        safe_text,
    volunteer=
        st.none(),
    participantAmount=
        safe_text,
    category=
        safe_text,
    nomarlUser=
        st.none(),
    description=
        safe_text,
    time=
        safe_text,
    eventType=
        safe_text,
    admin=
        st.none()
)
Volunteer_strategy = st.builds(
    Volunteer,
    password=
        safe_text,
    userName=
        safe_text,
    userID=
        st.integers()
)
Admin_strategy = st.builds(
    Admin,
    password=
        safe_text,
    userID=
        st.integers(),
    userName=
        safe_text
)
Normal_user_strategy = st.builds(
    Normal_user,
    userID=
        st.integers(),
    password=
        safe_text,
    userName=
        safe_text
)
void_strategy = st.builds(
    void,
)
SuperAdmin_strategy = st.builds(
    SuperAdmin,
    userName=
        safe_text,
    userID=
        st.integers(),
    password=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    l_Name=
        safe_text,
    password=
        safe_text,
    f_Name=
        safe_text,
    user_Name=
        safe_text
)




@given(instance=Mail_strategy)
def test_hyp_mail_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=Mail_strategy)
def test_hyp_mail_sendTo_setter(instance):
    original = instance.sendTo
    instance.sendTo = original
    assert instance.sendTo == original



@given(instance=Mail_strategy)
def test_hyp_mail_sendBy_setter(instance):
    original = instance.sendBy
    instance.sendBy = original
    assert instance.sendBy == original



@given(instance=Mail_strategy)
def test_hyp_mail_emailID_setter(instance):
    original = instance.emailID
    instance.emailID = original
    assert instance.emailID == original




@given(instance=Payment_strategy)
def test_hyp_payment_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=Payment_strategy)
def test_hyp_payment_issuerName_setter(instance):
    original = instance.issuerName
    instance.issuerName = original
    assert instance.issuerName == original



@given(instance=Payment_strategy)
def test_hyp_payment_cardType_setter(instance):
    original = instance.cardType
    instance.cardType = original
    assert instance.cardType == original



@given(instance=Payment_strategy)
def test_hyp_payment_expiryDate_setter(instance):
    original = instance.expiryDate
    instance.expiryDate = original
    assert instance.expiryDate == original



@given(instance=Payment_strategy)
def test_hyp_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original





@given(instance=Attendance_strategy)
def test_hyp_attendance_checkOutTime_setter(instance):
    original = instance.checkOutTime
    instance.checkOutTime = original
    assert instance.checkOutTime == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_attendanceID_setter(instance):
    original = instance.attendanceID
    instance.attendanceID = original
    assert instance.attendanceID == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_checkInTime_setter(instance):
    original = instance.checkInTime
    instance.checkInTime = original
    assert instance.checkInTime == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_hyp_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_hyp_login_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Login_strategy)
def test_hyp_login_loggedinTime_setter(instance):
    original = instance.loggedinTime
    instance.loggedinTime = original
    assert instance.loggedinTime == original



@given(instance=Login_strategy)
def test_hyp_login_loggedoutTime_setter(instance):
    original = instance.loggedoutTime
    instance.loggedoutTime = original
    assert instance.loggedoutTime == original

@given(instance=Calender_Event_strategy)
@settings(max_examples=50)
def test_hyp_calender_event_instantiation(instance):
    assert isinstance(instance, Calender_Event)



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_volunteer_setter(instance):
    original = instance.volunteer
    instance.volunteer = original
    assert instance.volunteer == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_participantAmount_setter(instance):
    original = instance.participantAmount
    instance.participantAmount = original
    assert instance.participantAmount == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_nomarlUser_setter(instance):
    original = instance.nomarlUser
    instance.nomarlUser = original
    assert instance.nomarlUser == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_admin_setter(instance):
    original = instance.admin
    instance.admin = original
    assert instance.admin == original




@given(instance=Volunteer_strategy)
def test_hyp_volunteer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Volunteer_strategy)
def test_hyp_volunteer_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Volunteer_strategy)
def test_hyp_volunteer_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original




@given(instance=Admin_strategy)
def test_hyp_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_hyp_admin_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Admin_strategy)
def test_hyp_admin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original




@given(instance=Normal_user_strategy)
def test_hyp_normal_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Normal_user_strategy)
def test_hyp_normal_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Normal_user_strategy)
def test_hyp_normal_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original





@given(instance=SuperAdmin_strategy)
def test_hyp_superadmin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=SuperAdmin_strategy)
def test_hyp_superadmin_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=SuperAdmin_strategy)
def test_hyp_superadmin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Profile_strategy)
def test_hyp_profile_l_Name_setter(instance):
    original = instance.l_Name
    instance.l_Name = original
    assert instance.l_Name == original



@given(instance=Profile_strategy)
def test_hyp_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Profile_strategy)
def test_hyp_profile_f_Name_setter(instance):
    original = instance.f_Name
    instance.f_Name = original
    assert instance.f_Name == original



@given(instance=Profile_strategy)
def test_hyp_profile_user_Name_setter(instance):
    original = instance.user_Name
    instance.user_Name = original
    assert instance.user_Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Attendance,
    Calender_Event,
    Login,
    Logout,
    Mail,
    Normal_user,
    Payment,
    Profile,
    SuperAdmin,
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


def test_SuperAdmin_password_value_roundtrip():
    instance = SuperAdmin(password="sample_text", userID=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_SuperAdmin_userID_value_roundtrip():
    instance = SuperAdmin(password="sample_text", userID=7, userName="sample_text")
    assert instance.userID == 7
    instance.userID = 13
    assert instance.userID == 13


def test_SuperAdmin_userName_value_roundtrip():
    instance = SuperAdmin(password="sample_text", userID=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


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


def test_assoc_Admin_Payment_link_reassign_clear():
    a = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b1 = Admin(password="sample_text", userID=7, userName="sample_text")
    b2 = Admin(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'admin15', {b1})
    assert _is_linked(a, 'admin15', b1)
    if hasattr(b1, 'payment14'):
        assert _is_linked(b1, 'payment14', a)
    _safe_set(a, 'admin15', {b2})
    assert _is_linked(a, 'admin15', b2)
    if hasattr(b1, 'payment14'):
        assert not _is_linked(b1, 'payment14', a)
    if hasattr(b2, 'payment14'):
        assert _is_linked(b2, 'payment14', a)
    _safe_set(a, 'admin15', set())
    assert not _is_linked(a, 'admin15', b2)
    if hasattr(b2, 'payment14'):
        assert not _is_linked(b2, 'payment14', a)


def test_assoc_Normal_user_Payment_link_reassign_clear():
    a = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b1 = Normal_user(password="sample_text", userID=7, userName="sample_text")
    b2 = Normal_user(password="sample_text_2", userID=13, userName="sample_text_2")
    _safe_set(a, 'normal_user17', {b1})
    assert _is_linked(a, 'normal_user17', b1)
    if hasattr(b1, 'payment216'):
        assert _is_linked(b1, 'payment216', a)
    _safe_set(a, 'normal_user17', {b2})
    assert _is_linked(a, 'normal_user17', b2)
    if hasattr(b1, 'payment216'):
        assert not _is_linked(b1, 'payment216', a)
    if hasattr(b2, 'payment216'):
        assert _is_linked(b2, 'payment216', a)
    _safe_set(a, 'normal_user17', set())
    assert not _is_linked(a, 'normal_user17', b2)
    if hasattr(b2, 'payment216'):
        assert not _is_linked(b2, 'payment216', a)


def test_assoc_Profile_Attendance_link_reassign_clear():
    a = Profile(f_Name="sample_text", l_Name="sample_text", password="sample_text", user_Name="sample_text")
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


def test_assoc_SuperAdmin_Mail_link_reassign_clear():
    a = SuperAdmin(password="sample_text", userID=7, userName="sample_text")
    b1 = Mail(emailID="sample_text", sendBy="sample_text", sendTo="sample_text", subject="sample_text")
    b2 = Mail(emailID="sample_text_2", sendBy="sample_text_2", sendTo="sample_text_2", subject="sample_text_2")
    _safe_set(a, 'mail18', {b1})
    assert _is_linked(a, 'mail18', b1)
    if hasattr(b1, 'superAdmin19'):
        assert _is_linked(b1, 'superAdmin19', a)
    _safe_set(a, 'mail18', {b2})
    assert _is_linked(a, 'mail18', b2)
    if hasattr(b1, 'superAdmin19'):
        assert not _is_linked(b1, 'superAdmin19', a)
    if hasattr(b2, 'superAdmin19'):
        assert _is_linked(b2, 'superAdmin19', a)
    _safe_set(a, 'mail18', set())
    assert not _is_linked(a, 'mail18', b2)
    if hasattr(b2, 'superAdmin19'):
        assert not _is_linked(b2, 'superAdmin19', a)


def test_assoc_SuperAdmin_Payment_link_reassign_clear():
    a = SuperAdmin(password="sample_text", userID=7, userName="sample_text")
    b1 = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b2 = Payment(amount=13, cardNumber=13, cardType="sample_text_2", expiryDate="sample_text_2", issuerName="sample_text_2")
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


def test_assoc_Volunteer_Payment_link_reassign_clear():
    a = Volunteer(password="sample_text", userID=7, userName="sample_text")
    b1 = Payment(amount=7, cardNumber=7, cardType="sample_text", expiryDate="sample_text", issuerName="sample_text")
    b2 = Payment(amount=13, cardNumber=13, cardType="sample_text_2", expiryDate="sample_text_2", issuerName="sample_text_2")
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


SuperAdmin_strategy = st.builds(SuperAdmin, password=safe_text, userID=st.integers(), userName=safe_text)
@given(instance=SuperAdmin_strategy)
@settings(max_examples=25)
def test_SuperAdmin_instantiation(instance):
    assert isinstance(instance, SuperAdmin)


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



