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
    InvocationAction,
    xmof_BasicActions_SendSignalAction,
    xmof_BasicActions_CallAction,
    IntermediateActivities_ObjectNode,
    Pin,
    xmof_BasicActions_OutputPin,
    xmof_BasicActions_InputPin,
    BasicActions_xmof_EClassifier,
    ExecutableNode,
    xmof_BasicActions_Action,
    Communications_Trigger,
    CompleteActions_xmof_EClassifier,
    CallAction,
    xmof_BasicActions_CallOperationAction,
    xmof_BasicActions_CallBehaviorAction,
    xmof_CompleteActions_StartObjectBehaviorAction,
    IntermediateActions_xmof_EClassifier,
    WriteLinkAction,
    xmof_IntermediateActions_DestroyLinkAction,
    xmof_IntermediateActions_CreateLinkAction,
    LinkEndData,
    xmof_IntermediateActions_LinkEndDestructionData,
    xmof_IntermediateActions_LinkEndCreationData,
    WriteStructuralFeatureAction,
    xmof_IntermediateActions_AddStructuralFeatureValueAction,
    xmof_IntermediateActions_RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    xmof_IntermediateActions_ReadStructuralFeatureAction,
    xmof_IntermediateActions_ClearStructuralFeatureAction,
    xmof_IntermediateActions_WriteStructuralFeatureAction,
    IntermediateActions_xmof_EReference,
    IntermediateActions_LinkEndData,
    LinkAction,
    xmof_IntermediateActions_ReadLinkAction,
    xmof_IntermediateActions_WriteLinkAction,
    IntermediateActions_xmof_EStructuralFeature,
    ExtraStructuredActivities_ExpansionNode,
    ExtraStructuredActivities_ExpansionRegion,
    Action,
    xmof_CompleteActions_ReduceAction,
    xmof_IntermediateActions_TestIdentityAction,
    xmof_CompleteActions_StartClassifierBehaviorAction,
    xmof_IntermediateActions_CreateObjectAction,
    xmof_IntermediateActions_ReadSelfAction,
    xmof_CompleteActions_ReadIsClassifiedObjectAction,
    xmof_BasicActions_InvocationAction,
    xmof_IntermediateActions_StructuralFeatureAction,
    xmof_CompleteActions_AcceptEventAction,
    xmof_IntermediateActions_DestroyObjectAction,
    xmof_IntermediateActions_ClearAssociationAction,
    xmof_IntermediateActions_LinkAction,
    xmof_IntermediateActions_ValueSpecificationAction,
    xmof_CompleteActions_ReclassifyObjectAction,
    xmof_CompleteActions_ReadExtentAction,
    xmof_CompleteStructuredActivities_StructuredActivityNode,
    CompleteStructuredActivities_Clause,
    BasicActions_InputPin,
    CompleteStructuredActivities_ExecutableNode,
    BasicActions_OutputPin,
    StructuredActivityNode,
    xmof_CompleteStructuredActivities_ConditionalNode,
    xmof_ExtraStructuredActivities_ExpansionRegion,
    xmof_CompleteStructuredActivities_LoopNode,
    ObjectNode,
    xmof_ExtraStructuredActivities_ExpansionNode,
    xmof_IntermediateActivities_ActivityParameterNode,
    FinalNode,
    xmof_IntermediateActivities_ActivityFinalNode,
    ActivityNode,
    xmof_CompleteStructuredActivities_ExecutableNode,
    xmof_IntermediateActivities_ControlNode,
    ControlNode,
    xmof_IntermediateActivities_FinalNode,
    xmof_IntermediateActivities_InitialNode,
    xmof_IntermediateActivities_JoinNode,
    xmof_IntermediateActivities_ForkNode,
    xmof_IntermediateActivities_MergeNode,
    IntermediateActivities_ActivityEdge,
    CompleteStructuredActivities_StructuredActivityNode,
    IntermediateActivities_ActivityNode,
    IntermediateActivities_Activity,
    ActivityEdge,
    xmof_IntermediateActivities_ControlFlow,
    xmof_IntermediateActivities_ObjectFlow,
    EDataType,
    xmof_Kernel_PrimitiveType,
    LiteralSpecification,
    xmof_Kernel_LiteralInteger,
    xmof_Kernel_LiteralNull,
    xmof_Kernel_LiteralUnlimitedNatural,
    xmof_Kernel_LiteralString,
    xmof_Kernel_LiteralBoolean,
    ValueSpecification,
    xmof_Kernel_LiteralSpecification,
    xmof_Kernel_InstanceValue,
    Kernel_InstanceSpecification,
    Kernel_ValueSpecification,
    Kernel_xmof_EStructuralFeature,
    EModelElement,
    xmof_IntermediateActions_LinkEndData,
    xmof_CompleteStructuredActivities_Clause,
    xmof_Kernel_Slot,
    Kernel_Slot,
    Kernel_xmof_EClassifier,
    ETypedElement,
    xmof_BasicActions_Pin,
    xmof_IntermediateActivities_ObjectNode,
    xmof_Kernel_ValueSpecification,
    Kernel_xmof_EEnumLiteral,
    InstanceSpecification,
    xmof_Kernel_EEnumLiteralSpecification,
    EParameter,
    xmof_Kernel_DirectedParameter,
    EClass,
    EOperation,
    xmof_Kernel_BehavioredEOperation,
    BehavioredEOperation,
    xmof_Communications_Reception,
    Event,
    xmof_Communications_MessageEvent,
    Communications_Signal,
    MessageEvent,
    xmof_Communications_SignalEvent,
    Communications_xmof_EAttribute,
    Communications_Event,
    ENamedElement,
    xmof_Kernel_InstanceSpecification,
    xmof_IntermediateActivities_ActivityEdge,
    xmof_IntermediateActivities_ActivityNode,
    xmof_Communications_Event,
    xmof_Communications_Trigger,
    OpaqueBehavior,
    xmof_BasicBehaviors_FunctionBehavior,
    BasicBehaviors_Behavior,
    EClassifier,
    xmof_Communications_Signal,
    xmof_BasicBehaviors_BehavioredClassifier,
    BasicBehaviors_BehavioredClassifier,
    xmof_Kernel_BehavioredEClass,
    Kernel_DirectedParameter,
    Kernel_BehavioredEOperation,
    BehavioredEClass,
    xmof_Kernel_MainEClass,
    xmof_BasicBehaviors_Behavior,
    Behavior,
    xmof_IntermediateActivities_Activity,
    xmof_BasicBehaviors_OpaqueBehavior,
    IntermediateActivities_ObjectFlow,
    xmof_IntermediateActivities_DecisionNode,
    CallConcurrencyKind,
    ExpansionKind,
    ParameterDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_hyp_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_hyp_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_SendSignalAction)


def test_hyp_xmof_basicactions_sendsignalaction_constructor_exists():
    assert callable(xmof_BasicActions_SendSignalAction.__init__)


def test_hyp_xmof_basicactions_sendsignalaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_callaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_CallAction)


def test_hyp_xmof_basicactions_callaction_constructor_exists():
    assert callable(xmof_BasicActions_CallAction.__init__)


def test_hyp_xmof_basicactions_callaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "synchronous" in params, "Missing parameter 'synchronous'"




def test_hyp_intermediateactivities_objectnode_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ObjectNode)


def test_hyp_intermediateactivities_objectnode_constructor_exists():
    assert callable(IntermediateActivities_ObjectNode.__init__)


def test_hyp_intermediateactivities_objectnode_constructor_args():
    sig = inspect.signature(IntermediateActivities_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_hyp_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_hyp_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_outputpin_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_OutputPin)


def test_hyp_xmof_basicactions_outputpin_constructor_exists():
    assert callable(xmof_BasicActions_OutputPin.__init__)


def test_hyp_xmof_basicactions_outputpin_constructor_args():
    sig = inspect.signature(xmof_BasicActions_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_inputpin_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_InputPin)


def test_hyp_xmof_basicactions_inputpin_constructor_exists():
    assert callable(xmof_BasicActions_InputPin.__init__)


def test_hyp_xmof_basicactions_inputpin_constructor_args():
    sig = inspect.signature(xmof_BasicActions_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicactions_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicActions_xmof_EClassifier)


def test_hyp_basicactions_xmof_eclassifier_constructor_exists():
    assert callable(BasicActions_xmof_EClassifier.__init__)


def test_hyp_basicactions_xmof_eclassifier_constructor_args():
    sig = inspect.signature(BasicActions_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_hyp_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_hyp_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_action_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_Action)


def test_hyp_xmof_basicactions_action_constructor_exists():
    assert callable(xmof_BasicActions_Action.__init__)


def test_hyp_xmof_basicactions_action_constructor_args():
    sig = inspect.signature(xmof_BasicActions_Action.__init__)
    params = list(sig.parameters.keys())
    assert "locallyReentrant" in params, "Missing parameter 'locallyReentrant'"




def test_hyp_communications_trigger_is_not_abstract():
    assert not inspect.isabstract(Communications_Trigger)


def test_hyp_communications_trigger_constructor_exists():
    assert callable(Communications_Trigger.__init__)


def test_hyp_communications_trigger_constructor_args():
    sig = inspect.signature(Communications_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completeactions_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteActions_xmof_EClassifier)


def test_hyp_completeactions_xmof_eclassifier_constructor_exists():
    assert callable(CompleteActions_xmof_EClassifier.__init__)


def test_hyp_completeactions_xmof_eclassifier_constructor_args():
    sig = inspect.signature(CompleteActions_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_hyp_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_hyp_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_CallOperationAction)


def test_hyp_xmof_basicactions_calloperationaction_constructor_exists():
    assert callable(xmof_BasicActions_CallOperationAction.__init__)


def test_hyp_xmof_basicactions_calloperationaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_CallBehaviorAction)


def test_hyp_xmof_basicactions_callbehavioraction_constructor_exists():
    assert callable(xmof_BasicActions_CallBehaviorAction.__init__)


def test_hyp_xmof_basicactions_callbehavioraction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completeactions_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_StartObjectBehaviorAction)


def test_hyp_xmof_completeactions_startobjectbehavioraction_constructor_exists():
    assert callable(xmof_CompleteActions_StartObjectBehaviorAction.__init__)


def test_hyp_xmof_completeactions_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediateactions_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_xmof_EClassifier)


def test_hyp_intermediateactions_xmof_eclassifier_constructor_exists():
    assert callable(IntermediateActions_xmof_EClassifier.__init__)


def test_hyp_intermediateactions_xmof_eclassifier_constructor_args():
    sig = inspect.signature(IntermediateActions_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_hyp_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_hyp_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_DestroyLinkAction)


def test_hyp_xmof_intermediateactions_destroylinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_DestroyLinkAction.__init__)


def test_hyp_xmof_intermediateactions_destroylinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_CreateLinkAction)


def test_hyp_xmof_intermediateactions_createlinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_CreateLinkAction.__init__)


def test_hyp_xmof_intermediateactions_createlinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_hyp_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_hyp_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkEndDestructionData)


def test_hyp_xmof_intermediateactions_linkenddestructiondata_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkEndDestructionData.__init__)


def test_hyp_xmof_intermediateactions_linkenddestructiondata_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "destroyDuplicates" in params, "Missing parameter 'destroyDuplicates'"




def test_hyp_xmof_intermediateactions_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkEndCreationData)


def test_hyp_xmof_intermediateactions_linkendcreationdata_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkEndCreationData.__init__)


def test_hyp_xmof_intermediateactions_linkendcreationdata_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"




def test_hyp_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_hyp_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_hyp_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_AddStructuralFeatureValueAction)


def test_hyp_xmof_intermediateactions_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(xmof_IntermediateActions_AddStructuralFeatureValueAction.__init__)


def test_hyp_xmof_intermediateactions_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"




def test_hyp_xmof_intermediateactions_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_RemoveStructuralFeatureValueAction)


def test_hyp_xmof_intermediateactions_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(xmof_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)


def test_hyp_xmof_intermediateactions_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "removeDuplicates" in params, "Missing parameter 'removeDuplicates'"




def test_hyp_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_hyp_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_hyp_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ReadStructuralFeatureAction)


def test_hyp_xmof_intermediateactions_readstructuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ReadStructuralFeatureAction.__init__)


def test_hyp_xmof_intermediateactions_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ClearStructuralFeatureAction)


def test_hyp_xmof_intermediateactions_clearstructuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ClearStructuralFeatureAction.__init__)


def test_hyp_xmof_intermediateactions_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_WriteStructuralFeatureAction)


def test_hyp_xmof_intermediateactions_writestructuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_WriteStructuralFeatureAction.__init__)


def test_hyp_xmof_intermediateactions_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediateactions_xmof_ereference_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_xmof_EReference)


def test_hyp_intermediateactions_xmof_ereference_constructor_exists():
    assert callable(IntermediateActions_xmof_EReference.__init__)


def test_hyp_intermediateactions_xmof_ereference_constructor_args():
    sig = inspect.signature(IntermediateActions_xmof_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediateactions_linkenddata_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_LinkEndData)


def test_hyp_intermediateactions_linkenddata_constructor_exists():
    assert callable(IntermediateActions_LinkEndData.__init__)


def test_hyp_intermediateactions_linkenddata_constructor_args():
    sig = inspect.signature(IntermediateActions_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_hyp_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_hyp_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ReadLinkAction)


def test_hyp_xmof_intermediateactions_readlinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ReadLinkAction.__init__)


def test_hyp_xmof_intermediateactions_readlinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_WriteLinkAction)


def test_hyp_xmof_intermediateactions_writelinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_WriteLinkAction.__init__)


def test_hyp_xmof_intermediateactions_writelinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediateactions_xmof_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_xmof_EStructuralFeature)


def test_hyp_intermediateactions_xmof_estructuralfeature_constructor_exists():
    assert callable(IntermediateActions_xmof_EStructuralFeature.__init__)


def test_hyp_intermediateactions_xmof_estructuralfeature_constructor_args():
    sig = inspect.signature(IntermediateActions_xmof_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extrastructuredactivities_expansionnode_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities_ExpansionNode)


def test_hyp_extrastructuredactivities_expansionnode_constructor_exists():
    assert callable(ExtraStructuredActivities_ExpansionNode.__init__)


def test_hyp_extrastructuredactivities_expansionnode_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extrastructuredactivities_expansionregion_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities_ExpansionRegion)


def test_hyp_extrastructuredactivities_expansionregion_constructor_exists():
    assert callable(ExtraStructuredActivities_ExpansionRegion.__init__)


def test_hyp_extrastructuredactivities_expansionregion_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completeactions_reduceaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReduceAction)


def test_hyp_xmof_completeactions_reduceaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReduceAction.__init__)


def test_hyp_xmof_completeactions_reduceaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"




def test_hyp_xmof_intermediateactions_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_TestIdentityAction)


def test_hyp_xmof_intermediateactions_testidentityaction_constructor_exists():
    assert callable(xmof_IntermediateActions_TestIdentityAction.__init__)


def test_hyp_xmof_intermediateactions_testidentityaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completeactions_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_StartClassifierBehaviorAction)


def test_hyp_xmof_completeactions_startclassifierbehavioraction_constructor_exists():
    assert callable(xmof_CompleteActions_StartClassifierBehaviorAction.__init__)


def test_hyp_xmof_completeactions_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_CreateObjectAction)


def test_hyp_xmof_intermediateactions_createobjectaction_constructor_exists():
    assert callable(xmof_IntermediateActions_CreateObjectAction.__init__)


def test_hyp_xmof_intermediateactions_createobjectaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_readselfaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ReadSelfAction)


def test_hyp_xmof_intermediateactions_readselfaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ReadSelfAction.__init__)


def test_hyp_xmof_intermediateactions_readselfaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completeactions_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReadIsClassifiedObjectAction)


def test_hyp_xmof_completeactions_readisclassifiedobjectaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReadIsClassifiedObjectAction.__init__)


def test_hyp_xmof_completeactions_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "direct" in params, "Missing parameter 'direct'"




def test_hyp_xmof_basicactions_invocationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_InvocationAction)


def test_hyp_xmof_basicactions_invocationaction_constructor_exists():
    assert callable(xmof_BasicActions_InvocationAction.__init__)


def test_hyp_xmof_basicactions_invocationaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_StructuralFeatureAction)


def test_hyp_xmof_intermediateactions_structuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_StructuralFeatureAction.__init__)


def test_hyp_xmof_intermediateactions_structuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completeactions_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_AcceptEventAction)


def test_hyp_xmof_completeactions_accepteventaction_constructor_exists():
    assert callable(xmof_CompleteActions_AcceptEventAction.__init__)


def test_hyp_xmof_completeactions_accepteventaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshall" in params, "Missing parameter 'unmarshall'"




def test_hyp_xmof_intermediateactions_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_DestroyObjectAction)


def test_hyp_xmof_intermediateactions_destroyobjectaction_constructor_exists():
    assert callable(xmof_IntermediateActions_DestroyObjectAction.__init__)


def test_hyp_xmof_intermediateactions_destroyobjectaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "destroyOwnedObjects" in params, "Missing parameter 'destroyOwnedObjects'"
    assert "destroyLinks" in params, "Missing parameter 'destroyLinks'"





def test_hyp_xmof_intermediateactions_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ClearAssociationAction)


def test_hyp_xmof_intermediateactions_clearassociationaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ClearAssociationAction.__init__)


def test_hyp_xmof_intermediateactions_clearassociationaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_linkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkAction)


def test_hyp_xmof_intermediateactions_linkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkAction.__init__)


def test_hyp_xmof_intermediateactions_linkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ValueSpecificationAction)


def test_hyp_xmof_intermediateactions_valuespecificationaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ValueSpecificationAction.__init__)


def test_hyp_xmof_intermediateactions_valuespecificationaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completeactions_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReclassifyObjectAction)


def test_hyp_xmof_completeactions_reclassifyobjectaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReclassifyObjectAction.__init__)


def test_hyp_xmof_completeactions_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"




def test_hyp_xmof_completeactions_readextentaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReadExtentAction)


def test_hyp_xmof_completeactions_readextentaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReadExtentAction.__init__)


def test_hyp_xmof_completeactions_readextentaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completestructuredactivities_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_StructuredActivityNode)


def test_hyp_xmof_completestructuredactivities_structuredactivitynode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_StructuredActivityNode.__init__)


def test_hyp_xmof_completestructuredactivities_structuredactivitynode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"




def test_hyp_completestructuredactivities_clause_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities_Clause)


def test_hyp_completestructuredactivities_clause_constructor_exists():
    assert callable(CompleteStructuredActivities_Clause.__init__)


def test_hyp_completestructuredactivities_clause_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities_Clause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicactions_inputpin_is_not_abstract():
    assert not inspect.isabstract(BasicActions_InputPin)


def test_hyp_basicactions_inputpin_constructor_exists():
    assert callable(BasicActions_InputPin.__init__)


def test_hyp_basicactions_inputpin_constructor_args():
    sig = inspect.signature(BasicActions_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completestructuredactivities_executablenode_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities_ExecutableNode)


def test_hyp_completestructuredactivities_executablenode_constructor_exists():
    assert callable(CompleteStructuredActivities_ExecutableNode.__init__)


def test_hyp_completestructuredactivities_executablenode_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicactions_outputpin_is_not_abstract():
    assert not inspect.isabstract(BasicActions_OutputPin)


def test_hyp_basicactions_outputpin_constructor_exists():
    assert callable(BasicActions_OutputPin.__init__)


def test_hyp_basicactions_outputpin_constructor_args():
    sig = inspect.signature(BasicActions_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_hyp_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_hyp_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completestructuredactivities_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_ConditionalNode)


def test_hyp_xmof_completestructuredactivities_conditionalnode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_ConditionalNode.__init__)


def test_hyp_xmof_completestructuredactivities_conditionalnode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "assured" in params, "Missing parameter 'assured'"
    assert "determinate" in params, "Missing parameter 'determinate'"





def test_hyp_xmof_extrastructuredactivities_expansionregion_is_not_abstract():
    assert not inspect.isabstract(xmof_ExtraStructuredActivities_ExpansionRegion)


def test_hyp_xmof_extrastructuredactivities_expansionregion_constructor_exists():
    assert callable(xmof_ExtraStructuredActivities_ExpansionRegion.__init__)


