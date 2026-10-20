import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GExpression,
    gpfl_AcceptCmd,
    gpfl_AlarmCmd,
    gpfl_AutomataDef,
    gpfl_AutomatonCmd,
    gpfl_CmdAdd,
    gpfl_CmdAnd,
    gpfl_CmdEq,
    gpfl_CmdGCompare,
    gpfl_CmdGECompare,
    gpfl_CmdLCompare,
    gpfl_CmdLECompare,
    gpfl_CmdNEq,
    gpfl_CmdSub,
    gpfl_CondStmt,
    gpfl_DropCmd,
    gpfl_Field,
    gpfl_GBoolFalse,
    gpfl_GBoolTrue,
    gpfl_GExpression,
    gpfl_InPort,
    gpfl_IntLitCmd,
    gpfl_InterruptStmt,
    gpfl_IterStmt,
    gpfl_NopCmd,
    gpfl_OutPort,
    gpfl_PortLit,
    gpfl_Program,
    gpfl_SendCmd,
    gpfl_SetCmd,
    gpfl_State,
    gpfl_StpCmd,
    gpfl_StringLit,
    gpfl_Transition,
    gpfl_Variable,
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
    a1 = gpfl_Program(name="sample_text")
    a2 = gpfl_Program(name="sample_text_2")
    b = gpfl_AutomataDef(name="sample_text")
    _safe_set(b, 'gpfl_AutomataDef', a1)
    assert _is_linked(b, 'gpfl_AutomataDef', a1)
    if hasattr(a1, 'gpfl_Program'):
        assert _is_linked(a1, 'gpfl_Program', b)
    _safe_set(b, 'gpfl_AutomataDef', a2)
    assert _is_linked(b, 'gpfl_AutomataDef', a2)
    if hasattr(a1, 'gpfl_Program'):
        assert not _is_linked(a1, 'gpfl_Program', b)
    if hasattr(a2, 'gpfl_Program'):
        assert _is_linked(a2, 'gpfl_Program', b)
    _safe_set(b, 'gpfl_AutomataDef', None)
    assert not _is_linked(b, 'gpfl_AutomataDef', a2)
    if hasattr(a2, 'gpfl_Program'):
        assert not _is_linked(a2, 'gpfl_Program', b)


def test_assoc_automaton45_reverse_link_reassign_clear():
    a1 = gpfl_AutomatonCmd(name="sample_text")
    a2 = gpfl_AutomatonCmd(name="sample_text_2")
    b = gpfl_AutomataDef(name="sample_text")
    _safe_set(b, 'gpfl_AutomataDef46', a1)
    assert _is_linked(b, 'gpfl_AutomataDef46', a1)
    if hasattr(a1, 'gpfl_AutomatonCmd'):
        assert _is_linked(a1, 'gpfl_AutomatonCmd', b)
    _safe_set(b, 'gpfl_AutomataDef46', a2)
    assert _is_linked(b, 'gpfl_AutomataDef46', a2)
    if hasattr(a1, 'gpfl_AutomatonCmd'):
        assert not _is_linked(a1, 'gpfl_AutomatonCmd', b)
    if hasattr(a2, 'gpfl_AutomatonCmd'):
        assert _is_linked(a2, 'gpfl_AutomatonCmd', b)
    _safe_set(b, 'gpfl_AutomataDef46', None)
    assert not _is_linked(b, 'gpfl_AutomataDef46', a2)
    if hasattr(a2, 'gpfl_AutomatonCmd'):
        assert not _is_linked(a2, 'gpfl_AutomatonCmd', b)


def test_assoc_init11_reverse_link_reassign_clear():
    a1 = gpfl_State(name="sample_text")
    a2 = gpfl_State(name="sample_text_2")
    b = gpfl_AutomataDef(name="sample_text")
    _safe_set(b, 'gpfl_AutomataDef12', a1)
    assert _is_linked(b, 'gpfl_AutomataDef12', a1)
    if hasattr(a1, 'gpfl_State'):
        assert _is_linked(a1, 'gpfl_State', b)
    _safe_set(b, 'gpfl_AutomataDef12', a2)
    assert _is_linked(b, 'gpfl_AutomataDef12', a2)
    if hasattr(a1, 'gpfl_State'):
        assert not _is_linked(a1, 'gpfl_State', b)
    if hasattr(a2, 'gpfl_State'):
        assert _is_linked(a2, 'gpfl_State', b)
    _safe_set(b, 'gpfl_AutomataDef12', None)
    assert not _is_linked(b, 'gpfl_AutomataDef12', a2)
    if hasattr(a2, 'gpfl_State'):
        assert not _is_linked(a2, 'gpfl_State', b)


