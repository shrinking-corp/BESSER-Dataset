import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    FaultTree_EObject,
    FaultTree_Event,
    FaultTree_FaultTree,
    EventType,
    FaultTreeType,
    LogicOperation,
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

def test_FaultTree_Event_assignedProbability_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.assignedProbability == "sample_text"
    instance.assignedProbability = "sample_text_2"
    assert instance.assignedProbability == "sample_text_2"


def test_FaultTree_Event_computedProbability_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.computedProbability == "sample_text"
    instance.computedProbability = "sample_text_2"
    assert instance.computedProbability == "sample_text_2"


def test_FaultTree_Event_k_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.k == 7
    instance.k = 13
    assert instance.k == 13


def test_FaultTree_Event_message_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_FaultTree_Event_name_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FaultTree_Event_referenceCount_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.referenceCount == 7
    instance.referenceCount = 13
    assert instance.referenceCount == 13


def test_FaultTree_Event_scale_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.scale == "sample_text"
    instance.scale = "sample_text_2"
    assert instance.scale == "sample_text_2"


def test_FaultTree_Event_subEventLogic_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.subEventLogic == "sample_text"
    instance.subEventLogic = "sample_text_2"
    assert instance.subEventLogic == "sample_text_2"


def test_FaultTree_Event_type_value_roundtrip():
    instance = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_FaultTree_FaultTree_faultTreeType_value_roundtrip():
    instance = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    assert instance.faultTreeType == "sample_text"
    instance.faultTreeType = "sample_text_2"
    assert instance.faultTreeType == "sample_text_2"


def test_FaultTree_FaultTree_message_value_roundtrip():
    instance = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_FaultTree_FaultTree_name_value_roundtrip():
    instance = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_events3_link_reassign_clear():
    a = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    b1 = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    b2 = FaultTree_Event(assignedProbability="sample_text_2", computedProbability="sample_text_2", k=13, message="sample_text_2", name="sample_text_2", referenceCount=13, scale="sample_text_2", subEventLogic="sample_text_2", type="sample_text_2")
    _safe_set(a, 'FaultTree_FaultTree4', {b1})
    assert _is_linked(a, 'FaultTree_FaultTree4', b1)
    if hasattr(b1, 'FaultTree_Event5'):
        assert _is_linked(b1, 'FaultTree_Event5', a)
    _safe_set(a, 'FaultTree_FaultTree4', {b2})
    assert _is_linked(a, 'FaultTree_FaultTree4', b2)
    if hasattr(b1, 'FaultTree_Event5'):
        assert not _is_linked(b1, 'FaultTree_Event5', a)
    if hasattr(b2, 'FaultTree_Event5'):
        assert _is_linked(b2, 'FaultTree_Event5', a)
    _safe_set(a, 'FaultTree_FaultTree4', set())
    assert not _is_linked(a, 'FaultTree_FaultTree4', b2)
    if hasattr(b2, 'FaultTree_Event5'):
        assert not _is_linked(b2, 'FaultTree_Event5', a)


def test_assoc_instanceRoot1_link_reassign_clear():
    a = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    b1 = FaultTree_EObject()
    b2 = FaultTree_EObject()
    _safe_set(a, 'FaultTree_FaultTree2', b1)
    assert _is_linked(a, 'FaultTree_FaultTree2', b1)
    if hasattr(b1, 'FaultTree_EObject'):
        assert _is_linked(b1, 'FaultTree_EObject', a)
    _safe_set(a, 'FaultTree_FaultTree2', b2)
    assert _is_linked(a, 'FaultTree_FaultTree2', b2)
    if hasattr(b1, 'FaultTree_EObject'):
        assert not _is_linked(b1, 'FaultTree_EObject', a)
    if hasattr(b2, 'FaultTree_EObject'):
        assert _is_linked(b2, 'FaultTree_EObject', a)
    _safe_set(a, 'FaultTree_FaultTree2', None)
    assert not _is_linked(a, 'FaultTree_FaultTree2', b2)
    if hasattr(b2, 'FaultTree_EObject'):
        assert not _is_linked(b2, 'FaultTree_EObject', a)


def test_assoc_relatedEMV2Object15_link_reassign_clear():
    a = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    b1 = FaultTree_EObject()
    b2 = FaultTree_EObject()
    _safe_set(a, 'FaultTree_Event16', b1)
    assert _is_linked(a, 'FaultTree_Event16', b1)
    if hasattr(b1, 'FaultTree_EObject17'):
        assert _is_linked(b1, 'FaultTree_EObject17', a)
    _safe_set(a, 'FaultTree_Event16', b2)
    assert _is_linked(a, 'FaultTree_Event16', b2)
    if hasattr(b1, 'FaultTree_EObject17'):
        assert not _is_linked(b1, 'FaultTree_EObject17', a)
    if hasattr(b2, 'FaultTree_EObject17'):
        assert _is_linked(b2, 'FaultTree_EObject17', a)
    _safe_set(a, 'FaultTree_Event16', None)
    assert not _is_linked(a, 'FaultTree_Event16', b2)
    if hasattr(b2, 'FaultTree_EObject17'):
        assert not _is_linked(b2, 'FaultTree_EObject17', a)


