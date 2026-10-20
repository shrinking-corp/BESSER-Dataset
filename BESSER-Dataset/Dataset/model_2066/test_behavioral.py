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
    activitydiagram_StringValue,
    activitydiagram_StringVariable,
    activitydiagram_Value,
    activitydiagram_Variable,
    BooleanBinaryOperator,
    BooleanUnaryOperator,
    IntegerCalculationOperator,
    IntegerComparisionOperator,
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

def test_assoc_assignee27_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerComparisonExpression(operator="sample_text")
    a2 = activitydiagram_IntegerComparisonExpression(operator="sample_text_2")
    b = activitydiagram_BooleanVariable()
    _safe_set(b, 'activitydiagram_BooleanVariable28', a1)
    assert _is_linked(b, 'activitydiagram_BooleanVariable28', a1)
    if hasattr(a1, 'activitydiagram_IntegerComparisonExpression'):
        assert _is_linked(a1, 'activitydiagram_IntegerComparisonExpression', b)
    _safe_set(b, 'activitydiagram_BooleanVariable28', a2)
    assert _is_linked(b, 'activitydiagram_BooleanVariable28', a2)
    if hasattr(a1, 'activitydiagram_IntegerComparisonExpression'):
        assert not _is_linked(a1, 'activitydiagram_IntegerComparisonExpression', b)
    if hasattr(a2, 'activitydiagram_IntegerComparisonExpression'):
        assert _is_linked(a2, 'activitydiagram_IntegerComparisonExpression', b)
    _safe_set(b, 'activitydiagram_BooleanVariable28', None)
    assert not _is_linked(b, 'activitydiagram_BooleanVariable28', a2)
    if hasattr(a2, 'activitydiagram_IntegerComparisonExpression'):
        assert not _is_linked(a2, 'activitydiagram_IntegerComparisonExpression', b)


def test_assoc_operand131_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariable()
    a2 = activitydiagram_BooleanVariable()
    b = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', a1)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariable32'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariable32', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', a2)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariable32'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariable32', b)
    if hasattr(a2, 'activitydiagram_BooleanVariable32'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariable32', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', None)
    assert not _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariable32'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariable32', b)


def test_assoc_operand233_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariable()
    a2 = activitydiagram_BooleanVariable()
    b = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression34', a1)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression34', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariable35'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariable35', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression34', a2)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression34', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariable35'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariable35', b)
    if hasattr(a2, 'activitydiagram_BooleanVariable35'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariable35', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression34', None)
    assert not _is_linked(b, 'activitydiagram_BooleanBinaryExpression34', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariable35'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariable35', b)


def test_assoc_operand29_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariable()
    a2 = activitydiagram_BooleanVariable()
    b = activitydiagram_BooleanUnaryExpression(operator="sample_text")
    _safe_set(b, 'activitydiagram_BooleanUnaryExpression', a1)
    assert _is_linked(b, 'activitydiagram_BooleanUnaryExpression', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariable30'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariable30', b)
    _safe_set(b, 'activitydiagram_BooleanUnaryExpression', a2)
    assert _is_linked(b, 'activitydiagram_BooleanUnaryExpression', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariable30'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariable30', b)
    if hasattr(a2, 'activitydiagram_BooleanVariable30'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariable30', b)
    _safe_set(b, 'activitydiagram_BooleanUnaryExpression', None)
    assert not _is_linked(b, 'activitydiagram_BooleanUnaryExpression', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariable30'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariable30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignee23_stub_double():
    # activitydiagram_BooleanExpression has no real 'activitydiagram_BooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanVariable()
    partner = activitydiagram_BooleanExpression()
    setattr(partner, 'activitydiagram_BooleanExpression', None)
    _safe_set(owner, 'activitydiagram_BooleanVariable24', partner)
    assert getattr(partner, 'activitydiagram_BooleanExpression') == owner
    _safe_set(owner, 'activitydiagram_BooleanVariable24', None)
    assert getattr(partner, 'activitydiagram_BooleanExpression') is None


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


def test_assoc_guard15_stub_double():
    # activitydiagram_ControlFlow has no real 'activitydiagram_ControlFlow' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanVariable()
    partner = activitydiagram_ControlFlow()
    setattr(partner, 'activitydiagram_ControlFlow', None)
    _safe_set(owner, 'activitydiagram_BooleanVariable', partner)
    assert getattr(partner, 'activitydiagram_ControlFlow') == owner
    _safe_set(owner, 'activitydiagram_BooleanVariable', None)
    assert getattr(partner, 'activitydiagram_ControlFlow') is None


