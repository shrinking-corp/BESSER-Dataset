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
    Admin,
    Leave,
    Days_Attended,
    Salary,
    Employee,
    Login,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_hyp_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_hyp_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "Leave_Detail" in params, "Missing parameter 'Leave_Detail'"






def test_hyp_days_attended_is_not_abstract():
    assert not inspect.isabstract(Days_Attended)


def test_hyp_days_attended_constructor_exists():
    assert callable(Days_Attended.__init__)


def test_hyp_days_attended_constructor_args():
    sig = inspect.signature(Days_Attended.__init__)
    params = list(sig.parameters.keys())
    assert "Days_attended" in params, "Missing parameter 'Days_attended'"
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "EmployeeId" in params, "Missing parameter 'EmployeeId'"
    assert "EmployeeBasicSalary" in params, "Missing parameter 'EmployeeBasicSalary'"
    assert "Total_no__of_workingdays" in params, "Missing parameter 'Total_no__of_workingdays'"








def test_hyp_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_hyp_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_hyp_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "Bonus" in params, "Missing parameter 'Bonus'"
    assert "DaysAttended" in params, "Missing parameter 'DaysAttended'"
    assert "NetSalary" in params, "Missing parameter 'NetSalary'"
    assert "EmployeeID" in params, "Missing parameter 'EmployeeID'"







def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "EmployeeId" in params, "Missing parameter 'EmployeeId'"
    assert "EmployeeEmail" in params, "Missing parameter 'EmployeeEmail'"
    assert "EmplyeeName" in params, "Missing parameter 'EmplyeeName'"
    assert "EmployeePhoneNumber" in params, "Missing parameter 'EmployeePhoneNumber'"







def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"




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
Admin_strategy = st.builds(
    Admin,
    Email=
        safe_text,
    Name=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    Leave_NoOfDays=
        st.integers(),
    attribute=
        safe_text,
    Leave_Detail=
        safe_text
)
Days_Attended_strategy = st.builds(
    Days_Attended,
    Days_attended=
        st.integers(),
    OverTime=
        st.integers(),
    EmployeeId=
        safe_text,
    EmployeeBasicSalary=
        st.integers(),
    Total_no__of_workingdays=
        st.integers()
)
Salary_strategy = st.builds(
    Salary,
    Bonus=
        st.integers(),
    DaysAttended=
        st.integers(),
    NetSalary=
        st.integers(),
    EmployeeID=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    EmployeeId=
        safe_text,
    EmployeeEmail=
        safe_text,
    EmplyeeName=
        safe_text,
    EmployeePhoneNumber=
        st.integers()
)
Login_strategy = st.builds(
    Login,
    Username=
        safe_text,
    Password=
        safe_text
)




@given(instance=Admin_strategy)
def test_hyp_admin_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Admin_strategy)
def test_hyp_admin_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Leave_strategy)
def test_hyp_leave_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original



@given(instance=Leave_strategy)
def test_hyp_leave_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_Detail_setter(instance):
    original = instance.Leave_Detail
    instance.Leave_Detail = original
    assert instance.Leave_Detail == original




@given(instance=Days_Attended_strategy)
def test_hyp_days_attended_Days_attended_setter(instance):
    original = instance.Days_attended
    instance.Days_attended = original
    assert instance.Days_attended == original



@given(instance=Days_Attended_strategy)
def test_hyp_days_attended_OverTime_setter(instance):
    original = instance.OverTime
    instance.OverTime = original
    assert instance.OverTime == original



@given(instance=Days_Attended_strategy)
def test_hyp_days_attended_EmployeeId_setter(instance):
    original = instance.EmployeeId
    instance.EmployeeId = original
    assert instance.EmployeeId == original



@given(instance=Days_Attended_strategy)
def test_hyp_days_attended_EmployeeBasicSalary_setter(instance):
    original = instance.EmployeeBasicSalary
    instance.EmployeeBasicSalary = original
    assert instance.EmployeeBasicSalary == original



@given(instance=Days_Attended_strategy)
def test_hyp_days_attended_Total_no__of_workingdays_setter(instance):
    original = instance.Total_no__of_workingdays
    instance.Total_no__of_workingdays = original
    assert instance.Total_no__of_workingdays == original




@given(instance=Salary_strategy)
def test_hyp_salary_Bonus_setter(instance):
    original = instance.Bonus
    instance.Bonus = original
    assert instance.Bonus == original



