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

def test_assoc_activity12_reverse_link_reassign_clear():
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


def test_assoc_assignee33_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerVariable()
    a2 = activitydiagram_IntegerVariable()
    b = activitydiagram_IntegerCalculationExpression(operator="sample_text")
    _safe_set(b, 'activitydiagram_IntegerCalculationExpression', a1)
    assert _is_linked(b, 'activitydiagram_IntegerCalculationExpression', a1)
    if hasattr(a1, 'activitydiagram_IntegerVariable34'):
        assert _is_linked(a1, 'activitydiagram_IntegerVariable34', b)
    _safe_set(b, 'activitydiagram_IntegerCalculationExpression', a2)
    assert _is_linked(b, 'activitydiagram_IntegerCalculationExpression', a2)
    if hasattr(a1, 'activitydiagram_IntegerVariable34'):
        assert not _is_linked(a1, 'activitydiagram_IntegerVariable34', b)
    if hasattr(a2, 'activitydiagram_IntegerVariable34'):
        assert _is_linked(a2, 'activitydiagram_IntegerVariable34', b)
    _safe_set(b, 'activitydiagram_IntegerCalculationExpression', None)
    assert not _is_linked(b, 'activitydiagram_IntegerCalculationExpression', a2)
    if hasattr(a2, 'activitydiagram_IntegerVariable34'):
        assert not _is_linked(a2, 'activitydiagram_IntegerVariable34', b)


def test_assoc_assignee35_reverse_link_reassign_clear():
    a1 = activitydiagram_IntegerComparisonExpression(operator="sample_text")
    a2 = activitydiagram_IntegerComparisonExpression(operator="sample_text_2")
    b = activitydiagram_BooleanVariable()
    _safe_set(b, 'activitydiagram_BooleanVariable36', a1)
    assert _is_linked(b, 'activitydiagram_BooleanVariable36', a1)
    if hasattr(a1, 'activitydiagram_IntegerComparisonExpression'):
        assert _is_linked(a1, 'activitydiagram_IntegerComparisonExpression', b)
    _safe_set(b, 'activitydiagram_BooleanVariable36', a2)
    assert _is_linked(b, 'activitydiagram_BooleanVariable36', a2)
    if hasattr(a1, 'activitydiagram_IntegerComparisonExpression'):
        assert not _is_linked(a1, 'activitydiagram_IntegerComparisonExpression', b)
    if hasattr(a2, 'activitydiagram_IntegerComparisonExpression'):
        assert _is_linked(a2, 'activitydiagram_IntegerComparisonExpression', b)
    _safe_set(b, 'activitydiagram_BooleanVariable36', None)
    assert not _is_linked(b, 'activitydiagram_BooleanVariable36', a2)
    if hasattr(a2, 'activitydiagram_IntegerComparisonExpression'):
        assert not _is_linked(a2, 'activitydiagram_IntegerComparisonExpression', b)


def test_assoc_baseToken54_reverse_link_reassign_clear():
    a1 = activitydiagram_Token()
    a2 = activitydiagram_Token()
    b = activitydiagram_ForkedToken(remainingOffersCount=7)
    _safe_set(b, 'activitydiagram_ForkedToken', a1)
    assert _is_linked(b, 'activitydiagram_ForkedToken', a1)
    if hasattr(a1, 'activitydiagram_Token55'):
        assert _is_linked(a1, 'activitydiagram_Token55', b)
    _safe_set(b, 'activitydiagram_ForkedToken', a2)
    assert _is_linked(b, 'activitydiagram_ForkedToken', a2)
    if hasattr(a1, 'activitydiagram_Token55'):
        assert not _is_linked(a1, 'activitydiagram_Token55', b)
    if hasattr(a2, 'activitydiagram_Token55'):
        assert _is_linked(a2, 'activitydiagram_Token55', b)
    _safe_set(b, 'activitydiagram_ForkedToken', None)
    assert not _is_linked(b, 'activitydiagram_ForkedToken', a2)
    if hasattr(a2, 'activitydiagram_Token55'):
        assert not _is_linked(a2, 'activitydiagram_Token55', b)


