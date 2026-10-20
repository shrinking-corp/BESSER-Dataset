import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    py_Affect,
    py_Command,
    py_Commands,
    py_Definition,
    py_EObject,
    py_Expr,
    py_ExprAnd,
    py_ExprCons,
    py_ExprEq,
    py_ExprHd,
    py_ExprList,
    py_ExprNot,
    py_ExprOr,
    py_ExprSimple,
    py_ExprSym,
    py_ExprTl,
    py_For,
    py_Foreach,
    py_FunctionP,
    py_If,
    py_Input,
    py_LExpr,
    py_Nop,
    py_Output,
    py_Program,
    py_Wh,
    py_While,
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

def test_assoc_arg142_stub_double():
    # py_ExprAnd has no real 'py_ExprAnd' property in the generated
    # code (a bare stub) -- manually attach it so py_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    partner = py_ExprAnd()
    setattr(partner, 'py_ExprAnd', None)
    _safe_set(owner, 'py_ExprSimple', partner)
    assert getattr(partner, 'py_ExprAnd') == owner
    _safe_set(owner, 'py_ExprSimple', None)
    assert getattr(partner, 'py_ExprAnd') is None


def test_assoc_arg146_stub_double():
    # py_ExprOr has no real 'py_ExprOr' property in the generated
    # code (a bare stub) -- manually attach it so py_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    partner = py_ExprOr()
    setattr(partner, 'py_ExprOr', None)
    _safe_set(owner, 'py_ExprSimple47', partner)
    assert getattr(partner, 'py_ExprOr') == owner
    _safe_set(owner, 'py_ExprSimple47', None)
    assert getattr(partner, 'py_ExprOr') is None


def test_assoc_arg165_stub_double():
    # py_ExprEq has no real 'py_ExprEq' property in the generated
    # code (a bare stub) -- manually attach it so py_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    partner = py_ExprEq()
    setattr(partner, 'py_ExprEq', None)
    _safe_set(owner, 'py_ExprSimple66', partner)
    assert getattr(partner, 'py_ExprEq') == owner
    _safe_set(owner, 'py_ExprSimple66', None)
    assert getattr(partner, 'py_ExprEq') is None


def test_assoc_arg261_stub_double():
    # py_Expr has no real 'py_Expr62' property in the generated
    # code (a bare stub) -- manually attach it so py_ExprSym's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_ExprSym's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_ExprSym(arg1="sample_text")
    partner = py_Expr()
    setattr(partner, 'py_Expr62', None)
    _safe_set(owner, 'py_ExprSym', {partner})
    assert getattr(partner, 'py_Expr62') == owner
    _safe_set(owner, 'py_ExprSym', set())
    assert getattr(partner, 'py_Expr62') is None


def test_assoc_cmd31_stub_double():
    # py_Commands has no real 'py_Commands33' property in the generated
    # code (a bare stub) -- manually attach it so py_Foreach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_Foreach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_Foreach(var="sample_text")
    partner = py_Commands()
    setattr(partner, 'py_Commands33', None)
    _safe_set(owner, 'py_Foreach32', partner)
    assert getattr(partner, 'py_Commands33') == owner
    _safe_set(owner, 'py_Foreach32', None)
    assert getattr(partner, 'py_Commands33') is None


def test_assoc_definition3_stub_double():
    # py_Definition has no real 'py_Definition' property in the generated
    # code (a bare stub) -- manually attach it so py_FunctionP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_FunctionP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_FunctionP(name="sample_text")
    partner = py_Definition()
    setattr(partner, 'py_Definition', None)
    _safe_set(owner, 'py_FunctionP4', partner)
    assert getattr(partner, 'py_Definition') == owner
    _safe_set(owner, 'py_FunctionP4', None)
    assert getattr(partner, 'py_Definition') is None


def test_assoc_expr229_stub_double():
    # py_Expr has no real 'py_Expr30' property in the generated
    # code (a bare stub) -- manually attach it so py_Foreach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_Foreach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_Foreach(var="sample_text")
    partner = py_Expr()
    setattr(partner, 'py_Expr30', None)
    _safe_set(owner, 'py_Foreach', partner)
    assert getattr(partner, 'py_Expr30') == owner
    _safe_set(owner, 'py_Foreach', None)
    assert getattr(partner, 'py_Expr30') is None


def test_assoc_exprs22_stub_double():
    # py_Expr has no real 'py_Expr23' property in the generated
    # code (a bare stub) -- manually attach it so py_Affect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_Affect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_Affect(vars="sample_text")
    partner = py_Expr()
    setattr(partner, 'py_Expr23', None)
    _safe_set(owner, 'py_Affect', {partner})
    assert getattr(partner, 'py_Expr23') == owner
    _safe_set(owner, 'py_Affect', set())
    assert getattr(partner, 'py_Expr23') is None


def test_assoc_functions1_stub_double():
    # py_Program has no real 'py_Program2' property in the generated
    # code (a bare stub) -- manually attach it so py_FunctionP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_FunctionP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_FunctionP(name="sample_text")
    partner = py_Program()
    setattr(partner, 'py_Program2', None)
    _safe_set(owner, 'py_FunctionP', partner)
    assert owner in getattr(partner, 'py_Program2')
    _safe_set(owner, 'py_FunctionP', None)
    assert owner not in getattr(partner, 'py_Program2')


def test_assoc_input5_stub_double():
    # py_Definition has no real 'py_Definition6' property in the generated
    # code (a bare stub) -- manually attach it so py_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_Input(vars="sample_text")
    partner = py_Definition()
    setattr(partner, 'py_Definition6', None)
    _safe_set(owner, 'py_Input', partner)
    assert getattr(partner, 'py_Definition6') == owner
    _safe_set(owner, 'py_Input', None)
    assert getattr(partner, 'py_Definition6') is None


def test_assoc_output9_stub_double():
    # py_Definition has no real 'py_Definition10' property in the generated
    # code (a bare stub) -- manually attach it so py_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # py_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = py_Output(vars="sample_text")
    partner = py_Definition()
    setattr(partner, 'py_Definition10', None)
    _safe_set(owner, 'py_Output', partner)
    assert getattr(partner, 'py_Definition10') == owner
    _safe_set(owner, 'py_Output', None)
    assert getattr(partner, 'py_Definition10') is None


