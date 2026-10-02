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
    Abstraction,
    AcceptEventAction,
    Action,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    AggregationKind,
    Artifact,
    Association,
    Behavior,
    BehavioralFeature,
    BehavioredClassifier,
    CallAction,
    CallConcurrencyFeature,
    CentralBufferNode,
    Class,
    Classifier,
    CombinedFragment,
    CompleteDSLPckg_Abstraction,
    CompleteDSLPckg_AcceptCallAction,
    CompleteDSLPckg_AcceptEventAction,
    CompleteDSLPckg_Action,
    CompleteDSLPckg_ActionExecutionSpecification,
    CompleteDSLPckg_ActionInputPin,
    CompleteDSLPckg_Activity,
    CompleteDSLPckg_ActivityEdge,
    CompleteDSLPckg_ActivityFinalNode,
    CompleteDSLPckg_ActivityGroup,
    CompleteDSLPckg_ActivityNode,
    CompleteDSLPckg_ActivityParameterNode,
    CompleteDSLPckg_ActivityPartition,
    CompleteDSLPckg_Actor,
    CompleteDSLPckg_AddStructuralFeatureValueAction,
    CompleteDSLPckg_AddVariableValueAction,
    CompleteDSLPckg_AnyReceiveEvent,
    CompleteDSLPckg_Artifact,
    CompleteDSLPckg_Association,
    CompleteDSLPckg_AssociationClass,
    CompleteDSLPckg_Behavior,
    CompleteDSLPckg_BehaviorExecutionSpecification,
    CompleteDSLPckg_BehavioralFeature,
    CompleteDSLPckg_BehavioredClassifier,
    CompleteDSLPckg_BroadcastSignalAction,
    CompleteDSLPckg_CallAction,
    CompleteDSLPckg_CallBehaviorAction,
    CompleteDSLPckg_CallEvent,
    CompleteDSLPckg_CallOperationAction,
    CompleteDSLPckg_CentralBufferNode,
    CompleteDSLPckg_ChangeEvent,
    CompleteDSLPckg_Class,
    CompleteDSLPckg_Classifier,
    CompleteDSLPckg_Clause,
    CompleteDSLPckg_ClearStructuralFeatureAction,
    CompleteDSLPckg_ClearVariableAction,
    CompleteDSLPckg_Collaboration,
    CompleteDSLPckg_CollaborationUse,
    CompleteDSLPckg_CombinedFragment,
    CompleteDSLPckg_Comment,
    CompleteDSLPckg_CommunicationPath,
    CompleteDSLPckg_Component,
    CompleteDSLPckg_ComponentRealization,
    CompleteDSLPckg_ConditionalNode,
    CompleteDSLPckg_ConnectableElement,
    CompleteDSLPckg_ConnectionPointReference,
    CompleteDSLPckg_Connector,
    CompleteDSLPckg_ConnectorEnd,
    CompleteDSLPckg_ConsiderIgnoreFragment,
    CompleteDSLPckg_Constraint,
    CompleteDSLPckg_Continuation,
    CompleteDSLPckg_ControlFlow,
    CompleteDSLPckg_ControlNode,
    CompleteDSLPckg_CreateLinkAction,
    CompleteDSLPckg_CreateLinkObjectAction,
    CompleteDSLPckg_CreateObjectAction,
    CompleteDSLPckg_DataStoreNode,
    CompleteDSLPckg_DataType,
    CompleteDSLPckg_DecisionNode,
    CompleteDSLPckg_Dependency,
    CompleteDSLPckg_DeployedArtifact,
    CompleteDSLPckg_Deployment,
    CompleteDSLPckg_DeploymentSpecification,
    CompleteDSLPckg_DeploymentTarget,
    CompleteDSLPckg_DestroyLinkAction,
    CompleteDSLPckg_DestroyObjectAction,
    CompleteDSLPckg_DestructionOccurrenceSpecification,
    CompleteDSLPckg_Device,
    CompleteDSLPckg_DirectedRelationship,
    CompleteDSLPckg_Duration,
    CompleteDSLPckg_DurationConstraint,
    CompleteDSLPckg_DurationInterval,
    CompleteDSLPckg_DurationObservation,
    CompleteDSLPckg_Element,
    CompleteDSLPckg_ElementImport,
    CompleteDSLPckg_EncapsulatedClassifier,
    CompleteDSLPckg_Enumeration,
    CompleteDSLPckg_EnumerationLiteral,
    CompleteDSLPckg_Event,
    CompleteDSLPckg_ExceptionHandler,
    CompleteDSLPckg_ExecutableNode,
    CompleteDSLPckg_ExecutionEnvironment,
    CompleteDSLPckg_ExecutionOccurrenceSpecification,
    CompleteDSLPckg_ExecutionSpecification,
    CompleteDSLPckg_ExpansionNode,
    CompleteDSLPckg_ExpansionRegion,
    CompleteDSLPckg_Expression,
    CompleteDSLPckg_Extend,
    CompleteDSLPckg_ExtensionPoint,
    CompleteDSLPckg_Feature,
    CompleteDSLPckg_FinalNode,
    CompleteDSLPckg_FinalState,
    CompleteDSLPckg_FlowFinalNode,
    CompleteDSLPckg_ForkNode,
    CompleteDSLPckg_FunctionBehavior,
    CompleteDSLPckg_Gate,
    CompleteDSLPckg_GeneralOrdering,
    CompleteDSLPckg_Generalization,
    CompleteDSLPckg_GeneralizationSet,
    CompleteDSLPckg_Include,
    CompleteDSLPckg_InitialNode,
    CompleteDSLPckg_InputPin,
    CompleteDSLPckg_InstanceSpecification,
    CompleteDSLPckg_InstanceValue,
    CompleteDSLPckg_Interaction,
    CompleteDSLPckg_InteractionConstraint,
    CompleteDSLPckg_InteractionFragment,
    CompleteDSLPckg_InteractionOperand,
    CompleteDSLPckg_InteractionUse,
    CompleteDSLPckg_Interface,
    CompleteDSLPckg_InterfaceRealization,
    CompleteDSLPckg_InterruptibleActivityRegion,
    CompleteDSLPckg_Interval,
    CompleteDSLPckg_IntervalConstraint,
    CompleteDSLPckg_InvocationAction,
    CompleteDSLPckg_JoinNode,
    CompleteDSLPckg_Lifeline,
    CompleteDSLPckg_LinkAction,
    CompleteDSLPckg_LinkEndCreationData,
    CompleteDSLPckg_LinkEndData,
    CompleteDSLPckg_LinkEndDestructionData,
    CompleteDSLPckg_LiteralBoolean,
    CompleteDSLPckg_LiteralInteger,
    CompleteDSLPckg_LiteralNull,
    CompleteDSLPckg_LiteralReal,
    CompleteDSLPckg_LiteralSpecification,
    CompleteDSLPckg_LiteralString,
    CompleteDSLPckg_LiteralUnilimitedNatural,
    CompleteDSLPckg_LoopNode,
    CompleteDSLPckg_Manifestation,
    CompleteDSLPckg_MergeNode,
    CompleteDSLPckg_Message,
    CompleteDSLPckg_MessageEnd,
    CompleteDSLPckg_MessageEvent,
    CompleteDSLPckg_MessageOccurrenceSpecification,
    CompleteDSLPckg_MultiplicityElement,
    CompleteDSLPckg_NamedElement,
    CompleteDSLPckg_Namespace,
    CompleteDSLPckg_Node,
    CompleteDSLPckg_ObjectFlow,
    CompleteDSLPckg_ObjectNode,
    CompleteDSLPckg_Observation,
    CompleteDSLPckg_OccurenceSpecification,
    CompleteDSLPckg_OpaqueAction,
    CompleteDSLPckg_OpaqueBehavior,
    CompleteDSLPckg_OpaqueExpression,
    CompleteDSLPckg_Operation,
    CompleteDSLPckg_OutputPin,
    CompleteDSLPckg_Package,
    CompleteDSLPckg_PackageImport,
    CompleteDSLPckg_PackageMerge,
    CompleteDSLPckg_PackageableElement,
    CompleteDSLPckg_Parameter,
    CompleteDSLPckg_ParameterSet,
    CompleteDSLPckg_PartDecomposition,
    CompleteDSLPckg_Pin,
    CompleteDSLPckg_Port,
    CompleteDSLPckg_PrimitiveType,
    CompleteDSLPckg_Property,
    CompleteDSLPckg_ProtocolConformance,
    CompleteDSLPckg_ProtocolStateMachine,
    CompleteDSLPckg_ProtocolTransition,
    CompleteDSLPckg_Pseudostate,
    CompleteDSLPckg_QualifierValue,
    CompleteDSLPckg_RaiseExceptionAction,
    CompleteDSLPckg_ReadExtendAction,
    CompleteDSLPckg_ReadLinkAction,
    CompleteDSLPckg_ReadLinkObjectEndAction,
    CompleteDSLPckg_ReadLinkObjectEndQualifierAction,
    CompleteDSLPckg_ReadSelfAction,
    CompleteDSLPckg_ReadStructuralFeatureAction,
    CompleteDSLPckg_ReadVariableAction,
    CompleteDSLPckg_ReadlsClassifiedObjectAction,
    CompleteDSLPckg_Realization,
    CompleteDSLPckg_Reception,
    CompleteDSLPckg_ReclassifyObjectAction,
    CompleteDSLPckg_RedefinableElement,
    CompleteDSLPckg_ReduceAction,
    CompleteDSLPckg_Region,
    CompleteDSLPckg_Relationship,
    CompleteDSLPckg_RemoveStructuralFeatureValueAction,
    CompleteDSLPckg_RemoveVariableValueAction,
    CompleteDSLPckg_ReplyAction,
    CompleteDSLPckg_SendObjectAction,
    CompleteDSLPckg_SendSignalAction,
    CompleteDSLPckg_SequenceNode,
    CompleteDSLPckg_Signal,
    CompleteDSLPckg_SignalEvent,
    CompleteDSLPckg_Slot,
    CompleteDSLPckg_StartClassifierBehaviorAction,
    CompleteDSLPckg_StartObjectBehaviorAction,
    CompleteDSLPckg_State,
    CompleteDSLPckg_StateInvariant,
    CompleteDSLPckg_StateMachine,
    CompleteDSLPckg_StructuralFeature,
    CompleteDSLPckg_StructuralFeatureAction,
    CompleteDSLPckg_StructuredActivityNode,
    CompleteDSLPckg_StructuredClassifier,
    CompleteDSLPckg_Substitution,
    CompleteDSLPckg_TestIdentityAction,
    CompleteDSLPckg_TimeConstraint,
    CompleteDSLPckg_TimeEvent,
    CompleteDSLPckg_TimeExpression,
    CompleteDSLPckg_TimeInterval,
    CompleteDSLPckg_TimeObservation,
    CompleteDSLPckg_Transition,
    CompleteDSLPckg_Trigger,
    CompleteDSLPckg_Type,
    CompleteDSLPckg_TypedElement,
    CompleteDSLPckg_UnmarshallAction,
    CompleteDSLPckg_Usage,
    CompleteDSLPckg_UseCase,
    CompleteDSLPckg_ValuePin,
    CompleteDSLPckg_ValueSpecification,
    CompleteDSLPckg_ValueSpecificationAction,
    CompleteDSLPckg_Variable,
    CompleteDSLPckg_VariableAction,
    CompleteDSLPckg_Vertex,
    CompleteDSLPckg_WriteLinkAction,
    CompleteDSLPckg_WriteStructuralFeatureAction,
    CompleteDSLPckg_WriteVariableAction,
    ConnectableElement,
    ConnectorKind,
    Constraint,
    ControlNode,
    CreateLinkAction,
    DataType,
    Dependency,
    DeployedArtifact,
    DeploymentTarget,
    DirectedRelationship,
    Element,
    EncapsulatedClassifier,
    Enum,
    Event,
    ExecutableNode,
    ExecutionSpecification,
    ExpansionKind,
    Feature,
    FinalNode,
    InputPin,
    InstanceSpecification,
    InteractionFragment,
    InteractionOperandKind,
    InteractionUse,
    Interval,
    IntervalConstraint,
    InvocationAction,
    LinkAction,
    LinkEndData,
    LiteralSpecification,
    MessageEnd,
    MessageEvent,
    MessageKind,
    MessageOccurrenceSpecification,
    MessageSort,
    MultiplicityElement,
    NamedElement,
    Namespace,
    Node,
    ObjectNode,
    ObjectNodeOrderingKind,
    Observation,
    OccurenceSpecification,
    OpaqueBehavior,
    PackageableElement,
    ParameterEffectKind,
    Pin,
    Property,
    Realization,
    RedefinableElement,
    Relationship,
    State,
    StateMachine,
    StructuralFeature,
    StructuralFeatureAction,
    StructuredActivityNode,
    StructuredClassifier,
    Transition,
    TransitionKind,
    Type,
    TypedElement,
    ValueSpecification,
    VariableAction,
    Vertex,
    VisibilityKind,
    WriteLinkAction,
    WriteStructuralFeatureAction,
    WriteVariableAction,
    abstractmethod,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_3 = python_code_.IntervalConstraint()
    var_5 = python_code_.CompleteDSLPckg_Collaboration()
    var_9 = False
    var_10 = python_code_.CompleteDSLPckg_ActivityGroup()
    var_11 = {var_10, var_10, var_10, var_10}
    var_12 = python_code_.CompleteDSLPckg_Activity(
        isReadOnly=var_3,
        isSingleExecution=var_9,
        CompleteDSLPckg_Activity721=var_10,
        CompleteDSLPckg_Activity683=var_11,
    )
    assert isinstance(var_12, python_code_.CompleteDSLPckg_Activity)
    var_23 = python_code_.CompleteDSLPckg_InputPin()
    var_24 = python_code_.Relationship
    python_code_.CompleteDSLPckg_ReclassifyObjectAction(
        isReplaceAll=var_5,
        CompleteDSLPckg_ReclassifyObjectAction=var_23,
        CompleteDSLPckg_ReclassifyObjectAction515=2632,
        CompleteDSLPckg_ReclassifyObjectAction518=var_24,
    )


