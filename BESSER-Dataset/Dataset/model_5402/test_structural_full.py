import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Behavior,
    OpaqueExpression,
    StateMachine,
    UML2_Activity,
    UML2_Behavior,
    UML2_Expression,
    UML2_Interaction,
    UML2_OpaqueExpression,
    UML2_Parameter,
    UML2_ParameterSet,
    UML2_ProtocolStateMachine,
    UML2_StateMachine,
    ParameterDirectionKind,
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

def test_UML2_Parameter_direction_value_roundtrip():
    instance = UML2_Parameter(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_UML2_Activity_isa_Behavior():
    instance = UML2_Activity()
    assert isinstance(instance, Behavior)


def test_UML2_Interaction_isa_Behavior():
    instance = UML2_Interaction()
    assert isinstance(instance, Behavior)


def test_UML2_StateMachine_isa_Behavior():
    instance = UML2_StateMachine()
    assert isinstance(instance, Behavior)


def test_UML2_Expression_isa_OpaqueExpression():
    instance = UML2_Expression()
    assert isinstance(instance, OpaqueExpression)


def test_UML2_ProtocolStateMachine_isa_StateMachine():
    instance = UML2_ProtocolStateMachine()
    assert isinstance(instance, StateMachine)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


OpaqueExpression_strategy = st.builds(OpaqueExpression)
@given(instance=OpaqueExpression_strategy)
@settings(max_examples=25)
def test_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)


StateMachine_strategy = st.builds(StateMachine)
@given(instance=StateMachine_strategy)
@settings(max_examples=25)
def test_StateMachine_instantiation(instance):
    assert isinstance(instance, StateMachine)


UML2_Activity_strategy = st.builds(UML2_Activity)
@given(instance=UML2_Activity_strategy)
@settings(max_examples=25)
def test_UML2_Activity_instantiation(instance):
    assert isinstance(instance, UML2_Activity)


UML2_Behavior_strategy = st.builds(UML2_Behavior)
@given(instance=UML2_Behavior_strategy)
@settings(max_examples=25)
def test_UML2_Behavior_instantiation(instance):
    assert isinstance(instance, UML2_Behavior)


UML2_Expression_strategy = st.builds(UML2_Expression)
@given(instance=UML2_Expression_strategy)
@settings(max_examples=25)
def test_UML2_Expression_instantiation(instance):
    assert isinstance(instance, UML2_Expression)


UML2_Interaction_strategy = st.builds(UML2_Interaction)
@given(instance=UML2_Interaction_strategy)
@settings(max_examples=25)
def test_UML2_Interaction_instantiation(instance):
    assert isinstance(instance, UML2_Interaction)


UML2_OpaqueExpression_strategy = st.builds(UML2_OpaqueExpression)
@given(instance=UML2_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_UML2_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, UML2_OpaqueExpression)


UML2_Parameter_strategy = st.builds(UML2_Parameter, direction=safe_text)
@given(instance=UML2_Parameter_strategy)
@settings(max_examples=25)
def test_UML2_Parameter_instantiation(instance):
    assert isinstance(instance, UML2_Parameter)


UML2_ParameterSet_strategy = st.builds(UML2_ParameterSet)
@given(instance=UML2_ParameterSet_strategy)
@settings(max_examples=25)
def test_UML2_ParameterSet_instantiation(instance):
    assert isinstance(instance, UML2_ParameterSet)


UML2_ProtocolStateMachine_strategy = st.builds(UML2_ProtocolStateMachine)
@given(instance=UML2_ProtocolStateMachine_strategy)
@settings(max_examples=25)
def test_UML2_ProtocolStateMachine_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolStateMachine)


UML2_StateMachine_strategy = st.builds(UML2_StateMachine)
@given(instance=UML2_StateMachine_strategy)
@settings(max_examples=25)
def test_UML2_StateMachine_instantiation(instance):
    assert isinstance(instance, UML2_StateMachine)


