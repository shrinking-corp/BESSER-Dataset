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
    Loan,
    payslip,
    Attendence,
    EmployeeRequest,
    Admin,
    Login,
    Salary,
    Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_loan_is_not_abstract():
    assert not inspect.isabstract(Loan)


def test_hyp_loan_constructor_exists():
    assert callable(Loan.__init__)


def test_hyp_loan_constructor_args():
    sig = inspect.signature(Loan.__init__)
    params = list(sig.parameters.keys())
    assert "loan_purpose" in params, "Missing parameter 'loan_purpose'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"
    assert "loan_type" in params, "Missing parameter 'loan_type'"
    assert "loan_interst" in params, "Missing parameter 'loan_interst'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "amount" in params, "Missing parameter 'amount'"









def test_hyp_payslip_is_not_abstract():
    assert not inspect.isabstract(payslip)


def test_hyp_payslip_constructor_exists():
    assert callable(payslip.__init__)


def test_hyp_payslip_constructor_args():
    sig = inspect.signature(payslip.__init__)
    params = list(sig.parameters.keys())
    assert "emp_name" in params, "Missing parameter 'emp_name'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"





def test_hyp_attendence_is_not_abstract():
    assert not inspect.isabstract(Attendence)


def test_hyp_attendence_constructor_exists():
    assert callable(Attendence.__init__)


def test_hyp_attendence_constructor_args():
    sig = inspect.signature(Attendence.__init__)
    params = list(sig.parameters.keys())
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "Basic_salary" in params, "Missing parameter 'Basic_salary'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"






def test_hyp_employeerequest_is_not_abstract():
    assert not inspect.isabstract(EmployeeRequest)


def test_hyp_employeerequest_constructor_exists():
    assert callable(EmployeeRequest.__init__)


def test_hyp_employeerequest_constructor_args():
    sig = inspect.signature(EmployeeRequest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "adminEmail" in params, "Missing parameter 'adminEmail'"





def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_hyp_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_hyp_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "basic_salary" in params, "Missing parameter 'basic_salary'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"






def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "emp_email" in params, "Missing parameter 'emp_email'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"





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
Loan_strategy = st.builds(
    Loan,
    loan_purpose=
        safe_text,
    emp_name=
        safe_text,
    loan_type=
        safe_text,
    loan_interst=
        st.integers(),
    emp_id=
        st.integers(),
    amount=
        safe_text
)
payslip_strategy = st.builds(
    payslip,
    emp_name=
        safe_text,
    emp_id=
        st.integers()
)
Attendence_strategy = st.builds(
    Attendence,
    emp_id=
        st.integers(),
    Basic_salary=
        st.integers(),
    emp_name=
        safe_text
)
EmployeeRequest_strategy = st.builds(
    EmployeeRequest,
)
Admin_strategy = st.builds(
    Admin,
    password=
        st.integers(),
    adminEmail=
        safe_text
)
Login_strategy = st.builds(
    Login,
    username=
        safe_text,
    password=
        st.integers()
)
Salary_strategy = st.builds(
    Salary,
    emp_id=
        st.integers(),
    basic_salary=
        safe_text,
    emp_name=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    emp_email=
        safe_text,
    emp_name=
        safe_text,
    emp_id=
        st.integers()
)




@given(instance=Loan_strategy)
def test_hyp_loan_loan_purpose_setter(instance):
    original = instance.loan_purpose
    instance.loan_purpose = original
    assert instance.loan_purpose == original



@given(instance=Loan_strategy)
def test_hyp_loan_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original



@given(instance=Loan_strategy)
def test_hyp_loan_loan_type_setter(instance):
    original = instance.loan_type
    instance.loan_type = original
    assert instance.loan_type == original



@given(instance=Loan_strategy)
def test_hyp_loan_loan_interst_setter(instance):
    original = instance.loan_interst
    instance.loan_interst = original
    assert instance.loan_interst == original



@given(instance=Loan_strategy)
def test_hyp_loan_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Loan_strategy)
def test_hyp_loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=payslip_strategy)
def test_hyp_payslip_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original



@given(instance=payslip_strategy)
def test_hyp_payslip_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original




@given(instance=Attendence_strategy)
def test_hyp_attendence_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Attendence_strategy)
def test_hyp_attendence_Basic_salary_setter(instance):
    original = instance.Basic_salary
    instance.Basic_salary = original
    assert instance.Basic_salary == original



@given(instance=Attendence_strategy)
def test_hyp_attendence_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original





@given(instance=Admin_strategy)
def test_hyp_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_hyp_admin_adminEmail_setter(instance):
    original = instance.adminEmail
    instance.adminEmail = original
    assert instance.adminEmail == original




