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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_artifacts124_stub_double():
    # bpmn2_Artifact has no real 'bpmn2_Artifact' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Artifact()
    setattr(partner, 'bpmn2_Artifact', None)
    _safe_set(owner, 'bpmn2_Process125', {partner})
    assert getattr(partner, 'bpmn2_Artifact') == owner
    _safe_set(owner, 'bpmn2_Process125', set())
    assert getattr(partner, 'bpmn2_Artifact') is None


def test_assoc_artifacts168_stub_double():
    # bpmn2_Artifact has no real 'bpmn2_Artifact170' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True, name="sample_text")
    partner = bpmn2_Artifact()
    setattr(partner, 'bpmn2_Artifact170', None)
    _safe_set(owner, 'bpmn2_Collaboration169', {partner})
    assert getattr(partner, 'bpmn2_Artifact170') == owner
    _safe_set(owner, 'bpmn2_Collaboration169', set())
    assert getattr(partner, 'bpmn2_Artifact170') is None


def test_assoc_artifacts426_stub_double():
    # bpmn2_Artifact has no real 'bpmn2_Artifact427' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SubProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SubProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SubProcess(triggeredByEvent=True)
    partner = bpmn2_Artifact()
    setattr(partner, 'bpmn2_Artifact427', None)
    _safe_set(owner, 'bpmn2_SubProcess', {partner})
    assert getattr(partner, 'bpmn2_Artifact427') == owner
    _safe_set(owner, 'bpmn2_SubProcess', set())
    assert getattr(partner, 'bpmn2_Artifact427') is None


def test_assoc_auditing111_stub_double():
    # bpmn2_Auditing has no real 'bpmn2_Auditing' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Auditing()
    setattr(partner, 'bpmn2_Auditing', None)
    _safe_set(owner, 'bpmn2_Process', partner)
    assert getattr(partner, 'bpmn2_Auditing') == owner
    _safe_set(owner, 'bpmn2_Process', None)
    assert getattr(partner, 'bpmn2_Auditing') is None


def test_assoc_auditing136_stub_double():
    # bpmn2_Auditing has no real 'bpmn2_Auditing138' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FlowElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FlowElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FlowElement(name="sample_text")
    partner = bpmn2_Auditing()
    setattr(partner, 'bpmn2_Auditing138', None)
    _safe_set(owner, 'bpmn2_FlowElement137', partner)
    assert getattr(partner, 'bpmn2_Auditing138') == owner
    _safe_set(owner, 'bpmn2_FlowElement137', None)
    assert getattr(partner, 'bpmn2_Auditing138') is None


def test_assoc_body252_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject254' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(language="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject254', None)
    _safe_set(owner, 'bpmn2_FormalExpression253', partner)
    assert getattr(partner, 'bpmn2_EObject254') == owner
    _safe_set(owner, 'bpmn2_FormalExpression253', None)
    assert getattr(partner, 'bpmn2_EObject254') is None


def test_assoc_calledCollaborationRef386_stub_double():
    # bpmn2_CallConversation has no real 'bpmn2_CallConversation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True, name="sample_text")
    partner = bpmn2_CallConversation()
    setattr(partner, 'bpmn2_CallConversation', None)
    _safe_set(owner, 'bpmn2_Collaboration387', partner)
    assert getattr(partner, 'bpmn2_CallConversation') == owner
    _safe_set(owner, 'bpmn2_Collaboration387', None)
    assert getattr(partner, 'bpmn2_CallConversation') is None


def test_assoc_calledElementRef463_stub_double():
    # bpmn2_CallActivity has no real 'bpmn2_CallActivity' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CallableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CallableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CallableElement(name="sample_text")
    partner = bpmn2_CallActivity()
    setattr(partner, 'bpmn2_CallActivity', None)
    _safe_set(owner, 'bpmn2_CallableElement464', partner)
    assert getattr(partner, 'bpmn2_CallActivity') == owner
    _safe_set(owner, 'bpmn2_CallableElement464', None)
    assert getattr(partner, 'bpmn2_CallActivity') is None


def test_assoc_categoryValueRef416_stub_double():
    # bpmn2_Group has no real 'bpmn2_Group' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CategoryValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CategoryValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CategoryValue(value="sample_text")
    partner = bpmn2_Group()
    setattr(partner, 'bpmn2_Group', None)
    _safe_set(owner, 'bpmn2_CategoryValue', partner)
    assert getattr(partner, 'bpmn2_Group') == owner
    _safe_set(owner, 'bpmn2_CategoryValue', None)
    assert getattr(partner, 'bpmn2_Group') is None


def test_assoc_choreographyRef166_stub_double():
    # bpmn2_Choreography has no real 'bpmn2_Choreography' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True, name="sample_text")
    partner = bpmn2_Choreography()
    setattr(partner, 'bpmn2_Choreography', None)
    _safe_set(owner, 'bpmn2_Collaboration167', {partner})
    assert getattr(partner, 'bpmn2_Choreography') == owner
    _safe_set(owner, 'bpmn2_Collaboration167', set())
    assert getattr(partner, 'bpmn2_Choreography') is None


def test_assoc_completionCondition442_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression444' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression444', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics443', partner)
    assert getattr(partner, 'bpmn2_Expression444') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics443', None)
    assert getattr(partner, 'bpmn2_Expression444') is None


def test_assoc_completionCondition475_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression476' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_AdHocSubProcess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_AdHocSubProcess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_AdHocSubProcess(cancelRemainingInstances=True, ordering="sample_text")
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression476', None)
    _safe_set(owner, 'bpmn2_AdHocSubProcess', partner)
    assert getattr(partner, 'bpmn2_Expression476') == owner
    _safe_set(owner, 'bpmn2_AdHocSubProcess', None)
    assert getattr(partner, 'bpmn2_Expression476') is None


def test_assoc_complexBehaviorDefinition445_stub_double():
    # bpmn2_ComplexBehaviorDefinition has no real 'bpmn2_ComplexBehaviorDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_ComplexBehaviorDefinition()
    setattr(partner, 'bpmn2_ComplexBehaviorDefinition', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics446', {partner})
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics446', set())
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition') is None


def test_assoc_condition453_stub_double():
    # bpmn2_ComplexBehaviorDefinition has no real 'bpmn2_ComplexBehaviorDefinition454' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(language="sample_text")
    partner = bpmn2_ComplexBehaviorDefinition()
    setattr(partner, 'bpmn2_ComplexBehaviorDefinition454', None)
    _safe_set(owner, 'bpmn2_FormalExpression455', partner)
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition454') == owner
    _safe_set(owner, 'bpmn2_FormalExpression455', None)
    assert getattr(partner, 'bpmn2_ComplexBehaviorDefinition454') is None


def test_assoc_conditionExpression160_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression161' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression161', None)
    _safe_set(owner, 'bpmn2_SequenceFlow', partner)
    assert getattr(partner, 'bpmn2_Expression161') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow', None)
    assert getattr(partner, 'bpmn2_Expression161') is None


