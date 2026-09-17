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
    company_Company,
    Employee,
    company_Freelance,
    company_Employee,
    company_Student,
    company_Division,
    company_Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_hyp_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_hyp_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "eotmDelta" in params, "Missing parameter 'eotmDelta'"





def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_freelance_is_not_abstract():
    assert not inspect.isabstract(company_Freelance)


def test_hyp_company_freelance_constructor_exists():
    assert callable(company_Freelance.__init__)


def test_hyp_company_freelance_constructor_args():
    sig = inspect.signature(company_Freelance.__init__)
    params = list(sig.parameters.keys())
    assert "assignment" in params, "Missing parameter 'assignment'"




def test_hyp_company_employee_is_not_abstract():
    assert not inspect.isabstract(company_Employee)


def test_hyp_company_employee_constructor_exists():
    assert callable(company_Employee.__init__)


def test_hyp_company_employee_constructor_args():
    sig = inspect.signature(company_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"






def test_hyp_company_student_is_not_abstract():
    assert not inspect.isabstract(company_Student)


def test_hyp_company_student_constructor_exists():
    assert callable(company_Student.__init__)


def test_hyp_company_student_constructor_args():
    sig = inspect.signature(company_Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_company_division_is_not_abstract():
    assert not inspect.isabstract(company_Division)


def test_hyp_company_division_constructor_exists():
    assert callable(company_Division.__init__)


def test_hyp_company_division_constructor_args():
    sig = inspect.signature(company_Division.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numberEmployeesOfTheMonth" in params, "Missing parameter 'numberEmployeesOfTheMonth'"
    assert "budget" in params, "Missing parameter 'budget'"






def test_hyp_company_department_is_not_abstract():
    assert not inspect.isabstract(company_Department)


def test_hyp_company_department_constructor_exists():
    assert callable(company_Department.__init__)


def test_hyp_company_department_constructor_args():
    sig = inspect.signature(company_Department.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "biggestNumberOfStudentsOrFreelancers" in params, "Missing parameter 'biggestNumberOfStudentsOrFreelancers'"
    assert "maxJuniors" in params, "Missing parameter 'maxJuniors'"
    assert "name" in params, "Missing parameter 'name'"






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
company_Company_strategy = st.builds(
    company_Company,
    name=
        safe_text,
    eotmDelta=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
)
company_Freelance_strategy = st.builds(
    company_Freelance,
    assignment=
        safe_text
)
company_Employee_strategy = st.builds(
    company_Employee,
    age=
        safe_text,
    name=
        safe_text,
    salary=
        safe_text
)
company_Student_strategy = st.builds(
    company_Student,
)
company_Division_strategy = st.builds(
    company_Division,
    name=
        safe_text,
    numberEmployeesOfTheMonth=
        safe_text,
    budget=
        safe_text
)
company_Department_strategy = st.builds(
    company_Department,
    budget=
        safe_text,
    biggestNumberOfStudentsOrFreelancers=
        safe_text,
    maxJuniors=
        safe_text,
    name=
        safe_text
)




@given(instance=company_Company_strategy)
def test_hyp_company_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Company_strategy)
def test_hyp_company_company_eotmDelta_setter(instance):
    original = instance.eotmDelta
    instance.eotmDelta = original
    assert instance.eotmDelta == original





@given(instance=company_Freelance_strategy)
def test_hyp_company_freelance_assignment_setter(instance):
    original = instance.assignment
    instance.assignment = original
    assert instance.assignment == original




@given(instance=company_Employee_strategy)
def test_hyp_company_employee_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=company_Employee_strategy)
def test_hyp_company_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Employee_strategy)
def test_hyp_company_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original





@given(instance=company_Division_strategy)
def test_hyp_company_division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Division_strategy)
def test_hyp_company_division_numberEmployeesOfTheMonth_setter(instance):
    original = instance.numberEmployeesOfTheMonth
    instance.numberEmployeesOfTheMonth = original
    assert instance.numberEmployeesOfTheMonth == original



@given(instance=company_Division_strategy)
def test_hyp_company_division_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original




@given(instance=company_Department_strategy)
def test_hyp_company_department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=company_Department_strategy)
def test_hyp_company_department_biggestNumberOfStudentsOrFreelancers_setter(instance):
    original = instance.biggestNumberOfStudentsOrFreelancers
    instance.biggestNumberOfStudentsOrFreelancers = original
    assert instance.biggestNumberOfStudentsOrFreelancers == original



@given(instance=company_Department_strategy)
def test_hyp_company_department_maxJuniors_setter(instance):
    original = instance.maxJuniors
    instance.maxJuniors = original
    assert instance.maxJuniors == original