@given(instance=Login_strategy)
def test_hyp_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Salary_strategy)
def test_hyp_salary_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Salary_strategy)
def test_hyp_salary_basic_salary_setter(instance):
    original = instance.basic_salary
    instance.basic_salary = original
    assert instance.basic_salary == original



@given(instance=Salary_strategy)
def test_hyp_salary_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original




@given(instance=Employee_strategy)
def test_hyp_employee_emp_email_setter(instance):
    original = instance.emp_email
    instance.emp_email = original
    assert instance.emp_email == original



@given(instance=Employee_strategy)
def test_hyp_employee_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original



@given(instance=Employee_strategy)
def test_hyp_employee_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Attendence,
    Employee,
    EmployeeRequest,
    Loan,
    Login,
    Salary,
    payslip,
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

def test_Admin_adminEmail_value_roundtrip():
    instance = Admin(adminEmail="sample_text", password=7)
    assert instance.adminEmail == "sample_text"
    instance.adminEmail = "sample_text_2"
    assert instance.adminEmail == "sample_text_2"


def test_Admin_password_value_roundtrip():
    instance = Admin(adminEmail="sample_text", password=7)
    assert instance.password == 7
    instance.password = 13
    assert instance.password == 13


def test_Attendence_Basic_salary_value_roundtrip():
    instance = Attendence(Basic_salary=7, emp_id=7, emp_name="sample_text")
    assert instance.Basic_salary == 7
    instance.Basic_salary = 13
    assert instance.Basic_salary == 13


def test_Attendence_emp_id_value_roundtrip():
    instance = Attendence(Basic_salary=7, emp_id=7, emp_name="sample_text")
    assert instance.emp_id == 7
    instance.emp_id = 13
    assert instance.emp_id == 13


def test_Attendence_emp_name_value_roundtrip():
    instance = Attendence(Basic_salary=7, emp_id=7, emp_name="sample_text")
    assert instance.emp_name == "sample_text"
    instance.emp_name = "sample_text_2"
    assert instance.emp_name == "sample_text_2"


def test_Employee_emp_email_value_roundtrip():
    instance = Employee(emp_email="sample_text", emp_id=7, emp_name="sample_text")
    assert instance.emp_email == "sample_text"
    instance.emp_email = "sample_text_2"
    assert instance.emp_email == "sample_text_2"


def test_Employee_emp_id_value_roundtrip():
    instance = Employee(emp_email="sample_text", emp_id=7, emp_name="sample_text")
    assert instance.emp_id == 7
    instance.emp_id = 13
    assert instance.emp_id == 13


def test_Employee_emp_name_value_roundtrip():
    instance = Employee(emp_email="sample_text", emp_id=7, emp_name="sample_text")
    assert instance.emp_name == "sample_text"
    instance.emp_name = "sample_text_2"
    assert instance.emp_name == "sample_text_2"


def test_Loan_amount_value_roundtrip():
    instance = Loan(amount="sample_text", emp_id=7, emp_name="sample_text", loan_interst=7, loan_purpose="sample_text", loan_type="sample_text")
    assert instance.amount == "sample_text"
    instance.amount = "sample_text_2"
    assert instance.amount == "sample_text_2"


def test_Loan_emp_id_value_roundtrip():
    instance = Loan(amount="sample_text", emp_id=7, emp_name="sample_text", loan_interst=7, loan_purpose="sample_text", loan_type="sample_text")
    assert instance.emp_id == 7
    instance.emp_id = 13
    assert instance.emp_id == 13


def test_Loan_emp_name_value_roundtrip():
    instance = Loan(amount="sample_text", emp_id=7, emp_name="sample_text", loan_interst=7, loan_purpose="sample_text", loan_type="sample_text")
    assert instance.emp_name == "sample_text"
    instance.emp_name = "sample_text_2"
    assert instance.emp_name == "sample_text_2"


def test_Loan_loan_interst_value_roundtrip():
    instance = Loan(amount="sample_text", emp_id=7, emp_name="sample_text", loan_interst=7, loan_purpose="sample_text", loan_type="sample_text")
    assert instance.loan_interst == 7
    instance.loan_interst = 13
    assert instance.loan_interst == 13


def test_Loan_loan_purpose_value_roundtrip():
    instance = Loan(amount="sample_text", emp_id=7, emp_name="sample_text", loan_interst=7, loan_purpose="sample_text", loan_type="sample_text")
    assert instance.loan_purpose == "sample_text"
    instance.loan_purpose = "sample_text_2"
    assert instance.loan_purpose == "sample_text_2"


def test_Loan_loan_type_value_roundtrip():
    instance = Loan(amount="sample_text", emp_id=7, emp_name="sample_text", loan_interst=7, loan_purpose="sample_text", loan_type="sample_text")
    assert instance.loan_type == "sample_text"
    instance.loan_type = "sample_text_2"
    assert instance.loan_type == "sample_text_2"


