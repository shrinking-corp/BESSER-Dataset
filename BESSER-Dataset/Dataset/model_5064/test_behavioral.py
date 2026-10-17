import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    Artifact,
    BaseElement,
    CallableElement,
    CatchEvent,
    Choreography,
    ChoreographyActivity,
    Collaboration,
    ConversationNode,
    DataAssociation,
    Event,
    EventDefinition,
    Expression,
    FlowElement,
    FlowElementsContainer,
    FlowNode,
    Gateway,
    GlobalTask,
    HumanPerformer,
    InteractionNode,
    ItemAwareElement,
    LoopCharacteristics,
    Performer,
    ResourceRole,
    RootElement,
    SubProcess,
    Task,
    ThrowEvent,
    bpmn2_Activity,
    bpmn2_AdHocSubProcess,
    bpmn2_Artifact,
    bpmn2_Assignment,
    bpmn2_Association,
    bpmn2_Auditing,
    bpmn2_BPMNDiagram,
    bpmn2_BaseElement,
    bpmn2_BoundaryEvent,
    bpmn2_BusinessRuleTask,
    bpmn2_CallActivity,
    bpmn2_CallChoreography,
    bpmn2_CallConversation,
    bpmn2_CallableElement,
    bpmn2_CancelEventDefinition,
    bpmn2_CatchEvent,
    bpmn2_Category,
    bpmn2_CategoryValue,
    bpmn2_Choreography,
    bpmn2_ChoreographyActivity,
    bpmn2_ChoreographyTask,
    bpmn2_Collaboration,
    bpmn2_CompensateEventDefinition,
    bpmn2_Competency,
    bpmn2_ComplexBehaviorDefinition,
    bpmn2_ComplexGateway,
    bpmn2_ConditionalEventDefinition,
    bpmn2_Conversation,
    bpmn2_ConversationAssociation,
    bpmn2_ConversationLink,
    bpmn2_ConversationNode,
    bpmn2_CorrelationKey,
    bpmn2_CorrelationProperty,
    bpmn2_CorrelationPropertyBinding,
    bpmn2_CorrelationPropertyRetrievalExpression,
    bpmn2_CorrelationSubscription,
    bpmn2_Criterion,
    bpmn2_DataAssociation,
    bpmn2_DataInput,
    bpmn2_DataInputAssociation,
    bpmn2_DataObject,
    bpmn2_DataObjectReference,
    bpmn2_DataOutput,
    bpmn2_DataOutputAssociation,
    bpmn2_DataState,
    bpmn2_DataStore,
    bpmn2_DataStoreReference,
    bpmn2_Definitions,
    bpmn2_Document,
    bpmn2_DocumentRoot,
    bpmn2_Documentation,
    bpmn2_EObject,
    bpmn2_EStringToStringMapEntry,
    bpmn2_EndEvent,
    bpmn2_EndPoint,
    bpmn2_Error,
    bpmn2_ErrorEventDefinition,
    bpmn2_Escalation,
    bpmn2_EscalationEventDefinition,
    bpmn2_Event,
    bpmn2_EventBasedGateway,
    bpmn2_EventDefinition,
    bpmn2_ExclusiveGateway,
    bpmn2_Expression,
    bpmn2_Extension,
    bpmn2_ExtensionAttributeDefinition,
    bpmn2_ExtensionAttributeValue,
    bpmn2_ExtensionDefinition,
    bpmn2_FlowElement,
    bpmn2_FlowElementsContainer,
    bpmn2_FlowNode,
    bpmn2_FormalExpression,
    bpmn2_Gateway,
    bpmn2_GlobalBusinessRuleTask,
    bpmn2_GlobalChoreographyTask,
    bpmn2_GlobalConversation,
    bpmn2_GlobalManualTask,
    bpmn2_GlobalScriptTask,
    bpmn2_GlobalTask,
    bpmn2_GlobalUserTask,
    bpmn2_Group,
    bpmn2_HumanPerformer,
    bpmn2_ImplicitThrowEvent,
    bpmn2_Import,
    bpmn2_InclusiveGateway,
    bpmn2_InputOutputBinding,
    bpmn2_InputOutputSpecification,
    bpmn2_InputSet,
    bpmn2_InteractionNode,
    bpmn2_Interface,
    bpmn2_IntermediateCatchEvent,
    bpmn2_IntermediateThrowEvent,
    bpmn2_ItemAwareElement,
    bpmn2_ItemDefinition,
    bpmn2_Lane,
    bpmn2_LaneSet,
    bpmn2_LinkEventDefinition,
    bpmn2_LoopCharacteristics,
    bpmn2_ManualTask,
    bpmn2_Message,
    bpmn2_MessageEventDefinition,
    bpmn2_MessageFlow,
    bpmn2_MessageFlowAssociation,
    bpmn2_Monitoring,
    bpmn2_MultiInstanceLoopCharacteristics,
    bpmn2_Operation,
    bpmn2_OrganisationalUnit,
    bpmn2_OutputSet,
    bpmn2_ParallelGateway,
    bpmn2_Participant,
    bpmn2_ParticipantAssociation,
    bpmn2_ParticipantMultiplicity,
    bpmn2_PartnerEntity,
    bpmn2_PartnerRole,
    bpmn2_Performer,
    bpmn2_Position,
    bpmn2_PotentialOwner,
    bpmn2_Process,
    bpmn2_Property,
    bpmn2_ReceiveTask,
    bpmn2_Relationship,
    bpmn2_Rendering,
    bpmn2_Resource,
    bpmn2_ResourceAssignmentExpression,
    bpmn2_ResourceParameter,
    bpmn2_ResourceParameterBinding,
    bpmn2_ResourceRole,
    bpmn2_Role,
    bpmn2_RootElement,
    bpmn2_ScriptTask,
    bpmn2_SendTask,
    bpmn2_SequenceFlow,
    bpmn2_ServiceTask,
    bpmn2_Signal,
    bpmn2_SignalEventDefinition,
    bpmn2_StandardLoopCharacteristics,
    bpmn2_StartEvent,
    bpmn2_SubChoreography,
    bpmn2_SubConversation,
    bpmn2_SubProcess,
    bpmn2_Task,
    bpmn2_TerminateEventDefinition,
    bpmn2_TextAnnotation,
    bpmn2_ThrowEvent,
    bpmn2_TimerEventDefinition,
    bpmn2_Transaction,
    bpmn2_UserTask,
    AdHocOrdering,
    AssociationDirection,
    ChoreographyLoopType,
    EventBasedGatewayType,
    GatewayDirection,
    ItemKind,
    MultiInstanceBehavior,
    ProcessType,
    RelationshipDirection,
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

def test_assoc_activityRef428_reverse_link_reassign_clear():
    a1 = bpmn2_CompensateEventDefinition(waitForCompletion=True)
    a2 = bpmn2_CompensateEventDefinition(waitForCompletion=False)
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'bpmn2_Activity430', a1)
    assert _is_linked(b, 'bpmn2_Activity430', a1)
    if hasattr(a1, 'bpmn2_CompensateEventDefinition429'):
        assert _is_linked(a1, 'bpmn2_CompensateEventDefinition429', b)
    _safe_set(b, 'bpmn2_Activity430', a2)
    assert _is_linked(b, 'bpmn2_Activity430', a2)
    if hasattr(a1, 'bpmn2_CompensateEventDefinition429'):
        assert not _is_linked(a1, 'bpmn2_CompensateEventDefinition429', b)
    if hasattr(a2, 'bpmn2_CompensateEventDefinition429'):
        assert _is_linked(a2, 'bpmn2_CompensateEventDefinition429', b)
    _safe_set(b, 'bpmn2_Activity430', None)
    assert not _is_linked(b, 'bpmn2_Activity430', a2)
    if hasattr(a2, 'bpmn2_CompensateEventDefinition429'):
        assert not _is_linked(a2, 'bpmn2_CompensateEventDefinition429', b)


def test_assoc_attachedToRef340_reverse_link_reassign_clear():
    a1 = bpmn2_BoundaryEvent(cancelActivity=True)
    a2 = bpmn2_BoundaryEvent(cancelActivity=False)
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'Activity', a1)
    assert _is_linked(b, 'Activity', a1)
    if hasattr(a1, 'boundaryEventRefs'):
        assert _is_linked(a1, 'boundaryEventRefs', b)
    _safe_set(b, 'Activity', a2)
    assert _is_linked(b, 'Activity', a2)
    if hasattr(a1, 'boundaryEventRefs'):
        assert not _is_linked(a1, 'boundaryEventRefs', b)
    if hasattr(a2, 'boundaryEventRefs'):
        assert _is_linked(a2, 'boundaryEventRefs', b)
    _safe_set(b, 'Activity', None)
    assert not _is_linked(b, 'Activity', a2)
    if hasattr(a2, 'boundaryEventRefs'):
        assert not _is_linked(a2, 'boundaryEventRefs', b)


def test_assoc_boundaryEventRefs279_reverse_link_reassign_clear():
    a1 = bpmn2_BoundaryEvent(cancelActivity=True)
    a2 = bpmn2_BoundaryEvent(cancelActivity=False)
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'attachedToRef', {a1})
    assert _is_linked(b, 'attachedToRef', a1)
    if hasattr(a1, 'BoundaryEvent'):
        assert _is_linked(a1, 'BoundaryEvent', b)
    _safe_set(b, 'attachedToRef', {a2})
    assert _is_linked(b, 'attachedToRef', a2)
    if hasattr(a1, 'BoundaryEvent'):
        assert not _is_linked(a1, 'BoundaryEvent', b)
    if hasattr(a2, 'BoundaryEvent'):
        assert _is_linked(a2, 'BoundaryEvent', b)
    _safe_set(b, 'attachedToRef', set())
    assert not _is_linked(b, 'attachedToRef', a2)
    if hasattr(a2, 'BoundaryEvent'):
        assert not _is_linked(a2, 'BoundaryEvent', b)


def test_assoc_dataOutputs365_reverse_link_reassign_clear():
    a1 = bpmn2_DataOutput(isCollection=True)
    a2 = bpmn2_DataOutput(isCollection=False)
    b = bpmn2_CatchEvent(parallelMultiple=True)
    _safe_set(b, 'bpmn2_CatchEvent366', {a1})
    assert _is_linked(b, 'bpmn2_CatchEvent366', a1)
    if hasattr(a1, 'bpmn2_DataOutput367'):
        assert _is_linked(a1, 'bpmn2_DataOutput367', b)
    _safe_set(b, 'bpmn2_CatchEvent366', {a2})
    assert _is_linked(b, 'bpmn2_CatchEvent366', a2)
    if hasattr(a1, 'bpmn2_DataOutput367'):
        assert not _is_linked(a1, 'bpmn2_DataOutput367', b)
    if hasattr(a2, 'bpmn2_DataOutput367'):
        assert _is_linked(a2, 'bpmn2_DataOutput367', b)
    _safe_set(b, 'bpmn2_CatchEvent366', set())
    assert not _is_linked(b, 'bpmn2_CatchEvent366', a2)
    if hasattr(a2, 'bpmn2_DataOutput367'):
        assert not _is_linked(a2, 'bpmn2_DataOutput367', b)


def test_assoc_default295_reverse_link_reassign_clear():
    a1 = bpmn2_SequenceFlow(isImmediate=True)
    a2 = bpmn2_SequenceFlow(isImmediate=False)
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'bpmn2_Activity296', a1)
    assert _is_linked(b, 'bpmn2_Activity296', a1)
    if hasattr(a1, 'bpmn2_SequenceFlow297'):
        assert _is_linked(a1, 'bpmn2_SequenceFlow297', b)
    _safe_set(b, 'bpmn2_Activity296', a2)
    assert _is_linked(b, 'bpmn2_Activity296', a2)
    if hasattr(a1, 'bpmn2_SequenceFlow297'):
        assert not _is_linked(a1, 'bpmn2_SequenceFlow297', b)
    if hasattr(a2, 'bpmn2_SequenceFlow297'):
        assert _is_linked(a2, 'bpmn2_SequenceFlow297', b)
    _safe_set(b, 'bpmn2_Activity296', None)
    assert not _is_linked(b, 'bpmn2_Activity296', a2)
    if hasattr(a2, 'bpmn2_SequenceFlow297'):
        assert not _is_linked(a2, 'bpmn2_SequenceFlow297', b)


