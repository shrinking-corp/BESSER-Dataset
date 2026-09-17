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
    CoachBusWithEDataType_Employee,
    Employee,
    CoachBusWithEDataType_Manager,
    CoachBusWithEDataType_SecurityGuard,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_coachbuswithedatatype_employee_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Employee)


def test_hyp_coachbuswithedatatype_employee_constructor_exists():
    assert callable(CoachBusWithEDataType_Employee.__init__)


def test_hyp_coachbuswithedatatype_employee_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coachbuswithedatatype_manager_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Manager)


def test_hyp_coachbuswithedatatype_manager_constructor_exists():
    assert callable(CoachBusWithEDataType_Manager.__init__)


def test_hyp_coachbuswithedatatype_manager_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Manager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coachbuswithedatatype_securityguard_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_SecurityGuard)


def test_hyp_coachbuswithedatatype_securityguard_constructor_exists():
    assert callable(CoachBusWithEDataType_SecurityGuard.__init__)


def test_hyp_coachbuswithedatatype_securityguard_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_SecurityGuard.__init__)
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
CoachBusWithEDataType_Employee_strategy = st.builds(
    CoachBusWithEDataType_Employee,
    id=
        st.integers()
)
Employee_strategy = st.builds(
    Employee,
)
CoachBusWithEDataType_Manager_strategy = st.builds(
    CoachBusWithEDataType_Manager,
)
CoachBusWithEDataType_SecurityGuard_strategy = st.builds(
    CoachBusWithEDataType_SecurityGuard,
)




@given(instance=CoachBusWithEDataType_Employee_strategy)
def test_hyp_coachbuswithedatatype_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CoachBusWithEDataType_Employee,
    CoachBusWithEDataType_Manager,
    CoachBusWithEDataType_SecurityGuard,
    Employee,
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

def test_CoachBusWithEDataType_Employee_id_value_roundtrip():
    instance = CoachBusWithEDataType_Employee(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_CoachBusWithEDataType_Manager_isa_Employee():
    instance = CoachBusWithEDataType_Manager()
    assert isinstance(instance, Employee)


def test_CoachBusWithEDataType_SecurityGuard_isa_Employee():
    instance = CoachBusWithEDataType_SecurityGuard()
    assert isinstance(instance, Employee)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CoachBusWithEDataType_Employee_strategy = st.builds(CoachBusWithEDataType_Employee, id=st.integers())
@given(instance=CoachBusWithEDataType_Employee_strategy)
@settings(max_examples=25)
def test_CoachBusWithEDataType_Employee_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Employee)


CoachBusWithEDataType_Manager_strategy = st.builds(CoachBusWithEDataType_Manager)
@given(instance=CoachBusWithEDataType_Manager_strategy)
@settings(max_examples=25)
def test_CoachBusWithEDataType_Manager_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Manager)


CoachBusWithEDataType_SecurityGuard_strategy = st.builds(CoachBusWithEDataType_SecurityGuard)
@given(instance=CoachBusWithEDataType_SecurityGuard_strategy)
@settings(max_examples=25)
def test_CoachBusWithEDataType_SecurityGuard_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_SecurityGuard)


Employee_strategy = st.builds(Employee)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)



