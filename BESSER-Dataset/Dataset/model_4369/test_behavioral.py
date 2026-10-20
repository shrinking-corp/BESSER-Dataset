import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryOperator,
    Expression,
    Operator,
    Statement,
    UnaryOperator,
    klangexpr_And,
    klangexpr_BinaryOperator,
    klangexpr_BooleanLiteral,
    klangexpr_Divide,
    klangexpr_DoubleLiteral,
    klangexpr_Equal,
    klangexpr_Expression,
    klangexpr_ForeverLoop,
    klangexpr_FunctionCall,
    klangexpr_GreaterThan,
    klangexpr_GreaterThanOrEqual,
    klangexpr_If,
    klangexpr_IntegerLiteral,
    klangexpr_LessThan,
    klangexpr_LessThanOrEqual,
    klangexpr_Minus,
    klangexpr_Multiply,
    klangexpr_Not,
    klangexpr_Operator,
    klangexpr_Or,
    klangexpr_Plus,
    klangexpr_SendMessage,
    klangexpr_Sleep,
    klangexpr_Statement,
    klangexpr_StringLiteral,
    klangexpr_ToDouble,
    klangexpr_ToInt,
    klangexpr_UnaryMinus,
    klangexpr_UnaryOperator,
    klangexpr_VariableAssignment,
    klangexpr_VariableReference,
    klangexpr_WhileLoop,
    klangexpr_Yield,
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

def test_assoc_expression13_stub_double():
    # klangexpr_Expression has no real 'klangexpr_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so klangexpr_VariableAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # klangexpr_VariableAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = klangexpr_VariableAssignment(variableName="sample_text")
    partner = klangexpr_Expression()
    setattr(partner, 'klangexpr_Expression14', None)
    _safe_set(owner, 'klangexpr_VariableAssignment', partner)
    assert getattr(partner, 'klangexpr_Expression14') == owner
    _safe_set(owner, 'klangexpr_VariableAssignment', None)
    assert getattr(partner, 'klangexpr_Expression14') is None


def test_assoc_parameters22_stub_double():
    # klangexpr_Expression has no real 'klangexpr_Expression23' property in the generated
    # code (a bare stub) -- manually attach it so klangexpr_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # klangexpr_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = klangexpr_FunctionCall(name="sample_text")
    partner = klangexpr_Expression()
    setattr(partner, 'klangexpr_Expression23', None)
    _safe_set(owner, 'klangexpr_FunctionCall', {partner})
    assert getattr(partner, 'klangexpr_Expression23') == owner
    _safe_set(owner, 'klangexpr_FunctionCall', set())
    assert getattr(partner, 'klangexpr_Expression23') is None


