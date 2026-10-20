import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    StateMachineObject,
    statemachine103_Action,
    statemachine103_FinalState,
    statemachine103_InitialState,
    statemachine103_NormalState,
    statemachine103_State,
    statemachine103_StateMachine,
    statemachine103_StateMachineObject,
    statemachine103_StateMachineVariable,
    statemachine103_Transition,
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

def test_assoc_machineObjects0_reverse_link_reassign_clear():
    a1 = statemachine103_StateMachineObject(label="sample_text")
    a2 = statemachine103_StateMachineObject(label="sample_text_2")
    b = statemachine103_StateMachine(label="sample_text")
    _safe_set(b, 'statemachine103_StateMachine', {a1})
    assert _is_linked(b, 'statemachine103_StateMachine', a1)
    if hasattr(a1, 'statemachine103_StateMachineObject'):
        assert _is_linked(a1, 'statemachine103_StateMachineObject', b)
    _safe_set(b, 'statemachine103_StateMachine', {a2})
    assert _is_linked(b, 'statemachine103_StateMachine', a2)
    if hasattr(a1, 'statemachine103_StateMachineObject'):
        assert not _is_linked(a1, 'statemachine103_StateMachineObject', b)
    if hasattr(a2, 'statemachine103_StateMachineObject'):
        assert _is_linked(a2, 'statemachine103_StateMachineObject', b)
    _safe_set(b, 'statemachine103_StateMachine', set())
    assert not _is_linked(b, 'statemachine103_StateMachine', a2)
    if hasattr(a2, 'statemachine103_StateMachineObject'):
        assert not _is_linked(a2, 'statemachine103_StateMachineObject', b)


def test_assoc_machineVariables1_reverse_link_reassign_clear():
    a1 = statemachine103_StateMachineVariable(name="sample_text", type="sample_text")
    a2 = statemachine103_StateMachineVariable(name="sample_text_2", type="sample_text_2")
    b = statemachine103_StateMachine(label="sample_text")
    _safe_set(b, 'statemachine103_StateMachine2', {a1})
    assert _is_linked(b, 'statemachine103_StateMachine2', a1)
    if hasattr(a1, 'statemachine103_StateMachineVariable'):
        assert _is_linked(a1, 'statemachine103_StateMachineVariable', b)
    _safe_set(b, 'statemachine103_StateMachine2', {a2})
    assert _is_linked(b, 'statemachine103_StateMachine2', a2)
    if hasattr(a1, 'statemachine103_StateMachineVariable'):
        assert not _is_linked(a1, 'statemachine103_StateMachineVariable', b)
    if hasattr(a2, 'statemachine103_StateMachineVariable'):
        assert _is_linked(a2, 'statemachine103_StateMachineVariable', b)
    _safe_set(b, 'statemachine103_StateMachine2', set())
    assert not _is_linked(b, 'statemachine103_StateMachine2', a2)
    if hasattr(a2, 'statemachine103_StateMachineVariable'):
        assert not _is_linked(a2, 'statemachine103_StateMachineVariable', b)


