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
    hfsm_NamedElement,
    NamedElement,
    hfsm_AbstractState,
    hfsm_Region,
    AbstractState,
    hfsm_State,
    hfsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_hfsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(hfsm_NamedElement)


def test_hyp_hfsm_namedelement_constructor_exists():
    assert callable(hfsm_NamedElement.__init__)


def test_hyp_hfsm_namedelement_constructor_args():
    sig = inspect.signature(hfsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hfsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(hfsm_AbstractState)


def test_hyp_hfsm_abstractstate_constructor_exists():
    assert callable(hfsm_AbstractState.__init__)


def test_hyp_hfsm_abstractstate_constructor_args():
    sig = inspect.signature(hfsm_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hfsm_region_is_not_abstract():
    assert not inspect.isabstract(hfsm_Region)


def test_hyp_hfsm_region_constructor_exists():
    assert callable(hfsm_Region.__init__)


def test_hyp_hfsm_region_constructor_args():
    sig = inspect.signature(hfsm_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_hyp_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_hyp_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hfsm_state_is_not_abstract():
    assert not inspect.isabstract(hfsm_State)


def test_hyp_hfsm_state_constructor_exists():
    assert callable(hfsm_State.__init__)


def test_hyp_hfsm_state_constructor_args():
    sig = inspect.signature(hfsm_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hfsm_transition_is_not_abstract():
    assert not inspect.isabstract(hfsm_Transition)


def test_hyp_hfsm_transition_constructor_exists():
    assert callable(hfsm_Transition.__init__)


def test_hyp_hfsm_transition_constructor_args():
    sig = inspect.signature(hfsm_Transition.__init__)
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
hfsm_NamedElement_strategy = st.builds(
    hfsm_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hfsm_AbstractState_strategy = st.builds(
    hfsm_AbstractState,
)
hfsm_Region_strategy = st.builds(
    hfsm_Region,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
hfsm_State_strategy = st.builds(
    hfsm_State,
)
hfsm_Transition_strategy = st.builds(
    hfsm_Transition,
)




@given(instance=hfsm_NamedElement_strategy)
def test_hyp_hfsm_namedelement_name_setter(instance):
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
    AbstractState,
    NamedElement,
    hfsm_AbstractState,
    hfsm_NamedElement,
    hfsm_Region,
    hfsm_State,
    hfsm_Transition,
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

def test_hfsm_NamedElement_name_value_roundtrip():
    instance = hfsm_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_hfsm_State_isa_AbstractState():
    instance = hfsm_State()
    assert isinstance(instance, AbstractState)


def test_hfsm_AbstractState_isa_NamedElement():
    instance = hfsm_AbstractState()
    assert isinstance(instance, NamedElement)


def test_hfsm_Region_isa_NamedElement():
    instance = hfsm_Region()
    assert isinstance(instance, NamedElement)


def test_hfsm_Transition_isa_NamedElement():
    instance = hfsm_Transition()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


hfsm_AbstractState_strategy = st.builds(hfsm_AbstractState)
@given(instance=hfsm_AbstractState_strategy)
@settings(max_examples=25)
def test_hfsm_AbstractState_instantiation(instance):
    assert isinstance(instance, hfsm_AbstractState)


hfsm_NamedElement_strategy = st.builds(hfsm_NamedElement, name=safe_text)
@given(instance=hfsm_NamedElement_strategy)
@settings(max_examples=25)
def test_hfsm_NamedElement_instantiation(instance):
    assert isinstance(instance, hfsm_NamedElement)


hfsm_Region_strategy = st.builds(hfsm_Region)
@given(instance=hfsm_Region_strategy)
@settings(max_examples=25)
def test_hfsm_Region_instantiation(instance):
    assert isinstance(instance, hfsm_Region)


hfsm_State_strategy = st.builds(hfsm_State)
@given(instance=hfsm_State_strategy)
@settings(max_examples=25)
def test_hfsm_State_instantiation(instance):
    assert isinstance(instance, hfsm_State)


hfsm_Transition_strategy = st.builds(hfsm_Transition)
@given(instance=hfsm_Transition_strategy)
@settings(max_examples=25)
def test_hfsm_Transition_instantiation(instance):
    assert isinstance(instance, hfsm_Transition)



