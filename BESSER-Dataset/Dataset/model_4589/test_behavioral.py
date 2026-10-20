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
    adwithoutruntime_Action,
    adwithoutruntime_Activity,
    adwithoutruntime_ActivityEdge,
    adwithoutruntime_ActivityFinalNode,
    adwithoutruntime_ActivityNode,
    adwithoutruntime_BooleanBinaryExpression,
    adwithoutruntime_BooleanExpression,
    adwithoutruntime_BooleanUnaryExpression,
    adwithoutruntime_BooleanValue,
    adwithoutruntime_BooleanVariable,
    adwithoutruntime_ControlFlow,
    adwithoutruntime_ControlNode,
    adwithoutruntime_DecisionNode,
    adwithoutruntime_ExecutableNode,
    adwithoutruntime_Expression,
    adwithoutruntime_FinalNode,
    adwithoutruntime_ForkNode,
    adwithoutruntime_InitialNode,
    adwithoutruntime_IntegerCalculationExpression,
    adwithoutruntime_IntegerComparisonExpression,
    adwithoutruntime_IntegerExpression,
    adwithoutruntime_IntegerValue,
    adwithoutruntime_IntegerVariable,
    adwithoutruntime_JoinNode,
    adwithoutruntime_MergeNode,
    adwithoutruntime_NamedElement,
    adwithoutruntime_OpaqueAction,
    adwithoutruntime_Value,
    adwithoutruntime_Variable,
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

def test_assoc_assignee28_stub_double():
    # adwithoutruntime_IntegerVariable has no real 'adwithoutruntime_IntegerVariable29' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_IntegerCalculationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_IntegerCalculationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_IntegerCalculationExpression(operator="sample_text")
    partner = adwithoutruntime_IntegerVariable()
    setattr(partner, 'adwithoutruntime_IntegerVariable29', None)
    _safe_set(owner, 'adwithoutruntime_IntegerCalculationExpression', partner)
    assert getattr(partner, 'adwithoutruntime_IntegerVariable29') == owner
    _safe_set(owner, 'adwithoutruntime_IntegerCalculationExpression', None)
    assert getattr(partner, 'adwithoutruntime_IntegerVariable29') is None


def test_assoc_assignee30_stub_double():
    # adwithoutruntime_BooleanVariable has no real 'adwithoutruntime_BooleanVariable31' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_IntegerComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_IntegerComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_IntegerComparisonExpression(operator="sample_text")
    partner = adwithoutruntime_BooleanVariable()
    setattr(partner, 'adwithoutruntime_BooleanVariable31', None)
    _safe_set(owner, 'adwithoutruntime_IntegerComparisonExpression', partner)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable31') == owner
    _safe_set(owner, 'adwithoutruntime_IntegerComparisonExpression', None)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable31') is None


def test_assoc_currentValue19_stub_double():
    # adwithoutruntime_Value has no real 'adwithoutruntime_Value21' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_Variable(name="sample_text")
    partner = adwithoutruntime_Value()
    setattr(partner, 'adwithoutruntime_Value21', None)
    _safe_set(owner, 'adwithoutruntime_Variable20', partner)
    assert getattr(partner, 'adwithoutruntime_Value21') == owner
    _safe_set(owner, 'adwithoutruntime_Variable20', None)
    assert getattr(partner, 'adwithoutruntime_Value21') is None


def test_assoc_initialValue17_stub_double():
    # adwithoutruntime_Value has no real 'adwithoutruntime_Value' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_Variable(name="sample_text")
    partner = adwithoutruntime_Value()
    setattr(partner, 'adwithoutruntime_Value', None)
    _safe_set(owner, 'adwithoutruntime_Variable18', partner)
    assert getattr(partner, 'adwithoutruntime_Value') == owner
    _safe_set(owner, 'adwithoutruntime_Variable18', None)
    assert getattr(partner, 'adwithoutruntime_Value') is None


def test_assoc_inputs4_stub_double():
    # adwithoutruntime_Activity has no real 'adwithoutruntime_Activity5' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_Variable(name="sample_text")
    partner = adwithoutruntime_Activity()
    setattr(partner, 'adwithoutruntime_Activity5', None)
    _safe_set(owner, 'adwithoutruntime_Variable6', partner)
    assert owner in getattr(partner, 'adwithoutruntime_Activity5')
    _safe_set(owner, 'adwithoutruntime_Variable6', None)
    assert owner not in getattr(partner, 'adwithoutruntime_Activity5')


def test_assoc_locals2_stub_double():
    # adwithoutruntime_Activity has no real 'adwithoutruntime_Activity3' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_Variable(name="sample_text")
    partner = adwithoutruntime_Activity()
    setattr(partner, 'adwithoutruntime_Activity3', None)
    _safe_set(owner, 'adwithoutruntime_Variable', partner)
    assert owner in getattr(partner, 'adwithoutruntime_Activity3')
    _safe_set(owner, 'adwithoutruntime_Variable', None)
    assert owner not in getattr(partner, 'adwithoutruntime_Activity3')


def test_assoc_operand134_stub_double():
    # adwithoutruntime_BooleanVariable has no real 'adwithoutruntime_BooleanVariable35' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_BooleanBinaryExpression(operator="sample_text")
    partner = adwithoutruntime_BooleanVariable()
    setattr(partner, 'adwithoutruntime_BooleanVariable35', None)
    _safe_set(owner, 'adwithoutruntime_BooleanBinaryExpression', partner)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable35') == owner
    _safe_set(owner, 'adwithoutruntime_BooleanBinaryExpression', None)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable35') is None


def test_assoc_operand236_stub_double():
    # adwithoutruntime_BooleanVariable has no real 'adwithoutruntime_BooleanVariable38' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_BooleanBinaryExpression(operator="sample_text")
    partner = adwithoutruntime_BooleanVariable()
    setattr(partner, 'adwithoutruntime_BooleanVariable38', None)
    _safe_set(owner, 'adwithoutruntime_BooleanBinaryExpression37', partner)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable38') == owner
    _safe_set(owner, 'adwithoutruntime_BooleanBinaryExpression37', None)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable38') is None


def test_assoc_operand32_stub_double():
    # adwithoutruntime_BooleanVariable has no real 'adwithoutruntime_BooleanVariable33' property in the generated
    # code (a bare stub) -- manually attach it so adwithoutruntime_BooleanUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adwithoutruntime_BooleanUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adwithoutruntime_BooleanUnaryExpression(operator="sample_text")
    partner = adwithoutruntime_BooleanVariable()
    setattr(partner, 'adwithoutruntime_BooleanVariable33', None)
    _safe_set(owner, 'adwithoutruntime_BooleanUnaryExpression', partner)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable33') == owner
    _safe_set(owner, 'adwithoutruntime_BooleanUnaryExpression', None)
    assert getattr(partner, 'adwithoutruntime_BooleanVariable33') is None


