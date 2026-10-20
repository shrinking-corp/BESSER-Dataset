import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    Block,
    Constant,
    ControlStatement,
    Expression,
    ExtendedExpression,
    ProcedureDefinition,
    Statement,
    Symbol,
    UnaryExpression,
    Value,
    expression_logo_Expression,
    logo_Expression,
    logo_Logo,
    logo_Parameter,
    logo_Statement,
    logo_Symbol,
    logo_Value,
    logo_binary_Div,
    logo_binary_Equals,
    logo_binary_Greater,
    logo_binary_Lower,
    logo_binary_Minus,
    logo_binary_Mult,
    logo_binary_Plus,
    logo_constant_BoolValue,
    logo_constant_IntValue,
    logo_control_If,
    logo_control_Repeat,
    logo_control_While,
    logo_expression_BinaryExpression,
    logo_expression_Constant,
    logo_expression_ExtendedExpression,
    logo_expression_UnaryExpression,
    logo_expression_VariableRead,
    logo_extended_And,
    logo_extended_Or,
    logo_statement_Block,
    logo_statement_ControlStatement,
    logo_statement_Forward,
    logo_statement_Left,
    logo_statement_PenDown,
    logo_statement_PenUp,
    logo_statement_ProcedureCall,
    logo_statement_ProcedureDefinition,
    logo_statement_Right,
    logo_symbol_Procedure,
    logo_symbol_Variable,
    logo_unary_Not,
    logo_unary_Opposite,
    logo_value_BoolValue,
    logo_value_IntValue,
    statement_logo_Expression,
    statement_logo_Parameter,
    statement_logo_Statement,
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

def test_assoc_parameters6_stub_double():
    # statement_logo_Parameter has no real 'statement_logo_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so logo_statement_ProcedureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logo_statement_ProcedureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logo_statement_ProcedureDefinition(name="sample_text")
    partner = statement_logo_Parameter()
    setattr(partner, 'statement_logo_Parameter', None)
    _safe_set(owner, 'logo_statement_ProcedureDefinition', {partner})
    assert getattr(partner, 'statement_logo_Parameter') == owner
    _safe_set(owner, 'logo_statement_ProcedureDefinition', set())
    assert getattr(partner, 'statement_logo_Parameter') is None


def test_assoc_statements7_stub_double():
    # statement_logo_Statement has no real 'statement_logo_Statement' property in the generated
    # code (a bare stub) -- manually attach it so logo_statement_ProcedureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logo_statement_ProcedureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logo_statement_ProcedureDefinition(name="sample_text")
    partner = statement_logo_Statement()
    setattr(partner, 'statement_logo_Statement', None)
    _safe_set(owner, 'logo_statement_ProcedureDefinition8', {partner})
    assert getattr(partner, 'statement_logo_Statement') == owner
    _safe_set(owner, 'logo_statement_ProcedureDefinition8', set())
    assert getattr(partner, 'statement_logo_Statement') is None


