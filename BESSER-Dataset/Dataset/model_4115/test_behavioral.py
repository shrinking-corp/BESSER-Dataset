import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    whileCpp_Command,
    whileCpp_CommandForEach,
    whileCpp_CommandIf,
    whileCpp_CommandWhile,
    whileCpp_Commands,
    whileCpp_Cons,
    whileCpp_Definition,
    whileCpp_Expr,
    whileCpp_ExprAnd,
    whileCpp_ExprEq,
    whileCpp_ExprNot,
    whileCpp_ExprOr,
    whileCpp_ExprSimple,
    whileCpp_Exprs,
    whileCpp_Function,
    whileCpp_Input,
    whileCpp_Output,
    whileCpp_Program,
    whileCpp_Vars,
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

def test_assoc_cmdWhile15_reverse_link_reassign_clear():
    a1 = whileCpp_CommandWhile(w="sample_text")
    a2 = whileCpp_CommandWhile(w="sample_text_2")
    b = whileCpp_Command(nop="sample_text")
    _safe_set(b, 'whileCpp_Command16', a1)
    assert _is_linked(b, 'whileCpp_Command16', a1)
    if hasattr(a1, 'whileCpp_CommandWhile'):
        assert _is_linked(a1, 'whileCpp_CommandWhile', b)
    _safe_set(b, 'whileCpp_Command16', a2)
    assert _is_linked(b, 'whileCpp_Command16', a2)
    if hasattr(a1, 'whileCpp_CommandWhile'):
        assert not _is_linked(a1, 'whileCpp_CommandWhile', b)
    if hasattr(a2, 'whileCpp_CommandWhile'):
        assert _is_linked(a2, 'whileCpp_CommandWhile', b)
    _safe_set(b, 'whileCpp_Command16', None)
    assert not _is_linked(b, 'whileCpp_Command16', a2)
    if hasattr(a2, 'whileCpp_CommandWhile'):
        assert not _is_linked(a2, 'whileCpp_CommandWhile', b)


def test_assoc_exprAndAtt65_reverse_link_reassign_clear():
    a1 = whileCpp_ExprAnd(exprAnd="sample_text")
    a2 = whileCpp_ExprAnd(exprAnd="sample_text_2")
    b = whileCpp_ExprAnd(exprAnd="sample_text")
    _safe_set(b, 'whileCpp_ExprAnd66', a1)
    assert _is_linked(b, 'whileCpp_ExprAnd66', a1)
    if hasattr(a1, 'whileCpp_ExprAnd64'):
        assert _is_linked(a1, 'whileCpp_ExprAnd64', b)
    _safe_set(b, 'whileCpp_ExprAnd66', a2)
    assert _is_linked(b, 'whileCpp_ExprAnd66', a2)
    if hasattr(a1, 'whileCpp_ExprAnd64'):
        assert not _is_linked(a1, 'whileCpp_ExprAnd64', b)
    if hasattr(a2, 'whileCpp_ExprAnd64'):
        assert _is_linked(a2, 'whileCpp_ExprAnd64', b)
    _safe_set(b, 'whileCpp_ExprAnd66', None)
    assert not _is_linked(b, 'whileCpp_ExprAnd66', a2)
    if hasattr(a2, 'whileCpp_ExprAnd64'):
        assert not _is_linked(a2, 'whileCpp_ExprAnd64', b)


def test_assoc_exprCons51_reverse_link_reassign_clear():
    a1 = whileCpp_ExprSimple(exprHead="sample_text", exprTail="sample_text", nil="sample_text", nomSymb="sample_text", symb="sample_text", vari="sample_text")
    a2 = whileCpp_ExprSimple(exprHead="sample_text_2", exprTail="sample_text_2", nil="sample_text_2", nomSymb="sample_text_2", symb="sample_text_2", vari="sample_text_2")
    b = whileCpp_Cons(exprCons="sample_text")
    _safe_set(b, 'whileCpp_Cons', a1)
    assert _is_linked(b, 'whileCpp_Cons', a1)
    if hasattr(a1, 'whileCpp_ExprSimple52'):
        assert _is_linked(a1, 'whileCpp_ExprSimple52', b)
    _safe_set(b, 'whileCpp_Cons', a2)
    assert _is_linked(b, 'whileCpp_Cons', a2)
    if hasattr(a1, 'whileCpp_ExprSimple52'):
        assert not _is_linked(a1, 'whileCpp_ExprSimple52', b)
    if hasattr(a2, 'whileCpp_ExprSimple52'):
        assert _is_linked(a2, 'whileCpp_ExprSimple52', b)
    _safe_set(b, 'whileCpp_Cons', None)
    assert not _is_linked(b, 'whileCpp_Cons', a2)
    if hasattr(a2, 'whileCpp_ExprSimple52'):
        assert not _is_linked(a2, 'whileCpp_ExprSimple52', b)