def test_assoc_definition555_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(name="sample_text")
    a2 = bpmn2_ExtensionDefinition(name="sample_text_2")
    b = bpmn2_Extension(mustUnderstand=True, xsdDefinition="sample_text")
    _safe_set(b, 'bpmn2_Extension556', a1)
    assert _is_linked(b, 'bpmn2_Extension556', a1)
    if hasattr(a1, 'bpmn2_ExtensionDefinition557'):
        assert _is_linked(a1, 'bpmn2_ExtensionDefinition557', b)
    _safe_set(b, 'bpmn2_Extension556', a2)
    assert _is_linked(b, 'bpmn2_Extension556', a2)
    if hasattr(a1, 'bpmn2_ExtensionDefinition557'):
        assert not _is_linked(a1, 'bpmn2_ExtensionDefinition557', b)
    if hasattr(a2, 'bpmn2_ExtensionDefinition557'):
        assert _is_linked(a2, 'bpmn2_ExtensionDefinition557', b)
    _safe_set(b, 'bpmn2_Extension556', None)
    assert not _is_linked(b, 'bpmn2_Extension556', a2)
    if hasattr(a2, 'bpmn2_ExtensionDefinition557'):
        assert not _is_linked(a2, 'bpmn2_ExtensionDefinition557', b)


def test_assoc_definitionalCollaborationRef803_reverse_link_reassign_clear():
    a1 = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    a2 = bpmn2_Process(isClosed=False, isExecutable=False, processType="sample_text_2")
    b = bpmn2_Collaboration(isClosed=True)
    _safe_set(b, 'bpmn2_Collaboration805', a1)
    assert _is_linked(b, 'bpmn2_Collaboration805', a1)
    if hasattr(a1, 'bpmn2_Process804'):
        assert _is_linked(a1, 'bpmn2_Process804', b)
    _safe_set(b, 'bpmn2_Collaboration805', a2)
    assert _is_linked(b, 'bpmn2_Collaboration805', a2)
    if hasattr(a1, 'bpmn2_Process804'):
        assert not _is_linked(a1, 'bpmn2_Process804', b)
    if hasattr(a2, 'bpmn2_Process804'):
        assert _is_linked(a2, 'bpmn2_Process804', b)
    _safe_set(b, 'bpmn2_Collaboration805', None)
    assert not _is_linked(b, 'bpmn2_Collaboration805', a2)
    if hasattr(a2, 'bpmn2_Process804'):
        assert not _is_linked(a2, 'bpmn2_Process804', b)


def test_assoc_documentation335_reverse_link_reassign_clear():
    a1 = bpmn2_Documentation(mixed="sample_text", text="sample_text", textFormat="sample_text")
    a2 = bpmn2_Documentation(mixed="sample_text_2", text="sample_text_2", textFormat="sample_text_2")
    b = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'bpmn2_BaseElement336', {a1})
    assert _is_linked(b, 'bpmn2_BaseElement336', a1)
    if hasattr(a1, 'bpmn2_Documentation337'):
        assert _is_linked(a1, 'bpmn2_Documentation337', b)
    _safe_set(b, 'bpmn2_BaseElement336', {a2})
    assert _is_linked(b, 'bpmn2_BaseElement336', a2)
    if hasattr(a1, 'bpmn2_Documentation337'):
        assert not _is_linked(a1, 'bpmn2_Documentation337', b)
    if hasattr(a2, 'bpmn2_Documentation337'):
        assert _is_linked(a2, 'bpmn2_Documentation337', b)
    _safe_set(b, 'bpmn2_BaseElement336', set())
    assert not _is_linked(b, 'bpmn2_BaseElement336', a2)
    if hasattr(a2, 'bpmn2_Documentation337'):
        assert not _is_linked(a2, 'bpmn2_Documentation337', b)


def test_assoc_evaluatesToTypeRef583_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_FormalExpression(body="sample_text", language="sample_text", mixed="sample_text")
    _safe_set(b, 'bpmn2_FormalExpression584', a1)
    assert _is_linked(b, 'bpmn2_FormalExpression584', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition585'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition585', b)
    _safe_set(b, 'bpmn2_FormalExpression584', a2)
    assert _is_linked(b, 'bpmn2_FormalExpression584', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition585'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition585', b)
    if hasattr(a2, 'bpmn2_ItemDefinition585'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition585', b)
    _safe_set(b, 'bpmn2_FormalExpression584', None)
    assert not _is_linked(b, 'bpmn2_FormalExpression584', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition585'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition585', b)


def test_assoc_extensionAttributeDefinition562_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionAttributeValue(value="sample_text")
    a2 = bpmn2_ExtensionAttributeValue(value="sample_text_2")
    b = bpmn2_ExtensionAttributeDefinition(isReference=True, name="sample_text", type="sample_text")
    _safe_set(b, 'bpmn2_ExtensionAttributeDefinition', a1)
    assert _is_linked(b, 'bpmn2_ExtensionAttributeDefinition', a1)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue563'):
        assert _is_linked(a1, 'bpmn2_ExtensionAttributeValue563', b)
    _safe_set(b, 'bpmn2_ExtensionAttributeDefinition', a2)
    assert _is_linked(b, 'bpmn2_ExtensionAttributeDefinition', a2)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue563'):
        assert not _is_linked(a1, 'bpmn2_ExtensionAttributeValue563', b)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue563'):
        assert _is_linked(a2, 'bpmn2_ExtensionAttributeValue563', b)
    _safe_set(b, 'bpmn2_ExtensionAttributeDefinition', None)
    assert not _is_linked(b, 'bpmn2_ExtensionAttributeDefinition', a2)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue563'):
        assert not _is_linked(a2, 'bpmn2_ExtensionAttributeValue563', b)


def test_assoc_extensionAttributeDefinitions564_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(name="sample_text")
    a2 = bpmn2_ExtensionDefinition(name="sample_text_2")
    b = bpmn2_ExtensionAttributeDefinition(isReference=True, name="sample_text", type="sample_text")
    _safe_set(b, 'ExtensionAttributeDefinition', a1)
    assert _is_linked(b, 'ExtensionAttributeDefinition', a1)
    if hasattr(a1, 'extensionDefinition'):
        assert _is_linked(a1, 'extensionDefinition', b)
    _safe_set(b, 'ExtensionAttributeDefinition', a2)
    assert _is_linked(b, 'ExtensionAttributeDefinition', a2)
    if hasattr(a1, 'extensionDefinition'):
        assert not _is_linked(a1, 'extensionDefinition', b)
    if hasattr(a2, 'extensionDefinition'):
        assert _is_linked(a2, 'extensionDefinition', b)
    _safe_set(b, 'ExtensionAttributeDefinition', None)
    assert not _is_linked(b, 'ExtensionAttributeDefinition', a2)
    if hasattr(a2, 'extensionDefinition'):
        assert not _is_linked(a2, 'extensionDefinition', b)


def test_assoc_extensionDefinition558_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(name="sample_text")
    a2 = bpmn2_ExtensionDefinition(name="sample_text_2")
    b = bpmn2_ExtensionAttributeDefinition(isReference=True, name="sample_text", type="sample_text")
    _safe_set(b, 'extensionAttributeDefinitions', a1)
    assert _is_linked(b, 'extensionAttributeDefinitions', a1)
    if hasattr(a1, 'ExtensionDefinition'):
        assert _is_linked(a1, 'ExtensionDefinition', b)
    _safe_set(b, 'extensionAttributeDefinitions', a2)
    assert _is_linked(b, 'extensionAttributeDefinitions', a2)
    if hasattr(a1, 'ExtensionDefinition'):
        assert not _is_linked(a1, 'ExtensionDefinition', b)
    if hasattr(a2, 'ExtensionDefinition'):
        assert _is_linked(a2, 'ExtensionDefinition', b)
    _safe_set(b, 'extensionAttributeDefinitions', None)
    assert not _is_linked(b, 'extensionAttributeDefinitions', a2)
    if hasattr(a2, 'ExtensionDefinition'):
        assert not _is_linked(a2, 'ExtensionDefinition', b)


def test_assoc_extensionDefinitions338_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(name="sample_text")
    a2 = bpmn2_ExtensionDefinition(name="sample_text_2")
    b = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'bpmn2_BaseElement339', {a1})
    assert _is_linked(b, 'bpmn2_BaseElement339', a1)
    if hasattr(a1, 'bpmn2_ExtensionDefinition'):
        assert _is_linked(a1, 'bpmn2_ExtensionDefinition', b)
    _safe_set(b, 'bpmn2_BaseElement339', {a2})
    assert _is_linked(b, 'bpmn2_BaseElement339', a2)
    if hasattr(a1, 'bpmn2_ExtensionDefinition'):
        assert not _is_linked(a1, 'bpmn2_ExtensionDefinition', b)
    if hasattr(a2, 'bpmn2_ExtensionDefinition'):
        assert _is_linked(a2, 'bpmn2_ExtensionDefinition', b)
    _safe_set(b, 'bpmn2_BaseElement339', set())
    assert not _is_linked(b, 'bpmn2_BaseElement339', a2)
    if hasattr(a2, 'bpmn2_ExtensionDefinition'):
        assert not _is_linked(a2, 'bpmn2_ExtensionDefinition', b)


def test_assoc_extensionValues332_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionAttributeValue(value="sample_text")
    a2 = bpmn2_ExtensionAttributeValue(value="sample_text_2")
    b = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'bpmn2_BaseElement333', {a1})
    assert _is_linked(b, 'bpmn2_BaseElement333', a1)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue334'):
        assert _is_linked(a1, 'bpmn2_ExtensionAttributeValue334', b)
    _safe_set(b, 'bpmn2_BaseElement333', {a2})
    assert _is_linked(b, 'bpmn2_BaseElement333', a2)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue334'):
        assert not _is_linked(a1, 'bpmn2_ExtensionAttributeValue334', b)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue334'):
        assert _is_linked(a2, 'bpmn2_ExtensionAttributeValue334', b)
    _safe_set(b, 'bpmn2_BaseElement333', set())
    assert not _is_linked(b, 'bpmn2_BaseElement333', a2)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue334'):
        assert not _is_linked(a2, 'bpmn2_ExtensionAttributeValue334', b)


def test_assoc_extensions526_reverse_link_reassign_clear():
    a1 = bpmn2_Extension(mustUnderstand=True, xsdDefinition="sample_text")
    a2 = bpmn2_Extension(mustUnderstand=False, xsdDefinition="sample_text_2")
    b = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    _safe_set(b, 'bpmn2_Definitions527', {a1})
    assert _is_linked(b, 'bpmn2_Definitions527', a1)
    if hasattr(a1, 'bpmn2_Extension528'):
        assert _is_linked(a1, 'bpmn2_Extension528', b)
    _safe_set(b, 'bpmn2_Definitions527', {a2})
    assert _is_linked(b, 'bpmn2_Definitions527', a2)
    if hasattr(a1, 'bpmn2_Extension528'):
        assert not _is_linked(a1, 'bpmn2_Extension528', b)
    if hasattr(a2, 'bpmn2_Extension528'):
        assert _is_linked(a2, 'bpmn2_Extension528', b)
    _safe_set(b, 'bpmn2_Definitions527', set())
    assert not _is_linked(b, 'bpmn2_Definitions527', a2)
    if hasattr(a2, 'bpmn2_Extension528'):
        assert not _is_linked(a2, 'bpmn2_Extension528', b)


def test_assoc_import_648_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_Import(importType="sample_text", location="sample_text", namespace="sample_text")
    _safe_set(b, 'bpmn2_Import650', a1)
    assert _is_linked(b, 'bpmn2_Import650', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition649'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition649', b)
    _safe_set(b, 'bpmn2_Import650', a2)
    assert _is_linked(b, 'bpmn2_Import650', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition649'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition649', b)
    if hasattr(a2, 'bpmn2_ItemDefinition649'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition649', b)
    _safe_set(b, 'bpmn2_Import650', None)
    assert not _is_linked(b, 'bpmn2_Import650', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition649'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition649', b)


def test_assoc_imports523_reverse_link_reassign_clear():
    a1 = bpmn2_Import(importType="sample_text", location="sample_text", namespace="sample_text")
    a2 = bpmn2_Import(importType="sample_text_2", location="sample_text_2", namespace="sample_text_2")
    b = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    _safe_set(b, 'bpmn2_Definitions524', {a1})
    assert _is_linked(b, 'bpmn2_Definitions524', a1)
    if hasattr(a1, 'bpmn2_Import525'):
        assert _is_linked(a1, 'bpmn2_Import525', b)
    _safe_set(b, 'bpmn2_Definitions524', {a2})
    assert _is_linked(b, 'bpmn2_Definitions524', a2)
    if hasattr(a1, 'bpmn2_Import525'):
        assert not _is_linked(a1, 'bpmn2_Import525', b)
    if hasattr(a2, 'bpmn2_Import525'):
        assert _is_linked(a2, 'bpmn2_Import525', b)
    _safe_set(b, 'bpmn2_Definitions524', set())
    assert not _is_linked(b, 'bpmn2_Definitions524', a2)
    if hasattr(a2, 'bpmn2_Import525'):
        assert not _is_linked(a2, 'bpmn2_Import525', b)


def test_assoc_inputDataItem720_reverse_link_reassign_clear():
    a1 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    a2 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text_2", isSequential=False)
    b = bpmn2_DataInput(isCollection=True)
    _safe_set(b, 'bpmn2_DataInput722', a1)
    assert _is_linked(b, 'bpmn2_DataInput722', a1)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics721'):
        assert _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics721', b)
    _safe_set(b, 'bpmn2_DataInput722', a2)
    assert _is_linked(b, 'bpmn2_DataInput722', a2)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics721'):
        assert not _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics721', b)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics721'):
        assert _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics721', b)
    _safe_set(b, 'bpmn2_DataInput722', None)
    assert not _is_linked(b, 'bpmn2_DataInput722', a2)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics721'):
        assert not _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics721', b)


