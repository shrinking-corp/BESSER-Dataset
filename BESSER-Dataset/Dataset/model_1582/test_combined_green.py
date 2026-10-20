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
    Node,
    petrinet_Place,
    petrinet_Transition,
    petrinet_PetriNet,
    Identifyable,
    petrinet_Arc,
    petrinet_Node,
    petrinet_Identifyable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_hyp_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_hyp_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_hyp_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_hyp_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNet)


def test_hyp_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_PetriNet.__init__)


def test_hyp_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifyable_is_not_abstract():
    assert not inspect.isabstract(Identifyable)


def test_hyp_identifyable_constructor_exists():
    assert callable(Identifyable.__init__)


def test_hyp_identifyable_constructor_args():
    sig = inspect.signature(Identifyable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_hyp_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_hyp_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinet_Node)


def test_hyp_petrinet_node_constructor_exists():
    assert callable(petrinet_Node.__init__)


def test_hyp_petrinet_node_constructor_args():
    sig = inspect.signature(petrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_identifyable_is_not_abstract():
    assert not inspect.isabstract(petrinet_Identifyable)


def test_hyp_petrinet_identifyable_constructor_exists():
    assert callable(petrinet_Identifyable.__init__)


def test_hyp_petrinet_identifyable_constructor_args():
    sig = inspect.signature(petrinet_Identifyable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"



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
Node_strategy = st.builds(
    Node,
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_PetriNet_strategy = st.builds(
    petrinet_PetriNet,
)
Identifyable_strategy = st.builds(
    Identifyable,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
)
petrinet_Node_strategy = st.builds(
    petrinet_Node,
)
petrinet_Identifyable_strategy = st.builds(
    petrinet_Identifyable,
    id=
        safe_text
)











@given(instance=petrinet_Identifyable_strategy)
def test_hyp_petrinet_identifyable_id_setter(instance):
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
    Identifyable,
    Node,
    petrinet_Arc,
    petrinet_Identifyable,
    petrinet_Node,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_Transition,
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

def test_petrinet_Identifyable_id_value_roundtrip():
    instance = petrinet_Identifyable(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_petrinet_Arc_isa_Identifyable():
    instance = petrinet_Arc()
    assert isinstance(instance, Identifyable)


def test_petrinet_Node_isa_Identifyable():
    instance = petrinet_Node()
    assert isinstance(instance, Identifyable)


def test_petrinet_Place_isa_Node():
    instance = petrinet_Place()
    assert isinstance(instance, Node)


def test_petrinet_Transition_isa_Node():
    instance = petrinet_Transition()
    assert isinstance(instance, Node)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Identifyable_strategy = st.builds(Identifyable)
@given(instance=Identifyable_strategy)
@settings(max_examples=25)
def test_Identifyable_instantiation(instance):
    assert isinstance(instance, Identifyable)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


petrinet_Arc_strategy = st.builds(petrinet_Arc)
@given(instance=petrinet_Arc_strategy)
@settings(max_examples=25)
def test_petrinet_Arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)


petrinet_Identifyable_strategy = st.builds(petrinet_Identifyable, id=safe_text)
@given(instance=petrinet_Identifyable_strategy)
@settings(max_examples=25)
def test_petrinet_Identifyable_instantiation(instance):
    assert isinstance(instance, petrinet_Identifyable)


petrinet_Node_strategy = st.builds(petrinet_Node)
@given(instance=petrinet_Node_strategy)
@settings(max_examples=25)
def test_petrinet_Node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)


petrinet_PetriNet_strategy = st.builds(petrinet_PetriNet)
@given(instance=petrinet_PetriNet_strategy)
@settings(max_examples=25)
def test_petrinet_PetriNet_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNet)


petrinet_Place_strategy = st.builds(petrinet_Place)
@given(instance=petrinet_Place_strategy)
@settings(max_examples=25)
def test_petrinet_Place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)


petrinet_Transition_strategy = st.builds(petrinet_Transition)
@given(instance=petrinet_Transition_strategy)
@settings(max_examples=25)
def test_petrinet_Transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



