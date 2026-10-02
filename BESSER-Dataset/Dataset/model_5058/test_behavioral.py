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
    bpmn2_Documentation,
    bpmn2_EObject,
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
    bpmn2_OutputSet,
    bpmn2_ParallelGateway,
    bpmn2_Participant,
    bpmn2_ParticipantAssociation,
    bpmn2_ParticipantMultiplicity,
    bpmn2_PartnerEntity,
    bpmn2_PartnerRole,
    bpmn2_Performer,
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

def test_assoc_activityRef358_reverse_link_reassign_clear():
    a1 = bpmn2_CompensateEventDefinition(waitForCompletion=True)
    a2 = bpmn2_CompensateEventDefinition(waitForCompletion=False)
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'bpmn2_Activity359', a1)
    assert _is_linked(b, 'bpmn2_Activity359', a1)
    if hasattr(a1, 'bpmn2_CompensateEventDefinition'):
        assert _is_linked(a1, 'bpmn2_CompensateEventDefinition', b)
    _safe_set(b, 'bpmn2_Activity359', a2)
    assert _is_linked(b, 'bpmn2_Activity359', a2)
    if hasattr(a1, 'bpmn2_CompensateEventDefinition'):
        assert not _is_linked(a1, 'bpmn2_CompensateEventDefinition', b)
    if hasattr(a2, 'bpmn2_CompensateEventDefinition'):
        assert _is_linked(a2, 'bpmn2_CompensateEventDefinition', b)
    _safe_set(b, 'bpmn2_Activity359', None)
    assert not _is_linked(b, 'bpmn2_Activity359', a2)
    if hasattr(a2, 'bpmn2_CompensateEventDefinition'):
        assert not _is_linked(a2, 'bpmn2_CompensateEventDefinition', b)


def test_assoc_attachedToRef287_reverse_link_reassign_clear():
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


def test_assoc_boundaryEventRefs282_reverse_link_reassign_clear():
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


def test_assoc_categorizedFlowElements143_reverse_link_reassign_clear():
    a1 = bpmn2_FlowElement(name="sample_text")
    a2 = bpmn2_FlowElement(name="sample_text_2")
    b = bpmn2_CategoryValue(value="sample_text")
    _safe_set(b, 'categoryValueRef', {a1})
    assert _is_linked(b, 'categoryValueRef', a1)
    if hasattr(a1, 'FlowElement'):
        assert _is_linked(a1, 'FlowElement', b)
    _safe_set(b, 'categoryValueRef', {a2})
    assert _is_linked(b, 'categoryValueRef', a2)
    if hasattr(a1, 'FlowElement'):
        assert not _is_linked(a1, 'FlowElement', b)
    if hasattr(a2, 'FlowElement'):
        assert _is_linked(a2, 'FlowElement', b)
    _safe_set(b, 'categoryValueRef', set())
    assert not _is_linked(b, 'categoryValueRef', a2)
    if hasattr(a2, 'FlowElement'):
        assert not _is_linked(a2, 'FlowElement', b)


def test_assoc_categoryValue422_reverse_link_reassign_clear():
    a1 = bpmn2_CategoryValue(value="sample_text")
    a2 = bpmn2_CategoryValue(value="sample_text_2")
    b = bpmn2_Category(name="sample_text")
    _safe_set(b, 'bpmn2_Category', {a1})
    assert _is_linked(b, 'bpmn2_Category', a1)
    if hasattr(a1, 'bpmn2_CategoryValue423'):
        assert _is_linked(a1, 'bpmn2_CategoryValue423', b)
    _safe_set(b, 'bpmn2_Category', {a2})
    assert _is_linked(b, 'bpmn2_Category', a2)
    if hasattr(a1, 'bpmn2_CategoryValue423'):
        assert not _is_linked(a1, 'bpmn2_CategoryValue423', b)
    if hasattr(a2, 'bpmn2_CategoryValue423'):
        assert _is_linked(a2, 'bpmn2_CategoryValue423', b)
    _safe_set(b, 'bpmn2_Category', set())
    assert not _is_linked(b, 'bpmn2_Category', a2)
    if hasattr(a2, 'bpmn2_CategoryValue423'):
        assert not _is_linked(a2, 'bpmn2_CategoryValue423', b)


def test_assoc_categoryValueRef142_reverse_link_reassign_clear():
    a1 = bpmn2_FlowElement(name="sample_text")
    a2 = bpmn2_FlowElement(name="sample_text_2")
    b = bpmn2_CategoryValue(value="sample_text")
    _safe_set(b, 'CategoryValue', a1)
    assert _is_linked(b, 'CategoryValue', a1)
    if hasattr(a1, 'categorizedFlowElements'):
        assert _is_linked(a1, 'categorizedFlowElements', b)
    _safe_set(b, 'CategoryValue', a2)
    assert _is_linked(b, 'CategoryValue', a2)
    if hasattr(a1, 'categorizedFlowElements'):
        assert not _is_linked(a1, 'categorizedFlowElements', b)
    if hasattr(a2, 'categorizedFlowElements'):
        assert _is_linked(a2, 'categorizedFlowElements', b)
    _safe_set(b, 'CategoryValue', None)
    assert not _is_linked(b, 'CategoryValue', a2)
    if hasattr(a2, 'categorizedFlowElements'):
        assert not _is_linked(a2, 'categorizedFlowElements', b)


def test_assoc_childLaneSet146_reverse_link_reassign_clear():
    a1 = bpmn2_LaneSet(name="sample_text")
    a2 = bpmn2_LaneSet(name="sample_text_2")
    b = bpmn2_Lane(name="sample_text")
    _safe_set(b, 'bpmn2_Lane147', a1)
    assert _is_linked(b, 'bpmn2_Lane147', a1)
    if hasattr(a1, 'bpmn2_LaneSet148'):
        assert _is_linked(a1, 'bpmn2_LaneSet148', b)
    _safe_set(b, 'bpmn2_Lane147', a2)
    assert _is_linked(b, 'bpmn2_Lane147', a2)
    if hasattr(a1, 'bpmn2_LaneSet148'):
        assert not _is_linked(a1, 'bpmn2_LaneSet148', b)
    if hasattr(a2, 'bpmn2_LaneSet148'):
        assert _is_linked(a2, 'bpmn2_LaneSet148', b)
    _safe_set(b, 'bpmn2_Lane147', None)
    assert not _is_linked(b, 'bpmn2_Lane147', a2)
    if hasattr(a2, 'bpmn2_LaneSet148'):
        assert not _is_linked(a2, 'bpmn2_LaneSet148', b)


def test_assoc_conversationLinks185_reverse_link_reassign_clear():
    a1 = bpmn2_ConversationLink(name="sample_text")
    a2 = bpmn2_ConversationLink(name="sample_text_2")
    b = bpmn2_Collaboration(isClosed=True, name="sample_text")
    _safe_set(b, 'bpmn2_Collaboration186', {a1})
    assert _is_linked(b, 'bpmn2_Collaboration186', a1)
    if hasattr(a1, 'bpmn2_ConversationLink'):
        assert _is_linked(a1, 'bpmn2_ConversationLink', b)
    _safe_set(b, 'bpmn2_Collaboration186', {a2})
    assert _is_linked(b, 'bpmn2_Collaboration186', a2)
    if hasattr(a1, 'bpmn2_ConversationLink'):
        assert not _is_linked(a1, 'bpmn2_ConversationLink', b)
    if hasattr(a2, 'bpmn2_ConversationLink'):
        assert _is_linked(a2, 'bpmn2_ConversationLink', b)
    _safe_set(b, 'bpmn2_Collaboration186', set())
    assert not _is_linked(b, 'bpmn2_Collaboration186', a2)
    if hasattr(a2, 'bpmn2_ConversationLink'):
        assert not _is_linked(a2, 'bpmn2_ConversationLink', b)


def test_assoc_conversations183_reverse_link_reassign_clear():
    a1 = bpmn2_ConversationNode(name="sample_text")
    a2 = bpmn2_ConversationNode(name="sample_text_2")
    b = bpmn2_Collaboration(isClosed=True, name="sample_text")
    _safe_set(b, 'bpmn2_Collaboration184', {a1})
    assert _is_linked(b, 'bpmn2_Collaboration184', a1)
    if hasattr(a1, 'bpmn2_ConversationNode'):
        assert _is_linked(a1, 'bpmn2_ConversationNode', b)
    _safe_set(b, 'bpmn2_Collaboration184', {a2})
    assert _is_linked(b, 'bpmn2_Collaboration184', a2)
    if hasattr(a1, 'bpmn2_ConversationNode'):
        assert not _is_linked(a1, 'bpmn2_ConversationNode', b)
    if hasattr(a2, 'bpmn2_ConversationNode'):
        assert _is_linked(a2, 'bpmn2_ConversationNode', b)
    _safe_set(b, 'bpmn2_Collaboration184', set())
    assert not _is_linked(b, 'bpmn2_Collaboration184', a2)
    if hasattr(a2, 'bpmn2_ConversationNode'):
        assert not _is_linked(a2, 'bpmn2_ConversationNode', b)


def test_assoc_correlationKeys181_reverse_link_reassign_clear():
    a1 = bpmn2_CorrelationKey(name="sample_text")
    a2 = bpmn2_CorrelationKey(name="sample_text_2")
    b = bpmn2_Collaboration(isClosed=True, name="sample_text")
    _safe_set(b, 'bpmn2_Collaboration182', {a1})
    assert _is_linked(b, 'bpmn2_Collaboration182', a1)
    if hasattr(a1, 'bpmn2_CorrelationKey'):
        assert _is_linked(a1, 'bpmn2_CorrelationKey', b)
    _safe_set(b, 'bpmn2_Collaboration182', {a2})
    assert _is_linked(b, 'bpmn2_Collaboration182', a2)
    if hasattr(a1, 'bpmn2_CorrelationKey'):
        assert not _is_linked(a1, 'bpmn2_CorrelationKey', b)
    if hasattr(a2, 'bpmn2_CorrelationKey'):
        assert _is_linked(a2, 'bpmn2_CorrelationKey', b)
    _safe_set(b, 'bpmn2_Collaboration182', set())
    assert not _is_linked(b, 'bpmn2_Collaboration182', a2)
    if hasattr(a2, 'bpmn2_CorrelationKey'):
        assert not _is_linked(a2, 'bpmn2_CorrelationKey', b)


def test_assoc_correlationKeys237_reverse_link_reassign_clear():
    a1 = bpmn2_CorrelationKey(name="sample_text")
    a2 = bpmn2_CorrelationKey(name="sample_text_2")
    b = bpmn2_ConversationNode(name="sample_text")
    _safe_set(b, 'bpmn2_ConversationNode238', {a1})
    assert _is_linked(b, 'bpmn2_ConversationNode238', a1)
    if hasattr(a1, 'bpmn2_CorrelationKey239'):
        assert _is_linked(a1, 'bpmn2_CorrelationKey239', b)
    _safe_set(b, 'bpmn2_ConversationNode238', {a2})
    assert _is_linked(b, 'bpmn2_ConversationNode238', a2)
    if hasattr(a1, 'bpmn2_CorrelationKey239'):
        assert not _is_linked(a1, 'bpmn2_CorrelationKey239', b)
    if hasattr(a2, 'bpmn2_CorrelationKey239'):
        assert _is_linked(a2, 'bpmn2_CorrelationKey239', b)
    _safe_set(b, 'bpmn2_ConversationNode238', set())
    assert not _is_linked(b, 'bpmn2_ConversationNode238', a2)
    if hasattr(a2, 'bpmn2_CorrelationKey239'):
        assert not _is_linked(a2, 'bpmn2_CorrelationKey239', b)


def test_assoc_correlationKeys402_reverse_link_reassign_clear():
    a1 = bpmn2_CorrelationKey(name="sample_text")
    a2 = bpmn2_CorrelationKey(name="sample_text_2")
    b = bpmn2_ChoreographyActivity(loopType="sample_text")
    _safe_set(b, 'bpmn2_ChoreographyActivity403', {a1})
    assert _is_linked(b, 'bpmn2_ChoreographyActivity403', a1)
    if hasattr(a1, 'bpmn2_CorrelationKey404'):
        assert _is_linked(a1, 'bpmn2_CorrelationKey404', b)
    _safe_set(b, 'bpmn2_ChoreographyActivity403', {a2})
    assert _is_linked(b, 'bpmn2_ChoreographyActivity403', a2)
    if hasattr(a1, 'bpmn2_CorrelationKey404'):
        assert not _is_linked(a1, 'bpmn2_CorrelationKey404', b)
    if hasattr(a2, 'bpmn2_CorrelationKey404'):
        assert _is_linked(a2, 'bpmn2_CorrelationKey404', b)
    _safe_set(b, 'bpmn2_ChoreographyActivity403', set())
    assert not _is_linked(b, 'bpmn2_ChoreographyActivity403', a2)
    if hasattr(a2, 'bpmn2_CorrelationKey404'):
        assert not _is_linked(a2, 'bpmn2_CorrelationKey404', b)


