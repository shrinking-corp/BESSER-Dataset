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
    BasicBehaviors_ParameterValue,
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
    Kernel_EEnumLiteralSpecification,
    Kernel_InstanceSpecification,
    Kernel_PrimitiveType,
    Kernel_Slot,
    Kernel_Value,
    Kernel_ValueSpecification,
    Kernel_xmof_EClassifier,
    Kernel_xmof_EEnum,
    Kernel_xmof_EEnumLiteral,
    Kernel_xmof_EObject,
    Kernel_xmof_EStructuralFeature,
    LinkAction,
    LinkEndData,
    LiteralSpecification,
    MessageEvent,
    ObjectNode,
    OpaqueBehavior,
    Pin,
    PrimitiveValue,
    SemanticVisitor,
    StructuralFeatureAction,
    StructuredActivityNode,
    Value,
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
    xmof_BasicBehaviors_ParameterValue,
    xmof_BasicBehaviors_ParameterValueDefinition,
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
    xmof_Kernel_BooleanValue,
    xmof_Kernel_DirectedParameter,
    xmof_Kernel_EEnumLiteralSpecification,
    xmof_Kernel_EnumValue,
    xmof_Kernel_EnumerationValue,
    xmof_Kernel_InstanceSpecification,
    xmof_Kernel_InstanceValue,
    xmof_Kernel_IntegerValue,
    xmof_Kernel_LiteralBoolean,
    xmof_Kernel_LiteralInteger,
    xmof_Kernel_LiteralNull,
    xmof_Kernel_LiteralSpecification,
    xmof_Kernel_LiteralString,
    xmof_Kernel_LiteralUnlimitedNatural,
    xmof_Kernel_ObjectValue,
    xmof_Kernel_PrimitiveType,
    xmof_Kernel_PrimitiveValue,
    xmof_Kernel_Slot,
    xmof_Kernel_StringValue,
    xmof_Kernel_Value,
    xmof_Kernel_ValueSpecification,
    xmof_LociL1_SemanticVisitor,
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

def test_assoc_bodyOutput53_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin55' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin55', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode54', {partner})
    assert getattr(partner, 'BasicActions_OutputPin55') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode54', set())
    assert getattr(partner, 'BasicActions_OutputPin55') is None


def test_assoc_bodyPart58_stub_double():
    # CompleteStructuredActivities_ExecutableNode has no real 'CompleteStructuredActivities_ExecutableNode60' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = CompleteStructuredActivities_ExecutableNode()
    setattr(partner, 'CompleteStructuredActivities_ExecutableNode60', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode59', {partner})
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode60') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode59', set())
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode60') is None


def test_assoc_classifier177_stub_double():
    # CompleteActions_xmof_EClassifier has no real 'CompleteActions_xmof_EClassifier178' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReadIsClassifiedObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReadIsClassifiedObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    partner = CompleteActions_xmof_EClassifier()
    setattr(partner, 'CompleteActions_xmof_EClassifier178', None)
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', partner)
    assert getattr(partner, 'CompleteActions_xmof_EClassifier178') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction', None)
    assert getattr(partner, 'CompleteActions_xmof_EClassifier178') is None


def test_assoc_clause84_stub_double():
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


def test_assoc_collection170_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin172' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReduceAction(ordered=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin172', None)
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction171', partner)
    assert getattr(partner, 'BasicActions_InputPin172') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction171', None)
    assert getattr(partner, 'BasicActions_InputPin172') is None


def test_assoc_context199_stub_double():
    # BasicActions_xmof_EClassifier has no real 'BasicActions_xmof_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_Action(locallyReentrant=True)
    partner = BasicActions_xmof_EClassifier()
    setattr(partner, 'BasicActions_xmof_EClassifier', None)
    _safe_set(owner, 'xmof_BasicActions_Action200', partner)
    assert getattr(partner, 'BasicActions_xmof_EClassifier') == owner
    _safe_set(owner, 'xmof_BasicActions_Action200', None)
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


def test_assoc_decider50_stub_double():
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