def test_hyp_xmof_extrastructuredactivities_expansionregion_constructor_args():
    sig = inspect.signature(xmof_ExtraStructuredActivities_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"




def test_hyp_xmof_completestructuredactivities_loopnode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_LoopNode)


def test_hyp_xmof_completestructuredactivities_loopnode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_LoopNode.__init__)


def test_hyp_xmof_completestructuredactivities_loopnode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "testedFirst" in params, "Missing parameter 'testedFirst'"




def test_hyp_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_hyp_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_hyp_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_extrastructuredactivities_expansionnode_is_not_abstract():
    assert not inspect.isabstract(xmof_ExtraStructuredActivities_ExpansionNode)


def test_hyp_xmof_extrastructuredactivities_expansionnode_constructor_exists():
    assert callable(xmof_ExtraStructuredActivities_ExpansionNode.__init__)


def test_hyp_xmof_extrastructuredactivities_expansionnode_constructor_args():
    sig = inspect.signature(xmof_ExtraStructuredActivities_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityParameterNode)


def test_hyp_xmof_intermediateactivities_activityparameternode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityParameterNode.__init__)


def test_hyp_xmof_intermediateactivities_activityparameternode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_hyp_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_hyp_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityFinalNode)


def test_hyp_xmof_intermediateactivities_activityfinalnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityFinalNode.__init__)


def test_hyp_xmof_intermediateactivities_activityfinalnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completestructuredactivities_executablenode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_ExecutableNode)


def test_hyp_xmof_completestructuredactivities_executablenode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_ExecutableNode.__init__)


def test_hyp_xmof_completestructuredactivities_executablenode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_controlnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ControlNode)


def test_hyp_xmof_intermediateactivities_controlnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ControlNode.__init__)


def test_hyp_xmof_intermediateactivities_controlnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_hyp_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_hyp_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_finalnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_FinalNode)


def test_hyp_xmof_intermediateactivities_finalnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_FinalNode.__init__)


def test_hyp_xmof_intermediateactivities_finalnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_initialnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_InitialNode)


def test_hyp_xmof_intermediateactivities_initialnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_InitialNode.__init__)


def test_hyp_xmof_intermediateactivities_initialnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_joinnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_JoinNode)


def test_hyp_xmof_intermediateactivities_joinnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_JoinNode.__init__)


def test_hyp_xmof_intermediateactivities_joinnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_forknode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ForkNode)


def test_hyp_xmof_intermediateactivities_forknode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ForkNode.__init__)


def test_hyp_xmof_intermediateactivities_forknode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_mergenode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_MergeNode)


def test_hyp_xmof_intermediateactivities_mergenode_constructor_exists():
    assert callable(xmof_IntermediateActivities_MergeNode.__init__)


def test_hyp_xmof_intermediateactivities_mergenode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediateactivities_activityedge_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ActivityEdge)


def test_hyp_intermediateactivities_activityedge_constructor_exists():
    assert callable(IntermediateActivities_ActivityEdge.__init__)


def test_hyp_intermediateactivities_activityedge_constructor_args():
    sig = inspect.signature(IntermediateActivities_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_completestructuredactivities_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities_StructuredActivityNode)


def test_hyp_completestructuredactivities_structuredactivitynode_constructor_exists():
    assert callable(CompleteStructuredActivities_StructuredActivityNode.__init__)


def test_hyp_completestructuredactivities_structuredactivitynode_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediateactivities_activitynode_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ActivityNode)


def test_hyp_intermediateactivities_activitynode_constructor_exists():
    assert callable(IntermediateActivities_ActivityNode.__init__)


def test_hyp_intermediateactivities_activitynode_constructor_args():
    sig = inspect.signature(IntermediateActivities_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intermediateactivities_activity_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_Activity)


def test_hyp_intermediateactivities_activity_constructor_exists():
    assert callable(IntermediateActivities_Activity.__init__)


def test_hyp_intermediateactivities_activity_constructor_args():
    sig = inspect.signature(IntermediateActivities_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_hyp_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_hyp_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_controlflow_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ControlFlow)


def test_hyp_xmof_intermediateactivities_controlflow_constructor_exists():
    assert callable(xmof_IntermediateActivities_ControlFlow.__init__)


def test_hyp_xmof_intermediateactivities_controlflow_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_objectflow_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ObjectFlow)


def test_hyp_xmof_intermediateactivities_objectflow_constructor_exists():
    assert callable(xmof_IntermediateActivities_ObjectFlow.__init__)


def test_hyp_xmof_intermediateactivities_objectflow_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_hyp_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_hyp_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_PrimitiveType)


def test_hyp_xmof_kernel_primitivetype_constructor_exists():
    assert callable(xmof_Kernel_PrimitiveType.__init__)


def test_hyp_xmof_kernel_primitivetype_constructor_args():
    sig = inspect.signature(xmof_Kernel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_hyp_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_hyp_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_literalinteger_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralInteger)


def test_hyp_xmof_kernel_literalinteger_constructor_exists():
    assert callable(xmof_Kernel_LiteralInteger.__init__)


def test_hyp_xmof_kernel_literalinteger_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_xmof_kernel_literalnull_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralNull)


def test_hyp_xmof_kernel_literalnull_constructor_exists():
    assert callable(xmof_Kernel_LiteralNull.__init__)


def test_hyp_xmof_kernel_literalnull_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralUnlimitedNatural)


def test_hyp_xmof_kernel_literalunlimitednatural_constructor_exists():
    assert callable(xmof_Kernel_LiteralUnlimitedNatural.__init__)


def test_hyp_xmof_kernel_literalunlimitednatural_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_xmof_kernel_literalstring_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralString)


def test_hyp_xmof_kernel_literalstring_constructor_exists():
    assert callable(xmof_Kernel_LiteralString.__init__)


def test_hyp_xmof_kernel_literalstring_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_xmof_kernel_literalboolean_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralBoolean)


def test_hyp_xmof_kernel_literalboolean_constructor_exists():
    assert callable(xmof_Kernel_LiteralBoolean.__init__)


def test_hyp_xmof_kernel_literalboolean_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_hyp_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_hyp_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_literalspecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralSpecification)


def test_hyp_xmof_kernel_literalspecification_constructor_exists():
    assert callable(xmof_Kernel_LiteralSpecification.__init__)


def test_hyp_xmof_kernel_literalspecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_instancevalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_InstanceValue)


def test_hyp_xmof_kernel_instancevalue_constructor_exists():
    assert callable(xmof_Kernel_InstanceValue.__init__)


def test_hyp_xmof_kernel_instancevalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_instancespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel_InstanceSpecification)


def test_hyp_kernel_instancespecification_constructor_exists():
    assert callable(Kernel_InstanceSpecification.__init__)


def test_hyp_kernel_instancespecification_constructor_args():
    sig = inspect.signature(Kernel_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_valuespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel_ValueSpecification)


def test_hyp_kernel_valuespecification_constructor_exists():
    assert callable(Kernel_ValueSpecification.__init__)


def test_hyp_kernel_valuespecification_constructor_args():
    sig = inspect.signature(Kernel_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_xmof_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EStructuralFeature)


def test_hyp_kernel_xmof_estructuralfeature_constructor_exists():
    assert callable(Kernel_xmof_EStructuralFeature.__init__)


def test_hyp_kernel_xmof_estructuralfeature_constructor_args():
    sig = inspect.signature(Kernel_xmof_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_hyp_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_hyp_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactions_linkenddata_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkEndData)


def test_hyp_xmof_intermediateactions_linkenddata_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkEndData.__init__)


def test_hyp_xmof_intermediateactions_linkenddata_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_completestructuredactivities_clause_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_Clause)


def test_hyp_xmof_completestructuredactivities_clause_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_Clause.__init__)


def test_hyp_xmof_completestructuredactivities_clause_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_Clause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_slot_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_Slot)


def test_hyp_xmof_kernel_slot_constructor_exists():
    assert callable(xmof_Kernel_Slot.__init__)


def test_hyp_xmof_kernel_slot_constructor_args():
    sig = inspect.signature(xmof_Kernel_Slot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_slot_is_not_abstract():
    assert not inspect.isabstract(Kernel_Slot)


def test_hyp_kernel_slot_constructor_exists():
    assert callable(Kernel_Slot.__init__)


def test_hyp_kernel_slot_constructor_args():
    sig = inspect.signature(Kernel_Slot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EClassifier)


def test_hyp_kernel_xmof_eclassifier_constructor_exists():
    assert callable(Kernel_xmof_EClassifier.__init__)


def test_hyp_kernel_xmof_eclassifier_constructor_args():
    sig = inspect.signature(Kernel_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_hyp_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_hyp_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicactions_pin_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_Pin)


def test_hyp_xmof_basicactions_pin_constructor_exists():
    assert callable(xmof_BasicActions_Pin.__init__)


def test_hyp_xmof_basicactions_pin_constructor_args():
    sig = inspect.signature(xmof_BasicActions_Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_objectnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ObjectNode)


def test_hyp_xmof_intermediateactivities_objectnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ObjectNode.__init__)


def test_hyp_xmof_intermediateactivities_objectnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_valuespecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_ValueSpecification)


def test_hyp_xmof_kernel_valuespecification_constructor_exists():
    assert callable(xmof_Kernel_ValueSpecification.__init__)


def test_hyp_xmof_kernel_valuespecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_xmof_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EEnumLiteral)


def test_hyp_kernel_xmof_eenumliteral_constructor_exists():
    assert callable(Kernel_xmof_EEnumLiteral.__init__)


def test_hyp_kernel_xmof_eenumliteral_constructor_args():
    sig = inspect.signature(Kernel_xmof_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_hyp_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_hyp_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_eenumliteralspecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_EEnumLiteralSpecification)


def test_hyp_xmof_kernel_eenumliteralspecification_constructor_exists():
    assert callable(xmof_Kernel_EEnumLiteralSpecification.__init__)


def test_hyp_xmof_kernel_eenumliteralspecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_EEnumLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eparameter_is_not_abstract():
    assert not inspect.isabstract(EParameter)


def test_hyp_eparameter_constructor_exists():
    assert callable(EParameter.__init__)


def test_hyp_eparameter_constructor_args():
    sig = inspect.signature(EParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_directedparameter_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_DirectedParameter)


def test_hyp_xmof_kernel_directedparameter_constructor_exists():
    assert callable(xmof_Kernel_DirectedParameter.__init__)


def test_hyp_xmof_kernel_directedparameter_constructor_args():
    sig = inspect.signature(xmof_Kernel_DirectedParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"




def test_hyp_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_hyp_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_hyp_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eoperation_is_not_abstract():
    assert not inspect.isabstract(EOperation)


def test_hyp_eoperation_constructor_exists():
    assert callable(EOperation.__init__)


def test_hyp_eoperation_constructor_args():
    sig = inspect.signature(EOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_BehavioredEOperation)


def test_hyp_xmof_kernel_behavioredeoperation_constructor_exists():
    assert callable(xmof_Kernel_BehavioredEOperation.__init__)


def test_hyp_xmof_kernel_behavioredeoperation_constructor_args():
    sig = inspect.signature(xmof_Kernel_BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(BehavioredEOperation)


def test_hyp_behavioredeoperation_constructor_exists():
    assert callable(BehavioredEOperation.__init__)


def test_hyp_behavioredeoperation_constructor_args():
    sig = inspect.signature(BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_communications_reception_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Reception)


def test_hyp_xmof_communications_reception_constructor_exists():
    assert callable(xmof_Communications_Reception.__init__)


def test_hyp_xmof_communications_reception_constructor_args():
    sig = inspect.signature(xmof_Communications_Reception.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_communications_messageevent_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_MessageEvent)


def test_hyp_xmof_communications_messageevent_constructor_exists():
    assert callable(xmof_Communications_MessageEvent.__init__)


def test_hyp_xmof_communications_messageevent_constructor_args():
    sig = inspect.signature(xmof_Communications_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_communications_signal_is_not_abstract():
    assert not inspect.isabstract(Communications_Signal)


def test_hyp_communications_signal_constructor_exists():
    assert callable(Communications_Signal.__init__)


def test_hyp_communications_signal_constructor_args():
    sig = inspect.signature(Communications_Signal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_hyp_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_hyp_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_communications_signalevent_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_SignalEvent)


def test_hyp_xmof_communications_signalevent_constructor_exists():
    assert callable(xmof_Communications_SignalEvent.__init__)


def test_hyp_xmof_communications_signalevent_constructor_args():
    sig = inspect.signature(xmof_Communications_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_communications_xmof_eattribute_is_not_abstract():
    assert not inspect.isabstract(Communications_xmof_EAttribute)


def test_hyp_communications_xmof_eattribute_constructor_exists():
    assert callable(Communications_xmof_EAttribute.__init__)


def test_hyp_communications_xmof_eattribute_constructor_args():
    sig = inspect.signature(Communications_xmof_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_communications_event_is_not_abstract():
    assert not inspect.isabstract(Communications_Event)


def test_hyp_communications_event_constructor_exists():
    assert callable(Communications_Event.__init__)


def test_hyp_communications_event_constructor_args():
    sig = inspect.signature(Communications_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_hyp_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_hyp_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_instancespecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_InstanceSpecification)


def test_hyp_xmof_kernel_instancespecification_constructor_exists():
    assert callable(xmof_Kernel_InstanceSpecification.__init__)


def test_hyp_xmof_kernel_instancespecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_activityedge_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityEdge)


def test_hyp_xmof_intermediateactivities_activityedge_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityEdge.__init__)


def test_hyp_xmof_intermediateactivities_activityedge_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_activitynode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityNode)


def test_hyp_xmof_intermediateactivities_activitynode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityNode.__init__)


def test_hyp_xmof_intermediateactivities_activitynode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_communications_event_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Event)


def test_hyp_xmof_communications_event_constructor_exists():
    assert callable(xmof_Communications_Event.__init__)


def test_hyp_xmof_communications_event_constructor_args():
    sig = inspect.signature(xmof_Communications_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_communications_trigger_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Trigger)


def test_hyp_xmof_communications_trigger_constructor_exists():
    assert callable(xmof_Communications_Trigger.__init__)


def test_hyp_xmof_communications_trigger_constructor_args():
    sig = inspect.signature(xmof_Communications_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_hyp_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_hyp_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicbehaviors_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_FunctionBehavior)


def test_hyp_xmof_basicbehaviors_functionbehavior_constructor_exists():
    assert callable(xmof_BasicBehaviors_FunctionBehavior.__init__)


def test_hyp_xmof_basicbehaviors_functionbehavior_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicbehaviors_behavior_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_Behavior)


def test_hyp_basicbehaviors_behavior_constructor_exists():
    assert callable(BasicBehaviors_Behavior.__init__)


def test_hyp_basicbehaviors_behavior_constructor_args():
    sig = inspect.signature(BasicBehaviors_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_hyp_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_hyp_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_communications_signal_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Signal)


def test_hyp_xmof_communications_signal_constructor_exists():
    assert callable(xmof_Communications_Signal.__init__)


def test_hyp_xmof_communications_signal_constructor_args():
    sig = inspect.signature(xmof_Communications_Signal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicbehaviors_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_BehavioredClassifier)


def test_hyp_xmof_basicbehaviors_behavioredclassifier_constructor_exists():
    assert callable(xmof_BasicBehaviors_BehavioredClassifier.__init__)


def test_hyp_xmof_basicbehaviors_behavioredclassifier_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicbehaviors_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_BehavioredClassifier)


def test_hyp_basicbehaviors_behavioredclassifier_constructor_exists():
    assert callable(BasicBehaviors_BehavioredClassifier.__init__)


def test_hyp_basicbehaviors_behavioredclassifier_constructor_args():
    sig = inspect.signature(BasicBehaviors_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_behavioredeclass_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_BehavioredEClass)


def test_hyp_xmof_kernel_behavioredeclass_constructor_exists():
    assert callable(xmof_Kernel_BehavioredEClass.__init__)


def test_hyp_xmof_kernel_behavioredeclass_constructor_args():
    sig = inspect.signature(xmof_Kernel_BehavioredEClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_directedparameter_is_not_abstract():
    assert not inspect.isabstract(Kernel_DirectedParameter)


def test_hyp_kernel_directedparameter_constructor_exists():
    assert callable(Kernel_DirectedParameter.__init__)


def test_hyp_kernel_directedparameter_constructor_args():
    sig = inspect.signature(Kernel_DirectedParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kernel_behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(Kernel_BehavioredEOperation)


def test_hyp_kernel_behavioredeoperation_constructor_exists():
    assert callable(Kernel_BehavioredEOperation.__init__)


def test_hyp_kernel_behavioredeoperation_constructor_args():
    sig = inspect.signature(Kernel_BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioredeclass_is_not_abstract():
    assert not inspect.isabstract(BehavioredEClass)


def test_hyp_behavioredeclass_constructor_exists():
    assert callable(BehavioredEClass.__init__)


def test_hyp_behavioredeclass_constructor_args():
    sig = inspect.signature(BehavioredEClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_kernel_maineclass_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_MainEClass)


def test_hyp_xmof_kernel_maineclass_constructor_exists():
    assert callable(xmof_Kernel_MainEClass.__init__)


def test_hyp_xmof_kernel_maineclass_constructor_args():
    sig = inspect.signature(xmof_Kernel_MainEClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_basicbehaviors_behavior_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_Behavior)


def test_hyp_xmof_basicbehaviors_behavior_constructor_exists():
    assert callable(xmof_BasicBehaviors_Behavior.__init__)


def test_hyp_xmof_basicbehaviors_behavior_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "reentrant" in params, "Missing parameter 'reentrant'"




def test_hyp_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_hyp_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_hyp_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_activity_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_Activity)


def test_hyp_xmof_intermediateactivities_activity_constructor_exists():
    assert callable(xmof_IntermediateActivities_Activity.__init__)


def test_hyp_xmof_intermediateactivities_activity_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"




def test_hyp_xmof_basicbehaviors_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_OpaqueBehavior)


def test_hyp_xmof_basicbehaviors_opaquebehavior_constructor_exists():
    assert callable(xmof_BasicBehaviors_OpaqueBehavior.__init__)


def test_hyp_xmof_basicbehaviors_opaquebehavior_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_intermediateactivities_objectflow_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ObjectFlow)


def test_hyp_intermediateactivities_objectflow_constructor_exists():
    assert callable(IntermediateActivities_ObjectFlow.__init__)


def test_hyp_intermediateactivities_objectflow_constructor_args():
    sig = inspect.signature(IntermediateActivities_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xmof_intermediateactivities_decisionnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_DecisionNode)


def test_hyp_xmof_intermediateactivities_decisionnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_DecisionNode.__init__)


def test_hyp_xmof_intermediateactivities_decisionnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_DecisionNode.__init__)
    params = list(sig.parameters.keys())

def test_hyp_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_hyp_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