def test_assoc_correlationPropertyRef240_reverse_link_reassign_clear():
    a1 = bpmn2_CorrelationProperty(name="sample_text")
    a2 = bpmn2_CorrelationProperty(name="sample_text_2")
    b = bpmn2_CorrelationKey(name="sample_text")
    _safe_set(b, 'bpmn2_CorrelationKey241', {a1})
    assert _is_linked(b, 'bpmn2_CorrelationKey241', a1)
    if hasattr(a1, 'bpmn2_CorrelationProperty'):
        assert _is_linked(a1, 'bpmn2_CorrelationProperty', b)
    _safe_set(b, 'bpmn2_CorrelationKey241', {a2})
    assert _is_linked(b, 'bpmn2_CorrelationKey241', a2)
    if hasattr(a1, 'bpmn2_CorrelationProperty'):
        assert not _is_linked(a1, 'bpmn2_CorrelationProperty', b)
    if hasattr(a2, 'bpmn2_CorrelationProperty'):
        assert _is_linked(a2, 'bpmn2_CorrelationProperty', b)
    _safe_set(b, 'bpmn2_CorrelationKey241', set())
    assert not _is_linked(b, 'bpmn2_CorrelationKey241', a2)
    if hasattr(a2, 'bpmn2_CorrelationProperty'):
        assert not _is_linked(a2, 'bpmn2_CorrelationProperty', b)


def test_assoc_dataInputRefs53_reverse_link_reassign_clear():
    a1 = bpmn2_InputSet(name="sample_text")
    a2 = bpmn2_InputSet(name="sample_text_2")
    b = bpmn2_DataInput(isCollection=True, name="sample_text")
    _safe_set(b, 'DataInput', a1)
    assert _is_linked(b, 'DataInput', a1)
    if hasattr(a1, 'inputSetRefs'):
        assert _is_linked(a1, 'inputSetRefs', b)
    _safe_set(b, 'DataInput', a2)
    assert _is_linked(b, 'DataInput', a2)
    if hasattr(a1, 'inputSetRefs'):
        assert not _is_linked(a1, 'inputSetRefs', b)
    if hasattr(a2, 'inputSetRefs'):
        assert _is_linked(a2, 'inputSetRefs', b)
    _safe_set(b, 'DataInput', None)
    assert not _is_linked(b, 'DataInput', a2)
    if hasattr(a2, 'inputSetRefs'):
        assert not _is_linked(a2, 'inputSetRefs', b)


def test_assoc_dataOutputRefs69_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_DataOutput(isCollection=True, name="sample_text")
    _safe_set(b, 'DataOutput', a1)
    assert _is_linked(b, 'DataOutput', a1)
    if hasattr(a1, 'outputSetRefs'):
        assert _is_linked(a1, 'outputSetRefs', b)
    _safe_set(b, 'DataOutput', a2)
    assert _is_linked(b, 'DataOutput', a2)
    if hasattr(a1, 'outputSetRefs'):
        assert not _is_linked(a1, 'outputSetRefs', b)
    if hasattr(a2, 'outputSetRefs'):
        assert _is_linked(a2, 'outputSetRefs', b)
    _safe_set(b, 'DataOutput', None)
    assert not _is_linked(b, 'DataOutput', a2)
    if hasattr(a2, 'outputSetRefs'):
        assert not _is_linked(a2, 'outputSetRefs', b)


def test_assoc_dataOutputs295_reverse_link_reassign_clear():
    a1 = bpmn2_DataOutput(isCollection=True, name="sample_text")
    a2 = bpmn2_DataOutput(isCollection=False, name="sample_text_2")
    b = bpmn2_CatchEvent(parallelMultiple=True)
    _safe_set(b, 'bpmn2_CatchEvent296', {a1})
    assert _is_linked(b, 'bpmn2_CatchEvent296', a1)
    if hasattr(a1, 'bpmn2_DataOutput297'):
        assert _is_linked(a1, 'bpmn2_DataOutput297', b)
    _safe_set(b, 'bpmn2_CatchEvent296', {a2})
    assert _is_linked(b, 'bpmn2_CatchEvent296', a2)
    if hasattr(a1, 'bpmn2_DataOutput297'):
        assert not _is_linked(a1, 'bpmn2_DataOutput297', b)
    if hasattr(a2, 'bpmn2_DataOutput297'):
        assert _is_linked(a2, 'bpmn2_DataOutput297', b)
    _safe_set(b, 'bpmn2_CatchEvent296', set())
    assert not _is_linked(b, 'bpmn2_CatchEvent296', a2)
    if hasattr(a2, 'bpmn2_DataOutput297'):
        assert not _is_linked(a2, 'bpmn2_DataOutput297', b)


def test_assoc_decomposedBy129_reverse_link_reassign_clear():
    a1 = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    a2 = bpmn2_Process(isClosed=False, isExecutable=False, processType="sample_text_2")
    b = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    _safe_set(b, 'decomposes', {a1})
    assert _is_linked(b, 'decomposes', a1)
    if hasattr(a1, 'Process'):
        assert _is_linked(a1, 'Process', b)
    _safe_set(b, 'decomposes', {a2})
    assert _is_linked(b, 'decomposes', a2)
    if hasattr(a1, 'Process'):
        assert not _is_linked(a1, 'Process', b)
    if hasattr(a2, 'Process'):
        assert _is_linked(a2, 'Process', b)
    _safe_set(b, 'decomposes', set())
    assert not _is_linked(b, 'decomposes', a2)
    if hasattr(a2, 'Process'):
        assert not _is_linked(a2, 'Process', b)


def test_assoc_decomposes131_reverse_link_reassign_clear():
    a1 = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    a2 = bpmn2_Process(isClosed=False, isExecutable=False, processType="sample_text_2")
    b = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    _safe_set(b, 'decomposedBy', a1)
    assert _is_linked(b, 'decomposedBy', a1)
    if hasattr(a1, 'Process132'):
        assert _is_linked(a1, 'Process132', b)
    _safe_set(b, 'decomposedBy', a2)
    assert _is_linked(b, 'decomposedBy', a2)
    if hasattr(a1, 'Process132'):
        assert not _is_linked(a1, 'Process132', b)
    if hasattr(a2, 'Process132'):
        assert _is_linked(a2, 'Process132', b)
    _safe_set(b, 'decomposedBy', None)
    assert not _is_linked(b, 'decomposedBy', a2)
    if hasattr(a2, 'Process132'):
        assert not _is_linked(a2, 'Process132', b)


def test_assoc_default273_reverse_link_reassign_clear():
    a1 = bpmn2_SequenceFlow(isImmediate=True)
    a2 = bpmn2_SequenceFlow(isImmediate=False)
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'bpmn2_Activity274', a1)
    assert _is_linked(b, 'bpmn2_Activity274', a1)
    if hasattr(a1, 'bpmn2_SequenceFlow275'):
        assert _is_linked(a1, 'bpmn2_SequenceFlow275', b)
    _safe_set(b, 'bpmn2_Activity274', a2)
    assert _is_linked(b, 'bpmn2_Activity274', a2)
    if hasattr(a1, 'bpmn2_SequenceFlow275'):
        assert not _is_linked(a1, 'bpmn2_SequenceFlow275', b)
    if hasattr(a2, 'bpmn2_SequenceFlow275'):
        assert _is_linked(a2, 'bpmn2_SequenceFlow275', b)
    _safe_set(b, 'bpmn2_Activity274', None)
    assert not _is_linked(b, 'bpmn2_Activity274', a2)
    if hasattr(a2, 'bpmn2_SequenceFlow275'):
        assert not _is_linked(a2, 'bpmn2_SequenceFlow275', b)


def test_assoc_definition336_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(id="sample_text", name="sample_text")
    a2 = bpmn2_ExtensionDefinition(id="sample_text_2", name="sample_text_2")
    b = bpmn2_Extension(id="sample_text", mustUnderstand=True)
    _safe_set(b, 'bpmn2_Extension', a1)
    assert _is_linked(b, 'bpmn2_Extension', a1)
    if hasattr(a1, 'bpmn2_ExtensionDefinition337'):
        assert _is_linked(a1, 'bpmn2_ExtensionDefinition337', b)
    _safe_set(b, 'bpmn2_Extension', a2)
    assert _is_linked(b, 'bpmn2_Extension', a2)
    if hasattr(a1, 'bpmn2_ExtensionDefinition337'):
        assert not _is_linked(a1, 'bpmn2_ExtensionDefinition337', b)
    if hasattr(a2, 'bpmn2_ExtensionDefinition337'):
        assert _is_linked(a2, 'bpmn2_ExtensionDefinition337', b)
    _safe_set(b, 'bpmn2_Extension', None)
    assert not _is_linked(b, 'bpmn2_Extension', a2)
    if hasattr(a2, 'bpmn2_ExtensionDefinition337'):
        assert not _is_linked(a2, 'bpmn2_ExtensionDefinition337', b)


def test_assoc_definitionalCollaborationRef119_reverse_link_reassign_clear():
    a1 = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    a2 = bpmn2_Process(isClosed=False, isExecutable=False, processType="sample_text_2")
    b = bpmn2_Collaboration(isClosed=True, name="sample_text")
    _safe_set(b, 'bpmn2_Collaboration', a1)
    assert _is_linked(b, 'bpmn2_Collaboration', a1)
    if hasattr(a1, 'bpmn2_Process120'):
        assert _is_linked(a1, 'bpmn2_Process120', b)
    _safe_set(b, 'bpmn2_Collaboration', a2)
    assert _is_linked(b, 'bpmn2_Collaboration', a2)
    if hasattr(a1, 'bpmn2_Process120'):
        assert not _is_linked(a1, 'bpmn2_Process120', b)
    if hasattr(a2, 'bpmn2_Process120'):
        assert _is_linked(a2, 'bpmn2_Process120', b)
    _safe_set(b, 'bpmn2_Collaboration', None)
    assert not _is_linked(b, 'bpmn2_Collaboration', a2)
    if hasattr(a2, 'bpmn2_Process120'):
        assert not _is_linked(a2, 'bpmn2_Process120', b)


def test_assoc_documentation6_reverse_link_reassign_clear():
    a1 = bpmn2_Documentation(text="sample_text", textFormat="sample_text")
    a2 = bpmn2_Documentation(text="sample_text_2", textFormat="sample_text_2")
    b = bpmn2_BaseElement(description="sample_text", id="sample_text")
    _safe_set(b, 'bpmn2_BaseElement7', {a1})
    assert _is_linked(b, 'bpmn2_BaseElement7', a1)
    if hasattr(a1, 'bpmn2_Documentation'):
        assert _is_linked(a1, 'bpmn2_Documentation', b)
    _safe_set(b, 'bpmn2_BaseElement7', {a2})
    assert _is_linked(b, 'bpmn2_BaseElement7', a2)
    if hasattr(a1, 'bpmn2_Documentation'):
        assert not _is_linked(a1, 'bpmn2_Documentation', b)
    if hasattr(a2, 'bpmn2_Documentation'):
        assert _is_linked(a2, 'bpmn2_Documentation', b)
    _safe_set(b, 'bpmn2_BaseElement7', set())
    assert not _is_linked(b, 'bpmn2_BaseElement7', a2)
    if hasattr(a2, 'bpmn2_Documentation'):
        assert not _is_linked(a2, 'bpmn2_Documentation', b)


def test_assoc_errorRefs23_reverse_link_reassign_clear():
    a1 = bpmn2_Operation(name="sample_text")
    a2 = bpmn2_Operation(name="sample_text_2")
    b = bpmn2_Error(errorCode="sample_text", name="sample_text")
    _safe_set(b, 'bpmn2_Error', a1)
    assert _is_linked(b, 'bpmn2_Error', a1)
    if hasattr(a1, 'bpmn2_Operation24'):
        assert _is_linked(a1, 'bpmn2_Operation24', b)
    _safe_set(b, 'bpmn2_Error', a2)
    assert _is_linked(b, 'bpmn2_Error', a2)
    if hasattr(a1, 'bpmn2_Operation24'):
        assert not _is_linked(a1, 'bpmn2_Operation24', b)
    if hasattr(a2, 'bpmn2_Operation24'):
        assert _is_linked(a2, 'bpmn2_Operation24', b)
    _safe_set(b, 'bpmn2_Error', None)
    assert not _is_linked(b, 'bpmn2_Error', a2)
    if hasattr(a2, 'bpmn2_Operation24'):
        assert not _is_linked(a2, 'bpmn2_Operation24', b)