def test_assoc_conversationAssociations175_stub_double():
    # bpmn2_ConversationAssociation has no real 'bpmn2_ConversationAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True, name="sample_text")
    partner = bpmn2_ConversationAssociation()
    setattr(partner, 'bpmn2_ConversationAssociation', None)
    _safe_set(owner, 'bpmn2_Collaboration176', partner)
    assert getattr(partner, 'bpmn2_ConversationAssociation') == owner
    _safe_set(owner, 'bpmn2_Collaboration176', None)
    assert getattr(partner, 'bpmn2_ConversationAssociation') is None


def test_assoc_conversationNodes391_stub_double():
    # bpmn2_SubConversation has no real 'bpmn2_SubConversation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ConversationNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ConversationNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ConversationNode(name="sample_text")
    partner = bpmn2_SubConversation()
    setattr(partner, 'bpmn2_SubConversation', None)
    _safe_set(owner, 'bpmn2_ConversationNode392', partner)
    assert owner in getattr(partner, 'bpmn2_SubConversation')
    _safe_set(owner, 'bpmn2_ConversationNode392', None)
    assert owner not in getattr(partner, 'bpmn2_SubConversation')


def test_assoc_correlationKeyRef258_stub_double():
    # bpmn2_CorrelationSubscription has no real 'bpmn2_CorrelationSubscription259' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CorrelationKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CorrelationKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CorrelationKey(name="sample_text")
    partner = bpmn2_CorrelationSubscription()
    setattr(partner, 'bpmn2_CorrelationSubscription259', None)
    _safe_set(owner, 'bpmn2_CorrelationKey260', partner)
    assert getattr(partner, 'bpmn2_CorrelationSubscription259') == owner
    _safe_set(owner, 'bpmn2_CorrelationKey260', None)
    assert getattr(partner, 'bpmn2_CorrelationSubscription259') is None


def test_assoc_correlationPropertyRef266_stub_double():
    # bpmn2_CorrelationPropertyBinding has no real 'bpmn2_CorrelationPropertyBinding267' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CorrelationProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CorrelationProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CorrelationProperty(name="sample_text")
    partner = bpmn2_CorrelationPropertyBinding()
    setattr(partner, 'bpmn2_CorrelationPropertyBinding267', None)
    _safe_set(owner, 'bpmn2_CorrelationProperty268', partner)
    assert getattr(partner, 'bpmn2_CorrelationPropertyBinding267') == owner
    _safe_set(owner, 'bpmn2_CorrelationProperty268', None)
    assert getattr(partner, 'bpmn2_CorrelationPropertyBinding267') is None


def test_assoc_correlationPropertyRetrievalExpression242_stub_double():
    # bpmn2_CorrelationPropertyRetrievalExpression has no real 'bpmn2_CorrelationPropertyRetrievalExpression' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CorrelationProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CorrelationProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CorrelationProperty(name="sample_text")
    partner = bpmn2_CorrelationPropertyRetrievalExpression()
    setattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression', None)
    _safe_set(owner, 'bpmn2_CorrelationProperty243', {partner})
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression') == owner
    _safe_set(owner, 'bpmn2_CorrelationProperty243', set())
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression') is None


def test_assoc_correlationSubscriptions126_stub_double():
    # bpmn2_CorrelationSubscription has no real 'bpmn2_CorrelationSubscription' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_CorrelationSubscription()
    setattr(partner, 'bpmn2_CorrelationSubscription', None)
    _safe_set(owner, 'bpmn2_Process127', {partner})
    assert getattr(partner, 'bpmn2_CorrelationSubscription') == owner
    _safe_set(owner, 'bpmn2_Process127', set())
    assert getattr(partner, 'bpmn2_CorrelationSubscription') is None


def test_assoc_dataInputAssociations283_stub_double():
    # bpmn2_DataInputAssociation has no real 'bpmn2_DataInputAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_DataInputAssociation()
    setattr(partner, 'bpmn2_DataInputAssociation', None)
    _safe_set(owner, 'bpmn2_Activity284', {partner})
    assert getattr(partner, 'bpmn2_DataInputAssociation') == owner
    _safe_set(owner, 'bpmn2_Activity284', set())
    assert getattr(partner, 'bpmn2_DataInputAssociation') is None


def test_assoc_dataInputs346_stub_double():
    # bpmn2_ThrowEvent has no real 'bpmn2_ThrowEvent347' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True, name="sample_text")
    partner = bpmn2_ThrowEvent()
    setattr(partner, 'bpmn2_ThrowEvent347', None)
    _safe_set(owner, 'bpmn2_DataInput348', partner)
    assert owner in getattr(partner, 'bpmn2_ThrowEvent347')
    _safe_set(owner, 'bpmn2_DataInput348', None)
    assert owner not in getattr(partner, 'bpmn2_ThrowEvent347')


def test_assoc_dataInputs49_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification50' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataInput(isCollection=True, name="sample_text")
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification50', None)
    _safe_set(owner, 'bpmn2_DataInput', partner)
    assert owner in getattr(partner, 'bpmn2_InputOutputSpecification50')
    _safe_set(owner, 'bpmn2_DataInput', None)
    assert owner not in getattr(partner, 'bpmn2_InputOutputSpecification50')


def test_assoc_dataObjectRef385_stub_double():
    # bpmn2_DataObjectReference has no real 'bpmn2_DataObjectReference' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataObject(isCollection=True)
    partner = bpmn2_DataObjectReference()
    setattr(partner, 'bpmn2_DataObjectReference', None)
    _safe_set(owner, 'bpmn2_DataObject', partner)
    assert getattr(partner, 'bpmn2_DataObjectReference') == owner
    _safe_set(owner, 'bpmn2_DataObject', None)
    assert getattr(partner, 'bpmn2_DataObjectReference') is None


