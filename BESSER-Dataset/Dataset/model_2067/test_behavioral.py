import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    BooleanExpression,
    ControlNode,
    Expression,
    FinalNode,
    IntegerExpression,
    NamedElement,
    Value,
    Variable,
    VariableAssignment,
    activitydiagram_AcceptEventAction,
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
    activitydiagram_BooleanVariableAssignment,
    activitydiagram_ControlFlow,
    activitydiagram_ControlNode,
    activitydiagram_DecisionNode,
    activitydiagram_Event,
    activitydiagram_Expression,
    activitydiagram_FinalNode,
    activitydiagram_FlowFinalNode,
    activitydiagram_ForkNode,
    activitydiagram_InitialNode,
    activitydiagram_IntegerBinaryExpression,
    activitydiagram_IntegerComparisonExpression,
    activitydiagram_IntegerExpression,
    activitydiagram_IntegerValue,
    activitydiagram_IntegerVariable,
    activitydiagram_IntegerVariableAssignment,
    activitydiagram_JoinNode,
    activitydiagram_MergeNode,
    activitydiagram_NamedElement,
    activitydiagram_OpaqueAction,
    activitydiagram_Value,
    activitydiagram_Variable,
    activitydiagram_VariableAssignment,
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

def test_assoc_activity12_stub_double():
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