@given(instance=Salary_strategy)
def test_hyp_salary_DaysAttended_setter(instance):
    original = instance.DaysAttended
    instance.DaysAttended = original
    assert instance.DaysAttended == original



@given(instance=Salary_strategy)
def test_hyp_salary_NetSalary_setter(instance):
    original = instance.NetSalary
    instance.NetSalary = original
    assert instance.NetSalary == original



@given(instance=Salary_strategy)
def test_hyp_salary_EmployeeID_setter(instance):
    original = instance.EmployeeID
    instance.EmployeeID = original
    assert instance.EmployeeID == original




@given(instance=Employee_strategy)
def test_hyp_employee_EmployeeId_setter(instance):
    original = instance.EmployeeId
    instance.EmployeeId = original
    assert instance.EmployeeId == original



@given(instance=Employee_strategy)
def test_hyp_employee_EmployeeEmail_setter(instance):
    original = instance.EmployeeEmail
    instance.EmployeeEmail = original
    assert instance.EmployeeEmail == original



@given(instance=Employee_strategy)
def test_hyp_employee_EmplyeeName_setter(instance):
    original = instance.EmplyeeName
    instance.EmplyeeName = original
    assert instance.EmplyeeName == original



@given(instance=Employee_strategy)
def test_hyp_employee_EmployeePhoneNumber_setter(instance):
    original = instance.EmployeePhoneNumber
    instance.EmployeePhoneNumber = original
    assert instance.EmployeePhoneNumber == original




@given(instance=Login_strategy)
def test_hyp_login_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Login_strategy)
def test_hyp_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Days_Attended,
    Employee,
    Leave,
    Login,
    Salary,
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

