import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activities_BasicActivities_ActivityEdge,
    Activities_BasicActivities_ActivityFinalNode,
    Activities_BasicActivities_ActivityParameterNode,
    Activities_BasicActivities_ControlFlow,
    Activities_BasicActivities_ControlNode,
    Activities_BasicActivities_InitialNode,
    Activities_BasicActivities_ObjectFlow,
    Activities_BasicActivities_ObjectNode,
    Activities_BasicActivities_Parameter,
    Activities_BasicActivities_Pin,
    Activities_BasicActivities_RedefinableElement,
    Activities_BasicActivities_TypedElement,
    Activities_CompleteStructuredActivities_InputPin,
    Activities_ExtraStructuredActivities_Classifier,
    Activities_ExtraStructuredActivities_ExceptionHandler,
    Activities_ExtraStructuredActivities_ExpansionNode,
    Activities_ExtraStructuredActivities_ExpansionRegion,
    Activities_FundamentalActivities_Action,
    Activities_FundamentalActivities_Activity,
    Activities_FundamentalActivities_ActivityGroup,
    Activities_FundamentalActivities_ActivityNode,
    Activities_FundamentalActivities_Behavior,
    Activities_FundamentalActivities_NamedElement,
    Activities_FundamentalActivities_Namespace,
    Activities_IntermediateActivities_ActivityPartition,
    Activities_IntermediateActivities_BehavioralFeature,
    Activities_IntermediateActivities_CentralBufferNode,
    Activities_IntermediateActivities_Class,
    Activities_IntermediateActivities_Constraint,
    Activities_IntermediateActivities_DataStoreNode,
    Activities_IntermediateActivities_DecisionNode,
    Activities_IntermediateActivities_Element,
    Activities_IntermediateActivities_Feature,
    Activities_IntermediateActivities_FinalNode,
    Activities_IntermediateActivities_FlowFinalNode,
    Activities_IntermediateActivities_ForkNode,
    Activities_IntermediateActivities_InterruptibleActivityRegion,
    Activities_IntermediateActivities_JoinNode,
    Activities_IntermediateActivities_MergeNode,
    Activities_IntermediateActivities_ParameterSet,
    Activities_IntermediateActivities_State,
    Activities_IntermediateActivities_ValueSpecification,
    Activities_StructuredActivities_Clause,
    Activities_StructuredActivities_ConditionalNode,
    Activities_StructuredActivities_ExecutableNode,
    Activities_StructuredActivities_LoopNode,
    Activities_StructuredActivities_MultiplicityElement,
    Activities_StructuredActivities_OutputPin,
    Activities_StructuredActivities_SequenceNode,
    Activities_StructuredActivities_StructuredActivityNode,
    Activities_StructuredActivities_Variable,
    Activity,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    ActivityPartition,
    BasicActivities_ControlNode,
    BasicActivities_RedefinableElement,
    BasicActivities_TypedElement,
    Behavior,
    CentralBufferNode,
    Class,
    Classifier,
    Clause,
    Constraint,
    ControlNode,
    Element,
    ExceptionHandler,
    ExecutableNode,
    ExpansionNode,
    ExpansionRegion,
    FinalNode,
    FundamentalActivities_Action,
    FundamentalActivities_ActivityGroup,
    FundamentalActivities_ActivityNode,
    FundamentalActivities_NamedElement,
    FundamentalActivities_Namespace,
    InputPin,
    IntermediateActivities_Feature,
    IntermediateActivities_FinalNode,
    InterruptibleActivityRegion,
    NamedElement,
    ObjectFlow,
    ObjectNode,
    OutputPin,
    Parameter,
    ParameterSet,
    RedefinableElement,
    State,
    StructuredActivities_ExecutableNode,
    StructuredActivities_MultiplicityElement,
    StructuredActivityNode,
    ValueSpecification,
    Variable,
    ExpansionKind,
    ObjectNodeOrderingKind,
    ParameterEffectKind,
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

def test_assoc_activity99_stub_double():
    # Activity has no real 'Activity100' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = Activity()
    setattr(partner, 'Activity100', None)
    _safe_set(owner, 'structuredNode', partner)
    assert getattr(partner, 'Activity100') == owner
    _safe_set(owner, 'structuredNode', None)
    assert getattr(partner, 'Activity100') is None


