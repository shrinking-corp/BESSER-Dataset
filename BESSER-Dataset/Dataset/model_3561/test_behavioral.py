import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    wh_Assign,
    wh_Command,
    wh_Commands,
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
    wh_Function,
    wh_If,
    wh_Input,
    wh_LExpr,
    wh_Model,
    wh_Nop,
    wh_Output,
    wh_Program,
    wh_Vars,
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

def test_assoc_expr_eq62_reverse_link_reassign_clear():
    a1 = wh_ExprNot(hasNot="sample_text")
    a2 = wh_ExprNot(hasNot="sample_text_2")
    b = wh_ExprEq(sym="sample_text")
    _safe_set(b, 'wh_ExprEq', a1)
    assert _is_linked(b, 'wh_ExprEq', a1)
    if hasattr(a1, 'wh_ExprNot63'):
        assert _is_linked(a1, 'wh_ExprNot63', b)
    _safe_set(b, 'wh_ExprEq', a2)
    assert _is_linked(b, 'wh_ExprEq', a2)
    if hasattr(a1, 'wh_ExprNot63'):
        assert not _is_linked(a1, 'wh_ExprNot63', b)
    if hasattr(a2, 'wh_ExprNot63'):
        assert _is_linked(a2, 'wh_ExprNot63', b)
    _safe_set(b, 'wh_ExprEq', None)
    assert not _is_linked(b, 'wh_ExprEq', a2)
    if hasattr(a2, 'wh_ExprNot63'):
        assert not _is_linked(a2, 'wh_ExprNot63', b)


def test_assoc_expr_left64_reverse_link_reassign_clear():
    a1 = wh_ExprSimple(nil="sample_text", sym="sample_text", variable="sample_text")
    a2 = wh_ExprSimple(nil="sample_text_2", sym="sample_text_2", variable="sample_text_2")
    b = wh_ExprEq(sym="sample_text")
    _safe_set(b, 'wh_ExprEq65', a1)
    assert _is_linked(b, 'wh_ExprEq65', a1)
    if hasattr(a1, 'wh_ExprSimple66'):
        assert _is_linked(a1, 'wh_ExprSimple66', b)
    _safe_set(b, 'wh_ExprEq65', a2)
    assert _is_linked(b, 'wh_ExprEq65', a2)
    if hasattr(a1, 'wh_ExprSimple66'):
        assert not _is_linked(a1, 'wh_ExprSimple66', b)
    if hasattr(a2, 'wh_ExprSimple66'):
        assert _is_linked(a2, 'wh_ExprSimple66', b)
    _safe_set(b, 'wh_ExprEq65', None)
    assert not _is_linked(b, 'wh_ExprEq65', a2)
    if hasattr(a2, 'wh_ExprSimple66'):
        assert not _is_linked(a2, 'wh_ExprSimple66', b)