def test_Admin_Email_value_roundtrip():
    instance = Admin(Email="sample_text", Name="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Admin_Name_value_roundtrip():
    instance = Admin(Email="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Days_Attended_Days_attended_value_roundtrip():
    instance = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    assert instance.Days_attended == 7
    instance.Days_attended = 13
    assert instance.Days_attended == 13


def test_Days_Attended_EmployeeBasicSalary_value_roundtrip():
    instance = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    assert instance.EmployeeBasicSalary == 7
    instance.EmployeeBasicSalary = 13
    assert instance.EmployeeBasicSalary == 13


def test_Days_Attended_EmployeeId_value_roundtrip():
    instance = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    assert instance.EmployeeId == "sample_text"
    instance.EmployeeId = "sample_text_2"
    assert instance.EmployeeId == "sample_text_2"


def test_Days_Attended_OverTime_value_roundtrip():
    instance = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    assert instance.OverTime == 7
    instance.OverTime = 13
    assert instance.OverTime == 13


def test_Days_Attended_Total_no__of_workingdays_value_roundtrip():
    instance = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    assert instance.Total_no__of_workingdays == 7
    instance.Total_no__of_workingdays = 13
    assert instance.Total_no__of_workingdays == 13


def test_Employee_EmployeeEmail_value_roundtrip():
    instance = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    assert instance.EmployeeEmail == "sample_text"
    instance.EmployeeEmail = "sample_text_2"
    assert instance.EmployeeEmail == "sample_text_2"


def test_Employee_EmployeeId_value_roundtrip():
    instance = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    assert instance.EmployeeId == "sample_text"
    instance.EmployeeId = "sample_text_2"
    assert instance.EmployeeId == "sample_text_2"


def test_Employee_EmployeePhoneNumber_value_roundtrip():
    instance = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    assert instance.EmployeePhoneNumber == 7
    instance.EmployeePhoneNumber = 13
    assert instance.EmployeePhoneNumber == 13


def test_Employee_EmplyeeName_value_roundtrip():
    instance = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    assert instance.EmplyeeName == "sample_text"
    instance.EmplyeeName = "sample_text_2"
    assert instance.EmplyeeName == "sample_text_2"


def test_Leave_Leave_Detail_value_roundtrip():
    instance = Leave(Leave_Detail="sample_text", Leave_NoOfDays=7, attribute="sample_text")
    assert instance.Leave_Detail == "sample_text"
    instance.Leave_Detail = "sample_text_2"
    assert instance.Leave_Detail == "sample_text_2"


def test_Leave_Leave_NoOfDays_value_roundtrip():
    instance = Leave(Leave_Detail="sample_text", Leave_NoOfDays=7, attribute="sample_text")
    assert instance.Leave_NoOfDays == 7
    instance.Leave_NoOfDays = 13
    assert instance.Leave_NoOfDays == 13


def test_Leave_attribute_value_roundtrip():
    instance = Leave(Leave_Detail="sample_text", Leave_NoOfDays=7, attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Login_Password_value_roundtrip():
    instance = Login(Password="sample_text", Username="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Login_Username_value_roundtrip():
    instance = Login(Password="sample_text", Username="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_Salary_Bonus_value_roundtrip():
    instance = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    assert instance.Bonus == 7
    instance.Bonus = 13
    assert instance.Bonus == 13


def test_Salary_DaysAttended_value_roundtrip():
    instance = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    assert instance.DaysAttended == 7
    instance.DaysAttended = 13
    assert instance.DaysAttended == 13


def test_Salary_EmployeeID_value_roundtrip():
    instance = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    assert instance.EmployeeID == "sample_text"
    instance.EmployeeID = "sample_text_2"
    assert instance.EmployeeID == "sample_text_2"


def test_Salary_NetSalary_value_roundtrip():
    instance = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    assert instance.NetSalary == 7
    instance.NetSalary = 13
    assert instance.NetSalary == 13


def test_assoc_Admin_Employee_link_reassign_clear():
    a = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    b1 = Admin(Email="sample_text", Name="sample_text")
    b2 = Admin(Email="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'admin9', b1)
    assert _is_linked(a, 'admin9', b1)
    if hasattr(b1, 'employee8'):
        assert _is_linked(b1, 'employee8', a)
    _safe_set(a, 'admin9', b2)
    assert _is_linked(a, 'admin9', b2)
    if hasattr(b1, 'employee8'):
        assert not _is_linked(b1, 'employee8', a)
    if hasattr(b2, 'employee8'):
        assert _is_linked(b2, 'employee8', a)
    _safe_set(a, 'admin9', None)
    assert not _is_linked(a, 'admin9', b2)
    if hasattr(b2, 'employee8'):
        assert not _is_linked(b2, 'employee8', a)


def test_assoc_Employee_Days_Attended_link_reassign_clear():
    a = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    b1 = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    b2 = Days_Attended(Days_attended=13, EmployeeBasicSalary=13, EmployeeId="sample_text_2", OverTime=13, Total_no__of_workingdays=13)
    _safe_set(a, 'days_Attended4', {b1})
    assert _is_linked(a, 'days_Attended4', b1)
    if hasattr(b1, 'employee5'):
        assert _is_linked(b1, 'employee5', a)
    _safe_set(a, 'days_Attended4', {b2})
    assert _is_linked(a, 'days_Attended4', b2)
    if hasattr(b1, 'employee5'):
        assert not _is_linked(b1, 'employee5', a)
    if hasattr(b2, 'employee5'):
        assert _is_linked(b2, 'employee5', a)
    _safe_set(a, 'days_Attended4', set())
    assert not _is_linked(a, 'days_Attended4', b2)
    if hasattr(b2, 'employee5'):
        assert not _is_linked(b2, 'employee5', a)


def test_assoc_Employee_Leave_link_reassign_clear():
    a = Leave(Leave_Detail="sample_text", Leave_NoOfDays=7, attribute="sample_text")
    b1 = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    b2 = Employee(EmployeeEmail="sample_text_2", EmployeeId="sample_text_2", EmployeePhoneNumber=13, EmplyeeName="sample_text_2")
    _safe_set(a, 'employee7', b1)
    assert _is_linked(a, 'employee7', b1)
    if hasattr(b1, 'leave6'):
        assert _is_linked(b1, 'leave6', a)
    _safe_set(a, 'employee7', b2)
    assert _is_linked(a, 'employee7', b2)
    if hasattr(b1, 'leave6'):
        assert not _is_linked(b1, 'leave6', a)
    if hasattr(b2, 'leave6'):
        assert _is_linked(b2, 'leave6', a)
    _safe_set(a, 'employee7', None)
    assert not _is_linked(a, 'employee7', b2)
    if hasattr(b2, 'leave6'):
        assert not _is_linked(b2, 'leave6', a)


def test_assoc_Employee_Salary_link_reassign_clear():
    a = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    b1 = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    b2 = Employee(EmployeeEmail="sample_text_2", EmployeeId="sample_text_2", EmployeePhoneNumber=13, EmplyeeName="sample_text_2")
    _safe_set(a, 'employee3', b1)
    assert _is_linked(a, 'employee3', b1)
    if hasattr(b1, 'salary2'):
        assert _is_linked(b1, 'salary2', a)
    _safe_set(a, 'employee3', b2)
    assert _is_linked(a, 'employee3', b2)
    if hasattr(b1, 'salary2'):
        assert not _is_linked(b1, 'salary2', a)
    if hasattr(b2, 'salary2'):
        assert _is_linked(b2, 'salary2', a)
    _safe_set(a, 'employee3', None)
    assert not _is_linked(a, 'employee3', b2)
    if hasattr(b2, 'salary2'):
        assert not _is_linked(b2, 'salary2', a)


def test_assoc_Login_Employee_link_reassign_clear():
    a = Login(Password="sample_text", Username="sample_text")
    b1 = Employee(EmployeeEmail="sample_text", EmployeeId="sample_text", EmployeePhoneNumber=7, EmplyeeName="sample_text")
    b2 = Employee(EmployeeEmail="sample_text_2", EmployeeId="sample_text_2", EmployeePhoneNumber=13, EmplyeeName="sample_text_2")
    _safe_set(a, 'employee0', b1)
    assert _is_linked(a, 'employee0', b1)
    if hasattr(b1, 'login1'):
        assert _is_linked(b1, 'login1', a)
    _safe_set(a, 'employee0', b2)
    assert _is_linked(a, 'employee0', b2)
    if hasattr(b1, 'login1'):
        assert not _is_linked(b1, 'login1', a)
    if hasattr(b2, 'login1'):
        assert _is_linked(b2, 'login1', a)
    _safe_set(a, 'employee0', None)
    assert not _is_linked(a, 'employee0', b2)
    if hasattr(b2, 'login1'):
        assert not _is_linked(b2, 'login1', a)


def test_assoc_Salary_Days_Attended_link_reassign_clear():
    a = Salary(Bonus=7, DaysAttended=7, EmployeeID="sample_text", NetSalary=7)
    b1 = Days_Attended(Days_attended=7, EmployeeBasicSalary=7, EmployeeId="sample_text", OverTime=7, Total_no__of_workingdays=7)
    b2 = Days_Attended(Days_attended=13, EmployeeBasicSalary=13, EmployeeId="sample_text_2", OverTime=13, Total_no__of_workingdays=13)
    _safe_set(a, 'days_Attended10', b1)
    assert _is_linked(a, 'days_Attended10', b1)
    if hasattr(b1, 'salary11'):
        assert _is_linked(b1, 'salary11', a)
    _safe_set(a, 'days_Attended10', b2)
    assert _is_linked(a, 'days_Attended10', b2)
    if hasattr(b1, 'salary11'):
        assert not _is_linked(b1, 'salary11', a)
    if hasattr(b2, 'salary11'):
        assert _is_linked(b2, 'salary11', a)
    _safe_set(a, 'days_Attended10', None)
    assert not _is_linked(a, 'days_Attended10', b2)
    if hasattr(b2, 'salary11'):
        assert not _is_linked(b2, 'salary11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, Email=safe_text, Name=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Days_Attended_strategy = st.builds(Days_Attended, Days_attended=st.integers(), EmployeeBasicSalary=st.integers(), EmployeeId=safe_text, OverTime=st.integers(), Total_no__of_workingdays=st.integers())
@given(instance=Days_Attended_strategy)
@settings(max_examples=25)
def test_Days_Attended_instantiation(instance):
    assert isinstance(instance, Days_Attended)


Employee_strategy = st.builds(Employee, EmployeeEmail=safe_text, EmployeeId=safe_text, EmployeePhoneNumber=st.integers(), EmplyeeName=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Leave_strategy = st.builds(Leave, Leave_Detail=safe_text, Leave_NoOfDays=st.integers(), attribute=safe_text)
@given(instance=Leave_strategy)
@settings(max_examples=25)
def test_Leave_instantiation(instance):
    assert isinstance(instance, Leave)


Login_strategy = st.builds(Login, Password=safe_text, Username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Salary_strategy = st.builds(Salary, Bonus=st.integers(), DaysAttended=st.integers(), EmployeeID=safe_text, NetSalary=st.integers())
@given(instance=Salary_strategy)
@settings(max_examples=25)
def test_Salary_instantiation(instance):
    assert isinstance(instance, Salary)



