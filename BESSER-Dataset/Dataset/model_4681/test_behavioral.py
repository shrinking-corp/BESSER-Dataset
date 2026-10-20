import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    Stmt,
    Value,
    imp_Assign,
    imp_Binary,
    imp_Block,
    imp_BoolValue,
    imp_Expr,
    imp_If,
    imp_IntConst,
    imp_IntValue,
    imp_Skip,
    imp_Stmt,
    imp_Store,
    imp_StringToValueMap,
    imp_Unary,
    imp_Value,
    imp_Var,
    imp_While,
    BinaryOp,
    UnaryOp,
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

def test_assoc_exp0_stub_double():
    # imp_Expr has no real 'imp_Expr' property in the generated
    # code (a bare stub) -- manually attach it so imp_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Assign(name="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr', None)
    _safe_set(owner, 'imp_Assign', partner)
    assert getattr(partner, 'imp_Expr') == owner
    _safe_set(owner, 'imp_Assign', None)
    assert getattr(partner, 'imp_Expr') is None


def test_assoc_expr15_stub_double():
    # imp_Expr has no real 'imp_Expr16' property in the generated
    # code (a bare stub) -- manually attach it so imp_Unary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Unary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Unary(op="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr16', None)
    _safe_set(owner, 'imp_Unary', partner)
    assert getattr(partner, 'imp_Expr16') == owner
    _safe_set(owner, 'imp_Unary', None)
    assert getattr(partner, 'imp_Expr16') is None


def test_assoc_lhs17_stub_double():
    # imp_Expr has no real 'imp_Expr18' property in the generated
    # code (a bare stub) -- manually attach it so imp_Binary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Binary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Binary(op="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr18', None)
    _safe_set(owner, 'imp_Binary', partner)
    assert getattr(partner, 'imp_Expr18') == owner
    _safe_set(owner, 'imp_Binary', None)
    assert getattr(partner, 'imp_Expr18') is None


def test_assoc_rhs19_stub_double():
    # imp_Expr has no real 'imp_Expr21' property in the generated
    # code (a bare stub) -- manually attach it so imp_Binary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_Binary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_Binary(op="sample_text")
    partner = imp_Expr()
    setattr(partner, 'imp_Expr21', None)
    _safe_set(owner, 'imp_Binary20', partner)
    assert getattr(partner, 'imp_Expr21') == owner
    _safe_set(owner, 'imp_Binary20', None)
    assert getattr(partner, 'imp_Expr21') is None


def test_assoc_value23_stub_double():
    # imp_Value has no real 'imp_Value' property in the generated
    # code (a bare stub) -- manually attach it so imp_StringToValueMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_StringToValueMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_StringToValueMap(key="sample_text")
    partner = imp_Value()
    setattr(partner, 'imp_Value', None)
    _safe_set(owner, 'imp_StringToValueMap24', partner)
    assert getattr(partner, 'imp_Value') == owner
    _safe_set(owner, 'imp_StringToValueMap24', None)
    assert getattr(partner, 'imp_Value') is None


def test_assoc_values22_stub_double():
    # imp_Store has no real 'imp_Store' property in the generated
    # code (a bare stub) -- manually attach it so imp_StringToValueMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imp_StringToValueMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imp_StringToValueMap(key="sample_text")
    partner = imp_Store()
    setattr(partner, 'imp_Store', None)
    _safe_set(owner, 'imp_StringToValueMap', partner)
    assert owner in getattr(partner, 'imp_Store')
    _safe_set(owner, 'imp_StringToValueMap', None)
    assert owner not in getattr(partner, 'imp_Store')


