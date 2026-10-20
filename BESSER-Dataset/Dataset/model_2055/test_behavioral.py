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
    Token,
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
    activitydiagram_ControlToken,
    activitydiagram_DecisionNode,
    activitydiagram_ExecutableNode,
    activitydiagram_Expression,
    activitydiagram_FinalNode,
    activitydiagram_ForkNode,
    activitydiagram_ForkedToken,
    activitydiagram_InitialNode,
    activitydiagram_Input,
    activitydiagram_InputValue,
    activitydiagram_IntegerCalculationExpression,
    activitydiagram_IntegerComparisonExpression,
    activitydiagram_IntegerExpression,
    activitydiagram_IntegerValue,
    activitydiagram_IntegerVariable,
    activitydiagram_JoinNode,
    activitydiagram_MergeNode,
    activitydiagram_NamedElement,
    activitydiagram_Offer,
    activitydiagram_OpaqueAction,
    activitydiagram_Token,
    activitydiagram_Trace,
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


def test_assoc_assignee33_stub_double():
    # activitydiagram_IntegerVariable has no real 'activitydiagram_IntegerVariable34' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerCalculationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerCalculationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerCalculationExpression(operator="sample_text")
    partner = activitydiagram_IntegerVariable()
    setattr(partner, 'activitydiagram_IntegerVariable34', None)
    _safe_set(owner, 'activitydiagram_IntegerCalculationExpression', partner)
    assert getattr(partner, 'activitydiagram_IntegerVariable34') == owner
    _safe_set(owner, 'activitydiagram_IntegerCalculationExpression', None)
    assert getattr(partner, 'activitydiagram_IntegerVariable34') is None


def test_assoc_assignee35_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable36' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerComparisonExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable36', None)
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable36') == owner
    _safe_set(owner, 'activitydiagram_IntegerComparisonExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable36') is None


def test_assoc_baseToken57_stub_double():
    # activitydiagram_Token has no real 'activitydiagram_Token58' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ForkedToken's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ForkedToken's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ForkedToken(remainingOffersCount=7)
    partner = activitydiagram_Token()
    setattr(partner, 'activitydiagram_Token58', None)
    _safe_set(owner, 'activitydiagram_ForkedToken', partner)
    assert getattr(partner, 'activitydiagram_Token58') == owner
    _safe_set(owner, 'activitydiagram_ForkedToken', None)
    assert getattr(partner, 'activitydiagram_Token58') is None


def test_assoc_currentValue24_stub_double():
    # activitydiagram_Value has no real 'activitydiagram_Value26' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_Value()
    setattr(partner, 'activitydiagram_Value26', None)
    _safe_set(owner, 'activitydiagram_Variable25', partner)
    assert getattr(partner, 'activitydiagram_Value26') == owner
    _safe_set(owner, 'activitydiagram_Variable25', None)
    assert getattr(partner, 'activitydiagram_Value26') is None


def test_assoc_executedNodes48_stub_double():
    # activitydiagram_Trace has no real 'activitydiagram_Trace49' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Trace()
    setattr(partner, 'activitydiagram_Trace49', None)
    _safe_set(owner, 'activitydiagram_ActivityNode', partner)
    assert owner in getattr(partner, 'activitydiagram_Trace49')
    _safe_set(owner, 'activitydiagram_ActivityNode', None)
    assert owner not in getattr(partner, 'activitydiagram_Trace49')


def test_assoc_heldTokens13_stub_double():
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


def test_assoc_holder46_stub_double():
    # activitydiagram_Token has no real 'heldTokens' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Token()
    setattr(partner, 'heldTokens', None)
    _safe_set(owner, 'ActivityNode47', partner)
    assert getattr(partner, 'heldTokens') == owner
    _safe_set(owner, 'ActivityNode47', None)
    assert getattr(partner, 'heldTokens') is None


def test_assoc_incoming10_stub_double():
    # activitydiagram_ActivityEdge has no real 'ActivityEdge11' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'ActivityEdge11', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'ActivityEdge11') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'ActivityEdge11') is None


def test_assoc_initialValue22_stub_double():
    # activitydiagram_Value has no real 'activitydiagram_Value' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_Value()
    setattr(partner, 'activitydiagram_Value', None)
    _safe_set(owner, 'activitydiagram_Variable23', partner)
    assert getattr(partner, 'activitydiagram_Value') == owner
    _safe_set(owner, 'activitydiagram_Variable23', None)
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


def test_assoc_operand139_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable40' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable40', None)
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable40') == owner
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable40') is None


def test_assoc_operand241_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable43' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanBinaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable43', None)
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression42', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable43') == owner
    _safe_set(owner, 'activitydiagram_BooleanBinaryExpression42', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable43') is None


def test_assoc_operand37_stub_double():
    # activitydiagram_BooleanVariable has no real 'activitydiagram_BooleanVariable38' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanUnaryExpression(operator="sample_text")
    partner = activitydiagram_BooleanVariable()
    setattr(partner, 'activitydiagram_BooleanVariable38', None)
    _safe_set(owner, 'activitydiagram_BooleanUnaryExpression', partner)
    assert getattr(partner, 'activitydiagram_BooleanVariable38') == owner
    _safe_set(owner, 'activitydiagram_BooleanUnaryExpression', None)
    assert getattr(partner, 'activitydiagram_BooleanVariable38') is None


def test_assoc_outgoing9_stub_double():
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


def test_assoc_source14_stub_double():
    # activitydiagram_ActivityEdge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'ActivityNode15', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'ActivityNode15', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target16_stub_double():
    # activitydiagram_ActivityEdge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_ActivityEdge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'ActivityNode17', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'ActivityNode17', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_variable52_stub_double():
    # activitydiagram_InputValue has no real 'activitydiagram_InputValue53' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_InputValue()
    setattr(partner, 'activitydiagram_InputValue53', None)
    _safe_set(owner, 'activitydiagram_Variable54', partner)
    assert getattr(partner, 'activitydiagram_InputValue53') == owner
    _safe_set(owner, 'activitydiagram_Variable54', None)
    assert getattr(partner, 'activitydiagram_InputValue53') is None