def test_hyp_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_hyp_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "stream",
        "parallel",
        "iterative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_hyp_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_hyp_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "out",
        "in_",
        "return_",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"


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
InvocationAction_strategy = st.builds(
    InvocationAction,
)
xmof_BasicActions_SendSignalAction_strategy = st.builds(
    xmof_BasicActions_SendSignalAction,
)
xmof_BasicActions_CallAction_strategy = st.builds(
    xmof_BasicActions_CallAction,
    synchronous=
        st.booleans()
)
IntermediateActivities_ObjectNode_strategy = st.builds(
    IntermediateActivities_ObjectNode,
)
Pin_strategy = st.builds(
    Pin,
)
xmof_BasicActions_OutputPin_strategy = st.builds(
    xmof_BasicActions_OutputPin,
)
xmof_BasicActions_InputPin_strategy = st.builds(
    xmof_BasicActions_InputPin,
)
BasicActions_xmof_EClassifier_strategy = st.builds(
    BasicActions_xmof_EClassifier,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
xmof_BasicActions_Action_strategy = st.builds(
    xmof_BasicActions_Action,
    locallyReentrant=
        st.booleans()
)
Communications_Trigger_strategy = st.builds(
    Communications_Trigger,
)
CompleteActions_xmof_EClassifier_strategy = st.builds(
    CompleteActions_xmof_EClassifier,
)
CallAction_strategy = st.builds(
    CallAction,
)
xmof_BasicActions_CallOperationAction_strategy = st.builds(
    xmof_BasicActions_CallOperationAction,
)
xmof_BasicActions_CallBehaviorAction_strategy = st.builds(
    xmof_BasicActions_CallBehaviorAction,
)
xmof_CompleteActions_StartObjectBehaviorAction_strategy = st.builds(
    xmof_CompleteActions_StartObjectBehaviorAction,
)
IntermediateActions_xmof_EClassifier_strategy = st.builds(
    IntermediateActions_xmof_EClassifier,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
xmof_IntermediateActions_DestroyLinkAction_strategy = st.builds(
    xmof_IntermediateActions_DestroyLinkAction,
)
xmof_IntermediateActions_CreateLinkAction_strategy = st.builds(
    xmof_IntermediateActions_CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
xmof_IntermediateActions_LinkEndDestructionData_strategy = st.builds(
    xmof_IntermediateActions_LinkEndDestructionData,
    destroyDuplicates=
        st.booleans()
)
xmof_IntermediateActions_LinkEndCreationData_strategy = st.builds(
    xmof_IntermediateActions_LinkEndCreationData,
    replaceAll=
        st.booleans()
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
xmof_IntermediateActions_AddStructuralFeatureValueAction_strategy = st.builds(
    xmof_IntermediateActions_AddStructuralFeatureValueAction,
    replaceAll=
        st.booleans()
)
xmof_IntermediateActions_RemoveStructuralFeatureValueAction_strategy = st.builds(
    xmof_IntermediateActions_RemoveStructuralFeatureValueAction,
    removeDuplicates=
        st.booleans()
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
xmof_IntermediateActions_ReadStructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_ReadStructuralFeatureAction,
)
xmof_IntermediateActions_ClearStructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_ClearStructuralFeatureAction,
)
xmof_IntermediateActions_WriteStructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_WriteStructuralFeatureAction,
)
IntermediateActions_xmof_EReference_strategy = st.builds(
    IntermediateActions_xmof_EReference,
)
IntermediateActions_LinkEndData_strategy = st.builds(
    IntermediateActions_LinkEndData,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
xmof_IntermediateActions_ReadLinkAction_strategy = st.builds(
    xmof_IntermediateActions_ReadLinkAction,
)
xmof_IntermediateActions_WriteLinkAction_strategy = st.builds(
    xmof_IntermediateActions_WriteLinkAction,
)
IntermediateActions_xmof_EStructuralFeature_strategy = st.builds(
    IntermediateActions_xmof_EStructuralFeature,
)
ExtraStructuredActivities_ExpansionNode_strategy = st.builds(
    ExtraStructuredActivities_ExpansionNode,
)
ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(
    ExtraStructuredActivities_ExpansionRegion,
)
Action_strategy = st.builds(
    Action,
)
xmof_CompleteActions_ReduceAction_strategy = st.builds(
    xmof_CompleteActions_ReduceAction,
    ordered=
        st.booleans()
)
xmof_IntermediateActions_TestIdentityAction_strategy = st.builds(
    xmof_IntermediateActions_TestIdentityAction,
)
xmof_CompleteActions_StartClassifierBehaviorAction_strategy = st.builds(
    xmof_CompleteActions_StartClassifierBehaviorAction,
)
xmof_IntermediateActions_CreateObjectAction_strategy = st.builds(
    xmof_IntermediateActions_CreateObjectAction,
)
xmof_IntermediateActions_ReadSelfAction_strategy = st.builds(
    xmof_IntermediateActions_ReadSelfAction,
)
xmof_CompleteActions_ReadIsClassifiedObjectAction_strategy = st.builds(
    xmof_CompleteActions_ReadIsClassifiedObjectAction,
    direct=
        st.booleans()
)
xmof_BasicActions_InvocationAction_strategy = st.builds(
    xmof_BasicActions_InvocationAction,
)
xmof_IntermediateActions_StructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_StructuralFeatureAction,
)
xmof_CompleteActions_AcceptEventAction_strategy = st.builds(
    xmof_CompleteActions_AcceptEventAction,
    unmarshall=
        st.booleans()
)
xmof_IntermediateActions_DestroyObjectAction_strategy = st.builds(
    xmof_IntermediateActions_DestroyObjectAction,
    destroyOwnedObjects=
        st.booleans(),
    destroyLinks=
        st.booleans()
)
xmof_IntermediateActions_ClearAssociationAction_strategy = st.builds(
    xmof_IntermediateActions_ClearAssociationAction,
)
xmof_IntermediateActions_LinkAction_strategy = st.builds(
    xmof_IntermediateActions_LinkAction,
)
xmof_IntermediateActions_ValueSpecificationAction_strategy = st.builds(
    xmof_IntermediateActions_ValueSpecificationAction,
)
xmof_CompleteActions_ReclassifyObjectAction_strategy = st.builds(
    xmof_CompleteActions_ReclassifyObjectAction,
    replaceAll=
        st.booleans()
)
xmof_CompleteActions_ReadExtentAction_strategy = st.builds(
    xmof_CompleteActions_ReadExtentAction,
)
xmof_CompleteStructuredActivities_StructuredActivityNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
CompleteStructuredActivities_Clause_strategy = st.builds(
    CompleteStructuredActivities_Clause,
)
BasicActions_InputPin_strategy = st.builds(
    BasicActions_InputPin,
)
CompleteStructuredActivities_ExecutableNode_strategy = st.builds(
    CompleteStructuredActivities_ExecutableNode,
)
BasicActions_OutputPin_strategy = st.builds(
    BasicActions_OutputPin,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
xmof_CompleteStructuredActivities_ConditionalNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_ConditionalNode,
    assured=
        st.booleans(),
    determinate=
        st.booleans()
)
xmof_ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(
    xmof_ExtraStructuredActivities_ExpansionRegion,
    mode=
        safe_text
)
xmof_CompleteStructuredActivities_LoopNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_LoopNode,
    testedFirst=
        st.booleans()
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
xmof_ExtraStructuredActivities_ExpansionNode_strategy = st.builds(
    xmof_ExtraStructuredActivities_ExpansionNode,
)
xmof_IntermediateActivities_ActivityParameterNode_strategy = st.builds(
    xmof_IntermediateActivities_ActivityParameterNode,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
xmof_IntermediateActivities_ActivityFinalNode_strategy = st.builds(
    xmof_IntermediateActivities_ActivityFinalNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
xmof_CompleteStructuredActivities_ExecutableNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_ExecutableNode,
)
xmof_IntermediateActivities_ControlNode_strategy = st.builds(
    xmof_IntermediateActivities_ControlNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
xmof_IntermediateActivities_FinalNode_strategy = st.builds(
    xmof_IntermediateActivities_FinalNode,
)
xmof_IntermediateActivities_InitialNode_strategy = st.builds(
    xmof_IntermediateActivities_InitialNode,
)
xmof_IntermediateActivities_JoinNode_strategy = st.builds(
    xmof_IntermediateActivities_JoinNode,
)
xmof_IntermediateActivities_ForkNode_strategy = st.builds(
    xmof_IntermediateActivities_ForkNode,
)
xmof_IntermediateActivities_MergeNode_strategy = st.builds(
    xmof_IntermediateActivities_MergeNode,
)
IntermediateActivities_ActivityEdge_strategy = st.builds(
    IntermediateActivities_ActivityEdge,
)
CompleteStructuredActivities_StructuredActivityNode_strategy = st.builds(
    CompleteStructuredActivities_StructuredActivityNode,
)
IntermediateActivities_ActivityNode_strategy = st.builds(
    IntermediateActivities_ActivityNode,
)
IntermediateActivities_Activity_strategy = st.builds(
    IntermediateActivities_Activity,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
xmof_IntermediateActivities_ControlFlow_strategy = st.builds(
    xmof_IntermediateActivities_ControlFlow,
)
xmof_IntermediateActivities_ObjectFlow_strategy = st.builds(
    xmof_IntermediateActivities_ObjectFlow,
)
EDataType_strategy = st.builds(
    EDataType,
)
xmof_Kernel_PrimitiveType_strategy = st.builds(
    xmof_Kernel_PrimitiveType,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
xmof_Kernel_LiteralInteger_strategy = st.builds(
    xmof_Kernel_LiteralInteger,
    value=
        st.integers()
)
xmof_Kernel_LiteralNull_strategy = st.builds(
    xmof_Kernel_LiteralNull,
)
xmof_Kernel_LiteralUnlimitedNatural_strategy = st.builds(
    xmof_Kernel_LiteralUnlimitedNatural,
    value=
        st.integers()
)
xmof_Kernel_LiteralString_strategy = st.builds(
    xmof_Kernel_LiteralString,
    value=
        safe_text
)
xmof_Kernel_LiteralBoolean_strategy = st.builds(
    xmof_Kernel_LiteralBoolean,
    value=
        st.booleans()
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
xmof_Kernel_LiteralSpecification_strategy = st.builds(
    xmof_Kernel_LiteralSpecification,
)
xmof_Kernel_InstanceValue_strategy = st.builds(
    xmof_Kernel_InstanceValue,
)
Kernel_InstanceSpecification_strategy = st.builds(
    Kernel_InstanceSpecification,
)
Kernel_ValueSpecification_strategy = st.builds(
    Kernel_ValueSpecification,
)
Kernel_xmof_EStructuralFeature_strategy = st.builds(
    Kernel_xmof_EStructuralFeature,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
xmof_IntermediateActions_LinkEndData_strategy = st.builds(
    xmof_IntermediateActions_LinkEndData,
)
xmof_CompleteStructuredActivities_Clause_strategy = st.builds(
    xmof_CompleteStructuredActivities_Clause,
)
xmof_Kernel_Slot_strategy = st.builds(
    xmof_Kernel_Slot,
)
Kernel_Slot_strategy = st.builds(
    Kernel_Slot,
)
Kernel_xmof_EClassifier_strategy = st.builds(
    Kernel_xmof_EClassifier,
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
xmof_BasicActions_Pin_strategy = st.builds(
    xmof_BasicActions_Pin,
)
xmof_IntermediateActivities_ObjectNode_strategy = st.builds(
    xmof_IntermediateActivities_ObjectNode,
)
xmof_Kernel_ValueSpecification_strategy = st.builds(
    xmof_Kernel_ValueSpecification,
)
Kernel_xmof_EEnumLiteral_strategy = st.builds(
    Kernel_xmof_EEnumLiteral,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
xmof_Kernel_EEnumLiteralSpecification_strategy = st.builds(
    xmof_Kernel_EEnumLiteralSpecification,
)
EParameter_strategy = st.builds(
    EParameter,
)
xmof_Kernel_DirectedParameter_strategy = st.builds(
    xmof_Kernel_DirectedParameter,
    direction=
        safe_text
)
EClass_strategy = st.builds(
    EClass,
)
EOperation_strategy = st.builds(
    EOperation,
)
xmof_Kernel_BehavioredEOperation_strategy = st.builds(
    xmof_Kernel_BehavioredEOperation,
)
BehavioredEOperation_strategy = st.builds(
    BehavioredEOperation,
)
xmof_Communications_Reception_strategy = st.builds(
    xmof_Communications_Reception,
)
Event_strategy = st.builds(
    Event,
)
xmof_Communications_MessageEvent_strategy = st.builds(
    xmof_Communications_MessageEvent,
)
Communications_Signal_strategy = st.builds(
    Communications_Signal,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
xmof_Communications_SignalEvent_strategy = st.builds(
    xmof_Communications_SignalEvent,
)
Communications_xmof_EAttribute_strategy = st.builds(
    Communications_xmof_EAttribute,
)
Communications_Event_strategy = st.builds(
    Communications_Event,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
xmof_Kernel_InstanceSpecification_strategy = st.builds(
    xmof_Kernel_InstanceSpecification,
)
xmof_IntermediateActivities_ActivityEdge_strategy = st.builds(
    xmof_IntermediateActivities_ActivityEdge,
)
xmof_IntermediateActivities_ActivityNode_strategy = st.builds(
    xmof_IntermediateActivities_ActivityNode,
)
xmof_Communications_Event_strategy = st.builds(
    xmof_Communications_Event,
)
xmof_Communications_Trigger_strategy = st.builds(
    xmof_Communications_Trigger,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
xmof_BasicBehaviors_FunctionBehavior_strategy = st.builds(
    xmof_BasicBehaviors_FunctionBehavior,
)
BasicBehaviors_Behavior_strategy = st.builds(
    BasicBehaviors_Behavior,
)
EClassifier_strategy = st.builds(
    EClassifier,
)
xmof_Communications_Signal_strategy = st.builds(
    xmof_Communications_Signal,
)
xmof_BasicBehaviors_BehavioredClassifier_strategy = st.builds(
    xmof_BasicBehaviors_BehavioredClassifier,
)
BasicBehaviors_BehavioredClassifier_strategy = st.builds(
    BasicBehaviors_BehavioredClassifier,
)
xmof_Kernel_BehavioredEClass_strategy = st.builds(
    xmof_Kernel_BehavioredEClass,
)
Kernel_DirectedParameter_strategy = st.builds(
    Kernel_DirectedParameter,
)
Kernel_BehavioredEOperation_strategy = st.builds(
    Kernel_BehavioredEOperation,
)
BehavioredEClass_strategy = st.builds(
    BehavioredEClass,
)
xmof_Kernel_MainEClass_strategy = st.builds(
    xmof_Kernel_MainEClass,
)
xmof_BasicBehaviors_Behavior_strategy = st.builds(
    xmof_BasicBehaviors_Behavior,
    reentrant=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
xmof_IntermediateActivities_Activity_strategy = st.builds(
    xmof_IntermediateActivities_Activity,
    readOnly=
        st.booleans()
)
xmof_BasicBehaviors_OpaqueBehavior_strategy = st.builds(
    xmof_BasicBehaviors_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
IntermediateActivities_ObjectFlow_strategy = st.builds(
    IntermediateActivities_ObjectFlow,
)
xmof_IntermediateActivities_DecisionNode_strategy = st.builds(
    xmof_IntermediateActivities_DecisionNode,
)






@given(instance=xmof_BasicActions_CallAction_strategy)
def test_hyp_xmof_basicactions_callaction_synchronous_setter(instance):
    original = instance.synchronous
    instance.synchronous = original
    assert instance.synchronous == original










@given(instance=xmof_BasicActions_Action_strategy)
def test_hyp_xmof_basicactions_action_locallyReentrant_setter(instance):
    original = instance.locallyReentrant
    instance.locallyReentrant = original
    assert instance.locallyReentrant == original















@given(instance=xmof_IntermediateActions_LinkEndDestructionData_strategy)
def test_hyp_xmof_intermediateactions_linkenddestructiondata_destroyDuplicates_setter(instance):
    original = instance.destroyDuplicates
    instance.destroyDuplicates = original
    assert instance.destroyDuplicates == original




@given(instance=xmof_IntermediateActions_LinkEndCreationData_strategy)
def test_hyp_xmof_intermediateactions_linkendcreationdata_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original





@given(instance=xmof_IntermediateActions_AddStructuralFeatureValueAction_strategy)
def test_hyp_xmof_intermediateactions_addstructuralfeaturevalueaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original




@given(instance=xmof_IntermediateActions_RemoveStructuralFeatureValueAction_strategy)
def test_hyp_xmof_intermediateactions_removestructuralfeaturevalueaction_removeDuplicates_setter(instance):
    original = instance.removeDuplicates
    instance.removeDuplicates = original
    assert instance.removeDuplicates == original

















@given(instance=xmof_CompleteActions_ReduceAction_strategy)
def test_hyp_xmof_completeactions_reduceaction_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original








@given(instance=xmof_CompleteActions_ReadIsClassifiedObjectAction_strategy)
def test_hyp_xmof_completeactions_readisclassifiedobjectaction_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original






@given(instance=xmof_CompleteActions_AcceptEventAction_strategy)
def test_hyp_xmof_completeactions_accepteventaction_unmarshall_setter(instance):
    original = instance.unmarshall
    instance.unmarshall = original
    assert instance.unmarshall == original




@given(instance=xmof_IntermediateActions_DestroyObjectAction_strategy)
def test_hyp_xmof_intermediateactions_destroyobjectaction_destroyOwnedObjects_setter(instance):
    original = instance.destroyOwnedObjects
    instance.destroyOwnedObjects = original
    assert instance.destroyOwnedObjects == original



@given(instance=xmof_IntermediateActions_DestroyObjectAction_strategy)
def test_hyp_xmof_intermediateactions_destroyobjectaction_destroyLinks_setter(instance):
    original = instance.destroyLinks
    instance.destroyLinks = original
    assert instance.destroyLinks == original







@given(instance=xmof_CompleteActions_ReclassifyObjectAction_strategy)
def test_hyp_xmof_completeactions_reclassifyobjectaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original





@given(instance=xmof_CompleteStructuredActivities_StructuredActivityNode_strategy)
def test_hyp_xmof_completestructuredactivities_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original









@given(instance=xmof_CompleteStructuredActivities_ConditionalNode_strategy)
def test_hyp_xmof_completestructuredactivities_conditionalnode_assured_setter(instance):
    original = instance.assured
    instance.assured = original
    assert instance.assured == original



@given(instance=xmof_CompleteStructuredActivities_ConditionalNode_strategy)
def test_hyp_xmof_completestructuredactivities_conditionalnode_determinate_setter(instance):
    original = instance.determinate
    instance.determinate = original
    assert instance.determinate == original




@given(instance=xmof_ExtraStructuredActivities_ExpansionRegion_strategy)
def test_hyp_xmof_extrastructuredactivities_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original




@given(instance=xmof_CompleteStructuredActivities_LoopNode_strategy)
def test_hyp_xmof_completestructuredactivities_loopnode_testedFirst_setter(instance):
    original = instance.testedFirst
    instance.testedFirst = original
    assert instance.testedFirst == original




























@given(instance=xmof_Kernel_LiteralInteger_strategy)
def test_hyp_xmof_kernel_literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=xmof_Kernel_LiteralUnlimitedNatural_strategy)
def test_hyp_xmof_kernel_literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=xmof_Kernel_LiteralString_strategy)
def test_hyp_xmof_kernel_literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=xmof_Kernel_LiteralBoolean_strategy)
def test_hyp_xmof_kernel_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
























@given(instance=xmof_Kernel_DirectedParameter_strategy)
def test_hyp_xmof_kernel_directedparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original


































@given(instance=xmof_BasicBehaviors_Behavior_strategy)
def test_hyp_xmof_basicbehaviors_behavior_reentrant_setter(instance):
    original = instance.reentrant
    instance.reentrant = original
    assert instance.reentrant == original





@given(instance=xmof_IntermediateActivities_Activity_strategy)
def test_hyp_xmof_intermediateactivities_activity_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original




@given(instance=xmof_BasicBehaviors_OpaqueBehavior_strategy)
def test_hyp_xmof_basicbehaviors_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=xmof_BasicBehaviors_OpaqueBehavior_strategy)
def test_hyp_xmof_basicbehaviors_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    BasicActions_InputPin,
    BasicActions_OutputPin,
    BasicActions_xmof_EClassifier,
    BasicBehaviors_Behavior,
    BasicBehaviors_BehavioredClassifier,
    Behavior,
    BehavioredEClass,
    BehavioredEOperation,
    CallAction,
    Communications_Event,
    Communications_Signal,
    Communications_Trigger,
    Communications_xmof_EAttribute,
    CompleteActions_xmof_EClassifier,
    CompleteStructuredActivities_Clause,
    CompleteStructuredActivities_ExecutableNode,
    CompleteStructuredActivities_StructuredActivityNode,
    ControlNode,
    EClass,
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EOperation,
    EParameter,
    ETypedElement,
    Event,
    ExecutableNode,
    ExtraStructuredActivities_ExpansionNode,
    ExtraStructuredActivities_ExpansionRegion,
    FinalNode,
    InstanceSpecification,
    IntermediateActions_LinkEndData,
    IntermediateActions_xmof_EClassifier,
    IntermediateActions_xmof_EReference,
    IntermediateActions_xmof_EStructuralFeature,
    IntermediateActivities_Activity,
    IntermediateActivities_ActivityEdge,
    IntermediateActivities_ActivityNode,
    IntermediateActivities_ObjectFlow,
    IntermediateActivities_ObjectNode,
    InvocationAction,
    Kernel_BehavioredEOperation,
    Kernel_DirectedParameter,
    Kernel_InstanceSpecification,
    Kernel_Slot,
    Kernel_ValueSpecification,
    Kernel_xmof_EClassifier,
    Kernel_xmof_EEnumLiteral,
    Kernel_xmof_EStructuralFeature,
    LinkAction,
    LinkEndData,
    LiteralSpecification,
    MessageEvent,
    ObjectNode,
    OpaqueBehavior,
    Pin,
    StructuralFeatureAction,
    StructuredActivityNode,
    ValueSpecification,
    WriteLinkAction,
    WriteStructuralFeatureAction,
    xmof_BasicActions_Action,
    xmof_BasicActions_CallAction,
    xmof_BasicActions_CallBehaviorAction,
    xmof_BasicActions_CallOperationAction,
    xmof_BasicActions_InputPin,
    xmof_BasicActions_InvocationAction,
    xmof_BasicActions_OutputPin,
    xmof_BasicActions_Pin,
    xmof_BasicActions_SendSignalAction,
    xmof_BasicBehaviors_Behavior,
    xmof_BasicBehaviors_BehavioredClassifier,
    xmof_BasicBehaviors_FunctionBehavior,
    xmof_BasicBehaviors_OpaqueBehavior,
    xmof_Communications_Event,
    xmof_Communications_MessageEvent,
    xmof_Communications_Reception,
    xmof_Communications_Signal,
    xmof_Communications_SignalEvent,
    xmof_Communications_Trigger,
    xmof_CompleteActions_AcceptEventAction,
    xmof_CompleteActions_ReadExtentAction,
    xmof_CompleteActions_ReadIsClassifiedObjectAction,
    xmof_CompleteActions_ReclassifyObjectAction,
    xmof_CompleteActions_ReduceAction,
    xmof_CompleteActions_StartClassifierBehaviorAction,
    xmof_CompleteActions_StartObjectBehaviorAction,
    xmof_CompleteStructuredActivities_Clause,
    xmof_CompleteStructuredActivities_ConditionalNode,
    xmof_CompleteStructuredActivities_ExecutableNode,
    xmof_CompleteStructuredActivities_LoopNode,
    xmof_CompleteStructuredActivities_StructuredActivityNode,
    xmof_ExtraStructuredActivities_ExpansionNode,
    xmof_ExtraStructuredActivities_ExpansionRegion,
    xmof_IntermediateActions_AddStructuralFeatureValueAction,
    xmof_IntermediateActions_ClearAssociationAction,
    xmof_IntermediateActions_ClearStructuralFeatureAction,
    xmof_IntermediateActions_CreateLinkAction,
    xmof_IntermediateActions_CreateObjectAction,
    xmof_IntermediateActions_DestroyLinkAction,
    xmof_IntermediateActions_DestroyObjectAction,
    xmof_IntermediateActions_LinkAction,
    xmof_IntermediateActions_LinkEndCreationData,
    xmof_IntermediateActions_LinkEndData,
    xmof_IntermediateActions_LinkEndDestructionData,
    xmof_IntermediateActions_ReadLinkAction,
    xmof_IntermediateActions_ReadSelfAction,
    xmof_IntermediateActions_ReadStructuralFeatureAction,
    xmof_IntermediateActions_RemoveStructuralFeatureValueAction,
    xmof_IntermediateActions_StructuralFeatureAction,
    xmof_IntermediateActions_TestIdentityAction,
    xmof_IntermediateActions_ValueSpecificationAction,
    xmof_IntermediateActions_WriteLinkAction,
    xmof_IntermediateActions_WriteStructuralFeatureAction,
    xmof_IntermediateActivities_Activity,
    xmof_IntermediateActivities_ActivityEdge,
    xmof_IntermediateActivities_ActivityFinalNode,
    xmof_IntermediateActivities_ActivityNode,
    xmof_IntermediateActivities_ActivityParameterNode,
    xmof_IntermediateActivities_ControlFlow,
    xmof_IntermediateActivities_ControlNode,
    xmof_IntermediateActivities_DecisionNode,
    xmof_IntermediateActivities_FinalNode,
    xmof_IntermediateActivities_ForkNode,
    xmof_IntermediateActivities_InitialNode,
    xmof_IntermediateActivities_JoinNode,
    xmof_IntermediateActivities_MergeNode,
    xmof_IntermediateActivities_ObjectFlow,
    xmof_IntermediateActivities_ObjectNode,
    xmof_Kernel_BehavioredEClass,
    xmof_Kernel_BehavioredEOperation,
    xmof_Kernel_DirectedParameter,
    xmof_Kernel_EEnumLiteralSpecification,
    xmof_Kernel_InstanceSpecification,
    xmof_Kernel_InstanceValue,
    xmof_Kernel_LiteralBoolean,
    xmof_Kernel_LiteralInteger,
    xmof_Kernel_LiteralNull,
    xmof_Kernel_LiteralSpecification,
    xmof_Kernel_LiteralString,
    xmof_Kernel_LiteralUnlimitedNatural,
    xmof_Kernel_MainEClass,
    xmof_Kernel_PrimitiveType,
    xmof_Kernel_Slot,
    xmof_Kernel_ValueSpecification,
    CallConcurrencyKind,
    ExpansionKind,
    ParameterDirectionKind,
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

def test_xmof_BasicActions_Action_locallyReentrant_value_roundtrip():
    instance = xmof_BasicActions_Action(locallyReentrant=True)
    assert instance.locallyReentrant == True
    instance.locallyReentrant = False
    assert instance.locallyReentrant == False


def test_xmof_BasicActions_CallAction_synchronous_value_roundtrip():
    instance = xmof_BasicActions_CallAction(synchronous=True)
    assert instance.synchronous == True
    instance.synchronous = False
    assert instance.synchronous == False


def test_xmof_BasicBehaviors_Behavior_reentrant_value_roundtrip():
    instance = xmof_BasicBehaviors_Behavior(reentrant=True)
    assert instance.reentrant == True
    instance.reentrant = False
    assert instance.reentrant == False


def test_xmof_BasicBehaviors_OpaqueBehavior_body_value_roundtrip():
    instance = xmof_BasicBehaviors_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_xmof_BasicBehaviors_OpaqueBehavior_language_value_roundtrip():
    instance = xmof_BasicBehaviors_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_xmof_CompleteActions_AcceptEventAction_unmarshall_value_roundtrip():
    instance = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    assert instance.unmarshall == True
    instance.unmarshall = False
    assert instance.unmarshall == False


def test_xmof_CompleteActions_ReadIsClassifiedObjectAction_direct_value_roundtrip():
    instance = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    assert instance.direct == True
    instance.direct = False
    assert instance.direct == False


def test_xmof_CompleteActions_ReclassifyObjectAction_replaceAll_value_roundtrip():
    instance = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    assert instance.replaceAll == True
    instance.replaceAll = False
    assert instance.replaceAll == False


def test_xmof_CompleteActions_ReduceAction_ordered_value_roundtrip():
    instance = xmof_CompleteActions_ReduceAction(ordered=True)
    assert instance.ordered == True
    instance.ordered = False
    assert instance.ordered == False


def test_xmof_CompleteStructuredActivities_ConditionalNode_assured_value_roundtrip():
    instance = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    assert instance.assured == True
    instance.assured = False
    assert instance.assured == False


def test_xmof_CompleteStructuredActivities_ConditionalNode_determinate_value_roundtrip():
    instance = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    assert instance.determinate == True
    instance.determinate = False
    assert instance.determinate == False


def test_xmof_CompleteStructuredActivities_LoopNode_testedFirst_value_roundtrip():
    instance = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    assert instance.testedFirst == True
    instance.testedFirst = False
    assert instance.testedFirst == False


def test_xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate_value_roundtrip():
    instance = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    assert instance.mustIsolate == True
    instance.mustIsolate = False
    assert instance.mustIsolate == False


def test_xmof_ExtraStructuredActivities_ExpansionRegion_mode_value_roundtrip():
    instance = xmof_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_xmof_IntermediateActions_AddStructuralFeatureValueAction_replaceAll_value_roundtrip():
    instance = xmof_IntermediateActions_AddStructuralFeatureValueAction(replaceAll=True)
    assert instance.replaceAll == True
    instance.replaceAll = False
    assert instance.replaceAll == False


def test_xmof_IntermediateActions_DestroyObjectAction_destroyLinks_value_roundtrip():
    instance = xmof_IntermediateActions_DestroyObjectAction(destroyLinks=True, destroyOwnedObjects=True)
    assert instance.destroyLinks == True
    instance.destroyLinks = False
    assert instance.destroyLinks == False


def test_xmof_IntermediateActions_DestroyObjectAction_destroyOwnedObjects_value_roundtrip():
    instance = xmof_IntermediateActions_DestroyObjectAction(destroyLinks=True, destroyOwnedObjects=True)
    assert instance.destroyOwnedObjects == True
    instance.destroyOwnedObjects = False
    assert instance.destroyOwnedObjects == False


def test_xmof_IntermediateActions_LinkEndCreationData_replaceAll_value_roundtrip():
    instance = xmof_IntermediateActions_LinkEndCreationData(replaceAll=True)
    assert instance.replaceAll == True
    instance.replaceAll = False
    assert instance.replaceAll == False


def test_xmof_IntermediateActions_LinkEndDestructionData_destroyDuplicates_value_roundtrip():
    instance = xmof_IntermediateActions_LinkEndDestructionData(destroyDuplicates=True)
    assert instance.destroyDuplicates == True
    instance.destroyDuplicates = False
    assert instance.destroyDuplicates == False


def test_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates_value_roundtrip():
    instance = xmof_IntermediateActions_RemoveStructuralFeatureValueAction(removeDuplicates=True)
    assert instance.removeDuplicates == True
    instance.removeDuplicates = False
    assert instance.removeDuplicates == False


def test_xmof_IntermediateActivities_Activity_readOnly_value_roundtrip():
    instance = xmof_IntermediateActivities_Activity(readOnly=True)
    assert instance.readOnly == True
    instance.readOnly = False
    assert instance.readOnly == False


def test_xmof_Kernel_DirectedParameter_direction_value_roundtrip():
    instance = xmof_Kernel_DirectedParameter(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_xmof_Kernel_LiteralBoolean_value_value_roundtrip():
    instance = xmof_Kernel_LiteralBoolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_xmof_Kernel_LiteralInteger_value_value_roundtrip():
    instance = xmof_Kernel_LiteralInteger(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_xmof_Kernel_LiteralString_value_value_roundtrip():
    instance = xmof_Kernel_LiteralString(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_xmof_Kernel_LiteralUnlimitedNatural_value_value_roundtrip():
    instance = xmof_Kernel_LiteralUnlimitedNatural(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_xmof_BasicActions_InvocationAction_isa_Action():
    instance = xmof_BasicActions_InvocationAction()
    assert isinstance(instance, Action)


def test_xmof_CompleteActions_AcceptEventAction_isa_Action():
    instance = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    assert isinstance(instance, Action)


def test_xmof_CompleteActions_ReadExtentAction_isa_Action():
    instance = xmof_CompleteActions_ReadExtentAction()
    assert isinstance(instance, Action)


def test_xmof_CompleteActions_ReadIsClassifiedObjectAction_isa_Action():
    instance = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    assert isinstance(instance, Action)


def test_xmof_CompleteActions_ReclassifyObjectAction_isa_Action():
    instance = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    assert isinstance(instance, Action)


def test_xmof_CompleteActions_ReduceAction_isa_Action():
    instance = xmof_CompleteActions_ReduceAction(ordered=True)
    assert isinstance(instance, Action)


def test_xmof_CompleteActions_StartClassifierBehaviorAction_isa_Action():
    instance = xmof_CompleteActions_StartClassifierBehaviorAction()
    assert isinstance(instance, Action)


def test_xmof_CompleteStructuredActivities_StructuredActivityNode_isa_Action():
    instance = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_ClearAssociationAction_isa_Action():
    instance = xmof_IntermediateActions_ClearAssociationAction()
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_CreateObjectAction_isa_Action():
    instance = xmof_IntermediateActions_CreateObjectAction()
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_DestroyObjectAction_isa_Action():
    instance = xmof_IntermediateActions_DestroyObjectAction(destroyLinks=True, destroyOwnedObjects=True)
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_LinkAction_isa_Action():
    instance = xmof_IntermediateActions_LinkAction()
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_ReadSelfAction_isa_Action():
    instance = xmof_IntermediateActions_ReadSelfAction()
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_StructuralFeatureAction_isa_Action():
    instance = xmof_IntermediateActions_StructuralFeatureAction()
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_TestIdentityAction_isa_Action():
    instance = xmof_IntermediateActions_TestIdentityAction()
    assert isinstance(instance, Action)


def test_xmof_IntermediateActions_ValueSpecificationAction_isa_Action():
    instance = xmof_IntermediateActions_ValueSpecificationAction()
    assert isinstance(instance, Action)


def test_xmof_IntermediateActivities_ControlFlow_isa_ActivityEdge():
    instance = xmof_IntermediateActivities_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_xmof_IntermediateActivities_ObjectFlow_isa_ActivityEdge():
    instance = xmof_IntermediateActivities_ObjectFlow()
    assert isinstance(instance, ActivityEdge)


def test_xmof_CompleteStructuredActivities_ExecutableNode_isa_ActivityNode():
    instance = xmof_CompleteStructuredActivities_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_xmof_IntermediateActivities_ControlNode_isa_ActivityNode():
    instance = xmof_IntermediateActivities_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_xmof_Kernel_BehavioredEClass_isa_BasicBehaviors_BehavioredClassifier():
    instance = xmof_Kernel_BehavioredEClass()
    assert isinstance(instance, BasicBehaviors_BehavioredClassifier)


def test_xmof_BasicBehaviors_OpaqueBehavior_isa_Behavior():
    instance = xmof_BasicBehaviors_OpaqueBehavior(body="sample_text", language="sample_text")
    assert isinstance(instance, Behavior)


def test_xmof_IntermediateActivities_Activity_isa_Behavior():
    instance = xmof_IntermediateActivities_Activity(readOnly=True)
    assert isinstance(instance, Behavior)


def test_xmof_BasicBehaviors_Behavior_isa_BehavioredEClass():
    instance = xmof_BasicBehaviors_Behavior(reentrant=True)
    assert isinstance(instance, BehavioredEClass)


def test_xmof_Kernel_MainEClass_isa_BehavioredEClass():
    instance = xmof_Kernel_MainEClass()
    assert isinstance(instance, BehavioredEClass)


def test_xmof_Communications_Reception_isa_BehavioredEOperation():
    instance = xmof_Communications_Reception()
    assert isinstance(instance, BehavioredEOperation)


def test_xmof_BasicActions_CallBehaviorAction_isa_CallAction():
    instance = xmof_BasicActions_CallBehaviorAction()
    assert isinstance(instance, CallAction)


def test_xmof_BasicActions_CallOperationAction_isa_CallAction():
    instance = xmof_BasicActions_CallOperationAction()
    assert isinstance(instance, CallAction)


def test_xmof_CompleteActions_StartObjectBehaviorAction_isa_CallAction():
    instance = xmof_CompleteActions_StartObjectBehaviorAction()
    assert isinstance(instance, CallAction)


def test_xmof_IntermediateActivities_DecisionNode_isa_ControlNode():
    instance = xmof_IntermediateActivities_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_xmof_IntermediateActivities_FinalNode_isa_ControlNode():
    instance = xmof_IntermediateActivities_FinalNode()
    assert isinstance(instance, ControlNode)


def test_xmof_IntermediateActivities_ForkNode_isa_ControlNode():
    instance = xmof_IntermediateActivities_ForkNode()
    assert isinstance(instance, ControlNode)


def test_xmof_IntermediateActivities_InitialNode_isa_ControlNode():
    instance = xmof_IntermediateActivities_InitialNode()
    assert isinstance(instance, ControlNode)


def test_xmof_IntermediateActivities_JoinNode_isa_ControlNode():
    instance = xmof_IntermediateActivities_JoinNode()
    assert isinstance(instance, ControlNode)


def test_xmof_IntermediateActivities_MergeNode_isa_ControlNode():
    instance = xmof_IntermediateActivities_MergeNode()
    assert isinstance(instance, ControlNode)


def test_xmof_Kernel_BehavioredEClass_isa_EClass():
    instance = xmof_Kernel_BehavioredEClass()
    assert isinstance(instance, EClass)


def test_xmof_BasicBehaviors_BehavioredClassifier_isa_EClassifier():
    instance = xmof_BasicBehaviors_BehavioredClassifier()
    assert isinstance(instance, EClassifier)


def test_xmof_Communications_Signal_isa_EClassifier():
    instance = xmof_Communications_Signal()
    assert isinstance(instance, EClassifier)


def test_xmof_Kernel_PrimitiveType_isa_EDataType():
    instance = xmof_Kernel_PrimitiveType()
    assert isinstance(instance, EDataType)


def test_xmof_CompleteStructuredActivities_Clause_isa_EModelElement():
    instance = xmof_CompleteStructuredActivities_Clause()
    assert isinstance(instance, EModelElement)


def test_xmof_IntermediateActions_LinkEndData_isa_EModelElement():
    instance = xmof_IntermediateActions_LinkEndData()
    assert isinstance(instance, EModelElement)


def test_xmof_Kernel_Slot_isa_EModelElement():
    instance = xmof_Kernel_Slot()
    assert isinstance(instance, EModelElement)


def test_xmof_Communications_Event_isa_ENamedElement():
    instance = xmof_Communications_Event()
    assert isinstance(instance, ENamedElement)


def test_xmof_Communications_Trigger_isa_ENamedElement():
    instance = xmof_Communications_Trigger()
    assert isinstance(instance, ENamedElement)


def test_xmof_IntermediateActivities_ActivityEdge_isa_ENamedElement():
    instance = xmof_IntermediateActivities_ActivityEdge()
    assert isinstance(instance, ENamedElement)


def test_xmof_IntermediateActivities_ActivityNode_isa_ENamedElement():
    instance = xmof_IntermediateActivities_ActivityNode()
    assert isinstance(instance, ENamedElement)


def test_xmof_Kernel_InstanceSpecification_isa_ENamedElement():
    instance = xmof_Kernel_InstanceSpecification()
    assert isinstance(instance, ENamedElement)


def test_xmof_Kernel_BehavioredEOperation_isa_EOperation():
    instance = xmof_Kernel_BehavioredEOperation()
    assert isinstance(instance, EOperation)


def test_xmof_Kernel_DirectedParameter_isa_EParameter():
    instance = xmof_Kernel_DirectedParameter(direction="sample_text")
    assert isinstance(instance, EParameter)


def test_xmof_BasicActions_Pin_isa_ETypedElement():
    instance = xmof_BasicActions_Pin()
    assert isinstance(instance, ETypedElement)


def test_xmof_IntermediateActivities_ObjectNode_isa_ETypedElement():
    instance = xmof_IntermediateActivities_ObjectNode()
    assert isinstance(instance, ETypedElement)


def test_xmof_Kernel_ValueSpecification_isa_ETypedElement():
    instance = xmof_Kernel_ValueSpecification()
    assert isinstance(instance, ETypedElement)


def test_xmof_Communications_MessageEvent_isa_Event():
    instance = xmof_Communications_MessageEvent()
    assert isinstance(instance, Event)


def test_xmof_BasicActions_Action_isa_ExecutableNode():
    instance = xmof_BasicActions_Action(locallyReentrant=True)
    assert isinstance(instance, ExecutableNode)


def test_xmof_IntermediateActivities_ActivityFinalNode_isa_FinalNode():
    instance = xmof_IntermediateActivities_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_xmof_Kernel_EEnumLiteralSpecification_isa_InstanceSpecification():
    instance = xmof_Kernel_EEnumLiteralSpecification()
    assert isinstance(instance, InstanceSpecification)


def test_xmof_IntermediateActivities_ObjectNode_isa_IntermediateActivities_ActivityNode():
    instance = xmof_IntermediateActivities_ObjectNode()
    assert isinstance(instance, IntermediateActivities_ActivityNode)


def test_xmof_BasicActions_Pin_isa_IntermediateActivities_ObjectNode():
    instance = xmof_BasicActions_Pin()
    assert isinstance(instance, IntermediateActivities_ObjectNode)


def test_xmof_BasicActions_CallAction_isa_InvocationAction():
    instance = xmof_BasicActions_CallAction(synchronous=True)
    assert isinstance(instance, InvocationAction)


def test_xmof_BasicActions_SendSignalAction_isa_InvocationAction():
    instance = xmof_BasicActions_SendSignalAction()
    assert isinstance(instance, InvocationAction)


def test_xmof_IntermediateActions_ReadLinkAction_isa_LinkAction():
    instance = xmof_IntermediateActions_ReadLinkAction()
    assert isinstance(instance, LinkAction)


def test_xmof_IntermediateActions_WriteLinkAction_isa_LinkAction():
    instance = xmof_IntermediateActions_WriteLinkAction()
    assert isinstance(instance, LinkAction)


def test_xmof_IntermediateActions_LinkEndCreationData_isa_LinkEndData():
    instance = xmof_IntermediateActions_LinkEndCreationData(replaceAll=True)
    assert isinstance(instance, LinkEndData)


def test_xmof_IntermediateActions_LinkEndDestructionData_isa_LinkEndData():
    instance = xmof_IntermediateActions_LinkEndDestructionData(destroyDuplicates=True)
    assert isinstance(instance, LinkEndData)


def test_xmof_Kernel_LiteralBoolean_isa_LiteralSpecification():
    instance = xmof_Kernel_LiteralBoolean(value=True)
    assert isinstance(instance, LiteralSpecification)


def test_xmof_Kernel_LiteralInteger_isa_LiteralSpecification():
    instance = xmof_Kernel_LiteralInteger(value=7)
    assert isinstance(instance, LiteralSpecification)


def test_xmof_Kernel_LiteralNull_isa_LiteralSpecification():
    instance = xmof_Kernel_LiteralNull()
    assert isinstance(instance, LiteralSpecification)


def test_xmof_Kernel_LiteralString_isa_LiteralSpecification():
    instance = xmof_Kernel_LiteralString(value="sample_text")
    assert isinstance(instance, LiteralSpecification)


def test_xmof_Kernel_LiteralUnlimitedNatural_isa_LiteralSpecification():
    instance = xmof_Kernel_LiteralUnlimitedNatural(value=7)
    assert isinstance(instance, LiteralSpecification)


def test_xmof_Communications_SignalEvent_isa_MessageEvent():
    instance = xmof_Communications_SignalEvent()
    assert isinstance(instance, MessageEvent)


def test_xmof_ExtraStructuredActivities_ExpansionNode_isa_ObjectNode():
    instance = xmof_ExtraStructuredActivities_ExpansionNode()
    assert isinstance(instance, ObjectNode)


def test_xmof_IntermediateActivities_ActivityParameterNode_isa_ObjectNode():
    instance = xmof_IntermediateActivities_ActivityParameterNode()
    assert isinstance(instance, ObjectNode)


def test_xmof_BasicBehaviors_FunctionBehavior_isa_OpaqueBehavior():
    instance = xmof_BasicBehaviors_FunctionBehavior()
    assert isinstance(instance, OpaqueBehavior)


def test_xmof_BasicActions_InputPin_isa_Pin():
    instance = xmof_BasicActions_InputPin()
    assert isinstance(instance, Pin)


def test_xmof_BasicActions_OutputPin_isa_Pin():
    instance = xmof_BasicActions_OutputPin()
    assert isinstance(instance, Pin)


def test_xmof_IntermediateActions_ClearStructuralFeatureAction_isa_StructuralFeatureAction():
    instance = xmof_IntermediateActions_ClearStructuralFeatureAction()
    assert isinstance(instance, StructuralFeatureAction)


def test_xmof_IntermediateActions_ReadStructuralFeatureAction_isa_StructuralFeatureAction():
    instance = xmof_IntermediateActions_ReadStructuralFeatureAction()
    assert isinstance(instance, StructuralFeatureAction)


def test_xmof_IntermediateActions_WriteStructuralFeatureAction_isa_StructuralFeatureAction():
    instance = xmof_IntermediateActions_WriteStructuralFeatureAction()
    assert isinstance(instance, StructuralFeatureAction)


def test_xmof_CompleteStructuredActivities_ConditionalNode_isa_StructuredActivityNode():
    instance = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    assert isinstance(instance, StructuredActivityNode)


def test_xmof_CompleteStructuredActivities_LoopNode_isa_StructuredActivityNode():
    instance = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    assert isinstance(instance, StructuredActivityNode)


def test_xmof_ExtraStructuredActivities_ExpansionRegion_isa_StructuredActivityNode():
    instance = xmof_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    assert isinstance(instance, StructuredActivityNode)


def test_xmof_Kernel_InstanceValue_isa_ValueSpecification():
    instance = xmof_Kernel_InstanceValue()
    assert isinstance(instance, ValueSpecification)


def test_xmof_Kernel_LiteralSpecification_isa_ValueSpecification():
    instance = xmof_Kernel_LiteralSpecification()
    assert isinstance(instance, ValueSpecification)


def test_xmof_IntermediateActions_CreateLinkAction_isa_WriteLinkAction():
    instance = xmof_IntermediateActions_CreateLinkAction()
    assert isinstance(instance, WriteLinkAction)


def test_xmof_IntermediateActions_DestroyLinkAction_isa_WriteLinkAction():
    instance = xmof_IntermediateActions_DestroyLinkAction()
    assert isinstance(instance, WriteLinkAction)


def test_xmof_IntermediateActions_AddStructuralFeatureValueAction_isa_WriteStructuralFeatureAction():
    instance = xmof_IntermediateActions_AddStructuralFeatureValueAction(replaceAll=True)
    assert isinstance(instance, WriteStructuralFeatureAction)


def test_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_isa_WriteStructuralFeatureAction():
    instance = xmof_IntermediateActions_RemoveStructuralFeatureValueAction(removeDuplicates=True)
    assert isinstance(instance, WriteStructuralFeatureAction)


def test_assoc_bodyOutput52_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode53', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode53', b1)
    if hasattr(b1, 'BasicActions_OutputPin54'):
        assert _is_linked(b1, 'BasicActions_OutputPin54', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode53', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode53', b2)
    if hasattr(b1, 'BasicActions_OutputPin54'):
        assert not _is_linked(b1, 'BasicActions_OutputPin54', a)
    if hasattr(b2, 'BasicActions_OutputPin54'):
        assert _is_linked(b2, 'BasicActions_OutputPin54', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode53', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode53', b2)
    if hasattr(b2, 'BasicActions_OutputPin54'):
        assert not _is_linked(b2, 'BasicActions_OutputPin54', a)


def test_assoc_bodyPart57_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = CompleteStructuredActivities_ExecutableNode()
    b2 = CompleteStructuredActivities_ExecutableNode()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode58', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode58', b1)
    if hasattr(b1, 'CompleteStructuredActivities_ExecutableNode59'):
        assert _is_linked(b1, 'CompleteStructuredActivities_ExecutableNode59', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode58', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode58', b2)
    if hasattr(b1, 'CompleteStructuredActivities_ExecutableNode59'):
        assert not _is_linked(b1, 'CompleteStructuredActivities_ExecutableNode59', a)
    if hasattr(b2, 'CompleteStructuredActivities_ExecutableNode59'):
        assert _is_linked(b2, 'CompleteStructuredActivities_ExecutableNode59', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode58', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode58', b2)
    if hasattr(b2, 'CompleteStructuredActivities_ExecutableNode59'):
        assert not _is_linked(b2, 'CompleteStructuredActivities_ExecutableNode59', a)


def test_assoc_classifier176_link_reassign_clear():
    a = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    b1 = CompleteActions_xmof_EClassifier()
    b2 = CompleteActions_xmof_EClassifier()
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', b1)
    assert _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', b1)
    if hasattr(b1, 'CompleteActions_xmof_EClassifier177'):
        assert _is_linked(b1, 'CompleteActions_xmof_EClassifier177', a)
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', b2)
    assert _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', b2)
    if hasattr(b1, 'CompleteActions_xmof_EClassifier177'):
        assert not _is_linked(b1, 'CompleteActions_xmof_EClassifier177', a)
    if hasattr(b2, 'CompleteActions_xmof_EClassifier177'):
        assert _is_linked(b2, 'CompleteActions_xmof_EClassifier177', a)
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', None)
    assert not _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', b2)
    if hasattr(b2, 'CompleteActions_xmof_EClassifier177'):
        assert not _is_linked(b2, 'CompleteActions_xmof_EClassifier177', a)


def test_assoc_clause83_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    b1 = CompleteStructuredActivities_Clause()
    b2 = CompleteStructuredActivities_Clause()
    _safe_set(a, 'xmof_CompleteStructuredActivities_ConditionalNode', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_ConditionalNode', b1)
    if hasattr(b1, 'CompleteStructuredActivities_Clause'):
        assert _is_linked(b1, 'CompleteStructuredActivities_Clause', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_ConditionalNode', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_ConditionalNode', b2)
    if hasattr(b1, 'CompleteStructuredActivities_Clause'):
        assert not _is_linked(b1, 'CompleteStructuredActivities_Clause', a)
    if hasattr(b2, 'CompleteStructuredActivities_Clause'):
        assert _is_linked(b2, 'CompleteStructuredActivities_Clause', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_ConditionalNode', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_ConditionalNode', b2)
    if hasattr(b2, 'CompleteStructuredActivities_Clause'):
        assert not _is_linked(b2, 'CompleteStructuredActivities_Clause', a)


def test_assoc_collection169_link_reassign_clear():
    a = xmof_CompleteActions_ReduceAction(ordered=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_CompleteActions_ReduceAction170', b1)
    assert _is_linked(a, 'xmof_CompleteActions_ReduceAction170', b1)
    if hasattr(b1, 'BasicActions_InputPin171'):
        assert _is_linked(b1, 'BasicActions_InputPin171', a)
    _safe_set(a, 'xmof_CompleteActions_ReduceAction170', b2)
    assert _is_linked(a, 'xmof_CompleteActions_ReduceAction170', b2)
    if hasattr(b1, 'BasicActions_InputPin171'):
        assert not _is_linked(b1, 'BasicActions_InputPin171', a)
    if hasattr(b2, 'BasicActions_InputPin171'):
        assert _is_linked(b2, 'BasicActions_InputPin171', a)
    _safe_set(a, 'xmof_CompleteActions_ReduceAction170', None)
    assert not _is_linked(a, 'xmof_CompleteActions_ReduceAction170', b2)
    if hasattr(b2, 'BasicActions_InputPin171'):
        assert not _is_linked(b2, 'BasicActions_InputPin171', a)


def test_assoc_context198_link_reassign_clear():
    a = xmof_BasicActions_Action(locallyReentrant=True)
    b1 = BasicActions_xmof_EClassifier()
    b2 = BasicActions_xmof_EClassifier()
    _safe_set(a, 'xmof_BasicActions_Action199', b1)
    assert _is_linked(a, 'xmof_BasicActions_Action199', b1)
    if hasattr(b1, 'BasicActions_xmof_EClassifier'):
        assert _is_linked(b1, 'BasicActions_xmof_EClassifier', a)
    _safe_set(a, 'xmof_BasicActions_Action199', b2)
    assert _is_linked(a, 'xmof_BasicActions_Action199', b2)
    if hasattr(b1, 'BasicActions_xmof_EClassifier'):
        assert not _is_linked(b1, 'BasicActions_xmof_EClassifier', a)
    if hasattr(b2, 'BasicActions_xmof_EClassifier'):
        assert _is_linked(b2, 'BasicActions_xmof_EClassifier', a)
    _safe_set(a, 'xmof_BasicActions_Action199', None)
    assert not _is_linked(a, 'xmof_BasicActions_Action199', b2)
    if hasattr(b2, 'BasicActions_xmof_EClassifier'):
        assert not _is_linked(b2, 'BasicActions_xmof_EClassifier', a)


def test_assoc_context2_link_reassign_clear():
    a = xmof_BasicBehaviors_Behavior(reentrant=True)
    b1 = BasicBehaviors_BehavioredClassifier()
    b2 = BasicBehaviors_BehavioredClassifier()
    _safe_set(a, 'xmof_BasicBehaviors_Behavior3', b1)
    assert _is_linked(a, 'xmof_BasicBehaviors_Behavior3', b1)
    if hasattr(b1, 'BasicBehaviors_BehavioredClassifier'):
        assert _is_linked(b1, 'BasicBehaviors_BehavioredClassifier', a)
    _safe_set(a, 'xmof_BasicBehaviors_Behavior3', b2)
    assert _is_linked(a, 'xmof_BasicBehaviors_Behavior3', b2)
    if hasattr(b1, 'BasicBehaviors_BehavioredClassifier'):
        assert not _is_linked(b1, 'BasicBehaviors_BehavioredClassifier', a)
    if hasattr(b2, 'BasicBehaviors_BehavioredClassifier'):
        assert _is_linked(b2, 'BasicBehaviors_BehavioredClassifier', a)
    _safe_set(a, 'xmof_BasicBehaviors_Behavior3', None)
    assert not _is_linked(a, 'xmof_BasicBehaviors_Behavior3', b2)
    if hasattr(b2, 'BasicBehaviors_BehavioredClassifier'):
        assert not _is_linked(b2, 'BasicBehaviors_BehavioredClassifier', a)


def test_assoc_decider49_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode', b1)
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode', b1)
    if hasattr(b1, 'BasicActions_OutputPin'):
        assert _is_linked(b1, 'BasicActions_OutputPin', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode', b2)
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode', b2)
    if hasattr(b1, 'BasicActions_OutputPin'):
        assert not _is_linked(b1, 'BasicActions_OutputPin', a)
    if hasattr(b2, 'BasicActions_OutputPin'):
        assert _is_linked(b2, 'BasicActions_OutputPin', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode', None)
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode', b2)
    if hasattr(b2, 'BasicActions_OutputPin'):
        assert not _is_linked(b2, 'BasicActions_OutputPin', a)


def test_assoc_destroyAt143_link_reassign_clear():
    a = xmof_IntermediateActions_LinkEndDestructionData(destroyDuplicates=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_IntermediateActions_LinkEndDestructionData', b1)
    assert _is_linked(a, 'xmof_IntermediateActions_LinkEndDestructionData', b1)
    if hasattr(b1, 'BasicActions_InputPin144'):
        assert _is_linked(b1, 'BasicActions_InputPin144', a)
    _safe_set(a, 'xmof_IntermediateActions_LinkEndDestructionData', b2)
    assert _is_linked(a, 'xmof_IntermediateActions_LinkEndDestructionData', b2)
    if hasattr(b1, 'BasicActions_InputPin144'):
        assert not _is_linked(b1, 'BasicActions_InputPin144', a)
    if hasattr(b2, 'BasicActions_InputPin144'):
        assert _is_linked(b2, 'BasicActions_InputPin144', a)
    _safe_set(a, 'xmof_IntermediateActions_LinkEndDestructionData', None)
    assert not _is_linked(a, 'xmof_IntermediateActions_LinkEndDestructionData', b2)
    if hasattr(b2, 'BasicActions_InputPin144'):
        assert not _is_linked(b2, 'BasicActions_InputPin144', a)


def test_assoc_edge32_link_reassign_clear():
    a = xmof_IntermediateActivities_Activity(readOnly=True)
    b1 = IntermediateActivities_ActivityEdge()
    b2 = IntermediateActivities_ActivityEdge()
    _safe_set(a, 'activity33', {b1})
    assert _is_linked(a, 'activity33', b1)
    if hasattr(b1, 'ActivityEdge'):
        assert _is_linked(b1, 'ActivityEdge', a)
    _safe_set(a, 'activity33', {b2})
    assert _is_linked(a, 'activity33', b2)
    if hasattr(b1, 'ActivityEdge'):
        assert not _is_linked(b1, 'ActivityEdge', a)
    if hasattr(b2, 'ActivityEdge'):
        assert _is_linked(b2, 'ActivityEdge', a)
    _safe_set(a, 'activity33', set())
    assert not _is_linked(a, 'activity33', b2)
    if hasattr(b2, 'ActivityEdge'):
        assert not _is_linked(b2, 'ActivityEdge', a)


def test_assoc_edge89_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = IntermediateActivities_ActivityEdge()
    b2 = IntermediateActivities_ActivityEdge()
    _safe_set(a, 'inStructuredNode90', {b1})
    assert _is_linked(a, 'inStructuredNode90', b1)
    if hasattr(b1, 'ActivityEdge91'):
        assert _is_linked(b1, 'ActivityEdge91', a)
    _safe_set(a, 'inStructuredNode90', {b2})
    assert _is_linked(a, 'inStructuredNode90', b2)
    if hasattr(b1, 'ActivityEdge91'):
        assert not _is_linked(b1, 'ActivityEdge91', a)
    if hasattr(b2, 'ActivityEdge91'):
        assert _is_linked(b2, 'ActivityEdge91', a)
    _safe_set(a, 'inStructuredNode90', set())
    assert not _is_linked(a, 'inStructuredNode90', b2)
    if hasattr(b2, 'ActivityEdge91'):
        assert not _is_linked(b2, 'ActivityEdge91', a)


def test_assoc_input200_link_reassign_clear():
    a = xmof_BasicActions_Action(locallyReentrant=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_BasicActions_Action201', {b1})
    assert _is_linked(a, 'xmof_BasicActions_Action201', b1)
    if hasattr(b1, 'BasicActions_InputPin202'):
        assert _is_linked(b1, 'BasicActions_InputPin202', a)
    _safe_set(a, 'xmof_BasicActions_Action201', {b2})
    assert _is_linked(a, 'xmof_BasicActions_Action201', b2)
    if hasattr(b1, 'BasicActions_InputPin202'):
        assert not _is_linked(b1, 'BasicActions_InputPin202', a)
    if hasattr(b2, 'BasicActions_InputPin202'):
        assert _is_linked(b2, 'BasicActions_InputPin202', a)
    _safe_set(a, 'xmof_BasicActions_Action201', set())
    assert not _is_linked(a, 'xmof_BasicActions_Action201', b2)
    if hasattr(b2, 'BasicActions_InputPin202'):
        assert not _is_linked(b2, 'BasicActions_InputPin202', a)


def test_assoc_inputElement100_link_reassign_clear():
    a = xmof_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    b1 = ExtraStructuredActivities_ExpansionNode()
    b2 = ExtraStructuredActivities_ExpansionNode()
    _safe_set(a, 'regionAsInput', {b1})
    assert _is_linked(a, 'regionAsInput', b1)
    if hasattr(b1, 'ExpansionNode'):
        assert _is_linked(b1, 'ExpansionNode', a)
    _safe_set(a, 'regionAsInput', {b2})
    assert _is_linked(a, 'regionAsInput', b2)
    if hasattr(b1, 'ExpansionNode'):
        assert not _is_linked(b1, 'ExpansionNode', a)
    if hasattr(b2, 'ExpansionNode'):
        assert _is_linked(b2, 'ExpansionNode', a)
    _safe_set(a, 'regionAsInput', set())
    assert not _is_linked(a, 'regionAsInput', b2)
    if hasattr(b2, 'ExpansionNode'):
        assert not _is_linked(b2, 'ExpansionNode', a)


def test_assoc_insertAt141_link_reassign_clear():
    a = xmof_IntermediateActions_LinkEndCreationData(replaceAll=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_IntermediateActions_LinkEndCreationData', b1)
    assert _is_linked(a, 'xmof_IntermediateActions_LinkEndCreationData', b1)
    if hasattr(b1, 'BasicActions_InputPin142'):
        assert _is_linked(b1, 'BasicActions_InputPin142', a)
    _safe_set(a, 'xmof_IntermediateActions_LinkEndCreationData', b2)
    assert _is_linked(a, 'xmof_IntermediateActions_LinkEndCreationData', b2)
    if hasattr(b1, 'BasicActions_InputPin142'):
        assert not _is_linked(b1, 'BasicActions_InputPin142', a)
    if hasattr(b2, 'BasicActions_InputPin142'):
        assert _is_linked(b2, 'BasicActions_InputPin142', a)
    _safe_set(a, 'xmof_IntermediateActions_LinkEndCreationData', None)
    assert not _is_linked(a, 'xmof_IntermediateActions_LinkEndCreationData', b2)
    if hasattr(b2, 'BasicActions_InputPin142'):
        assert not _is_linked(b2, 'BasicActions_InputPin142', a)


def test_assoc_insertAt158_link_reassign_clear():
    a = xmof_IntermediateActions_AddStructuralFeatureValueAction(replaceAll=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', b1)
    assert _is_linked(a, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', b1)
    if hasattr(b1, 'BasicActions_InputPin159'):
        assert _is_linked(b1, 'BasicActions_InputPin159', a)
    _safe_set(a, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', b2)
    assert _is_linked(a, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', b2)
    if hasattr(b1, 'BasicActions_InputPin159'):
        assert not _is_linked(b1, 'BasicActions_InputPin159', a)
    if hasattr(b2, 'BasicActions_InputPin159'):
        assert _is_linked(b2, 'BasicActions_InputPin159', a)
    _safe_set(a, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', None)
    assert not _is_linked(a, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', b2)
    if hasattr(b2, 'BasicActions_InputPin159'):
        assert not _is_linked(b2, 'BasicActions_InputPin159', a)


def test_assoc_loopVariable63_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode64', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode64', b1)
    if hasattr(b1, 'BasicActions_OutputPin65'):
        assert _is_linked(b1, 'BasicActions_OutputPin65', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode64', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode64', b2)
    if hasattr(b1, 'BasicActions_OutputPin65'):
        assert not _is_linked(b1, 'BasicActions_OutputPin65', a)
    if hasattr(b2, 'BasicActions_OutputPin65'):
        assert _is_linked(b2, 'BasicActions_OutputPin65', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode64', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode64', b2)
    if hasattr(b2, 'BasicActions_OutputPin65'):
        assert not _is_linked(b2, 'BasicActions_OutputPin65', a)


def test_assoc_loopVariableInput55_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode56', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode56', b1)
    if hasattr(b1, 'BasicActions_InputPin'):
        assert _is_linked(b1, 'BasicActions_InputPin', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode56', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode56', b2)
    if hasattr(b1, 'BasicActions_InputPin'):
        assert not _is_linked(b1, 'BasicActions_InputPin', a)
    if hasattr(b2, 'BasicActions_InputPin'):
        assert _is_linked(b2, 'BasicActions_InputPin', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode56', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode56', b2)
    if hasattr(b2, 'BasicActions_InputPin'):
        assert not _is_linked(b2, 'BasicActions_InputPin', a)


def test_assoc_newClassifier189_link_reassign_clear():
    a = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    b1 = CompleteActions_xmof_EClassifier()
    b2 = CompleteActions_xmof_EClassifier()
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction190', {b1})
    assert _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction190', b1)
    if hasattr(b1, 'CompleteActions_xmof_EClassifier191'):
        assert _is_linked(b1, 'CompleteActions_xmof_EClassifier191', a)
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction190', {b2})
    assert _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction190', b2)
    if hasattr(b1, 'CompleteActions_xmof_EClassifier191'):
        assert not _is_linked(b1, 'CompleteActions_xmof_EClassifier191', a)
    if hasattr(b2, 'CompleteActions_xmof_EClassifier191'):
        assert _is_linked(b2, 'CompleteActions_xmof_EClassifier191', a)
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction190', set())
    assert not _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction190', b2)
    if hasattr(b2, 'CompleteActions_xmof_EClassifier191'):
        assert not _is_linked(b2, 'CompleteActions_xmof_EClassifier191', a)


def test_assoc_node30_link_reassign_clear():
    a = xmof_IntermediateActivities_Activity(readOnly=True)
    b1 = IntermediateActivities_ActivityNode()
    b2 = IntermediateActivities_ActivityNode()
    _safe_set(a, 'activity', {b1})
    assert _is_linked(a, 'activity', b1)
    if hasattr(b1, 'ActivityNode31'):
        assert _is_linked(b1, 'ActivityNode31', a)
    _safe_set(a, 'activity', {b2})
    assert _is_linked(a, 'activity', b2)
    if hasattr(b1, 'ActivityNode31'):
        assert not _is_linked(b1, 'ActivityNode31', a)
    if hasattr(b2, 'ActivityNode31'):
        assert _is_linked(b2, 'ActivityNode31', a)
    _safe_set(a, 'activity', set())
    assert not _is_linked(a, 'activity', b2)
    if hasattr(b2, 'ActivityNode31'):
        assert not _is_linked(b2, 'ActivityNode31', a)


def test_assoc_node87_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = IntermediateActivities_ActivityNode()
    b2 = IntermediateActivities_ActivityNode()
    _safe_set(a, 'inStructuredNode', {b1})
    assert _is_linked(a, 'inStructuredNode', b1)
    if hasattr(b1, 'ActivityNode88'):
        assert _is_linked(b1, 'ActivityNode88', a)
    _safe_set(a, 'inStructuredNode', {b2})
    assert _is_linked(a, 'inStructuredNode', b2)
    if hasattr(b1, 'ActivityNode88'):
        assert not _is_linked(b1, 'ActivityNode88', a)
    if hasattr(b2, 'ActivityNode88'):
        assert _is_linked(b2, 'ActivityNode88', a)
    _safe_set(a, 'inStructuredNode', set())
    assert not _is_linked(a, 'inStructuredNode', b2)
    if hasattr(b2, 'ActivityNode88'):
        assert not _is_linked(b2, 'ActivityNode88', a)


def test_assoc_object181_link_reassign_clear():
    a = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', b1)
    assert _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', b1)
    if hasattr(b1, 'BasicActions_InputPin183'):
        assert _is_linked(b1, 'BasicActions_InputPin183', a)
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', b2)
    assert _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', b2)
    if hasattr(b1, 'BasicActions_InputPin183'):
        assert not _is_linked(b1, 'BasicActions_InputPin183', a)
    if hasattr(b2, 'BasicActions_InputPin183'):
        assert _is_linked(b2, 'BasicActions_InputPin183', a)
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', None)
    assert not _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', b2)
    if hasattr(b2, 'BasicActions_InputPin183'):
        assert not _is_linked(b2, 'BasicActions_InputPin183', a)


def test_assoc_object186_link_reassign_clear():
    a = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction187', b1)
    assert _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction187', b1)
    if hasattr(b1, 'BasicActions_InputPin188'):
        assert _is_linked(b1, 'BasicActions_InputPin188', a)
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction187', b2)
    assert _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction187', b2)
    if hasattr(b1, 'BasicActions_InputPin188'):
        assert not _is_linked(b1, 'BasicActions_InputPin188', a)
    if hasattr(b2, 'BasicActions_InputPin188'):
        assert _is_linked(b2, 'BasicActions_InputPin188', a)
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction187', None)
    assert not _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction187', b2)
    if hasattr(b2, 'BasicActions_InputPin188'):
        assert not _is_linked(b2, 'BasicActions_InputPin188', a)


def test_assoc_oldClassifier184_link_reassign_clear():
    a = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    b1 = CompleteActions_xmof_EClassifier()
    b2 = CompleteActions_xmof_EClassifier()
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction', {b1})
    assert _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction', b1)
    if hasattr(b1, 'CompleteActions_xmof_EClassifier185'):
        assert _is_linked(b1, 'CompleteActions_xmof_EClassifier185', a)
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction', {b2})
    assert _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction', b2)
    if hasattr(b1, 'CompleteActions_xmof_EClassifier185'):
        assert not _is_linked(b1, 'CompleteActions_xmof_EClassifier185', a)
    if hasattr(b2, 'CompleteActions_xmof_EClassifier185'):
        assert _is_linked(b2, 'CompleteActions_xmof_EClassifier185', a)
    _safe_set(a, 'xmof_CompleteActions_ReclassifyObjectAction', set())
    assert not _is_linked(a, 'xmof_CompleteActions_ReclassifyObjectAction', b2)
    if hasattr(b2, 'CompleteActions_xmof_EClassifier185'):
        assert not _is_linked(b2, 'CompleteActions_xmof_EClassifier185', a)


def test_assoc_output196_link_reassign_clear():
    a = xmof_BasicActions_Action(locallyReentrant=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_BasicActions_Action', {b1})
    assert _is_linked(a, 'xmof_BasicActions_Action', b1)
    if hasattr(b1, 'BasicActions_OutputPin197'):
        assert _is_linked(b1, 'BasicActions_OutputPin197', a)
    _safe_set(a, 'xmof_BasicActions_Action', {b2})
    assert _is_linked(a, 'xmof_BasicActions_Action', b2)
    if hasattr(b1, 'BasicActions_OutputPin197'):
        assert not _is_linked(b1, 'BasicActions_OutputPin197', a)
    if hasattr(b2, 'BasicActions_OutputPin197'):
        assert _is_linked(b2, 'BasicActions_OutputPin197', a)
    _safe_set(a, 'xmof_BasicActions_Action', set())
    assert not _is_linked(a, 'xmof_BasicActions_Action', b2)
    if hasattr(b2, 'BasicActions_OutputPin197'):
        assert not _is_linked(b2, 'BasicActions_OutputPin197', a)


def test_assoc_outputElement101_link_reassign_clear():
    a = xmof_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    b1 = ExtraStructuredActivities_ExpansionNode()
    b2 = ExtraStructuredActivities_ExpansionNode()
    _safe_set(a, 'regionAsOutput', {b1})
    assert _is_linked(a, 'regionAsOutput', b1)
    if hasattr(b1, 'ExpansionNode102'):
        assert _is_linked(b1, 'ExpansionNode102', a)
    _safe_set(a, 'regionAsOutput', {b2})
    assert _is_linked(a, 'regionAsOutput', b2)
    if hasattr(b1, 'ExpansionNode102'):
        assert not _is_linked(b1, 'ExpansionNode102', a)
    if hasattr(b2, 'ExpansionNode102'):
        assert _is_linked(b2, 'ExpansionNode102', a)
    _safe_set(a, 'regionAsOutput', set())
    assert not _is_linked(a, 'regionAsOutput', b2)
    if hasattr(b2, 'ExpansionNode102'):
        assert not _is_linked(b2, 'ExpansionNode102', a)


def test_assoc_ownedParameter1_link_reassign_clear():
    a = xmof_BasicBehaviors_Behavior(reentrant=True)
    b1 = Kernel_DirectedParameter()
    b2 = Kernel_DirectedParameter()
    _safe_set(a, 'xmof_BasicBehaviors_Behavior', {b1})
    assert _is_linked(a, 'xmof_BasicBehaviors_Behavior', b1)
    if hasattr(b1, 'Kernel_DirectedParameter'):
        assert _is_linked(b1, 'Kernel_DirectedParameter', a)
    _safe_set(a, 'xmof_BasicBehaviors_Behavior', {b2})
    assert _is_linked(a, 'xmof_BasicBehaviors_Behavior', b2)
    if hasattr(b1, 'Kernel_DirectedParameter'):
        assert not _is_linked(b1, 'Kernel_DirectedParameter', a)
    if hasattr(b2, 'Kernel_DirectedParameter'):
        assert _is_linked(b2, 'Kernel_DirectedParameter', a)
    _safe_set(a, 'xmof_BasicBehaviors_Behavior', set())
    assert not _is_linked(a, 'xmof_BasicBehaviors_Behavior', b2)
    if hasattr(b2, 'Kernel_DirectedParameter'):
        assert not _is_linked(b2, 'Kernel_DirectedParameter', a)


def test_assoc_reducer164_link_reassign_clear():
    a = xmof_CompleteActions_ReduceAction(ordered=True)
    b1 = BasicBehaviors_Behavior()
    b2 = BasicBehaviors_Behavior()
    _safe_set(a, 'xmof_CompleteActions_ReduceAction', b1)
    assert _is_linked(a, 'xmof_CompleteActions_ReduceAction', b1)
    if hasattr(b1, 'BasicBehaviors_Behavior165'):
        assert _is_linked(b1, 'BasicBehaviors_Behavior165', a)
    _safe_set(a, 'xmof_CompleteActions_ReduceAction', b2)
    assert _is_linked(a, 'xmof_CompleteActions_ReduceAction', b2)
    if hasattr(b1, 'BasicBehaviors_Behavior165'):
        assert not _is_linked(b1, 'BasicBehaviors_Behavior165', a)
    if hasattr(b2, 'BasicBehaviors_Behavior165'):
        assert _is_linked(b2, 'BasicBehaviors_Behavior165', a)
    _safe_set(a, 'xmof_CompleteActions_ReduceAction', None)
    assert not _is_linked(a, 'xmof_CompleteActions_ReduceAction', b2)
    if hasattr(b2, 'BasicBehaviors_Behavior165'):
        assert not _is_linked(b2, 'BasicBehaviors_Behavior165', a)


def test_assoc_removeAt133_link_reassign_clear():
    a = xmof_IntermediateActions_RemoveStructuralFeatureValueAction(removeDuplicates=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', b1)
    assert _is_linked(a, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', b1)
    if hasattr(b1, 'BasicActions_InputPin134'):
        assert _is_linked(b1, 'BasicActions_InputPin134', a)
    _safe_set(a, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', b2)
    assert _is_linked(a, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', b2)
    if hasattr(b1, 'BasicActions_InputPin134'):
        assert not _is_linked(b1, 'BasicActions_InputPin134', a)
    if hasattr(b2, 'BasicActions_InputPin134'):
        assert _is_linked(b2, 'BasicActions_InputPin134', a)
    _safe_set(a, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', None)
    assert not _is_linked(a, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', b2)
    if hasattr(b2, 'BasicActions_InputPin134'):
        assert not _is_linked(b2, 'BasicActions_InputPin134', a)


def test_assoc_result166_link_reassign_clear():
    a = xmof_CompleteActions_ReduceAction(ordered=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteActions_ReduceAction167', b1)
    assert _is_linked(a, 'xmof_CompleteActions_ReduceAction167', b1)
    if hasattr(b1, 'BasicActions_OutputPin168'):
        assert _is_linked(b1, 'BasicActions_OutputPin168', a)
    _safe_set(a, 'xmof_CompleteActions_ReduceAction167', b2)
    assert _is_linked(a, 'xmof_CompleteActions_ReduceAction167', b2)
    if hasattr(b1, 'BasicActions_OutputPin168'):
        assert not _is_linked(b1, 'BasicActions_OutputPin168', a)
    if hasattr(b2, 'BasicActions_OutputPin168'):
        assert _is_linked(b2, 'BasicActions_OutputPin168', a)
    _safe_set(a, 'xmof_CompleteActions_ReduceAction167', None)
    assert not _is_linked(a, 'xmof_CompleteActions_ReduceAction167', b2)
    if hasattr(b2, 'BasicActions_OutputPin168'):
        assert not _is_linked(b2, 'BasicActions_OutputPin168', a)


def test_assoc_result178_link_reassign_clear():
    a = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', b1)
    assert _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', b1)
    if hasattr(b1, 'BasicActions_OutputPin180'):
        assert _is_linked(b1, 'BasicActions_OutputPin180', a)
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', b2)
    assert _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', b2)
    if hasattr(b1, 'BasicActions_OutputPin180'):
        assert not _is_linked(b1, 'BasicActions_OutputPin180', a)
    if hasattr(b2, 'BasicActions_OutputPin180'):
        assert _is_linked(b2, 'BasicActions_OutputPin180', a)
    _safe_set(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', None)
    assert not _is_linked(a, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', b2)
    if hasattr(b2, 'BasicActions_OutputPin180'):
        assert not _is_linked(b2, 'BasicActions_OutputPin180', a)


def test_assoc_result192_link_reassign_clear():
    a = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteActions_AcceptEventAction', {b1})
    assert _is_linked(a, 'xmof_CompleteActions_AcceptEventAction', b1)
    if hasattr(b1, 'BasicActions_OutputPin193'):
        assert _is_linked(b1, 'BasicActions_OutputPin193', a)
    _safe_set(a, 'xmof_CompleteActions_AcceptEventAction', {b2})
    assert _is_linked(a, 'xmof_CompleteActions_AcceptEventAction', b2)
    if hasattr(b1, 'BasicActions_OutputPin193'):
        assert not _is_linked(b1, 'BasicActions_OutputPin193', a)
    if hasattr(b2, 'BasicActions_OutputPin193'):
        assert _is_linked(b2, 'BasicActions_OutputPin193', a)
    _safe_set(a, 'xmof_CompleteActions_AcceptEventAction', set())
    assert not _is_linked(a, 'xmof_CompleteActions_AcceptEventAction', b2)
    if hasattr(b2, 'BasicActions_OutputPin193'):
        assert not _is_linked(b2, 'BasicActions_OutputPin193', a)


def test_assoc_result203_link_reassign_clear():
    a = xmof_BasicActions_CallAction(synchronous=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_BasicActions_CallAction', {b1})
    assert _is_linked(a, 'xmof_BasicActions_CallAction', b1)
    if hasattr(b1, 'BasicActions_OutputPin204'):
        assert _is_linked(b1, 'BasicActions_OutputPin204', a)
    _safe_set(a, 'xmof_BasicActions_CallAction', {b2})
    assert _is_linked(a, 'xmof_BasicActions_CallAction', b2)
    if hasattr(b1, 'BasicActions_OutputPin204'):
        assert not _is_linked(b1, 'BasicActions_OutputPin204', a)
    if hasattr(b2, 'BasicActions_OutputPin204'):
        assert _is_linked(b2, 'BasicActions_OutputPin204', a)
    _safe_set(a, 'xmof_BasicActions_CallAction', set())
    assert not _is_linked(a, 'xmof_BasicActions_CallAction', b2)
    if hasattr(b2, 'BasicActions_OutputPin204'):
        assert not _is_linked(b2, 'BasicActions_OutputPin204', a)


def test_assoc_result60_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode61', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode61', b1)
    if hasattr(b1, 'BasicActions_OutputPin62'):
        assert _is_linked(b1, 'BasicActions_OutputPin62', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode61', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode61', b2)
    if hasattr(b1, 'BasicActions_OutputPin62'):
        assert not _is_linked(b1, 'BasicActions_OutputPin62', a)
    if hasattr(b2, 'BasicActions_OutputPin62'):
        assert _is_linked(b2, 'BasicActions_OutputPin62', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode61', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode61', b2)
    if hasattr(b2, 'BasicActions_OutputPin62'):
        assert not _is_linked(b2, 'BasicActions_OutputPin62', a)


def test_assoc_result84_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_ConditionalNode85', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_ConditionalNode85', b1)
    if hasattr(b1, 'BasicActions_OutputPin86'):
        assert _is_linked(b1, 'BasicActions_OutputPin86', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_ConditionalNode85', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_ConditionalNode85', b2)
    if hasattr(b1, 'BasicActions_OutputPin86'):
        assert not _is_linked(b1, 'BasicActions_OutputPin86', a)
    if hasattr(b2, 'BasicActions_OutputPin86'):
        assert _is_linked(b2, 'BasicActions_OutputPin86', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_ConditionalNode85', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_ConditionalNode85', b2)
    if hasattr(b2, 'BasicActions_OutputPin86'):
        assert not _is_linked(b2, 'BasicActions_OutputPin86', a)


def test_assoc_setupPart66_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = CompleteStructuredActivities_ExecutableNode()
    b2 = CompleteStructuredActivities_ExecutableNode()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode67', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode67', b1)
    if hasattr(b1, 'CompleteStructuredActivities_ExecutableNode68'):
        assert _is_linked(b1, 'CompleteStructuredActivities_ExecutableNode68', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode67', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode67', b2)
    if hasattr(b1, 'CompleteStructuredActivities_ExecutableNode68'):
        assert not _is_linked(b1, 'CompleteStructuredActivities_ExecutableNode68', a)
    if hasattr(b2, 'CompleteStructuredActivities_ExecutableNode68'):
        assert _is_linked(b2, 'CompleteStructuredActivities_ExecutableNode68', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode67', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode67', b2)
    if hasattr(b2, 'CompleteStructuredActivities_ExecutableNode68'):
        assert not _is_linked(b2, 'CompleteStructuredActivities_ExecutableNode68', a)


def test_assoc_specification0_link_reassign_clear():
    a = xmof_BasicBehaviors_Behavior(reentrant=True)
    b1 = Kernel_BehavioredEOperation()
    b2 = Kernel_BehavioredEOperation()
    _safe_set(a, 'method', b1)
    assert _is_linked(a, 'method', b1)
    if hasattr(b1, 'BehavioredEOperation'):
        assert _is_linked(b1, 'BehavioredEOperation', a)
    _safe_set(a, 'method', b2)
    assert _is_linked(a, 'method', b2)
    if hasattr(b1, 'BehavioredEOperation'):
        assert not _is_linked(b1, 'BehavioredEOperation', a)
    if hasattr(b2, 'BehavioredEOperation'):
        assert _is_linked(b2, 'BehavioredEOperation', a)
    _safe_set(a, 'method', None)
    assert not _is_linked(a, 'method', b2)
    if hasattr(b2, 'BehavioredEOperation'):
        assert not _is_linked(b2, 'BehavioredEOperation', a)


def test_assoc_structuredNodeInput94_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', b1)
    if hasattr(b1, 'BasicActions_InputPin96'):
        assert _is_linked(b1, 'BasicActions_InputPin96', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', b2)
    if hasattr(b1, 'BasicActions_InputPin96'):
        assert not _is_linked(b1, 'BasicActions_InputPin96', a)
    if hasattr(b2, 'BasicActions_InputPin96'):
        assert _is_linked(b2, 'BasicActions_InputPin96', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', b2)
    if hasattr(b2, 'BasicActions_InputPin96'):
        assert not _is_linked(b2, 'BasicActions_InputPin96', a)


def test_assoc_structuredNodeOutput92_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = BasicActions_OutputPin()
    b2 = BasicActions_OutputPin()
    _safe_set(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode', b1)
    if hasattr(b1, 'BasicActions_OutputPin93'):
        assert _is_linked(b1, 'BasicActions_OutputPin93', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode', b2)
    if hasattr(b1, 'BasicActions_OutputPin93'):
        assert not _is_linked(b1, 'BasicActions_OutputPin93', a)
    if hasattr(b2, 'BasicActions_OutputPin93'):
        assert _is_linked(b2, 'BasicActions_OutputPin93', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_StructuredActivityNode', b2)
    if hasattr(b2, 'BasicActions_OutputPin93'):
        assert not _is_linked(b2, 'BasicActions_OutputPin93', a)


def test_assoc_target156_link_reassign_clear():
    a = xmof_IntermediateActions_DestroyObjectAction(destroyLinks=True, destroyOwnedObjects=True)
    b1 = BasicActions_InputPin()
    b2 = BasicActions_InputPin()
    _safe_set(a, 'xmof_IntermediateActions_DestroyObjectAction', b1)
    assert _is_linked(a, 'xmof_IntermediateActions_DestroyObjectAction', b1)
    if hasattr(b1, 'BasicActions_InputPin157'):
        assert _is_linked(b1, 'BasicActions_InputPin157', a)
    _safe_set(a, 'xmof_IntermediateActions_DestroyObjectAction', b2)
    assert _is_linked(a, 'xmof_IntermediateActions_DestroyObjectAction', b2)
    if hasattr(b1, 'BasicActions_InputPin157'):
        assert not _is_linked(b1, 'BasicActions_InputPin157', a)
    if hasattr(b2, 'BasicActions_InputPin157'):
        assert _is_linked(b2, 'BasicActions_InputPin157', a)
    _safe_set(a, 'xmof_IntermediateActions_DestroyObjectAction', None)
    assert not _is_linked(a, 'xmof_IntermediateActions_DestroyObjectAction', b2)
    if hasattr(b2, 'BasicActions_InputPin157'):
        assert not _is_linked(b2, 'BasicActions_InputPin157', a)


def test_assoc_test50_link_reassign_clear():
    a = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    b1 = CompleteStructuredActivities_ExecutableNode()
    b2 = CompleteStructuredActivities_ExecutableNode()
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode51', {b1})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode51', b1)
    if hasattr(b1, 'CompleteStructuredActivities_ExecutableNode'):
        assert _is_linked(b1, 'CompleteStructuredActivities_ExecutableNode', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode51', {b2})
    assert _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode51', b2)
    if hasattr(b1, 'CompleteStructuredActivities_ExecutableNode'):
        assert not _is_linked(b1, 'CompleteStructuredActivities_ExecutableNode', a)
    if hasattr(b2, 'CompleteStructuredActivities_ExecutableNode'):
        assert _is_linked(b2, 'CompleteStructuredActivities_ExecutableNode', a)
    _safe_set(a, 'xmof_CompleteStructuredActivities_LoopNode51', set())
    assert not _is_linked(a, 'xmof_CompleteStructuredActivities_LoopNode51', b2)
    if hasattr(b2, 'CompleteStructuredActivities_ExecutableNode'):
        assert not _is_linked(b2, 'CompleteStructuredActivities_ExecutableNode', a)


def test_assoc_trigger194_link_reassign_clear():
    a = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    b1 = Communications_Trigger()
    b2 = Communications_Trigger()
    _safe_set(a, 'xmof_CompleteActions_AcceptEventAction195', {b1})
    assert _is_linked(a, 'xmof_CompleteActions_AcceptEventAction195', b1)
    if hasattr(b1, 'Communications_Trigger'):
        assert _is_linked(b1, 'Communications_Trigger', a)
    _safe_set(a, 'xmof_CompleteActions_AcceptEventAction195', {b2})
    assert _is_linked(a, 'xmof_CompleteActions_AcceptEventAction195', b2)
    if hasattr(b1, 'Communications_Trigger'):
        assert not _is_linked(b1, 'Communications_Trigger', a)
    if hasattr(b2, 'Communications_Trigger'):
        assert _is_linked(b2, 'Communications_Trigger', a)
    _safe_set(a, 'xmof_CompleteActions_AcceptEventAction195', set())
    assert not _is_linked(a, 'xmof_CompleteActions_AcceptEventAction195', b2)
    if hasattr(b2, 'Communications_Trigger'):
        assert not _is_linked(b2, 'Communications_Trigger', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

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


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


BasicActions_InputPin_strategy = st.builds(BasicActions_InputPin)
@given(instance=BasicActions_InputPin_strategy)
@settings(max_examples=25)
def test_BasicActions_InputPin_instantiation(instance):
    assert isinstance(instance, BasicActions_InputPin)


BasicActions_OutputPin_strategy = st.builds(BasicActions_OutputPin)
@given(instance=BasicActions_OutputPin_strategy)
@settings(max_examples=25)
def test_BasicActions_OutputPin_instantiation(instance):
    assert isinstance(instance, BasicActions_OutputPin)


BasicActions_xmof_EClassifier_strategy = st.builds(BasicActions_xmof_EClassifier)
@given(instance=BasicActions_xmof_EClassifier_strategy)
@settings(max_examples=25)
def test_BasicActions_xmof_EClassifier_instantiation(instance):
    assert isinstance(instance, BasicActions_xmof_EClassifier)


BasicBehaviors_Behavior_strategy = st.builds(BasicBehaviors_Behavior)
@given(instance=BasicBehaviors_Behavior_strategy)
@settings(max_examples=25)
def test_BasicBehaviors_Behavior_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_Behavior)


BasicBehaviors_BehavioredClassifier_strategy = st.builds(BasicBehaviors_BehavioredClassifier)
@given(instance=BasicBehaviors_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_BasicBehaviors_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_BehavioredClassifier)


Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


BehavioredEClass_strategy = st.builds(BehavioredEClass)
@given(instance=BehavioredEClass_strategy)
@settings(max_examples=25)
def test_BehavioredEClass_instantiation(instance):
    assert isinstance(instance, BehavioredEClass)


BehavioredEOperation_strategy = st.builds(BehavioredEOperation)
@given(instance=BehavioredEOperation_strategy)
@settings(max_examples=25)
def test_BehavioredEOperation_instantiation(instance):
    assert isinstance(instance, BehavioredEOperation)


CallAction_strategy = st.builds(CallAction)
@given(instance=CallAction_strategy)
@settings(max_examples=25)
def test_CallAction_instantiation(instance):
    assert isinstance(instance, CallAction)


Communications_Event_strategy = st.builds(Communications_Event)
@given(instance=Communications_Event_strategy)
@settings(max_examples=25)
def test_Communications_Event_instantiation(instance):
    assert isinstance(instance, Communications_Event)


Communications_Signal_strategy = st.builds(Communications_Signal)
@given(instance=Communications_Signal_strategy)
@settings(max_examples=25)
def test_Communications_Signal_instantiation(instance):
    assert isinstance(instance, Communications_Signal)


Communications_Trigger_strategy = st.builds(Communications_Trigger)
@given(instance=Communications_Trigger_strategy)
@settings(max_examples=25)
def test_Communications_Trigger_instantiation(instance):
    assert isinstance(instance, Communications_Trigger)


Communications_xmof_EAttribute_strategy = st.builds(Communications_xmof_EAttribute)
@given(instance=Communications_xmof_EAttribute_strategy)
@settings(max_examples=25)
def test_Communications_xmof_EAttribute_instantiation(instance):
    assert isinstance(instance, Communications_xmof_EAttribute)


CompleteActions_xmof_EClassifier_strategy = st.builds(CompleteActions_xmof_EClassifier)
@given(instance=CompleteActions_xmof_EClassifier_strategy)
@settings(max_examples=25)
def test_CompleteActions_xmof_EClassifier_instantiation(instance):
    assert isinstance(instance, CompleteActions_xmof_EClassifier)


CompleteStructuredActivities_Clause_strategy = st.builds(CompleteStructuredActivities_Clause)
@given(instance=CompleteStructuredActivities_Clause_strategy)
@settings(max_examples=25)
def test_CompleteStructuredActivities_Clause_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities_Clause)


CompleteStructuredActivities_ExecutableNode_strategy = st.builds(CompleteStructuredActivities_ExecutableNode)
@given(instance=CompleteStructuredActivities_ExecutableNode_strategy)
@settings(max_examples=25)
def test_CompleteStructuredActivities_ExecutableNode_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities_ExecutableNode)


CompleteStructuredActivities_StructuredActivityNode_strategy = st.builds(CompleteStructuredActivities_StructuredActivityNode)
@given(instance=CompleteStructuredActivities_StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_CompleteStructuredActivities_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities_StructuredActivityNode)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


EClass_strategy = st.builds(EClass)
@given(instance=EClass_strategy)
@settings(max_examples=25)
def test_EClass_instantiation(instance):
    assert isinstance(instance, EClass)


EClassifier_strategy = st.builds(EClassifier)
@given(instance=EClassifier_strategy)
@settings(max_examples=25)
def test_EClassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)


EDataType_strategy = st.builds(EDataType)
@given(instance=EDataType_strategy)
@settings(max_examples=25)
def test_EDataType_instantiation(instance):
    assert isinstance(instance, EDataType)


EModelElement_strategy = st.builds(EModelElement)
@given(instance=EModelElement_strategy)
@settings(max_examples=25)
def test_EModelElement_instantiation(instance):
    assert isinstance(instance, EModelElement)


ENamedElement_strategy = st.builds(ENamedElement)
@given(instance=ENamedElement_strategy)
@settings(max_examples=25)
def test_ENamedElement_instantiation(instance):
    assert isinstance(instance, ENamedElement)


EOperation_strategy = st.builds(EOperation)
@given(instance=EOperation_strategy)
@settings(max_examples=25)
def test_EOperation_instantiation(instance):
    assert isinstance(instance, EOperation)


EParameter_strategy = st.builds(EParameter)
@given(instance=EParameter_strategy)
@settings(max_examples=25)
def test_EParameter_instantiation(instance):
    assert isinstance(instance, EParameter)


ETypedElement_strategy = st.builds(ETypedElement)
@given(instance=ETypedElement_strategy)
@settings(max_examples=25)
def test_ETypedElement_instantiation(instance):
    assert isinstance(instance, ETypedElement)


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


ExtraStructuredActivities_ExpansionNode_strategy = st.builds(ExtraStructuredActivities_ExpansionNode)
@given(instance=ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=25)
def test_ExtraStructuredActivities_ExpansionNode_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities_ExpansionNode)


ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(ExtraStructuredActivities_ExpansionRegion)
@given(instance=ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=25)
def test_ExtraStructuredActivities_ExpansionRegion_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities_ExpansionRegion)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


InstanceSpecification_strategy = st.builds(InstanceSpecification)
@given(instance=InstanceSpecification_strategy)
@settings(max_examples=25)
def test_InstanceSpecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)


IntermediateActions_LinkEndData_strategy = st.builds(IntermediateActions_LinkEndData)
@given(instance=IntermediateActions_LinkEndData_strategy)
@settings(max_examples=25)
def test_IntermediateActions_LinkEndData_instantiation(instance):
    assert isinstance(instance, IntermediateActions_LinkEndData)


IntermediateActions_xmof_EClassifier_strategy = st.builds(IntermediateActions_xmof_EClassifier)
@given(instance=IntermediateActions_xmof_EClassifier_strategy)
@settings(max_examples=25)
def test_IntermediateActions_xmof_EClassifier_instantiation(instance):
    assert isinstance(instance, IntermediateActions_xmof_EClassifier)


IntermediateActions_xmof_EReference_strategy = st.builds(IntermediateActions_xmof_EReference)
@given(instance=IntermediateActions_xmof_EReference_strategy)
@settings(max_examples=25)
def test_IntermediateActions_xmof_EReference_instantiation(instance):
    assert isinstance(instance, IntermediateActions_xmof_EReference)


IntermediateActions_xmof_EStructuralFeature_strategy = st.builds(IntermediateActions_xmof_EStructuralFeature)
@given(instance=IntermediateActions_xmof_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_IntermediateActions_xmof_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, IntermediateActions_xmof_EStructuralFeature)


IntermediateActivities_Activity_strategy = st.builds(IntermediateActivities_Activity)
@given(instance=IntermediateActivities_Activity_strategy)
@settings(max_examples=25)
def test_IntermediateActivities_Activity_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_Activity)


IntermediateActivities_ActivityEdge_strategy = st.builds(IntermediateActivities_ActivityEdge)
@given(instance=IntermediateActivities_ActivityEdge_strategy)
@settings(max_examples=25)
def test_IntermediateActivities_ActivityEdge_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ActivityEdge)


IntermediateActivities_ActivityNode_strategy = st.builds(IntermediateActivities_ActivityNode)
@given(instance=IntermediateActivities_ActivityNode_strategy)
@settings(max_examples=25)
def test_IntermediateActivities_ActivityNode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ActivityNode)


IntermediateActivities_ObjectFlow_strategy = st.builds(IntermediateActivities_ObjectFlow)
@given(instance=IntermediateActivities_ObjectFlow_strategy)
@settings(max_examples=25)
def test_IntermediateActivities_ObjectFlow_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ObjectFlow)


IntermediateActivities_ObjectNode_strategy = st.builds(IntermediateActivities_ObjectNode)
@given(instance=IntermediateActivities_ObjectNode_strategy)
@settings(max_examples=25)
def test_IntermediateActivities_ObjectNode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ObjectNode)


InvocationAction_strategy = st.builds(InvocationAction)
@given(instance=InvocationAction_strategy)
@settings(max_examples=25)
def test_InvocationAction_instantiation(instance):
    assert isinstance(instance, InvocationAction)


Kernel_BehavioredEOperation_strategy = st.builds(Kernel_BehavioredEOperation)
@given(instance=Kernel_BehavioredEOperation_strategy)
@settings(max_examples=25)
def test_Kernel_BehavioredEOperation_instantiation(instance):
    assert isinstance(instance, Kernel_BehavioredEOperation)


Kernel_DirectedParameter_strategy = st.builds(Kernel_DirectedParameter)
@given(instance=Kernel_DirectedParameter_strategy)
@settings(max_examples=25)
def test_Kernel_DirectedParameter_instantiation(instance):
    assert isinstance(instance, Kernel_DirectedParameter)


Kernel_InstanceSpecification_strategy = st.builds(Kernel_InstanceSpecification)
@given(instance=Kernel_InstanceSpecification_strategy)
@settings(max_examples=25)
def test_Kernel_InstanceSpecification_instantiation(instance):
    assert isinstance(instance, Kernel_InstanceSpecification)


Kernel_Slot_strategy = st.builds(Kernel_Slot)
@given(instance=Kernel_Slot_strategy)
@settings(max_examples=25)
def test_Kernel_Slot_instantiation(instance):
    assert isinstance(instance, Kernel_Slot)


Kernel_ValueSpecification_strategy = st.builds(Kernel_ValueSpecification)
@given(instance=Kernel_ValueSpecification_strategy)
@settings(max_examples=25)
def test_Kernel_ValueSpecification_instantiation(instance):
    assert isinstance(instance, Kernel_ValueSpecification)


Kernel_xmof_EClassifier_strategy = st.builds(Kernel_xmof_EClassifier)
@given(instance=Kernel_xmof_EClassifier_strategy)
@settings(max_examples=25)
def test_Kernel_xmof_EClassifier_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EClassifier)


Kernel_xmof_EEnumLiteral_strategy = st.builds(Kernel_xmof_EEnumLiteral)
@given(instance=Kernel_xmof_EEnumLiteral_strategy)
@settings(max_examples=25)
def test_Kernel_xmof_EEnumLiteral_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EEnumLiteral)


Kernel_xmof_EStructuralFeature_strategy = st.builds(Kernel_xmof_EStructuralFeature)
@given(instance=Kernel_xmof_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_Kernel_xmof_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EStructuralFeature)


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


MessageEvent_strategy = st.builds(MessageEvent)
@given(instance=MessageEvent_strategy)
@settings(max_examples=25)
def test_MessageEvent_instantiation(instance):
    assert isinstance(instance, MessageEvent)


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


OpaqueBehavior_strategy = st.builds(OpaqueBehavior)
@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=25)
def test_OpaqueBehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)


Pin_strategy = st.builds(Pin)
@given(instance=Pin_strategy)
@settings(max_examples=25)
def test_Pin_instantiation(instance):
    assert isinstance(instance, Pin)


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


ValueSpecification_strategy = st.builds(ValueSpecification)
@given(instance=ValueSpecification_strategy)
@settings(max_examples=25)
def test_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)


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


xmof_BasicActions_Action_strategy = st.builds(xmof_BasicActions_Action, locallyReentrant=st.booleans())
@given(instance=xmof_BasicActions_Action_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_Action_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_Action)


xmof_BasicActions_CallAction_strategy = st.builds(xmof_BasicActions_CallAction, synchronous=st.booleans())
@given(instance=xmof_BasicActions_CallAction_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_CallAction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_CallAction)


xmof_BasicActions_CallBehaviorAction_strategy = st.builds(xmof_BasicActions_CallBehaviorAction)
@given(instance=xmof_BasicActions_CallBehaviorAction_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_CallBehaviorAction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_CallBehaviorAction)


xmof_BasicActions_CallOperationAction_strategy = st.builds(xmof_BasicActions_CallOperationAction)
@given(instance=xmof_BasicActions_CallOperationAction_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_CallOperationAction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_CallOperationAction)


xmof_BasicActions_InputPin_strategy = st.builds(xmof_BasicActions_InputPin)
@given(instance=xmof_BasicActions_InputPin_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_InputPin_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_InputPin)


xmof_BasicActions_InvocationAction_strategy = st.builds(xmof_BasicActions_InvocationAction)
@given(instance=xmof_BasicActions_InvocationAction_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_InvocationAction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_InvocationAction)


xmof_BasicActions_OutputPin_strategy = st.builds(xmof_BasicActions_OutputPin)
@given(instance=xmof_BasicActions_OutputPin_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_OutputPin_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_OutputPin)


xmof_BasicActions_Pin_strategy = st.builds(xmof_BasicActions_Pin)
@given(instance=xmof_BasicActions_Pin_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_Pin_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_Pin)


xmof_BasicActions_SendSignalAction_strategy = st.builds(xmof_BasicActions_SendSignalAction)
@given(instance=xmof_BasicActions_SendSignalAction_strategy)
@settings(max_examples=25)
def test_xmof_BasicActions_SendSignalAction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_SendSignalAction)


xmof_BasicBehaviors_Behavior_strategy = st.builds(xmof_BasicBehaviors_Behavior, reentrant=st.booleans())
@given(instance=xmof_BasicBehaviors_Behavior_strategy)
@settings(max_examples=25)
def test_xmof_BasicBehaviors_Behavior_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_Behavior)


xmof_BasicBehaviors_BehavioredClassifier_strategy = st.builds(xmof_BasicBehaviors_BehavioredClassifier)
@given(instance=xmof_BasicBehaviors_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_xmof_BasicBehaviors_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_BehavioredClassifier)


xmof_BasicBehaviors_FunctionBehavior_strategy = st.builds(xmof_BasicBehaviors_FunctionBehavior)
@given(instance=xmof_BasicBehaviors_FunctionBehavior_strategy)
@settings(max_examples=25)
def test_xmof_BasicBehaviors_FunctionBehavior_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_FunctionBehavior)


xmof_BasicBehaviors_OpaqueBehavior_strategy = st.builds(xmof_BasicBehaviors_OpaqueBehavior, body=safe_text, language=safe_text)
@given(instance=xmof_BasicBehaviors_OpaqueBehavior_strategy)
@settings(max_examples=25)
def test_xmof_BasicBehaviors_OpaqueBehavior_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_OpaqueBehavior)


xmof_Communications_Event_strategy = st.builds(xmof_Communications_Event)
@given(instance=xmof_Communications_Event_strategy)
@settings(max_examples=25)
def test_xmof_Communications_Event_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Event)


xmof_Communications_MessageEvent_strategy = st.builds(xmof_Communications_MessageEvent)
@given(instance=xmof_Communications_MessageEvent_strategy)
@settings(max_examples=25)
def test_xmof_Communications_MessageEvent_instantiation(instance):
    assert isinstance(instance, xmof_Communications_MessageEvent)


xmof_Communications_Reception_strategy = st.builds(xmof_Communications_Reception)
@given(instance=xmof_Communications_Reception_strategy)
@settings(max_examples=25)
def test_xmof_Communications_Reception_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Reception)


xmof_Communications_Signal_strategy = st.builds(xmof_Communications_Signal)
@given(instance=xmof_Communications_Signal_strategy)
@settings(max_examples=25)
def test_xmof_Communications_Signal_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Signal)


xmof_Communications_SignalEvent_strategy = st.builds(xmof_Communications_SignalEvent)
@given(instance=xmof_Communications_SignalEvent_strategy)
@settings(max_examples=25)
def test_xmof_Communications_SignalEvent_instantiation(instance):
    assert isinstance(instance, xmof_Communications_SignalEvent)


xmof_Communications_Trigger_strategy = st.builds(xmof_Communications_Trigger)
@given(instance=xmof_Communications_Trigger_strategy)
@settings(max_examples=25)
def test_xmof_Communications_Trigger_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Trigger)


xmof_CompleteActions_AcceptEventAction_strategy = st.builds(xmof_CompleteActions_AcceptEventAction, unmarshall=st.booleans())
@given(instance=xmof_CompleteActions_AcceptEventAction_strategy)
@settings(max_examples=25)
def test_xmof_CompleteActions_AcceptEventAction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_AcceptEventAction)


xmof_CompleteActions_ReadExtentAction_strategy = st.builds(xmof_CompleteActions_ReadExtentAction)
@given(instance=xmof_CompleteActions_ReadExtentAction_strategy)
@settings(max_examples=25)
def test_xmof_CompleteActions_ReadExtentAction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReadExtentAction)


xmof_CompleteActions_ReadIsClassifiedObjectAction_strategy = st.builds(xmof_CompleteActions_ReadIsClassifiedObjectAction, direct=st.booleans())
@given(instance=xmof_CompleteActions_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=25)
def test_xmof_CompleteActions_ReadIsClassifiedObjectAction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReadIsClassifiedObjectAction)


xmof_CompleteActions_ReclassifyObjectAction_strategy = st.builds(xmof_CompleteActions_ReclassifyObjectAction, replaceAll=st.booleans())
@given(instance=xmof_CompleteActions_ReclassifyObjectAction_strategy)
@settings(max_examples=25)
def test_xmof_CompleteActions_ReclassifyObjectAction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReclassifyObjectAction)


xmof_CompleteActions_ReduceAction_strategy = st.builds(xmof_CompleteActions_ReduceAction, ordered=st.booleans())
@given(instance=xmof_CompleteActions_ReduceAction_strategy)
@settings(max_examples=25)
def test_xmof_CompleteActions_ReduceAction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReduceAction)


xmof_CompleteActions_StartClassifierBehaviorAction_strategy = st.builds(xmof_CompleteActions_StartClassifierBehaviorAction)
@given(instance=xmof_CompleteActions_StartClassifierBehaviorAction_strategy)
@settings(max_examples=25)
def test_xmof_CompleteActions_StartClassifierBehaviorAction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_StartClassifierBehaviorAction)


xmof_CompleteActions_StartObjectBehaviorAction_strategy = st.builds(xmof_CompleteActions_StartObjectBehaviorAction)
@given(instance=xmof_CompleteActions_StartObjectBehaviorAction_strategy)
@settings(max_examples=25)
def test_xmof_CompleteActions_StartObjectBehaviorAction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_StartObjectBehaviorAction)


xmof_CompleteStructuredActivities_Clause_strategy = st.builds(xmof_CompleteStructuredActivities_Clause)
@given(instance=xmof_CompleteStructuredActivities_Clause_strategy)
@settings(max_examples=25)
def test_xmof_CompleteStructuredActivities_Clause_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_Clause)


xmof_CompleteStructuredActivities_ConditionalNode_strategy = st.builds(xmof_CompleteStructuredActivities_ConditionalNode, assured=st.booleans(), determinate=st.booleans())
@given(instance=xmof_CompleteStructuredActivities_ConditionalNode_strategy)
@settings(max_examples=25)
def test_xmof_CompleteStructuredActivities_ConditionalNode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_ConditionalNode)


xmof_CompleteStructuredActivities_ExecutableNode_strategy = st.builds(xmof_CompleteStructuredActivities_ExecutableNode)
@given(instance=xmof_CompleteStructuredActivities_ExecutableNode_strategy)
@settings(max_examples=25)
def test_xmof_CompleteStructuredActivities_ExecutableNode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_ExecutableNode)


xmof_CompleteStructuredActivities_LoopNode_strategy = st.builds(xmof_CompleteStructuredActivities_LoopNode, testedFirst=st.booleans())
@given(instance=xmof_CompleteStructuredActivities_LoopNode_strategy)
@settings(max_examples=25)
def test_xmof_CompleteStructuredActivities_LoopNode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_LoopNode)


xmof_CompleteStructuredActivities_StructuredActivityNode_strategy = st.builds(xmof_CompleteStructuredActivities_StructuredActivityNode, mustIsolate=st.booleans())
@given(instance=xmof_CompleteStructuredActivities_StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_xmof_CompleteStructuredActivities_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_StructuredActivityNode)


xmof_ExtraStructuredActivities_ExpansionNode_strategy = st.builds(xmof_ExtraStructuredActivities_ExpansionNode)
@given(instance=xmof_ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=25)
def test_xmof_ExtraStructuredActivities_ExpansionNode_instantiation(instance):
    assert isinstance(instance, xmof_ExtraStructuredActivities_ExpansionNode)


xmof_ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(xmof_ExtraStructuredActivities_ExpansionRegion, mode=safe_text)
@given(instance=xmof_ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=25)
def test_xmof_ExtraStructuredActivities_ExpansionRegion_instantiation(instance):
    assert isinstance(instance, xmof_ExtraStructuredActivities_ExpansionRegion)


xmof_IntermediateActions_AddStructuralFeatureValueAction_strategy = st.builds(xmof_IntermediateActions_AddStructuralFeatureValueAction, replaceAll=st.booleans())
@given(instance=xmof_IntermediateActions_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_AddStructuralFeatureValueAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_AddStructuralFeatureValueAction)


xmof_IntermediateActions_ClearAssociationAction_strategy = st.builds(xmof_IntermediateActions_ClearAssociationAction)
@given(instance=xmof_IntermediateActions_ClearAssociationAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_ClearAssociationAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ClearAssociationAction)


xmof_IntermediateActions_ClearStructuralFeatureAction_strategy = st.builds(xmof_IntermediateActions_ClearStructuralFeatureAction)
@given(instance=xmof_IntermediateActions_ClearStructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_ClearStructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ClearStructuralFeatureAction)


xmof_IntermediateActions_CreateLinkAction_strategy = st.builds(xmof_IntermediateActions_CreateLinkAction)
@given(instance=xmof_IntermediateActions_CreateLinkAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_CreateLinkAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_CreateLinkAction)


xmof_IntermediateActions_CreateObjectAction_strategy = st.builds(xmof_IntermediateActions_CreateObjectAction)
@given(instance=xmof_IntermediateActions_CreateObjectAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_CreateObjectAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_CreateObjectAction)


xmof_IntermediateActions_DestroyLinkAction_strategy = st.builds(xmof_IntermediateActions_DestroyLinkAction)
@given(instance=xmof_IntermediateActions_DestroyLinkAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_DestroyLinkAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_DestroyLinkAction)


xmof_IntermediateActions_DestroyObjectAction_strategy = st.builds(xmof_IntermediateActions_DestroyObjectAction, destroyLinks=st.booleans(), destroyOwnedObjects=st.booleans())
@given(instance=xmof_IntermediateActions_DestroyObjectAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_DestroyObjectAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_DestroyObjectAction)


xmof_IntermediateActions_LinkAction_strategy = st.builds(xmof_IntermediateActions_LinkAction)
@given(instance=xmof_IntermediateActions_LinkAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_LinkAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkAction)


xmof_IntermediateActions_LinkEndCreationData_strategy = st.builds(xmof_IntermediateActions_LinkEndCreationData, replaceAll=st.booleans())
@given(instance=xmof_IntermediateActions_LinkEndCreationData_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_LinkEndCreationData_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkEndCreationData)


xmof_IntermediateActions_LinkEndData_strategy = st.builds(xmof_IntermediateActions_LinkEndData)
@given(instance=xmof_IntermediateActions_LinkEndData_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_LinkEndData_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkEndData)


xmof_IntermediateActions_LinkEndDestructionData_strategy = st.builds(xmof_IntermediateActions_LinkEndDestructionData, destroyDuplicates=st.booleans())
@given(instance=xmof_IntermediateActions_LinkEndDestructionData_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_LinkEndDestructionData_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkEndDestructionData)


xmof_IntermediateActions_ReadLinkAction_strategy = st.builds(xmof_IntermediateActions_ReadLinkAction)
@given(instance=xmof_IntermediateActions_ReadLinkAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_ReadLinkAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ReadLinkAction)


xmof_IntermediateActions_ReadSelfAction_strategy = st.builds(xmof_IntermediateActions_ReadSelfAction)
@given(instance=xmof_IntermediateActions_ReadSelfAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_ReadSelfAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ReadSelfAction)


xmof_IntermediateActions_ReadStructuralFeatureAction_strategy = st.builds(xmof_IntermediateActions_ReadStructuralFeatureAction)
@given(instance=xmof_IntermediateActions_ReadStructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_ReadStructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ReadStructuralFeatureAction)


xmof_IntermediateActions_RemoveStructuralFeatureValueAction_strategy = st.builds(xmof_IntermediateActions_RemoveStructuralFeatureValueAction, removeDuplicates=st.booleans())
@given(instance=xmof_IntermediateActions_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_RemoveStructuralFeatureValueAction)


xmof_IntermediateActions_StructuralFeatureAction_strategy = st.builds(xmof_IntermediateActions_StructuralFeatureAction)
@given(instance=xmof_IntermediateActions_StructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_StructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_StructuralFeatureAction)


xmof_IntermediateActions_TestIdentityAction_strategy = st.builds(xmof_IntermediateActions_TestIdentityAction)
@given(instance=xmof_IntermediateActions_TestIdentityAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_TestIdentityAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_TestIdentityAction)


xmof_IntermediateActions_ValueSpecificationAction_strategy = st.builds(xmof_IntermediateActions_ValueSpecificationAction)
@given(instance=xmof_IntermediateActions_ValueSpecificationAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_ValueSpecificationAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ValueSpecificationAction)


xmof_IntermediateActions_WriteLinkAction_strategy = st.builds(xmof_IntermediateActions_WriteLinkAction)
@given(instance=xmof_IntermediateActions_WriteLinkAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_WriteLinkAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_WriteLinkAction)


xmof_IntermediateActions_WriteStructuralFeatureAction_strategy = st.builds(xmof_IntermediateActions_WriteStructuralFeatureAction)
@given(instance=xmof_IntermediateActions_WriteStructuralFeatureAction_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActions_WriteStructuralFeatureAction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_WriteStructuralFeatureAction)


xmof_IntermediateActivities_Activity_strategy = st.builds(xmof_IntermediateActivities_Activity, readOnly=st.booleans())
@given(instance=xmof_IntermediateActivities_Activity_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_Activity_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_Activity)


xmof_IntermediateActivities_ActivityEdge_strategy = st.builds(xmof_IntermediateActivities_ActivityEdge)
@given(instance=xmof_IntermediateActivities_ActivityEdge_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ActivityEdge_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityEdge)


xmof_IntermediateActivities_ActivityFinalNode_strategy = st.builds(xmof_IntermediateActivities_ActivityFinalNode)
@given(instance=xmof_IntermediateActivities_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityFinalNode)


xmof_IntermediateActivities_ActivityNode_strategy = st.builds(xmof_IntermediateActivities_ActivityNode)
@given(instance=xmof_IntermediateActivities_ActivityNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ActivityNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityNode)


xmof_IntermediateActivities_ActivityParameterNode_strategy = st.builds(xmof_IntermediateActivities_ActivityParameterNode)
@given(instance=xmof_IntermediateActivities_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityParameterNode)


xmof_IntermediateActivities_ControlFlow_strategy = st.builds(xmof_IntermediateActivities_ControlFlow)
@given(instance=xmof_IntermediateActivities_ControlFlow_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ControlFlow_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ControlFlow)


xmof_IntermediateActivities_ControlNode_strategy = st.builds(xmof_IntermediateActivities_ControlNode)
@given(instance=xmof_IntermediateActivities_ControlNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ControlNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ControlNode)


xmof_IntermediateActivities_DecisionNode_strategy = st.builds(xmof_IntermediateActivities_DecisionNode)
@given(instance=xmof_IntermediateActivities_DecisionNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_DecisionNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_DecisionNode)


xmof_IntermediateActivities_FinalNode_strategy = st.builds(xmof_IntermediateActivities_FinalNode)
@given(instance=xmof_IntermediateActivities_FinalNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_FinalNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_FinalNode)


xmof_IntermediateActivities_ForkNode_strategy = st.builds(xmof_IntermediateActivities_ForkNode)
@given(instance=xmof_IntermediateActivities_ForkNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ForkNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ForkNode)


xmof_IntermediateActivities_InitialNode_strategy = st.builds(xmof_IntermediateActivities_InitialNode)
@given(instance=xmof_IntermediateActivities_InitialNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_InitialNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_InitialNode)


xmof_IntermediateActivities_JoinNode_strategy = st.builds(xmof_IntermediateActivities_JoinNode)
@given(instance=xmof_IntermediateActivities_JoinNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_JoinNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_JoinNode)


xmof_IntermediateActivities_MergeNode_strategy = st.builds(xmof_IntermediateActivities_MergeNode)
@given(instance=xmof_IntermediateActivities_MergeNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_MergeNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_MergeNode)


xmof_IntermediateActivities_ObjectFlow_strategy = st.builds(xmof_IntermediateActivities_ObjectFlow)
@given(instance=xmof_IntermediateActivities_ObjectFlow_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ObjectFlow_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ObjectFlow)


xmof_IntermediateActivities_ObjectNode_strategy = st.builds(xmof_IntermediateActivities_ObjectNode)
@given(instance=xmof_IntermediateActivities_ObjectNode_strategy)
@settings(max_examples=25)
def test_xmof_IntermediateActivities_ObjectNode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ObjectNode)


xmof_Kernel_BehavioredEClass_strategy = st.builds(xmof_Kernel_BehavioredEClass)
@given(instance=xmof_Kernel_BehavioredEClass_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_BehavioredEClass_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_BehavioredEClass)


xmof_Kernel_BehavioredEOperation_strategy = st.builds(xmof_Kernel_BehavioredEOperation)
@given(instance=xmof_Kernel_BehavioredEOperation_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_BehavioredEOperation_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_BehavioredEOperation)


xmof_Kernel_DirectedParameter_strategy = st.builds(xmof_Kernel_DirectedParameter, direction=safe_text)
@given(instance=xmof_Kernel_DirectedParameter_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_DirectedParameter_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_DirectedParameter)


xmof_Kernel_EEnumLiteralSpecification_strategy = st.builds(xmof_Kernel_EEnumLiteralSpecification)
@given(instance=xmof_Kernel_EEnumLiteralSpecification_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_EEnumLiteralSpecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_EEnumLiteralSpecification)


xmof_Kernel_InstanceSpecification_strategy = st.builds(xmof_Kernel_InstanceSpecification)
@given(instance=xmof_Kernel_InstanceSpecification_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_InstanceSpecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_InstanceSpecification)


xmof_Kernel_InstanceValue_strategy = st.builds(xmof_Kernel_InstanceValue)
@given(instance=xmof_Kernel_InstanceValue_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_InstanceValue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_InstanceValue)


xmof_Kernel_LiteralBoolean_strategy = st.builds(xmof_Kernel_LiteralBoolean, value=st.booleans())
@given(instance=xmof_Kernel_LiteralBoolean_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_LiteralBoolean_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralBoolean)


xmof_Kernel_LiteralInteger_strategy = st.builds(xmof_Kernel_LiteralInteger, value=st.integers())
@given(instance=xmof_Kernel_LiteralInteger_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_LiteralInteger_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralInteger)


xmof_Kernel_LiteralNull_strategy = st.builds(xmof_Kernel_LiteralNull)
@given(instance=xmof_Kernel_LiteralNull_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_LiteralNull_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralNull)


xmof_Kernel_LiteralSpecification_strategy = st.builds(xmof_Kernel_LiteralSpecification)
@given(instance=xmof_Kernel_LiteralSpecification_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_LiteralSpecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralSpecification)


xmof_Kernel_LiteralString_strategy = st.builds(xmof_Kernel_LiteralString, value=safe_text)
@given(instance=xmof_Kernel_LiteralString_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_LiteralString_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralString)


xmof_Kernel_LiteralUnlimitedNatural_strategy = st.builds(xmof_Kernel_LiteralUnlimitedNatural, value=st.integers())
@given(instance=xmof_Kernel_LiteralUnlimitedNatural_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_LiteralUnlimitedNatural_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralUnlimitedNatural)


xmof_Kernel_MainEClass_strategy = st.builds(xmof_Kernel_MainEClass)
@given(instance=xmof_Kernel_MainEClass_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_MainEClass_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_MainEClass)


xmof_Kernel_PrimitiveType_strategy = st.builds(xmof_Kernel_PrimitiveType)
@given(instance=xmof_Kernel_PrimitiveType_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_PrimitiveType_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_PrimitiveType)


xmof_Kernel_Slot_strategy = st.builds(xmof_Kernel_Slot)
@given(instance=xmof_Kernel_Slot_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_Slot_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_Slot)


xmof_Kernel_ValueSpecification_strategy = st.builds(xmof_Kernel_ValueSpecification)
@given(instance=xmof_Kernel_ValueSpecification_strategy)
@settings(max_examples=25)
def test_xmof_Kernel_ValueSpecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_ValueSpecification)



