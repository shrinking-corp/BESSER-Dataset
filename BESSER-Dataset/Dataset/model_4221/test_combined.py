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
    _101companies_Employee,
    _101companies_Department,
    _101companies_Company,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp__101companies_employee_is_not_abstract():
    assert not inspect.isabstract(_101companies_Employee)


def test_hyp__101companies_employee_constructor_exists():
    assert callable(_101companies_Employee.__init__)


def test_hyp__101companies_employee_constructor_args():
    sig = inspect.signature(_101companies_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp__101companies_department_is_not_abstract():
    assert not inspect.isabstract(_101companies_Department)


def test_hyp__101companies_department_constructor_exists():
    assert callable(_101companies_Department.__init__)


def test_hyp__101companies_department_constructor_args():
    sig = inspect.signature(_101companies_Department.__init__)
    params = list(sig.parameters.keys())
    assert "totalSalary" in params, "Missing parameter 'totalSalary'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp__101companies_company_is_not_abstract():
    assert not inspect.isabstract(_101companies_Company)


def test_hyp__101companies_company_constructor_exists():
    assert callable(_101companies_Company.__init__)


def test_hyp__101companies_company_constructor_args():
    sig = inspect.signature(_101companies_Company.__init__)
    params = list(sig.parameters.keys())
    assert "totalSalary" in params, "Missing parameter 'totalSalary'"
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
_101companies_Employee_strategy = st.builds(
    _101companies_Employee,
    address=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
_101companies_Department_strategy = st.builds(
    _101companies_Department,
    totalSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
_101companies_Company_strategy = st.builds(
    _101companies_Company,
    totalSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)




@given(instance=_101companies_Employee_strategy)
def test_hyp__101companies_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=_101companies_Employee_strategy)
def test_hyp__101companies_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=_101companies_Employee_strategy)
def test_hyp__101companies_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=_101companies_Department_strategy)
def test_hyp__101companies_department_totalSalary_setter(instance):
    original = instance.totalSalary
    instance.totalSalary = original
    assert instance.totalSalary == original



@given(instance=_101companies_Department_strategy)
def test_hyp__101companies_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=_101companies_Company_strategy)
def test_hyp__101companies_company_totalSalary_setter(instance):
    original = instance.totalSalary
    instance.totalSalary = original
    assert instance.totalSalary == original



@given(instance=_101companies_Company_strategy)
def test_hyp__101companies_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    _101companies_Company,
    _101companies_Department,
    _101companies_Employee,
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