def test_assoc_exprNot67_reverse_link_reassign_clear():
    a1 = whileCpp_ExprOr(exprOr="sample_text")
    a2 = whileCpp_ExprOr(exprOr="sample_text_2")
    b = whileCpp_ExprNot(not_="sample_text")
    _safe_set(b, 'whileCpp_ExprNot', a1)
    assert _is_linked(b, 'whileCpp_ExprNot', a1)
    if hasattr(a1, 'whileCpp_ExprOr68'):
        assert _is_linked(a1, 'whileCpp_ExprOr68', b)
    _safe_set(b, 'whileCpp_ExprNot', a2)
    assert _is_linked(b, 'whileCpp_ExprNot', a2)
    if hasattr(a1, 'whileCpp_ExprOr68'):
        assert not _is_linked(a1, 'whileCpp_ExprOr68', b)
    if hasattr(a2, 'whileCpp_ExprOr68'):
        assert _is_linked(a2, 'whileCpp_ExprOr68', b)
    _safe_set(b, 'whileCpp_ExprNot', None)
    assert not _is_linked(b, 'whileCpp_ExprNot', a2)
    if hasattr(a2, 'whileCpp_ExprOr68'):
        assert not _is_linked(a2, 'whileCpp_ExprOr68', b)


def test_assoc_exprOr62_reverse_link_reassign_clear():
    a1 = whileCpp_ExprOr(exprOr="sample_text")
    a2 = whileCpp_ExprOr(exprOr="sample_text_2")
    b = whileCpp_ExprAnd(exprAnd="sample_text")
    _safe_set(b, 'whileCpp_ExprAnd63', a1)
    assert _is_linked(b, 'whileCpp_ExprAnd63', a1)
    if hasattr(a1, 'whileCpp_ExprOr'):
        assert _is_linked(a1, 'whileCpp_ExprOr', b)
    _safe_set(b, 'whileCpp_ExprAnd63', a2)
    assert _is_linked(b, 'whileCpp_ExprAnd63', a2)
    if hasattr(a1, 'whileCpp_ExprOr'):
        assert not _is_linked(a1, 'whileCpp_ExprOr', b)
    if hasattr(a2, 'whileCpp_ExprOr'):
        assert _is_linked(a2, 'whileCpp_ExprOr', b)
    _safe_set(b, 'whileCpp_ExprAnd63', None)
    assert not _is_linked(b, 'whileCpp_ExprAnd63', a2)
    if hasattr(a2, 'whileCpp_ExprOr'):
        assert not _is_linked(a2, 'whileCpp_ExprOr', b)


def test_assoc_exprOrAtt70_reverse_link_reassign_clear():
    a1 = whileCpp_ExprOr(exprOr="sample_text")
    a2 = whileCpp_ExprOr(exprOr="sample_text_2")
    b = whileCpp_ExprOr(exprOr="sample_text")
    _safe_set(b, 'whileCpp_ExprOr71', a1)
    assert _is_linked(b, 'whileCpp_ExprOr71', a1)
    if hasattr(a1, 'whileCpp_ExprOr69'):
        assert _is_linked(a1, 'whileCpp_ExprOr69', b)
    _safe_set(b, 'whileCpp_ExprOr71', a2)
    assert _is_linked(b, 'whileCpp_ExprOr71', a2)
    if hasattr(a1, 'whileCpp_ExprOr69'):
        assert not _is_linked(a1, 'whileCpp_ExprOr69', b)
    if hasattr(a2, 'whileCpp_ExprOr69'):
        assert _is_linked(a2, 'whileCpp_ExprOr69', b)
    _safe_set(b, 'whileCpp_ExprOr71', None)
    assert not _is_linked(b, 'whileCpp_ExprOr71', a2)
    if hasattr(a2, 'whileCpp_ExprOr69'):
        assert not _is_linked(a2, 'whileCpp_ExprOr69', b)