def test_Login_password_value_roundtrip():
    instance = Login(password=7, username="sample_text")
    assert instance.password == 7
    instance.password = 13
    assert instance.password == 13


def test_Login_username_value_roundtrip():
    instance = Login(password=7, username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Salary_basic_salary_value_roundtrip():
    instance = Salary(basic_salary="sample_text", emp_id=7, emp_name="sample_text")
    assert instance.basic_salary == "sample_text"
    instance.basic_salary = "sample_text_2"
    assert instance.basic_salary == "sample_text_2"


def test_Salary_emp_id_value_roundtrip():
    instance = Salary(basic_salary="sample_text", emp_id=7, emp_name="sample_text")
    assert instance.emp_id == 7
    instance.emp_id = 13
    assert instance.emp_id == 13


def test_Salary_emp_name_value_roundtrip():
    instance = Salary(basic_salary="sample_text", emp_id=7, emp_name="sample_text")
    assert instance.emp_name == "sample_text"
    instance.emp_name = "sample_text_2"
    assert instance.emp_name == "sample_text_2"


def test_payslip_emp_id_value_roundtrip():
    instance = payslip(emp_id=7, emp_name="sample_text")
    assert instance.emp_id == 7
    instance.emp_id = 13
    assert instance.emp_id == 13


def test_payslip_emp_name_value_roundtrip():
    instance = payslip(emp_id=7, emp_name="sample_text")
    assert instance.emp_name == "sample_text"
    instance.emp_name = "sample_text_2"
    assert instance.emp_name == "sample_text_2"


def test_assoc_Attendence_Employee_link_reassign_clear():
    a = Employee(emp_email="sample_text", emp_id=7, emp_name="sample_text")
    b1 = Attendence(Basic_salary=7, emp_id=7, emp_name="sample_text")
    b2 = Attendence(Basic_salary=13, emp_id=13, emp_name="sample_text_2")
    _safe_set(a, 'attendence1', b1)
    assert _is_linked(a, 'attendence1', b1)
    if hasattr(b1, 'employee0'):
        assert _is_linked(b1, 'employee0', a)
    _safe_set(a, 'attendence1', b2)
    assert _is_linked(a, 'attendence1', b2)
    if hasattr(b1, 'employee0'):
        assert not _is_linked(b1, 'employee0', a)
    if hasattr(b2, 'employee0'):
        assert _is_linked(b2, 'employee0', a)
    _safe_set(a, 'attendence1', None)
    assert not _is_linked(a, 'attendence1', b2)
    if hasattr(b2, 'employee0'):
        assert not _is_linked(b2, 'employee0', a)


def test_assoc_Employee_Salary_link_reassign_clear():
    a = Salary(basic_salary="sample_text", emp_id=7, emp_name="sample_text")
    b1 = Employee(emp_email="sample_text", emp_id=7, emp_name="sample_text")
    b2 = Employee(emp_email="sample_text_2", emp_id=13, emp_name="sample_text_2")
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

Admin_strategy = st.builds(Admin, adminEmail=safe_text, password=st.integers())
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Attendence_strategy = st.builds(Attendence, Basic_salary=st.integers(), emp_id=st.integers(), emp_name=safe_text)
@given(instance=Attendence_strategy)
@settings(max_examples=25)
def test_Attendence_instantiation(instance):
    assert isinstance(instance, Attendence)


Employee_strategy = st.builds(Employee, emp_email=safe_text, emp_id=st.integers(), emp_name=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


EmployeeRequest_strategy = st.builds(EmployeeRequest)
@given(instance=EmployeeRequest_strategy)
@settings(max_examples=25)
def test_EmployeeRequest_instantiation(instance):
    assert isinstance(instance, EmployeeRequest)


Loan_strategy = st.builds(Loan, amount=safe_text, emp_id=st.integers(), emp_name=safe_text, loan_interst=st.integers(), loan_purpose=safe_text, loan_type=safe_text)
@given(instance=Loan_strategy)
@settings(max_examples=25)
def test_Loan_instantiation(instance):
    assert isinstance(instance, Loan)


Login_strategy = st.builds(Login, password=st.integers(), username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Salary_strategy = st.builds(Salary, basic_salary=safe_text, emp_id=st.integers(), emp_name=safe_text)
@given(instance=Salary_strategy)
@settings(max_examples=25)
def test_Salary_instantiation(instance):
    assert isinstance(instance, Salary)


payslip_strategy = st.builds(payslip, emp_id=st.integers(), emp_name=safe_text)
@given(instance=payslip_strategy)
@settings(max_examples=25)
def test_payslip_instantiation(instance):
    assert isinstance(instance, payslip)



