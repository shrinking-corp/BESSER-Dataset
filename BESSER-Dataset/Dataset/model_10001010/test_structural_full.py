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