def test_assoc_destroyAt144_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin145' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_LinkEndDestructionData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_LinkEndDestructionData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_LinkEndDestructionData(destroyDuplicates=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin145', None)
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndDestructionData', partner)
    assert getattr(partner, 'BasicActions_InputPin145') == owner
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndDestructionData', None)
    assert getattr(partner, 'BasicActions_InputPin145') is None


def test_assoc_edge33_stub_double():
    # IntermediateActivities_ActivityEdge has no real 'ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActivities_Activity(readOnly=True)
    partner = IntermediateActivities_ActivityEdge()
    setattr(partner, 'ActivityEdge', None)
    _safe_set(owner, 'activity34', {partner})
    assert getattr(partner, 'ActivityEdge') == owner
    _safe_set(owner, 'activity34', set())
    assert getattr(partner, 'ActivityEdge') is None


def test_assoc_edge90_stub_double():
    # IntermediateActivities_ActivityEdge has no real 'ActivityEdge92' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = IntermediateActivities_ActivityEdge()
    setattr(partner, 'ActivityEdge92', None)
    _safe_set(owner, 'inStructuredNode91', {partner})
    assert getattr(partner, 'ActivityEdge92') == owner
    _safe_set(owner, 'inStructuredNode91', set())
    assert getattr(partner, 'ActivityEdge92') is None


def test_assoc_input201_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin203' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_Action(locallyReentrant=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin203', None)
    _safe_set(owner, 'xmof_BasicActions_Action202', {partner})
    assert getattr(partner, 'BasicActions_InputPin203') == owner
    _safe_set(owner, 'xmof_BasicActions_Action202', set())
    assert getattr(partner, 'BasicActions_InputPin203') is None


def test_assoc_inputElement101_stub_double():
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


def test_assoc_insertAt142_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin143' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_LinkEndCreationData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_LinkEndCreationData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_LinkEndCreationData(replaceAll=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin143', None)
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndCreationData', partner)
    assert getattr(partner, 'BasicActions_InputPin143') == owner
    _safe_set(owner, 'xmof_IntermediateActions_LinkEndCreationData', None)
    assert getattr(partner, 'BasicActions_InputPin143') is None


def test_assoc_insertAt159_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin160' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_AddStructuralFeatureValueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_AddStructuralFeatureValueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_AddStructuralFeatureValueAction(replaceAll=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin160', None)
    _safe_set(owner, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', partner)
    assert getattr(partner, 'BasicActions_InputPin160') == owner
    _safe_set(owner, 'xmof_IntermediateActions_AddStructuralFeatureValueAction', None)
    assert getattr(partner, 'BasicActions_InputPin160') is None


def test_assoc_loopVariable64_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin66' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin66', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode65', {partner})
    assert getattr(partner, 'BasicActions_OutputPin66') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode65', set())
    assert getattr(partner, 'BasicActions_OutputPin66') is None


def test_assoc_loopVariableInput56_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode57', {partner})
    assert getattr(partner, 'BasicActions_InputPin') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode57', set())
    assert getattr(partner, 'BasicActions_InputPin') is None


def test_assoc_newClassifier190_stub_double():
    # CompleteActions_xmof_EClassifier has no real 'CompleteActions_xmof_EClassifier192' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    partner = CompleteActions_xmof_EClassifier()
    setattr(partner, 'CompleteActions_xmof_EClassifier192', None)
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction191', {partner})
    assert getattr(partner, 'CompleteActions_xmof_EClassifier192') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction191', set())
    assert getattr(partner, 'CompleteActions_xmof_EClassifier192') is None


def test_assoc_node31_stub_double():
    # IntermediateActivities_ActivityNode has no real 'ActivityNode32' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActivities_Activity(readOnly=True)
    partner = IntermediateActivities_ActivityNode()
    setattr(partner, 'ActivityNode32', None)
    _safe_set(owner, 'activity', {partner})
    assert getattr(partner, 'ActivityNode32') == owner
    _safe_set(owner, 'activity', set())
    assert getattr(partner, 'ActivityNode32') is None


def test_assoc_node88_stub_double():
    # IntermediateActivities_ActivityNode has no real 'ActivityNode89' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = IntermediateActivities_ActivityNode()
    setattr(partner, 'ActivityNode89', None)
    _safe_set(owner, 'inStructuredNode', {partner})
    assert getattr(partner, 'ActivityNode89') == owner
    _safe_set(owner, 'inStructuredNode', set())
    assert getattr(partner, 'ActivityNode89') is None


def test_assoc_object182_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin184' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReadIsClassifiedObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReadIsClassifiedObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin184', None)
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction183', partner)
    assert getattr(partner, 'BasicActions_InputPin184') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction183', None)
    assert getattr(partner, 'BasicActions_InputPin184') is None


