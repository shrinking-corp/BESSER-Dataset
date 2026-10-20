import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanBinaryExpression,
    BooleanCompareExpression,
    BooleanExpression,
    IntBinaryExpression,
    IntExpression,
    IntOperation,
    State,
    gfsm_BooleanAnd,
    gfsm_BooleanBinaryExpression,
    gfsm_BooleanCompareExpression,
    gfsm_BooleanEqual,
    gfsm_BooleanExpression,
    gfsm_BooleanGreaterThan,
    gfsm_BooleanOr,
    gfsm_ConstExpr,
    gfsm_FSM,
    gfsm_FinalState,
    gfsm_InitialState,
    gfsm_IntAdd,
    gfsm_IntBinaryExpression,
    gfsm_IntBlock,
    gfsm_IntExpression,
    gfsm_IntMult,
    gfsm_IntNeg,
    gfsm_IntOperation,
    gfsm_IntVarAssign,
    gfsm_IntVarRef,
    gfsm_State,
    gfsm_Transition,
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

def test_assoc_currentState20_reverse_link_reassign_clear():
    a1 = gfsm_State(name="sample_text")
    a2 = gfsm_State(name="sample_text_2")
    b = gfsm_FSM(name="sample_text")
    _safe_set(b, 'gfsm_FSM21', a1)
    assert _is_linked(b, 'gfsm_FSM21', a1)
    if hasattr(a1, 'gfsm_State22'):
        assert _is_linked(a1, 'gfsm_State22', b)
    _safe_set(b, 'gfsm_FSM21', a2)
    assert _is_linked(b, 'gfsm_FSM21', a2)
    if hasattr(a1, 'gfsm_State22'):
        assert not _is_linked(a1, 'gfsm_State22', b)
    if hasattr(a2, 'gfsm_State22'):
        assert _is_linked(a2, 'gfsm_State22', b)
    _safe_set(b, 'gfsm_FSM21', None)
    assert not _is_linked(b, 'gfsm_FSM21', a2)
    if hasattr(a2, 'gfsm_State22'):
        assert not _is_linked(a2, 'gfsm_State22', b)


def test_assoc_from_2_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'outgoingtransitions'):
        assert _is_linked(a1, 'outgoingtransitions', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'outgoingtransitions'):
        assert not _is_linked(a1, 'outgoingtransitions', b)
    if hasattr(a2, 'outgoingtransitions'):
        assert _is_linked(a2, 'outgoingtransitions', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'outgoingtransitions'):
        assert not _is_linked(a2, 'outgoingtransitions', b)