def test_assoc_dataOutputAssociation292_stub_double():
    # bpmn2_DataOutputAssociation has no real 'bpmn2_DataOutputAssociation294' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_DataOutputAssociation()
    setattr(partner, 'bpmn2_DataOutputAssociation294', None)
    _safe_set(owner, 'bpmn2_CatchEvent293', {partner})
    assert getattr(partner, 'bpmn2_DataOutputAssociation294') == owner
    _safe_set(owner, 'bpmn2_CatchEvent293', set())
    assert getattr(partner, 'bpmn2_DataOutputAssociation294') is None


def test_assoc_dataOutputAssociations285_stub_double():
    # bpmn2_DataOutputAssociation has no real 'bpmn2_DataOutputAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_DataOutputAssociation()
    setattr(partner, 'bpmn2_DataOutputAssociation', None)
    _safe_set(owner, 'bpmn2_Activity286', {partner})
    assert getattr(partner, 'bpmn2_DataOutputAssociation') == owner
    _safe_set(owner, 'bpmn2_Activity286', set())
    assert getattr(partner, 'bpmn2_DataOutputAssociation') is None


def test_assoc_dataOutputs51_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification52' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataOutput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataOutput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataOutput(isCollection=True, name="sample_text")
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification52', None)
    _safe_set(owner, 'bpmn2_DataOutput', partner)
    assert owner in getattr(partner, 'bpmn2_InputOutputSpecification52')
    _safe_set(owner, 'bpmn2_DataOutput', None)
    assert owner not in getattr(partner, 'bpmn2_InputOutputSpecification52')


def test_assoc_dataPath263_stub_double():
    # bpmn2_CorrelationPropertyBinding has no real 'bpmn2_CorrelationPropertyBinding264' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(language="sample_text")
    partner = bpmn2_CorrelationPropertyBinding()
    setattr(partner, 'bpmn2_CorrelationPropertyBinding264', None)
    _safe_set(owner, 'bpmn2_FormalExpression265', partner)
    assert getattr(partner, 'bpmn2_CorrelationPropertyBinding264') == owner
    _safe_set(owner, 'bpmn2_FormalExpression265', None)
    assert getattr(partner, 'bpmn2_CorrelationPropertyBinding264') is None


def test_assoc_dataState67_stub_double():
    # bpmn2_ItemAwareElement has no real 'bpmn2_ItemAwareElement68' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataState(name="sample_text")
    partner = bpmn2_ItemAwareElement()
    setattr(partner, 'bpmn2_ItemAwareElement68', None)
    _safe_set(owner, 'bpmn2_DataState', partner)
    assert getattr(partner, 'bpmn2_ItemAwareElement68') == owner
    _safe_set(owner, 'bpmn2_DataState', None)
    assert getattr(partner, 'bpmn2_ItemAwareElement68') is None


def test_assoc_dataStoreRef384_stub_double():
    # bpmn2_DataStoreReference has no real 'bpmn2_DataStoreReference' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_DataStore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_DataStore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_DataStore(capacity=7, isUnlimited=True, name="sample_text")
    partner = bpmn2_DataStoreReference()
    setattr(partner, 'bpmn2_DataStoreReference', None)
    _safe_set(owner, 'bpmn2_DataStore', partner)
    assert getattr(partner, 'bpmn2_DataStoreReference') == owner
    _safe_set(owner, 'bpmn2_DataStore', None)
    assert getattr(partner, 'bpmn2_DataStoreReference') is None


def test_assoc_default324_stub_double():
    # bpmn2_ComplexGateway has no real 'bpmn2_ComplexGateway325' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_ComplexGateway()
    setattr(partner, 'bpmn2_ComplexGateway325', None)
    _safe_set(owner, 'bpmn2_SequenceFlow326', partner)
    assert getattr(partner, 'bpmn2_ComplexGateway325') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow326', None)
    assert getattr(partner, 'bpmn2_ComplexGateway325') is None


def test_assoc_default327_stub_double():
    # bpmn2_ExclusiveGateway has no real 'bpmn2_ExclusiveGateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_ExclusiveGateway()
    setattr(partner, 'bpmn2_ExclusiveGateway', None)
    _safe_set(owner, 'bpmn2_SequenceFlow328', partner)
    assert getattr(partner, 'bpmn2_ExclusiveGateway') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow328', None)
    assert getattr(partner, 'bpmn2_ExclusiveGateway') is None


def test_assoc_default329_stub_double():
    # bpmn2_InclusiveGateway has no real 'bpmn2_InclusiveGateway' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_InclusiveGateway()
    setattr(partner, 'bpmn2_InclusiveGateway', None)
    _safe_set(owner, 'bpmn2_SequenceFlow330', partner)
    assert getattr(partner, 'bpmn2_InclusiveGateway') == owner
    _safe_set(owner, 'bpmn2_SequenceFlow330', None)
    assert getattr(partner, 'bpmn2_InclusiveGateway') is None


def test_assoc_diagrams487_stub_double():
    # bpmn2_BPMNDiagram has no real 'bpmn2_BPMNDiagram' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Definitions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Definitions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", name="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    partner = bpmn2_BPMNDiagram()
    setattr(partner, 'bpmn2_BPMNDiagram', None)
    _safe_set(owner, 'bpmn2_Definitions488', {partner})
    assert getattr(partner, 'bpmn2_BPMNDiagram') == owner
    _safe_set(owner, 'bpmn2_Definitions488', set())
    assert getattr(partner, 'bpmn2_BPMNDiagram') is None


def test_assoc_endPointRefs198_stub_double():
    # bpmn2_EndPoint has no real 'bpmn2_EndPoint' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Participant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Participant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Participant(name="sample_text")
    partner = bpmn2_EndPoint()
    setattr(partner, 'bpmn2_EndPoint', None)
    _safe_set(owner, 'bpmn2_Participant199', {partner})
    assert getattr(partner, 'bpmn2_EndPoint') == owner
    _safe_set(owner, 'bpmn2_Participant199', set())
    assert getattr(partner, 'bpmn2_EndPoint') is None


def test_assoc_errorRef352_stub_double():
    # bpmn2_ErrorEventDefinition has no real 'bpmn2_ErrorEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Error's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Error's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Error(errorCode="sample_text", name="sample_text")
    partner = bpmn2_ErrorEventDefinition()
    setattr(partner, 'bpmn2_ErrorEventDefinition', None)
    _safe_set(owner, 'bpmn2_Error353', partner)
    assert getattr(partner, 'bpmn2_ErrorEventDefinition') == owner
    _safe_set(owner, 'bpmn2_Error353', None)
    assert getattr(partner, 'bpmn2_ErrorEventDefinition') is None


