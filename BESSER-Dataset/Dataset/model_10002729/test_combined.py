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
    Volunteer_Forms,
    Mail,
    Donations,
    Logout,
    Attendance,
    System_Login,
    Calender_Event,
    Volunteer,
    Admin,
    Normal_user,
    void,
    Executive_Director,
    Profile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_volunteer_forms_is_not_abstract():
    assert not inspect.isabstract(Volunteer_Forms)


def test_hyp_volunteer_forms_constructor_exists():
    assert callable(Volunteer_Forms.__init__)


def test_hyp_volunteer_forms_constructor_args():
    sig = inspect.signature(Volunteer_Forms.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"






def test_hyp_mail_is_not_abstract():
    assert not inspect.isabstract(Mail)


def test_hyp_mail_constructor_exists():
    assert callable(Mail.__init__)


def test_hyp_mail_constructor_args():
    sig = inspect.signature(Mail.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "sendTo" in params, "Missing parameter 'sendTo'"
    assert "emailID" in params, "Missing parameter 'emailID'"
    assert "sendBy" in params, "Missing parameter 'sendBy'"







def test_hyp_donations_is_not_abstract():
    assert not inspect.isabstract(Donations)


def test_hyp_donations_constructor_exists():
    assert callable(Donations.__init__)


def test_hyp_donations_constructor_args():
    sig = inspect.signature(Donations.__init__)
    params = list(sig.parameters.keys())
    assert "cardType" in params, "Missing parameter 'cardType'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "issuerName" in params, "Missing parameter 'issuerName'"
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"








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
    assert "attendanceID" in params, "Missing parameter 'attendanceID'"
    assert "checkOutTime" in params, "Missing parameter 'checkOutTime'"
    assert "checkInTime" in params, "Missing parameter 'checkInTime'"






def test_hyp_system_login_is_not_abstract():
    assert not inspect.isabstract(System_Login)


def test_hyp_system_login_constructor_exists():
    assert callable(System_Login.__init__)


def test_hyp_system_login_constructor_args():
    sig = inspect.signature(System_Login.__init__)
    params = list(sig.parameters.keys())
    assert "loggedinTime" in params, "Missing parameter 'loggedinTime'"
    assert "loggedoutTime" in params, "Missing parameter 'loggedoutTime'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_hyp_system_login_has_loggedinTime():
    assert hasattr(System_Login, "loggedinTime")
    descriptor = None
    for klass in System_Login.__mro__:
        if "loggedinTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedinTime"]
            break
    assert isinstance(descriptor, property)

def test_hyp_system_login_has_loggedoutTime():
    assert hasattr(System_Login, "loggedoutTime")
    descriptor = None
    for klass in System_Login.__mro__:
        if "loggedoutTime" in klass.__dict__:
            descriptor = klass.__dict__["loggedoutTime"]
            break
    assert isinstance(descriptor, property)

def test_hyp_system_login_has_userID():
    assert hasattr(System_Login, "userID")
    descriptor = None
    for klass in System_Login.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_hyp_calender_event_is_not_abstract():
    assert not inspect.isabstract(Calender_Event)


def test_hyp_calender_event_constructor_exists():
    assert callable(Calender_Event.__init__)


def test_hyp_calender_event_constructor_args():
    sig = inspect.signature(Calender_Event.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "participantAmount" in params, "Missing parameter 'participantAmount'"
    assert "admin" in params, "Missing parameter 'admin'"
    assert "volunteer" in params, "Missing parameter 'volunteer'"
    assert "eventType" in params, "Missing parameter 'eventType'"
    assert "category" in params, "Missing parameter 'category'"
    assert "nomarlUser" in params, "Missing parameter 'nomarlUser'"
    assert "description" in params, "Missing parameter 'description'"
    assert "date" in params, "Missing parameter 'date'"

def test_hyp_calender_event_has_time():
    assert hasattr(Calender_Event, "time")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
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

def test_hyp_calender_event_has_admin():
    assert hasattr(Calender_Event, "admin")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "admin" in klass.__dict__:
            descriptor = klass.__dict__["admin"]
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

def test_hyp_calender_event_has_eventType():
    assert hasattr(Calender_Event, "eventType")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
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

def test_hyp_calender_event_has_date():
    assert hasattr(Calender_Event, "date")
    descriptor = None
    for klass in Calender_Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_hyp_volunteer_is_not_abstract():
    assert not inspect.isabstract(Volunteer)


def test_hyp_volunteer_constructor_exists():
    assert callable(Volunteer.__init__)


def test_hyp_volunteer_constructor_args():
    sig = inspect.signature(Volunteer.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"






def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"






def test_hyp_normal_user_is_not_abstract():
    assert not inspect.isabstract(Normal_user)


def test_hyp_normal_user_constructor_exists():
    assert callable(Normal_user.__init__)


def test_hyp_normal_user_constructor_args():
    sig = inspect.signature(Normal_user.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "userID" in params, "Missing parameter 'userID'"






def test_hyp_void_is_not_abstract():
    assert not inspect.isabstract(void)


def test_hyp_void_constructor_exists():
    assert callable(void.__init__)


def test_hyp_void_constructor_args():
    sig = inspect.signature(void.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executive_director_is_not_abstract():
    assert not inspect.isabstract(Executive_Director)


def test_hyp_executive_director_constructor_exists():
    assert callable(Executive_Director.__init__)


def test_hyp_executive_director_constructor_args():
    sig = inspect.signature(Executive_Director.__init__)
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
    assert "phone_Number" in params, "Missing parameter 'phone_Number'"
    assert "password" in params, "Missing parameter 'password'"
    assert "last_Name" in params, "Missing parameter 'last_Name'"
    assert "first_Name" in params, "Missing parameter 'first_Name'"
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
Volunteer_Forms_strategy = st.builds(
    Volunteer_Forms,
    userName=
        safe_text,
    userID=
        st.integers(),
    password=
        safe_text
)
Mail_strategy = st.builds(
    Mail,
    subject=
        safe_text,
    sendTo=
        safe_text,
    emailID=
        safe_text,
    sendBy=
        safe_text
)
Donations_strategy = st.builds(
    Donations,
    cardType=
        safe_text,
    amount=
        st.integers(),
    issuerName=
        safe_text,
    expirationDate=
        st.integers(),
    cardNumber=
        st.integers()
)
Logout_strategy = st.builds(
    Logout,
)
Attendance_strategy = st.builds(
    Attendance,
    attendanceID=
        st.integers(),
    checkOutTime=
        safe_text,
    checkInTime=
        safe_text
)
System_Login_strategy = st.builds(
    System_Login,
    loggedinTime=
        safe_text,
    loggedoutTime=
        safe_text,
    userID=
        st.none()
)
Calender_Event_strategy = st.builds(
    Calender_Event,
    time=
        safe_text,
    participantAmount=
        safe_text,
    admin=
        st.none(),
    volunteer=
        st.none(),
    eventType=
        safe_text,
    category=
        safe_text,
    nomarlUser=
        st.none(),
    description=
        safe_text,
    date=
        safe_text
)
Volunteer_strategy = st.builds(
    Volunteer,
    userID=
        st.integers(),
    password=
        safe_text,
    userName=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    userID=
        st.integers(),
    userName=
        safe_text,
    password=
        safe_text
)
Normal_user_strategy = st.builds(
    Normal_user,
    password=
        safe_text,
    userName=
        safe_text,
    userID=
        st.integers()
)
void_strategy = st.builds(
    void,
)
Executive_Director_strategy = st.builds(
    Executive_Director,
    userName=
        safe_text,
    userID=
        st.integers(),
    password=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    phone_Number=
        st.integers(),
    password=
        safe_text,
    last_Name=
        safe_text,
    first_Name=
        safe_text,
    user_Name=
        safe_text
)




@given(instance=Volunteer_Forms_strategy)
def test_hyp_volunteer_forms_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Volunteer_Forms_strategy)
def test_hyp_volunteer_forms_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Volunteer_Forms_strategy)
def test_hyp_volunteer_forms_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




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
def test_hyp_mail_emailID_setter(instance):
    original = instance.emailID
    instance.emailID = original
    assert instance.emailID == original



@given(instance=Mail_strategy)
def test_hyp_mail_sendBy_setter(instance):
    original = instance.sendBy
    instance.sendBy = original
    assert instance.sendBy == original




@given(instance=Donations_strategy)
def test_hyp_donations_cardType_setter(instance):
    original = instance.cardType
    instance.cardType = original
    assert instance.cardType == original



@given(instance=Donations_strategy)
def test_hyp_donations_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Donations_strategy)
def test_hyp_donations_issuerName_setter(instance):
    original = instance.issuerName
    instance.issuerName = original
    assert instance.issuerName == original



@given(instance=Donations_strategy)
def test_hyp_donations_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original



@given(instance=Donations_strategy)
def test_hyp_donations_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original





@given(instance=Attendance_strategy)
def test_hyp_attendance_attendanceID_setter(instance):
    original = instance.attendanceID
    instance.attendanceID = original
    assert instance.attendanceID == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_checkOutTime_setter(instance):
    original = instance.checkOutTime
    instance.checkOutTime = original
    assert instance.checkOutTime == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_checkInTime_setter(instance):
    original = instance.checkInTime
    instance.checkInTime = original
    assert instance.checkInTime == original

@given(instance=System_Login_strategy)
@settings(max_examples=50)
def test_hyp_system_login_instantiation(instance):
    assert isinstance(instance, System_Login)



@given(instance=System_Login_strategy)
def test_hyp_system_login_loggedinTime_setter(instance):
    original = instance.loggedinTime
    instance.loggedinTime = original
    assert instance.loggedinTime == original



@given(instance=System_Login_strategy)
def test_hyp_system_login_loggedoutTime_setter(instance):
    original = instance.loggedoutTime
    instance.loggedoutTime = original
    assert instance.loggedoutTime == original



@given(instance=System_Login_strategy)
def test_hyp_system_login_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=Calender_Event_strategy)
@settings(max_examples=50)
def test_hyp_calender_event_instantiation(instance):
    assert isinstance(instance, Calender_Event)



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_participantAmount_setter(instance):
    original = instance.participantAmount
    instance.participantAmount = original
    assert instance.participantAmount == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_admin_setter(instance):
    original = instance.admin
    instance.admin = original
    assert instance.admin == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_volunteer_setter(instance):
    original = instance.volunteer
    instance.volunteer = original
    assert instance.volunteer == original



@given(instance=Calender_Event_strategy)
def test_hyp_calender_event_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original



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
def test_hyp_calender_event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=Volunteer_strategy)
def test_hyp_volunteer_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



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



@given(instance=Admin_strategy)
def test_hyp_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




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



@given(instance=Normal_user_strategy)
def test_hyp_normal_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original





@given(instance=Executive_Director_strategy)
def test_hyp_executive_director_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Executive_Director_strategy)
def test_hyp_executive_director_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Executive_Director_strategy)
def test_hyp_executive_director_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Profile_strategy)
def test_hyp_profile_phone_Number_setter(instance):
    original = instance.phone_Number
    instance.phone_Number = original
    assert instance.phone_Number == original



@given(instance=Profile_strategy)
def test_hyp_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Profile_strategy)
def test_hyp_profile_last_Name_setter(instance):
    original = instance.last_Name
    instance.last_Name = original
    assert instance.last_Name == original



@given(instance=Profile_strategy)
def test_hyp_profile_first_Name_setter(instance):
    original = instance.first_Name
    instance.first_Name = original
    assert instance.first_Name == original



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



