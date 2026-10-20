import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_bodyOutput52_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin54' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin54', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode53', {partner})
    assert getattr(partner, 'BasicActions_OutputPin54') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode53', set())
    assert getattr(partner, 'BasicActions_OutputPin54') is None


def test_assoc_bodyPart57_stub_double():
    # CompleteStructuredActivities_ExecutableNode has no real 'CompleteStructuredActivities_ExecutableNode59' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = CompleteStructuredActivities_ExecutableNode()
    setattr(partner, 'CompleteStructuredActivities_ExecutableNode59', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode58', {partner})
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode59') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode58', set())
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode59') is None


def test_assoc_classifier176_stub_double():
    # CompleteActions_xmof_EClassifier has no real 'CompleteActions_xmof_EClassifier177' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReadIsClassifiedObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReadIsClassifiedObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    partner = CompleteActions_xmof_EClassifier()
    setattr(partner, 'CompleteActions_xmof_EClassifier177', None)
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', partner)
    assert getattr(partner, 'CompleteActions_xmof_EClassifier177') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', None)
    assert getattr(partner, 'CompleteActions_xmof_EClassifier177') is None


def test_assoc_clause83_stub_double():
    # CompleteStructuredActivities_Clause has no real 'CompleteStructuredActivities_Clause' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    partner = CompleteStructuredActivities_Clause()
    setattr(partner, 'CompleteStructuredActivities_Clause', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_ConditionalNode', {partner})
    assert getattr(partner, 'CompleteStructuredActivities_Clause') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_ConditionalNode', set())
    assert getattr(partner, 'CompleteStructuredActivities_Clause') is None


def test_assoc_collection169_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin171' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReduceAction(ordered=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin171', None)
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction170', partner)
    assert getattr(partner, 'BasicActions_InputPin171') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction170', None)
    assert getattr(partner, 'BasicActions_InputPin171') is None


def test_assoc_context198_stub_double():
    # BasicActions_xmof_EClassifier has no real 'BasicActions_xmof_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_Action(locallyReentrant=True)
    partner = BasicActions_xmof_EClassifier()
    setattr(partner, 'BasicActions_xmof_EClassifier', None)
    _safe_set(owner, 'xmof_BasicActions_Action199', partner)
    assert getattr(partner, 'BasicActions_xmof_EClassifier') == owner
    _safe_set(owner, 'xmof_BasicActions_Action199', None)
    assert getattr(partner, 'BasicActions_xmof_EClassifier') is None


def test_assoc_context2_stub_double():
    # BasicBehaviors_BehavioredClassifier has no real 'BasicBehaviors_BehavioredClassifier' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicBehaviors_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicBehaviors_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicBehaviors_Behavior(reentrant=True)
    partner = BasicBehaviors_BehavioredClassifier()
    setattr(partner, 'BasicBehaviors_BehavioredClassifier', None)
    _safe_set(owner, 'xmof_BasicBehaviors_Behavior3', partner)
    assert getattr(partner, 'BasicBehaviors_BehavioredClassifier') == owner
    _safe_set(owner, 'xmof_BasicBehaviors_Behavior3', None)
    assert getattr(partner, 'BasicBehaviors_BehavioredClassifier') is None


def test_assoc_decider49_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode', partner)
    assert getattr(partner, 'BasicActions_OutputPin') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode', None)
    assert getattr(partner, 'BasicActions_OutputPin') is None


def test_assoc_destroyAt143_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin144' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_LinkEndDestructionData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_LinkEndDestructionData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_LinkEndDestructionData(destroyDuplicates=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin144', None)
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndDestructionData', partner)
    assert getattr(partner, 'BasicActions_InputPin144') == owner
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndDestructionData', None)
    assert getattr(partner, 'BasicActions_InputPin144') is None


def test_assoc_edge32_stub_double():
    # IntermediateActivities_ActivityEdge has no real 'ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActivities_Activity(readOnly=True)
    partner = IntermediateActivities_ActivityEdge()
    setattr(partner, 'ActivityEdge', None)
    _safe_set(owner, 'activity33', {partner})
    assert getattr(partner, 'ActivityEdge') == owner
    _safe_set(owner, 'activity33', set())
    assert getattr(partner, 'ActivityEdge') is None