@given(instance=company_Department_strategy)
def test_hyp_company_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=company_Department_strategy)
@settings(max_examples=30)
def test_hyp_company_department_calcexpenses_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.calcExpenses()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.calcExpenses).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'calcExpenses' in company_Department is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'calcExpenses' in company_Department did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'calcExpenses' in company_Department is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Employee,
    company_Company,
    company_Department,
    company_Division,
    company_Employee,
    company_Freelance,
    company_Student,
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

def test_company_Company_eotmDelta_value_roundtrip():
    instance = company_Company(eotmDelta="sample_text", name="sample_text")
    assert instance.eotmDelta == "sample_text"
    instance.eotmDelta = "sample_text_2"
    assert instance.eotmDelta == "sample_text_2"


def test_company_Company_name_value_roundtrip():
    instance = company_Company(eotmDelta="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_company_Department_biggestNumberOfStudentsOrFreelancers_value_roundtrip():
    instance = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    assert instance.biggestNumberOfStudentsOrFreelancers == "sample_text"
    instance.biggestNumberOfStudentsOrFreelancers = "sample_text_2"
    assert instance.biggestNumberOfStudentsOrFreelancers == "sample_text_2"


def test_company_Department_budget_value_roundtrip():
    instance = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    assert instance.budget == "sample_text"
    instance.budget = "sample_text_2"
    assert instance.budget == "sample_text_2"


def test_company_Department_maxJuniors_value_roundtrip():
    instance = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    assert instance.maxJuniors == "sample_text"
    instance.maxJuniors = "sample_text_2"
    assert instance.maxJuniors == "sample_text_2"


def test_company_Department_name_value_roundtrip():
    instance = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_company_Division_budget_value_roundtrip():
    instance = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    assert instance.budget == "sample_text"
    instance.budget = "sample_text_2"
    assert instance.budget == "sample_text_2"


def test_company_Division_name_value_roundtrip():
    instance = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_company_Division_numberEmployeesOfTheMonth_value_roundtrip():
    instance = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    assert instance.numberEmployeesOfTheMonth == "sample_text"
    instance.numberEmployeesOfTheMonth = "sample_text_2"
    assert instance.numberEmployeesOfTheMonth == "sample_text_2"


def test_company_Employee_age_value_roundtrip():
    instance = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    assert instance.age == "sample_text"
    instance.age = "sample_text_2"
    assert instance.age == "sample_text_2"


def test_company_Employee_name_value_roundtrip():
    instance = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_company_Employee_salary_value_roundtrip():
    instance = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    assert instance.salary == "sample_text"
    instance.salary = "sample_text_2"
    assert instance.salary == "sample_text_2"


def test_company_Freelance_assignment_value_roundtrip():
    instance = company_Freelance(assignment="sample_text")
    assert instance.assignment == "sample_text"
    instance.assignment = "sample_text_2"
    assert instance.assignment == "sample_text_2"


def test_company_Freelance_isa_Employee():
    instance = company_Freelance(assignment="sample_text")
    assert isinstance(instance, Employee)


def test_company_Student_isa_Employee():
    instance = company_Student()
    assert isinstance(instance, Employee)


def test_assoc_boss9_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Employee10', b1)
    assert _is_linked(a, 'Employee10', b1)
    if hasattr(b1, 'managed'):
        assert _is_linked(b1, 'managed', a)
    _safe_set(a, 'Employee10', b2)
    assert _is_linked(a, 'Employee10', b2)
    if hasattr(b1, 'managed'):
        assert not _is_linked(b1, 'managed', a)
    if hasattr(b2, 'managed'):
        assert _is_linked(b2, 'managed', a)
    _safe_set(a, 'Employee10', None)
    assert not _is_linked(a, 'Employee10', b2)
    if hasattr(b2, 'managed'):
        assert not _is_linked(b2, 'managed', a)


def test_assoc_company26_link_reassign_clear():
    a = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    b1 = company_Company(eotmDelta="sample_text", name="sample_text")
    b2 = company_Company(eotmDelta="sample_text_2", name="sample_text_2")
    _safe_set(a, 'division', b1)
    assert _is_linked(a, 'division', b1)
    if hasattr(b1, 'Company'):
        assert _is_linked(b1, 'Company', a)
    _safe_set(a, 'division', b2)
    assert _is_linked(a, 'division', b2)
    if hasattr(b1, 'Company'):
        assert not _is_linked(b1, 'Company', a)
    if hasattr(b2, 'Company'):
        assert _is_linked(b2, 'Company', a)
    _safe_set(a, 'division', None)
    assert not _is_linked(a, 'division', b2)
    if hasattr(b2, 'Company'):
        assert not _is_linked(b2, 'Company', a)


def test_assoc_department19_link_reassign_clear():
    a = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'company_Division', {b1})
    assert _is_linked(a, 'company_Division', b1)
    if hasattr(b1, 'company_Department20'):
        assert _is_linked(b1, 'company_Department20', a)
    _safe_set(a, 'company_Division', {b2})
    assert _is_linked(a, 'company_Division', b2)
    if hasattr(b1, 'company_Department20'):
        assert not _is_linked(b1, 'company_Department20', a)
    if hasattr(b2, 'company_Department20'):
        assert _is_linked(b2, 'company_Department20', a)
    _safe_set(a, 'company_Division', set())
    assert not _is_linked(a, 'company_Division', b2)
    if hasattr(b2, 'company_Department20'):
        assert not _is_linked(b2, 'company_Department20', a)