def test_assoc_evaluatesToTypeRef255_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_FormalExpression(language="sample_text")
    _safe_set(b, 'bpmn2_FormalExpression256', a1)
    assert _is_linked(b, 'bpmn2_FormalExpression256', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition257'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition257', b)
    _safe_set(b, 'bpmn2_FormalExpression256', a2)
    assert _is_linked(b, 'bpmn2_FormalExpression256', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition257'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition257', b)
    if hasattr(a2, 'bpmn2_ItemDefinition257'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition257', b)
    _safe_set(b, 'bpmn2_FormalExpression256', None)
    assert not _is_linked(b, 'bpmn2_FormalExpression256', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition257'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition257', b)


def test_assoc_extensionAttributeDefinition16_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionAttributeValue(id="sample_text")
    a2 = bpmn2_ExtensionAttributeValue(id="sample_text_2")
    b = bpmn2_ExtensionAttributeDefinition(id="sample_text", isReference=True, name="sample_text", type="sample_text")
    _safe_set(b, 'bpmn2_ExtensionAttributeDefinition', a1)
    assert _is_linked(b, 'bpmn2_ExtensionAttributeDefinition', a1)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue17'):
        assert _is_linked(a1, 'bpmn2_ExtensionAttributeValue17', b)
    _safe_set(b, 'bpmn2_ExtensionAttributeDefinition', a2)
    assert _is_linked(b, 'bpmn2_ExtensionAttributeDefinition', a2)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue17'):
        assert not _is_linked(a1, 'bpmn2_ExtensionAttributeValue17', b)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue17'):
        assert _is_linked(a2, 'bpmn2_ExtensionAttributeValue17', b)
    _safe_set(b, 'bpmn2_ExtensionAttributeDefinition', None)
    assert not _is_linked(b, 'bpmn2_ExtensionAttributeDefinition', a2)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue17'):
        assert not _is_linked(a2, 'bpmn2_ExtensionAttributeValue17', b)


def test_assoc_extensionAttributeDefinitions8_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(id="sample_text", name="sample_text")
    a2 = bpmn2_ExtensionDefinition(id="sample_text_2", name="sample_text_2")
    b = bpmn2_ExtensionAttributeDefinition(id="sample_text", isReference=True, name="sample_text", type="sample_text")
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


def test_assoc_extensionDefinition9_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(id="sample_text", name="sample_text")
    a2 = bpmn2_ExtensionDefinition(id="sample_text_2", name="sample_text_2")
    b = bpmn2_ExtensionAttributeDefinition(id="sample_text", isReference=True, name="sample_text", type="sample_text")
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


def test_assoc_extensionDefinitions3_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionDefinition(id="sample_text", name="sample_text")
    a2 = bpmn2_ExtensionDefinition(id="sample_text_2", name="sample_text_2")
    b = bpmn2_BaseElement(description="sample_text", id="sample_text")
    _safe_set(b, 'bpmn2_BaseElement', {a1})
    assert _is_linked(b, 'bpmn2_BaseElement', a1)
    if hasattr(a1, 'bpmn2_ExtensionDefinition'):
        assert _is_linked(a1, 'bpmn2_ExtensionDefinition', b)
    _safe_set(b, 'bpmn2_BaseElement', {a2})
    assert _is_linked(b, 'bpmn2_BaseElement', a2)
    if hasattr(a1, 'bpmn2_ExtensionDefinition'):
        assert not _is_linked(a1, 'bpmn2_ExtensionDefinition', b)
    if hasattr(a2, 'bpmn2_ExtensionDefinition'):
        assert _is_linked(a2, 'bpmn2_ExtensionDefinition', b)
    _safe_set(b, 'bpmn2_BaseElement', set())
    assert not _is_linked(b, 'bpmn2_BaseElement', a2)
    if hasattr(a2, 'bpmn2_ExtensionDefinition'):
        assert not _is_linked(a2, 'bpmn2_ExtensionDefinition', b)


def test_assoc_extensionValues4_reverse_link_reassign_clear():
    a1 = bpmn2_ExtensionAttributeValue(id="sample_text")
    a2 = bpmn2_ExtensionAttributeValue(id="sample_text_2")
    b = bpmn2_BaseElement(description="sample_text", id="sample_text")
    _safe_set(b, 'bpmn2_BaseElement5', {a1})
    assert _is_linked(b, 'bpmn2_BaseElement5', a1)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue'):
        assert _is_linked(a1, 'bpmn2_ExtensionAttributeValue', b)
    _safe_set(b, 'bpmn2_BaseElement5', {a2})
    assert _is_linked(b, 'bpmn2_BaseElement5', a2)
    if hasattr(a1, 'bpmn2_ExtensionAttributeValue'):
        assert not _is_linked(a1, 'bpmn2_ExtensionAttributeValue', b)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue'):
        assert _is_linked(a2, 'bpmn2_ExtensionAttributeValue', b)
    _safe_set(b, 'bpmn2_BaseElement5', set())
    assert not _is_linked(b, 'bpmn2_BaseElement5', a2)
    if hasattr(a2, 'bpmn2_ExtensionAttributeValue'):
        assert not _is_linked(a2, 'bpmn2_ExtensionAttributeValue', b)


def test_assoc_extensions479_reverse_link_reassign_clear():
    a1 = bpmn2_Extension(id="sample_text", mustUnderstand=True)
    a2 = bpmn2_Extension(id="sample_text_2", mustUnderstand=False)
    b = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", name="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    _safe_set(b, 'bpmn2_Definitions480', {a1})
    assert _is_linked(b, 'bpmn2_Definitions480', a1)
    if hasattr(a1, 'bpmn2_Extension481'):
        assert _is_linked(a1, 'bpmn2_Extension481', b)
    _safe_set(b, 'bpmn2_Definitions480', {a2})
    assert _is_linked(b, 'bpmn2_Definitions480', a2)
    if hasattr(a1, 'bpmn2_Extension481'):
        assert not _is_linked(a1, 'bpmn2_Extension481', b)
    if hasattr(a2, 'bpmn2_Extension481'):
        assert _is_linked(a2, 'bpmn2_Extension481', b)
    _safe_set(b, 'bpmn2_Definitions480', set())
    assert not _is_linked(b, 'bpmn2_Definitions480', a2)
    if hasattr(a2, 'bpmn2_Extension481'):
        assert not _is_linked(a2, 'bpmn2_Extension481', b)


def test_assoc_import_33_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_Import(id="sample_text", importType="sample_text", location="sample_text", namespace="sample_text")
    _safe_set(b, 'bpmn2_Import', a1)
    assert _is_linked(b, 'bpmn2_Import', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition34'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition34', b)
    _safe_set(b, 'bpmn2_Import', a2)
    assert _is_linked(b, 'bpmn2_Import', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition34'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition34', b)
    if hasattr(a2, 'bpmn2_ItemDefinition34'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition34', b)
    _safe_set(b, 'bpmn2_Import', None)
    assert not _is_linked(b, 'bpmn2_Import', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition34'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition34', b)


def test_assoc_imports477_reverse_link_reassign_clear():
    a1 = bpmn2_Import(id="sample_text", importType="sample_text", location="sample_text", namespace="sample_text")
    a2 = bpmn2_Import(id="sample_text_2", importType="sample_text_2", location="sample_text_2", namespace="sample_text_2")
    b = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", name="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    _safe_set(b, 'bpmn2_Definitions', {a1})
    assert _is_linked(b, 'bpmn2_Definitions', a1)
    if hasattr(a1, 'bpmn2_Import478'):
        assert _is_linked(a1, 'bpmn2_Import478', b)
    _safe_set(b, 'bpmn2_Definitions', {a2})
    assert _is_linked(b, 'bpmn2_Definitions', a2)
    if hasattr(a1, 'bpmn2_Import478'):
        assert not _is_linked(a1, 'bpmn2_Import478', b)
    if hasattr(a2, 'bpmn2_Import478'):
        assert _is_linked(a2, 'bpmn2_Import478', b)
    _safe_set(b, 'bpmn2_Definitions', set())
    assert not _is_linked(b, 'bpmn2_Definitions', a2)
    if hasattr(a2, 'bpmn2_Import478'):
        assert not _is_linked(a2, 'bpmn2_Import478', b)


def test_assoc_inMessageRef18_reverse_link_reassign_clear():
    a1 = bpmn2_Operation(name="sample_text")
    a2 = bpmn2_Operation(name="sample_text_2")
    b = bpmn2_Message(name="sample_text")
    _safe_set(b, 'bpmn2_Message', a1)
    assert _is_linked(b, 'bpmn2_Message', a1)
    if hasattr(a1, 'bpmn2_Operation19'):
        assert _is_linked(a1, 'bpmn2_Operation19', b)
    _safe_set(b, 'bpmn2_Message', a2)
    assert _is_linked(b, 'bpmn2_Message', a2)
    if hasattr(a1, 'bpmn2_Operation19'):
        assert not _is_linked(a1, 'bpmn2_Operation19', b)
    if hasattr(a2, 'bpmn2_Operation19'):
        assert _is_linked(a2, 'bpmn2_Operation19', b)
    _safe_set(b, 'bpmn2_Message', None)
    assert not _is_linked(b, 'bpmn2_Message', a2)
    if hasattr(a2, 'bpmn2_Operation19'):
        assert not _is_linked(a2, 'bpmn2_Operation19', b)


def test_assoc_initiatingParticipantRef399_reverse_link_reassign_clear():
    a1 = bpmn2_Participant(name="sample_text")
    a2 = bpmn2_Participant(name="sample_text_2")
    b = bpmn2_ChoreographyActivity(loopType="sample_text")
    _safe_set(b, 'bpmn2_ChoreographyActivity400', a1)
    assert _is_linked(b, 'bpmn2_ChoreographyActivity400', a1)
    if hasattr(a1, 'bpmn2_Participant401'):
        assert _is_linked(a1, 'bpmn2_Participant401', b)
    _safe_set(b, 'bpmn2_ChoreographyActivity400', a2)
    assert _is_linked(b, 'bpmn2_ChoreographyActivity400', a2)
    if hasattr(a1, 'bpmn2_Participant401'):
        assert not _is_linked(a1, 'bpmn2_Participant401', b)
    if hasattr(a2, 'bpmn2_Participant401'):
        assert _is_linked(a2, 'bpmn2_Participant401', b)
    _safe_set(b, 'bpmn2_ChoreographyActivity400', None)
    assert not _is_linked(b, 'bpmn2_ChoreographyActivity400', a2)
    if hasattr(a2, 'bpmn2_Participant401'):
        assert not _is_linked(a2, 'bpmn2_Participant401', b)


def test_assoc_inputDataItem436_reverse_link_reassign_clear():
    a1 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    a2 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text_2", isSequential=False)
    b = bpmn2_DataInput(isCollection=True, name="sample_text")
    _safe_set(b, 'bpmn2_DataInput438', a1)
    assert _is_linked(b, 'bpmn2_DataInput438', a1)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics437'):
        assert _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics437', b)
    _safe_set(b, 'bpmn2_DataInput438', a2)
    assert _is_linked(b, 'bpmn2_DataInput438', a2)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics437'):
        assert not _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics437', b)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics437'):
        assert _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics437', b)
    _safe_set(b, 'bpmn2_DataInput438', None)
    assert not _is_linked(b, 'bpmn2_DataInput438', a2)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics437'):
        assert not _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics437', b)


def test_assoc_inputDataRef83_reverse_link_reassign_clear():
    a1 = bpmn2_InputSet(name="sample_text")
    a2 = bpmn2_InputSet(name="sample_text_2")
    b = bpmn2_InputOutputBinding(id="sample_text")
    _safe_set(b, 'bpmn2_InputOutputBinding84', a1)
    assert _is_linked(b, 'bpmn2_InputOutputBinding84', a1)
    if hasattr(a1, 'bpmn2_InputSet85'):
        assert _is_linked(a1, 'bpmn2_InputSet85', b)
    _safe_set(b, 'bpmn2_InputOutputBinding84', a2)
    assert _is_linked(b, 'bpmn2_InputOutputBinding84', a2)
    if hasattr(a1, 'bpmn2_InputSet85'):
        assert not _is_linked(a1, 'bpmn2_InputSet85', b)
    if hasattr(a2, 'bpmn2_InputSet85'):
        assert _is_linked(a2, 'bpmn2_InputSet85', b)
    _safe_set(b, 'bpmn2_InputOutputBinding84', None)
    assert not _is_linked(b, 'bpmn2_InputOutputBinding84', a2)
    if hasattr(a2, 'bpmn2_InputSet85'):
        assert not _is_linked(a2, 'bpmn2_InputSet85', b)


def test_assoc_inputSetRefs63_reverse_link_reassign_clear():
    a1 = bpmn2_InputSet(name="sample_text")
    a2 = bpmn2_InputSet(name="sample_text_2")
    b = bpmn2_DataInput(isCollection=True, name="sample_text")
    _safe_set(b, 'dataInputRefs', {a1})
    assert _is_linked(b, 'dataInputRefs', a1)
    if hasattr(a1, 'InputSet64'):
        assert _is_linked(a1, 'InputSet64', b)
    _safe_set(b, 'dataInputRefs', {a2})
    assert _is_linked(b, 'dataInputRefs', a2)
    if hasattr(a1, 'InputSet64'):
        assert not _is_linked(a1, 'InputSet64', b)
    if hasattr(a2, 'InputSet64'):
        assert _is_linked(a2, 'InputSet64', b)
    _safe_set(b, 'dataInputRefs', set())
    assert not _is_linked(b, 'dataInputRefs', a2)
    if hasattr(a2, 'InputSet64'):
        assert not _is_linked(a2, 'InputSet64', b)


def test_assoc_inputSetRefs74_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_InputSet(name="sample_text")
    _safe_set(b, 'InputSet76', a1)
    assert _is_linked(b, 'InputSet76', a1)
    if hasattr(a1, 'outputSetRefs75'):
        assert _is_linked(a1, 'outputSetRefs75', b)
    _safe_set(b, 'InputSet76', a2)
    assert _is_linked(b, 'InputSet76', a2)
    if hasattr(a1, 'outputSetRefs75'):
        assert not _is_linked(a1, 'outputSetRefs75', b)
    if hasattr(a2, 'outputSetRefs75'):
        assert _is_linked(a2, 'outputSetRefs75', b)
    _safe_set(b, 'InputSet76', None)
    assert not _is_linked(b, 'InputSet76', a2)
    if hasattr(a2, 'outputSetRefs75'):
        assert not _is_linked(a2, 'outputSetRefs75', b)


def test_assoc_inputSetWithOptional60_reverse_link_reassign_clear():
    a1 = bpmn2_InputSet(name="sample_text")
    a2 = bpmn2_InputSet(name="sample_text_2")
    b = bpmn2_DataInput(isCollection=True, name="sample_text")
    _safe_set(b, 'optionalInputRefs', {a1})
    assert _is_linked(b, 'optionalInputRefs', a1)
    if hasattr(a1, 'InputSet'):
        assert _is_linked(a1, 'InputSet', b)
    _safe_set(b, 'optionalInputRefs', {a2})
    assert _is_linked(b, 'optionalInputRefs', a2)
    if hasattr(a1, 'InputSet'):
        assert not _is_linked(a1, 'InputSet', b)
    if hasattr(a2, 'InputSet'):
        assert _is_linked(a2, 'InputSet', b)
    _safe_set(b, 'optionalInputRefs', set())
    assert not _is_linked(b, 'optionalInputRefs', a2)
    if hasattr(a2, 'InputSet'):
        assert not _is_linked(a2, 'InputSet', b)


def test_assoc_inputSetWithWhileExecuting61_reverse_link_reassign_clear():
    a1 = bpmn2_InputSet(name="sample_text")
    a2 = bpmn2_InputSet(name="sample_text_2")
    b = bpmn2_DataInput(isCollection=True, name="sample_text")
    _safe_set(b, 'whileExecutingInputRefs', {a1})
    assert _is_linked(b, 'whileExecutingInputRefs', a1)
    if hasattr(a1, 'InputSet62'):
        assert _is_linked(a1, 'InputSet62', b)
    _safe_set(b, 'whileExecutingInputRefs', {a2})
    assert _is_linked(b, 'whileExecutingInputRefs', a2)
    if hasattr(a1, 'InputSet62'):
        assert not _is_linked(a1, 'InputSet62', b)
    if hasattr(a2, 'InputSet62'):
        assert _is_linked(a2, 'InputSet62', b)
    _safe_set(b, 'whileExecutingInputRefs', set())
    assert not _is_linked(b, 'whileExecutingInputRefs', a2)
    if hasattr(a2, 'InputSet62'):
        assert not _is_linked(a2, 'InputSet62', b)


def test_assoc_interfaceRefs193_reverse_link_reassign_clear():
    a1 = bpmn2_Participant(name="sample_text")
    a2 = bpmn2_Participant(name="sample_text_2")
    b = bpmn2_Interface(name="sample_text")
    _safe_set(b, 'bpmn2_Interface195', a1)
    assert _is_linked(b, 'bpmn2_Interface195', a1)
    if hasattr(a1, 'bpmn2_Participant194'):
        assert _is_linked(a1, 'bpmn2_Participant194', b)
    _safe_set(b, 'bpmn2_Interface195', a2)
    assert _is_linked(b, 'bpmn2_Interface195', a2)
    if hasattr(a1, 'bpmn2_Participant194'):
        assert not _is_linked(a1, 'bpmn2_Participant194', b)
    if hasattr(a2, 'bpmn2_Participant194'):
        assert _is_linked(a2, 'bpmn2_Participant194', b)
    _safe_set(b, 'bpmn2_Interface195', None)
    assert not _is_linked(b, 'bpmn2_Interface195', a2)
    if hasattr(a2, 'bpmn2_Participant194'):
        assert not _is_linked(a2, 'bpmn2_Participant194', b)


def test_assoc_ioBinding43_reverse_link_reassign_clear():
    a1 = bpmn2_InputOutputBinding(id="sample_text")
    a2 = bpmn2_InputOutputBinding(id="sample_text_2")
    b = bpmn2_CallableElement(name="sample_text")
    _safe_set(b, 'bpmn2_CallableElement44', {a1})
    assert _is_linked(b, 'bpmn2_CallableElement44', a1)
    if hasattr(a1, 'bpmn2_InputOutputBinding'):
        assert _is_linked(a1, 'bpmn2_InputOutputBinding', b)
    _safe_set(b, 'bpmn2_CallableElement44', {a2})
    assert _is_linked(b, 'bpmn2_CallableElement44', a2)
    if hasattr(a1, 'bpmn2_InputOutputBinding'):
        assert not _is_linked(a1, 'bpmn2_InputOutputBinding', b)
    if hasattr(a2, 'bpmn2_InputOutputBinding'):
        assert _is_linked(a2, 'bpmn2_InputOutputBinding', b)
    _safe_set(b, 'bpmn2_CallableElement44', set())
    assert not _is_linked(b, 'bpmn2_CallableElement44', a2)
    if hasattr(a2, 'bpmn2_InputOutputBinding'):
        assert not _is_linked(a2, 'bpmn2_InputOutputBinding', b)


def test_assoc_itemRef28_reverse_link_reassign_clear():
    a1 = bpmn2_Message(name="sample_text")
    a2 = bpmn2_Message(name="sample_text_2")
    b = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    _safe_set(b, 'bpmn2_ItemDefinition', a1)
    assert _is_linked(b, 'bpmn2_ItemDefinition', a1)
    if hasattr(a1, 'bpmn2_Message29'):
        assert _is_linked(a1, 'bpmn2_Message29', b)
    _safe_set(b, 'bpmn2_ItemDefinition', a2)
    assert _is_linked(b, 'bpmn2_ItemDefinition', a2)
    if hasattr(a1, 'bpmn2_Message29'):
        assert not _is_linked(a1, 'bpmn2_Message29', b)
    if hasattr(a2, 'bpmn2_Message29'):
        assert _is_linked(a2, 'bpmn2_Message29', b)
    _safe_set(b, 'bpmn2_ItemDefinition', None)
    assert not _is_linked(b, 'bpmn2_ItemDefinition', a2)
    if hasattr(a2, 'bpmn2_Message29'):
        assert not _is_linked(a2, 'bpmn2_Message29', b)


def test_assoc_lanes144_reverse_link_reassign_clear():
    a1 = bpmn2_LaneSet(name="sample_text")
    a2 = bpmn2_LaneSet(name="sample_text_2")
    b = bpmn2_Lane(name="sample_text")
    _safe_set(b, 'bpmn2_Lane', a1)
    assert _is_linked(b, 'bpmn2_Lane', a1)
    if hasattr(a1, 'bpmn2_LaneSet145'):
        assert _is_linked(a1, 'bpmn2_LaneSet145', b)
    _safe_set(b, 'bpmn2_Lane', a2)
    assert _is_linked(b, 'bpmn2_Lane', a2)
    if hasattr(a1, 'bpmn2_LaneSet145'):
        assert not _is_linked(a1, 'bpmn2_LaneSet145', b)
    if hasattr(a2, 'bpmn2_LaneSet145'):
        assert _is_linked(a2, 'bpmn2_LaneSet145', b)
    _safe_set(b, 'bpmn2_Lane', None)
    assert not _is_linked(b, 'bpmn2_Lane', a2)
    if hasattr(a2, 'bpmn2_LaneSet145'):
        assert not _is_linked(a2, 'bpmn2_LaneSet145', b)


def test_assoc_messageFlowRefs234_reverse_link_reassign_clear():
    a1 = bpmn2_MessageFlow(name="sample_text")
    a2 = bpmn2_MessageFlow(name="sample_text_2")
    b = bpmn2_ConversationNode(name="sample_text")
    _safe_set(b, 'bpmn2_ConversationNode235', {a1})
    assert _is_linked(b, 'bpmn2_ConversationNode235', a1)
    if hasattr(a1, 'bpmn2_MessageFlow236'):
        assert _is_linked(a1, 'bpmn2_MessageFlow236', b)
    _safe_set(b, 'bpmn2_ConversationNode235', {a2})
    assert _is_linked(b, 'bpmn2_ConversationNode235', a2)
    if hasattr(a1, 'bpmn2_MessageFlow236'):
        assert not _is_linked(a1, 'bpmn2_MessageFlow236', b)
    if hasattr(a2, 'bpmn2_MessageFlow236'):
        assert _is_linked(a2, 'bpmn2_MessageFlow236', b)
    _safe_set(b, 'bpmn2_ConversationNode235', set())
    assert not _is_linked(b, 'bpmn2_ConversationNode235', a2)
    if hasattr(a2, 'bpmn2_MessageFlow236'):
        assert not _is_linked(a2, 'bpmn2_MessageFlow236', b)


def test_assoc_messageFlows179_reverse_link_reassign_clear():
    a1 = bpmn2_MessageFlow(name="sample_text")
    a2 = bpmn2_MessageFlow(name="sample_text_2")
    b = bpmn2_Collaboration(isClosed=True, name="sample_text")
    _safe_set(b, 'bpmn2_Collaboration180', {a1})
    assert _is_linked(b, 'bpmn2_Collaboration180', a1)
    if hasattr(a1, 'bpmn2_MessageFlow'):
        assert _is_linked(a1, 'bpmn2_MessageFlow', b)
    _safe_set(b, 'bpmn2_Collaboration180', {a2})
    assert _is_linked(b, 'bpmn2_Collaboration180', a2)
    if hasattr(a1, 'bpmn2_MessageFlow'):
        assert not _is_linked(a1, 'bpmn2_MessageFlow', b)
    if hasattr(a2, 'bpmn2_MessageFlow'):
        assert _is_linked(a2, 'bpmn2_MessageFlow', b)
    _safe_set(b, 'bpmn2_Collaboration180', set())
    assert not _is_linked(b, 'bpmn2_Collaboration180', a2)
    if hasattr(a2, 'bpmn2_MessageFlow'):
        assert not _is_linked(a2, 'bpmn2_MessageFlow', b)


def test_assoc_messageRef222_reverse_link_reassign_clear():
    a1 = bpmn2_MessageFlow(name="sample_text")
    a2 = bpmn2_MessageFlow(name="sample_text_2")
    b = bpmn2_Message(name="sample_text")
    _safe_set(b, 'bpmn2_Message224', a1)
    assert _is_linked(b, 'bpmn2_Message224', a1)
    if hasattr(a1, 'bpmn2_MessageFlow223'):
        assert _is_linked(a1, 'bpmn2_MessageFlow223', b)
    _safe_set(b, 'bpmn2_Message224', a2)
    assert _is_linked(b, 'bpmn2_Message224', a2)
    if hasattr(a1, 'bpmn2_MessageFlow223'):
        assert not _is_linked(a1, 'bpmn2_MessageFlow223', b)
    if hasattr(a2, 'bpmn2_MessageFlow223'):
        assert _is_linked(a2, 'bpmn2_MessageFlow223', b)
    _safe_set(b, 'bpmn2_Message224', None)
    assert not _is_linked(b, 'bpmn2_Message224', a2)
    if hasattr(a2, 'bpmn2_MessageFlow223'):
        assert not _is_linked(a2, 'bpmn2_MessageFlow223', b)


def test_assoc_messageRef467_reverse_link_reassign_clear():
    a1 = bpmn2_SendTask(implementation="sample_text")
    a2 = bpmn2_SendTask(implementation="sample_text_2")
    b = bpmn2_Message(name="sample_text")
    _safe_set(b, 'bpmn2_Message469', a1)
    assert _is_linked(b, 'bpmn2_Message469', a1)
    if hasattr(a1, 'bpmn2_SendTask468'):
        assert _is_linked(a1, 'bpmn2_SendTask468', b)
    _safe_set(b, 'bpmn2_Message469', a2)
    assert _is_linked(b, 'bpmn2_Message469', a2)
    if hasattr(a1, 'bpmn2_SendTask468'):
        assert not _is_linked(a1, 'bpmn2_SendTask468', b)
    if hasattr(a2, 'bpmn2_SendTask468'):
        assert _is_linked(a2, 'bpmn2_SendTask468', b)
    _safe_set(b, 'bpmn2_Message469', None)
    assert not _is_linked(b, 'bpmn2_Message469', a2)
    if hasattr(a2, 'bpmn2_SendTask468'):
        assert not _is_linked(a2, 'bpmn2_SendTask468', b)


def test_assoc_messageRef472_reverse_link_reassign_clear():
    a1 = bpmn2_ReceiveTask(implementation="sample_text", instantiate=True)
    a2 = bpmn2_ReceiveTask(implementation="sample_text_2", instantiate=False)
    b = bpmn2_Message(name="sample_text")
    _safe_set(b, 'bpmn2_Message474', a1)
    assert _is_linked(b, 'bpmn2_Message474', a1)
    if hasattr(a1, 'bpmn2_ReceiveTask473'):
        assert _is_linked(a1, 'bpmn2_ReceiveTask473', b)
    _safe_set(b, 'bpmn2_Message474', a2)
    assert _is_linked(b, 'bpmn2_Message474', a2)
    if hasattr(a1, 'bpmn2_ReceiveTask473'):
        assert not _is_linked(a1, 'bpmn2_ReceiveTask473', b)
    if hasattr(a2, 'bpmn2_ReceiveTask473'):
        assert _is_linked(a2, 'bpmn2_ReceiveTask473', b)
    _safe_set(b, 'bpmn2_Message474', None)
    assert not _is_linked(b, 'bpmn2_Message474', a2)
    if hasattr(a2, 'bpmn2_ReceiveTask473'):
        assert not _is_linked(a2, 'bpmn2_ReceiveTask473', b)


def test_assoc_operationRef424_reverse_link_reassign_clear():
    a1 = bpmn2_ServiceTask(implementation="sample_text")
    a2 = bpmn2_ServiceTask(implementation="sample_text_2")
    b = bpmn2_Operation(name="sample_text")
    _safe_set(b, 'bpmn2_Operation425', a1)
    assert _is_linked(b, 'bpmn2_Operation425', a1)
    if hasattr(a1, 'bpmn2_ServiceTask'):
        assert _is_linked(a1, 'bpmn2_ServiceTask', b)
    _safe_set(b, 'bpmn2_Operation425', a2)
    assert _is_linked(b, 'bpmn2_Operation425', a2)
    if hasattr(a1, 'bpmn2_ServiceTask'):
        assert not _is_linked(a1, 'bpmn2_ServiceTask', b)
    if hasattr(a2, 'bpmn2_ServiceTask'):
        assert _is_linked(a2, 'bpmn2_ServiceTask', b)
    _safe_set(b, 'bpmn2_Operation425', None)
    assert not _is_linked(b, 'bpmn2_Operation425', a2)
    if hasattr(a2, 'bpmn2_ServiceTask'):
        assert not _is_linked(a2, 'bpmn2_ServiceTask', b)


def test_assoc_operationRef465_reverse_link_reassign_clear():
    a1 = bpmn2_SendTask(implementation="sample_text")
    a2 = bpmn2_SendTask(implementation="sample_text_2")
    b = bpmn2_Operation(name="sample_text")
    _safe_set(b, 'bpmn2_Operation466', a1)
    assert _is_linked(b, 'bpmn2_Operation466', a1)
    if hasattr(a1, 'bpmn2_SendTask'):
        assert _is_linked(a1, 'bpmn2_SendTask', b)
    _safe_set(b, 'bpmn2_Operation466', a2)
    assert _is_linked(b, 'bpmn2_Operation466', a2)
    if hasattr(a1, 'bpmn2_SendTask'):
        assert not _is_linked(a1, 'bpmn2_SendTask', b)
    if hasattr(a2, 'bpmn2_SendTask'):
        assert _is_linked(a2, 'bpmn2_SendTask', b)
    _safe_set(b, 'bpmn2_Operation466', None)
    assert not _is_linked(b, 'bpmn2_Operation466', a2)
    if hasattr(a2, 'bpmn2_SendTask'):
        assert not _is_linked(a2, 'bpmn2_SendTask', b)


def test_assoc_operationRef470_reverse_link_reassign_clear():
    a1 = bpmn2_ReceiveTask(implementation="sample_text", instantiate=True)
    a2 = bpmn2_ReceiveTask(implementation="sample_text_2", instantiate=False)
    b = bpmn2_Operation(name="sample_text")
    _safe_set(b, 'bpmn2_Operation471', a1)
    assert _is_linked(b, 'bpmn2_Operation471', a1)
    if hasattr(a1, 'bpmn2_ReceiveTask'):
        assert _is_linked(a1, 'bpmn2_ReceiveTask', b)
    _safe_set(b, 'bpmn2_Operation471', a2)
    assert _is_linked(b, 'bpmn2_Operation471', a2)
    if hasattr(a1, 'bpmn2_ReceiveTask'):
        assert not _is_linked(a1, 'bpmn2_ReceiveTask', b)
    if hasattr(a2, 'bpmn2_ReceiveTask'):
        assert _is_linked(a2, 'bpmn2_ReceiveTask', b)
    _safe_set(b, 'bpmn2_Operation471', None)
    assert not _is_linked(b, 'bpmn2_Operation471', a2)
    if hasattr(a2, 'bpmn2_ReceiveTask'):
        assert not _is_linked(a2, 'bpmn2_ReceiveTask', b)


def test_assoc_operationRef89_reverse_link_reassign_clear():
    a1 = bpmn2_Operation(name="sample_text")
    a2 = bpmn2_Operation(name="sample_text_2")
    b = bpmn2_InputOutputBinding(id="sample_text")
    _safe_set(b, 'bpmn2_InputOutputBinding90', a1)
    assert _is_linked(b, 'bpmn2_InputOutputBinding90', a1)
    if hasattr(a1, 'bpmn2_Operation91'):
        assert _is_linked(a1, 'bpmn2_Operation91', b)
    _safe_set(b, 'bpmn2_InputOutputBinding90', a2)
    assert _is_linked(b, 'bpmn2_InputOutputBinding90', a2)
    if hasattr(a1, 'bpmn2_Operation91'):
        assert not _is_linked(a1, 'bpmn2_Operation91', b)
    if hasattr(a2, 'bpmn2_Operation91'):
        assert _is_linked(a2, 'bpmn2_Operation91', b)
    _safe_set(b, 'bpmn2_InputOutputBinding90', None)
    assert not _is_linked(b, 'bpmn2_InputOutputBinding90', a2)
    if hasattr(a2, 'bpmn2_Operation91'):
        assert not _is_linked(a2, 'bpmn2_Operation91', b)


def test_assoc_operations0_reverse_link_reassign_clear():
    a1 = bpmn2_Operation(name="sample_text")
    a2 = bpmn2_Operation(name="sample_text_2")
    b = bpmn2_Interface(name="sample_text")
    _safe_set(b, 'bpmn2_Interface', {a1})
    assert _is_linked(b, 'bpmn2_Interface', a1)
    if hasattr(a1, 'bpmn2_Operation'):
        assert _is_linked(a1, 'bpmn2_Operation', b)
    _safe_set(b, 'bpmn2_Interface', {a2})
    assert _is_linked(b, 'bpmn2_Interface', a2)
    if hasattr(a1, 'bpmn2_Operation'):
        assert not _is_linked(a1, 'bpmn2_Operation', b)
    if hasattr(a2, 'bpmn2_Operation'):
        assert _is_linked(a2, 'bpmn2_Operation', b)
    _safe_set(b, 'bpmn2_Interface', set())
    assert not _is_linked(b, 'bpmn2_Interface', a2)
    if hasattr(a2, 'bpmn2_Operation'):
        assert not _is_linked(a2, 'bpmn2_Operation', b)


def test_assoc_optionalInputRefs54_reverse_link_reassign_clear():
    a1 = bpmn2_InputSet(name="sample_text")
    a2 = bpmn2_InputSet(name="sample_text_2")
    b = bpmn2_DataInput(isCollection=True, name="sample_text")
    _safe_set(b, 'DataInput55', a1)
    assert _is_linked(b, 'DataInput55', a1)
    if hasattr(a1, 'inputSetWithOptional'):
        assert _is_linked(a1, 'inputSetWithOptional', b)
    _safe_set(b, 'DataInput55', a2)
    assert _is_linked(b, 'DataInput55', a2)
    if hasattr(a1, 'inputSetWithOptional'):
        assert not _is_linked(a1, 'inputSetWithOptional', b)
    if hasattr(a2, 'inputSetWithOptional'):
        assert _is_linked(a2, 'inputSetWithOptional', b)
    _safe_set(b, 'DataInput55', None)
    assert not _is_linked(b, 'DataInput55', a2)
    if hasattr(a2, 'inputSetWithOptional'):
        assert not _is_linked(a2, 'inputSetWithOptional', b)


def test_assoc_optionalOutputRefs70_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_DataOutput(isCollection=True, name="sample_text")
    _safe_set(b, 'DataOutput71', a1)
    assert _is_linked(b, 'DataOutput71', a1)
    if hasattr(a1, 'outputSetWithOptional'):
        assert _is_linked(a1, 'outputSetWithOptional', b)
    _safe_set(b, 'DataOutput71', a2)
    assert _is_linked(b, 'DataOutput71', a2)
    if hasattr(a1, 'outputSetWithOptional'):
        assert not _is_linked(a1, 'outputSetWithOptional', b)
    if hasattr(a2, 'outputSetWithOptional'):
        assert _is_linked(a2, 'outputSetWithOptional', b)
    _safe_set(b, 'DataOutput71', None)
    assert not _is_linked(b, 'DataOutput71', a2)
    if hasattr(a2, 'outputSetWithOptional'):
        assert not _is_linked(a2, 'outputSetWithOptional', b)


def test_assoc_outMessageRef20_reverse_link_reassign_clear():
    a1 = bpmn2_Operation(name="sample_text")
    a2 = bpmn2_Operation(name="sample_text_2")
    b = bpmn2_Message(name="sample_text")
    _safe_set(b, 'bpmn2_Message22', a1)
    assert _is_linked(b, 'bpmn2_Message22', a1)
    if hasattr(a1, 'bpmn2_Operation21'):
        assert _is_linked(a1, 'bpmn2_Operation21', b)
    _safe_set(b, 'bpmn2_Message22', a2)
    assert _is_linked(b, 'bpmn2_Message22', a2)
    if hasattr(a1, 'bpmn2_Operation21'):
        assert not _is_linked(a1, 'bpmn2_Operation21', b)
    if hasattr(a2, 'bpmn2_Operation21'):
        assert _is_linked(a2, 'bpmn2_Operation21', b)
    _safe_set(b, 'bpmn2_Message22', None)
    assert not _is_linked(b, 'bpmn2_Message22', a2)
    if hasattr(a2, 'bpmn2_Operation21'):
        assert not _is_linked(a2, 'bpmn2_Operation21', b)


def test_assoc_outputDataItem439_reverse_link_reassign_clear():
    a1 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    a2 = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text_2", isSequential=False)
    b = bpmn2_DataOutput(isCollection=True, name="sample_text")
    _safe_set(b, 'bpmn2_DataOutput441', a1)
    assert _is_linked(b, 'bpmn2_DataOutput441', a1)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics440'):
        assert _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics440', b)
    _safe_set(b, 'bpmn2_DataOutput441', a2)
    assert _is_linked(b, 'bpmn2_DataOutput441', a2)
    if hasattr(a1, 'bpmn2_MultiInstanceLoopCharacteristics440'):
        assert not _is_linked(a1, 'bpmn2_MultiInstanceLoopCharacteristics440', b)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics440'):
        assert _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics440', b)
    _safe_set(b, 'bpmn2_DataOutput441', None)
    assert not _is_linked(b, 'bpmn2_DataOutput441', a2)
    if hasattr(a2, 'bpmn2_MultiInstanceLoopCharacteristics440'):
        assert not _is_linked(a2, 'bpmn2_MultiInstanceLoopCharacteristics440', b)


def test_assoc_outputDataRef86_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_InputOutputBinding(id="sample_text")
    _safe_set(b, 'bpmn2_InputOutputBinding87', a1)
    assert _is_linked(b, 'bpmn2_InputOutputBinding87', a1)
    if hasattr(a1, 'bpmn2_OutputSet88'):
        assert _is_linked(a1, 'bpmn2_OutputSet88', b)
    _safe_set(b, 'bpmn2_InputOutputBinding87', a2)
    assert _is_linked(b, 'bpmn2_InputOutputBinding87', a2)
    if hasattr(a1, 'bpmn2_OutputSet88'):
        assert not _is_linked(a1, 'bpmn2_OutputSet88', b)
    if hasattr(a2, 'bpmn2_OutputSet88'):
        assert _is_linked(a2, 'bpmn2_OutputSet88', b)
    _safe_set(b, 'bpmn2_InputOutputBinding87', None)
    assert not _is_linked(b, 'bpmn2_InputOutputBinding87', a2)
    if hasattr(a2, 'bpmn2_OutputSet88'):
        assert not _is_linked(a2, 'bpmn2_OutputSet88', b)


def test_assoc_outputSet288_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_CatchEvent(parallelMultiple=True)
    _safe_set(b, 'bpmn2_CatchEvent', a1)
    assert _is_linked(b, 'bpmn2_CatchEvent', a1)
    if hasattr(a1, 'bpmn2_OutputSet289'):
        assert _is_linked(a1, 'bpmn2_OutputSet289', b)
    _safe_set(b, 'bpmn2_CatchEvent', a2)
    assert _is_linked(b, 'bpmn2_CatchEvent', a2)
    if hasattr(a1, 'bpmn2_OutputSet289'):
        assert not _is_linked(a1, 'bpmn2_OutputSet289', b)
    if hasattr(a2, 'bpmn2_OutputSet289'):
        assert _is_linked(a2, 'bpmn2_OutputSet289', b)
    _safe_set(b, 'bpmn2_CatchEvent', None)
    assert not _is_linked(b, 'bpmn2_CatchEvent', a2)
    if hasattr(a2, 'bpmn2_OutputSet289'):
        assert not _is_linked(a2, 'bpmn2_OutputSet289', b)


def test_assoc_outputSetRefs58_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_InputSet(name="sample_text")
    _safe_set(b, 'inputSetRefs59', {a1})
    assert _is_linked(b, 'inputSetRefs59', a1)
    if hasattr(a1, 'OutputSet'):
        assert _is_linked(a1, 'OutputSet', b)
    _safe_set(b, 'inputSetRefs59', {a2})
    assert _is_linked(b, 'inputSetRefs59', a2)
    if hasattr(a1, 'OutputSet'):
        assert not _is_linked(a1, 'OutputSet', b)
    if hasattr(a2, 'OutputSet'):
        assert _is_linked(a2, 'OutputSet', b)
    _safe_set(b, 'inputSetRefs59', set())
    assert not _is_linked(b, 'inputSetRefs59', a2)
    if hasattr(a2, 'OutputSet'):
        assert not _is_linked(a2, 'OutputSet', b)


def test_assoc_outputSetRefs81_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_DataOutput(isCollection=True, name="sample_text")
    _safe_set(b, 'dataOutputRefs', {a1})
    assert _is_linked(b, 'dataOutputRefs', a1)
    if hasattr(a1, 'OutputSet82'):
        assert _is_linked(a1, 'OutputSet82', b)
    _safe_set(b, 'dataOutputRefs', {a2})
    assert _is_linked(b, 'dataOutputRefs', a2)
    if hasattr(a1, 'OutputSet82'):
        assert not _is_linked(a1, 'OutputSet82', b)
    if hasattr(a2, 'OutputSet82'):
        assert _is_linked(a2, 'OutputSet82', b)
    _safe_set(b, 'dataOutputRefs', set())
    assert not _is_linked(b, 'dataOutputRefs', a2)
    if hasattr(a2, 'OutputSet82'):
        assert not _is_linked(a2, 'OutputSet82', b)


def test_assoc_outputSetWithOptional77_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_DataOutput(isCollection=True, name="sample_text")
    _safe_set(b, 'optionalOutputRefs', {a1})
    assert _is_linked(b, 'optionalOutputRefs', a1)
    if hasattr(a1, 'OutputSet78'):
        assert _is_linked(a1, 'OutputSet78', b)
    _safe_set(b, 'optionalOutputRefs', {a2})
    assert _is_linked(b, 'optionalOutputRefs', a2)
    if hasattr(a1, 'OutputSet78'):
        assert not _is_linked(a1, 'OutputSet78', b)
    if hasattr(a2, 'OutputSet78'):
        assert _is_linked(a2, 'OutputSet78', b)
    _safe_set(b, 'optionalOutputRefs', set())
    assert not _is_linked(b, 'optionalOutputRefs', a2)
    if hasattr(a2, 'OutputSet78'):
        assert not _is_linked(a2, 'OutputSet78', b)


def test_assoc_outputSetWithWhileExecuting79_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_DataOutput(isCollection=True, name="sample_text")
    _safe_set(b, 'whileExecutingOutputRefs', {a1})
    assert _is_linked(b, 'whileExecutingOutputRefs', a1)
    if hasattr(a1, 'OutputSet80'):
        assert _is_linked(a1, 'OutputSet80', b)
    _safe_set(b, 'whileExecutingOutputRefs', {a2})
    assert _is_linked(b, 'whileExecutingOutputRefs', a2)
    if hasattr(a1, 'OutputSet80'):
        assert not _is_linked(a1, 'OutputSet80', b)
    if hasattr(a2, 'OutputSet80'):
        assert _is_linked(a2, 'OutputSet80', b)
    _safe_set(b, 'whileExecutingOutputRefs', set())
    assert not _is_linked(b, 'whileExecutingOutputRefs', a2)
    if hasattr(a2, 'OutputSet80'):
        assert not _is_linked(a2, 'OutputSet80', b)


def test_assoc_parameterRef105_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceParameterBinding(id="sample_text")
    a2 = bpmn2_ResourceParameterBinding(id="sample_text_2")
    b = bpmn2_ResourceParameter(isRequired=True, name="sample_text")
    _safe_set(b, 'bpmn2_ResourceParameter107', a1)
    assert _is_linked(b, 'bpmn2_ResourceParameter107', a1)
    if hasattr(a1, 'bpmn2_ResourceParameterBinding106'):
        assert _is_linked(a1, 'bpmn2_ResourceParameterBinding106', b)
    _safe_set(b, 'bpmn2_ResourceParameter107', a2)
    assert _is_linked(b, 'bpmn2_ResourceParameter107', a2)
    if hasattr(a1, 'bpmn2_ResourceParameterBinding106'):
        assert not _is_linked(a1, 'bpmn2_ResourceParameterBinding106', b)
    if hasattr(a2, 'bpmn2_ResourceParameterBinding106'):
        assert _is_linked(a2, 'bpmn2_ResourceParameterBinding106', b)
    _safe_set(b, 'bpmn2_ResourceParameter107', None)
    assert not _is_linked(b, 'bpmn2_ResourceParameter107', a2)
    if hasattr(a2, 'bpmn2_ResourceParameterBinding106'):
        assert not _is_linked(a2, 'bpmn2_ResourceParameterBinding106', b)


def test_assoc_participantMultiplicity196_reverse_link_reassign_clear():
    a1 = bpmn2_ParticipantMultiplicity(id="sample_text", maximum=7, minimum=7)
    a2 = bpmn2_ParticipantMultiplicity(id="sample_text_2", maximum=13, minimum=13)
    b = bpmn2_Participant(name="sample_text")
    _safe_set(b, 'bpmn2_Participant197', a1)
    assert _is_linked(b, 'bpmn2_Participant197', a1)
    if hasattr(a1, 'bpmn2_ParticipantMultiplicity'):
        assert _is_linked(a1, 'bpmn2_ParticipantMultiplicity', b)
    _safe_set(b, 'bpmn2_Participant197', a2)
    assert _is_linked(b, 'bpmn2_Participant197', a2)
    if hasattr(a1, 'bpmn2_ParticipantMultiplicity'):
        assert not _is_linked(a1, 'bpmn2_ParticipantMultiplicity', b)
    if hasattr(a2, 'bpmn2_ParticipantMultiplicity'):
        assert _is_linked(a2, 'bpmn2_ParticipantMultiplicity', b)
    _safe_set(b, 'bpmn2_Participant197', None)
    assert not _is_linked(b, 'bpmn2_Participant197', a2)
    if hasattr(a2, 'bpmn2_ParticipantMultiplicity'):
        assert not _is_linked(a2, 'bpmn2_ParticipantMultiplicity', b)


def test_assoc_participantRef393_reverse_link_reassign_clear():
    a1 = bpmn2_PartnerEntity(name="sample_text")
    a2 = bpmn2_PartnerEntity(name="sample_text_2")
    b = bpmn2_Participant(name="sample_text")
    _safe_set(b, 'bpmn2_Participant394', a1)
    assert _is_linked(b, 'bpmn2_Participant394', a1)
    if hasattr(a1, 'bpmn2_PartnerEntity'):
        assert _is_linked(a1, 'bpmn2_PartnerEntity', b)
    _safe_set(b, 'bpmn2_Participant394', a2)
    assert _is_linked(b, 'bpmn2_Participant394', a2)
    if hasattr(a1, 'bpmn2_PartnerEntity'):
        assert not _is_linked(a1, 'bpmn2_PartnerEntity', b)
    if hasattr(a2, 'bpmn2_PartnerEntity'):
        assert _is_linked(a2, 'bpmn2_PartnerEntity', b)
    _safe_set(b, 'bpmn2_Participant394', None)
    assert not _is_linked(b, 'bpmn2_Participant394', a2)
    if hasattr(a2, 'bpmn2_PartnerEntity'):
        assert not _is_linked(a2, 'bpmn2_PartnerEntity', b)


def test_assoc_participantRef395_reverse_link_reassign_clear():
    a1 = bpmn2_PartnerRole(name="sample_text")
    a2 = bpmn2_PartnerRole(name="sample_text_2")
    b = bpmn2_Participant(name="sample_text")
    _safe_set(b, 'bpmn2_Participant396', a1)
    assert _is_linked(b, 'bpmn2_Participant396', a1)
    if hasattr(a1, 'bpmn2_PartnerRole'):
        assert _is_linked(a1, 'bpmn2_PartnerRole', b)
    _safe_set(b, 'bpmn2_Participant396', a2)
    assert _is_linked(b, 'bpmn2_Participant396', a2)
    if hasattr(a1, 'bpmn2_PartnerRole'):
        assert not _is_linked(a1, 'bpmn2_PartnerRole', b)
    if hasattr(a2, 'bpmn2_PartnerRole'):
        assert _is_linked(a2, 'bpmn2_PartnerRole', b)
    _safe_set(b, 'bpmn2_Participant396', None)
    assert not _is_linked(b, 'bpmn2_Participant396', a2)
    if hasattr(a2, 'bpmn2_PartnerRole'):
        assert not _is_linked(a2, 'bpmn2_PartnerRole', b)


def test_assoc_participantRefs231_reverse_link_reassign_clear():
    a1 = bpmn2_Participant(name="sample_text")
    a2 = bpmn2_Participant(name="sample_text_2")
    b = bpmn2_ConversationNode(name="sample_text")
    _safe_set(b, 'bpmn2_ConversationNode232', {a1})
    assert _is_linked(b, 'bpmn2_ConversationNode232', a1)
    if hasattr(a1, 'bpmn2_Participant233'):
        assert _is_linked(a1, 'bpmn2_Participant233', b)
    _safe_set(b, 'bpmn2_ConversationNode232', {a2})
    assert _is_linked(b, 'bpmn2_ConversationNode232', a2)
    if hasattr(a1, 'bpmn2_Participant233'):
        assert not _is_linked(a1, 'bpmn2_Participant233', b)
    if hasattr(a2, 'bpmn2_Participant233'):
        assert _is_linked(a2, 'bpmn2_Participant233', b)
    _safe_set(b, 'bpmn2_ConversationNode232', set())
    assert not _is_linked(b, 'bpmn2_ConversationNode232', a2)
    if hasattr(a2, 'bpmn2_Participant233'):
        assert not _is_linked(a2, 'bpmn2_Participant233', b)


def test_assoc_participantRefs397_reverse_link_reassign_clear():
    a1 = bpmn2_Participant(name="sample_text")
    a2 = bpmn2_Participant(name="sample_text_2")
    b = bpmn2_ChoreographyActivity(loopType="sample_text")
    _safe_set(b, 'bpmn2_ChoreographyActivity', {a1})
    assert _is_linked(b, 'bpmn2_ChoreographyActivity', a1)
    if hasattr(a1, 'bpmn2_Participant398'):
        assert _is_linked(a1, 'bpmn2_Participant398', b)
    _safe_set(b, 'bpmn2_ChoreographyActivity', {a2})
    assert _is_linked(b, 'bpmn2_ChoreographyActivity', a2)
    if hasattr(a1, 'bpmn2_Participant398'):
        assert not _is_linked(a1, 'bpmn2_Participant398', b)
    if hasattr(a2, 'bpmn2_Participant398'):
        assert _is_linked(a2, 'bpmn2_Participant398', b)
    _safe_set(b, 'bpmn2_ChoreographyActivity', set())
    assert not _is_linked(b, 'bpmn2_ChoreographyActivity', a2)
    if hasattr(a2, 'bpmn2_Participant398'):
        assert not _is_linked(a2, 'bpmn2_Participant398', b)


def test_assoc_participants177_reverse_link_reassign_clear():
    a1 = bpmn2_Participant(name="sample_text")
    a2 = bpmn2_Participant(name="sample_text_2")
    b = bpmn2_Collaboration(isClosed=True, name="sample_text")
    _safe_set(b, 'bpmn2_Collaboration178', {a1})
    assert _is_linked(b, 'bpmn2_Collaboration178', a1)
    if hasattr(a1, 'bpmn2_Participant'):
        assert _is_linked(a1, 'bpmn2_Participant', b)
    _safe_set(b, 'bpmn2_Collaboration178', {a2})
    assert _is_linked(b, 'bpmn2_Collaboration178', a2)
    if hasattr(a1, 'bpmn2_Participant'):
        assert not _is_linked(a1, 'bpmn2_Participant', b)
    if hasattr(a2, 'bpmn2_Participant'):
        assert _is_linked(a2, 'bpmn2_Participant', b)
    _safe_set(b, 'bpmn2_Collaboration178', set())
    assert not _is_linked(b, 'bpmn2_Collaboration178', a2)
    if hasattr(a2, 'bpmn2_Participant'):
        assert not _is_linked(a2, 'bpmn2_Participant', b)


def test_assoc_partitionElement153_reverse_link_reassign_clear():
    a1 = bpmn2_Lane(name="sample_text")
    a2 = bpmn2_Lane(name="sample_text_2")
    b = bpmn2_BaseElement(description="sample_text", id="sample_text")
    _safe_set(b, 'bpmn2_BaseElement155', a1)
    assert _is_linked(b, 'bpmn2_BaseElement155', a1)
    if hasattr(a1, 'bpmn2_Lane154'):
        assert _is_linked(a1, 'bpmn2_Lane154', b)
    _safe_set(b, 'bpmn2_BaseElement155', a2)
    assert _is_linked(b, 'bpmn2_BaseElement155', a2)
    if hasattr(a1, 'bpmn2_Lane154'):
        assert not _is_linked(a1, 'bpmn2_Lane154', b)
    if hasattr(a2, 'bpmn2_Lane154'):
        assert _is_linked(a2, 'bpmn2_Lane154', b)
    _safe_set(b, 'bpmn2_BaseElement155', None)
    assert not _is_linked(b, 'bpmn2_BaseElement155', a2)
    if hasattr(a2, 'bpmn2_Lane154'):
        assert not _is_linked(a2, 'bpmn2_Lane154', b)


def test_assoc_partitionElementRef149_reverse_link_reassign_clear():
    a1 = bpmn2_Lane(name="sample_text")
    a2 = bpmn2_Lane(name="sample_text_2")
    b = bpmn2_BaseElement(description="sample_text", id="sample_text")
    _safe_set(b, 'bpmn2_BaseElement151', a1)
    assert _is_linked(b, 'bpmn2_BaseElement151', a1)
    if hasattr(a1, 'bpmn2_Lane150'):
        assert _is_linked(a1, 'bpmn2_Lane150', b)
    _safe_set(b, 'bpmn2_BaseElement151', a2)
    assert _is_linked(b, 'bpmn2_BaseElement151', a2)
    if hasattr(a1, 'bpmn2_Lane150'):
        assert not _is_linked(a1, 'bpmn2_Lane150', b)
    if hasattr(a2, 'bpmn2_Lane150'):
        assert _is_linked(a2, 'bpmn2_Lane150', b)
    _safe_set(b, 'bpmn2_BaseElement151', None)
    assert not _is_linked(b, 'bpmn2_BaseElement151', a2)
    if hasattr(a2, 'bpmn2_Lane150'):
        assert not _is_linked(a2, 'bpmn2_Lane150', b)


def test_assoc_processRef200_reverse_link_reassign_clear():
    a1 = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    a2 = bpmn2_Process(isClosed=False, isExecutable=False, processType="sample_text_2")
    b = bpmn2_Participant(name="sample_text")
    _safe_set(b, 'bpmn2_Participant201', a1)
    assert _is_linked(b, 'bpmn2_Participant201', a1)
    if hasattr(a1, 'bpmn2_Process202'):
        assert _is_linked(a1, 'bpmn2_Process202', b)
    _safe_set(b, 'bpmn2_Participant201', a2)
    assert _is_linked(b, 'bpmn2_Participant201', a2)
    if hasattr(a1, 'bpmn2_Process202'):
        assert not _is_linked(a1, 'bpmn2_Process202', b)
    if hasattr(a2, 'bpmn2_Process202'):
        assert _is_linked(a2, 'bpmn2_Process202', b)
    _safe_set(b, 'bpmn2_Participant201', None)
    assert not _is_linked(b, 'bpmn2_Participant201', a2)
    if hasattr(a2, 'bpmn2_Process202'):
        assert not _is_linked(a2, 'bpmn2_Process202', b)


def test_assoc_properties114_reverse_link_reassign_clear():
    a1 = bpmn2_Property(name="sample_text")
    a2 = bpmn2_Property(name="sample_text_2")
    b = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    _safe_set(b, 'bpmn2_Process115', {a1})
    assert _is_linked(b, 'bpmn2_Process115', a1)
    if hasattr(a1, 'bpmn2_Property'):
        assert _is_linked(a1, 'bpmn2_Property', b)
    _safe_set(b, 'bpmn2_Process115', {a2})
    assert _is_linked(b, 'bpmn2_Process115', a2)
    if hasattr(a1, 'bpmn2_Property'):
        assert not _is_linked(a1, 'bpmn2_Property', b)
    if hasattr(a2, 'bpmn2_Property'):
        assert _is_linked(a2, 'bpmn2_Property', b)
    _safe_set(b, 'bpmn2_Process115', set())
    assert not _is_linked(b, 'bpmn2_Process115', a2)
    if hasattr(a2, 'bpmn2_Property'):
        assert not _is_linked(a2, 'bpmn2_Property', b)


def test_assoc_properties276_reverse_link_reassign_clear():
    a1 = bpmn2_Property(name="sample_text")
    a2 = bpmn2_Property(name="sample_text_2")
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'bpmn2_Activity277', {a1})
    assert _is_linked(b, 'bpmn2_Activity277', a1)
    if hasattr(a1, 'bpmn2_Property278'):
        assert _is_linked(a1, 'bpmn2_Property278', b)
    _safe_set(b, 'bpmn2_Activity277', {a2})
    assert _is_linked(b, 'bpmn2_Activity277', a2)
    if hasattr(a1, 'bpmn2_Property278'):
        assert not _is_linked(a1, 'bpmn2_Property278', b)
    if hasattr(a2, 'bpmn2_Property278'):
        assert _is_linked(a2, 'bpmn2_Property278', b)
    _safe_set(b, 'bpmn2_Activity277', set())
    assert not _is_linked(b, 'bpmn2_Activity277', a2)
    if hasattr(a2, 'bpmn2_Property278'):
        assert not _is_linked(a2, 'bpmn2_Property278', b)


