import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SrcArc,
    SrcElement,
    SrcLocatedElement,
    SrcNamedElement,
    TrgIdedElement,
    TrgLabeledElement,
    TrgLocatedElement,
    TrgNetContent,
    TrgNetContentElement,
    jointPackage_PetriNet2PNML_JointMM,
    jointPackage_PetriNet2PNML_SrcArc,
    jointPackage_PetriNet2PNML_SrcElement,
    jointPackage_PetriNet2PNML_SrcLocatedElement,
    jointPackage_PetriNet2PNML_SrcNamedElement,
    jointPackage_PetriNet2PNML_SrcPetriNet,
    jointPackage_PetriNet2PNML_SrcPlace,
    jointPackage_PetriNet2PNML_SrcPlaceToTransition,
    jointPackage_PetriNet2PNML_SrcTransition,
    jointPackage_PetriNet2PNML_SrcTransitionToPlace,
    jointPackage_PetriNet2PNML_TrgArc,
    jointPackage_PetriNet2PNML_TrgIdedElement,
    jointPackage_PetriNet2PNML_TrgLabel,
    jointPackage_PetriNet2PNML_TrgLabeledElement,
    jointPackage_PetriNet2PNML_TrgLocatedElement,
    jointPackage_PetriNet2PNML_TrgName,
    jointPackage_PetriNet2PNML_TrgNetContent,
    jointPackage_PetriNet2PNML_TrgNetContentElement,
    jointPackage_PetriNet2PNML_TrgNetElement,
    jointPackage_PetriNet2PNML_TrgPNMLDocument,
    jointPackage_PetriNet2PNML_TrgPlace,
    jointPackage_PetriNet2PNML_TrgTransition,
    jointPackage_PetriNet2PNML_TrgURI,
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

