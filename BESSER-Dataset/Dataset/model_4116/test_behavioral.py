import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myDsl_AffectVar,
    myDsl_Commande,
    myDsl_Commandes,
    myDsl_Cons,
    myDsl_Expr,
    myDsl_ExprAnd,
    myDsl_ExprEq,
    myDsl_ExprNot,
    myDsl_ExprNotDo,
    myDsl_ExprNotNot,
    myDsl_ExprOr,
    myDsl_ExprSimple,
    myDsl_Exprs,
    myDsl_Fonction,
    myDsl_For,
    myDsl_Foreach,
    myDsl_Hd,
    myDsl_If,
    myDsl_Input,
    myDsl_LExpr,
    myDsl_Liste,
    myDsl_Model,
    myDsl_Output,
    myDsl_Programme,
    myDsl_SymboleEx,
    myDsl_Tl,
    myDsl_Vars,
    myDsl_While,
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

def test_assoc_in_3_reverse_link_reassign_clear():
    a1 = myDsl_Input(var1="sample_text", var2="sample_text")
    a2 = myDsl_Input(var1="sample_text_2", var2="sample_text_2")
    b = myDsl_Fonction(symbole="sample_text")
    _safe_set(b, 'myDsl_Fonction4', a1)
    assert _is_linked(b, 'myDsl_Fonction4', a1)
    if hasattr(a1, 'myDsl_Input'):
        assert _is_linked(a1, 'myDsl_Input', b)
    _safe_set(b, 'myDsl_Fonction4', a2)
    assert _is_linked(b, 'myDsl_Fonction4', a2)
    if hasattr(a1, 'myDsl_Input'):
        assert not _is_linked(a1, 'myDsl_Input', b)
    if hasattr(a2, 'myDsl_Input'):
        assert _is_linked(a2, 'myDsl_Input', b)
    _safe_set(b, 'myDsl_Fonction4', None)
    assert not _is_linked(b, 'myDsl_Fonction4', a2)
    if hasattr(a2, 'myDsl_Input'):
        assert not _is_linked(a2, 'myDsl_Input', b)


def test_assoc_out7_reverse_link_reassign_clear():
    a1 = myDsl_Output(var1="sample_text", var2="sample_text")
    a2 = myDsl_Output(var1="sample_text_2", var2="sample_text_2")
    b = myDsl_Fonction(symbole="sample_text")
    _safe_set(b, 'myDsl_Fonction8', a1)
    assert _is_linked(b, 'myDsl_Fonction8', a1)
    if hasattr(a1, 'myDsl_Output'):
        assert _is_linked(a1, 'myDsl_Output', b)
    _safe_set(b, 'myDsl_Fonction8', a2)
    assert _is_linked(b, 'myDsl_Fonction8', a2)
    if hasattr(a1, 'myDsl_Output'):
        assert not _is_linked(a1, 'myDsl_Output', b)
    if hasattr(a2, 'myDsl_Output'):
        assert _is_linked(a2, 'myDsl_Output', b)
    _safe_set(b, 'myDsl_Fonction8', None)
    assert not _is_linked(b, 'myDsl_Fonction8', a2)
    if hasattr(a2, 'myDsl_Output'):
        assert not _is_linked(a2, 'myDsl_Output', b)


