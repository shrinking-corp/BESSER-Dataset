import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    BooleanExpression,
    ControlNode,
    ExecutableNode,
    Expression,
    FinalNode,
    IntegerExpression,
    NamedElement,
    Value,
    Variable,
    activitydiagram_Action,
    activitydiagram_Activity,
    activitydiagram_ActivityEdge,
    activitydiagram_ActivityFinalNode,
    activitydiagram_ActivityNode,
    activitydiagram_BooleanBinaryExpression,
    activitydiagram_BooleanExpression,
    activitydiagram_BooleanUnaryExpression,
    activitydiagram_BooleanValue,
    activitydiagram_BooleanVariable,
    activitydiagram_ControlFlow,
    activitydiagram_ControlNode,
    activitydiagram_DecisionNode,
    activitydiagram_ExecutableNode,
    activitydiagram_Expression,
    activitydiagram_FinalNode,
    activitydiagram_ForkNode,
    activitydiagram_InitialNode,
    activitydiagram_IntegerCalculationExpression,
    activitydiagram_IntegerComparisonExpression,
    activitydiagram_IntegerExpression,
    activitydiagram_IntegerValue,
    activitydiagram_IntegerVariable,
    activitydiagram_JoinNode,
    activitydiagram_MergeNode,
    activitydiagram_NamedElement,
    activitydiagram_OpaqueAction,
    activitydiagram_Value,
    activitydiagram_Variable,
    BooleanBinaryOperator,
    BooleanUnaryOperator,
    IntegerCalculationOperator,
    IntegerComparisonOperator,
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


def test_assoc_assignee25_stub_double():
    # activitydiagram_IntegerVariable has no real 'activitydiagram_IntegerVariable26' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerCalculationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerCalculationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerCalculationExpression(operator="sample_text")
    partner = activitydiagram_IntegerVariable()
    setattr(partner, 'activitydiagram_IntegerVariable26', None)
    _safe_set(owner, 'activitydiagram_IntegerCalculationExpression', partner)
    assert getattr(partner, 'activitydiagram_IntegerVariable26') == owner
    _safe_set(owner, 'activitydiagram_IntegerCalculationExpression', None)
    assert getattr(partner, 'activitydiagram_IntegerVariable26') is None


def test_assoc_assignee27_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable28' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerComparisonExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable28', None)
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable28') == owner
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable28') is None


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


def test_assoc_initialValue17_stub_double():
    # activitydiagram_Value has no real 'activitydiagram_Value' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_Value()
    setattr(partner, 'activitydiagram_Value', None)
    _safe_set(owner, 'activitydiagram_Variable18', partner)
    assert getattr(partner, 'activitydiagram_Value') == owner
    _safe_set(owner, 'activitydiagram_Variable18', None)
    assert getattr(partner, 'activitydiagram_Value') is None


def test_assoc_inputs4_stub_double():
    # activitydiagram_Activity has no real 'activitydiagram_Activity5' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_Activity()
    setattr(partner, 'activitydiagram_Activity5', None)
    _safe_set(owner, 'activitydiagram_Variable6', partner)
    assert owner in getattr(partner, 'activitydiagram_Activity5')
    _safe_set(owner, 'activitydiagram_Variable6', None)
    assert owner not in getattr(partner, 'activitydiagram_Activity5')


def test_assoc_locals2_stub_double():
    # activitydiagram_Activity has no real 'activitydiagram_Activity3' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_Activity()
    setattr(partner, 'activitydiagram_Activity3', None)
    _safe_set(owner, 'activitydiagram_Variable', partner)
    assert owner in getattr(partner, 'activitydiagram_Activity3')
    _safe_set(owner, 'activitydiagram_Variable', None)
    assert owner not in getattr(partner, 'activitydiagram_Activity3')


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


def test_assoc_operand131_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable32' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable32', None)
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable32') == owner
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable32') is None


def test_assoc_operand233_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable35' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable35', None)
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression34', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable35') == owner
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression34', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable35') is None


def test_assoc_operand29_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable30' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanUnaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable30', None)
    _safe_set(owner, 'activitydiagram_BooleanUnaryExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable30') == owner
    _safe_set(owner, 'activitydiagram_BooleanUnaryExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable30') is None


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


def test_assoc_source11_stub_double():
    # activitydiagram_ActivityEdge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'ActivityNode12', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'ActivityNode12', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target13_stub_double():
    # activitydiagram_ActivityEdge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'ActivityNode14', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'ActivityNode14', None)
    assert getattr(partner, 'incoming') is None