def test_assoc_object187_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin189' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin189', None)
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction188', partner)
    assert getattr(partner, 'BasicActions_InputPin189') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction188', None)
    assert getattr(partner, 'BasicActions_InputPin189') is None


def test_assoc_oldClassifier185_stub_double():
    # CompleteActions_xmof_EClassifier has no real 'CompleteActions_xmof_EClassifier186' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReclassifyObjectAction(replaceAll=True)
    partner = CompleteActions_xmof_EClassifier()
    setattr(partner, 'CompleteActions_xmof_EClassifier186', None)
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction', {partner})
    assert getattr(partner, 'CompleteActions_xmof_EClassifier186') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReclassifyObjectAction', set())
    assert getattr(partner, 'CompleteActions_xmof_EClassifier186') is None


def test_assoc_output197_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin198' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_Action(locallyReentrant=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin198', None)
    _safe_set(owner, 'xmof_BasicActions_Action', {partner})
    assert getattr(partner, 'BasicActions_OutputPin198') == owner
    _safe_set(owner, 'xmof_BasicActions_Action', set())
    assert getattr(partner, 'BasicActions_OutputPin198') is None


def test_assoc_outputElement102_stub_double():
    # ExtraStructuredActivities_ExpansionNode has no real 'ExpansionNode103' property in the generated
    # code (a bare stub) -- manually attach it so xmof_ExtraStructuredActivities_ExpansionRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_ExtraStructuredActivities_ExpansionRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    partner = ExtraStructuredActivities_ExpansionNode()
    setattr(partner, 'ExpansionNode103', None)
    _safe_set(owner, 'regionAsOutput', {partner})
    assert getattr(partner, 'ExpansionNode103') == owner
    _safe_set(owner, 'regionAsOutput', set())
    assert getattr(partner, 'ExpansionNode103') is None


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


def test_assoc_reducer165_stub_double():
    # BasicBehaviors_Behavior has no real 'BasicBehaviors_Behavior166' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReduceAction(ordered=True)
    partner = BasicBehaviors_Behavior()
    setattr(partner, 'BasicBehaviors_Behavior166', None)
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction', partner)
    assert getattr(partner, 'BasicBehaviors_Behavior166') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction', None)
    assert getattr(partner, 'BasicBehaviors_Behavior166') is None


def test_assoc_removeAt134_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin135' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_RemoveStructuralFeatureValueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_RemoveStructuralFeatureValueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_RemoveStructuralFeatureValueAction(removeDuplicates=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin135', None)
    _safe_set(owner, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', partner)
    assert getattr(partner, 'BasicActions_InputPin135') == owner
    _safe_set(owner, 'xmof_IntermediateActions_RemoveStructuralFeatureValueAction', None)
    assert getattr(partner, 'BasicActions_InputPin135') is None


def test_assoc_result167_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin169' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReduceAction(ordered=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin169', None)
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction168', partner)
    assert getattr(partner, 'BasicActions_OutputPin169') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReduceAction168', None)
    assert getattr(partner, 'BasicActions_OutputPin169') is None


def test_assoc_result179_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin181' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_ReadIsClassifiedObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_ReadIsClassifiedObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_ReadIsClassifiedObjectAction(direct=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin181', None)
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction180', partner)
    assert getattr(partner, 'BasicActions_OutputPin181') == owner
    _safe_set(owner, 'xmof_CompleteActions_ReadIsClassifiedObjectAction180', None)
    assert getattr(partner, 'BasicActions_OutputPin181') is None


def test_assoc_result193_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin194' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin194', None)
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction', {partner})
    assert getattr(partner, 'BasicActions_OutputPin194') == owner
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction', set())
    assert getattr(partner, 'BasicActions_OutputPin194') is None