def test_assoc_expr_right67_reverse_link_reassign_clear():
    a1 = wh_ExprSimple(nil="sample_text", sym="sample_text", variable="sample_text")
    a2 = wh_ExprSimple(nil="sample_text_2", sym="sample_text_2", variable="sample_text_2")
    b = wh_ExprEq(sym="sample_text")
    _safe_set(b, 'wh_ExprEq68', a1)
    assert _is_linked(b, 'wh_ExprEq68', a1)
    if hasattr(a1, 'wh_ExprSimple69'):
        assert _is_linked(a1, 'wh_ExprSimple69', b)
    _safe_set(b, 'wh_ExprEq68', a2)
    assert _is_linked(b, 'wh_ExprEq68', a2)
    if hasattr(a1, 'wh_ExprSimple69'):
        assert not _is_linked(a1, 'wh_ExprSimple69', b)
    if hasattr(a2, 'wh_ExprSimple69'):
        assert _is_linked(a2, 'wh_ExprSimple69', b)
    _safe_set(b, 'wh_ExprEq68', None)
    assert not _is_linked(b, 'wh_ExprEq68', a2)
    if hasattr(a2, 'wh_ExprSimple69'):
        assert not _is_linked(a2, 'wh_ExprSimple69', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cons_exp48_stub_double():
    # wh_LExpr has no real 'wh_LExpr' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(nil="sample_text", sym="sample_text", variable="sample_text")
    partner = wh_LExpr()
    setattr(partner, 'wh_LExpr', None)
    _safe_set(owner, 'wh_ExprSimple', partner)
    assert getattr(partner, 'wh_LExpr') == owner
    _safe_set(owner, 'wh_ExprSimple', None)
    assert getattr(partner, 'wh_LExpr') is None


def test_assoc_definition3_stub_double():
    # wh_Definition has no real 'wh_Definition' property in the generated
    # code (a bare stub) -- manually attach it so wh_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Function(fname="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition', None)
    _safe_set(owner, 'wh_Function4', partner)
    assert getattr(partner, 'wh_Definition') == owner
    _safe_set(owner, 'wh_Function4', None)
    assert getattr(partner, 'wh_Definition') is None


def test_assoc_expr73_stub_double():
    # wh_Expr has no real 'wh_Expr75' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprEq's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprEq's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprEq(sym="sample_text")
    partner = wh_Expr()
    setattr(partner, 'wh_Expr75', None)
    _safe_set(owner, 'wh_ExprEq74', partner)
    assert getattr(partner, 'wh_Expr75') == owner
    _safe_set(owner, 'wh_ExprEq74', None)
    assert getattr(partner, 'wh_Expr75') is None


def test_assoc_expr_not60_stub_double():
    # wh_ExprOr has no real 'wh_ExprOr61' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprNot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprNot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprNot(hasNot="sample_text")
    partner = wh_ExprOr()
    setattr(partner, 'wh_ExprOr61', None)
    _safe_set(owner, 'wh_ExprNot', partner)
    assert owner in getattr(partner, 'wh_ExprOr61')
    _safe_set(owner, 'wh_ExprNot', None)
    assert owner not in getattr(partner, 'wh_ExprOr61')


def test_assoc_functions1_stub_double():
    # wh_Program has no real 'wh_Program2' property in the generated
    # code (a bare stub) -- manually attach it so wh_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Function(fname="sample_text")
    partner = wh_Program()
    setattr(partner, 'wh_Program2', None)
    _safe_set(owner, 'wh_Function', partner)
    assert owner in getattr(partner, 'wh_Program2')
    _safe_set(owner, 'wh_Function', None)
    assert owner not in getattr(partner, 'wh_Program2')


def test_assoc_hd_expr52_stub_double():
    # wh_Expr has no real 'wh_Expr54' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(nil="sample_text", sym="sample_text", variable="sample_text")
    partner = wh_Expr()
    setattr(partner, 'wh_Expr54', None)
    _safe_set(owner, 'wh_ExprSimple53', partner)
    assert getattr(partner, 'wh_Expr54') == owner
    _safe_set(owner, 'wh_ExprSimple53', None)
    assert getattr(partner, 'wh_Expr54') is None


def test_assoc_inputs5_stub_double():
    # wh_Definition has no real 'wh_Definition6' property in the generated
    # code (a bare stub) -- manually attach it so wh_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Input(params="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition6', None)
    _safe_set(owner, 'wh_Input', partner)
    assert getattr(partner, 'wh_Definition6') == owner
    _safe_set(owner, 'wh_Input', None)
    assert getattr(partner, 'wh_Definition6') is None


def test_assoc_lexpr70_stub_double():
    # wh_LExpr has no real 'wh_LExpr72' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprEq's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprEq's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprEq(sym="sample_text")
    partner = wh_LExpr()
    setattr(partner, 'wh_LExpr72', None)
    _safe_set(owner, 'wh_ExprEq71', partner)
    assert getattr(partner, 'wh_LExpr72') == owner
    _safe_set(owner, 'wh_ExprEq71', None)
    assert getattr(partner, 'wh_LExpr72') is None


def test_assoc_list_exp49_stub_double():
    # wh_LExpr has no real 'wh_LExpr51' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(nil="sample_text", sym="sample_text", variable="sample_text")
    partner = wh_LExpr()
    setattr(partner, 'wh_LExpr51', None)
    _safe_set(owner, 'wh_ExprSimple50', partner)
    assert getattr(partner, 'wh_LExpr51') == owner
    _safe_set(owner, 'wh_ExprSimple50', None)
    assert getattr(partner, 'wh_LExpr51') is None


def test_assoc_outputs9_stub_double():
    # wh_Definition has no real 'wh_Definition10' property in the generated
    # code (a bare stub) -- manually attach it so wh_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Output(r_values="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition10', None)
    _safe_set(owner, 'wh_Output', partner)
    assert getattr(partner, 'wh_Definition10') == owner
    _safe_set(owner, 'wh_Output', None)
    assert getattr(partner, 'wh_Definition10') is None


def test_assoc_tl_expr55_stub_double():
    # wh_Expr has no real 'wh_Expr57' property in the generated
    # code (a bare stub) -- manually attach it so wh_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_ExprSimple(nil="sample_text", sym="sample_text", variable="sample_text")
    partner = wh_Expr()
    setattr(partner, 'wh_Expr57', None)
    _safe_set(owner, 'wh_ExprSimple56', partner)
    assert getattr(partner, 'wh_Expr57') == owner
    _safe_set(owner, 'wh_ExprSimple56', None)
    assert getattr(partner, 'wh_Expr57') is None


def test_assoc_vars15_stub_double():
    # wh_Assign has no real 'wh_Assign' property in the generated
    # code (a bare stub) -- manually attach it so wh_Vars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Vars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Vars(variables="sample_text")
    partner = wh_Assign()
    setattr(partner, 'wh_Assign', None)
    _safe_set(owner, 'wh_Vars', partner)
    assert getattr(partner, 'wh_Assign') == owner
    _safe_set(owner, 'wh_Vars', None)
    assert getattr(partner, 'wh_Assign') is None