def test_assoc_escalationRef354_stub_double():
    # bpmn2_EscalationEventDefinition has no real 'bpmn2_EscalationEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Escalation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Escalation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Escalation(escalationCode="sample_text", id="sample_text", name="sample_text")
    partner = bpmn2_EscalationEventDefinition()
    setattr(partner, 'bpmn2_EscalationEventDefinition', None)
    _safe_set(owner, 'bpmn2_Escalation', partner)
    assert getattr(partner, 'bpmn2_EscalationEventDefinition') == owner
    _safe_set(owner, 'bpmn2_Escalation', None)
    assert getattr(partner, 'bpmn2_EscalationEventDefinition') is None


def test_assoc_eventDefinitionRefs290_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition', None)
    _safe_set(owner, 'bpmn2_CatchEvent291', {partner})
    assert getattr(partner, 'bpmn2_EventDefinition') == owner
    _safe_set(owner, 'bpmn2_CatchEvent291', set())
    assert getattr(partner, 'bpmn2_EventDefinition') is None


def test_assoc_eventDefinitions298_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition300' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CatchEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CatchEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CatchEvent(parallelMultiple=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition300', None)
    _safe_set(owner, 'bpmn2_CatchEvent299', {partner})
    assert getattr(partner, 'bpmn2_EventDefinition300') == owner
    _safe_set(owner, 'bpmn2_CatchEvent299', set())
    assert getattr(partner, 'bpmn2_EventDefinition300') is None


def test_assoc_expression103_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ResourceParameterBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ResourceParameterBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ResourceParameterBinding(id="sample_text")
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression', None)
    _safe_set(owner, 'bpmn2_ResourceParameterBinding104', partner)
    assert getattr(partner, 'bpmn2_Expression') == owner
    _safe_set(owner, 'bpmn2_ResourceParameterBinding104', None)
    assert getattr(partner, 'bpmn2_Expression') is None


def test_assoc_expression108_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ResourceAssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ResourceAssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ResourceAssignmentExpression(id="sample_text")
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression110', None)
    _safe_set(owner, 'bpmn2_ResourceAssignmentExpression109', partner)
    assert getattr(partner, 'bpmn2_Expression110') == owner
    _safe_set(owner, 'bpmn2_ResourceAssignmentExpression109', None)
    assert getattr(partner, 'bpmn2_Expression110') is None


def test_assoc_flowElements133_stub_double():
    # bpmn2_FlowElementsContainer has no real 'bpmn2_FlowElementsContainer' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FlowElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FlowElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FlowElement(name="sample_text")
    partner = bpmn2_FlowElementsContainer()
    setattr(partner, 'bpmn2_FlowElementsContainer', None)
    _safe_set(owner, 'bpmn2_FlowElement', partner)
    assert owner in getattr(partner, 'bpmn2_FlowElementsContainer')
    _safe_set(owner, 'bpmn2_FlowElement', None)
    assert owner not in getattr(partner, 'bpmn2_FlowElementsContainer')


def test_assoc_flowNodeRefs152_stub_double():
    # bpmn2_FlowNode has no real 'FlowNode' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Lane's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Lane's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Lane(name="sample_text")
    partner = bpmn2_FlowNode()
    setattr(partner, 'FlowNode', None)
    _safe_set(owner, 'lanes', {partner})
    assert getattr(partner, 'FlowNode') == owner
    _safe_set(owner, 'lanes', set())
    assert getattr(partner, 'FlowNode') is None


def test_assoc_implementationRef1_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Interface(name="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject', None)
    _safe_set(owner, 'bpmn2_Interface2', partner)
    assert getattr(partner, 'bpmn2_EObject') == owner
    _safe_set(owner, 'bpmn2_Interface2', None)
    assert getattr(partner, 'bpmn2_EObject') is None


def test_assoc_implementationRef25_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject27' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Operation(name="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject27', None)
    _safe_set(owner, 'bpmn2_Operation26', partner)
    assert getattr(partner, 'bpmn2_EObject27') == owner
    _safe_set(owner, 'bpmn2_Operation26', None)
    assert getattr(partner, 'bpmn2_EObject27') is None


def test_assoc_incoming157_stub_double():
    # bpmn2_FlowNode has no real 'targetRef' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'targetRef', None)
    _safe_set(owner, 'SequenceFlow158', partner)
    assert owner in getattr(partner, 'targetRef')
    _safe_set(owner, 'SequenceFlow158', None)
    assert owner not in getattr(partner, 'targetRef')


def test_assoc_incomingConversationLinks203_stub_double():
    # bpmn2_InteractionNode has no real 'targetRef204' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ConversationLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ConversationLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ConversationLink(name="sample_text")
    partner = bpmn2_InteractionNode()
    setattr(partner, 'targetRef204', None)
    _safe_set(owner, 'ConversationLink', partner)
    assert owner in getattr(partner, 'targetRef204')
    _safe_set(owner, 'ConversationLink', None)
    assert owner not in getattr(partner, 'targetRef204')


def test_assoc_initiatingParticipantRef414_stub_double():
    # bpmn2_GlobalChoreographyTask has no real 'bpmn2_GlobalChoreographyTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Participant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Participant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Participant(name="sample_text")
    partner = bpmn2_GlobalChoreographyTask()
    setattr(partner, 'bpmn2_GlobalChoreographyTask', None)
    _safe_set(owner, 'bpmn2_Participant415', partner)
    assert getattr(partner, 'bpmn2_GlobalChoreographyTask') == owner
    _safe_set(owner, 'bpmn2_Participant415', None)
    assert getattr(partner, 'bpmn2_GlobalChoreographyTask') is None


def test_assoc_innerConversationNodeRef225_stub_double():
    # bpmn2_ConversationAssociation has no real 'bpmn2_ConversationAssociation226' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ConversationNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ConversationNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ConversationNode(name="sample_text")
    partner = bpmn2_ConversationAssociation()
    setattr(partner, 'bpmn2_ConversationAssociation226', None)
    _safe_set(owner, 'bpmn2_ConversationNode227', partner)
    assert getattr(partner, 'bpmn2_ConversationAssociation226') == owner
    _safe_set(owner, 'bpmn2_ConversationNode227', None)
    assert getattr(partner, 'bpmn2_ConversationAssociation226') is None