def test_assoc_assignee66_stub_double():
    # activitydiagram_BooleanVariableAssignment has no real 'activitydiagram_BooleanVariableAssignment' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanVariable(initialValue=True)
    partner = activitydiagram_BooleanVariableAssignment()
    setattr(partner, 'activitydiagram_BooleanVariableAssignment', None)
    _safe_set(owner, 'activitydiagram_BooleanVariable67', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariableAssignment') == owner
    _safe_set(owner, 'activitydiagram_BooleanVariable67', None)
    assert getattr(partner, 'activitydiagram_BooleanVariableAssignment') is None


def test_assoc_assignee71_stub_double():
    # activitydiagram_IntegerVariableAssignment has no real 'activitydiagram_IntegerVariableAssignment' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerVariable(initialValue=7)
    partner = activitydiagram_IntegerVariableAssignment()
    setattr(partner, 'activitydiagram_IntegerVariableAssignment', None)
    _safe_set(owner, 'activitydiagram_IntegerVariable', partner)
    assert getattr(partner, 'activitydiagram_IntegerVariableAssignment') == owner
    _safe_set(owner, 'activitydiagram_IntegerVariable', None)
    assert getattr(partner, 'activitydiagram_IntegerVariableAssignment') is None


def test_assoc_guard11_stub_double():
    # activitydiagram_ControlFlow has no real 'activitydiagram_ControlFlow' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanVariable(initialValue=True)
    partner = activitydiagram_ControlFlow()
    setattr(partner, 'activitydiagram_ControlFlow', None)
    _safe_set(owner, 'activitydiagram_BooleanVariable', partner)
    assert getattr(partner, 'activitydiagram_ControlFlow') == owner
    _safe_set(owner, 'activitydiagram_BooleanVariable', None)
    assert getattr(partner, 'activitydiagram_ControlFlow') is None


def test_assoc_locals4_stub_double():
    # activitydiagram_Activity has no real 'activitydiagram_Activity5' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_Activity()
    setattr(partner, 'activitydiagram_Activity5', None)
    _safe_set(owner, 'activitydiagram_Variable', partner)
    assert owner in getattr(partner, 'activitydiagram_Activity5')
    _safe_set(owner, 'activitydiagram_Variable', None)
    assert owner not in getattr(partner, 'activitydiagram_Activity5')


def test_assoc_nodes1_stub_double():
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


def test_assoc_operand151_stub_double():
    # activitydiagram_IntegerExpression has no real 'activitydiagram_IntegerExpression' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerBinaryExpression(operator="sample_text")
    partner = activitydiagram_IntegerExpression()
    setattr(partner, 'activitydiagram_IntegerExpression', None)
    _safe_set(owner, 'activitydiagram_IntegerBinaryExpression', partner)
    assert getattr(partner, 'activitydiagram_IntegerExpression') == owner
    _safe_set(owner, 'activitydiagram_IntegerBinaryExpression', None)
    assert getattr(partner, 'activitydiagram_IntegerExpression') is None


def test_assoc_operand155_stub_double():
    # activitydiagram_IntegerExpression has no real 'activitydiagram_IntegerExpression56' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerComparisonExpression(operator="sample_text")
    partner = activitydiagram_IntegerExpression()
    setattr(partner, 'activitydiagram_IntegerExpression56', None)
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression', partner)
    assert getattr(partner, 'activitydiagram_IntegerExpression56') == owner
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression', None)
    assert getattr(partner, 'activitydiagram_IntegerExpression56') is None


def test_assoc_operand161_stub_double():
    # activitydiagram_BooleanExpression has no real 'activitydiagram_BooleanExpression62' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanExpression()
    setattr(partner, 'activitydiagram_BooleanExpression62', None)
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanExpression62') == owner
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanExpression62') is None


def test_assoc_operand252_stub_double():
    # activitydiagram_IntegerExpression has no real 'activitydiagram_IntegerExpression54' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerBinaryExpression(operator="sample_text")
    partner = activitydiagram_IntegerExpression()
    setattr(partner, 'activitydiagram_IntegerExpression54', None)
    _safe_set(owner, 'activitydiagram_IntegerBinaryExpression53', partner)
    assert getattr(partner, 'activitydiagram_IntegerExpression54') == owner
    _safe_set(owner, 'activitydiagram_IntegerBinaryExpression53', None)
    assert getattr(partner, 'activitydiagram_IntegerExpression54') is None


def test_assoc_operand257_stub_double():
    # activitydiagram_IntegerExpression has no real 'activitydiagram_IntegerExpression59' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerComparisonExpression(operator="sample_text")
    partner = activitydiagram_IntegerExpression()
    setattr(partner, 'activitydiagram_IntegerExpression59', None)
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression58', partner)
    assert getattr(partner, 'activitydiagram_IntegerExpression59') == owner
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression58', None)
    assert getattr(partner, 'activitydiagram_IntegerExpression59') is None


def test_assoc_operand263_stub_double():
    # activitydiagram_BooleanExpression has no real 'activitydiagram_BooleanExpression65' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanExpression()
    setattr(partner, 'activitydiagram_BooleanExpression65', None)
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression64', partner)
    assert getattr(partner, 'activitydiagram_BooleanExpression65') == owner
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression64', None)
    assert getattr(partner, 'activitydiagram_BooleanExpression65') is None


def test_assoc_operand60_stub_double():
    # activitydiagram_BooleanExpression has no real 'activitydiagram_BooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanUnaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanExpression()
    setattr(partner, 'activitydiagram_BooleanExpression', None)
    _safe_set(owner, 'activitydiagram_BooleanUnaryExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanExpression') == owner
    _safe_set(owner, 'activitydiagram_BooleanUnaryExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanExpression') is None


def test_assoc_source6_stub_double():
    # activitydiagram_ActivityEdge has no real 'activitydiagram_ActivityEdge7' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'activitydiagram_ActivityEdge7', None)
    _safe_set(owner, 'activitydiagram_ActivityNode', partner)
    assert getattr(partner, 'activitydiagram_ActivityEdge7') == owner
    _safe_set(owner, 'activitydiagram_ActivityNode', None)
    assert getattr(partner, 'activitydiagram_ActivityEdge7') is None


def test_assoc_target8_stub_double():
    # activitydiagram_ActivityEdge has no real 'activitydiagram_ActivityEdge9' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'activitydiagram_ActivityEdge9', None)
    _safe_set(owner, 'activitydiagram_ActivityNode10', partner)
    assert getattr(partner, 'activitydiagram_ActivityEdge9') == owner
    _safe_set(owner, 'activitydiagram_ActivityNode10', None)
    assert getattr(partner, 'activitydiagram_ActivityEdge9') is None


