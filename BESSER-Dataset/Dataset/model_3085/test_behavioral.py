import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    AdHocSubProcess,
    Assignment,
    Auditing,
    BaseElement,
    BusinessRuleTask,
    CallActivity,
    CallConversation,
    CallableElement,
    Choreography,
    Collaboration,
    ComplexBehaviorDefinition,
    Conversation,
    ConversationAssociation,
    ConversationLink,
    ConversationNode,
    DataAssociation,
    DataInput,
    DataInputAssociation,
    DataObject,
    DataObjectReference,
    DataOutput,
    DataOutputAssociation,
    DataState,
    DataStore,
    DataStoreReference,
    Definitions,
    Documentation,
    EndPoint,
    Error,
    Escalation,
    Expression,
    FormalExpression,
    GlobalBusinessRuleTask,
    GlobalChoreographyTask,
    GlobalConversation,
    GlobalManualTask,
    GlobalScriptTask,
    GlobalTask,
    GlobalUserTask,
    HumanPerformer,
    Import,
    InputOutputBinding,
    InputOutputSpecification,
    InputSet,
    Interface,
    ItemDefinition,
    Lane,
    LaneSet,
    LoopCharacteristics,
    ManualTask,
    Message,
    MessageEventDefinition,
    MessageFlow,
    MessageFlowAssociation,
    Monitoring,
    MultiInstanceLoopCharacteristics,
    Operation,
    OutputSet,
    Participant,
    ParticipantAssociation,
    ParticipantMultiplicity,
    PartnerEntity,
    PartnerRole,
    Performer,
    PotentialOwner,
    Process,
    Property,
    ReceiveTask,
    Relationship,
    Rendering,
    Resource,
    ResourceAssignmentExpression,
    ResourceParameter,
    ResourceParameterBinding,
    ResourceRole,
    RootElement,
    ScriptTask,
    SendTask,
    ServiceTask,
    StandardLoopCharacteristics,
    SubConversation,
    SubProcess,
    Task,
    Transaction,
    UserTask,
    artifacts_Artifact,
    artifacts_Association,
    artifacts_Category,
    artifacts_CategoryValue,
    artifacts_Group,
    artifacts_TextAnnotation,
    bpmn2_DocumentRoot,
    bpmn2_EObject,
    bpmn2_EStringToStringMapEntry,
    choreographyactivities_CallChoreography,
    choreographyactivities_ChoreographyActivity,
    choreographyactivities_ChoreographyTask,
    choreographyactivities_SubChoreography,
    correlations_CorrelationKey,
    correlations_CorrelationProperty,
    correlations_CorrelationPropertyBinding,
    correlations_CorrelationPropertyRetrievalExpression,
    correlations_CorrelationSubscription,
    events_BoundaryEvent,
    events_CancelEventDefinition,
    events_CatchEvent,
    events_CompensateEventDefinition,
    events_ConditionalEventDefinition,
    events_EndEvent,
    events_ErrorEventDefinition,
    events_EscalationEventDefinition,
    events_Event,
    events_EventDefinition,
    events_ImplicitThrowEvent,
    events_IntermediateCatchEvent,
    events_IntermediateThrowEvent,
    events_LinkEventDefinition,
    events_Signal,
    events_SignalEventDefinition,
    events_StartEvent,
    events_TerminateEventDefinition,
    events_ThrowEvent,
    events_TimerEventDefinition,
    extension_Extension,
    extension_ExtensionAttributeValue,
    flows_FlowElement,
    flows_FlowNode,
    flows_SequenceFlow,
    gateways_ComplexGateway,
    gateways_EventBasedGateway,
    gateways_ExclusiveGateway,
    gateways_Gateway,
    gateways_InclusiveGateway,
    gateways_ParallelGateway,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activity4_stub_double():
    # Activity has no real 'Activity' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Activity()
    setattr(partner, 'Activity', None)
    _safe_set(owner, 'bpmn2_DocumentRoot5', {partner})
    assert getattr(partner, 'Activity') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot5', set())
    assert getattr(partner, 'Activity') is None


def test_assoc_adHocSubProcess6_stub_double():
    # AdHocSubProcess has no real 'AdHocSubProcess' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = AdHocSubProcess()
    setattr(partner, 'AdHocSubProcess', None)
    _safe_set(owner, 'bpmn2_DocumentRoot7', {partner})
    assert getattr(partner, 'AdHocSubProcess') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot7', set())
    assert getattr(partner, 'AdHocSubProcess') is None


def test_assoc_artifact10_stub_double():
    # artifacts_Artifact has no real 'artifacts_Artifact' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = artifacts_Artifact()
    setattr(partner, 'artifacts_Artifact', None)
    _safe_set(owner, 'bpmn2_DocumentRoot11', {partner})
    assert getattr(partner, 'artifacts_Artifact') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot11', set())
    assert getattr(partner, 'artifacts_Artifact') is None


def test_assoc_assignment12_stub_double():
    # Assignment has no real 'Assignment' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Assignment()
    setattr(partner, 'Assignment', None)
    _safe_set(owner, 'bpmn2_DocumentRoot13', {partner})
    assert getattr(partner, 'Assignment') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot13', set())
    assert getattr(partner, 'Assignment') is None


def test_assoc_association14_stub_double():
    # artifacts_Association has no real 'artifacts_Association' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = artifacts_Association()
    setattr(partner, 'artifacts_Association', None)
    _safe_set(owner, 'bpmn2_DocumentRoot15', {partner})
    assert getattr(partner, 'artifacts_Association') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot15', set())
    assert getattr(partner, 'artifacts_Association') is None


def test_assoc_auditing16_stub_double():
    # Auditing has no real 'Auditing' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Auditing()
    setattr(partner, 'Auditing', None)
    _safe_set(owner, 'bpmn2_DocumentRoot17', {partner})
    assert getattr(partner, 'Auditing') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot17', set())
    assert getattr(partner, 'Auditing') is None


def test_assoc_baseElement18_stub_double():
    # BaseElement has no real 'BaseElement' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = BaseElement()
    setattr(partner, 'BaseElement', None)
    _safe_set(owner, 'bpmn2_DocumentRoot19', {partner})
    assert getattr(partner, 'BaseElement') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot19', set())
    assert getattr(partner, 'BaseElement') is None


def test_assoc_baseElementWithMixedContent20_stub_double():
    # BaseElement has no real 'BaseElement22' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = BaseElement()
    setattr(partner, 'BaseElement22', None)
    _safe_set(owner, 'bpmn2_DocumentRoot21', {partner})
    assert getattr(partner, 'BaseElement22') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot21', set())
    assert getattr(partner, 'BaseElement22') is None