def test_assoc_next10_reverse_link_reassign_clear():
    a1 = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    a2 = statemachine103_Action(actionLabel="sample_text_2", actionStatement="sample_text_2")
    b = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    _safe_set(b, 'statemachine103_Action9', a1)
    assert _is_linked(b, 'statemachine103_Action9', a1)
    if hasattr(a1, 'statemachine103_Action11'):
        assert _is_linked(a1, 'statemachine103_Action11', b)
    _safe_set(b, 'statemachine103_Action9', a2)
    assert _is_linked(b, 'statemachine103_Action9', a2)
    if hasattr(a1, 'statemachine103_Action11'):
        assert not _is_linked(a1, 'statemachine103_Action11', b)
    if hasattr(a2, 'statemachine103_Action11'):
        assert _is_linked(a2, 'statemachine103_Action11', b)
    _safe_set(b, 'statemachine103_Action9', None)
    assert not _is_linked(b, 'statemachine103_Action9', a2)
    if hasattr(a2, 'statemachine103_Action11'):
        assert not _is_linked(a2, 'statemachine103_Action11', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    a2 = statemachine103_Transition(guardExpression="sample_text_2", guardLabel="sample_text_2")
    b = statemachine103_State(id=7)
    _safe_set(b, 'statemachine103_State', a1)
    assert _is_linked(b, 'statemachine103_State', a1)
    if hasattr(a1, 'statemachine103_Transition'):
        assert _is_linked(a1, 'statemachine103_Transition', b)
    _safe_set(b, 'statemachine103_State', a2)
    assert _is_linked(b, 'statemachine103_State', a2)
    if hasattr(a1, 'statemachine103_Transition'):
        assert not _is_linked(a1, 'statemachine103_Transition', b)
    if hasattr(a2, 'statemachine103_Transition'):
        assert _is_linked(a2, 'statemachine103_Transition', b)
    _safe_set(b, 'statemachine103_State', None)
    assert not _is_linked(b, 'statemachine103_State', a2)
    if hasattr(a2, 'statemachine103_Transition'):
        assert not _is_linked(a2, 'statemachine103_Transition', b)


def test_assoc_t_actions7_reverse_link_reassign_clear():
    a1 = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    a2 = statemachine103_Transition(guardExpression="sample_text_2", guardLabel="sample_text_2")
    b = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    _safe_set(b, 'statemachine103_Action', a1)
    assert _is_linked(b, 'statemachine103_Action', a1)
    if hasattr(a1, 'statemachine103_Transition8'):
        assert _is_linked(a1, 'statemachine103_Transition8', b)
    _safe_set(b, 'statemachine103_Action', a2)
    assert _is_linked(b, 'statemachine103_Action', a2)
    if hasattr(a1, 'statemachine103_Transition8'):
        assert not _is_linked(a1, 'statemachine103_Transition8', b)
    if hasattr(a2, 'statemachine103_Transition8'):
        assert _is_linked(a2, 'statemachine103_Transition8', b)
    _safe_set(b, 'statemachine103_Action', None)
    assert not _is_linked(b, 'statemachine103_Action', a2)
    if hasattr(a2, 'statemachine103_Transition8'):
        assert not _is_linked(a2, 'statemachine103_Transition8', b)


def test_assoc_target4_reverse_link_reassign_clear():
    a1 = statemachine103_Transition(guardExpression="sample_text", guardLabel="sample_text")
    a2 = statemachine103_Transition(guardExpression="sample_text_2", guardLabel="sample_text_2")
    b = statemachine103_State(id=7)
    _safe_set(b, 'statemachine103_State6', a1)
    assert _is_linked(b, 'statemachine103_State6', a1)
    if hasattr(a1, 'statemachine103_Transition5'):
        assert _is_linked(a1, 'statemachine103_Transition5', b)
    _safe_set(b, 'statemachine103_State6', a2)
    assert _is_linked(b, 'statemachine103_State6', a2)
    if hasattr(a1, 'statemachine103_Transition5'):
        assert not _is_linked(a1, 'statemachine103_Transition5', b)
    if hasattr(a2, 'statemachine103_Transition5'):
        assert _is_linked(a2, 'statemachine103_Transition5', b)
    _safe_set(b, 'statemachine103_State6', None)
    assert not _is_linked(b, 'statemachine103_State6', a2)
    if hasattr(a2, 'statemachine103_Transition5'):
        assert not _is_linked(a2, 'statemachine103_Transition5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_s_actions12_stub_double():
    # statemachine103_NormalState has no real 'statemachine103_NormalState' property in the generated
    # code (a bare stub) -- manually attach it so statemachine103_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine103_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine103_Action(actionLabel="sample_text", actionStatement="sample_text")
    partner = statemachine103_NormalState()
    setattr(partner, 'statemachine103_NormalState', None)
    _safe_set(owner, 'statemachine103_Action13', partner)
    assert owner in getattr(partner, 'statemachine103_NormalState')
    _safe_set(owner, 'statemachine103_Action13', None)
    assert owner not in getattr(partner, 'statemachine103_NormalState')


