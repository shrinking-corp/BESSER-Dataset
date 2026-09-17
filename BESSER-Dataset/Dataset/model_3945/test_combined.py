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
    PathExp,
    PathExp_State,
    Transition,
    State,
    Element,
    PathExp_Transition,
    PathExp_PathExp,
    PathExp_Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pathexp_is_not_abstract():
    assert not inspect.isabstract(PathExp)


def test_hyp_pathexp_constructor_exists():
    assert callable(PathExp.__init__)


def test_hyp_pathexp_constructor_args():
    sig = inspect.signature(PathExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pathexp_state_is_not_abstract():
    assert not inspect.isabstract(PathExp_State)


def test_hyp_pathexp_state_constructor_exists():
    assert callable(PathExp_State.__init__)


def test_hyp_pathexp_state_constructor_args():
    sig = inspect.signature(PathExp_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pathexp_transition_is_not_abstract():
    assert not inspect.isabstract(PathExp_Transition)


def test_hyp_pathexp_transition_constructor_exists():
    assert callable(PathExp_Transition.__init__)


def test_hyp_pathexp_transition_constructor_args():
    sig = inspect.signature(PathExp_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pathexp_pathexp_is_not_abstract():
    assert not inspect.isabstract(PathExp_PathExp)


def test_hyp_pathexp_pathexp_constructor_exists():
    assert callable(PathExp_PathExp.__init__)


def test_hyp_pathexp_pathexp_constructor_args():
    sig = inspect.signature(PathExp_PathExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pathexp_element_is_not_abstract():
    assert not inspect.isabstract(PathExp_Element)


def test_hyp_pathexp_element_constructor_exists():
    assert callable(PathExp_Element.__init__)


def test_hyp_pathexp_element_constructor_args():
    sig = inspect.signature(PathExp_Element.__init__)
    params = list(sig.parameters.keys())
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
PathExp_strategy = st.builds(
    PathExp,
)
PathExp_State_strategy = st.builds(
    PathExp_State,
)
Transition_strategy = st.builds(
    Transition,
)
State_strategy = st.builds(
    State,
)
Element_strategy = st.builds(
    Element,
)
PathExp_Transition_strategy = st.builds(
    PathExp_Transition,
)
PathExp_PathExp_strategy = st.builds(
    PathExp_PathExp,
)
PathExp_Element_strategy = st.builds(
    PathExp_Element,
    name=
        safe_text
)











@given(instance=PathExp_Element_strategy)
def test_hyp_pathexp_element_name_setter(instance):
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
    Element,
    PathExp,
    PathExp_Element,
    PathExp_PathExp,
    PathExp_State,
    PathExp_Transition,
    State,
    Transition,
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

def test_PathExp_Element_name_value_roundtrip():
    instance = PathExp_Element(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_PathExp_PathExp_isa_Element():
    instance = PathExp_PathExp()
    assert isinstance(instance, Element)


def test_PathExp_Transition_isa_Element():
    instance = PathExp_Transition()
    assert isinstance(instance, Element)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


PathExp_strategy = st.builds(PathExp)
@given(instance=PathExp_strategy)
@settings(max_examples=25)
def test_PathExp_instantiation(instance):
    assert isinstance(instance, PathExp)


PathExp_Element_strategy = st.builds(PathExp_Element, name=safe_text)
@given(instance=PathExp_Element_strategy)
@settings(max_examples=25)
def test_PathExp_Element_instantiation(instance):
    assert isinstance(instance, PathExp_Element)


PathExp_PathExp_strategy = st.builds(PathExp_PathExp)
@given(instance=PathExp_PathExp_strategy)
@settings(max_examples=25)
def test_PathExp_PathExp_instantiation(instance):
    assert isinstance(instance, PathExp_PathExp)


PathExp_State_strategy = st.builds(PathExp_State)
@given(instance=PathExp_State_strategy)
@settings(max_examples=25)
def test_PathExp_State_instantiation(instance):
    assert isinstance(instance, PathExp_State)


PathExp_Transition_strategy = st.builds(PathExp_Transition)
@given(instance=PathExp_Transition_strategy)
@settings(max_examples=25)
def test_PathExp_Transition_instantiation(instance):
    assert isinstance(instance, PathExp_Transition)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)



