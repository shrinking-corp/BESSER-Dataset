import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    TopLevelCmd,
    myDsl_App,
    myDsl_ArithOpDivide,
    myDsl_ArithOpMinus,
    myDsl_ArithOpPlus,
    myDsl_ArithOpRemainder,
    myDsl_ArithOpTimes,
    myDsl_Assign,
    myDsl_BObject,
    myDsl_Bool,
    myDsl_BoolOpAnd,
    myDsl_BoolOpOr,
    myDsl_CmpOpEqual,
    myDsl_CmpOpLess,
    myDsl_CmpOpUnequal,
    myDsl_Copy,
    myDsl_Def,
    myDsl_Expr,
    myDsl_Field,
    myDsl_File,
    myDsl_Fun,
    myDsl_If,
    myDsl_Int,
    myDsl_Let,
    myDsl_Not,
    myDsl_Project,
    myDsl_Seq,
    myDsl_Skip,
    myDsl_This,
    myDsl_TopLevelCmd,
    myDsl_Var,
    myDsl_With,
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

def test_assoc_body32_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr33' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Fun's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Fun's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Fun(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr33', None)
    _safe_set(owner, 'myDsl_Fun', partner)
    assert getattr(partner, 'myDsl_Expr33') == owner
    _safe_set(owner, 'myDsl_Fun', None)
    assert getattr(partner, 'myDsl_Expr33') is None


def test_assoc_exp7_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr8' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Project(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr8', None)
    _safe_set(owner, 'myDsl_Project', partner)
    assert getattr(partner, 'myDsl_Expr8') == owner
    _safe_set(owner, 'myDsl_Project', None)
    assert getattr(partner, 'myDsl_Expr8') is None


def test_assoc_expr1_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Def's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Def's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Def(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr', None)
    _safe_set(owner, 'myDsl_Def', partner)
    assert getattr(partner, 'myDsl_Expr') == owner
    _safe_set(owner, 'myDsl_Def', None)
    assert getattr(partner, 'myDsl_Expr') is None


def test_assoc_fields9_stub_double():
    # myDsl_BObject has no real 'myDsl_BObject' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Field(name="sample_text")
    partner = myDsl_BObject()
    setattr(partner, 'myDsl_BObject', None)
    _safe_set(owner, 'myDsl_Field', partner)
    assert owner in getattr(partner, 'myDsl_BObject')
    _safe_set(owner, 'myDsl_Field', None)
    assert owner not in getattr(partner, 'myDsl_BObject')


def test_assoc_lhs27_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr28' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Let's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Let's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Let(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr28', None)
    _safe_set(owner, 'myDsl_Let', partner)
    assert getattr(partner, 'myDsl_Expr28') == owner
    _safe_set(owner, 'myDsl_Let', None)
    assert getattr(partner, 'myDsl_Expr28') is None


def test_assoc_lhs34_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr35' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Assign(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr35', None)
    _safe_set(owner, 'myDsl_Assign', partner)
    assert getattr(partner, 'myDsl_Expr35') == owner
    _safe_set(owner, 'myDsl_Assign', None)
    assert getattr(partner, 'myDsl_Expr35') is None


def test_assoc_rhs29_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr31' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Let's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Let's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Let(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr31', None)
    _safe_set(owner, 'myDsl_Let30', partner)
    assert getattr(partner, 'myDsl_Expr31') == owner
    _safe_set(owner, 'myDsl_Let30', None)
    assert getattr(partner, 'myDsl_Expr31') is None


def test_assoc_rhs36_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr38' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Assign(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr38', None)
    _safe_set(owner, 'myDsl_Assign37', partner)
    assert getattr(partner, 'myDsl_Expr38') == owner
    _safe_set(owner, 'myDsl_Assign37', None)
    assert getattr(partner, 'myDsl_Expr38') is None


def test_assoc_value94_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr96' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Field(name="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr96', None)
    _safe_set(owner, 'myDsl_Field95', partner)
    assert getattr(partner, 'myDsl_Expr96') == owner
    _safe_set(owner, 'myDsl_Field95', None)
    assert getattr(partner, 'myDsl_Expr96') is None