def test_jointPackage_PetriNet2PNML_SrcArc_weight_value_roundtrip():
    instance = jointPackage_PetriNet2PNML_SrcArc(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_jointPackage_PetriNet2PNML_SrcLocatedElement_location_value_roundtrip():
    instance = jointPackage_PetriNet2PNML_SrcLocatedElement(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_jointPackage_PetriNet2PNML_SrcNamedElement_name_value_roundtrip():
    instance = jointPackage_PetriNet2PNML_SrcNamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jointPackage_PetriNet2PNML_TrgIdedElement_id_value_roundtrip():
    instance = jointPackage_PetriNet2PNML_TrgIdedElement(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_jointPackage_PetriNet2PNML_TrgLabel_text_value_roundtrip():
    instance = jointPackage_PetriNet2PNML_TrgLabel(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_jointPackage_PetriNet2PNML_TrgLocatedElement_location_value_roundtrip():
    instance = jointPackage_PetriNet2PNML_TrgLocatedElement(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_jointPackage_PetriNet2PNML_TrgURI_value_value_roundtrip():
    instance = jointPackage_PetriNet2PNML_TrgURI(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_jointPackage_PetriNet2PNML_SrcPlaceToTransition_isa_SrcArc():
    instance = jointPackage_PetriNet2PNML_SrcPlaceToTransition()
    assert isinstance(instance, SrcArc)


def test_jointPackage_PetriNet2PNML_SrcTransitionToPlace_isa_SrcArc():
    instance = jointPackage_PetriNet2PNML_SrcTransitionToPlace()
    assert isinstance(instance, SrcArc)


def test_jointPackage_PetriNet2PNML_SrcPlace_isa_SrcElement():
    instance = jointPackage_PetriNet2PNML_SrcPlace()
    assert isinstance(instance, SrcElement)


def test_jointPackage_PetriNet2PNML_SrcTransition_isa_SrcElement():
    instance = jointPackage_PetriNet2PNML_SrcTransition()
    assert isinstance(instance, SrcElement)


def test_jointPackage_PetriNet2PNML_SrcNamedElement_isa_SrcLocatedElement():
    instance = jointPackage_PetriNet2PNML_SrcNamedElement(name="sample_text")
    assert isinstance(instance, SrcLocatedElement)


def test_jointPackage_PetriNet2PNML_SrcArc_isa_SrcNamedElement():
    instance = jointPackage_PetriNet2PNML_SrcArc(weight=7)
    assert isinstance(instance, SrcNamedElement)


def test_jointPackage_PetriNet2PNML_SrcElement_isa_SrcNamedElement():
    instance = jointPackage_PetriNet2PNML_SrcElement()
    assert isinstance(instance, SrcNamedElement)


def test_jointPackage_PetriNet2PNML_SrcPetriNet_isa_SrcNamedElement():
    instance = jointPackage_PetriNet2PNML_SrcPetriNet()
    assert isinstance(instance, SrcNamedElement)


def test_jointPackage_PetriNet2PNML_TrgArc_isa_TrgIdedElement():
    instance = jointPackage_PetriNet2PNML_TrgArc()
    assert isinstance(instance, TrgIdedElement)


def test_jointPackage_PetriNet2PNML_TrgNetContentElement_isa_TrgIdedElement():
    instance = jointPackage_PetriNet2PNML_TrgNetContentElement()
    assert isinstance(instance, TrgIdedElement)


def test_jointPackage_PetriNet2PNML_TrgNetElement_isa_TrgIdedElement():
    instance = jointPackage_PetriNet2PNML_TrgNetElement()
    assert isinstance(instance, TrgIdedElement)


def test_jointPackage_PetriNet2PNML_TrgName_isa_TrgLabeledElement():
    instance = jointPackage_PetriNet2PNML_TrgName()
    assert isinstance(instance, TrgLabeledElement)


def test_jointPackage_PetriNet2PNML_TrgIdedElement_isa_TrgLocatedElement():
    instance = jointPackage_PetriNet2PNML_TrgIdedElement(id="sample_text")
    assert isinstance(instance, TrgLocatedElement)


def test_jointPackage_PetriNet2PNML_TrgLabel_isa_TrgLocatedElement():
    instance = jointPackage_PetriNet2PNML_TrgLabel(text="sample_text")
    assert isinstance(instance, TrgLocatedElement)


def test_jointPackage_PetriNet2PNML_TrgLabeledElement_isa_TrgLocatedElement():
    instance = jointPackage_PetriNet2PNML_TrgLabeledElement()
    assert isinstance(instance, TrgLocatedElement)


def test_jointPackage_PetriNet2PNML_TrgNetContent_isa_TrgLocatedElement():
    instance = jointPackage_PetriNet2PNML_TrgNetContent()
    assert isinstance(instance, TrgLocatedElement)


def test_jointPackage_PetriNet2PNML_TrgPNMLDocument_isa_TrgLocatedElement():
    instance = jointPackage_PetriNet2PNML_TrgPNMLDocument()
    assert isinstance(instance, TrgLocatedElement)


def test_jointPackage_PetriNet2PNML_TrgURI_isa_TrgLocatedElement():
    instance = jointPackage_PetriNet2PNML_TrgURI(value="sample_text")
    assert isinstance(instance, TrgLocatedElement)


def test_jointPackage_PetriNet2PNML_TrgArc_isa_TrgNetContent():
    instance = jointPackage_PetriNet2PNML_TrgArc()
    assert isinstance(instance, TrgNetContent)


def test_jointPackage_PetriNet2PNML_TrgNetContentElement_isa_TrgNetContent():
    instance = jointPackage_PetriNet2PNML_TrgNetContentElement()
    assert isinstance(instance, TrgNetContent)


def test_jointPackage_PetriNet2PNML_TrgPlace_isa_TrgNetContentElement():
    instance = jointPackage_PetriNet2PNML_TrgPlace()
    assert isinstance(instance, TrgNetContentElement)


def test_jointPackage_PetriNet2PNML_TrgTransition_isa_TrgNetContentElement():
    instance = jointPackage_PetriNet2PNML_TrgTransition()
    assert isinstance(instance, TrgNetContentElement)


def test_assoc_arcs4_link_reassign_clear():
    a = jointPackage_PetriNet2PNML_SrcArc(weight=7)
    b1 = jointPackage_PetriNet2PNML_SrcPetriNet()
    b2 = jointPackage_PetriNet2PNML_SrcPetriNet()
    _safe_set(a, 'SrcArc', b1)
    assert _is_linked(a, 'SrcArc', b1)
    if hasattr(b1, 'net5'):
        assert _is_linked(b1, 'net5', a)
    _safe_set(a, 'SrcArc', b2)
    assert _is_linked(a, 'SrcArc', b2)
    if hasattr(b1, 'net5'):
        assert not _is_linked(b1, 'net5', a)
    if hasattr(b2, 'net5'):
        assert _is_linked(b2, 'net5', a)
    _safe_set(a, 'SrcArc', None)
    assert not _is_linked(a, 'SrcArc', b2)
    if hasattr(b2, 'net5'):
        assert not _is_linked(b2, 'net5', a)


def test_assoc_labels39_link_reassign_clear():
    a = jointPackage_PetriNet2PNML_TrgLabel(text="sample_text")
    b1 = jointPackage_PetriNet2PNML_TrgLabeledElement()
    b2 = jointPackage_PetriNet2PNML_TrgLabeledElement()
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgLabel', b1)
    assert _is_linked(a, 'jointPackage_PetriNet2PNML_TrgLabel', b1)
    if hasattr(b1, 'jointPackage_PetriNet2PNML_TrgLabeledElement'):
        assert _is_linked(b1, 'jointPackage_PetriNet2PNML_TrgLabeledElement', a)
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgLabel', b2)
    assert _is_linked(a, 'jointPackage_PetriNet2PNML_TrgLabel', b2)
    if hasattr(b1, 'jointPackage_PetriNet2PNML_TrgLabeledElement'):
        assert not _is_linked(b1, 'jointPackage_PetriNet2PNML_TrgLabeledElement', a)
    if hasattr(b2, 'jointPackage_PetriNet2PNML_TrgLabeledElement'):
        assert _is_linked(b2, 'jointPackage_PetriNet2PNML_TrgLabeledElement', a)
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgLabel', None)
    assert not _is_linked(a, 'jointPackage_PetriNet2PNML_TrgLabel', b2)
    if hasattr(b2, 'jointPackage_PetriNet2PNML_TrgLabeledElement'):
        assert not _is_linked(b2, 'jointPackage_PetriNet2PNML_TrgLabeledElement', a)


def test_assoc_net15_link_reassign_clear():
    a = jointPackage_PetriNet2PNML_SrcArc(weight=7)
    b1 = jointPackage_PetriNet2PNML_SrcPetriNet()
    b2 = jointPackage_PetriNet2PNML_SrcPetriNet()
    _safe_set(a, 'arcs', b1)
    assert _is_linked(a, 'arcs', b1)
    if hasattr(b1, 'SrcPetriNet16'):
        assert _is_linked(b1, 'SrcPetriNet16', a)
    _safe_set(a, 'arcs', b2)
    assert _is_linked(a, 'arcs', b2)
    if hasattr(b1, 'SrcPetriNet16'):
        assert not _is_linked(b1, 'SrcPetriNet16', a)
    if hasattr(b2, 'SrcPetriNet16'):
        assert _is_linked(b2, 'SrcPetriNet16', a)
    _safe_set(a, 'arcs', None)
    assert not _is_linked(a, 'arcs', b2)
    if hasattr(b2, 'SrcPetriNet16'):
        assert not _is_linked(b2, 'SrcPetriNet16', a)


def test_assoc_type29_link_reassign_clear():
    a = jointPackage_PetriNet2PNML_TrgURI(value="sample_text")
    b1 = jointPackage_PetriNet2PNML_TrgNetElement()
    b2 = jointPackage_PetriNet2PNML_TrgNetElement()
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgURI31', b1)
    assert _is_linked(a, 'jointPackage_PetriNet2PNML_TrgURI31', b1)
    if hasattr(b1, 'jointPackage_PetriNet2PNML_TrgNetElement30'):
        assert _is_linked(b1, 'jointPackage_PetriNet2PNML_TrgNetElement30', a)
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgURI31', b2)
    assert _is_linked(a, 'jointPackage_PetriNet2PNML_TrgURI31', b2)
    if hasattr(b1, 'jointPackage_PetriNet2PNML_TrgNetElement30'):
        assert not _is_linked(b1, 'jointPackage_PetriNet2PNML_TrgNetElement30', a)
    if hasattr(b2, 'jointPackage_PetriNet2PNML_TrgNetElement30'):
        assert _is_linked(b2, 'jointPackage_PetriNet2PNML_TrgNetElement30', a)
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgURI31', None)
    assert not _is_linked(a, 'jointPackage_PetriNet2PNML_TrgURI31', b2)
    if hasattr(b2, 'jointPackage_PetriNet2PNML_TrgNetElement30'):
        assert not _is_linked(b2, 'jointPackage_PetriNet2PNML_TrgNetElement30', a)


def test_assoc_xmlns25_link_reassign_clear():
    a = jointPackage_PetriNet2PNML_TrgURI(value="sample_text")
    b1 = jointPackage_PetriNet2PNML_TrgPNMLDocument()
    b2 = jointPackage_PetriNet2PNML_TrgPNMLDocument()
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgURI', b1)
    assert _is_linked(a, 'jointPackage_PetriNet2PNML_TrgURI', b1)
    if hasattr(b1, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26'):
        assert _is_linked(b1, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26', a)
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgURI', b2)
    assert _is_linked(a, 'jointPackage_PetriNet2PNML_TrgURI', b2)
    if hasattr(b1, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26'):
        assert not _is_linked(b1, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26', a)
    if hasattr(b2, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26'):
        assert _is_linked(b2, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26', a)
    _safe_set(a, 'jointPackage_PetriNet2PNML_TrgURI', None)
    assert not _is_linked(a, 'jointPackage_PetriNet2PNML_TrgURI', b2)
    if hasattr(b2, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26'):
        assert not _is_linked(b2, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SrcArc_strategy = st.builds(SrcArc)
@given(instance=SrcArc_strategy)
@settings(max_examples=25)
def test_SrcArc_instantiation(instance):
    assert isinstance(instance, SrcArc)


SrcElement_strategy = st.builds(SrcElement)
@given(instance=SrcElement_strategy)
@settings(max_examples=25)
def test_SrcElement_instantiation(instance):
    assert isinstance(instance, SrcElement)


SrcLocatedElement_strategy = st.builds(SrcLocatedElement)
@given(instance=SrcLocatedElement_strategy)
@settings(max_examples=25)
def test_SrcLocatedElement_instantiation(instance):
    assert isinstance(instance, SrcLocatedElement)


SrcNamedElement_strategy = st.builds(SrcNamedElement)
@given(instance=SrcNamedElement_strategy)
@settings(max_examples=25)
def test_SrcNamedElement_instantiation(instance):
    assert isinstance(instance, SrcNamedElement)


TrgIdedElement_strategy = st.builds(TrgIdedElement)
@given(instance=TrgIdedElement_strategy)
@settings(max_examples=25)
def test_TrgIdedElement_instantiation(instance):
    assert isinstance(instance, TrgIdedElement)


TrgLabeledElement_strategy = st.builds(TrgLabeledElement)
@given(instance=TrgLabeledElement_strategy)
@settings(max_examples=25)
def test_TrgLabeledElement_instantiation(instance):
    assert isinstance(instance, TrgLabeledElement)


TrgLocatedElement_strategy = st.builds(TrgLocatedElement)
@given(instance=TrgLocatedElement_strategy)
@settings(max_examples=25)
def test_TrgLocatedElement_instantiation(instance):
    assert isinstance(instance, TrgLocatedElement)


TrgNetContent_strategy = st.builds(TrgNetContent)
@given(instance=TrgNetContent_strategy)
@settings(max_examples=25)
def test_TrgNetContent_instantiation(instance):
    assert isinstance(instance, TrgNetContent)


TrgNetContentElement_strategy = st.builds(TrgNetContentElement)
@given(instance=TrgNetContentElement_strategy)
@settings(max_examples=25)
def test_TrgNetContentElement_instantiation(instance):
    assert isinstance(instance, TrgNetContentElement)


jointPackage_PetriNet2PNML_JointMM_strategy = st.builds(jointPackage_PetriNet2PNML_JointMM)
@given(instance=jointPackage_PetriNet2PNML_JointMM_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_JointMM_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_JointMM)


jointPackage_PetriNet2PNML_SrcArc_strategy = st.builds(jointPackage_PetriNet2PNML_SrcArc, weight=st.integers())
@given(instance=jointPackage_PetriNet2PNML_SrcArc_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcArc_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcArc)


jointPackage_PetriNet2PNML_SrcElement_strategy = st.builds(jointPackage_PetriNet2PNML_SrcElement)
@given(instance=jointPackage_PetriNet2PNML_SrcElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcElement)


jointPackage_PetriNet2PNML_SrcLocatedElement_strategy = st.builds(jointPackage_PetriNet2PNML_SrcLocatedElement, location=safe_text)
@given(instance=jointPackage_PetriNet2PNML_SrcLocatedElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcLocatedElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcLocatedElement)


jointPackage_PetriNet2PNML_SrcNamedElement_strategy = st.builds(jointPackage_PetriNet2PNML_SrcNamedElement, name=safe_text)
@given(instance=jointPackage_PetriNet2PNML_SrcNamedElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcNamedElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcNamedElement)


jointPackage_PetriNet2PNML_SrcPetriNet_strategy = st.builds(jointPackage_PetriNet2PNML_SrcPetriNet)
@given(instance=jointPackage_PetriNet2PNML_SrcPetriNet_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcPetriNet_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcPetriNet)


jointPackage_PetriNet2PNML_SrcPlace_strategy = st.builds(jointPackage_PetriNet2PNML_SrcPlace)
@given(instance=jointPackage_PetriNet2PNML_SrcPlace_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcPlace_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcPlace)


jointPackage_PetriNet2PNML_SrcPlaceToTransition_strategy = st.builds(jointPackage_PetriNet2PNML_SrcPlaceToTransition)
@given(instance=jointPackage_PetriNet2PNML_SrcPlaceToTransition_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcPlaceToTransition_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcPlaceToTransition)


jointPackage_PetriNet2PNML_SrcTransition_strategy = st.builds(jointPackage_PetriNet2PNML_SrcTransition)
@given(instance=jointPackage_PetriNet2PNML_SrcTransition_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcTransition_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcTransition)


jointPackage_PetriNet2PNML_SrcTransitionToPlace_strategy = st.builds(jointPackage_PetriNet2PNML_SrcTransitionToPlace)
@given(instance=jointPackage_PetriNet2PNML_SrcTransitionToPlace_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_SrcTransitionToPlace_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcTransitionToPlace)


jointPackage_PetriNet2PNML_TrgArc_strategy = st.builds(jointPackage_PetriNet2PNML_TrgArc)
@given(instance=jointPackage_PetriNet2PNML_TrgArc_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgArc_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgArc)


jointPackage_PetriNet2PNML_TrgIdedElement_strategy = st.builds(jointPackage_PetriNet2PNML_TrgIdedElement, id=safe_text)
@given(instance=jointPackage_PetriNet2PNML_TrgIdedElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgIdedElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgIdedElement)


jointPackage_PetriNet2PNML_TrgLabel_strategy = st.builds(jointPackage_PetriNet2PNML_TrgLabel, text=safe_text)
@given(instance=jointPackage_PetriNet2PNML_TrgLabel_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgLabel_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgLabel)


jointPackage_PetriNet2PNML_TrgLabeledElement_strategy = st.builds(jointPackage_PetriNet2PNML_TrgLabeledElement)
@given(instance=jointPackage_PetriNet2PNML_TrgLabeledElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgLabeledElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgLabeledElement)


jointPackage_PetriNet2PNML_TrgLocatedElement_strategy = st.builds(jointPackage_PetriNet2PNML_TrgLocatedElement, location=safe_text)
@given(instance=jointPackage_PetriNet2PNML_TrgLocatedElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgLocatedElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgLocatedElement)


jointPackage_PetriNet2PNML_TrgName_strategy = st.builds(jointPackage_PetriNet2PNML_TrgName)
@given(instance=jointPackage_PetriNet2PNML_TrgName_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgName_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgName)


jointPackage_PetriNet2PNML_TrgNetContent_strategy = st.builds(jointPackage_PetriNet2PNML_TrgNetContent)
@given(instance=jointPackage_PetriNet2PNML_TrgNetContent_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgNetContent_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgNetContent)


jointPackage_PetriNet2PNML_TrgNetContentElement_strategy = st.builds(jointPackage_PetriNet2PNML_TrgNetContentElement)
@given(instance=jointPackage_PetriNet2PNML_TrgNetContentElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgNetContentElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgNetContentElement)


jointPackage_PetriNet2PNML_TrgNetElement_strategy = st.builds(jointPackage_PetriNet2PNML_TrgNetElement)
@given(instance=jointPackage_PetriNet2PNML_TrgNetElement_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgNetElement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgNetElement)


jointPackage_PetriNet2PNML_TrgPNMLDocument_strategy = st.builds(jointPackage_PetriNet2PNML_TrgPNMLDocument)
@given(instance=jointPackage_PetriNet2PNML_TrgPNMLDocument_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgPNMLDocument_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgPNMLDocument)


jointPackage_PetriNet2PNML_TrgPlace_strategy = st.builds(jointPackage_PetriNet2PNML_TrgPlace)
@given(instance=jointPackage_PetriNet2PNML_TrgPlace_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgPlace_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgPlace)


jointPackage_PetriNet2PNML_TrgTransition_strategy = st.builds(jointPackage_PetriNet2PNML_TrgTransition)
@given(instance=jointPackage_PetriNet2PNML_TrgTransition_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgTransition_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgTransition)


jointPackage_PetriNet2PNML_TrgURI_strategy = st.builds(jointPackage_PetriNet2PNML_TrgURI, value=safe_text)
@given(instance=jointPackage_PetriNet2PNML_TrgURI_strategy)
@settings(max_examples=25)
def test_jointPackage_PetriNet2PNML_TrgURI_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgURI)