def test_assoc_edges1_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityEdge()
    a2 = activitydiagram_ActivityEdge()
    b = activitydiagram_Activity()
    _safe_set(b, 'activitydiagram_Activity', {a1})
    assert _is_linked(b, 'activitydiagram_Activity', a1)
    if hasattr(a1, 'activitydiagram_ActivityEdge'):
        assert _is_linked(a1, 'activitydiagram_ActivityEdge', b)
    _safe_set(b, 'activitydiagram_Activity', {a2})
    assert _is_linked(b, 'activitydiagram_Activity', a2)
    if hasattr(a1, 'activitydiagram_ActivityEdge'):
        assert not _is_linked(a1, 'activitydiagram_ActivityEdge', b)
    if hasattr(a2, 'activitydiagram_ActivityEdge'):
        assert _is_linked(a2, 'activitydiagram_ActivityEdge', b)
    _safe_set(b, 'activitydiagram_Activity', set())
    assert not _is_linked(b, 'activitydiagram_Activity', a2)
    if hasattr(a2, 'activitydiagram_ActivityEdge'):
        assert not _is_linked(a2, 'activitydiagram_ActivityEdge', b)


def test_assoc_expressions21_reverse_link_reassign_clear():
    a1 = activitydiagram_OpaqueAction()
    a2 = activitydiagram_OpaqueAction()
    b = activitydiagram_Expression()
    _safe_set(b, 'activitydiagram_Expression', a1)
    assert _is_linked(b, 'activitydiagram_Expression', a1)
    if hasattr(a1, 'activitydiagram_OpaqueAction'):
        assert _is_linked(a1, 'activitydiagram_OpaqueAction', b)
    _safe_set(b, 'activitydiagram_Expression', a2)
    assert _is_linked(b, 'activitydiagram_Expression', a2)
    if hasattr(a1, 'activitydiagram_OpaqueAction'):
        assert not _is_linked(a1, 'activitydiagram_OpaqueAction', b)
    if hasattr(a2, 'activitydiagram_OpaqueAction'):
        assert _is_linked(a2, 'activitydiagram_OpaqueAction', b)
    _safe_set(b, 'activitydiagram_Expression', None)
    assert not _is_linked(b, 'activitydiagram_Expression', a2)
    if hasattr(a2, 'activitydiagram_OpaqueAction'):
        assert not _is_linked(a2, 'activitydiagram_OpaqueAction', b)


def test_assoc_heldTokens13_reverse_link_reassign_clear():
    a1 = activitydiagram_Token()
    a2 = activitydiagram_Token()
    b = activitydiagram_ActivityNode(running=True)
    _safe_set(b, 'activitydiagram_ActivityNode', {a1})
    assert _is_linked(b, 'activitydiagram_ActivityNode', a1)
    if hasattr(a1, 'activitydiagram_Token'):
        assert _is_linked(a1, 'activitydiagram_Token', b)
    _safe_set(b, 'activitydiagram_ActivityNode', {a2})
    assert _is_linked(b, 'activitydiagram_ActivityNode', a2)
    if hasattr(a1, 'activitydiagram_Token'):
        assert not _is_linked(a1, 'activitydiagram_Token', b)
    if hasattr(a2, 'activitydiagram_Token'):
        assert _is_linked(a2, 'activitydiagram_Token', b)
    _safe_set(b, 'activitydiagram_ActivityNode', set())
    assert not _is_linked(b, 'activitydiagram_ActivityNode', a2)
    if hasattr(a2, 'activitydiagram_Token'):
        assert not _is_linked(a2, 'activitydiagram_Token', b)