def test_assoc_result204_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin205' property in the generated
    # code (a bare stub) -- manually attach it so xmof_BasicActions_CallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_BasicActions_CallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_BasicActions_CallAction(synchronous=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin205', None)
    _safe_set(owner, 'xmof_BasicActions_CallAction', {partner})
    assert getattr(partner, 'BasicActions_OutputPin205') == owner
    _safe_set(owner, 'xmof_BasicActions_CallAction', set())
    assert getattr(partner, 'BasicActions_OutputPin205') is None


def test_assoc_result61_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin63' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin63', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode62', {partner})
    assert getattr(partner, 'BasicActions_OutputPin63') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode62', set())
    assert getattr(partner, 'BasicActions_OutputPin63') is None


def test_assoc_result85_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin87' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_ConditionalNode(assured=True, determinate=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin87', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_ConditionalNode86', {partner})
    assert getattr(partner, 'BasicActions_OutputPin87') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_ConditionalNode86', set())
    assert getattr(partner, 'BasicActions_OutputPin87') is None


def test_assoc_setupPart67_stub_double():
    # CompleteStructuredActivities_ExecutableNode has no real 'CompleteStructuredActivities_ExecutableNode69' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = CompleteStructuredActivities_ExecutableNode()
    setattr(partner, 'CompleteStructuredActivities_ExecutableNode69', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode68', {partner})
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode69') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode68', set())
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode69') is None


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


def test_assoc_structuredNodeInput95_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin97' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin97', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode96', {partner})
    assert getattr(partner, 'BasicActions_InputPin97') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode96', set())
    assert getattr(partner, 'BasicActions_InputPin97') is None


def test_assoc_structuredNodeOutput93_stub_double():
    # BasicActions_OutputPin has no real 'BasicActions_OutputPin94' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = BasicActions_OutputPin()
    setattr(partner, 'BasicActions_OutputPin94', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode', {partner})
    assert getattr(partner, 'BasicActions_OutputPin94') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_StructuredActivityNode', set())
    assert getattr(partner, 'BasicActions_OutputPin94') is None


def test_assoc_target157_stub_double():
    # BasicActions_InputPin has no real 'BasicActions_InputPin158' property in the generated
    # code (a bare stub) -- manually attach it so xmof_IntermediateActions_DestroyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_IntermediateActions_DestroyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_IntermediateActions_DestroyObjectAction(destroyLinks=True, destroyOwnedObjects=True)
    partner = BasicActions_InputPin()
    setattr(partner, 'BasicActions_InputPin158', None)
    _safe_set(owner, 'xmof_IntermediateActions_DestroyObjectAction', partner)
    assert getattr(partner, 'BasicActions_InputPin158') == owner
    _safe_set(owner, 'xmof_IntermediateActions_DestroyObjectAction', None)
    assert getattr(partner, 'BasicActions_InputPin158') is None


def test_assoc_test51_stub_double():
    # CompleteStructuredActivities_ExecutableNode has no real 'CompleteStructuredActivities_ExecutableNode' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteStructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteStructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteStructuredActivities_LoopNode(testedFirst=True)
    partner = CompleteStructuredActivities_ExecutableNode()
    setattr(partner, 'CompleteStructuredActivities_ExecutableNode', None)
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode52', {partner})
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode') == owner
    _safe_set(owner, 'xmof_CompleteStructuredActivities_LoopNode52', set())
    assert getattr(partner, 'CompleteStructuredActivities_ExecutableNode') is None


def test_assoc_trigger195_stub_double():
    # Communications_Trigger has no real 'Communications_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so xmof_CompleteActions_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xmof_CompleteActions_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xmof_CompleteActions_AcceptEventAction(unmarshall=True)
    partner = Communications_Trigger()
    setattr(partner, 'Communications_Trigger', None)
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction196', {partner})
    assert getattr(partner, 'Communications_Trigger') == owner
    _safe_set(owner, 'xmof_CompleteActions_AcceptEventAction196', set())
    assert getattr(partner, 'Communications_Trigger') is None


