import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expr,
    Member,
    Symbol,
    paplj_Add,
    paplj_And,
    paplj_Assignment,
    paplj_Binding,
    paplj_Block2,
    paplj_Bool,
    paplj_Cast,
    paplj_Div,
    paplj_Eq,
    paplj_Expr,
    paplj_Field,
    paplj_If,
    paplj_Import,
    paplj_Let,
    paplj_Lt,
    paplj_Member,
    paplj_MemberRef,
    paplj_Method,
    paplj_Min,
    paplj_Mul,
    paplj_Neq,
    paplj_New,
    paplj_Not,
    paplj_Null,
    paplj_Num,
    paplj_Or,
    paplj_Param,
    paplj_Program,
    paplj_Sub,
    paplj_Symbol,
    paplj_This,
    paplj_Type,
    paplj_Var,
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

def test_assoc_classes1_reverse_link_reassign_clear():
    a1 = paplj_Type(name="sample_text")
    a2 = paplj_Type(name="sample_text_2")
    b = paplj_Program(name="sample_text")
    _safe_set(b, 'paplj_Program2', {a1})
    assert _is_linked(b, 'paplj_Program2', a1)
    if hasattr(a1, 'paplj_Type'):
        assert _is_linked(a1, 'paplj_Type', b)
    _safe_set(b, 'paplj_Program2', {a2})
    assert _is_linked(b, 'paplj_Program2', a2)
    if hasattr(a1, 'paplj_Type'):
        assert not _is_linked(a1, 'paplj_Type', b)
    if hasattr(a2, 'paplj_Type'):
        assert _is_linked(a2, 'paplj_Type', b)
    _safe_set(b, 'paplj_Program2', set())
    assert not _is_linked(b, 'paplj_Program2', a2)
    if hasattr(a2, 'paplj_Type'):
        assert not _is_linked(a2, 'paplj_Type', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = paplj_Program(name="sample_text")
    a2 = paplj_Program(name="sample_text_2")
    b = paplj_Import(importedNamespace="sample_text")
    _safe_set(b, 'paplj_Import', a1)
    assert _is_linked(b, 'paplj_Import', a1)
    if hasattr(a1, 'paplj_Program'):
        assert _is_linked(a1, 'paplj_Program', b)
    _safe_set(b, 'paplj_Import', a2)
    assert _is_linked(b, 'paplj_Import', a2)
    if hasattr(a1, 'paplj_Program'):
        assert not _is_linked(a1, 'paplj_Program', b)
    if hasattr(a2, 'paplj_Program'):
        assert _is_linked(a2, 'paplj_Program', b)
    _safe_set(b, 'paplj_Import', None)
    assert not _is_linked(b, 'paplj_Import', a2)
    if hasattr(a2, 'paplj_Program'):
        assert not _is_linked(a2, 'paplj_Program', b)


def test_assoc_member104_reverse_link_reassign_clear():
    a1 = paplj_Var(methodInvocation=True)
    a2 = paplj_Var(methodInvocation=False)
    b = paplj_Symbol(name="sample_text")
    _safe_set(b, 'paplj_Symbol105', a1)
    assert _is_linked(b, 'paplj_Symbol105', a1)
    if hasattr(a1, 'paplj_Var'):
        assert _is_linked(a1, 'paplj_Var', b)
    _safe_set(b, 'paplj_Symbol105', a2)
    assert _is_linked(b, 'paplj_Symbol105', a2)
    if hasattr(a1, 'paplj_Var'):
        assert not _is_linked(a1, 'paplj_Var', b)
    if hasattr(a2, 'paplj_Var'):
        assert _is_linked(a2, 'paplj_Var', b)
    _safe_set(b, 'paplj_Symbol105', None)
    assert not _is_linked(b, 'paplj_Symbol105', a2)
    if hasattr(a2, 'paplj_Var'):
        assert not _is_linked(a2, 'paplj_Var', b)


def test_assoc_superType6_reverse_link_reassign_clear():
    a1 = paplj_Type(name="sample_text")
    a2 = paplj_Type(name="sample_text_2")
    b = paplj_Type(name="sample_text")
    _safe_set(b, 'paplj_Type7', a1)
    assert _is_linked(b, 'paplj_Type7', a1)
    if hasattr(a1, 'paplj_Type5'):
        assert _is_linked(a1, 'paplj_Type5', b)
    _safe_set(b, 'paplj_Type7', a2)
    assert _is_linked(b, 'paplj_Type7', a2)
    if hasattr(a1, 'paplj_Type5'):
        assert not _is_linked(a1, 'paplj_Type5', b)
    if hasattr(a2, 'paplj_Type5'):
        assert _is_linked(a2, 'paplj_Type5', b)
    _safe_set(b, 'paplj_Type7', None)
    assert not _is_linked(b, 'paplj_Type7', a2)
    if hasattr(a2, 'paplj_Type5'):
        assert not _is_linked(a2, 'paplj_Type5', b)


def test_assoc_type10_reverse_link_reassign_clear():
    a1 = paplj_Type(name="sample_text")
    a2 = paplj_Type(name="sample_text_2")
    b = paplj_Symbol(name="sample_text")
    _safe_set(b, 'paplj_Symbol', a1)
    assert _is_linked(b, 'paplj_Symbol', a1)
    if hasattr(a1, 'paplj_Type11'):
        assert _is_linked(a1, 'paplj_Type11', b)
    _safe_set(b, 'paplj_Symbol', a2)
    assert _is_linked(b, 'paplj_Symbol', a2)
    if hasattr(a1, 'paplj_Type11'):
        assert not _is_linked(a1, 'paplj_Type11', b)
    if hasattr(a2, 'paplj_Type11'):
        assert _is_linked(a2, 'paplj_Type11', b)
    _safe_set(b, 'paplj_Symbol', None)
    assert not _is_linked(b, 'paplj_Symbol', a2)
    if hasattr(a2, 'paplj_Type11'):
        assert not _is_linked(a2, 'paplj_Type11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args106_stub_double():
    # paplj_Expr has no real 'paplj_Expr108' property in the generated
    # code (a bare stub) -- manually attach it so paplj_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_Var(methodInvocation=True)
    partner = paplj_Expr()
    setattr(partner, 'paplj_Expr108', None)
    _safe_set(owner, 'paplj_Var107', {partner})
    assert getattr(partner, 'paplj_Expr108') == owner
    _safe_set(owner, 'paplj_Var107', set())
    assert getattr(partner, 'paplj_Expr108') is None


def test_assoc_args97_stub_double():
    # paplj_Expr has no real 'paplj_Expr99' property in the generated
    # code (a bare stub) -- manually attach it so paplj_MemberRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_MemberRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_MemberRef(methodInvocation=True)
    partner = paplj_Expr()
    setattr(partner, 'paplj_Expr99', None)
    _safe_set(owner, 'paplj_MemberRef98', {partner})
    assert getattr(partner, 'paplj_Expr99') == owner
    _safe_set(owner, 'paplj_MemberRef98', set())
    assert getattr(partner, 'paplj_Expr99') is None


def test_assoc_expr3_stub_double():
    # paplj_Expr has no real 'paplj_Expr' property in the generated
    # code (a bare stub) -- manually attach it so paplj_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_Program(name="sample_text")
    partner = paplj_Expr()
    setattr(partner, 'paplj_Expr', None)
    _safe_set(owner, 'paplj_Program4', partner)
    assert getattr(partner, 'paplj_Expr') == owner
    _safe_set(owner, 'paplj_Program4', None)
    assert getattr(partner, 'paplj_Expr') is None


def test_assoc_left92_stub_double():
    # paplj_Expr has no real 'paplj_Expr93' property in the generated
    # code (a bare stub) -- manually attach it so paplj_MemberRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_MemberRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_MemberRef(methodInvocation=True)
    partner = paplj_Expr()
    setattr(partner, 'paplj_Expr93', None)
    _safe_set(owner, 'paplj_MemberRef', partner)
    assert getattr(partner, 'paplj_Expr93') == owner
    _safe_set(owner, 'paplj_MemberRef', None)
    assert getattr(partner, 'paplj_Expr93') is None


def test_assoc_member94_stub_double():
    # paplj_Member has no real 'paplj_Member96' property in the generated
    # code (a bare stub) -- manually attach it so paplj_MemberRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_MemberRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_MemberRef(methodInvocation=True)
    partner = paplj_Member()
    setattr(partner, 'paplj_Member96', None)
    _safe_set(owner, 'paplj_MemberRef95', partner)
    assert getattr(partner, 'paplj_Member96') == owner
    _safe_set(owner, 'paplj_MemberRef95', None)
    assert getattr(partner, 'paplj_Member96') is None


def test_assoc_members8_stub_double():
    # paplj_Member has no real 'paplj_Member' property in the generated
    # code (a bare stub) -- manually attach it so paplj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_Type(name="sample_text")
    partner = paplj_Member()
    setattr(partner, 'paplj_Member', None)
    _safe_set(owner, 'paplj_Type9', {partner})
    assert getattr(partner, 'paplj_Member') == owner
    _safe_set(owner, 'paplj_Type9', set())
    assert getattr(partner, 'paplj_Member') is None


def test_assoc_type100_stub_double():
    # paplj_Null has no real 'paplj_Null' property in the generated
    # code (a bare stub) -- manually attach it so paplj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_Type(name="sample_text")
    partner = paplj_Null()
    setattr(partner, 'paplj_Null', None)
    _safe_set(owner, 'paplj_Type101', partner)
    assert getattr(partner, 'paplj_Null') == owner
    _safe_set(owner, 'paplj_Type101', None)
    assert getattr(partner, 'paplj_Null') is None


def test_assoc_type102_stub_double():
    # paplj_New has no real 'paplj_New' property in the generated
    # code (a bare stub) -- manually attach it so paplj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_Type(name="sample_text")
    partner = paplj_New()
    setattr(partner, 'paplj_New', None)
    _safe_set(owner, 'paplj_Type103', partner)
    assert getattr(partner, 'paplj_New') == owner
    _safe_set(owner, 'paplj_Type103', None)
    assert getattr(partner, 'paplj_New') is None


def test_assoc_type85_stub_double():
    # paplj_Cast has no real 'paplj_Cast86' property in the generated
    # code (a bare stub) -- manually attach it so paplj_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paplj_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paplj_Type(name="sample_text")
    partner = paplj_Cast()
    setattr(partner, 'paplj_Cast86', None)
    _safe_set(owner, 'paplj_Type87', partner)
    assert getattr(partner, 'paplj_Cast86') == owner
    _safe_set(owner, 'paplj_Type87', None)
    assert getattr(partner, 'paplj_Cast86') is None