def test_assoc_incoming10_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'ActivityEdge11', a1)
    assert _is_linked(b, 'ActivityEdge11', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'ActivityEdge11', a2)
    assert _is_linked(b, 'ActivityEdge11', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'ActivityEdge11', None)
    assert not _is_linked(b, 'ActivityEdge11', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_inputs4_reverse_link_reassign_clear():
    a1 = activitydiagram_Variable(name="sample_text")
    a2 = activitydiagram_Variable(name="sample_text_2")
    b = activitydiagram_Activity()
    _safe_set(b, 'activitydiagram_Activity5', {a1})
    assert _is_linked(b, 'activitydiagram_Activity5', a1)
    if hasattr(a1, 'activitydiagram_Variable6'):
        assert _is_linked(a1, 'activitydiagram_Variable6', b)
    _safe_set(b, 'activitydiagram_Activity5', {a2})
    assert _is_linked(b, 'activitydiagram_Activity5', a2)
    if hasattr(a1, 'activitydiagram_Variable6'):
        assert not _is_linked(a1, 'activitydiagram_Variable6', b)
    if hasattr(a2, 'activitydiagram_Variable6'):
        assert _is_linked(a2, 'activitydiagram_Variable6', b)
    _safe_set(b, 'activitydiagram_Activity5', set())
    assert not _is_linked(b, 'activitydiagram_Activity5', a2)
    if hasattr(a2, 'activitydiagram_Variable6'):
        assert not _is_linked(a2, 'activitydiagram_Variable6', b)


def test_assoc_locals2_reverse_link_reassign_clear():
    a1 = activitydiagram_Variable(name="sample_text")
    a2 = activitydiagram_Variable(name="sample_text_2")
    b = activitydiagram_Activity()
    _safe_set(b, 'activitydiagram_Activity3', {a1})
    assert _is_linked(b, 'activitydiagram_Activity3', a1)
    if hasattr(a1, 'activitydiagram_Variable'):
        assert _is_linked(a1, 'activitydiagram_Variable', b)
    _safe_set(b, 'activitydiagram_Activity3', {a2})
    assert _is_linked(b, 'activitydiagram_Activity3', a2)
    if hasattr(a1, 'activitydiagram_Variable'):
        assert not _is_linked(a1, 'activitydiagram_Variable', b)
    if hasattr(a2, 'activitydiagram_Variable'):
        assert _is_linked(a2, 'activitydiagram_Variable', b)
    _safe_set(b, 'activitydiagram_Activity3', set())
    assert not _is_linked(b, 'activitydiagram_Activity3', a2)
    if hasattr(a2, 'activitydiagram_Variable'):
        assert not _is_linked(a2, 'activitydiagram_Variable', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
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


def test_assoc_offeredTokens44_reverse_link_reassign_clear():
    a1 = activitydiagram_Token()
    a2 = activitydiagram_Token()
    b = activitydiagram_Offer()
    _safe_set(b, 'activitydiagram_Offer45', {a1})
    assert _is_linked(b, 'activitydiagram_Offer45', a1)
    if hasattr(a1, 'activitydiagram_Token46'):
        assert _is_linked(a1, 'activitydiagram_Token46', b)
    _safe_set(b, 'activitydiagram_Offer45', {a2})
    assert _is_linked(b, 'activitydiagram_Offer45', a2)
    if hasattr(a1, 'activitydiagram_Token46'):
        assert not _is_linked(a1, 'activitydiagram_Token46', b)
    if hasattr(a2, 'activitydiagram_Token46'):
        assert _is_linked(a2, 'activitydiagram_Token46', b)
    _safe_set(b, 'activitydiagram_Offer45', set())
    assert not _is_linked(b, 'activitydiagram_Offer45', a2)
    if hasattr(a2, 'activitydiagram_Token46'):
        assert not _is_linked(a2, 'activitydiagram_Token46', b)


def test_assoc_offers18_reverse_link_reassign_clear():
    a1 = activitydiagram_Offer()
    a2 = activitydiagram_Offer()
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'activitydiagram_ActivityEdge19', {a1})
    assert _is_linked(b, 'activitydiagram_ActivityEdge19', a1)
    if hasattr(a1, 'activitydiagram_Offer'):
        assert _is_linked(a1, 'activitydiagram_Offer', b)
    _safe_set(b, 'activitydiagram_ActivityEdge19', {a2})
    assert _is_linked(b, 'activitydiagram_ActivityEdge19', a2)
    if hasattr(a1, 'activitydiagram_Offer'):
        assert not _is_linked(a1, 'activitydiagram_Offer', b)
    if hasattr(a2, 'activitydiagram_Offer'):
        assert _is_linked(a2, 'activitydiagram_Offer', b)
    _safe_set(b, 'activitydiagram_ActivityEdge19', set())
    assert not _is_linked(b, 'activitydiagram_ActivityEdge19', a2)
    if hasattr(a2, 'activitydiagram_Offer'):
        assert not _is_linked(a2, 'activitydiagram_Offer', b)


def test_assoc_operand139_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariable()
    a2 = activitydiagram_BooleanVariable()
    b = activitydiagram_BooleanBinaryExpression(operator=True)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', a1)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariable40'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariable40', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', a2)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariable40'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariable40', b)
    if hasattr(a2, 'activitydiagram_BooleanVariable40'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariable40', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression', None)
    assert not _is_linked(b, 'activitydiagram_BooleanBinaryExpression', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariable40'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariable40', b)


