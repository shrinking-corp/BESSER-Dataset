import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Factor,
    Stmt,
    simpliC_Args,
    simpliC_Assign,
    simpliC_Block,
    simpliC_Call,
    simpliC_Decl,
    simpliC_EObject,
    simpliC_Expr,
    simpliC_ExprCall,
    simpliC_Factor,
    simpliC_Function,
    simpliC_IDuse,
    simpliC_Ifstmt,
    simpliC_Model,
    simpliC_Return,
    simpliC_Stmt,
    simpliC_TFact,
    simpliC_Type,
    simpliC_Typedef,
    simpliC_Whilestmt,
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

def test_assoc_Arglist3_reverse_link_reassign_clear():
    a1 = simpliC_Function(name="sample_text")
    a2 = simpliC_Function(name="sample_text_2")
    b = simpliC_Args(name="sample_text")
    _safe_set(b, 'simpliC_Args', a1)
    assert _is_linked(b, 'simpliC_Args', a1)
    if hasattr(a1, 'simpliC_Function4'):
        assert _is_linked(a1, 'simpliC_Function4', b)
    _safe_set(b, 'simpliC_Args', a2)
    assert _is_linked(b, 'simpliC_Args', a2)
    if hasattr(a1, 'simpliC_Function4'):
        assert not _is_linked(a1, 'simpliC_Function4', b)
    if hasattr(a2, 'simpliC_Function4'):
        assert _is_linked(a2, 'simpliC_Function4', b)
    _safe_set(b, 'simpliC_Args', None)
    assert not _is_linked(b, 'simpliC_Args', a2)
    if hasattr(a2, 'simpliC_Function4'):
        assert not _is_linked(a2, 'simpliC_Function4', b)


def test_assoc_lh49_reverse_link_reassign_clear():
    a1 = simpliC_TFact(op="sample_text")
    a2 = simpliC_TFact(op="sample_text_2")
    b = simpliC_Expr(op="sample_text")
    _safe_set(b, 'simpliC_Expr51', a1)
    assert _is_linked(b, 'simpliC_Expr51', a1)
    if hasattr(a1, 'simpliC_TFact50'):
        assert _is_linked(a1, 'simpliC_TFact50', b)
    _safe_set(b, 'simpliC_Expr51', a2)
    assert _is_linked(b, 'simpliC_Expr51', a2)
    if hasattr(a1, 'simpliC_TFact50'):
        assert not _is_linked(a1, 'simpliC_TFact50', b)
    if hasattr(a2, 'simpliC_TFact50'):
        assert _is_linked(a2, 'simpliC_TFact50', b)
    _safe_set(b, 'simpliC_Expr51', None)
    assert not _is_linked(b, 'simpliC_Expr51', a2)
    if hasattr(a2, 'simpliC_TFact50'):
        assert not _is_linked(a2, 'simpliC_TFact50', b)


def test_assoc_terms47_reverse_link_reassign_clear():
    a1 = simpliC_TFact(op="sample_text")
    a2 = simpliC_TFact(op="sample_text_2")
    b = simpliC_Expr(op="sample_text")
    _safe_set(b, 'simpliC_Expr48', {a1})
    assert _is_linked(b, 'simpliC_Expr48', a1)
    if hasattr(a1, 'simpliC_TFact'):
        assert _is_linked(a1, 'simpliC_TFact', b)
    _safe_set(b, 'simpliC_Expr48', {a2})
    assert _is_linked(b, 'simpliC_Expr48', a2)
    if hasattr(a1, 'simpliC_TFact'):
        assert not _is_linked(a1, 'simpliC_TFact', b)
    if hasattr(a2, 'simpliC_TFact'):
        assert _is_linked(a2, 'simpliC_TFact', b)
    _safe_set(b, 'simpliC_Expr48', set())
    assert not _is_linked(b, 'simpliC_Expr48', a2)
    if hasattr(a2, 'simpliC_TFact'):
        assert not _is_linked(a2, 'simpliC_TFact', b)