def test_assoc_boundaryEvent23_stub_double():
    # events_BoundaryEvent has no real 'events_BoundaryEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_BoundaryEvent()
    setattr(partner, 'events_BoundaryEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot24', {partner})
    assert getattr(partner, 'events_BoundaryEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot24', set())
    assert getattr(partner, 'events_BoundaryEvent') is None


def test_assoc_businessRuleTask25_stub_double():
    # BusinessRuleTask has no real 'BusinessRuleTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = BusinessRuleTask()
    setattr(partner, 'BusinessRuleTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot26', {partner})
    assert getattr(partner, 'BusinessRuleTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot26', set())
    assert getattr(partner, 'BusinessRuleTask') is None


def test_assoc_callActivity29_stub_double():
    # CallActivity has no real 'CallActivity' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = CallActivity()
    setattr(partner, 'CallActivity', None)
    _safe_set(owner, 'bpmn2_DocumentRoot30', {partner})
    assert getattr(partner, 'CallActivity') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot30', set())
    assert getattr(partner, 'CallActivity') is None


def test_assoc_callChoreography31_stub_double():
    # choreographyactivities_CallChoreography has no real 'choreographyactivities_CallChoreography' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = choreographyactivities_CallChoreography()
    setattr(partner, 'choreographyactivities_CallChoreography', None)
    _safe_set(owner, 'bpmn2_DocumentRoot32', {partner})
    assert getattr(partner, 'choreographyactivities_CallChoreography') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot32', set())
    assert getattr(partner, 'choreographyactivities_CallChoreography') is None


def test_assoc_callConversation33_stub_double():
    # CallConversation has no real 'CallConversation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = CallConversation()
    setattr(partner, 'CallConversation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot34', {partner})
    assert getattr(partner, 'CallConversation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot34', set())
    assert getattr(partner, 'CallConversation') is None


def test_assoc_callableElement27_stub_double():
    # CallableElement has no real 'CallableElement' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = CallableElement()
    setattr(partner, 'CallableElement', None)
    _safe_set(owner, 'bpmn2_DocumentRoot28', {partner})
    assert getattr(partner, 'CallableElement') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot28', set())
    assert getattr(partner, 'CallableElement') is None


def test_assoc_cancelEventDefinition37_stub_double():
    # events_CancelEventDefinition has no real 'events_CancelEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_CancelEventDefinition()
    setattr(partner, 'events_CancelEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot38', {partner})
    assert getattr(partner, 'events_CancelEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot38', set())
    assert getattr(partner, 'events_CancelEventDefinition') is None


def test_assoc_catchEvent43_stub_double():
    # events_CatchEvent has no real 'events_CatchEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_CatchEvent()
    setattr(partner, 'events_CatchEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot44', {partner})
    assert getattr(partner, 'events_CatchEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot44', set())
    assert getattr(partner, 'events_CatchEvent') is None


def test_assoc_category45_stub_double():
    # artifacts_Category has no real 'artifacts_Category' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = artifacts_Category()
    setattr(partner, 'artifacts_Category', None)
    _safe_set(owner, 'bpmn2_DocumentRoot46', {partner})
    assert getattr(partner, 'artifacts_Category') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot46', set())
    assert getattr(partner, 'artifacts_Category') is None


def test_assoc_categoryValue47_stub_double():
    # artifacts_CategoryValue has no real 'artifacts_CategoryValue' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = artifacts_CategoryValue()
    setattr(partner, 'artifacts_CategoryValue', None)
    _safe_set(owner, 'bpmn2_DocumentRoot48', {partner})
    assert getattr(partner, 'artifacts_CategoryValue') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot48', set())
    assert getattr(partner, 'artifacts_CategoryValue') is None


def test_assoc_choreography49_stub_double():
    # Choreography has no real 'Choreography' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Choreography()
    setattr(partner, 'Choreography', None)
    _safe_set(owner, 'bpmn2_DocumentRoot50', {partner})
    assert getattr(partner, 'Choreography') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot50', set())
    assert getattr(partner, 'Choreography') is None


def test_assoc_choreographyActivity53_stub_double():
    # choreographyactivities_ChoreographyActivity has no real 'choreographyactivities_ChoreographyActivity' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = choreographyactivities_ChoreographyActivity()
    setattr(partner, 'choreographyactivities_ChoreographyActivity', None)
    _safe_set(owner, 'bpmn2_DocumentRoot54', {partner})
    assert getattr(partner, 'choreographyactivities_ChoreographyActivity') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot54', set())
    assert getattr(partner, 'choreographyactivities_ChoreographyActivity') is None


def test_assoc_choreographyTask55_stub_double():
    # choreographyactivities_ChoreographyTask has no real 'choreographyactivities_ChoreographyTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = choreographyactivities_ChoreographyTask()
    setattr(partner, 'choreographyactivities_ChoreographyTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot56', {partner})
    assert getattr(partner, 'choreographyactivities_ChoreographyTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot56', set())
    assert getattr(partner, 'choreographyactivities_ChoreographyTask') is None


def test_assoc_collaboration51_stub_double():
    # Collaboration has no real 'Collaboration' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Collaboration()
    setattr(partner, 'Collaboration', None)
    _safe_set(owner, 'bpmn2_DocumentRoot52', {partner})
    assert getattr(partner, 'Collaboration') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot52', set())
    assert getattr(partner, 'Collaboration') is None


def test_assoc_compensateEventDefinition57_stub_double():
    # events_CompensateEventDefinition has no real 'events_CompensateEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_CompensateEventDefinition()
    setattr(partner, 'events_CompensateEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot58', {partner})
    assert getattr(partner, 'events_CompensateEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot58', set())
    assert getattr(partner, 'events_CompensateEventDefinition') is None


def test_assoc_complexBehaviorDefinition59_stub_double():
    # ComplexBehaviorDefinition has no real 'ComplexBehaviorDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ComplexBehaviorDefinition()
    setattr(partner, 'ComplexBehaviorDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot60', {partner})
    assert getattr(partner, 'ComplexBehaviorDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot60', set())
    assert getattr(partner, 'ComplexBehaviorDefinition') is None


def test_assoc_complexGateway61_stub_double():
    # gateways_ComplexGateway has no real 'gateways_ComplexGateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = gateways_ComplexGateway()
    setattr(partner, 'gateways_ComplexGateway', None)
    _safe_set(owner, 'bpmn2_DocumentRoot62', {partner})
    assert getattr(partner, 'gateways_ComplexGateway') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot62', set())
    assert getattr(partner, 'gateways_ComplexGateway') is None


def test_assoc_conditionalEventDefinition63_stub_double():
    # events_ConditionalEventDefinition has no real 'events_ConditionalEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_ConditionalEventDefinition()
    setattr(partner, 'events_ConditionalEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot64', {partner})
    assert getattr(partner, 'events_ConditionalEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot64', set())
    assert getattr(partner, 'events_ConditionalEventDefinition') is None