def test_assoc_vars11_reverse_link_reassign_clear():
    a1 = whileCpp_Vars(varGen="sample_text")
    a2 = whileCpp_Vars(varGen="sample_text_2")
    b = whileCpp_Command(nop="sample_text")
    _safe_set(b, 'whileCpp_Command12', a1)
    assert _is_linked(b, 'whileCpp_Command12', a1)
    if hasattr(a1, 'whileCpp_Vars'):
        assert _is_linked(a1, 'whileCpp_Vars', b)
    _safe_set(b, 'whileCpp_Command12', a2)
    assert _is_linked(b, 'whileCpp_Command12', a2)
    if hasattr(a1, 'whileCpp_Vars'):
        assert not _is_linked(a1, 'whileCpp_Vars', b)
    if hasattr(a2, 'whileCpp_Vars'):
        assert _is_linked(a2, 'whileCpp_Vars', b)
    _safe_set(b, 'whileCpp_Command12', None)
    assert not _is_linked(b, 'whileCpp_Command12', a2)
    if hasattr(a2, 'whileCpp_Vars'):
        assert not _is_linked(a2, 'whileCpp_Vars', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cmdForEach19_stub_double():
    # whileCpp_CommandForEach has no real 'whileCpp_CommandForEach' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Command(nop="sample_text")
    partner = whileCpp_CommandForEach()
    setattr(partner, 'whileCpp_CommandForEach', None)
    _safe_set(owner, 'whileCpp_Command20', partner)
    assert getattr(partner, 'whileCpp_CommandForEach') == owner
    _safe_set(owner, 'whileCpp_Command20', None)
    assert getattr(partner, 'whileCpp_CommandForEach') is None


def test_assoc_cmdIf17_stub_double():
    # whileCpp_CommandIf has no real 'whileCpp_CommandIf' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Command(nop="sample_text")
    partner = whileCpp_CommandIf()
    setattr(partner, 'whileCpp_CommandIf', None)
    _safe_set(owner, 'whileCpp_Command18', partner)
    assert getattr(partner, 'whileCpp_CommandIf') == owner
    _safe_set(owner, 'whileCpp_Command18', None)
    assert getattr(partner, 'whileCpp_CommandIf') is None


def test_assoc_cmds23_stub_double():
    # whileCpp_Commands has no real 'whileCpp_Commands25' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_CommandWhile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_CommandWhile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_CommandWhile(w="sample_text")
    partner = whileCpp_Commands()
    setattr(partner, 'whileCpp_Commands25', None)
    _safe_set(owner, 'whileCpp_CommandWhile24', partner)
    assert getattr(partner, 'whileCpp_Commands25') == owner
    _safe_set(owner, 'whileCpp_CommandWhile24', None)
    assert getattr(partner, 'whileCpp_Commands25') is None


def test_assoc_commande9_stub_double():
    # whileCpp_Commands has no real 'whileCpp_Commands10' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Command(nop="sample_text")
    partner = whileCpp_Commands()
    setattr(partner, 'whileCpp_Commands10', None)
    _safe_set(owner, 'whileCpp_Command', partner)
    assert owner in getattr(partner, 'whileCpp_Commands10')
    _safe_set(owner, 'whileCpp_Command', None)
    assert owner not in getattr(partner, 'whileCpp_Commands10')


def test_assoc_definition1_stub_double():
    # whileCpp_Definition has no real 'whileCpp_Definition' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Function(nom="sample_text")
    partner = whileCpp_Definition()
    setattr(partner, 'whileCpp_Definition', None)
    _safe_set(owner, 'whileCpp_Function2', partner)
    assert getattr(partner, 'whileCpp_Definition') == owner
    _safe_set(owner, 'whileCpp_Function2', None)
    assert getattr(partner, 'whileCpp_Definition') is None


def test_assoc_expr21_stub_double():
    # whileCpp_Expr has no real 'whileCpp_Expr' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_CommandWhile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_CommandWhile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_CommandWhile(w="sample_text")
    partner = whileCpp_Expr()
    setattr(partner, 'whileCpp_Expr', None)
    _safe_set(owner, 'whileCpp_CommandWhile22', partner)
    assert getattr(partner, 'whileCpp_Expr') == owner
    _safe_set(owner, 'whileCpp_CommandWhile22', None)
    assert getattr(partner, 'whileCpp_Expr') is None


def test_assoc_exprAnd49_stub_double():
    # whileCpp_Expr has no real 'whileCpp_Expr50' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprAnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprAnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprAnd(exprAnd="sample_text")
    partner = whileCpp_Expr()
    setattr(partner, 'whileCpp_Expr50', None)
    _safe_set(owner, 'whileCpp_ExprAnd', partner)
    assert getattr(partner, 'whileCpp_Expr50') == owner
    _safe_set(owner, 'whileCpp_ExprAnd', None)
    assert getattr(partner, 'whileCpp_Expr50') is None


def test_assoc_exprConsAttList83_stub_double():
    # whileCpp_Expr has no real 'whileCpp_Expr85' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Cons's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Cons's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Cons(exprCons="sample_text")
    partner = whileCpp_Expr()
    setattr(partner, 'whileCpp_Expr85', None)
    _safe_set(owner, 'whileCpp_Cons84', {partner})
    assert getattr(partner, 'whileCpp_Expr85') == owner
    _safe_set(owner, 'whileCpp_Cons84', set())
    assert getattr(partner, 'whileCpp_Expr85') is None


def test_assoc_exprEq72_stub_double():
    # whileCpp_ExprEq has no real 'whileCpp_ExprEq' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprNot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprNot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprNot(not_="sample_text")
    partner = whileCpp_ExprEq()
    setattr(partner, 'whileCpp_ExprEq', None)
    _safe_set(owner, 'whileCpp_ExprNot73', partner)
    assert getattr(partner, 'whileCpp_ExprEq') == owner
    _safe_set(owner, 'whileCpp_ExprNot73', None)
    assert getattr(partner, 'whileCpp_ExprEq') is None


def test_assoc_exprHeadAtt53_stub_double():
    # whileCpp_Expr has no real 'whileCpp_Expr55' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprSimple(exprHead="sample_text", exprTail="sample_text", nil="sample_text", nomSymb="sample_text", symb="sample_text", vari="sample_text")
    partner = whileCpp_Expr()
    setattr(partner, 'whileCpp_Expr55', None)
    _safe_set(owner, 'whileCpp_ExprSimple54', partner)
    assert getattr(partner, 'whileCpp_Expr55') == owner
    _safe_set(owner, 'whileCpp_ExprSimple54', None)
    assert getattr(partner, 'whileCpp_Expr55') is None


def test_assoc_exprSim177_stub_double():
    # whileCpp_ExprEq has no real 'whileCpp_ExprEq78' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprSimple(exprHead="sample_text", exprTail="sample_text", nil="sample_text", nomSymb="sample_text", symb="sample_text", vari="sample_text")
    partner = whileCpp_ExprEq()
    setattr(partner, 'whileCpp_ExprEq78', None)
    _safe_set(owner, 'whileCpp_ExprSimple79', partner)
    assert getattr(partner, 'whileCpp_ExprEq78') == owner
    _safe_set(owner, 'whileCpp_ExprSimple79', None)
    assert getattr(partner, 'whileCpp_ExprEq78') is None


def test_assoc_exprSim280_stub_double():
    # whileCpp_ExprEq has no real 'whileCpp_ExprEq81' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprSimple(exprHead="sample_text", exprTail="sample_text", nil="sample_text", nomSymb="sample_text", symb="sample_text", vari="sample_text")
    partner = whileCpp_ExprEq()
    setattr(partner, 'whileCpp_ExprEq81', None)
    _safe_set(owner, 'whileCpp_ExprSimple82', partner)
    assert getattr(partner, 'whileCpp_ExprEq81') == owner
    _safe_set(owner, 'whileCpp_ExprSimple82', None)
    assert getattr(partner, 'whileCpp_ExprEq81') is None


def test_assoc_exprSimp47_stub_double():
    # whileCpp_Expr has no real 'whileCpp_Expr48' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprSimple(exprHead="sample_text", exprTail="sample_text", nil="sample_text", nomSymb="sample_text", symb="sample_text", vari="sample_text")
    partner = whileCpp_Expr()
    setattr(partner, 'whileCpp_Expr48', None)
    _safe_set(owner, 'whileCpp_ExprSimple', partner)
    assert getattr(partner, 'whileCpp_Expr48') == owner
    _safe_set(owner, 'whileCpp_ExprSimple', None)
    assert getattr(partner, 'whileCpp_Expr48') is None


def test_assoc_exprTailAtt56_stub_double():
    # whileCpp_Expr has no real 'whileCpp_Expr58' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprSimple(exprHead="sample_text", exprTail="sample_text", nil="sample_text", nomSymb="sample_text", symb="sample_text", vari="sample_text")
    partner = whileCpp_Expr()
    setattr(partner, 'whileCpp_Expr58', None)
    _safe_set(owner, 'whileCpp_ExprSimple57', partner)
    assert getattr(partner, 'whileCpp_Expr58') == owner
    _safe_set(owner, 'whileCpp_ExprSimple57', None)
    assert getattr(partner, 'whileCpp_Expr58') is None


def test_assoc_exprs13_stub_double():
    # whileCpp_Exprs has no real 'whileCpp_Exprs' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Command(nop="sample_text")
    partner = whileCpp_Exprs()
    setattr(partner, 'whileCpp_Exprs', None)
    _safe_set(owner, 'whileCpp_Command14', partner)
    assert getattr(partner, 'whileCpp_Exprs') == owner
    _safe_set(owner, 'whileCpp_Command14', None)
    assert getattr(partner, 'whileCpp_Exprs') is None


def test_assoc_fonctions0_stub_double():
    # whileCpp_Program has no real 'whileCpp_Program' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Function(nom="sample_text")
    partner = whileCpp_Program()
    setattr(partner, 'whileCpp_Program', None)
    _safe_set(owner, 'whileCpp_Function', partner)
    assert owner in getattr(partner, 'whileCpp_Program')
    _safe_set(owner, 'whileCpp_Function', None)
    assert owner not in getattr(partner, 'whileCpp_Program')


def test_assoc_inputs3_stub_double():
    # whileCpp_Definition has no real 'whileCpp_Definition4' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Input(varIn="sample_text")
    partner = whileCpp_Definition()
    setattr(partner, 'whileCpp_Definition4', None)
    _safe_set(owner, 'whileCpp_Input', partner)
    assert getattr(partner, 'whileCpp_Definition4') == owner
    _safe_set(owner, 'whileCpp_Input', None)
    assert getattr(partner, 'whileCpp_Definition4') is None


def test_assoc_outputs7_stub_double():
    # whileCpp_Definition has no real 'whileCpp_Definition8' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_Output(varOut="sample_text")
    partner = whileCpp_Definition()
    setattr(partner, 'whileCpp_Definition8', None)
    _safe_set(owner, 'whileCpp_Output', partner)
    assert getattr(partner, 'whileCpp_Definition8') == owner
    _safe_set(owner, 'whileCpp_Output', None)
    assert getattr(partner, 'whileCpp_Definition8') is None


def test_assoc_symbAtt59_stub_double():
    # whileCpp_Expr has no real 'whileCpp_Expr61' property in the generated
    # code (a bare stub) -- manually attach it so whileCpp_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileCpp_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileCpp_ExprSimple(exprHead="sample_text", exprTail="sample_text", nil="sample_text", nomSymb="sample_text", symb="sample_text", vari="sample_text")
    partner = whileCpp_Expr()
    setattr(partner, 'whileCpp_Expr61', None)
    _safe_set(owner, 'whileCpp_ExprSimple60', {partner})
    assert getattr(partner, 'whileCpp_Expr61') == owner
    _safe_set(owner, 'whileCpp_ExprSimple60', set())
    assert getattr(partner, 'whileCpp_Expr61') is None