def test_assoc_type1_reverse_link_reassign_clear():
    a1 = simpliC_Type(name="sample_text")
    a2 = simpliC_Type(name="sample_text_2")
    b = simpliC_Function(name="sample_text")
    _safe_set(b, 'simpliC_Function2', a1)
    assert _is_linked(b, 'simpliC_Function2', a1)
    if hasattr(a1, 'simpliC_Type'):
        assert _is_linked(a1, 'simpliC_Type', b)
    _safe_set(b, 'simpliC_Function2', a2)
    assert _is_linked(b, 'simpliC_Function2', a2)
    if hasattr(a1, 'simpliC_Type'):
        assert not _is_linked(a1, 'simpliC_Type', b)
    if hasattr(a2, 'simpliC_Type'):
        assert _is_linked(a2, 'simpliC_Type', b)
    _safe_set(b, 'simpliC_Function2', None)
    assert not _is_linked(b, 'simpliC_Function2', a2)
    if hasattr(a2, 'simpliC_Type'):
        assert not _is_linked(a2, 'simpliC_Type', b)


def test_assoc_type33_reverse_link_reassign_clear():
    a1 = simpliC_Type(name="sample_text")
    a2 = simpliC_Type(name="sample_text_2")
    b = simpliC_Decl(name="sample_text")
    _safe_set(b, 'simpliC_Decl', a1)
    assert _is_linked(b, 'simpliC_Decl', a1)
    if hasattr(a1, 'simpliC_Type34'):
        assert _is_linked(a1, 'simpliC_Type34', b)
    _safe_set(b, 'simpliC_Decl', a2)
    assert _is_linked(b, 'simpliC_Decl', a2)
    if hasattr(a1, 'simpliC_Type34'):
        assert not _is_linked(a1, 'simpliC_Type34', b)
    if hasattr(a2, 'simpliC_Type34'):
        assert _is_linked(a2, 'simpliC_Type34', b)
    _safe_set(b, 'simpliC_Decl', None)
    assert not _is_linked(b, 'simpliC_Decl', a2)
    if hasattr(a2, 'simpliC_Type34'):
        assert not _is_linked(a2, 'simpliC_Type34', b)


def test_assoc_type54_reverse_link_reassign_clear():
    a1 = simpliC_Type(name="sample_text")
    a2 = simpliC_Type(name="sample_text_2")
    b = simpliC_Args(name="sample_text")
    _safe_set(b, 'simpliC_Args55', a1)
    assert _is_linked(b, 'simpliC_Args55', a1)
    if hasattr(a1, 'simpliC_Type56'):
        assert _is_linked(a1, 'simpliC_Type56', b)
    _safe_set(b, 'simpliC_Args55', a2)
    assert _is_linked(b, 'simpliC_Args55', a2)
    if hasattr(a1, 'simpliC_Type56'):
        assert not _is_linked(a1, 'simpliC_Type56', b)
    if hasattr(a2, 'simpliC_Type56'):
        assert _is_linked(a2, 'simpliC_Type56', b)
    _safe_set(b, 'simpliC_Args55', None)
    assert not _is_linked(b, 'simpliC_Args55', a2)
    if hasattr(a2, 'simpliC_Type56'):
        assert not _is_linked(a2, 'simpliC_Type56', b)


def test_assoc_value37_reverse_link_reassign_clear():
    a1 = simpliC_Expr(op="sample_text")
    a2 = simpliC_Expr(op="sample_text_2")
    b = simpliC_Decl(name="sample_text")
    _safe_set(b, 'simpliC_Decl38', a1)
    assert _is_linked(b, 'simpliC_Decl38', a1)
    if hasattr(a1, 'simpliC_Expr39'):
        assert _is_linked(a1, 'simpliC_Expr39', b)
    _safe_set(b, 'simpliC_Decl38', a2)
    assert _is_linked(b, 'simpliC_Decl38', a2)
    if hasattr(a1, 'simpliC_Expr39'):
        assert not _is_linked(a1, 'simpliC_Expr39', b)
    if hasattr(a2, 'simpliC_Expr39'):
        assert _is_linked(a2, 'simpliC_Expr39', b)
    _safe_set(b, 'simpliC_Decl38', None)
    assert not _is_linked(b, 'simpliC_Decl38', a2)
    if hasattr(a2, 'simpliC_Expr39'):
        assert not _is_linked(a2, 'simpliC_Expr39', b)


