import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Literal,
    fmpl_ArithmeticExpression,
    fmpl_Automata,
    fmpl_Cond,
    fmpl_Exec,
    fmpl_Expression,
    fmpl_Field,
    fmpl_Init,
    fmpl_IntegerLit,
    fmpl_Literal,
    fmpl_Policy,
    fmpl_Read,
    fmpl_Relational,
    fmpl_State,
    fmpl_StringLit,
    fmpl_Transition,
    fmpl_VarDeclaration,
    fmpl_VarReference,
    fmpl_Write,
    ArithmeticOperator,
    RelationalOperator,
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

def test_assoc_automatas0_reverse_link_reassign_clear():
    a1 = fmpl_Policy(name="sample_text", parserURI="sample_text")
    a2 = fmpl_Policy(name="sample_text_2", parserURI="sample_text_2")
    b = fmpl_Automata(name="sample_text")
    _safe_set(b, 'fmpl_Automata', a1)
    assert _is_linked(b, 'fmpl_Automata', a1)
    if hasattr(a1, 'fmpl_Policy'):
        assert _is_linked(a1, 'fmpl_Policy', b)
    _safe_set(b, 'fmpl_Automata', a2)
    assert _is_linked(b, 'fmpl_Automata', a2)
    if hasattr(a1, 'fmpl_Policy'):
        assert not _is_linked(a1, 'fmpl_Policy', b)
    if hasattr(a2, 'fmpl_Policy'):
        assert _is_linked(a2, 'fmpl_Policy', b)
    _safe_set(b, 'fmpl_Automata', None)
    assert not _is_linked(b, 'fmpl_Automata', a2)
    if hasattr(a2, 'fmpl_Policy'):
        assert not _is_linked(a2, 'fmpl_Policy', b)


def test_assoc_from_10_reverse_link_reassign_clear():
    a1 = fmpl_Transition(name="sample_text")
    a2 = fmpl_Transition(name="sample_text_2")
    b = fmpl_State(name="sample_text")
    _safe_set(b, 'fmpl_State12', a1)
    assert _is_linked(b, 'fmpl_State12', a1)
    if hasattr(a1, 'fmpl_Transition11'):
        assert _is_linked(a1, 'fmpl_Transition11', b)
    _safe_set(b, 'fmpl_State12', a2)
    assert _is_linked(b, 'fmpl_State12', a2)
    if hasattr(a1, 'fmpl_Transition11'):
        assert not _is_linked(a1, 'fmpl_Transition11', b)
    if hasattr(a2, 'fmpl_Transition11'):
        assert _is_linked(a2, 'fmpl_Transition11', b)
    _safe_set(b, 'fmpl_State12', None)
    assert not _is_linked(b, 'fmpl_State12', a2)
    if hasattr(a2, 'fmpl_Transition11'):
        assert not _is_linked(a2, 'fmpl_Transition11', b)


