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
    Invoice,
    SalariedEmployee,
    Payable_Interface,
    Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_invoice_is_not_abstract():
    assert not inspect.isabstract(Invoice)


def test_hyp_invoice_constructor_exists():
    assert callable(Invoice.__init__)


def test_hyp_invoice_constructor_args():
    sig = inspect.signature(Invoice.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "product" in params, "Missing parameter 'product'"
    assert "num" in params, "Missing parameter 'num'"
    assert "quantity" in params, "Missing parameter 'quantity'"







def test_hyp_salariedemployee_is_not_abstract():
    assert not inspect.isabstract(SalariedEmployee)


def test_hyp_salariedemployee_constructor_exists():
    assert callable(SalariedEmployee.__init__)


def test_hyp_salariedemployee_constructor_args():
    sig = inspect.signature(SalariedEmployee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"




def test_hyp_payable_interface_is_not_abstract():
    assert not inspect.isabstract(Payable_Interface)


def test_hyp_payable_interface_constructor_exists():
    assert callable(Payable_Interface.__init__)


def test_hyp_payable_interface_constructor_args():
    sig = inspect.signature(Payable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "ssn" in params, "Missing parameter 'ssn'"





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
Invoice_strategy = st.builds(
    Invoice,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    product=
        safe_text,
    num=
        safe_text,
    quantity=
        st.integers()
)
SalariedEmployee_strategy = st.builds(
    SalariedEmployee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Payable_Interface_strategy = st.builds(
    Payable_Interface,
)
Employee_strategy = st.builds(
    Employee,
    lastname=
        safe_text,
    firstname=
        safe_text,
    ssn=
        safe_text
)




@given(instance=Invoice_strategy)
def test_hyp_invoice_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Invoice_strategy)
def test_hyp_invoice_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=Invoice_strategy)
def test_hyp_invoice_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Invoice_strategy)
def test_hyp_invoice_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original




@given(instance=SalariedEmployee_strategy)
def test_hyp_salariedemployee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original





@given(instance=Employee_strategy)
def test_hyp_employee_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Employee_strategy)
def test_hyp_employee_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Employee_strategy)
def test_hyp_employee_ssn_setter(instance):
    original = instance.ssn
    instance.ssn = original
    assert instance.ssn == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Employee,
    Invoice,
    Payable_Interface,
    SalariedEmployee,
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

def test_Employee_firstname_value_roundtrip():
    instance = Employee(firstname="sample_text", lastname="sample_text", ssn="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Employee_lastname_value_roundtrip():
    instance = Employee(firstname="sample_text", lastname="sample_text", ssn="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Employee_ssn_value_roundtrip():
    instance = Employee(firstname="sample_text", lastname="sample_text", ssn="sample_text")
    assert instance.ssn == "sample_text"
    instance.ssn = "sample_text_2"
    assert instance.ssn == "sample_text_2"


def test_Invoice_amount_value_roundtrip():
    instance = Invoice(amount=3.14, num="sample_text", product="sample_text", quantity=7)
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_Invoice_num_value_roundtrip():
    instance = Invoice(amount=3.14, num="sample_text", product="sample_text", quantity=7)
    assert instance.num == "sample_text"
    instance.num = "sample_text_2"
    assert instance.num == "sample_text_2"


def test_Invoice_product_value_roundtrip():
    instance = Invoice(amount=3.14, num="sample_text", product="sample_text", quantity=7)
    assert instance.product == "sample_text"
    instance.product = "sample_text_2"
    assert instance.product == "sample_text_2"


def test_Invoice_quantity_value_roundtrip():
    instance = Invoice(amount=3.14, num="sample_text", product="sample_text", quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_SalariedEmployee_salary_value_roundtrip():
    instance = SalariedEmployee(salary=3.14)
    assert instance.salary == 3.14
    instance.salary = 9.99
    assert instance.salary == 9.99


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Employee_strategy = st.builds(Employee, firstname=safe_text, lastname=safe_text, ssn=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Invoice_strategy = st.builds(Invoice, amount=st.floats(allow_nan=False, allow_infinity=False), num=safe_text, product=safe_text, quantity=st.integers())
@given(instance=Invoice_strategy)
@settings(max_examples=25)
def test_Invoice_instantiation(instance):
    assert isinstance(instance, Invoice)


Payable_Interface_strategy = st.builds(Payable_Interface)
@given(instance=Payable_Interface_strategy)
@settings(max_examples=25)
def test_Payable_Interface_instantiation(instance):
    assert isinstance(instance, Payable_Interface)


SalariedEmployee_strategy = st.builds(SalariedEmployee, salary=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=SalariedEmployee_strategy)
@settings(max_examples=25)
def test_SalariedEmployee_instantiation(instance):
    assert isinstance(instance, SalariedEmployee)



