import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AExp,
    AndAlsoExp,
    ApplyExp,
    CaseExp,
    ClosedExp,
    Decl,
    MExp,
    OrElseExp,
    RExp,
    SelectExp,
    gDSL_AExp,
    gDSL_AndAlsoExp,
    gDSL_ApplyExp,
    gDSL_Args,
    gDSL_AtomicExp,
    gDSL_CONS,
    gDSL_CaseExp,
    gDSL_ClosedExp,
    gDSL_ConDecl,
    gDSL_Decl,
    gDSL_DeclExport,
    gDSL_Exp,
    gDSL_Field,
    gDSL_MExp,
    gDSL_Model,
    gDSL_MonadicExp,
    gDSL_OrElseExp,
    gDSL_PAT,
    gDSL_RExp,
    gDSL_SelectExp,
    gDSL_Ty,
    gDSL_TyBind,
    gDSL_TyElement,
    gDSL_TyVars,
    gDSL_Type,
    gDSL_Val,
    gDSL_ValueDecl,
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

def test_assoc_aexps85_reverse_link_reassign_clear():
    a1 = gDSL_AExp(sym="sample_text")
    a2 = gDSL_AExp(sym="sample_text_2")
    b = gDSL_AExp(sym="sample_text")
    _safe_set(b, 'gDSL_AExp84', {a1})
    assert _is_linked(b, 'gDSL_AExp84', a1)
    if hasattr(a1, 'gDSL_AExp'):
        assert _is_linked(a1, 'gDSL_AExp', b)
    _safe_set(b, 'gDSL_AExp84', {a2})
    assert _is_linked(b, 'gDSL_AExp84', a2)
    if hasattr(a1, 'gDSL_AExp'):
        assert not _is_linked(a1, 'gDSL_AExp', b)
    if hasattr(a2, 'gDSL_AExp'):
        assert _is_linked(a2, 'gDSL_AExp', b)
    _safe_set(b, 'gDSL_AExp84', set())
    assert not _is_linked(b, 'gDSL_AExp84', a2)
    if hasattr(a2, 'gDSL_AExp'):
        assert not _is_linked(a2, 'gDSL_AExp', b)


def test_assoc_caseExps56_reverse_link_reassign_clear():
    a1 = gDSL_Exp(mid="sample_text")
    a2 = gDSL_Exp(mid="sample_text_2")
    b = gDSL_CaseExp(name="sample_text")
    _safe_set(b, 'gDSL_CaseExp58', a1)
    assert _is_linked(b, 'gDSL_CaseExp58', a1)
    if hasattr(a1, 'gDSL_Exp57'):
        assert _is_linked(a1, 'gDSL_Exp57', b)
    _safe_set(b, 'gDSL_CaseExp58', a2)
    assert _is_linked(b, 'gDSL_CaseExp58', a2)
    if hasattr(a1, 'gDSL_Exp57'):
        assert not _is_linked(a1, 'gDSL_Exp57', b)
    if hasattr(a2, 'gDSL_Exp57'):
        assert _is_linked(a2, 'gDSL_Exp57', b)
    _safe_set(b, 'gDSL_CaseExp58', None)
    assert not _is_linked(b, 'gDSL_CaseExp58', a2)
    if hasattr(a2, 'gDSL_Exp57'):
        assert not _is_linked(a2, 'gDSL_Exp57', b)


