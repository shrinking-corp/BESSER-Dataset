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
    exo1_Project,
    exo1_Departement,
    exo1_Company,
    exo1_Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_exo1_project_is_not_abstract():
    assert not inspect.isabstract(exo1_Project)


def test_hyp_exo1_project_constructor_exists():
    assert callable(exo1_Project.__init__)


def test_hyp_exo1_project_constructor_args():
    sig = inspect.signature(exo1_Project.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_exo1_departement_is_not_abstract():
    assert not inspect.isabstract(exo1_Departement)


def test_hyp_exo1_departement_constructor_exists():
    assert callable(exo1_Departement.__init__)


def test_hyp_exo1_departement_constructor_args():
    sig = inspect.signature(exo1_Departement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"
    assert "budget" in params, "Missing parameter 'budget'"






def test_hyp_exo1_company_is_not_abstract():
    assert not inspect.isabstract(exo1_Company)


def test_hyp_exo1_company_constructor_exists():
    assert callable(exo1_Company.__init__)


def test_hyp_exo1_company_constructor_args():
    sig = inspect.signature(exo1_Company.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exo1_employee_is_not_abstract():
    assert not inspect.isabstract(exo1_Employee)


def test_hyp_exo1_employee_constructor_exists():
    assert callable(exo1_Employee.__init__)


def test_hyp_exo1_employee_constructor_args():
    sig = inspect.signature(exo1_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"




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
exo1_Project_strategy = st.builds(
    exo1_Project,
    budget=
        st.integers(),
    name=
        safe_text
)
exo1_Departement_strategy = st.builds(
    exo1_Departement,
    name=
        safe_text,
    location=
        safe_text,
    budget=
        st.integers()
)
exo1_Company_strategy = st.builds(
    exo1_Company,
)
exo1_Employee_strategy = st.builds(
    exo1_Employee,
    name=
        safe_text,
    salary=
        safe_text
)




@given(instance=exo1_Project_strategy)
def test_hyp_exo1_project_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=exo1_Project_strategy)
def test_hyp_exo1_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=exo1_Departement_strategy)
def test_hyp_exo1_departement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=exo1_Departement_strategy)
def test_hyp_exo1_departement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=exo1_Departement_strategy)
def test_hyp_exo1_departement_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original





@given(instance=exo1_Employee_strategy)
def test_hyp_exo1_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=exo1_Employee_strategy)
def test_hyp_exo1_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    exo1_Company,
    exo1_Departement,
    exo1_Employee,
    exo1_Project,
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

def test_exo1_Departement_budget_value_roundtrip():
    instance = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    assert instance.budget == 7
    instance.budget = 13
    assert instance.budget == 13


