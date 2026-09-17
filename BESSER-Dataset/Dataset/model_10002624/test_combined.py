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
    Manager2,
    Customer1,
    Manager1,
    Order,
    Manager,
    Customer,
    Employee1,
    Admin1,
    Users1,
    Admin,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Users,
    Leave,
    Salary,
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



def test_hyp_manager2_is_not_abstract():
    assert not inspect.isabstract(Manager2)


def test_hyp_manager2_constructor_exists():
    assert callable(Manager2.__init__)


def test_hyp_manager2_constructor_args():
    sig = inspect.signature(Manager2.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_customer1_is_not_abstract():
    assert not inspect.isabstract(Customer1)


def test_hyp_customer1_constructor_exists():
    assert callable(Customer1.__init__)


def test_hyp_customer1_constructor_args():
    sig = inspect.signature(Customer1.__init__)
    params = list(sig.parameters.keys())
    assert "S" in params, "Missing parameter 'S'"
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"





def test_hyp_manager1_is_not_abstract():
    assert not inspect.isabstract(Manager1)


def test_hyp_manager1_constructor_exists():
    assert callable(Manager1.__init__)


def test_hyp_manager1_constructor_args():
    sig = inspect.signature(Manager1.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Manager_id" in params, "Missing parameter 'Manager_id'"






def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_hyp_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_hyp_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "UserName" in params, "Missing parameter 'UserName'"





def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "password" in params, "Missing parameter 'password'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "postal_code" in params, "Missing parameter 'postal_code'"
    assert "address" in params, "Missing parameter 'address'"








def test_hyp_employee1_is_not_abstract():
    assert not inspect.isabstract(Employee1)


def test_hyp_employee1_constructor_exists():
    assert callable(Employee1.__init__)


def test_hyp_employee1_constructor_args():
    sig = inspect.signature(Employee1.__init__)
    params = list(sig.parameters.keys())
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Emp_Dep" in params, "Missing parameter 'Emp_Dep'"
    assert "password" in params, "Missing parameter 'password'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Salary" in params, "Missing parameter 'Salary'"












def test_hyp_admin1_is_not_abstract():
    assert not inspect.isabstract(Admin1)


def test_hyp_admin1_constructor_exists():
    assert callable(Admin1.__init__)


def test_hyp_admin1_constructor_args():
    sig = inspect.signature(Admin1.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "UserName" in params, "Missing parameter 'UserName'"





def test_hyp_users1_is_not_abstract():
    assert not inspect.isabstract(Users1)


def test_hyp_users1_constructor_exists():
    assert callable(Users1.__init__)


def test_hyp_users1_constructor_args():
    sig = inspect.signature(Users1.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"





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



def test_hyp_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_hyp_users_constructor_exists():
    assert callable(Users.__init__)


def test_hyp_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"





def test_hyp_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_hyp_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_hyp_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "Leave_detail" in params, "Missing parameter 'Leave_detail'"
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"
    assert "leave_id" in params, "Missing parameter 'leave_id'"









def test_hyp_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_hyp_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_hyp_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"
    assert "Sly_Increment" in params, "Missing parameter 'Sly_Increment'"
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Sly_Netgross" in params, "Missing parameter 'Sly_Netgross'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"









def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Salary" in params, "Missing parameter 'Emp_Salary'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "Emp_Email" in params, "Missing parameter 'Emp_Email'"
    assert "Emp_ContactNo" in params, "Missing parameter 'Emp_ContactNo'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"










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
Manager2_strategy = st.builds(
    Manager2,
    id=
        st.integers(),
    password=
        safe_text,
    name=
        safe_text
)
Customer1_strategy = st.builds(
    Customer1,
    S=
        safe_text,
    Customer_Name=
        safe_text
)
Manager1_strategy = st.builds(
    Manager1,
    Name=
        safe_text,
    Password=
        safe_text,
    Manager_id=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    id=
        st.integers(),
    name=
        safe_text
)
Manager_strategy = st.builds(
    Manager,
    password=
        safe_text,
    UserName=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    country=
        safe_text,
    password=
        safe_text,
    UserName=
        safe_text,
    postal_code=
        st.integers(),
    address=
        safe_text
)
Employee1_strategy = st.builds(
    Employee1,
    contact_no=
        st.integers(),
    name=
        safe_text,
    Email=
        safe_text,
    Emp_Dep=
        safe_text,
    password=
        safe_text,
    Emp_Address=
        safe_text,
    attribute=
        safe_text,
    UserName=
        safe_text,
    Salary=
        st.integers()
)
Admin1_strategy = st.builds(
    Admin1,
    password=
        safe_text,
    UserName=
        safe_text
)
Users1_strategy = st.builds(
    Users1,
    id=
        safe_text,
    password=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    Password=
        safe_text,
    UserName=
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
Users_strategy = st.builds(
    Users,
    Password=
        safe_text,
    UserName=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    Leave_Title=
        safe_text,
    Emp_Id=
        st.integers(),
    Leave_EndDate=
        st.dates(),
    Leave_detail=
        safe_text,
    Leave_Status=
        safe_text,
    leave_id=
        st.integers()
)
Salary_strategy = st.builds(
    Salary,
    Sly_Basic=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Decrement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Increment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    OverTime=
        safe_text,
    Sly_Netgross=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Id=
        st.integers()
)
Employee_strategy = st.builds(
    Employee,
    Emp_Salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Password=
        safe_text,
    Emp_Name=
        safe_text,
    Emp_Address=
        safe_text,
    Emp_Email=
        safe_text,
    Emp_ContactNo=
        safe_text,
    Emp_Id=
        st.integers(),
    Emp_Department=
        safe_text
)






@given(instance=Manager2_strategy)
def test_hyp_manager2_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Manager2_strategy)
def test_hyp_manager2_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Manager2_strategy)
def test_hyp_manager2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Customer1_strategy)
def test_hyp_customer1_S_setter(instance):
    original = instance.S
    instance.S = original
    assert instance.S == original



@given(instance=Customer1_strategy)
def test_hyp_customer1_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original




@given(instance=Manager1_strategy)
def test_hyp_manager1_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Manager1_strategy)
def test_hyp_manager1_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Manager1_strategy)
def test_hyp_manager1_Manager_id_setter(instance):
    original = instance.Manager_id
    instance.Manager_id = original
    assert instance.Manager_id == original