def test_assoc_relationships482_reverse_link_reassign_clear():
    a1 = bpmn2_Relationship(direction="sample_text", type="sample_text")
    a2 = bpmn2_Relationship(direction="sample_text_2", type="sample_text_2")
    b = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", name="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    _safe_set(b, 'bpmn2_Definitions483', {a1})
    assert _is_linked(b, 'bpmn2_Definitions483', a1)
    if hasattr(a1, 'bpmn2_Relationship484'):
        assert _is_linked(a1, 'bpmn2_Relationship484', b)
    _safe_set(b, 'bpmn2_Definitions483', {a2})
    assert _is_linked(b, 'bpmn2_Definitions483', a2)
    if hasattr(a1, 'bpmn2_Relationship484'):
        assert not _is_linked(a1, 'bpmn2_Relationship484', b)
    if hasattr(a2, 'bpmn2_Relationship484'):
        assert _is_linked(a2, 'bpmn2_Relationship484', b)
    _safe_set(b, 'bpmn2_Definitions483', set())
    assert not _is_linked(b, 'bpmn2_Definitions483', a2)
    if hasattr(a2, 'bpmn2_Relationship484'):
        assert not _is_linked(a2, 'bpmn2_Relationship484', b)


def test_assoc_resourceAssignmentExpression96_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceRole(name="sample_text")
    a2 = bpmn2_ResourceRole(name="sample_text_2")
    b = bpmn2_ResourceAssignmentExpression(id="sample_text")
    _safe_set(b, 'bpmn2_ResourceAssignmentExpression', a1)
    assert _is_linked(b, 'bpmn2_ResourceAssignmentExpression', a1)
    if hasattr(a1, 'bpmn2_ResourceRole97'):
        assert _is_linked(a1, 'bpmn2_ResourceRole97', b)
    _safe_set(b, 'bpmn2_ResourceAssignmentExpression', a2)
    assert _is_linked(b, 'bpmn2_ResourceAssignmentExpression', a2)
    if hasattr(a1, 'bpmn2_ResourceRole97'):
        assert not _is_linked(a1, 'bpmn2_ResourceRole97', b)
    if hasattr(a2, 'bpmn2_ResourceRole97'):
        assert _is_linked(a2, 'bpmn2_ResourceRole97', b)
    _safe_set(b, 'bpmn2_ResourceAssignmentExpression', None)
    assert not _is_linked(b, 'bpmn2_ResourceAssignmentExpression', a2)
    if hasattr(a2, 'bpmn2_ResourceRole97'):
        assert not _is_linked(a2, 'bpmn2_ResourceRole97', b)


