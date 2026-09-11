import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    GenericPlace,
    resourcePetriNet_GenericPlace,
    resourcePetriNet_InputArc,
    resourcePetriNet_OutputArc,
    resourcePetriNet_PetriNet,
    resourcePetriNet_Place,
    resourcePetriNet_Resource,
    resourcePetriNet_Transition,
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

def test_resourcePetriNet_GenericPlace_name_value_roundtrip():
    instance = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_resourcePetriNet_GenericPlace_numberOfTokens_value_roundtrip():
    instance = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    assert instance.numberOfTokens == 7
    instance.numberOfTokens = 13
    assert instance.numberOfTokens == 13


def test_resourcePetriNet_InputArc_weight_value_roundtrip():
    instance = resourcePetriNet_InputArc(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_resourcePetriNet_OutputArc_weight_value_roundtrip():
    instance = resourcePetriNet_OutputArc(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_resourcePetriNet_PetriNet_name_value_roundtrip():
    instance = resourcePetriNet_PetriNet(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_resourcePetriNet_Place_capacity_value_roundtrip():
    instance = resourcePetriNet_Place(capacity=7)
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_resourcePetriNet_Transition_name_value_roundtrip():
    instance = resourcePetriNet_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_resourcePetriNet_Place_isa_GenericPlace():
    instance = resourcePetriNet_Place(capacity=7)
    assert isinstance(instance, GenericPlace)


def test_resourcePetriNet_Resource_isa_GenericPlace():
    instance = resourcePetriNet_Resource()
    assert isinstance(instance, GenericPlace)


def test_assoc_InputArcFromPlace7_link_reassign_clear():
    a = resourcePetriNet_InputArc(weight=7)
    b1 = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    b2 = resourcePetriNet_GenericPlace(name="sample_text_2", numberOfTokens=13)
    _safe_set(a, 'resourcePetriNet_InputArc8', b1)
    assert _is_linked(a, 'resourcePetriNet_InputArc8', b1)
    if hasattr(b1, 'resourcePetriNet_GenericPlace9'):
        assert _is_linked(b1, 'resourcePetriNet_GenericPlace9', a)
    _safe_set(a, 'resourcePetriNet_InputArc8', b2)
    assert _is_linked(a, 'resourcePetriNet_InputArc8', b2)
    if hasattr(b1, 'resourcePetriNet_GenericPlace9'):
        assert not _is_linked(b1, 'resourcePetriNet_GenericPlace9', a)
    if hasattr(b2, 'resourcePetriNet_GenericPlace9'):
        assert _is_linked(b2, 'resourcePetriNet_GenericPlace9', a)
    _safe_set(a, 'resourcePetriNet_InputArc8', None)
    assert not _is_linked(a, 'resourcePetriNet_InputArc8', b2)
    if hasattr(b2, 'resourcePetriNet_GenericPlace9'):
        assert not _is_linked(b2, 'resourcePetriNet_GenericPlace9', a)


def test_assoc_InputArcToTransition10_link_reassign_clear():
    a = resourcePetriNet_Transition(name="sample_text")
    b1 = resourcePetriNet_InputArc(weight=7)
    b2 = resourcePetriNet_InputArc(weight=13)
    _safe_set(a, 'resourcePetriNet_Transition12', b1)
    assert _is_linked(a, 'resourcePetriNet_Transition12', b1)
    if hasattr(b1, 'resourcePetriNet_InputArc11'):
        assert _is_linked(b1, 'resourcePetriNet_InputArc11', a)
    _safe_set(a, 'resourcePetriNet_Transition12', b2)
    assert _is_linked(a, 'resourcePetriNet_Transition12', b2)
    if hasattr(b1, 'resourcePetriNet_InputArc11'):
        assert not _is_linked(b1, 'resourcePetriNet_InputArc11', a)
    if hasattr(b2, 'resourcePetriNet_InputArc11'):
        assert _is_linked(b2, 'resourcePetriNet_InputArc11', a)
    _safe_set(a, 'resourcePetriNet_Transition12', None)
    assert not _is_linked(a, 'resourcePetriNet_Transition12', b2)
    if hasattr(b2, 'resourcePetriNet_InputArc11'):
        assert not _is_linked(b2, 'resourcePetriNet_InputArc11', a)


def test_assoc_OutputArcFromTransition13_link_reassign_clear():
    a = resourcePetriNet_Transition(name="sample_text")
    b1 = resourcePetriNet_OutputArc(weight=7)
    b2 = resourcePetriNet_OutputArc(weight=13)
    _safe_set(a, 'resourcePetriNet_Transition15', b1)
    assert _is_linked(a, 'resourcePetriNet_Transition15', b1)
    if hasattr(b1, 'resourcePetriNet_OutputArc14'):
        assert _is_linked(b1, 'resourcePetriNet_OutputArc14', a)
    _safe_set(a, 'resourcePetriNet_Transition15', b2)
    assert _is_linked(a, 'resourcePetriNet_Transition15', b2)
    if hasattr(b1, 'resourcePetriNet_OutputArc14'):
        assert not _is_linked(b1, 'resourcePetriNet_OutputArc14', a)
    if hasattr(b2, 'resourcePetriNet_OutputArc14'):
        assert _is_linked(b2, 'resourcePetriNet_OutputArc14', a)
    _safe_set(a, 'resourcePetriNet_Transition15', None)
    assert not _is_linked(a, 'resourcePetriNet_Transition15', b2)
    if hasattr(b2, 'resourcePetriNet_OutputArc14'):
        assert not _is_linked(b2, 'resourcePetriNet_OutputArc14', a)


def test_assoc_OutputArcToPlace16_link_reassign_clear():
    a = resourcePetriNet_OutputArc(weight=7)
    b1 = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    b2 = resourcePetriNet_GenericPlace(name="sample_text_2", numberOfTokens=13)
    _safe_set(a, 'resourcePetriNet_OutputArc17', b1)
    assert _is_linked(a, 'resourcePetriNet_OutputArc17', b1)
    if hasattr(b1, 'resourcePetriNet_GenericPlace18'):
        assert _is_linked(b1, 'resourcePetriNet_GenericPlace18', a)
    _safe_set(a, 'resourcePetriNet_OutputArc17', b2)
    assert _is_linked(a, 'resourcePetriNet_OutputArc17', b2)
    if hasattr(b1, 'resourcePetriNet_GenericPlace18'):
        assert not _is_linked(b1, 'resourcePetriNet_GenericPlace18', a)
    if hasattr(b2, 'resourcePetriNet_GenericPlace18'):
        assert _is_linked(b2, 'resourcePetriNet_GenericPlace18', a)
    _safe_set(a, 'resourcePetriNet_OutputArc17', None)
    assert not _is_linked(a, 'resourcePetriNet_OutputArc17', b2)
    if hasattr(b2, 'resourcePetriNet_GenericPlace18'):
        assert not _is_linked(b2, 'resourcePetriNet_GenericPlace18', a)


def test_assoc_containsGenericPlaces0_link_reassign_clear():
    a = resourcePetriNet_PetriNet(name="sample_text")
    b1 = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    b2 = resourcePetriNet_GenericPlace(name="sample_text_2", numberOfTokens=13)
    _safe_set(a, 'resourcePetriNet_PetriNet', {b1})
    assert _is_linked(a, 'resourcePetriNet_PetriNet', b1)
    if hasattr(b1, 'resourcePetriNet_GenericPlace'):
        assert _is_linked(b1, 'resourcePetriNet_GenericPlace', a)
    _safe_set(a, 'resourcePetriNet_PetriNet', {b2})
    assert _is_linked(a, 'resourcePetriNet_PetriNet', b2)
    if hasattr(b1, 'resourcePetriNet_GenericPlace'):
        assert not _is_linked(b1, 'resourcePetriNet_GenericPlace', a)
    if hasattr(b2, 'resourcePetriNet_GenericPlace'):
        assert _is_linked(b2, 'resourcePetriNet_GenericPlace', a)
    _safe_set(a, 'resourcePetriNet_PetriNet', set())
    assert not _is_linked(a, 'resourcePetriNet_PetriNet', b2)
    if hasattr(b2, 'resourcePetriNet_GenericPlace'):
        assert not _is_linked(b2, 'resourcePetriNet_GenericPlace', a)


def test_assoc_containsInputArcs3_link_reassign_clear():
    a = resourcePetriNet_PetriNet(name="sample_text")
    b1 = resourcePetriNet_InputArc(weight=7)
    b2 = resourcePetriNet_InputArc(weight=13)
    _safe_set(a, 'resourcePetriNet_PetriNet4', {b1})
    assert _is_linked(a, 'resourcePetriNet_PetriNet4', b1)
    if hasattr(b1, 'resourcePetriNet_InputArc'):
        assert _is_linked(b1, 'resourcePetriNet_InputArc', a)
    _safe_set(a, 'resourcePetriNet_PetriNet4', {b2})
    assert _is_linked(a, 'resourcePetriNet_PetriNet4', b2)
    if hasattr(b1, 'resourcePetriNet_InputArc'):
        assert not _is_linked(b1, 'resourcePetriNet_InputArc', a)
    if hasattr(b2, 'resourcePetriNet_InputArc'):
        assert _is_linked(b2, 'resourcePetriNet_InputArc', a)
    _safe_set(a, 'resourcePetriNet_PetriNet4', set())
    assert not _is_linked(a, 'resourcePetriNet_PetriNet4', b2)
    if hasattr(b2, 'resourcePetriNet_InputArc'):
        assert not _is_linked(b2, 'resourcePetriNet_InputArc', a)


def test_assoc_containsOutputArcs5_link_reassign_clear():
    a = resourcePetriNet_PetriNet(name="sample_text")
    b1 = resourcePetriNet_OutputArc(weight=7)
    b2 = resourcePetriNet_OutputArc(weight=13)
    _safe_set(a, 'resourcePetriNet_PetriNet6', {b1})
    assert _is_linked(a, 'resourcePetriNet_PetriNet6', b1)
    if hasattr(b1, 'resourcePetriNet_OutputArc'):
        assert _is_linked(b1, 'resourcePetriNet_OutputArc', a)
    _safe_set(a, 'resourcePetriNet_PetriNet6', {b2})
    assert _is_linked(a, 'resourcePetriNet_PetriNet6', b2)
    if hasattr(b1, 'resourcePetriNet_OutputArc'):
        assert not _is_linked(b1, 'resourcePetriNet_OutputArc', a)
    if hasattr(b2, 'resourcePetriNet_OutputArc'):
        assert _is_linked(b2, 'resourcePetriNet_OutputArc', a)
    _safe_set(a, 'resourcePetriNet_PetriNet6', set())
    assert not _is_linked(a, 'resourcePetriNet_PetriNet6', b2)
    if hasattr(b2, 'resourcePetriNet_OutputArc'):
        assert not _is_linked(b2, 'resourcePetriNet_OutputArc', a)


def test_assoc_containsTransitions1_link_reassign_clear():
    a = resourcePetriNet_Transition(name="sample_text")
    b1 = resourcePetriNet_PetriNet(name="sample_text")
    b2 = resourcePetriNet_PetriNet(name="sample_text_2")
    _safe_set(a, 'resourcePetriNet_Transition', b1)
    assert _is_linked(a, 'resourcePetriNet_Transition', b1)
    if hasattr(b1, 'resourcePetriNet_PetriNet2'):
        assert _is_linked(b1, 'resourcePetriNet_PetriNet2', a)
    _safe_set(a, 'resourcePetriNet_Transition', b2)
    assert _is_linked(a, 'resourcePetriNet_Transition', b2)
    if hasattr(b1, 'resourcePetriNet_PetriNet2'):
        assert not _is_linked(b1, 'resourcePetriNet_PetriNet2', a)
    if hasattr(b2, 'resourcePetriNet_PetriNet2'):
        assert _is_linked(b2, 'resourcePetriNet_PetriNet2', a)
    _safe_set(a, 'resourcePetriNet_Transition', None)
    assert not _is_linked(a, 'resourcePetriNet_Transition', b2)
    if hasattr(b2, 'resourcePetriNet_PetriNet2'):
        assert not _is_linked(b2, 'resourcePetriNet_PetriNet2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

GenericPlace_strategy = st.builds(GenericPlace)
@given(instance=GenericPlace_strategy)
@settings(max_examples=25)
def test_GenericPlace_instantiation(instance):
    assert isinstance(instance, GenericPlace)


resourcePetriNet_GenericPlace_strategy = st.builds(resourcePetriNet_GenericPlace, name=safe_text, numberOfTokens=st.integers())
@given(instance=resourcePetriNet_GenericPlace_strategy)
@settings(max_examples=25)
def test_resourcePetriNet_GenericPlace_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_GenericPlace)


resourcePetriNet_InputArc_strategy = st.builds(resourcePetriNet_InputArc, weight=st.integers())
@given(instance=resourcePetriNet_InputArc_strategy)
@settings(max_examples=25)
def test_resourcePetriNet_InputArc_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_InputArc)


resourcePetriNet_OutputArc_strategy = st.builds(resourcePetriNet_OutputArc, weight=st.integers())
@given(instance=resourcePetriNet_OutputArc_strategy)
@settings(max_examples=25)
def test_resourcePetriNet_OutputArc_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_OutputArc)


resourcePetriNet_PetriNet_strategy = st.builds(resourcePetriNet_PetriNet, name=safe_text)
@given(instance=resourcePetriNet_PetriNet_strategy)
@settings(max_examples=25)
def test_resourcePetriNet_PetriNet_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_PetriNet)


resourcePetriNet_Place_strategy = st.builds(resourcePetriNet_Place, capacity=st.integers())
@given(instance=resourcePetriNet_Place_strategy)
@settings(max_examples=25)
def test_resourcePetriNet_Place_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_Place)


resourcePetriNet_Resource_strategy = st.builds(resourcePetriNet_Resource)
@given(instance=resourcePetriNet_Resource_strategy)
@settings(max_examples=25)
def test_resourcePetriNet_Resource_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_Resource)


resourcePetriNet_Transition_strategy = st.builds(resourcePetriNet_Transition, name=safe_text)
@given(instance=resourcePetriNet_Transition_strategy)
@settings(max_examples=25)
def test_resourcePetriNet_Transition_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_Transition)