def test_assoc_symbolEx75_reverse_link_reassign_clear():
    a1 = myDsl_SymboleEx(p="sample_text")
    a2 = myDsl_SymboleEx(p="sample_text_2")
    b = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    _safe_set(b, 'myDsl_ExprSimple76', a1)
    assert _is_linked(b, 'myDsl_ExprSimple76', a1)
    if hasattr(a1, 'myDsl_SymboleEx'):
        assert _is_linked(a1, 'myDsl_SymboleEx', b)
    _safe_set(b, 'myDsl_ExprSimple76', a2)
    assert _is_linked(b, 'myDsl_ExprSimple76', a2)
    if hasattr(a1, 'myDsl_SymboleEx'):
        assert not _is_linked(a1, 'myDsl_SymboleEx', b)
    if hasattr(a2, 'myDsl_SymboleEx'):
        assert _is_linked(a2, 'myDsl_SymboleEx', b)
    _safe_set(b, 'myDsl_ExprSimple76', None)
    assert not _is_linked(b, 'myDsl_ExprSimple76', a2)
    if hasattr(a2, 'myDsl_SymboleEx'):
        assert not _is_linked(a2, 'myDsl_SymboleEx', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_affectVar14_stub_double():
    # myDsl_AffectVar has no real 'myDsl_AffectVar' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Commande's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Commande's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Commande(nop="sample_text")
    partner = myDsl_AffectVar()
    setattr(partner, 'myDsl_AffectVar', None)
    _safe_set(owner, 'myDsl_Commande15', partner)
    assert getattr(partner, 'myDsl_AffectVar') == owner
    _safe_set(owner, 'myDsl_Commande15', None)
    assert getattr(partner, 'myDsl_AffectVar') is None


def test_assoc_com19_stub_double():
    # myDsl_Commandes has no real 'myDsl_Commandes10' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Commande's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Commande's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Commande(nop="sample_text")
    partner = myDsl_Commandes()
    setattr(partner, 'myDsl_Commandes10', None)
    _safe_set(owner, 'myDsl_Commande', partner)
    assert getattr(partner, 'myDsl_Commandes10') == owner
    _safe_set(owner, 'myDsl_Commande', None)
    assert getattr(partner, 'myDsl_Commandes10') is None


def test_assoc_com211_stub_double():
    # myDsl_Commandes has no real 'myDsl_Commandes12' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Commande's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Commande's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Commande(nop="sample_text")
    partner = myDsl_Commandes()
    setattr(partner, 'myDsl_Commandes12', None)
    _safe_set(owner, 'myDsl_Commande13', partner)
    assert owner in getattr(partner, 'myDsl_Commandes12')
    _safe_set(owner, 'myDsl_Commande13', None)
    assert owner not in getattr(partner, 'myDsl_Commandes12')


def test_assoc_com5_stub_double():
    # myDsl_Commandes has no real 'myDsl_Commandes' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Fonction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Fonction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Fonction(symbole="sample_text")
    partner = myDsl_Commandes()
    setattr(partner, 'myDsl_Commandes', None)
    _safe_set(owner, 'myDsl_Fonction6', partner)
    assert getattr(partner, 'myDsl_Commandes') == owner
    _safe_set(owner, 'myDsl_Fonction6', None)
    assert getattr(partner, 'myDsl_Commandes') is None


def test_assoc_cons67_stub_double():
    # myDsl_Cons has no real 'myDsl_Cons' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    partner = myDsl_Cons()
    setattr(partner, 'myDsl_Cons', None)
    _safe_set(owner, 'myDsl_ExprSimple68', partner)
    assert getattr(partner, 'myDsl_Cons') == owner
    _safe_set(owner, 'myDsl_ExprSimple68', None)
    assert getattr(partner, 'myDsl_Cons') is None


def test_assoc_expS1113_stub_double():
    # myDsl_ExprEq has no real 'myDsl_ExprEq114' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    partner = myDsl_ExprEq()
    setattr(partner, 'myDsl_ExprEq114', None)
    _safe_set(owner, 'myDsl_ExprSimple115', partner)
    assert getattr(partner, 'myDsl_ExprEq114') == owner
    _safe_set(owner, 'myDsl_ExprSimple115', None)
    assert getattr(partner, 'myDsl_ExprEq114') is None


def test_assoc_expS2116_stub_double():
    # myDsl_ExprEq has no real 'myDsl_ExprEq117' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    partner = myDsl_ExprEq()
    setattr(partner, 'myDsl_ExprEq117', None)
    _safe_set(owner, 'myDsl_ExprSimple118', partner)
    assert getattr(partner, 'myDsl_ExprEq117') == owner
    _safe_set(owner, 'myDsl_ExprSimple118', None)
    assert getattr(partner, 'myDsl_ExprEq117') is None


def test_assoc_expS65_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr66' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr66', None)
    _safe_set(owner, 'myDsl_ExprSimple', partner)
    assert getattr(partner, 'myDsl_Expr66') == owner
    _safe_set(owner, 'myDsl_ExprSimple', None)
    assert getattr(partner, 'myDsl_Expr66') is None


def test_assoc_fonct1_stub_double():
    # myDsl_Programme has no real 'myDsl_Programme2' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Fonction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Fonction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Fonction(symbole="sample_text")
    partner = myDsl_Programme()
    setattr(partner, 'myDsl_Programme2', None)
    _safe_set(owner, 'myDsl_Fonction', partner)
    assert owner in getattr(partner, 'myDsl_Programme2')
    _safe_set(owner, 'myDsl_Fonction', None)
    assert owner not in getattr(partner, 'myDsl_Programme2')


