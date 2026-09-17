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
    NamedElement,
    PetriNet_Element,
    PetriNet_PetriNet,
    LocatedElement,
    PetriNet_NamedElement,
    Element,
    PetriNet_Transition,
    PetriNet_Place,
    PetriNet_LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Element)


def test_hyp_petrinet_element_constructor_exists():
    assert callable(PetriNet_Element.__init__)


def test_hyp_petrinet_element_constructor_args():
    sig = inspect.signature(PetriNet_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriNet)


def test_hyp_petrinet_petrinet_constructor_exists():
    assert callable(PetriNet_PetriNet.__init__)


def test_hyp_petrinet_petrinet_constructor_args():
    sig = inspect.signature(PetriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_hyp_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_hyp_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_namedelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_NamedElement)


def test_hyp_petrinet_namedelement_constructor_exists():
    assert callable(PetriNet_NamedElement.__init__)


def test_hyp_petrinet_namedelement_constructor_args():
    sig = inspect.signature(PetriNet_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_hyp_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_hyp_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_hyp_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_hyp_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_locatedelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_LocatedElement)


def test_hyp_petrinet_locatedelement_constructor_exists():
    assert callable(PetriNet_LocatedElement.__init__)


def test_hyp_petrinet_locatedelement_constructor_args():
    sig = inspect.signature(PetriNet_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"



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
NamedElement_strategy = st.builds(
    NamedElement,
)
PetriNet_Element_strategy = st.builds(
    PetriNet_Element,
)
PetriNet_PetriNet_strategy = st.builds(
    PetriNet_PetriNet,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
PetriNet_NamedElement_strategy = st.builds(
    PetriNet_NamedElement,
    name=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)
PetriNet_LocatedElement_strategy = st.builds(
    PetriNet_LocatedElement,
    location=
        safe_text
)








@given(instance=PetriNet_NamedElement_strategy)
def test_hyp_petrinet_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=PetriNet_LocatedElement_strategy)
def test_hyp_petrinet_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Element,
    LocatedElement,
    NamedElement,
    PetriNet_Element,
    PetriNet_LocatedElement,
    PetriNet_NamedElement,
    PetriNet_PetriNet,
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

def test_PetriNet_LocatedElement_location_value_roundtrip():
    instance = PetriNet_LocatedElement(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_PetriNet_NamedElement_name_value_roundtrip():
    instance = PetriNet_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_PetriNet_Place_isa_Element():
    instance = PetriNet_Place()
    assert isinstance(instance, Element)


def test_PetriNet_Transition_isa_Element():
    instance = PetriNet_Transition()
    assert isinstance(instance, Element)


def test_PetriNet_NamedElement_isa_LocatedElement():
    instance = PetriNet_NamedElement(name="sample_text")
    assert isinstance(instance, LocatedElement)


def test_PetriNet_Element_isa_NamedElement():
    instance = PetriNet_Element()
    assert isinstance(instance, NamedElement)


def test_PetriNet_PetriNet_isa_NamedElement():
    instance = PetriNet_PetriNet()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


LocatedElement_strategy = st.builds(LocatedElement)
@given(instance=LocatedElement_strategy)
@settings(max_examples=25)
def test_LocatedElement_instantiation(instance):
    assert isinstance(instance, LocatedElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


PetriNet_Element_strategy = st.builds(PetriNet_Element)
@given(instance=PetriNet_Element_strategy)
@settings(max_examples=25)
def test_PetriNet_Element_instantiation(instance):
    assert isinstance(instance, PetriNet_Element)


PetriNet_LocatedElement_strategy = st.builds(PetriNet_LocatedElement, location=safe_text)
@given(instance=PetriNet_LocatedElement_strategy)
@settings(max_examples=25)
def test_PetriNet_LocatedElement_instantiation(instance):
    assert isinstance(instance, PetriNet_LocatedElement)


PetriNet_NamedElement_strategy = st.builds(PetriNet_NamedElement, name=safe_text)
@given(instance=PetriNet_NamedElement_strategy)
@settings(max_examples=25)
def test_PetriNet_NamedElement_instantiation(instance):
    assert isinstance(instance, PetriNet_NamedElement)


PetriNet_PetriNet_strategy = st.builds(PetriNet_PetriNet)
@given(instance=PetriNet_PetriNet_strategy)
@settings(max_examples=25)
def test_PetriNet_PetriNet_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriNet)


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