def test_1():
    var_1 = python_code_.CompleteDSLPckg_ValueSpecification()
    var_5 = python_code_.Classifier()
    var_6 = python_code_.CompleteDSLPckg_Feature(isStatic=-1403)
    assert isinstance(var_6, python_code_.CompleteDSLPckg_Feature)
    var_11 = python_code_.CompleteDSLPckg_MessageEnd()
    var_12 = python_code_.CompleteDSLPckg_Message(
        messageKind=var_5, messageSort=var_1, CompleteDSLPckg_Message932=var_11
    )
    assert isinstance(var_12, python_code_.CompleteDSLPckg_Message)
    var_14 = python_code_.CompleteDSLPckg_DurationInterval()
    var_15 = python_code_.CompleteDSLPckg_DurationConstraint(
        firstEvent=var_11, CompleteDSLPckg_DurationConstraint=var_14
    )
    assert isinstance(var_15, python_code_.CompleteDSLPckg_DurationConstraint)
    var_18 = python_code_.CompleteDSLPckg_StateMachine()
    var_26 = "@<\x0c0{\t`)L+,-KLb"
    var_27 = lambda *args, **kwargs: False
    var_28 = python_code_.CompleteDSLPckg_PackageImport(
        visibility=var_26, CompleteDSLPckg_PackageImport=var_27
    )
    assert isinstance(var_28, python_code_.CompleteDSLPckg_PackageImport)
    var_30 = python_code_.CompleteDSLPckg_ElementImport(
        visibility=var_26,
        alias=var_18,
        CompleteDSLPckg_ElementImport=var_27,
        ElementImport=var_27,
    )
    assert isinstance(var_30, python_code_.CompleteDSLPckg_ElementImport)