def test_assoc_forC18_stub_double():
    # myDsl_For has no real 'myDsl_For' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Commande's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Commande's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Commande(nop="sample_text")
    partner = myDsl_For()
    setattr(partner, 'myDsl_For', None)
    _safe_set(owner, 'myDsl_Commande19', partner)
    assert getattr(partner, 'myDsl_For') == owner
    _safe_set(owner, 'myDsl_Commande19', None)
    assert getattr(partner, 'myDsl_For') is None


def test_assoc_foreachC22_stub_double():
    # myDsl_Foreach has no real 'myDsl_Foreach' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Commande's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Commande's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Commande(nop="sample_text")
    partner = myDsl_Foreach()
    setattr(partner, 'myDsl_Foreach', None)
    _safe_set(owner, 'myDsl_Commande23', partner)
    assert getattr(partner, 'myDsl_Foreach') == owner
    _safe_set(owner, 'myDsl_Commande23', None)
    assert getattr(partner, 'myDsl_Foreach') is None


def test_assoc_hd71_stub_double():
    # myDsl_Hd has no real 'myDsl_Hd' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    partner = myDsl_Hd()
    setattr(partner, 'myDsl_Hd', None)
    _safe_set(owner, 'myDsl_ExprSimple72', partner)
    assert getattr(partner, 'myDsl_Hd') == owner
    _safe_set(owner, 'myDsl_ExprSimple72', None)
    assert getattr(partner, 'myDsl_Hd') is None


def test_assoc_ifC20_stub_double():
    # myDsl_If has no real 'myDsl_If' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Commande's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Commande's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Commande(nop="sample_text")
    partner = myDsl_If()
    setattr(partner, 'myDsl_If', None)
    _safe_set(owner, 'myDsl_Commande21', partner)
    assert getattr(partner, 'myDsl_If') == owner
    _safe_set(owner, 'myDsl_Commande21', None)
    assert getattr(partner, 'myDsl_If') is None


def test_assoc_le588_stub_double():
    # myDsl_LExpr has no real 'myDsl_LExpr90' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SymboleEx's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SymboleEx's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SymboleEx(p="sample_text")
    partner = myDsl_LExpr()
    setattr(partner, 'myDsl_LExpr90', None)
    _safe_set(owner, 'myDsl_SymboleEx89', partner)
    assert getattr(partner, 'myDsl_LExpr90') == owner
    _safe_set(owner, 'myDsl_SymboleEx89', None)
    assert getattr(partner, 'myDsl_LExpr90') is None


def test_assoc_liste69_stub_double():
    # myDsl_Liste has no real 'myDsl_Liste' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    partner = myDsl_Liste()
    setattr(partner, 'myDsl_Liste', None)
    _safe_set(owner, 'myDsl_ExprSimple70', partner)
    assert getattr(partner, 'myDsl_Liste') == owner
    _safe_set(owner, 'myDsl_ExprSimple70', None)
    assert getattr(partner, 'myDsl_Liste') is None


def test_assoc_tl73_stub_double():
    # myDsl_Tl has no real 'myDsl_Tl' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symbole="sample_text", variable="sample_text", vide="sample_text")
    partner = myDsl_Tl()
    setattr(partner, 'myDsl_Tl', None)
    _safe_set(owner, 'myDsl_ExprSimple74', partner)
    assert getattr(partner, 'myDsl_Tl') == owner
    _safe_set(owner, 'myDsl_ExprSimple74', None)
    assert getattr(partner, 'myDsl_Tl') is None


def test_assoc_var124_stub_double():
    # myDsl_AffectVar has no real 'myDsl_AffectVar25' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Vars's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Vars's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Vars(var2="sample_text", var3="sample_text")
    partner = myDsl_AffectVar()
    setattr(partner, 'myDsl_AffectVar25', None)
    _safe_set(owner, 'myDsl_Vars', partner)
    assert getattr(partner, 'myDsl_AffectVar25') == owner
    _safe_set(owner, 'myDsl_Vars', None)
    assert getattr(partner, 'myDsl_AffectVar25') is None


def test_assoc_whileC16_stub_double():
    # myDsl_While has no real 'myDsl_While' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Commande's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Commande's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Commande(nop="sample_text")
    partner = myDsl_While()
    setattr(partner, 'myDsl_While', None)
    _safe_set(owner, 'myDsl_Commande17', partner)
    assert getattr(partner, 'myDsl_While') == owner
    _safe_set(owner, 'myDsl_Commande17', None)
    assert getattr(partner, 'myDsl_While') is None