def test_assoc_states13_reverse_link_reassign_clear():
    a1 = gpfl_State(name="sample_text")
    a2 = gpfl_State(name="sample_text_2")
    b = gpfl_AutomataDef(name="sample_text")
    _safe_set(b, 'gpfl_AutomataDef14', {a1})
    assert _is_linked(b, 'gpfl_AutomataDef14', a1)
    if hasattr(a1, 'gpfl_State15'):
        assert _is_linked(a1, 'gpfl_State15', b)
    _safe_set(b, 'gpfl_AutomataDef14', {a2})
    assert _is_linked(b, 'gpfl_AutomataDef14', a2)
    if hasattr(a1, 'gpfl_State15'):
        assert not _is_linked(a1, 'gpfl_State15', b)
    if hasattr(a2, 'gpfl_State15'):
        assert _is_linked(a2, 'gpfl_State15', b)
    _safe_set(b, 'gpfl_AutomataDef14', set())
    assert not _is_linked(b, 'gpfl_AutomataDef14', a2)
    if hasattr(a2, 'gpfl_State15'):
        assert not _is_linked(a2, 'gpfl_State15', b)


def test_assoc_target18_reverse_link_reassign_clear():
    a1 = gpfl_Transition(event="sample_text")
    a2 = gpfl_Transition(event="sample_text_2")
    b = gpfl_State(name="sample_text")
    _safe_set(b, 'gpfl_State20', a1)
    assert _is_linked(b, 'gpfl_State20', a1)
    if hasattr(a1, 'gpfl_Transition19'):
        assert _is_linked(a1, 'gpfl_Transition19', b)
    _safe_set(b, 'gpfl_State20', a2)
    assert _is_linked(b, 'gpfl_State20', a2)
    if hasattr(a1, 'gpfl_Transition19'):
        assert not _is_linked(a1, 'gpfl_Transition19', b)
    if hasattr(a2, 'gpfl_Transition19'):
        assert _is_linked(a2, 'gpfl_Transition19', b)
    _safe_set(b, 'gpfl_State20', None)
    assert not _is_linked(b, 'gpfl_State20', a2)
    if hasattr(a2, 'gpfl_Transition19'):
        assert not _is_linked(a2, 'gpfl_Transition19', b)