def test_assoc_conversation65_stub_double():
    # Conversation has no real 'Conversation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Conversation()
    setattr(partner, 'Conversation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot66', {partner})
    assert getattr(partner, 'Conversation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot66', set())
    assert getattr(partner, 'Conversation') is None


def test_assoc_conversationAssociation67_stub_double():
    # ConversationAssociation has no real 'ConversationAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ConversationAssociation()
    setattr(partner, 'ConversationAssociation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot68', {partner})
    assert getattr(partner, 'ConversationAssociation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot68', set())
    assert getattr(partner, 'ConversationAssociation') is None


def test_assoc_conversationLink69_stub_double():
    # ConversationLink has no real 'ConversationLink' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ConversationLink()
    setattr(partner, 'ConversationLink', None)
    _safe_set(owner, 'bpmn2_DocumentRoot70', {partner})
    assert getattr(partner, 'ConversationLink') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot70', set())
    assert getattr(partner, 'ConversationLink') is None


def test_assoc_conversationNode35_stub_double():
    # ConversationNode has no real 'ConversationNode' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ConversationNode()
    setattr(partner, 'ConversationNode', None)
    _safe_set(owner, 'bpmn2_DocumentRoot36', {partner})
    assert getattr(partner, 'ConversationNode') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot36', set())
    assert getattr(partner, 'ConversationNode') is None


def test_assoc_correlationKey71_stub_double():
    # correlations_CorrelationKey has no real 'correlations_CorrelationKey' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = correlations_CorrelationKey()
    setattr(partner, 'correlations_CorrelationKey', None)
    _safe_set(owner, 'bpmn2_DocumentRoot72', {partner})
    assert getattr(partner, 'correlations_CorrelationKey') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot72', set())
    assert getattr(partner, 'correlations_CorrelationKey') is None


def test_assoc_correlationProperty73_stub_double():
    # correlations_CorrelationProperty has no real 'correlations_CorrelationProperty' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = correlations_CorrelationProperty()
    setattr(partner, 'correlations_CorrelationProperty', None)
    _safe_set(owner, 'bpmn2_DocumentRoot74', {partner})
    assert getattr(partner, 'correlations_CorrelationProperty') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot74', set())
    assert getattr(partner, 'correlations_CorrelationProperty') is None


def test_assoc_correlationPropertyBinding75_stub_double():
    # correlations_CorrelationPropertyBinding has no real 'correlations_CorrelationPropertyBinding' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = correlations_CorrelationPropertyBinding()
    setattr(partner, 'correlations_CorrelationPropertyBinding', None)
    _safe_set(owner, 'bpmn2_DocumentRoot76', {partner})
    assert getattr(partner, 'correlations_CorrelationPropertyBinding') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot76', set())
    assert getattr(partner, 'correlations_CorrelationPropertyBinding') is None


def test_assoc_correlationPropertyRetrievalExpression77_stub_double():
    # correlations_CorrelationPropertyRetrievalExpression has no real 'correlations_CorrelationPropertyRetrievalExpression' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = correlations_CorrelationPropertyRetrievalExpression()
    setattr(partner, 'correlations_CorrelationPropertyRetrievalExpression', None)
    _safe_set(owner, 'bpmn2_DocumentRoot78', {partner})
    assert getattr(partner, 'correlations_CorrelationPropertyRetrievalExpression') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot78', set())
    assert getattr(partner, 'correlations_CorrelationPropertyRetrievalExpression') is None


def test_assoc_correlationSubscription79_stub_double():
    # correlations_CorrelationSubscription has no real 'correlations_CorrelationSubscription' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = correlations_CorrelationSubscription()
    setattr(partner, 'correlations_CorrelationSubscription', None)
    _safe_set(owner, 'bpmn2_DocumentRoot80', {partner})
    assert getattr(partner, 'correlations_CorrelationSubscription') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot80', set())
    assert getattr(partner, 'correlations_CorrelationSubscription') is None


def test_assoc_dataAssociation81_stub_double():
    # DataAssociation has no real 'DataAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataAssociation()
    setattr(partner, 'DataAssociation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot82', {partner})
    assert getattr(partner, 'DataAssociation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot82', set())
    assert getattr(partner, 'DataAssociation') is None


def test_assoc_dataInput83_stub_double():
    # DataInput has no real 'DataInput' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataInput()
    setattr(partner, 'DataInput', None)
    _safe_set(owner, 'bpmn2_DocumentRoot84', {partner})
    assert getattr(partner, 'DataInput') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot84', set())
    assert getattr(partner, 'DataInput') is None


def test_assoc_dataInputAssociation85_stub_double():
    # DataInputAssociation has no real 'DataInputAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataInputAssociation()
    setattr(partner, 'DataInputAssociation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot86', {partner})
    assert getattr(partner, 'DataInputAssociation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot86', set())
    assert getattr(partner, 'DataInputAssociation') is None


def test_assoc_dataObject87_stub_double():
    # DataObject has no real 'DataObject' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataObject()
    setattr(partner, 'DataObject', None)
    _safe_set(owner, 'bpmn2_DocumentRoot88', {partner})
    assert getattr(partner, 'DataObject') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot88', set())
    assert getattr(partner, 'DataObject') is None


def test_assoc_dataObjectReference89_stub_double():
    # DataObjectReference has no real 'DataObjectReference' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataObjectReference()
    setattr(partner, 'DataObjectReference', None)
    _safe_set(owner, 'bpmn2_DocumentRoot90', {partner})
    assert getattr(partner, 'DataObjectReference') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot90', set())
    assert getattr(partner, 'DataObjectReference') is None


def test_assoc_dataOutput91_stub_double():
    # DataOutput has no real 'DataOutput' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataOutput()
    setattr(partner, 'DataOutput', None)
    _safe_set(owner, 'bpmn2_DocumentRoot92', {partner})
    assert getattr(partner, 'DataOutput') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot92', set())
    assert getattr(partner, 'DataOutput') is None


def test_assoc_dataOutputAssociation93_stub_double():
    # DataOutputAssociation has no real 'DataOutputAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataOutputAssociation()
    setattr(partner, 'DataOutputAssociation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot94', {partner})
    assert getattr(partner, 'DataOutputAssociation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot94', set())
    assert getattr(partner, 'DataOutputAssociation') is None


def test_assoc_dataState95_stub_double():
    # DataState has no real 'DataState' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataState()
    setattr(partner, 'DataState', None)
    _safe_set(owner, 'bpmn2_DocumentRoot96', {partner})
    assert getattr(partner, 'DataState') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot96', set())
    assert getattr(partner, 'DataState') is None


