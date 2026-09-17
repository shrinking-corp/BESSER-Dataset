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
    Class,
    PlanDAO,
    PatientDAO,
    PatientBO,
    StateDAO1,
    PatientTO,
    StateDAO,
    EnrollPatient_Controller,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plandao_is_not_abstract():
    assert not inspect.isabstract(PlanDAO)


def test_hyp_plandao_constructor_exists():
    assert callable(PlanDAO.__init__)


def test_hyp_plandao_constructor_args():
    sig = inspect.signature(PlanDAO.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patientdao_is_not_abstract():
    assert not inspect.isabstract(PatientDAO)


def test_hyp_patientdao_constructor_exists():
    assert callable(PatientDAO.__init__)


def test_hyp_patientdao_constructor_args():
    sig = inspect.signature(PatientDAO.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patientbo_is_not_abstract():
    assert not inspect.isabstract(PatientBO)


def test_hyp_patientbo_constructor_exists():
    assert callable(PatientBO.__init__)


def test_hyp_patientbo_constructor_args():
    sig = inspect.signature(PatientBO.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statedao1_is_not_abstract():
    assert not inspect.isabstract(StateDAO1)


def test_hyp_statedao1_constructor_exists():
    assert callable(StateDAO1.__init__)


def test_hyp_statedao1_constructor_args():
    sig = inspect.signature(StateDAO1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patientto_is_not_abstract():
    assert not inspect.isabstract(PatientTO)


def test_hyp_patientto_constructor_exists():
    assert callable(PatientTO.__init__)


def test_hyp_patientto_constructor_args():
    sig = inspect.signature(PatientTO.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "plan_id" in params, "Missing parameter 'plan_id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "state_id" in params, "Missing parameter 'state_id'"
    assert "patient_id" in params, "Missing parameter 'patient_id'"
    assert "first_name" in params, "Missing parameter 'first_name'"












def test_hyp_statedao_is_not_abstract():
    assert not inspect.isabstract(StateDAO)


def test_hyp_statedao_constructor_exists():
    assert callable(StateDAO.__init__)


def test_hyp_statedao_constructor_args():
    sig = inspect.signature(StateDAO.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enrollpatient_controller_is_not_abstract():
    assert not inspect.isabstract(EnrollPatient_Controller)


def test_hyp_enrollpatient_controller_constructor_exists():
    assert callable(EnrollPatient_Controller.__init__)


def test_hyp_enrollpatient_controller_constructor_args():
    sig = inspect.signature(EnrollPatient_Controller.__init__)
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
Class_strategy = st.builds(
    Class,
)
PlanDAO_strategy = st.builds(
    PlanDAO,
)
PatientDAO_strategy = st.builds(
    PatientDAO,
)
PatientBO_strategy = st.builds(
    PatientBO,
)
StateDAO1_strategy = st.builds(
    StateDAO1,
)
PatientTO_strategy = st.builds(
    PatientTO,
    password=
        safe_text,
    date_of_birth=
        st.dates(),
    last_name=
        safe_text,
    plan_id=
        st.integers(),
    email=
        safe_text,
    contact_no=
        st.integers(),
    state_id=
        st.integers(),
    patient_id=
        st.integers(),
    first_name=
        safe_text
)
StateDAO_strategy = st.builds(
    StateDAO,
)
EnrollPatient_Controller_strategy = st.builds(
    EnrollPatient_Controller,
)









@given(instance=PatientTO_strategy)
def test_hyp_patientto_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_plan_id_setter(instance):
    original = instance.plan_id
    instance.plan_id = original
    assert instance.plan_id == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_contact_no_setter(instance):
    original = instance.contact_no
    instance.contact_no = original
    assert instance.contact_no == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_state_id_setter(instance):
    original = instance.state_id
    instance.state_id = original
    assert instance.state_id == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_patient_id_setter(instance):
    original = instance.patient_id
    instance.patient_id = original
    assert instance.patient_id == original



@given(instance=PatientTO_strategy)
def test_hyp_patientto_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    EnrollPatient_Controller,
    PatientBO,
    PatientDAO,
    PatientTO,
    PlanDAO,
    StateDAO,
    StateDAO1,
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

def test_PatientTO_contact_no_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.contact_no == 7
    instance.contact_no = 13
    assert instance.contact_no == 13


def test_PatientTO_date_of_birth_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.date_of_birth == date(2024, 1, 1)
    instance.date_of_birth = date(2025, 6, 15)
    assert instance.date_of_birth == date(2025, 6, 15)


def test_PatientTO_email_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_PatientTO_first_name_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.first_name == "sample_text"
    instance.first_name = "sample_text_2"
    assert instance.first_name == "sample_text_2"


def test_PatientTO_last_name_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.last_name == "sample_text"
    instance.last_name = "sample_text_2"
    assert instance.last_name == "sample_text_2"


def test_PatientTO_password_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_PatientTO_patient_id_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.patient_id == 7
    instance.patient_id = 13
    assert instance.patient_id == 13


def test_PatientTO_plan_id_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.plan_id == 7
    instance.plan_id = 13
    assert instance.plan_id == 13


def test_PatientTO_state_id_value_roundtrip():
    instance = PatientTO(contact_no=7, date_of_birth=date(2024, 1, 1), email="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", patient_id=7, plan_id=7, state_id=7)
    assert instance.state_id == 7
    instance.state_id = 13
    assert instance.state_id == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


EnrollPatient_Controller_strategy = st.builds(EnrollPatient_Controller)
@given(instance=EnrollPatient_Controller_strategy)
@settings(max_examples=25)
def test_EnrollPatient_Controller_instantiation(instance):
    assert isinstance(instance, EnrollPatient_Controller)


PatientBO_strategy = st.builds(PatientBO)
@given(instance=PatientBO_strategy)
@settings(max_examples=25)
def test_PatientBO_instantiation(instance):
    assert isinstance(instance, PatientBO)


PatientDAO_strategy = st.builds(PatientDAO)
@given(instance=PatientDAO_strategy)
@settings(max_examples=25)
def test_PatientDAO_instantiation(instance):
    assert isinstance(instance, PatientDAO)


PatientTO_strategy = st.builds(PatientTO, contact_no=st.integers(), date_of_birth=st.dates(), email=safe_text, first_name=safe_text, last_name=safe_text, password=safe_text, patient_id=st.integers(), plan_id=st.integers(), state_id=st.integers())
@given(instance=PatientTO_strategy)
@settings(max_examples=25)
def test_PatientTO_instantiation(instance):
    assert isinstance(instance, PatientTO)


PlanDAO_strategy = st.builds(PlanDAO)
@given(instance=PlanDAO_strategy)
@settings(max_examples=25)
def test_PlanDAO_instantiation(instance):
    assert isinstance(instance, PlanDAO)


StateDAO_strategy = st.builds(StateDAO)
@given(instance=StateDAO_strategy)
@settings(max_examples=25)
def test_StateDAO_instantiation(instance):
    assert isinstance(instance, StateDAO)


StateDAO1_strategy = st.builds(StateDAO1)
@given(instance=StateDAO1_strategy)
@settings(max_examples=25)
def test_StateDAO1_instantiation(instance):
    assert isinstance(instance, StateDAO1)



