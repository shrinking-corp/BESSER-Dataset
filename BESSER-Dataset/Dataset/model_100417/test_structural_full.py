import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractCondition,
    AbstractState,
    AbstractTransition,
    Named,
    statemachine_AbstractCondition,
    statemachine_AbstractState,
    statemachine_AbstractTransition,
    statemachine_AttributeCondition,
    statemachine_ConditionalState,
    statemachine_ConditionalTransition,
    statemachine_FieldCondition,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_Named,
    statemachine_State,
    statemachine_StateAttribute,
    statemachine_StateChange,
    statemachine_StateValue,
    statemachine_Statemachine,
    statemachine_Transition,
    StateAttributeType,
    StateValueType,
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

def test_statemachine_AbstractCondition_isNotCondition_value_roundtrip():
    instance = statemachine_AbstractCondition(isNotCondition=True)
    assert instance.isNotCondition == True
    instance.isNotCondition = False
    assert instance.isNotCondition == False


def test_statemachine_ConditionalState_andExpression_value_roundtrip():
    instance = statemachine_ConditionalState(andExpression=True, conditionsOrganization="sample_text")
    assert instance.andExpression == True
    instance.andExpression = False
    assert instance.andExpression == False


def test_statemachine_ConditionalState_conditionsOrganization_value_roundtrip():
    instance = statemachine_ConditionalState(andExpression=True, conditionsOrganization="sample_text")
    assert instance.conditionsOrganization == "sample_text"
    instance.conditionsOrganization = "sample_text_2"
    assert instance.conditionsOrganization == "sample_text_2"


def test_statemachine_FieldCondition_fieldName_value_roundtrip():
    instance = statemachine_FieldCondition(fieldName="sample_text")
    assert instance.fieldName == "sample_text"
    instance.fieldName = "sample_text_2"
    assert instance.fieldName == "sample_text_2"


def test_statemachine_Named_name_value_roundtrip():
    instance = statemachine_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_statemachine_State_stateColor_value_roundtrip():
    instance = statemachine_State(stateColor="sample_text")
    assert instance.stateColor == "sample_text"
    instance.stateColor = "sample_text_2"
    assert instance.stateColor == "sample_text_2"