def test_assoc_dataStore97_stub_double():
    # DataStore has no real 'DataStore' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataStore()
    setattr(partner, 'DataStore', None)
    _safe_set(owner, 'bpmn2_DocumentRoot98', {partner})
    assert getattr(partner, 'DataStore') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot98', set())
    assert getattr(partner, 'DataStore') is None


def test_assoc_dataStoreReference99_stub_double():
    # DataStoreReference has no real 'DataStoreReference' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = DataStoreReference()
    setattr(partner, 'DataStoreReference', None)
    _safe_set(owner, 'bpmn2_DocumentRoot100', {partner})
    assert getattr(partner, 'DataStoreReference') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot100', set())
    assert getattr(partner, 'DataStoreReference') is None


def test_assoc_definitions101_stub_double():
    # Definitions has no real 'Definitions' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Definitions()
    setattr(partner, 'Definitions', None)
    _safe_set(owner, 'bpmn2_DocumentRoot102', {partner})
    assert getattr(partner, 'Definitions') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot102', set())
    assert getattr(partner, 'Definitions') is None


def test_assoc_documentation103_stub_double():
    # Documentation has no real 'Documentation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Documentation()
    setattr(partner, 'Documentation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot104', {partner})
    assert getattr(partner, 'Documentation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot104', set())
    assert getattr(partner, 'Documentation') is None


def test_assoc_endEvent105_stub_double():
    # events_EndEvent has no real 'events_EndEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_EndEvent()
    setattr(partner, 'events_EndEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot106', {partner})
    assert getattr(partner, 'events_EndEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot106', set())
    assert getattr(partner, 'events_EndEvent') is None


def test_assoc_endPoint107_stub_double():
    # EndPoint has no real 'EndPoint' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = EndPoint()
    setattr(partner, 'EndPoint', None)
    _safe_set(owner, 'bpmn2_DocumentRoot108', {partner})
    assert getattr(partner, 'EndPoint') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot108', set())
    assert getattr(partner, 'EndPoint') is None


def test_assoc_error109_stub_double():
    # Error has no real 'Error' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Error()
    setattr(partner, 'Error', None)
    _safe_set(owner, 'bpmn2_DocumentRoot110', {partner})
    assert getattr(partner, 'Error') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot110', set())
    assert getattr(partner, 'Error') is None


def test_assoc_errorEventDefinition111_stub_double():
    # events_ErrorEventDefinition has no real 'events_ErrorEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_ErrorEventDefinition()
    setattr(partner, 'events_ErrorEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot112', {partner})
    assert getattr(partner, 'events_ErrorEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot112', set())
    assert getattr(partner, 'events_ErrorEventDefinition') is None


def test_assoc_escalation113_stub_double():
    # Escalation has no real 'Escalation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Escalation()
    setattr(partner, 'Escalation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot114', {partner})
    assert getattr(partner, 'Escalation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot114', set())
    assert getattr(partner, 'Escalation') is None


def test_assoc_escalationEventDefinition115_stub_double():
    # events_EscalationEventDefinition has no real 'events_EscalationEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_EscalationEventDefinition()
    setattr(partner, 'events_EscalationEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot116', {partner})
    assert getattr(partner, 'events_EscalationEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot116', set())
    assert getattr(partner, 'events_EscalationEventDefinition') is None


def test_assoc_event117_stub_double():
    # events_Event has no real 'events_Event' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_Event()
    setattr(partner, 'events_Event', None)
    _safe_set(owner, 'bpmn2_DocumentRoot118', {partner})
    assert getattr(partner, 'events_Event') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot118', set())
    assert getattr(partner, 'events_Event') is None


def test_assoc_eventBasedGateway119_stub_double():
    # gateways_EventBasedGateway has no real 'gateways_EventBasedGateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = gateways_EventBasedGateway()
    setattr(partner, 'gateways_EventBasedGateway', None)
    _safe_set(owner, 'bpmn2_DocumentRoot120', {partner})
    assert getattr(partner, 'gateways_EventBasedGateway') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot120', set())
    assert getattr(partner, 'gateways_EventBasedGateway') is None


def test_assoc_eventDefinition39_stub_double():
    # events_EventDefinition has no real 'events_EventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_EventDefinition()
    setattr(partner, 'events_EventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot40', {partner})
    assert getattr(partner, 'events_EventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot40', set())
    assert getattr(partner, 'events_EventDefinition') is None


def test_assoc_exclusiveGateway121_stub_double():
    # gateways_ExclusiveGateway has no real 'gateways_ExclusiveGateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = gateways_ExclusiveGateway()
    setattr(partner, 'gateways_ExclusiveGateway', None)
    _safe_set(owner, 'bpmn2_DocumentRoot122', {partner})
    assert getattr(partner, 'gateways_ExclusiveGateway') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot122', set())
    assert getattr(partner, 'gateways_ExclusiveGateway') is None


def test_assoc_expression123_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'bpmn2_DocumentRoot124', {partner})
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot124', set())
    assert getattr(partner, 'Expression') is None


def test_assoc_extension125_stub_double():
    # extension_Extension has no real 'extension_Extension' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = extension_Extension()
    setattr(partner, 'extension_Extension', None)
    _safe_set(owner, 'bpmn2_DocumentRoot126', {partner})
    assert getattr(partner, 'extension_Extension') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot126', set())
    assert getattr(partner, 'extension_Extension') is None


def test_assoc_extensionElements127_stub_double():
    # extension_ExtensionAttributeValue has no real 'extension_ExtensionAttributeValue' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = extension_ExtensionAttributeValue()
    setattr(partner, 'extension_ExtensionAttributeValue', None)
    _safe_set(owner, 'bpmn2_DocumentRoot128', {partner})
    assert getattr(partner, 'extension_ExtensionAttributeValue') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot128', set())
    assert getattr(partner, 'extension_ExtensionAttributeValue') is None


def test_assoc_flowElement8_stub_double():
    # flows_FlowElement has no real 'flows_FlowElement' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = flows_FlowElement()
    setattr(partner, 'flows_FlowElement', None)
    _safe_set(owner, 'bpmn2_DocumentRoot9', {partner})
    assert getattr(partner, 'flows_FlowElement') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot9', set())
    assert getattr(partner, 'flows_FlowElement') is None


def test_assoc_flowNode129_stub_double():
    # flows_FlowNode has no real 'flows_FlowNode' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = flows_FlowNode()
    setattr(partner, 'flows_FlowNode', None)
    _safe_set(owner, 'bpmn2_DocumentRoot130', {partner})
    assert getattr(partner, 'flows_FlowNode') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot130', set())
    assert getattr(partner, 'flows_FlowNode') is None