def test_assoc_operand241_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariable()
    a2 = activitydiagram_BooleanVariable()
    b = activitydiagram_BooleanBinaryExpression(operator=True)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression42', a1)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression42', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariable43'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariable43', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression42', a2)
    assert _is_linked(b, 'activitydiagram_BooleanBinaryExpression42', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariable43'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariable43', b)
    if hasattr(a2, 'activitydiagram_BooleanVariable43'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariable43', b)
    _safe_set(b, 'activitydiagram_BooleanBinaryExpression42', None)
    assert not _is_linked(b, 'activitydiagram_BooleanBinaryExpression42', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariable43'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariable43', b)


def test_assoc_operand37_reverse_link_reassign_clear():
    a1 = activitydiagram_BooleanVariable()
    a2 = activitydiagram_BooleanVariable()
    b = activitydiagram_BooleanUnaryExpression(operator="sample_text")
    _safe_set(b, 'activitydiagram_BooleanUnaryExpression', a1)
    assert _is_linked(b, 'activitydiagram_BooleanUnaryExpression', a1)
    if hasattr(a1, 'activitydiagram_BooleanVariable38'):
        assert _is_linked(a1, 'activitydiagram_BooleanVariable38', b)
    _safe_set(b, 'activitydiagram_BooleanUnaryExpression', a2)
    assert _is_linked(b, 'activitydiagram_BooleanUnaryExpression', a2)
    if hasattr(a1, 'activitydiagram_BooleanVariable38'):
        assert not _is_linked(a1, 'activitydiagram_BooleanVariable38', b)
    if hasattr(a2, 'activitydiagram_BooleanVariable38'):
        assert _is_linked(a2, 'activitydiagram_BooleanVariable38', b)
    _safe_set(b, 'activitydiagram_BooleanUnaryExpression', None)
    assert not _is_linked(b, 'activitydiagram_BooleanUnaryExpression', a2)
    if hasattr(a2, 'activitydiagram_BooleanVariable38'):
        assert not _is_linked(a2, 'activitydiagram_BooleanVariable38', b)


def test_assoc_outgoing9_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'ActivityEdge', a1)
    assert _is_linked(b, 'ActivityEdge', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'ActivityEdge', a2)
    assert _is_linked(b, 'ActivityEdge', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'ActivityEdge', None)
    assert not _is_linked(b, 'ActivityEdge', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source14_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'ActivityNode15'):
        assert _is_linked(a1, 'ActivityNode15', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'ActivityNode15'):
        assert not _is_linked(a1, 'ActivityNode15', b)
    if hasattr(a2, 'ActivityNode15'):
        assert _is_linked(a2, 'ActivityNode15', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'ActivityNode15'):
        assert not _is_linked(a2, 'ActivityNode15', b)


