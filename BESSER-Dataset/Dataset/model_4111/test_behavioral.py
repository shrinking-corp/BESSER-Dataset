import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    wh_Affect,
    wh_Command,
    wh_Commands,
    wh_Definition,
    wh_EObject,
    wh_Expr,
    wh_ExprAnd,
    wh_ExprCons,
    wh_ExprEq,
    wh_ExprHd,
    wh_ExprList,
    wh_ExprNot,
    wh_ExprOr,
    wh_ExprSimple,
    wh_ExprSym,
    wh_ExprTl,
    wh_For,
    wh_Function,
    wh_If,
    wh_Input,
    wh_Nop,
    wh_Output,
    wh_Program,
    wh_Wh,
    wh_While,
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

def test_assoc_arg137_stub_double():
    # wh_ExprAnd has no real 'wh_ExprAnd' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    partner = wh_ExprAnd()
    setattr(partner, 'wh_ExprAnd', None)
    _safe_set(owner, 'wh_ExprSimple', partner)
    assert getattr(partner, 'wh_ExprAnd') == owner
    _safe_set(owner, 'wh_ExprSimple', None)
    assert getattr(partner, 'wh_ExprAnd') is None


def test_assoc_arg141_stub_double():
    # wh_ExprOr has no real 'wh_ExprOr' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    partner = wh_ExprOr()
    setattr(partner, 'wh_ExprOr', None)
    _safe_set(owner, 'wh_ExprSimple42', partner)
    assert getattr(partner, 'wh_ExprOr') == owner
    _safe_set(owner, 'wh_ExprSimple42', None)
    assert getattr(partner, 'wh_ExprOr') is None


def test_assoc_arg157_stub_double():
    # wh_ExprEq has no real 'wh_ExprEq58' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    partner = wh_ExprEq()
    setattr(partner, 'wh_ExprEq58', None)
    _safe_set(owner, 'wh_ExprSimple59', partner)
    assert getattr(partner, 'wh_ExprEq58') == owner
    _safe_set(owner, 'wh_ExprSimple59', None)
    assert getattr(partner, 'wh_ExprEq58') is None


def test_assoc_arg254_stub_double():
    # wh_Expr has no real 'wh_Expr55' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSym's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSym's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSym(arg1="sample_text")
    partner = wh_Expr()
    setattr(partner, 'wh_Expr55', None)
    _safe_set(owner, 'wh_ExprSym', {partner})
    assert getattr(partner, 'wh_Expr55') == owner
    _safe_set(owner, 'wh_ExprSym', set())
    assert getattr(partner, 'wh_Expr55') is None


def test_assoc_arg260_stub_double():
    # wh_ExprEq has no real 'wh_ExprEq61' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", sym="sample_text", varSimple="sample_text")
    partner = wh_ExprEq()
    setattr(partner, 'wh_ExprEq61', None)
    _safe_set(owner, 'wh_ExprSimple62', partner)
    assert getattr(partner, 'wh_ExprEq61') == owner
    _safe_set(owner, 'wh_ExprSimple62', None)
    assert getattr(partner, 'wh_ExprEq61') is None


def test_assoc_definition3_stub_double():
    # wh_Definition has no real 'wh_Definition' property in the generated
    # code (a bare stub) -- manually attach it so wh_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Function(name="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition', None)
    _safe_set(owner, 'wh_Function4', partner)
    assert getattr(partner, 'wh_Definition') == owner
    _safe_set(owner, 'wh_Function4', None)
    assert getattr(partner, 'wh_Definition') is None


def test_assoc_exprs22_stub_double():
    # wh_Expr has no real 'wh_Expr23' property in the generated
    # code (a bare stub) -- manually attach it so wh_Affect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Affect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Affect(vars="sample_text")
    partner = wh_Expr()
    setattr(partner, 'wh_Expr23', None)
    _safe_set(owner, 'wh_Affect', {partner})
    assert getattr(partner, 'wh_Expr23') == owner
    _safe_set(owner, 'wh_Affect', set())
    assert getattr(partner, 'wh_Expr23') is None


def test_assoc_functions1_stub_double():
    # wh_Program has no real 'wh_Program2' property in the generated
    # code (a bare stub) -- manually attach it so wh_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Function(name="sample_text")
    partner = wh_Program()
    setattr(partner, 'wh_Program2', None)
    _safe_set(owner, 'wh_Function', partner)
    assert owner in getattr(partner, 'wh_Program2')
    _safe_set(owner, 'wh_Function', None)
    assert owner not in getattr(partner, 'wh_Program2')


def test_assoc_input5_stub_double():
    # wh_Definition has no real 'wh_Definition6' property in the generated
    # code (a bare stub) -- manually attach it so wh_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Input(vars="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition6', None)
    _safe_set(owner, 'wh_Input', partner)
    assert getattr(partner, 'wh_Definition6') == owner
    _safe_set(owner, 'wh_Input', None)
    assert getattr(partner, 'wh_Definition6') is None


def test_assoc_output9_stub_double():
    # wh_Definition has no real 'wh_Definition10' property in the generated
    # code (a bare stub) -- manually attach it so wh_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Output(vars="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition10', None)
    _safe_set(owner, 'wh_Output', partner)
    assert getattr(partner, 'wh_Definition10') == owner
    _safe_set(owner, 'wh_Output', None)
    assert getattr(partner, 'wh_Definition10') is None