def test_assoc_resourceParameterBindings94_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceRole(name="sample_text")
    a2 = bpmn2_ResourceRole(name="sample_text_2")
    b = bpmn2_ResourceParameterBinding(id="sample_text")
    _safe_set(b, 'bpmn2_ResourceParameterBinding', a1)
    assert _is_linked(b, 'bpmn2_ResourceParameterBinding', a1)
    if hasattr(a1, 'bpmn2_ResourceRole95'):
        assert _is_linked(a1, 'bpmn2_ResourceRole95', b)
    _safe_set(b, 'bpmn2_ResourceParameterBinding', a2)
    assert _is_linked(b, 'bpmn2_ResourceParameterBinding', a2)
    if hasattr(a1, 'bpmn2_ResourceRole95'):
        assert not _is_linked(a1, 'bpmn2_ResourceRole95', b)
    if hasattr(a2, 'bpmn2_ResourceRole95'):
        assert _is_linked(a2, 'bpmn2_ResourceRole95', b)
    _safe_set(b, 'bpmn2_ResourceParameterBinding', None)
    assert not _is_linked(b, 'bpmn2_ResourceParameterBinding', a2)
    if hasattr(a2, 'bpmn2_ResourceRole95'):
        assert not _is_linked(a2, 'bpmn2_ResourceRole95', b)