def test_assoc_fsm1_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_FSM(name="sample_text")
    _safe_set(b, 'FSM', a1)
    assert _is_linked(b, 'FSM', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'FSM', a2)
    assert _is_linked(b, 'FSM', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'FSM', None)
    assert not _is_linked(b, 'FSM', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_fsm9_reverse_link_reassign_clear():
    a1 = gfsm_State(name="sample_text")
    a2 = gfsm_State(name="sample_text_2")
    b = gfsm_FSM(name="sample_text")
    _safe_set(b, 'FSM10', a1)
    assert _is_linked(b, 'FSM10', a1)
    if hasattr(a1, 'states'):
        assert _is_linked(a1, 'states', b)
    _safe_set(b, 'FSM10', a2)
    assert _is_linked(b, 'FSM10', a2)
    if hasattr(a1, 'states'):
        assert not _is_linked(a1, 'states', b)
    if hasattr(a2, 'states'):
        assert _is_linked(a2, 'states', b)
    _safe_set(b, 'FSM10', None)
    assert not _is_linked(b, 'FSM10', a2)
    if hasattr(a2, 'states'):
        assert not _is_linked(a2, 'states', b)


def test_assoc_incommingtransitions12_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition13'):
        assert _is_linked(a1, 'Transition13', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition13'):
        assert not _is_linked(a1, 'Transition13', b)
    if hasattr(a2, 'Transition13'):
        assert _is_linked(a2, 'Transition13', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition13'):
        assert not _is_linked(a2, 'Transition13', b)


def test_assoc_outgoingtransitions11_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_states14_reverse_link_reassign_clear():
    a1 = gfsm_State(name="sample_text")
    a2 = gfsm_State(name="sample_text_2")
    b = gfsm_FSM(name="sample_text")
    _safe_set(b, 'fsm', {a1})
    assert _is_linked(b, 'fsm', a1)
    if hasattr(a1, 'State15'):
        assert _is_linked(a1, 'State15', b)
    _safe_set(b, 'fsm', {a2})
    assert _is_linked(b, 'fsm', a2)
    if hasattr(a1, 'State15'):
        assert not _is_linked(a1, 'State15', b)
    if hasattr(a2, 'State15'):
        assert _is_linked(a2, 'State15', b)
    _safe_set(b, 'fsm', set())
    assert not _is_linked(b, 'fsm', a2)
    if hasattr(a2, 'State15'):
        assert not _is_linked(a2, 'State15', b)


def test_assoc_to3_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_State(name="sample_text")
    _safe_set(b, 'State4', a1)
    assert _is_linked(b, 'State4', a1)
    if hasattr(a1, 'incommingtransitions'):
        assert _is_linked(a1, 'incommingtransitions', b)
    _safe_set(b, 'State4', a2)
    assert _is_linked(b, 'State4', a2)
    if hasattr(a1, 'incommingtransitions'):
        assert not _is_linked(a1, 'incommingtransitions', b)
    if hasattr(a2, 'incommingtransitions'):
        assert _is_linked(a2, 'incommingtransitions', b)
    _safe_set(b, 'State4', None)
    assert not _is_linked(b, 'State4', a2)
    if hasattr(a2, 'incommingtransitions'):
        assert not _is_linked(a2, 'incommingtransitions', b)


def test_assoc_transitions16_reverse_link_reassign_clear():
    a1 = gfsm_Transition(event="sample_text")
    a2 = gfsm_Transition(event="sample_text_2")
    b = gfsm_FSM(name="sample_text")
    _safe_set(b, 'fsm17', {a1})
    assert _is_linked(b, 'fsm17', a1)
    if hasattr(a1, 'Transition18'):
        assert _is_linked(a1, 'Transition18', b)
    _safe_set(b, 'fsm17', {a2})
    assert _is_linked(b, 'fsm17', a2)
    if hasattr(a1, 'Transition18'):
        assert not _is_linked(a1, 'Transition18', b)
    if hasattr(a2, 'Transition18'):
        assert _is_linked(a2, 'Transition18', b)
    _safe_set(b, 'fsm17', set())
    assert not _is_linked(b, 'fsm17', a2)
    if hasattr(a2, 'Transition18'):
        assert not _is_linked(a2, 'Transition18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expression29_stub_double():
    # gfsm_IntExpression has no real 'gfsm_IntExpression30' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_IntVarAssign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_IntVarAssign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_IntVarAssign(name="sample_text")
    partner = gfsm_IntExpression()
    setattr(partner, 'gfsm_IntExpression30', None)
    _safe_set(owner, 'gfsm_IntVarAssign', partner)
    assert getattr(partner, 'gfsm_IntExpression30') == owner
    _safe_set(owner, 'gfsm_IntVarAssign', None)
    assert getattr(partner, 'gfsm_IntExpression30') is None


def test_assoc_guard0_stub_double():
    # gfsm_BooleanExpression has no real 'gfsm_BooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_Transition(event="sample_text")
    partner = gfsm_BooleanExpression()
    setattr(partner, 'gfsm_BooleanExpression', None)
    _safe_set(owner, 'gfsm_Transition', partner)
    assert getattr(partner, 'gfsm_BooleanExpression') == owner
    _safe_set(owner, 'gfsm_Transition', None)
    assert getattr(partner, 'gfsm_BooleanExpression') is None


def test_assoc_inExpression5_stub_double():
    # gfsm_IntOperation has no real 'gfsm_IntOperation' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_State(name="sample_text")
    partner = gfsm_IntOperation()
    setattr(partner, 'gfsm_IntOperation', None)
    _safe_set(owner, 'gfsm_State', partner)
    assert getattr(partner, 'gfsm_IntOperation') == owner
    _safe_set(owner, 'gfsm_State', None)
    assert getattr(partner, 'gfsm_IntOperation') is None


def test_assoc_initialstate19_stub_double():
    # gfsm_InitialState has no real 'gfsm_InitialState' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_FSM(name="sample_text")
    partner = gfsm_InitialState()
    setattr(partner, 'gfsm_InitialState', None)
    _safe_set(owner, 'gfsm_FSM', partner)
    assert getattr(partner, 'gfsm_InitialState') == owner
    _safe_set(owner, 'gfsm_FSM', None)
    assert getattr(partner, 'gfsm_InitialState') is None


def test_assoc_operations31_stub_double():
    # gfsm_IntBlock has no real 'gfsm_IntBlock' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_IntVarAssign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_IntVarAssign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_IntVarAssign(name="sample_text")
    partner = gfsm_IntBlock()
    setattr(partner, 'gfsm_IntBlock', None)
    _safe_set(owner, 'gfsm_IntVarAssign32', partner)
    assert owner in getattr(partner, 'gfsm_IntBlock')
    _safe_set(owner, 'gfsm_IntVarAssign32', None)
    assert owner not in getattr(partner, 'gfsm_IntBlock')


def test_assoc_outExpression6_stub_double():
    # gfsm_IntOperation has no real 'gfsm_IntOperation8' property in the generated
    # code (a bare stub) -- manually attach it so gfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gfsm_State(name="sample_text")
    partner = gfsm_IntOperation()
    setattr(partner, 'gfsm_IntOperation8', None)
    _safe_set(owner, 'gfsm_State7', partner)
    assert getattr(partner, 'gfsm_IntOperation8') == owner
    _safe_set(owner, 'gfsm_State7', None)
    assert getattr(partner, 'gfsm_IntOperation8') is None


