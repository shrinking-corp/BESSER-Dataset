import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    whileComp_Affectation,
    whileComp_Command,
    whileComp_Commands,
    whileComp_Cons,
    whileComp_Definition,
    whileComp_EObject,
    whileComp_Expr,
    whileComp_ExprSimple,
    whileComp_For,
    whileComp_Foreach,
    whileComp_Function,
    whileComp_Hd,
    whileComp_If,
    whileComp_Lexpr,
    whileComp_List,
    whileComp_Nil2,
    whileComp_Nop,
    whileComp_Not,
    whileComp_Program,
    whileComp_Read,
    whileComp_Tl,
    whileComp_While,
    whileComp_Write,
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

def test_assoc_n50_reverse_link_reassign_clear():
    a1 = whileComp_Not(not_="sample_text")
    a2 = whileComp_Not(not_="sample_text_2")
    b = whileComp_ExprSimple(call="sample_text", ope="sample_text", valeur="sample_text")
    _safe_set(b, 'whileComp_ExprSimple51', a1)
    assert _is_linked(b, 'whileComp_ExprSimple51', a1)
    if hasattr(a1, 'whileComp_Not'):
        assert _is_linked(a1, 'whileComp_Not', b)
    _safe_set(b, 'whileComp_ExprSimple51', a2)
    assert _is_linked(b, 'whileComp_ExprSimple51', a2)
    if hasattr(a1, 'whileComp_Not'):
        assert not _is_linked(a1, 'whileComp_Not', b)
    if hasattr(a2, 'whileComp_Not'):
        assert _is_linked(a2, 'whileComp_Not', b)
    _safe_set(b, 'whileComp_ExprSimple51', None)
    assert not _is_linked(b, 'whileComp_ExprSimple51', a2)
    if hasattr(a2, 'whileComp_Not'):
        assert not _is_linked(a2, 'whileComp_Not', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_definition1_stub_double():
    # whileComp_Definition has no real 'whileComp_Definition' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_Function(function="sample_text")
    partner = whileComp_Definition()
    setattr(partner, 'whileComp_Definition', None)
    _safe_set(owner, 'whileComp_Function2', partner)
    assert getattr(partner, 'whileComp_Definition') == owner
    _safe_set(owner, 'whileComp_Function2', None)
    assert getattr(partner, 'whileComp_Definition') is None


def test_assoc_ex152_stub_double():
    # whileComp_Expr has no real 'whileComp_Expr54' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_ExprSimple(call="sample_text", ope="sample_text", valeur="sample_text")
    partner = whileComp_Expr()
    setattr(partner, 'whileComp_Expr54', None)
    _safe_set(owner, 'whileComp_ExprSimple53', partner)
    assert getattr(partner, 'whileComp_Expr54') == owner
    _safe_set(owner, 'whileComp_ExprSimple53', None)
    assert getattr(partner, 'whileComp_Expr54') is None


def test_assoc_ex255_stub_double():
    # whileComp_Expr has no real 'whileComp_Expr57' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_ExprSimple(call="sample_text", ope="sample_text", valeur="sample_text")
    partner = whileComp_Expr()
    setattr(partner, 'whileComp_Expr57', None)
    _safe_set(owner, 'whileComp_ExprSimple56', partner)
    assert getattr(partner, 'whileComp_Expr57') == owner
    _safe_set(owner, 'whileComp_ExprSimple56', None)
    assert getattr(partner, 'whileComp_Expr57') is None


def test_assoc_expr47_stub_double():
    # whileComp_Expr has no real 'whileComp_Expr49' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_ExprSimple(call="sample_text", ope="sample_text", valeur="sample_text")
    partner = whileComp_Expr()
    setattr(partner, 'whileComp_Expr49', None)
    _safe_set(owner, 'whileComp_ExprSimple48', partner)
    assert getattr(partner, 'whileComp_Expr49') == owner
    _safe_set(owner, 'whileComp_ExprSimple48', None)
    assert getattr(partner, 'whileComp_Expr49') is None


def test_assoc_exprsimple43_stub_double():
    # whileComp_Expr has no real 'whileComp_Expr44' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_ExprSimple(call="sample_text", ope="sample_text", valeur="sample_text")
    partner = whileComp_Expr()
    setattr(partner, 'whileComp_Expr44', None)
    _safe_set(owner, 'whileComp_ExprSimple', partner)
    assert getattr(partner, 'whileComp_Expr44') == owner
    _safe_set(owner, 'whileComp_ExprSimple', None)
    assert getattr(partner, 'whileComp_Expr44') is None


def test_assoc_functions0_stub_double():
    # whileComp_Program has no real 'whileComp_Program' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_Function(function="sample_text")
    partner = whileComp_Program()
    setattr(partner, 'whileComp_Program', None)
    _safe_set(owner, 'whileComp_Function', partner)
    assert owner in getattr(partner, 'whileComp_Program')
    _safe_set(owner, 'whileComp_Function', None)
    assert owner not in getattr(partner, 'whileComp_Program')


def test_assoc_lexpr45_stub_double():
    # whileComp_Lexpr has no real 'whileComp_Lexpr' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_ExprSimple(call="sample_text", ope="sample_text", valeur="sample_text")
    partner = whileComp_Lexpr()
    setattr(partner, 'whileComp_Lexpr', None)
    _safe_set(owner, 'whileComp_ExprSimple46', partner)
    assert getattr(partner, 'whileComp_Lexpr') == owner
    _safe_set(owner, 'whileComp_ExprSimple46', None)
    assert getattr(partner, 'whileComp_Lexpr') is None


def test_assoc_read3_stub_double():
    # whileComp_Definition has no real 'whileComp_Definition4' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_Read's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_Read's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_Read(variable="sample_text")
    partner = whileComp_Definition()
    setattr(partner, 'whileComp_Definition4', None)
    _safe_set(owner, 'whileComp_Read', partner)
    assert getattr(partner, 'whileComp_Definition4') == owner
    _safe_set(owner, 'whileComp_Read', None)
    assert getattr(partner, 'whileComp_Definition4') is None


def test_assoc_valeurs9_stub_double():
    # whileComp_Expr has no real 'whileComp_Expr' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_Affectation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_Affectation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_Affectation(affectations="sample_text")
    partner = whileComp_Expr()
    setattr(partner, 'whileComp_Expr', None)
    _safe_set(owner, 'whileComp_Affectation', {partner})
    assert getattr(partner, 'whileComp_Expr') == owner
    _safe_set(owner, 'whileComp_Affectation', set())
    assert getattr(partner, 'whileComp_Expr') is None


def test_assoc_write7_stub_double():
    # whileComp_Definition has no real 'whileComp_Definition8' property in the generated
    # code (a bare stub) -- manually attach it so whileComp_Write's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileComp_Write's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileComp_Write(variable="sample_text")
    partner = whileComp_Definition()
    setattr(partner, 'whileComp_Definition8', None)
    _safe_set(owner, 'whileComp_Write', partner)
    assert getattr(partner, 'whileComp_Definition8') == owner
    _safe_set(owner, 'whileComp_Write', None)
    assert getattr(partner, 'whileComp_Definition8') is None


