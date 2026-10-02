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
    date,
    datetime,
    time,
)


def test_0():
    var_0 = lambda *args, **kwargs: 1007
    var_1 = python_code_.bpmn2_Artifact()
    var_2 = {var_1, var_1}
    var_3 = python_code_.bpmn2_SubProcess(
        triggeredByEvent=var_0, bpmn2_SubProcess=var_2
    )
    assert isinstance(var_3, python_code_.bpmn2_SubProcess)
    var_4 = python_code_.bpmn2_AdHocSubProcess(
        ordering=-498, cancelRemainingInstances=var_3
    )
    assert isinstance(var_4, python_code_.bpmn2_AdHocSubProcess)


def test_1():
    var_1 = python_code_.bpmn2_SequenceFlow(
        isImmediate="_bpmn2_Category__bpmn2_Category"
    )
    assert isinstance(var_1, python_code_.bpmn2_SequenceFlow)
    var_2 = python_code_.bpmn2_Category(name=set())
    assert isinstance(var_2, python_code_.bpmn2_Category)
    var_3 = lambda *args, **kwargs: "\r:"
    var_4 = python_code_.bpmn2_Association(associationDirection=var_3)
    assert isinstance(var_4, python_code_.bpmn2_Association)
    var_6 = "&5^3\x0b?,X,Xn\nj4~4"
    var_7 = python_code_.bpmn2_Escalation(
        name=var_6,
        escalationCode=None,
        id=var_6,
        bpmn2_Escalation=-1868,
        bpmn2_Escalation356=False,
    )
    assert isinstance(var_7, python_code_.bpmn2_Escalation)
    var_8 = False
    var_9 = python_code_.bpmn2_ResourceParameter(
        name=b"JN8pc\x12\xa5\xa3\x99TB_\xc5(s\xa5\x17\x12", isRequired=var_8
    )
    assert isinstance(var_9, python_code_.bpmn2_ResourceParameter)