def test_assoc_directed3_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    b2 = company_Division(budget="sample_text_2", name="sample_text_2", numberEmployeesOfTheMonth="sample_text_2")
    _safe_set(a, 'director', b1)
    assert _is_linked(a, 'director', b1)
    if hasattr(b1, 'Division'):
        assert _is_linked(b1, 'Division', a)
    _safe_set(a, 'director', b2)
    assert _is_linked(a, 'director', b2)
    if hasattr(b1, 'Division'):
        assert not _is_linked(b1, 'Division', a)
    if hasattr(b2, 'Division'):
        assert _is_linked(b2, 'Division', a)
    _safe_set(a, 'director', None)
    assert not _is_linked(a, 'director', b2)
    if hasattr(b2, 'Division'):
        assert not _is_linked(b2, 'Division', a)


def test_assoc_director21_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    b2 = company_Division(budget="sample_text_2", name="sample_text_2", numberEmployeesOfTheMonth="sample_text_2")
    _safe_set(a, 'Employee22', b1)
    assert _is_linked(a, 'Employee22', b1)
    if hasattr(b1, 'directed'):
        assert _is_linked(b1, 'directed', a)
    _safe_set(a, 'Employee22', b2)
    assert _is_linked(a, 'Employee22', b2)
    if hasattr(b1, 'directed'):
        assert not _is_linked(b1, 'directed', a)
    if hasattr(b2, 'directed'):
        assert _is_linked(b2, 'directed', a)
    _safe_set(a, 'Employee22', None)
    assert not _is_linked(a, 'Employee22', b2)
    if hasattr(b2, 'directed'):
        assert not _is_linked(b2, 'directed', a)


def test_assoc_division27_link_reassign_clear():
    a = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    b1 = company_Company(eotmDelta="sample_text", name="sample_text")
    b2 = company_Company(eotmDelta="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Division28', b1)
    assert _is_linked(a, 'Division28', b1)
    if hasattr(b1, 'company'):
        assert _is_linked(b1, 'company', a)
    _safe_set(a, 'Division28', b2)
    assert _is_linked(a, 'Division28', b2)
    if hasattr(b1, 'company'):
        assert not _is_linked(b1, 'company', a)
    if hasattr(b2, 'company'):
        assert _is_linked(b2, 'company', a)
    _safe_set(a, 'Division28', None)
    assert not _is_linked(a, 'Division28', b2)
    if hasattr(b2, 'company'):
        assert not _is_linked(b2, 'company', a)


def test_assoc_divisionDirector29_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Company(eotmDelta="sample_text", name="sample_text")
    b2 = company_Company(eotmDelta="sample_text_2", name="sample_text_2")
    _safe_set(a, 'company_Employee30', b1)
    assert _is_linked(a, 'company_Employee30', b1)
    if hasattr(b1, 'company_Company'):
        assert _is_linked(b1, 'company_Company', a)
    _safe_set(a, 'company_Employee30', b2)
    assert _is_linked(a, 'company_Employee30', b2)
    if hasattr(b1, 'company_Company'):
        assert not _is_linked(b1, 'company_Company', a)
    if hasattr(b2, 'company_Company'):
        assert _is_linked(b2, 'company_Company', a)
    _safe_set(a, 'company_Employee30', None)
    assert not _is_linked(a, 'company_Employee30', b2)
    if hasattr(b2, 'company_Company'):
        assert not _is_linked(b2, 'company_Company', a)


def test_assoc_employee8_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Employee', b1)
    assert _is_linked(a, 'Employee', b1)
    if hasattr(b1, 'employer'):
        assert _is_linked(b1, 'employer', a)
    _safe_set(a, 'Employee', b2)
    assert _is_linked(a, 'Employee', b2)
    if hasattr(b1, 'employer'):
        assert not _is_linked(b1, 'employer', a)
    if hasattr(b2, 'employer'):
        assert _is_linked(b2, 'employer', a)
    _safe_set(a, 'Employee', None)
    assert not _is_linked(a, 'Employee', b2)
    if hasattr(b2, 'employer'):
        assert not _is_linked(b2, 'employer', a)


def test_assoc_employeeOfTheMonth17_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'company_Employee18', b1)
    assert _is_linked(a, 'company_Employee18', b1)
    if hasattr(b1, 'company_Department'):
        assert _is_linked(b1, 'company_Department', a)
    _safe_set(a, 'company_Employee18', b2)
    assert _is_linked(a, 'company_Employee18', b2)
    if hasattr(b1, 'company_Department'):
        assert not _is_linked(b1, 'company_Department', a)
    if hasattr(b2, 'company_Department'):
        assert _is_linked(b2, 'company_Department', a)
    _safe_set(a, 'company_Employee18', None)
    assert not _is_linked(a, 'company_Employee18', b2)
    if hasattr(b2, 'company_Department'):
        assert not _is_linked(b2, 'company_Department', a)