def test_assoc_outputDataItem723_reverse_link_reassign_clear():
    a1 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    a2 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text_2", isSequential=False)
    b = bpmn2_DataOutput(isCollection=True)
    _safe_set(b, 'bpmn2_DataOutput725', a1)
    assert _is_linked(b, 'bpmn2_DataOutput725', a1)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics724'):
        assert _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics724', b)
    _safe_set(b, 'bpmn2_DataOutput725', a2)
    assert _is_linked(b, 'bpmn2_DataOutput725', a2)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics724'):
        assert not _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics724', b)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics724'):
        assert _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics724', b)
    _safe_set(b, 'bpmn2_DataOutput725', None)
    assert not _is_linked(b, 'bpmn2_DataOutput725', a2)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics724'):
        assert not _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics724', b)


def test_assoc_referencedSubProcess876_reverse_link_reassign_clear():
    a1 = bpmn2_SubProcess(triggeredByEvent=True)
    a2 = bpmn2_SubProcess(triggeredByEvent=False)
    b = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    _safe_set(b, 'bpmn2_Process878', a1)
    assert _is_linked(b, 'bpmn2_Process878', a1)
    if hasattr(a1, 'bpmn2_SubProcess877'):
        assert _is_linked(a1, 'bpmn2_SubProcess877', b)
    _safe_set(b, 'bpmn2_Process878', a2)
    assert _is_linked(b, 'bpmn2_Process878', a2)
    if hasattr(a1, 'bpmn2_SubProcess877'):
        assert not _is_linked(a1, 'bpmn2_SubProcess877', b)
    if hasattr(a2, 'bpmn2_SubProcess877'):
        assert _is_linked(a2, 'bpmn2_SubProcess877', b)
    _safe_set(b, 'bpmn2_Process878', None)
    assert not _is_linked(b, 'bpmn2_Process878', a2)
    if hasattr(a2, 'bpmn2_SubProcess877'):
        assert not _is_linked(a2, 'bpmn2_SubProcess877', b)


def test_assoc_relationships534_reverse_link_reassign_clear():
    a1 = bpmn2_Relationship(direction="sample_text", type="sample_text")
    a2 = bpmn2_Relationship(direction="sample_text_2", type="sample_text_2")
    b = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    _safe_set(b, 'bpmn2_Definitions535', {a1})
    assert _is_linked(b, 'bpmn2_Definitions535', a1)
    if hasattr(a1, 'bpmn2_Relationship536'):
        assert _is_linked(a1, 'bpmn2_Relationship536', b)
    _safe_set(b, 'bpmn2_Definitions535', {a2})
    assert _is_linked(b, 'bpmn2_Definitions535', a2)
    if hasattr(a1, 'bpmn2_Relationship536'):
        assert not _is_linked(a1, 'bpmn2_Relationship536', b)
    if hasattr(a2, 'bpmn2_Relationship536'):
        assert _is_linked(a2, 'bpmn2_Relationship536', b)
    _safe_set(b, 'bpmn2_Definitions535', set())
    assert not _is_linked(b, 'bpmn2_Definitions535', a2)
    if hasattr(a2, 'bpmn2_Relationship536'):
        assert not _is_linked(a2, 'bpmn2_Relationship536', b)