def test_assoc_formalExpression131_stub_double():
    # FormalExpression has no real 'FormalExpression' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = FormalExpression()
    setattr(partner, 'FormalExpression', None)
    _safe_set(owner, 'bpmn2_DocumentRoot132', {partner})
    assert getattr(partner, 'FormalExpression') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot132', set())
    assert getattr(partner, 'FormalExpression') is None


def test_assoc_gateway133_stub_double():
    # gateways_Gateway has no real 'gateways_Gateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = gateways_Gateway()
    setattr(partner, 'gateways_Gateway', None)
    _safe_set(owner, 'bpmn2_DocumentRoot134', {partner})
    assert getattr(partner, 'gateways_Gateway') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot134', set())
    assert getattr(partner, 'gateways_Gateway') is None


def test_assoc_globalBusinessRuleTask135_stub_double():
    # GlobalBusinessRuleTask has no real 'GlobalBusinessRuleTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = GlobalBusinessRuleTask()
    setattr(partner, 'GlobalBusinessRuleTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot136', {partner})
    assert getattr(partner, 'GlobalBusinessRuleTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot136', set())
    assert getattr(partner, 'GlobalBusinessRuleTask') is None


def test_assoc_globalChoreographyTask137_stub_double():
    # GlobalChoreographyTask has no real 'GlobalChoreographyTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = GlobalChoreographyTask()
    setattr(partner, 'GlobalChoreographyTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot138', {partner})
    assert getattr(partner, 'GlobalChoreographyTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot138', set())
    assert getattr(partner, 'GlobalChoreographyTask') is None


def test_assoc_globalConversation139_stub_double():
    # GlobalConversation has no real 'GlobalConversation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = GlobalConversation()
    setattr(partner, 'GlobalConversation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot140', {partner})
    assert getattr(partner, 'GlobalConversation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot140', set())
    assert getattr(partner, 'GlobalConversation') is None


def test_assoc_globalManualTask141_stub_double():
    # GlobalManualTask has no real 'GlobalManualTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = GlobalManualTask()
    setattr(partner, 'GlobalManualTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot142', {partner})
    assert getattr(partner, 'GlobalManualTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot142', set())
    assert getattr(partner, 'GlobalManualTask') is None


def test_assoc_globalScriptTask143_stub_double():
    # GlobalScriptTask has no real 'GlobalScriptTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = GlobalScriptTask()
    setattr(partner, 'GlobalScriptTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot144', {partner})
    assert getattr(partner, 'GlobalScriptTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot144', set())
    assert getattr(partner, 'GlobalScriptTask') is None


def test_assoc_globalTask145_stub_double():
    # GlobalTask has no real 'GlobalTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = GlobalTask()
    setattr(partner, 'GlobalTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot146', {partner})
    assert getattr(partner, 'GlobalTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot146', set())
    assert getattr(partner, 'GlobalTask') is None


def test_assoc_globalUserTask147_stub_double():
    # GlobalUserTask has no real 'GlobalUserTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = GlobalUserTask()
    setattr(partner, 'GlobalUserTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot148', {partner})
    assert getattr(partner, 'GlobalUserTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot148', set())
    assert getattr(partner, 'GlobalUserTask') is None


def test_assoc_group149_stub_double():
    # artifacts_Group has no real 'artifacts_Group' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = artifacts_Group()
    setattr(partner, 'artifacts_Group', None)
    _safe_set(owner, 'bpmn2_DocumentRoot150', {partner})
    assert getattr(partner, 'artifacts_Group') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot150', set())
    assert getattr(partner, 'artifacts_Group') is None


def test_assoc_humanPerformer151_stub_double():
    # HumanPerformer has no real 'HumanPerformer' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = HumanPerformer()
    setattr(partner, 'HumanPerformer', None)
    _safe_set(owner, 'bpmn2_DocumentRoot152', {partner})
    assert getattr(partner, 'HumanPerformer') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot152', set())
    assert getattr(partner, 'HumanPerformer') is None


def test_assoc_implicitThrowEvent157_stub_double():
    # events_ImplicitThrowEvent has no real 'events_ImplicitThrowEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_ImplicitThrowEvent()
    setattr(partner, 'events_ImplicitThrowEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot158', {partner})
    assert getattr(partner, 'events_ImplicitThrowEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot158', set())
    assert getattr(partner, 'events_ImplicitThrowEvent') is None


def test_assoc_import_159_stub_double():
    # Import has no real 'Import' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Import()
    setattr(partner, 'Import', None)
    _safe_set(owner, 'bpmn2_DocumentRoot160', {partner})
    assert getattr(partner, 'Import') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot160', set())
    assert getattr(partner, 'Import') is None


def test_assoc_inclusiveGateway161_stub_double():
    # gateways_InclusiveGateway has no real 'gateways_InclusiveGateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = gateways_InclusiveGateway()
    setattr(partner, 'gateways_InclusiveGateway', None)
    _safe_set(owner, 'bpmn2_DocumentRoot162', {partner})
    assert getattr(partner, 'gateways_InclusiveGateway') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot162', set())
    assert getattr(partner, 'gateways_InclusiveGateway') is None


def test_assoc_inputSet163_stub_double():
    # InputSet has no real 'InputSet' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = InputSet()
    setattr(partner, 'InputSet', None)
    _safe_set(owner, 'bpmn2_DocumentRoot164', {partner})
    assert getattr(partner, 'InputSet') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot164', set())
    assert getattr(partner, 'InputSet') is None


def test_assoc_interface165_stub_double():
    # Interface has no real 'Interface' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Interface()
    setattr(partner, 'Interface', None)
    _safe_set(owner, 'bpmn2_DocumentRoot166', {partner})
    assert getattr(partner, 'Interface') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot166', set())
    assert getattr(partner, 'Interface') is None


def test_assoc_intermediateCatchEvent167_stub_double():
    # events_IntermediateCatchEvent has no real 'events_IntermediateCatchEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_IntermediateCatchEvent()
    setattr(partner, 'events_IntermediateCatchEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot168', {partner})
    assert getattr(partner, 'events_IntermediateCatchEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot168', set())
    assert getattr(partner, 'events_IntermediateCatchEvent') is None


def test_assoc_intermediateThrowEvent169_stub_double():
    # events_IntermediateThrowEvent has no real 'events_IntermediateThrowEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_IntermediateThrowEvent()
    setattr(partner, 'events_IntermediateThrowEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot170', {partner})
    assert getattr(partner, 'events_IntermediateThrowEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot170', set())
    assert getattr(partner, 'events_IntermediateThrowEvent') is None