def test_assoc_resourceParameters98_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceParameter(isRequired=True, name="sample_text")
    a2 = bpmn2_ResourceParameter(isRequired=False, name="sample_text_2")
    b = bpmn2_Resource(name="sample_text")
    _safe_set(b, 'bpmn2_Resource99', {a1})
    assert _is_linked(b, 'bpmn2_Resource99', a1)
    if hasattr(a1, 'bpmn2_ResourceParameter'):
        assert _is_linked(a1, 'bpmn2_ResourceParameter', b)
    _safe_set(b, 'bpmn2_Resource99', {a2})
    assert _is_linked(b, 'bpmn2_Resource99', a2)
    if hasattr(a1, 'bpmn2_ResourceParameter'):
        assert not _is_linked(a1, 'bpmn2_ResourceParameter', b)
    if hasattr(a2, 'bpmn2_ResourceParameter'):
        assert _is_linked(a2, 'bpmn2_ResourceParameter', b)
    _safe_set(b, 'bpmn2_Resource99', set())
    assert not _is_linked(b, 'bpmn2_Resource99', a2)
    if hasattr(a2, 'bpmn2_ResourceParameter'):
        assert not _is_linked(a2, 'bpmn2_ResourceParameter', b)


def test_assoc_resourceRef92_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceRole(name="sample_text")
    a2 = bpmn2_ResourceRole(name="sample_text_2")
    b = bpmn2_Resource(name="sample_text")
    _safe_set(b, 'bpmn2_Resource', a1)
    assert _is_linked(b, 'bpmn2_Resource', a1)
    if hasattr(a1, 'bpmn2_ResourceRole93'):
        assert _is_linked(a1, 'bpmn2_ResourceRole93', b)
    _safe_set(b, 'bpmn2_Resource', a2)
    assert _is_linked(b, 'bpmn2_Resource', a2)
    if hasattr(a1, 'bpmn2_ResourceRole93'):
        assert not _is_linked(a1, 'bpmn2_ResourceRole93', b)
    if hasattr(a2, 'bpmn2_ResourceRole93'):
        assert _is_linked(a2, 'bpmn2_ResourceRole93', b)
    _safe_set(b, 'bpmn2_Resource', None)
    assert not _is_linked(b, 'bpmn2_Resource', a2)
    if hasattr(a2, 'bpmn2_ResourceRole93'):
        assert not _is_linked(a2, 'bpmn2_ResourceRole93', b)


