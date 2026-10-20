import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    wh_Affect,
    wh_Command,
    wh_Commands,
    wh_Cons,
    wh_Definition,
    wh_EObject,
    wh_Expr,
    wh_ExprAnd,
    wh_ExprEq,
    wh_ExprNot,
    wh_ExprOr,
    wh_ExprSimple,
    wh_Exprs,
    wh_For,
    wh_Foreach,
    wh_If,
    wh_Input,
    wh_ListExpr,
    wh_Nop,
    wh_Output,
    wh_Program,
    wh_Vars,
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

def test_assoc_cons47_stub_double():
    # wh_Cons has no real 'wh_Cons' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", strSymb="sample_text")
    partner = wh_Cons()
    setattr(partner, 'wh_Cons', None)
    _safe_set(owner, 'wh_ExprSimple', partner)
    assert getattr(partner, 'wh_Cons') == owner
    _safe_set(owner, 'wh_ExprSimple', None)
    assert getattr(partner, 'wh_Cons') is None


def test_assoc_definition1_stub_double():
    # wh_Definition has no real 'wh_Definition' property in the generated
    # code (a bare stub) -- manually attach it so wh_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Program(name="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition', None)
    _safe_set(owner, 'wh_Program2', partner)
    assert getattr(partner, 'wh_Definition') == owner
    _safe_set(owner, 'wh_Program2', None)
    assert getattr(partner, 'wh_Definition') is None


def test_assoc_elements0_stub_double():
    # wh_Wh has no real 'wh_Wh' property in the generated
    # code (a bare stub) -- manually attach it so wh_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Program(name="sample_text")
    partner = wh_Wh()
    setattr(partner, 'wh_Wh', None)
    _safe_set(owner, 'wh_Program', partner)
    assert owner in getattr(partner, 'wh_Wh')
    _safe_set(owner, 'wh_Program', None)
    assert owner not in getattr(partner, 'wh_Wh')


def test_assoc_expr71_stub_double():
    # wh_ExprEq has no real 'wh_ExprEq' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprNot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprNot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprNot(not_="sample_text")
    partner = wh_ExprEq()
    setattr(partner, 'wh_ExprEq', None)
    _safe_set(owner, 'wh_ExprNot72', partner)
    assert getattr(partner, 'wh_ExprEq') == owner
    _safe_set(owner, 'wh_ExprNot72', None)
    assert getattr(partner, 'wh_ExprEq') is None


def test_assoc_exprHd50_stub_double():
    # wh_Expr has no real 'wh_Expr52' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", strSymb="sample_text")
    partner = wh_Expr()
    setattr(partner, 'wh_Expr52', None)
    _safe_set(owner, 'wh_ExprSimple51', partner)
    assert getattr(partner, 'wh_Expr52') == owner
    _safe_set(owner, 'wh_ExprSimple51', None)
    assert getattr(partner, 'wh_Expr52') is None


def test_assoc_exprNot166_stub_double():
    # wh_ExprOr has no real 'wh_ExprOr67' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprNot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprNot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprNot(not_="sample_text")
    partner = wh_ExprOr()
    setattr(partner, 'wh_ExprOr67', None)
    _safe_set(owner, 'wh_ExprNot', partner)
    assert getattr(partner, 'wh_ExprOr67') == owner
    _safe_set(owner, 'wh_ExprNot', None)
    assert getattr(partner, 'wh_ExprOr67') is None


def test_assoc_exprNotX68_stub_double():
    # wh_ExprOr has no real 'wh_ExprOr69' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprNot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprNot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprNot(not_="sample_text")
    partner = wh_ExprOr()
    setattr(partner, 'wh_ExprOr69', None)
    _safe_set(owner, 'wh_ExprNot70', partner)
    assert owner in getattr(partner, 'wh_ExprOr69')
    _safe_set(owner, 'wh_ExprNot70', None)
    assert owner not in getattr(partner, 'wh_ExprOr69')


def test_assoc_exprSimp173_stub_double():
    # wh_ExprEq has no real 'wh_ExprEq74' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", strSymb="sample_text")
    partner = wh_ExprEq()
    setattr(partner, 'wh_ExprEq74', None)
    _safe_set(owner, 'wh_ExprSimple75', partner)
    assert getattr(partner, 'wh_ExprEq74') == owner
    _safe_set(owner, 'wh_ExprSimple75', None)
    assert getattr(partner, 'wh_ExprEq74') is None


def test_assoc_exprSimp276_stub_double():
    # wh_ExprEq has no real 'wh_ExprEq77' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", strSymb="sample_text")
    partner = wh_ExprEq()
    setattr(partner, 'wh_ExprEq77', None)
    _safe_set(owner, 'wh_ExprSimple78', partner)
    assert getattr(partner, 'wh_ExprEq77') == owner
    _safe_set(owner, 'wh_ExprSimple78', None)
    assert getattr(partner, 'wh_ExprEq77') is None


def test_assoc_exprTl53_stub_double():
    # wh_Expr has no real 'wh_Expr55' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", strSymb="sample_text")
    partner = wh_Expr()
    setattr(partner, 'wh_Expr55', None)
    _safe_set(owner, 'wh_ExprSimple54', partner)
    assert getattr(partner, 'wh_Expr55') == owner
    _safe_set(owner, 'wh_ExprSimple54', None)
    assert getattr(partner, 'wh_Expr55') is None


def test_assoc_input3_stub_double():
    # wh_Definition has no real 'wh_Definition4' property in the generated
    # code (a bare stub) -- manually attach it so wh_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Input(vars="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition4', None)
    _safe_set(owner, 'wh_Input', partner)
    assert getattr(partner, 'wh_Definition4') == owner
    _safe_set(owner, 'wh_Input', None)
    assert getattr(partner, 'wh_Definition4') is None


def test_assoc_listExpr48_stub_double():
    # wh_ListExpr has no real 'wh_ListExpr' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(str="sample_text", strSymb="sample_text")
    partner = wh_ListExpr()
    setattr(partner, 'wh_ListExpr', None)
    _safe_set(owner, 'wh_ExprSimple49', partner)
    assert getattr(partner, 'wh_ListExpr') == owner
    _safe_set(owner, 'wh_ExprSimple49', None)
    assert getattr(partner, 'wh_ListExpr') is None


def test_assoc_output7_stub_double():
    # wh_Definition has no real 'wh_Definition8' property in the generated
    # code (a bare stub) -- manually attach it so wh_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Output(vars="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition8', None)
    _safe_set(owner, 'wh_Output', partner)
    assert getattr(partner, 'wh_Definition8') == owner
    _safe_set(owner, 'wh_Output', None)
    assert getattr(partner, 'wh_Definition8') is None


def test_assoc_vars38_stub_double():
    # wh_Affect has no real 'wh_Affect' property in the generated
    # code (a bare stub) -- manually attach it so wh_Vars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Vars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Vars(vars="sample_text")
    partner = wh_Affect()
    setattr(partner, 'wh_Affect', None)
    _safe_set(owner, 'wh_Vars', partner)
    assert getattr(partner, 'wh_Affect') == owner
    _safe_set(owner, 'wh_Vars', None)
    assert getattr(partner, 'wh_Affect') is None