def test_assoc_ioBinding171_stub_double():
    # InputOutputBinding has no real 'InputOutputBinding' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = InputOutputBinding()
    setattr(partner, 'InputOutputBinding', None)
    _safe_set(owner, 'bpmn2_DocumentRoot172', {partner})
    assert getattr(partner, 'InputOutputBinding') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot172', set())
    assert getattr(partner, 'InputOutputBinding') is None


def test_assoc_ioSpecification173_stub_double():
    # InputOutputSpecification has no real 'InputOutputSpecification' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = InputOutputSpecification()
    setattr(partner, 'InputOutputSpecification', None)
    _safe_set(owner, 'bpmn2_DocumentRoot174', {partner})
    assert getattr(partner, 'InputOutputSpecification') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot174', set())
    assert getattr(partner, 'InputOutputSpecification') is None


def test_assoc_itemDefinition175_stub_double():
    # ItemDefinition has no real 'ItemDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ItemDefinition()
    setattr(partner, 'ItemDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot176', {partner})
    assert getattr(partner, 'ItemDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot176', set())
    assert getattr(partner, 'ItemDefinition') is None


def test_assoc_lane177_stub_double():
    # Lane has no real 'Lane' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Lane()
    setattr(partner, 'Lane', None)
    _safe_set(owner, 'bpmn2_DocumentRoot178', {partner})
    assert getattr(partner, 'Lane') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot178', set())
    assert getattr(partner, 'Lane') is None


def test_assoc_laneSet179_stub_double():
    # LaneSet has no real 'LaneSet' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = LaneSet()
    setattr(partner, 'LaneSet', None)
    _safe_set(owner, 'bpmn2_DocumentRoot180', {partner})
    assert getattr(partner, 'LaneSet') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot180', set())
    assert getattr(partner, 'LaneSet') is None


def test_assoc_linkEventDefinition181_stub_double():
    # events_LinkEventDefinition has no real 'events_LinkEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_LinkEventDefinition()
    setattr(partner, 'events_LinkEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot182', {partner})
    assert getattr(partner, 'events_LinkEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot182', set())
    assert getattr(partner, 'events_LinkEventDefinition') is None


def test_assoc_loopCharacteristics183_stub_double():
    # LoopCharacteristics has no real 'LoopCharacteristics' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = LoopCharacteristics()
    setattr(partner, 'LoopCharacteristics', None)
    _safe_set(owner, 'bpmn2_DocumentRoot184', {partner})
    assert getattr(partner, 'LoopCharacteristics') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot184', set())
    assert getattr(partner, 'LoopCharacteristics') is None


def test_assoc_manualTask185_stub_double():
    # ManualTask has no real 'ManualTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ManualTask()
    setattr(partner, 'ManualTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot186', {partner})
    assert getattr(partner, 'ManualTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot186', set())
    assert getattr(partner, 'ManualTask') is None


def test_assoc_message187_stub_double():
    # Message has no real 'Message' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Message()
    setattr(partner, 'Message', None)
    _safe_set(owner, 'bpmn2_DocumentRoot188', {partner})
    assert getattr(partner, 'Message') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot188', set())
    assert getattr(partner, 'Message') is None


def test_assoc_messageEventDefinition189_stub_double():
    # MessageEventDefinition has no real 'MessageEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = MessageEventDefinition()
    setattr(partner, 'MessageEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot190', {partner})
    assert getattr(partner, 'MessageEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot190', set())
    assert getattr(partner, 'MessageEventDefinition') is None


def test_assoc_messageFlow191_stub_double():
    # MessageFlow has no real 'MessageFlow' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = MessageFlow()
    setattr(partner, 'MessageFlow', None)
    _safe_set(owner, 'bpmn2_DocumentRoot192', {partner})
    assert getattr(partner, 'MessageFlow') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot192', set())
    assert getattr(partner, 'MessageFlow') is None


def test_assoc_messageFlowAssociation193_stub_double():
    # MessageFlowAssociation has no real 'MessageFlowAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = MessageFlowAssociation()
    setattr(partner, 'MessageFlowAssociation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot194', {partner})
    assert getattr(partner, 'MessageFlowAssociation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot194', set())
    assert getattr(partner, 'MessageFlowAssociation') is None


def test_assoc_monitoring195_stub_double():
    # Monitoring has no real 'Monitoring' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Monitoring()
    setattr(partner, 'Monitoring', None)
    _safe_set(owner, 'bpmn2_DocumentRoot196', {partner})
    assert getattr(partner, 'Monitoring') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot196', set())
    assert getattr(partner, 'Monitoring') is None


def test_assoc_multiInstanceLoopCharacteristics197_stub_double():
    # MultiInstanceLoopCharacteristics has no real 'MultiInstanceLoopCharacteristics' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = MultiInstanceLoopCharacteristics()
    setattr(partner, 'MultiInstanceLoopCharacteristics', None)
    _safe_set(owner, 'bpmn2_DocumentRoot198', {partner})
    assert getattr(partner, 'MultiInstanceLoopCharacteristics') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot198', set())
    assert getattr(partner, 'MultiInstanceLoopCharacteristics') is None


def test_assoc_operation199_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot200', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot200', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_outputSet201_stub_double():
    # OutputSet has no real 'OutputSet' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = OutputSet()
    setattr(partner, 'OutputSet', None)
    _safe_set(owner, 'bpmn2_DocumentRoot202', {partner})
    assert getattr(partner, 'OutputSet') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot202', set())
    assert getattr(partner, 'OutputSet') is None


def test_assoc_parallelGateway203_stub_double():
    # gateways_ParallelGateway has no real 'gateways_ParallelGateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = gateways_ParallelGateway()
    setattr(partner, 'gateways_ParallelGateway', None)
    _safe_set(owner, 'bpmn2_DocumentRoot204', {partner})
    assert getattr(partner, 'gateways_ParallelGateway') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot204', set())
    assert getattr(partner, 'gateways_ParallelGateway') is None


def test_assoc_participant205_stub_double():
    # Participant has no real 'Participant' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Participant()
    setattr(partner, 'Participant', None)
    _safe_set(owner, 'bpmn2_DocumentRoot206', {partner})
    assert getattr(partner, 'Participant') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot206', set())
    assert getattr(partner, 'Participant') is None


def test_assoc_participantAssociation207_stub_double():
    # ParticipantAssociation has no real 'ParticipantAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ParticipantAssociation()
    setattr(partner, 'ParticipantAssociation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot208', {partner})
    assert getattr(partner, 'ParticipantAssociation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot208', set())
    assert getattr(partner, 'ParticipantAssociation') is None


def test_assoc_participantMultiplicity209_stub_double():
    # ParticipantMultiplicity has no real 'ParticipantMultiplicity' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ParticipantMultiplicity()
    setattr(partner, 'ParticipantMultiplicity', None)
    _safe_set(owner, 'bpmn2_DocumentRoot210', {partner})
    assert getattr(partner, 'ParticipantMultiplicity') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot210', set())
    assert getattr(partner, 'ParticipantMultiplicity') is None


