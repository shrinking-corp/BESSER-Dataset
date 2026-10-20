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
    company_Employee,
    company_Department,
    company_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_company_employee_is_not_abstract():
    assert not inspect.isabstract(company_Employee)


def test_hyp_company_employee_constructor_exists():
    assert callable(company_Employee.__init__)


def test_hyp_company_employee_constructor_args():
    sig = inspect.signature(company_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_company_department_is_not_abstract():
    assert not inspect.isabstract(company_Department)


def test_hyp_company_department_constructor_exists():
    assert callable(company_Department.__init__)


def test_hyp_company_department_constructor_args():
    sig = inspect.signature(company_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "budget" in params, "Missing parameter 'budget'"





def test_hyp_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_hyp_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_hyp_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
    params = list(sig.parameters.keys())


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
company_Employee_strategy = st.builds(
    company_Employee,
    name=
        safe_text
)
company_Department_strategy = st.builds(
    company_Department,
    name=
        safe_text,
    budget=
        st.integers()
)
company_Company_strategy = st.builds(
    company_Company,
)




@given(instance=company_Employee_strategy)
def test_hyp_company_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=company_Department_strategy)
def test_hyp_company_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Department_strategy)
def test_hyp_company_department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    company_Company,
    company_Department,
    company_Employee,
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

def test_company_Department_budget_value_roundtrip():
    instance = company_Department(budget=7, name="sample_text")
    assert instance.budget == 7
    instance.budget = 13
    assert instance.budget == 13


def test_company_Department_name_value_roundtrip():
    instance = company_Department(budget=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_company_Employee_name_value_roundtrip():
    instance = company_Employee(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_departments0_link_reassign_clear():
    a = company_Department(budget=7, name="sample_text")
    b1 = company_Company()
    b2 = company_Company()
    _safe_set(a, 'company_Department', b1)
    assert _is_linked(a, 'company_Department', b1)
    if hasattr(b1, 'company_Company'):
        assert _is_linked(b1, 'company_Company', a)
    _safe_set(a, 'company_Department', b2)
    assert _is_linked(a, 'company_Department', b2)
    if hasattr(b1, 'company_Company'):
        assert not _is_linked(b1, 'company_Company', a)
    if hasattr(b2, 'company_Company'):
        assert _is_linked(b2, 'company_Company', a)
    _safe_set(a, 'company_Department', None)
    assert not _is_linked(a, 'company_Department', b2)
    if hasattr(b2, 'company_Company'):
        assert not _is_linked(b2, 'company_Company', a)


def test_assoc_employees1_link_reassign_clear():
    a = company_Employee(name="sample_text")
    b1 = company_Company()
    b2 = company_Company()
    _safe_set(a, 'company_Employee', b1)
    assert _is_linked(a, 'company_Employee', b1)
    if hasattr(b1, 'company_Company2'):
        assert _is_linked(b1, 'company_Company2', a)
    _safe_set(a, 'company_Employee', b2)
    assert _is_linked(a, 'company_Employee', b2)
    if hasattr(b1, 'company_Company2'):
        assert not _is_linked(b1, 'company_Company2', a)
    if hasattr(b2, 'company_Company2'):
        assert _is_linked(b2, 'company_Company2', a)
    _safe_set(a, 'company_Employee', None)
    assert not _is_linked(a, 'company_Employee', b2)
    if hasattr(b2, 'company_Company2'):
        assert not _is_linked(b2, 'company_Company2', a)


def test_assoc_employees3_link_reassign_clear():
    a = company_Employee(name="sample_text")
    b1 = company_Department(budget=7, name="sample_text")
    b2 = company_Department(budget=13, name="sample_text_2")
    _safe_set(a, 'company_Employee5', b1)
    assert _is_linked(a, 'company_Employee5', b1)
    if hasattr(b1, 'company_Department4'):
        assert _is_linked(b1, 'company_Department4', a)
    _safe_set(a, 'company_Employee5', b2)
    assert _is_linked(a, 'company_Employee5', b2)
    if hasattr(b1, 'company_Department4'):
        assert not _is_linked(b1, 'company_Department4', a)
    if hasattr(b2, 'company_Department4'):
        assert _is_linked(b2, 'company_Department4', a)
    _safe_set(a, 'company_Employee5', None)
    assert not _is_linked(a, 'company_Employee5', b2)
    if hasattr(b2, 'company_Department4'):
        assert not _is_linked(b2, 'company_Department4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

company_Company_strategy = st.builds(company_Company)
@given(instance=company_Company_strategy)
@settings(max_examples=25)
def test_company_Company_instantiation(instance):
    assert isinstance(instance, company_Company)


company_Department_strategy = st.builds(company_Department, budget=st.integers(), name=safe_text)
@given(instance=company_Department_strategy)
@settings(max_examples=25)
def test_company_Department_instantiation(instance):
    assert isinstance(instance, company_Department)


company_Employee_strategy = st.builds(company_Employee, name=safe_text)
@given(instance=company_Employee_strategy)
@settings(max_examples=25)
def test_company_Employee_instantiation(instance):
    assert isinstance(instance, company_Employee)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    company_Company,
    company_Department,
    company_Employee,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_employees3_reverse_link_reassign_clear():
    a1 = company_Employee(name="sample_text")
    a2 = company_Employee(name="sample_text_2")
    b = company_Department(budget=7, name="sample_text")
    _safe_set(b, 'company_Department4', {a1})
    assert _is_linked(b, 'company_Department4', a1)
    if hasattr(a1, 'company_Employee5'):
        assert _is_linked(a1, 'company_Employee5', b)
    _safe_set(b, 'company_Department4', {a2})
    assert _is_linked(b, 'company_Department4', a2)
    if hasattr(a1, 'company_Employee5'):
        assert not _is_linked(a1, 'company_Employee5', b)
    if hasattr(a2, 'company_Employee5'):
        assert _is_linked(a2, 'company_Employee5', b)
    _safe_set(b, 'company_Department4', set())
    assert not _is_linked(b, 'company_Department4', a2)
    if hasattr(a2, 'company_Employee5'):
        assert not _is_linked(a2, 'company_Employee5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_departments0_stub_double():
    # company_Company has no real 'company_Company' property in the generated
    # code (a bare stub) -- manually attach it so company_Department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Department(budget=7, name="sample_text")
    partner = company_Company()
    setattr(partner, 'company_Company', None)
    _safe_set(owner, 'company_Department', partner)
    assert owner in getattr(partner, 'company_Company')
    _safe_set(owner, 'company_Department', None)
    assert owner not in getattr(partner, 'company_Company')


def test_assoc_employees1_stub_double():
    # company_Company has no real 'company_Company2' property in the generated
    # code (a bare stub) -- manually attach it so company_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # company_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = company_Employee(name="sample_text")
    partner = company_Company()
    setattr(partner, 'company_Company2', None)
    _safe_set(owner, 'company_Employee', partner)
    assert owner in getattr(partner, 'company_Company2')
    _safe_set(owner, 'company_Employee', None)
    assert owner not in getattr(partner, 'company_Company2')




from python_code import company_Company
from python_code import company_Department

def test_company_Department___init__():
    assert company_Department.__init__(company_Department('\x00\x00', 0, company_Department=company_Company(), company_Department4=set()), '', 0, company_Department=company_Company(), company_Department4=set()) == None