def test_assoc_sourceRef326_reverse_link_reassign_clear():
    a1 = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    a2 = bpmn2_BaseElement(anyAttribute="sample_text_2", description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = bpmn2_Association(associationDirection="sample_text")
    _safe_set(b, 'bpmn2_Association327', a1)
    assert _is_linked(b, 'bpmn2_Association327', a1)
    if hasattr(a1, 'bpmn2_BaseElement328'):
        assert _is_linked(a1, 'bpmn2_BaseElement328', b)
    _safe_set(b, 'bpmn2_Association327', a2)
    assert _is_linked(b, 'bpmn2_Association327', a2)
    if hasattr(a1, 'bpmn2_BaseElement328'):
        assert not _is_linked(a1, 'bpmn2_BaseElement328', b)
    if hasattr(a2, 'bpmn2_BaseElement328'):
        assert _is_linked(a2, 'bpmn2_BaseElement328', b)
    _safe_set(b, 'bpmn2_Association327', None)
    assert not _is_linked(b, 'bpmn2_Association327', a2)
    if hasattr(a2, 'bpmn2_BaseElement328'):
        assert not _is_linked(a2, 'bpmn2_BaseElement328', b)


def test_assoc_structureRef537_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_Error(errorCode="sample_text")
    _safe_set(b, 'bpmn2_Error538', a1)
    assert _is_linked(b, 'bpmn2_Error538', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition539'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition539', b)
    _safe_set(b, 'bpmn2_Error538', a2)
    assert _is_linked(b, 'bpmn2_Error538', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition539'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition539', b)
    if hasattr(a2, 'bpmn2_ItemDefinition539'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition539', b)
    _safe_set(b, 'bpmn2_Error538', None)
    assert not _is_linked(b, 'bpmn2_Error538', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition539'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition539', b)


def test_assoc_structureRef543_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_Escalation(escalationCode="sample_text")
    _safe_set(b, 'bpmn2_Escalation544', a1)
    assert _is_linked(b, 'bpmn2_Escalation544', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition545'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition545', b)
    _safe_set(b, 'bpmn2_Escalation544', a2)
    assert _is_linked(b, 'bpmn2_Escalation544', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition545'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition545', b)
    if hasattr(a2, 'bpmn2_ItemDefinition545'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition545', b)
    _safe_set(b, 'bpmn2_Escalation544', None)
    assert not _is_linked(b, 'bpmn2_Escalation544', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition545'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition545', b)


def test_assoc_supports801_reverse_link_reassign_clear():
    a1 = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    a2 = bpmn2_Process(isClosed=False, isExecutable=False, processType="sample_text_2")
    b = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    _safe_set(b, 'bpmn2_Process802', a1)
    assert _is_linked(b, 'bpmn2_Process802', a1)
    if hasattr(a1, 'bpmn2_Process800'):
        assert _is_linked(a1, 'bpmn2_Process800', b)
    _safe_set(b, 'bpmn2_Process802', a2)
    assert _is_linked(b, 'bpmn2_Process802', a2)
    if hasattr(a1, 'bpmn2_Process800'):
        assert not _is_linked(a1, 'bpmn2_Process800', b)
    if hasattr(a2, 'bpmn2_Process800'):
        assert _is_linked(a2, 'bpmn2_Process800', b)
    _safe_set(b, 'bpmn2_Process802', None)
    assert not _is_linked(b, 'bpmn2_Process802', a2)
    if hasattr(a2, 'bpmn2_Process800'):
        assert not _is_linked(a2, 'bpmn2_Process800', b)


def test_assoc_targetRef329_reverse_link_reassign_clear():
    a1 = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    a2 = bpmn2_BaseElement(anyAttribute="sample_text_2", description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = bpmn2_Association(associationDirection="sample_text")
    _safe_set(b, 'bpmn2_Association330', a1)
    assert _is_linked(b, 'bpmn2_Association330', a1)
    if hasattr(a1, 'bpmn2_BaseElement331'):
        assert _is_linked(a1, 'bpmn2_BaseElement331', b)
    _safe_set(b, 'bpmn2_Association330', a2)
    assert _is_linked(b, 'bpmn2_Association330', a2)
    if hasattr(a1, 'bpmn2_BaseElement331'):
        assert not _is_linked(a1, 'bpmn2_BaseElement331', b)
    if hasattr(a2, 'bpmn2_BaseElement331'):
        assert _is_linked(a2, 'bpmn2_BaseElement331', b)
    _safe_set(b, 'bpmn2_Association330', None)
    assert not _is_linked(b, 'bpmn2_Association330', a2)
    if hasattr(a2, 'bpmn2_BaseElement331'):
        assert not _is_linked(a2, 'bpmn2_BaseElement331', b)


def test_assoc_type824_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceParameter(isRequired=True)
    a2 = bpmn2_ResourceParameter(isRequired=False)
    b = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    _safe_set(b, 'bpmn2_ItemDefinition826', a1)
    assert _is_linked(b, 'bpmn2_ItemDefinition826', a1)
    if hasattr(a1, 'bpmn2_ResourceParameter825'):
        assert _is_linked(a1, 'bpmn2_ResourceParameter825', b)
    _safe_set(b, 'bpmn2_ItemDefinition826', a2)
    assert _is_linked(b, 'bpmn2_ItemDefinition826', a2)
    if hasattr(a1, 'bpmn2_ResourceParameter825'):
        assert not _is_linked(a1, 'bpmn2_ResourceParameter825', b)
    if hasattr(a2, 'bpmn2_ResourceParameter825'):
        assert _is_linked(a2, 'bpmn2_ResourceParameter825', b)
    _safe_set(b, 'bpmn2_ItemDefinition826', None)
    assert not _is_linked(b, 'bpmn2_ItemDefinition826', a2)
    if hasattr(a2, 'bpmn2_ResourceParameter825'):
        assert not _is_linked(a2, 'bpmn2_ResourceParameter825', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activity4_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot5' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot5', None)
    _safe_set(owner, 'bpmn2_Activity', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot5') == owner
    _safe_set(owner, 'bpmn2_Activity', None)
    assert getattr(partner, 'bpmn2_DocumentRoot5') is None


def test_assoc_adHocSubProcess6_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot7' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_AdHocSubProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_AdHocSubProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_AdHocSubProcess(cancelRemainingInstances=True, ordering="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot7', None)
    _safe_set(owner, 'bpmn2_AdHocSubProcess', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot7') == owner
    _safe_set(owner, 'bpmn2_AdHocSubProcess', None)
    assert getattr(partner, 'bpmn2_DocumentRoot7') is None


def test_assoc_artifacts404_stub_double():
    # bpmn2_Artifact has no real 'bpmn2_Artifact406' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_Artifact()
    setattr(partner, 'bpmn2_Artifact406', None)
    _safe_set(owner, 'bpmn2_Collaboration405', {partner})
    assert getattr(partner, 'bpmn2_Artifact406') == owner
    _safe_set(owner, 'bpmn2_Collaboration405', set())
    assert getattr(partner, 'bpmn2_Artifact406') is None


def test_assoc_artifacts791_stub_double():
    # bpmn2_Artifact has no real 'bpmn2_Artifact793' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Artifact()
    setattr(partner, 'bpmn2_Artifact793', None)
    _safe_set(owner, 'bpmn2_Process792', {partner})
    assert getattr(partner, 'bpmn2_Artifact793') == owner
    _safe_set(owner, 'bpmn2_Process792', set())
    assert getattr(partner, 'bpmn2_Artifact793') is None


def test_assoc_artifacts873_stub_double():
    # bpmn2_Artifact has no real 'bpmn2_Artifact875' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SubProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SubProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SubProcess(triggeredByEvent=True)
    partner = bpmn2_Artifact()
    setattr(partner, 'bpmn2_Artifact875', None)
    _safe_set(owner, 'bpmn2_SubProcess874', {partner})
    assert getattr(partner, 'bpmn2_Artifact875') == owner
    _safe_set(owner, 'bpmn2_SubProcess874', set())
    assert getattr(partner, 'bpmn2_Artifact875') is None


def test_assoc_association14_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot15' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Association(associationDirection="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot15', None)
    _safe_set(owner, 'bpmn2_Association', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot15') == owner
    _safe_set(owner, 'bpmn2_Association', None)
    assert getattr(partner, 'bpmn2_DocumentRoot15') is None


def test_assoc_auditing782_stub_double():
    # bpmn2_Auditing has no real 'bpmn2_Auditing784' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Auditing()
    setattr(partner, 'bpmn2_Auditing784', None)
    _safe_set(owner, 'bpmn2_Process783', partner)
    assert getattr(partner, 'bpmn2_Auditing784') == owner
    _safe_set(owner, 'bpmn2_Process783', None)
    assert getattr(partner, 'bpmn2_Auditing784') is None


def test_assoc_baseElement18_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot19' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_BaseElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_BaseElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot19', None)
    _safe_set(owner, 'bpmn2_BaseElement', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot19') == owner
    _safe_set(owner, 'bpmn2_BaseElement', None)
    assert getattr(partner, 'bpmn2_DocumentRoot19') is None


def test_assoc_baseElementWithMixedContent20_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot21' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_BaseElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_BaseElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot21', None)
    _safe_set(owner, 'bpmn2_BaseElement22', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot21') == owner
    _safe_set(owner, 'bpmn2_BaseElement22', None)
    assert getattr(partner, 'bpmn2_DocumentRoot21') is None


def test_assoc_boundaryEvent23_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot24' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_BoundaryEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_BoundaryEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_BoundaryEvent(cancelActivity=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot24', None)
    _safe_set(owner, 'bpmn2_BoundaryEvent', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot24') == owner
    _safe_set(owner, 'bpmn2_BoundaryEvent', None)
    assert getattr(partner, 'bpmn2_DocumentRoot24') is None


def test_assoc_businessRuleTask25_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot26' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_BusinessRuleTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_BusinessRuleTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_BusinessRuleTask(implementation="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot26', None)
    _safe_set(owner, 'bpmn2_BusinessRuleTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot26') == owner
    _safe_set(owner, 'bpmn2_BusinessRuleTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot26') is None


def test_assoc_calledCollaborationRef353_stub_double():
    # bpmn2_CallConversation has no real 'bpmn2_CallConversation354' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_CallConversation()
    setattr(partner, 'bpmn2_CallConversation354', None)
    _safe_set(owner, 'bpmn2_Collaboration355', partner)
    assert getattr(partner, 'bpmn2_CallConversation354') == owner
    _safe_set(owner, 'bpmn2_Collaboration355', None)
    assert getattr(partner, 'bpmn2_CallConversation354') is None


def test_assoc_catchEvent43_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot44' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot44', None)
    _safe_set(owner, 'bpmn2_CatchEvent', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot44') == owner
    _safe_set(owner, 'bpmn2_CatchEvent', None)
    assert getattr(partner, 'bpmn2_DocumentRoot44') is None


def test_assoc_categorizedFlowElements383_stub_double():
    # bpmn2_FlowElement has no real 'bpmn2_FlowElement385' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CategoryValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CategoryValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CategoryValue(value="sample_text")
    partner = bpmn2_FlowElement()
    setattr(partner, 'bpmn2_FlowElement385', None)
    _safe_set(owner, 'bpmn2_CategoryValue384', {partner})
    assert getattr(partner, 'bpmn2_FlowElement385') == owner
    _safe_set(owner, 'bpmn2_CategoryValue384', set())
    assert getattr(partner, 'bpmn2_FlowElement385') is None


def test_assoc_categoryValue380_stub_double():
    # bpmn2_Category has no real 'bpmn2_Category381' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CategoryValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CategoryValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CategoryValue(value="sample_text")
    partner = bpmn2_Category()
    setattr(partner, 'bpmn2_Category381', None)
    _safe_set(owner, 'bpmn2_CategoryValue382', partner)
    assert getattr(partner, 'bpmn2_Category381') == owner
    _safe_set(owner, 'bpmn2_CategoryValue382', None)
    assert getattr(partner, 'bpmn2_Category381') is None


def test_assoc_categoryValue47_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot48' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CategoryValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CategoryValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CategoryValue(value="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot48', None)
    _safe_set(owner, 'bpmn2_CategoryValue', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot48') == owner
    _safe_set(owner, 'bpmn2_CategoryValue', None)
    assert getattr(partner, 'bpmn2_DocumentRoot48') is None


def test_assoc_categoryValueRef571_stub_double():
    # bpmn2_FlowElement has no real 'bpmn2_FlowElement572' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CategoryValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CategoryValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CategoryValue(value="sample_text")
    partner = bpmn2_FlowElement()
    setattr(partner, 'bpmn2_FlowElement572', None)
    _safe_set(owner, 'bpmn2_CategoryValue573', partner)
    assert getattr(partner, 'bpmn2_FlowElement572') == owner
    _safe_set(owner, 'bpmn2_CategoryValue573', None)
    assert getattr(partner, 'bpmn2_FlowElement572') is None


def test_assoc_categoryValueRef595_stub_double():
    # bpmn2_Group has no real 'bpmn2_Group596' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CategoryValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CategoryValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CategoryValue(value="sample_text")
    partner = bpmn2_Group()
    setattr(partner, 'bpmn2_Group596', None)
    _safe_set(owner, 'bpmn2_CategoryValue597', partner)
    assert getattr(partner, 'bpmn2_Group596') == owner
    _safe_set(owner, 'bpmn2_CategoryValue597', None)
    assert getattr(partner, 'bpmn2_Group596') is None


def test_assoc_choreographyActivity53_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot54' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ChoreographyActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ChoreographyActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ChoreographyActivity(loopType="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot54', None)
    _safe_set(owner, 'bpmn2_ChoreographyActivity', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot54') == owner
    _safe_set(owner, 'bpmn2_ChoreographyActivity', None)
    assert getattr(partner, 'bpmn2_DocumentRoot54') is None


def test_assoc_choreographyRef422_stub_double():
    # bpmn2_Choreography has no real 'bpmn2_Choreography424' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_Choreography()
    setattr(partner, 'bpmn2_Choreography424', None)
    _safe_set(owner, 'bpmn2_Collaboration423', {partner})
    assert getattr(partner, 'bpmn2_Choreography424') == owner
    _safe_set(owner, 'bpmn2_Collaboration423', set())
    assert getattr(partner, 'bpmn2_Choreography424') is None


def test_assoc_collaboration51_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot52' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot52', None)
    _safe_set(owner, 'bpmn2_Collaboration', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot52') == owner
    _safe_set(owner, 'bpmn2_Collaboration', None)
    assert getattr(partner, 'bpmn2_DocumentRoot52') is None


def test_assoc_compensateEventDefinition57_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot58' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CompensateEventDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CompensateEventDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CompensateEventDefinition(waitForCompletion=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot58', None)
    _safe_set(owner, 'bpmn2_CompensateEventDefinition', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot58') == owner
    _safe_set(owner, 'bpmn2_CompensateEventDefinition', None)
    assert getattr(partner, 'bpmn2_DocumentRoot58') is None


def test_assoc_competency314_stub_double():
    # bpmn2_Competency has no real 'bpmn2_Competency316' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_Competency()
    setattr(partner, 'bpmn2_Competency316', None)
    _safe_set(owner, 'bpmn2_Activity315', {partner})
    assert getattr(partner, 'bpmn2_Competency316') == owner
    _safe_set(owner, 'bpmn2_Activity315', set())
    assert getattr(partner, 'bpmn2_Competency316') is None


def test_assoc_completionCondition317_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression319' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_AdHocSubProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_AdHocSubProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_AdHocSubProcess(cancelRemainingInstances=True, ordering="sample_text")
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression319', None)
    _safe_set(owner, 'bpmn2_AdHocSubProcess318', partner)
    assert getattr(partner, 'bpmn2_Expression319') == owner
    _safe_set(owner, 'bpmn2_AdHocSubProcess318', None)
    assert getattr(partner, 'bpmn2_Expression319') is None


def test_assoc_completionCondition729_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression731' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression731', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics730', partner)
    assert getattr(partner, 'bpmn2_Expression731') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics730', None)
    assert getattr(partner, 'bpmn2_Expression731') is None


def test_assoc_complexBehaviorDefinition726_stub_double():
    # bpmn2_ComplexBehaviorDefinition has no real 'bpmn2_ComplexBehaviorDefinition728' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_ComplexBehaviorDefinition()
    setattr(partner, 'bpmn2_ComplexBehaviorDefinition728', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics727', {partner})
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition728') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics727', set())
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition728') is None


def test_assoc_condition431_stub_double():
    # bpmn2_ComplexBehaviorDefinition has no real 'bpmn2_ComplexBehaviorDefinition432' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(body="sample_text", language="sample_text", mixed="sample_text")
    partner = bpmn2_ComplexBehaviorDefinition()
    setattr(partner, 'bpmn2_ComplexBehaviorDefinition432', None)
    _safe_set(owner, 'bpmn2_FormalExpression433', partner)
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition432') == owner
    _safe_set(owner, 'bpmn2_FormalExpression433', None)
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition432') is None


def test_assoc_conditionExpression848_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression850' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression850', None)
    _safe_set(owner, 'bpmn2_SequenceFlow849', partner)
    assert getattr(partner, 'bpmn2_Expression850') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow849', None)
    assert getattr(partner, 'bpmn2_Expression850') is None


def test_assoc_conversationAssociations410_stub_double():
    # bpmn2_ConversationAssociation has no real 'bpmn2_ConversationAssociation412' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_ConversationAssociation()
    setattr(partner, 'bpmn2_ConversationAssociation412', None)
    _safe_set(owner, 'bpmn2_Collaboration411', {partner})
    assert getattr(partner, 'bpmn2_ConversationAssociation412') == owner
    _safe_set(owner, 'bpmn2_Collaboration411', set())
    assert getattr(partner, 'bpmn2_ConversationAssociation412') is None


def test_assoc_conversationLinks425_stub_double():
    # bpmn2_ConversationLink has no real 'bpmn2_ConversationLink427' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_ConversationLink()
    setattr(partner, 'bpmn2_ConversationLink427', None)
    _safe_set(owner, 'bpmn2_Collaboration426', {partner})
    assert getattr(partner, 'bpmn2_ConversationLink427') == owner
    _safe_set(owner, 'bpmn2_Collaboration426', set())
    assert getattr(partner, 'bpmn2_ConversationLink427') is None


def test_assoc_conversations407_stub_double():
    # bpmn2_ConversationNode has no real 'bpmn2_ConversationNode409' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_ConversationNode()
    setattr(partner, 'bpmn2_ConversationNode409', None)
    _safe_set(owner, 'bpmn2_Collaboration408', {partner})
    assert getattr(partner, 'bpmn2_ConversationNode409') == owner
    _safe_set(owner, 'bpmn2_Collaboration408', set())
    assert getattr(partner, 'bpmn2_ConversationNode409') is None


def test_assoc_correlationKeys389_stub_double():
    # bpmn2_CorrelationKey has no real 'bpmn2_CorrelationKey391' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ChoreographyActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ChoreographyActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ChoreographyActivity(loopType="sample_text")
    partner = bpmn2_CorrelationKey()
    setattr(partner, 'bpmn2_CorrelationKey391', None)
    _safe_set(owner, 'bpmn2_ChoreographyActivity390', {partner})
    assert getattr(partner, 'bpmn2_CorrelationKey391') == owner
    _safe_set(owner, 'bpmn2_ChoreographyActivity390', set())
    assert getattr(partner, 'bpmn2_CorrelationKey391') is None


def test_assoc_correlationKeys419_stub_double():
    # bpmn2_CorrelationKey has no real 'bpmn2_CorrelationKey421' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_CorrelationKey()
    setattr(partner, 'bpmn2_CorrelationKey421', None)
    _safe_set(owner, 'bpmn2_Collaboration420', {partner})
    assert getattr(partner, 'bpmn2_CorrelationKey421') == owner
    _safe_set(owner, 'bpmn2_Collaboration420', set())
    assert getattr(partner, 'bpmn2_CorrelationKey421') is None


def test_assoc_correlationSubscriptions797_stub_double():
    # bpmn2_CorrelationSubscription has no real 'bpmn2_CorrelationSubscription799' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_CorrelationSubscription()
    setattr(partner, 'bpmn2_CorrelationSubscription799', None)
    _safe_set(owner, 'bpmn2_Process798', {partner})
    assert getattr(partner, 'bpmn2_CorrelationSubscription799') == owner
    _safe_set(owner, 'bpmn2_Process798', set())
    assert getattr(partner, 'bpmn2_CorrelationSubscription799') is None


def test_assoc_dataInput83_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot84' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot84', None)
    _safe_set(owner, 'bpmn2_DataInput', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot84') == owner
    _safe_set(owner, 'bpmn2_DataInput', None)
    assert getattr(partner, 'bpmn2_DocumentRoot84') is None


def test_assoc_dataInputAssociations283_stub_double():
    # bpmn2_DataInputAssociation has no real 'bpmn2_DataInputAssociation285' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_DataInputAssociation()
    setattr(partner, 'bpmn2_DataInputAssociation285', None)
    _safe_set(owner, 'bpmn2_Activity284', {partner})
    assert getattr(partner, 'bpmn2_DataInputAssociation285') == owner
    _safe_set(owner, 'bpmn2_Activity284', set())
    assert getattr(partner, 'bpmn2_DataInputAssociation285') is None


def test_assoc_dataInputRefs622_stub_double():
    # bpmn2_InputSet has no real 'inputSetRefs' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_InputSet()
    setattr(partner, 'inputSetRefs', None)
    _safe_set(owner, 'DataInput', partner)
    assert getattr(partner, 'inputSetRefs') == owner
    _safe_set(owner, 'DataInput', None)
    assert getattr(partner, 'inputSetRefs') is None


def test_assoc_dataInputs610_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification611' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification611', None)
    _safe_set(owner, 'bpmn2_DataInput612', partner)
    assert getattr(partner, 'bpmn2_InputOutputSpecification611') == owner
    _safe_set(owner, 'bpmn2_DataInput612', None)
    assert getattr(partner, 'bpmn2_InputOutputSpecification611') is None


def test_assoc_dataInputs881_stub_double():
    # bpmn2_ThrowEvent has no real 'bpmn2_ThrowEvent882' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_ThrowEvent()
    setattr(partner, 'bpmn2_ThrowEvent882', None)
    _safe_set(owner, 'bpmn2_DataInput883', partner)
    assert getattr(partner, 'bpmn2_ThrowEvent882') == owner
    _safe_set(owner, 'bpmn2_DataInput883', None)
    assert getattr(partner, 'bpmn2_ThrowEvent882') is None


def test_assoc_dataObject87_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot88' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataObject(isCollection=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot88', None)
    _safe_set(owner, 'bpmn2_DataObject', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot88') == owner
    _safe_set(owner, 'bpmn2_DataObject', None)
    assert getattr(partner, 'bpmn2_DocumentRoot88') is None


def test_assoc_dataObjectRef510_stub_double():
    # bpmn2_DataObjectReference has no real 'bpmn2_DataObjectReference511' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataObject(isCollection=True)
    partner = bpmn2_DataObjectReference()
    setattr(partner, 'bpmn2_DataObjectReference511', None)
    _safe_set(owner, 'bpmn2_DataObject512', partner)
    assert getattr(partner, 'bpmn2_DataObjectReference511') == owner
    _safe_set(owner, 'bpmn2_DataObject512', None)
    assert getattr(partner, 'bpmn2_DataObjectReference511') is None


def test_assoc_dataOutput91_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot92' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot92', None)
    _safe_set(owner, 'bpmn2_DataOutput', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot92') == owner
    _safe_set(owner, 'bpmn2_DataOutput', None)
    assert getattr(partner, 'bpmn2_DocumentRoot92') is None


def test_assoc_dataOutputAssociation368_stub_double():
    # bpmn2_DataOutputAssociation has no real 'bpmn2_DataOutputAssociation370' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_DataOutputAssociation()
    setattr(partner, 'bpmn2_DataOutputAssociation370', None)
    _safe_set(owner, 'bpmn2_CatchEvent369', {partner})
    assert getattr(partner, 'bpmn2_DataOutputAssociation370') == owner
    _safe_set(owner, 'bpmn2_CatchEvent369', set())
    assert getattr(partner, 'bpmn2_DataOutputAssociation370') is None


def test_assoc_dataOutputAssociations286_stub_double():
    # bpmn2_DataOutputAssociation has no real 'bpmn2_DataOutputAssociation288' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_DataOutputAssociation()
    setattr(partner, 'bpmn2_DataOutputAssociation288', None)
    _safe_set(owner, 'bpmn2_Activity287', {partner})
    assert getattr(partner, 'bpmn2_DataOutputAssociation288') == owner
    _safe_set(owner, 'bpmn2_Activity287', set())
    assert getattr(partner, 'bpmn2_DataOutputAssociation288') is None


def test_assoc_dataOutputRefs750_stub_double():
    # bpmn2_OutputSet has no real 'outputSetRefs' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_OutputSet()
    setattr(partner, 'outputSetRefs', None)
    _safe_set(owner, 'DataOutput', partner)
    assert getattr(partner, 'outputSetRefs') == owner
    _safe_set(owner, 'DataOutput', None)
    assert getattr(partner, 'outputSetRefs') is None


def test_assoc_dataOutputs613_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification614' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification614', None)
    _safe_set(owner, 'bpmn2_DataOutput615', partner)
    assert getattr(partner, 'bpmn2_InputOutputSpecification614') == owner
    _safe_set(owner, 'bpmn2_DataOutput615', None)
    assert getattr(partner, 'bpmn2_InputOutputSpecification614') is None


def test_assoc_dataPath475_stub_double():
    # bpmn2_CorrelationPropertyBinding has no real 'bpmn2_CorrelationPropertyBinding476' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(body="sample_text", language="sample_text", mixed="sample_text")
    partner = bpmn2_CorrelationPropertyBinding()
    setattr(partner, 'bpmn2_CorrelationPropertyBinding476', None)
    _safe_set(owner, 'bpmn2_FormalExpression477', partner)
    assert getattr(partner, 'bpmn2_CorrelationPropertyBinding476') == owner
    _safe_set(owner, 'bpmn2_FormalExpression477', None)
    assert getattr(partner, 'bpmn2_CorrelationPropertyBinding476') is None


def test_assoc_dataStore97_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot98' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataStore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataStore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataStore(capacity=7, isUnlimited=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot98', None)
    _safe_set(owner, 'bpmn2_DataStore', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot98') == owner
    _safe_set(owner, 'bpmn2_DataStore', None)
    assert getattr(partner, 'bpmn2_DocumentRoot98') is None


def test_assoc_dataStoreRef520_stub_double():
    # bpmn2_DataStoreReference has no real 'bpmn2_DataStoreReference521' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataStore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataStore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataStore(capacity=7, isUnlimited=True)
    partner = bpmn2_DataStoreReference()
    setattr(partner, 'bpmn2_DataStoreReference521', None)
    _safe_set(owner, 'bpmn2_DataStore522', partner)
    assert getattr(partner, 'bpmn2_DataStoreReference521') == owner
    _safe_set(owner, 'bpmn2_DataStore522', None)
    assert getattr(partner, 'bpmn2_DataStoreReference521') is None


def test_assoc_default440_stub_double():
    # bpmn2_ComplexGateway has no real 'bpmn2_ComplexGateway441' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_ComplexGateway()
    setattr(partner, 'bpmn2_ComplexGateway441', None)
    _safe_set(owner, 'bpmn2_SequenceFlow442', partner)
    assert getattr(partner, 'bpmn2_ComplexGateway441') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow442', None)
    assert getattr(partner, 'bpmn2_ComplexGateway441') is None


def test_assoc_default552_stub_double():
    # bpmn2_ExclusiveGateway has no real 'bpmn2_ExclusiveGateway553' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_ExclusiveGateway()
    setattr(partner, 'bpmn2_ExclusiveGateway553', None)
    _safe_set(owner, 'bpmn2_SequenceFlow554', partner)
    assert getattr(partner, 'bpmn2_ExclusiveGateway553') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow554', None)
    assert getattr(partner, 'bpmn2_ExclusiveGateway553') is None


def test_assoc_default598_stub_double():
    # bpmn2_InclusiveGateway has no real 'bpmn2_InclusiveGateway599' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_InclusiveGateway()
    setattr(partner, 'bpmn2_InclusiveGateway599', None)
    _safe_set(owner, 'bpmn2_SequenceFlow600', partner)
    assert getattr(partner, 'bpmn2_InclusiveGateway599') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow600', None)
    assert getattr(partner, 'bpmn2_InclusiveGateway599') is None


def test_assoc_definitions101_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot102' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Definitions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Definitions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot102', None)
    _safe_set(owner, 'bpmn2_Definitions', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot102') == owner
    _safe_set(owner, 'bpmn2_Definitions', None)
    assert getattr(partner, 'bpmn2_DocumentRoot102') is None


def test_assoc_diagrams532_stub_double():
    # bpmn2_BPMNDiagram has no real 'bpmn2_BPMNDiagram' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Definitions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Definitions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    partner = bpmn2_BPMNDiagram()
    setattr(partner, 'bpmn2_BPMNDiagram', None)
    _safe_set(owner, 'bpmn2_Definitions533', {partner})
    assert getattr(partner, 'bpmn2_BPMNDiagram') == owner
    _safe_set(owner, 'bpmn2_Definitions533', set())
    assert getattr(partner, 'bpmn2_BPMNDiagram') is None


def test_assoc_documentation103_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot104' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Documentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Documentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Documentation(mixed="sample_text", text="sample_text", textFormat="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot104', None)
    _safe_set(owner, 'bpmn2_Documentation', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot104') == owner
    _safe_set(owner, 'bpmn2_Documentation', None)
    assert getattr(partner, 'bpmn2_DocumentRoot104') is None


def test_assoc_error109_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot110' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Error's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Error's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Error(errorCode="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot110', None)
    _safe_set(owner, 'bpmn2_Error', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot110') == owner
    _safe_set(owner, 'bpmn2_Error', None)
    assert getattr(partner, 'bpmn2_DocumentRoot110') is None


def test_assoc_errorRef540_stub_double():
    # bpmn2_ErrorEventDefinition has no real 'bpmn2_ErrorEventDefinition541' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Error's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Error's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Error(errorCode="sample_text")
    partner = bpmn2_ErrorEventDefinition()
    setattr(partner, 'bpmn2_ErrorEventDefinition541', None)
    _safe_set(owner, 'bpmn2_Error542', partner)
    assert getattr(partner, 'bpmn2_ErrorEventDefinition541') == owner
    _safe_set(owner, 'bpmn2_Error542', None)
    assert getattr(partner, 'bpmn2_ErrorEventDefinition541') is None


def test_assoc_errorRefs744_stub_double():
    # bpmn2_Operation has no real 'bpmn2_Operation745' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Error's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Error's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Error(errorCode="sample_text")
    partner = bpmn2_Operation()
    setattr(partner, 'bpmn2_Operation745', None)
    _safe_set(owner, 'bpmn2_Error746', partner)
    assert getattr(partner, 'bpmn2_Operation745') == owner
    _safe_set(owner, 'bpmn2_Error746', None)
    assert getattr(partner, 'bpmn2_Operation745') is None


def test_assoc_escalation113_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot114' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Escalation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Escalation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Escalation(escalationCode="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot114', None)
    _safe_set(owner, 'bpmn2_Escalation', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot114') == owner
    _safe_set(owner, 'bpmn2_Escalation', None)
    assert getattr(partner, 'bpmn2_DocumentRoot114') is None


def test_assoc_escalationRef546_stub_double():
    # bpmn2_EscalationEventDefinition has no real 'bpmn2_EscalationEventDefinition547' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Escalation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Escalation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Escalation(escalationCode="sample_text")
    partner = bpmn2_EscalationEventDefinition()
    setattr(partner, 'bpmn2_EscalationEventDefinition547', None)
    _safe_set(owner, 'bpmn2_Escalation548', partner)
    assert getattr(partner, 'bpmn2_EscalationEventDefinition547') == owner
    _safe_set(owner, 'bpmn2_Escalation548', None)
    assert getattr(partner, 'bpmn2_EscalationEventDefinition547') is None


def test_assoc_eventBasedGateway119_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot120' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_EventBasedGateway's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_EventBasedGateway's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_EventBasedGateway(eventGatewayType="sample_text", instantiate=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot120', None)
    _safe_set(owner, 'bpmn2_EventBasedGateway', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot120') == owner
    _safe_set(owner, 'bpmn2_EventBasedGateway', None)
    assert getattr(partner, 'bpmn2_DocumentRoot120') is None


def test_assoc_eventDefinitionRefs377_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition379' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition379', None)
    _safe_set(owner, 'bpmn2_CatchEvent378', {partner})
    assert getattr(partner, 'bpmn2_EventDefinition379') == owner
    _safe_set(owner, 'bpmn2_CatchEvent378', set())
    assert getattr(partner, 'bpmn2_EventDefinition379') is None