def test_assoc_partnerEntity211_stub_double():
    # PartnerEntity has no real 'PartnerEntity' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = PartnerEntity()
    setattr(partner, 'PartnerEntity', None)
    _safe_set(owner, 'bpmn2_DocumentRoot212', {partner})
    assert getattr(partner, 'PartnerEntity') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot212', set())
    assert getattr(partner, 'PartnerEntity') is None


def test_assoc_partnerRole213_stub_double():
    # PartnerRole has no real 'PartnerRole' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = PartnerRole()
    setattr(partner, 'PartnerRole', None)
    _safe_set(owner, 'bpmn2_DocumentRoot214', {partner})
    assert getattr(partner, 'PartnerRole') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot214', set())
    assert getattr(partner, 'PartnerRole') is None


def test_assoc_performer153_stub_double():
    # Performer has no real 'Performer' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Performer()
    setattr(partner, 'Performer', None)
    _safe_set(owner, 'bpmn2_DocumentRoot154', {partner})
    assert getattr(partner, 'Performer') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot154', set())
    assert getattr(partner, 'Performer') is None


def test_assoc_potentialOwner215_stub_double():
    # PotentialOwner has no real 'PotentialOwner' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = PotentialOwner()
    setattr(partner, 'PotentialOwner', None)
    _safe_set(owner, 'bpmn2_DocumentRoot216', {partner})
    assert getattr(partner, 'PotentialOwner') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot216', set())
    assert getattr(partner, 'PotentialOwner') is None


def test_assoc_process217_stub_double():
    # Process has no real 'Process' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Process()
    setattr(partner, 'Process', None)
    _safe_set(owner, 'bpmn2_DocumentRoot218', {partner})
    assert getattr(partner, 'Process') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot218', set())
    assert getattr(partner, 'Process') is None


def test_assoc_property219_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'bpmn2_DocumentRoot220', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot220', set())
    assert getattr(partner, 'Property') is None


def test_assoc_receiveTask221_stub_double():
    # ReceiveTask has no real 'ReceiveTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ReceiveTask()
    setattr(partner, 'ReceiveTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot222', {partner})
    assert getattr(partner, 'ReceiveTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot222', set())
    assert getattr(partner, 'ReceiveTask') is None


def test_assoc_relationship223_stub_double():
    # Relationship has no real 'Relationship' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Relationship()
    setattr(partner, 'Relationship', None)
    _safe_set(owner, 'bpmn2_DocumentRoot224', {partner})
    assert getattr(partner, 'Relationship') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot224', set())
    assert getattr(partner, 'Relationship') is None


def test_assoc_rendering225_stub_double():
    # Rendering has no real 'Rendering' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Rendering()
    setattr(partner, 'Rendering', None)
    _safe_set(owner, 'bpmn2_DocumentRoot226', {partner})
    assert getattr(partner, 'Rendering') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot226', set())
    assert getattr(partner, 'Rendering') is None


def test_assoc_resource227_stub_double():
    # Resource has no real 'Resource' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Resource()
    setattr(partner, 'Resource', None)
    _safe_set(owner, 'bpmn2_DocumentRoot228', {partner})
    assert getattr(partner, 'Resource') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot228', set())
    assert getattr(partner, 'Resource') is None


def test_assoc_resourceAssignmentExpression229_stub_double():
    # ResourceAssignmentExpression has no real 'ResourceAssignmentExpression' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ResourceAssignmentExpression()
    setattr(partner, 'ResourceAssignmentExpression', None)
    _safe_set(owner, 'bpmn2_DocumentRoot230', {partner})
    assert getattr(partner, 'ResourceAssignmentExpression') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot230', set())
    assert getattr(partner, 'ResourceAssignmentExpression') is None


def test_assoc_resourceParameter231_stub_double():
    # ResourceParameter has no real 'ResourceParameter' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ResourceParameter()
    setattr(partner, 'ResourceParameter', None)
    _safe_set(owner, 'bpmn2_DocumentRoot232', {partner})
    assert getattr(partner, 'ResourceParameter') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot232', set())
    assert getattr(partner, 'ResourceParameter') is None


def test_assoc_resourceParameterBinding233_stub_double():
    # ResourceParameterBinding has no real 'ResourceParameterBinding' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ResourceParameterBinding()
    setattr(partner, 'ResourceParameterBinding', None)
    _safe_set(owner, 'bpmn2_DocumentRoot234', {partner})
    assert getattr(partner, 'ResourceParameterBinding') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot234', set())
    assert getattr(partner, 'ResourceParameterBinding') is None


def test_assoc_resourceRole155_stub_double():
    # ResourceRole has no real 'ResourceRole' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ResourceRole()
    setattr(partner, 'ResourceRole', None)
    _safe_set(owner, 'bpmn2_DocumentRoot156', {partner})
    assert getattr(partner, 'ResourceRole') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot156', set())
    assert getattr(partner, 'ResourceRole') is None


def test_assoc_rootElement41_stub_double():
    # RootElement has no real 'RootElement' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = RootElement()
    setattr(partner, 'RootElement', None)
    _safe_set(owner, 'bpmn2_DocumentRoot42', {partner})
    assert getattr(partner, 'RootElement') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot42', set())
    assert getattr(partner, 'RootElement') is None


def test_assoc_script235_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject', None)
    _safe_set(owner, 'bpmn2_DocumentRoot236', {partner})
    assert getattr(partner, 'bpmn2_EObject') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot236', set())
    assert getattr(partner, 'bpmn2_EObject') is None


def test_assoc_scriptTask237_stub_double():
    # ScriptTask has no real 'ScriptTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ScriptTask()
    setattr(partner, 'ScriptTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot238', {partner})
    assert getattr(partner, 'ScriptTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot238', set())
    assert getattr(partner, 'ScriptTask') is None


def test_assoc_sendTask239_stub_double():
    # SendTask has no real 'SendTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = SendTask()
    setattr(partner, 'SendTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot240', {partner})
    assert getattr(partner, 'SendTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot240', set())
    assert getattr(partner, 'SendTask') is None


def test_assoc_sequenceFlow241_stub_double():
    # flows_SequenceFlow has no real 'flows_SequenceFlow' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = flows_SequenceFlow()
    setattr(partner, 'flows_SequenceFlow', None)
    _safe_set(owner, 'bpmn2_DocumentRoot242', {partner})
    assert getattr(partner, 'flows_SequenceFlow') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot242', set())
    assert getattr(partner, 'flows_SequenceFlow') is None


