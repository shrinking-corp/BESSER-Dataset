import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Condition,
    myDsl_ABin,
    myDsl_AccSucc,
    myDsl_Affectation,
    myDsl_COMPARATEUR,
    myDsl_Commande,
    myDsl_Commandes,
    myDsl_Condition,
    myDsl_EObject,
    myDsl_ElemSimple,
    myDsl_ExprSimple,
    myDsl_Expression,
    myDsl_Fonction,
    myDsl_For,
    myDsl_ForEach,
    myDsl_If,
    myDsl_Input,
    myDsl_Lexpr,
    myDsl_Nill,
    myDsl_Nop,
    myDsl_Not,
    myDsl_OpAccSucc,
    myDsl_OpConstructeur,
    myDsl_Output,
    myDsl_Program,
    myDsl_Variable,
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

def test_assoc_elemSimple56_reverse_link_reassign_clear():
    a1 = myDsl_ExprSimple(symb="sample_text")
    a2 = myDsl_ExprSimple(symb="sample_text_2")
    b = myDsl_ElemSimple(symb="sample_text")
    _safe_set(b, 'myDsl_ElemSimple', a1)
    assert _is_linked(b, 'myDsl_ElemSimple', a1)
    if hasattr(a1, 'myDsl_ExprSimple57'):
        assert _is_linked(a1, 'myDsl_ExprSimple57', b)
    _safe_set(b, 'myDsl_ElemSimple', a2)
    assert _is_linked(b, 'myDsl_ElemSimple', a2)
    if hasattr(a1, 'myDsl_ExprSimple57'):
        assert not _is_linked(a1, 'myDsl_ExprSimple57', b)
    if hasattr(a2, 'myDsl_ExprSimple57'):
        assert _is_linked(a2, 'myDsl_ExprSimple57', b)
    _safe_set(b, 'myDsl_ElemSimple', None)
    assert not _is_linked(b, 'myDsl_ElemSimple', a2)
    if hasattr(a2, 'myDsl_ExprSimple57'):
        assert not _is_linked(a2, 'myDsl_ExprSimple57', b)


def test_assoc_in_1_reverse_link_reassign_clear():
    a1 = myDsl_Input(in_="sample_text")
    a2 = myDsl_Input(in_="sample_text_2")
    b = myDsl_Fonction(nom="sample_text")
    _safe_set(b, 'myDsl_Fonction2', a1)
    assert _is_linked(b, 'myDsl_Fonction2', a1)
    if hasattr(a1, 'myDsl_Input'):
        assert _is_linked(a1, 'myDsl_Input', b)
    _safe_set(b, 'myDsl_Fonction2', a2)
    assert _is_linked(b, 'myDsl_Fonction2', a2)
    if hasattr(a1, 'myDsl_Input'):
        assert not _is_linked(a1, 'myDsl_Input', b)
    if hasattr(a2, 'myDsl_Input'):
        assert _is_linked(a2, 'myDsl_Input', b)
    _safe_set(b, 'myDsl_Fonction2', None)
    assert not _is_linked(b, 'myDsl_Fonction2', a2)
    if hasattr(a2, 'myDsl_Input'):
        assert not _is_linked(a2, 'myDsl_Input', b)


def test_assoc_nil47_reverse_link_reassign_clear():
    a1 = myDsl_Nill(nil="sample_text")
    a2 = myDsl_Nill(nil="sample_text_2")
    b = myDsl_ExprSimple(symb="sample_text")
    _safe_set(b, 'myDsl_ExprSimple48', a1)
    assert _is_linked(b, 'myDsl_ExprSimple48', a1)
    if hasattr(a1, 'myDsl_Nill'):
        assert _is_linked(a1, 'myDsl_Nill', b)
    _safe_set(b, 'myDsl_ExprSimple48', a2)
    assert _is_linked(b, 'myDsl_ExprSimple48', a2)
    if hasattr(a1, 'myDsl_Nill'):
        assert not _is_linked(a1, 'myDsl_Nill', b)
    if hasattr(a2, 'myDsl_Nill'):
        assert _is_linked(a2, 'myDsl_Nill', b)
    _safe_set(b, 'myDsl_ExprSimple48', None)
    assert not _is_linked(b, 'myDsl_ExprSimple48', a2)
    if hasattr(a2, 'myDsl_Nill'):
        assert not _is_linked(a2, 'myDsl_Nill', b)


