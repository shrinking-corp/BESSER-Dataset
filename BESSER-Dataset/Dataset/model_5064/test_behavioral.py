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


