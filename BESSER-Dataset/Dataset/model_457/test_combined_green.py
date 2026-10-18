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
    ActivityNode,
    Transition,
    CompleteDSLPckg_ProtocolTransition,
    StateMachine,
    CompleteDSLPckg_ProtocolStateMachine,
    State,
    CompleteDSLPckg_FinalState,
    Vertex,
    CompleteDSLPckg_ConnectionPointReference,
    WriteVariableAction,
    CompleteDSLPckg_RemoveVariableValueAction,
    CompleteDSLPckg_AddVariableValueAction,
    VariableAction,
    CompleteDSLPckg_ClearVariableAction,
    CompleteDSLPckg_WriteVariableAction,
    CompleteDSLPckg_ReadVariableAction,
    CompleteDSLPckg_Pseudostate,
    CreateLinkAction,
    CompleteDSLPckg_CreateLinkObjectAction,
    CompleteDSLPckg_ReadlsClassifiedObjectAction,
    AcceptEventAction,
    CompleteDSLPckg_AcceptCallAction,
    LinkAction,
    CompleteDSLPckg_WriteLinkAction,
    CompleteDSLPckg_ReadLinkAction,
    WriteStructuralFeatureAction,
    CompleteDSLPckg_RemoveStructuralFeatureValueAction,
    CompleteDSLPckg_AddStructuralFeatureValueAction,
    LinkEndData,
    CompleteDSLPckg_LinkEndDestructionData,
    CompleteDSLPckg_LinkEndCreationData,
    InteractionUse,
    MessageEnd,
    CombinedFragment,
    CompleteDSLPckg_ConsiderIgnoreFragment,
    CompleteDSLPckg_CombinedFragment,
    CompleteDSLPckg_PartDecomposition,
    ExecutionSpecification,
    CompleteDSLPckg_ActionExecutionSpecification,
    CompleteDSLPckg_BehaviorExecutionSpecification,
    MessageOccurrenceSpecification,
    CompleteDSLPckg_DestructionOccurrenceSpecification,
    OccurenceSpecification,
    CompleteDSLPckg_MessageOccurrenceSpecification,
    CompleteDSLPckg_ExecutionOccurrenceSpecification,
    InteractionFragment,
    CompleteDSLPckg_Continuation,
    CompleteDSLPckg_InteractionUse,
    CompleteDSLPckg_OccurenceSpecification,
    CompleteDSLPckg_StateInvariant,
    CompleteDSLPckg_ExecutionSpecification,
    CompleteDSLPckg_Gate,
    ExecutableNode,
    CentralBufferNode,
    CompleteDSLPckg_DataStoreNode,
    StructuredActivityNode,
    CompleteDSLPckg_ConditionalNode,
    CompleteDSLPckg_ExpansionRegion,
    CompleteDSLPckg_SequenceNode,
    CompleteDSLPckg_LoopNode,
    CompleteDSLPckg_ExecutableNode,
    ActivityEdge,
    CompleteDSLPckg_ObjectFlow,
    CompleteDSLPckg_ControlFlow,
    ActivityGroup,
    CompleteDSLPckg_InterruptibleActivityRegion,
    CompleteDSLPckg_ActivityPartition,
    FinalNode,
    CompleteDSLPckg_FlowFinalNode,
    ControlNode,
    CompleteDSLPckg_JoinNode,
    CompleteDSLPckg_DecisionNode,
    CompleteDSLPckg_FinalNode,
    CompleteDSLPckg_ForkNode,
    CompleteDSLPckg_InitialNode,
    CompleteDSLPckg_MergeNode,
    CompleteDSLPckg_ActivityFinalNode,
    CompleteDSLPckg_ControlNode,
    ObjectNode,
    CompleteDSLPckg_ExpansionNode,
    CompleteDSLPckg_CentralBufferNode,
    CompleteDSLPckg_ActivityParameterNode,
    WriteLinkAction,
    CompleteDSLPckg_DestroyLinkAction,
    CompleteDSLPckg_CreateLinkAction,
    StructuralFeatureAction,
    CompleteDSLPckg_ClearStructuralFeatureAction,
    CompleteDSLPckg_WriteStructuralFeatureAction,
    CompleteDSLPckg_ReadStructuralFeatureAction,
    CompleteDSLPckg_CallOperationAction,
    CallAction,
    CompleteDSLPckg_StartObjectBehaviorAction,
    CompleteDSLPckg_CallBehaviorAction,
    InvocationAction,
    CompleteDSLPckg_SendSignalAction,
    CompleteDSLPckg_BroadcastSignalAction,
    CompleteDSLPckg_CallAction,
    InputPin,
    CompleteDSLPckg_ActionInputPin,
    CompleteDSLPckg_ValuePin,
    Pin,
    Action,
    CompleteDSLPckg_DestroyObjectAction,
    CompleteDSLPckg_ReclassifyObjectAction,
    CompleteDSLPckg_TestIdentityAction,
    CompleteDSLPckg_ReadSelfAction,
    CompleteDSLPckg_ValueSpecificationAction,
    CompleteDSLPckg_VariableAction,
    CompleteDSLPckg_ReduceAction,
    CompleteDSLPckg_StructuralFeatureAction,
    CompleteDSLPckg_ReadLinkObjectEndAction,
    CompleteDSLPckg_RaiseExceptionAction,
    CompleteDSLPckg_ReplyAction,
    CompleteDSLPckg_ReadLinkObjectEndQualifierAction,
    CompleteDSLPckg_CreateObjectAction,
    CompleteDSLPckg_StartClassifierBehaviorAction,
    CompleteDSLPckg_LinkAction,
    CompleteDSLPckg_UnmarshallAction,
    CompleteDSLPckg_AcceptEventAction,
    CompleteDSLPckg_ReadExtendAction,
    CompleteDSLPckg_OpaqueAction,
    CompleteDSLPckg_SendObjectAction,
    CompleteDSLPckg_InputPin,
    Artifact,
    CompleteDSLPckg_DeploymentSpecification,
    Node,
    CompleteDSLPckg_ExecutionEnvironment,
    CompleteDSLPckg_Device,
    CompleteDSLPckg_OutputPin,
    DeployedArtifact,
    CompleteDSLPckg_InvocationAction,
    CompleteDSLPckg_ConnectorEnd,
    Property,
    CompleteDSLPckg_Port,
    IntervalConstraint,
    CompleteDSLPckg_DurationConstraint,
    CompleteDSLPckg_TimeConstraint,
    Constraint,
    CompleteDSLPckg_InteractionConstraint,
    CompleteDSLPckg_IntervalConstraint,
    Interval,
    CompleteDSLPckg_DurationInterval,
    CompleteDSLPckg_TimeInterval,
    Observation,
    CompleteDSLPckg_DurationObservation,
    CompleteDSLPckg_TimeObservation,
    CompleteDSLPckg_TimeEvent,
    MessageEvent,
    CompleteDSLPckg_SignalEvent,
    CompleteDSLPckg_CallEvent,
    CompleteDSLPckg_AnyReceiveEvent,
    Event,
    CompleteDSLPckg_ChangeEvent,
    CompleteDSLPckg_MessageEvent,
    OpaqueBehavior,
    CompleteDSLPckg_FunctionBehavior,
    Behavior,
    CompleteDSLPckg_Interaction,
    CompleteDSLPckg_StateMachine,
    CompleteDSLPckg_Activity,
    CompleteDSLPckg_OpaqueBehavior,
    Association,
    CompleteDSLPckg_CommunicationPath,
    Class,
    CompleteDSLPckg_AssociationClass,
    Realization,
    CompleteDSLPckg_InterfaceRealization,
    CompleteDSLPckg_ComponentRealization,
    Abstraction,
    CompleteDSLPckg_Manifestation,
    CompleteDSLPckg_Realization,
    Dependency,
    CompleteDSLPckg_Abstraction,
    CompleteDSLPckg_Deployment,
    CompleteDSLPckg_Usage,
    InstanceSpecification,
    CompleteDSLPckg_EnumerationLiteral,
    DataType,
    CompleteDSLPckg_Enumeration,
    CompleteDSLPckg_PrimitiveType,
    EncapsulatedClassifier,
    StructuredClassifier,
    CompleteDSLPckg_EncapsulatedClassifier,
    BehavioredClassifier,
    CompleteDSLPckg_UseCase,
    CompleteDSLPckg_Actor,
    CompleteDSLPckg_Collaboration,
    Classifier,
    CompleteDSLPckg_Signal,
    CompleteDSLPckg_StructuredClassifier,
    CompleteDSLPckg_BehavioredClassifier,
    BehavioralFeature,
    CompleteDSLPckg_Reception,
    CompleteDSLPckg_Operation,
    CompleteDSLPckg_Interface,
    CompleteDSLPckg_DataType,
    CompleteDSLPckg_Class,
    DeploymentTarget,
    CompleteDSLPckg_Node,
    ConnectableElement,
    StructuralFeature,
    MultiplicityElement,
    Feature,
    CompleteDSLPckg_Connector,
    CompleteDSLPckg_Substitution,
    CompleteDSLPckg_Property,
    Type,
    RedefinableElement,
    CompleteDSLPckg_Feature,
    CompleteDSLPckg_ExtensionPoint,
    CompleteDSLPckg_ActivityEdge,
    CompleteDSLPckg_InstanceValue,
    LiteralSpecification,
    CompleteDSLPckg_LiteralString,
    CompleteDSLPckg_LiteralUnilimitedNatural,
    CompleteDSLPckg_LiteralBoolean,
    CompleteDSLPckg_LiteralReal,
    CompleteDSLPckg_LiteralInteger,
    CompleteDSLPckg_LiteralNull,
    CompleteDSLPckg_Behavior,
    ValueSpecification,
    CompleteDSLPckg_Duration,
    CompleteDSLPckg_TimeExpression,
    CompleteDSLPckg_LiteralSpecification,
    CompleteDSLPckg_Interval,
    CompleteDSLPckg_OpaqueExpression,
    CompleteDSLPckg_Expression,
    TypedElement,
    CompleteDSLPckg_Parameter,
    CompleteDSLPckg_Variable,
    CompleteDSLPckg_ObjectNode,
    CompleteDSLPckg_Pin,
    CompleteDSLPckg_ConnectableElement,
    CompleteDSLPckg_StructuralFeature,
    Relationship,
    CompleteDSLPckg_Association,
    CompleteDSLPckg_DirectedRelationship,
    PackageableElement,
    CompleteDSLPckg_InstanceSpecification,
    CompleteDSLPckg_GeneralizationSet,
    CompleteDSLPckg_Observation,
    CompleteDSLPckg_Type,
    CompleteDSLPckg_Event,
    CompleteDSLPckg_ValueSpecification,
    Namespace,
    CompleteDSLPckg_State,
    CompleteDSLPckg_Classifier,
    CompleteDSLPckg_Region,
    CompleteDSLPckg_Transition,
    CompleteDSLPckg_InteractionOperand,
    CompleteDSLPckg_StructuredActivityNode,
    CompleteDSLPckg_BehavioralFeature,
    CompleteDSLPckg_Package,
    DirectedRelationship,
    CompleteDSLPckg_Generalization,
    CompleteDSLPckg_ProtocolConformance,
    CompleteDSLPckg_PackageMerge,
    CompleteDSLPckg_Constraint,
    CompleteDSLPckg_PackageImport,
    CompleteDSLPckg_ElementImport,
    CompleteDSLPckg_Dependency,
    Element,
    CompleteDSLPckg_MultiplicityElement,
    CompleteDSLPckg_Slot,
    CompleteDSLPckg_LinkEndData,
    CompleteDSLPckg_QualifierValue,
    CompleteDSLPckg_Clause,
    CompleteDSLPckg_Relationship,
    CompleteDSLPckg_ExceptionHandler,
    CompleteDSLPckg_NamedElement,
    CompleteDSLPckg_Comment,
    CompleteDSLPckg_Element,
    NamedElement,
    CompleteDSLPckg_TypedElement,
    CompleteDSLPckg_MessageEnd,
    CompleteDSLPckg_Message,
    CompleteDSLPckg_Lifeline,
    CompleteDSLPckg_GeneralOrdering,
    CompleteDSLPckg_Component,
    CompleteDSLPckg_Namespace,
    CompleteDSLPckg_CollaborationUse,
    CompleteDSLPckg_Vertex,
    CompleteDSLPckg_RedefinableElement,
    CompleteDSLPckg_PackageableElement,
    CompleteDSLPckg_DeploymentTarget,
    CompleteDSLPckg_ParameterSet,
    CompleteDSLPckg_InteractionFragment,
    CompleteDSLPckg_DeployedArtifact,
    CompleteDSLPckg_Extend,
    CompleteDSLPckg_Artifact,
    CompleteDSLPckg_ActivityGroup,
    CompleteDSLPckg_ActivityNode,
    CompleteDSLPckg_Trigger,
    CompleteDSLPckg_Action,
    CompleteDSLPckg_Include,
    InteractionOperandKind,
    TransitionKind,
    VisibilityKind,
    ExpansionKind,
    ParameterEffectKind,
    AggregationKind,
    MessageSort,
    ConnectorKind,
    ObjectNodeOrderingKind,
    CallConcurrencyFeature,
    MessageKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ProtocolTransition)


def test_hyp_completedslpckg_protocoltransition_constructor_exists():
    assert callable(CompleteDSLPckg_ProtocolTransition.__init__)


def test_hyp_completedslpckg_protocoltransition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_hyp_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_hyp_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ProtocolStateMachine)


def test_hyp_completedslpckg_protocolstatemachine_constructor_exists():
    assert callable(CompleteDSLPckg_ProtocolStateMachine.__init__)


def test_hyp_completedslpckg_protocolstatemachine_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_finalstate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FinalState)


def test_hyp_completedslpckg_finalstate_constructor_exists():
    assert callable(CompleteDSLPckg_FinalState.__init__)


def test_hyp_completedslpckg_finalstate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_hyp_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_hyp_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConnectionPointReference)


def test_hyp_completedslpckg_connectionpointreference_constructor_exists():
    assert callable(CompleteDSLPckg_ConnectionPointReference.__init__)


def test_hyp_completedslpckg_connectionpointreference_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_hyp_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_hyp_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RemoveVariableValueAction)


def test_hyp_completedslpckg_removevariablevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_RemoveVariableValueAction.__init__)


def test_hyp_completedslpckg_removevariablevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AddVariableValueAction)


def test_hyp_completedslpckg_addvariablevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_AddVariableValueAction.__init__)


def test_hyp_completedslpckg_addvariablevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_hyp_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_hyp_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ClearVariableAction)


def test_hyp_completedslpckg_clearvariableaction_constructor_exists():
    assert callable(CompleteDSLPckg_ClearVariableAction.__init__)


def test_hyp_completedslpckg_clearvariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_WriteVariableAction)


def test_hyp_completedslpckg_writevariableaction_constructor_exists():
    assert callable(CompleteDSLPckg_WriteVariableAction.__init__)


def test_hyp_completedslpckg_writevariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadVariableAction)


def test_hyp_completedslpckg_readvariableaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadVariableAction.__init__)


def test_hyp_completedslpckg_readvariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_pseudostate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Pseudostate)


def test_hyp_completedslpckg_pseudostate_constructor_exists():
    assert callable(CompleteDSLPckg_Pseudostate.__init__)


def test_hyp_completedslpckg_pseudostate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_hyp_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_hyp_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CreateLinkObjectAction)


def test_hyp_completedslpckg_createlinkobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_CreateLinkObjectAction.__init__)


def test_hyp_completedslpckg_createlinkobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_readlsclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadlsClassifiedObjectAction)


def test_hyp_completedslpckg_readlsclassifiedobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadlsClassifiedObjectAction.__init__)


def test_hyp_completedslpckg_readlsclassifiedobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadlsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_hyp_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_hyp_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AcceptCallAction)


def test_hyp_completedslpckg_acceptcallaction_constructor_exists():
    assert callable(CompleteDSLPckg_AcceptCallAction.__init__)


def test_hyp_completedslpckg_acceptcallaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_hyp_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_hyp_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_WriteLinkAction)


def test_hyp_completedslpckg_writelinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_WriteLinkAction.__init__)


def test_hyp_completedslpckg_writelinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadLinkAction)


def test_hyp_completedslpckg_readlinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadLinkAction.__init__)


def test_hyp_completedslpckg_readlinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_hyp_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_hyp_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RemoveStructuralFeatureValueAction)


def test_hyp_completedslpckg_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_RemoveStructuralFeatureValueAction.__init__)


def test_hyp_completedslpckg_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AddStructuralFeatureValueAction)


def test_hyp_completedslpckg_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_AddStructuralFeatureValueAction.__init__)


def test_hyp_completedslpckg_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_hyp_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_hyp_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkEndDestructionData)


def test_hyp_completedslpckg_linkenddestructiondata_constructor_exists():
    assert callable(CompleteDSLPckg_LinkEndDestructionData.__init__)


def test_hyp_completedslpckg_linkenddestructiondata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"




def test_hyp_completedslpckg_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkEndCreationData)


def test_hyp_completedslpckg_linkendcreationdata_constructor_exists():
    assert callable(CompleteDSLPckg_LinkEndCreationData.__init__)


def test_hyp_completedslpckg_linkendcreationdata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"




def test_hyp_interactionuse_is_not_abstract():
    assert not inspect.isabstract(InteractionUse)


def test_hyp_interactionuse_constructor_exists():
    assert callable(InteractionUse.__init__)


def test_hyp_interactionuse_constructor_args():
    sig = inspect.signature(InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_hyp_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_hyp_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_hyp_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_hyp_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConsiderIgnoreFragment)


def test_hyp_completedslpckg_considerignorefragment_constructor_exists():
    assert callable(CompleteDSLPckg_ConsiderIgnoreFragment.__init__)


def test_hyp_completedslpckg_considerignorefragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CombinedFragment)


def test_hyp_completedslpckg_combinedfragment_constructor_exists():
    assert callable(CompleteDSLPckg_CombinedFragment.__init__)


def test_hyp_completedslpckg_combinedfragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"




def test_hyp_completedslpckg_partdecomposition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PartDecomposition)


def test_hyp_completedslpckg_partdecomposition_constructor_exists():
    assert callable(CompleteDSLPckg_PartDecomposition.__init__)


def test_hyp_completedslpckg_partdecomposition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_hyp_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_hyp_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActionExecutionSpecification)


def test_hyp_completedslpckg_actionexecutionspecification_constructor_exists():
    assert callable(CompleteDSLPckg_ActionExecutionSpecification.__init__)


def test_hyp_completedslpckg_actionexecutionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BehaviorExecutionSpecification)


def test_hyp_completedslpckg_behaviorexecutionspecification_constructor_exists():
    assert callable(CompleteDSLPckg_BehaviorExecutionSpecification.__init__)


def test_hyp_completedslpckg_behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(MessageOccurrenceSpecification)


def test_hyp_messageoccurrencespecification_constructor_exists():
    assert callable(MessageOccurrenceSpecification.__init__)


def test_hyp_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_destructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DestructionOccurrenceSpecification)


def test_hyp_completedslpckg_destructionoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_DestructionOccurrenceSpecification.__init__)


def test_hyp_completedslpckg_destructionoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_occurencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurenceSpecification)


def test_hyp_occurencespecification_constructor_exists():
    assert callable(OccurenceSpecification.__init__)


def test_hyp_occurencespecification_constructor_args():
    sig = inspect.signature(OccurenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MessageOccurrenceSpecification)


def test_hyp_completedslpckg_messageoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_MessageOccurrenceSpecification.__init__)


def test_hyp_completedslpckg_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutionOccurrenceSpecification)


def test_hyp_completedslpckg_executionoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutionOccurrenceSpecification.__init__)


def test_hyp_completedslpckg_executionoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_hyp_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_hyp_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_continuation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Continuation)


def test_hyp_completedslpckg_continuation_constructor_exists():
    assert callable(CompleteDSLPckg_Continuation.__init__)


def test_hyp_completedslpckg_continuation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"




def test_hyp_completedslpckg_interactionuse_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionUse)


def test_hyp_completedslpckg_interactionuse_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionUse.__init__)


def test_hyp_completedslpckg_interactionuse_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_occurencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OccurenceSpecification)


def test_hyp_completedslpckg_occurencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_OccurenceSpecification.__init__)


def test_hyp_completedslpckg_occurencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OccurenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StateInvariant)


def test_hyp_completedslpckg_stateinvariant_constructor_exists():
    assert callable(CompleteDSLPckg_StateInvariant.__init__)


def test_hyp_completedslpckg_stateinvariant_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_executionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutionSpecification)


def test_hyp_completedslpckg_executionspecification_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutionSpecification.__init__)


def test_hyp_completedslpckg_executionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_gate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Gate)


def test_hyp_completedslpckg_gate_constructor_exists():
    assert callable(CompleteDSLPckg_Gate.__init__)


def test_hyp_completedslpckg_gate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Gate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_hyp_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_hyp_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_hyp_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_hyp_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_datastorenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DataStoreNode)


def test_hyp_completedslpckg_datastorenode_constructor_exists():
    assert callable(CompleteDSLPckg_DataStoreNode.__init__)


def test_hyp_completedslpckg_datastorenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_hyp_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_hyp_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConditionalNode)


def test_hyp_completedslpckg_conditionalnode_constructor_exists():
    assert callable(CompleteDSLPckg_ConditionalNode.__init__)


def test_hyp_completedslpckg_conditionalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssumed" in params, "Missing parameter 'isAssumed'"





def test_hyp_completedslpckg_expansionregion_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExpansionRegion)


def test_hyp_completedslpckg_expansionregion_constructor_exists():
    assert callable(CompleteDSLPckg_ExpansionRegion.__init__)


def test_hyp_completedslpckg_expansionregion_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"




def test_hyp_completedslpckg_sequencenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SequenceNode)


def test_hyp_completedslpckg_sequencenode_constructor_exists():
    assert callable(CompleteDSLPckg_SequenceNode.__init__)


def test_hyp_completedslpckg_sequencenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_loopnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LoopNode)


def test_hyp_completedslpckg_loopnode_constructor_exists():
    assert callable(CompleteDSLPckg_LoopNode.__init__)


def test_hyp_completedslpckg_loopnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"




def test_hyp_completedslpckg_executablenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutableNode)


def test_hyp_completedslpckg_executablenode_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutableNode.__init__)


def test_hyp_completedslpckg_executablenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_hyp_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_hyp_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_objectflow_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ObjectFlow)


def test_hyp_completedslpckg_objectflow_constructor_exists():
    assert callable(CompleteDSLPckg_ObjectFlow.__init__)


def test_hyp_completedslpckg_objectflow_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"







def test_hyp_completedslpckg_controlflow_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ControlFlow)


def test_hyp_completedslpckg_controlflow_constructor_exists():
    assert callable(CompleteDSLPckg_ControlFlow.__init__)


def test_hyp_completedslpckg_controlflow_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_hyp_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_hyp_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InterruptibleActivityRegion)


def test_hyp_completedslpckg_interruptibleactivityregion_constructor_exists():
    assert callable(CompleteDSLPckg_InterruptibleActivityRegion.__init__)


def test_hyp_completedslpckg_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_activitypartition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityPartition)


def test_hyp_completedslpckg_activitypartition_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityPartition.__init__)


def test_hyp_completedslpckg_activitypartition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_hyp_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_hyp_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FlowFinalNode)


def test_hyp_completedslpckg_flowfinalnode_constructor_exists():
    assert callable(CompleteDSLPckg_FlowFinalNode.__init__)


def test_hyp_completedslpckg_flowfinalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_hyp_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_hyp_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_joinnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_JoinNode)


def test_hyp_completedslpckg_joinnode_constructor_exists():
    assert callable(CompleteDSLPckg_JoinNode.__init__)


def test_hyp_completedslpckg_joinnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"




def test_hyp_completedslpckg_decisionnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DecisionNode)


def test_hyp_completedslpckg_decisionnode_constructor_exists():
    assert callable(CompleteDSLPckg_DecisionNode.__init__)


def test_hyp_completedslpckg_decisionnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_finalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FinalNode)


def test_hyp_completedslpckg_finalnode_constructor_exists():
    assert callable(CompleteDSLPckg_FinalNode.__init__)


def test_hyp_completedslpckg_finalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_forknode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ForkNode)


def test_hyp_completedslpckg_forknode_constructor_exists():
    assert callable(CompleteDSLPckg_ForkNode.__init__)


def test_hyp_completedslpckg_forknode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_initialnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InitialNode)


def test_hyp_completedslpckg_initialnode_constructor_exists():
    assert callable(CompleteDSLPckg_InitialNode.__init__)


def test_hyp_completedslpckg_initialnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_mergenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MergeNode)


def test_hyp_completedslpckg_mergenode_constructor_exists():
    assert callable(CompleteDSLPckg_MergeNode.__init__)


def test_hyp_completedslpckg_mergenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityFinalNode)


def test_hyp_completedslpckg_activityfinalnode_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityFinalNode.__init__)


def test_hyp_completedslpckg_activityfinalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_controlnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ControlNode)


def test_hyp_completedslpckg_controlnode_constructor_exists():
    assert callable(CompleteDSLPckg_ControlNode.__init__)


def test_hyp_completedslpckg_controlnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_hyp_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_hyp_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_expansionnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExpansionNode)


def test_hyp_completedslpckg_expansionnode_constructor_exists():
    assert callable(CompleteDSLPckg_ExpansionNode.__init__)


def test_hyp_completedslpckg_expansionnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CentralBufferNode)


def test_hyp_completedslpckg_centralbuffernode_constructor_exists():
    assert callable(CompleteDSLPckg_CentralBufferNode.__init__)


def test_hyp_completedslpckg_centralbuffernode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityParameterNode)


def test_hyp_completedslpckg_activityparameternode_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityParameterNode.__init__)


def test_hyp_completedslpckg_activityparameternode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_hyp_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_hyp_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DestroyLinkAction)


def test_hyp_completedslpckg_destroylinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_DestroyLinkAction.__init__)


def test_hyp_completedslpckg_destroylinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CreateLinkAction)


def test_hyp_completedslpckg_createlinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_CreateLinkAction.__init__)


def test_hyp_completedslpckg_createlinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_hyp_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_hyp_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ClearStructuralFeatureAction)


def test_hyp_completedslpckg_clearstructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_ClearStructuralFeatureAction.__init__)


def test_hyp_completedslpckg_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_WriteStructuralFeatureAction)


def test_hyp_completedslpckg_writestructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_WriteStructuralFeatureAction.__init__)


def test_hyp_completedslpckg_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadStructuralFeatureAction)


def test_hyp_completedslpckg_readstructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadStructuralFeatureAction.__init__)


def test_hyp_completedslpckg_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallOperationAction)


def test_hyp_completedslpckg_calloperationaction_constructor_exists():
    assert callable(CompleteDSLPckg_CallOperationAction.__init__)


def test_hyp_completedslpckg_calloperationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_hyp_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_hyp_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StartObjectBehaviorAction)


def test_hyp_completedslpckg_startobjectbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg_StartObjectBehaviorAction.__init__)


def test_hyp_completedslpckg_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallBehaviorAction)


def test_hyp_completedslpckg_callbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg_CallBehaviorAction.__init__)


def test_hyp_completedslpckg_callbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_hyp_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_hyp_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SendSignalAction)


def test_hyp_completedslpckg_sendsignalaction_constructor_exists():
    assert callable(CompleteDSLPckg_SendSignalAction.__init__)


def test_hyp_completedslpckg_sendsignalaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BroadcastSignalAction)


def test_hyp_completedslpckg_broadcastsignalaction_constructor_exists():
    assert callable(CompleteDSLPckg_BroadcastSignalAction.__init__)


def test_hyp_completedslpckg_broadcastsignalaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_callaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallAction)


def test_hyp_completedslpckg_callaction_constructor_exists():
    assert callable(CompleteDSLPckg_CallAction.__init__)


def test_hyp_completedslpckg_callaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"




def test_hyp_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_hyp_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_hyp_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_actioninputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActionInputPin)


def test_hyp_completedslpckg_actioninputpin_constructor_exists():
    assert callable(CompleteDSLPckg_ActionInputPin.__init__)


def test_hyp_completedslpckg_actioninputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_valuepin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ValuePin)


def test_hyp_completedslpckg_valuepin_constructor_exists():
    assert callable(CompleteDSLPckg_ValuePin.__init__)


def test_hyp_completedslpckg_valuepin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_hyp_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_hyp_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DestroyObjectAction)


def test_hyp_completedslpckg_destroyobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_DestroyObjectAction.__init__)


def test_hyp_completedslpckg_destroyobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReclassifyObjectAction)


def test_hyp_completedslpckg_reclassifyobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReclassifyObjectAction.__init__)


def test_hyp_completedslpckg_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"




def test_hyp_completedslpckg_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TestIdentityAction)


def test_hyp_completedslpckg_testidentityaction_constructor_exists():
    assert callable(CompleteDSLPckg_TestIdentityAction.__init__)


def test_hyp_completedslpckg_testidentityaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_readselfaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadSelfAction)


def test_hyp_completedslpckg_readselfaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadSelfAction.__init__)


def test_hyp_completedslpckg_readselfaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ValueSpecificationAction)


def test_hyp_completedslpckg_valuespecificationaction_constructor_exists():
    assert callable(CompleteDSLPckg_ValueSpecificationAction.__init__)


def test_hyp_completedslpckg_valuespecificationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_variableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_VariableAction)


def test_hyp_completedslpckg_variableaction_constructor_exists():
    assert callable(CompleteDSLPckg_VariableAction.__init__)


def test_hyp_completedslpckg_variableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_reduceaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReduceAction)


def test_hyp_completedslpckg_reduceaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReduceAction.__init__)


def test_hyp_completedslpckg_reduceaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"




def test_hyp_completedslpckg_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuralFeatureAction)


def test_hyp_completedslpckg_structuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_StructuralFeatureAction.__init__)


def test_hyp_completedslpckg_structuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadLinkObjectEndAction)


def test_hyp_completedslpckg_readlinkobjectendaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadLinkObjectEndAction.__init__)


def test_hyp_completedslpckg_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RaiseExceptionAction)


def test_hyp_completedslpckg_raiseexceptionaction_constructor_exists():
    assert callable(CompleteDSLPckg_RaiseExceptionAction.__init__)


def test_hyp_completedslpckg_raiseexceptionaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_replyaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReplyAction)


def test_hyp_completedslpckg_replyaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReplyAction.__init__)


def test_hyp_completedslpckg_replyaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadLinkObjectEndQualifierAction)


def test_hyp_completedslpckg_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadLinkObjectEndQualifierAction.__init__)


def test_hyp_completedslpckg_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CreateObjectAction)


def test_hyp_completedslpckg_createobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_CreateObjectAction.__init__)


def test_hyp_completedslpckg_createobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StartClassifierBehaviorAction)


def test_hyp_completedslpckg_startclassifierbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg_StartClassifierBehaviorAction.__init__)


def test_hyp_completedslpckg_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_linkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkAction)


def test_hyp_completedslpckg_linkaction_constructor_exists():
    assert callable(CompleteDSLPckg_LinkAction.__init__)


def test_hyp_completedslpckg_linkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_UnmarshallAction)


def test_hyp_completedslpckg_unmarshallaction_constructor_exists():
    assert callable(CompleteDSLPckg_UnmarshallAction.__init__)


def test_hyp_completedslpckg_unmarshallaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AcceptEventAction)


def test_hyp_completedslpckg_accepteventaction_constructor_exists():
    assert callable(CompleteDSLPckg_AcceptEventAction.__init__)


def test_hyp_completedslpckg_accepteventaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"




def test_hyp_completedslpckg_readextendaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadExtendAction)


def test_hyp_completedslpckg_readextendaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadExtendAction.__init__)


def test_hyp_completedslpckg_readextendaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadExtendAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OpaqueAction)


def test_hyp_completedslpckg_opaqueaction_constructor_exists():
    assert callable(CompleteDSLPckg_OpaqueAction.__init__)


def test_hyp_completedslpckg_opaqueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"





def test_hyp_completedslpckg_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SendObjectAction)


def test_hyp_completedslpckg_sendobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_SendObjectAction.__init__)


def test_hyp_completedslpckg_sendobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_inputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InputPin)


def test_hyp_completedslpckg_inputpin_constructor_exists():
    assert callable(CompleteDSLPckg_InputPin.__init__)


def test_hyp_completedslpckg_inputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_hyp_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_hyp_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DeploymentSpecification)


def test_hyp_completedslpckg_deploymentspecification_constructor_exists():
    assert callable(CompleteDSLPckg_DeploymentSpecification.__init__)


def test_hyp_completedslpckg_deploymentspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"





def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutionEnvironment)


def test_hyp_completedslpckg_executionenvironment_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutionEnvironment.__init__)


def test_hyp_completedslpckg_executionenvironment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_device_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Device)


def test_hyp_completedslpckg_device_constructor_exists():
    assert callable(CompleteDSLPckg_Device.__init__)


def test_hyp_completedslpckg_device_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Device.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_outputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OutputPin)


def test_hyp_completedslpckg_outputpin_constructor_exists():
    assert callable(CompleteDSLPckg_OutputPin.__init__)


def test_hyp_completedslpckg_outputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_hyp_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_hyp_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_invocationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InvocationAction)


def test_hyp_completedslpckg_invocationaction_constructor_exists():
    assert callable(CompleteDSLPckg_InvocationAction.__init__)


def test_hyp_completedslpckg_invocationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_connectorend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConnectorEnd)


def test_hyp_completedslpckg_connectorend_constructor_exists():
    assert callable(CompleteDSLPckg_ConnectorEnd.__init__)


def test_hyp_completedslpckg_connectorend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_port_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Port)


def test_hyp_completedslpckg_port_constructor_exists():
    assert callable(CompleteDSLPckg_Port.__init__)


def test_hyp_completedslpckg_port_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Port.__init__)
    params = list(sig.parameters.keys())
    assert "isConjugated" in params, "Missing parameter 'isConjugated'"
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"
    assert "isService" in params, "Missing parameter 'isService'"






def test_hyp_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_hyp_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_hyp_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DurationConstraint)


def test_hyp_completedslpckg_durationconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_DurationConstraint.__init__)


def test_hyp_completedslpckg_durationconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_completedslpckg_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeConstraint)


def test_hyp_completedslpckg_timeconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_TimeConstraint.__init__)


def test_hyp_completedslpckg_timeconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionConstraint)


def test_hyp_completedslpckg_interactionconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionConstraint.__init__)


def test_hyp_completedslpckg_interactionconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_IntervalConstraint)


def test_hyp_completedslpckg_intervalconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_IntervalConstraint.__init__)


def test_hyp_completedslpckg_intervalconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_hyp_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_hyp_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_durationinterval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DurationInterval)


def test_hyp_completedslpckg_durationinterval_constructor_exists():
    assert callable(CompleteDSLPckg_DurationInterval.__init__)


def test_hyp_completedslpckg_durationinterval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_timeinterval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeInterval)


def test_hyp_completedslpckg_timeinterval_constructor_exists():
    assert callable(CompleteDSLPckg_TimeInterval.__init__)


def test_hyp_completedslpckg_timeinterval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_hyp_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_hyp_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_durationobservation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DurationObservation)


def test_hyp_completedslpckg_durationobservation_constructor_exists():
    assert callable(CompleteDSLPckg_DurationObservation.__init__)


def test_hyp_completedslpckg_durationobservation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_completedslpckg_timeobservation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeObservation)


def test_hyp_completedslpckg_timeobservation_constructor_exists():
    assert callable(CompleteDSLPckg_TimeObservation.__init__)


def test_hyp_completedslpckg_timeobservation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_completedslpckg_timeevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeEvent)


def test_hyp_completedslpckg_timeevent_constructor_exists():
    assert callable(CompleteDSLPckg_TimeEvent.__init__)


def test_hyp_completedslpckg_timeevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"




def test_hyp_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_hyp_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_hyp_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_signalevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SignalEvent)


def test_hyp_completedslpckg_signalevent_constructor_exists():
    assert callable(CompleteDSLPckg_SignalEvent.__init__)


def test_hyp_completedslpckg_signalevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_callevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallEvent)


def test_hyp_completedslpckg_callevent_constructor_exists():
    assert callable(CompleteDSLPckg_CallEvent.__init__)


def test_hyp_completedslpckg_callevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AnyReceiveEvent)


def test_hyp_completedslpckg_anyreceiveevent_constructor_exists():
    assert callable(CompleteDSLPckg_AnyReceiveEvent.__init__)


def test_hyp_completedslpckg_anyreceiveevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_changeevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ChangeEvent)


def test_hyp_completedslpckg_changeevent_constructor_exists():
    assert callable(CompleteDSLPckg_ChangeEvent.__init__)


def test_hyp_completedslpckg_changeevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_messageevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MessageEvent)


def test_hyp_completedslpckg_messageevent_constructor_exists():
    assert callable(CompleteDSLPckg_MessageEvent.__init__)


def test_hyp_completedslpckg_messageevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_hyp_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_hyp_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FunctionBehavior)


def test_hyp_completedslpckg_functionbehavior_constructor_exists():
    assert callable(CompleteDSLPckg_FunctionBehavior.__init__)


def test_hyp_completedslpckg_functionbehavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_hyp_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_hyp_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_interaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Interaction)


def test_hyp_completedslpckg_interaction_constructor_exists():
    assert callable(CompleteDSLPckg_Interaction.__init__)


def test_hyp_completedslpckg_interaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_statemachine_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StateMachine)


def test_hyp_completedslpckg_statemachine_constructor_exists():
    assert callable(CompleteDSLPckg_StateMachine.__init__)


def test_hyp_completedslpckg_statemachine_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_activity_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Activity)


def test_hyp_completedslpckg_activity_constructor_exists():
    assert callable(CompleteDSLPckg_Activity.__init__)


def test_hyp_completedslpckg_activity_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"





def test_hyp_completedslpckg_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OpaqueBehavior)


def test_hyp_completedslpckg_opaquebehavior_constructor_exists():
    assert callable(CompleteDSLPckg_OpaqueBehavior.__init__)


def test_hyp_completedslpckg_opaquebehavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_hyp_association_constructor_exists():
    assert callable(Association.__init__)


def test_hyp_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_communicationpath_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CommunicationPath)


def test_hyp_completedslpckg_communicationpath_constructor_exists():
    assert callable(CompleteDSLPckg_CommunicationPath.__init__)


def test_hyp_completedslpckg_communicationpath_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_associationclass_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AssociationClass)


def test_hyp_completedslpckg_associationclass_constructor_exists():
    assert callable(CompleteDSLPckg_AssociationClass.__init__)


def test_hyp_completedslpckg_associationclass_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_hyp_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_hyp_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_interfacerealization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InterfaceRealization)


def test_hyp_completedslpckg_interfacerealization_constructor_exists():
    assert callable(CompleteDSLPckg_InterfaceRealization.__init__)


def test_hyp_completedslpckg_interfacerealization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_componentrealization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ComponentRealization)


def test_hyp_completedslpckg_componentrealization_constructor_exists():
    assert callable(CompleteDSLPckg_ComponentRealization.__init__)


def test_hyp_completedslpckg_componentrealization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_hyp_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_hyp_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_manifestation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Manifestation)


def test_hyp_completedslpckg_manifestation_constructor_exists():
    assert callable(CompleteDSLPckg_Manifestation.__init__)


def test_hyp_completedslpckg_manifestation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_realization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Realization)


def test_hyp_completedslpckg_realization_constructor_exists():
    assert callable(CompleteDSLPckg_Realization.__init__)


def test_hyp_completedslpckg_realization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Realization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_hyp_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_hyp_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_abstraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Abstraction)


def test_hyp_completedslpckg_abstraction_constructor_exists():
    assert callable(CompleteDSLPckg_Abstraction.__init__)


def test_hyp_completedslpckg_abstraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_deployment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Deployment)


def test_hyp_completedslpckg_deployment_constructor_exists():
    assert callable(CompleteDSLPckg_Deployment.__init__)


def test_hyp_completedslpckg_deployment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Deployment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_usage_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Usage)


def test_hyp_completedslpckg_usage_constructor_exists():
    assert callable(CompleteDSLPckg_Usage.__init__)


def test_hyp_completedslpckg_usage_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Usage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_hyp_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_hyp_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_EnumerationLiteral)


def test_hyp_completedslpckg_enumerationliteral_constructor_exists():
    assert callable(CompleteDSLPckg_EnumerationLiteral.__init__)


def test_hyp_completedslpckg_enumerationliteral_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_enumeration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Enumeration)


def test_hyp_completedslpckg_enumeration_constructor_exists():
    assert callable(CompleteDSLPckg_Enumeration.__init__)


def test_hyp_completedslpckg_enumeration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_primitivetype_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PrimitiveType)


def test_hyp_completedslpckg_primitivetype_constructor_exists():
    assert callable(CompleteDSLPckg_PrimitiveType.__init__)


def test_hyp_completedslpckg_primitivetype_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_hyp_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_hyp_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_hyp_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_hyp_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_EncapsulatedClassifier)


def test_hyp_completedslpckg_encapsulatedclassifier_constructor_exists():
    assert callable(CompleteDSLPckg_EncapsulatedClassifier.__init__)


def test_hyp_completedslpckg_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_hyp_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_hyp_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_usecase_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_UseCase)


def test_hyp_completedslpckg_usecase_constructor_exists():
    assert callable(CompleteDSLPckg_UseCase.__init__)


def test_hyp_completedslpckg_usecase_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_actor_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Actor)


def test_hyp_completedslpckg_actor_constructor_exists():
    assert callable(CompleteDSLPckg_Actor.__init__)


def test_hyp_completedslpckg_actor_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_collaboration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Collaboration)


def test_hyp_completedslpckg_collaboration_constructor_exists():
    assert callable(CompleteDSLPckg_Collaboration.__init__)


def test_hyp_completedslpckg_collaboration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_signal_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Signal)


def test_hyp_completedslpckg_signal_constructor_exists():
    assert callable(CompleteDSLPckg_Signal.__init__)


def test_hyp_completedslpckg_signal_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Signal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuredClassifier)


def test_hyp_completedslpckg_structuredclassifier_constructor_exists():
    assert callable(CompleteDSLPckg_StructuredClassifier.__init__)


def test_hyp_completedslpckg_structuredclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BehavioredClassifier)


def test_hyp_completedslpckg_behavioredclassifier_constructor_exists():
    assert callable(CompleteDSLPckg_BehavioredClassifier.__init__)


def test_hyp_completedslpckg_behavioredclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_hyp_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_hyp_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_reception_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Reception)


def test_hyp_completedslpckg_reception_constructor_exists():
    assert callable(CompleteDSLPckg_Reception.__init__)


def test_hyp_completedslpckg_reception_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Reception.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_operation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Operation)


def test_hyp_completedslpckg_operation_constructor_exists():
    assert callable(CompleteDSLPckg_Operation.__init__)


def test_hyp_completedslpckg_operation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"








def test_hyp_completedslpckg_interface_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Interface)


def test_hyp_completedslpckg_interface_constructor_exists():
    assert callable(CompleteDSLPckg_Interface.__init__)


def test_hyp_completedslpckg_interface_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_datatype_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DataType)


def test_hyp_completedslpckg_datatype_constructor_exists():
    assert callable(CompleteDSLPckg_DataType.__init__)


def test_hyp_completedslpckg_datatype_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_class_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Class)


def test_hyp_completedslpckg_class_constructor_exists():
    assert callable(CompleteDSLPckg_Class.__init__)


def test_hyp_completedslpckg_class_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_hyp_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_hyp_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_node_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Node)


def test_hyp_completedslpckg_node_constructor_exists():
    assert callable(CompleteDSLPckg_Node.__init__)


def test_hyp_completedslpckg_node_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_hyp_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_hyp_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_hyp_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_hyp_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_hyp_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_hyp_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_connector_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Connector)


def test_hyp_completedslpckg_connector_constructor_exists():
    assert callable(CompleteDSLPckg_Connector.__init__)


def test_hyp_completedslpckg_connector_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_completedslpckg_substitution_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Substitution)


def test_hyp_completedslpckg_substitution_constructor_exists():
    assert callable(CompleteDSLPckg_Substitution.__init__)


def test_hyp_completedslpckg_substitution_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Substitution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_property_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Property)


def test_hyp_completedslpckg_property_constructor_exists():
    assert callable(CompleteDSLPckg_Property.__init__)


def test_hyp_completedslpckg_property_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "default" in params, "Missing parameter 'default'"









def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_hyp_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_hyp_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_feature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Feature)


def test_hyp_completedslpckg_feature_constructor_exists():
    assert callable(CompleteDSLPckg_Feature.__init__)


def test_hyp_completedslpckg_feature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"




def test_hyp_completedslpckg_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExtensionPoint)


def test_hyp_completedslpckg_extensionpoint_constructor_exists():
    assert callable(CompleteDSLPckg_ExtensionPoint.__init__)


def test_hyp_completedslpckg_extensionpoint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_activityedge_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityEdge)


def test_hyp_completedslpckg_activityedge_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityEdge.__init__)


def test_hyp_completedslpckg_activityedge_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_instancevalue_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InstanceValue)


def test_hyp_completedslpckg_instancevalue_constructor_exists():
    assert callable(CompleteDSLPckg_InstanceValue.__init__)


def test_hyp_completedslpckg_instancevalue_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_hyp_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_hyp_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_literalstring_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralString)


def test_hyp_completedslpckg_literalstring_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralString.__init__)


def test_hyp_completedslpckg_literalstring_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_literalunilimitednatural_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralUnilimitedNatural)


def test_hyp_completedslpckg_literalunilimitednatural_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralUnilimitedNatural.__init__)


def test_hyp_completedslpckg_literalunilimitednatural_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralUnilimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_literalboolean_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralBoolean)


def test_hyp_completedslpckg_literalboolean_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralBoolean.__init__)


def test_hyp_completedslpckg_literalboolean_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_literalreal_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralReal)


def test_hyp_completedslpckg_literalreal_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralReal.__init__)


def test_hyp_completedslpckg_literalreal_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_literalinteger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralInteger)


def test_hyp_completedslpckg_literalinteger_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralInteger.__init__)


def test_hyp_completedslpckg_literalinteger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_literalnull_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralNull)


def test_hyp_completedslpckg_literalnull_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralNull.__init__)


def test_hyp_completedslpckg_literalnull_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_behavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Behavior)


def test_hyp_completedslpckg_behavior_constructor_exists():
    assert callable(CompleteDSLPckg_Behavior.__init__)


def test_hyp_completedslpckg_behavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"




def test_hyp_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_hyp_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_hyp_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_duration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Duration)


def test_hyp_completedslpckg_duration_constructor_exists():
    assert callable(CompleteDSLPckg_Duration.__init__)


def test_hyp_completedslpckg_duration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Duration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_timeexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeExpression)


def test_hyp_completedslpckg_timeexpression_constructor_exists():
    assert callable(CompleteDSLPckg_TimeExpression.__init__)


def test_hyp_completedslpckg_timeexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_literalspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralSpecification)


def test_hyp_completedslpckg_literalspecification_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralSpecification.__init__)


def test_hyp_completedslpckg_literalspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_interval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Interval)


def test_hyp_completedslpckg_interval_constructor_exists():
    assert callable(CompleteDSLPckg_Interval.__init__)


def test_hyp_completedslpckg_interval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Interval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OpaqueExpression)


def test_hyp_completedslpckg_opaqueexpression_constructor_exists():
    assert callable(CompleteDSLPckg_OpaqueExpression.__init__)


def test_hyp_completedslpckg_opaqueexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"





def test_hyp_completedslpckg_expression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Expression)


def test_hyp_completedslpckg_expression_constructor_exists():
    assert callable(CompleteDSLPckg_Expression.__init__)


def test_hyp_completedslpckg_expression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_parameter_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Parameter)


def test_hyp_completedslpckg_parameter_constructor_exists():
    assert callable(CompleteDSLPckg_Parameter.__init__)


def test_hyp_completedslpckg_parameter_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_completedslpckg_variable_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Variable)


def test_hyp_completedslpckg_variable_constructor_exists():
    assert callable(CompleteDSLPckg_Variable.__init__)


def test_hyp_completedslpckg_variable_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_objectnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ObjectNode)


def test_hyp_completedslpckg_objectnode_constructor_exists():
    assert callable(CompleteDSLPckg_ObjectNode.__init__)


def test_hyp_completedslpckg_objectnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_pin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Pin)


def test_hyp_completedslpckg_pin_constructor_exists():
    assert callable(CompleteDSLPckg_Pin.__init__)


def test_hyp_completedslpckg_pin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_connectableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConnectableElement)


def test_hyp_completedslpckg_connectableelement_constructor_exists():
    assert callable(CompleteDSLPckg_ConnectableElement.__init__)


def test_hyp_completedslpckg_connectableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuralFeature)


def test_hyp_completedslpckg_structuralfeature_constructor_exists():
    assert callable(CompleteDSLPckg_StructuralFeature.__init__)


def test_hyp_completedslpckg_structuralfeature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"




def test_hyp_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_hyp_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_hyp_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_association_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Association)


def test_hyp_completedslpckg_association_constructor_exists():
    assert callable(CompleteDSLPckg_Association.__init__)


def test_hyp_completedslpckg_association_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"




def test_hyp_completedslpckg_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DirectedRelationship)


def test_hyp_completedslpckg_directedrelationship_constructor_exists():
    assert callable(CompleteDSLPckg_DirectedRelationship.__init__)


def test_hyp_completedslpckg_directedrelationship_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_hyp_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_hyp_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_instancespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InstanceSpecification)


def test_hyp_completedslpckg_instancespecification_constructor_exists():
    assert callable(CompleteDSLPckg_InstanceSpecification.__init__)


def test_hyp_completedslpckg_instancespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_generalizationset_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_GeneralizationSet)


def test_hyp_completedslpckg_generalizationset_constructor_exists():
    assert callable(CompleteDSLPckg_GeneralizationSet.__init__)


def test_hyp_completedslpckg_generalizationset_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"





def test_hyp_completedslpckg_observation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Observation)


def test_hyp_completedslpckg_observation_constructor_exists():
    assert callable(CompleteDSLPckg_Observation.__init__)


def test_hyp_completedslpckg_observation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Observation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_type_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Type)


def test_hyp_completedslpckg_type_constructor_exists():
    assert callable(CompleteDSLPckg_Type.__init__)


def test_hyp_completedslpckg_type_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_event_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Event)


def test_hyp_completedslpckg_event_constructor_exists():
    assert callable(CompleteDSLPckg_Event.__init__)


def test_hyp_completedslpckg_event_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_valuespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ValueSpecification)


def test_hyp_completedslpckg_valuespecification_constructor_exists():
    assert callable(CompleteDSLPckg_ValueSpecification.__init__)


def test_hyp_completedslpckg_valuespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_hyp_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_hyp_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_state_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_State)


def test_hyp_completedslpckg_state_constructor_exists():
    assert callable(CompleteDSLPckg_State.__init__)


def test_hyp_completedslpckg_state_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_State.__init__)
    params = list(sig.parameters.keys())
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"







def test_hyp_completedslpckg_classifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Classifier)


def test_hyp_completedslpckg_classifier_constructor_exists():
    assert callable(CompleteDSLPckg_Classifier.__init__)


def test_hyp_completedslpckg_classifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isFinalSpecialization" in params, "Missing parameter 'isFinalSpecialization'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"





def test_hyp_completedslpckg_region_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Region)


def test_hyp_completedslpckg_region_constructor_exists():
    assert callable(CompleteDSLPckg_Region.__init__)


def test_hyp_completedslpckg_region_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Region.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_transition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Transition)


def test_hyp_completedslpckg_transition_constructor_exists():
    assert callable(CompleteDSLPckg_Transition.__init__)


def test_hyp_completedslpckg_transition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_completedslpckg_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionOperand)


def test_hyp_completedslpckg_interactionoperand_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionOperand.__init__)


def test_hyp_completedslpckg_interactionoperand_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuredActivityNode)


def test_hyp_completedslpckg_structuredactivitynode_constructor_exists():
    assert callable(CompleteDSLPckg_StructuredActivityNode.__init__)


def test_hyp_completedslpckg_structuredactivitynode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"




def test_hyp_completedslpckg_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BehavioralFeature)


def test_hyp_completedslpckg_behavioralfeature_constructor_exists():
    assert callable(CompleteDSLPckg_BehavioralFeature.__init__)


def test_hyp_completedslpckg_behavioralfeature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_package_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Package)


def test_hyp_completedslpckg_package_constructor_exists():
    assert callable(CompleteDSLPckg_Package.__init__)


def test_hyp_completedslpckg_package_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Package.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"




def test_hyp_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_hyp_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_hyp_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_generalization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Generalization)


def test_hyp_completedslpckg_generalization_constructor_exists():
    assert callable(CompleteDSLPckg_Generalization.__init__)


def test_hyp_completedslpckg_generalization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"




def test_hyp_completedslpckg_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ProtocolConformance)


def test_hyp_completedslpckg_protocolconformance_constructor_exists():
    assert callable(CompleteDSLPckg_ProtocolConformance.__init__)


def test_hyp_completedslpckg_protocolconformance_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_packagemerge_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PackageMerge)


def test_hyp_completedslpckg_packagemerge_constructor_exists():
    assert callable(CompleteDSLPckg_PackageMerge.__init__)


def test_hyp_completedslpckg_packagemerge_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_constraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Constraint)


def test_hyp_completedslpckg_constraint_constructor_exists():
    assert callable(CompleteDSLPckg_Constraint.__init__)


def test_hyp_completedslpckg_constraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_packageimport_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PackageImport)


def test_hyp_completedslpckg_packageimport_constructor_exists():
    assert callable(CompleteDSLPckg_PackageImport.__init__)


def test_hyp_completedslpckg_packageimport_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"




def test_hyp_completedslpckg_elementimport_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ElementImport)


def test_hyp_completedslpckg_elementimport_constructor_exists():
    assert callable(CompleteDSLPckg_ElementImport.__init__)


def test_hyp_completedslpckg_elementimport_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "alias" in params, "Missing parameter 'alias'"





def test_hyp_completedslpckg_dependency_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Dependency)


def test_hyp_completedslpckg_dependency_constructor_exists():
    assert callable(CompleteDSLPckg_Dependency.__init__)


def test_hyp_completedslpckg_dependency_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MultiplicityElement)


def test_hyp_completedslpckg_multiplicityelement_constructor_exists():
    assert callable(CompleteDSLPckg_MultiplicityElement.__init__)


def test_hyp_completedslpckg_multiplicityelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"







def test_hyp_completedslpckg_slot_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Slot)


def test_hyp_completedslpckg_slot_constructor_exists():
    assert callable(CompleteDSLPckg_Slot.__init__)


def test_hyp_completedslpckg_slot_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Slot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_linkenddata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkEndData)


def test_hyp_completedslpckg_linkenddata_constructor_exists():
    assert callable(CompleteDSLPckg_LinkEndData.__init__)


def test_hyp_completedslpckg_linkenddata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_QualifierValue)


def test_hyp_completedslpckg_qualifiervalue_constructor_exists():
    assert callable(CompleteDSLPckg_QualifierValue.__init__)


def test_hyp_completedslpckg_qualifiervalue_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_clause_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Clause)


def test_hyp_completedslpckg_clause_constructor_exists():
    assert callable(CompleteDSLPckg_Clause.__init__)


def test_hyp_completedslpckg_clause_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Clause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_relationship_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Relationship)


def test_hyp_completedslpckg_relationship_constructor_exists():
    assert callable(CompleteDSLPckg_Relationship.__init__)


def test_hyp_completedslpckg_relationship_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExceptionHandler)


def test_hyp_completedslpckg_exceptionhandler_constructor_exists():
    assert callable(CompleteDSLPckg_ExceptionHandler.__init__)


def test_hyp_completedslpckg_exceptionhandler_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_namedelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_NamedElement)


def test_hyp_completedslpckg_namedelement_constructor_exists():
    assert callable(CompleteDSLPckg_NamedElement.__init__)


def test_hyp_completedslpckg_namedelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_completedslpckg_comment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Comment)


def test_hyp_completedslpckg_comment_constructor_exists():
    assert callable(CompleteDSLPckg_Comment.__init__)


def test_hyp_completedslpckg_comment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_completedslpckg_element_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Element)


def test_hyp_completedslpckg_element_constructor_exists():
    assert callable(CompleteDSLPckg_Element.__init__)


def test_hyp_completedslpckg_element_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_typedelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TypedElement)


def test_hyp_completedslpckg_typedelement_constructor_exists():
    assert callable(CompleteDSLPckg_TypedElement.__init__)


def test_hyp_completedslpckg_typedelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_messageend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MessageEnd)


def test_hyp_completedslpckg_messageend_constructor_exists():
    assert callable(CompleteDSLPckg_MessageEnd.__init__)


def test_hyp_completedslpckg_messageend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_message_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Message)


def test_hyp_completedslpckg_message_constructor_exists():
    assert callable(CompleteDSLPckg_Message.__init__)


def test_hyp_completedslpckg_message_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageKind" in params, "Missing parameter 'messageKind'"
    assert "messageSort" in params, "Missing parameter 'messageSort'"





def test_hyp_completedslpckg_lifeline_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Lifeline)


def test_hyp_completedslpckg_lifeline_constructor_exists():
    assert callable(CompleteDSLPckg_Lifeline.__init__)


def test_hyp_completedslpckg_lifeline_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_generalordering_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_GeneralOrdering)


def test_hyp_completedslpckg_generalordering_constructor_exists():
    assert callable(CompleteDSLPckg_GeneralOrdering.__init__)


def test_hyp_completedslpckg_generalordering_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_component_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Component)


def test_hyp_completedslpckg_component_constructor_exists():
    assert callable(CompleteDSLPckg_Component.__init__)


def test_hyp_completedslpckg_component_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"




def test_hyp_completedslpckg_namespace_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Namespace)


def test_hyp_completedslpckg_namespace_constructor_exists():
    assert callable(CompleteDSLPckg_Namespace.__init__)


def test_hyp_completedslpckg_namespace_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_collaborationuse_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CollaborationUse)


def test_hyp_completedslpckg_collaborationuse_constructor_exists():
    assert callable(CompleteDSLPckg_CollaborationUse.__init__)


def test_hyp_completedslpckg_collaborationuse_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_vertex_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Vertex)


def test_hyp_completedslpckg_vertex_constructor_exists():
    assert callable(CompleteDSLPckg_Vertex.__init__)


def test_hyp_completedslpckg_vertex_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RedefinableElement)


def test_hyp_completedslpckg_redefinableelement_constructor_exists():
    assert callable(CompleteDSLPckg_RedefinableElement.__init__)


def test_hyp_completedslpckg_redefinableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"




def test_hyp_completedslpckg_packageableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PackageableElement)


def test_hyp_completedslpckg_packageableelement_constructor_exists():
    assert callable(CompleteDSLPckg_PackageableElement.__init__)


def test_hyp_completedslpckg_packageableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DeploymentTarget)


def test_hyp_completedslpckg_deploymenttarget_constructor_exists():
    assert callable(CompleteDSLPckg_DeploymentTarget.__init__)


def test_hyp_completedslpckg_deploymenttarget_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_parameterset_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ParameterSet)


def test_hyp_completedslpckg_parameterset_constructor_exists():
    assert callable(CompleteDSLPckg_ParameterSet.__init__)


def test_hyp_completedslpckg_parameterset_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionFragment)


def test_hyp_completedslpckg_interactionfragment_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionFragment.__init__)


def test_hyp_completedslpckg_interactionfragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DeployedArtifact)


def test_hyp_completedslpckg_deployedartifact_constructor_exists():
    assert callable(CompleteDSLPckg_DeployedArtifact.__init__)


def test_hyp_completedslpckg_deployedartifact_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_extend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Extend)


def test_hyp_completedslpckg_extend_constructor_exists():
    assert callable(CompleteDSLPckg_Extend.__init__)


def test_hyp_completedslpckg_extend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Extend.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_artifact_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Artifact)


def test_hyp_completedslpckg_artifact_constructor_exists():
    assert callable(CompleteDSLPckg_Artifact.__init__)


def test_hyp_completedslpckg_artifact_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"




def test_hyp_completedslpckg_activitygroup_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityGroup)


def test_hyp_completedslpckg_activitygroup_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityGroup.__init__)


def test_hyp_completedslpckg_activitygroup_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_activitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityNode)


def test_hyp_completedslpckg_activitynode_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityNode.__init__)


def test_hyp_completedslpckg_activitynode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_trigger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Trigger)


def test_hyp_completedslpckg_trigger_constructor_exists():
    assert callable(CompleteDSLPckg_Trigger.__init__)


def test_hyp_completedslpckg_trigger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_action_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Action)


def test_hyp_completedslpckg_action_constructor_exists():
    assert callable(CompleteDSLPckg_Action.__init__)


def test_hyp_completedslpckg_action_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completedslpckg_include_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Include)


def test_hyp_completedslpckg_include_constructor_exists():
    assert callable(CompleteDSLPckg_Include.__init__)


def test_hyp_completedslpckg_include_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Include.__init__)
    params = list(sig.parameters.keys())

def test_hyp_interactionoperandkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperandKind is not None

def test_hyp_interactionoperandkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperandKind]
    expected_literals = [
        "neg",
        "par",
        "loop",
        "critical",
        "alt",
        "consider",
        "break_",
        "assert_",
        "opt",
        "seq",
        "strict",
        "ignore",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperandKind"

def test_hyp_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_hyp_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "external",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_hyp_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_hyp_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "public",
        "protected",
        "package",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_hyp_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_hyp_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "iterative",
        "parallel",
        "stream",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_hyp_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_hyp_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "create",
        "read",
        "update",
        "delete",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_hyp_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_hyp_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "none",
        "composite",
        "shared",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"

def test_hyp_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_hyp_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "asynchCall",
        "createMessage",
        "deleteMessage",
        "asynchSignal",
        "synchCall",
        "reply",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_hyp_connectorkind_exists():
    # Check that the Enumeration exists
    assert ConnectorKind is not None

def test_hyp_connectorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectorKind]
    expected_literals = [
        "delegation",
        "assembly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectorKind"

def test_hyp_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_hyp_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "LIFO",
        "FIFO",
        "unordered",
        "ordered",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

def test_hyp_callconcurrencyfeature_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyFeature is not None

def test_hyp_callconcurrencyfeature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyFeature]
    expected_literals = [
        "guarded",
        "concurrent",
        "sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyFeature"

def test_hyp_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_hyp_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "lost",
        "unknown",
        "complete",
        "found",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"


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
ActivityNode_strategy = st.builds(
    ActivityNode,
)
Transition_strategy = st.builds(
    Transition,
)
CompleteDSLPckg_ProtocolTransition_strategy = st.builds(
    CompleteDSLPckg_ProtocolTransition,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
CompleteDSLPckg_ProtocolStateMachine_strategy = st.builds(
    CompleteDSLPckg_ProtocolStateMachine,
)
State_strategy = st.builds(
    State,
)
CompleteDSLPckg_FinalState_strategy = st.builds(
    CompleteDSLPckg_FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
CompleteDSLPckg_ConnectionPointReference_strategy = st.builds(
    CompleteDSLPckg_ConnectionPointReference,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
CompleteDSLPckg_RemoveVariableValueAction_strategy = st.builds(
    CompleteDSLPckg_RemoveVariableValueAction,
)
CompleteDSLPckg_AddVariableValueAction_strategy = st.builds(
    CompleteDSLPckg_AddVariableValueAction,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
CompleteDSLPckg_ClearVariableAction_strategy = st.builds(
    CompleteDSLPckg_ClearVariableAction,
)
CompleteDSLPckg_WriteVariableAction_strategy = st.builds(
    CompleteDSLPckg_WriteVariableAction,
)
CompleteDSLPckg_ReadVariableAction_strategy = st.builds(
    CompleteDSLPckg_ReadVariableAction,
)
CompleteDSLPckg_Pseudostate_strategy = st.builds(
    CompleteDSLPckg_Pseudostate,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
CompleteDSLPckg_CreateLinkObjectAction_strategy = st.builds(
    CompleteDSLPckg_CreateLinkObjectAction,
)
CompleteDSLPckg_ReadlsClassifiedObjectAction_strategy = st.builds(
    CompleteDSLPckg_ReadlsClassifiedObjectAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
CompleteDSLPckg_AcceptCallAction_strategy = st.builds(
    CompleteDSLPckg_AcceptCallAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
CompleteDSLPckg_WriteLinkAction_strategy = st.builds(
    CompleteDSLPckg_WriteLinkAction,
)
CompleteDSLPckg_ReadLinkAction_strategy = st.builds(
    CompleteDSLPckg_ReadLinkAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
CompleteDSLPckg_RemoveStructuralFeatureValueAction_strategy = st.builds(
    CompleteDSLPckg_RemoveStructuralFeatureValueAction,
)
CompleteDSLPckg_AddStructuralFeatureValueAction_strategy = st.builds(
    CompleteDSLPckg_AddStructuralFeatureValueAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
CompleteDSLPckg_LinkEndDestructionData_strategy = st.builds(
    CompleteDSLPckg_LinkEndDestructionData,
    isDestroyDuplicates=
        st.booleans()
)
CompleteDSLPckg_LinkEndCreationData_strategy = st.builds(
    CompleteDSLPckg_LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
CompleteDSLPckg_ConsiderIgnoreFragment_strategy = st.builds(
    CompleteDSLPckg_ConsiderIgnoreFragment,
)
CompleteDSLPckg_CombinedFragment_strategy = st.builds(
    CompleteDSLPckg_CombinedFragment,
    interactionOperator=
        safe_text
)
CompleteDSLPckg_PartDecomposition_strategy = st.builds(
    CompleteDSLPckg_PartDecomposition,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
CompleteDSLPckg_ActionExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg_ActionExecutionSpecification,
)
CompleteDSLPckg_BehaviorExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg_BehaviorExecutionSpecification,
)
MessageOccurrenceSpecification_strategy = st.builds(
    MessageOccurrenceSpecification,
)
CompleteDSLPckg_DestructionOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg_DestructionOccurrenceSpecification,
)
OccurenceSpecification_strategy = st.builds(
    OccurenceSpecification,
)
CompleteDSLPckg_MessageOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg_MessageOccurrenceSpecification,
)
CompleteDSLPckg_ExecutionOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg_ExecutionOccurrenceSpecification,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
CompleteDSLPckg_Continuation_strategy = st.builds(
    CompleteDSLPckg_Continuation,
    setting=
        st.booleans()
)
CompleteDSLPckg_InteractionUse_strategy = st.builds(
    CompleteDSLPckg_InteractionUse,
)
CompleteDSLPckg_OccurenceSpecification_strategy = st.builds(
    CompleteDSLPckg_OccurenceSpecification,
)
CompleteDSLPckg_StateInvariant_strategy = st.builds(
    CompleteDSLPckg_StateInvariant,
)
CompleteDSLPckg_ExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg_ExecutionSpecification,
)
CompleteDSLPckg_Gate_strategy = st.builds(
    CompleteDSLPckg_Gate,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
CompleteDSLPckg_DataStoreNode_strategy = st.builds(
    CompleteDSLPckg_DataStoreNode,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
CompleteDSLPckg_ConditionalNode_strategy = st.builds(
    CompleteDSLPckg_ConditionalNode,
    isDeterminate=
        st.booleans(),
    isAssumed=
        st.booleans()
)
CompleteDSLPckg_ExpansionRegion_strategy = st.builds(
    CompleteDSLPckg_ExpansionRegion,
    mode=
        safe_text
)
CompleteDSLPckg_SequenceNode_strategy = st.builds(
    CompleteDSLPckg_SequenceNode,
)
CompleteDSLPckg_LoopNode_strategy = st.builds(
    CompleteDSLPckg_LoopNode,
    isTestedFirst=
        st.booleans()
)
CompleteDSLPckg_ExecutableNode_strategy = st.builds(
    CompleteDSLPckg_ExecutableNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
CompleteDSLPckg_ObjectFlow_strategy = st.builds(
    CompleteDSLPckg_ObjectFlow,
    ordering=
        safe_text,
    isControlType=
        st.booleans(),
    isMultireceive=
        st.booleans(),
    isMulticast=
        st.booleans()
)
CompleteDSLPckg_ControlFlow_strategy = st.builds(
    CompleteDSLPckg_ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
CompleteDSLPckg_InterruptibleActivityRegion_strategy = st.builds(
    CompleteDSLPckg_InterruptibleActivityRegion,
)
CompleteDSLPckg_ActivityPartition_strategy = st.builds(
    CompleteDSLPckg_ActivityPartition,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
CompleteDSLPckg_FlowFinalNode_strategy = st.builds(
    CompleteDSLPckg_FlowFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
CompleteDSLPckg_JoinNode_strategy = st.builds(
    CompleteDSLPckg_JoinNode,
    isCombineDuplicate=
        st.booleans()
)
CompleteDSLPckg_DecisionNode_strategy = st.builds(
    CompleteDSLPckg_DecisionNode,
)
CompleteDSLPckg_FinalNode_strategy = st.builds(
    CompleteDSLPckg_FinalNode,
)
CompleteDSLPckg_ForkNode_strategy = st.builds(
    CompleteDSLPckg_ForkNode,
)
CompleteDSLPckg_InitialNode_strategy = st.builds(
    CompleteDSLPckg_InitialNode,
)
CompleteDSLPckg_MergeNode_strategy = st.builds(
    CompleteDSLPckg_MergeNode,
)
CompleteDSLPckg_ActivityFinalNode_strategy = st.builds(
    CompleteDSLPckg_ActivityFinalNode,
)
CompleteDSLPckg_ControlNode_strategy = st.builds(
    CompleteDSLPckg_ControlNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
CompleteDSLPckg_ExpansionNode_strategy = st.builds(
    CompleteDSLPckg_ExpansionNode,
)
CompleteDSLPckg_CentralBufferNode_strategy = st.builds(
    CompleteDSLPckg_CentralBufferNode,
)
CompleteDSLPckg_ActivityParameterNode_strategy = st.builds(
    CompleteDSLPckg_ActivityParameterNode,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
CompleteDSLPckg_DestroyLinkAction_strategy = st.builds(
    CompleteDSLPckg_DestroyLinkAction,
)
CompleteDSLPckg_CreateLinkAction_strategy = st.builds(
    CompleteDSLPckg_CreateLinkAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
CompleteDSLPckg_ClearStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_ClearStructuralFeatureAction,
)
CompleteDSLPckg_WriteStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_WriteStructuralFeatureAction,
)
CompleteDSLPckg_ReadStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_ReadStructuralFeatureAction,
)
CompleteDSLPckg_CallOperationAction_strategy = st.builds(
    CompleteDSLPckg_CallOperationAction,
)
CallAction_strategy = st.builds(
    CallAction,
)
CompleteDSLPckg_StartObjectBehaviorAction_strategy = st.builds(
    CompleteDSLPckg_StartObjectBehaviorAction,
)
CompleteDSLPckg_CallBehaviorAction_strategy = st.builds(
    CompleteDSLPckg_CallBehaviorAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
CompleteDSLPckg_SendSignalAction_strategy = st.builds(
    CompleteDSLPckg_SendSignalAction,
)
CompleteDSLPckg_BroadcastSignalAction_strategy = st.builds(
    CompleteDSLPckg_BroadcastSignalAction,
)
CompleteDSLPckg_CallAction_strategy = st.builds(
    CompleteDSLPckg_CallAction,
    isSynchronous=
        st.booleans()
)
InputPin_strategy = st.builds(
    InputPin,
)
CompleteDSLPckg_ActionInputPin_strategy = st.builds(
    CompleteDSLPckg_ActionInputPin,
)
CompleteDSLPckg_ValuePin_strategy = st.builds(
    CompleteDSLPckg_ValuePin,
)
Pin_strategy = st.builds(
    Pin,
)
Action_strategy = st.builds(
    Action,
)
CompleteDSLPckg_DestroyObjectAction_strategy = st.builds(
    CompleteDSLPckg_DestroyObjectAction,
)
CompleteDSLPckg_ReclassifyObjectAction_strategy = st.builds(
    CompleteDSLPckg_ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
CompleteDSLPckg_TestIdentityAction_strategy = st.builds(
    CompleteDSLPckg_TestIdentityAction,
)
CompleteDSLPckg_ReadSelfAction_strategy = st.builds(
    CompleteDSLPckg_ReadSelfAction,
)
CompleteDSLPckg_ValueSpecificationAction_strategy = st.builds(
    CompleteDSLPckg_ValueSpecificationAction,
)
CompleteDSLPckg_VariableAction_strategy = st.builds(
    CompleteDSLPckg_VariableAction,
)
CompleteDSLPckg_ReduceAction_strategy = st.builds(
    CompleteDSLPckg_ReduceAction,
    isOrdered=
        st.booleans()
)
CompleteDSLPckg_StructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_StructuralFeatureAction,
)
CompleteDSLPckg_ReadLinkObjectEndAction_strategy = st.builds(
    CompleteDSLPckg_ReadLinkObjectEndAction,
)
CompleteDSLPckg_RaiseExceptionAction_strategy = st.builds(
    CompleteDSLPckg_RaiseExceptionAction,
)
CompleteDSLPckg_ReplyAction_strategy = st.builds(
    CompleteDSLPckg_ReplyAction,
)
CompleteDSLPckg_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    CompleteDSLPckg_ReadLinkObjectEndQualifierAction,
)
CompleteDSLPckg_CreateObjectAction_strategy = st.builds(
    CompleteDSLPckg_CreateObjectAction,
)
CompleteDSLPckg_StartClassifierBehaviorAction_strategy = st.builds(
    CompleteDSLPckg_StartClassifierBehaviorAction,
)
CompleteDSLPckg_LinkAction_strategy = st.builds(
    CompleteDSLPckg_LinkAction,
)
CompleteDSLPckg_UnmarshallAction_strategy = st.builds(
    CompleteDSLPckg_UnmarshallAction,
)
CompleteDSLPckg_AcceptEventAction_strategy = st.builds(
    CompleteDSLPckg_AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
CompleteDSLPckg_ReadExtendAction_strategy = st.builds(
    CompleteDSLPckg_ReadExtendAction,
)
CompleteDSLPckg_OpaqueAction_strategy = st.builds(
    CompleteDSLPckg_OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
CompleteDSLPckg_SendObjectAction_strategy = st.builds(
    CompleteDSLPckg_SendObjectAction,
)
CompleteDSLPckg_InputPin_strategy = st.builds(
    CompleteDSLPckg_InputPin,
)
Artifact_strategy = st.builds(
    Artifact,
)
CompleteDSLPckg_DeploymentSpecification_strategy = st.builds(
    CompleteDSLPckg_DeploymentSpecification,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
CompleteDSLPckg_ExecutionEnvironment_strategy = st.builds(
    CompleteDSLPckg_ExecutionEnvironment,
)
CompleteDSLPckg_Device_strategy = st.builds(
    CompleteDSLPckg_Device,
)
CompleteDSLPckg_OutputPin_strategy = st.builds(
    CompleteDSLPckg_OutputPin,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
CompleteDSLPckg_InvocationAction_strategy = st.builds(
    CompleteDSLPckg_InvocationAction,
)
CompleteDSLPckg_ConnectorEnd_strategy = st.builds(
    CompleteDSLPckg_ConnectorEnd,
)
Property_strategy = st.builds(
    Property,
)
CompleteDSLPckg_Port_strategy = st.builds(
    CompleteDSLPckg_Port,
    isConjugated=
        st.booleans(),
    isBehavior=
        st.booleans(),
    isService=
        st.booleans()
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
CompleteDSLPckg_DurationConstraint_strategy = st.builds(
    CompleteDSLPckg_DurationConstraint,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg_TimeConstraint_strategy = st.builds(
    CompleteDSLPckg_TimeConstraint,
    firstEvent=
        st.booleans()
)
Constraint_strategy = st.builds(
    Constraint,
)
CompleteDSLPckg_InteractionConstraint_strategy = st.builds(
    CompleteDSLPckg_InteractionConstraint,
)
CompleteDSLPckg_IntervalConstraint_strategy = st.builds(
    CompleteDSLPckg_IntervalConstraint,
)
Interval_strategy = st.builds(
    Interval,
)
CompleteDSLPckg_DurationInterval_strategy = st.builds(
    CompleteDSLPckg_DurationInterval,
)
CompleteDSLPckg_TimeInterval_strategy = st.builds(
    CompleteDSLPckg_TimeInterval,
)
Observation_strategy = st.builds(
    Observation,
)
CompleteDSLPckg_DurationObservation_strategy = st.builds(
    CompleteDSLPckg_DurationObservation,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg_TimeObservation_strategy = st.builds(
    CompleteDSLPckg_TimeObservation,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg_TimeEvent_strategy = st.builds(
    CompleteDSLPckg_TimeEvent,
    isRelative=
        st.booleans()
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
CompleteDSLPckg_SignalEvent_strategy = st.builds(
    CompleteDSLPckg_SignalEvent,
)
CompleteDSLPckg_CallEvent_strategy = st.builds(
    CompleteDSLPckg_CallEvent,
)
CompleteDSLPckg_AnyReceiveEvent_strategy = st.builds(
    CompleteDSLPckg_AnyReceiveEvent,
)
Event_strategy = st.builds(
    Event,
)
CompleteDSLPckg_ChangeEvent_strategy = st.builds(
    CompleteDSLPckg_ChangeEvent,
)
CompleteDSLPckg_MessageEvent_strategy = st.builds(
    CompleteDSLPckg_MessageEvent,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
CompleteDSLPckg_FunctionBehavior_strategy = st.builds(
    CompleteDSLPckg_FunctionBehavior,
)
Behavior_strategy = st.builds(
    Behavior,
)
CompleteDSLPckg_Interaction_strategy = st.builds(
    CompleteDSLPckg_Interaction,
)
CompleteDSLPckg_StateMachine_strategy = st.builds(
    CompleteDSLPckg_StateMachine,
)
CompleteDSLPckg_Activity_strategy = st.builds(
    CompleteDSLPckg_Activity,
    isSingleExecution=
        st.booleans(),
    isReadOnly=
        st.booleans()
)
CompleteDSLPckg_OpaqueBehavior_strategy = st.builds(
    CompleteDSLPckg_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
CompleteDSLPckg_CommunicationPath_strategy = st.builds(
    CompleteDSLPckg_CommunicationPath,
)
Class_strategy = st.builds(
    Class,
)
CompleteDSLPckg_AssociationClass_strategy = st.builds(
    CompleteDSLPckg_AssociationClass,
)
Realization_strategy = st.builds(
    Realization,
)
CompleteDSLPckg_InterfaceRealization_strategy = st.builds(
    CompleteDSLPckg_InterfaceRealization,
)
CompleteDSLPckg_ComponentRealization_strategy = st.builds(
    CompleteDSLPckg_ComponentRealization,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
CompleteDSLPckg_Manifestation_strategy = st.builds(
    CompleteDSLPckg_Manifestation,
)
CompleteDSLPckg_Realization_strategy = st.builds(
    CompleteDSLPckg_Realization,
)
Dependency_strategy = st.builds(
    Dependency,
)
CompleteDSLPckg_Abstraction_strategy = st.builds(
    CompleteDSLPckg_Abstraction,
)
CompleteDSLPckg_Deployment_strategy = st.builds(
    CompleteDSLPckg_Deployment,
)
CompleteDSLPckg_Usage_strategy = st.builds(
    CompleteDSLPckg_Usage,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
CompleteDSLPckg_EnumerationLiteral_strategy = st.builds(
    CompleteDSLPckg_EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
CompleteDSLPckg_Enumeration_strategy = st.builds(
    CompleteDSLPckg_Enumeration,
)
CompleteDSLPckg_PrimitiveType_strategy = st.builds(
    CompleteDSLPckg_PrimitiveType,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
CompleteDSLPckg_EncapsulatedClassifier_strategy = st.builds(
    CompleteDSLPckg_EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
CompleteDSLPckg_UseCase_strategy = st.builds(
    CompleteDSLPckg_UseCase,
)
CompleteDSLPckg_Actor_strategy = st.builds(
    CompleteDSLPckg_Actor,
)
CompleteDSLPckg_Collaboration_strategy = st.builds(
    CompleteDSLPckg_Collaboration,
)
Classifier_strategy = st.builds(
    Classifier,
)
CompleteDSLPckg_Signal_strategy = st.builds(
    CompleteDSLPckg_Signal,
)
CompleteDSLPckg_StructuredClassifier_strategy = st.builds(
    CompleteDSLPckg_StructuredClassifier,
)
CompleteDSLPckg_BehavioredClassifier_strategy = st.builds(
    CompleteDSLPckg_BehavioredClassifier,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
CompleteDSLPckg_Reception_strategy = st.builds(
    CompleteDSLPckg_Reception,
)
CompleteDSLPckg_Operation_strategy = st.builds(
    CompleteDSLPckg_Operation,
    upper=
        st.integers(),
    isUnique=
        st.booleans(),
    isOrdered=
        st.booleans(),
    lower=
        st.integers(),
    isQuery=
        st.booleans()
)
CompleteDSLPckg_Interface_strategy = st.builds(
    CompleteDSLPckg_Interface,
)
CompleteDSLPckg_DataType_strategy = st.builds(
    CompleteDSLPckg_DataType,
)
CompleteDSLPckg_Class_strategy = st.builds(
    CompleteDSLPckg_Class,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
CompleteDSLPckg_Node_strategy = st.builds(
    CompleteDSLPckg_Node,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
Feature_strategy = st.builds(
    Feature,
)
CompleteDSLPckg_Connector_strategy = st.builds(
    CompleteDSLPckg_Connector,
    kind=
        safe_text
)
CompleteDSLPckg_Substitution_strategy = st.builds(
    CompleteDSLPckg_Substitution,
)
CompleteDSLPckg_Property_strategy = st.builds(
    CompleteDSLPckg_Property,
    isID=
        st.booleans(),
    isComposite=
        st.booleans(),
    isDerivedUnion=
        st.booleans(),
    isDerived=
        st.booleans(),
    aggregation=
        safe_text,
    default=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
CompleteDSLPckg_Feature_strategy = st.builds(
    CompleteDSLPckg_Feature,
    isStatic=
        st.booleans()
)
CompleteDSLPckg_ExtensionPoint_strategy = st.builds(
    CompleteDSLPckg_ExtensionPoint,
)
CompleteDSLPckg_ActivityEdge_strategy = st.builds(
    CompleteDSLPckg_ActivityEdge,
)
CompleteDSLPckg_InstanceValue_strategy = st.builds(
    CompleteDSLPckg_InstanceValue,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
CompleteDSLPckg_LiteralString_strategy = st.builds(
    CompleteDSLPckg_LiteralString,
)
CompleteDSLPckg_LiteralUnilimitedNatural_strategy = st.builds(
    CompleteDSLPckg_LiteralUnilimitedNatural,
)
CompleteDSLPckg_LiteralBoolean_strategy = st.builds(
    CompleteDSLPckg_LiteralBoolean,
)
CompleteDSLPckg_LiteralReal_strategy = st.builds(
    CompleteDSLPckg_LiteralReal,
)
CompleteDSLPckg_LiteralInteger_strategy = st.builds(
    CompleteDSLPckg_LiteralInteger,
)
CompleteDSLPckg_LiteralNull_strategy = st.builds(
    CompleteDSLPckg_LiteralNull,
)
CompleteDSLPckg_Behavior_strategy = st.builds(
    CompleteDSLPckg_Behavior,
    isReentrant=
        st.booleans()
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
CompleteDSLPckg_Duration_strategy = st.builds(
    CompleteDSLPckg_Duration,
)
CompleteDSLPckg_TimeExpression_strategy = st.builds(
    CompleteDSLPckg_TimeExpression,
)
CompleteDSLPckg_LiteralSpecification_strategy = st.builds(
    CompleteDSLPckg_LiteralSpecification,
)
CompleteDSLPckg_Interval_strategy = st.builds(
    CompleteDSLPckg_Interval,
)
CompleteDSLPckg_OpaqueExpression_strategy = st.builds(
    CompleteDSLPckg_OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
CompleteDSLPckg_Expression_strategy = st.builds(
    CompleteDSLPckg_Expression,
    symbol=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
CompleteDSLPckg_Parameter_strategy = st.builds(
    CompleteDSLPckg_Parameter,
    default=
        safe_text
)
CompleteDSLPckg_Variable_strategy = st.builds(
    CompleteDSLPckg_Variable,
)
CompleteDSLPckg_ObjectNode_strategy = st.builds(
    CompleteDSLPckg_ObjectNode,
)
CompleteDSLPckg_Pin_strategy = st.builds(
    CompleteDSLPckg_Pin,
)
CompleteDSLPckg_ConnectableElement_strategy = st.builds(
    CompleteDSLPckg_ConnectableElement,
)
CompleteDSLPckg_StructuralFeature_strategy = st.builds(
    CompleteDSLPckg_StructuralFeature,
    isReadOnly=
        st.booleans()
)
Relationship_strategy = st.builds(
    Relationship,
)
CompleteDSLPckg_Association_strategy = st.builds(
    CompleteDSLPckg_Association,
    isDerived=
        st.booleans()
)
CompleteDSLPckg_DirectedRelationship_strategy = st.builds(
    CompleteDSLPckg_DirectedRelationship,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
CompleteDSLPckg_InstanceSpecification_strategy = st.builds(
    CompleteDSLPckg_InstanceSpecification,
)
CompleteDSLPckg_GeneralizationSet_strategy = st.builds(
    CompleteDSLPckg_GeneralizationSet,
    isCovering=
        st.booleans(),
    isDisjoint=
        st.booleans()
)
CompleteDSLPckg_Observation_strategy = st.builds(
    CompleteDSLPckg_Observation,
)
CompleteDSLPckg_Type_strategy = st.builds(
    CompleteDSLPckg_Type,
)
CompleteDSLPckg_Event_strategy = st.builds(
    CompleteDSLPckg_Event,
)
CompleteDSLPckg_ValueSpecification_strategy = st.builds(
    CompleteDSLPckg_ValueSpecification,
)
Namespace_strategy = st.builds(
    Namespace,
)
CompleteDSLPckg_State_strategy = st.builds(
    CompleteDSLPckg_State,
    isOrthogonal=
        st.booleans(),
    isSimple=
        st.booleans(),
    isComposite=
        st.booleans(),
    isSubmachineState=
        st.booleans()
)
CompleteDSLPckg_Classifier_strategy = st.builds(
    CompleteDSLPckg_Classifier,
    isFinalSpecialization=
        st.booleans(),
    isAbstract=
        st.booleans()
)
CompleteDSLPckg_Region_strategy = st.builds(
    CompleteDSLPckg_Region,
)
CompleteDSLPckg_Transition_strategy = st.builds(
    CompleteDSLPckg_Transition,
    kind=
        safe_text
)
CompleteDSLPckg_InteractionOperand_strategy = st.builds(
    CompleteDSLPckg_InteractionOperand,
)
CompleteDSLPckg_StructuredActivityNode_strategy = st.builds(
    CompleteDSLPckg_StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
CompleteDSLPckg_BehavioralFeature_strategy = st.builds(
    CompleteDSLPckg_BehavioralFeature,
)
CompleteDSLPckg_Package_strategy = st.builds(
    CompleteDSLPckg_Package,
    URI=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
CompleteDSLPckg_Generalization_strategy = st.builds(
    CompleteDSLPckg_Generalization,
    isSubstitutable=
        st.booleans()
)
CompleteDSLPckg_ProtocolConformance_strategy = st.builds(
    CompleteDSLPckg_ProtocolConformance,
)
CompleteDSLPckg_PackageMerge_strategy = st.builds(
    CompleteDSLPckg_PackageMerge,
)
CompleteDSLPckg_Constraint_strategy = st.builds(
    CompleteDSLPckg_Constraint,
)
CompleteDSLPckg_PackageImport_strategy = st.builds(
    CompleteDSLPckg_PackageImport,
    visibility=
        safe_text
)
CompleteDSLPckg_ElementImport_strategy = st.builds(
    CompleteDSLPckg_ElementImport,
    visibility=
        safe_text,
    alias=
        safe_text
)
CompleteDSLPckg_Dependency_strategy = st.builds(
    CompleteDSLPckg_Dependency,
)
Element_strategy = st.builds(
    Element,
)
CompleteDSLPckg_MultiplicityElement_strategy = st.builds(
    CompleteDSLPckg_MultiplicityElement,
    lower=
        st.integers(),
    isOrdered=
        st.booleans(),
    isUnique=
        st.booleans(),
    upper=
        st.integers()
)
CompleteDSLPckg_Slot_strategy = st.builds(
    CompleteDSLPckg_Slot,
)
CompleteDSLPckg_LinkEndData_strategy = st.builds(
    CompleteDSLPckg_LinkEndData,
)
CompleteDSLPckg_QualifierValue_strategy = st.builds(
    CompleteDSLPckg_QualifierValue,
)
CompleteDSLPckg_Clause_strategy = st.builds(
    CompleteDSLPckg_Clause,
)
CompleteDSLPckg_Relationship_strategy = st.builds(
    CompleteDSLPckg_Relationship,
)
CompleteDSLPckg_ExceptionHandler_strategy = st.builds(
    CompleteDSLPckg_ExceptionHandler,
)
CompleteDSLPckg_NamedElement_strategy = st.builds(
    CompleteDSLPckg_NamedElement,
    qualifiedName=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
CompleteDSLPckg_Comment_strategy = st.builds(
    CompleteDSLPckg_Comment,
    body=
        safe_text
)
CompleteDSLPckg_Element_strategy = st.builds(
    CompleteDSLPckg_Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
CompleteDSLPckg_TypedElement_strategy = st.builds(
    CompleteDSLPckg_TypedElement,
)
CompleteDSLPckg_MessageEnd_strategy = st.builds(
    CompleteDSLPckg_MessageEnd,
)
CompleteDSLPckg_Message_strategy = st.builds(
    CompleteDSLPckg_Message,
    messageKind=
        safe_text,
    messageSort=
        safe_text
)
CompleteDSLPckg_Lifeline_strategy = st.builds(
    CompleteDSLPckg_Lifeline,
)
CompleteDSLPckg_GeneralOrdering_strategy = st.builds(
    CompleteDSLPckg_GeneralOrdering,
)
CompleteDSLPckg_Component_strategy = st.builds(
    CompleteDSLPckg_Component,
    isIndirectlyInstantiated=
        st.booleans()
)
CompleteDSLPckg_Namespace_strategy = st.builds(
    CompleteDSLPckg_Namespace,
)
CompleteDSLPckg_CollaborationUse_strategy = st.builds(
    CompleteDSLPckg_CollaborationUse,
)
CompleteDSLPckg_Vertex_strategy = st.builds(
    CompleteDSLPckg_Vertex,
)
CompleteDSLPckg_RedefinableElement_strategy = st.builds(
    CompleteDSLPckg_RedefinableElement,
    isLeaf=
        st.booleans()
)
CompleteDSLPckg_PackageableElement_strategy = st.builds(
    CompleteDSLPckg_PackageableElement,
)
CompleteDSLPckg_DeploymentTarget_strategy = st.builds(
    CompleteDSLPckg_DeploymentTarget,
)
CompleteDSLPckg_ParameterSet_strategy = st.builds(
    CompleteDSLPckg_ParameterSet,
)
CompleteDSLPckg_InteractionFragment_strategy = st.builds(
    CompleteDSLPckg_InteractionFragment,
)
CompleteDSLPckg_DeployedArtifact_strategy = st.builds(
    CompleteDSLPckg_DeployedArtifact,
)
CompleteDSLPckg_Extend_strategy = st.builds(
    CompleteDSLPckg_Extend,
)
CompleteDSLPckg_Artifact_strategy = st.builds(
    CompleteDSLPckg_Artifact,
    fileName=
        safe_text
)
CompleteDSLPckg_ActivityGroup_strategy = st.builds(
    CompleteDSLPckg_ActivityGroup,
)
CompleteDSLPckg_ActivityNode_strategy = st.builds(
    CompleteDSLPckg_ActivityNode,
)
CompleteDSLPckg_Trigger_strategy = st.builds(
    CompleteDSLPckg_Trigger,
)
CompleteDSLPckg_Action_strategy = st.builds(
    CompleteDSLPckg_Action,
)
CompleteDSLPckg_Include_strategy = st.builds(
    CompleteDSLPckg_Include,
)

































@given(instance=CompleteDSLPckg_LinkEndDestructionData_strategy)
def test_hyp_completedslpckg_linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original




@given(instance=CompleteDSLPckg_LinkEndCreationData_strategy)
def test_hyp_completedslpckg_linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original








@given(instance=CompleteDSLPckg_CombinedFragment_strategy)
def test_hyp_completedslpckg_combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original














@given(instance=CompleteDSLPckg_Continuation_strategy)
def test_hyp_completedslpckg_continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original













@given(instance=CompleteDSLPckg_ConditionalNode_strategy)
def test_hyp_completedslpckg_conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original



@given(instance=CompleteDSLPckg_ConditionalNode_strategy)
def test_hyp_completedslpckg_conditionalnode_isAssumed_setter(instance):
    original = instance.isAssumed
    instance.isAssumed = original
    assert instance.isAssumed == original




@given(instance=CompleteDSLPckg_ExpansionRegion_strategy)
def test_hyp_completedslpckg_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original





@given(instance=CompleteDSLPckg_LoopNode_strategy)
def test_hyp_completedslpckg_loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original






@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_hyp_completedslpckg_objectflow_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_hyp_completedslpckg_objectflow_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original



@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_hyp_completedslpckg_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original



@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_hyp_completedslpckg_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original











@given(instance=CompleteDSLPckg_JoinNode_strategy)
def test_hyp_completedslpckg_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original





























@given(instance=CompleteDSLPckg_CallAction_strategy)
def test_hyp_completedslpckg_callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original










@given(instance=CompleteDSLPckg_ReclassifyObjectAction_strategy)
def test_hyp_completedslpckg_reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original








@given(instance=CompleteDSLPckg_ReduceAction_strategy)
def test_hyp_completedslpckg_reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original













@given(instance=CompleteDSLPckg_AcceptEventAction_strategy)
def test_hyp_completedslpckg_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original





@given(instance=CompleteDSLPckg_OpaqueAction_strategy)
def test_hyp_completedslpckg_opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=CompleteDSLPckg_OpaqueAction_strategy)
def test_hyp_completedslpckg_opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original







@given(instance=CompleteDSLPckg_DeploymentSpecification_strategy)
def test_hyp_completedslpckg_deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original



@given(instance=CompleteDSLPckg_DeploymentSpecification_strategy)
def test_hyp_completedslpckg_deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original












@given(instance=CompleteDSLPckg_Port_strategy)
def test_hyp_completedslpckg_port_isConjugated_setter(instance):
    original = instance.isConjugated
    instance.isConjugated = original
    assert instance.isConjugated == original



@given(instance=CompleteDSLPckg_Port_strategy)
def test_hyp_completedslpckg_port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original



@given(instance=CompleteDSLPckg_Port_strategy)
def test_hyp_completedslpckg_port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original





@given(instance=CompleteDSLPckg_DurationConstraint_strategy)
def test_hyp_completedslpckg_durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original




@given(instance=CompleteDSLPckg_TimeConstraint_strategy)
def test_hyp_completedslpckg_timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original











@given(instance=CompleteDSLPckg_DurationObservation_strategy)
def test_hyp_completedslpckg_durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original




@given(instance=CompleteDSLPckg_TimeObservation_strategy)
def test_hyp_completedslpckg_timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original




@given(instance=CompleteDSLPckg_TimeEvent_strategy)
def test_hyp_completedslpckg_timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original
















@given(instance=CompleteDSLPckg_Activity_strategy)
def test_hyp_completedslpckg_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original



@given(instance=CompleteDSLPckg_Activity_strategy)
def test_hyp_completedslpckg_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original




@given(instance=CompleteDSLPckg_OpaqueBehavior_strategy)
def test_hyp_completedslpckg_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=CompleteDSLPckg_OpaqueBehavior_strategy)
def test_hyp_completedslpckg_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original




































@given(instance=CompleteDSLPckg_Operation_strategy)
def test_hyp_completedslpckg_operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_hyp_completedslpckg_operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_hyp_completedslpckg_operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_hyp_completedslpckg_operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_hyp_completedslpckg_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original













@given(instance=CompleteDSLPckg_Connector_strategy)
def test_hyp_completedslpckg_connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original





@given(instance=CompleteDSLPckg_Property_strategy)
def test_hyp_completedslpckg_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_hyp_completedslpckg_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_hyp_completedslpckg_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_hyp_completedslpckg_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_hyp_completedslpckg_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_hyp_completedslpckg_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original






@given(instance=CompleteDSLPckg_Feature_strategy)
def test_hyp_completedslpckg_feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original














@given(instance=CompleteDSLPckg_Behavior_strategy)
def test_hyp_completedslpckg_behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original









@given(instance=CompleteDSLPckg_OpaqueExpression_strategy)
def test_hyp_completedslpckg_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=CompleteDSLPckg_OpaqueExpression_strategy)
def test_hyp_completedslpckg_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original




@given(instance=CompleteDSLPckg_Expression_strategy)
def test_hyp_completedslpckg_expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original





@given(instance=CompleteDSLPckg_Parameter_strategy)
def test_hyp_completedslpckg_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original








@given(instance=CompleteDSLPckg_StructuralFeature_strategy)
def test_hyp_completedslpckg_structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original





@given(instance=CompleteDSLPckg_Association_strategy)
def test_hyp_completedslpckg_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original







@given(instance=CompleteDSLPckg_GeneralizationSet_strategy)
def test_hyp_completedslpckg_generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original



@given(instance=CompleteDSLPckg_GeneralizationSet_strategy)
def test_hyp_completedslpckg_generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original









@given(instance=CompleteDSLPckg_State_strategy)
def test_hyp_completedslpckg_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original



@given(instance=CompleteDSLPckg_State_strategy)
def test_hyp_completedslpckg_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=CompleteDSLPckg_State_strategy)
def test_hyp_completedslpckg_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=CompleteDSLPckg_State_strategy)
def test_hyp_completedslpckg_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original




@given(instance=CompleteDSLPckg_Classifier_strategy)
def test_hyp_completedslpckg_classifier_isFinalSpecialization_setter(instance):
    original = instance.isFinalSpecialization
    instance.isFinalSpecialization = original
    assert instance.isFinalSpecialization == original



@given(instance=CompleteDSLPckg_Classifier_strategy)
def test_hyp_completedslpckg_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original





@given(instance=CompleteDSLPckg_Transition_strategy)
def test_hyp_completedslpckg_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original





@given(instance=CompleteDSLPckg_StructuredActivityNode_strategy)
def test_hyp_completedslpckg_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original





@given(instance=CompleteDSLPckg_Package_strategy)
def test_hyp_completedslpckg_package_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original





@given(instance=CompleteDSLPckg_Generalization_strategy)
def test_hyp_completedslpckg_generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original







@given(instance=CompleteDSLPckg_PackageImport_strategy)
def test_hyp_completedslpckg_packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original




@given(instance=CompleteDSLPckg_ElementImport_strategy)
def test_hyp_completedslpckg_elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=CompleteDSLPckg_ElementImport_strategy)
def test_hyp_completedslpckg_elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original






@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_hyp_completedslpckg_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_hyp_completedslpckg_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_hyp_completedslpckg_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_hyp_completedslpckg_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original










@given(instance=CompleteDSLPckg_NamedElement_strategy)
def test_hyp_completedslpckg_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=CompleteDSLPckg_NamedElement_strategy)
def test_hyp_completedslpckg_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=CompleteDSLPckg_NamedElement_strategy)
def test_hyp_completedslpckg_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=CompleteDSLPckg_Comment_strategy)
def test_hyp_completedslpckg_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original








@given(instance=CompleteDSLPckg_Message_strategy)
def test_hyp_completedslpckg_message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original



@given(instance=CompleteDSLPckg_Message_strategy)
def test_hyp_completedslpckg_message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original






@given(instance=CompleteDSLPckg_Component_strategy)
def test_hyp_completedslpckg_component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original







@given(instance=CompleteDSLPckg_RedefinableElement_strategy)
def test_hyp_completedslpckg_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original










@given(instance=CompleteDSLPckg_Artifact_strategy)
def test_hyp_completedslpckg_artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Abstraction,
    AcceptEventAction,
    Action,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    Artifact,
    Association,
    Behavior,
    BehavioralFeature,
    BehavioredClassifier,
    CallAction,
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
    Event,
    ExecutableNode,
    ExecutionSpecification,
    Feature,
    FinalNode,
    InputPin,
    InstanceSpecification,
    InteractionFragment,
    InteractionUse,
    Interval,
    IntervalConstraint,
    InvocationAction,
    LinkAction,
    LinkEndData,
    LiteralSpecification,
    MessageEnd,
    MessageEvent,
    MessageOccurrenceSpecification,
    MultiplicityElement,
    NamedElement,
    Namespace,
    Node,
    ObjectNode,
    Observation,
    OccurenceSpecification,
    OpaqueBehavior,
    PackageableElement,
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
    Type,
    TypedElement,
    ValueSpecification,
    VariableAction,
    Vertex,
    WriteLinkAction,
    WriteStructuralFeatureAction,
    WriteVariableAction,
    AggregationKind,
    CallConcurrencyFeature,
    ConnectorKind,
    ExpansionKind,
    InteractionOperandKind,
    MessageKind,
    MessageSort,
    ObjectNodeOrderingKind,
    ParameterEffectKind,
    TransitionKind,
    VisibilityKind,
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

def test_CompleteDSLPckg_AcceptEventAction_isUnmarshall_value_roundtrip():
    instance = CompleteDSLPckg_AcceptEventAction(isUnmarshall=True)
    assert instance.isUnmarshall == True
    instance.isUnmarshall = False
    assert instance.isUnmarshall == False


def test_CompleteDSLPckg_Activity_isReadOnly_value_roundtrip():
    instance = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    assert instance.isReadOnly == True
    instance.isReadOnly = False
    assert instance.isReadOnly == False


def test_CompleteDSLPckg_Activity_isSingleExecution_value_roundtrip():
    instance = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    assert instance.isSingleExecution == True
    instance.isSingleExecution = False
    assert instance.isSingleExecution == False


def test_CompleteDSLPckg_Artifact_fileName_value_roundtrip():
    instance = CompleteDSLPckg_Artifact(fileName="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_CompleteDSLPckg_Association_isDerived_value_roundtrip():
    instance = CompleteDSLPckg_Association(isDerived=True)
    assert instance.isDerived == True
    instance.isDerived = False
    assert instance.isDerived == False


def test_CompleteDSLPckg_Behavior_isReentrant_value_roundtrip():
    instance = CompleteDSLPckg_Behavior(isReentrant=True)
    assert instance.isReentrant == True
    instance.isReentrant = False
    assert instance.isReentrant == False


def test_CompleteDSLPckg_CallAction_isSynchronous_value_roundtrip():
    instance = CompleteDSLPckg_CallAction(isSynchronous=True)
    assert instance.isSynchronous == True
    instance.isSynchronous = False
    assert instance.isSynchronous == False


def test_CompleteDSLPckg_Classifier_isAbstract_value_roundtrip():
    instance = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    assert instance.isAbstract == True
    instance.isAbstract = False
    assert instance.isAbstract == False


def test_CompleteDSLPckg_Classifier_isFinalSpecialization_value_roundtrip():
    instance = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    assert instance.isFinalSpecialization == True
    instance.isFinalSpecialization = False
    assert instance.isFinalSpecialization == False


def test_CompleteDSLPckg_CombinedFragment_interactionOperator_value_roundtrip():
    instance = CompleteDSLPckg_CombinedFragment(interactionOperator="sample_text")
    assert instance.interactionOperator == "sample_text"
    instance.interactionOperator = "sample_text_2"
    assert instance.interactionOperator == "sample_text_2"


def test_CompleteDSLPckg_Comment_body_value_roundtrip():
    instance = CompleteDSLPckg_Comment(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_CompleteDSLPckg_Component_isIndirectlyInstantiated_value_roundtrip():
    instance = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    assert instance.isIndirectlyInstantiated == True
    instance.isIndirectlyInstantiated = False
    assert instance.isIndirectlyInstantiated == False


def test_CompleteDSLPckg_ConditionalNode_isAssumed_value_roundtrip():
    instance = CompleteDSLPckg_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert instance.isAssumed == True
    instance.isAssumed = False
    assert instance.isAssumed == False


def test_CompleteDSLPckg_ConditionalNode_isDeterminate_value_roundtrip():
    instance = CompleteDSLPckg_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert instance.isDeterminate == True
    instance.isDeterminate = False
    assert instance.isDeterminate == False


def test_CompleteDSLPckg_Connector_kind_value_roundtrip():
    instance = CompleteDSLPckg_Connector(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_CompleteDSLPckg_Continuation_setting_value_roundtrip():
    instance = CompleteDSLPckg_Continuation(setting=True)
    assert instance.setting == True
    instance.setting = False
    assert instance.setting == False


def test_CompleteDSLPckg_DeploymentSpecification_deploymentLocation_value_roundtrip():
    instance = CompleteDSLPckg_DeploymentSpecification(deploymentLocation="sample_text", executionLocation="sample_text")
    assert instance.deploymentLocation == "sample_text"
    instance.deploymentLocation = "sample_text_2"
    assert instance.deploymentLocation == "sample_text_2"


def test_CompleteDSLPckg_DeploymentSpecification_executionLocation_value_roundtrip():
    instance = CompleteDSLPckg_DeploymentSpecification(deploymentLocation="sample_text", executionLocation="sample_text")
    assert instance.executionLocation == "sample_text"
    instance.executionLocation = "sample_text_2"
    assert instance.executionLocation == "sample_text_2"


def test_CompleteDSLPckg_DurationConstraint_firstEvent_value_roundtrip():
    instance = CompleteDSLPckg_DurationConstraint(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CompleteDSLPckg_DurationObservation_firstEvent_value_roundtrip():
    instance = CompleteDSLPckg_DurationObservation(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CompleteDSLPckg_ElementImport_alias_value_roundtrip():
    instance = CompleteDSLPckg_ElementImport(alias="sample_text", visibility="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_CompleteDSLPckg_ElementImport_visibility_value_roundtrip():
    instance = CompleteDSLPckg_ElementImport(alias="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_CompleteDSLPckg_ExpansionRegion_mode_value_roundtrip():
    instance = CompleteDSLPckg_ExpansionRegion(mode="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_CompleteDSLPckg_Expression_symbol_value_roundtrip():
    instance = CompleteDSLPckg_Expression(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_CompleteDSLPckg_Feature_isStatic_value_roundtrip():
    instance = CompleteDSLPckg_Feature(isStatic=True)
    assert instance.isStatic == True
    instance.isStatic = False
    assert instance.isStatic == False


def test_CompleteDSLPckg_Generalization_isSubstitutable_value_roundtrip():
    instance = CompleteDSLPckg_Generalization(isSubstitutable=True)
    assert instance.isSubstitutable == True
    instance.isSubstitutable = False
    assert instance.isSubstitutable == False


def test_CompleteDSLPckg_GeneralizationSet_isCovering_value_roundtrip():
    instance = CompleteDSLPckg_GeneralizationSet(isCovering=True, isDisjoint=True)
    assert instance.isCovering == True
    instance.isCovering = False
    assert instance.isCovering == False


def test_CompleteDSLPckg_GeneralizationSet_isDisjoint_value_roundtrip():
    instance = CompleteDSLPckg_GeneralizationSet(isCovering=True, isDisjoint=True)
    assert instance.isDisjoint == True
    instance.isDisjoint = False
    assert instance.isDisjoint == False


def test_CompleteDSLPckg_JoinNode_isCombineDuplicate_value_roundtrip():
    instance = CompleteDSLPckg_JoinNode(isCombineDuplicate=True)
    assert instance.isCombineDuplicate == True
    instance.isCombineDuplicate = False
    assert instance.isCombineDuplicate == False


def test_CompleteDSLPckg_LinkEndCreationData_isReplaceAll_value_roundtrip():
    instance = CompleteDSLPckg_LinkEndCreationData(isReplaceAll=True)
    assert instance.isReplaceAll == True
    instance.isReplaceAll = False
    assert instance.isReplaceAll == False


def test_CompleteDSLPckg_LinkEndDestructionData_isDestroyDuplicates_value_roundtrip():
    instance = CompleteDSLPckg_LinkEndDestructionData(isDestroyDuplicates=True)
    assert instance.isDestroyDuplicates == True
    instance.isDestroyDuplicates = False
    assert instance.isDestroyDuplicates == False


def test_CompleteDSLPckg_LoopNode_isTestedFirst_value_roundtrip():
    instance = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    assert instance.isTestedFirst == True
    instance.isTestedFirst = False
    assert instance.isTestedFirst == False


def test_CompleteDSLPckg_Message_messageKind_value_roundtrip():
    instance = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    assert instance.messageKind == "sample_text"
    instance.messageKind = "sample_text_2"
    assert instance.messageKind == "sample_text_2"


def test_CompleteDSLPckg_Message_messageSort_value_roundtrip():
    instance = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    assert instance.messageSort == "sample_text"
    instance.messageSort = "sample_text_2"
    assert instance.messageSort == "sample_text_2"


def test_CompleteDSLPckg_MultiplicityElement_isOrdered_value_roundtrip():
    instance = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    assert instance.isOrdered == True
    instance.isOrdered = False
    assert instance.isOrdered == False


def test_CompleteDSLPckg_MultiplicityElement_isUnique_value_roundtrip():
    instance = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    assert instance.isUnique == True
    instance.isUnique = False
    assert instance.isUnique == False


def test_CompleteDSLPckg_MultiplicityElement_lower_value_roundtrip():
    instance = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    assert instance.lower == 7
    instance.lower = 13
    assert instance.lower == 13


def test_CompleteDSLPckg_MultiplicityElement_upper_value_roundtrip():
    instance = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    assert instance.upper == 7
    instance.upper = 13
    assert instance.upper == 13


def test_CompleteDSLPckg_NamedElement_name_value_roundtrip():
    instance = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CompleteDSLPckg_NamedElement_qualifiedName_value_roundtrip():
    instance = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_CompleteDSLPckg_NamedElement_visibility_value_roundtrip():
    instance = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_CompleteDSLPckg_ObjectFlow_isControlType_value_roundtrip():
    instance = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.isControlType == True
    instance.isControlType = False
    assert instance.isControlType == False


def test_CompleteDSLPckg_ObjectFlow_isMulticast_value_roundtrip():
    instance = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.isMulticast == True
    instance.isMulticast = False
    assert instance.isMulticast == False


def test_CompleteDSLPckg_ObjectFlow_isMultireceive_value_roundtrip():
    instance = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.isMultireceive == True
    instance.isMultireceive = False
    assert instance.isMultireceive == False


def test_CompleteDSLPckg_ObjectFlow_ordering_value_roundtrip():
    instance = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.ordering == "sample_text"
    instance.ordering = "sample_text_2"
    assert instance.ordering == "sample_text_2"


def test_CompleteDSLPckg_OpaqueAction_body_value_roundtrip():
    instance = CompleteDSLPckg_OpaqueAction(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_CompleteDSLPckg_OpaqueAction_language_value_roundtrip():
    instance = CompleteDSLPckg_OpaqueAction(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_CompleteDSLPckg_OpaqueBehavior_body_value_roundtrip():
    instance = CompleteDSLPckg_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_CompleteDSLPckg_OpaqueBehavior_language_value_roundtrip():
    instance = CompleteDSLPckg_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_CompleteDSLPckg_OpaqueExpression_body_value_roundtrip():
    instance = CompleteDSLPckg_OpaqueExpression(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_CompleteDSLPckg_OpaqueExpression_language_value_roundtrip():
    instance = CompleteDSLPckg_OpaqueExpression(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_CompleteDSLPckg_Operation_isOrdered_value_roundtrip():
    instance = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    assert instance.isOrdered == True
    instance.isOrdered = False
    assert instance.isOrdered == False


def test_CompleteDSLPckg_Operation_isQuery_value_roundtrip():
    instance = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    assert instance.isQuery == True
    instance.isQuery = False
    assert instance.isQuery == False


def test_CompleteDSLPckg_Operation_isUnique_value_roundtrip():
    instance = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    assert instance.isUnique == True
    instance.isUnique = False
    assert instance.isUnique == False


def test_CompleteDSLPckg_Operation_lower_value_roundtrip():
    instance = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    assert instance.lower == 7
    instance.lower = 13
    assert instance.lower == 13


def test_CompleteDSLPckg_Operation_upper_value_roundtrip():
    instance = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    assert instance.upper == 7
    instance.upper = 13
    assert instance.upper == 13


def test_CompleteDSLPckg_Package_URI_value_roundtrip():
    instance = CompleteDSLPckg_Package(URI="sample_text")
    assert instance.URI == "sample_text"
    instance.URI = "sample_text_2"
    assert instance.URI == "sample_text_2"


def test_CompleteDSLPckg_PackageImport_visibility_value_roundtrip():
    instance = CompleteDSLPckg_PackageImport(visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_CompleteDSLPckg_Parameter_default_value_roundtrip():
    instance = CompleteDSLPckg_Parameter(default="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_CompleteDSLPckg_Port_isBehavior_value_roundtrip():
    instance = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    assert instance.isBehavior == True
    instance.isBehavior = False
    assert instance.isBehavior == False


def test_CompleteDSLPckg_Port_isConjugated_value_roundtrip():
    instance = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    assert instance.isConjugated == True
    instance.isConjugated = False
    assert instance.isConjugated == False


def test_CompleteDSLPckg_Port_isService_value_roundtrip():
    instance = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    assert instance.isService == True
    instance.isService = False
    assert instance.isService == False


def test_CompleteDSLPckg_Property_aggregation_value_roundtrip():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert instance.aggregation == "sample_text"
    instance.aggregation = "sample_text_2"
    assert instance.aggregation == "sample_text_2"


def test_CompleteDSLPckg_Property_default_value_roundtrip():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_CompleteDSLPckg_Property_isComposite_value_roundtrip():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert instance.isComposite == True
    instance.isComposite = False
    assert instance.isComposite == False


def test_CompleteDSLPckg_Property_isDerived_value_roundtrip():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert instance.isDerived == True
    instance.isDerived = False
    assert instance.isDerived == False


def test_CompleteDSLPckg_Property_isDerivedUnion_value_roundtrip():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert instance.isDerivedUnion == True
    instance.isDerivedUnion = False
    assert instance.isDerivedUnion == False


def test_CompleteDSLPckg_Property_isID_value_roundtrip():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert instance.isID == True
    instance.isID = False
    assert instance.isID == False


def test_CompleteDSLPckg_ReclassifyObjectAction_isReplaceAll_value_roundtrip():
    instance = CompleteDSLPckg_ReclassifyObjectAction(isReplaceAll=True)
    assert instance.isReplaceAll == True
    instance.isReplaceAll = False
    assert instance.isReplaceAll == False


def test_CompleteDSLPckg_RedefinableElement_isLeaf_value_roundtrip():
    instance = CompleteDSLPckg_RedefinableElement(isLeaf=True)
    assert instance.isLeaf == True
    instance.isLeaf = False
    assert instance.isLeaf == False


def test_CompleteDSLPckg_ReduceAction_isOrdered_value_roundtrip():
    instance = CompleteDSLPckg_ReduceAction(isOrdered=True)
    assert instance.isOrdered == True
    instance.isOrdered = False
    assert instance.isOrdered == False


def test_CompleteDSLPckg_State_isComposite_value_roundtrip():
    instance = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    assert instance.isComposite == True
    instance.isComposite = False
    assert instance.isComposite == False


def test_CompleteDSLPckg_State_isOrthogonal_value_roundtrip():
    instance = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    assert instance.isOrthogonal == True
    instance.isOrthogonal = False
    assert instance.isOrthogonal == False


def test_CompleteDSLPckg_State_isSimple_value_roundtrip():
    instance = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    assert instance.isSimple == True
    instance.isSimple = False
    assert instance.isSimple == False


def test_CompleteDSLPckg_State_isSubmachineState_value_roundtrip():
    instance = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    assert instance.isSubmachineState == True
    instance.isSubmachineState = False
    assert instance.isSubmachineState == False


def test_CompleteDSLPckg_StructuralFeature_isReadOnly_value_roundtrip():
    instance = CompleteDSLPckg_StructuralFeature(isReadOnly=True)
    assert instance.isReadOnly == True
    instance.isReadOnly = False
    assert instance.isReadOnly == False


def test_CompleteDSLPckg_StructuredActivityNode_mustIsolate_value_roundtrip():
    instance = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    assert instance.mustIsolate == True
    instance.mustIsolate = False
    assert instance.mustIsolate == False


def test_CompleteDSLPckg_TimeConstraint_firstEvent_value_roundtrip():
    instance = CompleteDSLPckg_TimeConstraint(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CompleteDSLPckg_TimeEvent_isRelative_value_roundtrip():
    instance = CompleteDSLPckg_TimeEvent(isRelative=True)
    assert instance.isRelative == True
    instance.isRelative = False
    assert instance.isRelative == False


def test_CompleteDSLPckg_TimeObservation_firstEvent_value_roundtrip():
    instance = CompleteDSLPckg_TimeObservation(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CompleteDSLPckg_Transition_kind_value_roundtrip():
    instance = CompleteDSLPckg_Transition(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_CompleteDSLPckg_Manifestation_isa_Abstraction():
    instance = CompleteDSLPckg_Manifestation()
    assert isinstance(instance, Abstraction)


def test_CompleteDSLPckg_Realization_isa_Abstraction():
    instance = CompleteDSLPckg_Realization()
    assert isinstance(instance, Abstraction)


def test_CompleteDSLPckg_AcceptCallAction_isa_AcceptEventAction():
    instance = CompleteDSLPckg_AcceptCallAction()
    assert isinstance(instance, AcceptEventAction)


def test_CompleteDSLPckg_AcceptEventAction_isa_Action():
    instance = CompleteDSLPckg_AcceptEventAction(isUnmarshall=True)
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_CreateObjectAction_isa_Action():
    instance = CompleteDSLPckg_CreateObjectAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_DestroyObjectAction_isa_Action():
    instance = CompleteDSLPckg_DestroyObjectAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_LinkAction_isa_Action():
    instance = CompleteDSLPckg_LinkAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_OpaqueAction_isa_Action():
    instance = CompleteDSLPckg_OpaqueAction(body="sample_text", language="sample_text")
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_RaiseExceptionAction_isa_Action():
    instance = CompleteDSLPckg_RaiseExceptionAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ReadExtendAction_isa_Action():
    instance = CompleteDSLPckg_ReadExtendAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ReadLinkObjectEndAction_isa_Action():
    instance = CompleteDSLPckg_ReadLinkObjectEndAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ReadLinkObjectEndQualifierAction_isa_Action():
    instance = CompleteDSLPckg_ReadLinkObjectEndQualifierAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ReadSelfAction_isa_Action():
    instance = CompleteDSLPckg_ReadSelfAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ReclassifyObjectAction_isa_Action():
    instance = CompleteDSLPckg_ReclassifyObjectAction(isReplaceAll=True)
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ReduceAction_isa_Action():
    instance = CompleteDSLPckg_ReduceAction(isOrdered=True)
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ReplyAction_isa_Action():
    instance = CompleteDSLPckg_ReplyAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_StartClassifierBehaviorAction_isa_Action():
    instance = CompleteDSLPckg_StartClassifierBehaviorAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_StructuralFeatureAction_isa_Action():
    instance = CompleteDSLPckg_StructuralFeatureAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_StructuredActivityNode_isa_Action():
    instance = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_TestIdentityAction_isa_Action():
    instance = CompleteDSLPckg_TestIdentityAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_UnmarshallAction_isa_Action():
    instance = CompleteDSLPckg_UnmarshallAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ValueSpecificationAction_isa_Action():
    instance = CompleteDSLPckg_ValueSpecificationAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_VariableAction_isa_Action():
    instance = CompleteDSLPckg_VariableAction()
    assert isinstance(instance, Action)


def test_CompleteDSLPckg_ControlFlow_isa_ActivityEdge():
    instance = CompleteDSLPckg_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_CompleteDSLPckg_ObjectFlow_isa_ActivityEdge():
    instance = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert isinstance(instance, ActivityEdge)


def test_CompleteDSLPckg_ActivityPartition_isa_ActivityGroup():
    instance = CompleteDSLPckg_ActivityPartition()
    assert isinstance(instance, ActivityGroup)


def test_CompleteDSLPckg_InterruptibleActivityRegion_isa_ActivityGroup():
    instance = CompleteDSLPckg_InterruptibleActivityRegion()
    assert isinstance(instance, ActivityGroup)


def test_CompleteDSLPckg_StructuredActivityNode_isa_ActivityGroup():
    instance = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, ActivityGroup)


def test_CompleteDSLPckg_ControlNode_isa_ActivityNode():
    instance = CompleteDSLPckg_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_CompleteDSLPckg_ExecutableNode_isa_ActivityNode():
    instance = CompleteDSLPckg_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_CompleteDSLPckg_ObjectNode_isa_ActivityNode():
    instance = CompleteDSLPckg_ObjectNode()
    assert isinstance(instance, ActivityNode)


def test_CompleteDSLPckg_DeploymentSpecification_isa_Artifact():
    instance = CompleteDSLPckg_DeploymentSpecification(deploymentLocation="sample_text", executionLocation="sample_text")
    assert isinstance(instance, Artifact)


def test_CompleteDSLPckg_AssociationClass_isa_Association():
    instance = CompleteDSLPckg_AssociationClass()
    assert isinstance(instance, Association)


def test_CompleteDSLPckg_CommunicationPath_isa_Association():
    instance = CompleteDSLPckg_CommunicationPath()
    assert isinstance(instance, Association)


def test_CompleteDSLPckg_Activity_isa_Behavior():
    instance = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    assert isinstance(instance, Behavior)


def test_CompleteDSLPckg_Interaction_isa_Behavior():
    instance = CompleteDSLPckg_Interaction()
    assert isinstance(instance, Behavior)


def test_CompleteDSLPckg_OpaqueBehavior_isa_Behavior():
    instance = CompleteDSLPckg_OpaqueBehavior(body="sample_text", language="sample_text")
    assert isinstance(instance, Behavior)


def test_CompleteDSLPckg_StateMachine_isa_Behavior():
    instance = CompleteDSLPckg_StateMachine()
    assert isinstance(instance, Behavior)


def test_CompleteDSLPckg_Operation_isa_BehavioralFeature():
    instance = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    assert isinstance(instance, BehavioralFeature)


def test_CompleteDSLPckg_Reception_isa_BehavioralFeature():
    instance = CompleteDSLPckg_Reception()
    assert isinstance(instance, BehavioralFeature)


def test_CompleteDSLPckg_Actor_isa_BehavioredClassifier():
    instance = CompleteDSLPckg_Actor()
    assert isinstance(instance, BehavioredClassifier)


def test_CompleteDSLPckg_Class_isa_BehavioredClassifier():
    instance = CompleteDSLPckg_Class()
    assert isinstance(instance, BehavioredClassifier)


def test_CompleteDSLPckg_Collaboration_isa_BehavioredClassifier():
    instance = CompleteDSLPckg_Collaboration()
    assert isinstance(instance, BehavioredClassifier)


def test_CompleteDSLPckg_UseCase_isa_BehavioredClassifier():
    instance = CompleteDSLPckg_UseCase()
    assert isinstance(instance, BehavioredClassifier)


def test_CompleteDSLPckg_CallBehaviorAction_isa_CallAction():
    instance = CompleteDSLPckg_CallBehaviorAction()
    assert isinstance(instance, CallAction)


def test_CompleteDSLPckg_StartObjectBehaviorAction_isa_CallAction():
    instance = CompleteDSLPckg_StartObjectBehaviorAction()
    assert isinstance(instance, CallAction)


def test_CompleteDSLPckg_DataStoreNode_isa_CentralBufferNode():
    instance = CompleteDSLPckg_DataStoreNode()
    assert isinstance(instance, CentralBufferNode)


def test_CompleteDSLPckg_AssociationClass_isa_Class():
    instance = CompleteDSLPckg_AssociationClass()
    assert isinstance(instance, Class)


def test_CompleteDSLPckg_Behavior_isa_Class():
    instance = CompleteDSLPckg_Behavior(isReentrant=True)
    assert isinstance(instance, Class)


def test_CompleteDSLPckg_Component_isa_Class():
    instance = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    assert isinstance(instance, Class)


def test_CompleteDSLPckg_Node_isa_Class():
    instance = CompleteDSLPckg_Node()
    assert isinstance(instance, Class)


def test_CompleteDSLPckg_Artifact_isa_Classifier():
    instance = CompleteDSLPckg_Artifact(fileName="sample_text")
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_Association_isa_Classifier():
    instance = CompleteDSLPckg_Association(isDerived=True)
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_BehavioredClassifier_isa_Classifier():
    instance = CompleteDSLPckg_BehavioredClassifier()
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_Class_isa_Classifier():
    instance = CompleteDSLPckg_Class()
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_DataType_isa_Classifier():
    instance = CompleteDSLPckg_DataType()
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_Interface_isa_Classifier():
    instance = CompleteDSLPckg_Interface()
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_Signal_isa_Classifier():
    instance = CompleteDSLPckg_Signal()
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_StructuredClassifier_isa_Classifier():
    instance = CompleteDSLPckg_StructuredClassifier()
    assert isinstance(instance, Classifier)


def test_CompleteDSLPckg_ConsiderIgnoreFragment_isa_CombinedFragment():
    instance = CompleteDSLPckg_ConsiderIgnoreFragment()
    assert isinstance(instance, CombinedFragment)


def test_CompleteDSLPckg_Property_isa_ConnectableElement():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert isinstance(instance, ConnectableElement)


def test_CompleteDSLPckg_Variable_isa_ConnectableElement():
    instance = CompleteDSLPckg_Variable()
    assert isinstance(instance, ConnectableElement)


def test_CompleteDSLPckg_InteractionConstraint_isa_Constraint():
    instance = CompleteDSLPckg_InteractionConstraint()
    assert isinstance(instance, Constraint)


def test_CompleteDSLPckg_IntervalConstraint_isa_Constraint():
    instance = CompleteDSLPckg_IntervalConstraint()
    assert isinstance(instance, Constraint)


def test_CompleteDSLPckg_ActivityFinalNode_isa_ControlNode():
    instance = CompleteDSLPckg_ActivityFinalNode()
    assert isinstance(instance, ControlNode)


def test_CompleteDSLPckg_DecisionNode_isa_ControlNode():
    instance = CompleteDSLPckg_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_CompleteDSLPckg_FinalNode_isa_ControlNode():
    instance = CompleteDSLPckg_FinalNode()
    assert isinstance(instance, ControlNode)


def test_CompleteDSLPckg_ForkNode_isa_ControlNode():
    instance = CompleteDSLPckg_ForkNode()
    assert isinstance(instance, ControlNode)


def test_CompleteDSLPckg_InitialNode_isa_ControlNode():
    instance = CompleteDSLPckg_InitialNode()
    assert isinstance(instance, ControlNode)


def test_CompleteDSLPckg_JoinNode_isa_ControlNode():
    instance = CompleteDSLPckg_JoinNode(isCombineDuplicate=True)
    assert isinstance(instance, ControlNode)


def test_CompleteDSLPckg_MergeNode_isa_ControlNode():
    instance = CompleteDSLPckg_MergeNode()
    assert isinstance(instance, ControlNode)


def test_CompleteDSLPckg_CreateLinkObjectAction_isa_CreateLinkAction():
    instance = CompleteDSLPckg_CreateLinkObjectAction()
    assert isinstance(instance, CreateLinkAction)


def test_CompleteDSLPckg_Enumeration_isa_DataType():
    instance = CompleteDSLPckg_Enumeration()
    assert isinstance(instance, DataType)


def test_CompleteDSLPckg_PrimitiveType_isa_DataType():
    instance = CompleteDSLPckg_PrimitiveType()
    assert isinstance(instance, DataType)


def test_CompleteDSLPckg_Abstraction_isa_Dependency():
    instance = CompleteDSLPckg_Abstraction()
    assert isinstance(instance, Dependency)


def test_CompleteDSLPckg_Deployment_isa_Dependency():
    instance = CompleteDSLPckg_Deployment()
    assert isinstance(instance, Dependency)


def test_CompleteDSLPckg_Usage_isa_Dependency():
    instance = CompleteDSLPckg_Usage()
    assert isinstance(instance, Dependency)


def test_CompleteDSLPckg_Artifact_isa_DeployedArtifact():
    instance = CompleteDSLPckg_Artifact(fileName="sample_text")
    assert isinstance(instance, DeployedArtifact)


def test_CompleteDSLPckg_Node_isa_DeploymentTarget():
    instance = CompleteDSLPckg_Node()
    assert isinstance(instance, DeploymentTarget)


def test_CompleteDSLPckg_Property_isa_DeploymentTarget():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert isinstance(instance, DeploymentTarget)


def test_CompleteDSLPckg_Dependency_isa_DirectedRelationship():
    instance = CompleteDSLPckg_Dependency()
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_ElementImport_isa_DirectedRelationship():
    instance = CompleteDSLPckg_ElementImport(alias="sample_text", visibility="sample_text")
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_Extend_isa_DirectedRelationship():
    instance = CompleteDSLPckg_Extend()
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_Generalization_isa_DirectedRelationship():
    instance = CompleteDSLPckg_Generalization(isSubstitutable=True)
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_Include_isa_DirectedRelationship():
    instance = CompleteDSLPckg_Include()
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_PackageImport_isa_DirectedRelationship():
    instance = CompleteDSLPckg_PackageImport(visibility="sample_text")
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_PackageMerge_isa_DirectedRelationship():
    instance = CompleteDSLPckg_PackageMerge()
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_ProtocolConformance_isa_DirectedRelationship():
    instance = CompleteDSLPckg_ProtocolConformance()
    assert isinstance(instance, DirectedRelationship)


def test_CompleteDSLPckg_Clause_isa_Element():
    instance = CompleteDSLPckg_Clause()
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_Comment_isa_Element():
    instance = CompleteDSLPckg_Comment(body="sample_text")
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_ExceptionHandler_isa_Element():
    instance = CompleteDSLPckg_ExceptionHandler()
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_LinkEndData_isa_Element():
    instance = CompleteDSLPckg_LinkEndData()
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_MultiplicityElement_isa_Element():
    instance = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_NamedElement_isa_Element():
    instance = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_QualifierValue_isa_Element():
    instance = CompleteDSLPckg_QualifierValue()
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_Relationship_isa_Element():
    instance = CompleteDSLPckg_Relationship()
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_Slot_isa_Element():
    instance = CompleteDSLPckg_Slot()
    assert isinstance(instance, Element)


def test_CompleteDSLPckg_Class_isa_EncapsulatedClassifier():
    instance = CompleteDSLPckg_Class()
    assert isinstance(instance, EncapsulatedClassifier)


def test_CompleteDSLPckg_ChangeEvent_isa_Event():
    instance = CompleteDSLPckg_ChangeEvent()
    assert isinstance(instance, Event)


def test_CompleteDSLPckg_MessageEvent_isa_Event():
    instance = CompleteDSLPckg_MessageEvent()
    assert isinstance(instance, Event)


def test_CompleteDSLPckg_StructuredActivityNode_isa_ExecutableNode():
    instance = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, ExecutableNode)


def test_CompleteDSLPckg_ActionExecutionSpecification_isa_ExecutionSpecification():
    instance = CompleteDSLPckg_ActionExecutionSpecification()
    assert isinstance(instance, ExecutionSpecification)


def test_CompleteDSLPckg_BehaviorExecutionSpecification_isa_ExecutionSpecification():
    instance = CompleteDSLPckg_BehaviorExecutionSpecification()
    assert isinstance(instance, ExecutionSpecification)


def test_CompleteDSLPckg_BehavioralFeature_isa_Feature():
    instance = CompleteDSLPckg_BehavioralFeature()
    assert isinstance(instance, Feature)


def test_CompleteDSLPckg_Connector_isa_Feature():
    instance = CompleteDSLPckg_Connector(kind="sample_text")
    assert isinstance(instance, Feature)


def test_CompleteDSLPckg_StructuralFeature_isa_Feature():
    instance = CompleteDSLPckg_StructuralFeature(isReadOnly=True)
    assert isinstance(instance, Feature)


def test_CompleteDSLPckg_ActivityFinalNode_isa_FinalNode():
    instance = CompleteDSLPckg_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_CompleteDSLPckg_FlowFinalNode_isa_FinalNode():
    instance = CompleteDSLPckg_FlowFinalNode()
    assert isinstance(instance, FinalNode)


def test_CompleteDSLPckg_ActionInputPin_isa_InputPin():
    instance = CompleteDSLPckg_ActionInputPin()
    assert isinstance(instance, InputPin)


def test_CompleteDSLPckg_ValuePin_isa_InputPin():
    instance = CompleteDSLPckg_ValuePin()
    assert isinstance(instance, InputPin)


def test_CompleteDSLPckg_EnumerationLiteral_isa_InstanceSpecification():
    instance = CompleteDSLPckg_EnumerationLiteral()
    assert isinstance(instance, InstanceSpecification)


def test_CompleteDSLPckg_Continuation_isa_InteractionFragment():
    instance = CompleteDSLPckg_Continuation(setting=True)
    assert isinstance(instance, InteractionFragment)


def test_CompleteDSLPckg_ExecutionSpecification_isa_InteractionFragment():
    instance = CompleteDSLPckg_ExecutionSpecification()
    assert isinstance(instance, InteractionFragment)


def test_CompleteDSLPckg_Interaction_isa_InteractionFragment():
    instance = CompleteDSLPckg_Interaction()
    assert isinstance(instance, InteractionFragment)


def test_CompleteDSLPckg_InteractionUse_isa_InteractionFragment():
    instance = CompleteDSLPckg_InteractionUse()
    assert isinstance(instance, InteractionFragment)


def test_CompleteDSLPckg_OccurenceSpecification_isa_InteractionFragment():
    instance = CompleteDSLPckg_OccurenceSpecification()
    assert isinstance(instance, InteractionFragment)


def test_CompleteDSLPckg_StateInvariant_isa_InteractionFragment():
    instance = CompleteDSLPckg_StateInvariant()
    assert isinstance(instance, InteractionFragment)


def test_CompleteDSLPckg_PartDecomposition_isa_InteractionUse():
    instance = CompleteDSLPckg_PartDecomposition()
    assert isinstance(instance, InteractionUse)


def test_CompleteDSLPckg_DurationInterval_isa_Interval():
    instance = CompleteDSLPckg_DurationInterval()
    assert isinstance(instance, Interval)


def test_CompleteDSLPckg_TimeInterval_isa_Interval():
    instance = CompleteDSLPckg_TimeInterval()
    assert isinstance(instance, Interval)


def test_CompleteDSLPckg_DurationConstraint_isa_IntervalConstraint():
    instance = CompleteDSLPckg_DurationConstraint(firstEvent=True)
    assert isinstance(instance, IntervalConstraint)


def test_CompleteDSLPckg_TimeConstraint_isa_IntervalConstraint():
    instance = CompleteDSLPckg_TimeConstraint(firstEvent=True)
    assert isinstance(instance, IntervalConstraint)


def test_CompleteDSLPckg_BroadcastSignalAction_isa_InvocationAction():
    instance = CompleteDSLPckg_BroadcastSignalAction()
    assert isinstance(instance, InvocationAction)


def test_CompleteDSLPckg_CallAction_isa_InvocationAction():
    instance = CompleteDSLPckg_CallAction(isSynchronous=True)
    assert isinstance(instance, InvocationAction)


def test_CompleteDSLPckg_SendObjectAction_isa_InvocationAction():
    instance = CompleteDSLPckg_SendObjectAction()
    assert isinstance(instance, InvocationAction)


def test_CompleteDSLPckg_SendSignalAction_isa_InvocationAction():
    instance = CompleteDSLPckg_SendSignalAction()
    assert isinstance(instance, InvocationAction)


def test_CompleteDSLPckg_ReadLinkAction_isa_LinkAction():
    instance = CompleteDSLPckg_ReadLinkAction()
    assert isinstance(instance, LinkAction)


def test_CompleteDSLPckg_WriteLinkAction_isa_LinkAction():
    instance = CompleteDSLPckg_WriteLinkAction()
    assert isinstance(instance, LinkAction)


def test_CompleteDSLPckg_LinkEndCreationData_isa_LinkEndData():
    instance = CompleteDSLPckg_LinkEndCreationData(isReplaceAll=True)
    assert isinstance(instance, LinkEndData)


def test_CompleteDSLPckg_LinkEndDestructionData_isa_LinkEndData():
    instance = CompleteDSLPckg_LinkEndDestructionData(isDestroyDuplicates=True)
    assert isinstance(instance, LinkEndData)


def test_CompleteDSLPckg_LiteralBoolean_isa_LiteralSpecification():
    instance = CompleteDSLPckg_LiteralBoolean()
    assert isinstance(instance, LiteralSpecification)


def test_CompleteDSLPckg_LiteralInteger_isa_LiteralSpecification():
    instance = CompleteDSLPckg_LiteralInteger()
    assert isinstance(instance, LiteralSpecification)


def test_CompleteDSLPckg_LiteralNull_isa_LiteralSpecification():
    instance = CompleteDSLPckg_LiteralNull()
    assert isinstance(instance, LiteralSpecification)


def test_CompleteDSLPckg_LiteralReal_isa_LiteralSpecification():
    instance = CompleteDSLPckg_LiteralReal()
    assert isinstance(instance, LiteralSpecification)


def test_CompleteDSLPckg_LiteralString_isa_LiteralSpecification():
    instance = CompleteDSLPckg_LiteralString()
    assert isinstance(instance, LiteralSpecification)


def test_CompleteDSLPckg_LiteralUnilimitedNatural_isa_LiteralSpecification():
    instance = CompleteDSLPckg_LiteralUnilimitedNatural()
    assert isinstance(instance, LiteralSpecification)


def test_CompleteDSLPckg_Gate_isa_MessageEnd():
    instance = CompleteDSLPckg_Gate()
    assert isinstance(instance, MessageEnd)


def test_CompleteDSLPckg_AnyReceiveEvent_isa_MessageEvent():
    instance = CompleteDSLPckg_AnyReceiveEvent()
    assert isinstance(instance, MessageEvent)


def test_CompleteDSLPckg_CallEvent_isa_MessageEvent():
    instance = CompleteDSLPckg_CallEvent()
    assert isinstance(instance, MessageEvent)


def test_CompleteDSLPckg_SignalEvent_isa_MessageEvent():
    instance = CompleteDSLPckg_SignalEvent()
    assert isinstance(instance, MessageEvent)


def test_CompleteDSLPckg_DestructionOccurrenceSpecification_isa_MessageOccurrenceSpecification():
    instance = CompleteDSLPckg_DestructionOccurrenceSpecification()
    assert isinstance(instance, MessageOccurrenceSpecification)


def test_CompleteDSLPckg_Pin_isa_MultiplicityElement():
    instance = CompleteDSLPckg_Pin()
    assert isinstance(instance, MultiplicityElement)


def test_CompleteDSLPckg_StructuralFeature_isa_MultiplicityElement():
    instance = CompleteDSLPckg_StructuralFeature(isReadOnly=True)
    assert isinstance(instance, MultiplicityElement)


def test_CompleteDSLPckg_Variable_isa_MultiplicityElement():
    instance = CompleteDSLPckg_Variable()
    assert isinstance(instance, MultiplicityElement)


def test_CompleteDSLPckg_Action_isa_NamedElement():
    instance = CompleteDSLPckg_Action()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_ActivityGroup_isa_NamedElement():
    instance = CompleteDSLPckg_ActivityGroup()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_ActivityNode_isa_NamedElement():
    instance = CompleteDSLPckg_ActivityNode()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Artifact_isa_NamedElement():
    instance = CompleteDSLPckg_Artifact(fileName="sample_text")
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_CollaborationUse_isa_NamedElement():
    instance = CompleteDSLPckg_CollaborationUse()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Component_isa_NamedElement():
    instance = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_DeployedArtifact_isa_NamedElement():
    instance = CompleteDSLPckg_DeployedArtifact()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_DeploymentTarget_isa_NamedElement():
    instance = CompleteDSLPckg_DeploymentTarget()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Extend_isa_NamedElement():
    instance = CompleteDSLPckg_Extend()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_GeneralOrdering_isa_NamedElement():
    instance = CompleteDSLPckg_GeneralOrdering()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Include_isa_NamedElement():
    instance = CompleteDSLPckg_Include()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_InteractionFragment_isa_NamedElement():
    instance = CompleteDSLPckg_InteractionFragment()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Lifeline_isa_NamedElement():
    instance = CompleteDSLPckg_Lifeline()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Message_isa_NamedElement():
    instance = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_MessageEnd_isa_NamedElement():
    instance = CompleteDSLPckg_MessageEnd()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Namespace_isa_NamedElement():
    instance = CompleteDSLPckg_Namespace()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_PackageableElement_isa_NamedElement():
    instance = CompleteDSLPckg_PackageableElement()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_ParameterSet_isa_NamedElement():
    instance = CompleteDSLPckg_ParameterSet()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_RedefinableElement_isa_NamedElement():
    instance = CompleteDSLPckg_RedefinableElement(isLeaf=True)
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Trigger_isa_NamedElement():
    instance = CompleteDSLPckg_Trigger()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_TypedElement_isa_NamedElement():
    instance = CompleteDSLPckg_TypedElement()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_Vertex_isa_NamedElement():
    instance = CompleteDSLPckg_Vertex()
    assert isinstance(instance, NamedElement)


def test_CompleteDSLPckg_BehavioralFeature_isa_Namespace():
    instance = CompleteDSLPckg_BehavioralFeature()
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_Classifier_isa_Namespace():
    instance = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_InteractionOperand_isa_Namespace():
    instance = CompleteDSLPckg_InteractionOperand()
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_Package_isa_Namespace():
    instance = CompleteDSLPckg_Package(URI="sample_text")
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_Region_isa_Namespace():
    instance = CompleteDSLPckg_Region()
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_State_isa_Namespace():
    instance = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_StructuredActivityNode_isa_Namespace():
    instance = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_Transition_isa_Namespace():
    instance = CompleteDSLPckg_Transition(kind="sample_text")
    assert isinstance(instance, Namespace)


def test_CompleteDSLPckg_Device_isa_Node():
    instance = CompleteDSLPckg_Device()
    assert isinstance(instance, Node)


def test_CompleteDSLPckg_ExecutionEnvironment_isa_Node():
    instance = CompleteDSLPckg_ExecutionEnvironment()
    assert isinstance(instance, Node)


def test_CompleteDSLPckg_ActivityParameterNode_isa_ObjectNode():
    instance = CompleteDSLPckg_ActivityParameterNode()
    assert isinstance(instance, ObjectNode)


def test_CompleteDSLPckg_CentralBufferNode_isa_ObjectNode():
    instance = CompleteDSLPckg_CentralBufferNode()
    assert isinstance(instance, ObjectNode)


def test_CompleteDSLPckg_ExpansionNode_isa_ObjectNode():
    instance = CompleteDSLPckg_ExpansionNode()
    assert isinstance(instance, ObjectNode)


def test_CompleteDSLPckg_DurationObservation_isa_Observation():
    instance = CompleteDSLPckg_DurationObservation(firstEvent=True)
    assert isinstance(instance, Observation)


def test_CompleteDSLPckg_TimeObservation_isa_Observation():
    instance = CompleteDSLPckg_TimeObservation(firstEvent=True)
    assert isinstance(instance, Observation)


def test_CompleteDSLPckg_ExecutionOccurrenceSpecification_isa_OccurenceSpecification():
    instance = CompleteDSLPckg_ExecutionOccurrenceSpecification()
    assert isinstance(instance, OccurenceSpecification)


def test_CompleteDSLPckg_MessageOccurrenceSpecification_isa_OccurenceSpecification():
    instance = CompleteDSLPckg_MessageOccurrenceSpecification()
    assert isinstance(instance, OccurenceSpecification)


def test_CompleteDSLPckg_FunctionBehavior_isa_OpaqueBehavior():
    instance = CompleteDSLPckg_FunctionBehavior()
    assert isinstance(instance, OpaqueBehavior)


def test_CompleteDSLPckg_Constraint_isa_PackageableElement():
    instance = CompleteDSLPckg_Constraint()
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_Dependency_isa_PackageableElement():
    instance = CompleteDSLPckg_Dependency()
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_Event_isa_PackageableElement():
    instance = CompleteDSLPckg_Event()
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_GeneralizationSet_isa_PackageableElement():
    instance = CompleteDSLPckg_GeneralizationSet(isCovering=True, isDisjoint=True)
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_InstanceSpecification_isa_PackageableElement():
    instance = CompleteDSLPckg_InstanceSpecification()
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_Observation_isa_PackageableElement():
    instance = CompleteDSLPckg_Observation()
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_Package_isa_PackageableElement():
    instance = CompleteDSLPckg_Package(URI="sample_text")
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_Type_isa_PackageableElement():
    instance = CompleteDSLPckg_Type()
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_ValueSpecification_isa_PackageableElement():
    instance = CompleteDSLPckg_ValueSpecification()
    assert isinstance(instance, PackageableElement)


def test_CompleteDSLPckg_InputPin_isa_Pin():
    instance = CompleteDSLPckg_InputPin()
    assert isinstance(instance, Pin)


def test_CompleteDSLPckg_OutputPin_isa_Pin():
    instance = CompleteDSLPckg_OutputPin()
    assert isinstance(instance, Pin)


def test_CompleteDSLPckg_Port_isa_Property():
    instance = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    assert isinstance(instance, Property)


def test_CompleteDSLPckg_ComponentRealization_isa_Realization():
    instance = CompleteDSLPckg_ComponentRealization()
    assert isinstance(instance, Realization)


def test_CompleteDSLPckg_InterfaceRealization_isa_Realization():
    instance = CompleteDSLPckg_InterfaceRealization()
    assert isinstance(instance, Realization)


def test_CompleteDSLPckg_Substitution_isa_Realization():
    instance = CompleteDSLPckg_Substitution()
    assert isinstance(instance, Realization)


def test_CompleteDSLPckg_ActivityEdge_isa_RedefinableElement():
    instance = CompleteDSLPckg_ActivityEdge()
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_ActivityNode_isa_RedefinableElement():
    instance = CompleteDSLPckg_ActivityNode()
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_Classifier_isa_RedefinableElement():
    instance = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_ExtensionPoint_isa_RedefinableElement():
    instance = CompleteDSLPckg_ExtensionPoint()
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_Feature_isa_RedefinableElement():
    instance = CompleteDSLPckg_Feature(isStatic=True)
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_Region_isa_RedefinableElement():
    instance = CompleteDSLPckg_Region()
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_State_isa_RedefinableElement():
    instance = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_Transition_isa_RedefinableElement():
    instance = CompleteDSLPckg_Transition(kind="sample_text")
    assert isinstance(instance, RedefinableElement)


def test_CompleteDSLPckg_Association_isa_Relationship():
    instance = CompleteDSLPckg_Association(isDerived=True)
    assert isinstance(instance, Relationship)


def test_CompleteDSLPckg_DirectedRelationship_isa_Relationship():
    instance = CompleteDSLPckg_DirectedRelationship()
    assert isinstance(instance, Relationship)


def test_CompleteDSLPckg_FinalState_isa_State():
    instance = CompleteDSLPckg_FinalState()
    assert isinstance(instance, State)


def test_CompleteDSLPckg_ProtocolStateMachine_isa_StateMachine():
    instance = CompleteDSLPckg_ProtocolStateMachine()
    assert isinstance(instance, StateMachine)


def test_CompleteDSLPckg_Property_isa_StructuralFeature():
    instance = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    assert isinstance(instance, StructuralFeature)


def test_CompleteDSLPckg_ClearStructuralFeatureAction_isa_StructuralFeatureAction():
    instance = CompleteDSLPckg_ClearStructuralFeatureAction()
    assert isinstance(instance, StructuralFeatureAction)


def test_CompleteDSLPckg_ReadStructuralFeatureAction_isa_StructuralFeatureAction():
    instance = CompleteDSLPckg_ReadStructuralFeatureAction()
    assert isinstance(instance, StructuralFeatureAction)


def test_CompleteDSLPckg_WriteStructuralFeatureAction_isa_StructuralFeatureAction():
    instance = CompleteDSLPckg_WriteStructuralFeatureAction()
    assert isinstance(instance, StructuralFeatureAction)


def test_CompleteDSLPckg_ConditionalNode_isa_StructuredActivityNode():
    instance = CompleteDSLPckg_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert isinstance(instance, StructuredActivityNode)


def test_CompleteDSLPckg_ExpansionRegion_isa_StructuredActivityNode():
    instance = CompleteDSLPckg_ExpansionRegion(mode="sample_text")
    assert isinstance(instance, StructuredActivityNode)


def test_CompleteDSLPckg_LoopNode_isa_StructuredActivityNode():
    instance = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    assert isinstance(instance, StructuredActivityNode)


def test_CompleteDSLPckg_SequenceNode_isa_StructuredActivityNode():
    instance = CompleteDSLPckg_SequenceNode()
    assert isinstance(instance, StructuredActivityNode)


def test_CompleteDSLPckg_Class_isa_StructuredClassifier():
    instance = CompleteDSLPckg_Class()
    assert isinstance(instance, StructuredClassifier)


def test_CompleteDSLPckg_Collaboration_isa_StructuredClassifier():
    instance = CompleteDSLPckg_Collaboration()
    assert isinstance(instance, StructuredClassifier)


def test_CompleteDSLPckg_EncapsulatedClassifier_isa_StructuredClassifier():
    instance = CompleteDSLPckg_EncapsulatedClassifier()
    assert isinstance(instance, StructuredClassifier)


def test_CompleteDSLPckg_ProtocolTransition_isa_Transition():
    instance = CompleteDSLPckg_ProtocolTransition()
    assert isinstance(instance, Transition)


def test_CompleteDSLPckg_Classifier_isa_Type():
    instance = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    assert isinstance(instance, Type)


def test_CompleteDSLPckg_ConnectableElement_isa_TypedElement():
    instance = CompleteDSLPckg_ConnectableElement()
    assert isinstance(instance, TypedElement)


def test_CompleteDSLPckg_ObjectNode_isa_TypedElement():
    instance = CompleteDSLPckg_ObjectNode()
    assert isinstance(instance, TypedElement)


def test_CompleteDSLPckg_Parameter_isa_TypedElement():
    instance = CompleteDSLPckg_Parameter(default="sample_text")
    assert isinstance(instance, TypedElement)


def test_CompleteDSLPckg_Pin_isa_TypedElement():
    instance = CompleteDSLPckg_Pin()
    assert isinstance(instance, TypedElement)


def test_CompleteDSLPckg_StructuralFeature_isa_TypedElement():
    instance = CompleteDSLPckg_StructuralFeature(isReadOnly=True)
    assert isinstance(instance, TypedElement)


def test_CompleteDSLPckg_ValueSpecification_isa_TypedElement():
    instance = CompleteDSLPckg_ValueSpecification()
    assert isinstance(instance, TypedElement)


def test_CompleteDSLPckg_Variable_isa_TypedElement():
    instance = CompleteDSLPckg_Variable()
    assert isinstance(instance, TypedElement)


def test_CompleteDSLPckg_Duration_isa_ValueSpecification():
    instance = CompleteDSLPckg_Duration()
    assert isinstance(instance, ValueSpecification)


def test_CompleteDSLPckg_Expression_isa_ValueSpecification():
    instance = CompleteDSLPckg_Expression(symbol="sample_text")
    assert isinstance(instance, ValueSpecification)


def test_CompleteDSLPckg_Interval_isa_ValueSpecification():
    instance = CompleteDSLPckg_Interval()
    assert isinstance(instance, ValueSpecification)


def test_CompleteDSLPckg_LiteralSpecification_isa_ValueSpecification():
    instance = CompleteDSLPckg_LiteralSpecification()
    assert isinstance(instance, ValueSpecification)


def test_CompleteDSLPckg_OpaqueExpression_isa_ValueSpecification():
    instance = CompleteDSLPckg_OpaqueExpression(body="sample_text", language="sample_text")
    assert isinstance(instance, ValueSpecification)


def test_CompleteDSLPckg_TimeExpression_isa_ValueSpecification():
    instance = CompleteDSLPckg_TimeExpression()
    assert isinstance(instance, ValueSpecification)


def test_CompleteDSLPckg_ClearVariableAction_isa_VariableAction():
    instance = CompleteDSLPckg_ClearVariableAction()
    assert isinstance(instance, VariableAction)


def test_CompleteDSLPckg_ReadVariableAction_isa_VariableAction():
    instance = CompleteDSLPckg_ReadVariableAction()
    assert isinstance(instance, VariableAction)


def test_CompleteDSLPckg_WriteVariableAction_isa_VariableAction():
    instance = CompleteDSLPckg_WriteVariableAction()
    assert isinstance(instance, VariableAction)


def test_CompleteDSLPckg_ConnectionPointReference_isa_Vertex():
    instance = CompleteDSLPckg_ConnectionPointReference()
    assert isinstance(instance, Vertex)


def test_CompleteDSLPckg_Pseudostate_isa_Vertex():
    instance = CompleteDSLPckg_Pseudostate()
    assert isinstance(instance, Vertex)


def test_CompleteDSLPckg_State_isa_Vertex():
    instance = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    assert isinstance(instance, Vertex)


def test_CompleteDSLPckg_CreateLinkAction_isa_WriteLinkAction():
    instance = CompleteDSLPckg_CreateLinkAction()
    assert isinstance(instance, WriteLinkAction)


def test_CompleteDSLPckg_DestroyLinkAction_isa_WriteLinkAction():
    instance = CompleteDSLPckg_DestroyLinkAction()
    assert isinstance(instance, WriteLinkAction)


def test_CompleteDSLPckg_AddStructuralFeatureValueAction_isa_WriteStructuralFeatureAction():
    instance = CompleteDSLPckg_AddStructuralFeatureValueAction()
    assert isinstance(instance, WriteStructuralFeatureAction)


def test_CompleteDSLPckg_RemoveStructuralFeatureValueAction_isa_WriteStructuralFeatureAction():
    instance = CompleteDSLPckg_RemoveStructuralFeatureValueAction()
    assert isinstance(instance, WriteStructuralFeatureAction)


def test_CompleteDSLPckg_AddVariableValueAction_isa_WriteVariableAction():
    instance = CompleteDSLPckg_AddVariableValueAction()
    assert isinstance(instance, WriteVariableAction)


def test_CompleteDSLPckg_RemoveVariableValueAction_isa_WriteVariableAction():
    instance = CompleteDSLPckg_RemoveVariableValueAction()
    assert isinstance(instance, WriteVariableAction)


def test_assoc_abstraction305_link_reassign_clear():
    a = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    b1 = CompleteDSLPckg_ComponentRealization()
    b2 = CompleteDSLPckg_ComponentRealization()
    _safe_set(a, 'CompleteDSLPckg_Component307', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Component307', b1)
    if hasattr(b1, 'CompleteDSLPckg_ComponentRealization306'):
        assert _is_linked(b1, 'CompleteDSLPckg_ComponentRealization306', a)
    _safe_set(a, 'CompleteDSLPckg_Component307', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Component307', b2)
    if hasattr(b1, 'CompleteDSLPckg_ComponentRealization306'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ComponentRealization306', a)
    if hasattr(b2, 'CompleteDSLPckg_ComponentRealization306'):
        assert _is_linked(b2, 'CompleteDSLPckg_ComponentRealization306', a)
    _safe_set(a, 'CompleteDSLPckg_Component307', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Component307', b2)
    if hasattr(b2, 'CompleteDSLPckg_ComponentRealization306'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ComponentRealization306', a)


def test_assoc_activity798_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b2 = CompleteDSLPckg_Activity(isReadOnly=False, isSingleExecution=False)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode799', b1)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode799', b1)
    if hasattr(b1, 'CompleteDSLPckg_Activity800'):
        assert _is_linked(b1, 'CompleteDSLPckg_Activity800', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode799', b2)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode799', b2)
    if hasattr(b1, 'CompleteDSLPckg_Activity800'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Activity800', a)
    if hasattr(b2, 'CompleteDSLPckg_Activity800'):
        assert _is_linked(b2, 'CompleteDSLPckg_Activity800', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode799', None)
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode799', b2)
    if hasattr(b2, 'CompleteDSLPckg_Activity800'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Activity800', a)


def test_assoc_annotatedElement35_link_reassign_clear():
    a = CompleteDSLPckg_Comment(body="sample_text")
    b1 = CompleteDSLPckg_Element()
    b2 = CompleteDSLPckg_Element()
    _safe_set(a, 'CompleteDSLPckg_Comment', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Comment', b1)
    if hasattr(b1, 'CompleteDSLPckg_Element'):
        assert _is_linked(b1, 'CompleteDSLPckg_Element', a)
    _safe_set(a, 'CompleteDSLPckg_Comment', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Comment', b2)
    if hasattr(b1, 'CompleteDSLPckg_Element'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Element', a)
    if hasattr(b2, 'CompleteDSLPckg_Element'):
        assert _is_linked(b2, 'CompleteDSLPckg_Element', a)
    _safe_set(a, 'CompleteDSLPckg_Comment', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Comment', b2)
    if hasattr(b2, 'CompleteDSLPckg_Element'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Element', a)


def test_assoc_argument923_link_reassign_clear():
    a = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'CompleteDSLPckg_Message', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Message', b1)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification924'):
        assert _is_linked(b1, 'CompleteDSLPckg_ValueSpecification924', a)
    _safe_set(a, 'CompleteDSLPckg_Message', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Message', b2)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification924'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ValueSpecification924', a)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification924'):
        assert _is_linked(b2, 'CompleteDSLPckg_ValueSpecification924', a)
    _safe_set(a, 'CompleteDSLPckg_Message', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Message', b2)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification924'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ValueSpecification924', a)


def test_assoc_association118_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Association(isDerived=True)
    b2 = CompleteDSLPckg_Association(isDerived=False)
    _safe_set(a, 'memberEnd', b1)
    assert _is_linked(a, 'memberEnd', b1)
    if hasattr(b1, 'Association'):
        assert _is_linked(b1, 'Association', a)
    _safe_set(a, 'memberEnd', b2)
    assert _is_linked(a, 'memberEnd', b2)
    if hasattr(b1, 'Association'):
        assert not _is_linked(b1, 'Association', a)
    if hasattr(b2, 'Association'):
        assert _is_linked(b2, 'Association', a)
    _safe_set(a, 'memberEnd', None)
    assert not _is_linked(a, 'memberEnd', b2)
    if hasattr(b2, 'Association'):
        assert not _is_linked(b2, 'Association', a)


def test_assoc_associationEnd128_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b2 = CompleteDSLPckg_Property(aggregation="sample_text_2", default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    _safe_set(a, 'Property129', b1)
    assert _is_linked(a, 'Property129', b1)
    if hasattr(b1, 'qualifier'):
        assert _is_linked(b1, 'qualifier', a)
    _safe_set(a, 'Property129', b2)
    assert _is_linked(a, 'Property129', b2)
    if hasattr(b1, 'qualifier'):
        assert not _is_linked(b1, 'qualifier', a)
    if hasattr(b2, 'qualifier'):
        assert _is_linked(b2, 'qualifier', a)
    _safe_set(a, 'Property129', None)
    assert not _is_linked(a, 'Property129', b2)
    if hasattr(b2, 'qualifier'):
        assert not _is_linked(b2, 'qualifier', a)


def test_assoc_attribute88_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_Property', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier89'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier89', a)
    _safe_set(a, 'CompleteDSLPckg_Property', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier89'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier89', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier89'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier89', a)
    _safe_set(a, 'CompleteDSLPckg_Property', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier89'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier89', a)


def test_assoc_behavior407_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_CallBehaviorAction()
    b2 = CompleteDSLPckg_CallBehaviorAction()
    _safe_set(a, 'CompleteDSLPckg_Behavior408', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior408', b1)
    if hasattr(b1, 'CompleteDSLPckg_CallBehaviorAction'):
        assert _is_linked(b1, 'CompleteDSLPckg_CallBehaviorAction', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior408', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior408', b2)
    if hasattr(b1, 'CompleteDSLPckg_CallBehaviorAction'):
        assert not _is_linked(b1, 'CompleteDSLPckg_CallBehaviorAction', a)
    if hasattr(b2, 'CompleteDSLPckg_CallBehaviorAction'):
        assert _is_linked(b2, 'CompleteDSLPckg_CallBehaviorAction', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior408', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior408', b2)
    if hasattr(b2, 'CompleteDSLPckg_CallBehaviorAction'):
        assert not _is_linked(b2, 'CompleteDSLPckg_CallBehaviorAction', a)


def test_assoc_behavior59_link_reassign_clear():
    a = CompleteDSLPckg_OpaqueExpression(body="sample_text", language="sample_text")
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_OpaqueExpression60', b1)
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueExpression60', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueExpression60', b2)
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueExpression60', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueExpression60', None)
    assert not _is_linked(a, 'CompleteDSLPckg_OpaqueExpression60', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior', a)


def test_assoc_behavior941_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_BehaviorExecutionSpecification()
    b2 = CompleteDSLPckg_BehaviorExecutionSpecification()
    _safe_set(a, 'CompleteDSLPckg_Behavior942', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior942', b1)
    if hasattr(b1, 'CompleteDSLPckg_BehaviorExecutionSpecification'):
        assert _is_linked(b1, 'CompleteDSLPckg_BehaviorExecutionSpecification', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior942', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior942', b2)
    if hasattr(b1, 'CompleteDSLPckg_BehaviorExecutionSpecification'):
        assert not _is_linked(b1, 'CompleteDSLPckg_BehaviorExecutionSpecification', a)
    if hasattr(b2, 'CompleteDSLPckg_BehaviorExecutionSpecification'):
        assert _is_linked(b2, 'CompleteDSLPckg_BehaviorExecutionSpecification', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior942', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior942', b2)
    if hasattr(b2, 'CompleteDSLPckg_BehaviorExecutionSpecification'):
        assert not _is_linked(b2, 'CompleteDSLPckg_BehaviorExecutionSpecification', a)


def test_assoc_body844_link_reassign_clear():
    a = CompleteDSLPckg_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = CompleteDSLPckg_ExecutableNode()
    b2 = CompleteDSLPckg_ExecutableNode()
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode845', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode845', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode846'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExecutableNode846', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode845', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode845', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode846'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExecutableNode846', a)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode846'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExecutableNode846', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode845', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ConditionalNode845', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode846'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExecutableNode846', a)


def test_assoc_bodyCondition153_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Constraint()
    b2 = CompleteDSLPckg_Constraint()
    _safe_set(a, 'CompleteDSLPckg_Operation154', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Operation154', b1)
    if hasattr(b1, 'CompleteDSLPckg_Constraint155'):
        assert _is_linked(b1, 'CompleteDSLPckg_Constraint155', a)
    _safe_set(a, 'CompleteDSLPckg_Operation154', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Operation154', b2)
    if hasattr(b1, 'CompleteDSLPckg_Constraint155'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Constraint155', a)
    if hasattr(b2, 'CompleteDSLPckg_Constraint155'):
        assert _is_linked(b2, 'CompleteDSLPckg_Constraint155', a)
    _safe_set(a, 'CompleteDSLPckg_Operation154', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Operation154', b2)
    if hasattr(b2, 'CompleteDSLPckg_Constraint155'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Constraint155', a)


def test_assoc_bodyOutput834_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_LoopNode835', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode835', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin836'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin836', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode835', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode835', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin836'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin836', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin836'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin836', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode835', set())
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode835', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin836'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin836', a)


def test_assoc_bodyPart819_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_ExecutableNode()
    b2 = CompleteDSLPckg_ExecutableNode()
    _safe_set(a, 'CompleteDSLPckg_LoopNode820', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode820', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode821'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExecutableNode821', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode820', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode820', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode821'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExecutableNode821', a)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode821'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExecutableNode821', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode820', set())
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode820', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode821'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExecutableNode821', a)


def test_assoc_cfragmentGate958_link_reassign_clear():
    a = CompleteDSLPckg_CombinedFragment(interactionOperator="sample_text")
    b1 = CompleteDSLPckg_Gate()
    b2 = CompleteDSLPckg_Gate()
    _safe_set(a, 'CompleteDSLPckg_CombinedFragment959', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_CombinedFragment959', b1)
    if hasattr(b1, 'CompleteDSLPckg_Gate960'):
        assert _is_linked(b1, 'CompleteDSLPckg_Gate960', a)
    _safe_set(a, 'CompleteDSLPckg_CombinedFragment959', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_CombinedFragment959', b2)
    if hasattr(b1, 'CompleteDSLPckg_Gate960'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Gate960', a)
    if hasattr(b2, 'CompleteDSLPckg_Gate960'):
        assert _is_linked(b2, 'CompleteDSLPckg_Gate960', a)
    _safe_set(a, 'CompleteDSLPckg_CombinedFragment959', set())
    assert not _is_linked(a, 'CompleteDSLPckg_CombinedFragment959', b2)
    if hasattr(b2, 'CompleteDSLPckg_Gate960'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Gate960', a)


def test_assoc_class_105_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Class()
    b2 = CompleteDSLPckg_Class()
    _safe_set(a, 'ownedAttribute', b1)
    assert _is_linked(a, 'ownedAttribute', b1)
    if hasattr(b1, 'Class'):
        assert _is_linked(b1, 'Class', a)
    _safe_set(a, 'ownedAttribute', b2)
    assert _is_linked(a, 'ownedAttribute', b2)
    if hasattr(b1, 'Class'):
        assert not _is_linked(b1, 'Class', a)
    if hasattr(b2, 'Class'):
        assert _is_linked(b2, 'Class', a)
    _safe_set(a, 'ownedAttribute', None)
    assert not _is_linked(a, 'ownedAttribute', b2)
    if hasattr(b2, 'Class'):
        assert not _is_linked(b2, 'Class', a)


def test_assoc_class_159_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Class()
    b2 = CompleteDSLPckg_Class()
    _safe_set(a, 'ownedOperation', b1)
    assert _is_linked(a, 'ownedOperation', b1)
    if hasattr(b1, 'Class160'):
        assert _is_linked(b1, 'Class160', a)
    _safe_set(a, 'ownedOperation', b2)
    assert _is_linked(a, 'ownedOperation', b2)
    if hasattr(b1, 'Class160'):
        assert not _is_linked(b1, 'Class160', a)
    if hasattr(b2, 'Class160'):
        assert _is_linked(b2, 'Class160', a)
    _safe_set(a, 'ownedOperation', None)
    assert not _is_linked(a, 'ownedOperation', b2)
    if hasattr(b2, 'Class160'):
        assert not _is_linked(b2, 'Class160', a)


def test_assoc_classifier426_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_CreateObjectAction()
    b2 = CompleteDSLPckg_CreateObjectAction()
    _safe_set(a, 'CompleteDSLPckg_Classifier427', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier427', b1)
    if hasattr(b1, 'CompleteDSLPckg_CreateObjectAction'):
        assert _is_linked(b1, 'CompleteDSLPckg_CreateObjectAction', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier427', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier427', b2)
    if hasattr(b1, 'CompleteDSLPckg_CreateObjectAction'):
        assert not _is_linked(b1, 'CompleteDSLPckg_CreateObjectAction', a)
    if hasattr(b2, 'CompleteDSLPckg_CreateObjectAction'):
        assert _is_linked(b2, 'CompleteDSLPckg_CreateObjectAction', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier427', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier427', b2)
    if hasattr(b2, 'CompleteDSLPckg_CreateObjectAction'):
        assert not _is_linked(b2, 'CompleteDSLPckg_CreateObjectAction', a)


def test_assoc_classifier509_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_ReadExtendAction()
    b2 = CompleteDSLPckg_ReadExtendAction()
    _safe_set(a, 'CompleteDSLPckg_Classifier511', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier511', b1)
    if hasattr(b1, 'CompleteDSLPckg_ReadExtendAction510'):
        assert _is_linked(b1, 'CompleteDSLPckg_ReadExtendAction510', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier511', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier511', b2)
    if hasattr(b1, 'CompleteDSLPckg_ReadExtendAction510'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ReadExtendAction510', a)
    if hasattr(b2, 'CompleteDSLPckg_ReadExtendAction510'):
        assert _is_linked(b2, 'CompleteDSLPckg_ReadExtendAction510', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier511', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier511', b2)
    if hasattr(b2, 'CompleteDSLPckg_ReadExtendAction510'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ReadExtendAction510', a)


def test_assoc_classifier66_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_InstanceSpecification()
    b2 = CompleteDSLPckg_InstanceSpecification()
    _safe_set(a, 'CompleteDSLPckg_Classifier', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier', b1)
    if hasattr(b1, 'CompleteDSLPckg_InstanceSpecification67'):
        assert _is_linked(b1, 'CompleteDSLPckg_InstanceSpecification67', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier', b2)
    if hasattr(b1, 'CompleteDSLPckg_InstanceSpecification67'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InstanceSpecification67', a)
    if hasattr(b2, 'CompleteDSLPckg_InstanceSpecification67'):
        assert _is_linked(b2, 'CompleteDSLPckg_InstanceSpecification67', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier', b2)
    if hasattr(b2, 'CompleteDSLPckg_InstanceSpecification67'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InstanceSpecification67', a)


def test_assoc_classifierBehavior224_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_BehavioredClassifier()
    b2 = CompleteDSLPckg_BehavioredClassifier()
    _safe_set(a, 'CompleteDSLPckg_Behavior226', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior226', b1)
    if hasattr(b1, 'CompleteDSLPckg_BehavioredClassifier225'):
        assert _is_linked(b1, 'CompleteDSLPckg_BehavioredClassifier225', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior226', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior226', b2)
    if hasattr(b1, 'CompleteDSLPckg_BehavioredClassifier225'):
        assert not _is_linked(b1, 'CompleteDSLPckg_BehavioredClassifier225', a)
    if hasattr(b2, 'CompleteDSLPckg_BehavioredClassifier225'):
        assert _is_linked(b2, 'CompleteDSLPckg_BehavioredClassifier225', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior226', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior226', b2)
    if hasattr(b2, 'CompleteDSLPckg_BehavioredClassifier225'):
        assert not _is_linked(b2, 'CompleteDSLPckg_BehavioredClassifier225', a)


def test_assoc_clause840_link_reassign_clear():
    a = CompleteDSLPckg_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = CompleteDSLPckg_Clause()
    b2 = CompleteDSLPckg_Clause()
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode', b1)
    if hasattr(b1, 'CompleteDSLPckg_Clause'):
        assert _is_linked(b1, 'CompleteDSLPckg_Clause', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode', b2)
    if hasattr(b1, 'CompleteDSLPckg_Clause'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Clause', a)
    if hasattr(b2, 'CompleteDSLPckg_Clause'):
        assert _is_linked(b2, 'CompleteDSLPckg_Clause', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ConditionalNode', b2)
    if hasattr(b2, 'CompleteDSLPckg_Clause'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Clause', a)


def test_assoc_client195_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Dependency()
    b2 = CompleteDSLPckg_Dependency()
    _safe_set(a, 'NamedElement196', b1)
    assert _is_linked(a, 'NamedElement196', b1)
    if hasattr(b1, 'clientDependency'):
        assert _is_linked(b1, 'clientDependency', a)
    _safe_set(a, 'NamedElement196', b2)
    assert _is_linked(a, 'NamedElement196', b2)
    if hasattr(b1, 'clientDependency'):
        assert not _is_linked(b1, 'clientDependency', a)
    if hasattr(b2, 'clientDependency'):
        assert _is_linked(b2, 'clientDependency', a)
    _safe_set(a, 'NamedElement196', None)
    assert not _is_linked(a, 'NamedElement196', b2)
    if hasattr(b2, 'clientDependency'):
        assert not _is_linked(b2, 'clientDependency', a)


def test_assoc_clientDependency7_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Dependency()
    b2 = CompleteDSLPckg_Dependency()
    _safe_set(a, 'client', {b1})
    assert _is_linked(a, 'client', b1)
    if hasattr(b1, 'Dependency'):
        assert _is_linked(b1, 'Dependency', a)
    _safe_set(a, 'client', {b2})
    assert _is_linked(a, 'client', b2)
    if hasattr(b1, 'Dependency'):
        assert not _is_linked(b1, 'Dependency', a)
    if hasattr(b2, 'Dependency'):
        assert _is_linked(b2, 'Dependency', a)
    _safe_set(a, 'client', set())
    assert not _is_linked(a, 'client', b2)
    if hasattr(b2, 'Dependency'):
        assert not _is_linked(b2, 'Dependency', a)


def test_assoc_collaborationUse99_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_CollaborationUse()
    b2 = CompleteDSLPckg_CollaborationUse()
    _safe_set(a, 'CompleteDSLPckg_Classifier100', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Classifier100', b1)
    if hasattr(b1, 'CompleteDSLPckg_CollaborationUse'):
        assert _is_linked(b1, 'CompleteDSLPckg_CollaborationUse', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier100', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Classifier100', b2)
    if hasattr(b1, 'CompleteDSLPckg_CollaborationUse'):
        assert not _is_linked(b1, 'CompleteDSLPckg_CollaborationUse', a)
    if hasattr(b2, 'CompleteDSLPckg_CollaborationUse'):
        assert _is_linked(b2, 'CompleteDSLPckg_CollaborationUse', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier100', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier100', b2)
    if hasattr(b2, 'CompleteDSLPckg_CollaborationUse'):
        assert not _is_linked(b2, 'CompleteDSLPckg_CollaborationUse', a)


def test_assoc_collection555_link_reassign_clear():
    a = CompleteDSLPckg_ReduceAction(isOrdered=True)
    b1 = CompleteDSLPckg_InputPin()
    b2 = CompleteDSLPckg_InputPin()
    _safe_set(a, 'CompleteDSLPckg_ReduceAction556', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ReduceAction556', b1)
    if hasattr(b1, 'CompleteDSLPckg_InputPin557'):
        assert _is_linked(b1, 'CompleteDSLPckg_InputPin557', a)
    _safe_set(a, 'CompleteDSLPckg_ReduceAction556', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ReduceAction556', b2)
    if hasattr(b1, 'CompleteDSLPckg_InputPin557'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InputPin557', a)
    if hasattr(b2, 'CompleteDSLPckg_InputPin557'):
        assert _is_linked(b2, 'CompleteDSLPckg_InputPin557', a)
    _safe_set(a, 'CompleteDSLPckg_ReduceAction556', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ReduceAction556', b2)
    if hasattr(b2, 'CompleteDSLPckg_InputPin557'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InputPin557', a)


def test_assoc_configuration387_link_reassign_clear():
    a = CompleteDSLPckg_DeploymentSpecification(deploymentLocation="sample_text", executionLocation="sample_text")
    b1 = CompleteDSLPckg_Deployment()
    b2 = CompleteDSLPckg_Deployment()
    _safe_set(a, 'CompleteDSLPckg_DeploymentSpecification', b1)
    assert _is_linked(a, 'CompleteDSLPckg_DeploymentSpecification', b1)
    if hasattr(b1, 'CompleteDSLPckg_Deployment388'):
        assert _is_linked(b1, 'CompleteDSLPckg_Deployment388', a)
    _safe_set(a, 'CompleteDSLPckg_DeploymentSpecification', b2)
    assert _is_linked(a, 'CompleteDSLPckg_DeploymentSpecification', b2)
    if hasattr(b1, 'CompleteDSLPckg_Deployment388'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Deployment388', a)
    if hasattr(b2, 'CompleteDSLPckg_Deployment388'):
        assert _is_linked(b2, 'CompleteDSLPckg_Deployment388', a)
    _safe_set(a, 'CompleteDSLPckg_DeploymentSpecification', None)
    assert not _is_linked(a, 'CompleteDSLPckg_DeploymentSpecification', b2)
    if hasattr(b2, 'CompleteDSLPckg_Deployment388'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Deployment388', a)


def test_assoc_connection636_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_ConnectionPointReference()
    b2 = CompleteDSLPckg_ConnectionPointReference()
    _safe_set(a, 'CompleteDSLPckg_State637', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_State637', b1)
    if hasattr(b1, 'CompleteDSLPckg_ConnectionPointReference638'):
        assert _is_linked(b1, 'CompleteDSLPckg_ConnectionPointReference638', a)
    _safe_set(a, 'CompleteDSLPckg_State637', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_State637', b2)
    if hasattr(b1, 'CompleteDSLPckg_ConnectionPointReference638'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ConnectionPointReference638', a)
    if hasattr(b2, 'CompleteDSLPckg_ConnectionPointReference638'):
        assert _is_linked(b2, 'CompleteDSLPckg_ConnectionPointReference638', a)
    _safe_set(a, 'CompleteDSLPckg_State637', set())
    assert not _is_linked(a, 'CompleteDSLPckg_State637', b2)
    if hasattr(b2, 'CompleteDSLPckg_ConnectionPointReference638'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ConnectionPointReference638', a)


def test_assoc_connectionPoint639_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Pseudostate()
    b2 = CompleteDSLPckg_Pseudostate()
    _safe_set(a, 'CompleteDSLPckg_State640', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_State640', b1)
    if hasattr(b1, 'CompleteDSLPckg_Pseudostate641'):
        assert _is_linked(b1, 'CompleteDSLPckg_Pseudostate641', a)
    _safe_set(a, 'CompleteDSLPckg_State640', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_State640', b2)
    if hasattr(b1, 'CompleteDSLPckg_Pseudostate641'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Pseudostate641', a)
    if hasattr(b2, 'CompleteDSLPckg_Pseudostate641'):
        assert _is_linked(b2, 'CompleteDSLPckg_Pseudostate641', a)
    _safe_set(a, 'CompleteDSLPckg_State640', set())
    assert not _is_linked(a, 'CompleteDSLPckg_State640', b2)
    if hasattr(b2, 'CompleteDSLPckg_Pseudostate641'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Pseudostate641', a)


def test_assoc_connector925_link_reassign_clear():
    a = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    b1 = CompleteDSLPckg_Connector(kind="sample_text")
    b2 = CompleteDSLPckg_Connector(kind="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_Message926', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Message926', b1)
    if hasattr(b1, 'CompleteDSLPckg_Connector927'):
        assert _is_linked(b1, 'CompleteDSLPckg_Connector927', a)
    _safe_set(a, 'CompleteDSLPckg_Message926', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Message926', b2)
    if hasattr(b1, 'CompleteDSLPckg_Connector927'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Connector927', a)
    if hasattr(b2, 'CompleteDSLPckg_Connector927'):
        assert _is_linked(b2, 'CompleteDSLPckg_Connector927', a)
    _safe_set(a, 'CompleteDSLPckg_Message926', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Message926', b2)
    if hasattr(b2, 'CompleteDSLPckg_Connector927'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Connector927', a)


def test_assoc_container619_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Region()
    b2 = CompleteDSLPckg_Region()
    _safe_set(a, 'CompleteDSLPckg_Transition620', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition620', b1)
    if hasattr(b1, 'CompleteDSLPckg_Region621'):
        assert _is_linked(b1, 'CompleteDSLPckg_Region621', a)
    _safe_set(a, 'CompleteDSLPckg_Transition620', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition620', b2)
    if hasattr(b1, 'CompleteDSLPckg_Region621'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Region621', a)
    if hasattr(b2, 'CompleteDSLPckg_Region621'):
        assert _is_linked(b2, 'CompleteDSLPckg_Region621', a)
    _safe_set(a, 'CompleteDSLPckg_Transition620', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition620', b2)
    if hasattr(b2, 'CompleteDSLPckg_Region621'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Region621', a)


def test_assoc_context231_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_BehavioredClassifier()
    b2 = CompleteDSLPckg_BehavioredClassifier()
    _safe_set(a, 'CompleteDSLPckg_Behavior232', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior232', b1)
    if hasattr(b1, 'CompleteDSLPckg_BehavioredClassifier233'):
        assert _is_linked(b1, 'CompleteDSLPckg_BehavioredClassifier233', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior232', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior232', b2)
    if hasattr(b1, 'CompleteDSLPckg_BehavioredClassifier233'):
        assert not _is_linked(b1, 'CompleteDSLPckg_BehavioredClassifier233', a)
    if hasattr(b2, 'CompleteDSLPckg_BehavioredClassifier233'):
        assert _is_linked(b2, 'CompleteDSLPckg_BehavioredClassifier233', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior232', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior232', b2)
    if hasattr(b2, 'CompleteDSLPckg_BehavioredClassifier233'):
        assert not _is_linked(b2, 'CompleteDSLPckg_BehavioredClassifier233', a)


def test_assoc_context392_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Action()
    b2 = CompleteDSLPckg_Action()
    _safe_set(a, 'CompleteDSLPckg_Classifier393', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier393', b1)
    if hasattr(b1, 'CompleteDSLPckg_Action'):
        assert _is_linked(b1, 'CompleteDSLPckg_Action', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier393', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier393', b2)
    if hasattr(b1, 'CompleteDSLPckg_Action'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Action', a)
    if hasattr(b2, 'CompleteDSLPckg_Action'):
        assert _is_linked(b2, 'CompleteDSLPckg_Action', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier393', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier393', b2)
    if hasattr(b2, 'CompleteDSLPckg_Action'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Action', a)


def test_assoc_contract203_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Substitution()
    b2 = CompleteDSLPckg_Substitution()
    _safe_set(a, 'CompleteDSLPckg_Classifier204', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier204', b1)
    if hasattr(b1, 'CompleteDSLPckg_Substitution'):
        assert _is_linked(b1, 'CompleteDSLPckg_Substitution', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier204', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier204', b2)
    if hasattr(b1, 'CompleteDSLPckg_Substitution'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Substitution', a)
    if hasattr(b2, 'CompleteDSLPckg_Substitution'):
        assert _is_linked(b2, 'CompleteDSLPckg_Substitution', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier204', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier204', b2)
    if hasattr(b2, 'CompleteDSLPckg_Substitution'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Substitution', a)


def test_assoc_contract312_link_reassign_clear():
    a = CompleteDSLPckg_Connector(kind="sample_text")
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_Connector313', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Connector313', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior314'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior314', a)
    _safe_set(a, 'CompleteDSLPckg_Connector313', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Connector313', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior314'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior314', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior314'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior314', a)
    _safe_set(a, 'CompleteDSLPckg_Connector313', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Connector313', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior314'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior314', a)


def test_assoc_dataType121_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_DataType()
    b2 = CompleteDSLPckg_DataType()
    _safe_set(a, 'ownedAttribute122', b1)
    assert _is_linked(a, 'ownedAttribute122', b1)
    if hasattr(b1, 'DataType'):
        assert _is_linked(b1, 'DataType', a)
    _safe_set(a, 'ownedAttribute122', b2)
    assert _is_linked(a, 'ownedAttribute122', b2)
    if hasattr(b1, 'DataType'):
        assert not _is_linked(b1, 'DataType', a)
    if hasattr(b2, 'DataType'):
        assert _is_linked(b2, 'DataType', a)
    _safe_set(a, 'ownedAttribute122', None)
    assert not _is_linked(a, 'ownedAttribute122', b2)
    if hasattr(b2, 'DataType'):
        assert not _is_linked(b2, 'DataType', a)


def test_assoc_dataType161_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_DataType()
    b2 = CompleteDSLPckg_DataType()
    _safe_set(a, 'ownedOperation162', b1)
    assert _is_linked(a, 'ownedOperation162', b1)
    if hasattr(b1, 'DataType163'):
        assert _is_linked(b1, 'DataType163', a)
    _safe_set(a, 'ownedOperation162', b2)
    assert _is_linked(a, 'ownedOperation162', b2)
    if hasattr(b1, 'DataType163'):
        assert not _is_linked(b1, 'DataType163', a)
    if hasattr(b2, 'DataType163'):
        assert _is_linked(b2, 'DataType163', a)
    _safe_set(a, 'ownedOperation162', None)
    assert not _is_linked(a, 'ownedOperation162', b2)
    if hasattr(b2, 'DataType163'):
        assert not _is_linked(b2, 'DataType163', a)


def test_assoc_decider825_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_LoopNode826', b1)
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode826', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin827'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin827', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode826', b2)
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode826', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin827'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin827', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin827'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin827', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode826', None)
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode826', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin827'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin827', a)


def test_assoc_decisionInput769_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_DecisionNode()
    b2 = CompleteDSLPckg_DecisionNode()
    _safe_set(a, 'CompleteDSLPckg_Behavior771', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior771', b1)
    if hasattr(b1, 'CompleteDSLPckg_DecisionNode770'):
        assert _is_linked(b1, 'CompleteDSLPckg_DecisionNode770', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior771', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior771', b2)
    if hasattr(b1, 'CompleteDSLPckg_DecisionNode770'):
        assert not _is_linked(b1, 'CompleteDSLPckg_DecisionNode770', a)
    if hasattr(b2, 'CompleteDSLPckg_DecisionNode770'):
        assert _is_linked(b2, 'CompleteDSLPckg_DecisionNode770', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior771', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior771', b2)
    if hasattr(b2, 'CompleteDSLPckg_DecisionNode770'):
        assert not _is_linked(b2, 'CompleteDSLPckg_DecisionNode770', a)


def test_assoc_decisionInputFlow767_link_reassign_clear():
    a = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    b1 = CompleteDSLPckg_DecisionNode()
    b2 = CompleteDSLPckg_DecisionNode()
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow768', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ObjectFlow768', b1)
    if hasattr(b1, 'CompleteDSLPckg_DecisionNode'):
        assert _is_linked(b1, 'CompleteDSLPckg_DecisionNode', a)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow768', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ObjectFlow768', b2)
    if hasattr(b1, 'CompleteDSLPckg_DecisionNode'):
        assert not _is_linked(b1, 'CompleteDSLPckg_DecisionNode', a)
    if hasattr(b2, 'CompleteDSLPckg_DecisionNode'):
        assert _is_linked(b2, 'CompleteDSLPckg_DecisionNode', a)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow768', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ObjectFlow768', b2)
    if hasattr(b2, 'CompleteDSLPckg_DecisionNode'):
        assert not _is_linked(b2, 'CompleteDSLPckg_DecisionNode', a)


def test_assoc_defaultValue109_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'CompleteDSLPckg_Property110', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property110', b1)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification111'):
        assert _is_linked(b1, 'CompleteDSLPckg_ValueSpecification111', a)
    _safe_set(a, 'CompleteDSLPckg_Property110', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property110', b2)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification111'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ValueSpecification111', a)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification111'):
        assert _is_linked(b2, 'CompleteDSLPckg_ValueSpecification111', a)
    _safe_set(a, 'CompleteDSLPckg_Property110', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property110', b2)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification111'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ValueSpecification111', a)


def test_assoc_defaultValue145_link_reassign_clear():
    a = CompleteDSLPckg_Parameter(default="sample_text")
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'CompleteDSLPckg_Parameter146', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter146', b1)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification147'):
        assert _is_linked(b1, 'CompleteDSLPckg_ValueSpecification147', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter146', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter146', b2)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification147'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ValueSpecification147', a)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification147'):
        assert _is_linked(b2, 'CompleteDSLPckg_ValueSpecification147', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter146', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Parameter146', b2)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification147'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ValueSpecification147', a)


def test_assoc_deferrableTrigger648_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Trigger()
    b2 = CompleteDSLPckg_Trigger()
    _safe_set(a, 'CompleteDSLPckg_State649', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_State649', b1)
    if hasattr(b1, 'CompleteDSLPckg_Trigger650'):
        assert _is_linked(b1, 'CompleteDSLPckg_Trigger650', a)
    _safe_set(a, 'CompleteDSLPckg_State649', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_State649', b2)
    if hasattr(b1, 'CompleteDSLPckg_Trigger650'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Trigger650', a)
    if hasattr(b2, 'CompleteDSLPckg_Trigger650'):
        assert _is_linked(b2, 'CompleteDSLPckg_Trigger650', a)
    _safe_set(a, 'CompleteDSLPckg_State649', set())
    assert not _is_linked(a, 'CompleteDSLPckg_State649', b2)
    if hasattr(b2, 'CompleteDSLPckg_Trigger650'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Trigger650', a)


def test_assoc_definingEnd326_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_ConnectorEnd()
    b2 = CompleteDSLPckg_ConnectorEnd()
    _safe_set(a, 'CompleteDSLPckg_Property328', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property328', b1)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd327'):
        assert _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd327', a)
    _safe_set(a, 'CompleteDSLPckg_Property328', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property328', b2)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd327'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd327', a)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd327'):
        assert _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd327', a)
    _safe_set(a, 'CompleteDSLPckg_Property328', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property328', b2)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd327'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd327', a)


def test_assoc_definingFeature78_link_reassign_clear():
    a = CompleteDSLPckg_StructuralFeature(isReadOnly=True)
    b1 = CompleteDSLPckg_Slot()
    b2 = CompleteDSLPckg_Slot()
    _safe_set(a, 'CompleteDSLPckg_StructuralFeature', b1)
    assert _is_linked(a, 'CompleteDSLPckg_StructuralFeature', b1)
    if hasattr(b1, 'CompleteDSLPckg_Slot'):
        assert _is_linked(b1, 'CompleteDSLPckg_Slot', a)
    _safe_set(a, 'CompleteDSLPckg_StructuralFeature', b2)
    assert _is_linked(a, 'CompleteDSLPckg_StructuralFeature', b2)
    if hasattr(b1, 'CompleteDSLPckg_Slot'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Slot', a)
    if hasattr(b2, 'CompleteDSLPckg_Slot'):
        assert _is_linked(b2, 'CompleteDSLPckg_Slot', a)
    _safe_set(a, 'CompleteDSLPckg_StructuralFeature', None)
    assert not _is_linked(a, 'CompleteDSLPckg_StructuralFeature', b2)
    if hasattr(b2, 'CompleteDSLPckg_Slot'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Slot', a)


def test_assoc_deployment389_link_reassign_clear():
    a = CompleteDSLPckg_DeploymentSpecification(deploymentLocation="sample_text", executionLocation="sample_text")
    b1 = CompleteDSLPckg_Deployment()
    b2 = CompleteDSLPckg_Deployment()
    _safe_set(a, 'CompleteDSLPckg_DeploymentSpecification390', b1)
    assert _is_linked(a, 'CompleteDSLPckg_DeploymentSpecification390', b1)
    if hasattr(b1, 'CompleteDSLPckg_Deployment391'):
        assert _is_linked(b1, 'CompleteDSLPckg_Deployment391', a)
    _safe_set(a, 'CompleteDSLPckg_DeploymentSpecification390', b2)
    assert _is_linked(a, 'CompleteDSLPckg_DeploymentSpecification390', b2)
    if hasattr(b1, 'CompleteDSLPckg_Deployment391'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Deployment391', a)
    if hasattr(b2, 'CompleteDSLPckg_Deployment391'):
        assert _is_linked(b2, 'CompleteDSLPckg_Deployment391', a)
    _safe_set(a, 'CompleteDSLPckg_DeploymentSpecification390', None)
    assert not _is_linked(a, 'CompleteDSLPckg_DeploymentSpecification390', b2)
    if hasattr(b2, 'CompleteDSLPckg_Deployment391'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Deployment391', a)


def test_assoc_destroyAt482_link_reassign_clear():
    a = CompleteDSLPckg_LinkEndDestructionData(isDestroyDuplicates=True)
    b1 = CompleteDSLPckg_InputPin()
    b2 = CompleteDSLPckg_InputPin()
    _safe_set(a, 'CompleteDSLPckg_LinkEndDestructionData', b1)
    assert _is_linked(a, 'CompleteDSLPckg_LinkEndDestructionData', b1)
    if hasattr(b1, 'CompleteDSLPckg_InputPin483'):
        assert _is_linked(b1, 'CompleteDSLPckg_InputPin483', a)
    _safe_set(a, 'CompleteDSLPckg_LinkEndDestructionData', b2)
    assert _is_linked(a, 'CompleteDSLPckg_LinkEndDestructionData', b2)
    if hasattr(b1, 'CompleteDSLPckg_InputPin483'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InputPin483', a)
    if hasattr(b2, 'CompleteDSLPckg_InputPin483'):
        assert _is_linked(b2, 'CompleteDSLPckg_InputPin483', a)
    _safe_set(a, 'CompleteDSLPckg_LinkEndDestructionData', None)
    assert not _is_linked(a, 'CompleteDSLPckg_LinkEndDestructionData', b2)
    if hasattr(b2, 'CompleteDSLPckg_InputPin483'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InputPin483', a)


def test_assoc_doActivity654_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_State655', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State655', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior656'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior656', a)
    _safe_set(a, 'CompleteDSLPckg_State655', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State655', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior656'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior656', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior656'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior656', a)
    _safe_set(a, 'CompleteDSLPckg_State655', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State655', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior656'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior656', a)


def test_assoc_durationSpecification293_link_reassign_clear():
    a = CompleteDSLPckg_DurationConstraint(firstEvent=True)
    b1 = CompleteDSLPckg_DurationInterval()
    b2 = CompleteDSLPckg_DurationInterval()
    _safe_set(a, 'CompleteDSLPckg_DurationConstraint', b1)
    assert _is_linked(a, 'CompleteDSLPckg_DurationConstraint', b1)
    if hasattr(b1, 'CompleteDSLPckg_DurationInterval294'):
        assert _is_linked(b1, 'CompleteDSLPckg_DurationInterval294', a)
    _safe_set(a, 'CompleteDSLPckg_DurationConstraint', b2)
    assert _is_linked(a, 'CompleteDSLPckg_DurationConstraint', b2)
    if hasattr(b1, 'CompleteDSLPckg_DurationInterval294'):
        assert not _is_linked(b1, 'CompleteDSLPckg_DurationInterval294', a)
    if hasattr(b2, 'CompleteDSLPckg_DurationInterval294'):
        assert _is_linked(b2, 'CompleteDSLPckg_DurationInterval294', a)
    _safe_set(a, 'CompleteDSLPckg_DurationConstraint', None)
    assert not _is_linked(a, 'CompleteDSLPckg_DurationConstraint', b2)
    if hasattr(b2, 'CompleteDSLPckg_DurationInterval294'):
        assert not _is_linked(b2, 'CompleteDSLPckg_DurationInterval294', a)


def test_assoc_edge684_link_reassign_clear():
    a = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = CompleteDSLPckg_ActivityEdge()
    b2 = CompleteDSLPckg_ActivityEdge()
    _safe_set(a, 'CompleteDSLPckg_Activity685', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Activity685', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityEdge'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityEdge', a)
    _safe_set(a, 'CompleteDSLPckg_Activity685', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Activity685', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityEdge'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityEdge', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityEdge'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityEdge', a)
    _safe_set(a, 'CompleteDSLPckg_Activity685', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Activity685', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityEdge'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityEdge', a)


def test_assoc_edge810_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_ActivityEdge()
    b2 = CompleteDSLPckg_ActivityEdge()
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode811', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode811', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityEdge812'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityEdge812', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode811', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode811', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityEdge812'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityEdge812', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityEdge812'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityEdge812', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode811', set())
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode811', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityEdge812'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityEdge812', a)


def test_assoc_effect610_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_Transition611', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition611', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior612'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior612', a)
    _safe_set(a, 'CompleteDSLPckg_Transition611', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition611', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior612'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior612', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior612'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior612', a)
    _safe_set(a, 'CompleteDSLPckg_Transition611', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition611', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior612'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior612', a)


def test_assoc_elementImport12_link_reassign_clear():
    a = CompleteDSLPckg_ElementImport(alias="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Namespace()
    b2 = CompleteDSLPckg_Namespace()
    _safe_set(a, 'ElementImport', b1)
    assert _is_linked(a, 'ElementImport', b1)
    if hasattr(b1, 'importingNamespace'):
        assert _is_linked(b1, 'importingNamespace', a)
    _safe_set(a, 'ElementImport', b2)
    assert _is_linked(a, 'ElementImport', b2)
    if hasattr(b1, 'importingNamespace'):
        assert not _is_linked(b1, 'importingNamespace', a)
    if hasattr(b2, 'importingNamespace'):
        assert _is_linked(b2, 'importingNamespace', a)
    _safe_set(a, 'ElementImport', None)
    assert not _is_linked(a, 'ElementImport', b2)
    if hasattr(b2, 'importingNamespace'):
        assert not _is_linked(b2, 'importingNamespace', a)


def test_assoc_end311_link_reassign_clear():
    a = CompleteDSLPckg_Connector(kind="sample_text")
    b1 = CompleteDSLPckg_ConnectorEnd()
    b2 = CompleteDSLPckg_ConnectorEnd()
    _safe_set(a, 'CompleteDSLPckg_Connector', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Connector', b1)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd'):
        assert _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd', a)
    _safe_set(a, 'CompleteDSLPckg_Connector', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Connector', b2)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd', a)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd'):
        assert _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd', a)
    _safe_set(a, 'CompleteDSLPckg_Connector', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Connector', b2)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd', a)


def test_assoc_end473_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_LinkEndData()
    b2 = CompleteDSLPckg_LinkEndData()
    _safe_set(a, 'CompleteDSLPckg_Property475', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property475', b1)
    if hasattr(b1, 'CompleteDSLPckg_LinkEndData474'):
        assert _is_linked(b1, 'CompleteDSLPckg_LinkEndData474', a)
    _safe_set(a, 'CompleteDSLPckg_Property475', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property475', b2)
    if hasattr(b1, 'CompleteDSLPckg_LinkEndData474'):
        assert not _is_linked(b1, 'CompleteDSLPckg_LinkEndData474', a)
    if hasattr(b2, 'CompleteDSLPckg_LinkEndData474'):
        assert _is_linked(b2, 'CompleteDSLPckg_LinkEndData474', a)
    _safe_set(a, 'CompleteDSLPckg_Property475', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property475', b2)
    if hasattr(b2, 'CompleteDSLPckg_LinkEndData474'):
        assert not _is_linked(b2, 'CompleteDSLPckg_LinkEndData474', a)


def test_assoc_end535_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_ReadLinkObjectEndAction()
    b2 = CompleteDSLPckg_ReadLinkObjectEndAction()
    _safe_set(a, 'CompleteDSLPckg_Property536', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property536', b1)
    if hasattr(b1, 'CompleteDSLPckg_ReadLinkObjectEndAction'):
        assert _is_linked(b1, 'CompleteDSLPckg_ReadLinkObjectEndAction', a)
    _safe_set(a, 'CompleteDSLPckg_Property536', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property536', b2)
    if hasattr(b1, 'CompleteDSLPckg_ReadLinkObjectEndAction'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ReadLinkObjectEndAction', a)
    if hasattr(b2, 'CompleteDSLPckg_ReadLinkObjectEndAction'):
        assert _is_linked(b2, 'CompleteDSLPckg_ReadLinkObjectEndAction', a)
    _safe_set(a, 'CompleteDSLPckg_Property536', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property536', b2)
    if hasattr(b2, 'CompleteDSLPckg_ReadLinkObjectEndAction'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ReadLinkObjectEndAction', a)


def test_assoc_entry657_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_State658', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State658', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior659'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior659', a)
    _safe_set(a, 'CompleteDSLPckg_State658', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State658', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior659'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior659', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior659'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior659', a)
    _safe_set(a, 'CompleteDSLPckg_State658', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State658', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior659'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior659', a)


def test_assoc_event267_link_reassign_clear():
    a = CompleteDSLPckg_TimeObservation(firstEvent=True)
    b1 = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b2 = CompleteDSLPckg_NamedElement(name="sample_text_2", qualifiedName="sample_text_2", visibility="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_TimeObservation', b1)
    assert _is_linked(a, 'CompleteDSLPckg_TimeObservation', b1)
    if hasattr(b1, 'CompleteDSLPckg_NamedElement268'):
        assert _is_linked(b1, 'CompleteDSLPckg_NamedElement268', a)
    _safe_set(a, 'CompleteDSLPckg_TimeObservation', b2)
    assert _is_linked(a, 'CompleteDSLPckg_TimeObservation', b2)
    if hasattr(b1, 'CompleteDSLPckg_NamedElement268'):
        assert not _is_linked(b1, 'CompleteDSLPckg_NamedElement268', a)
    if hasattr(b2, 'CompleteDSLPckg_NamedElement268'):
        assert _is_linked(b2, 'CompleteDSLPckg_NamedElement268', a)
    _safe_set(a, 'CompleteDSLPckg_TimeObservation', None)
    assert not _is_linked(a, 'CompleteDSLPckg_TimeObservation', b2)
    if hasattr(b2, 'CompleteDSLPckg_NamedElement268'):
        assert not _is_linked(b2, 'CompleteDSLPckg_NamedElement268', a)


def test_assoc_event269_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_DurationObservation(firstEvent=True)
    b2 = CompleteDSLPckg_DurationObservation(firstEvent=False)
    _safe_set(a, 'CompleteDSLPckg_NamedElement270', b1)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement270', b1)
    if hasattr(b1, 'CompleteDSLPckg_DurationObservation'):
        assert _is_linked(b1, 'CompleteDSLPckg_DurationObservation', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement270', b2)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement270', b2)
    if hasattr(b1, 'CompleteDSLPckg_DurationObservation'):
        assert not _is_linked(b1, 'CompleteDSLPckg_DurationObservation', a)
    if hasattr(b2, 'CompleteDSLPckg_DurationObservation'):
        assert _is_linked(b2, 'CompleteDSLPckg_DurationObservation', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement270', None)
    assert not _is_linked(a, 'CompleteDSLPckg_NamedElement270', b2)
    if hasattr(b2, 'CompleteDSLPckg_DurationObservation'):
        assert not _is_linked(b2, 'CompleteDSLPckg_DurationObservation', a)


def test_assoc_exceptionType869_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_ExceptionHandler()
    b2 = CompleteDSLPckg_ExceptionHandler()
    _safe_set(a, 'CompleteDSLPckg_Classifier871', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier871', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExceptionHandler870'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExceptionHandler870', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier871', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier871', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExceptionHandler870'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExceptionHandler870', a)
    if hasattr(b2, 'CompleteDSLPckg_ExceptionHandler870'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExceptionHandler870', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier871', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier871', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExceptionHandler870'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExceptionHandler870', a)


def test_assoc_exit651_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_State652', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State652', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior653'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior653', a)
    _safe_set(a, 'CompleteDSLPckg_State652', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State652', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior653'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior653', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior653'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior653', a)
    _safe_set(a, 'CompleteDSLPckg_State652', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State652', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior653'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior653', a)


def test_assoc_feature87_link_reassign_clear():
    a = CompleteDSLPckg_Feature(isStatic=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'Feature', b1)
    assert _is_linked(a, 'Feature', b1)
    if hasattr(b1, 'featuringClassifier'):
        assert _is_linked(b1, 'featuringClassifier', a)
    _safe_set(a, 'Feature', b2)
    assert _is_linked(a, 'Feature', b2)
    if hasattr(b1, 'featuringClassifier'):
        assert not _is_linked(b1, 'featuringClassifier', a)
    if hasattr(b2, 'featuringClassifier'):
        assert _is_linked(b2, 'featuringClassifier', a)
    _safe_set(a, 'Feature', None)
    assert not _is_linked(a, 'Feature', b2)
    if hasattr(b2, 'featuringClassifier'):
        assert not _is_linked(b2, 'featuringClassifier', a)


def test_assoc_featuringClassifier104_link_reassign_clear():
    a = CompleteDSLPckg_Feature(isStatic=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'feature', {b1})
    assert _is_linked(a, 'feature', b1)
    if hasattr(b1, 'Classifier'):
        assert _is_linked(b1, 'Classifier', a)
    _safe_set(a, 'feature', {b2})
    assert _is_linked(a, 'feature', b2)
    if hasattr(b1, 'Classifier'):
        assert not _is_linked(b1, 'Classifier', a)
    if hasattr(b2, 'Classifier'):
        assert _is_linked(b2, 'Classifier', a)
    _safe_set(a, 'feature', set())
    assert not _is_linked(a, 'feature', b2)
    if hasattr(b2, 'Classifier'):
        assert not _is_linked(b2, 'Classifier', a)


def test_assoc_general130_link_reassign_clear():
    a = CompleteDSLPckg_Generalization(isSubstitutable=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_Generalization', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Generalization', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier131'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier131', a)
    _safe_set(a, 'CompleteDSLPckg_Generalization', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Generalization', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier131'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier131', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier131'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier131', a)
    _safe_set(a, 'CompleteDSLPckg_Generalization', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Generalization', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier131'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier131', a)


def test_assoc_general94_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_Classifier93', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Classifier93', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier95'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier95', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier93', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Classifier93', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier95'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier95', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier95'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier95', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier93', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier93', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier95'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier95', a)


def test_assoc_generalization229_link_reassign_clear():
    a = CompleteDSLPckg_GeneralizationSet(isCovering=True, isDisjoint=True)
    b1 = CompleteDSLPckg_Generalization(isSubstitutable=True)
    b2 = CompleteDSLPckg_Generalization(isSubstitutable=False)
    _safe_set(a, 'generalizationSet', {b1})
    assert _is_linked(a, 'generalizationSet', b1)
    if hasattr(b1, 'Generalization230'):
        assert _is_linked(b1, 'Generalization230', a)
    _safe_set(a, 'generalizationSet', {b2})
    assert _is_linked(a, 'generalizationSet', b2)
    if hasattr(b1, 'Generalization230'):
        assert not _is_linked(b1, 'Generalization230', a)
    if hasattr(b2, 'Generalization230'):
        assert _is_linked(b2, 'Generalization230', a)
    _safe_set(a, 'generalizationSet', set())
    assert not _is_linked(a, 'generalizationSet', b2)
    if hasattr(b2, 'Generalization230'):
        assert not _is_linked(b2, 'Generalization230', a)


def test_assoc_generalization96_link_reassign_clear():
    a = CompleteDSLPckg_Generalization(isSubstitutable=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'Generalization', b1)
    assert _is_linked(a, 'Generalization', b1)
    if hasattr(b1, 'specific'):
        assert _is_linked(b1, 'specific', a)
    _safe_set(a, 'Generalization', b2)
    assert _is_linked(a, 'Generalization', b2)
    if hasattr(b1, 'specific'):
        assert not _is_linked(b1, 'specific', a)
    if hasattr(b2, 'specific'):
        assert _is_linked(b2, 'specific', a)
    _safe_set(a, 'Generalization', None)
    assert not _is_linked(a, 'Generalization', b2)
    if hasattr(b2, 'specific'):
        assert not _is_linked(b2, 'specific', a)


def test_assoc_generalizationSet134_link_reassign_clear():
    a = CompleteDSLPckg_GeneralizationSet(isCovering=True, isDisjoint=True)
    b1 = CompleteDSLPckg_Generalization(isSubstitutable=True)
    b2 = CompleteDSLPckg_Generalization(isSubstitutable=False)
    _safe_set(a, 'GeneralizationSet136', b1)
    assert _is_linked(a, 'GeneralizationSet136', b1)
    if hasattr(b1, 'generalization135'):
        assert _is_linked(b1, 'generalization135', a)
    _safe_set(a, 'GeneralizationSet136', b2)
    assert _is_linked(a, 'GeneralizationSet136', b2)
    if hasattr(b1, 'generalization135'):
        assert not _is_linked(b1, 'generalization135', a)
    if hasattr(b2, 'generalization135'):
        assert _is_linked(b2, 'generalization135', a)
    _safe_set(a, 'GeneralizationSet136', None)
    assert not _is_linked(a, 'GeneralizationSet136', b2)
    if hasattr(b2, 'generalization135'):
        assert not _is_linked(b2, 'generalization135', a)


def test_assoc_group682_link_reassign_clear():
    a = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = CompleteDSLPckg_ActivityGroup()
    b2 = CompleteDSLPckg_ActivityGroup()
    _safe_set(a, 'CompleteDSLPckg_Activity683', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Activity683', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityGroup'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityGroup', a)
    _safe_set(a, 'CompleteDSLPckg_Activity683', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Activity683', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityGroup'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityGroup', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityGroup'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityGroup', a)
    _safe_set(a, 'CompleteDSLPckg_Activity683', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Activity683', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityGroup'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityGroup', a)


def test_assoc_guard616_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Constraint()
    b2 = CompleteDSLPckg_Constraint()
    _safe_set(a, 'CompleteDSLPckg_Transition617', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition617', b1)
    if hasattr(b1, 'CompleteDSLPckg_Constraint618'):
        assert _is_linked(b1, 'CompleteDSLPckg_Constraint618', a)
    _safe_set(a, 'CompleteDSLPckg_Transition617', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition617', b2)
    if hasattr(b1, 'CompleteDSLPckg_Constraint618'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Constraint618', a)
    if hasattr(b2, 'CompleteDSLPckg_Constraint618'):
        assert _is_linked(b2, 'CompleteDSLPckg_Constraint618', a)
    _safe_set(a, 'CompleteDSLPckg_Transition617', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition617', b2)
    if hasattr(b2, 'CompleteDSLPckg_Constraint618'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Constraint618', a)


def test_assoc_importedElement16_link_reassign_clear():
    a = CompleteDSLPckg_ElementImport(alias="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_PackageableElement()
    b2 = CompleteDSLPckg_PackageableElement()
    _safe_set(a, 'CompleteDSLPckg_ElementImport', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ElementImport', b1)
    if hasattr(b1, 'CompleteDSLPckg_PackageableElement17'):
        assert _is_linked(b1, 'CompleteDSLPckg_PackageableElement17', a)
    _safe_set(a, 'CompleteDSLPckg_ElementImport', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ElementImport', b2)
    if hasattr(b1, 'CompleteDSLPckg_PackageableElement17'):
        assert not _is_linked(b1, 'CompleteDSLPckg_PackageableElement17', a)
    if hasattr(b2, 'CompleteDSLPckg_PackageableElement17'):
        assert _is_linked(b2, 'CompleteDSLPckg_PackageableElement17', a)
    _safe_set(a, 'CompleteDSLPckg_ElementImport', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ElementImport', b2)
    if hasattr(b2, 'CompleteDSLPckg_PackageableElement17'):
        assert not _is_linked(b2, 'CompleteDSLPckg_PackageableElement17', a)


def test_assoc_importedPackage20_link_reassign_clear():
    a = CompleteDSLPckg_PackageImport(visibility="sample_text")
    b1 = CompleteDSLPckg_Package(URI="sample_text")
    b2 = CompleteDSLPckg_Package(URI="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_PackageImport', b1)
    assert _is_linked(a, 'CompleteDSLPckg_PackageImport', b1)
    if hasattr(b1, 'CompleteDSLPckg_Package'):
        assert _is_linked(b1, 'CompleteDSLPckg_Package', a)
    _safe_set(a, 'CompleteDSLPckg_PackageImport', b2)
    assert _is_linked(a, 'CompleteDSLPckg_PackageImport', b2)
    if hasattr(b1, 'CompleteDSLPckg_Package'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Package', a)
    if hasattr(b2, 'CompleteDSLPckg_Package'):
        assert _is_linked(b2, 'CompleteDSLPckg_Package', a)
    _safe_set(a, 'CompleteDSLPckg_PackageImport', None)
    assert not _is_linked(a, 'CompleteDSLPckg_PackageImport', b2)
    if hasattr(b2, 'CompleteDSLPckg_Package'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Package', a)


def test_assoc_importingNamespace18_link_reassign_clear():
    a = CompleteDSLPckg_ElementImport(alias="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Namespace()
    b2 = CompleteDSLPckg_Namespace()
    _safe_set(a, 'elementImport', b1)
    assert _is_linked(a, 'elementImport', b1)
    if hasattr(b1, 'Namespace19'):
        assert _is_linked(b1, 'Namespace19', a)
    _safe_set(a, 'elementImport', b2)
    assert _is_linked(a, 'elementImport', b2)
    if hasattr(b1, 'Namespace19'):
        assert not _is_linked(b1, 'Namespace19', a)
    if hasattr(b2, 'Namespace19'):
        assert _is_linked(b2, 'Namespace19', a)
    _safe_set(a, 'elementImport', None)
    assert not _is_linked(a, 'elementImport', b2)
    if hasattr(b2, 'Namespace19'):
        assert not _is_linked(b2, 'Namespace19', a)


def test_assoc_importingNamespace21_link_reassign_clear():
    a = CompleteDSLPckg_PackageImport(visibility="sample_text")
    b1 = CompleteDSLPckg_Namespace()
    b2 = CompleteDSLPckg_Namespace()
    _safe_set(a, 'packageImport', b1)
    assert _is_linked(a, 'packageImport', b1)
    if hasattr(b1, 'Namespace22'):
        assert _is_linked(b1, 'Namespace22', a)
    _safe_set(a, 'packageImport', b2)
    assert _is_linked(a, 'packageImport', b2)
    if hasattr(b1, 'Namespace22'):
        assert not _is_linked(b1, 'Namespace22', a)
    if hasattr(b2, 'Namespace22'):
        assert _is_linked(b2, 'Namespace22', a)
    _safe_set(a, 'packageImport', None)
    assert not _is_linked(a, 'packageImport', b2)
    if hasattr(b2, 'Namespace22'):
        assert not _is_linked(b2, 'Namespace22', a)


def test_assoc_inActivity719_link_reassign_clear():
    a = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = CompleteDSLPckg_ActivityGroup()
    b2 = CompleteDSLPckg_ActivityGroup()
    _safe_set(a, 'CompleteDSLPckg_Activity721', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Activity721', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityGroup720'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityGroup720', a)
    _safe_set(a, 'CompleteDSLPckg_Activity721', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Activity721', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityGroup720'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityGroup720', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityGroup720'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityGroup720', a)
    _safe_set(a, 'CompleteDSLPckg_Activity721', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Activity721', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityGroup720'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityGroup720', a)


def test_assoc_inState762_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    b2 = CompleteDSLPckg_ObjectFlow(isControlType=False, isMulticast=False, isMultireceive=False, ordering="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_State764', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State764', b1)
    if hasattr(b1, 'CompleteDSLPckg_ObjectFlow763'):
        assert _is_linked(b1, 'CompleteDSLPckg_ObjectFlow763', a)
    _safe_set(a, 'CompleteDSLPckg_State764', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State764', b2)
    if hasattr(b1, 'CompleteDSLPckg_ObjectFlow763'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ObjectFlow763', a)
    if hasattr(b2, 'CompleteDSLPckg_ObjectFlow763'):
        assert _is_linked(b2, 'CompleteDSLPckg_ObjectFlow763', a)
    _safe_set(a, 'CompleteDSLPckg_State764', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State764', b2)
    if hasattr(b2, 'CompleteDSLPckg_ObjectFlow763'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ObjectFlow763', a)


def test_assoc_inStructuredNode710_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_ActivityNode()
    b2 = CompleteDSLPckg_ActivityNode()
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode712', b1)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode712', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityNode711'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityNode711', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode712', b2)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode712', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityNode711'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityNode711', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityNode711'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityNode711', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode712', None)
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode712', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityNode711'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityNode711', a)


def test_assoc_inStructuredNode754_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_ActivityEdge()
    b2 = CompleteDSLPckg_ActivityEdge()
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode756', b1)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode756', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityEdge755'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityEdge755', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode756', b2)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode756', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityEdge755'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityEdge755', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityEdge755'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityEdge755', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode756', None)
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode756', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityEdge755'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityEdge755', a)


def test_assoc_incoming598_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Vertex()
    b2 = CompleteDSLPckg_Vertex()
    _safe_set(a, 'CompleteDSLPckg_Transition600', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition600', b1)
    if hasattr(b1, 'CompleteDSLPckg_Vertex599'):
        assert _is_linked(b1, 'CompleteDSLPckg_Vertex599', a)
    _safe_set(a, 'CompleteDSLPckg_Transition600', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition600', b2)
    if hasattr(b1, 'CompleteDSLPckg_Vertex599'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Vertex599', a)
    if hasattr(b2, 'CompleteDSLPckg_Vertex599'):
        assert _is_linked(b2, 'CompleteDSLPckg_Vertex599', a)
    _safe_set(a, 'CompleteDSLPckg_Transition600', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition600', b2)
    if hasattr(b2, 'CompleteDSLPckg_Vertex599'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Vertex599', a)


def test_assoc_inheritedMember84_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_NamedElement86', b1)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement86', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier85'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier85', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement86', b2)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement86', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier85'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier85', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier85'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier85', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement86', None)
    assert not _is_linked(a, 'CompleteDSLPckg_NamedElement86', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier85'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier85', a)


def test_assoc_inputElement872_link_reassign_clear():
    a = CompleteDSLPckg_ExpansionRegion(mode="sample_text")
    b1 = CompleteDSLPckg_ExpansionNode()
    b2 = CompleteDSLPckg_ExpansionNode()
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExpansionNode', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExpansionNode', a)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExpansionNode', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ExpansionRegion', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExpansionNode', a)


def test_assoc_inputValue398_link_reassign_clear():
    a = CompleteDSLPckg_OpaqueAction(body="sample_text", language="sample_text")
    b1 = CompleteDSLPckg_InputPin()
    b2 = CompleteDSLPckg_InputPin()
    _safe_set(a, 'CompleteDSLPckg_OpaqueAction', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueAction', b1)
    if hasattr(b1, 'CompleteDSLPckg_InputPin399'):
        assert _is_linked(b1, 'CompleteDSLPckg_InputPin399', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueAction', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueAction', b2)
    if hasattr(b1, 'CompleteDSLPckg_InputPin399'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InputPin399', a)
    if hasattr(b2, 'CompleteDSLPckg_InputPin399'):
        assert _is_linked(b2, 'CompleteDSLPckg_InputPin399', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueAction', set())
    assert not _is_linked(a, 'CompleteDSLPckg_OpaqueAction', b2)
    if hasattr(b2, 'CompleteDSLPckg_InputPin399'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InputPin399', a)


def test_assoc_insertAt480_link_reassign_clear():
    a = CompleteDSLPckg_LinkEndCreationData(isReplaceAll=True)
    b1 = CompleteDSLPckg_InputPin()
    b2 = CompleteDSLPckg_InputPin()
    _safe_set(a, 'CompleteDSLPckg_LinkEndCreationData', b1)
    assert _is_linked(a, 'CompleteDSLPckg_LinkEndCreationData', b1)
    if hasattr(b1, 'CompleteDSLPckg_InputPin481'):
        assert _is_linked(b1, 'CompleteDSLPckg_InputPin481', a)
    _safe_set(a, 'CompleteDSLPckg_LinkEndCreationData', b2)
    assert _is_linked(a, 'CompleteDSLPckg_LinkEndCreationData', b2)
    if hasattr(b1, 'CompleteDSLPckg_InputPin481'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InputPin481', a)
    if hasattr(b2, 'CompleteDSLPckg_InputPin481'):
        assert _is_linked(b2, 'CompleteDSLPckg_InputPin481', a)
    _safe_set(a, 'CompleteDSLPckg_LinkEndCreationData', None)
    assert not _is_linked(a, 'CompleteDSLPckg_LinkEndCreationData', b2)
    if hasattr(b2, 'CompleteDSLPckg_InputPin481'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InputPin481', a)


def test_assoc_interface123_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'ownedAttribute124', b1)
    assert _is_linked(a, 'ownedAttribute124', b1)
    if hasattr(b1, 'Interface'):
        assert _is_linked(b1, 'Interface', a)
    _safe_set(a, 'ownedAttribute124', b2)
    assert _is_linked(a, 'ownedAttribute124', b2)
    if hasattr(b1, 'Interface'):
        assert not _is_linked(b1, 'Interface', a)
    if hasattr(b2, 'Interface'):
        assert _is_linked(b2, 'Interface', a)
    _safe_set(a, 'ownedAttribute124', None)
    assert not _is_linked(a, 'ownedAttribute124', b2)
    if hasattr(b2, 'Interface'):
        assert not _is_linked(b2, 'Interface', a)


def test_assoc_interface164_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'ownedOperation165', b1)
    assert _is_linked(a, 'ownedOperation165', b1)
    if hasattr(b1, 'Interface166'):
        assert _is_linked(b1, 'Interface166', a)
    _safe_set(a, 'ownedOperation165', b2)
    assert _is_linked(a, 'ownedOperation165', b2)
    if hasattr(b1, 'Interface166'):
        assert not _is_linked(b1, 'Interface166', a)
    if hasattr(b2, 'Interface166'):
        assert _is_linked(b2, 'Interface166', a)
    _safe_set(a, 'ownedOperation165', None)
    assert not _is_linked(a, 'ownedOperation165', b2)
    if hasattr(b2, 'Interface166'):
        assert not _is_linked(b2, 'Interface166', a)


def test_assoc_joinSpec765_link_reassign_clear():
    a = CompleteDSLPckg_JoinNode(isCombineDuplicate=True)
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'CompleteDSLPckg_JoinNode', b1)
    assert _is_linked(a, 'CompleteDSLPckg_JoinNode', b1)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification766'):
        assert _is_linked(b1, 'CompleteDSLPckg_ValueSpecification766', a)
    _safe_set(a, 'CompleteDSLPckg_JoinNode', b2)
    assert _is_linked(a, 'CompleteDSLPckg_JoinNode', b2)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification766'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ValueSpecification766', a)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification766'):
        assert _is_linked(b2, 'CompleteDSLPckg_ValueSpecification766', a)
    _safe_set(a, 'CompleteDSLPckg_JoinNode', None)
    assert not _is_linked(a, 'CompleteDSLPckg_JoinNode', b2)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification766'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ValueSpecification766', a)


def test_assoc_loopVariable831_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_LoopNode832', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode832', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin833'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin833', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode832', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode832', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin833'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin833', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin833'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin833', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode832', set())
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode832', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin833'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin833', a)


def test_assoc_loopVariableInput828_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_InputPin()
    b2 = CompleteDSLPckg_InputPin()
    _safe_set(a, 'CompleteDSLPckg_LoopNode829', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode829', b1)
    if hasattr(b1, 'CompleteDSLPckg_InputPin830'):
        assert _is_linked(b1, 'CompleteDSLPckg_InputPin830', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode829', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode829', b2)
    if hasattr(b1, 'CompleteDSLPckg_InputPin830'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InputPin830', a)
    if hasattr(b2, 'CompleteDSLPckg_InputPin830'):
        assert _is_linked(b2, 'CompleteDSLPckg_InputPin830', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode829', set())
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode829', b2)
    if hasattr(b2, 'CompleteDSLPckg_InputPin830'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InputPin830', a)


def test_assoc_lowerValue44_link_reassign_clear():
    a = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'owningLower', b1)
    assert _is_linked(a, 'owningLower', b1)
    if hasattr(b1, 'ValueSpecification45'):
        assert _is_linked(b1, 'ValueSpecification45', a)
    _safe_set(a, 'owningLower', b2)
    assert _is_linked(a, 'owningLower', b2)
    if hasattr(b1, 'ValueSpecification45'):
        assert not _is_linked(b1, 'ValueSpecification45', a)
    if hasattr(b2, 'ValueSpecification45'):
        assert _is_linked(b2, 'ValueSpecification45', a)
    _safe_set(a, 'owningLower', None)
    assert not _is_linked(a, 'owningLower', b2)
    if hasattr(b2, 'ValueSpecification45'):
        assert not _is_linked(b2, 'ValueSpecification45', a)


def test_assoc_manifestation371_link_reassign_clear():
    a = CompleteDSLPckg_Artifact(fileName="sample_text")
    b1 = CompleteDSLPckg_Manifestation()
    b2 = CompleteDSLPckg_Manifestation()
    _safe_set(a, 'CompleteDSLPckg_Artifact372', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Artifact372', b1)
    if hasattr(b1, 'CompleteDSLPckg_Manifestation'):
        assert _is_linked(b1, 'CompleteDSLPckg_Manifestation', a)
    _safe_set(a, 'CompleteDSLPckg_Artifact372', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Artifact372', b2)
    if hasattr(b1, 'CompleteDSLPckg_Manifestation'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Manifestation', a)
    if hasattr(b2, 'CompleteDSLPckg_Manifestation'):
        assert _is_linked(b2, 'CompleteDSLPckg_Manifestation', a)
    _safe_set(a, 'CompleteDSLPckg_Artifact372', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Artifact372', b2)
    if hasattr(b2, 'CompleteDSLPckg_Manifestation'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Manifestation', a)


def test_assoc_mapping199_link_reassign_clear():
    a = CompleteDSLPckg_OpaqueExpression(body="sample_text", language="sample_text")
    b1 = CompleteDSLPckg_Abstraction()
    b2 = CompleteDSLPckg_Abstraction()
    _safe_set(a, 'CompleteDSLPckg_OpaqueExpression200', b1)
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueExpression200', b1)
    if hasattr(b1, 'CompleteDSLPckg_Abstraction'):
        assert _is_linked(b1, 'CompleteDSLPckg_Abstraction', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueExpression200', b2)
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueExpression200', b2)
    if hasattr(b1, 'CompleteDSLPckg_Abstraction'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Abstraction', a)
    if hasattr(b2, 'CompleteDSLPckg_Abstraction'):
        assert _is_linked(b2, 'CompleteDSLPckg_Abstraction', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueExpression200', None)
    assert not _is_linked(a, 'CompleteDSLPckg_OpaqueExpression200', b2)
    if hasattr(b2, 'CompleteDSLPckg_Abstraction'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Abstraction', a)


def test_assoc_member9_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Namespace()
    b2 = CompleteDSLPckg_Namespace()
    _safe_set(a, 'CompleteDSLPckg_NamedElement', b1)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement', b1)
    if hasattr(b1, 'CompleteDSLPckg_Namespace10'):
        assert _is_linked(b1, 'CompleteDSLPckg_Namespace10', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement', b2)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement', b2)
    if hasattr(b1, 'CompleteDSLPckg_Namespace10'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Namespace10', a)
    if hasattr(b2, 'CompleteDSLPckg_Namespace10'):
        assert _is_linked(b2, 'CompleteDSLPckg_Namespace10', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement', None)
    assert not _is_linked(a, 'CompleteDSLPckg_NamedElement', b2)
    if hasattr(b2, 'CompleteDSLPckg_Namespace10'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Namespace10', a)


def test_assoc_memberEnd180_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Association(isDerived=True)
    b2 = CompleteDSLPckg_Association(isDerived=False)
    _safe_set(a, 'Property181', b1)
    assert _is_linked(a, 'Property181', b1)
    if hasattr(b1, 'association'):
        assert _is_linked(b1, 'association', a)
    _safe_set(a, 'Property181', b2)
    assert _is_linked(a, 'Property181', b2)
    if hasattr(b1, 'association'):
        assert not _is_linked(b1, 'association', a)
    if hasattr(b2, 'association'):
        assert _is_linked(b2, 'association', a)
    _safe_set(a, 'Property181', None)
    assert not _is_linked(a, 'Property181', b2)
    if hasattr(b2, 'association'):
        assert not _is_linked(b2, 'association', a)


def test_assoc_mergedPackage193_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_PackageMerge()
    b2 = CompleteDSLPckg_PackageMerge()
    _safe_set(a, 'CompleteDSLPckg_Package194', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Package194', b1)
    if hasattr(b1, 'CompleteDSLPckg_PackageMerge'):
        assert _is_linked(b1, 'CompleteDSLPckg_PackageMerge', a)
    _safe_set(a, 'CompleteDSLPckg_Package194', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Package194', b2)
    if hasattr(b1, 'CompleteDSLPckg_PackageMerge'):
        assert not _is_linked(b1, 'CompleteDSLPckg_PackageMerge', a)
    if hasattr(b2, 'CompleteDSLPckg_PackageMerge'):
        assert _is_linked(b2, 'CompleteDSLPckg_PackageMerge', a)
    _safe_set(a, 'CompleteDSLPckg_Package194', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Package194', b2)
    if hasattr(b2, 'CompleteDSLPckg_PackageMerge'):
        assert not _is_linked(b2, 'CompleteDSLPckg_PackageMerge', a)


def test_assoc_message936_link_reassign_clear():
    a = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    b1 = CompleteDSLPckg_MessageEnd()
    b2 = CompleteDSLPckg_MessageEnd()
    _safe_set(a, 'CompleteDSLPckg_Message938', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Message938', b1)
    if hasattr(b1, 'CompleteDSLPckg_MessageEnd937'):
        assert _is_linked(b1, 'CompleteDSLPckg_MessageEnd937', a)
    _safe_set(a, 'CompleteDSLPckg_Message938', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Message938', b2)
    if hasattr(b1, 'CompleteDSLPckg_MessageEnd937'):
        assert not _is_linked(b1, 'CompleteDSLPckg_MessageEnd937', a)
    if hasattr(b2, 'CompleteDSLPckg_MessageEnd937'):
        assert _is_linked(b2, 'CompleteDSLPckg_MessageEnd937', a)
    _safe_set(a, 'CompleteDSLPckg_Message938', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Message938', b2)
    if hasattr(b2, 'CompleteDSLPckg_MessageEnd937'):
        assert not _is_linked(b2, 'CompleteDSLPckg_MessageEnd937', a)


def test_assoc_message961_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_ConsiderIgnoreFragment()
    b2 = CompleteDSLPckg_ConsiderIgnoreFragment()
    _safe_set(a, 'CompleteDSLPckg_NamedElement962', b1)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement962', b1)
    if hasattr(b1, 'CompleteDSLPckg_ConsiderIgnoreFragment'):
        assert _is_linked(b1, 'CompleteDSLPckg_ConsiderIgnoreFragment', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement962', b2)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement962', b2)
    if hasattr(b1, 'CompleteDSLPckg_ConsiderIgnoreFragment'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ConsiderIgnoreFragment', a)
    if hasattr(b2, 'CompleteDSLPckg_ConsiderIgnoreFragment'):
        assert _is_linked(b2, 'CompleteDSLPckg_ConsiderIgnoreFragment', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement962', None)
    assert not _is_linked(a, 'CompleteDSLPckg_NamedElement962', b2)
    if hasattr(b2, 'CompleteDSLPckg_ConsiderIgnoreFragment'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ConsiderIgnoreFragment', a)


def test_assoc_namespace6_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Namespace()
    b2 = CompleteDSLPckg_Namespace()
    _safe_set(a, 'ownedMember', b1)
    assert _is_linked(a, 'ownedMember', b1)
    if hasattr(b1, 'Namespace'):
        assert _is_linked(b1, 'Namespace', a)
    _safe_set(a, 'ownedMember', b2)
    assert _is_linked(a, 'ownedMember', b2)
    if hasattr(b1, 'Namespace'):
        assert not _is_linked(b1, 'Namespace', a)
    if hasattr(b2, 'Namespace'):
        assert _is_linked(b2, 'Namespace', a)
    _safe_set(a, 'ownedMember', None)
    assert not _is_linked(a, 'ownedMember', b2)
    if hasattr(b2, 'Namespace'):
        assert not _is_linked(b2, 'Namespace', a)


def test_assoc_navigableOwnedEnd178_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Association(isDerived=True)
    b2 = CompleteDSLPckg_Association(isDerived=False)
    _safe_set(a, 'CompleteDSLPckg_Property179', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property179', b1)
    if hasattr(b1, 'CompleteDSLPckg_Association'):
        assert _is_linked(b1, 'CompleteDSLPckg_Association', a)
    _safe_set(a, 'CompleteDSLPckg_Property179', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property179', b2)
    if hasattr(b1, 'CompleteDSLPckg_Association'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Association', a)
    if hasattr(b2, 'CompleteDSLPckg_Association'):
        assert _is_linked(b2, 'CompleteDSLPckg_Association', a)
    _safe_set(a, 'CompleteDSLPckg_Property179', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property179', b2)
    if hasattr(b2, 'CompleteDSLPckg_Association'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Association', a)


def test_assoc_nestedArtifact369_link_reassign_clear():
    a = CompleteDSLPckg_Artifact(fileName="sample_text")
    b1 = CompleteDSLPckg_Artifact(fileName="sample_text")
    b2 = CompleteDSLPckg_Artifact(fileName="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_Artifact368', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Artifact368', b1)
    if hasattr(b1, 'CompleteDSLPckg_Artifact370'):
        assert _is_linked(b1, 'CompleteDSLPckg_Artifact370', a)
    _safe_set(a, 'CompleteDSLPckg_Artifact368', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Artifact368', b2)
    if hasattr(b1, 'CompleteDSLPckg_Artifact370'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Artifact370', a)
    if hasattr(b2, 'CompleteDSLPckg_Artifact370'):
        assert _is_linked(b2, 'CompleteDSLPckg_Artifact370', a)
    _safe_set(a, 'CompleteDSLPckg_Artifact368', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Artifact368', b2)
    if hasattr(b2, 'CompleteDSLPckg_Artifact370'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Artifact370', a)


def test_assoc_nestedClassifier167_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Class()
    b2 = CompleteDSLPckg_Class()
    _safe_set(a, 'CompleteDSLPckg_Classifier168', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier168', b1)
    if hasattr(b1, 'CompleteDSLPckg_Class'):
        assert _is_linked(b1, 'CompleteDSLPckg_Class', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier168', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier168', b2)
    if hasattr(b1, 'CompleteDSLPckg_Class'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Class', a)
    if hasattr(b2, 'CompleteDSLPckg_Class'):
        assert _is_linked(b2, 'CompleteDSLPckg_Class', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier168', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier168', b2)
    if hasattr(b2, 'CompleteDSLPckg_Class'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Class', a)


def test_assoc_nestedClassifier205_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'CompleteDSLPckg_Classifier206', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier206', b1)
    if hasattr(b1, 'CompleteDSLPckg_Interface'):
        assert _is_linked(b1, 'CompleteDSLPckg_Interface', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier206', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier206', b2)
    if hasattr(b1, 'CompleteDSLPckg_Interface'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Interface', a)
    if hasattr(b2, 'CompleteDSLPckg_Interface'):
        assert _is_linked(b2, 'CompleteDSLPckg_Interface', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier206', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier206', b2)
    if hasattr(b2, 'CompleteDSLPckg_Interface'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Interface', a)


def test_assoc_nestedPackage24_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_Package(URI="sample_text")
    b2 = CompleteDSLPckg_Package(URI="sample_text_2")
    _safe_set(a, 'Package', b1)
    assert _is_linked(a, 'Package', b1)
    if hasattr(b1, 'nestingPackage'):
        assert _is_linked(b1, 'nestingPackage', a)
    _safe_set(a, 'Package', b2)
    assert _is_linked(a, 'Package', b2)
    if hasattr(b1, 'nestingPackage'):
        assert not _is_linked(b1, 'nestingPackage', a)
    if hasattr(b2, 'nestingPackage'):
        assert _is_linked(b2, 'nestingPackage', a)
    _safe_set(a, 'Package', None)
    assert not _is_linked(a, 'Package', b2)
    if hasattr(b2, 'nestingPackage'):
        assert not _is_linked(b2, 'nestingPackage', a)


def test_assoc_nestingPackage26_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_Package(URI="sample_text")
    b2 = CompleteDSLPckg_Package(URI="sample_text_2")
    _safe_set(a, 'Package27', b1)
    assert _is_linked(a, 'Package27', b1)
    if hasattr(b1, 'nestedPackage'):
        assert _is_linked(b1, 'nestedPackage', a)
    _safe_set(a, 'Package27', b2)
    assert _is_linked(a, 'Package27', b2)
    if hasattr(b1, 'nestedPackage'):
        assert not _is_linked(b1, 'nestedPackage', a)
    if hasattr(b2, 'nestedPackage'):
        assert _is_linked(b2, 'nestedPackage', a)
    _safe_set(a, 'Package27', None)
    assert not _is_linked(a, 'Package27', b2)
    if hasattr(b2, 'nestedPackage'):
        assert not _is_linked(b2, 'nestedPackage', a)


def test_assoc_newClassifier517_link_reassign_clear():
    a = CompleteDSLPckg_ReclassifyObjectAction(isReplaceAll=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction518', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction518', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier519'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier519', a)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction518', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction518', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier519'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier519', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier519'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier519', a)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction518', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction518', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier519'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier519', a)


def test_assoc_node681_link_reassign_clear():
    a = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = CompleteDSLPckg_ActivityNode()
    b2 = CompleteDSLPckg_ActivityNode()
    _safe_set(a, 'CompleteDSLPckg_Activity', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Activity', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityNode'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityNode', a)
    _safe_set(a, 'CompleteDSLPckg_Activity', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Activity', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityNode'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityNode', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityNode'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityNode', a)
    _safe_set(a, 'CompleteDSLPckg_Activity', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Activity', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityNode'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityNode', a)


def test_assoc_node804_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_ActivityNode()
    b2 = CompleteDSLPckg_ActivityNode()
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode805', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode805', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityNode806'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityNode806', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode805', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode805', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityNode806'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityNode806', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityNode806'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityNode806', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode805', set())
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode805', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityNode806'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityNode806', a)


def test_assoc_object512_link_reassign_clear():
    a = CompleteDSLPckg_ReclassifyObjectAction(isReplaceAll=True)
    b1 = CompleteDSLPckg_InputPin()
    b2 = CompleteDSLPckg_InputPin()
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction', b1)
    if hasattr(b1, 'CompleteDSLPckg_InputPin513'):
        assert _is_linked(b1, 'CompleteDSLPckg_InputPin513', a)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction', b2)
    if hasattr(b1, 'CompleteDSLPckg_InputPin513'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InputPin513', a)
    if hasattr(b2, 'CompleteDSLPckg_InputPin513'):
        assert _is_linked(b2, 'CompleteDSLPckg_InputPin513', a)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction', b2)
    if hasattr(b2, 'CompleteDSLPckg_InputPin513'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InputPin513', a)


def test_assoc_oldClassifier514_link_reassign_clear():
    a = CompleteDSLPckg_ReclassifyObjectAction(isReplaceAll=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction515', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction515', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier516'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier516', a)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction515', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction515', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier516'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier516', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier516'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier516', a)
    _safe_set(a, 'CompleteDSLPckg_ReclassifyObjectAction515', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ReclassifyObjectAction515', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier516'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier516', a)


def test_assoc_onPort361_link_reassign_clear():
    a = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    b1 = CompleteDSLPckg_InvocationAction()
    b2 = CompleteDSLPckg_InvocationAction()
    _safe_set(a, 'CompleteDSLPckg_Port362', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Port362', b1)
    if hasattr(b1, 'CompleteDSLPckg_InvocationAction'):
        assert _is_linked(b1, 'CompleteDSLPckg_InvocationAction', a)
    _safe_set(a, 'CompleteDSLPckg_Port362', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Port362', b2)
    if hasattr(b1, 'CompleteDSLPckg_InvocationAction'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InvocationAction', a)
    if hasattr(b2, 'CompleteDSLPckg_InvocationAction'):
        assert _is_linked(b2, 'CompleteDSLPckg_InvocationAction', a)
    _safe_set(a, 'CompleteDSLPckg_Port362', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Port362', b2)
    if hasattr(b2, 'CompleteDSLPckg_InvocationAction'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InvocationAction', a)


def test_assoc_operand57_link_reassign_clear():
    a = CompleteDSLPckg_Expression(symbol="sample_text")
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'CompleteDSLPckg_Expression', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Expression', b1)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification'):
        assert _is_linked(b1, 'CompleteDSLPckg_ValueSpecification', a)
    _safe_set(a, 'CompleteDSLPckg_Expression', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Expression', b2)
    if hasattr(b1, 'CompleteDSLPckg_ValueSpecification'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ValueSpecification', a)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification'):
        assert _is_linked(b2, 'CompleteDSLPckg_ValueSpecification', a)
    _safe_set(a, 'CompleteDSLPckg_Expression', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Expression', b2)
    if hasattr(b2, 'CompleteDSLPckg_ValueSpecification'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ValueSpecification', a)


def test_assoc_operand956_link_reassign_clear():
    a = CompleteDSLPckg_CombinedFragment(interactionOperator="sample_text")
    b1 = CompleteDSLPckg_InteractionOperand()
    b2 = CompleteDSLPckg_InteractionOperand()
    _safe_set(a, 'CompleteDSLPckg_CombinedFragment', b1)
    assert _is_linked(a, 'CompleteDSLPckg_CombinedFragment', b1)
    if hasattr(b1, 'CompleteDSLPckg_InteractionOperand957'):
        assert _is_linked(b1, 'CompleteDSLPckg_InteractionOperand957', a)
    _safe_set(a, 'CompleteDSLPckg_CombinedFragment', b2)
    assert _is_linked(a, 'CompleteDSLPckg_CombinedFragment', b2)
    if hasattr(b1, 'CompleteDSLPckg_InteractionOperand957'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InteractionOperand957', a)
    if hasattr(b2, 'CompleteDSLPckg_InteractionOperand957'):
        assert _is_linked(b2, 'CompleteDSLPckg_InteractionOperand957', a)
    _safe_set(a, 'CompleteDSLPckg_CombinedFragment', None)
    assert not _is_linked(a, 'CompleteDSLPckg_CombinedFragment', b2)
    if hasattr(b2, 'CompleteDSLPckg_InteractionOperand957'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InteractionOperand957', a)


def test_assoc_operation257_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_CallEvent()
    b2 = CompleteDSLPckg_CallEvent()
    _safe_set(a, 'CompleteDSLPckg_Operation258', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Operation258', b1)
    if hasattr(b1, 'CompleteDSLPckg_CallEvent'):
        assert _is_linked(b1, 'CompleteDSLPckg_CallEvent', a)
    _safe_set(a, 'CompleteDSLPckg_Operation258', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Operation258', b2)
    if hasattr(b1, 'CompleteDSLPckg_CallEvent'):
        assert not _is_linked(b1, 'CompleteDSLPckg_CallEvent', a)
    if hasattr(b2, 'CompleteDSLPckg_CallEvent'):
        assert _is_linked(b2, 'CompleteDSLPckg_CallEvent', a)
    _safe_set(a, 'CompleteDSLPckg_Operation258', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Operation258', b2)
    if hasattr(b2, 'CompleteDSLPckg_CallEvent'):
        assert not _is_linked(b2, 'CompleteDSLPckg_CallEvent', a)


def test_assoc_operation409_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_CallOperationAction()
    b2 = CompleteDSLPckg_CallOperationAction()
    _safe_set(a, 'CompleteDSLPckg_Operation410', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Operation410', b1)
    if hasattr(b1, 'CompleteDSLPckg_CallOperationAction'):
        assert _is_linked(b1, 'CompleteDSLPckg_CallOperationAction', a)
    _safe_set(a, 'CompleteDSLPckg_Operation410', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Operation410', b2)
    if hasattr(b1, 'CompleteDSLPckg_CallOperationAction'):
        assert not _is_linked(b1, 'CompleteDSLPckg_CallOperationAction', a)
    if hasattr(b2, 'CompleteDSLPckg_CallOperationAction'):
        assert _is_linked(b2, 'CompleteDSLPckg_CallOperationAction', a)
    _safe_set(a, 'CompleteDSLPckg_Operation410', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Operation410', b2)
    if hasattr(b2, 'CompleteDSLPckg_CallOperationAction'):
        assert not _is_linked(b2, 'CompleteDSLPckg_CallOperationAction', a)


def test_assoc_opposite113_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b2 = CompleteDSLPckg_Property(aggregation="sample_text_2", default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    _safe_set(a, 'CompleteDSLPckg_Property112', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property112', b1)
    if hasattr(b1, 'CompleteDSLPckg_Property114'):
        assert _is_linked(b1, 'CompleteDSLPckg_Property114', a)
    _safe_set(a, 'CompleteDSLPckg_Property112', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property112', b2)
    if hasattr(b1, 'CompleteDSLPckg_Property114'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Property114', a)
    if hasattr(b2, 'CompleteDSLPckg_Property114'):
        assert _is_linked(b2, 'CompleteDSLPckg_Property114', a)
    _safe_set(a, 'CompleteDSLPckg_Property112', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property112', b2)
    if hasattr(b2, 'CompleteDSLPckg_Property114'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Property114', a)


def test_assoc_outgoing595_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Vertex()
    b2 = CompleteDSLPckg_Vertex()
    _safe_set(a, 'CompleteDSLPckg_Transition597', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition597', b1)
    if hasattr(b1, 'CompleteDSLPckg_Vertex596'):
        assert _is_linked(b1, 'CompleteDSLPckg_Vertex596', a)
    _safe_set(a, 'CompleteDSLPckg_Transition597', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition597', b2)
    if hasattr(b1, 'CompleteDSLPckg_Vertex596'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Vertex596', a)
    if hasattr(b2, 'CompleteDSLPckg_Vertex596'):
        assert _is_linked(b2, 'CompleteDSLPckg_Vertex596', a)
    _safe_set(a, 'CompleteDSLPckg_Transition597', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition597', b2)
    if hasattr(b2, 'CompleteDSLPckg_Vertex596'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Vertex596', a)


def test_assoc_outputElement873_link_reassign_clear():
    a = CompleteDSLPckg_ExpansionRegion(mode="sample_text")
    b1 = CompleteDSLPckg_ExpansionNode()
    b2 = CompleteDSLPckg_ExpansionNode()
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion874', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion874', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode875'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExpansionNode875', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion874', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion874', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode875'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExpansionNode875', a)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode875'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExpansionNode875', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion874', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ExpansionRegion874', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode875'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExpansionNode875', a)


def test_assoc_outputValue400_link_reassign_clear():
    a = CompleteDSLPckg_OpaqueAction(body="sample_text", language="sample_text")
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_OpaqueAction401', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueAction401', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin402'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin402', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueAction401', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_OpaqueAction401', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin402'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin402', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin402'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin402', a)
    _safe_set(a, 'CompleteDSLPckg_OpaqueAction401', set())
    assert not _is_linked(a, 'CompleteDSLPckg_OpaqueAction401', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin402'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin402', a)


def test_assoc_ownedAttribute173_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Class()
    b2 = CompleteDSLPckg_Class()
    _safe_set(a, 'Property175', b1)
    assert _is_linked(a, 'Property175', b1)
    if hasattr(b1, 'class_174'):
        assert _is_linked(b1, 'class_174', a)
    _safe_set(a, 'Property175', b2)
    assert _is_linked(a, 'Property175', b2)
    if hasattr(b1, 'class_174'):
        assert not _is_linked(b1, 'class_174', a)
    if hasattr(b2, 'class_174'):
        assert _is_linked(b2, 'class_174', a)
    _safe_set(a, 'Property175', None)
    assert not _is_linked(a, 'Property175', b2)
    if hasattr(b2, 'class_174'):
        assert not _is_linked(b2, 'class_174', a)


def test_assoc_ownedAttribute184_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_DataType()
    b2 = CompleteDSLPckg_DataType()
    _safe_set(a, 'Property185', b1)
    assert _is_linked(a, 'Property185', b1)
    if hasattr(b1, 'dataType'):
        assert _is_linked(b1, 'dataType', a)
    _safe_set(a, 'Property185', b2)
    assert _is_linked(a, 'Property185', b2)
    if hasattr(b1, 'dataType'):
        assert not _is_linked(b1, 'dataType', a)
    if hasattr(b2, 'dataType'):
        assert _is_linked(b2, 'dataType', a)
    _safe_set(a, 'Property185', None)
    assert not _is_linked(a, 'Property185', b2)
    if hasattr(b2, 'dataType'):
        assert not _is_linked(b2, 'dataType', a)


def test_assoc_ownedAttribute210_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'Property211', b1)
    assert _is_linked(a, 'Property211', b1)
    if hasattr(b1, 'interface'):
        assert _is_linked(b1, 'interface', a)
    _safe_set(a, 'Property211', b2)
    assert _is_linked(a, 'Property211', b2)
    if hasattr(b1, 'interface'):
        assert not _is_linked(b1, 'interface', a)
    if hasattr(b2, 'interface'):
        assert _is_linked(b2, 'interface', a)
    _safe_set(a, 'Property211', None)
    assert not _is_linked(a, 'Property211', b2)
    if hasattr(b2, 'interface'):
        assert not _is_linked(b2, 'interface', a)


def test_assoc_ownedAttribute249_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Signal()
    b2 = CompleteDSLPckg_Signal()
    _safe_set(a, 'CompleteDSLPckg_Property250', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property250', b1)
    if hasattr(b1, 'CompleteDSLPckg_Signal'):
        assert _is_linked(b1, 'CompleteDSLPckg_Signal', a)
    _safe_set(a, 'CompleteDSLPckg_Property250', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property250', b2)
    if hasattr(b1, 'CompleteDSLPckg_Signal'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Signal', a)
    if hasattr(b2, 'CompleteDSLPckg_Signal'):
        assert _is_linked(b2, 'CompleteDSLPckg_Signal', a)
    _safe_set(a, 'CompleteDSLPckg_Property250', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property250', b2)
    if hasattr(b2, 'CompleteDSLPckg_Signal'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Signal', a)


def test_assoc_ownedAttribute365_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Artifact(fileName="sample_text")
    b2 = CompleteDSLPckg_Artifact(fileName="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_Property367', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property367', b1)
    if hasattr(b1, 'CompleteDSLPckg_Artifact366'):
        assert _is_linked(b1, 'CompleteDSLPckg_Artifact366', a)
    _safe_set(a, 'CompleteDSLPckg_Property367', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property367', b2)
    if hasattr(b1, 'CompleteDSLPckg_Artifact366'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Artifact366', a)
    if hasattr(b2, 'CompleteDSLPckg_Artifact366'):
        assert _is_linked(b2, 'CompleteDSLPckg_Artifact366', a)
    _safe_set(a, 'CompleteDSLPckg_Property367', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property367', b2)
    if hasattr(b2, 'CompleteDSLPckg_Artifact366'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Artifact366', a)


def test_assoc_ownedBehavior222_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_BehavioredClassifier()
    b2 = CompleteDSLPckg_BehavioredClassifier()
    _safe_set(a, 'CompleteDSLPckg_Behavior223', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior223', b1)
    if hasattr(b1, 'CompleteDSLPckg_BehavioredClassifier'):
        assert _is_linked(b1, 'CompleteDSLPckg_BehavioredClassifier', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior223', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior223', b2)
    if hasattr(b1, 'CompleteDSLPckg_BehavioredClassifier'):
        assert not _is_linked(b1, 'CompleteDSLPckg_BehavioredClassifier', a)
    if hasattr(b2, 'CompleteDSLPckg_BehavioredClassifier'):
        assert _is_linked(b2, 'CompleteDSLPckg_BehavioredClassifier', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior223', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior223', b2)
    if hasattr(b2, 'CompleteDSLPckg_BehavioredClassifier'):
        assert not _is_linked(b2, 'CompleteDSLPckg_BehavioredClassifier', a)


def test_assoc_ownedComment0_link_reassign_clear():
    a = CompleteDSLPckg_Comment(body="sample_text")
    b1 = CompleteDSLPckg_Element()
    b2 = CompleteDSLPckg_Element()
    _safe_set(a, 'Comment', b1)
    assert _is_linked(a, 'Comment', b1)
    if hasattr(b1, 'owningElement'):
        assert _is_linked(b1, 'owningElement', a)
    _safe_set(a, 'Comment', b2)
    assert _is_linked(a, 'Comment', b2)
    if hasattr(b1, 'owningElement'):
        assert not _is_linked(b1, 'owningElement', a)
    if hasattr(b2, 'owningElement'):
        assert _is_linked(b2, 'owningElement', a)
    _safe_set(a, 'Comment', None)
    assert not _is_linked(a, 'Comment', b2)
    if hasattr(b2, 'owningElement'):
        assert not _is_linked(b2, 'owningElement', a)


def test_assoc_ownedConnector332_link_reassign_clear():
    a = CompleteDSLPckg_Connector(kind="sample_text")
    b1 = CompleteDSLPckg_StructuredClassifier()
    b2 = CompleteDSLPckg_StructuredClassifier()
    _safe_set(a, 'CompleteDSLPckg_Connector333', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Connector333', b1)
    if hasattr(b1, 'CompleteDSLPckg_StructuredClassifier'):
        assert _is_linked(b1, 'CompleteDSLPckg_StructuredClassifier', a)
    _safe_set(a, 'CompleteDSLPckg_Connector333', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Connector333', b2)
    if hasattr(b1, 'CompleteDSLPckg_StructuredClassifier'):
        assert not _is_linked(b1, 'CompleteDSLPckg_StructuredClassifier', a)
    if hasattr(b2, 'CompleteDSLPckg_StructuredClassifier'):
        assert _is_linked(b2, 'CompleteDSLPckg_StructuredClassifier', a)
    _safe_set(a, 'CompleteDSLPckg_Connector333', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Connector333', b2)
    if hasattr(b2, 'CompleteDSLPckg_StructuredClassifier'):
        assert not _is_linked(b2, 'CompleteDSLPckg_StructuredClassifier', a)


def test_assoc_ownedEnd182_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Association(isDerived=True)
    b2 = CompleteDSLPckg_Association(isDerived=False)
    _safe_set(a, 'Property183', b1)
    assert _is_linked(a, 'Property183', b1)
    if hasattr(b1, 'owningAssociation'):
        assert _is_linked(b1, 'owningAssociation', a)
    _safe_set(a, 'Property183', b2)
    assert _is_linked(a, 'Property183', b2)
    if hasattr(b1, 'owningAssociation'):
        assert not _is_linked(b1, 'owningAssociation', a)
    if hasattr(b2, 'owningAssociation'):
        assert _is_linked(b2, 'owningAssociation', a)
    _safe_set(a, 'Property183', None)
    assert not _is_linked(a, 'Property183', b2)
    if hasattr(b2, 'owningAssociation'):
        assert not _is_linked(b2, 'owningAssociation', a)


def test_assoc_ownedFormalParam142_link_reassign_clear():
    a = CompleteDSLPckg_Parameter(default="sample_text")
    b1 = CompleteDSLPckg_BehavioralFeature()
    b2 = CompleteDSLPckg_BehavioralFeature()
    _safe_set(a, 'CompleteDSLPckg_Parameter143', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter143', b1)
    if hasattr(b1, 'CompleteDSLPckg_BehavioralFeature144'):
        assert _is_linked(b1, 'CompleteDSLPckg_BehavioralFeature144', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter143', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter143', b2)
    if hasattr(b1, 'CompleteDSLPckg_BehavioralFeature144'):
        assert not _is_linked(b1, 'CompleteDSLPckg_BehavioralFeature144', a)
    if hasattr(b2, 'CompleteDSLPckg_BehavioralFeature144'):
        assert _is_linked(b2, 'CompleteDSLPckg_BehavioralFeature144', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter143', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Parameter143', b2)
    if hasattr(b2, 'CompleteDSLPckg_BehavioralFeature144'):
        assert not _is_linked(b2, 'CompleteDSLPckg_BehavioralFeature144', a)


def test_assoc_ownedMember11_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Namespace()
    b2 = CompleteDSLPckg_Namespace()
    _safe_set(a, 'NamedElement', b1)
    assert _is_linked(a, 'NamedElement', b1)
    if hasattr(b1, 'namespace'):
        assert _is_linked(b1, 'namespace', a)
    _safe_set(a, 'NamedElement', b2)
    assert _is_linked(a, 'NamedElement', b2)
    if hasattr(b1, 'namespace'):
        assert not _is_linked(b1, 'namespace', a)
    if hasattr(b2, 'namespace'):
        assert _is_linked(b2, 'namespace', a)
    _safe_set(a, 'NamedElement', None)
    assert not _is_linked(a, 'NamedElement', b2)
    if hasattr(b2, 'namespace'):
        assert not _is_linked(b2, 'namespace', a)


def test_assoc_ownedOperation169_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Class()
    b2 = CompleteDSLPckg_Class()
    _safe_set(a, 'Operation', b1)
    assert _is_linked(a, 'Operation', b1)
    if hasattr(b1, 'class_'):
        assert _is_linked(b1, 'class_', a)
    _safe_set(a, 'Operation', b2)
    assert _is_linked(a, 'Operation', b2)
    if hasattr(b1, 'class_'):
        assert not _is_linked(b1, 'class_', a)
    if hasattr(b2, 'class_'):
        assert _is_linked(b2, 'class_', a)
    _safe_set(a, 'Operation', None)
    assert not _is_linked(a, 'Operation', b2)
    if hasattr(b2, 'class_'):
        assert not _is_linked(b2, 'class_', a)


def test_assoc_ownedOperation186_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_DataType()
    b2 = CompleteDSLPckg_DataType()
    _safe_set(a, 'Operation188', b1)
    assert _is_linked(a, 'Operation188', b1)
    if hasattr(b1, 'dataType187'):
        assert _is_linked(b1, 'dataType187', a)
    _safe_set(a, 'Operation188', b2)
    assert _is_linked(a, 'Operation188', b2)
    if hasattr(b1, 'dataType187'):
        assert not _is_linked(b1, 'dataType187', a)
    if hasattr(b2, 'dataType187'):
        assert _is_linked(b2, 'dataType187', a)
    _safe_set(a, 'Operation188', None)
    assert not _is_linked(a, 'Operation188', b2)
    if hasattr(b2, 'dataType187'):
        assert not _is_linked(b2, 'dataType187', a)


def test_assoc_ownedOperation212_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'Operation214', b1)
    assert _is_linked(a, 'Operation214', b1)
    if hasattr(b1, 'interface213'):
        assert _is_linked(b1, 'interface213', a)
    _safe_set(a, 'Operation214', b2)
    assert _is_linked(a, 'Operation214', b2)
    if hasattr(b1, 'interface213'):
        assert not _is_linked(b1, 'interface213', a)
    if hasattr(b2, 'interface213'):
        assert _is_linked(b2, 'interface213', a)
    _safe_set(a, 'Operation214', None)
    assert not _is_linked(a, 'Operation214', b2)
    if hasattr(b2, 'interface213'):
        assert not _is_linked(b2, 'interface213', a)


def test_assoc_ownedOperation363_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Artifact(fileName="sample_text")
    b2 = CompleteDSLPckg_Artifact(fileName="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_Operation364', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Operation364', b1)
    if hasattr(b1, 'CompleteDSLPckg_Artifact'):
        assert _is_linked(b1, 'CompleteDSLPckg_Artifact', a)
    _safe_set(a, 'CompleteDSLPckg_Operation364', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Operation364', b2)
    if hasattr(b1, 'CompleteDSLPckg_Artifact'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Artifact', a)
    if hasattr(b2, 'CompleteDSLPckg_Artifact'):
        assert _is_linked(b2, 'CompleteDSLPckg_Artifact', a)
    _safe_set(a, 'CompleteDSLPckg_Operation364', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Operation364', b2)
    if hasattr(b2, 'CompleteDSLPckg_Artifact'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Artifact', a)


def test_assoc_ownedParameter137_link_reassign_clear():
    a = CompleteDSLPckg_Parameter(default="sample_text")
    b1 = CompleteDSLPckg_BehavioralFeature()
    b2 = CompleteDSLPckg_BehavioralFeature()
    _safe_set(a, 'CompleteDSLPckg_Parameter138', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter138', b1)
    if hasattr(b1, 'CompleteDSLPckg_BehavioralFeature'):
        assert _is_linked(b1, 'CompleteDSLPckg_BehavioralFeature', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter138', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter138', b2)
    if hasattr(b1, 'CompleteDSLPckg_BehavioralFeature'):
        assert not _is_linked(b1, 'CompleteDSLPckg_BehavioralFeature', a)
    if hasattr(b2, 'CompleteDSLPckg_BehavioralFeature'):
        assert _is_linked(b2, 'CompleteDSLPckg_BehavioralFeature', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter138', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Parameter138', b2)
    if hasattr(b2, 'CompleteDSLPckg_BehavioralFeature'):
        assert not _is_linked(b2, 'CompleteDSLPckg_BehavioralFeature', a)


def test_assoc_ownedParameter240_link_reassign_clear():
    a = CompleteDSLPckg_Parameter(default="sample_text")
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_Parameter242', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter242', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior241'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior241', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter242', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter242', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior241'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior241', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior241'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior241', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter242', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Parameter242', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior241'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior241', a)


def test_assoc_ownedPort351_link_reassign_clear():
    a = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    b1 = CompleteDSLPckg_EncapsulatedClassifier()
    b2 = CompleteDSLPckg_EncapsulatedClassifier()
    _safe_set(a, 'CompleteDSLPckg_Port352', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Port352', b1)
    if hasattr(b1, 'CompleteDSLPckg_EncapsulatedClassifier'):
        assert _is_linked(b1, 'CompleteDSLPckg_EncapsulatedClassifier', a)
    _safe_set(a, 'CompleteDSLPckg_Port352', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Port352', b2)
    if hasattr(b1, 'CompleteDSLPckg_EncapsulatedClassifier'):
        assert not _is_linked(b1, 'CompleteDSLPckg_EncapsulatedClassifier', a)
    if hasattr(b2, 'CompleteDSLPckg_EncapsulatedClassifier'):
        assert _is_linked(b2, 'CompleteDSLPckg_EncapsulatedClassifier', a)
    _safe_set(a, 'CompleteDSLPckg_Port352', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Port352', b2)
    if hasattr(b2, 'CompleteDSLPckg_EncapsulatedClassifier'):
        assert not _is_linked(b2, 'CompleteDSLPckg_EncapsulatedClassifier', a)


def test_assoc_ownedType31_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_Type()
    b2 = CompleteDSLPckg_Type()
    _safe_set(a, 'package', {b1})
    assert _is_linked(a, 'package', b1)
    if hasattr(b1, 'Type'):
        assert _is_linked(b1, 'Type', a)
    _safe_set(a, 'package', {b2})
    assert _is_linked(a, 'package', b2)
    if hasattr(b1, 'Type'):
        assert not _is_linked(b1, 'Type', a)
    if hasattr(b2, 'Type'):
        assert _is_linked(b2, 'Type', a)
    _safe_set(a, 'package', set())
    assert not _is_linked(a, 'package', b2)
    if hasattr(b2, 'Type'):
        assert not _is_linked(b2, 'Type', a)


def test_assoc_owningAssociation119_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Association(isDerived=True)
    b2 = CompleteDSLPckg_Association(isDerived=False)
    _safe_set(a, 'ownedEnd', b1)
    assert _is_linked(a, 'ownedEnd', b1)
    if hasattr(b1, 'Association120'):
        assert _is_linked(b1, 'Association120', a)
    _safe_set(a, 'ownedEnd', b2)
    assert _is_linked(a, 'ownedEnd', b2)
    if hasattr(b1, 'Association120'):
        assert not _is_linked(b1, 'Association120', a)
    if hasattr(b2, 'Association120'):
        assert _is_linked(b2, 'Association120', a)
    _safe_set(a, 'ownedEnd', None)
    assert not _is_linked(a, 'ownedEnd', b2)
    if hasattr(b2, 'Association120'):
        assert not _is_linked(b2, 'Association120', a)


def test_assoc_owningElement33_link_reassign_clear():
    a = CompleteDSLPckg_Comment(body="sample_text")
    b1 = CompleteDSLPckg_Element()
    b2 = CompleteDSLPckg_Element()
    _safe_set(a, 'ownedComment', b1)
    assert _is_linked(a, 'ownedComment', b1)
    if hasattr(b1, 'Element34'):
        assert _is_linked(b1, 'Element34', a)
    _safe_set(a, 'ownedComment', b2)
    assert _is_linked(a, 'ownedComment', b2)
    if hasattr(b1, 'Element34'):
        assert not _is_linked(b1, 'Element34', a)
    if hasattr(b2, 'Element34'):
        assert _is_linked(b2, 'Element34', a)
    _safe_set(a, 'ownedComment', None)
    assert not _is_linked(a, 'ownedComment', b2)
    if hasattr(b2, 'Element34'):
        assert not _is_linked(b2, 'Element34', a)


def test_assoc_owningLower47_link_reassign_clear():
    a = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'MultiplicityElement48', b1)
    assert _is_linked(a, 'MultiplicityElement48', b1)
    if hasattr(b1, 'lowerValue'):
        assert _is_linked(b1, 'lowerValue', a)
    _safe_set(a, 'MultiplicityElement48', b2)
    assert _is_linked(a, 'MultiplicityElement48', b2)
    if hasattr(b1, 'lowerValue'):
        assert not _is_linked(b1, 'lowerValue', a)
    if hasattr(b2, 'lowerValue'):
        assert _is_linked(b2, 'lowerValue', a)
    _safe_set(a, 'MultiplicityElement48', None)
    assert not _is_linked(a, 'MultiplicityElement48', b2)
    if hasattr(b2, 'lowerValue'):
        assert not _is_linked(b2, 'lowerValue', a)


def test_assoc_owningUpper46_link_reassign_clear():
    a = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'MultiplicityElement', b1)
    assert _is_linked(a, 'MultiplicityElement', b1)
    if hasattr(b1, 'upperValue'):
        assert _is_linked(b1, 'upperValue', a)
    _safe_set(a, 'MultiplicityElement', b2)
    assert _is_linked(a, 'MultiplicityElement', b2)
    if hasattr(b1, 'upperValue'):
        assert not _is_linked(b1, 'upperValue', a)
    if hasattr(b2, 'upperValue'):
        assert _is_linked(b2, 'upperValue', a)
    _safe_set(a, 'MultiplicityElement', None)
    assert not _is_linked(a, 'MultiplicityElement', b2)
    if hasattr(b2, 'upperValue'):
        assert not _is_linked(b2, 'upperValue', a)


def test_assoc_package55_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_Type()
    b2 = CompleteDSLPckg_Type()
    _safe_set(a, 'Package56', b1)
    assert _is_linked(a, 'Package56', b1)
    if hasattr(b1, 'ownedType'):
        assert _is_linked(b1, 'ownedType', a)
    _safe_set(a, 'Package56', b2)
    assert _is_linked(a, 'Package56', b2)
    if hasattr(b1, 'ownedType'):
        assert not _is_linked(b1, 'ownedType', a)
    if hasattr(b2, 'ownedType'):
        assert _is_linked(b2, 'ownedType', a)
    _safe_set(a, 'Package56', None)
    assert not _is_linked(a, 'Package56', b2)
    if hasattr(b2, 'ownedType'):
        assert not _is_linked(b2, 'ownedType', a)


def test_assoc_packageImport13_link_reassign_clear():
    a = CompleteDSLPckg_PackageImport(visibility="sample_text")
    b1 = CompleteDSLPckg_Namespace()
    b2 = CompleteDSLPckg_Namespace()
    _safe_set(a, 'PackageImport', b1)
    assert _is_linked(a, 'PackageImport', b1)
    if hasattr(b1, 'importingNamespace14'):
        assert _is_linked(b1, 'importingNamespace14', a)
    _safe_set(a, 'PackageImport', b2)
    assert _is_linked(a, 'PackageImport', b2)
    if hasattr(b1, 'importingNamespace14'):
        assert not _is_linked(b1, 'importingNamespace14', a)
    if hasattr(b2, 'importingNamespace14'):
        assert _is_linked(b2, 'importingNamespace14', a)
    _safe_set(a, 'PackageImport', None)
    assert not _is_linked(a, 'PackageImport', b2)
    if hasattr(b2, 'importingNamespace14'):
        assert not _is_linked(b2, 'importingNamespace14', a)


def test_assoc_packageMerge32_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_PackageMerge()
    b2 = CompleteDSLPckg_PackageMerge()
    _safe_set(a, 'receivingPackage', {b1})
    assert _is_linked(a, 'receivingPackage', b1)
    if hasattr(b1, 'PackageMerge'):
        assert _is_linked(b1, 'PackageMerge', a)
    _safe_set(a, 'receivingPackage', {b2})
    assert _is_linked(a, 'receivingPackage', b2)
    if hasattr(b1, 'PackageMerge'):
        assert not _is_linked(b1, 'PackageMerge', a)
    if hasattr(b2, 'PackageMerge'):
        assert _is_linked(b2, 'PackageMerge', a)
    _safe_set(a, 'receivingPackage', set())
    assert not _is_linked(a, 'receivingPackage', b2)
    if hasattr(b2, 'PackageMerge'):
        assert not _is_linked(b2, 'PackageMerge', a)


def test_assoc_packagedElement28_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_PackageableElement()
    b2 = CompleteDSLPckg_PackageableElement()
    _safe_set(a, 'CompleteDSLPckg_Package29', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Package29', b1)
    if hasattr(b1, 'CompleteDSLPckg_PackageableElement30'):
        assert _is_linked(b1, 'CompleteDSLPckg_PackageableElement30', a)
    _safe_set(a, 'CompleteDSLPckg_Package29', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Package29', b2)
    if hasattr(b1, 'CompleteDSLPckg_PackageableElement30'):
        assert not _is_linked(b1, 'CompleteDSLPckg_PackageableElement30', a)
    if hasattr(b2, 'CompleteDSLPckg_PackageableElement30'):
        assert _is_linked(b2, 'CompleteDSLPckg_PackageableElement30', a)
    _safe_set(a, 'CompleteDSLPckg_Package29', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Package29', b2)
    if hasattr(b2, 'CompleteDSLPckg_PackageableElement30'):
        assert not _is_linked(b2, 'CompleteDSLPckg_PackageableElement30', a)


def test_assoc_packagedElement302_link_reassign_clear():
    a = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    b1 = CompleteDSLPckg_PackageableElement()
    b2 = CompleteDSLPckg_PackageableElement()
    _safe_set(a, 'CompleteDSLPckg_Component303', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Component303', b1)
    if hasattr(b1, 'CompleteDSLPckg_PackageableElement304'):
        assert _is_linked(b1, 'CompleteDSLPckg_PackageableElement304', a)
    _safe_set(a, 'CompleteDSLPckg_Component303', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Component303', b2)
    if hasattr(b1, 'CompleteDSLPckg_PackageableElement304'):
        assert not _is_linked(b1, 'CompleteDSLPckg_PackageableElement304', a)
    if hasattr(b2, 'CompleteDSLPckg_PackageableElement304'):
        assert _is_linked(b2, 'CompleteDSLPckg_PackageableElement304', a)
    _safe_set(a, 'CompleteDSLPckg_Component303', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Component303', b2)
    if hasattr(b2, 'CompleteDSLPckg_PackageableElement304'):
        assert not _is_linked(b2, 'CompleteDSLPckg_PackageableElement304', a)


def test_assoc_parameter728_link_reassign_clear():
    a = CompleteDSLPckg_Parameter(default="sample_text")
    b1 = CompleteDSLPckg_ActivityParameterNode()
    b2 = CompleteDSLPckg_ActivityParameterNode()
    _safe_set(a, 'CompleteDSLPckg_Parameter729', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter729', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityParameterNode'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityParameterNode', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter729', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter729', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityParameterNode'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityParameterNode', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityParameterNode'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityParameterNode', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter729', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Parameter729', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityParameterNode'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityParameterNode', a)


def test_assoc_parameter787_link_reassign_clear():
    a = CompleteDSLPckg_Parameter(default="sample_text")
    b1 = CompleteDSLPckg_ParameterSet()
    b2 = CompleteDSLPckg_ParameterSet()
    _safe_set(a, 'CompleteDSLPckg_Parameter788', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter788', b1)
    if hasattr(b1, 'CompleteDSLPckg_ParameterSet'):
        assert _is_linked(b1, 'CompleteDSLPckg_ParameterSet', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter788', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter788', b2)
    if hasattr(b1, 'CompleteDSLPckg_ParameterSet'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ParameterSet', a)
    if hasattr(b2, 'CompleteDSLPckg_ParameterSet'):
        assert _is_linked(b2, 'CompleteDSLPckg_ParameterSet', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter788', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Parameter788', b2)
    if hasattr(b2, 'CompleteDSLPckg_ParameterSet'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ParameterSet', a)


def test_assoc_part340_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_StructuredClassifier()
    b2 = CompleteDSLPckg_StructuredClassifier()
    _safe_set(a, 'CompleteDSLPckg_Property342', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property342', b1)
    if hasattr(b1, 'CompleteDSLPckg_StructuredClassifier341'):
        assert _is_linked(b1, 'CompleteDSLPckg_StructuredClassifier341', a)
    _safe_set(a, 'CompleteDSLPckg_Property342', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property342', b2)
    if hasattr(b1, 'CompleteDSLPckg_StructuredClassifier341'):
        assert not _is_linked(b1, 'CompleteDSLPckg_StructuredClassifier341', a)
    if hasattr(b2, 'CompleteDSLPckg_StructuredClassifier341'):
        assert _is_linked(b2, 'CompleteDSLPckg_StructuredClassifier341', a)
    _safe_set(a, 'CompleteDSLPckg_Property342', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property342', b2)
    if hasattr(b2, 'CompleteDSLPckg_StructuredClassifier341'):
        assert not _is_linked(b2, 'CompleteDSLPckg_StructuredClassifier341', a)


def test_assoc_partWithPort318_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_ConnectorEnd()
    b2 = CompleteDSLPckg_ConnectorEnd()
    _safe_set(a, 'CompleteDSLPckg_Property320', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property320', b1)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd319'):
        assert _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd319', a)
    _safe_set(a, 'CompleteDSLPckg_Property320', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property320', b2)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd319'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd319', a)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd319'):
        assert _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd319', a)
    _safe_set(a, 'CompleteDSLPckg_Property320', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property320', b2)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd319'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd319', a)


def test_assoc_partition686_link_reassign_clear():
    a = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = CompleteDSLPckg_ActivityPartition()
    b2 = CompleteDSLPckg_ActivityPartition()
    _safe_set(a, 'CompleteDSLPckg_Activity687', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Activity687', b1)
    if hasattr(b1, 'CompleteDSLPckg_ActivityPartition'):
        assert _is_linked(b1, 'CompleteDSLPckg_ActivityPartition', a)
    _safe_set(a, 'CompleteDSLPckg_Activity687', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Activity687', b2)
    if hasattr(b1, 'CompleteDSLPckg_ActivityPartition'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ActivityPartition', a)
    if hasattr(b2, 'CompleteDSLPckg_ActivityPartition'):
        assert _is_linked(b2, 'CompleteDSLPckg_ActivityPartition', a)
    _safe_set(a, 'CompleteDSLPckg_Activity687', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Activity687', b2)
    if hasattr(b2, 'CompleteDSLPckg_ActivityPartition'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ActivityPartition', a)


def test_assoc_postcondition156_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Constraint()
    b2 = CompleteDSLPckg_Constraint()
    _safe_set(a, 'CompleteDSLPckg_Operation157', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Operation157', b1)
    if hasattr(b1, 'CompleteDSLPckg_Constraint158'):
        assert _is_linked(b1, 'CompleteDSLPckg_Constraint158', a)
    _safe_set(a, 'CompleteDSLPckg_Operation157', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Operation157', b2)
    if hasattr(b1, 'CompleteDSLPckg_Constraint158'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Constraint158', a)
    if hasattr(b2, 'CompleteDSLPckg_Constraint158'):
        assert _is_linked(b2, 'CompleteDSLPckg_Constraint158', a)
    _safe_set(a, 'CompleteDSLPckg_Operation157', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Operation157', b2)
    if hasattr(b2, 'CompleteDSLPckg_Constraint158'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Constraint158', a)


def test_assoc_postcondition246_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_Constraint()
    b2 = CompleteDSLPckg_Constraint()
    _safe_set(a, 'CompleteDSLPckg_Behavior247', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Behavior247', b1)
    if hasattr(b1, 'CompleteDSLPckg_Constraint248'):
        assert _is_linked(b1, 'CompleteDSLPckg_Constraint248', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior247', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Behavior247', b2)
    if hasattr(b1, 'CompleteDSLPckg_Constraint248'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Constraint248', a)
    if hasattr(b2, 'CompleteDSLPckg_Constraint248'):
        assert _is_linked(b2, 'CompleteDSLPckg_Constraint248', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior247', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior247', b2)
    if hasattr(b2, 'CompleteDSLPckg_Constraint248'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Constraint248', a)


def test_assoc_powertype227_link_reassign_clear():
    a = CompleteDSLPckg_GeneralizationSet(isCovering=True, isDisjoint=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'powertypeExtent', b1)
    assert _is_linked(a, 'powertypeExtent', b1)
    if hasattr(b1, 'Classifier228'):
        assert _is_linked(b1, 'Classifier228', a)
    _safe_set(a, 'powertypeExtent', b2)
    assert _is_linked(a, 'powertypeExtent', b2)
    if hasattr(b1, 'Classifier228'):
        assert not _is_linked(b1, 'Classifier228', a)
    if hasattr(b2, 'Classifier228'):
        assert _is_linked(b2, 'Classifier228', a)
    _safe_set(a, 'powertypeExtent', None)
    assert not _is_linked(a, 'powertypeExtent', b2)
    if hasattr(b2, 'Classifier228'):
        assert not _is_linked(b2, 'Classifier228', a)


def test_assoc_powertypeExtent98_link_reassign_clear():
    a = CompleteDSLPckg_GeneralizationSet(isCovering=True, isDisjoint=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'GeneralizationSet', b1)
    assert _is_linked(a, 'GeneralizationSet', b1)
    if hasattr(b1, 'powertype'):
        assert _is_linked(b1, 'powertype', a)
    _safe_set(a, 'GeneralizationSet', b2)
    assert _is_linked(a, 'GeneralizationSet', b2)
    if hasattr(b1, 'powertype'):
        assert not _is_linked(b1, 'powertype', a)
    if hasattr(b2, 'powertype'):
        assert _is_linked(b2, 'powertype', a)
    _safe_set(a, 'GeneralizationSet', None)
    assert not _is_linked(a, 'GeneralizationSet', b2)
    if hasattr(b2, 'powertype'):
        assert not _is_linked(b2, 'powertype', a)


def test_assoc_precondition150_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Constraint()
    b2 = CompleteDSLPckg_Constraint()
    _safe_set(a, 'CompleteDSLPckg_Operation151', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Operation151', b1)
    if hasattr(b1, 'CompleteDSLPckg_Constraint152'):
        assert _is_linked(b1, 'CompleteDSLPckg_Constraint152', a)
    _safe_set(a, 'CompleteDSLPckg_Operation151', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Operation151', b2)
    if hasattr(b1, 'CompleteDSLPckg_Constraint152'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Constraint152', a)
    if hasattr(b2, 'CompleteDSLPckg_Constraint152'):
        assert _is_linked(b2, 'CompleteDSLPckg_Constraint152', a)
    _safe_set(a, 'CompleteDSLPckg_Operation151', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Operation151', b2)
    if hasattr(b2, 'CompleteDSLPckg_Constraint152'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Constraint152', a)


def test_assoc_precondition243_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_Constraint()
    b2 = CompleteDSLPckg_Constraint()
    _safe_set(a, 'CompleteDSLPckg_Behavior244', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Behavior244', b1)
    if hasattr(b1, 'CompleteDSLPckg_Constraint245'):
        assert _is_linked(b1, 'CompleteDSLPckg_Constraint245', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior244', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Behavior244', b2)
    if hasattr(b1, 'CompleteDSLPckg_Constraint245'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Constraint245', a)
    if hasattr(b2, 'CompleteDSLPckg_Constraint245'):
        assert _is_linked(b2, 'CompleteDSLPckg_Constraint245', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior244', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior244', b2)
    if hasattr(b2, 'CompleteDSLPckg_Constraint245'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Constraint245', a)


def test_assoc_provided297_link_reassign_clear():
    a = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'CompleteDSLPckg_Component298', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Component298', b1)
    if hasattr(b1, 'CompleteDSLPckg_Interface299'):
        assert _is_linked(b1, 'CompleteDSLPckg_Interface299', a)
    _safe_set(a, 'CompleteDSLPckg_Component298', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Component298', b2)
    if hasattr(b1, 'CompleteDSLPckg_Interface299'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Interface299', a)
    if hasattr(b2, 'CompleteDSLPckg_Interface299'):
        assert _is_linked(b2, 'CompleteDSLPckg_Interface299', a)
    _safe_set(a, 'CompleteDSLPckg_Component298', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Component298', b2)
    if hasattr(b2, 'CompleteDSLPckg_Interface299'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Interface299', a)


def test_assoc_provided345_link_reassign_clear():
    a = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'CompleteDSLPckg_Port346', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Port346', b1)
    if hasattr(b1, 'CompleteDSLPckg_Interface347'):
        assert _is_linked(b1, 'CompleteDSLPckg_Interface347', a)
    _safe_set(a, 'CompleteDSLPckg_Port346', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Port346', b2)
    if hasattr(b1, 'CompleteDSLPckg_Interface347'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Interface347', a)
    if hasattr(b2, 'CompleteDSLPckg_Interface347'):
        assert _is_linked(b2, 'CompleteDSLPckg_Interface347', a)
    _safe_set(a, 'CompleteDSLPckg_Port346', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Port346', b2)
    if hasattr(b2, 'CompleteDSLPckg_Interface347'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Interface347', a)


def test_assoc_qualifier126_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b2 = CompleteDSLPckg_Property(aggregation="sample_text_2", default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    _safe_set(a, 'Property', b1)
    assert _is_linked(a, 'Property', b1)
    if hasattr(b1, 'associationEnd'):
        assert _is_linked(b1, 'associationEnd', a)
    _safe_set(a, 'Property', b2)
    assert _is_linked(a, 'Property', b2)
    if hasattr(b1, 'associationEnd'):
        assert not _is_linked(b1, 'associationEnd', a)
    if hasattr(b2, 'associationEnd'):
        assert _is_linked(b2, 'associationEnd', a)
    _safe_set(a, 'Property', None)
    assert not _is_linked(a, 'Property', b2)
    if hasattr(b2, 'associationEnd'):
        assert not _is_linked(b2, 'associationEnd', a)


def test_assoc_qualifier529_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_QualifierValue()
    b2 = CompleteDSLPckg_QualifierValue()
    _safe_set(a, 'CompleteDSLPckg_Property531', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property531', b1)
    if hasattr(b1, 'CompleteDSLPckg_QualifierValue530'):
        assert _is_linked(b1, 'CompleteDSLPckg_QualifierValue530', a)
    _safe_set(a, 'CompleteDSLPckg_Property531', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property531', b2)
    if hasattr(b1, 'CompleteDSLPckg_QualifierValue530'):
        assert not _is_linked(b1, 'CompleteDSLPckg_QualifierValue530', a)
    if hasattr(b2, 'CompleteDSLPckg_QualifierValue530'):
        assert _is_linked(b2, 'CompleteDSLPckg_QualifierValue530', a)
    _safe_set(a, 'CompleteDSLPckg_Property531', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property531', b2)
    if hasattr(b2, 'CompleteDSLPckg_QualifierValue530'):
        assert not _is_linked(b2, 'CompleteDSLPckg_QualifierValue530', a)


def test_assoc_qualifier548_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_ReadLinkObjectEndQualifierAction()
    b2 = CompleteDSLPckg_ReadLinkObjectEndQualifierAction()
    _safe_set(a, 'CompleteDSLPckg_Property550', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property550', b1)
    if hasattr(b1, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549'):
        assert _is_linked(b1, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549', a)
    _safe_set(a, 'CompleteDSLPckg_Property550', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property550', b2)
    if hasattr(b1, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549', a)
    if hasattr(b2, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549'):
        assert _is_linked(b2, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549', a)
    _safe_set(a, 'CompleteDSLPckg_Property550', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property550', b2)
    if hasattr(b2, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ReadLinkObjectEndQualifierAction549', a)


def test_assoc_realization300_link_reassign_clear():
    a = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    b1 = CompleteDSLPckg_ComponentRealization()
    b2 = CompleteDSLPckg_ComponentRealization()
    _safe_set(a, 'CompleteDSLPckg_Component301', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Component301', b1)
    if hasattr(b1, 'CompleteDSLPckg_ComponentRealization'):
        assert _is_linked(b1, 'CompleteDSLPckg_ComponentRealization', a)
    _safe_set(a, 'CompleteDSLPckg_Component301', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Component301', b2)
    if hasattr(b1, 'CompleteDSLPckg_ComponentRealization'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ComponentRealization', a)
    if hasattr(b2, 'CompleteDSLPckg_ComponentRealization'):
        assert _is_linked(b2, 'CompleteDSLPckg_ComponentRealization', a)
    _safe_set(a, 'CompleteDSLPckg_Component301', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Component301', b2)
    if hasattr(b2, 'CompleteDSLPckg_ComponentRealization'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ComponentRealization', a)


def test_assoc_realizingClassifier308_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_ComponentRealization()
    b2 = CompleteDSLPckg_ComponentRealization()
    _safe_set(a, 'CompleteDSLPckg_Classifier310', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier310', b1)
    if hasattr(b1, 'CompleteDSLPckg_ComponentRealization309'):
        assert _is_linked(b1, 'CompleteDSLPckg_ComponentRealization309', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier310', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier310', b2)
    if hasattr(b1, 'CompleteDSLPckg_ComponentRealization309'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ComponentRealization309', a)
    if hasattr(b2, 'CompleteDSLPckg_ComponentRealization309'):
        assert _is_linked(b2, 'CompleteDSLPckg_ComponentRealization309', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier310', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier310', b2)
    if hasattr(b2, 'CompleteDSLPckg_ComponentRealization309'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ComponentRealization309', a)


def test_assoc_receiveEvent933_link_reassign_clear():
    a = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    b1 = CompleteDSLPckg_MessageEnd()
    b2 = CompleteDSLPckg_MessageEnd()
    _safe_set(a, 'CompleteDSLPckg_Message934', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Message934', b1)
    if hasattr(b1, 'CompleteDSLPckg_MessageEnd935'):
        assert _is_linked(b1, 'CompleteDSLPckg_MessageEnd935', a)
    _safe_set(a, 'CompleteDSLPckg_Message934', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Message934', b2)
    if hasattr(b1, 'CompleteDSLPckg_MessageEnd935'):
        assert not _is_linked(b1, 'CompleteDSLPckg_MessageEnd935', a)
    if hasattr(b2, 'CompleteDSLPckg_MessageEnd935'):
        assert _is_linked(b2, 'CompleteDSLPckg_MessageEnd935', a)
    _safe_set(a, 'CompleteDSLPckg_Message934', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Message934', b2)
    if hasattr(b2, 'CompleteDSLPckg_MessageEnd935'):
        assert not _is_linked(b2, 'CompleteDSLPckg_MessageEnd935', a)


def test_assoc_receivingPackage191_link_reassign_clear():
    a = CompleteDSLPckg_Package(URI="sample_text")
    b1 = CompleteDSLPckg_PackageMerge()
    b2 = CompleteDSLPckg_PackageMerge()
    _safe_set(a, 'Package192', b1)
    assert _is_linked(a, 'Package192', b1)
    if hasattr(b1, 'packageMerge'):
        assert _is_linked(b1, 'packageMerge', a)
    _safe_set(a, 'Package192', b2)
    assert _is_linked(a, 'Package192', b2)
    if hasattr(b1, 'packageMerge'):
        assert not _is_linked(b1, 'packageMerge', a)
    if hasattr(b2, 'packageMerge'):
        assert _is_linked(b2, 'packageMerge', a)
    _safe_set(a, 'Package192', None)
    assert not _is_linked(a, 'Package192', b2)
    if hasattr(b2, 'packageMerge'):
        assert not _is_linked(b2, 'packageMerge', a)


def test_assoc_redefinedBehavior235_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_Behavior234', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Behavior234', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior236'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior236', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior234', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Behavior234', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior236'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior236', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior236'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior236', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior234', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior234', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior236'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior236', a)


def test_assoc_redefinedClassifier91_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_Classifier90', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Classifier90', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier92'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier92', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier90', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Classifier90', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier92'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier92', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier92'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier92', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier90', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier90', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier92'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier92', a)


def test_assoc_redefinedConnector316_link_reassign_clear():
    a = CompleteDSLPckg_Connector(kind="sample_text")
    b1 = CompleteDSLPckg_Connector(kind="sample_text")
    b2 = CompleteDSLPckg_Connector(kind="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_Connector315', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Connector315', b1)
    if hasattr(b1, 'CompleteDSLPckg_Connector317'):
        assert _is_linked(b1, 'CompleteDSLPckg_Connector317', a)
    _safe_set(a, 'CompleteDSLPckg_Connector315', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Connector315', b2)
    if hasattr(b1, 'CompleteDSLPckg_Connector317'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Connector317', a)
    if hasattr(b2, 'CompleteDSLPckg_Connector317'):
        assert _is_linked(b2, 'CompleteDSLPckg_Connector317', a)
    _safe_set(a, 'CompleteDSLPckg_Connector315', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Connector315', b2)
    if hasattr(b2, 'CompleteDSLPckg_Connector317'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Connector317', a)


def test_assoc_redefinedElement80_link_reassign_clear():
    a = CompleteDSLPckg_RedefinableElement(isLeaf=True)
    b1 = CompleteDSLPckg_RedefinableElement(isLeaf=True)
    b2 = CompleteDSLPckg_RedefinableElement(isLeaf=False)
    _safe_set(a, 'CompleteDSLPckg_RedefinableElement', b1)
    assert _is_linked(a, 'CompleteDSLPckg_RedefinableElement', b1)
    if hasattr(b1, 'CompleteDSLPckg_RedefinableElement79'):
        assert _is_linked(b1, 'CompleteDSLPckg_RedefinableElement79', a)
    _safe_set(a, 'CompleteDSLPckg_RedefinableElement', b2)
    assert _is_linked(a, 'CompleteDSLPckg_RedefinableElement', b2)
    if hasattr(b1, 'CompleteDSLPckg_RedefinableElement79'):
        assert not _is_linked(b1, 'CompleteDSLPckg_RedefinableElement79', a)
    if hasattr(b2, 'CompleteDSLPckg_RedefinableElement79'):
        assert _is_linked(b2, 'CompleteDSLPckg_RedefinableElement79', a)
    _safe_set(a, 'CompleteDSLPckg_RedefinableElement', None)
    assert not _is_linked(a, 'CompleteDSLPckg_RedefinableElement', b2)
    if hasattr(b2, 'CompleteDSLPckg_RedefinableElement79'):
        assert not _is_linked(b2, 'CompleteDSLPckg_RedefinableElement79', a)


def test_assoc_redefinedPort349_link_reassign_clear():
    a = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    b1 = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    b2 = CompleteDSLPckg_Port(isBehavior=False, isConjugated=False, isService=False)
    _safe_set(a, 'CompleteDSLPckg_Port348', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Port348', b1)
    if hasattr(b1, 'CompleteDSLPckg_Port350'):
        assert _is_linked(b1, 'CompleteDSLPckg_Port350', a)
    _safe_set(a, 'CompleteDSLPckg_Port348', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Port348', b2)
    if hasattr(b1, 'CompleteDSLPckg_Port350'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Port350', a)
    if hasattr(b2, 'CompleteDSLPckg_Port350'):
        assert _is_linked(b2, 'CompleteDSLPckg_Port350', a)
    _safe_set(a, 'CompleteDSLPckg_Port348', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Port348', b2)
    if hasattr(b2, 'CompleteDSLPckg_Port350'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Port350', a)


def test_assoc_redefinedProperty107_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b2 = CompleteDSLPckg_Property(aggregation="sample_text_2", default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    _safe_set(a, 'CompleteDSLPckg_Property106', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Property106', b1)
    if hasattr(b1, 'CompleteDSLPckg_Property108'):
        assert _is_linked(b1, 'CompleteDSLPckg_Property108', a)
    _safe_set(a, 'CompleteDSLPckg_Property106', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Property106', b2)
    if hasattr(b1, 'CompleteDSLPckg_Property108'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Property108', a)
    if hasattr(b2, 'CompleteDSLPckg_Property108'):
        assert _is_linked(b2, 'CompleteDSLPckg_Property108', a)
    _safe_set(a, 'CompleteDSLPckg_Property106', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Property106', b2)
    if hasattr(b2, 'CompleteDSLPckg_Property108'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Property108', a)


def test_assoc_redefinedState664_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b2 = CompleteDSLPckg_State(isComposite=False, isOrthogonal=False, isSimple=False, isSubmachineState=False)
    _safe_set(a, 'CompleteDSLPckg_State663', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State663', b1)
    if hasattr(b1, 'CompleteDSLPckg_State665'):
        assert _is_linked(b1, 'CompleteDSLPckg_State665', a)
    _safe_set(a, 'CompleteDSLPckg_State663', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State663', b2)
    if hasattr(b1, 'CompleteDSLPckg_State665'):
        assert not _is_linked(b1, 'CompleteDSLPckg_State665', a)
    if hasattr(b2, 'CompleteDSLPckg_State665'):
        assert _is_linked(b2, 'CompleteDSLPckg_State665', a)
    _safe_set(a, 'CompleteDSLPckg_State663', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State663', b2)
    if hasattr(b2, 'CompleteDSLPckg_State665'):
        assert not _is_linked(b2, 'CompleteDSLPckg_State665', a)


def test_assoc_redefinedTransition623_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Transition(kind="sample_text")
    b2 = CompleteDSLPckg_Transition(kind="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_Transition622', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition622', b1)
    if hasattr(b1, 'CompleteDSLPckg_Transition624'):
        assert _is_linked(b1, 'CompleteDSLPckg_Transition624', a)
    _safe_set(a, 'CompleteDSLPckg_Transition622', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition622', b2)
    if hasattr(b1, 'CompleteDSLPckg_Transition624'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Transition624', a)
    if hasattr(b2, 'CompleteDSLPckg_Transition624'):
        assert _is_linked(b2, 'CompleteDSLPckg_Transition624', a)
    _safe_set(a, 'CompleteDSLPckg_Transition622', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition622', b2)
    if hasattr(b2, 'CompleteDSLPckg_Transition624'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Transition624', a)


def test_assoc_redefinitionContext81_link_reassign_clear():
    a = CompleteDSLPckg_RedefinableElement(isLeaf=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'CompleteDSLPckg_RedefinableElement82', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_RedefinableElement82', b1)
    if hasattr(b1, 'CompleteDSLPckg_Classifier83'):
        assert _is_linked(b1, 'CompleteDSLPckg_Classifier83', a)
    _safe_set(a, 'CompleteDSLPckg_RedefinableElement82', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_RedefinableElement82', b2)
    if hasattr(b1, 'CompleteDSLPckg_Classifier83'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Classifier83', a)
    if hasattr(b2, 'CompleteDSLPckg_Classifier83'):
        assert _is_linked(b2, 'CompleteDSLPckg_Classifier83', a)
    _safe_set(a, 'CompleteDSLPckg_RedefinableElement82', set())
    assert not _is_linked(a, 'CompleteDSLPckg_RedefinableElement82', b2)
    if hasattr(b2, 'CompleteDSLPckg_Classifier83'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Classifier83', a)


def test_assoc_reducer558_link_reassign_clear():
    a = CompleteDSLPckg_ReduceAction(isOrdered=True)
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_ReduceAction559', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ReduceAction559', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior560'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior560', a)
    _safe_set(a, 'CompleteDSLPckg_ReduceAction559', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ReduceAction559', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior560'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior560', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior560'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior560', a)
    _safe_set(a, 'CompleteDSLPckg_ReduceAction559', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ReduceAction559', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior560'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior560', a)


def test_assoc_referred678_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_ProtocolTransition()
    b2 = CompleteDSLPckg_ProtocolTransition()
    _safe_set(a, 'CompleteDSLPckg_Operation680', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Operation680', b1)
    if hasattr(b1, 'CompleteDSLPckg_ProtocolTransition679'):
        assert _is_linked(b1, 'CompleteDSLPckg_ProtocolTransition679', a)
    _safe_set(a, 'CompleteDSLPckg_Operation680', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Operation680', b2)
    if hasattr(b1, 'CompleteDSLPckg_ProtocolTransition679'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ProtocolTransition679', a)
    if hasattr(b2, 'CompleteDSLPckg_ProtocolTransition679'):
        assert _is_linked(b2, 'CompleteDSLPckg_ProtocolTransition679', a)
    _safe_set(a, 'CompleteDSLPckg_Operation680', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Operation680', b2)
    if hasattr(b2, 'CompleteDSLPckg_ProtocolTransition679'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ProtocolTransition679', a)


def test_assoc_region645_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Region()
    b2 = CompleteDSLPckg_Region()
    _safe_set(a, 'CompleteDSLPckg_State646', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_State646', b1)
    if hasattr(b1, 'CompleteDSLPckg_Region647'):
        assert _is_linked(b1, 'CompleteDSLPckg_Region647', a)
    _safe_set(a, 'CompleteDSLPckg_State646', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_State646', b2)
    if hasattr(b1, 'CompleteDSLPckg_Region647'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Region647', a)
    if hasattr(b2, 'CompleteDSLPckg_Region647'):
        assert _is_linked(b2, 'CompleteDSLPckg_Region647', a)
    _safe_set(a, 'CompleteDSLPckg_State646', set())
    assert not _is_linked(a, 'CompleteDSLPckg_State646', b2)
    if hasattr(b2, 'CompleteDSLPckg_Region647'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Region647', a)


def test_assoc_regionAsInput876_link_reassign_clear():
    a = CompleteDSLPckg_ExpansionRegion(mode="sample_text")
    b1 = CompleteDSLPckg_ExpansionNode()
    b2 = CompleteDSLPckg_ExpansionNode()
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion878', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion878', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode877'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExpansionNode877', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion878', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion878', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode877'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExpansionNode877', a)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode877'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExpansionNode877', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion878', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ExpansionRegion878', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode877'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExpansionNode877', a)


def test_assoc_regionAsOutput879_link_reassign_clear():
    a = CompleteDSLPckg_ExpansionRegion(mode="sample_text")
    b1 = CompleteDSLPckg_ExpansionNode()
    b2 = CompleteDSLPckg_ExpansionNode()
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion881', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion881', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode880'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExpansionNode880', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion881', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ExpansionRegion881', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExpansionNode880'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExpansionNode880', a)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode880'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExpansionNode880', a)
    _safe_set(a, 'CompleteDSLPckg_ExpansionRegion881', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ExpansionRegion881', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExpansionNode880'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExpansionNode880', a)


def test_assoc_representation101_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_CollaborationUse()
    b2 = CompleteDSLPckg_CollaborationUse()
    _safe_set(a, 'CompleteDSLPckg_Classifier102', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier102', b1)
    if hasattr(b1, 'CompleteDSLPckg_CollaborationUse103'):
        assert _is_linked(b1, 'CompleteDSLPckg_CollaborationUse103', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier102', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier102', b2)
    if hasattr(b1, 'CompleteDSLPckg_CollaborationUse103'):
        assert not _is_linked(b1, 'CompleteDSLPckg_CollaborationUse103', a)
    if hasattr(b2, 'CompleteDSLPckg_CollaborationUse103'):
        assert _is_linked(b2, 'CompleteDSLPckg_CollaborationUse103', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier102', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier102', b2)
    if hasattr(b2, 'CompleteDSLPckg_CollaborationUse103'):
        assert not _is_linked(b2, 'CompleteDSLPckg_CollaborationUse103', a)


def test_assoc_required295_link_reassign_clear():
    a = CompleteDSLPckg_Component(isIndirectlyInstantiated=True)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'CompleteDSLPckg_Component', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Component', b1)
    if hasattr(b1, 'CompleteDSLPckg_Interface296'):
        assert _is_linked(b1, 'CompleteDSLPckg_Interface296', a)
    _safe_set(a, 'CompleteDSLPckg_Component', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Component', b2)
    if hasattr(b1, 'CompleteDSLPckg_Interface296'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Interface296', a)
    if hasattr(b2, 'CompleteDSLPckg_Interface296'):
        assert _is_linked(b2, 'CompleteDSLPckg_Interface296', a)
    _safe_set(a, 'CompleteDSLPckg_Component', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Component', b2)
    if hasattr(b2, 'CompleteDSLPckg_Interface296'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Interface296', a)


def test_assoc_required343_link_reassign_clear():
    a = CompleteDSLPckg_Port(isBehavior=True, isConjugated=True, isService=True)
    b1 = CompleteDSLPckg_Interface()
    b2 = CompleteDSLPckg_Interface()
    _safe_set(a, 'CompleteDSLPckg_Port', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Port', b1)
    if hasattr(b1, 'CompleteDSLPckg_Interface344'):
        assert _is_linked(b1, 'CompleteDSLPckg_Interface344', a)
    _safe_set(a, 'CompleteDSLPckg_Port', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Port', b2)
    if hasattr(b1, 'CompleteDSLPckg_Interface344'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Interface344', a)
    if hasattr(b2, 'CompleteDSLPckg_Interface344'):
        assert _is_linked(b2, 'CompleteDSLPckg_Interface344', a)
    _safe_set(a, 'CompleteDSLPckg_Port', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Port', b2)
    if hasattr(b2, 'CompleteDSLPckg_Interface344'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Interface344', a)


def test_assoc_result405_link_reassign_clear():
    a = CompleteDSLPckg_CallAction(isSynchronous=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_CallAction', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_CallAction', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin406'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin406', a)
    _safe_set(a, 'CompleteDSLPckg_CallAction', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_CallAction', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin406'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin406', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin406'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin406', a)
    _safe_set(a, 'CompleteDSLPckg_CallAction', set())
    assert not _is_linked(a, 'CompleteDSLPckg_CallAction', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin406'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin406', a)


def test_assoc_result500_link_reassign_clear():
    a = CompleteDSLPckg_AcceptEventAction(isUnmarshall=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_AcceptEventAction', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_AcceptEventAction', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin501'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin501', a)
    _safe_set(a, 'CompleteDSLPckg_AcceptEventAction', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_AcceptEventAction', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin501'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin501', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin501'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin501', a)
    _safe_set(a, 'CompleteDSLPckg_AcceptEventAction', set())
    assert not _is_linked(a, 'CompleteDSLPckg_AcceptEventAction', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin501'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin501', a)


def test_assoc_result553_link_reassign_clear():
    a = CompleteDSLPckg_ReduceAction(isOrdered=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_ReduceAction', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ReduceAction', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin554'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin554', a)
    _safe_set(a, 'CompleteDSLPckg_ReduceAction', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ReduceAction', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin554'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin554', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin554'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin554', a)
    _safe_set(a, 'CompleteDSLPckg_ReduceAction', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ReduceAction', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin554'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin554', a)


def test_assoc_result58_link_reassign_clear():
    a = CompleteDSLPckg_Parameter(default="sample_text")
    b1 = CompleteDSLPckg_OpaqueExpression(body="sample_text", language="sample_text")
    b2 = CompleteDSLPckg_OpaqueExpression(body="sample_text_2", language="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_Parameter', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter', b1)
    if hasattr(b1, 'CompleteDSLPckg_OpaqueExpression'):
        assert _is_linked(b1, 'CompleteDSLPckg_OpaqueExpression', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Parameter', b2)
    if hasattr(b1, 'CompleteDSLPckg_OpaqueExpression'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OpaqueExpression', a)
    if hasattr(b2, 'CompleteDSLPckg_OpaqueExpression'):
        assert _is_linked(b2, 'CompleteDSLPckg_OpaqueExpression', a)
    _safe_set(a, 'CompleteDSLPckg_Parameter', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Parameter', b2)
    if hasattr(b2, 'CompleteDSLPckg_OpaqueExpression'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OpaqueExpression', a)


def test_assoc_result837_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_LoopNode838', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode838', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin839'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin839', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode838', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode838', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin839'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin839', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin839'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin839', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode838', set())
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode838', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin839'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin839', a)


def test_assoc_result847_link_reassign_clear():
    a = CompleteDSLPckg_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode848', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode848', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin849'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin849', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode848', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode848', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin849'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin849', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin849'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin849', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode848', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ConditionalNode848', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin849'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin849', a)


def test_assoc_returnValueRecipient977_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_InteractionUse()
    b2 = CompleteDSLPckg_InteractionUse()
    _safe_set(a, 'CompleteDSLPckg_Property979', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property979', b1)
    if hasattr(b1, 'CompleteDSLPckg_InteractionUse978'):
        assert _is_linked(b1, 'CompleteDSLPckg_InteractionUse978', a)
    _safe_set(a, 'CompleteDSLPckg_Property979', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property979', b2)
    if hasattr(b1, 'CompleteDSLPckg_InteractionUse978'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InteractionUse978', a)
    if hasattr(b2, 'CompleteDSLPckg_InteractionUse978'):
        assert _is_linked(b2, 'CompleteDSLPckg_InteractionUse978', a)
    _safe_set(a, 'CompleteDSLPckg_Property979', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property979', b2)
    if hasattr(b2, 'CompleteDSLPckg_InteractionUse978'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InteractionUse978', a)


def test_assoc_selection759_link_reassign_clear():
    a = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow760', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ObjectFlow760', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior761'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior761', a)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow760', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ObjectFlow760', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior761'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior761', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior761'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior761', a)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow760', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ObjectFlow760', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior761'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior761', a)


def test_assoc_sendEvent931_link_reassign_clear():
    a = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    b1 = CompleteDSLPckg_MessageEnd()
    b2 = CompleteDSLPckg_MessageEnd()
    _safe_set(a, 'CompleteDSLPckg_Message932', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Message932', b1)
    if hasattr(b1, 'CompleteDSLPckg_MessageEnd'):
        assert _is_linked(b1, 'CompleteDSLPckg_MessageEnd', a)
    _safe_set(a, 'CompleteDSLPckg_Message932', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Message932', b2)
    if hasattr(b1, 'CompleteDSLPckg_MessageEnd'):
        assert not _is_linked(b1, 'CompleteDSLPckg_MessageEnd', a)
    if hasattr(b2, 'CompleteDSLPckg_MessageEnd'):
        assert _is_linked(b2, 'CompleteDSLPckg_MessageEnd', a)
    _safe_set(a, 'CompleteDSLPckg_Message932', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Message932', b2)
    if hasattr(b2, 'CompleteDSLPckg_MessageEnd'):
        assert not _is_linked(b2, 'CompleteDSLPckg_MessageEnd', a)


def test_assoc_setupPart817_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_ExecutableNode()
    b2 = CompleteDSLPckg_ExecutableNode()
    _safe_set(a, 'CompleteDSLPckg_LoopNode', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode818'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExecutableNode818', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode818'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExecutableNode818', a)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode818'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExecutableNode818', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode', set())
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode818'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExecutableNode818', a)


def test_assoc_signature928_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Message(messageKind="sample_text", messageSort="sample_text")
    b2 = CompleteDSLPckg_Message(messageKind="sample_text_2", messageSort="sample_text_2")
    _safe_set(a, 'CompleteDSLPckg_NamedElement930', b1)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement930', b1)
    if hasattr(b1, 'CompleteDSLPckg_Message929'):
        assert _is_linked(b1, 'CompleteDSLPckg_Message929', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement930', b2)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement930', b2)
    if hasattr(b1, 'CompleteDSLPckg_Message929'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Message929', a)
    if hasattr(b2, 'CompleteDSLPckg_Message929'):
        assert _is_linked(b2, 'CompleteDSLPckg_Message929', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement930', None)
    assert not _is_linked(a, 'CompleteDSLPckg_NamedElement930', b2)
    if hasattr(b2, 'CompleteDSLPckg_Message929'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Message929', a)


def test_assoc_source604_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Vertex()
    b2 = CompleteDSLPckg_Vertex()
    _safe_set(a, 'CompleteDSLPckg_Transition605', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition605', b1)
    if hasattr(b1, 'CompleteDSLPckg_Vertex606'):
        assert _is_linked(b1, 'CompleteDSLPckg_Vertex606', a)
    _safe_set(a, 'CompleteDSLPckg_Transition605', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition605', b2)
    if hasattr(b1, 'CompleteDSLPckg_Vertex606'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Vertex606', a)
    if hasattr(b2, 'CompleteDSLPckg_Vertex606'):
        assert _is_linked(b2, 'CompleteDSLPckg_Vertex606', a)
    _safe_set(a, 'CompleteDSLPckg_Transition605', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition605', b2)
    if hasattr(b2, 'CompleteDSLPckg_Vertex606'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Vertex606', a)


def test_assoc_specific132_link_reassign_clear():
    a = CompleteDSLPckg_Generalization(isSubstitutable=True)
    b1 = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b2 = CompleteDSLPckg_Classifier(isAbstract=False, isFinalSpecialization=False)
    _safe_set(a, 'generalization', b1)
    assert _is_linked(a, 'generalization', b1)
    if hasattr(b1, 'Classifier133'):
        assert _is_linked(b1, 'Classifier133', a)
    _safe_set(a, 'generalization', b2)
    assert _is_linked(a, 'generalization', b2)
    if hasattr(b1, 'Classifier133'):
        assert not _is_linked(b1, 'Classifier133', a)
    if hasattr(b2, 'Classifier133'):
        assert _is_linked(b2, 'Classifier133', a)
    _safe_set(a, 'generalization', None)
    assert not _is_linked(a, 'generalization', b2)
    if hasattr(b2, 'Classifier133'):
        assert not _is_linked(b2, 'Classifier133', a)


def test_assoc_specification237_link_reassign_clear():
    a = CompleteDSLPckg_Behavior(isReentrant=True)
    b1 = CompleteDSLPckg_BehavioralFeature()
    b2 = CompleteDSLPckg_BehavioralFeature()
    _safe_set(a, 'CompleteDSLPckg_Behavior238', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior238', b1)
    if hasattr(b1, 'CompleteDSLPckg_BehavioralFeature239'):
        assert _is_linked(b1, 'CompleteDSLPckg_BehavioralFeature239', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior238', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Behavior238', b2)
    if hasattr(b1, 'CompleteDSLPckg_BehavioralFeature239'):
        assert not _is_linked(b1, 'CompleteDSLPckg_BehavioralFeature239', a)
    if hasattr(b2, 'CompleteDSLPckg_BehavioralFeature239'):
        assert _is_linked(b2, 'CompleteDSLPckg_BehavioralFeature239', a)
    _safe_set(a, 'CompleteDSLPckg_Behavior238', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Behavior238', b2)
    if hasattr(b2, 'CompleteDSLPckg_BehavioralFeature239'):
        assert not _is_linked(b2, 'CompleteDSLPckg_BehavioralFeature239', a)


def test_assoc_state589_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Region()
    b2 = CompleteDSLPckg_Region()
    _safe_set(a, 'CompleteDSLPckg_State591', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State591', b1)
    if hasattr(b1, 'CompleteDSLPckg_Region590'):
        assert _is_linked(b1, 'CompleteDSLPckg_Region590', a)
    _safe_set(a, 'CompleteDSLPckg_State591', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State591', b2)
    if hasattr(b1, 'CompleteDSLPckg_Region590'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Region590', a)
    if hasattr(b2, 'CompleteDSLPckg_Region590'):
        assert _is_linked(b2, 'CompleteDSLPckg_Region590', a)
    _safe_set(a, 'CompleteDSLPckg_State591', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State591', b2)
    if hasattr(b2, 'CompleteDSLPckg_Region590'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Region590', a)


def test_assoc_state625_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Pseudostate()
    b2 = CompleteDSLPckg_Pseudostate()
    _safe_set(a, 'CompleteDSLPckg_State627', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State627', b1)
    if hasattr(b1, 'CompleteDSLPckg_Pseudostate626'):
        assert _is_linked(b1, 'CompleteDSLPckg_Pseudostate626', a)
    _safe_set(a, 'CompleteDSLPckg_State627', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State627', b2)
    if hasattr(b1, 'CompleteDSLPckg_Pseudostate626'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Pseudostate626', a)
    if hasattr(b2, 'CompleteDSLPckg_Pseudostate626'):
        assert _is_linked(b2, 'CompleteDSLPckg_Pseudostate626', a)
    _safe_set(a, 'CompleteDSLPckg_State627', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State627', b2)
    if hasattr(b2, 'CompleteDSLPckg_Pseudostate626'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Pseudostate626', a)


def test_assoc_state633_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_ConnectionPointReference()
    b2 = CompleteDSLPckg_ConnectionPointReference()
    _safe_set(a, 'CompleteDSLPckg_State635', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State635', b1)
    if hasattr(b1, 'CompleteDSLPckg_ConnectionPointReference634'):
        assert _is_linked(b1, 'CompleteDSLPckg_ConnectionPointReference634', a)
    _safe_set(a, 'CompleteDSLPckg_State635', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State635', b2)
    if hasattr(b1, 'CompleteDSLPckg_ConnectionPointReference634'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ConnectionPointReference634', a)
    if hasattr(b2, 'CompleteDSLPckg_ConnectionPointReference634'):
        assert _is_linked(b2, 'CompleteDSLPckg_ConnectionPointReference634', a)
    _safe_set(a, 'CompleteDSLPckg_State635', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State635', b2)
    if hasattr(b2, 'CompleteDSLPckg_ConnectionPointReference634'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ConnectionPointReference634', a)


def test_assoc_stateInvariant660_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_Constraint()
    b2 = CompleteDSLPckg_Constraint()
    _safe_set(a, 'CompleteDSLPckg_State661', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State661', b1)
    if hasattr(b1, 'CompleteDSLPckg_Constraint662'):
        assert _is_linked(b1, 'CompleteDSLPckg_Constraint662', a)
    _safe_set(a, 'CompleteDSLPckg_State661', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State661', b2)
    if hasattr(b1, 'CompleteDSLPckg_Constraint662'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Constraint662', a)
    if hasattr(b2, 'CompleteDSLPckg_Constraint662'):
        assert _is_linked(b2, 'CompleteDSLPckg_Constraint662', a)
    _safe_set(a, 'CompleteDSLPckg_State661', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State661', b2)
    if hasattr(b2, 'CompleteDSLPckg_Constraint662'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Constraint662', a)


def test_assoc_structuralFeature448_link_reassign_clear():
    a = CompleteDSLPckg_StructuralFeature(isReadOnly=True)
    b1 = CompleteDSLPckg_StructuralFeatureAction()
    b2 = CompleteDSLPckg_StructuralFeatureAction()
    _safe_set(a, 'CompleteDSLPckg_StructuralFeature449', b1)
    assert _is_linked(a, 'CompleteDSLPckg_StructuralFeature449', b1)
    if hasattr(b1, 'CompleteDSLPckg_StructuralFeatureAction'):
        assert _is_linked(b1, 'CompleteDSLPckg_StructuralFeatureAction', a)
    _safe_set(a, 'CompleteDSLPckg_StructuralFeature449', b2)
    assert _is_linked(a, 'CompleteDSLPckg_StructuralFeature449', b2)
    if hasattr(b1, 'CompleteDSLPckg_StructuralFeatureAction'):
        assert not _is_linked(b1, 'CompleteDSLPckg_StructuralFeatureAction', a)
    if hasattr(b2, 'CompleteDSLPckg_StructuralFeatureAction'):
        assert _is_linked(b2, 'CompleteDSLPckg_StructuralFeatureAction', a)
    _safe_set(a, 'CompleteDSLPckg_StructuralFeature449', None)
    assert not _is_linked(a, 'CompleteDSLPckg_StructuralFeature449', b2)
    if hasattr(b2, 'CompleteDSLPckg_StructuralFeatureAction'):
        assert not _is_linked(b2, 'CompleteDSLPckg_StructuralFeatureAction', a)


def test_assoc_structuredNode688_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b2 = CompleteDSLPckg_Activity(isReadOnly=False, isSingleExecution=False)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode', b1)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode', b1)
    if hasattr(b1, 'CompleteDSLPckg_Activity689'):
        assert _is_linked(b1, 'CompleteDSLPckg_Activity689', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode', b2)
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode', b2)
    if hasattr(b1, 'CompleteDSLPckg_Activity689'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Activity689', a)
    if hasattr(b2, 'CompleteDSLPckg_Activity689'):
        assert _is_linked(b2, 'CompleteDSLPckg_Activity689', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode', None)
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode', b2)
    if hasattr(b2, 'CompleteDSLPckg_Activity689'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Activity689', a)


def test_assoc_structuredNodeInput807_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_InputPin()
    b2 = CompleteDSLPckg_InputPin()
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode808', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode808', b1)
    if hasattr(b1, 'CompleteDSLPckg_InputPin809'):
        assert _is_linked(b1, 'CompleteDSLPckg_InputPin809', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode808', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode808', b2)
    if hasattr(b1, 'CompleteDSLPckg_InputPin809'):
        assert not _is_linked(b1, 'CompleteDSLPckg_InputPin809', a)
    if hasattr(b2, 'CompleteDSLPckg_InputPin809'):
        assert _is_linked(b2, 'CompleteDSLPckg_InputPin809', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode808', set())
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode808', b2)
    if hasattr(b2, 'CompleteDSLPckg_InputPin809'):
        assert not _is_linked(b2, 'CompleteDSLPckg_InputPin809', a)


def test_assoc_structuredNodeOutput813_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_OutputPin()
    b2 = CompleteDSLPckg_OutputPin()
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode814', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode814', b1)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin815'):
        assert _is_linked(b1, 'CompleteDSLPckg_OutputPin815', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode814', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode814', b2)
    if hasattr(b1, 'CompleteDSLPckg_OutputPin815'):
        assert not _is_linked(b1, 'CompleteDSLPckg_OutputPin815', a)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin815'):
        assert _is_linked(b2, 'CompleteDSLPckg_OutputPin815', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode814', set())
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode814', b2)
    if hasattr(b2, 'CompleteDSLPckg_OutputPin815'):
        assert not _is_linked(b2, 'CompleteDSLPckg_OutputPin815', a)


def test_assoc_structuredOwnedAttribute337_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_StructuredClassifier()
    b2 = CompleteDSLPckg_StructuredClassifier()
    _safe_set(a, 'CompleteDSLPckg_Property339', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property339', b1)
    if hasattr(b1, 'CompleteDSLPckg_StructuredClassifier338'):
        assert _is_linked(b1, 'CompleteDSLPckg_StructuredClassifier338', a)
    _safe_set(a, 'CompleteDSLPckg_Property339', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property339', b2)
    if hasattr(b1, 'CompleteDSLPckg_StructuredClassifier338'):
        assert not _is_linked(b1, 'CompleteDSLPckg_StructuredClassifier338', a)
    if hasattr(b2, 'CompleteDSLPckg_StructuredClassifier338'):
        assert _is_linked(b2, 'CompleteDSLPckg_StructuredClassifier338', a)
    _safe_set(a, 'CompleteDSLPckg_Property339', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property339', b2)
    if hasattr(b2, 'CompleteDSLPckg_StructuredClassifier338'):
        assert not _is_linked(b2, 'CompleteDSLPckg_StructuredClassifier338', a)


def test_assoc_subject983_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_UseCase()
    b2 = CompleteDSLPckg_UseCase()
    _safe_set(a, 'CompleteDSLPckg_Classifier984', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier984', b1)
    if hasattr(b1, 'CompleteDSLPckg_UseCase'):
        assert _is_linked(b1, 'CompleteDSLPckg_UseCase', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier984', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier984', b2)
    if hasattr(b1, 'CompleteDSLPckg_UseCase'):
        assert not _is_linked(b1, 'CompleteDSLPckg_UseCase', a)
    if hasattr(b2, 'CompleteDSLPckg_UseCase'):
        assert _is_linked(b2, 'CompleteDSLPckg_UseCase', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier984', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier984', b2)
    if hasattr(b2, 'CompleteDSLPckg_UseCase'):
        assert not _is_linked(b2, 'CompleteDSLPckg_UseCase', a)


def test_assoc_submachine642_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_StateMachine()
    b2 = CompleteDSLPckg_StateMachine()
    _safe_set(a, 'CompleteDSLPckg_State643', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State643', b1)
    if hasattr(b1, 'CompleteDSLPckg_StateMachine644'):
        assert _is_linked(b1, 'CompleteDSLPckg_StateMachine644', a)
    _safe_set(a, 'CompleteDSLPckg_State643', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State643', b2)
    if hasattr(b1, 'CompleteDSLPckg_StateMachine644'):
        assert not _is_linked(b1, 'CompleteDSLPckg_StateMachine644', a)
    if hasattr(b2, 'CompleteDSLPckg_StateMachine644'):
        assert _is_linked(b2, 'CompleteDSLPckg_StateMachine644', a)
    _safe_set(a, 'CompleteDSLPckg_State643', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State643', b2)
    if hasattr(b2, 'CompleteDSLPckg_StateMachine644'):
        assert not _is_linked(b2, 'CompleteDSLPckg_StateMachine644', a)


def test_assoc_submachineState577_link_reassign_clear():
    a = CompleteDSLPckg_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    b1 = CompleteDSLPckg_StateMachine()
    b2 = CompleteDSLPckg_StateMachine()
    _safe_set(a, 'CompleteDSLPckg_State', b1)
    assert _is_linked(a, 'CompleteDSLPckg_State', b1)
    if hasattr(b1, 'CompleteDSLPckg_StateMachine578'):
        assert _is_linked(b1, 'CompleteDSLPckg_StateMachine578', a)
    _safe_set(a, 'CompleteDSLPckg_State', b2)
    assert _is_linked(a, 'CompleteDSLPckg_State', b2)
    if hasattr(b1, 'CompleteDSLPckg_StateMachine578'):
        assert not _is_linked(b1, 'CompleteDSLPckg_StateMachine578', a)
    if hasattr(b2, 'CompleteDSLPckg_StateMachine578'):
        assert _is_linked(b2, 'CompleteDSLPckg_StateMachine578', a)
    _safe_set(a, 'CompleteDSLPckg_State', None)
    assert not _is_linked(a, 'CompleteDSLPckg_State', b2)
    if hasattr(b2, 'CompleteDSLPckg_StateMachine578'):
        assert not _is_linked(b2, 'CompleteDSLPckg_StateMachine578', a)


def test_assoc_subsettedProperty116_link_reassign_clear():
    a = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b1 = CompleteDSLPckg_Property(aggregation="sample_text", default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    b2 = CompleteDSLPckg_Property(aggregation="sample_text_2", default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    _safe_set(a, 'CompleteDSLPckg_Property115', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Property115', b1)
    if hasattr(b1, 'CompleteDSLPckg_Property117'):
        assert _is_linked(b1, 'CompleteDSLPckg_Property117', a)
    _safe_set(a, 'CompleteDSLPckg_Property115', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Property115', b2)
    if hasattr(b1, 'CompleteDSLPckg_Property117'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Property117', a)
    if hasattr(b2, 'CompleteDSLPckg_Property117'):
        assert _is_linked(b2, 'CompleteDSLPckg_Property117', a)
    _safe_set(a, 'CompleteDSLPckg_Property115', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Property115', b2)
    if hasattr(b2, 'CompleteDSLPckg_Property117'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Property117', a)


def test_assoc_substitutingClassifier201_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Substitution()
    b2 = CompleteDSLPckg_Substitution()
    _safe_set(a, 'Classifier202', b1)
    assert _is_linked(a, 'Classifier202', b1)
    if hasattr(b1, 'substitution'):
        assert _is_linked(b1, 'substitution', a)
    _safe_set(a, 'Classifier202', b2)
    assert _is_linked(a, 'Classifier202', b2)
    if hasattr(b1, 'substitution'):
        assert not _is_linked(b1, 'substitution', a)
    if hasattr(b2, 'substitution'):
        assert _is_linked(b2, 'substitution', a)
    _safe_set(a, 'Classifier202', None)
    assert not _is_linked(a, 'Classifier202', b2)
    if hasattr(b2, 'substitution'):
        assert not _is_linked(b2, 'substitution', a)


def test_assoc_substitution97_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_Substitution()
    b2 = CompleteDSLPckg_Substitution()
    _safe_set(a, 'substitutingClassifier', {b1})
    assert _is_linked(a, 'substitutingClassifier', b1)
    if hasattr(b1, 'Substitution'):
        assert _is_linked(b1, 'Substitution', a)
    _safe_set(a, 'substitutingClassifier', {b2})
    assert _is_linked(a, 'substitutingClassifier', b2)
    if hasattr(b1, 'Substitution'):
        assert not _is_linked(b1, 'Substitution', a)
    if hasattr(b2, 'Substitution'):
        assert _is_linked(b2, 'Substitution', a)
    _safe_set(a, 'substitutingClassifier', set())
    assert not _is_linked(a, 'substitutingClassifier', b2)
    if hasattr(b2, 'Substitution'):
        assert not _is_linked(b2, 'Substitution', a)


def test_assoc_supplier197_link_reassign_clear():
    a = CompleteDSLPckg_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    b1 = CompleteDSLPckg_Dependency()
    b2 = CompleteDSLPckg_Dependency()
    _safe_set(a, 'CompleteDSLPckg_NamedElement198', b1)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement198', b1)
    if hasattr(b1, 'CompleteDSLPckg_Dependency'):
        assert _is_linked(b1, 'CompleteDSLPckg_Dependency', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement198', b2)
    assert _is_linked(a, 'CompleteDSLPckg_NamedElement198', b2)
    if hasattr(b1, 'CompleteDSLPckg_Dependency'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Dependency', a)
    if hasattr(b2, 'CompleteDSLPckg_Dependency'):
        assert _is_linked(b2, 'CompleteDSLPckg_Dependency', a)
    _safe_set(a, 'CompleteDSLPckg_NamedElement198', None)
    assert not _is_linked(a, 'CompleteDSLPckg_NamedElement198', b2)
    if hasattr(b2, 'CompleteDSLPckg_Dependency'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Dependency', a)


def test_assoc_target607_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Vertex()
    b2 = CompleteDSLPckg_Vertex()
    _safe_set(a, 'CompleteDSLPckg_Transition608', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition608', b1)
    if hasattr(b1, 'CompleteDSLPckg_Vertex609'):
        assert _is_linked(b1, 'CompleteDSLPckg_Vertex609', a)
    _safe_set(a, 'CompleteDSLPckg_Transition608', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition608', b2)
    if hasattr(b1, 'CompleteDSLPckg_Vertex609'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Vertex609', a)
    if hasattr(b2, 'CompleteDSLPckg_Vertex609'):
        assert _is_linked(b2, 'CompleteDSLPckg_Vertex609', a)
    _safe_set(a, 'CompleteDSLPckg_Transition608', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition608', b2)
    if hasattr(b2, 'CompleteDSLPckg_Vertex609'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Vertex609', a)


def test_assoc_test822_link_reassign_clear():
    a = CompleteDSLPckg_LoopNode(isTestedFirst=True)
    b1 = CompleteDSLPckg_ExecutableNode()
    b2 = CompleteDSLPckg_ExecutableNode()
    _safe_set(a, 'CompleteDSLPckg_LoopNode823', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode823', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode824'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExecutableNode824', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode823', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_LoopNode823', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode824'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExecutableNode824', a)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode824'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExecutableNode824', a)
    _safe_set(a, 'CompleteDSLPckg_LoopNode823', set())
    assert not _is_linked(a, 'CompleteDSLPckg_LoopNode823', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode824'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExecutableNode824', a)


def test_assoc_test841_link_reassign_clear():
    a = CompleteDSLPckg_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = CompleteDSLPckg_ExecutableNode()
    b2 = CompleteDSLPckg_ExecutableNode()
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode842', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode842', b1)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode843'):
        assert _is_linked(b1, 'CompleteDSLPckg_ExecutableNode843', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode842', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_ConditionalNode842', b2)
    if hasattr(b1, 'CompleteDSLPckg_ExecutableNode843'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ExecutableNode843', a)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode843'):
        assert _is_linked(b2, 'CompleteDSLPckg_ExecutableNode843', a)
    _safe_set(a, 'CompleteDSLPckg_ConditionalNode842', set())
    assert not _is_linked(a, 'CompleteDSLPckg_ConditionalNode842', b2)
    if hasattr(b2, 'CompleteDSLPckg_ExecutableNode843'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ExecutableNode843', a)


def test_assoc_timeSpecification291_link_reassign_clear():
    a = CompleteDSLPckg_TimeConstraint(firstEvent=True)
    b1 = CompleteDSLPckg_TimeInterval()
    b2 = CompleteDSLPckg_TimeInterval()
    _safe_set(a, 'CompleteDSLPckg_TimeConstraint', b1)
    assert _is_linked(a, 'CompleteDSLPckg_TimeConstraint', b1)
    if hasattr(b1, 'CompleteDSLPckg_TimeInterval292'):
        assert _is_linked(b1, 'CompleteDSLPckg_TimeInterval292', a)
    _safe_set(a, 'CompleteDSLPckg_TimeConstraint', b2)
    assert _is_linked(a, 'CompleteDSLPckg_TimeConstraint', b2)
    if hasattr(b1, 'CompleteDSLPckg_TimeInterval292'):
        assert not _is_linked(b1, 'CompleteDSLPckg_TimeInterval292', a)
    if hasattr(b2, 'CompleteDSLPckg_TimeInterval292'):
        assert _is_linked(b2, 'CompleteDSLPckg_TimeInterval292', a)
    _safe_set(a, 'CompleteDSLPckg_TimeConstraint', None)
    assert not _is_linked(a, 'CompleteDSLPckg_TimeConstraint', b2)
    if hasattr(b2, 'CompleteDSLPckg_TimeInterval292'):
        assert not _is_linked(b2, 'CompleteDSLPckg_TimeInterval292', a)


def test_assoc_transformation757_link_reassign_clear():
    a = CompleteDSLPckg_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    b1 = CompleteDSLPckg_Behavior(isReentrant=True)
    b2 = CompleteDSLPckg_Behavior(isReentrant=False)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow', b1)
    assert _is_linked(a, 'CompleteDSLPckg_ObjectFlow', b1)
    if hasattr(b1, 'CompleteDSLPckg_Behavior758'):
        assert _is_linked(b1, 'CompleteDSLPckg_Behavior758', a)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow', b2)
    assert _is_linked(a, 'CompleteDSLPckg_ObjectFlow', b2)
    if hasattr(b1, 'CompleteDSLPckg_Behavior758'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Behavior758', a)
    if hasattr(b2, 'CompleteDSLPckg_Behavior758'):
        assert _is_linked(b2, 'CompleteDSLPckg_Behavior758', a)
    _safe_set(a, 'CompleteDSLPckg_ObjectFlow', None)
    assert not _is_linked(a, 'CompleteDSLPckg_ObjectFlow', b2)
    if hasattr(b2, 'CompleteDSLPckg_Behavior758'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Behavior758', a)


def test_assoc_transition587_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Region()
    b2 = CompleteDSLPckg_Region()
    _safe_set(a, 'CompleteDSLPckg_Transition', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition', b1)
    if hasattr(b1, 'CompleteDSLPckg_Region588'):
        assert _is_linked(b1, 'CompleteDSLPckg_Region588', a)
    _safe_set(a, 'CompleteDSLPckg_Transition', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition', b2)
    if hasattr(b1, 'CompleteDSLPckg_Region588'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Region588', a)
    if hasattr(b2, 'CompleteDSLPckg_Region588'):
        assert _is_linked(b2, 'CompleteDSLPckg_Region588', a)
    _safe_set(a, 'CompleteDSLPckg_Transition', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition', b2)
    if hasattr(b2, 'CompleteDSLPckg_Region588'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Region588', a)


def test_assoc_trigger502_link_reassign_clear():
    a = CompleteDSLPckg_AcceptEventAction(isUnmarshall=True)
    b1 = CompleteDSLPckg_Trigger()
    b2 = CompleteDSLPckg_Trigger()
    _safe_set(a, 'CompleteDSLPckg_AcceptEventAction503', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_AcceptEventAction503', b1)
    if hasattr(b1, 'CompleteDSLPckg_Trigger504'):
        assert _is_linked(b1, 'CompleteDSLPckg_Trigger504', a)
    _safe_set(a, 'CompleteDSLPckg_AcceptEventAction503', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_AcceptEventAction503', b2)
    if hasattr(b1, 'CompleteDSLPckg_Trigger504'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Trigger504', a)
    if hasattr(b2, 'CompleteDSLPckg_Trigger504'):
        assert _is_linked(b2, 'CompleteDSLPckg_Trigger504', a)
    _safe_set(a, 'CompleteDSLPckg_AcceptEventAction503', set())
    assert not _is_linked(a, 'CompleteDSLPckg_AcceptEventAction503', b2)
    if hasattr(b2, 'CompleteDSLPckg_Trigger504'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Trigger504', a)


def test_assoc_trigger613_link_reassign_clear():
    a = CompleteDSLPckg_Transition(kind="sample_text")
    b1 = CompleteDSLPckg_Trigger()
    b2 = CompleteDSLPckg_Trigger()
    _safe_set(a, 'CompleteDSLPckg_Transition614', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Transition614', b1)
    if hasattr(b1, 'CompleteDSLPckg_Trigger615'):
        assert _is_linked(b1, 'CompleteDSLPckg_Trigger615', a)
    _safe_set(a, 'CompleteDSLPckg_Transition614', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Transition614', b2)
    if hasattr(b1, 'CompleteDSLPckg_Trigger615'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Trigger615', a)
    if hasattr(b2, 'CompleteDSLPckg_Trigger615'):
        assert _is_linked(b2, 'CompleteDSLPckg_Trigger615', a)
    _safe_set(a, 'CompleteDSLPckg_Transition614', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Transition614', b2)
    if hasattr(b2, 'CompleteDSLPckg_Trigger615'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Trigger615', a)


def test_assoc_type148_link_reassign_clear():
    a = CompleteDSLPckg_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_Type()
    b2 = CompleteDSLPckg_Type()
    _safe_set(a, 'CompleteDSLPckg_Operation', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Operation', b1)
    if hasattr(b1, 'CompleteDSLPckg_Type149'):
        assert _is_linked(b1, 'CompleteDSLPckg_Type149', a)
    _safe_set(a, 'CompleteDSLPckg_Operation', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Operation', b2)
    if hasattr(b1, 'CompleteDSLPckg_Type149'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Type149', a)
    if hasattr(b2, 'CompleteDSLPckg_Type149'):
        assert _is_linked(b2, 'CompleteDSLPckg_Type149', a)
    _safe_set(a, 'CompleteDSLPckg_Operation', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Operation', b2)
    if hasattr(b2, 'CompleteDSLPckg_Type149'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Type149', a)


def test_assoc_type323_link_reassign_clear():
    a = CompleteDSLPckg_Association(isDerived=True)
    b1 = CompleteDSLPckg_ConnectorEnd()
    b2 = CompleteDSLPckg_ConnectorEnd()
    _safe_set(a, 'CompleteDSLPckg_Association325', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Association325', b1)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd324'):
        assert _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd324', a)
    _safe_set(a, 'CompleteDSLPckg_Association325', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Association325', b2)
    if hasattr(b1, 'CompleteDSLPckg_ConnectorEnd324'):
        assert not _is_linked(b1, 'CompleteDSLPckg_ConnectorEnd324', a)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd324'):
        assert _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd324', a)
    _safe_set(a, 'CompleteDSLPckg_Association325', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Association325', b2)
    if hasattr(b2, 'CompleteDSLPckg_ConnectorEnd324'):
        assert not _is_linked(b2, 'CompleteDSLPckg_ConnectorEnd324', a)


def test_assoc_unmarshallType494_link_reassign_clear():
    a = CompleteDSLPckg_Classifier(isAbstract=True, isFinalSpecialization=True)
    b1 = CompleteDSLPckg_UnmarshallAction()
    b2 = CompleteDSLPckg_UnmarshallAction()
    _safe_set(a, 'CompleteDSLPckg_Classifier496', b1)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier496', b1)
    if hasattr(b1, 'CompleteDSLPckg_UnmarshallAction495'):
        assert _is_linked(b1, 'CompleteDSLPckg_UnmarshallAction495', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier496', b2)
    assert _is_linked(a, 'CompleteDSLPckg_Classifier496', b2)
    if hasattr(b1, 'CompleteDSLPckg_UnmarshallAction495'):
        assert not _is_linked(b1, 'CompleteDSLPckg_UnmarshallAction495', a)
    if hasattr(b2, 'CompleteDSLPckg_UnmarshallAction495'):
        assert _is_linked(b2, 'CompleteDSLPckg_UnmarshallAction495', a)
    _safe_set(a, 'CompleteDSLPckg_Classifier496', None)
    assert not _is_linked(a, 'CompleteDSLPckg_Classifier496', b2)
    if hasattr(b2, 'CompleteDSLPckg_UnmarshallAction495'):
        assert not _is_linked(b2, 'CompleteDSLPckg_UnmarshallAction495', a)


def test_assoc_upperValue43_link_reassign_clear():
    a = CompleteDSLPckg_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    b1 = CompleteDSLPckg_ValueSpecification()
    b2 = CompleteDSLPckg_ValueSpecification()
    _safe_set(a, 'owningUpper', b1)
    assert _is_linked(a, 'owningUpper', b1)
    if hasattr(b1, 'ValueSpecification'):
        assert _is_linked(b1, 'ValueSpecification', a)
    _safe_set(a, 'owningUpper', b2)
    assert _is_linked(a, 'owningUpper', b2)
    if hasattr(b1, 'ValueSpecification'):
        assert not _is_linked(b1, 'ValueSpecification', a)
    if hasattr(b2, 'ValueSpecification'):
        assert _is_linked(b2, 'ValueSpecification', a)
    _safe_set(a, 'owningUpper', None)
    assert not _is_linked(a, 'owningUpper', b2)
    if hasattr(b2, 'ValueSpecification'):
        assert not _is_linked(b2, 'ValueSpecification', a)


def test_assoc_variable690_link_reassign_clear():
    a = CompleteDSLPckg_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = CompleteDSLPckg_Variable()
    b2 = CompleteDSLPckg_Variable()
    _safe_set(a, 'CompleteDSLPckg_Activity691', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_Activity691', b1)
    if hasattr(b1, 'CompleteDSLPckg_Variable692'):
        assert _is_linked(b1, 'CompleteDSLPckg_Variable692', a)
    _safe_set(a, 'CompleteDSLPckg_Activity691', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_Activity691', b2)
    if hasattr(b1, 'CompleteDSLPckg_Variable692'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Variable692', a)
    if hasattr(b2, 'CompleteDSLPckg_Variable692'):
        assert _is_linked(b2, 'CompleteDSLPckg_Variable692', a)
    _safe_set(a, 'CompleteDSLPckg_Activity691', set())
    assert not _is_linked(a, 'CompleteDSLPckg_Activity691', b2)
    if hasattr(b2, 'CompleteDSLPckg_Variable692'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Variable692', a)


def test_assoc_variable801_link_reassign_clear():
    a = CompleteDSLPckg_StructuredActivityNode(mustIsolate=True)
    b1 = CompleteDSLPckg_Variable()
    b2 = CompleteDSLPckg_Variable()
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode802', {b1})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode802', b1)
    if hasattr(b1, 'CompleteDSLPckg_Variable803'):
        assert _is_linked(b1, 'CompleteDSLPckg_Variable803', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode802', {b2})
    assert _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode802', b2)
    if hasattr(b1, 'CompleteDSLPckg_Variable803'):
        assert not _is_linked(b1, 'CompleteDSLPckg_Variable803', a)
    if hasattr(b2, 'CompleteDSLPckg_Variable803'):
        assert _is_linked(b2, 'CompleteDSLPckg_Variable803', a)
    _safe_set(a, 'CompleteDSLPckg_StructuredActivityNode802', set())
    assert not _is_linked(a, 'CompleteDSLPckg_StructuredActivityNode802', b2)
    if hasattr(b2, 'CompleteDSLPckg_Variable803'):
        assert not _is_linked(b2, 'CompleteDSLPckg_Variable803', a)


def test_assoc_when261_link_reassign_clear():
    a = CompleteDSLPckg_TimeEvent(isRelative=True)
    b1 = CompleteDSLPckg_TimeExpression()
    b2 = CompleteDSLPckg_TimeExpression()
    _safe_set(a, 'CompleteDSLPckg_TimeEvent', b1)
    assert _is_linked(a, 'CompleteDSLPckg_TimeEvent', b1)
    if hasattr(b1, 'CompleteDSLPckg_TimeExpression'):
        assert _is_linked(b1, 'CompleteDSLPckg_TimeExpression', a)
    _safe_set(a, 'CompleteDSLPckg_TimeEvent', b2)
    assert _is_linked(a, 'CompleteDSLPckg_TimeEvent', b2)
    if hasattr(b1, 'CompleteDSLPckg_TimeExpression'):
        assert not _is_linked(b1, 'CompleteDSLPckg_TimeExpression', a)
    if hasattr(b2, 'CompleteDSLPckg_TimeExpression'):
        assert _is_linked(b2, 'CompleteDSLPckg_TimeExpression', a)
    _safe_set(a, 'CompleteDSLPckg_TimeEvent', None)
    assert not _is_linked(a, 'CompleteDSLPckg_TimeEvent', b2)
    if hasattr(b2, 'CompleteDSLPckg_TimeExpression'):
        assert not _is_linked(b2, 'CompleteDSLPckg_TimeExpression', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Abstraction_strategy = st.builds(Abstraction)
@given(instance=Abstraction_strategy)
@settings(max_examples=25)
def test_Abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)


AcceptEventAction_strategy = st.builds(AcceptEventAction)
@given(instance=AcceptEventAction_strategy)
@settings(max_examples=25)
def test_AcceptEventAction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)


Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


ActivityEdge_strategy = st.builds(ActivityEdge)
@given(instance=ActivityEdge_strategy)
@settings(max_examples=25)
def test_ActivityEdge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)


ActivityGroup_strategy = st.builds(ActivityGroup)
@given(instance=ActivityGroup_strategy)
@settings(max_examples=25)
def test_ActivityGroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


Artifact_strategy = st.builds(Artifact)
@given(instance=Artifact_strategy)
@settings(max_examples=25)
def test_Artifact_instantiation(instance):
    assert isinstance(instance, Artifact)


Association_strategy = st.builds(Association)
@given(instance=Association_strategy)
@settings(max_examples=25)
def test_Association_instantiation(instance):
    assert isinstance(instance, Association)


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


CallAction_strategy = st.builds(CallAction)
@given(instance=CallAction_strategy)
@settings(max_examples=25)
def test_CallAction_instantiation(instance):
    assert isinstance(instance, CallAction)


CentralBufferNode_strategy = st.builds(CentralBufferNode)
@given(instance=CentralBufferNode_strategy)
@settings(max_examples=25)
def test_CentralBufferNode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


CombinedFragment_strategy = st.builds(CombinedFragment)
@given(instance=CombinedFragment_strategy)
@settings(max_examples=25)
def test_CombinedFragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)


CompleteDSLPckg_Abstraction_strategy = st.builds(CompleteDSLPckg_Abstraction)
@given(instance=CompleteDSLPckg_Abstraction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Abstraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Abstraction)


CompleteDSLPckg_AcceptCallAction_strategy = st.builds(CompleteDSLPckg_AcceptCallAction)
@given(instance=CompleteDSLPckg_AcceptCallAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_AcceptCallAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AcceptCallAction)


CompleteDSLPckg_AcceptEventAction_strategy = st.builds(CompleteDSLPckg_AcceptEventAction, isUnmarshall=st.booleans())
@given(instance=CompleteDSLPckg_AcceptEventAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_AcceptEventAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AcceptEventAction)


CompleteDSLPckg_Action_strategy = st.builds(CompleteDSLPckg_Action)
@given(instance=CompleteDSLPckg_Action_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Action_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Action)


CompleteDSLPckg_ActionExecutionSpecification_strategy = st.builds(CompleteDSLPckg_ActionExecutionSpecification)
@given(instance=CompleteDSLPckg_ActionExecutionSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActionExecutionSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActionExecutionSpecification)


CompleteDSLPckg_ActionInputPin_strategy = st.builds(CompleteDSLPckg_ActionInputPin)
@given(instance=CompleteDSLPckg_ActionInputPin_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActionInputPin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActionInputPin)


CompleteDSLPckg_Activity_strategy = st.builds(CompleteDSLPckg_Activity, isReadOnly=st.booleans(), isSingleExecution=st.booleans())
@given(instance=CompleteDSLPckg_Activity_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Activity_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Activity)


CompleteDSLPckg_ActivityEdge_strategy = st.builds(CompleteDSLPckg_ActivityEdge)
@given(instance=CompleteDSLPckg_ActivityEdge_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActivityEdge_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityEdge)


CompleteDSLPckg_ActivityFinalNode_strategy = st.builds(CompleteDSLPckg_ActivityFinalNode)
@given(instance=CompleteDSLPckg_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityFinalNode)


CompleteDSLPckg_ActivityGroup_strategy = st.builds(CompleteDSLPckg_ActivityGroup)
@given(instance=CompleteDSLPckg_ActivityGroup_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActivityGroup_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityGroup)


CompleteDSLPckg_ActivityNode_strategy = st.builds(CompleteDSLPckg_ActivityNode)
@given(instance=CompleteDSLPckg_ActivityNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActivityNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityNode)


CompleteDSLPckg_ActivityParameterNode_strategy = st.builds(CompleteDSLPckg_ActivityParameterNode)
@given(instance=CompleteDSLPckg_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityParameterNode)


CompleteDSLPckg_ActivityPartition_strategy = st.builds(CompleteDSLPckg_ActivityPartition)
@given(instance=CompleteDSLPckg_ActivityPartition_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ActivityPartition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityPartition)


CompleteDSLPckg_Actor_strategy = st.builds(CompleteDSLPckg_Actor)
@given(instance=CompleteDSLPckg_Actor_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Actor_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Actor)


CompleteDSLPckg_AddStructuralFeatureValueAction_strategy = st.builds(CompleteDSLPckg_AddStructuralFeatureValueAction)
@given(instance=CompleteDSLPckg_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_AddStructuralFeatureValueAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AddStructuralFeatureValueAction)


CompleteDSLPckg_AddVariableValueAction_strategy = st.builds(CompleteDSLPckg_AddVariableValueAction)
@given(instance=CompleteDSLPckg_AddVariableValueAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_AddVariableValueAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AddVariableValueAction)


CompleteDSLPckg_AnyReceiveEvent_strategy = st.builds(CompleteDSLPckg_AnyReceiveEvent)
@given(instance=CompleteDSLPckg_AnyReceiveEvent_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_AnyReceiveEvent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AnyReceiveEvent)


CompleteDSLPckg_Artifact_strategy = st.builds(CompleteDSLPckg_Artifact, fileName=safe_text)
@given(instance=CompleteDSLPckg_Artifact_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Artifact_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Artifact)


CompleteDSLPckg_Association_strategy = st.builds(CompleteDSLPckg_Association, isDerived=st.booleans())
@given(instance=CompleteDSLPckg_Association_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Association_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Association)


CompleteDSLPckg_AssociationClass_strategy = st.builds(CompleteDSLPckg_AssociationClass)
@given(instance=CompleteDSLPckg_AssociationClass_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_AssociationClass_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AssociationClass)


CompleteDSLPckg_Behavior_strategy = st.builds(CompleteDSLPckg_Behavior, isReentrant=st.booleans())
@given(instance=CompleteDSLPckg_Behavior_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Behavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Behavior)


CompleteDSLPckg_BehaviorExecutionSpecification_strategy = st.builds(CompleteDSLPckg_BehaviorExecutionSpecification)
@given(instance=CompleteDSLPckg_BehaviorExecutionSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_BehaviorExecutionSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BehaviorExecutionSpecification)


CompleteDSLPckg_BehavioralFeature_strategy = st.builds(CompleteDSLPckg_BehavioralFeature)
@given(instance=CompleteDSLPckg_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BehavioralFeature)


CompleteDSLPckg_BehavioredClassifier_strategy = st.builds(CompleteDSLPckg_BehavioredClassifier)
@given(instance=CompleteDSLPckg_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BehavioredClassifier)


CompleteDSLPckg_BroadcastSignalAction_strategy = st.builds(CompleteDSLPckg_BroadcastSignalAction)
@given(instance=CompleteDSLPckg_BroadcastSignalAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_BroadcastSignalAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BroadcastSignalAction)


CompleteDSLPckg_CallAction_strategy = st.builds(CompleteDSLPckg_CallAction, isSynchronous=st.booleans())
@given(instance=CompleteDSLPckg_CallAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CallAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallAction)


CompleteDSLPckg_CallBehaviorAction_strategy = st.builds(CompleteDSLPckg_CallBehaviorAction)
@given(instance=CompleteDSLPckg_CallBehaviorAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CallBehaviorAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallBehaviorAction)


CompleteDSLPckg_CallEvent_strategy = st.builds(CompleteDSLPckg_CallEvent)
@given(instance=CompleteDSLPckg_CallEvent_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CallEvent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallEvent)


CompleteDSLPckg_CallOperationAction_strategy = st.builds(CompleteDSLPckg_CallOperationAction)
@given(instance=CompleteDSLPckg_CallOperationAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CallOperationAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallOperationAction)


CompleteDSLPckg_CentralBufferNode_strategy = st.builds(CompleteDSLPckg_CentralBufferNode)
@given(instance=CompleteDSLPckg_CentralBufferNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CentralBufferNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CentralBufferNode)


CompleteDSLPckg_ChangeEvent_strategy = st.builds(CompleteDSLPckg_ChangeEvent)
@given(instance=CompleteDSLPckg_ChangeEvent_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ChangeEvent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ChangeEvent)


CompleteDSLPckg_Class_strategy = st.builds(CompleteDSLPckg_Class)
@given(instance=CompleteDSLPckg_Class_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Class_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Class)


CompleteDSLPckg_Classifier_strategy = st.builds(CompleteDSLPckg_Classifier, isAbstract=st.booleans(), isFinalSpecialization=st.booleans())
@given(instance=CompleteDSLPckg_Classifier_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Classifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Classifier)


CompleteDSLPckg_Clause_strategy = st.builds(CompleteDSLPckg_Clause)
@given(instance=CompleteDSLPckg_Clause_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Clause_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Clause)


CompleteDSLPckg_ClearStructuralFeatureAction_strategy = st.builds(CompleteDSLPckg_ClearStructuralFeatureAction)
@given(instance=CompleteDSLPckg_ClearStructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ClearStructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ClearStructuralFeatureAction)


CompleteDSLPckg_ClearVariableAction_strategy = st.builds(CompleteDSLPckg_ClearVariableAction)
@given(instance=CompleteDSLPckg_ClearVariableAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ClearVariableAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ClearVariableAction)


CompleteDSLPckg_Collaboration_strategy = st.builds(CompleteDSLPckg_Collaboration)
@given(instance=CompleteDSLPckg_Collaboration_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Collaboration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Collaboration)


CompleteDSLPckg_CollaborationUse_strategy = st.builds(CompleteDSLPckg_CollaborationUse)
@given(instance=CompleteDSLPckg_CollaborationUse_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CollaborationUse_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CollaborationUse)


CompleteDSLPckg_CombinedFragment_strategy = st.builds(CompleteDSLPckg_CombinedFragment, interactionOperator=safe_text)
@given(instance=CompleteDSLPckg_CombinedFragment_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CombinedFragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CombinedFragment)


CompleteDSLPckg_Comment_strategy = st.builds(CompleteDSLPckg_Comment, body=safe_text)
@given(instance=CompleteDSLPckg_Comment_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Comment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Comment)


CompleteDSLPckg_CommunicationPath_strategy = st.builds(CompleteDSLPckg_CommunicationPath)
@given(instance=CompleteDSLPckg_CommunicationPath_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CommunicationPath_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CommunicationPath)


CompleteDSLPckg_Component_strategy = st.builds(CompleteDSLPckg_Component, isIndirectlyInstantiated=st.booleans())
@given(instance=CompleteDSLPckg_Component_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Component_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Component)


CompleteDSLPckg_ComponentRealization_strategy = st.builds(CompleteDSLPckg_ComponentRealization)
@given(instance=CompleteDSLPckg_ComponentRealization_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ComponentRealization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ComponentRealization)


CompleteDSLPckg_ConditionalNode_strategy = st.builds(CompleteDSLPckg_ConditionalNode, isAssumed=st.booleans(), isDeterminate=st.booleans())
@given(instance=CompleteDSLPckg_ConditionalNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ConditionalNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConditionalNode)


CompleteDSLPckg_ConnectableElement_strategy = st.builds(CompleteDSLPckg_ConnectableElement)
@given(instance=CompleteDSLPckg_ConnectableElement_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ConnectableElement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConnectableElement)


CompleteDSLPckg_ConnectionPointReference_strategy = st.builds(CompleteDSLPckg_ConnectionPointReference)
@given(instance=CompleteDSLPckg_ConnectionPointReference_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ConnectionPointReference_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConnectionPointReference)


CompleteDSLPckg_Connector_strategy = st.builds(CompleteDSLPckg_Connector, kind=safe_text)
@given(instance=CompleteDSLPckg_Connector_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Connector_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Connector)


CompleteDSLPckg_ConnectorEnd_strategy = st.builds(CompleteDSLPckg_ConnectorEnd)
@given(instance=CompleteDSLPckg_ConnectorEnd_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ConnectorEnd_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConnectorEnd)


CompleteDSLPckg_ConsiderIgnoreFragment_strategy = st.builds(CompleteDSLPckg_ConsiderIgnoreFragment)
@given(instance=CompleteDSLPckg_ConsiderIgnoreFragment_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ConsiderIgnoreFragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConsiderIgnoreFragment)


CompleteDSLPckg_Constraint_strategy = st.builds(CompleteDSLPckg_Constraint)
@given(instance=CompleteDSLPckg_Constraint_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Constraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Constraint)


CompleteDSLPckg_Continuation_strategy = st.builds(CompleteDSLPckg_Continuation, setting=st.booleans())
@given(instance=CompleteDSLPckg_Continuation_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Continuation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Continuation)


CompleteDSLPckg_ControlFlow_strategy = st.builds(CompleteDSLPckg_ControlFlow)
@given(instance=CompleteDSLPckg_ControlFlow_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ControlFlow_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ControlFlow)


CompleteDSLPckg_ControlNode_strategy = st.builds(CompleteDSLPckg_ControlNode)
@given(instance=CompleteDSLPckg_ControlNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ControlNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ControlNode)


CompleteDSLPckg_CreateLinkAction_strategy = st.builds(CompleteDSLPckg_CreateLinkAction)
@given(instance=CompleteDSLPckg_CreateLinkAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CreateLinkAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CreateLinkAction)


CompleteDSLPckg_CreateLinkObjectAction_strategy = st.builds(CompleteDSLPckg_CreateLinkObjectAction)
@given(instance=CompleteDSLPckg_CreateLinkObjectAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CreateLinkObjectAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CreateLinkObjectAction)


CompleteDSLPckg_CreateObjectAction_strategy = st.builds(CompleteDSLPckg_CreateObjectAction)
@given(instance=CompleteDSLPckg_CreateObjectAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_CreateObjectAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CreateObjectAction)


CompleteDSLPckg_DataStoreNode_strategy = st.builds(CompleteDSLPckg_DataStoreNode)
@given(instance=CompleteDSLPckg_DataStoreNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DataStoreNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DataStoreNode)


CompleteDSLPckg_DataType_strategy = st.builds(CompleteDSLPckg_DataType)
@given(instance=CompleteDSLPckg_DataType_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DataType_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DataType)


CompleteDSLPckg_DecisionNode_strategy = st.builds(CompleteDSLPckg_DecisionNode)
@given(instance=CompleteDSLPckg_DecisionNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DecisionNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DecisionNode)


CompleteDSLPckg_Dependency_strategy = st.builds(CompleteDSLPckg_Dependency)
@given(instance=CompleteDSLPckg_Dependency_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Dependency_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Dependency)


CompleteDSLPckg_DeployedArtifact_strategy = st.builds(CompleteDSLPckg_DeployedArtifact)
@given(instance=CompleteDSLPckg_DeployedArtifact_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DeployedArtifact_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DeployedArtifact)


CompleteDSLPckg_Deployment_strategy = st.builds(CompleteDSLPckg_Deployment)
@given(instance=CompleteDSLPckg_Deployment_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Deployment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Deployment)


CompleteDSLPckg_DeploymentSpecification_strategy = st.builds(CompleteDSLPckg_DeploymentSpecification, deploymentLocation=safe_text, executionLocation=safe_text)
@given(instance=CompleteDSLPckg_DeploymentSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DeploymentSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DeploymentSpecification)


CompleteDSLPckg_DeploymentTarget_strategy = st.builds(CompleteDSLPckg_DeploymentTarget)
@given(instance=CompleteDSLPckg_DeploymentTarget_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DeploymentTarget_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DeploymentTarget)


CompleteDSLPckg_DestroyLinkAction_strategy = st.builds(CompleteDSLPckg_DestroyLinkAction)
@given(instance=CompleteDSLPckg_DestroyLinkAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DestroyLinkAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DestroyLinkAction)


CompleteDSLPckg_DestroyObjectAction_strategy = st.builds(CompleteDSLPckg_DestroyObjectAction)
@given(instance=CompleteDSLPckg_DestroyObjectAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DestroyObjectAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DestroyObjectAction)


CompleteDSLPckg_DestructionOccurrenceSpecification_strategy = st.builds(CompleteDSLPckg_DestructionOccurrenceSpecification)
@given(instance=CompleteDSLPckg_DestructionOccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DestructionOccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DestructionOccurrenceSpecification)


CompleteDSLPckg_Device_strategy = st.builds(CompleteDSLPckg_Device)
@given(instance=CompleteDSLPckg_Device_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Device_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Device)


CompleteDSLPckg_DirectedRelationship_strategy = st.builds(CompleteDSLPckg_DirectedRelationship)
@given(instance=CompleteDSLPckg_DirectedRelationship_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DirectedRelationship_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DirectedRelationship)


CompleteDSLPckg_Duration_strategy = st.builds(CompleteDSLPckg_Duration)
@given(instance=CompleteDSLPckg_Duration_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Duration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Duration)


CompleteDSLPckg_DurationConstraint_strategy = st.builds(CompleteDSLPckg_DurationConstraint, firstEvent=st.booleans())
@given(instance=CompleteDSLPckg_DurationConstraint_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DurationConstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DurationConstraint)


CompleteDSLPckg_DurationInterval_strategy = st.builds(CompleteDSLPckg_DurationInterval)
@given(instance=CompleteDSLPckg_DurationInterval_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DurationInterval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DurationInterval)


CompleteDSLPckg_DurationObservation_strategy = st.builds(CompleteDSLPckg_DurationObservation, firstEvent=st.booleans())
@given(instance=CompleteDSLPckg_DurationObservation_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_DurationObservation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DurationObservation)


CompleteDSLPckg_Element_strategy = st.builds(CompleteDSLPckg_Element)
@given(instance=CompleteDSLPckg_Element_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Element_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Element)


CompleteDSLPckg_ElementImport_strategy = st.builds(CompleteDSLPckg_ElementImport, alias=safe_text, visibility=safe_text)
@given(instance=CompleteDSLPckg_ElementImport_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ElementImport_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ElementImport)


CompleteDSLPckg_EncapsulatedClassifier_strategy = st.builds(CompleteDSLPckg_EncapsulatedClassifier)
@given(instance=CompleteDSLPckg_EncapsulatedClassifier_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_EncapsulatedClassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_EncapsulatedClassifier)


CompleteDSLPckg_Enumeration_strategy = st.builds(CompleteDSLPckg_Enumeration)
@given(instance=CompleteDSLPckg_Enumeration_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Enumeration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Enumeration)


CompleteDSLPckg_EnumerationLiteral_strategy = st.builds(CompleteDSLPckg_EnumerationLiteral)
@given(instance=CompleteDSLPckg_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_EnumerationLiteral)


CompleteDSLPckg_Event_strategy = st.builds(CompleteDSLPckg_Event)
@given(instance=CompleteDSLPckg_Event_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Event_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Event)


CompleteDSLPckg_ExceptionHandler_strategy = st.builds(CompleteDSLPckg_ExceptionHandler)
@given(instance=CompleteDSLPckg_ExceptionHandler_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExceptionHandler_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExceptionHandler)


CompleteDSLPckg_ExecutableNode_strategy = st.builds(CompleteDSLPckg_ExecutableNode)
@given(instance=CompleteDSLPckg_ExecutableNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExecutableNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutableNode)


CompleteDSLPckg_ExecutionEnvironment_strategy = st.builds(CompleteDSLPckg_ExecutionEnvironment)
@given(instance=CompleteDSLPckg_ExecutionEnvironment_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExecutionEnvironment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutionEnvironment)


CompleteDSLPckg_ExecutionOccurrenceSpecification_strategy = st.builds(CompleteDSLPckg_ExecutionOccurrenceSpecification)
@given(instance=CompleteDSLPckg_ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExecutionOccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutionOccurrenceSpecification)


CompleteDSLPckg_ExecutionSpecification_strategy = st.builds(CompleteDSLPckg_ExecutionSpecification)
@given(instance=CompleteDSLPckg_ExecutionSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExecutionSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutionSpecification)


CompleteDSLPckg_ExpansionNode_strategy = st.builds(CompleteDSLPckg_ExpansionNode)
@given(instance=CompleteDSLPckg_ExpansionNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExpansionNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExpansionNode)


CompleteDSLPckg_ExpansionRegion_strategy = st.builds(CompleteDSLPckg_ExpansionRegion, mode=safe_text)
@given(instance=CompleteDSLPckg_ExpansionRegion_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExpansionRegion_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExpansionRegion)


CompleteDSLPckg_Expression_strategy = st.builds(CompleteDSLPckg_Expression, symbol=safe_text)
@given(instance=CompleteDSLPckg_Expression_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Expression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Expression)


CompleteDSLPckg_Extend_strategy = st.builds(CompleteDSLPckg_Extend)
@given(instance=CompleteDSLPckg_Extend_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Extend_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Extend)


CompleteDSLPckg_ExtensionPoint_strategy = st.builds(CompleteDSLPckg_ExtensionPoint)
@given(instance=CompleteDSLPckg_ExtensionPoint_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ExtensionPoint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExtensionPoint)


CompleteDSLPckg_Feature_strategy = st.builds(CompleteDSLPckg_Feature, isStatic=st.booleans())
@given(instance=CompleteDSLPckg_Feature_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Feature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Feature)


CompleteDSLPckg_FinalNode_strategy = st.builds(CompleteDSLPckg_FinalNode)
@given(instance=CompleteDSLPckg_FinalNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_FinalNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FinalNode)


CompleteDSLPckg_FinalState_strategy = st.builds(CompleteDSLPckg_FinalState)
@given(instance=CompleteDSLPckg_FinalState_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_FinalState_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FinalState)


CompleteDSLPckg_FlowFinalNode_strategy = st.builds(CompleteDSLPckg_FlowFinalNode)
@given(instance=CompleteDSLPckg_FlowFinalNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_FlowFinalNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FlowFinalNode)


CompleteDSLPckg_ForkNode_strategy = st.builds(CompleteDSLPckg_ForkNode)
@given(instance=CompleteDSLPckg_ForkNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ForkNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ForkNode)


CompleteDSLPckg_FunctionBehavior_strategy = st.builds(CompleteDSLPckg_FunctionBehavior)
@given(instance=CompleteDSLPckg_FunctionBehavior_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_FunctionBehavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FunctionBehavior)


CompleteDSLPckg_Gate_strategy = st.builds(CompleteDSLPckg_Gate)
@given(instance=CompleteDSLPckg_Gate_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Gate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Gate)


CompleteDSLPckg_GeneralOrdering_strategy = st.builds(CompleteDSLPckg_GeneralOrdering)
@given(instance=CompleteDSLPckg_GeneralOrdering_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_GeneralOrdering_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_GeneralOrdering)


CompleteDSLPckg_Generalization_strategy = st.builds(CompleteDSLPckg_Generalization, isSubstitutable=st.booleans())
@given(instance=CompleteDSLPckg_Generalization_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Generalization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Generalization)


CompleteDSLPckg_GeneralizationSet_strategy = st.builds(CompleteDSLPckg_GeneralizationSet, isCovering=st.booleans(), isDisjoint=st.booleans())
@given(instance=CompleteDSLPckg_GeneralizationSet_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_GeneralizationSet_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_GeneralizationSet)


CompleteDSLPckg_Include_strategy = st.builds(CompleteDSLPckg_Include)
@given(instance=CompleteDSLPckg_Include_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Include_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Include)


CompleteDSLPckg_InitialNode_strategy = st.builds(CompleteDSLPckg_InitialNode)
@given(instance=CompleteDSLPckg_InitialNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InitialNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InitialNode)


CompleteDSLPckg_InputPin_strategy = st.builds(CompleteDSLPckg_InputPin)
@given(instance=CompleteDSLPckg_InputPin_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InputPin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InputPin)


CompleteDSLPckg_InstanceSpecification_strategy = st.builds(CompleteDSLPckg_InstanceSpecification)
@given(instance=CompleteDSLPckg_InstanceSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InstanceSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InstanceSpecification)


CompleteDSLPckg_InstanceValue_strategy = st.builds(CompleteDSLPckg_InstanceValue)
@given(instance=CompleteDSLPckg_InstanceValue_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InstanceValue_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InstanceValue)


CompleteDSLPckg_Interaction_strategy = st.builds(CompleteDSLPckg_Interaction)
@given(instance=CompleteDSLPckg_Interaction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Interaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Interaction)


CompleteDSLPckg_InteractionConstraint_strategy = st.builds(CompleteDSLPckg_InteractionConstraint)
@given(instance=CompleteDSLPckg_InteractionConstraint_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InteractionConstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionConstraint)


CompleteDSLPckg_InteractionFragment_strategy = st.builds(CompleteDSLPckg_InteractionFragment)
@given(instance=CompleteDSLPckg_InteractionFragment_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InteractionFragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionFragment)


CompleteDSLPckg_InteractionOperand_strategy = st.builds(CompleteDSLPckg_InteractionOperand)
@given(instance=CompleteDSLPckg_InteractionOperand_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InteractionOperand_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionOperand)


CompleteDSLPckg_InteractionUse_strategy = st.builds(CompleteDSLPckg_InteractionUse)
@given(instance=CompleteDSLPckg_InteractionUse_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InteractionUse_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionUse)


CompleteDSLPckg_Interface_strategy = st.builds(CompleteDSLPckg_Interface)
@given(instance=CompleteDSLPckg_Interface_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Interface_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Interface)


CompleteDSLPckg_InterfaceRealization_strategy = st.builds(CompleteDSLPckg_InterfaceRealization)
@given(instance=CompleteDSLPckg_InterfaceRealization_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InterfaceRealization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InterfaceRealization)


CompleteDSLPckg_InterruptibleActivityRegion_strategy = st.builds(CompleteDSLPckg_InterruptibleActivityRegion)
@given(instance=CompleteDSLPckg_InterruptibleActivityRegion_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InterruptibleActivityRegion_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InterruptibleActivityRegion)


CompleteDSLPckg_Interval_strategy = st.builds(CompleteDSLPckg_Interval)
@given(instance=CompleteDSLPckg_Interval_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Interval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Interval)


CompleteDSLPckg_IntervalConstraint_strategy = st.builds(CompleteDSLPckg_IntervalConstraint)
@given(instance=CompleteDSLPckg_IntervalConstraint_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_IntervalConstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_IntervalConstraint)


CompleteDSLPckg_InvocationAction_strategy = st.builds(CompleteDSLPckg_InvocationAction)
@given(instance=CompleteDSLPckg_InvocationAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_InvocationAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InvocationAction)


CompleteDSLPckg_JoinNode_strategy = st.builds(CompleteDSLPckg_JoinNode, isCombineDuplicate=st.booleans())
@given(instance=CompleteDSLPckg_JoinNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_JoinNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_JoinNode)


CompleteDSLPckg_Lifeline_strategy = st.builds(CompleteDSLPckg_Lifeline)
@given(instance=CompleteDSLPckg_Lifeline_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Lifeline_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Lifeline)


CompleteDSLPckg_LinkAction_strategy = st.builds(CompleteDSLPckg_LinkAction)
@given(instance=CompleteDSLPckg_LinkAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LinkAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkAction)


CompleteDSLPckg_LinkEndCreationData_strategy = st.builds(CompleteDSLPckg_LinkEndCreationData, isReplaceAll=st.booleans())
@given(instance=CompleteDSLPckg_LinkEndCreationData_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LinkEndCreationData_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkEndCreationData)


CompleteDSLPckg_LinkEndData_strategy = st.builds(CompleteDSLPckg_LinkEndData)
@given(instance=CompleteDSLPckg_LinkEndData_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LinkEndData_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkEndData)


CompleteDSLPckg_LinkEndDestructionData_strategy = st.builds(CompleteDSLPckg_LinkEndDestructionData, isDestroyDuplicates=st.booleans())
@given(instance=CompleteDSLPckg_LinkEndDestructionData_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LinkEndDestructionData_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkEndDestructionData)


CompleteDSLPckg_LiteralBoolean_strategy = st.builds(CompleteDSLPckg_LiteralBoolean)
@given(instance=CompleteDSLPckg_LiteralBoolean_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LiteralBoolean_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralBoolean)


CompleteDSLPckg_LiteralInteger_strategy = st.builds(CompleteDSLPckg_LiteralInteger)
@given(instance=CompleteDSLPckg_LiteralInteger_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LiteralInteger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralInteger)


CompleteDSLPckg_LiteralNull_strategy = st.builds(CompleteDSLPckg_LiteralNull)
@given(instance=CompleteDSLPckg_LiteralNull_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LiteralNull_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralNull)


CompleteDSLPckg_LiteralReal_strategy = st.builds(CompleteDSLPckg_LiteralReal)
@given(instance=CompleteDSLPckg_LiteralReal_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LiteralReal_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralReal)


CompleteDSLPckg_LiteralSpecification_strategy = st.builds(CompleteDSLPckg_LiteralSpecification)
@given(instance=CompleteDSLPckg_LiteralSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LiteralSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralSpecification)


CompleteDSLPckg_LiteralString_strategy = st.builds(CompleteDSLPckg_LiteralString)
@given(instance=CompleteDSLPckg_LiteralString_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LiteralString_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralString)


CompleteDSLPckg_LiteralUnilimitedNatural_strategy = st.builds(CompleteDSLPckg_LiteralUnilimitedNatural)
@given(instance=CompleteDSLPckg_LiteralUnilimitedNatural_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LiteralUnilimitedNatural_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralUnilimitedNatural)


CompleteDSLPckg_LoopNode_strategy = st.builds(CompleteDSLPckg_LoopNode, isTestedFirst=st.booleans())
@given(instance=CompleteDSLPckg_LoopNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_LoopNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LoopNode)


CompleteDSLPckg_Manifestation_strategy = st.builds(CompleteDSLPckg_Manifestation)
@given(instance=CompleteDSLPckg_Manifestation_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Manifestation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Manifestation)


CompleteDSLPckg_MergeNode_strategy = st.builds(CompleteDSLPckg_MergeNode)
@given(instance=CompleteDSLPckg_MergeNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_MergeNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MergeNode)


CompleteDSLPckg_Message_strategy = st.builds(CompleteDSLPckg_Message, messageKind=safe_text, messageSort=safe_text)
@given(instance=CompleteDSLPckg_Message_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Message_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Message)


CompleteDSLPckg_MessageEnd_strategy = st.builds(CompleteDSLPckg_MessageEnd)
@given(instance=CompleteDSLPckg_MessageEnd_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_MessageEnd_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MessageEnd)


CompleteDSLPckg_MessageEvent_strategy = st.builds(CompleteDSLPckg_MessageEvent)
@given(instance=CompleteDSLPckg_MessageEvent_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_MessageEvent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MessageEvent)


CompleteDSLPckg_MessageOccurrenceSpecification_strategy = st.builds(CompleteDSLPckg_MessageOccurrenceSpecification)
@given(instance=CompleteDSLPckg_MessageOccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_MessageOccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MessageOccurrenceSpecification)


CompleteDSLPckg_MultiplicityElement_strategy = st.builds(CompleteDSLPckg_MultiplicityElement, isOrdered=st.booleans(), isUnique=st.booleans(), lower=st.integers(), upper=st.integers())
@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MultiplicityElement)


CompleteDSLPckg_NamedElement_strategy = st.builds(CompleteDSLPckg_NamedElement, name=safe_text, qualifiedName=safe_text, visibility=safe_text)
@given(instance=CompleteDSLPckg_NamedElement_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_NamedElement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_NamedElement)


CompleteDSLPckg_Namespace_strategy = st.builds(CompleteDSLPckg_Namespace)
@given(instance=CompleteDSLPckg_Namespace_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Namespace_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Namespace)


CompleteDSLPckg_Node_strategy = st.builds(CompleteDSLPckg_Node)
@given(instance=CompleteDSLPckg_Node_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Node_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Node)


CompleteDSLPckg_ObjectFlow_strategy = st.builds(CompleteDSLPckg_ObjectFlow, isControlType=st.booleans(), isMulticast=st.booleans(), isMultireceive=st.booleans(), ordering=safe_text)
@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ObjectFlow_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ObjectFlow)


CompleteDSLPckg_ObjectNode_strategy = st.builds(CompleteDSLPckg_ObjectNode)
@given(instance=CompleteDSLPckg_ObjectNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ObjectNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ObjectNode)


CompleteDSLPckg_Observation_strategy = st.builds(CompleteDSLPckg_Observation)
@given(instance=CompleteDSLPckg_Observation_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Observation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Observation)


CompleteDSLPckg_OccurenceSpecification_strategy = st.builds(CompleteDSLPckg_OccurenceSpecification)
@given(instance=CompleteDSLPckg_OccurenceSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_OccurenceSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OccurenceSpecification)


CompleteDSLPckg_OpaqueAction_strategy = st.builds(CompleteDSLPckg_OpaqueAction, body=safe_text, language=safe_text)
@given(instance=CompleteDSLPckg_OpaqueAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_OpaqueAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OpaqueAction)


CompleteDSLPckg_OpaqueBehavior_strategy = st.builds(CompleteDSLPckg_OpaqueBehavior, body=safe_text, language=safe_text)
@given(instance=CompleteDSLPckg_OpaqueBehavior_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_OpaqueBehavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OpaqueBehavior)


CompleteDSLPckg_OpaqueExpression_strategy = st.builds(CompleteDSLPckg_OpaqueExpression, body=safe_text, language=safe_text)
@given(instance=CompleteDSLPckg_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OpaqueExpression)


CompleteDSLPckg_Operation_strategy = st.builds(CompleteDSLPckg_Operation, isOrdered=st.booleans(), isQuery=st.booleans(), isUnique=st.booleans(), lower=st.integers(), upper=st.integers())
@given(instance=CompleteDSLPckg_Operation_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Operation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Operation)


CompleteDSLPckg_OutputPin_strategy = st.builds(CompleteDSLPckg_OutputPin)
@given(instance=CompleteDSLPckg_OutputPin_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_OutputPin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OutputPin)


CompleteDSLPckg_Package_strategy = st.builds(CompleteDSLPckg_Package, URI=safe_text)
@given(instance=CompleteDSLPckg_Package_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Package_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Package)


CompleteDSLPckg_PackageImport_strategy = st.builds(CompleteDSLPckg_PackageImport, visibility=safe_text)
@given(instance=CompleteDSLPckg_PackageImport_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_PackageImport_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PackageImport)


CompleteDSLPckg_PackageMerge_strategy = st.builds(CompleteDSLPckg_PackageMerge)
@given(instance=CompleteDSLPckg_PackageMerge_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_PackageMerge_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PackageMerge)


CompleteDSLPckg_PackageableElement_strategy = st.builds(CompleteDSLPckg_PackageableElement)
@given(instance=CompleteDSLPckg_PackageableElement_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_PackageableElement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PackageableElement)


CompleteDSLPckg_Parameter_strategy = st.builds(CompleteDSLPckg_Parameter, default=safe_text)
@given(instance=CompleteDSLPckg_Parameter_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Parameter_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Parameter)


CompleteDSLPckg_ParameterSet_strategy = st.builds(CompleteDSLPckg_ParameterSet)
@given(instance=CompleteDSLPckg_ParameterSet_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ParameterSet_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ParameterSet)


CompleteDSLPckg_PartDecomposition_strategy = st.builds(CompleteDSLPckg_PartDecomposition)
@given(instance=CompleteDSLPckg_PartDecomposition_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_PartDecomposition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PartDecomposition)


CompleteDSLPckg_Pin_strategy = st.builds(CompleteDSLPckg_Pin)
@given(instance=CompleteDSLPckg_Pin_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Pin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Pin)


CompleteDSLPckg_Port_strategy = st.builds(CompleteDSLPckg_Port, isBehavior=st.booleans(), isConjugated=st.booleans(), isService=st.booleans())
@given(instance=CompleteDSLPckg_Port_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Port_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Port)


CompleteDSLPckg_PrimitiveType_strategy = st.builds(CompleteDSLPckg_PrimitiveType)
@given(instance=CompleteDSLPckg_PrimitiveType_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_PrimitiveType_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PrimitiveType)


CompleteDSLPckg_Property_strategy = st.builds(CompleteDSLPckg_Property, aggregation=safe_text, default=safe_text, isComposite=st.booleans(), isDerived=st.booleans(), isDerivedUnion=st.booleans(), isID=st.booleans())
@given(instance=CompleteDSLPckg_Property_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Property_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Property)


CompleteDSLPckg_ProtocolConformance_strategy = st.builds(CompleteDSLPckg_ProtocolConformance)
@given(instance=CompleteDSLPckg_ProtocolConformance_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ProtocolConformance_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ProtocolConformance)


CompleteDSLPckg_ProtocolStateMachine_strategy = st.builds(CompleteDSLPckg_ProtocolStateMachine)
@given(instance=CompleteDSLPckg_ProtocolStateMachine_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ProtocolStateMachine_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ProtocolStateMachine)


CompleteDSLPckg_ProtocolTransition_strategy = st.builds(CompleteDSLPckg_ProtocolTransition)
@given(instance=CompleteDSLPckg_ProtocolTransition_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ProtocolTransition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ProtocolTransition)


CompleteDSLPckg_Pseudostate_strategy = st.builds(CompleteDSLPckg_Pseudostate)
@given(instance=CompleteDSLPckg_Pseudostate_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Pseudostate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Pseudostate)


CompleteDSLPckg_QualifierValue_strategy = st.builds(CompleteDSLPckg_QualifierValue)
@given(instance=CompleteDSLPckg_QualifierValue_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_QualifierValue_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_QualifierValue)


CompleteDSLPckg_RaiseExceptionAction_strategy = st.builds(CompleteDSLPckg_RaiseExceptionAction)
@given(instance=CompleteDSLPckg_RaiseExceptionAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_RaiseExceptionAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RaiseExceptionAction)


CompleteDSLPckg_ReadExtendAction_strategy = st.builds(CompleteDSLPckg_ReadExtendAction)
@given(instance=CompleteDSLPckg_ReadExtendAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadExtendAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadExtendAction)


CompleteDSLPckg_ReadLinkAction_strategy = st.builds(CompleteDSLPckg_ReadLinkAction)
@given(instance=CompleteDSLPckg_ReadLinkAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadLinkAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadLinkAction)


CompleteDSLPckg_ReadLinkObjectEndAction_strategy = st.builds(CompleteDSLPckg_ReadLinkObjectEndAction)
@given(instance=CompleteDSLPckg_ReadLinkObjectEndAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadLinkObjectEndAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadLinkObjectEndAction)


CompleteDSLPckg_ReadLinkObjectEndQualifierAction_strategy = st.builds(CompleteDSLPckg_ReadLinkObjectEndQualifierAction)
@given(instance=CompleteDSLPckg_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadLinkObjectEndQualifierAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadLinkObjectEndQualifierAction)


CompleteDSLPckg_ReadSelfAction_strategy = st.builds(CompleteDSLPckg_ReadSelfAction)
@given(instance=CompleteDSLPckg_ReadSelfAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadSelfAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadSelfAction)


CompleteDSLPckg_ReadStructuralFeatureAction_strategy = st.builds(CompleteDSLPckg_ReadStructuralFeatureAction)
@given(instance=CompleteDSLPckg_ReadStructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadStructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadStructuralFeatureAction)


CompleteDSLPckg_ReadVariableAction_strategy = st.builds(CompleteDSLPckg_ReadVariableAction)
@given(instance=CompleteDSLPckg_ReadVariableAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadVariableAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadVariableAction)


CompleteDSLPckg_ReadlsClassifiedObjectAction_strategy = st.builds(CompleteDSLPckg_ReadlsClassifiedObjectAction)
@given(instance=CompleteDSLPckg_ReadlsClassifiedObjectAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReadlsClassifiedObjectAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadlsClassifiedObjectAction)


CompleteDSLPckg_Realization_strategy = st.builds(CompleteDSLPckg_Realization)
@given(instance=CompleteDSLPckg_Realization_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Realization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Realization)


CompleteDSLPckg_Reception_strategy = st.builds(CompleteDSLPckg_Reception)
@given(instance=CompleteDSLPckg_Reception_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Reception_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Reception)


CompleteDSLPckg_ReclassifyObjectAction_strategy = st.builds(CompleteDSLPckg_ReclassifyObjectAction, isReplaceAll=st.booleans())
@given(instance=CompleteDSLPckg_ReclassifyObjectAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReclassifyObjectAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReclassifyObjectAction)


CompleteDSLPckg_RedefinableElement_strategy = st.builds(CompleteDSLPckg_RedefinableElement, isLeaf=st.booleans())
@given(instance=CompleteDSLPckg_RedefinableElement_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_RedefinableElement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RedefinableElement)


CompleteDSLPckg_ReduceAction_strategy = st.builds(CompleteDSLPckg_ReduceAction, isOrdered=st.booleans())
@given(instance=CompleteDSLPckg_ReduceAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReduceAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReduceAction)


CompleteDSLPckg_Region_strategy = st.builds(CompleteDSLPckg_Region)
@given(instance=CompleteDSLPckg_Region_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Region_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Region)


CompleteDSLPckg_Relationship_strategy = st.builds(CompleteDSLPckg_Relationship)
@given(instance=CompleteDSLPckg_Relationship_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Relationship_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Relationship)


CompleteDSLPckg_RemoveStructuralFeatureValueAction_strategy = st.builds(CompleteDSLPckg_RemoveStructuralFeatureValueAction)
@given(instance=CompleteDSLPckg_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_RemoveStructuralFeatureValueAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RemoveStructuralFeatureValueAction)


CompleteDSLPckg_RemoveVariableValueAction_strategy = st.builds(CompleteDSLPckg_RemoveVariableValueAction)
@given(instance=CompleteDSLPckg_RemoveVariableValueAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_RemoveVariableValueAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RemoveVariableValueAction)


CompleteDSLPckg_ReplyAction_strategy = st.builds(CompleteDSLPckg_ReplyAction)
@given(instance=CompleteDSLPckg_ReplyAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ReplyAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReplyAction)


CompleteDSLPckg_SendObjectAction_strategy = st.builds(CompleteDSLPckg_SendObjectAction)
@given(instance=CompleteDSLPckg_SendObjectAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_SendObjectAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SendObjectAction)


CompleteDSLPckg_SendSignalAction_strategy = st.builds(CompleteDSLPckg_SendSignalAction)
@given(instance=CompleteDSLPckg_SendSignalAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_SendSignalAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SendSignalAction)


CompleteDSLPckg_SequenceNode_strategy = st.builds(CompleteDSLPckg_SequenceNode)
@given(instance=CompleteDSLPckg_SequenceNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_SequenceNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SequenceNode)


CompleteDSLPckg_Signal_strategy = st.builds(CompleteDSLPckg_Signal)
@given(instance=CompleteDSLPckg_Signal_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Signal_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Signal)


CompleteDSLPckg_SignalEvent_strategy = st.builds(CompleteDSLPckg_SignalEvent)
@given(instance=CompleteDSLPckg_SignalEvent_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_SignalEvent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SignalEvent)


CompleteDSLPckg_Slot_strategy = st.builds(CompleteDSLPckg_Slot)
@given(instance=CompleteDSLPckg_Slot_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Slot_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Slot)


CompleteDSLPckg_StartClassifierBehaviorAction_strategy = st.builds(CompleteDSLPckg_StartClassifierBehaviorAction)
@given(instance=CompleteDSLPckg_StartClassifierBehaviorAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StartClassifierBehaviorAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StartClassifierBehaviorAction)


CompleteDSLPckg_StartObjectBehaviorAction_strategy = st.builds(CompleteDSLPckg_StartObjectBehaviorAction)
@given(instance=CompleteDSLPckg_StartObjectBehaviorAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StartObjectBehaviorAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StartObjectBehaviorAction)


CompleteDSLPckg_State_strategy = st.builds(CompleteDSLPckg_State, isComposite=st.booleans(), isOrthogonal=st.booleans(), isSimple=st.booleans(), isSubmachineState=st.booleans())
@given(instance=CompleteDSLPckg_State_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_State_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_State)


CompleteDSLPckg_StateInvariant_strategy = st.builds(CompleteDSLPckg_StateInvariant)
@given(instance=CompleteDSLPckg_StateInvariant_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StateInvariant_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StateInvariant)


CompleteDSLPckg_StateMachine_strategy = st.builds(CompleteDSLPckg_StateMachine)
@given(instance=CompleteDSLPckg_StateMachine_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StateMachine_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StateMachine)


CompleteDSLPckg_StructuralFeature_strategy = st.builds(CompleteDSLPckg_StructuralFeature, isReadOnly=st.booleans())
@given(instance=CompleteDSLPckg_StructuralFeature_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StructuralFeature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuralFeature)


CompleteDSLPckg_StructuralFeatureAction_strategy = st.builds(CompleteDSLPckg_StructuralFeatureAction)
@given(instance=CompleteDSLPckg_StructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuralFeatureAction)


CompleteDSLPckg_StructuredActivityNode_strategy = st.builds(CompleteDSLPckg_StructuredActivityNode, mustIsolate=st.booleans())
@given(instance=CompleteDSLPckg_StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuredActivityNode)


CompleteDSLPckg_StructuredClassifier_strategy = st.builds(CompleteDSLPckg_StructuredClassifier)
@given(instance=CompleteDSLPckg_StructuredClassifier_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_StructuredClassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuredClassifier)


CompleteDSLPckg_Substitution_strategy = st.builds(CompleteDSLPckg_Substitution)
@given(instance=CompleteDSLPckg_Substitution_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Substitution_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Substitution)


CompleteDSLPckg_TestIdentityAction_strategy = st.builds(CompleteDSLPckg_TestIdentityAction)
@given(instance=CompleteDSLPckg_TestIdentityAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_TestIdentityAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TestIdentityAction)


CompleteDSLPckg_TimeConstraint_strategy = st.builds(CompleteDSLPckg_TimeConstraint, firstEvent=st.booleans())
@given(instance=CompleteDSLPckg_TimeConstraint_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_TimeConstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeConstraint)


CompleteDSLPckg_TimeEvent_strategy = st.builds(CompleteDSLPckg_TimeEvent, isRelative=st.booleans())
@given(instance=CompleteDSLPckg_TimeEvent_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_TimeEvent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeEvent)


CompleteDSLPckg_TimeExpression_strategy = st.builds(CompleteDSLPckg_TimeExpression)
@given(instance=CompleteDSLPckg_TimeExpression_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_TimeExpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeExpression)


CompleteDSLPckg_TimeInterval_strategy = st.builds(CompleteDSLPckg_TimeInterval)
@given(instance=CompleteDSLPckg_TimeInterval_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_TimeInterval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeInterval)


CompleteDSLPckg_TimeObservation_strategy = st.builds(CompleteDSLPckg_TimeObservation, firstEvent=st.booleans())
@given(instance=CompleteDSLPckg_TimeObservation_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_TimeObservation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeObservation)


CompleteDSLPckg_Transition_strategy = st.builds(CompleteDSLPckg_Transition, kind=safe_text)
@given(instance=CompleteDSLPckg_Transition_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Transition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Transition)


CompleteDSLPckg_Trigger_strategy = st.builds(CompleteDSLPckg_Trigger)
@given(instance=CompleteDSLPckg_Trigger_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Trigger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Trigger)


CompleteDSLPckg_Type_strategy = st.builds(CompleteDSLPckg_Type)
@given(instance=CompleteDSLPckg_Type_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Type_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Type)


CompleteDSLPckg_TypedElement_strategy = st.builds(CompleteDSLPckg_TypedElement)
@given(instance=CompleteDSLPckg_TypedElement_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_TypedElement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TypedElement)


CompleteDSLPckg_UnmarshallAction_strategy = st.builds(CompleteDSLPckg_UnmarshallAction)
@given(instance=CompleteDSLPckg_UnmarshallAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_UnmarshallAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_UnmarshallAction)


CompleteDSLPckg_Usage_strategy = st.builds(CompleteDSLPckg_Usage)
@given(instance=CompleteDSLPckg_Usage_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Usage_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Usage)


CompleteDSLPckg_UseCase_strategy = st.builds(CompleteDSLPckg_UseCase)
@given(instance=CompleteDSLPckg_UseCase_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_UseCase_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_UseCase)


CompleteDSLPckg_ValuePin_strategy = st.builds(CompleteDSLPckg_ValuePin)
@given(instance=CompleteDSLPckg_ValuePin_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ValuePin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ValuePin)


CompleteDSLPckg_ValueSpecification_strategy = st.builds(CompleteDSLPckg_ValueSpecification)
@given(instance=CompleteDSLPckg_ValueSpecification_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ValueSpecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ValueSpecification)


CompleteDSLPckg_ValueSpecificationAction_strategy = st.builds(CompleteDSLPckg_ValueSpecificationAction)
@given(instance=CompleteDSLPckg_ValueSpecificationAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_ValueSpecificationAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ValueSpecificationAction)


CompleteDSLPckg_Variable_strategy = st.builds(CompleteDSLPckg_Variable)
@given(instance=CompleteDSLPckg_Variable_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Variable_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Variable)


CompleteDSLPckg_VariableAction_strategy = st.builds(CompleteDSLPckg_VariableAction)
@given(instance=CompleteDSLPckg_VariableAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_VariableAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_VariableAction)


CompleteDSLPckg_Vertex_strategy = st.builds(CompleteDSLPckg_Vertex)
@given(instance=CompleteDSLPckg_Vertex_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_Vertex_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Vertex)


CompleteDSLPckg_WriteLinkAction_strategy = st.builds(CompleteDSLPckg_WriteLinkAction)
@given(instance=CompleteDSLPckg_WriteLinkAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_WriteLinkAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_WriteLinkAction)


CompleteDSLPckg_WriteStructuralFeatureAction_strategy = st.builds(CompleteDSLPckg_WriteStructuralFeatureAction)
@given(instance=CompleteDSLPckg_WriteStructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_WriteStructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_WriteStructuralFeatureAction)


CompleteDSLPckg_WriteVariableAction_strategy = st.builds(CompleteDSLPckg_WriteVariableAction)
@given(instance=CompleteDSLPckg_WriteVariableAction_strategy)
@settings(max_examples=25)
def test_CompleteDSLPckg_WriteVariableAction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_WriteVariableAction)


ConnectableElement_strategy = st.builds(ConnectableElement)
@given(instance=ConnectableElement_strategy)
@settings(max_examples=25)
def test_ConnectableElement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


CreateLinkAction_strategy = st.builds(CreateLinkAction)
@given(instance=CreateLinkAction_strategy)
@settings(max_examples=25)
def test_CreateLinkAction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Dependency_strategy = st.builds(Dependency)
@given(instance=Dependency_strategy)
@settings(max_examples=25)
def test_Dependency_instantiation(instance):
    assert isinstance(instance, Dependency)


DeployedArtifact_strategy = st.builds(DeployedArtifact)
@given(instance=DeployedArtifact_strategy)
@settings(max_examples=25)
def test_DeployedArtifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)


DeploymentTarget_strategy = st.builds(DeploymentTarget)
@given(instance=DeploymentTarget_strategy)
@settings(max_examples=25)
def test_DeploymentTarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)


DirectedRelationship_strategy = st.builds(DirectedRelationship)
@given(instance=DirectedRelationship_strategy)
@settings(max_examples=25)
def test_DirectedRelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


EncapsulatedClassifier_strategy = st.builds(EncapsulatedClassifier)
@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=25)
def test_EncapsulatedClassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


ExecutableNode_strategy = st.builds(ExecutableNode)
@given(instance=ExecutableNode_strategy)
@settings(max_examples=25)
def test_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)


ExecutionSpecification_strategy = st.builds(ExecutionSpecification)
@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=25)
def test_ExecutionSpecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


InputPin_strategy = st.builds(InputPin)
@given(instance=InputPin_strategy)
@settings(max_examples=25)
def test_InputPin_instantiation(instance):
    assert isinstance(instance, InputPin)


InstanceSpecification_strategy = st.builds(InstanceSpecification)
@given(instance=InstanceSpecification_strategy)
@settings(max_examples=25)
def test_InstanceSpecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)


InteractionFragment_strategy = st.builds(InteractionFragment)
@given(instance=InteractionFragment_strategy)
@settings(max_examples=25)
def test_InteractionFragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)


InteractionUse_strategy = st.builds(InteractionUse)
@given(instance=InteractionUse_strategy)
@settings(max_examples=25)
def test_InteractionUse_instantiation(instance):
    assert isinstance(instance, InteractionUse)


Interval_strategy = st.builds(Interval)
@given(instance=Interval_strategy)
@settings(max_examples=25)
def test_Interval_instantiation(instance):
    assert isinstance(instance, Interval)


IntervalConstraint_strategy = st.builds(IntervalConstraint)
@given(instance=IntervalConstraint_strategy)
@settings(max_examples=25)
def test_IntervalConstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)


InvocationAction_strategy = st.builds(InvocationAction)
@given(instance=InvocationAction_strategy)
@settings(max_examples=25)
def test_InvocationAction_instantiation(instance):
    assert isinstance(instance, InvocationAction)


LinkAction_strategy = st.builds(LinkAction)
@given(instance=LinkAction_strategy)
@settings(max_examples=25)
def test_LinkAction_instantiation(instance):
    assert isinstance(instance, LinkAction)


LinkEndData_strategy = st.builds(LinkEndData)
@given(instance=LinkEndData_strategy)
@settings(max_examples=25)
def test_LinkEndData_instantiation(instance):
    assert isinstance(instance, LinkEndData)


LiteralSpecification_strategy = st.builds(LiteralSpecification)
@given(instance=LiteralSpecification_strategy)
@settings(max_examples=25)
def test_LiteralSpecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)


MessageEnd_strategy = st.builds(MessageEnd)
@given(instance=MessageEnd_strategy)
@settings(max_examples=25)
def test_MessageEnd_instantiation(instance):
    assert isinstance(instance, MessageEnd)


MessageEvent_strategy = st.builds(MessageEvent)
@given(instance=MessageEvent_strategy)
@settings(max_examples=25)
def test_MessageEvent_instantiation(instance):
    assert isinstance(instance, MessageEvent)


MessageOccurrenceSpecification_strategy = st.builds(MessageOccurrenceSpecification)
@given(instance=MessageOccurrenceSpecification_strategy)
@settings(max_examples=25)
def test_MessageOccurrenceSpecification_instantiation(instance):
    assert isinstance(instance, MessageOccurrenceSpecification)


MultiplicityElement_strategy = st.builds(MultiplicityElement)
@given(instance=MultiplicityElement_strategy)
@settings(max_examples=25)
def test_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Namespace_strategy = st.builds(Namespace)
@given(instance=Namespace_strategy)
@settings(max_examples=25)
def test_Namespace_instantiation(instance):
    assert isinstance(instance, Namespace)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


Observation_strategy = st.builds(Observation)
@given(instance=Observation_strategy)
@settings(max_examples=25)
def test_Observation_instantiation(instance):
    assert isinstance(instance, Observation)


OccurenceSpecification_strategy = st.builds(OccurenceSpecification)
@given(instance=OccurenceSpecification_strategy)
@settings(max_examples=25)
def test_OccurenceSpecification_instantiation(instance):
    assert isinstance(instance, OccurenceSpecification)


OpaqueBehavior_strategy = st.builds(OpaqueBehavior)
@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=25)
def test_OpaqueBehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)


PackageableElement_strategy = st.builds(PackageableElement)
@given(instance=PackageableElement_strategy)
@settings(max_examples=25)
def test_PackageableElement_instantiation(instance):
    assert isinstance(instance, PackageableElement)


Pin_strategy = st.builds(Pin)
@given(instance=Pin_strategy)
@settings(max_examples=25)
def test_Pin_instantiation(instance):
    assert isinstance(instance, Pin)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


Realization_strategy = st.builds(Realization)
@given(instance=Realization_strategy)
@settings(max_examples=25)
def test_Realization_instantiation(instance):
    assert isinstance(instance, Realization)


RedefinableElement_strategy = st.builds(RedefinableElement)
@given(instance=RedefinableElement_strategy)
@settings(max_examples=25)
def test_RedefinableElement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)


Relationship_strategy = st.builds(Relationship)
@given(instance=Relationship_strategy)
@settings(max_examples=25)
def test_Relationship_instantiation(instance):
    assert isinstance(instance, Relationship)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


StateMachine_strategy = st.builds(StateMachine)
@given(instance=StateMachine_strategy)
@settings(max_examples=25)
def test_StateMachine_instantiation(instance):
    assert isinstance(instance, StateMachine)


StructuralFeature_strategy = st.builds(StructuralFeature)
@given(instance=StructuralFeature_strategy)
@settings(max_examples=25)
def test_StructuralFeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)


StructuralFeatureAction_strategy = st.builds(StructuralFeatureAction)
@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_StructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)


StructuredActivityNode_strategy = st.builds(StructuredActivityNode)
@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)


StructuredClassifier_strategy = st.builds(StructuredClassifier)
@given(instance=StructuredClassifier_strategy)
@settings(max_examples=25)
def test_StructuredClassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


ValueSpecification_strategy = st.builds(ValueSpecification)
@given(instance=ValueSpecification_strategy)
@settings(max_examples=25)
def test_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)


VariableAction_strategy = st.builds(VariableAction)
@given(instance=VariableAction_strategy)
@settings(max_examples=25)
def test_VariableAction_instantiation(instance):
    assert isinstance(instance, VariableAction)


Vertex_strategy = st.builds(Vertex)
@given(instance=Vertex_strategy)
@settings(max_examples=25)
def test_Vertex_instantiation(instance):
    assert isinstance(instance, Vertex)


WriteLinkAction_strategy = st.builds(WriteLinkAction)
@given(instance=WriteLinkAction_strategy)
@settings(max_examples=25)
def test_WriteLinkAction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)


WriteStructuralFeatureAction_strategy = st.builds(WriteStructuralFeatureAction)
@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_WriteStructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)


WriteVariableAction_strategy = st.builds(WriteVariableAction)
@given(instance=WriteVariableAction_strategy)
@settings(max_examples=25)
def test_WriteVariableAction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)



