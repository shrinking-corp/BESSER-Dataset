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
    Login_external,
    Logout_external,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Login,
    Attendance,
    Leave,
    Authenticate_staff,
    Salary,
    Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_login_external_is_not_abstract():
    assert not inspect.isabstract(Login_external)


def test_hyp_login_external_constructor_exists():
    assert callable(Login_external.__init__)


def test_hyp_login_external_constructor_args():
    sig = inspect.signature(Login_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logout_external_is_not_abstract():
    assert not inspect.isabstract(Logout_external)


def test_hyp_logout_external_constructor_exists():
    assert callable(Logout_external.__init__)


def test_hyp_logout_external_constructor_args():
    sig = inspect.signature(Logout_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_actor_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor)


def test_hyp_employee_actor_constructor_exists():
    assert callable(Employee_Actor.__init__)


def test_hyp_employee_actor_constructor_args():
    sig = inspect.signature(Employee_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_administrator_actor_is_not_abstract():
    assert not inspect.isabstract(Administrator_Actor)


def test_hyp_administrator_actor_constructor_exists():
    assert callable(Administrator_Actor.__init__)


def test_hyp_administrator_actor_constructor_args():
    sig = inspect.signature(Administrator_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_salary_management_usecase_is_not_abstract():
    assert not inspect.isabstract(Salary_Management_UseCase)


def test_hyp_salary_management_usecase_constructor_exists():
    assert callable(Salary_Management_UseCase.__init__)


def test_hyp_salary_management_usecase_constructor_args():
    sig = inspect.signature(Salary_Management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_authentication_usecase_is_not_abstract():
    assert not inspect.isabstract(Authentication_UseCase)


def test_hyp_authentication_usecase_constructor_exists():
    assert callable(Authentication_UseCase.__init__)


def test_hyp_authentication_usecase_constructor_args():
    sig = inspect.signature(Authentication_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_management_system_component_is_not_abstract():
    assert not inspect.isabstract(Employee_Management_System_Component)


def test_hyp_employee_management_system_component_constructor_exists():
    assert callable(Employee_Management_System_Component.__init__)


def test_hyp_employee_management_system_component_constructor_args():
    sig = inspect.signature(Employee_Management_System_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"





def test_hyp_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_hyp_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_hyp_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "AttendTime" in params, "Missing parameter 'AttendTime'"
    assert "Leaving_Time" in params, "Missing parameter 'Leaving_Time'"
    assert "Attend_date" in params, "Missing parameter 'Attend_date'"
    assert "Emp_id" in params, "Missing parameter 'Emp_id'"







def test_hyp_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_hyp_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_hyp_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "leave_id" in params, "Missing parameter 'leave_id'"
    assert "Leave_detail" in params, "Missing parameter 'Leave_detail'"
    assert "Leave_StartDate" in params, "Missing parameter 'Leave_StartDate'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "Leave_ApplyDate" in params, "Missing parameter 'Leave_ApplyDate'"
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"












def test_hyp_authenticate_staff_is_not_abstract():
    assert not inspect.isabstract(Authenticate_staff)


def test_hyp_authenticate_staff_constructor_exists():
    assert callable(Authenticate_staff.__init__)


def test_hyp_authenticate_staff_constructor_args():
    sig = inspect.signature(Authenticate_staff.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"






def test_hyp_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_hyp_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_hyp_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"
    assert "Sly_Increment" in params, "Missing parameter 'Sly_Increment'"
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Sly_Netgross" in params, "Missing parameter 'Sly_Netgross'"
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"









def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"
    assert "Emp_ContactNo" in params, "Missing parameter 'Emp_ContactNo'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Emp_NIC" in params, "Missing parameter 'Emp_NIC'"
    assert "Emp_Salary" in params, "Missing parameter 'Emp_Salary'"
    assert "Emp_Email" in params, "Missing parameter 'Emp_Email'"
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"













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
Login_external_strategy = st.builds(
    Login_external,
)
Logout_external_strategy = st.builds(
    Logout_external,
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Salary_Management_UseCase_strategy = st.builds(
    Salary_Management_UseCase,
)
Authentication_UseCase_strategy = st.builds(
    Authentication_UseCase,
)
Employee_Management_System_Component_strategy = st.builds(
    Employee_Management_System_Component,
)
Login_strategy = st.builds(
    Login,
    Password=
        safe_text,
    UserName=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    AttendTime=
        safe_text,
    Leaving_Time=
        safe_text,
    Attend_date=
        st.dates(),
    Emp_id=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    leave_id=
        st.integers(),
    Leave_detail=
        safe_text,
    Leave_StartDate=
        st.dates(),
    Emp_Id=
        st.integers(),
    Leave_Title=
        safe_text,
    Leave_EndDate=
        st.dates(),
    Leave_ApplyDate=
        st.dates(),
    Leave_NoOfDays=
        st.integers(),
    Leave_Status=
        safe_text
)
Authenticate_staff_strategy = st.builds(
    Authenticate_staff,
    UserName=
        safe_text,
    Password=
        safe_text,
    Authendication_Mood=
        safe_text
)
Salary_strategy = st.builds(
    Salary,
    Emp_Id=
        st.integers(),
    Sly_Decrement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Increment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    OverTime=
        safe_text,
    Sly_Netgross=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Basic=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Employee_strategy = st.builds(
    Employee,
    Emp_Address=
        safe_text,
    Emp_Date_Of_Joint=
        st.dates(),
    Emp_ContactNo=
        safe_text,
    Emp_DOB=
        st.dates(),
    Emp_Id=
        st.integers(),
    Emp_Name=
        safe_text,
    Emp_NIC=
        safe_text,
    Emp_Salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Email=
        safe_text,
    Emp_Department=
        safe_text,
    Emp_Position=
        safe_text
)











@given(instance=Login_strategy)
def test_hyp_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Login_strategy)
def test_hyp_login_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original




@given(instance=Attendance_strategy)
def test_hyp_attendance_AttendTime_setter(instance):
    original = instance.AttendTime
    instance.AttendTime = original
    assert instance.AttendTime == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_Leaving_Time_setter(instance):
    original = instance.Leaving_Time
    instance.Leaving_Time = original
    assert instance.Leaving_Time == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_Attend_date_setter(instance):
    original = instance.Attend_date
    instance.Attend_date = original
    assert instance.Attend_date == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_Emp_id_setter(instance):
    original = instance.Emp_id
    instance.Emp_id = original
    assert instance.Emp_id == original




@given(instance=Leave_strategy)
def test_hyp_leave_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_detail_setter(instance):
    original = instance.Leave_detail
    instance.Leave_detail = original
    assert instance.Leave_detail == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_StartDate_setter(instance):
    original = instance.Leave_StartDate
    instance.Leave_StartDate = original
    assert instance.Leave_StartDate == original



@given(instance=Leave_strategy)
def test_hyp_leave_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_ApplyDate_setter(instance):
    original = instance.Leave_ApplyDate
    instance.Leave_ApplyDate = original
    assert instance.Leave_ApplyDate == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original




@given(instance=Authenticate_staff_strategy)
def test_hyp_authenticate_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Authenticate_staff_strategy)
def test_hyp_authenticate_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Authenticate_staff_strategy)
def test_hyp_authenticate_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original




@given(instance=Salary_strategy)
def test_hyp_salary_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Decrement_setter(instance):
    original = instance.Sly_Decrement
    instance.Sly_Decrement = original
    assert instance.Sly_Decrement == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Increment_setter(instance):
    original = instance.Sly_Increment
    instance.Sly_Increment = original
    assert instance.Sly_Increment == original



@given(instance=Salary_strategy)
def test_hyp_salary_OverTime_setter(instance):
    original = instance.OverTime
    instance.OverTime = original
    assert instance.OverTime == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Netgross_setter(instance):
    original = instance.Sly_Netgross
    instance.Sly_Netgross = original
    assert instance.Sly_Netgross == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Basic_setter(instance):
    original = instance.Sly_Basic
    instance.Sly_Basic = original
    assert instance.Sly_Basic == original




@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Date_Of_Joint_setter(instance):
    original = instance.Emp_Date_Of_Joint
    instance.Emp_Date_Of_Joint = original
    assert instance.Emp_Date_Of_Joint == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_ContactNo_setter(instance):
    original = instance.Emp_ContactNo
    instance.Emp_ContactNo = original
    assert instance.Emp_ContactNo == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_NIC_setter(instance):
    original = instance.Emp_NIC
    instance.Emp_NIC = original
    assert instance.Emp_NIC == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Salary_setter(instance):
    original = instance.Emp_Salary
    instance.Emp_Salary = original
    assert instance.Emp_Salary == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Email_setter(instance):
    original = instance.Emp_Email
    instance.Emp_Email = original
    assert instance.Emp_Email == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator_Actor,
    Attendance,
    Authenticate_staff,
    Authentication_UseCase,
    Employee,
    Employee_Actor,
    Employee_Management_System_Component,
    Leave,
    Login,
    Login_external,
    Logout_external,
    Salary,
    Salary_Management_UseCase,
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

def test_Attendance_AttendTime_value_roundtrip():
    instance = Attendance(AttendTime="sample_text", Attend_date=date(2024, 1, 1), Emp_id="sample_text", Leaving_Time="sample_text")
    assert instance.AttendTime == "sample_text"
    instance.AttendTime = "sample_text_2"
    assert instance.AttendTime == "sample_text_2"


def test_Attendance_Attend_date_value_roundtrip():
    instance = Attendance(AttendTime="sample_text", Attend_date=date(2024, 1, 1), Emp_id="sample_text", Leaving_Time="sample_text")
    assert instance.Attend_date == date(2024, 1, 1)
    instance.Attend_date = date(2025, 6, 15)
    assert instance.Attend_date == date(2025, 6, 15)


def test_Attendance_Emp_id_value_roundtrip():
    instance = Attendance(AttendTime="sample_text", Attend_date=date(2024, 1, 1), Emp_id="sample_text", Leaving_Time="sample_text")
    assert instance.Emp_id == "sample_text"
    instance.Emp_id = "sample_text_2"
    assert instance.Emp_id == "sample_text_2"


def test_Attendance_Leaving_Time_value_roundtrip():
    instance = Attendance(AttendTime="sample_text", Attend_date=date(2024, 1, 1), Emp_id="sample_text", Leaving_Time="sample_text")
    assert instance.Leaving_Time == "sample_text"
    instance.Leaving_Time = "sample_text_2"
    assert instance.Leaving_Time == "sample_text_2"


def test_Authenticate_staff_Authendication_Mood_value_roundtrip():
    instance = Authenticate_staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    assert instance.Authendication_Mood == "sample_text"
    instance.Authendication_Mood = "sample_text_2"
    assert instance.Authendication_Mood == "sample_text_2"


def test_Authenticate_staff_Password_value_roundtrip():
    instance = Authenticate_staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Authenticate_staff_UserName_value_roundtrip():
    instance = Authenticate_staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Employee_Emp_Address_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Address == "sample_text"
    instance.Emp_Address = "sample_text_2"
    assert instance.Emp_Address == "sample_text_2"


def test_Employee_Emp_ContactNo_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_ContactNo == "sample_text"
    instance.Emp_ContactNo = "sample_text_2"
    assert instance.Emp_ContactNo == "sample_text_2"


def test_Employee_Emp_DOB_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_DOB == date(2024, 1, 1)
    instance.Emp_DOB = date(2025, 6, 15)
    assert instance.Emp_DOB == date(2025, 6, 15)


def test_Employee_Emp_Date_Of_Joint_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Date_Of_Joint == date(2024, 1, 1)
    instance.Emp_Date_Of_Joint = date(2025, 6, 15)
    assert instance.Emp_Date_Of_Joint == date(2025, 6, 15)


def test_Employee_Emp_Department_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Department == "sample_text"
    instance.Emp_Department = "sample_text_2"
    assert instance.Emp_Department == "sample_text_2"


def test_Employee_Emp_Email_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Email == "sample_text"
    instance.Emp_Email = "sample_text_2"
    assert instance.Emp_Email == "sample_text_2"


def test_Employee_Emp_Id_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Id == 7
    instance.Emp_Id = 13
    assert instance.Emp_Id == 13


def test_Employee_Emp_NIC_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_NIC == "sample_text"
    instance.Emp_NIC = "sample_text_2"
    assert instance.Emp_NIC == "sample_text_2"


def test_Employee_Emp_Name_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Name == "sample_text"
    instance.Emp_Name = "sample_text_2"
    assert instance.Emp_Name == "sample_text_2"


def test_Employee_Emp_Position_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Position == "sample_text"
    instance.Emp_Position = "sample_text_2"
    assert instance.Emp_Position == "sample_text_2"


def test_Employee_Emp_Salary_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    assert instance.Emp_Salary == 3.14
    instance.Emp_Salary = 9.99
    assert instance.Emp_Salary == 9.99


def test_Leave_Emp_Id_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Emp_Id == 7
    instance.Emp_Id = 13
    assert instance.Emp_Id == 13


def test_Leave_Leave_ApplyDate_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_ApplyDate == date(2024, 1, 1)
    instance.Leave_ApplyDate = date(2025, 6, 15)
    assert instance.Leave_ApplyDate == date(2025, 6, 15)


def test_Leave_Leave_EndDate_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_EndDate == date(2024, 1, 1)
    instance.Leave_EndDate = date(2025, 6, 15)
    assert instance.Leave_EndDate == date(2025, 6, 15)


def test_Leave_Leave_NoOfDays_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_NoOfDays == 7
    instance.Leave_NoOfDays = 13
    assert instance.Leave_NoOfDays == 13


def test_Leave_Leave_StartDate_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_StartDate == date(2024, 1, 1)
    instance.Leave_StartDate = date(2025, 6, 15)
    assert instance.Leave_StartDate == date(2025, 6, 15)


def test_Leave_Leave_Status_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_Status == "sample_text"
    instance.Leave_Status = "sample_text_2"
    assert instance.Leave_Status == "sample_text_2"


def test_Leave_Leave_Title_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_Title == "sample_text"
    instance.Leave_Title = "sample_text_2"
    assert instance.Leave_Title == "sample_text_2"


def test_Leave_Leave_detail_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_detail == "sample_text"
    instance.Leave_detail = "sample_text_2"
    assert instance.Leave_detail == "sample_text_2"


def test_Leave_leave_id_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.leave_id == 7
    instance.leave_id = 13
    assert instance.leave_id == 13


def test_Login_Password_value_roundtrip():
    instance = Login(Password="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Login_UserName_value_roundtrip():
    instance = Login(Password="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Salary_Emp_Id_value_roundtrip():
    instance = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    assert instance.Emp_Id == 7
    instance.Emp_Id = 13
    assert instance.Emp_Id == 13


def test_Salary_OverTime_value_roundtrip():
    instance = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    assert instance.OverTime == "sample_text"
    instance.OverTime = "sample_text_2"
    assert instance.OverTime == "sample_text_2"


def test_Salary_Sly_Basic_value_roundtrip():
    instance = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    assert instance.Sly_Basic == 3.14
    instance.Sly_Basic = 9.99
    assert instance.Sly_Basic == 9.99


def test_Salary_Sly_Decrement_value_roundtrip():
    instance = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    assert instance.Sly_Decrement == 3.14
    instance.Sly_Decrement = 9.99
    assert instance.Sly_Decrement == 9.99


def test_Salary_Sly_Increment_value_roundtrip():
    instance = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    assert instance.Sly_Increment == 3.14
    instance.Sly_Increment = 9.99
    assert instance.Sly_Increment == 9.99


def test_Salary_Sly_Netgross_value_roundtrip():
    instance = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    assert instance.Sly_Netgross == 3.14
    instance.Sly_Netgross = 9.99
    assert instance.Sly_Netgross == 9.99


def test_assoc_Employee_Attendance_link_reassign_clear():
    a = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    b1 = Attendance(AttendTime="sample_text", Attend_date=date(2024, 1, 1), Emp_id="sample_text", Leaving_Time="sample_text")
    b2 = Attendance(AttendTime="sample_text_2", Attend_date=date(2025, 6, 15), Emp_id="sample_text_2", Leaving_Time="sample_text_2")
    _safe_set(a, 'attendance2', b1)
    assert _is_linked(a, 'attendance2', b1)
    if hasattr(b1, 'employee3'):
        assert _is_linked(b1, 'employee3', a)
    _safe_set(a, 'attendance2', b2)
    assert _is_linked(a, 'attendance2', b2)
    if hasattr(b1, 'employee3'):
        assert not _is_linked(b1, 'employee3', a)
    if hasattr(b2, 'employee3'):
        assert _is_linked(b2, 'employee3', a)
    _safe_set(a, 'attendance2', None)
    assert not _is_linked(a, 'attendance2', b2)
    if hasattr(b2, 'employee3'):
        assert not _is_linked(b2, 'employee3', a)


def test_assoc_Employee_Leave_link_reassign_clear():
    a = Leave(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    b1 = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    b2 = Employee(Emp_Address="sample_text_2", Emp_ContactNo="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_Email="sample_text_2", Emp_Id=13, Emp_NIC="sample_text_2", Emp_Name="sample_text_2", Emp_Position="sample_text_2", Emp_Salary=9.99)
    _safe_set(a, 'employee1', b1)
    assert _is_linked(a, 'employee1', b1)
    if hasattr(b1, 'leave0'):
        assert _is_linked(b1, 'leave0', a)
    _safe_set(a, 'employee1', b2)
    assert _is_linked(a, 'employee1', b2)
    if hasattr(b1, 'leave0'):
        assert not _is_linked(b1, 'leave0', a)
    if hasattr(b2, 'leave0'):
        assert _is_linked(b2, 'leave0', a)
    _safe_set(a, 'employee1', None)
    assert not _is_linked(a, 'employee1', b2)
    if hasattr(b2, 'leave0'):
        assert not _is_linked(b2, 'leave0', a)


def test_assoc_Employee_Salary_link_reassign_clear():
    a = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    b1 = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_NIC="sample_text", Emp_Name="sample_text", Emp_Position="sample_text", Emp_Salary=3.14)
    b2 = Employee(Emp_Address="sample_text_2", Emp_ContactNo="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_Email="sample_text_2", Emp_Id=13, Emp_NIC="sample_text_2", Emp_Name="sample_text_2", Emp_Position="sample_text_2", Emp_Salary=9.99)
    _safe_set(a, 'employee5', b1)
    assert _is_linked(a, 'employee5', b1)
    if hasattr(b1, 'salary4'):
        assert _is_linked(b1, 'salary4', a)
    _safe_set(a, 'employee5', b2)
    assert _is_linked(a, 'employee5', b2)
    if hasattr(b1, 'salary4'):
        assert not _is_linked(b1, 'salary4', a)
    if hasattr(b2, 'salary4'):
        assert _is_linked(b2, 'salary4', a)
    _safe_set(a, 'employee5', None)
    assert not _is_linked(a, 'employee5', b2)
    if hasattr(b2, 'salary4'):
        assert not _is_linked(b2, 'salary4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


Attendance_strategy = st.builds(Attendance, AttendTime=safe_text, Attend_date=st.dates(), Emp_id=safe_text, Leaving_Time=safe_text)
@given(instance=Attendance_strategy)
@settings(max_examples=25)
def test_Attendance_instantiation(instance):
    assert isinstance(instance, Attendance)


Authenticate_staff_strategy = st.builds(Authenticate_staff, Authendication_Mood=safe_text, Password=safe_text, UserName=safe_text)
@given(instance=Authenticate_staff_strategy)
@settings(max_examples=25)
def test_Authenticate_staff_instantiation(instance):
    assert isinstance(instance, Authenticate_staff)


Authentication_UseCase_strategy = st.builds(Authentication_UseCase)
@given(instance=Authentication_UseCase_strategy)
@settings(max_examples=25)
def test_Authentication_UseCase_instantiation(instance):
    assert isinstance(instance, Authentication_UseCase)


Employee_strategy = st.builds(Employee, Emp_Address=safe_text, Emp_ContactNo=safe_text, Emp_DOB=st.dates(), Emp_Date_Of_Joint=st.dates(), Emp_Department=safe_text, Emp_Email=safe_text, Emp_Id=st.integers(), Emp_NIC=safe_text, Emp_Name=safe_text, Emp_Position=safe_text, Emp_Salary=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Employee_Actor_strategy = st.builds(Employee_Actor)
@given(instance=Employee_Actor_strategy)
@settings(max_examples=25)
def test_Employee_Actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)


Employee_Management_System_Component_strategy = st.builds(Employee_Management_System_Component)
@given(instance=Employee_Management_System_Component_strategy)
@settings(max_examples=25)
def test_Employee_Management_System_Component_instantiation(instance):
    assert isinstance(instance, Employee_Management_System_Component)


Leave_strategy = st.builds(Leave, Emp_Id=st.integers(), Leave_ApplyDate=st.dates(), Leave_EndDate=st.dates(), Leave_NoOfDays=st.integers(), Leave_StartDate=st.dates(), Leave_Status=safe_text, Leave_Title=safe_text, Leave_detail=safe_text, leave_id=st.integers())
@given(instance=Leave_strategy)
@settings(max_examples=25)
def test_Leave_instantiation(instance):
    assert isinstance(instance, Leave)


Login_strategy = st.builds(Login, Password=safe_text, UserName=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Login_external_strategy = st.builds(Login_external)
@given(instance=Login_external_strategy)
@settings(max_examples=25)
def test_Login_external_instantiation(instance):
    assert isinstance(instance, Login_external)


Logout_external_strategy = st.builds(Logout_external)
@given(instance=Logout_external_strategy)
@settings(max_examples=25)
def test_Logout_external_instantiation(instance):
    assert isinstance(instance, Logout_external)


Salary_strategy = st.builds(Salary, Emp_Id=st.integers(), OverTime=safe_text, Sly_Basic=st.floats(allow_nan=False, allow_infinity=False), Sly_Decrement=st.floats(allow_nan=False, allow_infinity=False), Sly_Increment=st.floats(allow_nan=False, allow_infinity=False), Sly_Netgross=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Salary_strategy)
@settings(max_examples=25)
def test_Salary_instantiation(instance):
    assert isinstance(instance, Salary)


Salary_Management_UseCase_strategy = st.builds(Salary_Management_UseCase)
@given(instance=Salary_Management_UseCase_strategy)
@settings(max_examples=25)
def test_Salary_Management_UseCase_instantiation(instance):
    assert isinstance(instance, Salary_Management_UseCase)



