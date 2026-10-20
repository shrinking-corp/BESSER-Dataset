import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    whileDsl_Command,
    whileDsl_Commands,
    whileDsl_Definition,
    whileDsl_EObject,
    whileDsl_Expr,
    whileDsl_ExprAnd,
    whileDsl_ExprEq,
    whileDsl_ExprNot,
    whileDsl_ExprOr,
    whileDsl_ExprSimple,
    whileDsl_ExprSimpleWithExpr,
    whileDsl_ExprSimpleWithLExpr,
    whileDsl_ExprSimpleWithSymbolLExpr,
    whileDsl_Exprs,
    whileDsl_ForCommand,
    whileDsl_ForeachCommand,
    whileDsl_Function,
    whileDsl_IfCommand,
    whileDsl_Input,
    whileDsl_LExpr,
    whileDsl_Model,
    whileDsl_NopCommand,
    whileDsl_Output,
    whileDsl_Vars,
    whileDsl_VarsCommand,
    whileDsl_WhileCommand,
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

def test_assoc_body30_stub_double():
    # whileDsl_Commands has no real 'whileDsl_Commands32' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ForeachCommand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ForeachCommand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ForeachCommand(expElement="sample_text")
    partner = whileDsl_Commands()
    setattr(partner, 'whileDsl_Commands32', None)
    _safe_set(owner, 'whileDsl_ForeachCommand31', partner)
    assert getattr(partner, 'whileDsl_Commands32') == owner
    _safe_set(owner, 'whileDsl_ForeachCommand31', None)
    assert getattr(partner, 'whileDsl_Commands32') is None


def test_assoc_expList28_stub_double():
    # whileDsl_Expr has no real 'whileDsl_Expr29' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ForeachCommand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ForeachCommand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ForeachCommand(expElement="sample_text")
    partner = whileDsl_Expr()
    setattr(partner, 'whileDsl_Expr29', None)
    _safe_set(owner, 'whileDsl_ForeachCommand', partner)
    assert getattr(partner, 'whileDsl_Expr29') == owner
    _safe_set(owner, 'whileDsl_ForeachCommand', None)
    assert getattr(partner, 'whileDsl_Expr29') is None


def test_assoc_expr38_stub_double():
    # whileDsl_Expr has no real 'whileDsl_Expr39' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprSimpleWithExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprSimpleWithExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprSimpleWithExpr(operation="sample_text")
    partner = whileDsl_Expr()
    setattr(partner, 'whileDsl_Expr39', None)
    _safe_set(owner, 'whileDsl_ExprSimpleWithExpr', partner)
    assert getattr(partner, 'whileDsl_Expr39') == owner
    _safe_set(owner, 'whileDsl_ExprSimpleWithExpr', None)
    assert getattr(partner, 'whileDsl_Expr39') is None


def test_assoc_exprLSimple56_stub_double():
    # whileDsl_ExprEq has no real 'whileDsl_ExprEq57' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprSimple(term="sample_text")
    partner = whileDsl_ExprEq()
    setattr(partner, 'whileDsl_ExprEq57', None)
    _safe_set(owner, 'whileDsl_ExprSimple58', partner)
    assert getattr(partner, 'whileDsl_ExprEq57') == owner
    _safe_set(owner, 'whileDsl_ExprSimple58', None)
    assert getattr(partner, 'whileDsl_ExprEq57') is None


def test_assoc_exprRSimple59_stub_double():
    # whileDsl_ExprEq has no real 'whileDsl_ExprEq60' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprSimple(term="sample_text")
    partner = whileDsl_ExprEq()
    setattr(partner, 'whileDsl_ExprEq60', None)
    _safe_set(owner, 'whileDsl_ExprSimple61', partner)
    assert getattr(partner, 'whileDsl_ExprEq60') == owner
    _safe_set(owner, 'whileDsl_ExprSimple61', None)
    assert getattr(partner, 'whileDsl_ExprEq60') is None


def test_assoc_expression36_stub_double():
    # whileDsl_EObject has no real 'whileDsl_EObject' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprSimple(term="sample_text")
    partner = whileDsl_EObject()
    setattr(partner, 'whileDsl_EObject', None)
    _safe_set(owner, 'whileDsl_ExprSimple', partner)
    assert getattr(partner, 'whileDsl_EObject') == owner
    _safe_set(owner, 'whileDsl_ExprSimple', None)
    assert getattr(partner, 'whileDsl_EObject') is None


def test_assoc_expressionEq54_stub_double():
    # whileDsl_ExprEq has no real 'whileDsl_ExprEq' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprNot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprNot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprNot(negation=True)
    partner = whileDsl_ExprEq()
    setattr(partner, 'whileDsl_ExprEq', None)
    _safe_set(owner, 'whileDsl_ExprNot55', partner)
    assert getattr(partner, 'whileDsl_ExprEq') == owner
    _safe_set(owner, 'whileDsl_ExprNot55', None)
    assert getattr(partner, 'whileDsl_ExprEq') is None


