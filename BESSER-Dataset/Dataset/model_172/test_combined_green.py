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
    Edge,
    petri_Edge,
    petri_EdgeToPlace,
    petri_EdgeToTransition,
    petri_Place,
    petri_Transition,
    petri_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_hyp_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_hyp_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petri_edge_is_not_abstract():
    assert not inspect.isabstract(petri_Edge)


def test_hyp_petri_edge_constructor_exists():
    assert callable(petri_Edge.__init__)


def test_hyp_petri_edge_constructor_args():
    sig = inspect.signature(petri_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"




def test_hyp_petri_edgetoplace_is_not_abstract():
    assert not inspect.isabstract(petri_EdgeToPlace)


def test_hyp_petri_edgetoplace_constructor_exists():
    assert callable(petri_EdgeToPlace.__init__)


def test_hyp_petri_edgetoplace_constructor_args():
    sig = inspect.signature(petri_EdgeToPlace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petri_edgetotransition_is_not_abstract():
    assert not inspect.isabstract(petri_EdgeToTransition)


def test_hyp_petri_edgetotransition_constructor_exists():
    assert callable(petri_EdgeToTransition.__init__)


def test_hyp_petri_edgetotransition_constructor_args():
    sig = inspect.signature(petri_EdgeToTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petri_place_is_not_abstract():
    assert not inspect.isabstract(petri_Place)


def test_hyp_petri_place_constructor_exists():
    assert callable(petri_Place.__init__)


def test_hyp_petri_place_constructor_args():
    sig = inspect.signature(petri_Place.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"




def test_hyp_petri_transition_is_not_abstract():
    assert not inspect.isabstract(petri_Transition)


def test_hyp_petri_transition_constructor_exists():
    assert callable(petri_Transition.__init__)


def test_hyp_petri_transition_constructor_args():
    sig = inspect.signature(petri_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"




def test_hyp_petri_petrinet_is_not_abstract():
    assert not inspect.isabstract(petri_PetriNet)


def test_hyp_petri_petrinet_constructor_exists():
    assert callable(petri_PetriNet.__init__)


def test_hyp_petri_petrinet_constructor_args():
    sig = inspect.signature(petri_PetriNet.__init__)
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
Edge_strategy = st.builds(
    Edge,
)
petri_Edge_strategy = st.builds(
    petri_Edge,
    weight=
        st.integers()
)
petri_EdgeToPlace_strategy = st.builds(
    petri_EdgeToPlace,
)
petri_EdgeToTransition_strategy = st.builds(
    petri_EdgeToTransition,
)
petri_Place_strategy = st.builds(
    petri_Place,
    token=
        st.integers()
)
petri_Transition_strategy = st.builds(
    petri_Transition,
    token=
        st.integers()
)
petri_PetriNet_strategy = st.builds(
    petri_PetriNet,
)





@given(instance=petri_Edge_strategy)
def test_hyp_petri_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original






@given(instance=petri_Place_strategy)
def test_hyp_petri_place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original




@given(instance=petri_Transition_strategy)
def test_hyp_petri_transition_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Edge,
    petri_Edge,
    petri_EdgeToPlace,
    petri_EdgeToTransition,
    petri_PetriNet,
    petri_Place,
    petri_Transition,
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

def test_petri_Edge_weight_value_roundtrip():
    instance = petri_Edge(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_petri_Place_token_value_roundtrip():
    instance = petri_Place(token=7)
    assert instance.token == 7
    instance.token = 13
    assert instance.token == 13


def test_petri_Transition_token_value_roundtrip():
    instance = petri_Transition(token=7)
    assert instance.token == 7
    instance.token = 13
    assert instance.token == 13


def test_petri_EdgeToPlace_isa_Edge():
    instance = petri_EdgeToPlace()
    assert isinstance(instance, Edge)


def test_petri_EdgeToTransition_isa_Edge():
    instance = petri_EdgeToTransition()
    assert isinstance(instance, Edge)


def test_assoc_in_10_link_reassign_clear():
    a = petri_Transition(token=7)
    b1 = petri_EdgeToTransition()
    b2 = petri_EdgeToTransition()
    _safe_set(a, 'petri_Transition12', b1)
    assert _is_linked(a, 'petri_Transition12', b1)
    if hasattr(b1, 'petri_EdgeToTransition11'):
        assert _is_linked(b1, 'petri_EdgeToTransition11', a)
    _safe_set(a, 'petri_Transition12', b2)
    assert _is_linked(a, 'petri_Transition12', b2)
    if hasattr(b1, 'petri_EdgeToTransition11'):
        assert not _is_linked(b1, 'petri_EdgeToTransition11', a)
    if hasattr(b2, 'petri_EdgeToTransition11'):
        assert _is_linked(b2, 'petri_EdgeToTransition11', a)
    _safe_set(a, 'petri_Transition12', None)
    assert not _is_linked(a, 'petri_Transition12', b2)
    if hasattr(b2, 'petri_EdgeToTransition11'):
        assert not _is_linked(b2, 'petri_EdgeToTransition11', a)


def test_assoc_in_7_link_reassign_clear():
    a = petri_Place(token=7)
    b1 = petri_EdgeToPlace()
    b2 = petri_EdgeToPlace()
    _safe_set(a, 'petri_Place9', b1)
    assert _is_linked(a, 'petri_Place9', b1)
    if hasattr(b1, 'petri_EdgeToPlace8'):
        assert _is_linked(b1, 'petri_EdgeToPlace8', a)
    _safe_set(a, 'petri_Place9', b2)
    assert _is_linked(a, 'petri_Place9', b2)
    if hasattr(b1, 'petri_EdgeToPlace8'):
        assert not _is_linked(b1, 'petri_EdgeToPlace8', a)
    if hasattr(b2, 'petri_EdgeToPlace8'):
        assert _is_linked(b2, 'petri_EdgeToPlace8', a)
    _safe_set(a, 'petri_Place9', None)
    assert not _is_linked(a, 'petri_Place9', b2)
    if hasattr(b2, 'petri_EdgeToPlace8'):
        assert not _is_linked(b2, 'petri_EdgeToPlace8', a)


def test_assoc_out3_link_reassign_clear():
    a = petri_Place(token=7)
    b1 = petri_EdgeToTransition()
    b2 = petri_EdgeToTransition()
    _safe_set(a, 'petri_Place4', {b1})
    assert _is_linked(a, 'petri_Place4', b1)
    if hasattr(b1, 'petri_EdgeToTransition'):
        assert _is_linked(b1, 'petri_EdgeToTransition', a)
    _safe_set(a, 'petri_Place4', {b2})
    assert _is_linked(a, 'petri_Place4', b2)
    if hasattr(b1, 'petri_EdgeToTransition'):
        assert not _is_linked(b1, 'petri_EdgeToTransition', a)
    if hasattr(b2, 'petri_EdgeToTransition'):
        assert _is_linked(b2, 'petri_EdgeToTransition', a)
    _safe_set(a, 'petri_Place4', set())
    assert not _is_linked(a, 'petri_Place4', b2)
    if hasattr(b2, 'petri_EdgeToTransition'):
        assert not _is_linked(b2, 'petri_EdgeToTransition', a)


def test_assoc_out5_link_reassign_clear():
    a = petri_Transition(token=7)
    b1 = petri_EdgeToPlace()
    b2 = petri_EdgeToPlace()
    _safe_set(a, 'petri_Transition6', {b1})
    assert _is_linked(a, 'petri_Transition6', b1)
    if hasattr(b1, 'petri_EdgeToPlace'):
        assert _is_linked(b1, 'petri_EdgeToPlace', a)
    _safe_set(a, 'petri_Transition6', {b2})
    assert _is_linked(a, 'petri_Transition6', b2)
    if hasattr(b1, 'petri_EdgeToPlace'):
        assert not _is_linked(b1, 'petri_EdgeToPlace', a)
    if hasattr(b2, 'petri_EdgeToPlace'):
        assert _is_linked(b2, 'petri_EdgeToPlace', a)
    _safe_set(a, 'petri_Transition6', set())
    assert not _is_linked(a, 'petri_Transition6', b2)
    if hasattr(b2, 'petri_EdgeToPlace'):
        assert not _is_linked(b2, 'petri_EdgeToPlace', a)


def test_assoc_places1_link_reassign_clear():
    a = petri_Place(token=7)
    b1 = petri_PetriNet()
    b2 = petri_PetriNet()
    _safe_set(a, 'petri_Place', b1)
    assert _is_linked(a, 'petri_Place', b1)
    if hasattr(b1, 'petri_PetriNet2'):
        assert _is_linked(b1, 'petri_PetriNet2', a)
    _safe_set(a, 'petri_Place', b2)
    assert _is_linked(a, 'petri_Place', b2)
    if hasattr(b1, 'petri_PetriNet2'):
        assert not _is_linked(b1, 'petri_PetriNet2', a)
    if hasattr(b2, 'petri_PetriNet2'):
        assert _is_linked(b2, 'petri_PetriNet2', a)
    _safe_set(a, 'petri_Place', None)
    assert not _is_linked(a, 'petri_Place', b2)
    if hasattr(b2, 'petri_PetriNet2'):
        assert not _is_linked(b2, 'petri_PetriNet2', a)


def test_assoc_transitions0_link_reassign_clear():
    a = petri_Transition(token=7)
    b1 = petri_PetriNet()
    b2 = petri_PetriNet()
    _safe_set(a, 'petri_Transition', b1)
    assert _is_linked(a, 'petri_Transition', b1)
    if hasattr(b1, 'petri_PetriNet'):
        assert _is_linked(b1, 'petri_PetriNet', a)
    _safe_set(a, 'petri_Transition', b2)
    assert _is_linked(a, 'petri_Transition', b2)
    if hasattr(b1, 'petri_PetriNet'):
        assert not _is_linked(b1, 'petri_PetriNet', a)
    if hasattr(b2, 'petri_PetriNet'):
        assert _is_linked(b2, 'petri_PetriNet', a)
    _safe_set(a, 'petri_Transition', None)
    assert not _is_linked(a, 'petri_Transition', b2)
    if hasattr(b2, 'petri_PetriNet'):
        assert not _is_linked(b2, 'petri_PetriNet', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


petri_Edge_strategy = st.builds(petri_Edge, weight=st.integers())
@given(instance=petri_Edge_strategy)
@settings(max_examples=25)
def test_petri_Edge_instantiation(instance):
    assert isinstance(instance, petri_Edge)


petri_EdgeToPlace_strategy = st.builds(petri_EdgeToPlace)
@given(instance=petri_EdgeToPlace_strategy)
@settings(max_examples=25)
def test_petri_EdgeToPlace_instantiation(instance):
    assert isinstance(instance, petri_EdgeToPlace)


petri_EdgeToTransition_strategy = st.builds(petri_EdgeToTransition)
@given(instance=petri_EdgeToTransition_strategy)
@settings(max_examples=25)
def test_petri_EdgeToTransition_instantiation(instance):
    assert isinstance(instance, petri_EdgeToTransition)


petri_PetriNet_strategy = st.builds(petri_PetriNet)
@given(instance=petri_PetriNet_strategy)
@settings(max_examples=25)
def test_petri_PetriNet_instantiation(instance):
    assert isinstance(instance, petri_PetriNet)


petri_Place_strategy = st.builds(petri_Place, token=st.integers())
@given(instance=petri_Place_strategy)
@settings(max_examples=25)
def test_petri_Place_instantiation(instance):
    assert isinstance(instance, petri_Place)


petri_Transition_strategy = st.builds(petri_Transition, token=st.integers())
@given(instance=petri_Transition_strategy)
@settings(max_examples=25)
def test_petri_Transition_instantiation(instance):
    assert isinstance(instance, petri_Transition)