def test_2():
    var_1 = False
    var_2 = python_code_.CompleteDSLPckg_StructuralFeature(isReadOnly=var_1)
    assert isinstance(var_2, python_code_.CompleteDSLPckg_StructuralFeature)
    var_5 = python_code_.CompleteDSLPckg_ActivityNode
    var_6 = python_code_.CompleteDSLPckg_DurationObservation(firstEvent=var_5)
    assert isinstance(var_6, python_code_.CompleteDSLPckg_DurationObservation)
    var_7 = False
    var_8 = python_code_.CompleteDSLPckg_ConditionalNode(
        isDeterminate=var_7,
        isAssumed=var_7,
        CompleteDSLPckg_ConditionalNode842=(False, ""),
    )
    assert isinstance(var_8, python_code_.CompleteDSLPckg_ConditionalNode)
    var_10 = python_code_.CompleteDSLPckg_Expression(symbol=[884, "7:\\AVP"])
    assert isinstance(var_10, python_code_.CompleteDSLPckg_Expression)


def test_3():
    var_4 = (
        lambda *args, **kwargs: "_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier93 synchCall"
    )
    var_5 = python_code_.CompleteDSLPckg_Comment(body=var_4)
    assert isinstance(var_5, python_code_.CompleteDSLPckg_Comment)
    var_11 = python_code_.CompleteDSLPckg_JoinNode(
        isCombineDuplicate=var_4, CompleteDSLPckg_JoinNode=()
    )
    assert isinstance(var_11, python_code_.CompleteDSLPckg_JoinNode)
    var_14 = True
    var_15 = False
    var_16 = True
    var_17 = python_code_.CompleteDSLPckg_ActivityGroup()
    var_18 = python_code_.CompleteDSLPckg_Activity(
        isReadOnly=var_15, isSingleExecution=var_16, CompleteDSLPckg_Activity721=var_17
    )
    assert isinstance(var_18, python_code_.CompleteDSLPckg_Activity)
    var_19 = python_code_.CompleteDSLPckg_StructuredActivityNode(
        mustIsolate=var_14, CompleteDSLPckg_StructuredActivityNode=var_18
    )
    assert isinstance(var_19, python_code_.CompleteDSLPckg_StructuredActivityNode)


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = True
    var_1 = python_code_.CompleteDSLPckg_ActivityPartition()
    var_2 = {var_1, var_1, var_1, var_1}
    var_3 = python_code_.CompleteDSLPckg_Activity(
        isReadOnly=None,
        isSingleExecution=var_0,
        CompleteDSLPckg_Activity=None,
        CompleteDSLPckg_Activity687=var_2,
    )
    assert isinstance(var_3, python_code_.CompleteDSLPckg_Activity)
    python_code_.CompleteDSLPckg_StructuredActivityNode(
        mustIsolate=var_0,
        CompleteDSLPckg_StructuredActivityNode799=var_3,
        CompleteDSLPckg_StructuredActivityNode805=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_2 = "_CompleteDSLPckg_MultiplicityElement__owningUpper._CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode802.lowerValue"
    var_3 = "0ayvd51s"
    var_4 = python_code_.CompleteDSLPckg_ElementImport(
        visibility=var_2, alias=var_3, elementImport=["WKk^<7|G", 29.16]
    )
    assert isinstance(var_4, python_code_.CompleteDSLPckg_ElementImport)
    var_13 = python_code_.MessageKind.found
    var_17 = False
    var_18 = -1247
    var_19 = python_code_.CompleteDSLPckg_Type()
    var_20 = python_code_.CompleteDSLPckg_ProtocolStateMachine
    var_21 = python_code_.CompleteDSLPckg_Constraint()
    var_22 = {var_21}
    var_23 = python_code_.CompleteDSLPckg_Class()
    python_code_.CompleteDSLPckg_Operation(
        isQuery=var_17,
        isOrdered={},
        isUnique=var_13,
        upper=var_18,
        lower=var_18,
        CompleteDSLPckg_Operation=var_19,
        CompleteDSLPckg_Operation151=var_20,
        CompleteDSLPckg_Operation154=var_22,
        Operation=var_23,
    )


def test_6():
    var_0 = True
    var_1 = python_code_.CompleteDSLPckg_Feature(isStatic=var_0)
    assert isinstance(var_1, python_code_.CompleteDSLPckg_Feature)
    var_2 = python_code_.CompleteDSLPckg_Realization()
    var_5 = python_code_.CompleteDSLPckg_Device()
    var_9 = "^\x0b!s.$](\\6T@jKb05"
    var_10 = python_code_.CompleteDSLPckg_Message(
        messageKind=var_9, messageSort=var_2, CompleteDSLPckg_Message934=var_5
    )
    assert isinstance(var_10, python_code_.CompleteDSLPckg_Message)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.CompleteDSLPckg_BehavioredClassifier()
    var_1 = python_code_.CompleteDSLPckg_Constraint()
    var_2 = {var_1, var_1, var_1, var_1}
    var_3 = False
    var_4 = lambda *args, **kwargs: "p.R"
    var_5 = python_code_.CompleteDSLPckg_ConnectionPointReference()
    var_6 = python_code_.CompleteDSLPckg_StateMachine()
    var_7 = False
    var_8 = python_code_.CompleteDSLPckg_Pseudostate()
    var_9 = python_code_.CompleteDSLPckg_State(
        isComposite=var_3,
        isOrthogonal=var_7,
        isSimple=var_6,
        isSubmachineState=var_4,
        CompleteDSLPckg_State627=var_8,
        CompleteDSLPckg_State635=var_5,
        CompleteDSLPckg_State661=var_1,
        CompleteDSLPckg_State663=var_4,
    )
    assert isinstance(var_9, python_code_.CompleteDSLPckg_State)
    python_code_.CompleteDSLPckg_State(
        isComposite=var_3,
        isOrthogonal=var_3,
        isSimple=var_3,
        isSubmachineState=var_3,
        CompleteDSLPckg_State591=var_4,
        CompleteDSLPckg_State627=var_0,
        CompleteDSLPckg_State635=var_5,
        CompleteDSLPckg_State637=var_4,
        CompleteDSLPckg_State640=var_2,
        CompleteDSLPckg_State=var_6,
        CompleteDSLPckg_State649=var_2,
        CompleteDSLPckg_State658=var_4,
        CompleteDSLPckg_State665=var_9,
        CompleteDSLPckg_State663=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_1 = python_code_.CompleteDSLPckg_ReadExtendAction()
    var_6 = "OT$6_V>s+c"
    python_code_.CompleteDSLPckg_Message(
        messageKind=var_6,
        messageSort=b"\xab\xaf\x86\x90x\x96lr",
        CompleteDSLPckg_Message=var_1,
    )


def test_9():
    var_0 = lambda *args, **kwargs: []
    var_1 = "_CompleteDSLPckg_Classifier__substitutingClassifier"
    var_2 = python_code_.CompleteDSLPckg_OpaqueBehavior(body=var_0, language=var_1)
    assert isinstance(var_2, python_code_.CompleteDSLPckg_OpaqueBehavior)