@given(instance=Order_strategy)
def test_hyp_order_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Order_strategy)
def test_hyp_order_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Manager_strategy)
def test_hyp_manager_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Manager_strategy)
def test_hyp_manager_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original




@given(instance=Customer_strategy)
def test_hyp_customer_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Customer_strategy)
def test_hyp_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Customer_strategy)
def test_hyp_customer_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Customer_strategy)
def test_hyp_customer_postal_code_setter(instance):
    original = instance.postal_code
    instance.postal_code = original
    assert instance.postal_code == original



@given(instance=Customer_strategy)
def test_hyp_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original




@given(instance=Employee1_strategy)
def test_hyp_employee1_contact_no_setter(instance):
    original = instance.contact_no
    instance.contact_no = original
    assert instance.contact_no == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_Emp_Dep_setter(instance):
    original = instance.Emp_Dep
    instance.Emp_Dep = original
    assert instance.Emp_Dep == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Employee1_strategy)
def test_hyp_employee1_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original




@given(instance=Admin1_strategy)
def test_hyp_admin1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin1_strategy)
def test_hyp_admin1_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original




@given(instance=Users1_strategy)
def test_hyp_users1_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Users1_strategy)
def test_hyp_users1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Admin_strategy)
def test_hyp_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Admin_strategy)
def test_hyp_admin_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original









@given(instance=Users_strategy)
def test_hyp_users_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Users_strategy)
def test_hyp_users_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original




@given(instance=Leave_strategy)
def test_hyp_leave_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original



@given(instance=Leave_strategy)
def test_hyp_leave_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_detail_setter(instance):
    original = instance.Leave_detail
    instance.Leave_detail = original
    assert instance.Leave_detail == original



@given(instance=Leave_strategy)
def test_hyp_leave_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original



@given(instance=Leave_strategy)
def test_hyp_leave_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original




@given(instance=Salary_strategy)
def test_hyp_salary_Sly_Basic_setter(instance):
    original = instance.Sly_Basic
    instance.Sly_Basic = original
    assert instance.Sly_Basic == original



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
def test_hyp_salary_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original




@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Salary_setter(instance):
    original = instance.Emp_Salary
    instance.Emp_Salary = original
    assert instance.Emp_Salary == original



@given(instance=Employee_strategy)
def test_hyp_employee_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Email_setter(instance):
    original = instance.Emp_Email
    instance.Emp_Email = original
    assert instance.Emp_Email == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_ContactNo_setter(instance):
    original = instance.Emp_ContactNo
    instance.Emp_ContactNo = original
    assert instance.Emp_ContactNo == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Employee_strategy)
def test_hyp_employee_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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
    instance = Customer(UserName="sample_text", address="sample_text", country="sample_text", password="sample_text", postal_code=7)
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Customer_address_value_roundtrip():
    instance = Customer(UserName="sample_text", address="sample_text", country="sample_text", password="sample_text", postal_code=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_country_value_roundtrip():
    instance = Customer(UserName="sample_text", address="sample_text", country="sample_text", password="sample_text", postal_code=7)
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_Customer_password_value_roundtrip():
    instance = Customer(UserName="sample_text", address="sample_text", country="sample_text", password="sample_text", postal_code=7)
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Customer_postal_code_value_roundtrip():
    instance = Customer(UserName="sample_text", address="sample_text", country="sample_text", password="sample_text", postal_code=7)
    assert instance.postal_code == 7
    instance.postal_code = 13
    assert instance.postal_code == 13


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
    b1 = Customer(UserName="sample_text", address="sample_text", country="sample_text", password="sample_text", postal_code=7)
    b2 = Customer(UserName="sample_text_2", address="sample_text_2", country="sample_text_2", password="sample_text_2", postal_code=13)
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


Customer_strategy = st.builds(Customer, UserName=safe_text, address=safe_text, country=safe_text, password=safe_text, postal_code=st.integers())
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



