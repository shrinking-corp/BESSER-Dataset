#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    Activity,
    AdHocOrdering,
    Artifact,
    AssociationDirection,
    BaseElement,
    CallableElement,
    CatchEvent,
    Choreography,
    ChoreographyActivity,
    ChoreographyLoopType,
    Collaboration,
    ConversationNode,
    DataAssociation,
    Enum,
    Event,
    EventBasedGatewayType,
    EventDefinition,
    Expression,
    FlowElement,
    FlowElementsContainer,
    FlowNode,
    Gateway,
    GatewayDirection,
    GlobalTask,
    HumanPerformer,
    InteractionNode,
    ItemAwareElement,
    ItemKind,
    LoopCharacteristics,
    MultiInstanceBehavior,
    Performer,
    ProcessType,
    RelationshipDirection,
    ResourceRole,
    RootElement,
    SubProcess,
    Task,
    ThrowEvent,
    abstractmethod,
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
    date,
    datetime,
    time,
)


def test_0():
    var_1 = "It`[yyz@"
    var_2 = python_code_.bpmn2_Message()
    var_3 = python_code_.bpmn2_SendTask(implementation=var_1, bpmn2_SendTask843=var_2)
    assert isinstance(var_3, python_code_.bpmn2_SendTask)
    var_5 = python_code_.bpmn2_PartnerEntity()
    var_7 = python_code_.bpmn2_UserTask(implementation=var_5)
    assert isinstance(var_7, python_code_.bpmn2_UserTask)
    var_11 = python_code_.bpmn2_DataStore(
        capacity=True, isUnlimited=[], bpmn2_DataStore522=False
    )
    assert isinstance(var_11, python_code_.bpmn2_DataStore)
    var_12 = "W},1:jvy}HY^A/?4a"
    var_13 = float
    var_14 = python_code_.bpmn2_ExtensionAttributeDefinition(
        name=complex(-1686.05, -75.102),
        type=var_12,
        isReference=var_13,
        bpmn2_ExtensionAttributeDefinition="_bpmn2_FormalExpression__bpmn2_FormalExpression500,bpmn2_Monitoring787",
        ExtensionAttributeDefinition=("*4PxnsnV`", False, -301.65),
    )
    assert isinstance(var_14, python_code_.bpmn2_ExtensionAttributeDefinition)
    var_19 = python_code_.bpmn2_SubProcess(triggeredByEvent=-1461)
    assert isinstance(var_19, python_code_.bpmn2_SubProcess)


@pytest.mark.xfail(strict=True)
def test_1():
    var_2 = False
    var_3 = python_code_.bpmn2_DataStore(capacity=set(), isUnlimited=var_2)
    assert isinstance(var_3, python_code_.bpmn2_DataStore)
    var_5 = True
    var_6 = python_code_.bpmn2_StartEvent(isInterrupting=var_5, bpmn2_StartEvent=None)
    assert isinstance(var_6, python_code_.bpmn2_StartEvent)
    var_10 = python_code_.GlobalTask()
    var_11 = False
    var_12 = python_code_.bpmn2_EventBasedGateway
    python_code_.bpmn2_Extension(
        mustUnderstand=var_11, xsdDefinition=var_10, bpmn2_Extension=var_12
    )
    var_17 = "bpmn2_InclusiveGateway,_bpmn2_Activity__bpmn2_Activity311,bpmn2_ItemAwareElement646"
    var_18 = python_code_.bpmn2_GlobalScriptTask(script=var_17, scriptLanguage=var_17)
    assert isinstance(var_18, python_code_.bpmn2_GlobalScriptTask)
    python_code_.bpmn2_ExtensionDefinition(name=var_17, extensionDefinition=var_12)


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = python_code_.bpmn2_DocumentRoot()
    var_3 = "bKT6MT]%8"
    var_4 = python_code_.bpmn2_TextAnnotation(text=True, textFormat=var_3)
    assert isinstance(var_4, python_code_.bpmn2_TextAnnotation)
    var_5 = "zkBE?SH&]"
    python_code_.bpmn2_Import(
        importType=var_5,
        location=complex(2575.603954, -1289.007),
        namespace=var_3,
        bpmn2_Import=var_3,
    )
    var_23 = python_code_.bpmn2_ExclusiveGateway()
    var_25 = python_code_.bpmn2_ConversationNode()
    var_27 = python_code_.bpmn2_Escalation
    var_28 = python_code_.bpmn2_Competency()
    var_29 = {var_28, var_28, var_28}
    python_code_.bpmn2_Activity(
        completionQuantity=None,
        isForCompensation={"f": 2992.53, "L+H?": -1019},
        startQuantity=var_27,
        bpmn2_Activity=var_1,
        bpmn2_Activity296=var_4,
        bpmn2_Activity299=var_29,
        bpmn2_Activity303=var_25,
        bpmn2_Activity305="i",
        bpmn2_Activity430=var_23,
    )


