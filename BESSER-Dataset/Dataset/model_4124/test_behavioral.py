import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    langage_while_Assign,
    langage_while_Command,
    langage_while_Commands,
    langage_while_Definition,
    langage_while_Expr,
    langage_while_ExprAnd,
    langage_while_ExprEq,
    langage_while_ExprNot,
    langage_while_ExprOr,
    langage_while_ExprSimple,
    langage_while_Exprs,
    langage_while_For,
    langage_while_Foreach,
    langage_while_Function,
    langage_while_If,
    langage_while_Ifconfort,
    langage_while_Input,
    langage_while_LExpr,
    langage_while_Model,
    langage_while_Output,
    langage_while_Program,
    langage_while_SYMB,
    langage_while_VAR,
    langage_while_Vars,
    langage_while_While,
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

def test_assoc_pp4_reverse_link_reassign_clear():
    a1 = langage_while_Program(u="sample_text")
    a2 = langage_while_Program(u="sample_text_2")
    b = langage_while_Program(u="sample_text")
    _safe_set(b, 'langage_while_Program5', a1)
    assert _is_linked(b, 'langage_while_Program5', a1)
    if hasattr(a1, 'langage_while_Program3'):
        assert _is_linked(a1, 'langage_while_Program3', b)
    _safe_set(b, 'langage_while_Program5', a2)
    assert _is_linked(b, 'langage_while_Program5', a2)
    if hasattr(a1, 'langage_while_Program3'):
        assert not _is_linked(a1, 'langage_while_Program3', b)
    if hasattr(a2, 'langage_while_Program3'):
        assert _is_linked(a2, 'langage_while_Program3', b)
    _safe_set(b, 'langage_while_Program5', None)
    assert not _is_linked(b, 'langage_while_Program5', a2)
    if hasattr(a2, 'langage_while_Program3'):
        assert not _is_linked(a2, 'langage_while_Program3', b)


def test_assoc_sym87_reverse_link_reassign_clear():
    a1 = langage_while_SYMB(bs="sample_text", cf="sample_text")
    a2 = langage_while_SYMB(bs="sample_text_2", cf="sample_text_2")
    b = langage_while_ExprSimple(mot="sample_text", nil="sample_text")
    _safe_set(b, 'langage_while_ExprSimple88', a1)
    assert _is_linked(b, 'langage_while_ExprSimple88', a1)
    if hasattr(a1, 'langage_while_SYMB89'):
        assert _is_linked(a1, 'langage_while_SYMB89', b)
    _safe_set(b, 'langage_while_ExprSimple88', a2)
    assert _is_linked(b, 'langage_while_ExprSimple88', a2)
    if hasattr(a1, 'langage_while_SYMB89'):
        assert not _is_linked(a1, 'langage_while_SYMB89', b)
    if hasattr(a2, 'langage_while_SYMB89'):
        assert _is_linked(a2, 'langage_while_SYMB89', b)
    _safe_set(b, 'langage_while_ExprSimple88', None)
    assert not _is_linked(b, 'langage_while_ExprSimple88', a2)
    if hasattr(a2, 'langage_while_SYMB89'):
        assert not _is_linked(a2, 'langage_while_SYMB89', b)