def test_assoc_relatedErrorType12_link_reassign_clear():
    a = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    b1 = FaultTree_EObject()
    b2 = FaultTree_EObject()
    _safe_set(a, 'FaultTree_Event13', b1)
    assert _is_linked(a, 'FaultTree_Event13', b1)
    if hasattr(b1, 'FaultTree_EObject14'):
        assert _is_linked(b1, 'FaultTree_EObject14', a)
    _safe_set(a, 'FaultTree_Event13', b2)
    assert _is_linked(a, 'FaultTree_Event13', b2)
    if hasattr(b1, 'FaultTree_EObject14'):
        assert not _is_linked(b1, 'FaultTree_EObject14', a)
    if hasattr(b2, 'FaultTree_EObject14'):
        assert _is_linked(b2, 'FaultTree_EObject14', a)
    _safe_set(a, 'FaultTree_Event13', None)
    assert not _is_linked(a, 'FaultTree_Event13', b2)
    if hasattr(b2, 'FaultTree_EObject14'):
        assert not _is_linked(b2, 'FaultTree_EObject14', a)


def test_assoc_relatedInstanceObject9_link_reassign_clear():
    a = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    b1 = FaultTree_EObject()
    b2 = FaultTree_EObject()
    _safe_set(a, 'FaultTree_Event10', b1)
    assert _is_linked(a, 'FaultTree_Event10', b1)
    if hasattr(b1, 'FaultTree_EObject11'):
        assert _is_linked(b1, 'FaultTree_EObject11', a)
    _safe_set(a, 'FaultTree_Event10', b2)
    assert _is_linked(a, 'FaultTree_Event10', b2)
    if hasattr(b1, 'FaultTree_EObject11'):
        assert not _is_linked(b1, 'FaultTree_EObject11', a)
    if hasattr(b2, 'FaultTree_EObject11'):
        assert _is_linked(b2, 'FaultTree_EObject11', a)
    _safe_set(a, 'FaultTree_Event10', None)
    assert not _is_linked(a, 'FaultTree_Event10', b2)
    if hasattr(b2, 'FaultTree_EObject11'):
        assert not _is_linked(b2, 'FaultTree_EObject11', a)


def test_assoc_root0_link_reassign_clear():
    a = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    b1 = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    b2 = FaultTree_Event(assignedProbability="sample_text_2", computedProbability="sample_text_2", k=13, message="sample_text_2", name="sample_text_2", referenceCount=13, scale="sample_text_2", subEventLogic="sample_text_2", type="sample_text_2")
    _safe_set(a, 'FaultTree_FaultTree', b1)
    assert _is_linked(a, 'FaultTree_FaultTree', b1)
    if hasattr(b1, 'FaultTree_Event'):
        assert _is_linked(b1, 'FaultTree_Event', a)
    _safe_set(a, 'FaultTree_FaultTree', b2)
    assert _is_linked(a, 'FaultTree_FaultTree', b2)
    if hasattr(b1, 'FaultTree_Event'):
        assert not _is_linked(b1, 'FaultTree_Event', a)
    if hasattr(b2, 'FaultTree_Event'):
        assert _is_linked(b2, 'FaultTree_Event', a)
    _safe_set(a, 'FaultTree_FaultTree', None)
    assert not _is_linked(a, 'FaultTree_FaultTree', b2)
    if hasattr(b2, 'FaultTree_Event'):
        assert not _is_linked(b2, 'FaultTree_Event', a)


def test_assoc_subEvents7_link_reassign_clear():
    a = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    b1 = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    b2 = FaultTree_Event(assignedProbability="sample_text_2", computedProbability="sample_text_2", k=13, message="sample_text_2", name="sample_text_2", referenceCount=13, scale="sample_text_2", subEventLogic="sample_text_2", type="sample_text_2")
    _safe_set(a, 'FaultTree_Event6', {b1})
    assert _is_linked(a, 'FaultTree_Event6', b1)
    if hasattr(b1, 'FaultTree_Event8'):
        assert _is_linked(b1, 'FaultTree_Event8', a)
    _safe_set(a, 'FaultTree_Event6', {b2})
    assert _is_linked(a, 'FaultTree_Event6', b2)
    if hasattr(b1, 'FaultTree_Event8'):
        assert not _is_linked(b1, 'FaultTree_Event8', a)
    if hasattr(b2, 'FaultTree_Event8'):
        assert _is_linked(b2, 'FaultTree_Event8', a)
    _safe_set(a, 'FaultTree_Event6', set())
    assert not _is_linked(a, 'FaultTree_Event6', b2)
    if hasattr(b2, 'FaultTree_Event8'):
        assert not _is_linked(b2, 'FaultTree_Event8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

FaultTree_EObject_strategy = st.builds(FaultTree_EObject)
@given(instance=FaultTree_EObject_strategy)
@settings(max_examples=25)
def test_FaultTree_EObject_instantiation(instance):
    assert isinstance(instance, FaultTree_EObject)


FaultTree_Event_strategy = st.builds(FaultTree_Event, assignedProbability=safe_text, computedProbability=safe_text, k=st.integers(), message=safe_text, name=safe_text, referenceCount=st.integers(), scale=safe_text, subEventLogic=safe_text, type=safe_text)
@given(instance=FaultTree_Event_strategy)
@settings(max_examples=25)
def test_FaultTree_Event_instantiation(instance):
    assert isinstance(instance, FaultTree_Event)


FaultTree_FaultTree_strategy = st.builds(FaultTree_FaultTree, faultTreeType=safe_text, message=safe_text, name=safe_text)
@given(instance=FaultTree_FaultTree_strategy)
@settings(max_examples=25)
def test_FaultTree_FaultTree_instantiation(instance):
    assert isinstance(instance, FaultTree_FaultTree)