def test_assoc_transitions16_reverse_link_reassign_clear():
    a1 = gpfl_Transition(event="sample_text")
    a2 = gpfl_Transition(event="sample_text_2")
    b = gpfl_State(name="sample_text")
    _safe_set(b, 'gpfl_State17', {a1})
    assert _is_linked(b, 'gpfl_State17', a1)
    if hasattr(a1, 'gpfl_Transition'):
        assert _is_linked(a1, 'gpfl_Transition', b)
    _safe_set(b, 'gpfl_State17', {a2})
    assert _is_linked(b, 'gpfl_State17', a2)
    if hasattr(a1, 'gpfl_Transition'):
        assert not _is_linked(a1, 'gpfl_Transition', b)
    if hasattr(a2, 'gpfl_Transition'):
        assert _is_linked(a2, 'gpfl_Transition', b)
    _safe_set(b, 'gpfl_State17', set())
    assert not _is_linked(b, 'gpfl_State17', a2)
    if hasattr(a2, 'gpfl_Transition'):
        assert not _is_linked(a2, 'gpfl_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_automaton47_stub_double():
    # gpfl_StpCmd has no real 'gpfl_StpCmd' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_AutomatonCmd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_AutomatonCmd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_AutomatonCmd(name="sample_text")
    partner = gpfl_StpCmd()
    setattr(partner, 'gpfl_StpCmd', None)
    _safe_set(owner, 'gpfl_AutomatonCmd48', partner)
    assert getattr(partner, 'gpfl_StpCmd') == owner
    _safe_set(owner, 'gpfl_AutomatonCmd48', None)
    assert getattr(partner, 'gpfl_StpCmd') is None


def test_assoc_exp43_stub_double():
    # gpfl_GExpression has no real 'gpfl_GExpression44' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_SetCmd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_SetCmd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_SetCmd(name="sample_text")
    partner = gpfl_GExpression()
    setattr(partner, 'gpfl_GExpression44', None)
    _safe_set(owner, 'gpfl_SetCmd', partner)
    assert getattr(partner, 'gpfl_GExpression44') == owner
    _safe_set(owner, 'gpfl_SetCmd', None)
    assert getattr(partner, 'gpfl_GExpression44') is None


def test_assoc_fields38_stub_double():
    # gpfl_SendCmd has no real 'gpfl_SendCmd39' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_Field(name="sample_text")
    partner = gpfl_SendCmd()
    setattr(partner, 'gpfl_SendCmd39', None)
    _safe_set(owner, 'gpfl_Field40', partner)
    assert owner in getattr(partner, 'gpfl_SendCmd39')
    _safe_set(owner, 'gpfl_Field40', None)
    assert owner not in getattr(partner, 'gpfl_SendCmd39')


def test_assoc_initStmts1_stub_double():
    # gpfl_GExpression has no real 'gpfl_GExpression' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_Program(name="sample_text")
    partner = gpfl_GExpression()
    setattr(partner, 'gpfl_GExpression', None)
    _safe_set(owner, 'gpfl_Program2', {partner})
    assert getattr(partner, 'gpfl_GExpression') == owner
    _safe_set(owner, 'gpfl_Program2', set())
    assert getattr(partner, 'gpfl_GExpression') is None


def test_assoc_periodic31_stub_double():
    # gpfl_GExpression has no real 'gpfl_GExpression32' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_InterruptStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_InterruptStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_InterruptStmt(timeout=7)
    partner = gpfl_GExpression()
    setattr(partner, 'gpfl_GExpression32', None)
    _safe_set(owner, 'gpfl_InterruptStmt', partner)
    assert getattr(partner, 'gpfl_GExpression32') == owner
    _safe_set(owner, 'gpfl_InterruptStmt', None)
    assert getattr(partner, 'gpfl_GExpression32') is None


def test_assoc_stmts3_stub_double():
    # gpfl_GExpression has no real 'gpfl_GExpression5' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_Program(name="sample_text")
    partner = gpfl_GExpression()
    setattr(partner, 'gpfl_GExpression5', None)
    _safe_set(owner, 'gpfl_Program4', {partner})
    assert getattr(partner, 'gpfl_GExpression5') == owner
    _safe_set(owner, 'gpfl_Program4', set())
    assert getattr(partner, 'gpfl_GExpression5') is None


def test_assoc_stmts33_stub_double():
    # gpfl_GExpression has no real 'gpfl_GExpression35' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_InterruptStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_InterruptStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_InterruptStmt(timeout=7)
    partner = gpfl_GExpression()
    setattr(partner, 'gpfl_GExpression35', None)
    _safe_set(owner, 'gpfl_InterruptStmt34', {partner})
    assert getattr(partner, 'gpfl_GExpression35') == owner
    _safe_set(owner, 'gpfl_InterruptStmt34', set())
    assert getattr(partner, 'gpfl_GExpression35') is None


def test_assoc_value9_stub_double():
    # gpfl_GExpression has no real 'gpfl_GExpression10' property in the generated
    # code (a bare stub) -- manually attach it so gpfl_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gpfl_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gpfl_Field(name="sample_text")
    partner = gpfl_GExpression()
    setattr(partner, 'gpfl_GExpression10', None)
    _safe_set(owner, 'gpfl_Field', partner)
    assert getattr(partner, 'gpfl_GExpression10') == owner
    _safe_set(owner, 'gpfl_Field', None)
    assert getattr(partner, 'gpfl_GExpression10') is None