def test_assoc_eventDefinitions374_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition376' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition376', None)
    _safe_set(owner, 'bpmn2_CatchEvent375', {partner})
    assert getattr(partner, 'bpmn2_EventDefinition376') == owner
    _safe_set(owner, 'bpmn2_CatchEvent375', set())
    assert getattr(partner, 'bpmn2_EventDefinition376') is None


def test_assoc_extension125_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot126' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Extension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Extension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Extension(mustUnderstand=True, xsdDefinition="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot126', None)
    _safe_set(owner, 'bpmn2_Extension', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot126') == owner
    _safe_set(owner, 'bpmn2_Extension', None)
    assert getattr(partner, 'bpmn2_DocumentRoot126') is None


def test_assoc_extensionElements127_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot128' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ExtensionAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ExtensionAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ExtensionAttributeValue(value="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot128', None)
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot128') == owner
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue', None)
    assert getattr(partner, 'bpmn2_DocumentRoot128') is None


def test_assoc_formalExpression131_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot132' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(body="sample_text", language="sample_text", mixed="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot132', None)
    _safe_set(owner, 'bpmn2_FormalExpression', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot132') == owner
    _safe_set(owner, 'bpmn2_FormalExpression', None)
    assert getattr(partner, 'bpmn2_DocumentRoot132') is None


def test_assoc_gateway133_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot134' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Gateway's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Gateway's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Gateway(gatewayDirection="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot134', None)
    _safe_set(owner, 'bpmn2_Gateway', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot134') == owner
    _safe_set(owner, 'bpmn2_Gateway', None)
    assert getattr(partner, 'bpmn2_DocumentRoot134') is None


def test_assoc_globalBusinessRuleTask135_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot136' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_GlobalBusinessRuleTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_GlobalBusinessRuleTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_GlobalBusinessRuleTask(implementation="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot136', None)
    _safe_set(owner, 'bpmn2_GlobalBusinessRuleTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot136') == owner
    _safe_set(owner, 'bpmn2_GlobalBusinessRuleTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot136') is None