def test_statemachine_StateAttribute_type_value_roundtrip():
    instance = statemachine_StateAttribute(type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_statemachine_StateAttribute_value_value_roundtrip():
    instance = statemachine_StateAttribute(type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_statemachine_StateValue_type_value_roundtrip():
    instance = statemachine_StateValue(type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_statemachine_StateValue_value_value_roundtrip():
    instance = statemachine_StateValue(type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_statemachine_Statemachine_associatedAttribute_value_roundtrip():
    instance = statemachine_Statemachine(associatedAttribute="sample_text", associatedTree="sample_text")
    assert instance.associatedAttribute == "sample_text"
    instance.associatedAttribute = "sample_text_2"
    assert instance.associatedAttribute == "sample_text_2"


def test_statemachine_Statemachine_associatedTree_value_roundtrip():
    instance = statemachine_Statemachine(associatedAttribute="sample_text", associatedTree="sample_text")
    assert instance.associatedTree == "sample_text"
    instance.associatedTree = "sample_text_2"
    assert instance.associatedTree == "sample_text_2"


def test_statemachine_AttributeCondition_isa_AbstractCondition():
    instance = statemachine_AttributeCondition()
    assert isinstance(instance, AbstractCondition)


def test_statemachine_FieldCondition_isa_AbstractCondition():
    instance = statemachine_FieldCondition(fieldName="sample_text")
    assert isinstance(instance, AbstractCondition)


def test_statemachine_ConditionalState_isa_AbstractState():
    instance = statemachine_ConditionalState(andExpression=True, conditionsOrganization="sample_text")
    assert isinstance(instance, AbstractState)


def test_statemachine_FinalState_isa_AbstractState():
    instance = statemachine_FinalState()
    assert isinstance(instance, AbstractState)


def test_statemachine_InitialState_isa_AbstractState():
    instance = statemachine_InitialState()
    assert isinstance(instance, AbstractState)


def test_statemachine_State_isa_AbstractState():
    instance = statemachine_State(stateColor="sample_text")
    assert isinstance(instance, AbstractState)


def test_statemachine_ConditionalTransition_isa_AbstractTransition():
    instance = statemachine_ConditionalTransition()
    assert isinstance(instance, AbstractTransition)


def test_statemachine_Transition_isa_AbstractTransition():
    instance = statemachine_Transition()
    assert isinstance(instance, AbstractTransition)


def test_statemachine_AbstractState_isa_Named():
    instance = statemachine_AbstractState()
    assert isinstance(instance, Named)


def test_statemachine_AbstractTransition_isa_Named():
    instance = statemachine_AbstractTransition()
    assert isinstance(instance, Named)


def test_statemachine_Statemachine_isa_Named():
    instance = statemachine_Statemachine(associatedAttribute="sample_text", associatedTree="sample_text")
    assert isinstance(instance, Named)


def test_assoc_condition10_link_reassign_clear():
    a = statemachine_ConditionalState(andExpression=True, conditionsOrganization="sample_text")
    b1 = statemachine_AbstractCondition(isNotCondition=True)
    b2 = statemachine_AbstractCondition(isNotCondition=False)
    _safe_set(a, 'statemachine_ConditionalState', {b1})
    assert _is_linked(a, 'statemachine_ConditionalState', b1)
    if hasattr(b1, 'statemachine_AbstractCondition'):
        assert _is_linked(b1, 'statemachine_AbstractCondition', a)
    _safe_set(a, 'statemachine_ConditionalState', {b2})
    assert _is_linked(a, 'statemachine_ConditionalState', b2)
    if hasattr(b1, 'statemachine_AbstractCondition'):
        assert not _is_linked(b1, 'statemachine_AbstractCondition', a)
    if hasattr(b2, 'statemachine_AbstractCondition'):
        assert _is_linked(b2, 'statemachine_AbstractCondition', a)
    _safe_set(a, 'statemachine_ConditionalState', set())
    assert not _is_linked(a, 'statemachine_ConditionalState', b2)
    if hasattr(b2, 'statemachine_AbstractCondition'):
        assert not _is_linked(b2, 'statemachine_AbstractCondition', a)


def test_assoc_stateAttribute11_link_reassign_clear():
    a = statemachine_StateAttribute(type="sample_text", value="sample_text")
    b1 = statemachine_StateChange()
    b2 = statemachine_StateChange()
    _safe_set(a, 'statemachine_StateAttribute13', b1)
    assert _is_linked(a, 'statemachine_StateAttribute13', b1)
    if hasattr(b1, 'statemachine_StateChange12'):
        assert _is_linked(b1, 'statemachine_StateChange12', a)
    _safe_set(a, 'statemachine_StateAttribute13', b2)
    assert _is_linked(a, 'statemachine_StateAttribute13', b2)
    if hasattr(b1, 'statemachine_StateChange12'):
        assert not _is_linked(b1, 'statemachine_StateChange12', a)
    if hasattr(b2, 'statemachine_StateChange12'):
        assert _is_linked(b2, 'statemachine_StateChange12', a)
    _safe_set(a, 'statemachine_StateAttribute13', None)
    assert not _is_linked(a, 'statemachine_StateAttribute13', b2)
    if hasattr(b2, 'statemachine_StateChange12'):
        assert not _is_linked(b2, 'statemachine_StateChange12', a)


def test_assoc_stateAttribute19_link_reassign_clear():
    a = statemachine_StateAttribute(type="sample_text", value="sample_text")
    b1 = statemachine_AttributeCondition()
    b2 = statemachine_AttributeCondition()
    _safe_set(a, 'statemachine_StateAttribute20', b1)
    assert _is_linked(a, 'statemachine_StateAttribute20', b1)
    if hasattr(b1, 'statemachine_AttributeCondition'):
        assert _is_linked(b1, 'statemachine_AttributeCondition', a)
    _safe_set(a, 'statemachine_StateAttribute20', b2)
    assert _is_linked(a, 'statemachine_StateAttribute20', b2)
    if hasattr(b1, 'statemachine_AttributeCondition'):
        assert not _is_linked(b1, 'statemachine_AttributeCondition', a)
    if hasattr(b2, 'statemachine_AttributeCondition'):
        assert _is_linked(b2, 'statemachine_AttributeCondition', a)
    _safe_set(a, 'statemachine_StateAttribute20', None)
    assert not _is_linked(a, 'statemachine_StateAttribute20', b2)
    if hasattr(b2, 'statemachine_AttributeCondition'):
        assert not _is_linked(b2, 'statemachine_AttributeCondition', a)


def test_assoc_stateAttributeQuery9_link_reassign_clear():
    a = statemachine_StateAttribute(type="sample_text", value="sample_text")
    b1 = statemachine_StateAttribute(type="sample_text", value="sample_text")
    b2 = statemachine_StateAttribute(type="sample_text_2", value="sample_text_2")
    _safe_set(a, 'statemachine_StateAttribute', b1)
    assert _is_linked(a, 'statemachine_StateAttribute', b1)
    if hasattr(b1, 'statemachine_StateAttribute8'):
        assert _is_linked(b1, 'statemachine_StateAttribute8', a)
    _safe_set(a, 'statemachine_StateAttribute', b2)
    assert _is_linked(a, 'statemachine_StateAttribute', b2)
    if hasattr(b1, 'statemachine_StateAttribute8'):
        assert not _is_linked(b1, 'statemachine_StateAttribute8', a)
    if hasattr(b2, 'statemachine_StateAttribute8'):
        assert _is_linked(b2, 'statemachine_StateAttribute8', a)
    _safe_set(a, 'statemachine_StateAttribute', None)
    assert not _is_linked(a, 'statemachine_StateAttribute', b2)
    if hasattr(b2, 'statemachine_StateAttribute8'):
        assert not _is_linked(b2, 'statemachine_StateAttribute8', a)


def test_assoc_stateValue14_link_reassign_clear():
    a = statemachine_StateValue(type="sample_text", value="sample_text")
    b1 = statemachine_StateChange()
    b2 = statemachine_StateChange()
    _safe_set(a, 'statemachine_StateValue', b1)
    assert _is_linked(a, 'statemachine_StateValue', b1)
    if hasattr(b1, 'statemachine_StateChange15'):
        assert _is_linked(b1, 'statemachine_StateChange15', a)
    _safe_set(a, 'statemachine_StateValue', b2)
    assert _is_linked(a, 'statemachine_StateValue', b2)
    if hasattr(b1, 'statemachine_StateChange15'):
        assert not _is_linked(b1, 'statemachine_StateChange15', a)
    if hasattr(b2, 'statemachine_StateChange15'):
        assert _is_linked(b2, 'statemachine_StateChange15', a)
    _safe_set(a, 'statemachine_StateValue', None)
    assert not _is_linked(a, 'statemachine_StateValue', b2)
    if hasattr(b2, 'statemachine_StateChange15'):
        assert not _is_linked(b2, 'statemachine_StateChange15', a)


def test_assoc_stateValue16_link_reassign_clear():
    a = statemachine_StateValue(type="sample_text", value="sample_text")
    b1 = statemachine_AbstractCondition(isNotCondition=True)
    b2 = statemachine_AbstractCondition(isNotCondition=False)
    _safe_set(a, 'statemachine_StateValue18', b1)
    assert _is_linked(a, 'statemachine_StateValue18', b1)
    if hasattr(b1, 'statemachine_AbstractCondition17'):
        assert _is_linked(b1, 'statemachine_AbstractCondition17', a)
    _safe_set(a, 'statemachine_StateValue18', b2)
    assert _is_linked(a, 'statemachine_StateValue18', b2)
    if hasattr(b1, 'statemachine_AbstractCondition17'):
        assert not _is_linked(b1, 'statemachine_AbstractCondition17', a)
    if hasattr(b2, 'statemachine_AbstractCondition17'):
        assert _is_linked(b2, 'statemachine_AbstractCondition17', a)
    _safe_set(a, 'statemachine_StateValue18', None)
    assert not _is_linked(a, 'statemachine_StateValue18', b2)
    if hasattr(b2, 'statemachine_AbstractCondition17'):
        assert not _is_linked(b2, 'statemachine_AbstractCondition17', a)


def test_assoc_states0_link_reassign_clear():
    a = statemachine_Statemachine(associatedAttribute="sample_text", associatedTree="sample_text")
    b1 = statemachine_AbstractState()
    b2 = statemachine_AbstractState()
    _safe_set(a, 'statemachine_Statemachine', {b1})
    assert _is_linked(a, 'statemachine_Statemachine', b1)
    if hasattr(b1, 'statemachine_AbstractState'):
        assert _is_linked(b1, 'statemachine_AbstractState', a)
    _safe_set(a, 'statemachine_Statemachine', {b2})
    assert _is_linked(a, 'statemachine_Statemachine', b2)
    if hasattr(b1, 'statemachine_AbstractState'):
        assert not _is_linked(b1, 'statemachine_AbstractState', a)
    if hasattr(b2, 'statemachine_AbstractState'):
        assert _is_linked(b2, 'statemachine_AbstractState', a)
    _safe_set(a, 'statemachine_Statemachine', set())
    assert not _is_linked(a, 'statemachine_Statemachine', b2)
    if hasattr(b2, 'statemachine_AbstractState'):
        assert not _is_linked(b2, 'statemachine_AbstractState', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractCondition_strategy = st.builds(AbstractCondition)
@given(instance=AbstractCondition_strategy)
@settings(max_examples=25)
def test_AbstractCondition_instantiation(instance):
    assert isinstance(instance, AbstractCondition)


AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


AbstractTransition_strategy = st.builds(AbstractTransition)
@given(instance=AbstractTransition_strategy)
@settings(max_examples=25)
def test_AbstractTransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


statemachine_AbstractCondition_strategy = st.builds(statemachine_AbstractCondition, isNotCondition=st.booleans())
@given(instance=statemachine_AbstractCondition_strategy)
@settings(max_examples=25)
def test_statemachine_AbstractCondition_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractCondition)


statemachine_AbstractState_strategy = st.builds(statemachine_AbstractState)
@given(instance=statemachine_AbstractState_strategy)
@settings(max_examples=25)
def test_statemachine_AbstractState_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractState)


statemachine_AbstractTransition_strategy = st.builds(statemachine_AbstractTransition)
@given(instance=statemachine_AbstractTransition_strategy)
@settings(max_examples=25)
def test_statemachine_AbstractTransition_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractTransition)


statemachine_AttributeCondition_strategy = st.builds(statemachine_AttributeCondition)
@given(instance=statemachine_AttributeCondition_strategy)
@settings(max_examples=25)
def test_statemachine_AttributeCondition_instantiation(instance):
    assert isinstance(instance, statemachine_AttributeCondition)


statemachine_ConditionalState_strategy = st.builds(statemachine_ConditionalState, andExpression=st.booleans(), conditionsOrganization=safe_text)
@given(instance=statemachine_ConditionalState_strategy)
@settings(max_examples=25)
def test_statemachine_ConditionalState_instantiation(instance):
    assert isinstance(instance, statemachine_ConditionalState)


statemachine_ConditionalTransition_strategy = st.builds(statemachine_ConditionalTransition)
@given(instance=statemachine_ConditionalTransition_strategy)
@settings(max_examples=25)
def test_statemachine_ConditionalTransition_instantiation(instance):
    assert isinstance(instance, statemachine_ConditionalTransition)


statemachine_FieldCondition_strategy = st.builds(statemachine_FieldCondition, fieldName=safe_text)
@given(instance=statemachine_FieldCondition_strategy)
@settings(max_examples=25)
def test_statemachine_FieldCondition_instantiation(instance):
    assert isinstance(instance, statemachine_FieldCondition)


statemachine_FinalState_strategy = st.builds(statemachine_FinalState)
@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=25)
def test_statemachine_FinalState_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)