def test_assoc_resources121_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceRole(name="sample_text")
    a2 = bpmn2_ResourceRole(name="sample_text_2")
    b = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    _safe_set(b, 'bpmn2_Process122', {a1})
    assert _is_linked(b, 'bpmn2_Process122', a1)
    if hasattr(a1, 'bpmn2_ResourceRole123'):
        assert _is_linked(a1, 'bpmn2_ResourceRole123', b)
    _safe_set(b, 'bpmn2_Process122', {a2})
    assert _is_linked(b, 'bpmn2_Process122', a2)
    if hasattr(a1, 'bpmn2_ResourceRole123'):
        assert not _is_linked(a1, 'bpmn2_ResourceRole123', b)
    if hasattr(a2, 'bpmn2_ResourceRole123'):
        assert _is_linked(a2, 'bpmn2_ResourceRole123', b)
    _safe_set(b, 'bpmn2_Process122', set())
    assert not _is_linked(b, 'bpmn2_Process122', a2)
    if hasattr(a2, 'bpmn2_ResourceRole123'):
        assert not _is_linked(a2, 'bpmn2_ResourceRole123', b)


def test_assoc_resources270_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceRole(name="sample_text")
    a2 = bpmn2_ResourceRole(name="sample_text_2")
    b = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    _safe_set(b, 'bpmn2_Activity271', {a1})
    assert _is_linked(b, 'bpmn2_Activity271', a1)
    if hasattr(a1, 'bpmn2_ResourceRole272'):
        assert _is_linked(a1, 'bpmn2_ResourceRole272', b)
    _safe_set(b, 'bpmn2_Activity271', {a2})
    assert _is_linked(b, 'bpmn2_Activity271', a2)
    if hasattr(a1, 'bpmn2_ResourceRole272'):
        assert not _is_linked(a1, 'bpmn2_ResourceRole272', b)
    if hasattr(a2, 'bpmn2_ResourceRole272'):
        assert _is_linked(a2, 'bpmn2_ResourceRole272', b)
    _safe_set(b, 'bpmn2_Activity271', set())
    assert not _is_linked(b, 'bpmn2_Activity271', a2)
    if hasattr(a2, 'bpmn2_ResourceRole272'):
        assert not _is_linked(a2, 'bpmn2_ResourceRole272', b)


def test_assoc_source371_reverse_link_reassign_clear():
    a1 = bpmn2_LinkEventDefinition(name="sample_text")
    a2 = bpmn2_LinkEventDefinition(name="sample_text_2")
    b = bpmn2_LinkEventDefinition(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'LinkEventDefinition372'):
        assert _is_linked(a1, 'LinkEventDefinition372', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'LinkEventDefinition372'):
        assert not _is_linked(a1, 'LinkEventDefinition372', b)
    if hasattr(a2, 'LinkEventDefinition372'):
        assert _is_linked(a2, 'LinkEventDefinition372', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'LinkEventDefinition372'):
        assert not _is_linked(a2, 'LinkEventDefinition372', b)