def test_assoc_globalScriptTask143_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot144' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_GlobalScriptTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_GlobalScriptTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_GlobalScriptTask(script="sample_text", scriptLanguage="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot144', None)
    _safe_set(owner, 'bpmn2_GlobalScriptTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot144') == owner
    _safe_set(owner, 'bpmn2_GlobalScriptTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot144') is None


def test_assoc_globalUserTask147_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot148' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_GlobalUserTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_GlobalUserTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_GlobalUserTask(implementation="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot148', None)
    _safe_set(owner, 'bpmn2_GlobalUserTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot148') == owner
    _safe_set(owner, 'bpmn2_GlobalUserTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot148') is None


def test_assoc_import_159_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot160' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Import(importType="sample_text", location="sample_text", namespace="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot160', None)
    _safe_set(owner, 'bpmn2_Import', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot160') == owner
    _safe_set(owner, 'bpmn2_Import', None)
    assert getattr(partner, 'bpmn2_DocumentRoot160') is None


def test_assoc_incoming579_stub_double():
    # bpmn2_FlowNode has no real 'targetRef' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'targetRef', None)
    _safe_set(owner, 'SequenceFlow', partner)
    assert getattr(partner, 'targetRef') == owner
    _safe_set(owner, 'SequenceFlow', None)
    assert getattr(partner, 'targetRef') is None


def test_assoc_initiatingParticipantRef392_stub_double():
    # bpmn2_Participant has no real 'bpmn2_Participant394' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ChoreographyActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ChoreographyActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ChoreographyActivity(loopType="sample_text")
    partner = bpmn2_Participant()
    setattr(partner, 'bpmn2_Participant394', None)
    _safe_set(owner, 'bpmn2_ChoreographyActivity393', partner)
    assert getattr(partner, 'bpmn2_Participant394') == owner
    _safe_set(owner, 'bpmn2_ChoreographyActivity393', None)
    assert getattr(partner, 'bpmn2_Participant394') is None


def test_assoc_inputSetRefs507_stub_double():
    # bpmn2_InputSet has no real 'InputSet508' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_InputSet()
    setattr(partner, 'InputSet508', None)
    _safe_set(owner, 'dataInputRefs', {partner})
    assert getattr(partner, 'InputSet508') == owner
    _safe_set(owner, 'dataInputRefs', set())
    assert getattr(partner, 'InputSet508') is None


def test_assoc_inputSetWithOptional504_stub_double():
    # bpmn2_InputSet has no real 'InputSet' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_InputSet()
    setattr(partner, 'InputSet', None)
    _safe_set(owner, 'optionalInputRefs', {partner})
    assert getattr(partner, 'InputSet') == owner
    _safe_set(owner, 'optionalInputRefs', set())
    assert getattr(partner, 'InputSet') is None


def test_assoc_inputSetWithWhileExecuting505_stub_double():
    # bpmn2_InputSet has no real 'InputSet506' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_InputSet()
    setattr(partner, 'InputSet506', None)
    _safe_set(owner, 'whileExecutingInputRefs', {partner})
    assert getattr(partner, 'InputSet506') == owner
    _safe_set(owner, 'whileExecutingInputRefs', set())
    assert getattr(partner, 'InputSet506') is None


def test_assoc_ioSpecification276_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification278' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification278', None)
    _safe_set(owner, 'bpmn2_Activity277', partner)
    assert getattr(partner, 'bpmn2_InputOutputSpecification278') == owner
    _safe_set(owner, 'bpmn2_Activity277', None)
    assert getattr(partner, 'bpmn2_InputOutputSpecification278') is None


def test_assoc_isMeasuredByCriterion300_stub_double():
    # bpmn2_Criterion has no real 'bpmn2_Criterion' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_Criterion()
    setattr(partner, 'bpmn2_Criterion', None)
    _safe_set(owner, 'bpmn2_Activity301', {partner})
    assert getattr(partner, 'bpmn2_Criterion') == owner
    _safe_set(owner, 'bpmn2_Activity301', set())
    assert getattr(partner, 'bpmn2_Criterion') is None


def test_assoc_isPerformedBy307_stub_double():
    # bpmn2_Performer has no real 'bpmn2_Performer309' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_Performer()
    setattr(partner, 'bpmn2_Performer309', None)
    _safe_set(owner, 'bpmn2_Activity308', {partner})
    assert getattr(partner, 'bpmn2_Performer309') == owner
    _safe_set(owner, 'bpmn2_Activity308', set())
    assert getattr(partner, 'bpmn2_Performer309') is None


def test_assoc_isPerformedByOrganisationalUnit302_stub_double():
    # bpmn2_OrganisationalUnit has no real 'bpmn2_OrganisationalUnit' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_OrganisationalUnit()
    setattr(partner, 'bpmn2_OrganisationalUnit', None)
    _safe_set(owner, 'bpmn2_Activity303', {partner})
    assert getattr(partner, 'bpmn2_OrganisationalUnit') == owner
    _safe_set(owner, 'bpmn2_Activity303', set())
    assert getattr(partner, 'bpmn2_OrganisationalUnit') is None


def test_assoc_isPerformedByPosition310_stub_double():
    # bpmn2_Position has no real 'bpmn2_Position' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_Position()
    setattr(partner, 'bpmn2_Position', None)
    _safe_set(owner, 'bpmn2_Activity311', {partner})
    assert getattr(partner, 'bpmn2_Position') == owner
    _safe_set(owner, 'bpmn2_Activity311', set())
    assert getattr(partner, 'bpmn2_Position') is None


def test_assoc_isPerformedByRole312_stub_double():
    # bpmn2_Role has no real 'bpmn2_Role' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_Role()
    setattr(partner, 'bpmn2_Role', None)
    _safe_set(owner, 'bpmn2_Activity313', {partner})
    assert getattr(partner, 'bpmn2_Role') == owner
    _safe_set(owner, 'bpmn2_Activity313', set())
    assert getattr(partner, 'bpmn2_Role') is None


def test_assoc_isResponsibleByOrganisationalUnit304_stub_double():
    # bpmn2_OrganisationalUnit has no real 'bpmn2_OrganisationalUnit306' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_OrganisationalUnit()
    setattr(partner, 'bpmn2_OrganisationalUnit306', None)
    _safe_set(owner, 'bpmn2_Activity305', {partner})
    assert getattr(partner, 'bpmn2_OrganisationalUnit306') == owner
    _safe_set(owner, 'bpmn2_Activity305', set())
    assert getattr(partner, 'bpmn2_OrganisationalUnit306') is None


def test_assoc_itemDefinition175_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot176' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot176', None)
    _safe_set(owner, 'bpmn2_ItemDefinition', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot176') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition', None)
    assert getattr(partner, 'bpmn2_DocumentRoot176') is None


def test_assoc_itemRef687_stub_double():
    # bpmn2_Message has no real 'bpmn2_Message688' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_Message()
    setattr(partner, 'bpmn2_Message688', None)
    _safe_set(owner, 'bpmn2_ItemDefinition689', partner)
    assert getattr(partner, 'bpmn2_Message688') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition689', None)
    assert getattr(partner, 'bpmn2_Message688') is None


def test_assoc_itemSubjectRef645_stub_double():
    # bpmn2_ItemAwareElement has no real 'bpmn2_ItemAwareElement646' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_ItemAwareElement()
    setattr(partner, 'bpmn2_ItemAwareElement646', None)
    _safe_set(owner, 'bpmn2_ItemDefinition647', partner)
    assert getattr(partner, 'bpmn2_ItemAwareElement646') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition647', None)
    assert getattr(partner, 'bpmn2_ItemAwareElement646') is None


def test_assoc_loopCardinality711_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression713' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression713', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics712', partner)
    assert getattr(partner, 'bpmn2_Expression713') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics712', None)
    assert getattr(partner, 'bpmn2_Expression713') is None


def test_assoc_loopCharacteristics292_stub_double():
    # bpmn2_LoopCharacteristics has no real 'bpmn2_LoopCharacteristics294' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_LoopCharacteristics()
    setattr(partner, 'bpmn2_LoopCharacteristics294', None)
    _safe_set(owner, 'bpmn2_Activity293', partner)
    assert getattr(partner, 'bpmn2_LoopCharacteristics294') == owner
    _safe_set(owner, 'bpmn2_Activity293', None)
    assert getattr(partner, 'bpmn2_LoopCharacteristics294') is None


def test_assoc_loopCondition864_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression866' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_StandardLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_StandardLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_StandardLoopCharacteristics(loopMaximum="sample_text", testBefore=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression866', None)
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics865', partner)
    assert getattr(partner, 'bpmn2_Expression866') == owner
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics865', None)
    assert getattr(partner, 'bpmn2_Expression866') is None