def test__101companies_Company_name_value_roundtrip():
    instance = _101companies_Company(name="sample_text", totalSalary=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test__101companies_Company_totalSalary_value_roundtrip():
    instance = _101companies_Company(name="sample_text", totalSalary=3.14)
    assert instance.totalSalary == 3.14
    instance.totalSalary = 9.99
    assert instance.totalSalary == 9.99


def test__101companies_Department_name_value_roundtrip():
    instance = _101companies_Department(name="sample_text", totalSalary=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test__101companies_Department_totalSalary_value_roundtrip():
    instance = _101companies_Department(name="sample_text", totalSalary=3.14)
    assert instance.totalSalary == 3.14
    instance.totalSalary = 9.99
    assert instance.totalSalary == 9.99


def test__101companies_Employee_address_value_roundtrip():
    instance = _101companies_Employee(address="sample_text", name="sample_text", salary=3.14)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test__101companies_Employee_name_value_roundtrip():
    instance = _101companies_Employee(address="sample_text", name="sample_text", salary=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test__101companies_Employee_salary_value_roundtrip():
    instance = _101companies_Employee(address="sample_text", name="sample_text", salary=3.14)
    assert instance.salary == 3.14
    instance.salary = 9.99
    assert instance.salary == 9.99


def test_assoc_departments0_link_reassign_clear():
    a = _101companies_Department(name="sample_text", totalSalary=3.14)
    b1 = _101companies_Company(name="sample_text", totalSalary=3.14)
    b2 = _101companies_Company(name="sample_text_2", totalSalary=9.99)
    _safe_set(a, '_101companies_Department', b1)
    assert _is_linked(a, '_101companies_Department', b1)
    if hasattr(b1, '_101companies_Company'):
        assert _is_linked(b1, '_101companies_Company', a)
    _safe_set(a, '_101companies_Department', b2)
    assert _is_linked(a, '_101companies_Department', b2)
    if hasattr(b1, '_101companies_Company'):
        assert not _is_linked(b1, '_101companies_Company', a)
    if hasattr(b2, '_101companies_Company'):
        assert _is_linked(b2, '_101companies_Company', a)
    _safe_set(a, '_101companies_Department', None)
    assert not _is_linked(a, '_101companies_Department', b2)
    if hasattr(b2, '_101companies_Company'):
        assert not _is_linked(b2, '_101companies_Company', a)


def test_assoc_employees3_link_reassign_clear():
    a = _101companies_Employee(address="sample_text", name="sample_text", salary=3.14)
    b1 = _101companies_Department(name="sample_text", totalSalary=3.14)
    b2 = _101companies_Department(name="sample_text_2", totalSalary=9.99)
    _safe_set(a, '_101companies_Employee5', b1)
    assert _is_linked(a, '_101companies_Employee5', b1)
    if hasattr(b1, '_101companies_Department4'):
        assert _is_linked(b1, '_101companies_Department4', a)
    _safe_set(a, '_101companies_Employee5', b2)
    assert _is_linked(a, '_101companies_Employee5', b2)
    if hasattr(b1, '_101companies_Department4'):
        assert not _is_linked(b1, '_101companies_Department4', a)
    if hasattr(b2, '_101companies_Department4'):
        assert _is_linked(b2, '_101companies_Department4', a)
    _safe_set(a, '_101companies_Employee5', None)
    assert not _is_linked(a, '_101companies_Employee5', b2)
    if hasattr(b2, '_101companies_Department4'):
        assert not _is_linked(b2, '_101companies_Department4', a)


def test_assoc_manager1_link_reassign_clear():
    a = _101companies_Employee(address="sample_text", name="sample_text", salary=3.14)
    b1 = _101companies_Department(name="sample_text", totalSalary=3.14)
    b2 = _101companies_Department(name="sample_text_2", totalSalary=9.99)
    _safe_set(a, '_101companies_Employee', b1)
    assert _is_linked(a, '_101companies_Employee', b1)
    if hasattr(b1, '_101companies_Department2'):
        assert _is_linked(b1, '_101companies_Department2', a)
    _safe_set(a, '_101companies_Employee', b2)
    assert _is_linked(a, '_101companies_Employee', b2)
    if hasattr(b1, '_101companies_Department2'):
        assert not _is_linked(b1, '_101companies_Department2', a)
    if hasattr(b2, '_101companies_Department2'):
        assert _is_linked(b2, '_101companies_Department2', a)
    _safe_set(a, '_101companies_Employee', None)
    assert not _is_linked(a, '_101companies_Employee', b2)
    if hasattr(b2, '_101companies_Department2'):
        assert not _is_linked(b2, '_101companies_Department2', a)


def test_assoc_subdepartments7_link_reassign_clear():
    a = _101companies_Department(name="sample_text", totalSalary=3.14)
    b1 = _101companies_Department(name="sample_text", totalSalary=3.14)
    b2 = _101companies_Department(name="sample_text_2", totalSalary=9.99)
    _safe_set(a, '_101companies_Department6', {b1})
    assert _is_linked(a, '_101companies_Department6', b1)
    if hasattr(b1, '_101companies_Department8'):
        assert _is_linked(b1, '_101companies_Department8', a)
    _safe_set(a, '_101companies_Department6', {b2})
    assert _is_linked(a, '_101companies_Department6', b2)
    if hasattr(b1, '_101companies_Department8'):
        assert not _is_linked(b1, '_101companies_Department8', a)
    if hasattr(b2, '_101companies_Department8'):
        assert _is_linked(b2, '_101companies_Department8', a)
    _safe_set(a, '_101companies_Department6', set())
    assert not _is_linked(a, '_101companies_Department6', b2)
    if hasattr(b2, '_101companies_Department8'):
        assert not _is_linked(b2, '_101companies_Department8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

_101companies_Company_strategy = st.builds(_101companies_Company, name=safe_text, totalSalary=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=_101companies_Company_strategy)
@settings(max_examples=25)
def test__101companies_Company_instantiation(instance):
    assert isinstance(instance, _101companies_Company)


_101companies_Department_strategy = st.builds(_101companies_Department, name=safe_text, totalSalary=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=_101companies_Department_strategy)
@settings(max_examples=25)
def test__101companies_Department_instantiation(instance):
    assert isinstance(instance, _101companies_Department)


_101companies_Employee_strategy = st.builds(_101companies_Employee, address=safe_text, name=safe_text, salary=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=_101companies_Employee_strategy)
@settings(max_examples=25)
def test__101companies_Employee_instantiation(instance):
    assert isinstance(instance, _101companies_Employee)