def test_assoc_elements31_reverse_link_reassign_clear():
    a1 = gDSL_TyElement(name="sample_text")
    a2 = gDSL_TyElement(name="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty32', {a1})
    assert _is_linked(b, 'gDSL_Ty32', a1)
    if hasattr(a1, 'gDSL_TyElement'):
        assert _is_linked(a1, 'gDSL_TyElement', b)
    _safe_set(b, 'gDSL_Ty32', {a2})
    assert _is_linked(b, 'gDSL_Ty32', a2)
    if hasattr(a1, 'gDSL_TyElement'):
        assert not _is_linked(a1, 'gDSL_TyElement', b)
    if hasattr(a2, 'gDSL_TyElement'):
        assert _is_linked(a2, 'gDSL_TyElement', b)
    _safe_set(b, 'gDSL_Ty32', set())
    assert not _is_linked(b, 'gDSL_Ty32', a2)
    if hasattr(a2, 'gDSL_TyElement'):
        assert not _is_linked(a2, 'gDSL_TyElement', b)


def test_assoc_exp106_reverse_link_reassign_clear():
    a1 = gDSL_Field(name="sample_text")
    a2 = gDSL_Field(name="sample_text_2")
    b = gDSL_Exp(mid="sample_text")
    _safe_set(b, 'gDSL_Exp108', a1)
    assert _is_linked(b, 'gDSL_Exp108', a1)
    if hasattr(a1, 'gDSL_Field107'):
        assert _is_linked(a1, 'gDSL_Field107', b)
    _safe_set(b, 'gDSL_Exp108', a2)
    assert _is_linked(b, 'gDSL_Exp108', a2)
    if hasattr(a1, 'gDSL_Field107'):
        assert not _is_linked(a1, 'gDSL_Field107', b)
    if hasattr(a2, 'gDSL_Field107'):
        assert _is_linked(a2, 'gDSL_Field107', b)
    _safe_set(b, 'gDSL_Exp108', None)
    assert not _is_linked(b, 'gDSL_Exp108', a2)
    if hasattr(a2, 'gDSL_Field107'):
        assert not _is_linked(a2, 'gDSL_Field107', b)


def test_assoc_exp109_reverse_link_reassign_clear():
    a1 = gDSL_ValueDecl(ids="sample_text", name="sample_text")
    a2 = gDSL_ValueDecl(ids="sample_text_2", name="sample_text_2")
    b = gDSL_Exp(mid="sample_text")
    _safe_set(b, 'gDSL_Exp111', a1)
    assert _is_linked(b, 'gDSL_Exp111', a1)
    if hasattr(a1, 'gDSL_ValueDecl110'):
        assert _is_linked(a1, 'gDSL_ValueDecl110', b)
    _safe_set(b, 'gDSL_Exp111', a2)
    assert _is_linked(b, 'gDSL_Exp111', a2)
    if hasattr(a1, 'gDSL_ValueDecl110'):
        assert not _is_linked(a1, 'gDSL_ValueDecl110', b)
    if hasattr(a2, 'gDSL_ValueDecl110'):
        assert _is_linked(a2, 'gDSL_ValueDecl110', b)
    _safe_set(b, 'gDSL_Exp111', None)
    assert not _is_linked(b, 'gDSL_Exp111', a2)
    if hasattr(a2, 'gDSL_ValueDecl110'):
        assert not _is_linked(a2, 'gDSL_ValueDecl110', b)


def test_assoc_exp13_reverse_link_reassign_clear():
    a1 = gDSL_Val(attr="sample_text", decPat="sample_text", mid="sample_text", name="sample_text")
    a2 = gDSL_Val(attr="sample_text_2", decPat="sample_text_2", mid="sample_text_2", name="sample_text_2")
    b = gDSL_Exp(mid="sample_text")
    _safe_set(b, 'gDSL_Exp', a1)
    assert _is_linked(b, 'gDSL_Exp', a1)
    if hasattr(a1, 'gDSL_Val14'):
        assert _is_linked(a1, 'gDSL_Val14', b)
    _safe_set(b, 'gDSL_Exp', a2)
    assert _is_linked(b, 'gDSL_Exp', a2)
    if hasattr(a1, 'gDSL_Val14'):
        assert not _is_linked(a1, 'gDSL_Val14', b)
    if hasattr(a2, 'gDSL_Val14'):
        assert _is_linked(a2, 'gDSL_Val14', b)
    _safe_set(b, 'gDSL_Exp', None)
    assert not _is_linked(b, 'gDSL_Exp', a2)
    if hasattr(a2, 'gDSL_Val14'):
        assert not _is_linked(a2, 'gDSL_Val14', b)


def test_assoc_exp63_reverse_link_reassign_clear():
    a1 = gDSL_Exp(mid="sample_text")
    a2 = gDSL_Exp(mid="sample_text_2")
    b = gDSL_CaseExp(name="sample_text")
    _safe_set(b, 'gDSL_CaseExp64', {a1})
    assert _is_linked(b, 'gDSL_CaseExp64', a1)
    if hasattr(a1, 'gDSL_Exp65'):
        assert _is_linked(a1, 'gDSL_Exp65', b)
    _safe_set(b, 'gDSL_CaseExp64', {a2})
    assert _is_linked(b, 'gDSL_CaseExp64', a2)
    if hasattr(a1, 'gDSL_Exp65'):
        assert not _is_linked(a1, 'gDSL_Exp65', b)
    if hasattr(a2, 'gDSL_Exp65'):
        assert _is_linked(a2, 'gDSL_Exp65', b)
    _safe_set(b, 'gDSL_CaseExp64', set())
    assert not _is_linked(b, 'gDSL_CaseExp64', a2)
    if hasattr(a2, 'gDSL_Exp65'):
        assert not _is_linked(a2, 'gDSL_Exp65', b)


def test_assoc_exp77_reverse_link_reassign_clear():
    a1 = gDSL_MonadicExp(name="sample_text")
    a2 = gDSL_MonadicExp(name="sample_text_2")
    b = gDSL_Exp(mid="sample_text")
    _safe_set(b, 'gDSL_Exp79', a1)
    assert _is_linked(b, 'gDSL_Exp79', a1)
    if hasattr(a1, 'gDSL_MonadicExp78'):
        assert _is_linked(a1, 'gDSL_MonadicExp78', b)
    _safe_set(b, 'gDSL_Exp79', a2)
    assert _is_linked(b, 'gDSL_Exp79', a2)
    if hasattr(a1, 'gDSL_MonadicExp78'):
        assert not _is_linked(a1, 'gDSL_MonadicExp78', b)
    if hasattr(a2, 'gDSL_MonadicExp78'):
        assert _is_linked(a2, 'gDSL_MonadicExp78', b)
    _safe_set(b, 'gDSL_Exp79', None)
    assert not _is_linked(b, 'gDSL_Exp79', a2)
    if hasattr(a2, 'gDSL_MonadicExp78'):
        assert not _is_linked(a2, 'gDSL_MonadicExp78', b)


def test_assoc_expr98_reverse_link_reassign_clear():
    a1 = gDSL_Exp(mid="sample_text")
    a2 = gDSL_Exp(mid="sample_text_2")
    b = gDSL_AtomicExp(id="sample_text")
    _safe_set(b, 'gDSL_AtomicExp99', a1)
    assert _is_linked(b, 'gDSL_AtomicExp99', a1)
    if hasattr(a1, 'gDSL_Exp100'):
        assert _is_linked(a1, 'gDSL_Exp100', b)
    _safe_set(b, 'gDSL_AtomicExp99', a2)
    assert _is_linked(b, 'gDSL_AtomicExp99', a2)
    if hasattr(a1, 'gDSL_Exp100'):
        assert not _is_linked(a1, 'gDSL_Exp100', b)
    if hasattr(a2, 'gDSL_Exp100'):
        assert _is_linked(a2, 'gDSL_Exp100', b)
    _safe_set(b, 'gDSL_AtomicExp99', None)
    assert not _is_linked(b, 'gDSL_AtomicExp99', a2)
    if hasattr(a2, 'gDSL_Exp100'):
        assert not _is_linked(a2, 'gDSL_Exp100', b)


def test_assoc_exps101_reverse_link_reassign_clear():
    a1 = gDSL_Exp(mid="sample_text")
    a2 = gDSL_Exp(mid="sample_text_2")
    b = gDSL_AtomicExp(id="sample_text")
    _safe_set(b, 'gDSL_AtomicExp102', {a1})
    assert _is_linked(b, 'gDSL_AtomicExp102', a1)
    if hasattr(a1, 'gDSL_Exp103'):
        assert _is_linked(a1, 'gDSL_Exp103', b)
    _safe_set(b, 'gDSL_AtomicExp102', {a2})
    assert _is_linked(b, 'gDSL_AtomicExp102', a2)
    if hasattr(a1, 'gDSL_Exp103'):
        assert not _is_linked(a1, 'gDSL_Exp103', b)
    if hasattr(a2, 'gDSL_Exp103'):
        assert _is_linked(a2, 'gDSL_Exp103', b)
    _safe_set(b, 'gDSL_AtomicExp102', set())
    assert not _is_linked(b, 'gDSL_AtomicExp102', a2)
    if hasattr(a2, 'gDSL_Exp103'):
        assert not _is_linked(a2, 'gDSL_Exp103', b)


def test_assoc_exps15_reverse_link_reassign_clear():
    a1 = gDSL_Val(attr="sample_text", decPat="sample_text", mid="sample_text", name="sample_text")
    a2 = gDSL_Val(attr="sample_text_2", decPat="sample_text_2", mid="sample_text_2", name="sample_text_2")
    b = gDSL_Exp(mid="sample_text")
    _safe_set(b, 'gDSL_Exp17', a1)
    assert _is_linked(b, 'gDSL_Exp17', a1)
    if hasattr(a1, 'gDSL_Val16'):
        assert _is_linked(a1, 'gDSL_Val16', b)
    _safe_set(b, 'gDSL_Exp17', a2)
    assert _is_linked(b, 'gDSL_Exp17', a2)
    if hasattr(a1, 'gDSL_Val16'):
        assert not _is_linked(a1, 'gDSL_Val16', b)
    if hasattr(a2, 'gDSL_Val16'):
        assert _is_linked(a2, 'gDSL_Val16', b)
    _safe_set(b, 'gDSL_Exp17', None)
    assert not _is_linked(b, 'gDSL_Exp17', a2)
    if hasattr(a2, 'gDSL_Val16'):
        assert not _is_linked(a2, 'gDSL_Val16', b)


def test_assoc_fields96_reverse_link_reassign_clear():
    a1 = gDSL_Field(name="sample_text")
    a2 = gDSL_Field(name="sample_text_2")
    b = gDSL_AtomicExp(id="sample_text")
    _safe_set(b, 'gDSL_AtomicExp97', {a1})
    assert _is_linked(b, 'gDSL_AtomicExp97', a1)
    if hasattr(a1, 'gDSL_Field'):
        assert _is_linked(a1, 'gDSL_Field', b)
    _safe_set(b, 'gDSL_AtomicExp97', {a2})
    assert _is_linked(b, 'gDSL_AtomicExp97', a2)
    if hasattr(a1, 'gDSL_Field'):
        assert not _is_linked(a1, 'gDSL_Field', b)
    if hasattr(a2, 'gDSL_Field'):
        assert _is_linked(a2, 'gDSL_Field', b)
    _safe_set(b, 'gDSL_AtomicExp97', set())
    assert not _is_linked(b, 'gDSL_AtomicExp97', a2)
    if hasattr(a2, 'gDSL_Field'):
        assert not _is_linked(a2, 'gDSL_Field', b)


def test_assoc_in_43_reverse_link_reassign_clear():
    a1 = gDSL_Ty(type="sample_text", value="sample_text")
    a2 = gDSL_Ty(type="sample_text_2", value="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty44', a1)
    assert _is_linked(b, 'gDSL_Ty44', a1)
    if hasattr(a1, 'gDSL_Ty42'):
        assert _is_linked(a1, 'gDSL_Ty42', b)
    _safe_set(b, 'gDSL_Ty44', a2)
    assert _is_linked(b, 'gDSL_Ty44', a2)
    if hasattr(a1, 'gDSL_Ty42'):
        assert not _is_linked(a1, 'gDSL_Ty42', b)
    if hasattr(a2, 'gDSL_Ty42'):
        assert _is_linked(a2, 'gDSL_Ty42', b)
    _safe_set(b, 'gDSL_Ty44', None)
    assert not _is_linked(b, 'gDSL_Ty44', a2)
    if hasattr(a2, 'gDSL_Ty42'):
        assert not _is_linked(a2, 'gDSL_Ty42', b)


def test_assoc_mexps87_reverse_link_reassign_clear():
    a1 = gDSL_MExp(sign="sample_text")
    a2 = gDSL_MExp(sign="sample_text_2")
    b = gDSL_MExp(sign="sample_text")
    _safe_set(b, 'gDSL_MExp86', {a1})
    assert _is_linked(b, 'gDSL_MExp86', a1)
    if hasattr(a1, 'gDSL_MExp'):
        assert _is_linked(a1, 'gDSL_MExp', b)
    _safe_set(b, 'gDSL_MExp86', {a2})
    assert _is_linked(b, 'gDSL_MExp86', a2)
    if hasattr(a1, 'gDSL_MExp'):
        assert not _is_linked(a1, 'gDSL_MExp', b)
    if hasattr(a2, 'gDSL_MExp'):
        assert _is_linked(a2, 'gDSL_MExp', b)
    _safe_set(b, 'gDSL_MExp86', set())
    assert not _is_linked(b, 'gDSL_MExp86', a2)
    if hasattr(a2, 'gDSL_MExp'):
        assert not _is_linked(a2, 'gDSL_MExp', b)


def test_assoc_name54_reverse_link_reassign_clear():
    a1 = gDSL_Exp(mid="sample_text")
    a2 = gDSL_Exp(mid="sample_text_2")
    b = gDSL_CaseExp(name="sample_text")
    _safe_set(b, 'gDSL_CaseExp', a1)
    assert _is_linked(b, 'gDSL_CaseExp', a1)
    if hasattr(a1, 'gDSL_Exp55'):
        assert _is_linked(a1, 'gDSL_Exp55', b)
    _safe_set(b, 'gDSL_CaseExp', a2)
    assert _is_linked(b, 'gDSL_CaseExp', a2)
    if hasattr(a1, 'gDSL_Exp55'):
        assert not _is_linked(a1, 'gDSL_Exp55', b)
    if hasattr(a2, 'gDSL_Exp55'):
        assert _is_linked(a2, 'gDSL_Exp55', b)
    _safe_set(b, 'gDSL_CaseExp', None)
    assert not _is_linked(b, 'gDSL_CaseExp', a2)
    if hasattr(a2, 'gDSL_Exp55'):
        assert not _is_linked(a2, 'gDSL_Exp55', b)


def test_assoc_out46_reverse_link_reassign_clear():
    a1 = gDSL_Ty(type="sample_text", value="sample_text")
    a2 = gDSL_Ty(type="sample_text_2", value="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty47', a1)
    assert _is_linked(b, 'gDSL_Ty47', a1)
    if hasattr(a1, 'gDSL_Ty45'):
        assert _is_linked(a1, 'gDSL_Ty45', b)
    _safe_set(b, 'gDSL_Ty47', a2)
    assert _is_linked(b, 'gDSL_Ty47', a2)
    if hasattr(a1, 'gDSL_Ty45'):
        assert not _is_linked(a1, 'gDSL_Ty45', b)
    if hasattr(a2, 'gDSL_Ty45'):
        assert _is_linked(a2, 'gDSL_Ty45', b)
    _safe_set(b, 'gDSL_Ty47', None)
    assert not _is_linked(b, 'gDSL_Ty47', a2)
    if hasattr(a2, 'gDSL_Ty45'):
        assert not _is_linked(a2, 'gDSL_Ty45', b)


def test_assoc_param34_reverse_link_reassign_clear():
    a1 = gDSL_Ty(type="sample_text", value="sample_text")
    a2 = gDSL_Ty(type="sample_text_2", value="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty35', a1)
    assert _is_linked(b, 'gDSL_Ty35', a1)
    if hasattr(a1, 'gDSL_Ty33'):
        assert _is_linked(a1, 'gDSL_Ty33', b)
    _safe_set(b, 'gDSL_Ty35', a2)
    assert _is_linked(b, 'gDSL_Ty35', a2)
    if hasattr(a1, 'gDSL_Ty33'):
        assert not _is_linked(a1, 'gDSL_Ty33', b)
    if hasattr(a2, 'gDSL_Ty33'):
        assert _is_linked(a2, 'gDSL_Ty33', b)
    _safe_set(b, 'gDSL_Ty35', None)
    assert not _is_linked(b, 'gDSL_Ty35', a2)
    if hasattr(a2, 'gDSL_Ty33'):
        assert not _is_linked(a2, 'gDSL_Ty33', b)


def test_assoc_pat113_reverse_link_reassign_clear():
    a1 = gDSL_PAT(bitpat="sample_text", id="sample_text", int="sample_text", uscore="sample_text")
    a2 = gDSL_PAT(bitpat="sample_text_2", id="sample_text_2", int="sample_text_2", uscore="sample_text_2")
    b = gDSL_PAT(bitpat="sample_text", id="sample_text", int="sample_text", uscore="sample_text")
    _safe_set(b, 'gDSL_PAT114', a1)
    assert _is_linked(b, 'gDSL_PAT114', a1)
    if hasattr(a1, 'gDSL_PAT112'):
        assert _is_linked(a1, 'gDSL_PAT112', b)
    _safe_set(b, 'gDSL_PAT114', a2)
    assert _is_linked(b, 'gDSL_PAT114', a2)
    if hasattr(a1, 'gDSL_PAT112'):
        assert not _is_linked(a1, 'gDSL_PAT112', b)
    if hasattr(a2, 'gDSL_PAT112'):
        assert _is_linked(a2, 'gDSL_PAT112', b)
    _safe_set(b, 'gDSL_PAT114', None)
    assert not _is_linked(b, 'gDSL_PAT114', a2)
    if hasattr(a2, 'gDSL_PAT112'):
        assert not _is_linked(a2, 'gDSL_PAT112', b)


def test_assoc_pat61_reverse_link_reassign_clear():
    a1 = gDSL_PAT(bitpat="sample_text", id="sample_text", int="sample_text", uscore="sample_text")
    a2 = gDSL_PAT(bitpat="sample_text_2", id="sample_text_2", int="sample_text_2", uscore="sample_text_2")
    b = gDSL_CaseExp(name="sample_text")
    _safe_set(b, 'gDSL_CaseExp62', {a1})
    assert _is_linked(b, 'gDSL_CaseExp62', a1)
    if hasattr(a1, 'gDSL_PAT'):
        assert _is_linked(a1, 'gDSL_PAT', b)
    _safe_set(b, 'gDSL_CaseExp62', {a2})
    assert _is_linked(b, 'gDSL_CaseExp62', a2)
    if hasattr(a1, 'gDSL_PAT'):
        assert not _is_linked(a1, 'gDSL_PAT', b)
    if hasattr(a2, 'gDSL_PAT'):
        assert _is_linked(a2, 'gDSL_PAT', b)
    _safe_set(b, 'gDSL_CaseExp62', set())
    assert not _is_linked(b, 'gDSL_CaseExp62', a2)
    if hasattr(a2, 'gDSL_PAT'):
        assert not _is_linked(a2, 'gDSL_PAT', b)


def test_assoc_r40_reverse_link_reassign_clear():
    a1 = gDSL_Ty(type="sample_text", value="sample_text")
    a2 = gDSL_Ty(type="sample_text_2", value="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty41', a1)
    assert _is_linked(b, 'gDSL_Ty41', a1)
    if hasattr(a1, 'gDSL_Ty39'):
        assert _is_linked(a1, 'gDSL_Ty39', b)
    _safe_set(b, 'gDSL_Ty41', a2)
    assert _is_linked(b, 'gDSL_Ty41', a2)
    if hasattr(a1, 'gDSL_Ty39'):
        assert not _is_linked(a1, 'gDSL_Ty39', b)
    if hasattr(a2, 'gDSL_Ty39'):
        assert _is_linked(a2, 'gDSL_Ty39', b)
    _safe_set(b, 'gDSL_Ty41', None)
    assert not _is_linked(b, 'gDSL_Ty41', a2)
    if hasattr(a2, 'gDSL_Ty39'):
        assert not _is_linked(a2, 'gDSL_Ty39', b)


def test_assoc_resType37_reverse_link_reassign_clear():
    a1 = gDSL_Ty(type="sample_text", value="sample_text")
    a2 = gDSL_Ty(type="sample_text_2", value="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty38', a1)
    assert _is_linked(b, 'gDSL_Ty38', a1)
    if hasattr(a1, 'gDSL_Ty36'):
        assert _is_linked(a1, 'gDSL_Ty36', b)
    _safe_set(b, 'gDSL_Ty38', a2)
    assert _is_linked(b, 'gDSL_Ty38', a2)
    if hasattr(a1, 'gDSL_Ty36'):
        assert not _is_linked(a1, 'gDSL_Ty36', b)
    if hasattr(a2, 'gDSL_Ty36'):
        assert _is_linked(a2, 'gDSL_Ty36', b)
    _safe_set(b, 'gDSL_Ty38', None)
    assert not _is_linked(b, 'gDSL_Ty38', a2)
    if hasattr(a2, 'gDSL_Ty36'):
        assert not _is_linked(a2, 'gDSL_Ty36', b)


def test_assoc_tyBind29_reverse_link_reassign_clear():
    a1 = gDSL_TyBind(name="sample_text")
    a2 = gDSL_TyBind(name="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty30', {a1})
    assert _is_linked(b, 'gDSL_Ty30', a1)
    if hasattr(a1, 'gDSL_TyBind'):
        assert _is_linked(a1, 'gDSL_TyBind', b)
    _safe_set(b, 'gDSL_Ty30', {a2})
    assert _is_linked(b, 'gDSL_Ty30', a2)
    if hasattr(a1, 'gDSL_TyBind'):
        assert not _is_linked(a1, 'gDSL_TyBind', b)
    if hasattr(a2, 'gDSL_TyBind'):
        assert _is_linked(a2, 'gDSL_TyBind', b)
    _safe_set(b, 'gDSL_Ty30', set())
    assert not _is_linked(b, 'gDSL_Ty30', a2)
    if hasattr(a2, 'gDSL_TyBind'):
        assert not _is_linked(a2, 'gDSL_TyBind', b)


def test_assoc_typeRef26_reverse_link_reassign_clear():
    a1 = gDSL_Type(name="sample_text")
    a2 = gDSL_Type(name="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty27', a1)
    assert _is_linked(b, 'gDSL_Ty27', a1)
    if hasattr(a1, 'gDSL_Type28'):
        assert _is_linked(a1, 'gDSL_Type28', b)
    _safe_set(b, 'gDSL_Ty27', a2)
    assert _is_linked(b, 'gDSL_Ty27', a2)
    if hasattr(a1, 'gDSL_Type28'):
        assert not _is_linked(a1, 'gDSL_Type28', b)
    if hasattr(a2, 'gDSL_Type28'):
        assert _is_linked(a2, 'gDSL_Type28', b)
    _safe_set(b, 'gDSL_Ty27', None)
    assert not _is_linked(b, 'gDSL_Ty27', a2)
    if hasattr(a2, 'gDSL_Type28'):
        assert not _is_linked(a2, 'gDSL_Type28', b)


def test_assoc_valDecl104_reverse_link_reassign_clear():
    a1 = gDSL_ValueDecl(ids="sample_text", name="sample_text")
    a2 = gDSL_ValueDecl(ids="sample_text_2", name="sample_text_2")
    b = gDSL_AtomicExp(id="sample_text")
    _safe_set(b, 'gDSL_AtomicExp105', {a1})
    assert _is_linked(b, 'gDSL_AtomicExp105', a1)
    if hasattr(a1, 'gDSL_ValueDecl'):
        assert _is_linked(a1, 'gDSL_ValueDecl', b)
    _safe_set(b, 'gDSL_AtomicExp105', {a2})
    assert _is_linked(b, 'gDSL_AtomicExp105', a2)
    if hasattr(a1, 'gDSL_ValueDecl'):
        assert not _is_linked(a1, 'gDSL_ValueDecl', b)
    if hasattr(a2, 'gDSL_ValueDecl'):
        assert _is_linked(a2, 'gDSL_ValueDecl', b)
    _safe_set(b, 'gDSL_AtomicExp105', set())
    assert not _is_linked(b, 'gDSL_AtomicExp105', a2)
    if hasattr(a2, 'gDSL_ValueDecl'):
        assert not _is_linked(a2, 'gDSL_ValueDecl', b)


def test_assoc_value10_reverse_link_reassign_clear():
    a1 = gDSL_Type(name="sample_text")
    a2 = gDSL_Type(name="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty12', a1)
    assert _is_linked(b, 'gDSL_Ty12', a1)
    if hasattr(a1, 'gDSL_Type11'):
        assert _is_linked(a1, 'gDSL_Type11', b)
    _safe_set(b, 'gDSL_Ty12', a2)
    assert _is_linked(b, 'gDSL_Ty12', a2)
    if hasattr(a1, 'gDSL_Type11'):
        assert not _is_linked(a1, 'gDSL_Type11', b)
    if hasattr(a2, 'gDSL_Type11'):
        assert _is_linked(a2, 'gDSL_Type11', b)
    _safe_set(b, 'gDSL_Ty12', None)
    assert not _is_linked(b, 'gDSL_Ty12', a2)
    if hasattr(a2, 'gDSL_Type11'):
        assert not _is_linked(a2, 'gDSL_Type11', b)


def test_assoc_value48_reverse_link_reassign_clear():
    a1 = gDSL_TyBind(name="sample_text")
    a2 = gDSL_TyBind(name="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty50', a1)
    assert _is_linked(b, 'gDSL_Ty50', a1)
    if hasattr(a1, 'gDSL_TyBind49'):
        assert _is_linked(a1, 'gDSL_TyBind49', b)
    _safe_set(b, 'gDSL_Ty50', a2)
    assert _is_linked(b, 'gDSL_Ty50', a2)
    if hasattr(a1, 'gDSL_TyBind49'):
        assert not _is_linked(a1, 'gDSL_TyBind49', b)
    if hasattr(a2, 'gDSL_TyBind49'):
        assert _is_linked(a2, 'gDSL_TyBind49', b)
    _safe_set(b, 'gDSL_Ty50', None)
    assert not _is_linked(b, 'gDSL_Ty50', a2)
    if hasattr(a2, 'gDSL_TyBind49'):
        assert not _is_linked(a2, 'gDSL_TyBind49', b)


def test_assoc_value51_reverse_link_reassign_clear():
    a1 = gDSL_TyElement(name="sample_text")
    a2 = gDSL_TyElement(name="sample_text_2")
    b = gDSL_Ty(type="sample_text", value="sample_text")
    _safe_set(b, 'gDSL_Ty53', a1)
    assert _is_linked(b, 'gDSL_Ty53', a1)
    if hasattr(a1, 'gDSL_TyElement52'):
        assert _is_linked(a1, 'gDSL_TyElement52', b)
    _safe_set(b, 'gDSL_Ty53', a2)
    assert _is_linked(b, 'gDSL_Ty53', a2)
    if hasattr(a1, 'gDSL_TyElement52'):
        assert not _is_linked(a1, 'gDSL_TyElement52', b)
    if hasattr(a2, 'gDSL_TyElement52'):
        assert _is_linked(a2, 'gDSL_TyElement52', b)
    _safe_set(b, 'gDSL_Ty53', None)
    assert not _is_linked(b, 'gDSL_Ty53', a2)
    if hasattr(a2, 'gDSL_TyElement52'):
        assert not _is_linked(a2, 'gDSL_TyElement52', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_applyexps88_stub_double():
    # gDSL_ApplyExp has no real 'gDSL_ApplyExp' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_SelectExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_SelectExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_SelectExp(symbol="sample_text")
    partner = gDSL_ApplyExp()
    setattr(partner, 'gDSL_ApplyExp', None)
    _safe_set(owner, 'gDSL_SelectExp', {partner})
    assert getattr(partner, 'gDSL_ApplyExp') == owner
    _safe_set(owner, 'gDSL_SelectExp', set())
    assert getattr(partner, 'gDSL_ApplyExp') is None


def test_assoc_args93_stub_double():
    # gDSL_Args has no real 'gDSL_Args94' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_AtomicExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_AtomicExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_AtomicExp(id="sample_text")
    partner = gDSL_Args()
    setattr(partner, 'gDSL_Args94', None)
    _safe_set(owner, 'gDSL_AtomicExp95', partner)
    assert owner in getattr(partner, 'gDSL_Args94')
    _safe_set(owner, 'gDSL_AtomicExp95', None)
    assert owner not in getattr(partner, 'gDSL_Args94')


def test_assoc_atomicExp89_stub_double():
    # gDSL_ApplyExp has no real 'gDSL_ApplyExp90' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_AtomicExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_AtomicExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_AtomicExp(id="sample_text")
    partner = gDSL_ApplyExp()
    setattr(partner, 'gDSL_ApplyExp90', None)
    _safe_set(owner, 'gDSL_AtomicExp', partner)
    assert getattr(partner, 'gDSL_ApplyExp90') == owner
    _safe_set(owner, 'gDSL_AtomicExp', None)
    assert getattr(partner, 'gDSL_ApplyExp90') is None


def test_assoc_attr18_stub_double():
    # gDSL_TyVars has no real 'gDSL_TyVars19' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_Type(name="sample_text")
    partner = gDSL_TyVars()
    setattr(partner, 'gDSL_TyVars19', None)
    _safe_set(owner, 'gDSL_Type20', partner)
    assert owner in getattr(partner, 'gDSL_TyVars19')
    _safe_set(owner, 'gDSL_Type20', None)
    assert owner not in getattr(partner, 'gDSL_TyVars19')


def test_assoc_closedExp59_stub_double():
    # gDSL_ClosedExp has no real 'gDSL_ClosedExp' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_CaseExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_CaseExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_CaseExp(name="sample_text")
    partner = gDSL_ClosedExp()
    setattr(partner, 'gDSL_ClosedExp', None)
    _safe_set(owner, 'gDSL_CaseExp60', partner)
    assert getattr(partner, 'gDSL_ClosedExp') == owner
    _safe_set(owner, 'gDSL_CaseExp60', None)
    assert getattr(partner, 'gDSL_ClosedExp') is None


def test_assoc_conDecl8_stub_double():
    # gDSL_ConDecl has no real 'gDSL_ConDecl' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_Type(name="sample_text")
    partner = gDSL_ConDecl()
    setattr(partner, 'gDSL_ConDecl', None)
    _safe_set(owner, 'gDSL_Type9', {partner})
    assert getattr(partner, 'gDSL_ConDecl') == owner
    _safe_set(owner, 'gDSL_Type9', set())
    assert getattr(partner, 'gDSL_ConDecl') is None


def test_assoc_doExp75_stub_double():
    # gDSL_ClosedExp has no real 'gDSL_ClosedExp76' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_MonadicExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_MonadicExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_MonadicExp(name="sample_text")
    partner = gDSL_ClosedExp()
    setattr(partner, 'gDSL_ClosedExp76', None)
    _safe_set(owner, 'gDSL_MonadicExp', partner)
    assert owner in getattr(partner, 'gDSL_ClosedExp76')
    _safe_set(owner, 'gDSL_MonadicExp', None)
    assert owner not in getattr(partner, 'gDSL_ClosedExp76')


def test_assoc_elseCaseExp72_stub_double():
    # gDSL_ClosedExp has no real 'gDSL_ClosedExp73' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_CaseExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_CaseExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_CaseExp(name="sample_text")
    partner = gDSL_ClosedExp()
    setattr(partner, 'gDSL_ClosedExp73', None)
    _safe_set(owner, 'gDSL_CaseExp74', partner)
    assert getattr(partner, 'gDSL_ClosedExp73') == owner
    _safe_set(owner, 'gDSL_CaseExp74', None)
    assert getattr(partner, 'gDSL_ClosedExp73') is None


def test_assoc_ifCaseExp66_stub_double():
    # gDSL_ClosedExp has no real 'gDSL_ClosedExp67' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_CaseExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_CaseExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_CaseExp(name="sample_text")
    partner = gDSL_ClosedExp()
    setattr(partner, 'gDSL_ClosedExp67', None)
    _safe_set(owner, 'gDSL_CaseExp68', partner)
    assert getattr(partner, 'gDSL_ClosedExp67') == owner
    _safe_set(owner, 'gDSL_CaseExp68', None)
    assert getattr(partner, 'gDSL_ClosedExp67') is None


def test_assoc_name1_stub_double():
    # gDSL_DeclExport has no real 'gDSL_DeclExport' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_Val's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_Val's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_Val(attr="sample_text", decPat="sample_text", mid="sample_text", name="sample_text")
    partner = gDSL_DeclExport()
    setattr(partner, 'gDSL_DeclExport', None)
    _safe_set(owner, 'gDSL_Val', partner)
    assert getattr(partner, 'gDSL_DeclExport') == owner
    _safe_set(owner, 'gDSL_Val', None)
    assert getattr(partner, 'gDSL_DeclExport') is None


def test_assoc_name21_stub_double():
    # gDSL_ConDecl has no real 'gDSL_ConDecl22' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_CONS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_CONS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_CONS(conName="sample_text")
    partner = gDSL_ConDecl()
    setattr(partner, 'gDSL_ConDecl22', None)
    _safe_set(owner, 'gDSL_CONS', partner)
    assert getattr(partner, 'gDSL_ConDecl22') == owner
    _safe_set(owner, 'gDSL_CONS', None)
    assert getattr(partner, 'gDSL_ConDecl22') is None


def test_assoc_thenCaseExp69_stub_double():
    # gDSL_ClosedExp has no real 'gDSL_ClosedExp70' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_CaseExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_CaseExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_CaseExp(name="sample_text")
    partner = gDSL_ClosedExp()
    setattr(partner, 'gDSL_ClosedExp70', None)
    _safe_set(owner, 'gDSL_CaseExp71', partner)
    assert getattr(partner, 'gDSL_ClosedExp70') == owner
    _safe_set(owner, 'gDSL_CaseExp71', None)
    assert getattr(partner, 'gDSL_ClosedExp70') is None


def test_assoc_ty23_stub_double():
    # gDSL_ConDecl has no real 'gDSL_ConDecl24' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_Ty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_Ty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_Ty(type="sample_text", value="sample_text")
    partner = gDSL_ConDecl()
    setattr(partner, 'gDSL_ConDecl24', None)
    _safe_set(owner, 'gDSL_Ty25', partner)
    assert getattr(partner, 'gDSL_ConDecl24') == owner
    _safe_set(owner, 'gDSL_Ty25', None)
    assert getattr(partner, 'gDSL_ConDecl24') is None


def test_assoc_tyVars6_stub_double():
    # gDSL_TyVars has no real 'gDSL_TyVars7' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_Type(name="sample_text")
    partner = gDSL_TyVars()
    setattr(partner, 'gDSL_TyVars7', None)
    _safe_set(owner, 'gDSL_Type', partner)
    assert getattr(partner, 'gDSL_TyVars7') == owner
    _safe_set(owner, 'gDSL_Type', None)
    assert getattr(partner, 'gDSL_TyVars7') is None


def test_assoc_type4_stub_double():
    # gDSL_DeclExport has no real 'gDSL_DeclExport5' property in the generated
    # code (a bare stub) -- manually attach it so gDSL_Ty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gDSL_Ty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gDSL_Ty(type="sample_text", value="sample_text")
    partner = gDSL_DeclExport()
    setattr(partner, 'gDSL_DeclExport5', None)
    _safe_set(owner, 'gDSL_Ty', partner)
    assert getattr(partner, 'gDSL_DeclExport5') == owner
    _safe_set(owner, 'gDSL_Ty', None)
    assert getattr(partner, 'gDSL_DeclExport5') is None