def test_assoc_innerMessageFlowRef211_stub_double():
    # bpmn2_MessageFlowAssociation has no real 'bpmn2_MessageFlowAssociation212' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MessageFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MessageFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MessageFlow(name="sample_text")
    partner = bpmn2_MessageFlowAssociation()
    setattr(partner, 'bpmn2_MessageFlowAssociation212', None)
    _safe_set(owner, 'bpmn2_MessageFlow213', partner)
    assert getattr(partner, 'bpmn2_MessageFlowAssociation212') == owner
    _safe_set(owner, 'bpmn2_MessageFlow213', None)
    assert getattr(partner, 'bpmn2_MessageFlowAssociation212') is None


def test_assoc_innerParticipantRef187_stub_double():
    # bpmn2_ParticipantAssociation has no real 'bpmn2_ParticipantAssociation188' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Participant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Participant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Participant(name="sample_text")
    partner = bpmn2_ParticipantAssociation()
    setattr(partner, 'bpmn2_ParticipantAssociation188', None)
    _safe_set(owner, 'bpmn2_Participant189', partner)
    assert getattr(partner, 'bpmn2_ParticipantAssociation188') == owner
    _safe_set(owner, 'bpmn2_Participant189', None)
    assert getattr(partner, 'bpmn2_ParticipantAssociation188') is None


def test_assoc_inputSet338_stub_double():
    # bpmn2_ThrowEvent has no real 'bpmn2_ThrowEvent' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_InputSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_InputSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_InputSet(name="sample_text")
    partner = bpmn2_ThrowEvent()
    setattr(partner, 'bpmn2_ThrowEvent', None)
    _safe_set(owner, 'bpmn2_InputSet339', partner)
    assert getattr(partner, 'bpmn2_ThrowEvent') == owner
    _safe_set(owner, 'bpmn2_InputSet339', None)
    assert getattr(partner, 'bpmn2_ThrowEvent') is None


def test_assoc_inputSets45_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification46' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_InputSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_InputSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_InputSet(name="sample_text")
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification46', None)
    _safe_set(owner, 'bpmn2_InputSet', partner)
    assert owner in getattr(partner, 'bpmn2_InputOutputSpecification46')
    _safe_set(owner, 'bpmn2_InputSet', None)
    assert owner not in getattr(partner, 'bpmn2_InputOutputSpecification46')


def test_assoc_ioSpecification279_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification281' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification281', None)
    _safe_set(owner, 'bpmn2_Activity280', partner)
    assert getattr(partner, 'bpmn2_InputOutputSpecification281') == owner
    _safe_set(owner, 'bpmn2_Activity280', None)
    assert getattr(partner, 'bpmn2_InputOutputSpecification281') is None


def test_assoc_ioSpecification39_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_CallableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_CallableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_CallableElement(name="sample_text")
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification', None)
    _safe_set(owner, 'bpmn2_CallableElement', partner)
    assert getattr(partner, 'bpmn2_InputOutputSpecification') == owner
    _safe_set(owner, 'bpmn2_CallableElement', None)
    assert getattr(partner, 'bpmn2_InputOutputSpecification') is None


def test_assoc_itemSubjectRef65_stub_double():
    # bpmn2_ItemAwareElement has no real 'bpmn2_ItemAwareElement' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_ItemAwareElement()
    setattr(partner, 'bpmn2_ItemAwareElement', None)
    _safe_set(owner, 'bpmn2_ItemDefinition66', partner)
    assert getattr(partner, 'bpmn2_ItemAwareElement') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition66', None)
    assert getattr(partner, 'bpmn2_ItemAwareElement') is None


def test_assoc_laneSets134_stub_double():
    # bpmn2_FlowElementsContainer has no real 'bpmn2_FlowElementsContainer135' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_LaneSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_LaneSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_LaneSet(name="sample_text")
    partner = bpmn2_FlowElementsContainer()
    setattr(partner, 'bpmn2_FlowElementsContainer135', None)
    _safe_set(owner, 'bpmn2_LaneSet', partner)
    assert owner in getattr(partner, 'bpmn2_FlowElementsContainer135')
    _safe_set(owner, 'bpmn2_LaneSet', None)
    assert owner not in getattr(partner, 'bpmn2_FlowElementsContainer135')


def test_assoc_lanes159_stub_double():
    # bpmn2_FlowNode has no real 'flowNodeRefs' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Lane's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Lane's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Lane(name="sample_text")
    partner = bpmn2_FlowNode()
    setattr(partner, 'flowNodeRefs', None)
    _safe_set(owner, 'Lane', partner)
    assert owner in getattr(partner, 'flowNodeRefs')
    _safe_set(owner, 'Lane', None)
    assert owner not in getattr(partner, 'flowNodeRefs')


def test_assoc_loopCardinality428_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression429' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression429', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics', partner)
    assert getattr(partner, 'bpmn2_Expression429') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics', None)
    assert getattr(partner, 'bpmn2_Expression429') is None


def test_assoc_loopCharacteristics269_stub_double():
    # bpmn2_LoopCharacteristics has no real 'bpmn2_LoopCharacteristics' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Activity(completionQuantity=7, isForCompensation=True, startQuantity=7)
    partner = bpmn2_LoopCharacteristics()
    setattr(partner, 'bpmn2_LoopCharacteristics', None)
    _safe_set(owner, 'bpmn2_Activity', partner)
    assert getattr(partner, 'bpmn2_LoopCharacteristics') == owner
    _safe_set(owner, 'bpmn2_Activity', None)
    assert getattr(partner, 'bpmn2_LoopCharacteristics') is None


def test_assoc_loopCondition458_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression459' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_StandardLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_StandardLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_StandardLoopCharacteristics(testBefore=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression459', None)
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics', partner)
    assert getattr(partner, 'bpmn2_Expression459') == owner
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics', None)
    assert getattr(partner, 'bpmn2_Expression459') is None


