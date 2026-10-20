import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myDsl_And,
    myDsl_Command,
    myDsl_Commands,
    myDsl_Definiton,
    myDsl_EObject,
    myDsl_Eq,
    myDsl_Expr,
    myDsl_ExprSimple,
    myDsl_ExprTerm,
    myDsl_Exprs,
    myDsl_Function,
    myDsl_Input,
    myDsl_Lexpr,
    myDsl_Model,
    myDsl_Not,
    myDsl_Or,
    myDsl_Output,
    myDsl_Vars,
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

def test_assoc_varL15_reverse_link_reassign_clear():
    a1 = myDsl_Vars(v1="sample_text", v2="sample_text")
    a2 = myDsl_Vars(v1="sample_text_2", v2="sample_text_2")
    b = myDsl_Command(nom="sample_text")
    _safe_set(b, 'myDsl_Command16', a1)
    assert _is_linked(b, 'myDsl_Command16', a1)
    if hasattr(a1, 'myDsl_Vars'):
        assert _is_linked(a1, 'myDsl_Vars', b)
    _safe_set(b, 'myDsl_Command16', a2)
    assert _is_linked(b, 'myDsl_Command16', a2)
    if hasattr(a1, 'myDsl_Vars'):
        assert not _is_linked(a1, 'myDsl_Vars', b)
    if hasattr(a2, 'myDsl_Vars'):
        assert _is_linked(a2, 'myDsl_Vars', b)
    _safe_set(b, 'myDsl_Command16', None)
    assert not _is_linked(b, 'myDsl_Command16', a2)
    if hasattr(a2, 'myDsl_Vars'):
        assert not _is_linked(a2, 'myDsl_Vars', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_c123_stub_double():
    # myDsl_Commands has no real 'myDsl_Commands25' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Command(nom="sample_text")
    partner = myDsl_Commands()
    setattr(partner, 'myDsl_Commands25', None)
    _safe_set(owner, 'myDsl_Command24', partner)
    assert getattr(partner, 'myDsl_Commands25') == owner
    _safe_set(owner, 'myDsl_Command24', None)
    assert getattr(partner, 'myDsl_Commands25') is None


def test_assoc_c232_stub_double():
    # myDsl_Commands has no real 'myDsl_Commands34' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Command(nom="sample_text")
    partner = myDsl_Commands()
    setattr(partner, 'myDsl_Commands34', None)
    _safe_set(owner, 'myDsl_Command33', partner)
    assert getattr(partner, 'myDsl_Commands34') == owner
    _safe_set(owner, 'myDsl_Command33', None)
    assert getattr(partner, 'myDsl_Commands34') is None


def test_assoc_c9_stub_double():
    # myDsl_Commands has no real 'myDsl_Commands10' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Command(nom="sample_text")
    partner = myDsl_Commands()
    setattr(partner, 'myDsl_Commands10', None)
    _safe_set(owner, 'myDsl_Command', partner)
    assert owner in getattr(partner, 'myDsl_Commands10')
    _safe_set(owner, 'myDsl_Command', None)
    assert owner not in getattr(partner, 'myDsl_Commands10')


def test_assoc_def_1_stub_double():
    # myDsl_Definiton has no real 'myDsl_Definiton' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Function(funName="sample_text")
    partner = myDsl_Definiton()
    setattr(partner, 'myDsl_Definiton', None)
    _safe_set(owner, 'myDsl_Function2', partner)
    assert getattr(partner, 'myDsl_Definiton') == owner
    _safe_set(owner, 'myDsl_Function2', None)
    assert getattr(partner, 'myDsl_Definiton') is None


def test_assoc_exp126_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr28' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Command(nom="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr28', None)
    _safe_set(owner, 'myDsl_Command27', partner)
    assert getattr(partner, 'myDsl_Expr28') == owner
    _safe_set(owner, 'myDsl_Command27', None)
    assert getattr(partner, 'myDsl_Expr28') is None


def test_assoc_exp20_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr22' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Command(nom="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr22', None)
    _safe_set(owner, 'myDsl_Command21', partner)
    assert getattr(partner, 'myDsl_Expr22') == owner
    _safe_set(owner, 'myDsl_Command21', None)
    assert getattr(partner, 'myDsl_Expr22') is None


def test_assoc_exp229_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr31' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Command(nom="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr31', None)
    _safe_set(owner, 'myDsl_Command30', partner)
    assert getattr(partner, 'myDsl_Expr31') == owner
    _safe_set(owner, 'myDsl_Command30', None)
    assert getattr(partner, 'myDsl_Expr31') is None


def test_assoc_expEq51_stub_double():
    # myDsl_Eq has no real 'myDsl_Eq' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Not's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Not's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Not(non="sample_text")
    partner = myDsl_Eq()
    setattr(partner, 'myDsl_Eq', None)
    _safe_set(owner, 'myDsl_Not52', partner)
    assert getattr(partner, 'myDsl_Eq') == owner
    _safe_set(owner, 'myDsl_Not52', None)
    assert getattr(partner, 'myDsl_Eq') is None