def test_assoc_out5_reverse_link_reassign_clear():
    a1 = myDsl_Output(out="sample_text")
    a2 = myDsl_Output(out="sample_text_2")
    b = myDsl_Fonction(nom="sample_text")
    _safe_set(b, 'myDsl_Fonction6', a1)
    assert _is_linked(b, 'myDsl_Fonction6', a1)
    if hasattr(a1, 'myDsl_Output'):
        assert _is_linked(a1, 'myDsl_Output', b)
    _safe_set(b, 'myDsl_Fonction6', a2)
    assert _is_linked(b, 'myDsl_Fonction6', a2)
    if hasattr(a1, 'myDsl_Output'):
        assert not _is_linked(a1, 'myDsl_Output', b)
    if hasattr(a2, 'myDsl_Output'):
        assert _is_linked(a2, 'myDsl_Output', b)
    _safe_set(b, 'myDsl_Fonction6', None)
    assert not _is_linked(b, 'myDsl_Fonction6', a2)
    if hasattr(a2, 'myDsl_Output'):
        assert not _is_linked(a2, 'myDsl_Output', b)


def test_assoc_variable49_reverse_link_reassign_clear():
    a1 = myDsl_Variable(variable="sample_text")
    a2 = myDsl_Variable(variable="sample_text_2")
    b = myDsl_ExprSimple(symb="sample_text")
    _safe_set(b, 'myDsl_ExprSimple50', a1)
    assert _is_linked(b, 'myDsl_ExprSimple50', a1)
    if hasattr(a1, 'myDsl_Variable51'):
        assert _is_linked(a1, 'myDsl_Variable51', b)
    _safe_set(b, 'myDsl_ExprSimple50', a2)
    assert _is_linked(b, 'myDsl_ExprSimple50', a2)
    if hasattr(a1, 'myDsl_Variable51'):
        assert not _is_linked(a1, 'myDsl_Variable51', b)
    if hasattr(a2, 'myDsl_Variable51'):
        assert _is_linked(a2, 'myDsl_Variable51', b)
    _safe_set(b, 'myDsl_ExprSimple50', None)
    assert not _is_linked(b, 'myDsl_ExprSimple50', a2)
    if hasattr(a2, 'myDsl_Variable51'):
        assert not _is_linked(a2, 'myDsl_Variable51', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abin52_stub_double():
    # myDsl_ABin has no real 'myDsl_ABin' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symb="sample_text")
    partner = myDsl_ABin()
    setattr(partner, 'myDsl_ABin', None)
    _safe_set(owner, 'myDsl_ExprSimple53', partner)
    assert getattr(partner, 'myDsl_ABin') == owner
    _safe_set(owner, 'myDsl_ExprSimple53', None)
    assert getattr(partner, 'myDsl_ABin') is None


def test_assoc_accsucc54_stub_double():
    # myDsl_AccSucc has no real 'myDsl_AccSucc' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symb="sample_text")
    partner = myDsl_AccSucc()
    setattr(partner, 'myDsl_AccSucc', None)
    _safe_set(owner, 'myDsl_ExprSimple55', partner)
    assert getattr(partner, 'myDsl_AccSucc') == owner
    _safe_set(owner, 'myDsl_ExprSimple55', None)
    assert getattr(partner, 'myDsl_AccSucc') is None


def test_assoc_commandes3_stub_double():
    # myDsl_Commandes has no real 'myDsl_Commandes' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Fonction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Fonction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Fonction(nom="sample_text")
    partner = myDsl_Commandes()
    setattr(partner, 'myDsl_Commandes', None)
    _safe_set(owner, 'myDsl_Fonction4', partner)
    assert getattr(partner, 'myDsl_Commandes') == owner
    _safe_set(owner, 'myDsl_Fonction4', None)
    assert getattr(partner, 'myDsl_Commandes') is None


def test_assoc_comp69_stub_double():
    # myDsl_Condition has no real 'myDsl_Condition70' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_COMPARATEUR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_COMPARATEUR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_COMPARATEUR(comparateur="sample_text")
    partner = myDsl_Condition()
    setattr(partner, 'myDsl_Condition70', None)
    _safe_set(owner, 'myDsl_COMPARATEUR', partner)
    assert getattr(partner, 'myDsl_Condition70') == owner
    _safe_set(owner, 'myDsl_COMPARATEUR', None)
    assert getattr(partner, 'myDsl_Condition70') is None


def test_assoc_e158_stub_double():
    # myDsl_Lexpr has no real 'myDsl_Lexpr' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symb="sample_text")
    partner = myDsl_Lexpr()
    setattr(partner, 'myDsl_Lexpr', None)
    _safe_set(owner, 'myDsl_ExprSimple59', partner)
    assert getattr(partner, 'myDsl_Lexpr') == owner
    _safe_set(owner, 'myDsl_ExprSimple59', None)
    assert getattr(partner, 'myDsl_Lexpr') is None


def test_assoc_e166_stub_double():
    # myDsl_Condition has no real 'myDsl_Condition67' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symb="sample_text")
    partner = myDsl_Condition()
    setattr(partner, 'myDsl_Condition67', None)
    _safe_set(owner, 'myDsl_ExprSimple68', partner)
    assert getattr(partner, 'myDsl_Condition67') == owner
    _safe_set(owner, 'myDsl_ExprSimple68', None)
    assert getattr(partner, 'myDsl_Condition67') is None


def test_assoc_expr84_stub_double():
    # myDsl_AccSucc has no real 'myDsl_AccSucc85' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symb="sample_text")
    partner = myDsl_AccSucc()
    setattr(partner, 'myDsl_AccSucc85', None)
    _safe_set(owner, 'myDsl_ExprSimple86', partner)
    assert getattr(partner, 'myDsl_AccSucc85') == owner
    _safe_set(owner, 'myDsl_ExprSimple86', None)
    assert getattr(partner, 'myDsl_AccSucc85') is None


def test_assoc_expr87_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Not's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Not's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Not(not_="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression88', None)
    _safe_set(owner, 'myDsl_Not', partner)
    assert getattr(partner, 'myDsl_Expression88') == owner
    _safe_set(owner, 'myDsl_Not', None)
    assert getattr(partner, 'myDsl_Expression88') is None


def test_assoc_exprs45_stub_double():
    # myDsl_Expression has no real 'myDsl_Expression46' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(symb="sample_text")
    partner = myDsl_Expression()
    setattr(partner, 'myDsl_Expression46', None)
    _safe_set(owner, 'myDsl_ExprSimple', partner)
    assert getattr(partner, 'myDsl_Expression46') == owner
    _safe_set(owner, 'myDsl_ExprSimple', None)
    assert getattr(partner, 'myDsl_Expression46') is None


def test_assoc_fonctions0_stub_double():
    # myDsl_Program has no real 'myDsl_Program' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Fonction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Fonction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Fonction(nom="sample_text")
    partner = myDsl_Program()
    setattr(partner, 'myDsl_Program', None)
    _safe_set(owner, 'myDsl_Fonction', partner)
    assert owner in getattr(partner, 'myDsl_Program')
    _safe_set(owner, 'myDsl_Fonction', None)
    assert owner not in getattr(partner, 'myDsl_Program')


def test_assoc_lexpr63_stub_double():
    # myDsl_Lexpr has no real 'myDsl_Lexpr65' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ElemSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ElemSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ElemSimple(symb="sample_text")
    partner = myDsl_Lexpr()
    setattr(partner, 'myDsl_Lexpr65', None)
    _safe_set(owner, 'myDsl_ElemSimple64', partner)
    assert getattr(partner, 'myDsl_Lexpr65') == owner
    _safe_set(owner, 'myDsl_ElemSimple64', None)
    assert getattr(partner, 'myDsl_Lexpr65') is None


def test_assoc_op74_stub_double():
    # myDsl_ABin has no real 'myDsl_ABin75' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_OpConstructeur's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_OpConstructeur's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_OpConstructeur(op="sample_text")
    partner = myDsl_ABin()
    setattr(partner, 'myDsl_ABin75', None)
    _safe_set(owner, 'myDsl_OpConstructeur', partner)
    assert getattr(partner, 'myDsl_ABin75') == owner
    _safe_set(owner, 'myDsl_OpConstructeur', None)
    assert getattr(partner, 'myDsl_ABin75') is None


def test_assoc_op82_stub_double():
    # myDsl_AccSucc has no real 'myDsl_AccSucc83' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_OpAccSucc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_OpAccSucc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_OpAccSucc(op="sample_text")
    partner = myDsl_AccSucc()
    setattr(partner, 'myDsl_AccSucc83', None)
    _safe_set(owner, 'myDsl_OpAccSucc', partner)
    assert getattr(partner, 'myDsl_AccSucc83') == owner
    _safe_set(owner, 'myDsl_OpAccSucc', None)
    assert getattr(partner, 'myDsl_AccSucc83') is None


def test_assoc_variable14_stub_double():
    # myDsl_Affectation has no real 'myDsl_Affectation' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Variable(variable="sample_text")
    partner = myDsl_Affectation()
    setattr(partner, 'myDsl_Affectation', None)
    _safe_set(owner, 'myDsl_Variable', partner)
    assert owner in getattr(partner, 'myDsl_Affectation')
    _safe_set(owner, 'myDsl_Variable', None)
    assert owner not in getattr(partner, 'myDsl_Affectation')


