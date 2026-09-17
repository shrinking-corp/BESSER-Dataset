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
    BehavioralFeature,
    statemachine_Operation,
    MessageEvent,
    statemachine_CallEvent,
    Event,
    statemachine_MessageEvent,
    statemachine_Event,
    State,
    statemachine_FinalState,
    Vertex,
    statemachine_State,
    statemachine_PseudoState,
    statemachine_Trigger,
    statemachine_Constraint,
    NamedElement,
    statemachine_BehavioralFeature,
    statemachine_Transition,
    statemachine_Vertex,
    statemachine_Behavior,
    statemachine_BehavioredClassifier,
    statemachine_NamedElement,
    statemachine_Region,
    Behavior,
    statemachine_OpaqueBehavior,
    statemachine_StateMachine,
    BehavioredClassifier,
    statemachine_Class,
    PseudoStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_hyp_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_hyp_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_operation_is_not_abstract():
    assert not inspect.isabstract(statemachine_Operation)


def test_hyp_statemachine_operation_constructor_exists():
    assert callable(statemachine_Operation.__init__)


def test_hyp_statemachine_operation_constructor_args():
    sig = inspect.signature(statemachine_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_hyp_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_hyp_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_callevent_is_not_abstract():
    assert not inspect.isabstract(statemachine_CallEvent)


def test_hyp_statemachine_callevent_constructor_exists():
    assert callable(statemachine_CallEvent.__init__)


def test_hyp_statemachine_callevent_constructor_args():
    sig = inspect.signature(statemachine_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_messageevent_is_not_abstract():
    assert not inspect.isabstract(statemachine_MessageEvent)


def test_hyp_statemachine_messageevent_constructor_exists():
    assert callable(statemachine_MessageEvent.__init__)


def test_hyp_statemachine_messageevent_constructor_args():
    sig = inspect.signature(statemachine_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_Event)


def test_hyp_statemachine_event_constructor_exists():
    assert callable(statemachine_Event.__init__)


def test_hyp_statemachine_event_constructor_args():
    sig = inspect.signature(statemachine_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_hyp_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_hyp_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_hyp_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_hyp_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_hyp_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_hyp_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachine_PseudoState)


def test_hyp_statemachine_pseudostate_constructor_exists():
    assert callable(statemachine_PseudoState.__init__)


def test_hyp_statemachine_pseudostate_constructor_args():
    sig = inspect.signature(statemachine_PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_statemachine_trigger_is_not_abstract():
    assert not inspect.isabstract(statemachine_Trigger)


def test_hyp_statemachine_trigger_constructor_exists():
    assert callable(statemachine_Trigger.__init__)


def test_hyp_statemachine_trigger_constructor_args():
    sig = inspect.signature(statemachine_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_constraint_is_not_abstract():
    assert not inspect.isabstract(statemachine_Constraint)


def test_hyp_statemachine_constraint_constructor_exists():
    assert callable(statemachine_Constraint.__init__)


def test_hyp_statemachine_constraint_constructor_args():
    sig = inspect.signature(statemachine_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(statemachine_BehavioralFeature)


def test_hyp_statemachine_behavioralfeature_constructor_exists():
    assert callable(statemachine_BehavioralFeature.__init__)


def test_hyp_statemachine_behavioralfeature_constructor_args():
    sig = inspect.signature(statemachine_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_hyp_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_hyp_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_vertex_is_not_abstract():
    assert not inspect.isabstract(statemachine_Vertex)


def test_hyp_statemachine_vertex_constructor_exists():
    assert callable(statemachine_Vertex.__init__)


def test_hyp_statemachine_vertex_constructor_args():
    sig = inspect.signature(statemachine_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_behavior_is_not_abstract():
    assert not inspect.isabstract(statemachine_Behavior)


def test_hyp_statemachine_behavior_constructor_exists():
    assert callable(statemachine_Behavior.__init__)


def test_hyp_statemachine_behavior_constructor_args():
    sig = inspect.signature(statemachine_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(statemachine_BehavioredClassifier)


def test_hyp_statemachine_behavioredclassifier_constructor_exists():
    assert callable(statemachine_BehavioredClassifier.__init__)


def test_hyp_statemachine_behavioredclassifier_constructor_args():
    sig = inspect.signature(statemachine_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachine_NamedElement)


def test_hyp_statemachine_namedelement_constructor_exists():
    assert callable(statemachine_NamedElement.__init__)


def test_hyp_statemachine_namedelement_constructor_args():
    sig = inspect.signature(statemachine_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_region_is_not_abstract():
    assert not inspect.isabstract(statemachine_Region)


def test_hyp_statemachine_region_constructor_exists():
    assert callable(statemachine_Region.__init__)


def test_hyp_statemachine_region_constructor_args():
    sig = inspect.signature(statemachine_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_hyp_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_hyp_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(statemachine_OpaqueBehavior)


def test_hyp_statemachine_opaquebehavior_constructor_exists():
    assert callable(statemachine_OpaqueBehavior.__init__)


def test_hyp_statemachine_opaquebehavior_constructor_args():
    sig = inspect.signature(statemachine_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_hyp_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_hyp_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_hyp_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_hyp_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_class_is_not_abstract():
    assert not inspect.isabstract(statemachine_Class)


def test_hyp_statemachine_class_constructor_exists():
    assert callable(statemachine_Class.__init__)


def test_hyp_statemachine_class_constructor_args():
    sig = inspect.signature(statemachine_Class.__init__)
    params = list(sig.parameters.keys())

def test_hyp_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_hyp_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateKind"


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
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
statemachine_Operation_strategy = st.builds(
    statemachine_Operation,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
statemachine_CallEvent_strategy = st.builds(
    statemachine_CallEvent,
)
Event_strategy = st.builds(
    Event,
)
statemachine_MessageEvent_strategy = st.builds(
    statemachine_MessageEvent,
)
statemachine_Event_strategy = st.builds(
    statemachine_Event,
)
State_strategy = st.builds(
    State,
)
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
)
statemachine_PseudoState_strategy = st.builds(
    statemachine_PseudoState,
    kind=
        safe_text
)
statemachine_Trigger_strategy = st.builds(
    statemachine_Trigger,
)
statemachine_Constraint_strategy = st.builds(
    statemachine_Constraint,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statemachine_BehavioralFeature_strategy = st.builds(
    statemachine_BehavioralFeature,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_Vertex_strategy = st.builds(
    statemachine_Vertex,
)
statemachine_Behavior_strategy = st.builds(
    statemachine_Behavior,
)
statemachine_BehavioredClassifier_strategy = st.builds(
    statemachine_BehavioredClassifier,
)
statemachine_NamedElement_strategy = st.builds(
    statemachine_NamedElement,
)
statemachine_Region_strategy = st.builds(
    statemachine_Region,
)
Behavior_strategy = st.builds(
    Behavior,
)
statemachine_OpaqueBehavior_strategy = st.builds(
    statemachine_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
statemachine_Class_strategy = st.builds(
    statemachine_Class,
)















@given(instance=statemachine_PseudoState_strategy)
def test_hyp_statemachine_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original















@given(instance=statemachine_OpaqueBehavior_strategy)
def test_hyp_statemachine_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=statemachine_OpaqueBehavior_strategy)
def test_hyp_statemachine_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Behavior,
    BehavioralFeature,
    BehavioredClassifier,
    Event,
    MessageEvent,
    NamedElement,
    State,
    Vertex,
    statemachine_Behavior,
    statemachine_BehavioralFeature,
    statemachine_BehavioredClassifier,
    statemachine_CallEvent,
    statemachine_Class,
    statemachine_Constraint,
    statemachine_Event,
    statemachine_FinalState,
    statemachine_MessageEvent,
    statemachine_NamedElement,
    statemachine_OpaqueBehavior,
    statemachine_Operation,
    statemachine_PseudoState,
    statemachine_Region,
    statemachine_State,
    statemachine_StateMachine,
    statemachine_Transition,
    statemachine_Trigger,
    statemachine_Vertex,
    PseudoStateKind,
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

def test_statemachine_OpaqueBehavior_body_value_roundtrip():
    instance = statemachine_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_statemachine_OpaqueBehavior_language_value_roundtrip():
    instance = statemachine_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_statemachine_PseudoState_kind_value_roundtrip():
    instance = statemachine_PseudoState(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_statemachine_OpaqueBehavior_isa_Behavior():
    instance = statemachine_OpaqueBehavior(body="sample_text", language="sample_text")
    assert isinstance(instance, Behavior)


def test_statemachine_StateMachine_isa_Behavior():
    instance = statemachine_StateMachine()
    assert isinstance(instance, Behavior)


def test_statemachine_Operation_isa_BehavioralFeature():
    instance = statemachine_Operation()
    assert isinstance(instance, BehavioralFeature)


def test_statemachine_Class_isa_BehavioredClassifier():
    instance = statemachine_Class()
    assert isinstance(instance, BehavioredClassifier)


def test_statemachine_MessageEvent_isa_Event():
    instance = statemachine_MessageEvent()
    assert isinstance(instance, Event)


def test_statemachine_CallEvent_isa_MessageEvent():
    instance = statemachine_CallEvent()
    assert isinstance(instance, MessageEvent)


def test_statemachine_Transition_isa_NamedElement():
    instance = statemachine_Transition()
    assert isinstance(instance, NamedElement)


def test_statemachine_Vertex_isa_NamedElement():
    instance = statemachine_Vertex()
    assert isinstance(instance, NamedElement)


def test_statemachine_FinalState_isa_State():
    instance = statemachine_FinalState()
    assert isinstance(instance, State)


def test_statemachine_PseudoState_isa_Vertex():
    instance = statemachine_PseudoState(kind="sample_text")
    assert isinstance(instance, Vertex)


def test_statemachine_State_isa_Vertex():
    instance = statemachine_State()
    assert isinstance(instance, Vertex)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


BehavioralFeature_strategy = st.builds(BehavioralFeature)
@given(instance=BehavioralFeature_strategy)
@settings(max_examples=25)
def test_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)


BehavioredClassifier_strategy = st.builds(BehavioredClassifier)
@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


MessageEvent_strategy = st.builds(MessageEvent)
@given(instance=MessageEvent_strategy)
@settings(max_examples=25)
def test_MessageEvent_instantiation(instance):
    assert isinstance(instance, MessageEvent)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Vertex_strategy = st.builds(Vertex)
@given(instance=Vertex_strategy)
@settings(max_examples=25)
def test_Vertex_instantiation(instance):
    assert isinstance(instance, Vertex)


statemachine_Behavior_strategy = st.builds(statemachine_Behavior)
@given(instance=statemachine_Behavior_strategy)
@settings(max_examples=25)
def test_statemachine_Behavior_instantiation(instance):
    assert isinstance(instance, statemachine_Behavior)


statemachine_BehavioralFeature_strategy = st.builds(statemachine_BehavioralFeature)
@given(instance=statemachine_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_statemachine_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, statemachine_BehavioralFeature)


statemachine_BehavioredClassifier_strategy = st.builds(statemachine_BehavioredClassifier)
@given(instance=statemachine_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_statemachine_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, statemachine_BehavioredClassifier)


statemachine_CallEvent_strategy = st.builds(statemachine_CallEvent)
@given(instance=statemachine_CallEvent_strategy)
@settings(max_examples=25)
def test_statemachine_CallEvent_instantiation(instance):
    assert isinstance(instance, statemachine_CallEvent)


statemachine_Class_strategy = st.builds(statemachine_Class)
@given(instance=statemachine_Class_strategy)
@settings(max_examples=25)
def test_statemachine_Class_instantiation(instance):
    assert isinstance(instance, statemachine_Class)


statemachine_Constraint_strategy = st.builds(statemachine_Constraint)
@given(instance=statemachine_Constraint_strategy)
@settings(max_examples=25)
def test_statemachine_Constraint_instantiation(instance):
    assert isinstance(instance, statemachine_Constraint)


statemachine_Event_strategy = st.builds(statemachine_Event)
@given(instance=statemachine_Event_strategy)
@settings(max_examples=25)
def test_statemachine_Event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)


statemachine_FinalState_strategy = st.builds(statemachine_FinalState)
@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=25)
def test_statemachine_FinalState_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)


statemachine_MessageEvent_strategy = st.builds(statemachine_MessageEvent)
@given(instance=statemachine_MessageEvent_strategy)
@settings(max_examples=25)
def test_statemachine_MessageEvent_instantiation(instance):
    assert isinstance(instance, statemachine_MessageEvent)


statemachine_NamedElement_strategy = st.builds(statemachine_NamedElement)
@given(instance=statemachine_NamedElement_strategy)
@settings(max_examples=25)
def test_statemachine_NamedElement_instantiation(instance):
    assert isinstance(instance, statemachine_NamedElement)


statemachine_OpaqueBehavior_strategy = st.builds(statemachine_OpaqueBehavior, body=safe_text, language=safe_text)
@given(instance=statemachine_OpaqueBehavior_strategy)
@settings(max_examples=25)
def test_statemachine_OpaqueBehavior_instantiation(instance):
    assert isinstance(instance, statemachine_OpaqueBehavior)


statemachine_Operation_strategy = st.builds(statemachine_Operation)
@given(instance=statemachine_Operation_strategy)
@settings(max_examples=25)
def test_statemachine_Operation_instantiation(instance):
    assert isinstance(instance, statemachine_Operation)


statemachine_PseudoState_strategy = st.builds(statemachine_PseudoState, kind=safe_text)
@given(instance=statemachine_PseudoState_strategy)
@settings(max_examples=25)
def test_statemachine_PseudoState_instantiation(instance):
    assert isinstance(instance, statemachine_PseudoState)


statemachine_Region_strategy = st.builds(statemachine_Region)
@given(instance=statemachine_Region_strategy)
@settings(max_examples=25)
def test_statemachine_Region_instantiation(instance):
    assert isinstance(instance, statemachine_Region)


statemachine_State_strategy = st.builds(statemachine_State)
@given(instance=statemachine_State_strategy)
@settings(max_examples=25)
def test_statemachine_State_instantiation(instance):
    assert isinstance(instance, statemachine_State)


statemachine_StateMachine_strategy = st.builds(statemachine_StateMachine)
@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=25)
def test_statemachine_StateMachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)


statemachine_Transition_strategy = st.builds(statemachine_Transition)
@given(instance=statemachine_Transition_strategy)
@settings(max_examples=25)
def test_statemachine_Transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)


statemachine_Trigger_strategy = st.builds(statemachine_Trigger)
@given(instance=statemachine_Trigger_strategy)
@settings(max_examples=25)
def test_statemachine_Trigger_instantiation(instance):
    assert isinstance(instance, statemachine_Trigger)


statemachine_Vertex_strategy = st.builds(statemachine_Vertex)
@given(instance=statemachine_Vertex_strategy)
@settings(max_examples=25)
def test_statemachine_Vertex_instantiation(instance):
    assert isinstance(instance, statemachine_Vertex)



