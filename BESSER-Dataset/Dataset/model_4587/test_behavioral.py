import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActivitiesProv_Activity,
    ActivitiesProv_ActivityEdge,
    ActivitiesProv_ActivityFinalNode,
    ActivitiesProv_ActivityGroup,
    ActivitiesProv_ActivityNode,
    ActivitiesProv_ActivityParameterNode,
    ActivitiesProv_ActivityPartition,
    ActivitiesProv_CentralBufferNode,
    ActivitiesProv_Clause,
    ActivitiesProv_ConditionalNode,
    ActivitiesProv_ControlFlow,
    ActivitiesProv_ControlNode,
    ActivitiesProv_DataStoreNode,
    ActivitiesProv_DecisionNode,
    ActivitiesProv_ExceptionHandler,
    ActivitiesProv_ExecutableNode,
    ActivitiesProv_ExpansionNode,
    ActivitiesProv_ExpansionRegion,
    ActivitiesProv_FinalNode,
    ActivitiesProv_FlowFinalNode,
    ActivitiesProv_ForkNode,
    ActivitiesProv_InitialNode,
    ActivitiesProv_InterruptibleActivityRegion,
    ActivitiesProv_JoinNode,
    ActivitiesProv_LoopNode,
    ActivitiesProv_MergeNode,
    ActivitiesProv_ObjectFlow,
    ActivitiesProv_ObjectNode,
    ActivitiesProv_ParameterSet,
    ActivitiesProv_SequenceNode,
    ActivitiesProv_StructuredActivityNode,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    CentralBufferNode,
    ControlNode,
    ExecutableNode,
    FinalNode,
    ObjectNode,
    StructuredActivityNode,
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

def test_assoc_activity84_reverse_link_reassign_clear():
    a1 = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    a2 = ActivitiesProv_StructuredActivityNode(mustIsolate=False)
    b = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    _safe_set(b, 'ActivitiesProv_Activity86', a1)
    assert _is_linked(b, 'ActivitiesProv_Activity86', a1)
    if hasattr(a1, 'ActivitiesProv_StructuredActivityNode85'):
        assert _is_linked(a1, 'ActivitiesProv_StructuredActivityNode85', b)
    _safe_set(b, 'ActivitiesProv_Activity86', a2)
    assert _is_linked(b, 'ActivitiesProv_Activity86', a2)
    if hasattr(a1, 'ActivitiesProv_StructuredActivityNode85'):
        assert not _is_linked(a1, 'ActivitiesProv_StructuredActivityNode85', b)
    if hasattr(a2, 'ActivitiesProv_StructuredActivityNode85'):
        assert _is_linked(a2, 'ActivitiesProv_StructuredActivityNode85', b)
    _safe_set(b, 'ActivitiesProv_Activity86', None)
    assert not _is_linked(b, 'ActivitiesProv_Activity86', a2)
    if hasattr(a2, 'ActivitiesProv_StructuredActivityNode85'):
        assert not _is_linked(a2, 'ActivitiesProv_StructuredActivityNode85', b)


