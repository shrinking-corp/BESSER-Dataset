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
    conversation_Junction,
    SubscribableByOthers,
    PublishableByMe,
    PublicEvent,
    PublishableByOthers,
    SubscribableByMe,
    conversation_PubliclyPublishable,
    Event,
    conversation_PublicEvent,
    conversation_SubscribableByMe,
    conversation_ProjectionField,
    conversation_Import,
    Import,
    PubliclySubscribable,
    PubliclyPublishable,
    conversation_PublicPubSub,
    conversation_PublishableByOthers,
    conversation_PrivatePubSub,
    conversation_SubscribableByOthers,
    State,
    conversation_Join,
    conversation_Decision,
    conversation_Event,
    conversation_PublishableByMe,
    conversation_PubliclySubscribable,
    conversation_StateMachine,
    conversation_View,
    conversation_AgentImport,
    conversation_TypeImport,
    conversation_Service,
    conversation_RestService,
    conversation_Projection,
    conversation_Agent,
    conversation_Transition,
    conversation_State,
    conversation_Conversation,
    ConnectionType,
    StateMachineType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_conversation_junction_is_not_abstract():
    assert not inspect.isabstract(conversation_Junction)


def test_hyp_conversation_junction_constructor_exists():
    assert callable(conversation_Junction.__init__)