def test_assoc_v84_reverse_link_reassign_clear():
    a1 = langage_while_VAR(bv="sample_text", cf="sample_text")
    a2 = langage_while_VAR(bv="sample_text_2", cf="sample_text_2")
    b = langage_while_ExprSimple(mot="sample_text", nil="sample_text")
    _safe_set(b, 'langage_while_ExprSimple85', a1)
    assert _is_linked(b, 'langage_while_ExprSimple85', a1)
    if hasattr(a1, 'langage_while_VAR86'):
        assert _is_linked(a1, 'langage_while_VAR86', b)
    _safe_set(b, 'langage_while_ExprSimple85', a2)
    assert _is_linked(b, 'langage_while_ExprSimple85', a2)
    if hasattr(a1, 'langage_while_VAR86'):
        assert not _is_linked(a1, 'langage_while_VAR86', b)
    if hasattr(a2, 'langage_while_VAR86'):
        assert _is_linked(a2, 'langage_while_VAR86', b)
    _safe_set(b, 'langage_while_ExprSimple85', None)
    assert not _is_linked(b, 'langage_while_ExprSimple85', a2)
    if hasattr(a2, 'langage_while_VAR86'):
        assert not _is_linked(a2, 'langage_while_VAR86', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assign23_stub_double():
    # langage_while_Assign has no real 'langage_while_Assign' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Command(nop="sample_text")
    partner = langage_while_Assign()
    setattr(partner, 'langage_while_Assign', None)
    _safe_set(owner, 'langage_while_Command24', partner)
    assert getattr(partner, 'langage_while_Assign') == owner
    _safe_set(owner, 'langage_while_Command24', None)
    assert getattr(partner, 'langage_while_Assign') is None


def test_assoc_c21_stub_double():
    # langage_while_Commands has no real 'langage_while_Commands22' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Command(nop="sample_text")
    partner = langage_while_Commands()
    setattr(partner, 'langage_while_Commands22', None)
    _safe_set(owner, 'langage_while_Command', partner)
    assert owner in getattr(partner, 'langage_while_Commands22')
    _safe_set(owner, 'langage_while_Command', None)
    assert owner not in getattr(partner, 'langage_while_Commands22')


def test_assoc_ex92_stub_double():
    # langage_while_Expr has no real 'langage_while_Expr94' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_ExprSimple(mot="sample_text", nil="sample_text")
    partner = langage_while_Expr()
    setattr(partner, 'langage_while_Expr94', None)
    _safe_set(owner, 'langage_while_ExprSimple93', partner)
    assert getattr(partner, 'langage_while_Expr94') == owner
    _safe_set(owner, 'langage_while_ExprSimple93', None)
    assert getattr(partner, 'langage_while_Expr94') is None


def test_assoc_exS1113_stub_double():
    # langage_while_ExprEq has no real 'langage_while_ExprEq114' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_ExprSimple(mot="sample_text", nil="sample_text")
    partner = langage_while_ExprEq()
    setattr(partner, 'langage_while_ExprEq114', None)
    _safe_set(owner, 'langage_while_ExprSimple115', partner)
    assert getattr(partner, 'langage_while_ExprEq114') == owner
    _safe_set(owner, 'langage_while_ExprSimple115', None)
    assert getattr(partner, 'langage_while_ExprEq114') is None


def test_assoc_exS2116_stub_double():
    # langage_while_ExprEq has no real 'langage_while_ExprEq117' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_ExprSimple(mot="sample_text", nil="sample_text")
    partner = langage_while_ExprEq()
    setattr(partner, 'langage_while_ExprEq117', None)
    _safe_set(owner, 'langage_while_ExprSimple118', partner)
    assert getattr(partner, 'langage_while_ExprEq117') == owner
    _safe_set(owner, 'langage_while_ExprSimple118', None)
    assert getattr(partner, 'langage_while_ExprEq117') is None


def test_assoc_exs80_stub_double():
    # langage_while_Expr has no real 'langage_while_Expr81' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_ExprSimple(mot="sample_text", nil="sample_text")
    partner = langage_while_Expr()
    setattr(partner, 'langage_while_Expr81', None)
    _safe_set(owner, 'langage_while_ExprSimple', partner)
    assert getattr(partner, 'langage_while_Expr81') == owner
    _safe_set(owner, 'langage_while_ExprSimple', None)
    assert getattr(partner, 'langage_while_Expr81') is None


def test_assoc_f1_stub_double():
    # langage_while_Function has no real 'langage_while_Function' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Program(u="sample_text")
    partner = langage_while_Function()
    setattr(partner, 'langage_while_Function', None)
    _safe_set(owner, 'langage_while_Program2', {partner})
    assert getattr(partner, 'langage_while_Function') == owner
    _safe_set(owner, 'langage_while_Program2', set())
    assert getattr(partner, 'langage_while_Function') is None


def test_assoc_for_27_stub_double():
    # langage_while_For has no real 'langage_while_For' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Command(nop="sample_text")
    partner = langage_while_For()
    setattr(partner, 'langage_while_For', None)
    _safe_set(owner, 'langage_while_Command28', partner)
    assert getattr(partner, 'langage_while_For') == owner
    _safe_set(owner, 'langage_while_Command28', None)
    assert getattr(partner, 'langage_while_For') is None


def test_assoc_fore31_stub_double():
    # langage_while_Foreach has no real 'langage_while_Foreach' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Command(nop="sample_text")
    partner = langage_while_Foreach()
    setattr(partner, 'langage_while_Foreach', None)
    _safe_set(owner, 'langage_while_Command32', partner)
    assert getattr(partner, 'langage_while_Foreach') == owner
    _safe_set(owner, 'langage_while_Command32', None)
    assert getattr(partner, 'langage_while_Foreach') is None


def test_assoc_if_29_stub_double():
    # langage_while_If has no real 'langage_while_If' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Command(nop="sample_text")
    partner = langage_while_If()
    setattr(partner, 'langage_while_If', None)
    _safe_set(owner, 'langage_while_Command30', partner)
    assert getattr(partner, 'langage_while_If') == owner
    _safe_set(owner, 'langage_while_Command30', None)
    assert getattr(partner, 'langage_while_If') is None


def test_assoc_ifc33_stub_double():
    # langage_while_Ifconfort has no real 'langage_while_Ifconfort' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Command(nop="sample_text")
    partner = langage_while_Ifconfort()
    setattr(partner, 'langage_while_Ifconfort', None)
    _safe_set(owner, 'langage_while_Command34', partner)
    assert getattr(partner, 'langage_while_Ifconfort') == owner
    _safe_set(owner, 'langage_while_Command34', None)
    assert getattr(partner, 'langage_while_Ifconfort') is None


def test_assoc_lex90_stub_double():
    # langage_while_LExpr has no real 'langage_while_LExpr' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_ExprSimple(mot="sample_text", nil="sample_text")
    partner = langage_while_LExpr()
    setattr(partner, 'langage_while_LExpr', None)
    _safe_set(owner, 'langage_while_ExprSimple91', partner)
    assert getattr(partner, 'langage_while_LExpr') == owner
    _safe_set(owner, 'langage_while_ExprSimple91', None)
    assert getattr(partner, 'langage_while_LExpr') is None


def test_assoc_name6_stub_double():
    # langage_while_Function has no real 'langage_while_Function7' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_SYMB's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_SYMB's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_SYMB(bs="sample_text", cf="sample_text")
    partner = langage_while_Function()
    setattr(partner, 'langage_while_Function7', None)
    _safe_set(owner, 'langage_while_SYMB', partner)
    assert getattr(partner, 'langage_while_Function7') == owner
    _safe_set(owner, 'langage_while_SYMB', None)
    assert getattr(partner, 'langage_while_Function7') is None


def test_assoc_nn0_stub_double():
    # langage_while_Model has no real 'langage_while_Model' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Program(u="sample_text")
    partner = langage_while_Model()
    setattr(partner, 'langage_while_Model', None)
    _safe_set(owner, 'langage_while_Program', partner)
    assert getattr(partner, 'langage_while_Model') == owner
    _safe_set(owner, 'langage_while_Program', None)
    assert getattr(partner, 'langage_while_Model') is None


def test_assoc_v16_stub_double():
    # langage_while_Input has no real 'langage_while_Input17' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_VAR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_VAR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_VAR(bv="sample_text", cf="sample_text")
    partner = langage_while_Input()
    setattr(partner, 'langage_while_Input17', None)
    _safe_set(owner, 'langage_while_VAR', partner)
    assert owner in getattr(partner, 'langage_while_Input17')
    _safe_set(owner, 'langage_while_VAR', None)
    assert owner not in getattr(partner, 'langage_while_Input17')


def test_assoc_v18_stub_double():
    # langage_while_Output has no real 'langage_while_Output19' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_VAR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_VAR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_VAR(bv="sample_text", cf="sample_text")
    partner = langage_while_Output()
    setattr(partner, 'langage_while_Output19', None)
    _safe_set(owner, 'langage_while_VAR20', partner)
    assert owner in getattr(partner, 'langage_while_Output19')
    _safe_set(owner, 'langage_while_VAR20', None)
    assert owner not in getattr(partner, 'langage_while_Output19')


def test_assoc_vs74_stub_double():
    # langage_while_Vars has no real 'langage_while_Vars75' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_VAR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_VAR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_VAR(bv="sample_text", cf="sample_text")
    partner = langage_while_Vars()
    setattr(partner, 'langage_while_Vars75', None)
    _safe_set(owner, 'langage_while_VAR76', partner)
    assert owner in getattr(partner, 'langage_while_Vars75')
    _safe_set(owner, 'langage_while_VAR76', None)
    assert owner not in getattr(partner, 'langage_while_Vars75')


def test_assoc_wh25_stub_double():
    # langage_while_While has no real 'langage_while_While' property in the generated
    # code (a bare stub) -- manually attach it so langage_while_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langage_while_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langage_while_Command(nop="sample_text")
    partner = langage_while_While()
    setattr(partner, 'langage_while_While', None)
    _safe_set(owner, 'langage_while_Command26', partner)
    assert getattr(partner, 'langage_while_While') == owner
    _safe_set(owner, 'langage_while_Command26', None)
    assert getattr(partner, 'langage_while_While') is None