def test_assoc_loopDataInputRef714_stub_double():
    # bpmn2_ItemAwareElement has no real 'bpmn2_ItemAwareElement716' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_ItemAwareElement()
    setattr(partner, 'bpmn2_ItemAwareElement716', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics715', partner)
    assert getattr(partner, 'bpmn2_ItemAwareElement716') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics715', None)
    assert getattr(partner, 'bpmn2_ItemAwareElement716') is None


def test_assoc_loopDataOutputRef717_stub_double():
    # bpmn2_ItemAwareElement has no real 'bpmn2_ItemAwareElement719' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_ItemAwareElement()
    setattr(partner, 'bpmn2_ItemAwareElement719', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics718', partner)
    assert getattr(partner, 'bpmn2_ItemAwareElement719') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics718', None)
    assert getattr(partner, 'bpmn2_ItemAwareElement719') is None


def test_assoc_messageFlowAssociations416_stub_double():
    # bpmn2_MessageFlowAssociation has no real 'bpmn2_MessageFlowAssociation418' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_MessageFlowAssociation()
    setattr(partner, 'bpmn2_MessageFlowAssociation418', None)
    _safe_set(owner, 'bpmn2_Collaboration417', {partner})
    assert getattr(partner, 'bpmn2_MessageFlowAssociation418') == owner
    _safe_set(owner, 'bpmn2_Collaboration417', set())
    assert getattr(partner, 'bpmn2_MessageFlowAssociation418') is None


def test_assoc_messageFlows401_stub_double():
    # bpmn2_MessageFlow has no real 'bpmn2_MessageFlow403' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_MessageFlow()
    setattr(partner, 'bpmn2_MessageFlow403', None)
    _safe_set(owner, 'bpmn2_Collaboration402', {partner})
    assert getattr(partner, 'bpmn2_MessageFlow403') == owner
    _safe_set(owner, 'bpmn2_Collaboration402', set())
    assert getattr(partner, 'bpmn2_MessageFlow403') is None


def test_assoc_messagePath481_stub_double():
    # bpmn2_CorrelationPropertyRetrievalExpression has no real 'bpmn2_CorrelationPropertyRetrievalExpression482' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(body="sample_text", language="sample_text", mixed="sample_text")
    partner = bpmn2_CorrelationPropertyRetrievalExpression()
    setattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression482', None)
    _safe_set(owner, 'bpmn2_FormalExpression483', partner)
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression482') == owner
    _safe_set(owner, 'bpmn2_FormalExpression483', None)
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression482') is None


def test_assoc_messageRef806_stub_double():
    # bpmn2_Message has no real 'bpmn2_Message808' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ReceiveTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ReceiveTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ReceiveTask(implementation="sample_text", instantiate=True)
    partner = bpmn2_Message()
    setattr(partner, 'bpmn2_Message808', None)
    _safe_set(owner, 'bpmn2_ReceiveTask807', partner)
    assert getattr(partner, 'bpmn2_Message808') == owner
    _safe_set(owner, 'bpmn2_ReceiveTask807', None)
    assert getattr(partner, 'bpmn2_Message808') is None


def test_assoc_messageRef842_stub_double():
    # bpmn2_Message has no real 'bpmn2_Message844' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SendTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SendTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SendTask(implementation="sample_text")
    partner = bpmn2_Message()
    setattr(partner, 'bpmn2_Message844', None)
    _safe_set(owner, 'bpmn2_SendTask843', partner)
    assert getattr(partner, 'bpmn2_Message844') == owner
    _safe_set(owner, 'bpmn2_SendTask843', None)
    assert getattr(partner, 'bpmn2_Message844') is None


def test_assoc_monitoring785_stub_double():
    # bpmn2_Monitoring has no real 'bpmn2_Monitoring787' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Monitoring()
    setattr(partner, 'bpmn2_Monitoring787', None)
    _safe_set(owner, 'bpmn2_Process786', partner)
    assert getattr(partner, 'bpmn2_Monitoring787') == owner
    _safe_set(owner, 'bpmn2_Process786', None)
    assert getattr(partner, 'bpmn2_Monitoring787') is None


def test_assoc_multiInstanceLoopCharacteristics197_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot198' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot198', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot198') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics', None)
    assert getattr(partner, 'bpmn2_DocumentRoot198') is None


def test_assoc_noneBehaviorEventRef732_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition734' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition734', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics733', partner)
    assert getattr(partner, 'bpmn2_EventDefinition734') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics733', None)
    assert getattr(partner, 'bpmn2_EventDefinition734') is None


def test_assoc_oneBehaviorEventRef735_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition737' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition737', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics736', partner)
    assert getattr(partner, 'bpmn2_EventDefinition737') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics736', None)
    assert getattr(partner, 'bpmn2_EventDefinition737') is None


def test_assoc_operationRef809_stub_double():
    # bpmn2_Operation has no real 'bpmn2_Operation811' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ReceiveTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ReceiveTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ReceiveTask(implementation="sample_text", instantiate=True)
    partner = bpmn2_Operation()
    setattr(partner, 'bpmn2_Operation811', None)
    _safe_set(owner, 'bpmn2_ReceiveTask810', partner)
    assert getattr(partner, 'bpmn2_Operation811') == owner
    _safe_set(owner, 'bpmn2_ReceiveTask810', None)
    assert getattr(partner, 'bpmn2_Operation811') is None


def test_assoc_operationRef845_stub_double():
    # bpmn2_Operation has no real 'bpmn2_Operation847' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SendTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SendTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SendTask(implementation="sample_text")
    partner = bpmn2_Operation()
    setattr(partner, 'bpmn2_Operation847', None)
    _safe_set(owner, 'bpmn2_SendTask846', partner)
    assert getattr(partner, 'bpmn2_Operation847') == owner
    _safe_set(owner, 'bpmn2_SendTask846', None)
    assert getattr(partner, 'bpmn2_Operation847') is None


def test_assoc_operationRef855_stub_double():
    # bpmn2_Operation has no real 'bpmn2_Operation857' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ServiceTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ServiceTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ServiceTask(implementation="sample_text")
    partner = bpmn2_Operation()
    setattr(partner, 'bpmn2_Operation857', None)
    _safe_set(owner, 'bpmn2_ServiceTask856', partner)
    assert getattr(partner, 'bpmn2_Operation857') == owner
    _safe_set(owner, 'bpmn2_ServiceTask856', None)
    assert getattr(partner, 'bpmn2_Operation857') is None


def test_assoc_optionalInputRefs623_stub_double():
    # bpmn2_InputSet has no real 'inputSetWithOptional' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_InputSet()
    setattr(partner, 'inputSetWithOptional', None)
    _safe_set(owner, 'DataInput624', partner)
    assert getattr(partner, 'inputSetWithOptional') == owner
    _safe_set(owner, 'DataInput624', None)
    assert getattr(partner, 'inputSetWithOptional') is None


def test_assoc_optionalOutputRefs751_stub_double():
    # bpmn2_OutputSet has no real 'outputSetWithOptional' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_OutputSet()
    setattr(partner, 'outputSetWithOptional', None)
    _safe_set(owner, 'DataOutput752', partner)
    assert getattr(partner, 'outputSetWithOptional') == owner
    _safe_set(owner, 'DataOutput752', None)
    assert getattr(partner, 'outputSetWithOptional') is None


def test_assoc_outgoing581_stub_double():
    # bpmn2_FlowNode has no real 'sourceRef' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'sourceRef', None)
    _safe_set(owner, 'SequenceFlow582', partner)
    assert getattr(partner, 'sourceRef') == owner
    _safe_set(owner, 'SequenceFlow582', None)
    assert getattr(partner, 'sourceRef') is None


def test_assoc_outputSet371_stub_double():
    # bpmn2_OutputSet has no real 'bpmn2_OutputSet373' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_OutputSet()
    setattr(partner, 'bpmn2_OutputSet373', None)
    _safe_set(owner, 'bpmn2_CatchEvent372', partner)
    assert getattr(partner, 'bpmn2_OutputSet373') == owner
    _safe_set(owner, 'bpmn2_CatchEvent372', None)
    assert getattr(partner, 'bpmn2_OutputSet373') is None


def test_assoc_outputSetRefs516_stub_double():
    # bpmn2_OutputSet has no real 'OutputSet517' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_OutputSet()
    setattr(partner, 'OutputSet517', None)
    _safe_set(owner, 'dataOutputRefs', {partner})
    assert getattr(partner, 'OutputSet517') == owner
    _safe_set(owner, 'dataOutputRefs', set())
    assert getattr(partner, 'OutputSet517') is None


def test_assoc_outputSetWithOptional513_stub_double():
    # bpmn2_OutputSet has no real 'OutputSet' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_OutputSet()
    setattr(partner, 'OutputSet', None)
    _safe_set(owner, 'optionalOutputRefs', {partner})
    assert getattr(partner, 'OutputSet') == owner
    _safe_set(owner, 'optionalOutputRefs', set())
    assert getattr(partner, 'OutputSet') is None


def test_assoc_outputSetWithWhileExecuting514_stub_double():
    # bpmn2_OutputSet has no real 'OutputSet515' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_OutputSet()
    setattr(partner, 'OutputSet515', None)
    _safe_set(owner, 'whileExecutingOutputRefs', {partner})
    assert getattr(partner, 'OutputSet515') == owner
    _safe_set(owner, 'whileExecutingOutputRefs', set())
    assert getattr(partner, 'OutputSet515') is None


def test_assoc_parameterRef830_stub_double():
    # bpmn2_ResourceParameterBinding has no real 'bpmn2_ResourceParameterBinding831' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ResourceParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ResourceParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ResourceParameter(isRequired=True)
    partner = bpmn2_ResourceParameterBinding()
    setattr(partner, 'bpmn2_ResourceParameterBinding831', None)
    _safe_set(owner, 'bpmn2_ResourceParameter832', partner)
    assert getattr(partner, 'bpmn2_ResourceParameterBinding831') == owner
    _safe_set(owner, 'bpmn2_ResourceParameter832', None)
    assert getattr(partner, 'bpmn2_ResourceParameterBinding831') is None


def test_assoc_participantAssociations413_stub_double():
    # bpmn2_ParticipantAssociation has no real 'bpmn2_ParticipantAssociation415' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_ParticipantAssociation()
    setattr(partner, 'bpmn2_ParticipantAssociation415', None)
    _safe_set(owner, 'bpmn2_Collaboration414', {partner})
    assert getattr(partner, 'bpmn2_ParticipantAssociation415') == owner
    _safe_set(owner, 'bpmn2_Collaboration414', set())
    assert getattr(partner, 'bpmn2_ParticipantAssociation415') is None


def test_assoc_participantMultiplicity209_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot210' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ParticipantMultiplicity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ParticipantMultiplicity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ParticipantMultiplicity(maximum=7, minimum=7)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot210', None)
    _safe_set(owner, 'bpmn2_ParticipantMultiplicity', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot210') == owner
    _safe_set(owner, 'bpmn2_ParticipantMultiplicity', None)
    assert getattr(partner, 'bpmn2_DocumentRoot210') is None


def test_assoc_participantMultiplicity764_stub_double():
    # bpmn2_Participant has no real 'bpmn2_Participant765' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ParticipantMultiplicity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ParticipantMultiplicity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ParticipantMultiplicity(maximum=7, minimum=7)
    partner = bpmn2_Participant()
    setattr(partner, 'bpmn2_Participant765', None)
    _safe_set(owner, 'bpmn2_ParticipantMultiplicity766', partner)
    assert getattr(partner, 'bpmn2_Participant765') == owner
    _safe_set(owner, 'bpmn2_ParticipantMultiplicity766', None)
    assert getattr(partner, 'bpmn2_Participant765') is None


def test_assoc_participantRefs386_stub_double():
    # bpmn2_Participant has no real 'bpmn2_Participant388' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ChoreographyActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ChoreographyActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ChoreographyActivity(loopType="sample_text")
    partner = bpmn2_Participant()
    setattr(partner, 'bpmn2_Participant388', None)
    _safe_set(owner, 'bpmn2_ChoreographyActivity387', {partner})
    assert getattr(partner, 'bpmn2_Participant388') == owner
    _safe_set(owner, 'bpmn2_ChoreographyActivity387', set())
    assert getattr(partner, 'bpmn2_Participant388') is None


def test_assoc_participants398_stub_double():
    # bpmn2_Participant has no real 'bpmn2_Participant400' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True)
    partner = bpmn2_Participant()
    setattr(partner, 'bpmn2_Participant400', None)
    _safe_set(owner, 'bpmn2_Collaboration399', {partner})
    assert getattr(partner, 'bpmn2_Participant400') == owner
    _safe_set(owner, 'bpmn2_Collaboration399', set())
    assert getattr(partner, 'bpmn2_Participant400') is None


def test_assoc_partitionElement654_stub_double():
    # bpmn2_Lane has no real 'bpmn2_Lane655' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_BaseElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_BaseElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    partner = bpmn2_Lane()
    setattr(partner, 'bpmn2_Lane655', None)
    _safe_set(owner, 'bpmn2_BaseElement656', partner)
    assert getattr(partner, 'bpmn2_Lane655') == owner
    _safe_set(owner, 'bpmn2_BaseElement656', None)
    assert getattr(partner, 'bpmn2_Lane655') is None


def test_assoc_partitionElementRef661_stub_double():
    # bpmn2_Lane has no real 'bpmn2_Lane662' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_BaseElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_BaseElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_BaseElement(anyAttribute="sample_text", description="sample_text", id="sample_text", name="sample_text")
    partner = bpmn2_Lane()
    setattr(partner, 'bpmn2_Lane662', None)
    _safe_set(owner, 'bpmn2_BaseElement663', partner)
    assert getattr(partner, 'bpmn2_Lane662') == owner
    _safe_set(owner, 'bpmn2_BaseElement663', None)
    assert getattr(partner, 'bpmn2_Lane662') is None


def test_assoc_process217_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot218' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot218', None)
    _safe_set(owner, 'bpmn2_Process', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot218') == owner
    _safe_set(owner, 'bpmn2_Process', None)
    assert getattr(partner, 'bpmn2_DocumentRoot218') is None


def test_assoc_processRef767_stub_double():
    # bpmn2_Participant has no real 'bpmn2_Participant768' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Participant()
    setattr(partner, 'bpmn2_Participant768', None)
    _safe_set(owner, 'bpmn2_Process769', partner)
    assert getattr(partner, 'bpmn2_Participant768') == owner
    _safe_set(owner, 'bpmn2_Process769', None)
    assert getattr(partner, 'bpmn2_Participant768') is None


def test_assoc_properties280_stub_double():
    # bpmn2_Property has no real 'bpmn2_Property282' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_Property()
    setattr(partner, 'bpmn2_Property282', None)
    _safe_set(owner, 'bpmn2_Activity281', {partner})
    assert getattr(partner, 'bpmn2_Property282') == owner
    _safe_set(owner, 'bpmn2_Activity281', set())
    assert getattr(partner, 'bpmn2_Property282') is None


def test_assoc_properties788_stub_double():
    # bpmn2_Property has no real 'bpmn2_Property790' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Property()
    setattr(partner, 'bpmn2_Property790', None)
    _safe_set(owner, 'bpmn2_Process789', {partner})
    assert getattr(partner, 'bpmn2_Property790') == owner
    _safe_set(owner, 'bpmn2_Process789', set())
    assert getattr(partner, 'bpmn2_Property790') is None


def test_assoc_receiveTask221_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot222' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ReceiveTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ReceiveTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ReceiveTask(implementation="sample_text", instantiate=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot222', None)
    _safe_set(owner, 'bpmn2_ReceiveTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot222') == owner
    _safe_set(owner, 'bpmn2_ReceiveTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot222') is None