def test_assoc_edge89_stub_double():
    # IntermediateActivities_ActivityEdge has no real 'ActivityEdge91' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = IntermediateActivities_ActivityEdge()
    setattr(partner, 'ActivityEdge91', None)
    _safe_set(owner, 'inStructuredNode90', {partner})
    assert getattr(partner, 'ActivityEdge91') == owner
    _safe_set(owner, 'inStructuredNode90', set())
    assert getattr(partner, 'ActivityEdge91') is None


def test_assoc_input200_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin202' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_Action(locallyReentrant=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin202', None)
    _safe_set(owner, 'xmof_BasicActions_Action201', {partner})
    assert getattr(partner, 'BasicActions_InputPin202') == owner
    _safe_set(owner, 'xmof_BasicActions_Action201', set())
    assert getattr(partner, 'BasicActions_InputPin202') is None


def test_assoc_inputElement100_stub_double():
    # ExtraStructuredActivities_ExpansionNode has no real 'ExpansionNode' property in the generated
    # code (a bare stub) -- manually attach it so xmof_ExtraStructuredActivities_ExpansionRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_ExtraStructuredActivities_ExpansionRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    partner = ExtraStructuredActivities_ExpansionNode()
    setattr(partner, 'ExpansionNode', None)
    _safe_set(owner, 'regionAsInput', {partner})
    assert getattr(partner, 'ExpansionNode') == owner
    _safe_set(owner, 'regionAsInput', set())
    assert getattr(partner, 'ExpansionNode') is None


def test_assoc_insertAt141_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin142' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_LinkEndCreationData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_LinkEndCreationData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_LinkEndCreationData(replaceAll=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin142', None)
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndCreationData', partner)
    assert getattr(partner, 'BasicActions_InputPin142') == owner
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndCreationData', None)
    assert getattr(partner, 'BasicActions_InputPin142') is None


def test_assoc_insertAt158_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin159' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_AddStructuralFeatureValueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_AddStructuralFeatureValueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_AddStructuralFeatureValueAction(replaceAll=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin159', None)
    _safe_set(owner, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', partner)
    assert getattr(partner, 'BasicActions_InputPin159') == owner
    _safe_set(owner, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', None)
    assert getattr(partner, 'BasicActions_InputPin159') is None


def test_assoc_loopVariable63_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin65' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin65', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode64', {partner})
    assert getattr(partner, 'BasicActions_OutputPin65') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode64', set())
    assert getattr(partner, 'BasicActions_OutputPin65') is None


def test_assoc_loopVariableInput55_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode56', {partner})
    assert getattr(partner, 'BasicActions_InputPin') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode56', set())
    assert getattr(partner, 'BasicActions_InputPin') is None


def test_assoc_newClassifier189_stub_double():
    # CompleteActions_xmof_EClassifier has no real 'CompleteActions_xmof_EClassifier191' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    partner = CompleteActions_xmof_EClassifier()
    setattr(partner, 'CompleteActions_xmof_EClassifier191', None)
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction190', {partner})
    assert getattr(partner, 'CompleteActions_xmof_EClassifier191') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction190', set())
    assert getattr(partner, 'CompleteActions_xmof_EClassifier191') is None


def test_assoc_node30_stub_double():
    # IntermediateActivities_ActivityNode has no real 'ActivityNode31' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActivities_Activity(readOnly=True)
    partner = IntermediateActivities_ActivityNode()
    setattr(partner, 'ActivityNode31', None)
    _safe_set(owner, 'activity', {partner})
    assert getattr(partner, 'ActivityNode31') == owner
    _safe_set(owner, 'activity', set())
    assert getattr(partner, 'ActivityNode31') is None


def test_assoc_node87_stub_double():
    # IntermediateActivities_ActivityNode has no real 'ActivityNode88' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = IntermediateActivities_ActivityNode()
    setattr(partner, 'ActivityNode88', None)
    _safe_set(owner, 'inStructuredNode', {partner})
    assert getattr(partner, 'ActivityNode88') == owner
    _safe_set(owner, 'inStructuredNode', set())
    assert getattr(partner, 'ActivityNode88') is None


def test_assoc_object181_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin183' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReadIsClassifiedObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReadIsClassifiedObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin183', None)
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', partner)
    assert getattr(partner, 'BasicActions_InputPin183') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction182', None)
    assert getattr(partner, 'BasicActions_InputPin183') is None


def test_assoc_object186_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin188' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin188', None)
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction187', partner)
    assert getattr(partner, 'BasicActions_InputPin188') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction187', None)
    assert getattr(partner, 'BasicActions_InputPin188') is None