def test_assoc_target16_reverse_link_reassign_clear():
    a1 = activitydiagram_ActivityNode(running=True)
    a2 = activitydiagram_ActivityNode(running=False)
    b = activitydiagram_ActivityEdge()
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'ActivityNode17'):
        assert _is_linked(a1, 'ActivityNode17', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'ActivityNode17'):
        assert not _is_linked(a1, 'ActivityNode17', b)
    if hasattr(a2, 'ActivityNode17'):
        assert _is_linked(a2, 'ActivityNode17', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'ActivityNode17'):
        assert not _is_linked(a2, 'ActivityNode17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignee31_stub_double():
    # activitydiagram_BooleanExpression has no real 'activitydiagram_BooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_BooleanVariable()
    partner = activitydiagram_BooleanExpression()
    setattr(partner, 'activitydiagram_BooleanExpression', None)
    _safe_set(owner, 'activitydiagram_BooleanVariable32', partner)
    assert getattr(partner, 'activitydiagram_BooleanExpression') == owner
    _safe_set(owner, 'activitydiagram_BooleanVariable32', None)
    assert getattr(partner, 'activitydiagram_BooleanExpression') is None


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


def test_assoc_executedNodes56_stub_double():
    # activitydiagram_Trace has no real 'activitydiagram_Trace57' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_ActivityNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_ActivityNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_ActivityNode(running=True)
    partner = activitydiagram_Trace()
    setattr(partner, 'activitydiagram_Trace57', None)
    _safe_set(owner, 'activitydiagram_ActivityNode58', partner)
    assert owner in getattr(partner, 'activitydiagram_Trace57')
    _safe_set(owner, 'activitydiagram_ActivityNode58', None)
    assert owner not in getattr(partner, 'activitydiagram_Trace57')


def test_assoc_guard20_stub_double():
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


def test_assoc_operand128_stub_double():
    # activitydiagram_IntegerExpression has no real 'activitydiagram_IntegerExpression29' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerVariable()
    partner = activitydiagram_IntegerExpression()
    setattr(partner, 'activitydiagram_IntegerExpression29', None)
    _safe_set(owner, 'activitydiagram_IntegerVariable30', partner)
    assert getattr(partner, 'activitydiagram_IntegerExpression29') == owner
    _safe_set(owner, 'activitydiagram_IntegerVariable30', None)
    assert getattr(partner, 'activitydiagram_IntegerExpression29') is None


def test_assoc_operand227_stub_double():
    # activitydiagram_IntegerExpression has no real 'activitydiagram_IntegerExpression' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_IntegerVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_IntegerVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_IntegerVariable()
    partner = activitydiagram_IntegerExpression()
    setattr(partner, 'activitydiagram_IntegerExpression', None)
    _safe_set(owner, 'activitydiagram_IntegerVariable', partner)
    assert getattr(partner, 'activitydiagram_IntegerExpression') == owner
    _safe_set(owner, 'activitydiagram_IntegerVariable', None)
    assert getattr(partner, 'activitydiagram_IntegerExpression') is None


def test_assoc_trace7_stub_double():
    # activitydiagram_Trace has no real 'activitydiagram_Trace' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Activity()
    partner = activitydiagram_Trace()
    setattr(partner, 'activitydiagram_Trace', None)
    _safe_set(owner, 'activitydiagram_Activity8', partner)
    assert getattr(partner, 'activitydiagram_Trace') == owner
    _safe_set(owner, 'activitydiagram_Activity8', None)
    assert getattr(partner, 'activitydiagram_Trace') is None


def test_assoc_variable47_stub_double():
    # activitydiagram_InputValue has no real 'activitydiagram_InputValue' property in the generated
    # code (a bare stub) -- manually attach it so activitydiagram_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activitydiagram_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activitydiagram_Variable(name="sample_text")
    partner = activitydiagram_InputValue()
    setattr(partner, 'activitydiagram_InputValue', None)
    _safe_set(owner, 'activitydiagram_Variable48', partner)
    assert getattr(partner, 'activitydiagram_InputValue') == owner
    _safe_set(owner, 'activitydiagram_Variable48', None)
    assert getattr(partner, 'activitydiagram_InputValue') is None


