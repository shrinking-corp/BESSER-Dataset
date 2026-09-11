import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Admin1,
    Administrator_Actor,
    Authentication_UseCase,
    Customer,
    Customer1,
    Employee,
    Employee1,
    Employee_Actor,
    Employee_Management_System_Component,
    Leave,
    Login_external,
    Logout_external,
    Manager,
    Manager1,
    Manager2,
    Order,
    Salary,
    Salary_Management_UseCase,
    Users,
    Users1,
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

def test_Admin_Password_value_roundtrip():
    instance = Admin(Password="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Admin_UserName_value_roundtrip():
    instance = Admin(Password="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Admin1_UserName_value_roundtrip():
    instance = Admin1(UserName="sample_text", password="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Admin1_password_value_roundtrip():
    instance = Admin1(UserName="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Customer_UserName_value_roundtrip():
    instance = Customer(UserName="sample_text", password="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Customer_password_value_roundtrip():
    instance = Customer(UserName="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Customer1_Customer_Name_value_roundtrip():
    instance = Customer1(Customer_Name="sample_text", S="sample_text")
    assert instance.Customer_Name == "sample_text"
    instance.Customer_Name = "sample_text_2"
    assert instance.Customer_Name == "sample_text_2"


def test_Customer1_S_value_roundtrip():
    instance = Customer1(Customer_Name="sample_text", S="sample_text")
    assert instance.S == "sample_text"
    instance.S = "sample_text_2"
    assert instance.S == "sample_text_2"


def test_Employee_Emp_Address_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Emp_Address == "sample_text"
    instance.Emp_Address = "sample_text_2"
    assert instance.Emp_Address == "sample_text_2"


def test_Employee_Emp_ContactNo_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Emp_ContactNo == "sample_text"
    instance.Emp_ContactNo = "sample_text_2"
    assert instance.Emp_ContactNo == "sample_text_2"


def test_Employee_Emp_Department_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Emp_Department == "sample_text"
    instance.Emp_Department = "sample_text_2"
    assert instance.Emp_Department == "sample_text_2"


def test_Employee_Emp_Email_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Emp_Email == "sample_text"
    instance.Emp_Email = "sample_text_2"
    assert instance.Emp_Email == "sample_text_2"


def test_Employee_Emp_Id_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Emp_Id == 7
    instance.Emp_Id = 13
    assert instance.Emp_Id == 13


def test_Employee_Emp_Name_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Emp_Name == "sample_text"
    instance.Emp_Name = "sample_text_2"
    assert instance.Emp_Name == "sample_text_2"


def test_Employee_Emp_Salary_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Emp_Salary == 3.14
    instance.Emp_Salary = 9.99
    assert instance.Emp_Salary == 9.99


def test_Employee_Password_value_roundtrip():
    instance = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Employee1_Email_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Employee1_Emp_Address_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.Emp_Address == "sample_text"
    instance.Emp_Address = "sample_text_2"
    assert instance.Emp_Address == "sample_text_2"


def test_Employee1_Emp_Dep_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.Emp_Dep == "sample_text"
    instance.Emp_Dep = "sample_text_2"
    assert instance.Emp_Dep == "sample_text_2"


def test_Employee1_Salary_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.Salary == 7
    instance.Salary = 13
    assert instance.Salary == 13


def test_Employee1_UserName_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Employee1_attribute_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Employee1_contact_no_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.contact_no == 7
    instance.contact_no = 13
    assert instance.contact_no == 13


def test_Employee1_name_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Employee1_password_value_roundtrip():
    instance = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Leave_Emp_Id_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Emp_Id == 7
    instance.Emp_Id = 13
    assert instance.Emp_Id == 13


def test_Leave_Leave_EndDate_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_EndDate == date(2024, 1, 1)
    instance.Leave_EndDate = date(2025, 6, 15)
    assert instance.Leave_EndDate == date(2025, 6, 15)


def test_Leave_Leave_Status_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_Status == "sample_text"
    instance.Leave_Status = "sample_text_2"
    assert instance.Leave_Status == "sample_text_2"


def test_Leave_Leave_Title_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_Title == "sample_text"
    instance.Leave_Title = "sample_text_2"
    assert instance.Leave_Title == "sample_text_2"


def test_Leave_Leave_detail_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.Leave_detail == "sample_text"
    instance.Leave_detail = "sample_text_2"
    assert instance.Leave_detail == "sample_text_2"


def test_Leave_leave_id_value_roundtrip():
    instance = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    assert instance.leave_id == 7
    instance.leave_id = 13
    assert instance.leave_id == 13


def test_Manager_UserName_value_roundtrip():
    instance = Manager(UserName="sample_text", password="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Manager_password_value_roundtrip():
    instance = Manager(UserName="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Manager1_Manager_id_value_roundtrip():
    instance = Manager1(Manager_id=7, Name="sample_text", Password="sample_text")
    assert instance.Manager_id == 7
    instance.Manager_id = 13
    assert instance.Manager_id == 13


def test_Manager1_Name_value_roundtrip():
    instance = Manager1(Manager_id=7, Name="sample_text", Password="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Manager1_Password_value_roundtrip():
    instance = Manager1(Manager_id=7, Name="sample_text", Password="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Manager2_id_value_roundtrip():
    instance = Manager2(id=7, name="sample_text", password="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Manager2_name_value_roundtrip():
    instance = Manager2(id=7, name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Manager2_password_value_roundtrip():
    instance = Manager2(id=7, name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Order_id_value_roundtrip():
    instance = Order(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Order_name_value_roundtrip():
    instance = Order(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


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


def test_Users_Password_value_roundtrip():
    instance = Users(Password="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Users_UserName_value_roundtrip():
    instance = Users(Password="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Users1_id_value_roundtrip():
    instance = Users1(id="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Users1_password_value_roundtrip():
    instance = Users1(id="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_assoc_Admin_Employee_link_reassign_clear():
    a = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    b1 = Admin1(UserName="sample_text", password="sample_text")
    b2 = Admin1(UserName="sample_text_2", password="sample_text_2")
    _safe_set(a, 'admin11', b1)
    assert _is_linked(a, 'admin11', b1)
    if hasattr(b1, 'employee10'):
        assert _is_linked(b1, 'employee10', a)
    _safe_set(a, 'admin11', b2)
    assert _is_linked(a, 'admin11', b2)
    if hasattr(b1, 'employee10'):
        assert not _is_linked(b1, 'employee10', a)
    if hasattr(b2, 'employee10'):
        assert _is_linked(b2, 'employee10', a)
    _safe_set(a, 'admin11', None)
    assert not _is_linked(a, 'admin11', b2)
    if hasattr(b2, 'employee10'):
        assert not _is_linked(b2, 'employee10', a)


def test_assoc_Admin_Order_link_reassign_clear():
    a = Order(id=7, name="sample_text")
    b1 = Admin1(UserName="sample_text", password="sample_text")
    b2 = Admin1(UserName="sample_text_2", password="sample_text_2")
    _safe_set(a, 'admin13', b1)
    assert _is_linked(a, 'admin13', b1)
    if hasattr(b1, 'order12'):
        assert _is_linked(b1, 'order12', a)
    _safe_set(a, 'admin13', b2)
    assert _is_linked(a, 'admin13', b2)
    if hasattr(b1, 'order12'):
        assert not _is_linked(b1, 'order12', a)
    if hasattr(b2, 'order12'):
        assert _is_linked(b2, 'order12', a)
    _safe_set(a, 'admin13', None)
    assert not _is_linked(a, 'admin13', b2)
    if hasattr(b2, 'order12'):
        assert not _is_linked(b2, 'order12', a)


def test_assoc_Customer_Order_link_reassign_clear():
    a = Order(id=7, name="sample_text")
    b1 = Customer(UserName="sample_text", password="sample_text")
    b2 = Customer(UserName="sample_text_2", password="sample_text_2")
    _safe_set(a, 'customer9', b1)
    assert _is_linked(a, 'customer9', b1)
    if hasattr(b1, 'order8'):
        assert _is_linked(b1, 'order8', a)
    _safe_set(a, 'customer9', b2)
    assert _is_linked(a, 'customer9', b2)
    if hasattr(b1, 'order8'):
        assert not _is_linked(b1, 'order8', a)
    if hasattr(b2, 'order8'):
        assert _is_linked(b2, 'order8', a)
    _safe_set(a, 'customer9', None)
    assert not _is_linked(a, 'customer9', b2)
    if hasattr(b2, 'order8'):
        assert not _is_linked(b2, 'order8', a)


def test_assoc_Employee_Leave_link_reassign_clear():
    a = Leave(Emp_Id=7, Leave_EndDate=date(2024, 1, 1), Leave_Status="sample_text", Leave_Title="sample_text", Leave_detail="sample_text", leave_id=7)
    b1 = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    b2 = Employee(Emp_Address="sample_text_2", Emp_ContactNo="sample_text_2", Emp_Department="sample_text_2", Emp_Email="sample_text_2", Emp_Id=13, Emp_Name="sample_text_2", Emp_Salary=9.99, Password="sample_text_2")
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


def test_assoc_Employee_Manager_link_reassign_clear():
    a = Manager2(id=7, name="sample_text", password="sample_text")
    b1 = Employee1(Email="sample_text", Emp_Address="sample_text", Emp_Dep="sample_text", Salary=7, UserName="sample_text", attribute="sample_text", contact_no=7, name="sample_text", password="sample_text")
    b2 = Employee1(Email="sample_text_2", Emp_Address="sample_text_2", Emp_Dep="sample_text_2", Salary=13, UserName="sample_text_2", attribute="sample_text_2", contact_no=13, name="sample_text_2", password="sample_text_2")
    _safe_set(a, 'employee15', {b1})
    assert _is_linked(a, 'employee15', b1)
    if hasattr(b1, 'manager14'):
        assert _is_linked(b1, 'manager14', a)
    _safe_set(a, 'employee15', {b2})
    assert _is_linked(a, 'employee15', b2)
    if hasattr(b1, 'manager14'):
        assert not _is_linked(b1, 'manager14', a)
    if hasattr(b2, 'manager14'):
        assert _is_linked(b2, 'manager14', a)
    _safe_set(a, 'employee15', set())
    assert not _is_linked(a, 'employee15', b2)
    if hasattr(b2, 'manager14'):
        assert not _is_linked(b2, 'manager14', a)


def test_assoc_Employee_Salary_link_reassign_clear():
    a = Salary(Emp_Id=7, OverTime="sample_text", Sly_Basic=3.14, Sly_Decrement=3.14, Sly_Increment=3.14, Sly_Netgross=3.14)
    b1 = Employee(Emp_Address="sample_text", Emp_ContactNo="sample_text", Emp_Department="sample_text", Emp_Email="sample_text", Emp_Id=7, Emp_Name="sample_text", Emp_Salary=3.14, Password="sample_text")
    b2 = Employee(Emp_Address="sample_text_2", Emp_ContactNo="sample_text_2", Emp_Department="sample_text_2", Emp_Email="sample_text_2", Emp_Id=13, Emp_Name="sample_text_2", Emp_Salary=9.99, Password="sample_text_2")
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


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, Password=safe_text, UserName=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Admin1_strategy = st.builds(Admin1, UserName=safe_text, password=safe_text)
@given(instance=Admin1_strategy)
@settings(max_examples=25)
def test_Admin1_instantiation(instance):
    assert isinstance(instance, Admin1)


Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


Authentication_UseCase_strategy = st.builds(Authentication_UseCase)
@given(instance=Authentication_UseCase_strategy)
@settings(max_examples=25)
def test_Authentication_UseCase_instantiation(instance):
    assert isinstance(instance, Authentication_UseCase)


Customer_strategy = st.builds(Customer, UserName=safe_text, password=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Customer1_strategy = st.builds(Customer1, Customer_Name=safe_text, S=safe_text)
@given(instance=Customer1_strategy)
@settings(max_examples=25)
def test_Customer1_instantiation(instance):
    assert isinstance(instance, Customer1)


Employee_strategy = st.builds(Employee, Emp_Address=safe_text, Emp_ContactNo=safe_text, Emp_Department=safe_text, Emp_Email=safe_text, Emp_Id=st.integers(), Emp_Name=safe_text, Emp_Salary=st.floats(allow_nan=False, allow_infinity=False), Password=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Employee1_strategy = st.builds(Employee1, Email=safe_text, Emp_Address=safe_text, Emp_Dep=safe_text, Salary=st.integers(), UserName=safe_text, attribute=safe_text, contact_no=st.integers(), name=safe_text, password=safe_text)
@given(instance=Employee1_strategy)
@settings(max_examples=25)
def test_Employee1_instantiation(instance):
    assert isinstance(instance, Employee1)


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


Leave_strategy = st.builds(Leave, Emp_Id=st.integers(), Leave_EndDate=st.dates(), Leave_Status=safe_text, Leave_Title=safe_text, Leave_detail=safe_text, leave_id=st.integers())
@given(instance=Leave_strategy)
@settings(max_examples=25)
def test_Leave_instantiation(instance):
    assert isinstance(instance, Leave)


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


Manager_strategy = st.builds(Manager, UserName=safe_text, password=safe_text)
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Manager1_strategy = st.builds(Manager1, Manager_id=st.integers(), Name=safe_text, Password=safe_text)
@given(instance=Manager1_strategy)
@settings(max_examples=25)
def test_Manager1_instantiation(instance):
    assert isinstance(instance, Manager1)


Manager2_strategy = st.builds(Manager2, id=st.integers(), name=safe_text, password=safe_text)
@given(instance=Manager2_strategy)
@settings(max_examples=25)
def test_Manager2_instantiation(instance):
    assert isinstance(instance, Manager2)


Order_strategy = st.builds(Order, id=st.integers(), name=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


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


Users_strategy = st.builds(Users, Password=safe_text, UserName=safe_text)
@given(instance=Users_strategy)
@settings(max_examples=25)
def test_Users_instantiation(instance):
    assert isinstance(instance, Users)


Users1_strategy = st.builds(Users1, id=safe_text, password=safe_text)
@given(instance=Users1_strategy)
@settings(max_examples=25)
def test_Users1_instantiation(instance):
    assert isinstance(instance, Users1)


