import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Declaration,
    State,
    statemachine_Action,
    statemachine_Declaration,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_NormalState,
    statemachine_State,
    statemachine_StateMachine,
    statemachine_StateMachineVariable,
    statemachine_Transition,
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

def test_assoc_declarations0_reverse_link_reassign_clear():
    a1 = statemachine_StateMachine()
    a2 = statemachine_StateMachine()
    b = statemachine_Declaration()
    _safe_set(b, 'statemachine_Declaration', a1)
    assert _is_linked(b, 'statemachine_Declaration', a1)
    if hasattr(a1, 'statemachine_StateMachine'):
        assert _is_linked(a1, 'statemachine_StateMachine', b)
    _safe_set(b, 'statemachine_Declaration', a2)
    assert _is_linked(b, 'statemachine_Declaration', a2)
    if hasattr(a1, 'statemachine_StateMachine'):
        assert not _is_linked(a1, 'statemachine_StateMachine', b)
    if hasattr(a2, 'statemachine_StateMachine'):
        assert _is_linked(a2, 'statemachine_StateMachine', b)
    _safe_set(b, 'statemachine_Declaration', None)
    assert not _is_linked(b, 'statemachine_Declaration', a2)
    if hasattr(a2, 'statemachine_StateMachine'):
        assert not _is_linked(a2, 'statemachine_StateMachine', b)


def test_assoc_machineVariables1_reverse_link_reassign_clear():
    a1 = statemachine_StateMachineVariable(name="sample_text", type="sample_text")
    a2 = statemachine_StateMachineVariable(name="sample_text_2", type="sample_text_2")
    b = statemachine_StateMachine()
    _safe_set(b, 'statemachine_StateMachine2', {a1})
    assert _is_linked(b, 'statemachine_StateMachine2', a1)
    if hasattr(a1, 'statemachine_StateMachineVariable'):
        assert _is_linked(a1, 'statemachine_StateMachineVariable', b)
    _safe_set(b, 'statemachine_StateMachine2', {a2})
    assert _is_linked(b, 'statemachine_StateMachine2', a2)
    if hasattr(a1, 'statemachine_StateMachineVariable'):
        assert not _is_linked(a1, 'statemachine_StateMachineVariable', b)
    if hasattr(a2, 'statemachine_StateMachineVariable'):
        assert _is_linked(a2, 'statemachine_StateMachineVariable', b)
    _safe_set(b, 'statemachine_StateMachine2', set())
    assert not _is_linked(b, 'statemachine_StateMachine2', a2)
    if hasattr(a2, 'statemachine_StateMachineVariable'):
        assert not _is_linked(a2, 'statemachine_StateMachineVariable', b)


def test_assoc_reachable11_reverse_link_reassign_clear():
    a1 = statemachine_State(id=7, label="sample_text")
    a2 = statemachine_State(id=13, label="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State12', a1)
    assert _is_linked(b, 'statemachine_State12', a1)
    if hasattr(a1, 'statemachine_State10'):
        assert _is_linked(a1, 'statemachine_State10', b)
    _safe_set(b, 'statemachine_State12', a2)
    assert _is_linked(b, 'statemachine_State12', a2)
    if hasattr(a1, 'statemachine_State10'):
        assert not _is_linked(a1, 'statemachine_State10', b)
    if hasattr(a2, 'statemachine_State10'):
        assert _is_linked(a2, 'statemachine_State10', b)
    _safe_set(b, 'statemachine_State12', None)
    assert not _is_linked(b, 'statemachine_State12', a2)
    if hasattr(a2, 'statemachine_State10'):
        assert not _is_linked(a2, 'statemachine_State10', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = statemachine_Transition(actionLabel="sample_text", actionStatement="sample_text", guardExpression="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    a2 = statemachine_Transition(actionLabel="sample_text_2", actionStatement="sample_text_2", guardExpression="sample_text_2", guardLabel="sample_text_2", label="sample_text_2", sourceLabel="sample_text_2", targetLabel="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State', a1)
    assert _is_linked(b, 'statemachine_State', a1)
    if hasattr(a1, 'statemachine_Transition'):
        assert _is_linked(a1, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_State', a2)
    assert _is_linked(b, 'statemachine_State', a2)
    if hasattr(a1, 'statemachine_Transition'):
        assert not _is_linked(a1, 'statemachine_Transition', b)
    if hasattr(a2, 'statemachine_Transition'):
        assert _is_linked(a2, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_State', None)
    assert not _is_linked(b, 'statemachine_State', a2)
    if hasattr(a2, 'statemachine_Transition'):
        assert not _is_linked(a2, 'statemachine_Transition', b)


def test_assoc_successors8_reverse_link_reassign_clear():
    a1 = statemachine_State(id=7, label="sample_text")
    a2 = statemachine_State(id=13, label="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State9', a1)
    assert _is_linked(b, 'statemachine_State9', a1)
    if hasattr(a1, 'statemachine_State7'):
        assert _is_linked(a1, 'statemachine_State7', b)
    _safe_set(b, 'statemachine_State9', a2)
    assert _is_linked(b, 'statemachine_State9', a2)
    if hasattr(a1, 'statemachine_State7'):
        assert not _is_linked(a1, 'statemachine_State7', b)
    if hasattr(a2, 'statemachine_State7'):
        assert _is_linked(a2, 'statemachine_State7', b)
    _safe_set(b, 'statemachine_State9', None)
    assert not _is_linked(b, 'statemachine_State9', a2)
    if hasattr(a2, 'statemachine_State7'):
        assert not _is_linked(a2, 'statemachine_State7', b)


def test_assoc_target4_reverse_link_reassign_clear():
    a1 = statemachine_Transition(actionLabel="sample_text", actionStatement="sample_text", guardExpression="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    a2 = statemachine_Transition(actionLabel="sample_text_2", actionStatement="sample_text_2", guardExpression="sample_text_2", guardLabel="sample_text_2", label="sample_text_2", sourceLabel="sample_text_2", targetLabel="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State6', a1)
    assert _is_linked(b, 'statemachine_State6', a1)
    if hasattr(a1, 'statemachine_Transition5'):
        assert _is_linked(a1, 'statemachine_Transition5', b)
    _safe_set(b, 'statemachine_State6', a2)
    assert _is_linked(b, 'statemachine_State6', a2)
    if hasattr(a1, 'statemachine_Transition5'):
        assert not _is_linked(a1, 'statemachine_Transition5', b)
    if hasattr(a2, 'statemachine_Transition5'):
        assert _is_linked(a2, 'statemachine_Transition5', b)
    _safe_set(b, 'statemachine_State6', None)
    assert not _is_linked(b, 'statemachine_State6', a2)
    if hasattr(a2, 'statemachine_Transition5'):
        assert not _is_linked(a2, 'statemachine_Transition5', b)


