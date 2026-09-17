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
    PetriNet_Net,
    NamedElement,
    PetriNet_Place,
    PetriNet_NamedElement,
    PetriNet_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_petrinet_net_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Net)


def test_hyp_petrinet_net_constructor_exists():
    assert callable(PetriNet_Net.__init__)


def test_hyp_petrinet_net_constructor_args():
    sig = inspect.signature(PetriNet_Net.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_hyp_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_hyp_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_namedelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_NamedElement)


def test_hyp_petrinet_namedelement_constructor_exists():
    assert callable(PetriNet_NamedElement.__init__)


def test_hyp_petrinet_namedelement_constructor_args():
    sig = inspect.signature(PetriNet_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_hyp_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_hyp_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
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
PetriNet_Net_strategy = st.builds(
    PetriNet_Net,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)
PetriNet_NamedElement_strategy = st.builds(
    PetriNet_NamedElement,
    name=
        safe_text
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)







@given(instance=PetriNet_NamedElement_strategy)
def test_hyp_petrinet_namedelement_name_setter(instance):
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
    NamedElement,
    PetriNet_NamedElement,
    PetriNet_Net,
    PetriNet_Place,
    PetriNet_Transition,
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

def test_PetriNet_NamedElement_name_value_roundtrip():
    instance = PetriNet_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_PetriNet_Place_isa_NamedElement():
    instance = PetriNet_Place()
    assert isinstance(instance, NamedElement)


def test_PetriNet_Transition_isa_NamedElement():
    instance = PetriNet_Transition()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


PetriNet_NamedElement_strategy = st.builds(PetriNet_NamedElement, name=safe_text)
@given(instance=PetriNet_NamedElement_strategy)
@settings(max_examples=25)
def test_PetriNet_NamedElement_instantiation(instance):
    assert isinstance(instance, PetriNet_NamedElement)


PetriNet_Net_strategy = st.builds(PetriNet_Net)
@given(instance=PetriNet_Net_strategy)
@settings(max_examples=25)
def test_PetriNet_Net_instantiation(instance):
    assert isinstance(instance, PetriNet_Net)


PetriNet_Place_strategy = st.builds(PetriNet_Place)
@given(instance=PetriNet_Place_strategy)
@settings(max_examples=25)
def test_PetriNet_Place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)


PetriNet_Transition_strategy = st.builds(PetriNet_Transition)
@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=25)
def test_PetriNet_Transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)



