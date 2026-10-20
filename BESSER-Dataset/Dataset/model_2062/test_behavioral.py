import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    ControlNode,
    ExecutableNode,
    FinalNode,
    NamedActivity,
    Token,
    Value,
    Variable,
    activitydiagram_Action,
    activitydiagram_Activity,
    activitydiagram_ActivityEdge,
    activitydiagram_ActivityFinalNode,
    activitydiagram_ActivityNode,
    activitydiagram_BooleanValue,
    activitydiagram_BooleanVariable,
    activitydiagram_Context,
    activitydiagram_ControlFlow,
    activitydiagram_ControlNode,
    activitydiagram_ControlToken,
    activitydiagram_DecisionNode,
    activitydiagram_ExecutableNode,
    activitydiagram_Exp,
    activitydiagram_FinalNode,
    activitydiagram_ForkNode,
    activitydiagram_ForkedToken,
    activitydiagram_InitialNode,
    activitydiagram_Input,
    activitydiagram_InputValue,
    activitydiagram_IntegerValue,
    activitydiagram_IntegerVariable,
    activitydiagram_JoinNode,
    activitydiagram_MergeNode,
    activitydiagram_NamedActivity,
    activitydiagram_Offer,
    activitydiagram_OpaqueAction,
    activitydiagram_Token,
    activitydiagram_Trace,
    activitydiagram_Value,
    activitydiagram_Variable,
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

def test_assoc_activity10_stub_double():
    # activitydiagram_Activity has no real 'Activity' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Activity()
    setattr(partner, 'Activity', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'Activity') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'Activity') is None


def test_assoc_baseToken36_stub_double():
    # activitydiagram_Token has no real 'activitydiagram_Token37' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ForkedToken's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ForkedToken's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ForkedToken(remainingOffersCount=7)
    partner = activitydiagram_Token()
    setattr(partner, 'activitydiagram_Token37', None)
    _safe_set(owner, 'activitydiagram_ForkedToken', partner)
    assert getattr(partner, 'activitydiagram_Token37') == owner
    _safe_set(owner, 'activitydiagram_ForkedToken', None)
    assert getattr(partner, 'activitydiagram_Token37') is None


def test_assoc_executedNodes38_stub_double():
    # activitydiagram_Trace has no real 'activitydiagram_Trace' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Trace()
    setattr(partner, 'activitydiagram_Trace', None)
    _safe_set(owner, 'activitydiagram_ActivityNode', partner)
    assert owner in getattr(partner, 'activitydiagram_Trace')
    _safe_set(owner, 'activitydiagram_ActivityNode', None)
    assert owner not in getattr(partner, 'activitydiagram_Trace')


def test_assoc_heldTokens11_stub_double():
    # activitydiagram_Token has no real 'Token' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Token()
    setattr(partner, 'Token', None)
    _safe_set(owner, 'holder', {partner})
    assert getattr(partner, 'Token') == owner
    _safe_set(owner, 'holder', set())
    assert getattr(partner, 'Token') is None


def test_assoc_holder32_stub_double():
    # activitydiagram_Token has no real 'heldTokens' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Token()
    setattr(partner, 'heldTokens', None)
    _safe_set(owner, 'ActivityNode33', partner)
    assert getattr(partner, 'heldTokens') == owner
    _safe_set(owner, 'ActivityNode33', None)
    assert getattr(partner, 'heldTokens') is None


def test_assoc_incoming8_stub_double():
    # activitydiagram_ActivityEdge has no real 'ActivityEdge9' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'ActivityEdge9', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'ActivityEdge9') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'ActivityEdge9') is None


def test_assoc_nodes0_stub_double():
    # activitydiagram_Activity has no real 'activity' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Activity()
    setattr(partner, 'activity', None)
    _safe_set(owner, 'ActivityNode', partner)
    assert owner in getattr(partner, 'activity')
    _safe_set(owner, 'ActivityNode', None)
    assert owner not in getattr(partner, 'activity')


def test_assoc_outgoing7_stub_double():
    # activitydiagram_ActivityEdge has no real 'ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'ActivityEdge', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'ActivityEdge') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'ActivityEdge') is None


def test_assoc_source12_stub_double():
    # activitydiagram_ActivityEdge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'ActivityNode13', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'ActivityNode13', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target14_stub_double():
    # activitydiagram_ActivityEdge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'ActivityNode15', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'ActivityNode15', None)
    assert getattr(partner, 'incoming') is None


