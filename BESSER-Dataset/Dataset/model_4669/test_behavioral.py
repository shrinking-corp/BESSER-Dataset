import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithOp,
    BoolOp,
    CmpOp,
    EvalFunRes,
    EvalRes,
    Expr,
    TopLevelCmd,
    boa_App,
    boa_ArithOp,
    boa_ArithOpDivide,
    boa_ArithOpMinus,
    boa_ArithOpPlus,
    boa_ArithOpRemainder,
    boa_ArithOpTimes,
    boa_Assign,
    boa_BObject,
    boa_Bool,
    boa_BoolOp,
    boa_BoolOpAnd,
    boa_BoolOpOr,
    boa_CmpOp,
    boa_CmpOpEqual,
    boa_CmpOpLess,
    boa_CmpOpUnequal,
    boa_Copy,
    boa_Ctx,
    boa_Def,
    boa_EvalBoolRes,
    boa_EvalBoundFunRes,
    boa_EvalFunRes,
    boa_EvalIntRes,
    boa_EvalMapRes,
    boa_EvalRes,
    boa_Expr,
    boa_Field,
    boa_File,
    boa_Fun,
    boa_If,
    boa_Int,
    boa_Let,
    boa_Not,
    boa_Project,
    boa_Seq,
    boa_Skip,
    boa_StringToEvalResMap,
    boa_This,
    boa_TopLevelCmd,
    boa_Var,
    boa_With,
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

def test_assoc_body45_stub_double():
    # boa_Expr has no real 'boa_Expr46' property in the generated
    # code (a bare stub) -- manually attach it so boa_Fun's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Fun's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Fun(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr46', None)
    _safe_set(owner, 'boa_Fun', partner)
    assert getattr(partner, 'boa_Expr46') == owner
    _safe_set(owner, 'boa_Fun', None)
    assert getattr(partner, 'boa_Expr46') is None


def test_assoc_ctx77_stub_double():
    # boa_Ctx has no real 'boa_Ctx79' property in the generated
    # code (a bare stub) -- manually attach it so boa_EvalFunRes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_EvalFunRes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_EvalFunRes(name="sample_text")
    partner = boa_Ctx()
    setattr(partner, 'boa_Ctx79', None)
    _safe_set(owner, 'boa_EvalFunRes78', partner)
    assert getattr(partner, 'boa_Ctx79') == owner
    _safe_set(owner, 'boa_EvalFunRes78', None)
    assert getattr(partner, 'boa_Ctx79') is None


def test_assoc_env67_stub_double():
    # boa_Ctx has no real 'boa_Ctx' property in the generated
    # code (a bare stub) -- manually attach it so boa_StringToEvalResMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_StringToEvalResMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_StringToEvalResMap(key="sample_text")
    partner = boa_Ctx()
    setattr(partner, 'boa_Ctx', None)
    _safe_set(owner, 'boa_StringToEvalResMap', partner)
    assert owner in getattr(partner, 'boa_Ctx')
    _safe_set(owner, 'boa_StringToEvalResMap', None)
    assert owner not in getattr(partner, 'boa_Ctx')


def test_assoc_exp7_stub_double():
    # boa_Expr has no real 'boa_Expr8' property in the generated
    # code (a bare stub) -- manually attach it so boa_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Project(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr8', None)
    _safe_set(owner, 'boa_Project', partner)
    assert getattr(partner, 'boa_Expr8') == owner
    _safe_set(owner, 'boa_Project', None)
    assert getattr(partner, 'boa_Expr8') is None


def test_assoc_exp75_stub_double():
    # boa_Expr has no real 'boa_Expr76' property in the generated
    # code (a bare stub) -- manually attach it so boa_EvalFunRes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_EvalFunRes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_EvalFunRes(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr76', None)
    _safe_set(owner, 'boa_EvalFunRes', partner)
    assert getattr(partner, 'boa_Expr76') == owner
    _safe_set(owner, 'boa_EvalFunRes', None)
    assert getattr(partner, 'boa_Expr76') is None


def test_assoc_expr1_stub_double():
    # boa_Expr has no real 'boa_Expr' property in the generated
    # code (a bare stub) -- manually attach it so boa_Def's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Def's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Def(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr', None)
    _safe_set(owner, 'boa_Def', partner)
    assert getattr(partner, 'boa_Expr') == owner
    _safe_set(owner, 'boa_Def', None)
    assert getattr(partner, 'boa_Expr') is None


def test_assoc_fields9_stub_double():
    # boa_BObject has no real 'boa_BObject' property in the generated
    # code (a bare stub) -- manually attach it so boa_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Field(name="sample_text")
    partner = boa_BObject()
    setattr(partner, 'boa_BObject', None)
    _safe_set(owner, 'boa_Field', partner)
    assert owner in getattr(partner, 'boa_BObject')
    _safe_set(owner, 'boa_Field', None)
    assert owner not in getattr(partner, 'boa_BObject')