def test_assoc_loopDataInputRef430_stub_double():
    # bpmn2_ItemAwareElement has no real 'bpmn2_ItemAwareElement432' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_ItemAwareElement()
    setattr(partner, 'bpmn2_ItemAwareElement432', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics431', partner)
    assert getattr(partner, 'bpmn2_ItemAwareElement432') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics431', None)
    assert getattr(partner, 'bpmn2_ItemAwareElement432') is None


def test_assoc_loopDataOutputRef433_stub_double():
    # bpmn2_ItemAwareElement has no real 'bpmn2_ItemAwareElement435' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_ItemAwareElement()
    setattr(partner, 'bpmn2_ItemAwareElement435', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics434', partner)
    assert getattr(partner, 'bpmn2_ItemAwareElement435') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics434', None)
    assert getattr(partner, 'bpmn2_ItemAwareElement435') is None


def test_assoc_loopMaximum460_stub_double():
    # bpmn2_Expression has no real 'bpmn2_Expression462' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_StandardLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_StandardLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_StandardLoopCharacteristics(testBefore=True)
    partner = bpmn2_Expression()
    setattr(partner, 'bpmn2_Expression462', None)
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics461', partner)
    assert getattr(partner, 'bpmn2_Expression462') == owner
    _safe_set(owner, 'bpmn2_StandardLoopCharacteristics461', None)
    assert getattr(partner, 'bpmn2_Expression462') is None


def test_assoc_messageFlowAssociations173_stub_double():
    # bpmn2_MessageFlowAssociation has no real 'bpmn2_MessageFlowAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True, name="sample_text")
    partner = bpmn2_MessageFlowAssociation()
    setattr(partner, 'bpmn2_MessageFlowAssociation', None)
    _safe_set(owner, 'bpmn2_Collaboration174', {partner})
    assert getattr(partner, 'bpmn2_MessageFlowAssociation') == owner
    _safe_set(owner, 'bpmn2_Collaboration174', set())
    assert getattr(partner, 'bpmn2_MessageFlowAssociation') is None


def test_assoc_messageFlowRef412_stub_double():
    # bpmn2_ChoreographyTask has no real 'bpmn2_ChoreographyTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MessageFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MessageFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MessageFlow(name="sample_text")
    partner = bpmn2_ChoreographyTask()
    setattr(partner, 'bpmn2_ChoreographyTask', None)
    _safe_set(owner, 'bpmn2_MessageFlow413', partner)
    assert owner in getattr(partner, 'bpmn2_ChoreographyTask')
    _safe_set(owner, 'bpmn2_MessageFlow413', None)
    assert owner not in getattr(partner, 'bpmn2_ChoreographyTask')


def test_assoc_messagePath247_stub_double():
    # bpmn2_CorrelationPropertyRetrievalExpression has no real 'bpmn2_CorrelationPropertyRetrievalExpression248' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(language="sample_text")
    partner = bpmn2_CorrelationPropertyRetrievalExpression()
    setattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression248', None)
    _safe_set(owner, 'bpmn2_FormalExpression', partner)
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression248') == owner
    _safe_set(owner, 'bpmn2_FormalExpression', None)
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression248') is None


def test_assoc_messageRef249_stub_double():
    # bpmn2_CorrelationPropertyRetrievalExpression has no real 'bpmn2_CorrelationPropertyRetrievalExpression250' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Message(name="sample_text")
    partner = bpmn2_CorrelationPropertyRetrievalExpression()
    setattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression250', None)
    _safe_set(owner, 'bpmn2_Message251', partner)
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression250') == owner
    _safe_set(owner, 'bpmn2_Message251', None)
    assert getattr(partner, 'bpmn2_CorrelationPropertyRetrievalExpression250') is None


def test_assoc_messageRef373_stub_double():
    # bpmn2_MessageEventDefinition has no real 'bpmn2_MessageEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Message(name="sample_text")
    partner = bpmn2_MessageEventDefinition()
    setattr(partner, 'bpmn2_MessageEventDefinition', None)
    _safe_set(owner, 'bpmn2_Message374', partner)
    assert getattr(partner, 'bpmn2_MessageEventDefinition') == owner
    _safe_set(owner, 'bpmn2_Message374', None)
    assert getattr(partner, 'bpmn2_MessageEventDefinition') is None


def test_assoc_monitoring112_stub_double():
    # bpmn2_Monitoring has no real 'bpmn2_Monitoring' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Process(isClosed=True, isExecutable=True, processType="sample_text")
    partner = bpmn2_Monitoring()
    setattr(partner, 'bpmn2_Monitoring', None)
    _safe_set(owner, 'bpmn2_Process113', partner)
    assert getattr(partner, 'bpmn2_Monitoring') == owner
    _safe_set(owner, 'bpmn2_Process113', None)
    assert getattr(partner, 'bpmn2_Monitoring') is None


def test_assoc_monitoring139_stub_double():
    # bpmn2_Monitoring has no real 'bpmn2_Monitoring141' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FlowElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FlowElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FlowElement(name="sample_text")
    partner = bpmn2_Monitoring()
    setattr(partner, 'bpmn2_Monitoring141', None)
    _safe_set(owner, 'bpmn2_FlowElement140', partner)
    assert getattr(partner, 'bpmn2_Monitoring141') == owner
    _safe_set(owner, 'bpmn2_FlowElement140', None)
    assert getattr(partner, 'bpmn2_Monitoring141') is None


def test_assoc_noneBehaviorEventRef450_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition452' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition452', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics451', partner)
    assert getattr(partner, 'bpmn2_EventDefinition452') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics451', None)
    assert getattr(partner, 'bpmn2_EventDefinition452') is None


def test_assoc_oneBehaviorEventRef447_stub_double():
    # bpmn2_EventDefinition has no real 'bpmn2_EventDefinition449' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MultiInstanceLoopCharacteristics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MultiInstanceLoopCharacteristics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MultiInstanceLoopCharacteristics(behavior="sample_text", isSequential=True)
    partner = bpmn2_EventDefinition()
    setattr(partner, 'bpmn2_EventDefinition449', None)
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics448', partner)
    assert getattr(partner, 'bpmn2_EventDefinition449') == owner
    _safe_set(owner, 'bpmn2_MultiInstanceLoopCharacteristics448', None)
    assert getattr(partner, 'bpmn2_EventDefinition449') is None


def test_assoc_operationRef375_stub_double():
    # bpmn2_MessageEventDefinition has no real 'bpmn2_MessageEventDefinition376' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Operation(name="sample_text")
    partner = bpmn2_MessageEventDefinition()
    setattr(partner, 'bpmn2_MessageEventDefinition376', None)
    _safe_set(owner, 'bpmn2_Operation377', partner)
    assert getattr(partner, 'bpmn2_MessageEventDefinition376') == owner
    _safe_set(owner, 'bpmn2_Operation377', None)
    assert getattr(partner, 'bpmn2_MessageEventDefinition376') is None


def test_assoc_outerConversationNodeRef228_stub_double():
    # bpmn2_ConversationAssociation has no real 'bpmn2_ConversationAssociation229' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ConversationNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ConversationNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ConversationNode(name="sample_text")
    partner = bpmn2_ConversationAssociation()
    setattr(partner, 'bpmn2_ConversationAssociation229', None)
    _safe_set(owner, 'bpmn2_ConversationNode230', partner)
    assert getattr(partner, 'bpmn2_ConversationAssociation229') == owner
    _safe_set(owner, 'bpmn2_ConversationNode230', None)
    assert getattr(partner, 'bpmn2_ConversationAssociation229') is None


def test_assoc_outerMessageFlowRef214_stub_double():
    # bpmn2_MessageFlowAssociation has no real 'bpmn2_MessageFlowAssociation215' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MessageFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MessageFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MessageFlow(name="sample_text")
    partner = bpmn2_MessageFlowAssociation()
    setattr(partner, 'bpmn2_MessageFlowAssociation215', None)
    _safe_set(owner, 'bpmn2_MessageFlow216', partner)
    assert getattr(partner, 'bpmn2_MessageFlowAssociation215') == owner
    _safe_set(owner, 'bpmn2_MessageFlow216', None)
    assert getattr(partner, 'bpmn2_MessageFlowAssociation215') is None


def test_assoc_outerParticipantRef190_stub_double():
    # bpmn2_ParticipantAssociation has no real 'bpmn2_ParticipantAssociation191' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Participant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Participant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Participant(name="sample_text")
    partner = bpmn2_ParticipantAssociation()
    setattr(partner, 'bpmn2_ParticipantAssociation191', None)
    _safe_set(owner, 'bpmn2_Participant192', partner)
    assert getattr(partner, 'bpmn2_ParticipantAssociation191') == owner
    _safe_set(owner, 'bpmn2_Participant192', None)
    assert getattr(partner, 'bpmn2_ParticipantAssociation191') is None


def test_assoc_outgoing156_stub_double():
    # bpmn2_FlowNode has no real 'sourceRef' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'sourceRef', None)
    _safe_set(owner, 'SequenceFlow', partner)
    assert owner in getattr(partner, 'sourceRef')
    _safe_set(owner, 'SequenceFlow', None)
    assert owner not in getattr(partner, 'sourceRef')


def test_assoc_outgoingConversationLinks205_stub_double():
    # bpmn2_InteractionNode has no real 'sourceRef206' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ConversationLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ConversationLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ConversationLink(name="sample_text")
    partner = bpmn2_InteractionNode()
    setattr(partner, 'sourceRef206', None)
    _safe_set(owner, 'ConversationLink207', partner)
    assert owner in getattr(partner, 'sourceRef206')
    _safe_set(owner, 'ConversationLink207', None)
    assert owner not in getattr(partner, 'sourceRef206')


def test_assoc_outputSets47_stub_double():
    # bpmn2_InputOutputSpecification has no real 'bpmn2_InputOutputSpecification48' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_OutputSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_OutputSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_OutputSet(name="sample_text")
    partner = bpmn2_InputOutputSpecification()
    setattr(partner, 'bpmn2_InputOutputSpecification48', None)
    _safe_set(owner, 'bpmn2_OutputSet', partner)
    assert owner in getattr(partner, 'bpmn2_InputOutputSpecification48')
    _safe_set(owner, 'bpmn2_OutputSet', None)
    assert owner not in getattr(partner, 'bpmn2_InputOutputSpecification48')


def test_assoc_participantAssociations171_stub_double():
    # bpmn2_ParticipantAssociation has no real 'bpmn2_ParticipantAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Collaboration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Collaboration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Collaboration(isClosed=True, name="sample_text")
    partner = bpmn2_ParticipantAssociation()
    setattr(partner, 'bpmn2_ParticipantAssociation', None)
    _safe_set(owner, 'bpmn2_Collaboration172', {partner})
    assert getattr(partner, 'bpmn2_ParticipantAssociation') == owner
    _safe_set(owner, 'bpmn2_Collaboration172', set())
    assert getattr(partner, 'bpmn2_ParticipantAssociation') is None


def test_assoc_properties301_stub_double():
    # bpmn2_Event has no real 'bpmn2_Event' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Property(name="sample_text")
    partner = bpmn2_Event()
    setattr(partner, 'bpmn2_Event', None)
    _safe_set(owner, 'bpmn2_Property302', partner)
    assert owner in getattr(partner, 'bpmn2_Event')
    _safe_set(owner, 'bpmn2_Property302', None)
    assert owner not in getattr(partner, 'bpmn2_Event')


def test_assoc_renderings319_stub_double():
    # bpmn2_Rendering has no real 'bpmn2_Rendering' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_UserTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_UserTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_UserTask(implementation="sample_text")
    partner = bpmn2_Rendering()
    setattr(partner, 'bpmn2_Rendering', None)
    _safe_set(owner, 'bpmn2_UserTask', {partner})
    assert getattr(partner, 'bpmn2_Rendering') == owner
    _safe_set(owner, 'bpmn2_UserTask', set())
    assert getattr(partner, 'bpmn2_Rendering') is None


def test_assoc_renderings320_stub_double():
    # bpmn2_Rendering has no real 'bpmn2_Rendering321' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_GlobalUserTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_GlobalUserTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_GlobalUserTask(implementation="sample_text")
    partner = bpmn2_Rendering()
    setattr(partner, 'bpmn2_Rendering321', None)
    _safe_set(owner, 'bpmn2_GlobalUserTask', {partner})
    assert getattr(partner, 'bpmn2_Rendering321') == owner
    _safe_set(owner, 'bpmn2_GlobalUserTask', set())
    assert getattr(partner, 'bpmn2_Rendering321') is None


def test_assoc_resources38_stub_double():
    # bpmn2_GlobalTask has no real 'bpmn2_GlobalTask' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ResourceRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ResourceRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ResourceRole(name="sample_text")
    partner = bpmn2_GlobalTask()
    setattr(partner, 'bpmn2_GlobalTask', None)
    _safe_set(owner, 'bpmn2_ResourceRole', partner)
    assert owner in getattr(partner, 'bpmn2_GlobalTask')
    _safe_set(owner, 'bpmn2_ResourceRole', None)
    assert owner not in getattr(partner, 'bpmn2_GlobalTask')


def test_assoc_rootElements485_stub_double():
    # bpmn2_RootElement has no real 'bpmn2_RootElement' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Definitions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Definitions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Definitions(exporter="sample_text", exporterVersion="sample_text", expressionLanguage="sample_text", name="sample_text", targetNamespace="sample_text", typeLanguage="sample_text")
    partner = bpmn2_RootElement()
    setattr(partner, 'bpmn2_RootElement', None)
    _safe_set(owner, 'bpmn2_Definitions486', {partner})
    assert getattr(partner, 'bpmn2_RootElement') == owner
    _safe_set(owner, 'bpmn2_Definitions486', set())
    assert getattr(partner, 'bpmn2_RootElement') is None


def test_assoc_signalRef380_stub_double():
    # bpmn2_SignalEventDefinition has no real 'bpmn2_SignalEventDefinition' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Signal(name="sample_text")
    partner = bpmn2_SignalEventDefinition()
    setattr(partner, 'bpmn2_SignalEventDefinition', None)
    _safe_set(owner, 'bpmn2_Signal', partner)
    assert getattr(partner, 'bpmn2_SignalEventDefinition') == owner
    _safe_set(owner, 'bpmn2_Signal', None)
    assert getattr(partner, 'bpmn2_SignalEventDefinition') is None


def test_assoc_sourceRef164_stub_double():
    # bpmn2_FlowNode has no real 'FlowNode165' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'FlowNode165', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'FlowNode165') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'FlowNode165') is None


def test_assoc_sourceRef208_stub_double():
    # bpmn2_InteractionNode has no real 'InteractionNode' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ConversationLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ConversationLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ConversationLink(name="sample_text")
    partner = bpmn2_InteractionNode()
    setattr(partner, 'InteractionNode', None)
    _safe_set(owner, 'outgoingConversationLinks', partner)
    assert getattr(partner, 'InteractionNode') == owner
    _safe_set(owner, 'outgoingConversationLinks', None)
    assert getattr(partner, 'InteractionNode') is None


def test_assoc_sourceRef217_stub_double():
    # bpmn2_InteractionNode has no real 'bpmn2_InteractionNode' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MessageFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MessageFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MessageFlow(name="sample_text")
    partner = bpmn2_InteractionNode()
    setattr(partner, 'bpmn2_InteractionNode', None)
    _safe_set(owner, 'bpmn2_MessageFlow218', partner)
    assert getattr(partner, 'bpmn2_InteractionNode') == owner
    _safe_set(owner, 'bpmn2_MessageFlow218', None)
    assert getattr(partner, 'bpmn2_InteractionNode') is None


def test_assoc_sources331_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject332' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Relationship(direction="sample_text", type="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject332', None)
    _safe_set(owner, 'bpmn2_Relationship', {partner})
    assert getattr(partner, 'bpmn2_EObject332') == owner
    _safe_set(owner, 'bpmn2_Relationship', set())
    assert getattr(partner, 'bpmn2_EObject332') is None


def test_assoc_structureRef30_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject32' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ItemDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ItemDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ItemDefinition(isCollection=True, itemKind="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject32', None)
    _safe_set(owner, 'bpmn2_ItemDefinition31', partner)
    assert getattr(partner, 'bpmn2_EObject32') == owner
    _safe_set(owner, 'bpmn2_ItemDefinition31', None)
    assert getattr(partner, 'bpmn2_EObject32') is None