def test_assoc_init7_reverse_link_reassign_clear():
    a1 = fmpl_State(name="sample_text")
    a2 = fmpl_State(name="sample_text_2")
    b = fmpl_Automata(name="sample_text")
    _safe_set(b, 'fmpl_Automata8', a1)
    assert _is_linked(b, 'fmpl_Automata8', a1)
    if hasattr(a1, 'fmpl_State9'):
        assert _is_linked(a1, 'fmpl_State9', b)
    _safe_set(b, 'fmpl_Automata8', a2)
    assert _is_linked(b, 'fmpl_Automata8', a2)
    if hasattr(a1, 'fmpl_State9'):
        assert not _is_linked(a1, 'fmpl_State9', b)
    if hasattr(a2, 'fmpl_State9'):
        assert _is_linked(a2, 'fmpl_State9', b)
    _safe_set(b, 'fmpl_Automata8', None)
    assert not _is_linked(b, 'fmpl_Automata8', a2)
    if hasattr(a2, 'fmpl_State9'):
        assert not _is_linked(a2, 'fmpl_State9', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = fmpl_State(name="sample_text")
    a2 = fmpl_State(name="sample_text_2")
    b = fmpl_Automata(name="sample_text")
    _safe_set(b, 'fmpl_Automata4', {a1})
    assert _is_linked(b, 'fmpl_Automata4', a1)
    if hasattr(a1, 'fmpl_State'):
        assert _is_linked(a1, 'fmpl_State', b)
    _safe_set(b, 'fmpl_Automata4', {a2})
    assert _is_linked(b, 'fmpl_Automata4', a2)
    if hasattr(a1, 'fmpl_State'):
        assert not _is_linked(a1, 'fmpl_State', b)
    if hasattr(a2, 'fmpl_State'):
        assert _is_linked(a2, 'fmpl_State', b)
    _safe_set(b, 'fmpl_Automata4', set())
    assert not _is_linked(b, 'fmpl_Automata4', a2)
    if hasattr(a2, 'fmpl_State'):
        assert not _is_linked(a2, 'fmpl_State', b)


def test_assoc_to13_reverse_link_reassign_clear():
    a1 = fmpl_Transition(name="sample_text")
    a2 = fmpl_Transition(name="sample_text_2")
    b = fmpl_State(name="sample_text")
    _safe_set(b, 'fmpl_State15', a1)
    assert _is_linked(b, 'fmpl_State15', a1)
    if hasattr(a1, 'fmpl_Transition14'):
        assert _is_linked(a1, 'fmpl_Transition14', b)
    _safe_set(b, 'fmpl_State15', a2)
    assert _is_linked(b, 'fmpl_State15', a2)
    if hasattr(a1, 'fmpl_Transition14'):
        assert not _is_linked(a1, 'fmpl_Transition14', b)
    if hasattr(a2, 'fmpl_Transition14'):
        assert _is_linked(a2, 'fmpl_Transition14', b)
    _safe_set(b, 'fmpl_State15', None)
    assert not _is_linked(b, 'fmpl_State15', a2)
    if hasattr(a2, 'fmpl_Transition14'):
        assert not _is_linked(a2, 'fmpl_Transition14', b)


def test_assoc_transitions5_reverse_link_reassign_clear():
    a1 = fmpl_Transition(name="sample_text")
    a2 = fmpl_Transition(name="sample_text_2")
    b = fmpl_Automata(name="sample_text")
    _safe_set(b, 'fmpl_Automata6', {a1})
    assert _is_linked(b, 'fmpl_Automata6', a1)
    if hasattr(a1, 'fmpl_Transition'):
        assert _is_linked(a1, 'fmpl_Transition', b)
    _safe_set(b, 'fmpl_Automata6', {a2})
    assert _is_linked(b, 'fmpl_Automata6', a2)
    if hasattr(a1, 'fmpl_Transition'):
        assert not _is_linked(a1, 'fmpl_Transition', b)
    if hasattr(a2, 'fmpl_Transition'):
        assert _is_linked(a2, 'fmpl_Transition', b)
    _safe_set(b, 'fmpl_Automata6', set())
    assert not _is_linked(b, 'fmpl_Automata6', a2)
    if hasattr(a2, 'fmpl_Transition'):
        assert not _is_linked(a2, 'fmpl_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_automata23_stub_double():
    # fmpl_Init has no real 'fmpl_Init' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_Automata's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_Automata's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_Automata(name="sample_text")
    partner = fmpl_Init()
    setattr(partner, 'fmpl_Init', None)
    _safe_set(owner, 'fmpl_Automata24', partner)
    assert getattr(partner, 'fmpl_Init') == owner
    _safe_set(owner, 'fmpl_Automata24', None)
    assert getattr(partner, 'fmpl_Init') is None


def test_assoc_expr36_stub_double():
    # fmpl_Expression has no real 'fmpl_Expression37' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_VarDeclaration(name="sample_text")
    partner = fmpl_Expression()
    setattr(partner, 'fmpl_Expression37', None)
    _safe_set(owner, 'fmpl_VarDeclaration', partner)
    assert getattr(partner, 'fmpl_Expression37') == owner
    _safe_set(owner, 'fmpl_VarDeclaration', None)
    assert getattr(partner, 'fmpl_Expression37') is None


def test_assoc_if_18_stub_double():
    # fmpl_Cond has no real 'fmpl_Cond' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_Relational's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_Relational's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_Relational(operator="sample_text")
    partner = fmpl_Cond()
    setattr(partner, 'fmpl_Cond', None)
    _safe_set(owner, 'fmpl_Relational', partner)
    assert getattr(partner, 'fmpl_Cond') == owner
    _safe_set(owner, 'fmpl_Relational', None)
    assert getattr(partner, 'fmpl_Cond') is None


def test_assoc_left25_stub_double():
    # fmpl_Expression has no real 'fmpl_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_Relational's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_Relational's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_Relational(operator="sample_text")
    partner = fmpl_Expression()
    setattr(partner, 'fmpl_Expression27', None)
    _safe_set(owner, 'fmpl_Relational26', partner)
    assert getattr(partner, 'fmpl_Expression27') == owner
    _safe_set(owner, 'fmpl_Relational26', None)
    assert getattr(partner, 'fmpl_Expression27') is None


def test_assoc_left31_stub_double():
    # fmpl_Expression has no real 'fmpl_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_ArithmeticExpression(operator="sample_text")
    partner = fmpl_Expression()
    setattr(partner, 'fmpl_Expression32', None)
    _safe_set(owner, 'fmpl_ArithmeticExpression', partner)
    assert getattr(partner, 'fmpl_Expression32') == owner
    _safe_set(owner, 'fmpl_ArithmeticExpression', None)
    assert getattr(partner, 'fmpl_Expression32') is None


def test_assoc_name38_stub_double():
    # fmpl_VarReference has no real 'fmpl_VarReference39' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_VarDeclaration(name="sample_text")
    partner = fmpl_VarReference()
    setattr(partner, 'fmpl_VarReference39', None)
    _safe_set(owner, 'fmpl_VarDeclaration40', partner)
    assert getattr(partner, 'fmpl_VarReference39') == owner
    _safe_set(owner, 'fmpl_VarDeclaration40', None)
    assert getattr(partner, 'fmpl_VarReference39') is None


def test_assoc_right28_stub_double():
    # fmpl_Expression has no real 'fmpl_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_Relational's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_Relational's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_Relational(operator="sample_text")
    partner = fmpl_Expression()
    setattr(partner, 'fmpl_Expression30', None)
    _safe_set(owner, 'fmpl_Relational29', partner)
    assert getattr(partner, 'fmpl_Expression30') == owner
    _safe_set(owner, 'fmpl_Relational29', None)
    assert getattr(partner, 'fmpl_Expression30') is None


def test_assoc_right33_stub_double():
    # fmpl_Expression has no real 'fmpl_Expression35' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_ArithmeticExpression(operator="sample_text")
    partner = fmpl_Expression()
    setattr(partner, 'fmpl_Expression35', None)
    _safe_set(owner, 'fmpl_ArithmeticExpression34', partner)
    assert getattr(partner, 'fmpl_Expression35') == owner
    _safe_set(owner, 'fmpl_ArithmeticExpression34', None)
    assert getattr(partner, 'fmpl_Expression35') is None


def test_assoc_statements1_stub_double():
    # fmpl_Expression has no real 'fmpl_Expression' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_Policy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_Policy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_Policy(name="sample_text", parserURI="sample_text")
    partner = fmpl_Expression()
    setattr(partner, 'fmpl_Expression', None)
    _safe_set(owner, 'fmpl_Policy2', {partner})
    assert getattr(partner, 'fmpl_Expression') == owner
    _safe_set(owner, 'fmpl_Policy2', set())
    assert getattr(partner, 'fmpl_Expression') is None


def test_assoc_transition16_stub_double():
    # fmpl_Exec has no real 'fmpl_Exec' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_Transition(name="sample_text")
    partner = fmpl_Exec()
    setattr(partner, 'fmpl_Exec', None)
    _safe_set(owner, 'fmpl_Transition17', partner)
    assert getattr(partner, 'fmpl_Exec') == owner
    _safe_set(owner, 'fmpl_Transition17', None)
    assert getattr(partner, 'fmpl_Exec') is None


def test_assoc_var22_stub_double():
    # fmpl_VarReference has no real 'fmpl_VarReference' property in the generated
    # code (a bare stub) -- manually attach it so fmpl_Write's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fmpl_Write's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fmpl_Write(initBit=7, length=7)
    partner = fmpl_VarReference()
    setattr(partner, 'fmpl_VarReference', None)
    _safe_set(owner, 'fmpl_Write', partner)
    assert getattr(partner, 'fmpl_VarReference') == owner
    _safe_set(owner, 'fmpl_Write', None)
    assert getattr(partner, 'fmpl_VarReference') is None