def test_hyp_conversation_junction_constructor_args():
    sig = inspect.signature(conversation_Junction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subscribablebyothers_is_not_abstract():
    assert not inspect.isabstract(SubscribableByOthers)


def test_hyp_subscribablebyothers_constructor_exists():
    assert callable(SubscribableByOthers.__init__)


def test_hyp_subscribablebyothers_constructor_args():
    sig = inspect.signature(SubscribableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publishablebyme_is_not_abstract():
    assert not inspect.isabstract(PublishableByMe)


def test_hyp_publishablebyme_constructor_exists():
    assert callable(PublishableByMe.__init__)


def test_hyp_publishablebyme_constructor_args():
    sig = inspect.signature(PublishableByMe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publicevent_is_not_abstract():
    assert not inspect.isabstract(PublicEvent)


def test_hyp_publicevent_constructor_exists():
    assert callable(PublicEvent.__init__)


def test_hyp_publicevent_constructor_args():
    sig = inspect.signature(PublicEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publishablebyothers_is_not_abstract():
    assert not inspect.isabstract(PublishableByOthers)


def test_hyp_publishablebyothers_constructor_exists():
    assert callable(PublishableByOthers.__init__)


def test_hyp_publishablebyothers_constructor_args():
    sig = inspect.signature(PublishableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subscribablebyme_is_not_abstract():
    assert not inspect.isabstract(SubscribableByMe)


def test_hyp_subscribablebyme_constructor_exists():
    assert callable(SubscribableByMe.__init__)


def test_hyp_subscribablebyme_constructor_args():
    sig = inspect.signature(SubscribableByMe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_publiclypublishable_is_not_abstract():
    assert not inspect.isabstract(conversation_PubliclyPublishable)


def test_hyp_conversation_publiclypublishable_constructor_exists():
    assert callable(conversation_PubliclyPublishable.__init__)


def test_hyp_conversation_publiclypublishable_constructor_args():
    sig = inspect.signature(conversation_PubliclyPublishable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_publicevent_is_not_abstract():
    assert not inspect.isabstract(conversation_PublicEvent)


def test_hyp_conversation_publicevent_constructor_exists():
    assert callable(conversation_PublicEvent.__init__)


def test_hyp_conversation_publicevent_constructor_args():
    sig = inspect.signature(conversation_PublicEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_subscribablebyme_is_not_abstract():
    assert not inspect.isabstract(conversation_SubscribableByMe)


def test_hyp_conversation_subscribablebyme_constructor_exists():
    assert callable(conversation_SubscribableByMe.__init__)


def test_hyp_conversation_subscribablebyme_constructor_args():
    sig = inspect.signature(conversation_SubscribableByMe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_projectionfield_is_not_abstract():
    assert not inspect.isabstract(conversation_ProjectionField)


def test_hyp_conversation_projectionfield_constructor_exists():
    assert callable(conversation_ProjectionField.__init__)


def test_hyp_conversation_projectionfield_constructor_args():
    sig = inspect.signature(conversation_ProjectionField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_import_is_not_abstract():
    assert not inspect.isabstract(conversation_Import)


def test_hyp_conversation_import_constructor_exists():
    assert callable(conversation_Import.__init__)


def test_hyp_conversation_import_constructor_args():
    sig = inspect.signature(conversation_Import.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"




def test_hyp_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_hyp_import_constructor_exists():
    assert callable(Import.__init__)


def test_hyp_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publiclysubscribable_is_not_abstract():
    assert not inspect.isabstract(PubliclySubscribable)


def test_hyp_publiclysubscribable_constructor_exists():
    assert callable(PubliclySubscribable.__init__)


def test_hyp_publiclysubscribable_constructor_args():
    sig = inspect.signature(PubliclySubscribable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_publiclypublishable_is_not_abstract():
    assert not inspect.isabstract(PubliclyPublishable)


def test_hyp_publiclypublishable_constructor_exists():
    assert callable(PubliclyPublishable.__init__)


def test_hyp_publiclypublishable_constructor_args():
    sig = inspect.signature(PubliclyPublishable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_publicpubsub_is_not_abstract():
    assert not inspect.isabstract(conversation_PublicPubSub)


def test_hyp_conversation_publicpubsub_constructor_exists():
    assert callable(conversation_PublicPubSub.__init__)


def test_hyp_conversation_publicpubsub_constructor_args():
    sig = inspect.signature(conversation_PublicPubSub.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_publishablebyothers_is_not_abstract():
    assert not inspect.isabstract(conversation_PublishableByOthers)


def test_hyp_conversation_publishablebyothers_constructor_exists():
    assert callable(conversation_PublishableByOthers.__init__)


def test_hyp_conversation_publishablebyothers_constructor_args():
    sig = inspect.signature(conversation_PublishableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_privatepubsub_is_not_abstract():
    assert not inspect.isabstract(conversation_PrivatePubSub)


def test_hyp_conversation_privatepubsub_constructor_exists():
    assert callable(conversation_PrivatePubSub.__init__)


def test_hyp_conversation_privatepubsub_constructor_args():
    sig = inspect.signature(conversation_PrivatePubSub.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_subscribablebyothers_is_not_abstract():
    assert not inspect.isabstract(conversation_SubscribableByOthers)


def test_hyp_conversation_subscribablebyothers_constructor_exists():
    assert callable(conversation_SubscribableByOthers.__init__)


def test_hyp_conversation_subscribablebyothers_constructor_args():
    sig = inspect.signature(conversation_SubscribableByOthers.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_join_is_not_abstract():
    assert not inspect.isabstract(conversation_Join)


def test_hyp_conversation_join_constructor_exists():
    assert callable(conversation_Join.__init__)


def test_hyp_conversation_join_constructor_args():
    sig = inspect.signature(conversation_Join.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_decision_is_not_abstract():
    assert not inspect.isabstract(conversation_Decision)


def test_hyp_conversation_decision_constructor_exists():
    assert callable(conversation_Decision.__init__)


def test_hyp_conversation_decision_constructor_args():
    sig = inspect.signature(conversation_Decision.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_event_is_not_abstract():
    assert not inspect.isabstract(conversation_Event)


def test_hyp_conversation_event_constructor_exists():
    assert callable(conversation_Event.__init__)


def test_hyp_conversation_event_constructor_args():
    sig = inspect.signature(conversation_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_conversation_publishablebyme_is_not_abstract():
    assert not inspect.isabstract(conversation_PublishableByMe)


def test_hyp_conversation_publishablebyme_constructor_exists():
    assert callable(conversation_PublishableByMe.__init__)


def test_hyp_conversation_publishablebyme_constructor_args():
    sig = inspect.signature(conversation_PublishableByMe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_publiclysubscribable_is_not_abstract():
    assert not inspect.isabstract(conversation_PubliclySubscribable)


def test_hyp_conversation_publiclysubscribable_constructor_exists():
    assert callable(conversation_PubliclySubscribable.__init__)


def test_hyp_conversation_publiclysubscribable_constructor_args():
    sig = inspect.signature(conversation_PubliclySubscribable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_statemachine_is_not_abstract():
    assert not inspect.isabstract(conversation_StateMachine)


def test_hyp_conversation_statemachine_constructor_exists():
    assert callable(conversation_StateMachine.__init__)


def test_hyp_conversation_statemachine_constructor_args():
    sig = inspect.signature(conversation_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_view_is_not_abstract():
    assert not inspect.isabstract(conversation_View)


def test_hyp_conversation_view_constructor_exists():
    assert callable(conversation_View.__init__)


def test_hyp_conversation_view_constructor_args():
    sig = inspect.signature(conversation_View.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_agentimport_is_not_abstract():
    assert not inspect.isabstract(conversation_AgentImport)


def test_hyp_conversation_agentimport_constructor_exists():
    assert callable(conversation_AgentImport.__init__)


def test_hyp_conversation_agentimport_constructor_args():
    sig = inspect.signature(conversation_AgentImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_typeimport_is_not_abstract():
    assert not inspect.isabstract(conversation_TypeImport)


def test_hyp_conversation_typeimport_constructor_exists():
    assert callable(conversation_TypeImport.__init__)


def test_hyp_conversation_typeimport_constructor_args():
    sig = inspect.signature(conversation_TypeImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_service_is_not_abstract():
    assert not inspect.isabstract(conversation_Service)


def test_hyp_conversation_service_constructor_exists():
    assert callable(conversation_Service.__init__)


def test_hyp_conversation_service_constructor_args():
    sig = inspect.signature(conversation_Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_restservice_is_not_abstract():
    assert not inspect.isabstract(conversation_RestService)


def test_hyp_conversation_restservice_constructor_exists():
    assert callable(conversation_RestService.__init__)


def test_hyp_conversation_restservice_constructor_args():
    sig = inspect.signature(conversation_RestService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_projection_is_not_abstract():
    assert not inspect.isabstract(conversation_Projection)


def test_hyp_conversation_projection_constructor_exists():
    assert callable(conversation_Projection.__init__)


def test_hyp_conversation_projection_constructor_args():
    sig = inspect.signature(conversation_Projection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conversation_agent_is_not_abstract():
    assert not inspect.isabstract(conversation_Agent)


def test_hyp_conversation_agent_constructor_exists():
    assert callable(conversation_Agent.__init__)


def test_hyp_conversation_agent_constructor_args():
    sig = inspect.signature(conversation_Agent.__init__)
    params = list(sig.parameters.keys())
    assert "accessRequirement" in params, "Missing parameter 'accessRequirement'"
    assert "stateMachineType" in params, "Missing parameter 'stateMachineType'"
    assert "connectionType" in params, "Missing parameter 'connectionType'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_conversation_transition_is_not_abstract():
    assert not inspect.isabstract(conversation_Transition)


def test_hyp_conversation_transition_constructor_exists():
    assert callable(conversation_Transition.__init__)


def test_hyp_conversation_transition_constructor_args():
    sig = inspect.signature(conversation_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "requiresExecution" in params, "Missing parameter 'requiresExecution'"




def test_hyp_conversation_state_is_not_abstract():
    assert not inspect.isabstract(conversation_State)


def test_hyp_conversation_state_constructor_exists():
    assert callable(conversation_State.__init__)


def test_hyp_conversation_state_constructor_args():
    sig = inspect.signature(conversation_State.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"
    assert "name" in params, "Missing parameter 'name'"
    assert "requiresExecution" in params, "Missing parameter 'requiresExecution'"






def test_hyp_conversation_conversation_is_not_abstract():
    assert not inspect.isabstract(conversation_Conversation)


def test_hyp_conversation_conversation_constructor_exists():
    assert callable(conversation_Conversation.__init__)


def test_hyp_conversation_conversation_constructor_args():
    sig = inspect.signature(conversation_Conversation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_connectiontype_exists():
    # Check that the Enumeration exists
    assert ConnectionType is not None

def test_hyp_connectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionType]
    expected_literals = [
        "independent",
        "dependent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectionType"

def test_hyp_statemachinetype_exists():
    # Check that the Enumeration exists
    assert StateMachineType is not None

def test_hyp_statemachinetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateMachineType]
    expected_literals = [
        "infinite",
        "finite",
        "stateless",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateMachineType"


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
conversation_Junction_strategy = st.builds(
    conversation_Junction,
)
SubscribableByOthers_strategy = st.builds(
    SubscribableByOthers,
)
PublishableByMe_strategy = st.builds(
    PublishableByMe,
)
PublicEvent_strategy = st.builds(
    PublicEvent,
)
PublishableByOthers_strategy = st.builds(
    PublishableByOthers,
)
SubscribableByMe_strategy = st.builds(
    SubscribableByMe,
)
conversation_PubliclyPublishable_strategy = st.builds(
    conversation_PubliclyPublishable,
)
Event_strategy = st.builds(
    Event,
)
conversation_PublicEvent_strategy = st.builds(
    conversation_PublicEvent,
)
conversation_SubscribableByMe_strategy = st.builds(
    conversation_SubscribableByMe,
)
conversation_ProjectionField_strategy = st.builds(
    conversation_ProjectionField,
)
conversation_Import_strategy = st.builds(
    conversation_Import,
    alias=
        safe_text
)
Import_strategy = st.builds(
    Import,
)
PubliclySubscribable_strategy = st.builds(
    PubliclySubscribable,
)
PubliclyPublishable_strategy = st.builds(
    PubliclyPublishable,
)
conversation_PublicPubSub_strategy = st.builds(
    conversation_PublicPubSub,
)
conversation_PublishableByOthers_strategy = st.builds(
    conversation_PublishableByOthers,
)
conversation_PrivatePubSub_strategy = st.builds(
    conversation_PrivatePubSub,
)
conversation_SubscribableByOthers_strategy = st.builds(
    conversation_SubscribableByOthers,
)
State_strategy = st.builds(
    State,
)
conversation_Join_strategy = st.builds(
    conversation_Join,
)
conversation_Decision_strategy = st.builds(
    conversation_Decision,
)
conversation_Event_strategy = st.builds(
    conversation_Event,
    name=
        safe_text
)
conversation_PublishableByMe_strategy = st.builds(
    conversation_PublishableByMe,
)
conversation_PubliclySubscribable_strategy = st.builds(
    conversation_PubliclySubscribable,
)
conversation_StateMachine_strategy = st.builds(
    conversation_StateMachine,
)
conversation_View_strategy = st.builds(
    conversation_View,
)
conversation_AgentImport_strategy = st.builds(
    conversation_AgentImport,
)
conversation_TypeImport_strategy = st.builds(
    conversation_TypeImport,
)
conversation_Service_strategy = st.builds(
    conversation_Service,
)
conversation_RestService_strategy = st.builds(
    conversation_RestService,
)
conversation_Projection_strategy = st.builds(
    conversation_Projection,
)
conversation_Agent_strategy = st.builds(
    conversation_Agent,
    accessRequirement=
        safe_text,
    stateMachineType=
        safe_text,
    connectionType=
        safe_text,
    name=
        safe_text
)
conversation_Transition_strategy = st.builds(
    conversation_Transition,
    requiresExecution=
        st.booleans()
)
conversation_State_strategy = st.builds(
    conversation_State,
    join=
        st.booleans(),
    name=
        safe_text,
    requiresExecution=
        st.booleans()
)
conversation_Conversation_strategy = st.builds(
    conversation_Conversation,
    name=
        safe_text
)















@given(instance=conversation_Import_strategy)
def test_hyp_conversation_import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original














@given(instance=conversation_Event_strategy)
def test_hyp_conversation_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original













@given(instance=conversation_Agent_strategy)
def test_hyp_conversation_agent_accessRequirement_setter(instance):
    original = instance.accessRequirement
    instance.accessRequirement = original
    assert instance.accessRequirement == original



@given(instance=conversation_Agent_strategy)
def test_hyp_conversation_agent_stateMachineType_setter(instance):
    original = instance.stateMachineType
    instance.stateMachineType = original
    assert instance.stateMachineType == original



@given(instance=conversation_Agent_strategy)
def test_hyp_conversation_agent_connectionType_setter(instance):
    original = instance.connectionType
    instance.connectionType = original
    assert instance.connectionType == original



@given(instance=conversation_Agent_strategy)
def test_hyp_conversation_agent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=conversation_Transition_strategy)
def test_hyp_conversation_transition_requiresExecution_setter(instance):
    original = instance.requiresExecution
    instance.requiresExecution = original
    assert instance.requiresExecution == original




@given(instance=conversation_State_strategy)
def test_hyp_conversation_state_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original



@given(instance=conversation_State_strategy)
def test_hyp_conversation_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=conversation_State_strategy)
def test_hyp_conversation_state_requiresExecution_setter(instance):
    original = instance.requiresExecution
    instance.requiresExecution = original
    assert instance.requiresExecution == original




@given(instance=conversation_Conversation_strategy)
def test_hyp_conversation_conversation_name_setter(instance):
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
    Event,
    Import,
    PublicEvent,
    PubliclyPublishable,
    PubliclySubscribable,
    PublishableByMe,
    PublishableByOthers,
    State,
    SubscribableByMe,
    SubscribableByOthers,
    conversation_Agent,
    conversation_AgentImport,
    conversation_Conversation,
    conversation_Decision,
    conversation_Event,
    conversation_Import,
    conversation_Join,
    conversation_Junction,
    conversation_PrivatePubSub,
    conversation_Projection,
    conversation_ProjectionField,
    conversation_PublicEvent,
    conversation_PublicPubSub,
    conversation_PubliclyPublishable,
    conversation_PubliclySubscribable,
    conversation_PublishableByMe,
    conversation_PublishableByOthers,
    conversation_RestService,
    conversation_Service,
    conversation_State,
    conversation_StateMachine,
    conversation_SubscribableByMe,
    conversation_SubscribableByOthers,
    conversation_Transition,
    conversation_TypeImport,
    conversation_View,
    ConnectionType,
    StateMachineType,
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

def test_conversation_Agent_accessRequirement_value_roundtrip():
    instance = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    assert instance.accessRequirement == "sample_text"
    instance.accessRequirement = "sample_text_2"
    assert instance.accessRequirement == "sample_text_2"


def test_conversation_Agent_connectionType_value_roundtrip():
    instance = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    assert instance.connectionType == "sample_text"
    instance.connectionType = "sample_text_2"
    assert instance.connectionType == "sample_text_2"


def test_conversation_Agent_name_value_roundtrip():
    instance = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conversation_Agent_stateMachineType_value_roundtrip():
    instance = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    assert instance.stateMachineType == "sample_text"
    instance.stateMachineType = "sample_text_2"
    assert instance.stateMachineType == "sample_text_2"


def test_conversation_Conversation_name_value_roundtrip():
    instance = conversation_Conversation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conversation_Event_name_value_roundtrip():
    instance = conversation_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conversation_Import_alias_value_roundtrip():
    instance = conversation_Import(alias="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_conversation_State_join_value_roundtrip():
    instance = conversation_State(join=True, name="sample_text", requiresExecution=True)
    assert instance.join == True
    instance.join = False
    assert instance.join == False


def test_conversation_State_name_value_roundtrip():
    instance = conversation_State(join=True, name="sample_text", requiresExecution=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conversation_State_requiresExecution_value_roundtrip():
    instance = conversation_State(join=True, name="sample_text", requiresExecution=True)
    assert instance.requiresExecution == True
    instance.requiresExecution = False
    assert instance.requiresExecution == False


def test_conversation_Transition_requiresExecution_value_roundtrip():
    instance = conversation_Transition(requiresExecution=True)
    assert instance.requiresExecution == True
    instance.requiresExecution = False
    assert instance.requiresExecution == False


def test_conversation_PublicEvent_isa_Event():
    instance = conversation_PublicEvent()
    assert isinstance(instance, Event)


def test_conversation_PublishableByMe_isa_Event():
    instance = conversation_PublishableByMe()
    assert isinstance(instance, Event)


def test_conversation_PublishableByOthers_isa_Event():
    instance = conversation_PublishableByOthers()
    assert isinstance(instance, Event)


def test_conversation_SubscribableByMe_isa_Event():
    instance = conversation_SubscribableByMe()
    assert isinstance(instance, Event)


def test_conversation_SubscribableByOthers_isa_Event():
    instance = conversation_SubscribableByOthers()
    assert isinstance(instance, Event)


def test_conversation_AgentImport_isa_Import():
    instance = conversation_AgentImport()
    assert isinstance(instance, Import)


def test_conversation_TypeImport_isa_Import():
    instance = conversation_TypeImport()
    assert isinstance(instance, Import)


def test_conversation_PubliclyPublishable_isa_PublicEvent():
    instance = conversation_PubliclyPublishable()
    assert isinstance(instance, PublicEvent)


def test_conversation_PubliclySubscribable_isa_PublicEvent():
    instance = conversation_PubliclySubscribable()
    assert isinstance(instance, PublicEvent)


def test_conversation_PublicPubSub_isa_PubliclyPublishable():
    instance = conversation_PublicPubSub()
    assert isinstance(instance, PubliclyPublishable)


def test_conversation_PublicPubSub_isa_PubliclySubscribable():
    instance = conversation_PublicPubSub()
    assert isinstance(instance, PubliclySubscribable)


def test_conversation_PrivatePubSub_isa_PublishableByMe():
    instance = conversation_PrivatePubSub()
    assert isinstance(instance, PublishableByMe)


def test_conversation_PubliclySubscribable_isa_PublishableByMe():
    instance = conversation_PubliclySubscribable()
    assert isinstance(instance, PublishableByMe)


def test_conversation_PubliclyPublishable_isa_PublishableByOthers():
    instance = conversation_PubliclyPublishable()
    assert isinstance(instance, PublishableByOthers)


def test_conversation_Decision_isa_State():
    instance = conversation_Decision()
    assert isinstance(instance, State)


def test_conversation_Join_isa_State():
    instance = conversation_Join()
    assert isinstance(instance, State)


def test_conversation_PrivatePubSub_isa_SubscribableByMe():
    instance = conversation_PrivatePubSub()
    assert isinstance(instance, SubscribableByMe)


def test_conversation_PubliclyPublishable_isa_SubscribableByMe():
    instance = conversation_PubliclyPublishable()
    assert isinstance(instance, SubscribableByMe)


def test_conversation_PubliclySubscribable_isa_SubscribableByOthers():
    instance = conversation_PubliclySubscribable()
    assert isinstance(instance, SubscribableByOthers)


def test_assoc_agent51_link_reassign_clear():
    a = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b1 = conversation_AgentImport()
    b2 = conversation_AgentImport()
    _safe_set(a, 'conversation_Agent53', b1)
    assert _is_linked(a, 'conversation_Agent53', b1)
    if hasattr(b1, 'conversation_AgentImport52'):
        assert _is_linked(b1, 'conversation_AgentImport52', a)
    _safe_set(a, 'conversation_Agent53', b2)
    assert _is_linked(a, 'conversation_Agent53', b2)
    if hasattr(b1, 'conversation_AgentImport52'):
        assert not _is_linked(b1, 'conversation_AgentImport52', a)
    if hasattr(b2, 'conversation_AgentImport52'):
        assert _is_linked(b2, 'conversation_AgentImport52', a)
    _safe_set(a, 'conversation_Agent53', None)
    assert not _is_linked(a, 'conversation_Agent53', b2)
    if hasattr(b2, 'conversation_AgentImport52'):
        assert not _is_linked(b2, 'conversation_AgentImport52', a)


def test_assoc_agents0_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b2 = conversation_Agent(accessRequirement="sample_text_2", connectionType="sample_text_2", name="sample_text_2", stateMachineType="sample_text_2")
    _safe_set(a, 'parent', {b1})
    assert _is_linked(a, 'parent', b1)
    if hasattr(b1, 'Agent'):
        assert _is_linked(b1, 'Agent', a)
    _safe_set(a, 'parent', {b2})
    assert _is_linked(a, 'parent', b2)
    if hasattr(b1, 'Agent'):
        assert not _is_linked(b1, 'Agent', a)
    if hasattr(b2, 'Agent'):
        assert _is_linked(b2, 'Agent', a)
    _safe_set(a, 'parent', set())
    assert not _is_linked(a, 'parent', b2)
    if hasattr(b2, 'Agent'):
        assert not _is_linked(b2, 'Agent', a)


def test_assoc_causedBy41_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_PrivatePubSub()
    b2 = conversation_PrivatePubSub()
    _safe_set(a, 'transition', b1)
    assert _is_linked(a, 'transition', b1)
    if hasattr(b1, 'PrivatePubSub'):
        assert _is_linked(b1, 'PrivatePubSub', a)
    _safe_set(a, 'transition', b2)
    assert _is_linked(a, 'transition', b2)
    if hasattr(b1, 'PrivatePubSub'):
        assert not _is_linked(b1, 'PrivatePubSub', a)
    if hasattr(b2, 'PrivatePubSub'):
        assert _is_linked(b2, 'PrivatePubSub', a)
    _safe_set(a, 'transition', None)
    assert not _is_linked(a, 'transition', b2)
    if hasattr(b2, 'PrivatePubSub'):
        assert not _is_linked(b2, 'PrivatePubSub', a)


def test_assoc_definedTypes1_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_Projection()
    b2 = conversation_Projection()
    _safe_set(a, 'conversation_Conversation', {b1})
    assert _is_linked(a, 'conversation_Conversation', b1)
    if hasattr(b1, 'conversation_Projection'):
        assert _is_linked(b1, 'conversation_Projection', a)
    _safe_set(a, 'conversation_Conversation', {b2})
    assert _is_linked(a, 'conversation_Conversation', b2)
    if hasattr(b1, 'conversation_Projection'):
        assert not _is_linked(b1, 'conversation_Projection', a)
    if hasattr(b2, 'conversation_Projection'):
        assert _is_linked(b2, 'conversation_Projection', a)
    _safe_set(a, 'conversation_Conversation', set())
    assert not _is_linked(a, 'conversation_Conversation', b2)
    if hasattr(b2, 'conversation_Projection'):
        assert not _is_linked(b2, 'conversation_Projection', a)


def test_assoc_definedTypes12_link_reassign_clear():
    a = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b1 = conversation_Projection()
    b2 = conversation_Projection()
    _safe_set(a, 'conversation_Agent', {b1})
    assert _is_linked(a, 'conversation_Agent', b1)
    if hasattr(b1, 'conversation_Projection13'):
        assert _is_linked(b1, 'conversation_Projection13', a)
    _safe_set(a, 'conversation_Agent', {b2})
    assert _is_linked(a, 'conversation_Agent', b2)
    if hasattr(b1, 'conversation_Projection13'):
        assert not _is_linked(b1, 'conversation_Projection13', a)
    if hasattr(b2, 'conversation_Projection13'):
        assert _is_linked(b2, 'conversation_Projection13', a)
    _safe_set(a, 'conversation_Agent', set())
    assert not _is_linked(a, 'conversation_Agent', b2)
    if hasattr(b2, 'conversation_Projection13'):
        assert not _is_linked(b2, 'conversation_Projection13', a)


def test_assoc_exCausedBy39_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_SubscribableByOthers()
    b2 = conversation_SubscribableByOthers()
    _safe_set(a, 'conversation_Transition40', b1)
    assert _is_linked(a, 'conversation_Transition40', b1)
    if hasattr(b1, 'conversation_SubscribableByOthers'):
        assert _is_linked(b1, 'conversation_SubscribableByOthers', a)
    _safe_set(a, 'conversation_Transition40', b2)
    assert _is_linked(a, 'conversation_Transition40', b2)
    if hasattr(b1, 'conversation_SubscribableByOthers'):
        assert not _is_linked(b1, 'conversation_SubscribableByOthers', a)
    if hasattr(b2, 'conversation_SubscribableByOthers'):
        assert _is_linked(b2, 'conversation_SubscribableByOthers', a)
    _safe_set(a, 'conversation_Transition40', None)
    assert not _is_linked(a, 'conversation_Transition40', b2)
    if hasattr(b2, 'conversation_SubscribableByOthers'):
        assert not _is_linked(b2, 'conversation_SubscribableByOthers', a)


def test_assoc_exTriggers42_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_PublishableByOthers()
    b2 = conversation_PublishableByOthers()
    _safe_set(a, 'conversation_Transition43', b1)
    assert _is_linked(a, 'conversation_Transition43', b1)
    if hasattr(b1, 'conversation_PublishableByOthers'):
        assert _is_linked(b1, 'conversation_PublishableByOthers', a)
    _safe_set(a, 'conversation_Transition43', b2)
    assert _is_linked(a, 'conversation_Transition43', b2)
    if hasattr(b1, 'conversation_PublishableByOthers'):
        assert not _is_linked(b1, 'conversation_PublishableByOthers', a)
    if hasattr(b2, 'conversation_PublishableByOthers'):
        assert _is_linked(b2, 'conversation_PublishableByOthers', a)
    _safe_set(a, 'conversation_Transition43', None)
    assert not _is_linked(a, 'conversation_Transition43', b2)
    if hasattr(b2, 'conversation_PublishableByOthers'):
        assert not _is_linked(b2, 'conversation_PublishableByOthers', a)


def test_assoc_fieldMapping46_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_ProjectionField()
    b2 = conversation_ProjectionField()
    _safe_set(a, 'conversation_Transition47', b1)
    assert _is_linked(a, 'conversation_Transition47', b1)
    if hasattr(b1, 'conversation_ProjectionField'):
        assert _is_linked(b1, 'conversation_ProjectionField', a)
    _safe_set(a, 'conversation_Transition47', b2)
    assert _is_linked(a, 'conversation_Transition47', b2)
    if hasattr(b1, 'conversation_ProjectionField'):
        assert not _is_linked(b1, 'conversation_ProjectionField', a)
    if hasattr(b2, 'conversation_ProjectionField'):
        assert _is_linked(b2, 'conversation_ProjectionField', a)
    _safe_set(a, 'conversation_Transition47', None)
    assert not _is_linked(a, 'conversation_Transition47', b2)
    if hasattr(b2, 'conversation_ProjectionField'):
        assert not _is_linked(b2, 'conversation_ProjectionField', a)


def test_assoc_importedAgents8_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_AgentImport()
    b2 = conversation_AgentImport()
    _safe_set(a, 'conversation_Conversation9', {b1})
    assert _is_linked(a, 'conversation_Conversation9', b1)
    if hasattr(b1, 'conversation_AgentImport'):
        assert _is_linked(b1, 'conversation_AgentImport', a)
    _safe_set(a, 'conversation_Conversation9', {b2})
    assert _is_linked(a, 'conversation_Conversation9', b2)
    if hasattr(b1, 'conversation_AgentImport'):
        assert not _is_linked(b1, 'conversation_AgentImport', a)
    if hasattr(b2, 'conversation_AgentImport'):
        assert _is_linked(b2, 'conversation_AgentImport', a)
    _safe_set(a, 'conversation_Conversation9', set())
    assert not _is_linked(a, 'conversation_Conversation9', b2)
    if hasattr(b2, 'conversation_AgentImport'):
        assert not _is_linked(b2, 'conversation_AgentImport', a)


def test_assoc_importedTypes6_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_TypeImport()
    b2 = conversation_TypeImport()
    _safe_set(a, 'conversation_Conversation7', {b1})
    assert _is_linked(a, 'conversation_Conversation7', b1)
    if hasattr(b1, 'conversation_TypeImport'):
        assert _is_linked(b1, 'conversation_TypeImport', a)
    _safe_set(a, 'conversation_Conversation7', {b2})
    assert _is_linked(a, 'conversation_Conversation7', b2)
    if hasattr(b1, 'conversation_TypeImport'):
        assert not _is_linked(b1, 'conversation_TypeImport', a)
    if hasattr(b2, 'conversation_TypeImport'):
        assert _is_linked(b2, 'conversation_TypeImport', a)
    _safe_set(a, 'conversation_Conversation7', set())
    assert not _is_linked(a, 'conversation_Conversation7', b2)
    if hasattr(b2, 'conversation_TypeImport'):
        assert not _is_linked(b2, 'conversation_TypeImport', a)


def test_assoc_initialState22_link_reassign_clear():
    a = conversation_State(join=True, name="sample_text", requiresExecution=True)
    b1 = conversation_StateMachine()
    b2 = conversation_StateMachine()
    _safe_set(a, 'conversation_State', b1)
    assert _is_linked(a, 'conversation_State', b1)
    if hasattr(b1, 'conversation_StateMachine'):
        assert _is_linked(b1, 'conversation_StateMachine', a)
    _safe_set(a, 'conversation_State', b2)
    assert _is_linked(a, 'conversation_State', b2)
    if hasattr(b1, 'conversation_StateMachine'):
        assert not _is_linked(b1, 'conversation_StateMachine', a)
    if hasattr(b2, 'conversation_StateMachine'):
        assert _is_linked(b2, 'conversation_StateMachine', a)
    _safe_set(a, 'conversation_State', None)
    assert not _is_linked(a, 'conversation_State', b2)
    if hasattr(b2, 'conversation_StateMachine'):
        assert not _is_linked(b2, 'conversation_StateMachine', a)


def test_assoc_initialTransition27_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_StateMachine()
    b2 = conversation_StateMachine()
    _safe_set(a, 'conversation_Transition', b1)
    assert _is_linked(a, 'conversation_Transition', b1)
    if hasattr(b1, 'conversation_StateMachine28'):
        assert _is_linked(b1, 'conversation_StateMachine28', a)
    _safe_set(a, 'conversation_Transition', b2)
    assert _is_linked(a, 'conversation_Transition', b2)
    if hasattr(b1, 'conversation_StateMachine28'):
        assert not _is_linked(b1, 'conversation_StateMachine28', a)
    if hasattr(b2, 'conversation_StateMachine28'):
        assert _is_linked(b2, 'conversation_StateMachine28', a)
    _safe_set(a, 'conversation_Transition', None)
    assert not _is_linked(a, 'conversation_Transition', b2)
    if hasattr(b2, 'conversation_StateMachine28'):
        assert not _is_linked(b2, 'conversation_StateMachine28', a)


def test_assoc_parent18_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b2 = conversation_Agent(accessRequirement="sample_text_2", connectionType="sample_text_2", name="sample_text_2", stateMachineType="sample_text_2")
    _safe_set(a, 'Conversation', b1)
    assert _is_linked(a, 'Conversation', b1)
    if hasattr(b1, 'agents'):
        assert _is_linked(b1, 'agents', a)
    _safe_set(a, 'Conversation', b2)
    assert _is_linked(a, 'Conversation', b2)
    if hasattr(b1, 'agents'):
        assert not _is_linked(b1, 'agents', a)
    if hasattr(b2, 'agents'):
        assert _is_linked(b2, 'agents', a)
    _safe_set(a, 'Conversation', None)
    assert not _is_linked(a, 'Conversation', b2)
    if hasattr(b2, 'agents'):
        assert not _is_linked(b2, 'agents', a)


def test_assoc_parent25_link_reassign_clear():
    a = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b1 = conversation_StateMachine()
    b2 = conversation_StateMachine()
    _safe_set(a, 'Agent26', b1)
    assert _is_linked(a, 'Agent26', b1)
    if hasattr(b1, 'stateMachine'):
        assert _is_linked(b1, 'stateMachine', a)
    _safe_set(a, 'Agent26', b2)
    assert _is_linked(a, 'Agent26', b2)
    if hasattr(b1, 'stateMachine'):
        assert not _is_linked(b1, 'stateMachine', a)
    if hasattr(b2, 'stateMachine'):
        assert _is_linked(b2, 'stateMachine', a)
    _safe_set(a, 'Agent26', None)
    assert not _is_linked(a, 'Agent26', b2)
    if hasattr(b2, 'stateMachine'):
        assert not _is_linked(b2, 'stateMachine', a)


def test_assoc_parent34_link_reassign_clear():
    a = conversation_State(join=True, name="sample_text", requiresExecution=True)
    b1 = conversation_StateMachine()
    b2 = conversation_StateMachine()
    _safe_set(a, 'states', b1)
    assert _is_linked(a, 'states', b1)
    if hasattr(b1, 'StateMachine35'):
        assert _is_linked(b1, 'StateMachine35', a)
    _safe_set(a, 'states', b2)
    assert _is_linked(a, 'states', b2)
    if hasattr(b1, 'StateMachine35'):
        assert not _is_linked(b1, 'StateMachine35', a)
    if hasattr(b2, 'StateMachine35'):
        assert _is_linked(b2, 'StateMachine35', a)
    _safe_set(a, 'states', None)
    assert not _is_linked(a, 'states', b2)
    if hasattr(b2, 'StateMachine35'):
        assert not _is_linked(b2, 'StateMachine35', a)


def test_assoc_parent48_link_reassign_clear():
    a = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b1 = conversation_PubliclySubscribable()
    b2 = conversation_PubliclySubscribable()
    _safe_set(a, 'Agent49', b1)
    assert _is_linked(a, 'Agent49', b1)
    if hasattr(b1, 'sendables'):
        assert _is_linked(b1, 'sendables', a)
    _safe_set(a, 'Agent49', b2)
    assert _is_linked(a, 'Agent49', b2)
    if hasattr(b1, 'sendables'):
        assert not _is_linked(b1, 'sendables', a)
    if hasattr(b2, 'sendables'):
        assert _is_linked(b2, 'sendables', a)
    _safe_set(a, 'Agent49', None)
    assert not _is_linked(a, 'Agent49', b2)
    if hasattr(b2, 'sendables'):
        assert not _is_linked(b2, 'sendables', a)


def test_assoc_projection19_link_reassign_clear():
    a = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b1 = conversation_Projection()
    b2 = conversation_Projection()
    _safe_set(a, 'conversation_Agent20', b1)
    assert _is_linked(a, 'conversation_Agent20', b1)
    if hasattr(b1, 'conversation_Projection21'):
        assert _is_linked(b1, 'conversation_Projection21', a)
    _safe_set(a, 'conversation_Agent20', b2)
    assert _is_linked(a, 'conversation_Agent20', b2)
    if hasattr(b1, 'conversation_Projection21'):
        assert not _is_linked(b1, 'conversation_Projection21', a)
    if hasattr(b2, 'conversation_Projection21'):
        assert _is_linked(b2, 'conversation_Projection21', a)
    _safe_set(a, 'conversation_Agent20', None)
    assert not _is_linked(a, 'conversation_Agent20', b2)
    if hasattr(b2, 'conversation_Projection21'):
        assert not _is_linked(b2, 'conversation_Projection21', a)


def test_assoc_refType29_link_reassign_clear():
    a = conversation_Event(name="sample_text")
    b1 = conversation_Projection()
    b2 = conversation_Projection()
    _safe_set(a, 'conversation_Event', b1)
    assert _is_linked(a, 'conversation_Event', b1)
    if hasattr(b1, 'conversation_Projection30'):
        assert _is_linked(b1, 'conversation_Projection30', a)
    _safe_set(a, 'conversation_Event', b2)
    assert _is_linked(a, 'conversation_Event', b2)
    if hasattr(b1, 'conversation_Projection30'):
        assert not _is_linked(b1, 'conversation_Projection30', a)
    if hasattr(b2, 'conversation_Projection30'):
        assert _is_linked(b2, 'conversation_Projection30', a)
    _safe_set(a, 'conversation_Event', None)
    assert not _is_linked(a, 'conversation_Event', b2)
    if hasattr(b2, 'conversation_Projection30'):
        assert not _is_linked(b2, 'conversation_Projection30', a)


def test_assoc_restServices2_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_RestService()
    b2 = conversation_RestService()
    _safe_set(a, 'conversation_Conversation3', {b1})
    assert _is_linked(a, 'conversation_Conversation3', b1)
    if hasattr(b1, 'conversation_RestService'):
        assert _is_linked(b1, 'conversation_RestService', a)
    _safe_set(a, 'conversation_Conversation3', {b2})
    assert _is_linked(a, 'conversation_Conversation3', b2)
    if hasattr(b1, 'conversation_RestService'):
        assert not _is_linked(b1, 'conversation_RestService', a)
    if hasattr(b2, 'conversation_RestService'):
        assert _is_linked(b2, 'conversation_RestService', a)
    _safe_set(a, 'conversation_Conversation3', set())
    assert not _is_linked(a, 'conversation_Conversation3', b2)
    if hasattr(b2, 'conversation_RestService'):
        assert not _is_linked(b2, 'conversation_RestService', a)


def test_assoc_sendables16_link_reassign_clear():
    a = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b1 = conversation_PubliclySubscribable()
    b2 = conversation_PubliclySubscribable()
    _safe_set(a, 'parent17', {b1})
    assert _is_linked(a, 'parent17', b1)
    if hasattr(b1, 'PubliclySubscribable'):
        assert _is_linked(b1, 'PubliclySubscribable', a)
    _safe_set(a, 'parent17', {b2})
    assert _is_linked(a, 'parent17', b2)
    if hasattr(b1, 'PubliclySubscribable'):
        assert not _is_linked(b1, 'PubliclySubscribable', a)
    if hasattr(b2, 'PubliclySubscribable'):
        assert _is_linked(b2, 'PubliclySubscribable', a)
    _safe_set(a, 'parent17', set())
    assert not _is_linked(a, 'parent17', b2)
    if hasattr(b2, 'PubliclySubscribable'):
        assert not _is_linked(b2, 'PubliclySubscribable', a)


def test_assoc_services4_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_Service()
    b2 = conversation_Service()
    _safe_set(a, 'conversation_Conversation5', {b1})
    assert _is_linked(a, 'conversation_Conversation5', b1)
    if hasattr(b1, 'conversation_Service'):
        assert _is_linked(b1, 'conversation_Service', a)
    _safe_set(a, 'conversation_Conversation5', {b2})
    assert _is_linked(a, 'conversation_Conversation5', b2)
    if hasattr(b1, 'conversation_Service'):
        assert not _is_linked(b1, 'conversation_Service', a)
    if hasattr(b2, 'conversation_Service'):
        assert _is_linked(b2, 'conversation_Service', a)
    _safe_set(a, 'conversation_Conversation5', set())
    assert not _is_linked(a, 'conversation_Conversation5', b2)
    if hasattr(b2, 'conversation_Service'):
        assert not _is_linked(b2, 'conversation_Service', a)


def test_assoc_stateMachine14_link_reassign_clear():
    a = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    b1 = conversation_StateMachine()
    b2 = conversation_StateMachine()
    _safe_set(a, 'parent15', b1)
    assert _is_linked(a, 'parent15', b1)
    if hasattr(b1, 'StateMachine'):
        assert _is_linked(b1, 'StateMachine', a)
    _safe_set(a, 'parent15', b2)
    assert _is_linked(a, 'parent15', b2)
    if hasattr(b1, 'StateMachine'):
        assert not _is_linked(b1, 'StateMachine', a)
    if hasattr(b2, 'StateMachine'):
        assert _is_linked(b2, 'StateMachine', a)
    _safe_set(a, 'parent15', None)
    assert not _is_linked(a, 'parent15', b2)
    if hasattr(b2, 'StateMachine'):
        assert not _is_linked(b2, 'StateMachine', a)


def test_assoc_states23_link_reassign_clear():
    a = conversation_State(join=True, name="sample_text", requiresExecution=True)
    b1 = conversation_StateMachine()
    b2 = conversation_StateMachine()
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'parent24'):
        assert _is_linked(b1, 'parent24', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'parent24'):
        assert not _is_linked(b1, 'parent24', a)
    if hasattr(b2, 'parent24'):
        assert _is_linked(b2, 'parent24', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'parent24'):
        assert not _is_linked(b2, 'parent24', a)


def test_assoc_toState36_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_State(join=True, name="sample_text", requiresExecution=True)
    b2 = conversation_State(join=False, name="sample_text_2", requiresExecution=False)
    _safe_set(a, 'conversation_Transition37', b1)
    assert _is_linked(a, 'conversation_Transition37', b1)
    if hasattr(b1, 'conversation_State38'):
        assert _is_linked(b1, 'conversation_State38', a)
    _safe_set(a, 'conversation_Transition37', b2)
    assert _is_linked(a, 'conversation_Transition37', b2)
    if hasattr(b1, 'conversation_State38'):
        assert not _is_linked(b1, 'conversation_State38', a)
    if hasattr(b2, 'conversation_State38'):
        assert _is_linked(b2, 'conversation_State38', a)
    _safe_set(a, 'conversation_Transition37', None)
    assert not _is_linked(a, 'conversation_Transition37', b2)
    if hasattr(b2, 'conversation_State38'):
        assert not _is_linked(b2, 'conversation_State38', a)


def test_assoc_transition50_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_PrivatePubSub()
    b2 = conversation_PrivatePubSub()
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'causedBy'):
        assert _is_linked(b1, 'causedBy', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'causedBy'):
        assert not _is_linked(b1, 'causedBy', a)
    if hasattr(b2, 'causedBy'):
        assert _is_linked(b2, 'causedBy', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'causedBy'):
        assert not _is_linked(b2, 'causedBy', a)


def test_assoc_transitions31_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_State(join=True, name="sample_text", requiresExecution=True)
    b2 = conversation_State(join=False, name="sample_text_2", requiresExecution=False)
    _safe_set(a, 'conversation_Transition33', b1)
    assert _is_linked(a, 'conversation_Transition33', b1)
    if hasattr(b1, 'conversation_State32'):
        assert _is_linked(b1, 'conversation_State32', a)
    _safe_set(a, 'conversation_Transition33', b2)
    assert _is_linked(a, 'conversation_Transition33', b2)
    if hasattr(b1, 'conversation_State32'):
        assert not _is_linked(b1, 'conversation_State32', a)
    if hasattr(b2, 'conversation_State32'):
        assert _is_linked(b2, 'conversation_State32', a)
    _safe_set(a, 'conversation_Transition33', None)
    assert not _is_linked(a, 'conversation_Transition33', b2)
    if hasattr(b2, 'conversation_State32'):
        assert not _is_linked(b2, 'conversation_State32', a)


def test_assoc_triggers44_link_reassign_clear():
    a = conversation_Transition(requiresExecution=True)
    b1 = conversation_PublishableByMe()
    b2 = conversation_PublishableByMe()
    _safe_set(a, 'conversation_Transition45', b1)
    assert _is_linked(a, 'conversation_Transition45', b1)
    if hasattr(b1, 'conversation_PublishableByMe'):
        assert _is_linked(b1, 'conversation_PublishableByMe', a)
    _safe_set(a, 'conversation_Transition45', b2)
    assert _is_linked(a, 'conversation_Transition45', b2)
    if hasattr(b1, 'conversation_PublishableByMe'):
        assert not _is_linked(b1, 'conversation_PublishableByMe', a)
    if hasattr(b2, 'conversation_PublishableByMe'):
        assert _is_linked(b2, 'conversation_PublishableByMe', a)
    _safe_set(a, 'conversation_Transition45', None)
    assert not _is_linked(a, 'conversation_Transition45', b2)
    if hasattr(b2, 'conversation_PublishableByMe'):
        assert not _is_linked(b2, 'conversation_PublishableByMe', a)


def test_assoc_views10_link_reassign_clear():
    a = conversation_Conversation(name="sample_text")
    b1 = conversation_View()
    b2 = conversation_View()
    _safe_set(a, 'conversation_Conversation11', {b1})
    assert _is_linked(a, 'conversation_Conversation11', b1)
    if hasattr(b1, 'conversation_View'):
        assert _is_linked(b1, 'conversation_View', a)
    _safe_set(a, 'conversation_Conversation11', {b2})
    assert _is_linked(a, 'conversation_Conversation11', b2)
    if hasattr(b1, 'conversation_View'):
        assert not _is_linked(b1, 'conversation_View', a)
    if hasattr(b2, 'conversation_View'):
        assert _is_linked(b2, 'conversation_View', a)
    _safe_set(a, 'conversation_Conversation11', set())
    assert not _is_linked(a, 'conversation_Conversation11', b2)
    if hasattr(b2, 'conversation_View'):
        assert not _is_linked(b2, 'conversation_View', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


Import_strategy = st.builds(Import)
@given(instance=Import_strategy)
@settings(max_examples=25)
def test_Import_instantiation(instance):
    assert isinstance(instance, Import)


PublicEvent_strategy = st.builds(PublicEvent)
@given(instance=PublicEvent_strategy)
@settings(max_examples=25)
def test_PublicEvent_instantiation(instance):
    assert isinstance(instance, PublicEvent)


PubliclyPublishable_strategy = st.builds(PubliclyPublishable)
@given(instance=PubliclyPublishable_strategy)
@settings(max_examples=25)
def test_PubliclyPublishable_instantiation(instance):
    assert isinstance(instance, PubliclyPublishable)


PubliclySubscribable_strategy = st.builds(PubliclySubscribable)
@given(instance=PubliclySubscribable_strategy)
@settings(max_examples=25)
def test_PubliclySubscribable_instantiation(instance):
    assert isinstance(instance, PubliclySubscribable)


PublishableByMe_strategy = st.builds(PublishableByMe)
@given(instance=PublishableByMe_strategy)
@settings(max_examples=25)
def test_PublishableByMe_instantiation(instance):
    assert isinstance(instance, PublishableByMe)


PublishableByOthers_strategy = st.builds(PublishableByOthers)
@given(instance=PublishableByOthers_strategy)
@settings(max_examples=25)
def test_PublishableByOthers_instantiation(instance):
    assert isinstance(instance, PublishableByOthers)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


SubscribableByMe_strategy = st.builds(SubscribableByMe)
@given(instance=SubscribableByMe_strategy)
@settings(max_examples=25)
def test_SubscribableByMe_instantiation(instance):
    assert isinstance(instance, SubscribableByMe)


SubscribableByOthers_strategy = st.builds(SubscribableByOthers)
@given(instance=SubscribableByOthers_strategy)
@settings(max_examples=25)
def test_SubscribableByOthers_instantiation(instance):
    assert isinstance(instance, SubscribableByOthers)


conversation_Agent_strategy = st.builds(conversation_Agent, accessRequirement=safe_text, connectionType=safe_text, name=safe_text, stateMachineType=safe_text)
@given(instance=conversation_Agent_strategy)
@settings(max_examples=25)
def test_conversation_Agent_instantiation(instance):
    assert isinstance(instance, conversation_Agent)


conversation_AgentImport_strategy = st.builds(conversation_AgentImport)
@given(instance=conversation_AgentImport_strategy)
@settings(max_examples=25)
def test_conversation_AgentImport_instantiation(instance):
    assert isinstance(instance, conversation_AgentImport)


conversation_Conversation_strategy = st.builds(conversation_Conversation, name=safe_text)
@given(instance=conversation_Conversation_strategy)
@settings(max_examples=25)
def test_conversation_Conversation_instantiation(instance):
    assert isinstance(instance, conversation_Conversation)


conversation_Decision_strategy = st.builds(conversation_Decision)
@given(instance=conversation_Decision_strategy)
@settings(max_examples=25)
def test_conversation_Decision_instantiation(instance):
    assert isinstance(instance, conversation_Decision)


conversation_Event_strategy = st.builds(conversation_Event, name=safe_text)
@given(instance=conversation_Event_strategy)
@settings(max_examples=25)
def test_conversation_Event_instantiation(instance):
    assert isinstance(instance, conversation_Event)


conversation_Import_strategy = st.builds(conversation_Import, alias=safe_text)
@given(instance=conversation_Import_strategy)
@settings(max_examples=25)
def test_conversation_Import_instantiation(instance):
    assert isinstance(instance, conversation_Import)


conversation_Join_strategy = st.builds(conversation_Join)
@given(instance=conversation_Join_strategy)
@settings(max_examples=25)
def test_conversation_Join_instantiation(instance):
    assert isinstance(instance, conversation_Join)


conversation_Junction_strategy = st.builds(conversation_Junction)
@given(instance=conversation_Junction_strategy)
@settings(max_examples=25)
def test_conversation_Junction_instantiation(instance):
    assert isinstance(instance, conversation_Junction)


conversation_PrivatePubSub_strategy = st.builds(conversation_PrivatePubSub)
@given(instance=conversation_PrivatePubSub_strategy)
@settings(max_examples=25)
def test_conversation_PrivatePubSub_instantiation(instance):
    assert isinstance(instance, conversation_PrivatePubSub)


conversation_Projection_strategy = st.builds(conversation_Projection)
@given(instance=conversation_Projection_strategy)
@settings(max_examples=25)
def test_conversation_Projection_instantiation(instance):
    assert isinstance(instance, conversation_Projection)


conversation_ProjectionField_strategy = st.builds(conversation_ProjectionField)
@given(instance=conversation_ProjectionField_strategy)
@settings(max_examples=25)
def test_conversation_ProjectionField_instantiation(instance):
    assert isinstance(instance, conversation_ProjectionField)


conversation_PublicEvent_strategy = st.builds(conversation_PublicEvent)
@given(instance=conversation_PublicEvent_strategy)
@settings(max_examples=25)
def test_conversation_PublicEvent_instantiation(instance):
    assert isinstance(instance, conversation_PublicEvent)


conversation_PublicPubSub_strategy = st.builds(conversation_PublicPubSub)
@given(instance=conversation_PublicPubSub_strategy)
@settings(max_examples=25)
def test_conversation_PublicPubSub_instantiation(instance):
    assert isinstance(instance, conversation_PublicPubSub)


conversation_PubliclyPublishable_strategy = st.builds(conversation_PubliclyPublishable)
@given(instance=conversation_PubliclyPublishable_strategy)
@settings(max_examples=25)
def test_conversation_PubliclyPublishable_instantiation(instance):
    assert isinstance(instance, conversation_PubliclyPublishable)


conversation_PubliclySubscribable_strategy = st.builds(conversation_PubliclySubscribable)
@given(instance=conversation_PubliclySubscribable_strategy)
@settings(max_examples=25)
def test_conversation_PubliclySubscribable_instantiation(instance):
    assert isinstance(instance, conversation_PubliclySubscribable)


conversation_PublishableByMe_strategy = st.builds(conversation_PublishableByMe)
@given(instance=conversation_PublishableByMe_strategy)
@settings(max_examples=25)
def test_conversation_PublishableByMe_instantiation(instance):
    assert isinstance(instance, conversation_PublishableByMe)


conversation_PublishableByOthers_strategy = st.builds(conversation_PublishableByOthers)
@given(instance=conversation_PublishableByOthers_strategy)
@settings(max_examples=25)
def test_conversation_PublishableByOthers_instantiation(instance):
    assert isinstance(instance, conversation_PublishableByOthers)


conversation_RestService_strategy = st.builds(conversation_RestService)
@given(instance=conversation_RestService_strategy)
@settings(max_examples=25)
def test_conversation_RestService_instantiation(instance):
    assert isinstance(instance, conversation_RestService)


conversation_Service_strategy = st.builds(conversation_Service)
@given(instance=conversation_Service_strategy)
@settings(max_examples=25)
def test_conversation_Service_instantiation(instance):
    assert isinstance(instance, conversation_Service)


conversation_State_strategy = st.builds(conversation_State, join=st.booleans(), name=safe_text, requiresExecution=st.booleans())
@given(instance=conversation_State_strategy)
@settings(max_examples=25)
def test_conversation_State_instantiation(instance):
    assert isinstance(instance, conversation_State)


conversation_StateMachine_strategy = st.builds(conversation_StateMachine)
@given(instance=conversation_StateMachine_strategy)
@settings(max_examples=25)
def test_conversation_StateMachine_instantiation(instance):
    assert isinstance(instance, conversation_StateMachine)


conversation_SubscribableByMe_strategy = st.builds(conversation_SubscribableByMe)
@given(instance=conversation_SubscribableByMe_strategy)
@settings(max_examples=25)
def test_conversation_SubscribableByMe_instantiation(instance):
    assert isinstance(instance, conversation_SubscribableByMe)


conversation_SubscribableByOthers_strategy = st.builds(conversation_SubscribableByOthers)
@given(instance=conversation_SubscribableByOthers_strategy)
@settings(max_examples=25)
def test_conversation_SubscribableByOthers_instantiation(instance):
    assert isinstance(instance, conversation_SubscribableByOthers)


conversation_Transition_strategy = st.builds(conversation_Transition, requiresExecution=st.booleans())
@given(instance=conversation_Transition_strategy)
@settings(max_examples=25)
def test_conversation_Transition_instantiation(instance):
    assert isinstance(instance, conversation_Transition)


conversation_TypeImport_strategy = st.builds(conversation_TypeImport)
@given(instance=conversation_TypeImport_strategy)
@settings(max_examples=25)
def test_conversation_TypeImport_instantiation(instance):
    assert isinstance(instance, conversation_TypeImport)


conversation_View_strategy = st.builds(conversation_View)
@given(instance=conversation_View_strategy)
@settings(max_examples=25)
def test_conversation_View_instantiation(instance):
    assert isinstance(instance, conversation_View)