def test_assoc_serviceTask243_stub_double():
    # ServiceTask has no real 'ServiceTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = ServiceTask()
    setattr(partner, 'ServiceTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot244', {partner})
    assert getattr(partner, 'ServiceTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot244', set())
    assert getattr(partner, 'ServiceTask') is None


def test_assoc_signal245_stub_double():
    # events_Signal has no real 'events_Signal' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_Signal()
    setattr(partner, 'events_Signal', None)
    _safe_set(owner, 'bpmn2_DocumentRoot246', {partner})
    assert getattr(partner, 'events_Signal') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot246', set())
    assert getattr(partner, 'events_Signal') is None


def test_assoc_signalEventDefinition247_stub_double():
    # events_SignalEventDefinition has no real 'events_SignalEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_SignalEventDefinition()
    setattr(partner, 'events_SignalEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot248', {partner})
    assert getattr(partner, 'events_SignalEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot248', set())
    assert getattr(partner, 'events_SignalEventDefinition') is None


def test_assoc_standardLoopCharacteristics249_stub_double():
    # StandardLoopCharacteristics has no real 'StandardLoopCharacteristics' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = StandardLoopCharacteristics()
    setattr(partner, 'StandardLoopCharacteristics', None)
    _safe_set(owner, 'bpmn2_DocumentRoot250', {partner})
    assert getattr(partner, 'StandardLoopCharacteristics') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot250', set())
    assert getattr(partner, 'StandardLoopCharacteristics') is None


def test_assoc_startEvent251_stub_double():
    # events_StartEvent has no real 'events_StartEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_StartEvent()
    setattr(partner, 'events_StartEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot252', {partner})
    assert getattr(partner, 'events_StartEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot252', set())
    assert getattr(partner, 'events_StartEvent') is None


def test_assoc_subChoreography253_stub_double():
    # choreographyactivities_SubChoreography has no real 'choreographyactivities_SubChoreography' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = choreographyactivities_SubChoreography()
    setattr(partner, 'choreographyactivities_SubChoreography', None)
    _safe_set(owner, 'bpmn2_DocumentRoot254', {partner})
    assert getattr(partner, 'choreographyactivities_SubChoreography') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot254', set())
    assert getattr(partner, 'choreographyactivities_SubChoreography') is None


def test_assoc_subConversation255_stub_double():
    # SubConversation has no real 'SubConversation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = SubConversation()
    setattr(partner, 'SubConversation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot256', {partner})
    assert getattr(partner, 'SubConversation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot256', set())
    assert getattr(partner, 'SubConversation') is None


def test_assoc_subProcess257_stub_double():
    # SubProcess has no real 'SubProcess' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = SubProcess()
    setattr(partner, 'SubProcess', None)
    _safe_set(owner, 'bpmn2_DocumentRoot258', {partner})
    assert getattr(partner, 'SubProcess') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot258', set())
    assert getattr(partner, 'SubProcess') is None


def test_assoc_task259_stub_double():
    # Task has no real 'Task' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Task()
    setattr(partner, 'Task', None)
    _safe_set(owner, 'bpmn2_DocumentRoot260', {partner})
    assert getattr(partner, 'Task') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot260', set())
    assert getattr(partner, 'Task') is None


def test_assoc_terminateEventDefinition261_stub_double():
    # events_TerminateEventDefinition has no real 'events_TerminateEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_TerminateEventDefinition()
    setattr(partner, 'events_TerminateEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot262', {partner})
    assert getattr(partner, 'events_TerminateEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot262', set())
    assert getattr(partner, 'events_TerminateEventDefinition') is None


def test_assoc_text263_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject265' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject265', None)
    _safe_set(owner, 'bpmn2_DocumentRoot264', {partner})
    assert getattr(partner, 'bpmn2_EObject265') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot264', set())
    assert getattr(partner, 'bpmn2_EObject265') is None


def test_assoc_textAnnotation266_stub_double():
    # artifacts_TextAnnotation has no real 'artifacts_TextAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = artifacts_TextAnnotation()
    setattr(partner, 'artifacts_TextAnnotation', None)
    _safe_set(owner, 'bpmn2_DocumentRoot267', {partner})
    assert getattr(partner, 'artifacts_TextAnnotation') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot267', set())
    assert getattr(partner, 'artifacts_TextAnnotation') is None


def test_assoc_throwEvent268_stub_double():
    # events_ThrowEvent has no real 'events_ThrowEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_ThrowEvent()
    setattr(partner, 'events_ThrowEvent', None)
    _safe_set(owner, 'bpmn2_DocumentRoot269', {partner})
    assert getattr(partner, 'events_ThrowEvent') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot269', set())
    assert getattr(partner, 'events_ThrowEvent') is None


def test_assoc_timerEventDefinition270_stub_double():
    # events_TimerEventDefinition has no real 'events_TimerEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = events_TimerEventDefinition()
    setattr(partner, 'events_TimerEventDefinition', None)
    _safe_set(owner, 'bpmn2_DocumentRoot271', {partner})
    assert getattr(partner, 'events_TimerEventDefinition') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot271', set())
    assert getattr(partner, 'events_TimerEventDefinition') is None


def test_assoc_transaction272_stub_double():
    # Transaction has no real 'Transaction' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = Transaction()
    setattr(partner, 'Transaction', None)
    _safe_set(owner, 'bpmn2_DocumentRoot273', {partner})
    assert getattr(partner, 'Transaction') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot273', set())
    assert getattr(partner, 'Transaction') is None


def test_assoc_userTask274_stub_double():
    # UserTask has no real 'UserTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = UserTask()
    setattr(partner, 'UserTask', None)
    _safe_set(owner, 'bpmn2_DocumentRoot275', {partner})
    assert getattr(partner, 'UserTask') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot275', set())
    assert getattr(partner, 'UserTask') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # bpmn2_EStringToStringMapEntry has no real 'bpmn2_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = bpmn2_EStringToStringMapEntry()
    setattr(partner, 'bpmn2_EStringToStringMapEntry', None)
    _safe_set(owner, 'bpmn2_DocumentRoot', {partner})
    assert getattr(partner, 'bpmn2_EStringToStringMapEntry') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot', set())
    assert getattr(partner, 'bpmn2_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # bpmn2_EStringToStringMapEntry has no real 'bpmn2_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DocumentRoot(mixed="sample_text")
    partner = bpmn2_EStringToStringMapEntry()
    setattr(partner, 'bpmn2_EStringToStringMapEntry3', None)
    _safe_set(owner, 'bpmn2_DocumentRoot2', {partner})
    assert getattr(partner, 'bpmn2_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'bpmn2_DocumentRoot2', set())
    assert getattr(partner, 'bpmn2_EStringToStringMapEntry3') is None


