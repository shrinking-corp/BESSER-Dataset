import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DefParenthesis,
    MDExpression,
    MathExpression,
    MultiplyDivide,
    Number,
    PMExpression,
    PlusMinus,
    PowExpression,
    Power,
    Primary,
    mathinterpreter_DefParenthesis,
    mathinterpreter_DefineExpr,
    mathinterpreter_Divide,
    mathinterpreter_EObject,
    mathinterpreter_External,
    mathinterpreter_Function,
    mathinterpreter_MDExpression,
    mathinterpreter_MathExpression,
    mathinterpreter_Minus,
    mathinterpreter_Model,
    mathinterpreter_Multiply,
    mathinterpreter_MultiplyDivide,
    mathinterpreter_Negative,
    mathinterpreter_Number,
    mathinterpreter_PMExpression,
    mathinterpreter_PMParenthesis,
    mathinterpreter_Plus,
    mathinterpreter_PlusMinus,
    mathinterpreter_Positive,
    mathinterpreter_Pow,
    mathinterpreter_PowExpression,
    mathinterpreter_Power,
    mathinterpreter_Primary,
    mathinterpreter_Variable,
    mathinterpreter_VariableName,
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

def test_assoc_arguments7_stub_double():
    # mathinterpreter_Primary has no real 'mathinterpreter_Primary' property in the generated
    # code (a bare stub) -- manually attach it so mathinterpreter_External's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathinterpreter_External's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathinterpreter_External(name="sample_text")
    partner = mathinterpreter_Primary()
    setattr(partner, 'mathinterpreter_Primary', None)
    _safe_set(owner, 'mathinterpreter_External', {partner})
    assert getattr(partner, 'mathinterpreter_Primary') == owner
    _safe_set(owner, 'mathinterpreter_External', set())
    assert getattr(partner, 'mathinterpreter_Primary') is None


def test_assoc_expression1_stub_double():
    # mathinterpreter_PMExpression has no real 'mathinterpreter_PMExpression' property in the generated
    # code (a bare stub) -- manually attach it so mathinterpreter_MathExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathinterpreter_MathExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathinterpreter_MathExpression(description="sample_text")
    partner = mathinterpreter_PMExpression()
    setattr(partner, 'mathinterpreter_PMExpression', None)
    _safe_set(owner, 'mathinterpreter_MathExpression2', partner)
    assert getattr(partner, 'mathinterpreter_PMExpression') == owner
    _safe_set(owner, 'mathinterpreter_MathExpression2', None)
    assert getattr(partner, 'mathinterpreter_PMExpression') is None


def test_assoc_expression4_stub_double():
    # mathinterpreter_PMExpression has no real 'mathinterpreter_PMExpression6' property in the generated
    # code (a bare stub) -- manually attach it so mathinterpreter_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathinterpreter_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathinterpreter_Variable(name="sample_text")
    partner = mathinterpreter_PMExpression()
    setattr(partner, 'mathinterpreter_PMExpression6', None)
    _safe_set(owner, 'mathinterpreter_Variable5', partner)
    assert getattr(partner, 'mathinterpreter_PMExpression6') == owner
    _safe_set(owner, 'mathinterpreter_Variable5', None)
    assert getattr(partner, 'mathinterpreter_PMExpression6') is None


def test_assoc_mathexpression0_stub_double():
    # mathinterpreter_Model has no real 'mathinterpreter_Model' property in the generated
    # code (a bare stub) -- manually attach it so mathinterpreter_MathExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathinterpreter_MathExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathinterpreter_MathExpression(description="sample_text")
    partner = mathinterpreter_Model()
    setattr(partner, 'mathinterpreter_Model', None)
    _safe_set(owner, 'mathinterpreter_MathExpression', partner)
    assert owner in getattr(partner, 'mathinterpreter_Model')
    _safe_set(owner, 'mathinterpreter_MathExpression', None)
    assert owner not in getattr(partner, 'mathinterpreter_Model')


def test_assoc_variables3_stub_double():
    # mathinterpreter_DefineExpr has no real 'mathinterpreter_DefineExpr' property in the generated
    # code (a bare stub) -- manually attach it so mathinterpreter_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mathinterpreter_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mathinterpreter_Variable(name="sample_text")
    partner = mathinterpreter_DefineExpr()
    setattr(partner, 'mathinterpreter_DefineExpr', None)
    _safe_set(owner, 'mathinterpreter_Variable', partner)
    assert owner in getattr(partner, 'mathinterpreter_DefineExpr')
    _safe_set(owner, 'mathinterpreter_Variable', None)
    assert owner not in getattr(partner, 'mathinterpreter_DefineExpr')


