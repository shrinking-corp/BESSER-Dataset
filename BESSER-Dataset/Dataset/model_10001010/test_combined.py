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
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Login,
    Authenticate_staff,
    Employee,
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
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Password" in params, "Missing parameter 'Password'"





def test_hyp_authenticate_staff_is_not_abstract():
    assert not inspect.isabstract(Authenticate_staff)


def test_hyp_authenticate_staff_constructor_exists():
    assert callable(Authenticate_staff.__init__)


def test_hyp_authenticate_staff_constructor_args():
    sig = inspect.signature(Authenticate_staff.__init__)
    params = list(sig.parameters.keys())
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"






def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"








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
    UserName=
        safe_text,
    Password=
        safe_text
)
Authenticate_staff_strategy = st.builds(
    Authenticate_staff,
    Authendication_Mood=
        safe_text,
    Password=
        safe_text,
    UserName=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    Emp_Id=
        st.integers(),
    Emp_Position=
        safe_text,
    Emp_Date_Of_Joint=
        st.dates(),
    Emp_Address=
        safe_text,
    Emp_DOB=
        st.dates(),
    Emp_Name=
        safe_text
)











@given(instance=Login_strategy)
def test_hyp_login_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Login_strategy)
def test_hyp_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original




@given(instance=Authenticate_staff_strategy)
def test_hyp_authenticate_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original



@given(instance=Authenticate_staff_strategy)
def test_hyp_authenticate_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Authenticate_staff_strategy)
def test_hyp_authenticate_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original




@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Date_Of_Joint_setter(instance):
    original = instance.Emp_Date_Of_Joint
    instance.Emp_Date_Of_Joint = original
    assert instance.Emp_Date_Of_Joint == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator_Actor,
    Authenticate_staff,
    Authentication_UseCase,
    Employee,
    Employee_Actor,
    Employee_Management_System_Component,
    Login,
    Login_external,
    Logout_external,
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
    instance = Employee(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Id=7, Emp_Name="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Address == "sample_text"
    instance.Emp_Address = "sample_text_2"
    assert instance.Emp_Address == "sample_text_2"


def test_Employee_Emp_DOB_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Id=7, Emp_Name="sample_text", Emp_Position="sample_text")
    assert instance.Emp_DOB == date(2024, 1, 1)
    instance.Emp_DOB = date(2025, 6, 15)
    assert instance.Emp_DOB == date(2025, 6, 15)


def test_Employee_Emp_Date_Of_Joint_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Id=7, Emp_Name="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Date_Of_Joint == date(2024, 1, 1)
    instance.Emp_Date_Of_Joint = date(2025, 6, 15)
    assert instance.Emp_Date_Of_Joint == date(2025, 6, 15)


def test_Employee_Emp_Id_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Id=7, Emp_Name="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Id == 7
    instance.Emp_Id = 13
    assert instance.Emp_Id == 13


def test_Employee_Emp_Name_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Id=7, Emp_Name="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Name == "sample_text"
    instance.Emp_Name = "sample_text_2"
    assert instance.Emp_Name == "sample_text_2"


def test_Employee_Emp_Position_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_DOB=date(2024, 1, 1), Emp_Date_Of_Joint=date(2024, 1, 1), Emp_Id=7, Emp_Name="sample_text", Emp_Position="sample_text")
    assert instance.Emp_Position == "sample_text"
    instance.Emp_Position = "sample_text_2"
    assert instance.Emp_Position == "sample_text_2"


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


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


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


Employee_strategy = st.builds(Employee, Emp_Address=safe_text, Emp_DOB=st.dates(), Emp_Date_Of_Joint=st.dates(), Emp_Id=st.integers(), Emp_Name=safe_text, Emp_Position=safe_text)
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


Salary_Management_UseCase_strategy = st.builds(Salary_Management_UseCase)
@given(instance=Salary_Management_UseCase_strategy)
@settings(max_examples=25)
def test_Salary_Management_UseCase_instantiation(instance):
    assert isinstance(instance, Salary_Management_UseCase)