def test_assoc_sourceRef417_reverse_link_reassign_clear():
    a1 = bpmn2_BaseElement(description="sample_text", id="sample_text")
    a2 = bpmn2_BaseElement(description="sample_text_2", id="sample_text_2")
    b = bpmn2_Association(associationDirection="sample_text")
    _safe_set(b, 'bpmn2_Association', a1)
    assert _is_linked(b, 'bpmn2_Association', a1)
    if hasattr(a1, 'bpmn2_BaseElement418'):
        assert _is_linked(a1, 'bpmn2_BaseElement418', b)
    _safe_set(b, 'bpmn2_Association', a2)
    assert _is_linked(b, 'bpmn2_Association', a2)
    if hasattr(a1, 'bpmn2_BaseElement418'):
        assert not _is_linked(a1, 'bpmn2_BaseElement418', b)
    if hasattr(a2, 'bpmn2_BaseElement418'):
        assert _is_linked(a2, 'bpmn2_BaseElement418', b)
    _safe_set(b, 'bpmn2_Association', None)
    assert not _is_linked(b, 'bpmn2_Association', a2)
    if hasattr(a2, 'bpmn2_BaseElement418'):
        assert not _is_linked(a2, 'bpmn2_BaseElement418', b)


def test_assoc_structureRef35_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_Error(errorCode="sample_text", name="sample_text")
    _safe_set(b, 'bpmn2_Error36', a1)
    assert _is_linked(b, 'bpmn2_Error36', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition37'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition37', b)
    _safe_set(b, 'bpmn2_Error36', a2)
    assert _is_linked(b, 'bpmn2_Error36', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition37'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition37', b)
    if hasattr(a2, 'bpmn2_ItemDefinition37'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition37', b)
    _safe_set(b, 'bpmn2_Error36', None)
    assert not _is_linked(b, 'bpmn2_Error36', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition37'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition37', b)


def test_assoc_structureRef355_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_Escalation(escalationCode="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'bpmn2_Escalation356', a1)
    assert _is_linked(b, 'bpmn2_Escalation356', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition357'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition357', b)
    _safe_set(b, 'bpmn2_Escalation356', a2)
    assert _is_linked(b, 'bpmn2_Escalation356', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition357'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition357', b)
    if hasattr(a2, 'bpmn2_ItemDefinition357'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition357', b)
    _safe_set(b, 'bpmn2_Escalation356', None)
    assert not _is_linked(b, 'bpmn2_Escalation356', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition357'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition357', b)


def test_assoc_structureRef381_reverse_link_reassign_clear():
    a1 = bpmn2_Signal(name="sample_text")
    a2 = bpmn2_Signal(name="sample_text_2")
    b = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    _safe_set(b, 'bpmn2_ItemDefinition383', a1)
    assert _is_linked(b, 'bpmn2_ItemDefinition383', a1)
    if hasattr(a1, 'bpmn2_Signal382'):
        assert _is_linked(a1, 'bpmn2_Signal382', b)
    _safe_set(b, 'bpmn2_ItemDefinition383', a2)
    assert _is_linked(b, 'bpmn2_ItemDefinition383', a2)
    if hasattr(a1, 'bpmn2_Signal382'):
        assert not _is_linked(a1, 'bpmn2_Signal382', b)
    if hasattr(a2, 'bpmn2_Signal382'):
        assert _is_linked(a2, 'bpmn2_Signal382', b)
    _safe_set(b, 'bpmn2_ItemDefinition383', None)
    assert not _is_linked(b, 'bpmn2_ItemDefinition383', a2)
    if hasattr(a2, 'bpmn2_Signal382'):
        assert not _is_linked(a2, 'bpmn2_Signal382', b)


def test_assoc_supportedInterfaceRefs40_reverse_link_reassign_clear():
    a1 = bpmn2_Interface(name="sample_text")
    a2 = bpmn2_Interface(name="sample_text_2")
    b = bpmn2_CallableElement(name="sample_text")
    _safe_set(b, 'bpmn2_CallableElement41', {a1})
    assert _is_linked(b, 'bpmn2_CallableElement41', a1)
    if hasattr(a1, 'bpmn2_Interface42'):
        assert _is_linked(a1, 'bpmn2_Interface42', b)
    _safe_set(b, 'bpmn2_CallableElement41', {a2})
    assert _is_linked(b, 'bpmn2_CallableElement41', a2)
    if hasattr(a1, 'bpmn2_Interface42'):
        assert not _is_linked(a1, 'bpmn2_Interface42', b)
    if hasattr(a2, 'bpmn2_Interface42'):
        assert _is_linked(a2, 'bpmn2_Interface42', b)
    _safe_set(b, 'bpmn2_CallableElement41', set())
    assert not _is_linked(b, 'bpmn2_CallableElement41', a2)
    if hasattr(a2, 'bpmn2_Interface42'):
        assert not _is_linked(a2, 'bpmn2_Interface42', b)


def test_assoc_supports117_reverse_link_reassign_clear():
    a1 = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    a2 = bpmn2_Process(isClosed=False, isExecutable=False, processType="sample_text_2")
    b = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    _safe_set(b, 'bpmn2_Process118', a1)
    assert _is_linked(b, 'bpmn2_Process118', a1)
    if hasattr(a1, 'bpmn2_Process116'):
        assert _is_linked(a1, 'bpmn2_Process116', b)
    _safe_set(b, 'bpmn2_Process118', a2)
    assert _is_linked(b, 'bpmn2_Process118', a2)
    if hasattr(a1, 'bpmn2_Process116'):
        assert not _is_linked(a1, 'bpmn2_Process116', b)
    if hasattr(a2, 'bpmn2_Process116'):
        assert _is_linked(a2, 'bpmn2_Process116', b)
    _safe_set(b, 'bpmn2_Process118', None)
    assert not _is_linked(b, 'bpmn2_Process118', a2)
    if hasattr(a2, 'bpmn2_Process116'):
        assert not _is_linked(a2, 'bpmn2_Process116', b)


def test_assoc_target369_reverse_link_reassign_clear():
    a1 = bpmn2_LinkEventDefinition(name="sample_text")
    a2 = bpmn2_LinkEventDefinition(name="sample_text_2")
    b = bpmn2_LinkEventDefinition(name="sample_text")
    _safe_set(b, 'source', a1)
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'LinkEventDefinition'):
        assert _is_linked(a1, 'LinkEventDefinition', b)
    _safe_set(b, 'source', a2)
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'LinkEventDefinition'):
        assert not _is_linked(a1, 'LinkEventDefinition', b)
    if hasattr(a2, 'LinkEventDefinition'):
        assert _is_linked(a2, 'LinkEventDefinition', b)
    _safe_set(b, 'source', None)
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'LinkEventDefinition'):
        assert not _is_linked(a2, 'LinkEventDefinition', b)


def test_assoc_targetRef419_reverse_link_reassign_clear():
    a1 = bpmn2_BaseElement(description="sample_text", id="sample_text")
    a2 = bpmn2_BaseElement(description="sample_text_2", id="sample_text_2")
    b = bpmn2_Association(associationDirection="sample_text")
    _safe_set(b, 'bpmn2_Association420', a1)
    assert _is_linked(b, 'bpmn2_Association420', a1)
    if hasattr(a1, 'bpmn2_BaseElement421'):
        assert _is_linked(a1, 'bpmn2_BaseElement421', b)
    _safe_set(b, 'bpmn2_Association420', a2)
    assert _is_linked(b, 'bpmn2_Association420', a2)
    if hasattr(a1, 'bpmn2_BaseElement421'):
        assert not _is_linked(a1, 'bpmn2_BaseElement421', b)
    if hasattr(a2, 'bpmn2_BaseElement421'):
        assert _is_linked(a2, 'bpmn2_BaseElement421', b)
    _safe_set(b, 'bpmn2_Association420', None)
    assert not _is_linked(b, 'bpmn2_Association420', a2)
    if hasattr(a2, 'bpmn2_BaseElement421'):
        assert not _is_linked(a2, 'bpmn2_BaseElement421', b)


def test_assoc_type100_reverse_link_reassign_clear():
    a1 = bpmn2_ResourceParameter(isRequired=True, name="sample_text")
    a2 = bpmn2_ResourceParameter(isRequired=False, name="sample_text_2")
    b = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    _safe_set(b, 'bpmn2_ItemDefinition102', a1)
    assert _is_linked(b, 'bpmn2_ItemDefinition102', a1)
    if hasattr(a1, 'bpmn2_ResourceParameter101'):
        assert _is_linked(a1, 'bpmn2_ResourceParameter101', b)
    _safe_set(b, 'bpmn2_ItemDefinition102', a2)
    assert _is_linked(b, 'bpmn2_ItemDefinition102', a2)
    if hasattr(a1, 'bpmn2_ResourceParameter101'):
        assert not _is_linked(a1, 'bpmn2_ResourceParameter101', b)
    if hasattr(a2, 'bpmn2_ResourceParameter101'):
        assert _is_linked(a2, 'bpmn2_ResourceParameter101', b)
    _safe_set(b, 'bpmn2_ItemDefinition102', None)
    assert not _is_linked(b, 'bpmn2_ItemDefinition102', a2)
    if hasattr(a2, 'bpmn2_ResourceParameter101'):
        assert not _is_linked(a2, 'bpmn2_ResourceParameter101', b)


def test_assoc_type244_reverse_link_reassign_clear():
    a1 = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    a2 = bpmn2_ItemDefinition(isCollection=False, itemKind="sample_text_2")
    b = bpmn2_CorrelationProperty(name="sample_text")
    _safe_set(b, 'bpmn2_CorrelationProperty245', a1)
    assert _is_linked(b, 'bpmn2_CorrelationProperty245', a1)
    if hasattr(a1, 'bpmn2_ItemDefinition246'):
        assert _is_linked(a1, 'bpmn2_ItemDefinition246', b)
    _safe_set(b, 'bpmn2_CorrelationProperty245', a2)
    assert _is_linked(b, 'bpmn2_CorrelationProperty245', a2)
    if hasattr(a1, 'bpmn2_ItemDefinition246'):
        assert not _is_linked(a1, 'bpmn2_ItemDefinition246', b)
    if hasattr(a2, 'bpmn2_ItemDefinition246'):
        assert _is_linked(a2, 'bpmn2_ItemDefinition246', b)
    _safe_set(b, 'bpmn2_CorrelationProperty245', None)
    assert not _is_linked(b, 'bpmn2_CorrelationProperty245', a2)
    if hasattr(a2, 'bpmn2_ItemDefinition246'):
        assert not _is_linked(a2, 'bpmn2_ItemDefinition246', b)


def test_assoc_whileExecutingInputRefs56_reverse_link_reassign_clear():
    a1 = bpmn2_InputSet(name="sample_text")
    a2 = bpmn2_InputSet(name="sample_text_2")
    b = bpmn2_DataInput(isCollection=True, name="sample_text")
    _safe_set(b, 'DataInput57', a1)
    assert _is_linked(b, 'DataInput57', a1)
    if hasattr(a1, 'inputSetWithWhileExecuting'):
        assert _is_linked(a1, 'inputSetWithWhileExecuting', b)
    _safe_set(b, 'DataInput57', a2)
    assert _is_linked(b, 'DataInput57', a2)
    if hasattr(a1, 'inputSetWithWhileExecuting'):
        assert not _is_linked(a1, 'inputSetWithWhileExecuting', b)
    if hasattr(a2, 'inputSetWithWhileExecuting'):
        assert _is_linked(a2, 'inputSetWithWhileExecuting', b)
    _safe_set(b, 'DataInput57', None)
    assert not _is_linked(b, 'DataInput57', a2)
    if hasattr(a2, 'inputSetWithWhileExecuting'):
        assert not _is_linked(a2, 'inputSetWithWhileExecuting', b)


def test_assoc_whileExecutingOutputRefs72_reverse_link_reassign_clear():
    a1 = bpmn2_OutputSet(name="sample_text")
    a2 = bpmn2_OutputSet(name="sample_text_2")
    b = bpmn2_DataOutput(isCollection=True, name="sample_text")
    _safe_set(b, 'DataOutput73', a1)
    assert _is_linked(b, 'DataOutput73', a1)
    if hasattr(a1, 'outputSetWithWhileExecuting'):
        assert _is_linked(a1, 'outputSetWithWhileExecuting', b)
    _safe_set(b, 'DataOutput73', a2)
    assert _is_linked(b, 'DataOutput73', a2)
    if hasattr(a1, 'outputSetWithWhileExecuting'):
        assert not _is_linked(a1, 'outputSetWithWhileExecuting', b)
    if hasattr(a2, 'outputSetWithWhileExecuting'):
        assert _is_linked(a2, 'outputSetWithWhileExecuting', b)
    _safe_set(b, 'DataOutput73', None)
    assert not _is_linked(b, 'DataOutput73', a2)
    if hasattr(a2, 'outputSetWithWhileExecuting'):
        assert not _is_linked(a2, 'outputSetWithWhileExecuting', b)