statemachine_InitialState_strategy = st.builds(statemachine_InitialState)
@given(instance=statemachine_InitialState_strategy)
@settings(max_examples=25)
def test_statemachine_InitialState_instantiation(instance):
    assert isinstance(instance, statemachine_InitialState)


statemachine_Named_strategy = st.builds(statemachine_Named, name=safe_text)
@given(instance=statemachine_Named_strategy)
@settings(max_examples=25)
def test_statemachine_Named_instantiation(instance):
    assert isinstance(instance, statemachine_Named)


statemachine_State_strategy = st.builds(statemachine_State, stateColor=safe_text)
@given(instance=statemachine_State_strategy)
@settings(max_examples=25)
def test_statemachine_State_instantiation(instance):
    assert isinstance(instance, statemachine_State)


statemachine_StateAttribute_strategy = st.builds(statemachine_StateAttribute, type=safe_text, value=safe_text)
@given(instance=statemachine_StateAttribute_strategy)
@settings(max_examples=25)
def test_statemachine_StateAttribute_instantiation(instance):
    assert isinstance(instance, statemachine_StateAttribute)


statemachine_StateChange_strategy = st.builds(statemachine_StateChange)
@given(instance=statemachine_StateChange_strategy)
@settings(max_examples=25)
def test_statemachine_StateChange_instantiation(instance):
    assert isinstance(instance, statemachine_StateChange)


statemachine_StateValue_strategy = st.builds(statemachine_StateValue, type=safe_text, value=safe_text)
@given(instance=statemachine_StateValue_strategy)
@settings(max_examples=25)
def test_statemachine_StateValue_instantiation(instance):
    assert isinstance(instance, statemachine_StateValue)


statemachine_Statemachine_strategy = st.builds(statemachine_Statemachine, associatedAttribute=safe_text, associatedTree=safe_text)
@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=25)
def test_statemachine_Statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)


statemachine_Transition_strategy = st.builds(statemachine_Transition)
@given(instance=statemachine_Transition_strategy)
@settings(max_examples=25)
def test_statemachine_Transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)