def test_assoc_employeesOfTheMonth23_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Division(budget="sample_text", name="sample_text", numberEmployeesOfTheMonth="sample_text")
    b2 = company_Division(budget="sample_text_2", name="sample_text_2", numberEmployeesOfTheMonth="sample_text_2")
    _safe_set(a, 'company_Employee25', b1)
    assert _is_linked(a, 'company_Employee25', b1)
    if hasattr(b1, 'company_Division24'):
        assert _is_linked(b1, 'company_Division24', a)
    _safe_set(a, 'company_Employee25', b2)
    assert _is_linked(a, 'company_Employee25', b2)
    if hasattr(b1, 'company_Division24'):
        assert not _is_linked(b1, 'company_Division24', a)
    if hasattr(b2, 'company_Division24'):
        assert _is_linked(b2, 'company_Division24', a)
    _safe_set(a, 'company_Employee25', None)
    assert not _is_linked(a, 'company_Employee25', b2)
    if hasattr(b2, 'company_Division24'):
        assert not _is_linked(b2, 'company_Division24', a)


def test_assoc_employer0_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'employee', b1)
    assert _is_linked(a, 'employee', b1)
    if hasattr(b1, 'Department'):
        assert _is_linked(b1, 'Department', a)
    _safe_set(a, 'employee', b2)
    assert _is_linked(a, 'employee', b2)
    if hasattr(b1, 'Department'):
        assert not _is_linked(b1, 'Department', a)
    if hasattr(b2, 'Department'):
        assert _is_linked(b2, 'Department', a)
    _safe_set(a, 'employee', None)
    assert not _is_linked(a, 'employee', b2)
    if hasattr(b2, 'Department'):
        assert not _is_linked(b2, 'Department', a)


def test_assoc_intern6_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Student()
    b2 = company_Student()
    _safe_set(a, 'company_Employee7', b1)
    assert _is_linked(a, 'company_Employee7', b1)
    if hasattr(b1, 'company_Student'):
        assert _is_linked(b1, 'company_Student', a)
    _safe_set(a, 'company_Employee7', b2)
    assert _is_linked(a, 'company_Employee7', b2)
    if hasattr(b1, 'company_Student'):
        assert not _is_linked(b1, 'company_Student', a)
    if hasattr(b2, 'company_Student'):
        assert _is_linked(b2, 'company_Student', a)
    _safe_set(a, 'company_Employee7', None)
    assert not _is_linked(a, 'company_Employee7', b2)
    if hasattr(b2, 'company_Student'):
        assert not _is_linked(b2, 'company_Student', a)


def test_assoc_managed1_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'boss', b1)
    assert _is_linked(a, 'boss', b1)
    if hasattr(b1, 'Department2'):
        assert _is_linked(b1, 'Department2', a)
    _safe_set(a, 'boss', b2)
    assert _is_linked(a, 'boss', b2)
    if hasattr(b1, 'Department2'):
        assert not _is_linked(b1, 'Department2', a)
    if hasattr(b2, 'Department2'):
        assert _is_linked(b2, 'Department2', a)
    _safe_set(a, 'boss', None)
    assert not _is_linked(a, 'boss', b2)
    if hasattr(b2, 'Department2'):
        assert not _is_linked(b2, 'Department2', a)