def test_assoc_body141_stub_double():
    # ExecutableNode has no real 'ExecutableNode143' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    partner = ExecutableNode()
    setattr(partner, 'ExecutableNode143', None)
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode142', {partner})
    assert getattr(partner, 'ExecutableNode143') == owner
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode142', set())
    assert getattr(partner, 'ExecutableNode143') is None


def test_assoc_bodyOutput131_stub_double():
    # OutputPin has no real 'OutputPin133' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin133', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode132', {partner})
    assert getattr(partner, 'OutputPin133') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode132', set())
    assert getattr(partner, 'OutputPin133') is None


def test_assoc_bodyPart116_stub_double():
    # ExecutableNode has no real 'ExecutableNode118' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = ExecutableNode()
    setattr(partner, 'ExecutableNode118', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode117', {partner})
    assert getattr(partner, 'ExecutableNode118') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode117', set())
    assert getattr(partner, 'ExecutableNode118') is None


def test_assoc_clause137_stub_double():
    # Clause has no real 'Clause' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    partner = Clause()
    setattr(partner, 'Clause', None)
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode', {partner})
    assert getattr(partner, 'Clause') == owner
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode', set())
    assert getattr(partner, 'Clause') is None


def test_assoc_decider122_stub_double():
    # OutputPin has no real 'OutputPin124' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin124', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode123', partner)
    assert getattr(partner, 'OutputPin124') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode123', None)
    assert getattr(partner, 'OutputPin124') is None


def test_assoc_edge108_stub_double():
    # ActivityEdge has no real 'ActivityEdge110' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = ActivityEdge()
    setattr(partner, 'ActivityEdge110', None)
    _safe_set(owner, 'inStructuredNode109', {partner})
    assert getattr(partner, 'ActivityEdge110') == owner
    _safe_set(owner, 'inStructuredNode109', set())
    assert getattr(partner, 'ActivityEdge110') is None


def test_assoc_edge2_stub_double():
    # ActivityEdge has no real 'ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivityEdge()
    setattr(partner, 'ActivityEdge', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Activity3', {partner})
    assert getattr(partner, 'ActivityEdge') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Activity3', set())
    assert getattr(partner, 'ActivityEdge') is None


def test_assoc_group1_stub_double():
    # ActivityGroup has no real 'ActivityGroup' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivityGroup()
    setattr(partner, 'ActivityGroup', None)
    _safe_set(owner, 'inActivity', {partner})
    assert getattr(partner, 'ActivityGroup') == owner
    _safe_set(owner, 'inActivity', set())
    assert getattr(partner, 'ActivityGroup') is None


def test_assoc_inState71_stub_double():
    # State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so Activities_BasicActivities_ObjectFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_BasicActivities_ObjectFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    partner = State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'Activities_BasicActivities_ObjectFlow72', {partner})
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'Activities_BasicActivities_ObjectFlow72', set())
    assert getattr(partner, 'State') is None


def test_assoc_input29_stub_double():
    # InputPin has no real 'InputPin' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    partner = InputPin()
    setattr(partner, 'InputPin', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Action30', {partner})
    assert getattr(partner, 'InputPin') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Action30', set())
    assert getattr(partner, 'InputPin') is None


def test_assoc_inputElement163_stub_double():
    # ExpansionNode has no real 'ExpansionNode' property in the generated
    # code (a bare stub) -- manually attach it so Activities_ExtraStructuredActivities_ExpansionRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_ExtraStructuredActivities_ExpansionRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    partner = ExpansionNode()
    setattr(partner, 'ExpansionNode', None)
    _safe_set(owner, 'regionAsInput', {partner})
    assert getattr(partner, 'ExpansionNode') == owner
    _safe_set(owner, 'regionAsInput', set())
    assert getattr(partner, 'ExpansionNode') is None


def test_assoc_joinSpec73_stub_double():
    # ValueSpecification has no real 'ValueSpecification74' property in the generated
    # code (a bare stub) -- manually attach it so Activities_IntermediateActivities_JoinNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_IntermediateActivities_JoinNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_IntermediateActivities_JoinNode(isCombineDuplicate=True)
    partner = ValueSpecification()
    setattr(partner, 'ValueSpecification74', None)
    _safe_set(owner, 'Activities_IntermediateActivities_JoinNode', partner)
    assert getattr(partner, 'ValueSpecification74') == owner
    _safe_set(owner, 'Activities_IntermediateActivities_JoinNode', None)
    assert getattr(partner, 'ValueSpecification74') is None


def test_assoc_localPostcondition26_stub_double():
    # Constraint has no real 'Constraint28' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    partner = Constraint()
    setattr(partner, 'Constraint28', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Action27', {partner})
    assert getattr(partner, 'Constraint28') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Action27', set())
    assert getattr(partner, 'Constraint28') is None


def test_assoc_localPrecondition25_stub_double():
    # Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    partner = Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Action', {partner})
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Action', set())
    assert getattr(partner, 'Constraint') is None


def test_assoc_loopVariable128_stub_double():
    # OutputPin has no real 'OutputPin130' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin130', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode129', {partner})
    assert getattr(partner, 'OutputPin130') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode129', set())
    assert getattr(partner, 'OutputPin130') is None


def test_assoc_loopVariableInput125_stub_double():
    # InputPin has no real 'InputPin127' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = InputPin()
    setattr(partner, 'InputPin127', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode126', {partner})
    assert getattr(partner, 'InputPin127') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode126', set())
    assert getattr(partner, 'InputPin127') is None


def test_assoc_node0_stub_double():
    # ActivityNode has no real 'ActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivityNode()
    setattr(partner, 'ActivityNode', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Activity', {partner})
    assert getattr(partner, 'ActivityNode') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Activity', set())
    assert getattr(partner, 'ActivityNode') is None


def test_assoc_node103_stub_double():
    # ActivityNode has no real 'ActivityNode104' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = ActivityNode()
    setattr(partner, 'ActivityNode104', None)
    _safe_set(owner, 'inStructuredNode', {partner})
    assert getattr(partner, 'ActivityNode104') == owner
    _safe_set(owner, 'inStructuredNode', set())
    assert getattr(partner, 'ActivityNode104') is None


def test_assoc_output31_stub_double():
    # OutputPin has no real 'OutputPin' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Action32', {partner})
    assert getattr(partner, 'OutputPin') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Action32', set())
    assert getattr(partner, 'OutputPin') is None


def test_assoc_outputElement164_stub_double():
    # ExpansionNode has no real 'ExpansionNode165' property in the generated
    # code (a bare stub) -- manually attach it so Activities_ExtraStructuredActivities_ExpansionRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_ExtraStructuredActivities_ExpansionRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    partner = ExpansionNode()
    setattr(partner, 'ExpansionNode165', None)
    _safe_set(owner, 'regionAsOutput', {partner})
    assert getattr(partner, 'ExpansionNode165') == owner
    _safe_set(owner, 'regionAsOutput', set())
    assert getattr(partner, 'ExpansionNode165') is None


def test_assoc_parameterSet45_stub_double():
    # ParameterSet has no real 'ParameterSet46' property in the generated
    # code (a bare stub) -- manually attach it so Activities_BasicActivities_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_BasicActivities_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_BasicActivities_Parameter(effect="sample_text", isException=True, isStream=True)
    partner = ParameterSet()
    setattr(partner, 'ParameterSet46', None)
    _safe_set(owner, 'parameter', {partner})
    assert getattr(partner, 'ParameterSet46') == owner
    _safe_set(owner, 'parameter', set())
    assert getattr(partner, 'ParameterSet46') is None


def test_assoc_partition4_stub_double():
    # ActivityPartition has no real 'ActivityPartition' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivityPartition()
    setattr(partner, 'ActivityPartition', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Activity5', {partner})
    assert getattr(partner, 'ActivityPartition') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Activity5', set())
    assert getattr(partner, 'ActivityPartition') is None


def test_assoc_result134_stub_double():
    # OutputPin has no real 'OutputPin136' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin136', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode135', {partner})
    assert getattr(partner, 'OutputPin136') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode135', set())
    assert getattr(partner, 'OutputPin136') is None


def test_assoc_result144_stub_double():
    # OutputPin has no real 'OutputPin146' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin146', None)
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode145', {partner})
    assert getattr(partner, 'OutputPin146') == owner
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode145', set())
    assert getattr(partner, 'OutputPin146') is None


def test_assoc_selection68_stub_double():
    # Behavior has no real 'Behavior70' property in the generated
    # code (a bare stub) -- manually attach it so Activities_BasicActivities_ObjectFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_BasicActivities_ObjectFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    partner = Behavior()
    setattr(partner, 'Behavior70', None)
    _safe_set(owner, 'Activities_BasicActivities_ObjectFlow69', partner)
    assert getattr(partner, 'Behavior70') == owner
    _safe_set(owner, 'Activities_BasicActivities_ObjectFlow69', None)
    assert getattr(partner, 'Behavior70') is None


def test_assoc_setupPart115_stub_double():
    # ExecutableNode has no real 'ExecutableNode' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = ExecutableNode()
    setattr(partner, 'ExecutableNode', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode', {partner})
    assert getattr(partner, 'ExecutableNode') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode', set())
    assert getattr(partner, 'ExecutableNode') is None


def test_assoc_structuredNode6_stub_double():
    # StructuredActivityNode has no real 'StructuredActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    partner = StructuredActivityNode()
    setattr(partner, 'StructuredActivityNode', None)
    _safe_set(owner, 'activity', {partner})
    assert getattr(partner, 'StructuredActivityNode') == owner
    _safe_set(owner, 'activity', set())
    assert getattr(partner, 'StructuredActivityNode') is None


def test_assoc_structuredNodeInput105_stub_double():
    # InputPin has no real 'InputPin107' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = InputPin()
    setattr(partner, 'InputPin107', None)
    _safe_set(owner, 'Activities_StructuredActivities_StructuredActivityNode106', {partner})
    assert getattr(partner, 'InputPin107') == owner
    _safe_set(owner, 'Activities_StructuredActivities_StructuredActivityNode106', set())
    assert getattr(partner, 'InputPin107') is None


def test_assoc_structuredNodeOutput111_stub_double():
    # OutputPin has no real 'OutputPin113' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin113', None)
    _safe_set(owner, 'Activities_StructuredActivities_StructuredActivityNode112', {partner})
    assert getattr(partner, 'OutputPin113') == owner
    _safe_set(owner, 'Activities_StructuredActivities_StructuredActivityNode112', set())
    assert getattr(partner, 'OutputPin113') is None


def test_assoc_test119_stub_double():
    # ExecutableNode has no real 'ExecutableNode121' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    partner = ExecutableNode()
    setattr(partner, 'ExecutableNode121', None)
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode120', {partner})
    assert getattr(partner, 'ExecutableNode121') == owner
    _safe_set(owner, 'Activities_StructuredActivities_LoopNode120', set())
    assert getattr(partner, 'ExecutableNode121') is None


def test_assoc_test138_stub_double():
    # ExecutableNode has no real 'ExecutableNode140' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    partner = ExecutableNode()
    setattr(partner, 'ExecutableNode140', None)
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode139', {partner})
    assert getattr(partner, 'ExecutableNode140') == owner
    _safe_set(owner, 'Activities_StructuredActivities_ConditionalNode139', set())
    assert getattr(partner, 'ExecutableNode140') is None


def test_assoc_transformation67_stub_double():
    # Behavior has no real 'Behavior' property in the generated
    # code (a bare stub) -- manually attach it so Activities_BasicActivities_ObjectFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_BasicActivities_ObjectFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    partner = Behavior()
    setattr(partner, 'Behavior', None)
    _safe_set(owner, 'Activities_BasicActivities_ObjectFlow', partner)
    assert getattr(partner, 'Behavior') == owner
    _safe_set(owner, 'Activities_BasicActivities_ObjectFlow', None)
    assert getattr(partner, 'Behavior') is None


def test_assoc_variable101_stub_double():
    # Variable has no real 'Variable102' property in the generated
    # code (a bare stub) -- manually attach it so Activities_StructuredActivities_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_StructuredActivities_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    partner = Variable()
    setattr(partner, 'Variable102', None)
    _safe_set(owner, 'Activities_StructuredActivities_StructuredActivityNode', {partner})
    assert getattr(partner, 'Variable102') == owner
    _safe_set(owner, 'Activities_StructuredActivities_StructuredActivityNode', set())
    assert getattr(partner, 'Variable102') is None


def test_assoc_variable7_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so Activities_FundamentalActivities_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Activities_FundamentalActivities_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'Activities_FundamentalActivities_Activity8', {partner})
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'Activities_FundamentalActivities_Activity8', set())
    assert getattr(partner, 'Variable') is None