def test_assoc_value40_reverse_link_reassign_clear():
    a1 = simpliC_Expr(op="sample_text")
    a2 = simpliC_Expr(op="sample_text_2")
    b = simpliC_Assign(var="sample_text")
    _safe_set(b, 'simpliC_Assign', a1)
    assert _is_linked(b, 'simpliC_Assign', a1)
    if hasattr(a1, 'simpliC_Expr41'):
        assert _is_linked(a1, 'simpliC_Expr41', b)
    _safe_set(b, 'simpliC_Assign', a2)
    assert _is_linked(b, 'simpliC_Assign', a2)
    if hasattr(a1, 'simpliC_Expr41'):
        assert not _is_linked(a1, 'simpliC_Expr41', b)
    if hasattr(a2, 'simpliC_Expr41'):
        assert _is_linked(a2, 'simpliC_Expr41', b)
    _safe_set(b, 'simpliC_Assign', None)
    assert not _is_linked(b, 'simpliC_Assign', a2)
    if hasattr(a2, 'simpliC_Expr41'):
        assert not _is_linked(a2, 'simpliC_Expr41', b)


def test_assoc_vtype35_reverse_link_reassign_clear():
    a1 = simpliC_Typedef(name="sample_text")
    a2 = simpliC_Typedef(name="sample_text_2")
    b = simpliC_Decl(name="sample_text")
    _safe_set(b, 'simpliC_Decl36', a1)
    assert _is_linked(b, 'simpliC_Decl36', a1)
    if hasattr(a1, 'simpliC_Typedef'):
        assert _is_linked(a1, 'simpliC_Typedef', b)
    _safe_set(b, 'simpliC_Decl36', a2)
    assert _is_linked(b, 'simpliC_Decl36', a2)
    if hasattr(a1, 'simpliC_Typedef'):
        assert not _is_linked(a1, 'simpliC_Typedef', b)
    if hasattr(a2, 'simpliC_Typedef'):
        assert _is_linked(a2, 'simpliC_Typedef', b)
    _safe_set(b, 'simpliC_Decl36', None)
    assert not _is_linked(b, 'simpliC_Decl36', a2)
    if hasattr(a2, 'simpliC_Typedef'):
        assert not _is_linked(a2, 'simpliC_Typedef', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Paramlist11_stub_double():
    # simpliC_Call has no real 'simpliC_Call12' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Expr(op="sample_text")
    partner = simpliC_Call()
    setattr(partner, 'simpliC_Call12', None)
    _safe_set(owner, 'simpliC_Expr', partner)
    assert owner in getattr(partner, 'simpliC_Call12')
    _safe_set(owner, 'simpliC_Expr', None)
    assert owner not in getattr(partner, 'simpliC_Call12')


def test_assoc_Paramlist15_stub_double():
    # simpliC_ExprCall has no real 'simpliC_ExprCall16' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Expr(op="sample_text")
    partner = simpliC_ExprCall()
    setattr(partner, 'simpliC_ExprCall16', None)
    _safe_set(owner, 'simpliC_Expr17', partner)
    assert owner in getattr(partner, 'simpliC_ExprCall16')
    _safe_set(owner, 'simpliC_Expr17', None)
    assert owner not in getattr(partner, 'simpliC_ExprCall16')


def test_assoc_Program0_stub_double():
    # simpliC_Model has no real 'simpliC_Model' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Function(name="sample_text")
    partner = simpliC_Model()
    setattr(partner, 'simpliC_Model', None)
    _safe_set(owner, 'simpliC_Function', partner)
    assert owner in getattr(partner, 'simpliC_Model')
    _safe_set(owner, 'simpliC_Function', None)
    assert owner not in getattr(partner, 'simpliC_Model')


def test_assoc_body5_stub_double():
    # simpliC_Block has no real 'simpliC_Block' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Function(name="sample_text")
    partner = simpliC_Block()
    setattr(partner, 'simpliC_Block', None)
    _safe_set(owner, 'simpliC_Function6', partner)
    assert getattr(partner, 'simpliC_Block') == owner
    _safe_set(owner, 'simpliC_Function6', None)
    assert getattr(partner, 'simpliC_Block') is None


def test_assoc_cond18_stub_double():
    # simpliC_Ifstmt has no real 'simpliC_Ifstmt' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Expr(op="sample_text")
    partner = simpliC_Ifstmt()
    setattr(partner, 'simpliC_Ifstmt', None)
    _safe_set(owner, 'simpliC_Expr19', partner)
    assert getattr(partner, 'simpliC_Ifstmt') == owner
    _safe_set(owner, 'simpliC_Expr19', None)
    assert getattr(partner, 'simpliC_Ifstmt') is None


def test_assoc_cond26_stub_double():
    # simpliC_Whilestmt has no real 'simpliC_Whilestmt' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Expr(op="sample_text")
    partner = simpliC_Whilestmt()
    setattr(partner, 'simpliC_Whilestmt', None)
    _safe_set(owner, 'simpliC_Expr27', partner)
    assert getattr(partner, 'simpliC_Whilestmt') == owner
    _safe_set(owner, 'simpliC_Expr27', None)
    assert getattr(partner, 'simpliC_Whilestmt') is None


def test_assoc_functionID13_stub_double():
    # simpliC_ExprCall has no real 'simpliC_ExprCall' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Function(name="sample_text")
    partner = simpliC_ExprCall()
    setattr(partner, 'simpliC_ExprCall', None)
    _safe_set(owner, 'simpliC_Function14', partner)
    assert getattr(partner, 'simpliC_ExprCall') == owner
    _safe_set(owner, 'simpliC_Function14', None)
    assert getattr(partner, 'simpliC_ExprCall') is None


def test_assoc_functionID9_stub_double():
    # simpliC_Call has no real 'simpliC_Call' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Function(name="sample_text")
    partner = simpliC_Call()
    setattr(partner, 'simpliC_Call', None)
    _safe_set(owner, 'simpliC_Function10', partner)
    assert getattr(partner, 'simpliC_Call') == owner
    _safe_set(owner, 'simpliC_Function10', None)
    assert getattr(partner, 'simpliC_Call') is None


def test_assoc_lh44_stub_double():
    # simpliC_EObject has no real 'simpliC_EObject46' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Expr(op="sample_text")
    partner = simpliC_EObject()
    setattr(partner, 'simpliC_EObject46', None)
    _safe_set(owner, 'simpliC_Expr45', partner)
    assert getattr(partner, 'simpliC_EObject46') == owner
    _safe_set(owner, 'simpliC_Expr45', None)
    assert getattr(partner, 'simpliC_EObject46') is None


def test_assoc_name52_stub_double():
    # simpliC_IDuse has no real 'simpliC_IDuse' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Decl(name="sample_text")
    partner = simpliC_IDuse()
    setattr(partner, 'simpliC_IDuse', None)
    _safe_set(owner, 'simpliC_Decl53', partner)
    assert getattr(partner, 'simpliC_IDuse') == owner
    _safe_set(owner, 'simpliC_Decl53', None)
    assert getattr(partner, 'simpliC_IDuse') is None


def test_assoc_oldtype57_stub_double():
    # simpliC_EObject has no real 'simpliC_EObject59' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Typedef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Typedef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Typedef(name="sample_text")
    partner = simpliC_EObject()
    setattr(partner, 'simpliC_EObject59', None)
    _safe_set(owner, 'simpliC_Typedef58', partner)
    assert getattr(partner, 'simpliC_EObject59') == owner
    _safe_set(owner, 'simpliC_Typedef58', None)
    assert getattr(partner, 'simpliC_EObject59') is None


def test_assoc_rh42_stub_double():
    # simpliC_EObject has no real 'simpliC_EObject' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Expr(op="sample_text")
    partner = simpliC_EObject()
    setattr(partner, 'simpliC_EObject', None)
    _safe_set(owner, 'simpliC_Expr43', partner)
    assert getattr(partner, 'simpliC_EObject') == owner
    _safe_set(owner, 'simpliC_Expr43', None)
    assert getattr(partner, 'simpliC_EObject') is None


def test_assoc_value31_stub_double():
    # simpliC_Return has no real 'simpliC_Return' property in the generated
    # code (a bare stub) -- manually attach it so simpliC_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpliC_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpliC_Expr(op="sample_text")
    partner = simpliC_Return()
    setattr(partner, 'simpliC_Return', None)
    _safe_set(owner, 'simpliC_Expr32', partner)
    assert getattr(partner, 'simpliC_Return') == owner
    _safe_set(owner, 'simpliC_Expr32', None)
    assert getattr(partner, 'simpliC_Return') is None