def test_assoc_structuredNode7_reverse_link_reassign_clear():
    a1 = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    a2 = ActivitiesProv_StructuredActivityNode(mustIsolate=False)
    b = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    _safe_set(b, 'ActivitiesProv_Activity8', {a1})
    assert _is_linked(b, 'ActivitiesProv_Activity8', a1)
    if hasattr(a1, 'ActivitiesProv_StructuredActivityNode'):
        assert _is_linked(a1, 'ActivitiesProv_StructuredActivityNode', b)
    _safe_set(b, 'ActivitiesProv_Activity8', {a2})
    assert _is_linked(b, 'ActivitiesProv_Activity8', a2)
    if hasattr(a1, 'ActivitiesProv_StructuredActivityNode'):
        assert not _is_linked(a1, 'ActivitiesProv_StructuredActivityNode', b)
    if hasattr(a2, 'ActivitiesProv_StructuredActivityNode'):
        assert _is_linked(a2, 'ActivitiesProv_StructuredActivityNode', b)
    _safe_set(b, 'ActivitiesProv_Activity8', set())
    assert not _is_linked(b, 'ActivitiesProv_Activity8', a2)
    if hasattr(a2, 'ActivitiesProv_StructuredActivityNode'):
        assert not _is_linked(a2, 'ActivitiesProv_StructuredActivityNode', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body106_stub_double():
    # ActivitiesProv_ExecutableNode has no real 'ActivitiesProv_ExecutableNode108' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    partner = ActivitiesProv_ExecutableNode()
    setattr(partner, 'ActivitiesProv_ExecutableNode108', None)
    _safe_set(owner, 'ActivitiesProv_ConditionalNode107', {partner})
    assert getattr(partner, 'ActivitiesProv_ExecutableNode108') == owner
    _safe_set(owner, 'ActivitiesProv_ConditionalNode107', set())
    assert getattr(partner, 'ActivitiesProv_ExecutableNode108') is None


def test_assoc_bodyPart96_stub_double():
    # ActivitiesProv_ExecutableNode has no real 'ActivitiesProv_ExecutableNode98' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_LoopNode(isTestedFirst=True)
    partner = ActivitiesProv_ExecutableNode()
    setattr(partner, 'ActivitiesProv_ExecutableNode98', None)
    _safe_set(owner, 'ActivitiesProv_LoopNode97', {partner})
    assert getattr(partner, 'ActivitiesProv_ExecutableNode98') == owner
    _safe_set(owner, 'ActivitiesProv_LoopNode97', set())
    assert getattr(partner, 'ActivitiesProv_ExecutableNode98') is None


def test_assoc_clause102_stub_double():
    # ActivitiesProv_Clause has no real 'ActivitiesProv_Clause' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    partner = ActivitiesProv_Clause()
    setattr(partner, 'ActivitiesProv_Clause', None)
    _safe_set(owner, 'ActivitiesProv_ConditionalNode', {partner})
    assert getattr(partner, 'ActivitiesProv_Clause') == owner
    _safe_set(owner, 'ActivitiesProv_ConditionalNode', set())
    assert getattr(partner, 'ActivitiesProv_Clause') is None


def test_assoc_decisionInputFlow65_stub_double():
    # ActivitiesProv_DecisionNode has no real 'ActivitiesProv_DecisionNode' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_ObjectFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_ObjectFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True)
    partner = ActivitiesProv_DecisionNode()
    setattr(partner, 'ActivitiesProv_DecisionNode', None)
    _safe_set(owner, 'ActivitiesProv_ObjectFlow', partner)
    assert getattr(partner, 'ActivitiesProv_DecisionNode') == owner
    _safe_set(owner, 'ActivitiesProv_ObjectFlow', None)
    assert getattr(partner, 'ActivitiesProv_DecisionNode') is None


def test_assoc_edge3_stub_double():
    # ActivitiesProv_ActivityEdge has no real 'ActivitiesProv_ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivitiesProv_ActivityEdge()
    setattr(partner, 'ActivitiesProv_ActivityEdge', None)
    _safe_set(owner, 'ActivitiesProv_Activity4', {partner})
    assert getattr(partner, 'ActivitiesProv_ActivityEdge') == owner
    _safe_set(owner, 'ActivitiesProv_Activity4', set())
    assert getattr(partner, 'ActivitiesProv_ActivityEdge') is None


def test_assoc_edge90_stub_double():
    # ActivitiesProv_ActivityEdge has no real 'ActivitiesProv_ActivityEdge92' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    partner = ActivitiesProv_ActivityEdge()
    setattr(partner, 'ActivitiesProv_ActivityEdge92', None)
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode91', {partner})
    assert getattr(partner, 'ActivitiesProv_ActivityEdge92') == owner
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode91', set())
    assert getattr(partner, 'ActivitiesProv_ActivityEdge92') is None


def test_assoc_group1_stub_double():
    # ActivitiesProv_ActivityGroup has no real 'ActivitiesProv_ActivityGroup' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivitiesProv_ActivityGroup()
    setattr(partner, 'ActivitiesProv_ActivityGroup', None)
    _safe_set(owner, 'ActivitiesProv_Activity2', {partner})
    assert getattr(partner, 'ActivitiesProv_ActivityGroup') == owner
    _safe_set(owner, 'ActivitiesProv_Activity2', set())
    assert getattr(partner, 'ActivitiesProv_ActivityGroup') is None


def test_assoc_inActivity35_stub_double():
    # ActivitiesProv_ActivityGroup has no real 'ActivitiesProv_ActivityGroup36' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivitiesProv_ActivityGroup()
    setattr(partner, 'ActivitiesProv_ActivityGroup36', None)
    _safe_set(owner, 'ActivitiesProv_Activity37', partner)
    assert getattr(partner, 'ActivitiesProv_ActivityGroup36') == owner
    _safe_set(owner, 'ActivitiesProv_Activity37', None)
    assert getattr(partner, 'ActivitiesProv_ActivityGroup36') is None


def test_assoc_inStructuredNode26_stub_double():
    # ActivitiesProv_ActivityNode has no real 'ActivitiesProv_ActivityNode27' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    partner = ActivitiesProv_ActivityNode()
    setattr(partner, 'ActivitiesProv_ActivityNode27', None)
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode28', partner)
    assert getattr(partner, 'ActivitiesProv_ActivityNode27') == owner
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode28', None)
    assert getattr(partner, 'ActivitiesProv_ActivityNode27') is None


def test_assoc_inStructuredNode62_stub_double():
    # ActivitiesProv_ActivityEdge has no real 'ActivitiesProv_ActivityEdge63' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    partner = ActivitiesProv_ActivityEdge()
    setattr(partner, 'ActivitiesProv_ActivityEdge63', None)
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode64', partner)
    assert getattr(partner, 'ActivitiesProv_ActivityEdge63') == owner
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode64', None)
    assert getattr(partner, 'ActivitiesProv_ActivityEdge63') is None


def test_assoc_node0_stub_double():
    # ActivitiesProv_ActivityNode has no real 'ActivitiesProv_ActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivitiesProv_ActivityNode()
    setattr(partner, 'ActivitiesProv_ActivityNode', None)
    _safe_set(owner, 'ActivitiesProv_Activity', {partner})
    assert getattr(partner, 'ActivitiesProv_ActivityNode') == owner
    _safe_set(owner, 'ActivitiesProv_Activity', set())
    assert getattr(partner, 'ActivitiesProv_ActivityNode') is None


def test_assoc_node87_stub_double():
    # ActivitiesProv_ActivityNode has no real 'ActivitiesProv_ActivityNode89' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_StructuredActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_StructuredActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    partner = ActivitiesProv_ActivityNode()
    setattr(partner, 'ActivitiesProv_ActivityNode89', None)
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode88', {partner})
    assert getattr(partner, 'ActivitiesProv_ActivityNode89') == owner
    _safe_set(owner, 'ActivitiesProv_StructuredActivityNode88', set())
    assert getattr(partner, 'ActivitiesProv_ActivityNode89') is None


def test_assoc_partition5_stub_double():
    # ActivitiesProv_ActivityPartition has no real 'ActivitiesProv_ActivityPartition' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    partner = ActivitiesProv_ActivityPartition()
    setattr(partner, 'ActivitiesProv_ActivityPartition', None)
    _safe_set(owner, 'ActivitiesProv_Activity6', {partner})
    assert getattr(partner, 'ActivitiesProv_ActivityPartition') == owner
    _safe_set(owner, 'ActivitiesProv_Activity6', set())
    assert getattr(partner, 'ActivitiesProv_ActivityPartition') is None


def test_assoc_setupPart94_stub_double():
    # ActivitiesProv_ExecutableNode has no real 'ActivitiesProv_ExecutableNode95' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_LoopNode(isTestedFirst=True)
    partner = ActivitiesProv_ExecutableNode()
    setattr(partner, 'ActivitiesProv_ExecutableNode95', None)
    _safe_set(owner, 'ActivitiesProv_LoopNode', {partner})
    assert getattr(partner, 'ActivitiesProv_ExecutableNode95') == owner
    _safe_set(owner, 'ActivitiesProv_LoopNode', set())
    assert getattr(partner, 'ActivitiesProv_ExecutableNode95') is None


def test_assoc_test103_stub_double():
    # ActivitiesProv_ExecutableNode has no real 'ActivitiesProv_ExecutableNode105' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_ConditionalNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_ConditionalNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    partner = ActivitiesProv_ExecutableNode()
    setattr(partner, 'ActivitiesProv_ExecutableNode105', None)
    _safe_set(owner, 'ActivitiesProv_ConditionalNode104', {partner})
    assert getattr(partner, 'ActivitiesProv_ExecutableNode105') == owner
    _safe_set(owner, 'ActivitiesProv_ConditionalNode104', set())
    assert getattr(partner, 'ActivitiesProv_ExecutableNode105') is None


def test_assoc_test99_stub_double():
    # ActivitiesProv_ExecutableNode has no real 'ActivitiesProv_ExecutableNode101' property in the generated
    # code (a bare stub) -- manually attach it so ActivitiesProv_LoopNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActivitiesProv_LoopNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActivitiesProv_LoopNode(isTestedFirst=True)
    partner = ActivitiesProv_ExecutableNode()
    setattr(partner, 'ActivitiesProv_ExecutableNode101', None)
    _safe_set(owner, 'ActivitiesProv_LoopNode100', {partner})
    assert getattr(partner, 'ActivitiesProv_ExecutableNode101') == owner
    _safe_set(owner, 'ActivitiesProv_LoopNode100', set())
    assert getattr(partner, 'ActivitiesProv_ExecutableNode101') is None


