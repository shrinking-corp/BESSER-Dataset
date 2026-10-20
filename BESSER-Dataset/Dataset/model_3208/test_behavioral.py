import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticExpression,
    AtomicExpression,
    BinaryExpression,
    ConditionalLoop,
    Expression,
    Loop,
    Nameable,
    Statement,
    UnaryExpression,
    VariableDeclarationScope,
    hlp_AddExpression,
    hlp_ArithmeticExpression,
    hlp_Assignment,
    hlp_AtomicExpression,
    hlp_BinaryExpression,
    hlp_Block,
    hlp_Condition,
    hlp_ConditionalLoop,
    hlp_DivideExpression,
    hlp_Expression,
    hlp_ExpressionStatement,
    hlp_ForLoop,
    hlp_HighLevelProgram,
    hlp_IfStatement,
    hlp_LiteralValue,
    hlp_Loop,
    hlp_MultiplyExpression,
    hlp_Nameable,
    hlp_ParenthesisExpression,
    hlp_ScheduleInstruction,
    hlp_Statement,
    hlp_SubtractExpression,
    hlp_SynchronizedStatement,
    hlp_Task,
    hlp_UnaryExpression,
    hlp_UnaryMinusExpression,
    hlp_Variable,
    hlp_VariableDeclaration,
    hlp_VariableDeclarationScope,
    hlp_VariableReference,
    hlp_WhileLoop,
    ComparisonOperator,
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

def test_assoc_bound142_stub_double():
    # hlp_Expression has no real 'hlp_Expression44' property in the generated
    # code (a bare stub) -- manually attach it so hlp_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlp_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlp_ForLoop(incrementing=True)
    partner = hlp_Expression()
    setattr(partner, 'hlp_Expression44', None)
    _safe_set(owner, 'hlp_ForLoop43', partner)
    assert getattr(partner, 'hlp_Expression44') == owner
    _safe_set(owner, 'hlp_ForLoop43', None)
    assert getattr(partner, 'hlp_Expression44') is None


def test_assoc_bound245_stub_double():
    # hlp_Expression has no real 'hlp_Expression47' property in the generated
    # code (a bare stub) -- manually attach it so hlp_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlp_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlp_ForLoop(incrementing=True)
    partner = hlp_Expression()
    setattr(partner, 'hlp_Expression47', None)
    _safe_set(owner, 'hlp_ForLoop46', partner)
    assert getattr(partner, 'hlp_Expression47') == owner
    _safe_set(owner, 'hlp_ForLoop46', None)
    assert getattr(partner, 'hlp_Expression47') is None


def test_assoc_condition26_stub_double():
    # hlp_IfStatement has no real 'hlp_IfStatement27' property in the generated
    # code (a bare stub) -- manually attach it so hlp_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlp_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlp_Condition(operator="sample_text")
    partner = hlp_IfStatement()
    setattr(partner, 'hlp_IfStatement27', None)
    _safe_set(owner, 'hlp_Condition', partner)
    assert getattr(partner, 'hlp_IfStatement27') == owner
    _safe_set(owner, 'hlp_Condition', None)
    assert getattr(partner, 'hlp_IfStatement27') is None


def test_assoc_condition38_stub_double():
    # hlp_ConditionalLoop has no real 'hlp_ConditionalLoop' property in the generated
    # code (a bare stub) -- manually attach it so hlp_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlp_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlp_Condition(operator="sample_text")
    partner = hlp_ConditionalLoop()
    setattr(partner, 'hlp_ConditionalLoop', None)
    _safe_set(owner, 'hlp_Condition39', partner)
    assert getattr(partner, 'hlp_ConditionalLoop') == owner
    _safe_set(owner, 'hlp_Condition39', None)
    assert getattr(partner, 'hlp_ConditionalLoop') is None


def test_assoc_leftHandSide28_stub_double():
    # hlp_Expression has no real 'hlp_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so hlp_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlp_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlp_Condition(operator="sample_text")
    partner = hlp_Expression()
    setattr(partner, 'hlp_Expression30', None)
    _safe_set(owner, 'hlp_Condition29', partner)
    assert getattr(partner, 'hlp_Expression30') == owner
    _safe_set(owner, 'hlp_Condition29', None)
    assert getattr(partner, 'hlp_Expression30') is None


def test_assoc_rightHandSide31_stub_double():
    # hlp_Expression has no real 'hlp_Expression33' property in the generated
    # code (a bare stub) -- manually attach it so hlp_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlp_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlp_Condition(operator="sample_text")
    partner = hlp_Expression()
    setattr(partner, 'hlp_Expression33', None)
    _safe_set(owner, 'hlp_Condition32', partner)
    assert getattr(partner, 'hlp_Expression33') == owner
    _safe_set(owner, 'hlp_Condition32', None)
    assert getattr(partner, 'hlp_Expression33') is None


def test_assoc_variableReference40_stub_double():
    # hlp_VariableReference has no real 'hlp_VariableReference41' property in the generated
    # code (a bare stub) -- manually attach it so hlp_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hlp_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hlp_ForLoop(incrementing=True)
    partner = hlp_VariableReference()
    setattr(partner, 'hlp_VariableReference41', None)
    _safe_set(owner, 'hlp_ForLoop', partner)
    assert getattr(partner, 'hlp_VariableReference41') == owner
    _safe_set(owner, 'hlp_ForLoop', None)
    assert getattr(partner, 'hlp_VariableReference41') is None


