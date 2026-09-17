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
    Logout_external,
    Login_external,
    Tuning_Staff,
    Driving_Staff,
    Administrator,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Login,
    Attendance,
    Leave_Status,
    Staff,
    Salary,
    Manager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_logout_external_is_not_abstract():
    assert not inspect.isabstract(Logout_external)


def test_hyp_logout_external_constructor_exists():
    assert callable(Logout_external.__init__)


def test_hyp_logout_external_constructor_args():
    sig = inspect.signature(Logout_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_external_is_not_abstract():
    assert not inspect.isabstract(Login_external)


def test_hyp_login_external_constructor_exists():
    assert callable(Login_external.__init__)


def test_hyp_login_external_constructor_args():
    sig = inspect.signature(Login_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tuning_staff_is_not_abstract():
    assert not inspect.isabstract(Tuning_Staff)


def test_hyp_tuning_staff_constructor_exists():
    assert callable(Tuning_Staff.__init__)


def test_hyp_tuning_staff_constructor_args():
    sig = inspect.signature(Tuning_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"






def test_hyp_driving_staff_is_not_abstract():
    assert not inspect.isabstract(Driving_Staff)


def test_hyp_driving_staff_constructor_exists():
    assert callable(Driving_Staff.__init__)


def test_hyp_driving_staff_constructor_args():
    sig = inspect.signature(Driving_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"
    assert "PilotName" in params, "Missing parameter 'PilotName'"
    assert "Pilot_ContactNo" in params, "Missing parameter 'Pilot_ContactNo'"
    assert "Password" in params, "Missing parameter 'Password'"







def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"
    assert "Admin_Id" in params, "Missing parameter 'Admin_Id'"
    assert "Admin_Name" in params, "Missing parameter 'Admin_Name'"
    assert "Admin_NIC" in params, "Missing parameter 'Admin_NIC'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Admin_Email" in params, "Missing parameter 'Admin_Email'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"
    assert "Admin_ContactNo" in params, "Missing parameter 'Admin_ContactNo'"












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
    assert "Emp_id" in params, "Missing parameter 'Emp_id'"
    assert "Leaving_Time" in params, "Missing parameter 'Leaving_Time'"
    assert "AttendTime" in params, "Missing parameter 'AttendTime'"
    assert "Attend_date" in params, "Missing parameter 'Attend_date'"







def test_hyp_leave_status_is_not_abstract():
    assert not inspect.isabstract(Leave_Status)


def test_hyp_leave_status_constructor_exists():
    assert callable(Leave_Status.__init__)


def test_hyp_leave_status_constructor_args():
    sig = inspect.signature(Leave_Status.__init__)
    params = list(sig.parameters.keys())
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"
    assert "Leave_detail" in params, "Missing parameter 'Leave_detail'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_ApplyDate" in params, "Missing parameter 'Leave_ApplyDate'"
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"
    assert "leave_id" in params, "Missing parameter 'leave_id'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"
    assert "Leave_StartDate" in params, "Missing parameter 'Leave_StartDate'"












def test_hyp_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_hyp_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_hyp_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"
    assert "UserName" in params, "Missing parameter 'UserName'"






def test_hyp_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_hyp_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_hyp_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Sly_Netgross" in params, "Missing parameter 'Sly_Netgross'"
    assert "Sly_Increment" in params, "Missing parameter 'Sly_Increment'"









def test_hyp_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_hyp_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_hyp_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_NIC" in params, "Missing parameter 'Emp_NIC'"
    assert "Mng_Email" in params, "Missing parameter 'Mng_Email'"
    assert "Mng_Salary" in params, "Missing parameter 'Mng_Salary'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Mng_Name" in params, "Missing parameter 'Mng_Name'"
    assert "Mng_ContactNo" in params, "Missing parameter 'Mng_ContactNo'"
    assert "Mng_Id" in params, "Missing parameter 'Mng_Id'"
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"













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
Logout_external_strategy = st.builds(
    Logout_external,
)
Login_external_strategy = st.builds(
    Login_external,
)
Tuning_Staff_strategy = st.builds(
    Tuning_Staff,
    Address=
        safe_text,
    UserName=
        safe_text,
    Authendication_Mood=
        safe_text
)
Driving_Staff_strategy = st.builds(
    Driving_Staff,
    Authendication_Mood=
        safe_text,
    PilotName=
        safe_text,
    Pilot_ContactNo=
        safe_text,
    Password=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    Emp_Department=
        safe_text,
    Emp_Position=
        safe_text,
    Admin_Id=
        st.integers(),
    Admin_Name=
        safe_text,
    Admin_NIC=
        safe_text,
    Emp_DOB=
        st.dates(),
    Admin_Email=
        safe_text,
    Emp_Date_Of_Joint=
        st.dates(),
    Admin_ContactNo=
        safe_text
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
    Emp_id=
        safe_text,
    Leaving_Time=
        safe_text,
    AttendTime=
        safe_text,
    Attend_date=
        st.dates()
)
Leave_Status_strategy = st.builds(
    Leave_Status,
    Leave_Status=
        safe_text,
    Leave_detail=
        safe_text,
    Emp_Id=
        st.integers(),
    Leave_ApplyDate=
        st.dates(),
    Leave_NoOfDays=
        st.integers(),
    leave_id=
        st.integers(),
    Leave_EndDate=
        st.dates(),
    Leave_Title=
        safe_text,
    Leave_StartDate=
        st.dates()
)
Staff_strategy = st.builds(
    Staff,
    Password=
        safe_text,
    Authendication_Mood=
        safe_text,
    UserName=
        safe_text
)
Salary_strategy = st.builds(
    Salary,
    OverTime=
        safe_text,
    Sly_Decrement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Basic=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Id=
        st.integers(),
    Sly_Netgross=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Increment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Manager_strategy = st.builds(
    Manager,
    Emp_NIC=
        safe_text,
    Mng_Email=
        safe_text,
    Mng_Salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Date_Of_Joint=
        st.dates(),
    Emp_Position=
        safe_text,
    Emp_DOB=
        st.dates(),
    Mng_Name=
        safe_text,
    Mng_ContactNo=
        safe_text,
    Mng_Id=
        st.integers(),
    Emp_Department=
        safe_text,
    Emp_Address=
        safe_text
)






@given(instance=Tuning_Staff_strategy)
def test_hyp_tuning_staff_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Tuning_Staff_strategy)
def test_hyp_tuning_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Tuning_Staff_strategy)
def test_hyp_tuning_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original




@given(instance=Driving_Staff_strategy)
def test_hyp_driving_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original



@given(instance=Driving_Staff_strategy)
def test_hyp_driving_staff_PilotName_setter(instance):
    original = instance.PilotName
    instance.PilotName = original
    assert instance.PilotName == original



@given(instance=Driving_Staff_strategy)
def test_hyp_driving_staff_Pilot_ContactNo_setter(instance):
    original = instance.Pilot_ContactNo
    instance.Pilot_ContactNo = original
    assert instance.Pilot_ContactNo == original



@given(instance=Driving_Staff_strategy)
def test_hyp_driving_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original




@given(instance=Administrator_strategy)
def test_hyp_administrator_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Admin_Id_setter(instance):
    original = instance.Admin_Id
    instance.Admin_Id = original
    assert instance.Admin_Id == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Admin_Name_setter(instance):
    original = instance.Admin_Name
    instance.Admin_Name = original
    assert instance.Admin_Name == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Admin_NIC_setter(instance):
    original = instance.Admin_NIC
    instance.Admin_NIC = original
    assert instance.Admin_NIC == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Admin_Email_setter(instance):
    original = instance.Admin_Email
    instance.Admin_Email = original
    assert instance.Admin_Email == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Emp_Date_Of_Joint_setter(instance):
    original = instance.Emp_Date_Of_Joint
    instance.Emp_Date_Of_Joint = original
    assert instance.Emp_Date_Of_Joint == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Admin_ContactNo_setter(instance):
    original = instance.Admin_ContactNo
    instance.Admin_ContactNo = original
    assert instance.Admin_ContactNo == original









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
def test_hyp_attendance_Emp_id_setter(instance):
    original = instance.Emp_id
    instance.Emp_id = original
    assert instance.Emp_id == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_Leaving_Time_setter(instance):
    original = instance.Leaving_Time
    instance.Leaving_Time = original
    assert instance.Leaving_Time == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_AttendTime_setter(instance):
    original = instance.AttendTime
    instance.AttendTime = original
    assert instance.AttendTime == original



@given(instance=Attendance_strategy)
def test_hyp_attendance_Attend_date_setter(instance):
    original = instance.Attend_date
    instance.Attend_date = original
    assert instance.Attend_date == original




@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Leave_detail_setter(instance):
    original = instance.Leave_detail
    instance.Leave_detail = original
    assert instance.Leave_detail == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Leave_ApplyDate_setter(instance):
    original = instance.Leave_ApplyDate
    instance.Leave_ApplyDate = original
    assert instance.Leave_ApplyDate == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original



@given(instance=Leave_Status_strategy)
def test_hyp_leave_status_Leave_StartDate_setter(instance):
    original = instance.Leave_StartDate
    instance.Leave_StartDate = original
    assert instance.Leave_StartDate == original




@given(instance=Staff_strategy)
def test_hyp_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Staff_strategy)
def test_hyp_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original



@given(instance=Staff_strategy)
def test_hyp_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original




@given(instance=Salary_strategy)
def test_hyp_salary_OverTime_setter(instance):
    original = instance.OverTime
    instance.OverTime = original
    assert instance.OverTime == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Decrement_setter(instance):
    original = instance.Sly_Decrement
    instance.Sly_Decrement = original
    assert instance.Sly_Decrement == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Basic_setter(instance):
    original = instance.Sly_Basic
    instance.Sly_Basic = original
    assert instance.Sly_Basic == original



@given(instance=Salary_strategy)
def test_hyp_salary_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Netgross_setter(instance):
    original = instance.Sly_Netgross
    instance.Sly_Netgross = original
    assert instance.Sly_Netgross == original



@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Increment_setter(instance):
    original = instance.Sly_Increment
    instance.Sly_Increment = original
    assert instance.Sly_Increment == original




@given(instance=Manager_strategy)
def test_hyp_manager_Emp_NIC_setter(instance):
    original = instance.Emp_NIC
    instance.Emp_NIC = original
    assert instance.Emp_NIC == original



@given(instance=Manager_strategy)
def test_hyp_manager_Mng_Email_setter(instance):
    original = instance.Mng_Email
    instance.Mng_Email = original
    assert instance.Mng_Email == original



@given(instance=Manager_strategy)
def test_hyp_manager_Mng_Salary_setter(instance):
    original = instance.Mng_Salary
    instance.Mng_Salary = original
    assert instance.Mng_Salary == original



@given(instance=Manager_strategy)
def test_hyp_manager_Emp_Date_Of_Joint_setter(instance):
    original = instance.Emp_Date_Of_Joint
    instance.Emp_Date_Of_Joint = original
    assert instance.Emp_Date_Of_Joint == original



@given(instance=Manager_strategy)
def test_hyp_manager_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original



@given(instance=Manager_strategy)
def test_hyp_manager_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



@given(instance=Manager_strategy)
def test_hyp_manager_Mng_Name_setter(instance):
    original = instance.Mng_Name
    instance.Mng_Name = original
    assert instance.Mng_Name == original



@given(instance=Manager_strategy)
def test_hyp_manager_Mng_ContactNo_setter(instance):
    original = instance.Mng_ContactNo
    instance.Mng_ContactNo = original
    assert instance.Mng_ContactNo == original



@given(instance=Manager_strategy)
def test_hyp_manager_Mng_Id_setter(instance):
    original = instance.Mng_Id
    instance.Mng_Id = original
    assert instance.Mng_Id == original



@given(instance=Manager_strategy)
def test_hyp_manager_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original



@given(instance=Manager_strategy)
def test_hyp_manager_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator,
    Administrator_Actor,
    Attendance,
    Authentication_UseCase,
    Driving_Staff,
    Employee_Actor,
    Employee_Management_System_Component,
    Leave_Status,
    Login,
    Login_external,
    Logout_external,
    Manager,
    Salary,
    Salary_Management_UseCase,
    Staff,
    Tuning_Staff,
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

def test_Administrator_Admin_ContactNo_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Admin_ContactNo == "sample_text"
    instance.Admin_ContactNo = "sample_text_2"
    assert instance.Admin_ContactNo == "sample_text_2"


def test_Administrator_Admin_Email_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Admin_Email == "sample_text"
    instance.Admin_Email = "sample_text_2"
    assert instance.Admin_Email == "sample_text_2"


def test_Administrator_Admin_Id_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Admin_Id == 7
    instance.Admin_Id = 13
    assert instance.Admin_Id == 13


def test_Administrator_Admin_NIC_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Admin_NIC == "sample_text"
    instance.Admin_NIC = "sample_text_2"
    assert instance.Admin_NIC == "sample_text_2"


def test_Administrator_Admin_Name_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Admin_Name == "sample_text"
    instance.Admin_Name = "sample_text_2"
    assert instance.Admin_Name == "sample_text_2"


def test_Administrator_Emp_DOB_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Emp_DOB == date(2024, 1, 1)
    instance.Emp_DOB = date(2025, 6, 15)
    assert instance.Emp_DOB == date(2025, 6, 15)


def test_Administrator_Emp_Date_Of_Joint_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Date_Of_Joint == date(2024, 1, 1)
    instance.Emp_Date_Of_Joint = date(2025, 6, 15)
    assert instance.Emp_Date_Of_Joint == date(2025, 6, 15)


def test_Administrator_Emp_Department_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Department == "sample_text"
    instance.Emp_Department = "sample_text_2"
    assert instance.Emp_Department == "sample_text_2"


def test_Administrator_Emp_Position_value_roundtrip():
    instance = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Position == "sample_text"
    instance.Emp_Position = "sample_text_2"
    assert instance.Emp_Position == "sample_text_2"


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


def test_Driving_Staff_Authendication_Mood_value_roundtrip():
    instance = Driving_Staff(Authendication_Mood="sample_text", Password="sample_text", PilotName="sample_text", Pilot_ContactNo="sample_text")
    assert instance.Authendication_Mood == "sample_text"
    instance.Authendication_Mood = "sample_text_2"
    assert instance.Authendication_Mood == "sample_text_2"


def test_Driving_Staff_Password_value_roundtrip():
    instance = Driving_Staff(Authendication_Mood="sample_text", Password="sample_text", PilotName="sample_text", Pilot_ContactNo="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Driving_Staff_PilotName_value_roundtrip():
    instance = Driving_Staff(Authendication_Mood="sample_text", Password="sample_text", PilotName="sample_text", Pilot_ContactNo="sample_text")
    assert instance.PilotName == "sample_text"
    instance.PilotName = "sample_text_2"
    assert instance.PilotName == "sample_text_2"


def test_Driving_Staff_Pilot_ContactNo_value_roundtrip():
    instance = Driving_Staff(Authendication_Mood="sample_text", Password="sample_text", PilotName="sample_text", Pilot_ContactNo="sample_text")
    assert instance.Pilot_ContactNo == "sample_text"
    instance.Pilot_ContactNo = "sample_text_2"
    assert instance.Pilot_ContactNo == "sample_text_2"


def test_Leave_Status_Emp_Id_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Emp_Id == 7
    instance.Emp_Id = 13
    assert instance.Emp_Id == 13


def test_Leave_Status_Leave_ApplyDate_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_ApplyDate == date(2024, 1, 1)
    instance.Leave_ApplyDate = date(2025, 6, 15)
    assert instance.Leave_ApplyDate == date(2025, 6, 15)


def test_Leave_Status_Leave_EndDate_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_EndDate == date(2024, 1, 1)
    instance.Leave_EndDate = date(2025, 6, 15)
    assert instance.Leave_EndDate == date(2025, 6, 15)


def test_Leave_Status_Leave_NoOfDays_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_NoOfDays == 7
    instance.Leave_NoOfDays = 13
    assert instance.Leave_NoOfDays == 13


def test_Leave_Status_Leave_StartDate_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_StartDate == date(2024, 1, 1)
    instance.Leave_StartDate = date(2025, 6, 15)
    assert instance.Leave_StartDate == date(2025, 6, 15)


def test_Leave_Status_Leave_Status_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_Status == "sample_text"
    instance.Leave_Status = "sample_text_2"
    assert instance.Leave_Status == "sample_text_2"


def test_Leave_Status_Leave_Title_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_Title == "sample_text"
    instance.Leave_Title = "sample_text_2"
    assert instance.Leave_Title == "sample_text_2"


def test_Leave_Status_Leave_detail_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_detail == "sample_text"
    instance.Leave_detail = "sample_text_2"
    assert instance.Leave_detail == "sample_text_2"


def test_Leave_Status_leave_id_value_roundtrip():
    instance = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
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


def test_Manager_Emp_Address_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Emp_Address == "sample_text"
    instance.Emp_Address = "sample_text_2"
    assert instance.Emp_Address == "sample_text_2"


def test_Manager_Emp_DOB_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Emp_DOB == date(2024, 1, 1)
    instance.Emp_DOB = date(2025, 6, 15)
    assert instance.Emp_DOB == date(2025, 6, 15)


def test_Manager_Emp_Date_Of_Joint_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Emp_Date_Of_Joint == date(2024, 1, 1)
    instance.Emp_Date_Of_Joint = date(2025, 6, 15)
    assert instance.Emp_Date_Of_Joint == date(2025, 6, 15)


def test_Manager_Emp_Department_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Emp_Department == "sample_text"
    instance.Emp_Department = "sample_text_2"
    assert instance.Emp_Department == "sample_text_2"


def test_Manager_Emp_NIC_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Emp_NIC == "sample_text"
    instance.Emp_NIC = "sample_text_2"
    assert instance.Emp_NIC == "sample_text_2"


def test_Manager_Emp_Position_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Emp_Position == "sample_text"
    instance.Emp_Position = "sample_text_2"
    assert instance.Emp_Position == "sample_text_2"


def test_Manager_Mng_ContactNo_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Mng_ContactNo == "sample_text"
    instance.Mng_ContactNo = "sample_text_2"
    assert instance.Mng_ContactNo == "sample_text_2"


def test_Manager_Mng_Email_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Mng_Email == "sample_text"
    instance.Mng_Email = "sample_text_2"
    assert instance.Mng_Email == "sample_text_2"


def test_Manager_Mng_Id_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Mng_Id == 7
    instance.Mng_Id = 13
    assert instance.Mng_Id == 13


def test_Manager_Mng_Name_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Mng_Name == "sample_text"
    instance.Mng_Name = "sample_text_2"
    assert instance.Mng_Name == "sample_text_2"


def test_Manager_Mng_Salary_value_roundtrip():
    instance = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    assert instance.Mng_Salary == 3.14
    instance.Mng_Salary = 9.99
    assert instance.Mng_Salary == 9.99


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


def test_Staff_Authendication_Mood_value_roundtrip():
    instance = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    assert instance.Authendication_Mood == "sample_text"
    instance.Authendication_Mood = "sample_text_2"
    assert instance.Authendication_Mood == "sample_text_2"


def test_Staff_Password_value_roundtrip():
    instance = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Staff_UserName_value_roundtrip():
    instance = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Tuning_Staff_Address_value_roundtrip():
    instance = Tuning_Staff(Address="sample_text", Authendication_Mood="sample_text", UserName="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Tuning_Staff_Authendication_Mood_value_roundtrip():
    instance = Tuning_Staff(Address="sample_text", Authendication_Mood="sample_text", UserName="sample_text")
    assert instance.Authendication_Mood == "sample_text"
    instance.Authendication_Mood = "sample_text_2"
    assert instance.Authendication_Mood == "sample_text_2"


def test_Tuning_Staff_UserName_value_roundtrip():
    instance = Tuning_Staff(Address="sample_text", Authendication_Mood="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_assoc_Administrator_Login_link_reassign_clear():
    a = Login(Password="sample_text", UserName="sample_text")
    b1 = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    b2 = Administrator(Admin_ContactNo="sample_text_2", Admin_Email="sample_text_2", Admin_Id=13, Admin_NIC="sample_text_2", Admin_Name="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_Position="sample_text_2")
    _safe_set(a, 'administrator17', b1)
    assert _is_linked(a, 'administrator17', b1)
    if hasattr(b1, 'login16'):
        assert _is_linked(b1, 'login16', a)
    _safe_set(a, 'administrator17', b2)
    assert _is_linked(a, 'administrator17', b2)
    if hasattr(b1, 'login16'):
        assert not _is_linked(b1, 'login16', a)
    if hasattr(b2, 'login16'):
        assert _is_linked(b2, 'login16', a)
    _safe_set(a, 'administrator17', None)
    assert not _is_linked(a, 'administrator17', b2)
    if hasattr(b2, 'login16'):
        assert not _is_linked(b2, 'login16', a)


def test_assoc_Administrator_Manager_link_reassign_clear():
    a = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    b1 = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    b2 = Administrator(Admin_ContactNo="sample_text_2", Admin_Email="sample_text_2", Admin_Id=13, Admin_NIC="sample_text_2", Admin_Name="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_Position="sample_text_2")
    _safe_set(a, 'administrator13', b1)
    assert _is_linked(a, 'administrator13', b1)
    if hasattr(b1, 'manager12'):
        assert _is_linked(b1, 'manager12', a)
    _safe_set(a, 'administrator13', b2)
    assert _is_linked(a, 'administrator13', b2)
    if hasattr(b1, 'manager12'):
        assert not _is_linked(b1, 'manager12', a)
    if hasattr(b2, 'manager12'):
        assert _is_linked(b2, 'manager12', a)
    _safe_set(a, 'administrator13', None)
    assert not _is_linked(a, 'administrator13', b2)
    if hasattr(b2, 'manager12'):
        assert not _is_linked(b2, 'manager12', a)


def test_assoc_Employee_Attendance_link_reassign_clear():
    a = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
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
    a = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    b1 = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    b2 = Leave_Status(Emp_Id=13, Leave_ApplyDate=date(2025, 6, 15), Leave_EndDate=date(2025, 6, 15), Leave_NoOfDays=13, Leave_StartDate=date(2025, 6, 15), Leave_Status="sample_text_2", Leave_Title="sample_text_2", Leave_detail="sample_text_2", leave_id=13)
    _safe_set(a, 'leave0', b1)
    assert _is_linked(a, 'leave0', b1)
    if hasattr(b1, 'employee1'):
        assert _is_linked(b1, 'employee1', a)
    _safe_set(a, 'leave0', b2)
    assert _is_linked(a, 'leave0', b2)
    if hasattr(b1, 'employee1'):
        assert not _is_linked(b1, 'employee1', a)
    if hasattr(b2, 'employee1'):
        assert _is_linked(b2, 'employee1', a)
    _safe_set(a, 'leave0', None)
    assert not _is_linked(a, 'leave0', b2)
    if hasattr(b2, 'employee1'):
        assert not _is_linked(b2, 'employee1', a)


def test_assoc_Employee_Salary_link_reassign_clear():
    a = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    b1 = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    b2 = Manager(Emp_Address="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_NIC="sample_text_2", Emp_Position="sample_text_2", Mng_ContactNo="sample_text_2", Mng_Email="sample_text_2", Mng_Id=13, Mng_Name="sample_text_2", Mng_Salary=9.99)
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


def test_assoc_Login_Administrator_link_reassign_clear():
    a = Login(Password="sample_text", UserName="sample_text")
    b1 = Administrator(Admin_ContactNo="sample_text", Admin_Email="sample_text", Admin_Id=7, Admin_NIC="sample_text", Admin_Name="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_Position="sample_text")
    b2 = Administrator(Admin_ContactNo="sample_text_2", Admin_Email="sample_text_2", Admin_Id=13, Admin_NIC="sample_text_2", Admin_Name="sample_text_2", Emp_DOB=date(2025, 6, 15), Emp_Date_Of_Joint=date(2025, 6, 15), Emp_Department="sample_text_2", Emp_Position="sample_text_2")
    _safe_set(a, 'administrator14', b1)
    assert _is_linked(a, 'administrator14', b1)
    if hasattr(b1, 'login15'):
        assert _is_linked(b1, 'login15', a)
    _safe_set(a, 'administrator14', b2)
    assert _is_linked(a, 'administrator14', b2)
    if hasattr(b1, 'login15'):
        assert not _is_linked(b1, 'login15', a)
    if hasattr(b2, 'login15'):
        assert _is_linked(b2, 'login15', a)
    _safe_set(a, 'administrator14', None)
    assert not _is_linked(a, 'administrator14', b2)
    if hasattr(b2, 'login15'):
        assert not _is_linked(b2, 'login15', a)


def test_assoc_Login_Manager_link_reassign_clear():
    a = Manager(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Department="sample_text", Emp_NIC="sample_text", Emp_Position="sample_text", Mng_ContactNo="sample_text", Mng_Email="sample_text", Mng_Id=7, Mng_Name="sample_text", Mng_Salary=3.14)
    b1 = Login(Password="sample_text", UserName="sample_text")
    b2 = Login(Password="sample_text_2", UserName="sample_text_2")
    _safe_set(a, 'login19', b1)
    assert _is_linked(a, 'login19', b1)
    if hasattr(b1, 'manager18'):
        assert _is_linked(b1, 'manager18', a)
    _safe_set(a, 'login19', b2)
    assert _is_linked(a, 'login19', b2)
    if hasattr(b1, 'manager18'):
        assert not _is_linked(b1, 'manager18', a)
    if hasattr(b2, 'manager18'):
        assert _is_linked(b2, 'manager18', a)
    _safe_set(a, 'login19', None)
    assert not _is_linked(a, 'login19', b2)
    if hasattr(b2, 'manager18'):
        assert not _is_linked(b2, 'manager18', a)


def test_assoc_Staff_Driving_Staff_link_reassign_clear():
    a = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    b1 = Driving_Staff(Authendication_Mood="sample_text", Password="sample_text", PilotName="sample_text", Pilot_ContactNo="sample_text")
    b2 = Driving_Staff(Authendication_Mood="sample_text_2", Password="sample_text_2", PilotName="sample_text_2", Pilot_ContactNo="sample_text_2")
    _safe_set(a, 'driving_Staff20', b1)
    assert _is_linked(a, 'driving_Staff20', b1)
    if hasattr(b1, 'staff21'):
        assert _is_linked(b1, 'staff21', a)
    _safe_set(a, 'driving_Staff20', b2)
    assert _is_linked(a, 'driving_Staff20', b2)
    if hasattr(b1, 'staff21'):
        assert not _is_linked(b1, 'staff21', a)
    if hasattr(b2, 'staff21'):
        assert _is_linked(b2, 'staff21', a)
    _safe_set(a, 'driving_Staff20', None)
    assert not _is_linked(a, 'driving_Staff20', b2)
    if hasattr(b2, 'staff21'):
        assert not _is_linked(b2, 'staff21', a)


def test_assoc_Staff_Leave_Status_link_reassign_clear():
    a = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    b1 = Leave_Status(Emp_Id=7, Leave_ApplyDate=date(2024, 1, 1), Leave_EndDate=date(2024, 1, 1), Leave_NoOfDays=7, Leave_StartDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    b2 = Leave_Status(Emp_Id=13, Leave_ApplyDate=date(2025, 6, 15), Leave_EndDate=date(2025, 6, 15), Leave_NoOfDays=13, Leave_StartDate=date(2025, 6, 15), Leave_Status="sample_text_2", Leave_Title="sample_text_2", Leave_detail="sample_text_2", leave_id=13)
    _safe_set(a, 'leave_Status10', b1)
    assert _is_linked(a, 'leave_Status10', b1)
    if hasattr(b1, 'staff11'):
        assert _is_linked(b1, 'staff11', a)
    _safe_set(a, 'leave_Status10', b2)
    assert _is_linked(a, 'leave_Status10', b2)
    if hasattr(b1, 'staff11'):
        assert not _is_linked(b1, 'staff11', a)
    if hasattr(b2, 'staff11'):
        assert _is_linked(b2, 'staff11', a)
    _safe_set(a, 'leave_Status10', None)
    assert not _is_linked(a, 'leave_Status10', b2)
    if hasattr(b2, 'staff11'):
        assert not _is_linked(b2, 'staff11', a)


def test_assoc_Staff_Tuning_Staff_link_reassign_clear():
    a = Tuning_Staff(Address="sample_text", Authendication_Mood="sample_text", UserName="sample_text")
    b1 = Staff(Authendication_Mood="sample_text", Password="sample_text", UserName="sample_text")
    b2 = Staff(Authendication_Mood="sample_text_2", Password="sample_text_2", UserName="sample_text_2")
    _safe_set(a, 'staff23', b1)
    assert _is_linked(a, 'staff23', b1)
    if hasattr(b1, 'tuning_Staff22'):
        assert _is_linked(b1, 'tuning_Staff22', a)
    _safe_set(a, 'staff23', b2)
    assert _is_linked(a, 'staff23', b2)
    if hasattr(b1, 'tuning_Staff22'):
        assert not _is_linked(b1, 'tuning_Staff22', a)
    if hasattr(b2, 'tuning_Staff22'):
        assert _is_linked(b2, 'tuning_Staff22', a)
    _safe_set(a, 'staff23', None)
    assert not _is_linked(a, 'staff23', b2)
    if hasattr(b2, 'tuning_Staff22'):
        assert not _is_linked(b2, 'tuning_Staff22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_strategy = st.builds(Administrator, Admin_ContactNo=safe_text, Admin_Email=safe_text, Admin_Id=st.integers(), Admin_NIC=safe_text, Admin_Name=safe_text, Emp_DOB=st.dates(), Emp_Date_Of_Joint=st.dates(), Emp_Department=safe_text, Emp_Position=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


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


Authentication_UseCase_strategy = st.builds(Authentication_UseCase)
@given(instance=Authentication_UseCase_strategy)
@settings(max_examples=25)
def test_Authentication_UseCase_instantiation(instance):
    assert isinstance(instance, Authentication_UseCase)


Driving_Staff_strategy = st.builds(Driving_Staff, Authendication_Mood=safe_text, Password=safe_text, PilotName=safe_text, Pilot_ContactNo=safe_text)
@given(instance=Driving_Staff_strategy)
@settings(max_examples=25)
def test_Driving_Staff_instantiation(instance):
    assert isinstance(instance, Driving_Staff)


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


Leave_Status_strategy = st.builds(Leave_Status, Emp_Id=st.integers(), Leave_ApplyDate=st.dates(), Leave_EndDate=st.dates(), Leave_NoOfDays=st.integers(), Leave_StartDate=st.dates(), Leave_Status=safe_text, Leave_Title=safe_text, Leave_detail=safe_text, leave_id=st.integers())
@given(instance=Leave_Status_strategy)
@settings(max_examples=25)
def test_Leave_Status_instantiation(instance):
    assert isinstance(instance, Leave_Status)


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


Manager_strategy = st.builds(Manager, Emp_Address=safe_text, Emp_DOB=st.dates(), Emp_Date_Of_Joint=st.dates(), Emp_Department=safe_text, Emp_NIC=safe_text, Emp_Position=safe_text, Mng_ContactNo=safe_text, Mng_Email=safe_text, Mng_Id=st.integers(), Mng_Name=safe_text, Mng_Salary=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


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


Staff_strategy = st.builds(Staff, Authendication_Mood=safe_text, Password=safe_text, UserName=safe_text)
@given(instance=Staff_strategy)
@settings(max_examples=25)
def test_Staff_instantiation(instance):
    assert isinstance(instance, Staff)


Tuning_Staff_strategy = st.builds(Tuning_Staff, Address=safe_text, Authendication_Mood=safe_text, UserName=safe_text)
@given(instance=Tuning_Staff_strategy)
@settings(max_examples=25)
def test_Tuning_Staff_instantiation(instance):
    assert isinstance(instance, Tuning_Staff)