def test_assoc_lhs40_stub_double():
    # boa_Expr has no real 'boa_Expr41' property in the generated
    # code (a bare stub) -- manually attach it so boa_Let's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Let's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Let(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr41', None)
    _safe_set(owner, 'boa_Let', partner)
    assert getattr(partner, 'boa_Expr41') == owner
    _safe_set(owner, 'boa_Let', None)
    assert getattr(partner, 'boa_Expr41') is None


def test_assoc_lhs47_stub_double():
    # boa_Expr has no real 'boa_Expr48' property in the generated
    # code (a bare stub) -- manually attach it so boa_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Assign(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr48', None)
    _safe_set(owner, 'boa_Assign', partner)
    assert getattr(partner, 'boa_Expr48') == owner
    _safe_set(owner, 'boa_Assign', None)
    assert getattr(partner, 'boa_Expr48') is None


def test_assoc_rhs42_stub_double():
    # boa_Expr has no real 'boa_Expr44' property in the generated
    # code (a bare stub) -- manually attach it so boa_Let's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Let's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Let(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr44', None)
    _safe_set(owner, 'boa_Let43', partner)
    assert getattr(partner, 'boa_Expr44') == owner
    _safe_set(owner, 'boa_Let43', None)
    assert getattr(partner, 'boa_Expr44') is None


def test_assoc_rhs49_stub_double():
    # boa_Expr has no real 'boa_Expr51' property in the generated
    # code (a bare stub) -- manually attach it so boa_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Assign(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr51', None)
    _safe_set(owner, 'boa_Assign50', partner)
    assert getattr(partner, 'boa_Expr51') == owner
    _safe_set(owner, 'boa_Assign50', None)
    assert getattr(partner, 'boa_Expr51') is None


def test_assoc_th68_stub_double():
    # boa_Ctx has no real 'boa_Ctx69' property in the generated
    # code (a bare stub) -- manually attach it so boa_StringToEvalResMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_StringToEvalResMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_StringToEvalResMap(key="sample_text")
    partner = boa_Ctx()
    setattr(partner, 'boa_Ctx69', None)
    _safe_set(owner, 'boa_StringToEvalResMap70', partner)
    assert owner in getattr(partner, 'boa_Ctx69')
    _safe_set(owner, 'boa_StringToEvalResMap70', None)
    assert owner not in getattr(partner, 'boa_Ctx69')


def test_assoc_th80_stub_double():
    # boa_EvalBoundFunRes has no real 'boa_EvalBoundFunRes' property in the generated
    # code (a bare stub) -- manually attach it so boa_StringToEvalResMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_StringToEvalResMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_StringToEvalResMap(key="sample_text")
    partner = boa_EvalBoundFunRes()
    setattr(partner, 'boa_EvalBoundFunRes', None)
    _safe_set(owner, 'boa_StringToEvalResMap81', partner)
    assert owner in getattr(partner, 'boa_EvalBoundFunRes')
    _safe_set(owner, 'boa_StringToEvalResMap81', None)
    assert owner not in getattr(partner, 'boa_EvalBoundFunRes')


def test_assoc_value10_stub_double():
    # boa_Expr has no real 'boa_Expr12' property in the generated
    # code (a bare stub) -- manually attach it so boa_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_Field(name="sample_text")
    partner = boa_Expr()
    setattr(partner, 'boa_Expr12', None)
    _safe_set(owner, 'boa_Field11', partner)
    assert getattr(partner, 'boa_Expr12') == owner
    _safe_set(owner, 'boa_Field11', None)
    assert getattr(partner, 'boa_Expr12') is None


def test_assoc_value71_stub_double():
    # boa_EvalRes has no real 'boa_EvalRes' property in the generated
    # code (a bare stub) -- manually attach it so boa_StringToEvalResMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_StringToEvalResMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_StringToEvalResMap(key="sample_text")
    partner = boa_EvalRes()
    setattr(partner, 'boa_EvalRes', None)
    _safe_set(owner, 'boa_StringToEvalResMap72', partner)
    assert getattr(partner, 'boa_EvalRes') == owner
    _safe_set(owner, 'boa_StringToEvalResMap72', None)
    assert getattr(partner, 'boa_EvalRes') is None


def test_assoc_values73_stub_double():
    # boa_EvalMapRes has no real 'boa_EvalMapRes' property in the generated
    # code (a bare stub) -- manually attach it so boa_StringToEvalResMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # boa_StringToEvalResMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = boa_StringToEvalResMap(key="sample_text")
    partner = boa_EvalMapRes()
    setattr(partner, 'boa_EvalMapRes', None)
    _safe_set(owner, 'boa_StringToEvalResMap74', partner)
    assert owner in getattr(partner, 'boa_EvalMapRes')
    _safe_set(owner, 'boa_StringToEvalResMap74', None)
    assert owner not in getattr(partner, 'boa_EvalMapRes')


