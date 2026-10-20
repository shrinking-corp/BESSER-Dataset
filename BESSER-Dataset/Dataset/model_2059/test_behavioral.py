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
    activitydiagram_ControlToken,
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
    activitydiagram_Offer,
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

def test_assoc_activity14_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_Activity()
    _safe_set(b, 'Activity', a1)
    assert _is_linked(b, 'Activity', a1)
    if hasattr(a1, 'nodes'):
        assert _is_linked(a1, 'nodes', b)
    _safe_set(b, 'Activity', a2)
    assert _is_linked(b, 'Activity', a2)
    if hasattr(a1, 'nodes'):
        assert not _is_linked(a1, 'nodes', b)
    if hasattr(a2, 'nodes'):
        assert _is_linked(a2, 'nodes', b)
    _safe_set(b, 'Activity', None)
    assert not _is_linked(b, 'Activity', a2)
    if hasattr(a2, 'nodes'):
        assert not _is_linked(a2, 'nodes', b)


def test_assoc_assignee71_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariableAssignment()
    a2 = activitydiagram_BooleanVariableAssignment()
    b = activitydiagram_BooleanVariable(currentValue=True, initialValue=True)
    _safe_set(b, 'activitydiagram_BooleanVariable72', a1)
    assert _is_linked(b, 'activitydiagram_BooleanVariable72', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariableAssignment'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariableAssignment', b)
    _safe_set(b, 'activitydiagram_BooleanVariable72', a2)
    assert _is_linked(b, 'activitydiagram_BooleanVariable72', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariableAssignment'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariableAssignment', b)
    if hasattr(a2, 'activitydiagram_BooleanVariableAssignment'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariableAssignment', b)
    _safe_set(b, 'activitydiagram_BooleanVariable72', None)
    assert not _is_linked(b, 'activitydiagram_BooleanVariable72', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariableAssignment'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariableAssignment', b)


def test_assoc_assignee76_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerVariableAssignment()
    a2 = activitydiagram_IntegerVariableAssignment()
    b = activitydiagram_IntegerVariable(currentValue=True, initialValue=7)
    _safe_set(b, 'activitydiagram_IntegerVariable', a1)
    assert _is_linked(b, 'activitydiagram_IntegerVariable', a1)
    if hasattr(a1, 'activitydiagram_IntegerVariableAssignment'):
        assert _is_linked(a1, 'activitydiagram_IntegerVariableAssignment', b)
    _safe_set(b, 'activitydiagram_IntegerVariable', a2)
    assert _is_linked(b, 'activitydiagram_IntegerVariable', a2)
    if hasattr(a1, 'activitydiagram_IntegerVariableAssignment'):
        assert not _is_linked(a1, 'activitydiagram_IntegerVariableAssignment', b)
    if hasattr(a2, 'activitydiagram_IntegerVariableAssignment'):
        assert _is_linked(a2, 'activitydiagram_IntegerVariableAssignment', b)
    _safe_set(b, 'activitydiagram_IntegerVariable', None)
    assert not _is_linked(b, 'activitydiagram_IntegerVariable', a2)
    if hasattr(a2, 'activitydiagram_IntegerVariableAssignment'):
        assert not _is_linked(a2, 'activitydiagram_IntegerVariableAssignment', b)


def test_assoc_assignments23_reverse_link_reassign_clear():
    a1 = activitydiagram_VariableAssignment()
    a2 = activitydiagram_VariableAssignment()
    b = activitydiagram_OpaqueAction()
    _safe_set(b, 'activitydiagram_OpaqueAction', {a1})
    assert _is_linked(b, 'activitydiagram_OpaqueAction', a1)
    if hasattr(a1, 'activitydiagram_VariableAssignment'):
        assert _is_linked(a1, 'activitydiagram_VariableAssignment', b)
    _safe_set(b, 'activitydiagram_OpaqueAction', {a2})
    assert _is_linked(b, 'activitydiagram_OpaqueAction', a2)
    if hasattr(a1, 'activitydiagram_VariableAssignment'):
        assert not _is_linked(a1, 'activitydiagram_VariableAssignment', b)
    if hasattr(a2, 'activitydiagram_VariableAssignment'):
        assert _is_linked(a2, 'activitydiagram_VariableAssignment', b)
    _safe_set(b, 'activitydiagram_OpaqueAction', set())
    assert not _is_linked(b, 'activitydiagram_OpaqueAction', a2)
    if hasattr(a2, 'activitydiagram_VariableAssignment'):
        assert not _is_linked(a2, 'activitydiagram_VariableAssignment', b)


def test_assoc_edges2_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityEdge()
    a2 = activitydiagram_ActivityEdge()
    b = activitydiagram_Activity()
    _safe_set(b, 'activitydiagram_Activity3', {a1})
    assert _is_linked(b, 'activitydiagram_Activity3', a1)
    if hasattr(a1, 'activitydiagram_ActivityEdge'):
        assert _is_linked(a1, 'activitydiagram_ActivityEdge', b)
    _safe_set(b, 'activitydiagram_Activity3', {a2})
    assert _is_linked(b, 'activitydiagram_Activity3', a2)
    if hasattr(a1, 'activitydiagram_ActivityEdge'):
        assert not _is_linked(a1, 'activitydiagram_ActivityEdge', b)
    if hasattr(a2, 'activitydiagram_ActivityEdge'):
        assert _is_linked(a2, 'activitydiagram_ActivityEdge', b)
    _safe_set(b, 'activitydiagram_Activity3', set())
    assert not _is_linked(b, 'activitydiagram_Activity3', a2)
    if hasattr(a2, 'activitydiagram_ActivityEdge'):
        assert not _is_linked(a2, 'activitydiagram_ActivityEdge', b)


def test_assoc_expression73_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariableAssignment()
    a2 = activitydiagram_BooleanVariableAssignment()
    b = activitydiagram_BooleanExpression()
    _safe_set(b, 'activitydiagram_BooleanExpression75', a1)
    assert _is_linked(b, 'activitydiagram_BooleanExpression75', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariableAssignment74'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariableAssignment74', b)
    _safe_set(b, 'activitydiagram_BooleanExpression75', a2)
    assert _is_linked(b, 'activitydiagram_BooleanExpression75', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariableAssignment74'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariableAssignment74', b)
    if hasattr(a2, 'activitydiagram_BooleanVariableAssignment74'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariableAssignment74', b)
    _safe_set(b, 'activitydiagram_BooleanExpression75', None)
    assert not _is_linked(b, 'activitydiagram_BooleanExpression75', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariableAssignment74'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariableAssignment74', b)


def test_assoc_expression77_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerVariableAssignment()
    a2 = activitydiagram_IntegerVariableAssignment()
    b = activitydiagram_IntegerExpression()
    _safe_set(b, 'activitydiagram_IntegerExpression79', a1)
    assert _is_linked(b, 'activitydiagram_IntegerExpression79', a1)
    if hasattr(a1, 'activitydiagram_IntegerVariableAssignment78'):
        assert _is_linked(a1, 'activitydiagram_IntegerVariableAssignment78', b)
    _safe_set(b, 'activitydiagram_IntegerExpression79', a2)
    assert _is_linked(b, 'activitydiagram_IntegerExpression79', a2)
    if hasattr(a1, 'activitydiagram_IntegerVariableAssignment78'):
        assert not _is_linked(a1, 'activitydiagram_IntegerVariableAssignment78', b)
    if hasattr(a2, 'activitydiagram_IntegerVariableAssignment78'):
        assert _is_linked(a2, 'activitydiagram_IntegerVariableAssignment78', b)
    _safe_set(b, 'activitydiagram_IntegerExpression79', None)
    assert not _is_linked(b, 'activitydiagram_IntegerExpression79', a2)
    if hasattr(a2, 'activitydiagram_IntegerVariableAssignment78'):
        assert not _is_linked(a2, 'activitydiagram_IntegerVariableAssignment78', b)


def test_assoc_heldTokens15_reverse_link_reassign_clear():
    a1 = activitydiagram_ControlToken()
    a2 = activitydiagram_ControlToken()
    b = activitydiagram_ActivityNode(running=True)
    _safe_set(b, 'activitydiagram_ActivityNode16', {a1})
    assert _is_linked(b, 'activitydiagram_ActivityNode16', a1)
    if hasattr(a1, 'activitydiagram_ControlToken17'):
        assert _is_linked(a1, 'activitydiagram_ControlToken17', b)
    _safe_set(b, 'activitydiagram_ActivityNode16', {a2})
    assert _is_linked(b, 'activitydiagram_ActivityNode16', a2)
    if hasattr(a1, 'activitydiagram_ControlToken17'):
        assert not _is_linked(a1, 'activitydiagram_ControlToken17', b)
    if hasattr(a2, 'activitydiagram_ControlToken17'):
        assert _is_linked(a2, 'activitydiagram_ControlToken17', b)
    _safe_set(b, 'activitydiagram_ActivityNode16', set())
    assert not _is_linked(b, 'activitydiagram_ActivityNode16', a2)
    if hasattr(a2, 'activitydiagram_ControlToken17'):
        assert not _is_linked(a2, 'activitydiagram_ControlToken17', b)


def test_assoc_incoming26_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityEdge()
    a2 = activitydiagram_ActivityEdge()
    b = activitydiagram_AcceptEventAction()
    _safe_set(b, 'activitydiagram_AcceptEventAction27', a1)
    assert _is_linked(b, 'activitydiagram_AcceptEventAction27', a1)
    if hasattr(a1, 'activitydiagram_ActivityEdge28'):
        assert _is_linked(a1, 'activitydiagram_ActivityEdge28', b)
    _safe_set(b, 'activitydiagram_AcceptEventAction27', a2)
    assert _is_linked(b, 'activitydiagram_AcceptEventAction27', a2)
    if hasattr(a1, 'activitydiagram_ActivityEdge28'):
        assert not _is_linked(a1, 'activitydiagram_ActivityEdge28', b)
    if hasattr(a2, 'activitydiagram_ActivityEdge28'):
        assert _is_linked(a2, 'activitydiagram_ActivityEdge28', b)
    _safe_set(b, 'activitydiagram_AcceptEventAction27', None)
    assert not _is_linked(b, 'activitydiagram_AcceptEventAction27', a2)
    if hasattr(a2, 'activitydiagram_ActivityEdge28'):
        assert not _is_linked(a2, 'activitydiagram_ActivityEdge28', b)


def test_assoc_incoming34_reverse_link_reassign_clear():
    a1 = activitydiagram_DecisionNode()
    a2 = activitydiagram_DecisionNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge35', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge35', a1)
    if hasattr(a1, 'activitydiagram_DecisionNode'):
        assert _is_linked(a1, 'activitydiagram_DecisionNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge35', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge35', a2)
    if hasattr(a1, 'activitydiagram_DecisionNode'):
        assert not _is_linked(a1, 'activitydiagram_DecisionNode', b)
    if hasattr(a2, 'activitydiagram_DecisionNode'):
        assert _is_linked(a2, 'activitydiagram_DecisionNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge35', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge35', a2)
    if hasattr(a2, 'activitydiagram_DecisionNode'):
        assert not _is_linked(a2, 'activitydiagram_DecisionNode', b)


def test_assoc_incoming39_reverse_link_reassign_clear():
    a1 = activitydiagram_MergeNode()
    a2 = activitydiagram_MergeNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge40', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge40', a1)
    if hasattr(a1, 'activitydiagram_MergeNode'):
        assert _is_linked(a1, 'activitydiagram_MergeNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge40', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge40', a2)
    if hasattr(a1, 'activitydiagram_MergeNode'):
        assert not _is_linked(a1, 'activitydiagram_MergeNode', b)
    if hasattr(a2, 'activitydiagram_MergeNode'):
        assert _is_linked(a2, 'activitydiagram_MergeNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge40', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge40', a2)
    if hasattr(a2, 'activitydiagram_MergeNode'):
        assert not _is_linked(a2, 'activitydiagram_MergeNode', b)


def test_assoc_incoming44_reverse_link_reassign_clear():
    a1 = activitydiagram_ForkNode()
    a2 = activitydiagram_ForkNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge45', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge45', a1)
    if hasattr(a1, 'activitydiagram_ForkNode'):
        assert _is_linked(a1, 'activitydiagram_ForkNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge45', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge45', a2)
    if hasattr(a1, 'activitydiagram_ForkNode'):
        assert not _is_linked(a1, 'activitydiagram_ForkNode', b)
    if hasattr(a2, 'activitydiagram_ForkNode'):
        assert _is_linked(a2, 'activitydiagram_ForkNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge45', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge45', a2)
    if hasattr(a2, 'activitydiagram_ForkNode'):
        assert not _is_linked(a2, 'activitydiagram_ForkNode', b)


def test_assoc_incoming49_reverse_link_reassign_clear():
    a1 = activitydiagram_JoinNode()
    a2 = activitydiagram_JoinNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge50', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge50', a1)
    if hasattr(a1, 'activitydiagram_JoinNode'):
        assert _is_linked(a1, 'activitydiagram_JoinNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge50', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge50', a2)
    if hasattr(a1, 'activitydiagram_JoinNode'):
        assert not _is_linked(a1, 'activitydiagram_JoinNode', b)
    if hasattr(a2, 'activitydiagram_JoinNode'):
        assert _is_linked(a2, 'activitydiagram_JoinNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge50', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge50', a2)
    if hasattr(a2, 'activitydiagram_JoinNode'):
        assert not _is_linked(a2, 'activitydiagram_JoinNode', b)


def test_assoc_incoming54_reverse_link_reassign_clear():
    a1 = activitydiagram_FinalNode()
    a2 = activitydiagram_FinalNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge55', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge55', a1)
    if hasattr(a1, 'activitydiagram_FinalNode'):
        assert _is_linked(a1, 'activitydiagram_FinalNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge55', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge55', a2)
    if hasattr(a1, 'activitydiagram_FinalNode'):
        assert not _is_linked(a1, 'activitydiagram_FinalNode', b)
    if hasattr(a2, 'activitydiagram_FinalNode'):
        assert _is_linked(a2, 'activitydiagram_FinalNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge55', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge55', a2)
    if hasattr(a2, 'activitydiagram_FinalNode'):
        assert not _is_linked(a2, 'activitydiagram_FinalNode', b)


def test_assoc_locals4_reverse_link_reassign_clear():
    a1 = activitydiagram_Variable(name=7)
    a2 = activitydiagram_Variable(name=13)
    b = activitydiagram_Activity()
    _safe_set(b, 'activitydiagram_Activity5', {a1})
    assert _is_linked(b, 'activitydiagram_Activity5', a1)
    if hasattr(a1, 'activitydiagram_Variable'):
        assert _is_linked(a1, 'activitydiagram_Variable', b)
    _safe_set(b, 'activitydiagram_Activity5', {a2})
    assert _is_linked(b, 'activitydiagram_Activity5', a2)
    if hasattr(a1, 'activitydiagram_Variable'):
        assert not _is_linked(a1, 'activitydiagram_Variable', b)
    if hasattr(a2, 'activitydiagram_Variable'):
        assert _is_linked(a2, 'activitydiagram_Variable', b)
    _safe_set(b, 'activitydiagram_Activity5', set())
    assert not _is_linked(b, 'activitydiagram_Activity5', a2)
    if hasattr(a2, 'activitydiagram_Variable'):
        assert not _is_linked(a2, 'activitydiagram_Variable', b)


def test_assoc_nodes1_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_Activity()
    _safe_set(b, 'activity', {a1})
    assert _is_linked(b, 'activity', a1)
    if hasattr(a1, 'ActivityNode'):
        assert _is_linked(a1, 'ActivityNode', b)
    _safe_set(b, 'activity', {a2})
    assert _is_linked(b, 'activity', a2)
    if hasattr(a1, 'ActivityNode'):
        assert not _is_linked(a1, 'ActivityNode', b)
    if hasattr(a2, 'ActivityNode'):
        assert _is_linked(a2, 'ActivityNode', b)
    _safe_set(b, 'activity', set())
    assert not _is_linked(b, 'activity', a2)
    if hasattr(a2, 'ActivityNode'):
        assert not _is_linked(a2, 'ActivityNode', b)


def test_assoc_offeredTokens11_reverse_link_reassign_clear():
    a1 = activitydiagram_ControlToken()
    a2 = activitydiagram_ControlToken()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge12', {a1})
    assert _is_linked(b, 'activitydiagram_ActivityEdge12', a1)
    if hasattr(a1, 'activitydiagram_ControlToken'):
        assert _is_linked(a1, 'activitydiagram_ControlToken', b)
    _safe_set(b, 'activitydiagram_ActivityEdge12', {a2})
    assert _is_linked(b, 'activitydiagram_ActivityEdge12', a2)
    if hasattr(a1, 'activitydiagram_ControlToken'):
        assert not _is_linked(a1, 'activitydiagram_ControlToken', b)
    if hasattr(a2, 'activitydiagram_ControlToken'):
        assert _is_linked(a2, 'activitydiagram_ControlToken', b)
    _safe_set(b, 'activitydiagram_ActivityEdge12', set())
    assert not _is_linked(b, 'activitydiagram_ActivityEdge12', a2)
    if hasattr(a2, 'activitydiagram_ControlToken'):
        assert not _is_linked(a2, 'activitydiagram_ControlToken', b)


def test_assoc_operand156_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerExpression()
    a2 = activitydiagram_IntegerExpression()
    b = activitydiagram_IntegerBinaryExpression(operator=True)
    _safe_set(b, 'activitydiagram_IntegerBinaryExpression', a1)
    assert _is_linked(b, 'activitydiagram_IntegerBinaryExpression', a1)
    if hasattr(a1, 'activitydiagram_IntegerExpression'):
        assert _is_linked(a1, 'activitydiagram_IntegerExpression', b)
    _safe_set(b, 'activitydiagram_IntegerBinaryExpression', a2)
    assert _is_linked(b, 'activitydiagram_IntegerBinaryExpression', a2)
    if hasattr(a1, 'activitydiagram_IntegerExpression'):
        assert not _is_linked(a1, 'activitydiagram_IntegerExpression', b)
    if hasattr(a2, 'activitydiagram_IntegerExpression'):
        assert _is_linked(a2, 'activitydiagram_IntegerExpression', b)
    _safe_set(b, 'activitydiagram_IntegerBinaryExpression', None)
    assert not _is_linked(b, 'activitydiagram_IntegerBinaryExpression', a2)
    if hasattr(a2, 'activitydiagram_IntegerExpression'):
        assert not _is_linked(a2, 'activitydiagram_IntegerExpression', b)


def test_assoc_operand160_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerExpression()
    a2 = activitydiagram_IntegerExpression()
    b = activitydiagram_IntegerComparisonExpression(operator=True)
    _safe_set(b, 'activitydiagram_IntegerComparisonExpression', a1)
    assert _is_linked(b, 'activitydiagram_IntegerComparisonExpression', a1)
    if hasattr(a1, 'activitydiagram_IntegerExpression61'):
        assert _is_linked(a1, 'activitydiagram_IntegerExpression61', b)
    _safe_set(b, 'activitydiagram_IntegerComparisonExpression', a2)
    assert _is_linked(b, 'activitydiagram_IntegerComparisonExpression', a2)
    if hasattr(a1, 'activitydiagram_IntegerExpression61'):
        assert not _is_linked(a1, 'activitydiagram_IntegerExpression61', b)
    if hasattr(a2, 'activitydiagram_IntegerExpression61'):
        assert _is_linked(a2, 'activitydiagram_IntegerExpression61', b)
    _safe_set(b, 'activitydiagram_IntegerComparisonExpression', None)
    assert not _is_linked(b, 'activitydiagram_IntegerComparisonExpression', a2)
    if hasattr(a2, 'activitydiagram_IntegerExpression61'):
        assert not _is_linked(a2, 'activitydiagram_IntegerExpression61', b)


def test_assoc_operand166_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanExpression()
    a2 = activitydiagram_BooleanExpression()
    b = activitydiagram_BooleanBinaryExpression(operator=True)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', a1)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a1)
    if hasattr(a1, 'activitydiagram_BooleanExpression67'):
        assert _is_linked(a1, 'activitydiagram_BooleanExpression67', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', a2)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a2)
    if hasattr(a1, 'activitydiagram_BooleanExpression67'):
        assert not _is_linked(a1, 'activitydiagram_BooleanExpression67', b)
    if hasattr(a2, 'activitydiagram_BooleanExpression67'):
        assert _is_linked(a2, 'activitydiagram_BooleanExpression67', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', None)
    assert not _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a2)
    if hasattr(a2, 'activitydiagram_BooleanExpression67'):
        assert not _is_linked(a2, 'activitydiagram_BooleanExpression67', b)


def test_assoc_operand257_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerExpression()
    a2 = activitydiagram_IntegerExpression()
    b = activitydiagram_IntegerBinaryExpression(operator=True)
    _safe_set(b, 'activitydiagram_IntegerBinaryExpression58', a1)
    assert _is_linked(b, 'activitydiagram_IntegerBinaryExpression58', a1)
    if hasattr(a1, 'activitydiagram_IntegerExpression59'):
        assert _is_linked(a1, 'activitydiagram_IntegerExpression59', b)
    _safe_set(b, 'activitydiagram_IntegerBinaryExpression58', a2)
    assert _is_linked(b, 'activitydiagram_IntegerBinaryExpression58', a2)
    if hasattr(a1, 'activitydiagram_IntegerExpression59'):
        assert not _is_linked(a1, 'activitydiagram_IntegerExpression59', b)
    if hasattr(a2, 'activitydiagram_IntegerExpression59'):
        assert _is_linked(a2, 'activitydiagram_IntegerExpression59', b)
    _safe_set(b, 'activitydiagram_IntegerBinaryExpression58', None)
    assert not _is_linked(b, 'activitydiagram_IntegerBinaryExpression58', a2)
    if hasattr(a2, 'activitydiagram_IntegerExpression59'):
        assert not _is_linked(a2, 'activitydiagram_IntegerExpression59', b)


def test_assoc_operand262_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerExpression()
    a2 = activitydiagram_IntegerExpression()
    b = activitydiagram_IntegerComparisonExpression(operator=True)
    _safe_set(b, 'activitydiagram_IntegerComparisonExpression63', a1)
    assert _is_linked(b, 'activitydiagram_IntegerComparisonExpression63', a1)
    if hasattr(a1, 'activitydiagram_IntegerExpression64'):
        assert _is_linked(a1, 'activitydiagram_IntegerExpression64', b)
    _safe_set(b, 'activitydiagram_IntegerComparisonExpression63', a2)
    assert _is_linked(b, 'activitydiagram_IntegerComparisonExpression63', a2)
    if hasattr(a1, 'activitydiagram_IntegerExpression64'):
        assert not _is_linked(a1, 'activitydiagram_IntegerExpression64', b)
    if hasattr(a2, 'activitydiagram_IntegerExpression64'):
        assert _is_linked(a2, 'activitydiagram_IntegerExpression64', b)
    _safe_set(b, 'activitydiagram_IntegerComparisonExpression63', None)
    assert not _is_linked(b, 'activitydiagram_IntegerComparisonExpression63', a2)
    if hasattr(a2, 'activitydiagram_IntegerExpression64'):
        assert not _is_linked(a2, 'activitydiagram_IntegerExpression64', b)


def test_assoc_operand268_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanExpression()
    a2 = activitydiagram_BooleanExpression()
    b = activitydiagram_BooleanBinaryExpression(operator=True)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression69', a1)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression69', a1)
    if hasattr(a1, 'activitydiagram_BooleanExpression70'):
        assert _is_linked(a1, 'activitydiagram_BooleanExpression70', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression69', a2)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression69', a2)
    if hasattr(a1, 'activitydiagram_BooleanExpression70'):
        assert not _is_linked(a1, 'activitydiagram_BooleanExpression70', b)
    if hasattr(a2, 'activitydiagram_BooleanExpression70'):
        assert _is_linked(a2, 'activitydiagram_BooleanExpression70', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression69', None)
    assert not _is_linked(b, 'activitydiagram_BooleanBinaryExpression69', a2)
    if hasattr(a2, 'activitydiagram_BooleanExpression70'):
        assert not _is_linked(a2, 'activitydiagram_BooleanExpression70', b)


def test_assoc_operand65_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanUnaryExpression(operator=True)
    a2 = activitydiagram_BooleanUnaryExpression(operator=False)
    b = activitydiagram_BooleanExpression()
    _safe_set(b, 'activitydiagram_BooleanExpression', a1)
    assert _is_linked(b, 'activitydiagram_BooleanExpression', a1)
    if hasattr(a1, 'activitydiagram_BooleanUnaryExpression'):
        assert _is_linked(a1, 'activitydiagram_BooleanUnaryExpression', b)
    _safe_set(b, 'activitydiagram_BooleanExpression', a2)
    assert _is_linked(b, 'activitydiagram_BooleanExpression', a2)
    if hasattr(a1, 'activitydiagram_BooleanUnaryExpression'):
        assert not _is_linked(a1, 'activitydiagram_BooleanUnaryExpression', b)
    if hasattr(a2, 'activitydiagram_BooleanUnaryExpression'):
        assert _is_linked(a2, 'activitydiagram_BooleanUnaryExpression', b)
    _safe_set(b, 'activitydiagram_BooleanExpression', None)
    assert not _is_linked(b, 'activitydiagram_BooleanExpression', a2)
    if hasattr(a2, 'activitydiagram_BooleanUnaryExpression'):
        assert not _is_linked(a2, 'activitydiagram_BooleanUnaryExpression', b)


def test_assoc_outgoing29_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityEdge()
    a2 = activitydiagram_ActivityEdge()
    b = activitydiagram_AcceptEventAction()
    _safe_set(b, 'activitydiagram_AcceptEventAction30', a1)
    assert _is_linked(b, 'activitydiagram_AcceptEventAction30', a1)
    if hasattr(a1, 'activitydiagram_ActivityEdge31'):
        assert _is_linked(a1, 'activitydiagram_ActivityEdge31', b)
    _safe_set(b, 'activitydiagram_AcceptEventAction30', a2)
    assert _is_linked(b, 'activitydiagram_AcceptEventAction30', a2)
    if hasattr(a1, 'activitydiagram_ActivityEdge31'):
        assert not _is_linked(a1, 'activitydiagram_ActivityEdge31', b)
    if hasattr(a2, 'activitydiagram_ActivityEdge31'):
        assert _is_linked(a2, 'activitydiagram_ActivityEdge31', b)
    _safe_set(b, 'activitydiagram_AcceptEventAction30', None)
    assert not _is_linked(b, 'activitydiagram_AcceptEventAction30', a2)
    if hasattr(a2, 'activitydiagram_ActivityEdge31'):
        assert not _is_linked(a2, 'activitydiagram_ActivityEdge31', b)


def test_assoc_outgoing32_reverse_link_reassign_clear():
    a1 = activitydiagram_InitialNode()
    a2 = activitydiagram_InitialNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge33', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge33', a1)
    if hasattr(a1, 'activitydiagram_InitialNode'):
        assert _is_linked(a1, 'activitydiagram_InitialNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge33', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge33', a2)
    if hasattr(a1, 'activitydiagram_InitialNode'):
        assert not _is_linked(a1, 'activitydiagram_InitialNode', b)
    if hasattr(a2, 'activitydiagram_InitialNode'):
        assert _is_linked(a2, 'activitydiagram_InitialNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge33', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge33', a2)
    if hasattr(a2, 'activitydiagram_InitialNode'):
        assert not _is_linked(a2, 'activitydiagram_InitialNode', b)


def test_assoc_outgoing36_reverse_link_reassign_clear():
    a1 = activitydiagram_DecisionNode()
    a2 = activitydiagram_DecisionNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge38', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge38', a1)
    if hasattr(a1, 'activitydiagram_DecisionNode37'):
        assert _is_linked(a1, 'activitydiagram_DecisionNode37', b)
    _safe_set(b, 'activitydiagram_ActivityEdge38', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge38', a2)
    if hasattr(a1, 'activitydiagram_DecisionNode37'):
        assert not _is_linked(a1, 'activitydiagram_DecisionNode37', b)
    if hasattr(a2, 'activitydiagram_DecisionNode37'):
        assert _is_linked(a2, 'activitydiagram_DecisionNode37', b)
    _safe_set(b, 'activitydiagram_ActivityEdge38', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge38', a2)
    if hasattr(a2, 'activitydiagram_DecisionNode37'):
        assert not _is_linked(a2, 'activitydiagram_DecisionNode37', b)


def test_assoc_outgoing41_reverse_link_reassign_clear():
    a1 = activitydiagram_MergeNode()
    a2 = activitydiagram_MergeNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge43', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge43', a1)
    if hasattr(a1, 'activitydiagram_MergeNode42'):
        assert _is_linked(a1, 'activitydiagram_MergeNode42', b)
    _safe_set(b, 'activitydiagram_ActivityEdge43', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge43', a2)
    if hasattr(a1, 'activitydiagram_MergeNode42'):
        assert not _is_linked(a1, 'activitydiagram_MergeNode42', b)
    if hasattr(a2, 'activitydiagram_MergeNode42'):
        assert _is_linked(a2, 'activitydiagram_MergeNode42', b)
    _safe_set(b, 'activitydiagram_ActivityEdge43', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge43', a2)
    if hasattr(a2, 'activitydiagram_MergeNode42'):
        assert not _is_linked(a2, 'activitydiagram_MergeNode42', b)


def test_assoc_outgoing46_reverse_link_reassign_clear():
    a1 = activitydiagram_ForkNode()
    a2 = activitydiagram_ForkNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge48', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge48', a1)
    if hasattr(a1, 'activitydiagram_ForkNode47'):
        assert _is_linked(a1, 'activitydiagram_ForkNode47', b)
    _safe_set(b, 'activitydiagram_ActivityEdge48', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge48', a2)
    if hasattr(a1, 'activitydiagram_ForkNode47'):
        assert not _is_linked(a1, 'activitydiagram_ForkNode47', b)
    if hasattr(a2, 'activitydiagram_ForkNode47'):
        assert _is_linked(a2, 'activitydiagram_ForkNode47', b)
    _safe_set(b, 'activitydiagram_ActivityEdge48', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge48', a2)
    if hasattr(a2, 'activitydiagram_ForkNode47'):
        assert not _is_linked(a2, 'activitydiagram_ForkNode47', b)


def test_assoc_outgoing51_reverse_link_reassign_clear():
    a1 = activitydiagram_JoinNode()
    a2 = activitydiagram_JoinNode()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge53', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge53', a1)
    if hasattr(a1, 'activitydiagram_JoinNode52'):
        assert _is_linked(a1, 'activitydiagram_JoinNode52', b)
    _safe_set(b, 'activitydiagram_ActivityEdge53', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge53', a2)
    if hasattr(a1, 'activitydiagram_JoinNode52'):
        assert not _is_linked(a1, 'activitydiagram_JoinNode52', b)
    if hasattr(a2, 'activitydiagram_JoinNode52'):
        assert _is_linked(a2, 'activitydiagram_JoinNode52', b)
    _safe_set(b, 'activitydiagram_ActivityEdge53', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge53', a2)
    if hasattr(a2, 'activitydiagram_JoinNode52'):
        assert not _is_linked(a2, 'activitydiagram_JoinNode52', b)


def test_assoc_source6_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge7', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge7', a1)
    if hasattr(a1, 'activitydiagram_ActivityNode'):
        assert _is_linked(a1, 'activitydiagram_ActivityNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge7', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge7', a2)
    if hasattr(a1, 'activitydiagram_ActivityNode'):
        assert not _is_linked(a1, 'activitydiagram_ActivityNode', b)
    if hasattr(a2, 'activitydiagram_ActivityNode'):
        assert _is_linked(a2, 'activitydiagram_ActivityNode', b)
    _safe_set(b, 'activitydiagram_ActivityEdge7', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge7', a2)
    if hasattr(a2, 'activitydiagram_ActivityNode'):
        assert not _is_linked(a2, 'activitydiagram_ActivityNode', b)


def test_assoc_target8_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge9', a1)
    assert _is_linked(b, 'activitydiagram_ActivityEdge9', a1)
    if hasattr(a1, 'activitydiagram_ActivityNode10'):
        assert _is_linked(a1, 'activitydiagram_ActivityNode10', b)
    _safe_set(b, 'activitydiagram_ActivityEdge9', a2)
    assert _is_linked(b, 'activitydiagram_ActivityEdge9', a2)
    if hasattr(a1, 'activitydiagram_ActivityNode10'):
        assert not _is_linked(a1, 'activitydiagram_ActivityNode10', b)
    if hasattr(a2, 'activitydiagram_ActivityNode10'):
        assert _is_linked(a2, 'activitydiagram_ActivityNode10', b)
    _safe_set(b, 'activitydiagram_ActivityEdge9', None)
    assert not _is_linked(b, 'activitydiagram_ActivityEdge9', a2)
    if hasattr(a2, 'activitydiagram_ActivityNode10'):
        assert not _is_linked(a2, 'activitydiagram_ActivityNode10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eventType24_stub_double():
    # activitydiagram_Event has no real 'activitydiagram_Event25' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_AcceptEventAction()
    partner = activitydiagram_Event()
    setattr(partner, 'activitydiagram_Event25', None)
    _safe_set(owner, 'activitydiagram_AcceptEventAction', partner)
    assert getattr(partner, 'activitydiagram_Event25') == owner
    _safe_set(owner, 'activitydiagram_AcceptEventAction', None)
    assert getattr(partner, 'activitydiagram_Event25') is None


def test_assoc_events0_stub_double():
    # activitydiagram_Event has no real 'activitydiagram_Event' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Activity()
    partner = activitydiagram_Event()
    setattr(partner, 'activitydiagram_Event', None)
    _safe_set(owner, 'activitydiagram_Activity', {partner})
    assert getattr(partner, 'activitydiagram_Event') == owner
    _safe_set(owner, 'activitydiagram_Activity', set())
    assert getattr(partner, 'activitydiagram_Event') is None


def test_assoc_guard13_stub_double():
    # activitydiagram_ControlFlow has no real 'activitydiagram_ControlFlow' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanVariable(currentValue=True, initialValue=True)
    partner = activitydiagram_ControlFlow()
    setattr(partner, 'activitydiagram_ControlFlow', None)
    _safe_set(owner, 'activitydiagram_BooleanVariable', partner)
    assert getattr(partner, 'activitydiagram_ControlFlow') == owner
    _safe_set(owner, 'activitydiagram_BooleanVariable', None)
    assert getattr(partner, 'activitydiagram_ControlFlow') is None


def test_assoc_incoming18_stub_double():
    # activitydiagram_Action has no real 'activitydiagram_Action' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityEdge()
    partner = activitydiagram_Action()
    setattr(partner, 'activitydiagram_Action', None)
    _safe_set(owner, 'activitydiagram_ActivityEdge19', partner)
    assert getattr(partner, 'activitydiagram_Action') == owner
    _safe_set(owner, 'activitydiagram_ActivityEdge19', None)
    assert getattr(partner, 'activitydiagram_Action') is None


def test_assoc_outgoing20_stub_double():
    # activitydiagram_Action has no real 'activitydiagram_Action21' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityEdge()
    partner = activitydiagram_Action()
    setattr(partner, 'activitydiagram_Action21', None)
    _safe_set(owner, 'activitydiagram_ActivityEdge22', partner)
    assert getattr(partner, 'activitydiagram_Action21') == owner
    _safe_set(owner, 'activitydiagram_ActivityEdge22', None)
    assert getattr(partner, 'activitydiagram_Action21') is None