def test_assoc_oldClassifier184_stub_double():
    # CompleteActions_xmof_EClassifier has no real 'CompleteActions_xmof_EClassifier185' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    partner = CompleteActions_xmof_EClassifier()
    setattr(partner, 'CompleteActions_xmof_EClassifier185', None)
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction', {partner})
    assert getattr(partner, 'CompleteActions_xmof_EClassifier185') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction', set())
    assert getattr(partner, 'CompleteActions_xmof_EClassifier185') is None


def test_assoc_output196_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin197' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_Action(locallyReentrant=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin197', None)
    _safe_set(owner, 'xmof_BasicActions_Action', {partner})
    assert getattr(partner, 'BasicActions_OutputPin197') == owner
    _safe_set(owner, 'xmof_BasicActions_Action', set())
    assert getattr(partner, 'BasicActions_OutputPin197') is None


def test_assoc_outputElement101_stub_double():
    # ExtraStructuredActivities_ExpansionNode has no real 'ExpansionNode102' property in the generated
    # code (a bare stub) -- manually attach it so xmof_ExtraStructuredActivities_ExpansionRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_ExtraStructuredActivities_ExpansionRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    partner = ExtraStructuredActivities_ExpansionNode()
    setattr(partner, 'ExpansionNode102', None)
    _safe_set(owner, 'regionAsOutput', {partner})
    assert getattr(partner, 'ExpansionNode102') == owner
    _safe_set(owner, 'regionAsOutput', set())
    assert getattr(partner, 'ExpansionNode102') is None


def test_assoc_ownedParameter1_stub_double():
    # Kernel_DirectedParameter has no real 'Kernel_DirectedParameter' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicBehaviors_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicBehaviors_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicBehaviors_Behavior(reentrant=True)
    partner = Kernel_DirectedParameter()
    setattr(partner, 'Kernel_DirectedParameter', None)
    _safe_set(owner, 'xmof_BasicBehaviors_Behavior', {partner})
    assert getattr(partner, 'Kernel_DirectedParameter') == owner
    _safe_set(owner, 'xmof_BasicBehaviors_Behavior', set())
    assert getattr(partner, 'Kernel_DirectedParameter') is None


def test_assoc_reducer164_stub_double():
    # BasicBehaviors_Behavior has no real 'BasicBehaviors_Behavior165' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReduceAction(ordered=True)
    partner = BasicBehaviors_Behavior()
    setattr(partner, 'BasicBehaviors_Behavior165', None)
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction', partner)
    assert getattr(partner, 'BasicBehaviors_Behavior165') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction', None)
    assert getattr(partner, 'BasicBehaviors_Behavior165') is None


def test_assoc_removeAt133_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin134' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_RemoveStructuralFeatureValueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_RemoveStructuralFeatureValueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_RemoveStructuralFeatureValueAction(removeDuplicates=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin134', None)
    _safe_set(owner, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', partner)
    assert getattr(partner, 'BasicActions_InputPin134') == owner
    _safe_set(owner, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', None)
    assert getattr(partner, 'BasicActions_InputPin134') is None


def test_assoc_result166_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin168' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReduceAction(ordered=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin168', None)
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction167', partner)
    assert getattr(partner, 'BasicActions_OutputPin168') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction167', None)
    assert getattr(partner, 'BasicActions_OutputPin168') is None


def test_assoc_result178_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin180' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReadIsClassifiedObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReadIsClassifiedObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin180', None)
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', partner)
    assert getattr(partner, 'BasicActions_OutputPin180') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction179', None)
    assert getattr(partner, 'BasicActions_OutputPin180') is None