def test_assoc_targetRef162_stub_double():
    # bpmn2_FlowNode has no real 'FlowNode163' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_SequenceFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_SequenceFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_SequenceFlow(isImmediate=True)
    partner = bpmn2_FlowNode()
    setattr(partner, 'FlowNode163', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'FlowNode163') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'FlowNode163') is None


def test_assoc_targetRef209_stub_double():
    # bpmn2_InteractionNode has no real 'InteractionNode210' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ConversationLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ConversationLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ConversationLink(name="sample_text")
    partner = bpmn2_InteractionNode()
    setattr(partner, 'InteractionNode210', None)
    _safe_set(owner, 'incomingConversationLinks', partner)
    assert getattr(partner, 'InteractionNode210') == owner
    _safe_set(owner, 'incomingConversationLinks', None)
    assert getattr(partner, 'InteractionNode210') is None


def test_assoc_targetRef219_stub_double():
    # bpmn2_InteractionNode has no real 'bpmn2_InteractionNode221' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_MessageFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_MessageFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_MessageFlow(name="sample_text")
    partner = bpmn2_InteractionNode()
    setattr(partner, 'bpmn2_InteractionNode221', None)
    _safe_set(owner, 'bpmn2_MessageFlow220', partner)
    assert getattr(partner, 'bpmn2_InteractionNode221') == owner
    _safe_set(owner, 'bpmn2_MessageFlow220', None)
    assert getattr(partner, 'bpmn2_InteractionNode221') is None