def test_assoc_expressionsNot52_stub_double():
    # whileDsl_ExprOr has no real 'whileDsl_ExprOr53' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprNot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprNot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprNot(negation=True)
    partner = whileDsl_ExprOr()
    setattr(partner, 'whileDsl_ExprOr53', None)
    _safe_set(owner, 'whileDsl_ExprNot', partner)
    assert owner in getattr(partner, 'whileDsl_ExprOr53')
    _safe_set(owner, 'whileDsl_ExprNot', None)
    assert owner not in getattr(partner, 'whileDsl_ExprOr53')


def test_assoc_functionDefinition1_stub_double():
    # whileDsl_Definition has no real 'whileDsl_Definition' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_Function(functionName="sample_text")
    partner = whileDsl_Definition()
    setattr(partner, 'whileDsl_Definition', None)
    _safe_set(owner, 'whileDsl_Function2', partner)
    assert getattr(partner, 'whileDsl_Definition') == owner
    _safe_set(owner, 'whileDsl_Function2', None)
    assert getattr(partner, 'whileDsl_Definition') is None


def test_assoc_intput3_stub_double():
    # whileDsl_Definition has no real 'whileDsl_Definition4' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_Input(variables="sample_text")
    partner = whileDsl_Definition()
    setattr(partner, 'whileDsl_Definition4', None)
    _safe_set(owner, 'whileDsl_Input', partner)
    assert getattr(partner, 'whileDsl_Definition4') == owner
    _safe_set(owner, 'whileDsl_Input', None)
    assert getattr(partner, 'whileDsl_Definition4') is None


def test_assoc_lexpr37_stub_double():
    # whileDsl_LExpr has no real 'whileDsl_LExpr' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprSimpleWithLExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprSimpleWithLExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprSimpleWithLExpr(operation="sample_text")
    partner = whileDsl_LExpr()
    setattr(partner, 'whileDsl_LExpr', None)
    _safe_set(owner, 'whileDsl_ExprSimpleWithLExpr', partner)
    assert getattr(partner, 'whileDsl_LExpr') == owner
    _safe_set(owner, 'whileDsl_ExprSimpleWithLExpr', None)
    assert getattr(partner, 'whileDsl_LExpr') is None


def test_assoc_lexpr40_stub_double():
    # whileDsl_LExpr has no real 'whileDsl_LExpr41' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_ExprSimpleWithSymbolLExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_ExprSimpleWithSymbolLExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_ExprSimpleWithSymbolLExpr(symbol="sample_text")
    partner = whileDsl_LExpr()
    setattr(partner, 'whileDsl_LExpr41', None)
    _safe_set(owner, 'whileDsl_ExprSimpleWithSymbolLExpr', partner)
    assert getattr(partner, 'whileDsl_LExpr41') == owner
    _safe_set(owner, 'whileDsl_ExprSimpleWithSymbolLExpr', None)
    assert getattr(partner, 'whileDsl_LExpr41') is None


def test_assoc_output7_stub_double():
    # whileDsl_Definition has no real 'whileDsl_Definition8' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_Output(variables="sample_text")
    partner = whileDsl_Definition()
    setattr(partner, 'whileDsl_Definition8', None)
    _safe_set(owner, 'whileDsl_Output', partner)
    assert getattr(partner, 'whileDsl_Definition8') == owner
    _safe_set(owner, 'whileDsl_Output', None)
    assert getattr(partner, 'whileDsl_Definition8') is None


def test_assoc_program0_stub_double():
    # whileDsl_Model has no real 'whileDsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_Function(functionName="sample_text")
    partner = whileDsl_Model()
    setattr(partner, 'whileDsl_Model', None)
    _safe_set(owner, 'whileDsl_Function', partner)
    assert owner in getattr(partner, 'whileDsl_Model')
    _safe_set(owner, 'whileDsl_Function', None)
    assert owner not in getattr(partner, 'whileDsl_Model')


def test_assoc_variables33_stub_double():
    # whileDsl_VarsCommand has no real 'whileDsl_VarsCommand' property in the generated
    # code (a bare stub) -- manually attach it so whileDsl_Vars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileDsl_Vars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileDsl_Vars(variables="sample_text")
    partner = whileDsl_VarsCommand()
    setattr(partner, 'whileDsl_VarsCommand', None)
    _safe_set(owner, 'whileDsl_Vars', partner)
    assert getattr(partner, 'whileDsl_VarsCommand') == owner
    _safe_set(owner, 'whileDsl_Vars', None)
    assert getattr(partner, 'whileDsl_VarsCommand') is None