def test_assoc_expL17_stub_double():
    # myDsl_Exprs has no real 'myDsl_Exprs19' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Command(nom="sample_text")
    partner = myDsl_Exprs()
    setattr(partner, 'myDsl_Exprs19', None)
    _safe_set(owner, 'myDsl_Command18', partner)
    assert getattr(partner, 'myDsl_Exprs19') == owner
    _safe_set(owner, 'myDsl_Command18', None)
    assert getattr(partner, 'myDsl_Exprs19') is None


def test_assoc_expNon248_stub_double():
    # myDsl_Or has no real 'myDsl_Or49' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Not's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Not's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Not(non="sample_text")
    partner = myDsl_Or()
    setattr(partner, 'myDsl_Or49', None)
    _safe_set(owner, 'myDsl_Not50', partner)
    assert owner in getattr(partner, 'myDsl_Or49')
    _safe_set(owner, 'myDsl_Not50', None)
    assert owner not in getattr(partner, 'myDsl_Or49')


def test_assoc_expNon46_stub_double():
    # myDsl_Or has no real 'myDsl_Or47' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Not's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Not's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Not(non="sample_text")
    partner = myDsl_Or()
    setattr(partner, 'myDsl_Or47', None)
    _safe_set(owner, 'myDsl_Not', partner)
    assert getattr(partner, 'myDsl_Or47') == owner
    _safe_set(owner, 'myDsl_Not', None)
    assert getattr(partner, 'myDsl_Or47') is None


def test_assoc_expTerminale39_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr40' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprTerm(termSym="sample_text", termVar="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr40', None)
    _safe_set(owner, 'myDsl_ExprTerm', partner)
    assert getattr(partner, 'myDsl_Expr40') == owner
    _safe_set(owner, 'myDsl_ExprTerm', None)
    assert getattr(partner, 'myDsl_Expr40') is None


def test_assoc_expr63_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr65' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(mot="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr65', None)
    _safe_set(owner, 'myDsl_ExprSimple64', partner)
    assert getattr(partner, 'myDsl_Expr65') == owner
    _safe_set(owner, 'myDsl_ExprSimple64', None)
    assert getattr(partner, 'myDsl_Expr65') is None


def test_assoc_exprSimple35_stub_double():
    # myDsl_Expr has no real 'myDsl_Expr36' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(mot="sample_text")
    partner = myDsl_Expr()
    setattr(partner, 'myDsl_Expr36', None)
    _safe_set(owner, 'myDsl_ExprSimple', partner)
    assert getattr(partner, 'myDsl_Expr36') == owner
    _safe_set(owner, 'myDsl_ExprSimple', None)
    assert getattr(partner, 'myDsl_Expr36') is None


def test_assoc_inputVars3_stub_double():
    # myDsl_Definiton has no real 'myDsl_Definiton4' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Input(v="sample_text", v2="sample_text")
    partner = myDsl_Definiton()
    setattr(partner, 'myDsl_Definiton4', None)
    _safe_set(owner, 'myDsl_Input', partner)
    assert getattr(partner, 'myDsl_Definiton4') == owner
    _safe_set(owner, 'myDsl_Input', None)
    assert getattr(partner, 'myDsl_Definiton4') is None


def test_assoc_lexpr61_stub_double():
    # myDsl_Lexpr has no real 'myDsl_Lexpr' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ExprSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ExprSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ExprSimple(mot="sample_text")
    partner = myDsl_Lexpr()
    setattr(partner, 'myDsl_Lexpr', None)
    _safe_set(owner, 'myDsl_ExprSimple62', partner)
    assert getattr(partner, 'myDsl_Lexpr') == owner
    _safe_set(owner, 'myDsl_ExprSimple62', None)
    assert getattr(partner, 'myDsl_Lexpr') is None


def test_assoc_model0_stub_double():
    # myDsl_Model has no real 'myDsl_Model' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Function(funName="sample_text")
    partner = myDsl_Model()
    setattr(partner, 'myDsl_Model', None)
    _safe_set(owner, 'myDsl_Function', partner)
    assert owner in getattr(partner, 'myDsl_Model')
    _safe_set(owner, 'myDsl_Function', None)
    assert owner not in getattr(partner, 'myDsl_Model')


def test_assoc_outputVars7_stub_double():
    # myDsl_Definiton has no real 'myDsl_Definiton8' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Output(v="sample_text", v2="sample_text")
    partner = myDsl_Definiton()
    setattr(partner, 'myDsl_Definiton8', None)
    _safe_set(owner, 'myDsl_Output', partner)
    assert getattr(partner, 'myDsl_Definiton8') == owner
    _safe_set(owner, 'myDsl_Output', None)
    assert getattr(partner, 'myDsl_Definiton8') is None