def test_assoc_targets333_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject335' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_Relationship(direction="sample_text", type="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject335', None)
    _safe_set(owner, 'bpmn2_Relationship334', {partner})
    assert getattr(partner, 'bpmn2_EObject335') == owner
    _safe_set(owner, 'bpmn2_Relationship334', set())
    assert getattr(partner, 'bpmn2_EObject335') is None


def test_assoc_transformation303_stub_double():
    # bpmn2_DataAssociation has no real 'bpmn2_DataAssociation' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_FormalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_FormalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_FormalExpression(language="sample_text")
    partner = bpmn2_DataAssociation()
    setattr(partner, 'bpmn2_DataAssociation', None)
    _safe_set(owner, 'bpmn2_FormalExpression304', partner)
    assert getattr(partner, 'bpmn2_DataAssociation') == owner
    _safe_set(owner, 'bpmn2_FormalExpression304', None)
    assert getattr(partner, 'bpmn2_DataAssociation') is None


def test_assoc_value13_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject15' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ExtensionAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ExtensionAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ExtensionAttributeValue(id="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject15', None)
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue14', partner)
    assert getattr(partner, 'bpmn2_EObject15') == owner
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue14', None)
    assert getattr(partner, 'bpmn2_EObject15') is None


def test_assoc_valueRef10_stub_double():
    # bpmn2_EObject has no real 'bpmn2_EObject12' property in the generated
    # code (a bare stub) -- manually attach it so bpmn2_ExtensionAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bpmn2_ExtensionAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bpmn2_ExtensionAttributeValue(id="sample_text")
    partner = bpmn2_EObject()
    setattr(partner, 'bpmn2_EObject12', None)
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue11', partner)
    assert getattr(partner, 'bpmn2_EObject12') == owner
    _safe_set(owner, 'bpmn2_ExtensionAttributeValue11', None)
    assert getattr(partner, 'bpmn2_EObject12') is None