def test_3():
    var_0 = python_code_.bpmn2_Category()
    var_1 = python_code_.bpmn2_GlobalScriptTask(
        script=b'\x9bo\xcd\xa4\x02\x95pDn\xc7\xdb\x94"5', scriptLanguage=var_0
    )
    assert isinstance(var_1, python_code_.bpmn2_GlobalScriptTask)
    var_4 = "Pr\t%&VGa9\tLluDqfRV"
    var_5 = python_code_.MultiInstanceBehavior
    var_6 = python_code_.bpmn2_DocumentRoot()
    var_7 = python_code_.bpmn2_Documentation(
        mixed=var_4,
        text=complex(284.33806, 279.12726),
        textFormat=var_5,
        bpmn2_Documentation=var_6,
    )
    assert isinstance(var_7, python_code_.bpmn2_Documentation)
    var_8 = False
    var_9 = python_code_.bpmn2_SubProcess(
        triggeredByEvent=var_8, bpmn2_SubProcess874=var_5
    )
    assert isinstance(var_9, python_code_.bpmn2_SubProcess)


def test_4():
    var_0 = python_code_.BaseElement()
    var_1 = True
    var_2 = "d\n9c598R7Eu|J)-x$"
    var_3 = python_code_.bpmn2_ResourceAssignmentExpression
    var_4 = python_code_.bpmn2_Process(
        isClosed=complex(-3153.4466, -2344.0),
        isExecutable=var_1,
        processType=var_2,
        bpmn2_Process783=var_3,
        bpmn2_Process789=var_2,
        bpmn2_Process878=var_0,
    )
    assert isinstance(var_4, python_code_.bpmn2_Process)
    var_7 = python_code_.bpmn2_ManualTask()
    var_11 = -3847
    var_12 = python_code_.bpmn2_DataStoreReference()
    var_13 = python_code_.bpmn2_DataStore(
        capacity=var_11,
        isUnlimited=complex(713.483447, -1216.488),
        bpmn2_DataStore522=var_12,
    )
    assert isinstance(var_13, python_code_.bpmn2_DataStore)
    var_14 = python_code_.bpmn2_StandardLoopCharacteristics(
        loopMaximum=-916.46, testBefore=var_1, bpmn2_StandardLoopCharacteristics=var_3
    )
    assert isinstance(var_14, python_code_.bpmn2_StandardLoopCharacteristics)
    var_17 = python_code_.bpmn2_DocumentRoot()
    var_18 = python_code_.bpmn2_Error(
        errorCode=var_7, bpmn2_Error=var_17, bpmn2_Error542="3a\x0cj!d0iS"
    )
    assert isinstance(var_18, python_code_.bpmn2_Error)
    var_19 = python_code_.bpmn2_FlowElement()
    var_23 = python_code_.bpmn2_CategoryValue(
        value=var_2, bpmn2_CategoryValue573=var_19
    )
    assert isinstance(var_23, python_code_.bpmn2_CategoryValue)
    var_24 = True
    var_25 = python_code_.bpmn2_FlowNode()
    var_26 = python_code_.bpmn2_SequenceFlow(
        isImmediate=var_24,
        bpmn2_SequenceFlow=var_3,
        bpmn2_SequenceFlow554={"cXuY": False},
        SequenceFlow582=var_3,
        outgoing=var_25,
        bpmn2_SequenceFlow849=var_0,
    )
    assert isinstance(var_26, python_code_.bpmn2_SequenceFlow)
    var_31 = python_code_.bpmn2_Association(
        associationDirection=1806.18, bpmn2_Association330=None
    )
    assert isinstance(var_31, python_code_.bpmn2_Association)
    var_37 = ".i8:g"
    var_38 = python_code_.bpmn2_Gateway(gatewayDirection=var_37)
    assert isinstance(var_38, python_code_.bpmn2_Gateway)
    var_41 = python_code_.bpmn2_UserTask(implementation=var_11)
    assert isinstance(var_41, python_code_.bpmn2_UserTask)
    var_43 = lambda *args, **kwargs: -1
    var_44 = python_code_.bpmn2_BoundaryEvent(
        cancelActivity=b"\xb3[\xdbYI\x01\xd1", BoundaryEvent=var_43
    )
    assert isinstance(var_44, python_code_.bpmn2_BoundaryEvent)
    var_45 = "bpmn2_OutputSet-_bpmn2_DataOutput__optionalOutputRefs"
    python_code_.bpmn2_StandardLoopCharacteristics(
        loopMaximum=var_45,
        testBefore=var_24,
        bpmn2_StandardLoopCharacteristics865=b"\xcfk\xb4B\xb3}\x88x\x18\x90\xf2\xb0",
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_2 = python_code_.bpmn2_Association
    var_3 = python_code_.bpmn2_DocumentRoot()
    var_4 = python_code_.bpmn2_Gateway(gatewayDirection=var_2, bpmn2_Gateway=var_3)
    assert isinstance(var_4, python_code_.bpmn2_Gateway)
    var_11 = True
    python_code_.bpmn2_DataInput(
        isCollection=var_11, whileExecutingInputRefs=-99, DataInput624="\nRm\\"
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.bpmn2_Position()
    var_2 = python_code_.bpmn2_CancelEventDefinition()
    var_3 = "Complex:bpmn2_ErrorEventDefinition541"
    var_4 = python_code_.bpmn2_FormalExpression(
        mixed=var_3,
        body=var_2,
        language=var_3,
        bpmn2_FormalExpression500={
            "_bpmn2_Process__bpmn2_Process795_bpmn2_Process__bpmn2_Process": 2141.75,
            '@xnlS=0k"!fnQr|-': 3942,
        },
    )
    assert isinstance(var_4, python_code_.bpmn2_FormalExpression)
    var_11 = python_code_.GatewayDirection.Unspecified
    var_12 = 3
    var_13 = python_code_.bpmn2_CorrelationProperty
    python_code_.bpmn2_Activity(
        completionQuantity=var_12,
        isForCompensation=var_0,
        startQuantity=var_12,
        bpmn2_Activity299=var_11,
        bpmn2_Activity313=None,
        bpmn2_Activity277=var_13,
        bpmn2_Activity287=complex(987.0, -1355.0),
        bpmn2_Activity430=var_2,
    )


def test_7():
    var_0 = python_code_.ThrowEvent()
    var_4 = "bpmn2_Definitions527"
    var_5 = len
    var_6 = python_code_.bpmn2_DocumentRoot()
    var_7 = python_code_.bpmn2_Definitions(
        exporter=var_4,
        exporterVersion=var_5,
        expressionLanguage=var_4,
        targetNamespace=var_0,
        typeLanguage=var_4,
        bpmn2_Definitions=var_6,
    )
    assert isinstance(var_7, python_code_.bpmn2_Definitions)


@pytest.mark.xfail(strict=True)
def test_8():
    var_3 = python_code_.bpmn2_ItemAwareElement()
    var_4 = False
    var_5 = python_code_.bpmn2_PartnerEntity
    var_6 = python_code_.bpmn2_DocumentRoot()
    var_7 = set()
    var_8 = lambda *args, **kwargs: True
    var_9 = python_code_.bpmn2_BoundaryEvent(
        cancelActivity=False, bpmn2_BoundaryEvent=var_6
    )
    assert isinstance(var_9, python_code_.bpmn2_BoundaryEvent)
    var_10 = python_code_.bpmn2_InputOutputSpecification()
    var_11 = python_code_.bpmn2_CompensateEventDefinition(waitForCompletion=var_4)
    assert isinstance(var_11, python_code_.bpmn2_CompensateEventDefinition)
    python_code_.bpmn2_Activity(
        completionQuantity=b"t..\x16\xbb-\xea\x1dG\xbd\xfb\xbbd^'=",
        isForCompensation=var_4,
        startQuantity=var_5,
        bpmn2_Activity=var_6,
        bpmn2_Activity293=[115.35, 1905],
        bpmn2_Activity299=var_4,
        bpmn2_Activity311=var_7,
        bpmn2_Activity313=var_8,
        Activity=var_9,
        bpmn2_Activity277=var_10,
        attachedToRef=["e K5]"],
        bpmn2_Activity287=var_3,
        bpmn2_Activity430=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = True
    var_1 = python_code_.bpmn2_Performer()
    var_2 = {var_1, var_1, var_1, var_1}
    var_3 = python_code_.bpmn2_InputOutputSpecification()
    python_code_.bpmn2_Activity(
        completionQuantity=-2252.54,
        isForCompensation=var_0,
        startQuantity="$O|VB8-:{\x0c|C5u@c0",
        bpmn2_Activity299={},
        bpmn2_Activity305=var_0,
        bpmn2_Activity308=var_2,
        bpmn2_Activity277=var_3,
        attachedToRef=True,
        bpmn2_Activity281=var_0,
    )