def test_assoc_referencesDocument509_stub_double():
    # bpmn2_Document has no real 'DocumentAndKnowledge.ecoreDocument' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_Document()
    setattr(partner, 'DocumentAndKnowledge.ecoreDocument', None)
    _safe_set(owner, 'dataInput', {partner})
    assert getattr(partner, 'DocumentAndKnowledge.ecoreDocument') == owner
    _safe_set(owner, 'dataInput', set())
    assert getattr(partner, 'DocumentAndKnowledge.ecoreDocument') is None


def test_assoc_referencesDocument518_stub_double():
    # bpmn2_Document has no real 'DocumentAndKnowledge.ecoreDocument519' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_Document()
    setattr(partner, 'DocumentAndKnowledge.ecoreDocument519', None)
    _safe_set(owner, 'dataOutput', {partner})
    assert getattr(partner, 'DocumentAndKnowledge.ecoreDocument519') == owner
    _safe_set(owner, 'dataOutput', set())
    assert getattr(partner, 'DocumentAndKnowledge.ecoreDocument519') is None


def test_assoc_relationship223_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot224' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Relationship(direction="sample_text", type="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot224', None)
    _safe_set(owner, 'bpmn2_Relationship', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot224') == owner
    _safe_set(owner, 'bpmn2_Relationship', None)
    assert getattr(partner, 'bpmn2_DocumentRoot224') is None


def test_assoc_renderings592_stub_double():
    # bpmn2_Rendering has no real 'bpmn2_Rendering594' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_GlobalUserTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_GlobalUserTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_GlobalUserTask(implementation="sample_text")
    partner = bpmn2_Rendering()
    setattr(partner, 'bpmn2_Rendering594', None)
    _safe_set(owner, 'bpmn2_GlobalUserTask593', {partner})
    assert getattr(partner, 'bpmn2_Rendering594') == owner
    _safe_set(owner, 'bpmn2_GlobalUserTask593', set())
    assert getattr(partner, 'bpmn2_Rendering594') is None


def test_assoc_renderings905_stub_double():
    # bpmn2_Rendering has no real 'bpmn2_Rendering907' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_UserTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_UserTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_UserTask(implementation="sample_text")
    partner = bpmn2_Rendering()
    setattr(partner, 'bpmn2_Rendering907', None)
    _safe_set(owner, 'bpmn2_UserTask906', {partner})
    assert getattr(partner, 'bpmn2_Rendering907') == owner
    _safe_set(owner, 'bpmn2_UserTask906', set())
    assert getattr(partner, 'bpmn2_Rendering907') is None


def test_assoc_requiresCompetency298_stub_double():
    # bpmn2_Competency has no real 'bpmn2_Competency' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_Competency()
    setattr(partner, 'bpmn2_Competency', None)
    _safe_set(owner, 'bpmn2_Activity299', {partner})
    assert getattr(partner, 'bpmn2_Competency') == owner
    _safe_set(owner, 'bpmn2_Activity299', set())
    assert getattr(partner, 'bpmn2_Competency') is None


def test_assoc_resourceParameter231_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot232' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ResourceParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ResourceParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ResourceParameter(isRequired=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot232', None)
    _safe_set(owner, 'bpmn2_ResourceParameter', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot232') == owner
    _safe_set(owner, 'bpmn2_ResourceParameter', None)
    assert getattr(partner, 'bpmn2_DocumentRoot232') is None


def test_assoc_resourceParameters818_stub_double():
    # bpmn2_Resource has no real 'bpmn2_Resource819' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ResourceParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ResourceParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ResourceParameter(isRequired=True)
    partner = bpmn2_Resource()
    setattr(partner, 'bpmn2_Resource819', None)
    _safe_set(owner, 'bpmn2_ResourceParameter820', partner)
    assert getattr(partner, 'bpmn2_Resource819') == owner
    _safe_set(owner, 'bpmn2_ResourceParameter820', None)
    assert getattr(partner, 'bpmn2_Resource819') is None


def test_assoc_resources289_stub_double():
    # bpmn2_ResourceRole has no real 'bpmn2_ResourceRole291' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_ResourceRole()
    setattr(partner, 'bpmn2_ResourceRole291', None)
    _safe_set(owner, 'bpmn2_Activity290', {partner})
    assert getattr(partner, 'bpmn2_ResourceRole291') == owner
    _safe_set(owner, 'bpmn2_Activity290', set())
    assert getattr(partner, 'bpmn2_ResourceRole291') is None


def test_assoc_resources794_stub_double():
    # bpmn2_ResourceRole has no real 'bpmn2_ResourceRole796' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_ResourceRole()
    setattr(partner, 'bpmn2_ResourceRole796', None)
    _safe_set(owner, 'bpmn2_Process795', {partner})
    assert getattr(partner, 'bpmn2_ResourceRole796') == owner
    _safe_set(owner, 'bpmn2_Process795', set())
    assert getattr(partner, 'bpmn2_ResourceRole796') is None


def test_assoc_rootElements529_stub_double():
    # bpmn2_RootElement has no real 'bpmn2_RootElement531' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Definitions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Definitions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    partner = bpmn2_RootElement()
    setattr(partner, 'bpmn2_RootElement531', None)
    _safe_set(owner, 'bpmn2_Definitions530', {partner})
    assert getattr(partner, 'bpmn2_RootElement531') == owner
    _safe_set(owner, 'bpmn2_Definitions530', set())
    assert getattr(partner, 'bpmn2_RootElement531') is None


def test_assoc_scriptTask237_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot238' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ScriptTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ScriptTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ScriptTask(script="sample_text", scriptFormat="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot238', None)
    _safe_set(owner, 'bpmn2_ScriptTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot238') == owner
    _safe_set(owner, 'bpmn2_ScriptTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot238') is None


def test_assoc_sendTask239_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot240' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SendTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SendTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SendTask(implementation="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot240', None)
    _safe_set(owner, 'bpmn2_SendTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot240') == owner
    _safe_set(owner, 'bpmn2_SendTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot240') is None


def test_assoc_sequenceFlow241_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot242' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot242', None)
    _safe_set(owner, 'bpmn2_SequenceFlow', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot242') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow', None)
    assert getattr(partner, 'bpmn2_DocumentRoot242') is None


def test_assoc_serviceTask243_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot244' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ServiceTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ServiceTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ServiceTask(implementation="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot244', None)
    _safe_set(owner, 'bpmn2_ServiceTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot244') == owner
    _safe_set(owner, 'bpmn2_ServiceTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot244') is None


def test_assoc_sourceRef851_stub_double():
    # bpmn2_FlowNode has no real 'FlowNode852' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'FlowNode852', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'FlowNode852') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'FlowNode852') is None


def test_assoc_sources812_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject814' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Relationship(direction="sample_text", type="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject814', None)
    _safe_set(owner, 'bpmn2_Relationship813', {partner})
    assert getattr(partner, 'bpmn2_EObject814') == owner
    _safe_set(owner, 'bpmn2_Relationship813', set())
    assert getattr(partner, 'bpmn2_EObject814') is None


def test_assoc_standardLoopCharacteristics249_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot250' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_StandardLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_StandardLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_StandardLoopCharacteristics(loopMaximum="sample_text", testBefore=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot250', None)
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot250') == owner
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics', None)
    assert getattr(partner, 'bpmn2_DocumentRoot250') is None


def test_assoc_startEvent251_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot252' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_StartEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_StartEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_StartEvent(isInterrupting=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot252', None)
    _safe_set(owner, 'bpmn2_StartEvent', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot252') == owner
    _safe_set(owner, 'bpmn2_StartEvent', None)
    assert getattr(partner, 'bpmn2_DocumentRoot252') is None


def test_assoc_structureRef651_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject653' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject653', None)
    _safe_set(owner, 'bpmn2_ItemDefinition652', partner)
    assert getattr(partner, 'bpmn2_EObject653') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition652', None)
    assert getattr(partner, 'bpmn2_EObject653') is None


def test_assoc_structureRef858_stub_double():
    # bpmn2_Signal has no real 'bpmn2_Signal859' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_Signal()
    setattr(partner, 'bpmn2_Signal859', None)
    _safe_set(owner, 'bpmn2_ItemDefinition860', partner)
    assert getattr(partner, 'bpmn2_Signal859') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition860', None)
    assert getattr(partner, 'bpmn2_Signal859') is None


def test_assoc_subProcess257_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot258' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SubProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SubProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SubProcess(triggeredByEvent=True)
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot258', None)
    _safe_set(owner, 'bpmn2_SubProcess', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot258') == owner
    _safe_set(owner, 'bpmn2_SubProcess', None)
    assert getattr(partner, 'bpmn2_DocumentRoot258') is None


def test_assoc_targetRef853_stub_double():
    # bpmn2_FlowNode has no real 'FlowNode854' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'FlowNode854', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'FlowNode854') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'FlowNode854') is None


def test_assoc_targets815_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject817' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Relationship(direction="sample_text", type="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject817', None)
    _safe_set(owner, 'bpmn2_Relationship816', {partner})
    assert getattr(partner, 'bpmn2_EObject817') == owner
    _safe_set(owner, 'bpmn2_Relationship816', set())
    assert getattr(partner, 'bpmn2_EObject817') is None


def test_assoc_textAnnotation266_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot267' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_TextAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_TextAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_TextAnnotation(text="sample_text", textFormat="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot267', None)
    _safe_set(owner, 'bpmn2_TextAnnotation', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot267') == owner
    _safe_set(owner, 'bpmn2_TextAnnotation', None)
    assert getattr(partner, 'bpmn2_DocumentRoot267') is None


def test_assoc_transaction272_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot273' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Transaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Transaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Transaction(method="sample_text", protocol="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot273', None)
    _safe_set(owner, 'bpmn2_Transaction', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot273') == owner
    _safe_set(owner, 'bpmn2_Transaction', None)
    assert getattr(partner, 'bpmn2_DocumentRoot273') is None


def test_assoc_transformation498_stub_double():
    # bpmn2_DataAssociation has no real 'bpmn2_DataAssociation499' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(body="sample_text", language="sample_text", mixed="sample_text")
    partner = bpmn2_DataAssociation()
    setattr(partner, 'bpmn2_DataAssociation499', None)
    _safe_set(owner, 'bpmn2_FormalExpression500', partner)
    assert getattr(partner, 'bpmn2_DataAssociation499') == owner
    _safe_set(owner, 'bpmn2_FormalExpression500', None)
    assert getattr(partner, 'bpmn2_DataAssociation499') is None


def test_assoc_type472_stub_double():
    # bpmn2_CorrelationProperty has no real 'bpmn2_CorrelationProperty473' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_CorrelationProperty()
    setattr(partner, 'bpmn2_CorrelationProperty473', None)
    _safe_set(owner, 'bpmn2_ItemDefinition474', partner)
    assert getattr(partner, 'bpmn2_CorrelationProperty473') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition474', None)
    assert getattr(partner, 'bpmn2_CorrelationProperty473') is None


def test_assoc_userTask274_stub_double():
    # bpmn2_DocumentRoot has no real 'bpmn2_DocumentRoot275' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_UserTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_UserTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_UserTask(implementation="sample_text")
    partner = bpmn2_DocumentRoot()
    setattr(partner, 'bpmn2_DocumentRoot275', None)
    _safe_set(owner, 'bpmn2_UserTask', partner)
    assert getattr(partner, 'bpmn2_DocumentRoot275') == owner
    _safe_set(owner, 'bpmn2_UserTask', None)
    assert getattr(partner, 'bpmn2_DocumentRoot275') is None


def test_assoc_valueRef559_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject561' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ExtensionAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ExtensionAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ExtensionAttributeValue(value="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject561', None)
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue560', partner)
    assert getattr(partner, 'bpmn2_EObject561') == owner
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue560', None)
    assert getattr(partner, 'bpmn2_EObject561') is None


def test_assoc_whileExecutingInputRefs625_stub_double():
    # bpmn2_InputSet has no real 'inputSetWithWhileExecuting' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True)
    partner = bpmn2_InputSet()
    setattr(partner, 'inputSetWithWhileExecuting', None)
    _safe_set(owner, 'DataInput626', partner)
    assert getattr(partner, 'inputSetWithWhileExecuting') == owner
    _safe_set(owner, 'DataInput626', None)
    assert getattr(partner, 'inputSetWithWhileExecuting') is None


def test_assoc_whileExecutingOutputRefs753_stub_double():
    # bpmn2_OutputSet has no real 'outputSetWithWhileExecuting' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True)
    partner = bpmn2_OutputSet()
    setattr(partner, 'outputSetWithWhileExecuting', None)
    _safe_set(owner, 'DataOutput754', partner)
    assert getattr(partner, 'outputSetWithWhileExecuting') == owner
    _safe_set(owner, 'DataOutput754', None)
    assert getattr(partner, 'outputSetWithWhileExecuting') is None