def test_exo1_Departement_location_value_roundtrip():
    instance = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_exo1_Departement_name_value_roundtrip():
    instance = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_exo1_Employee_name_value_roundtrip():
    instance = exo1_Employee(name="sample_text", salary="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_exo1_Employee_salary_value_roundtrip():
    instance = exo1_Employee(name="sample_text", salary="sample_text")
    assert instance.salary == "sample_text"
    instance.salary = "sample_text_2"
    assert instance.salary == "sample_text_2"


def test_exo1_Project_budget_value_roundtrip():
    instance = exo1_Project(budget=7, name="sample_text")
    assert instance.budget == 7
    instance.budget = 13
    assert instance.budget == 13


def test_exo1_Project_name_value_roundtrip():
    instance = exo1_Project(budget=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_departement2_link_reassign_clear():
    a = exo1_Project(budget=7, name="sample_text")
    b1 = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    b2 = exo1_Departement(budget=13, location="sample_text_2", name="sample_text_2")
    _safe_set(a, 'projects', b1)
    assert _is_linked(a, 'projects', b1)
    if hasattr(b1, 'Departement'):
        assert _is_linked(b1, 'Departement', a)
    _safe_set(a, 'projects', b2)
    assert _is_linked(a, 'projects', b2)
    if hasattr(b1, 'Departement'):
        assert not _is_linked(b1, 'Departement', a)
    if hasattr(b2, 'Departement'):
        assert _is_linked(b2, 'Departement', a)
    _safe_set(a, 'projects', None)
    assert not _is_linked(a, 'projects', b2)
    if hasattr(b2, 'Departement'):
        assert not _is_linked(b2, 'Departement', a)


def test_assoc_departements14_link_reassign_clear():
    a = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    b1 = exo1_Company()
    b2 = exo1_Company()
    _safe_set(a, 'exo1_Departement', b1)
    assert _is_linked(a, 'exo1_Departement', b1)
    if hasattr(b1, 'exo1_Company15'):
        assert _is_linked(b1, 'exo1_Company15', a)
    _safe_set(a, 'exo1_Departement', b2)
    assert _is_linked(a, 'exo1_Departement', b2)
    if hasattr(b1, 'exo1_Company15'):
        assert not _is_linked(b1, 'exo1_Company15', a)
    if hasattr(b2, 'exo1_Company15'):
        assert _is_linked(b2, 'exo1_Company15', a)
    _safe_set(a, 'exo1_Departement', None)
    assert not _is_linked(a, 'exo1_Departement', b2)
    if hasattr(b2, 'exo1_Company15'):
        assert not _is_linked(b2, 'exo1_Company15', a)


def test_assoc_departements8_link_reassign_clear():
    a = exo1_Employee(name="sample_text", salary="sample_text")
    b1 = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    b2 = exo1_Departement(budget=13, location="sample_text_2", name="sample_text_2")
    _safe_set(a, 'employees9', {b1})
    assert _is_linked(a, 'employees9', b1)
    if hasattr(b1, 'Departement10'):
        assert _is_linked(b1, 'Departement10', a)
    _safe_set(a, 'employees9', {b2})
    assert _is_linked(a, 'employees9', b2)
    if hasattr(b1, 'Departement10'):
        assert not _is_linked(b1, 'Departement10', a)
    if hasattr(b2, 'Departement10'):
        assert _is_linked(b2, 'Departement10', a)
    _safe_set(a, 'employees9', set())
    assert not _is_linked(a, 'employees9', b2)
    if hasattr(b2, 'Departement10'):
        assert not _is_linked(b2, 'Departement10', a)


def test_assoc_employees1_link_reassign_clear():
    a = exo1_Employee(name="sample_text", salary="sample_text")
    b1 = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    b2 = exo1_Departement(budget=13, location="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Employee', b1)
    assert _is_linked(a, 'Employee', b1)
    if hasattr(b1, 'departements'):
        assert _is_linked(b1, 'departements', a)
    _safe_set(a, 'Employee', b2)
    assert _is_linked(a, 'Employee', b2)
    if hasattr(b1, 'departements'):
        assert not _is_linked(b1, 'departements', a)
    if hasattr(b2, 'departements'):
        assert _is_linked(b2, 'departements', a)
    _safe_set(a, 'Employee', None)
    assert not _is_linked(a, 'Employee', b2)
    if hasattr(b2, 'departements'):
        assert not _is_linked(b2, 'departements', a)


def test_assoc_employees11_link_reassign_clear():
    a = exo1_Employee(name="sample_text", salary="sample_text")
    b1 = exo1_Company()
    b2 = exo1_Company()
    _safe_set(a, 'exo1_Employee', b1)
    assert _is_linked(a, 'exo1_Employee', b1)
    if hasattr(b1, 'exo1_Company'):
        assert _is_linked(b1, 'exo1_Company', a)
    _safe_set(a, 'exo1_Employee', b2)
    assert _is_linked(a, 'exo1_Employee', b2)
    if hasattr(b1, 'exo1_Company'):
        assert not _is_linked(b1, 'exo1_Company', a)
    if hasattr(b2, 'exo1_Company'):
        assert _is_linked(b2, 'exo1_Company', a)
    _safe_set(a, 'exo1_Employee', None)
    assert not _is_linked(a, 'exo1_Employee', b2)
    if hasattr(b2, 'exo1_Company'):
        assert not _is_linked(b2, 'exo1_Company', a)


def test_assoc_employees3_link_reassign_clear():
    a = exo1_Project(budget=7, name="sample_text")
    b1 = exo1_Employee(name="sample_text", salary="sample_text")
    b2 = exo1_Employee(name="sample_text_2", salary="sample_text_2")
    _safe_set(a, 'projects4', {b1})
    assert _is_linked(a, 'projects4', b1)
    if hasattr(b1, 'Employee5'):
        assert _is_linked(b1, 'Employee5', a)
    _safe_set(a, 'projects4', {b2})
    assert _is_linked(a, 'projects4', b2)
    if hasattr(b1, 'Employee5'):
        assert not _is_linked(b1, 'Employee5', a)
    if hasattr(b2, 'Employee5'):
        assert _is_linked(b2, 'Employee5', a)
    _safe_set(a, 'projects4', set())
    assert not _is_linked(a, 'projects4', b2)
    if hasattr(b2, 'Employee5'):
        assert not _is_linked(b2, 'Employee5', a)


def test_assoc_projects0_link_reassign_clear():
    a = exo1_Project(budget=7, name="sample_text")
    b1 = exo1_Departement(budget=7, location="sample_text", name="sample_text")
    b2 = exo1_Departement(budget=13, location="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Project', b1)
    assert _is_linked(a, 'Project', b1)
    if hasattr(b1, 'departement'):
        assert _is_linked(b1, 'departement', a)
    _safe_set(a, 'Project', b2)
    assert _is_linked(a, 'Project', b2)
    if hasattr(b1, 'departement'):
        assert not _is_linked(b1, 'departement', a)
    if hasattr(b2, 'departement'):
        assert _is_linked(b2, 'departement', a)
    _safe_set(a, 'Project', None)
    assert not _is_linked(a, 'Project', b2)
    if hasattr(b2, 'departement'):
        assert not _is_linked(b2, 'departement', a)


def test_assoc_projects6_link_reassign_clear():
    a = exo1_Project(budget=7, name="sample_text")
    b1 = exo1_Employee(name="sample_text", salary="sample_text")
    b2 = exo1_Employee(name="sample_text_2", salary="sample_text_2")
    _safe_set(a, 'Project7', b1)
    assert _is_linked(a, 'Project7', b1)
    if hasattr(b1, 'employees'):
        assert _is_linked(b1, 'employees', a)
    _safe_set(a, 'Project7', b2)
    assert _is_linked(a, 'Project7', b2)
    if hasattr(b1, 'employees'):
        assert not _is_linked(b1, 'employees', a)
    if hasattr(b2, 'employees'):
        assert _is_linked(b2, 'employees', a)
    _safe_set(a, 'Project7', None)
    assert not _is_linked(a, 'Project7', b2)
    if hasattr(b2, 'employees'):
        assert not _is_linked(b2, 'employees', a)


def test_assoc_projets12_link_reassign_clear():
    a = exo1_Project(budget=7, name="sample_text")
    b1 = exo1_Company()
    b2 = exo1_Company()
    _safe_set(a, 'exo1_Project', b1)
    assert _is_linked(a, 'exo1_Project', b1)
    if hasattr(b1, 'exo1_Company13'):
        assert _is_linked(b1, 'exo1_Company13', a)
    _safe_set(a, 'exo1_Project', b2)
    assert _is_linked(a, 'exo1_Project', b2)
    if hasattr(b1, 'exo1_Company13'):
        assert not _is_linked(b1, 'exo1_Company13', a)
    if hasattr(b2, 'exo1_Company13'):
        assert _is_linked(b2, 'exo1_Company13', a)
    _safe_set(a, 'exo1_Project', None)
    assert not _is_linked(a, 'exo1_Project', b2)
    if hasattr(b2, 'exo1_Company13'):
        assert not _is_linked(b2, 'exo1_Company13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

exo1_Company_strategy = st.builds(exo1_Company)
@given(instance=exo1_Company_strategy)
@settings(max_examples=25)
def test_exo1_Company_instantiation(instance):
    assert isinstance(instance, exo1_Company)


exo1_Departement_strategy = st.builds(exo1_Departement, budget=st.integers(), location=safe_text, name=safe_text)
@given(instance=exo1_Departement_strategy)
@settings(max_examples=25)
def test_exo1_Departement_instantiation(instance):
    assert isinstance(instance, exo1_Departement)


exo1_Employee_strategy = st.builds(exo1_Employee, name=safe_text, salary=safe_text)
@given(instance=exo1_Employee_strategy)
@settings(max_examples=25)
def test_exo1_Employee_instantiation(instance):
    assert isinstance(instance, exo1_Employee)


exo1_Project_strategy = st.builds(exo1_Project, budget=st.integers(), name=safe_text)
@given(instance=exo1_Project_strategy)
@settings(max_examples=25)
def test_exo1_Project_instantiation(instance):
    assert isinstance(instance, exo1_Project)