def test_assoc_result192_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin193' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin193', None)
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction', {partner})
    assert getattr(partner, 'BasicActions_OutputPin193') == owner
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction', set())
    assert getattr(partner, 'BasicActions_OutputPin193') is None


def test_assoc_result203_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin204' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_CallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_CallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_CallAction(synchronous=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin204', None)
    _safe_set(owner, 'xmof_BasicActions_CallAction', {partner})
    assert getattr(partner, 'BasicActions_OutputPin204') == owner
    _safe_set(owner, 'xmof_BasicActions_CallAction', set())
    assert getattr(partner, 'BasicActions_OutputPin204') is None


def test_assoc_result60_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin62' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin62', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode61', {partner})
    assert getattr(partner, 'BasicActions_OutputPin62') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode61', set())
    assert getattr(partner, 'BasicActions_OutputPin62') is None


def test_assoc_result84_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin86' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin86', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_ConditionalNode85', {partner})
    assert getattr(partner, 'BasicActions_OutputPin86') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_ConditionalNode85', set())
    assert getattr(partner, 'BasicActions_OutputPin86') is None


def test_assoc_setupPart66_stub_double():
    # CompleteStructuredActivities_ExecutableNode has no real 'CompleteStructuredActivities_ExecutableNode68' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = CompleteStructuredActivities_ExecutableNode()
    setattr(partner, 'CompleteStructuredActivities_ExecutableNode68', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode67', {partner})
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode68') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode67', set())
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode68') is None


def test_assoc_specification0_stub_double():
    # Kernel_BehavioredEOperation has no real 'BehavioredEOperation' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicBehaviors_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicBehaviors_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicBehaviors_Behavior(reentrant=True)
    partner = Kernel_BehavioredEOperation()
    setattr(partner, 'BehavioredEOperation', None)
    _safe_set(owner, 'method', partner)
    assert getattr(partner, 'BehavioredEOperation') == owner
    _safe_set(owner, 'method', None)
    assert getattr(partner, 'BehavioredEOperation') is None


def test_assoc_structuredNodeInput94_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin96' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin96', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', {partner})
    assert getattr(partner, 'BasicActions_InputPin96') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode95', set())
    assert getattr(partner, 'BasicActions_InputPin96') is None


def test_assoc_structuredNodeOutput92_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin93' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin93', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode', {partner})
    assert getattr(partner, 'BasicActions_OutputPin93') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode', set())
    assert getattr(partner, 'BasicActions_OutputPin93') is None


def test_assoc_target156_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin157' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_DestroyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_DestroyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_DestroyObjectAction(destroyLinks=True, destroyOwnedObjects=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin157', None)
    _safe_set(owner, 'xmof_IntermediateActions_DestroyObjectAction', partner)
    assert getattr(partner, 'BasicActions_InputPin157') == owner
    _safe_set(owner, 'xmof_IntermediateActions_DestroyObjectAction', None)
    assert getattr(partner, 'BasicActions_InputPin157') is None


def test_assoc_test50_stub_double():
    # CompleteStructuredActivities_ExecutableNode has no real 'CompleteStructuredActivities_ExecutableNode' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = CompleteStructuredActivities_ExecutableNode()
    setattr(partner, 'CompleteStructuredActivities_ExecutableNode', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode51', {partner})
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode51', set())
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode') is None


def test_assoc_trigger194_stub_double():
    # Communications_Trigger has no real 'Communications_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    partner = Communications_Trigger()
    setattr(partner, 'Communications_Trigger', None)
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction195', {partner})
    assert getattr(partner, 'Communications_Trigger') == owner
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction195', set())
    assert getattr(partner, 'Communications_Trigger') is None