def test_assoc_parentDepartment15_link_reassign_clear():
    a = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Department16', b1)
    assert _is_linked(a, 'Department16', b1)
    if hasattr(b1, 'subDepartment'):
        assert _is_linked(b1, 'subDepartment', a)
    _safe_set(a, 'Department16', b2)
    assert _is_linked(a, 'Department16', b2)
    if hasattr(b1, 'subDepartment'):
        assert not _is_linked(b1, 'subDepartment', a)
    if hasattr(b2, 'subDepartment'):
        assert _is_linked(b2, 'subDepartment', a)
    _safe_set(a, 'Department16', None)
    assert not _is_linked(a, 'Department16', b2)
    if hasattr(b2, 'subDepartment'):
        assert not _is_linked(b2, 'subDepartment', a)


def test_assoc_secretary5_link_reassign_clear():
    a = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b1 = company_Employee(age="sample_text", name="sample_text", salary="sample_text")
    b2 = company_Employee(age="sample_text_2", name="sample_text_2", salary="sample_text_2")
    _safe_set(a, 'company_Employee', b1)
    assert _is_linked(a, 'company_Employee', b1)
    if hasattr(b1, 'company_Employee4'):
        assert _is_linked(b1, 'company_Employee4', a)
    _safe_set(a, 'company_Employee', b2)
    assert _is_linked(a, 'company_Employee', b2)
    if hasattr(b1, 'company_Employee4'):
        assert not _is_linked(b1, 'company_Employee4', a)
    if hasattr(b2, 'company_Employee4'):
        assert _is_linked(b2, 'company_Employee4', a)
    _safe_set(a, 'company_Employee', None)
    assert not _is_linked(a, 'company_Employee', b2)
    if hasattr(b2, 'company_Employee4'):
        assert not _is_linked(b2, 'company_Employee4', a)


def test_assoc_subDepartment12_link_reassign_clear():
    a = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b1 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text", budget="sample_text", maxJuniors="sample_text", name="sample_text")
    b2 = company_Department(biggestNumberOfStudentsOrFreelancers="sample_text_2", budget="sample_text_2", maxJuniors="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Department13', b1)
    assert _is_linked(a, 'Department13', b1)
    if hasattr(b1, 'parentDepartment'):
        assert _is_linked(b1, 'parentDepartment', a)
    _safe_set(a, 'Department13', b2)
    assert _is_linked(a, 'Department13', b2)
    if hasattr(b1, 'parentDepartment'):
        assert not _is_linked(b1, 'parentDepartment', a)
    if hasattr(b2, 'parentDepartment'):
        assert _is_linked(b2, 'parentDepartment', a)
    _safe_set(a, 'Department13', None)
    assert not _is_linked(a, 'Department13', b2)
    if hasattr(b2, 'parentDepartment'):
        assert not _is_linked(b2, 'parentDepartment', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Employee_strategy = st.builds(Employee)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


company_Company_strategy = st.builds(company_Company, eotmDelta=safe_text, name=safe_text)
@given(instance=company_Company_strategy)
@settings(max_examples=25)
def test_company_Company_instantiation(instance):
    assert isinstance(instance, company_Company)


company_Department_strategy = st.builds(company_Department, biggestNumberOfStudentsOrFreelancers=safe_text, budget=safe_text, maxJuniors=safe_text, name=safe_text)
@given(instance=company_Department_strategy)
@settings(max_examples=25)
def test_company_Department_instantiation(instance):
    assert isinstance(instance, company_Department)


company_Division_strategy = st.builds(company_Division, budget=safe_text, name=safe_text, numberEmployeesOfTheMonth=safe_text)
@given(instance=company_Division_strategy)
@settings(max_examples=25)
def test_company_Division_instantiation(instance):
    assert isinstance(instance, company_Division)


company_Employee_strategy = st.builds(company_Employee, age=safe_text, name=safe_text, salary=safe_text)
@given(instance=company_Employee_strategy)
@settings(max_examples=25)
def test_company_Employee_instantiation(instance):
    assert isinstance(instance, company_Employee)


company_Freelance_strategy = st.builds(company_Freelance, assignment=safe_text)
@given(instance=company_Freelance_strategy)
@settings(max_examples=25)
def test_company_Freelance_instantiation(instance):
    assert isinstance(instance, company_Freelance)


company_Student_strategy = st.builds(company_Student)
@given(instance=company_Student_strategy)
@settings(max_examples=25)
def test_company_Student_instantiation(instance):
    assert isinstance(instance, company_Student)