def test_2():
    var_1 = lambda *args, **kwargs: -4299
    var_2 = python_code_.bpmn2_UserTask(implementation=var_1)
    assert isinstance(var_2, python_code_.bpmn2_UserTask)


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = "I#b}A:'dK`IcHk"
    var_1 = python_code_.bpmn2_MessageEventDefinition()
    var_2 = python_code_.bpmn2_Operation(
        name=var_0, bpmn2_Operation24=var_0, bpmn2_Operation377=var_1
    )
    assert isinstance(var_2, python_code_.bpmn2_Operation)
    var_3 = python_code_.Collaboration()
    var_6 = python_code_.bpmn2_CategoryValue(value=-185)
    assert isinstance(var_6, python_code_.bpmn2_CategoryValue)
    var_9 = False
    var_10 = python_code_.bpmn2_LoopCharacteristics()
    var_11 = lambda *args, **kwargs: -2113
    var_12 = python_code_.bpmn2_InputOutputSpecification()
    python_code_.bpmn2_Activity(
        isForCompensation=var_9,
        startQuantity=var_3,
        completionQuantity=complex(2114.4835182, 1728.4),
        bpmn2_Activity=var_10,
        bpmn2_Activity271=var_11,
        bpmn2_Activity280=var_12,
        bpmn2_Activity284=var_11,
        bpmn2_Activity286=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.bpmn2_LoopCharacteristics()
    var_1 = python_code_.bpmn2_ResourceAssignmentExpression(id=var_0)
    var_2 = "%@\\o$d[\\"
    var_3 = python_code_.bpmn2_DataStore(
        capacity="W,,T/aR$qqY}HS;cj", isUnlimited=var_1, name=var_2
    )
    assert isinstance(var_3, python_code_.bpmn2_DataStore)
    var_4 = "aG>7-"
    var_5 = python_code_.bpmn2_Monitoring()
    var_6 = python_code_.bpmn2_CorrelationSubscription()
    var_7 = {var_6, var_6, var_6}
    var_8 = python_code_.bpmn2_Process(
        isClosed=None,
        isExecutable=("o\nP}~7/xCajA", 435, False),
        processType=var_4,
        bpmn2_Process113=var_5,
        bpmn2_Process115=[],
        bpmn2_Process118=var_1,
        bpmn2_Process120=complex(-90.0, -3.7564),
        bpmn2_Process127=var_7,
        decomposes=var_7,
    )
    assert isinstance(var_8, python_code_.bpmn2_Process)
    var_9 = python_code_.bpmn2_Property(name=-1856.54, bpmn2_Property=var_8)
    assert isinstance(var_9, python_code_.bpmn2_Property)
    var_11 = python_code_.bpmn2_BusinessRuleTask(
        implementation=complex(-84.81509, 2658.7)
    )
    assert isinstance(var_11, python_code_.bpmn2_BusinessRuleTask)
    var_12 = True
    var_13 = "1@*a=W= :XGm~"
    var_14 = python_code_.bpmn2_ItemDefinition(itemKind=var_13, isCollection=var_12)
    assert isinstance(var_14, python_code_.bpmn2_ItemDefinition)
    var_15 = "bpmn2_ItemDefinition102"
    var_16 = python_code_.bpmn2_Resource(name=var_2)
    assert isinstance(var_16, python_code_.bpmn2_Resource)
    python_code_.bpmn2_ResourceRole(
        name=var_15,
        bpmn2_ResourceRole93=var_16,
        bpmn2_ResourceRole97=True,
        bpmn2_ResourceRole123=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_1 = python_code_.ResourceRole()
    var_2 = python_code_.Artifact
    var_3 = python_code_.bpmn2_ResourceParameter(
        name=-3493.48,
        isRequired=var_2,
        bpmn2_ResourceParameter=var_1,
        bpmn2_ResourceParameter107=var_2,
    )
    assert isinstance(var_3, python_code_.bpmn2_ResourceParameter)
    var_4 = python_code_.bpmn2_StartEvent(isInterrupting=var_2)
    assert isinstance(var_4, python_code_.bpmn2_StartEvent)
    var_6 = python_code_.bpmn2_GlobalScriptTask(scriptLanguage=var_1, script=var_2)
    assert isinstance(var_6, python_code_.bpmn2_GlobalScriptTask)
    var_7 = python_code_.FlowElement()
    var_8 = "_bpmn2_ItemDefinition__bpmn2_ItemDefinition34:_bpmn2_CategoryValue__bpmn2_CategoryValue:bpmn2_ComplexGateway"
    var_9 = python_code_.bpmn2_Relationship(type="", direction=var_8)
    assert isinstance(var_9, python_code_.bpmn2_Relationship)
    var_13 = python_code_.bpmn2_PartnerEntity(name=var_6)
    assert isinstance(var_13, python_code_.bpmn2_PartnerEntity)
    var_20 = python_code_.bpmn2_Property(name=var_8)
    assert isinstance(var_20, python_code_.bpmn2_Property)
    var_21 = python_code_.bpmn2_MessageFlowAssociation()
    var_22 = {var_21}
    var_23 = python_code_.bpmn2_CallConversation()
    var_24 = python_code_.bpmn2_Collaboration(
        name=var_8,
        isClosed=set(),
        bpmn2_Collaboration174=var_22,
        bpmn2_Collaboration387=var_23,
    )
    assert isinstance(var_24, python_code_.bpmn2_Collaboration)
    var_25 = python_code_.bpmn2_ScriptTask(scriptFormat=-830, script=var_2)
    assert isinstance(var_25, python_code_.bpmn2_ScriptTask)
    var_27 = python_code_.bpmn2_EndPoint()
    var_33 = "bpmn2_ExtensionDefinition337"
    var_34 = python_code_.bpmn2_InputOutputSpecification()
    var_35 = python_code_.bpmn2_OutputSet(
        name=var_33,
        OutputSet82=var_7,
        bpmn2_OutputSet=var_34,
        bpmn2_OutputSet289={True},
    )
    assert isinstance(var_35, python_code_.bpmn2_OutputSet)
    var_36 = lambda *args, **kwargs: False
    var_37 = python_code_.bpmn2_MessageFlow(name=var_36, bpmn2_MessageFlow=-2662)
    assert isinstance(var_37, python_code_.bpmn2_MessageFlow)
    python_code_.bpmn2_ResourceRole(
        name=var_8, bpmn2_ResourceRole95=var_27, bpmn2_ResourceRole272=var_23
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.bpmn2_Assignment()
    var_1 = "bpmn2_DataOutput441"
    var_2 = python_code_.bpmn2_Message
    var_3 = python_code_.bpmn2_CorrelationKey(
        name=var_1,
        bpmn2_CorrelationKey=var_2,
        bpmn2_CorrelationKey260={
            "_bpmn2_Participant__bpmn2_Participant199,bpmn2_CallableElement41,_bpmn2_SendTask__bpmn2_SendTask468": 335,
            "_bpmn2_Participant__bpmn2_Participant401bpmn2_ChoreographyActivity_bpmn2_Participant__bpmn2_Participant189bpmn2_ItemAwareElement432": -2716.76,
        },
    )
    assert isinstance(var_3, python_code_.bpmn2_CorrelationKey)
    var_4 = python_code_.bpmn2_InputOutputBinding(id=var_1)
    var_5 = python_code_.bpmn2_DataInput(name=-4758.3, isCollection=var_2)
    assert isinstance(var_5, python_code_.bpmn2_DataInput)
    python_code_.bpmn2_InputSet(
        name=var_3,
        InputSet76=var_0,
        bpmn2_InputSet85=var_4,
        InputSet=var_5,
        InputSet62=var_3,
        InputSet64=b"\r\xb7\xd1\xb3\xf8w\xc7\xbe\xae\x80H\xf5A\xf7\x00",
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.bpmn2_GlobalChoreographyTask()
    var_1 = python_code_.bpmn2_Gateway(gatewayDirection=var_0)
    assert isinstance(var_1, python_code_.bpmn2_Gateway)
    var_2 = ""
    var_3 = python_code_.bpmn2_Resource(
        name=var_0, bpmn2_Resource=complex(656.040833, 3984.2)
    )
    assert isinstance(var_3, python_code_.bpmn2_Resource)
    var_4 = "bpmn2_ConversationNode235 _bpmn2_Collaboration__bpmn2_Collaboration167 DataOutput"
    var_5 = python_code_.bpmn2_SequenceFlow
    var_6 = python_code_.bpmn2_Participant(
        name=var_4,
        bpmn2_Participant=var_4,
        bpmn2_Participant233=var_0,
        bpmn2_Participant415=var_0,
        bpmn2_Participant396=var_5,
    )
    assert isinstance(var_6, python_code_.bpmn2_Participant)
    var_7 = set()
    python_code_.bpmn2_Process(
        isClosed="bpmn2_Message224 FlowElement",
        isExecutable={
            "bpmn2_Rendering321_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue14bpmn2_DataOutputAssociation_bpmn2_BaseElement__bpmn2_BaseElement5": 491.26
        },
        processType=var_2,
        bpmn2_Process202=var_6,
        bpmn2_Process115=var_7,
        bpmn2_Process122={
            "Physical-bpmn2_LoopCharacteristics-_bpmn2_Resource__bpmn2_Resource": False,
            "bpmn2_ConversationAssociation226-bpmn2_MultiInstanceLoopCharacteristics-bpmn2_Resource": 2181.83,
        },
        decomposedBy=3,
    )


def test_8():
    var_0 = "Baz7fYYgXyG"
    var_1 = python_code_.bpmn2_MessageFlowAssociation()
    var_2 = python_code_.bpmn2_MessageFlow(
        name=var_0, bpmn2_MessageFlow213=var_1, bpmn2_MessageFlow218=[]
    )
    assert isinstance(var_2, python_code_.bpmn2_MessageFlow)
    var_3 = 'ycY<rs0G}"nN?'
    var_4 = lambda *args, **kwargs: -1277
    var_5 = python_code_.bpmn2_CorrelationProperty(
        name=var_3, bpmn2_CorrelationProperty=var_4, bpmn2_CorrelationProperty245=var_4
    )
    assert isinstance(var_5, python_code_.bpmn2_CorrelationProperty)


@pytest.mark.xfail(strict=True)
def test_9():
    var_3 = python_code_.bpmn2_ConditionalEventDefinition()
    var_5 = True
    var_6 = python_code_.bpmn2_StartEvent(isInterrupting=var_5)
    assert isinstance(var_6, python_code_.bpmn2_StartEvent)
    var_8 = python_code_.Event
    var_9 = set()
    python_code_.bpmn2_Collaboration(
        name=[3],
        isClosed=var_8,
        bpmn2_Collaboration169=var_9,
        bpmn2_Collaboration172=var_3,
        bpmn2_Collaboration178=var_5,
        bpmn2_Collaboration182=[],
    )
