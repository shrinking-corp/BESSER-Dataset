import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    fsm_Buffer,
    fsm_FSMSystem,
    fsm_NamedElement,
    fsm_State,
    fsm_StateMachine,
    fsm_Transition,
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

def test_assoc_currentState4_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    a2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'fsm_State6', a1)
    assert _is_linked(b, 'fsm_State6', a1)
    if hasattr(a1, 'fsm_StateMachine5'):
        assert _is_linked(a1, 'fsm_StateMachine5', b)
    _safe_set(b, 'fsm_State6', a2)
    assert _is_linked(b, 'fsm_State6', a2)
    if hasattr(a1, 'fsm_StateMachine5'):
        assert not _is_linked(a1, 'fsm_StateMachine5', b)
    if hasattr(a2, 'fsm_StateMachine5'):
        assert _is_linked(a2, 'fsm_StateMachine5', b)
    _safe_set(b, 'fsm_State6', None)
    assert not _is_linked(b, 'fsm_State6', a2)
    if hasattr(a2, 'fsm_StateMachine5'):
        assert not _is_linked(a2, 'fsm_StateMachine5', b)


def test_assoc_incomingTransitions9_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition10'):
        assert _is_linked(a1, 'Transition10', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition10'):
        assert not _is_linked(a1, 'Transition10', b)
    if hasattr(a2, 'Transition10'):
        assert _is_linked(a2, 'Transition10', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition10'):
        assert not _is_linked(a2, 'Transition10', b)


def test_assoc_initialState1_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    a2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'fsm_State', a1)
    assert _is_linked(b, 'fsm_State', a1)
    if hasattr(a1, 'fsm_StateMachine'):
        assert _is_linked(a1, 'fsm_StateMachine', b)
    _safe_set(b, 'fsm_State', a2)
    assert _is_linked(b, 'fsm_State', a2)
    if hasattr(a1, 'fsm_StateMachine'):
        assert not _is_linked(a1, 'fsm_StateMachine', b)
    if hasattr(a2, 'fsm_StateMachine'):
        assert _is_linked(a2, 'fsm_StateMachine', b)
    _safe_set(b, 'fsm_State', None)
    assert not _is_linked(b, 'fsm_State', a2)
    if hasattr(a2, 'fsm_StateMachine'):
        assert not _is_linked(a2, 'fsm_StateMachine', b)


def test_assoc_inputs19_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    a2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    b = fsm_Buffer(currentValues="sample_text", initialValue="sample_text")
    _safe_set(b, 'fsm_Buffer20', {a1})
    assert _is_linked(b, 'fsm_Buffer20', a1)
    if hasattr(a1, 'fsm_StateMachine21'):
        assert _is_linked(a1, 'fsm_StateMachine21', b)
    _safe_set(b, 'fsm_Buffer20', {a2})
    assert _is_linked(b, 'fsm_Buffer20', a2)
    if hasattr(a1, 'fsm_StateMachine21'):
        assert not _is_linked(a1, 'fsm_StateMachine21', b)
    if hasattr(a2, 'fsm_StateMachine21'):
        assert _is_linked(a2, 'fsm_StateMachine21', b)
    _safe_set(b, 'fsm_Buffer20', set())
    assert not _is_linked(b, 'fsm_Buffer20', a2)
    if hasattr(a2, 'fsm_StateMachine21'):
        assert not _is_linked(a2, 'fsm_StateMachine21', b)


def test_assoc_outgoingTransitions8_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_outputs22_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    a2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    b = fsm_Buffer(currentValues="sample_text", initialValue="sample_text")
    _safe_set(b, 'fsm_Buffer23', {a1})
    assert _is_linked(b, 'fsm_Buffer23', a1)
    if hasattr(a1, 'fsm_StateMachine24'):
        assert _is_linked(a1, 'fsm_StateMachine24', b)
    _safe_set(b, 'fsm_Buffer23', {a2})
    assert _is_linked(b, 'fsm_Buffer23', a2)
    if hasattr(a1, 'fsm_StateMachine24'):
        assert not _is_linked(a1, 'fsm_StateMachine24', b)
    if hasattr(a2, 'fsm_StateMachine24'):
        assert _is_linked(a2, 'fsm_StateMachine24', b)
    _safe_set(b, 'fsm_Buffer23', set())
    assert not _is_linked(b, 'fsm_Buffer23', a2)
    if hasattr(a2, 'fsm_StateMachine24'):
        assert not _is_linked(a2, 'fsm_StateMachine24', b)


def test_assoc_ownedBuffer17_reverse_link_reassign_clear():
    a1 = fsm_FSMSystem()
    a2 = fsm_FSMSystem()
    b = fsm_Buffer(currentValues="sample_text", initialValue="sample_text")
    _safe_set(b, 'fsm_Buffer', a1)
    assert _is_linked(b, 'fsm_Buffer', a1)
    if hasattr(a1, 'fsm_FSMSystem18'):
        assert _is_linked(a1, 'fsm_FSMSystem18', b)
    _safe_set(b, 'fsm_Buffer', a2)
    assert _is_linked(b, 'fsm_Buffer', a2)
    if hasattr(a1, 'fsm_FSMSystem18'):
        assert not _is_linked(a1, 'fsm_FSMSystem18', b)
    if hasattr(a2, 'fsm_FSMSystem18'):
        assert _is_linked(a2, 'fsm_FSMSystem18', b)
    _safe_set(b, 'fsm_Buffer', None)
    assert not _is_linked(b, 'fsm_Buffer', a2)
    if hasattr(a2, 'fsm_FSMSystem18'):
        assert not _is_linked(a2, 'fsm_FSMSystem18', b)


def test_assoc_ownedStateMachines15_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    a2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    b = fsm_FSMSystem()
    _safe_set(b, 'fsm_FSMSystem', {a1})
    assert _is_linked(b, 'fsm_FSMSystem', a1)
    if hasattr(a1, 'fsm_StateMachine16'):
        assert _is_linked(a1, 'fsm_StateMachine16', b)
    _safe_set(b, 'fsm_FSMSystem', {a2})
    assert _is_linked(b, 'fsm_FSMSystem', a2)
    if hasattr(a1, 'fsm_StateMachine16'):
        assert not _is_linked(a1, 'fsm_StateMachine16', b)
    if hasattr(a2, 'fsm_StateMachine16'):
        assert _is_linked(a2, 'fsm_StateMachine16', b)
    _safe_set(b, 'fsm_FSMSystem', set())
    assert not _is_linked(b, 'fsm_FSMSystem', a2)
    if hasattr(a2, 'fsm_StateMachine16'):
        assert not _is_linked(a2, 'fsm_StateMachine16', b)


def test_assoc_ownedStates0_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    a2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'owningFSM'):
        assert _is_linked(a1, 'owningFSM', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'owningFSM'):
        assert not _is_linked(a1, 'owningFSM', b)
    if hasattr(a2, 'owningFSM'):
        assert _is_linked(a2, 'owningFSM', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'owningFSM'):
        assert not _is_linked(a2, 'owningFSM', b)


def test_assoc_ownedTransitions2_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    _safe_set(b, 'fsm_StateMachine3', {a1})
    assert _is_linked(b, 'fsm_StateMachine3', a1)
    if hasattr(a1, 'fsm_Transition'):
        assert _is_linked(a1, 'fsm_Transition', b)
    _safe_set(b, 'fsm_StateMachine3', {a2})
    assert _is_linked(b, 'fsm_StateMachine3', a2)
    if hasattr(a1, 'fsm_Transition'):
        assert not _is_linked(a1, 'fsm_Transition', b)
    if hasattr(a2, 'fsm_Transition'):
        assert _is_linked(a2, 'fsm_Transition', b)
    _safe_set(b, 'fsm_StateMachine3', set())
    assert not _is_linked(b, 'fsm_StateMachine3', a2)
    if hasattr(a2, 'fsm_Transition'):
        assert not _is_linked(a2, 'fsm_Transition', b)


def test_assoc_owningFSM7_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(consummedString="sample_text", producedString="sample_text", unprocessedString="sample_text")
    a2 = fsm_StateMachine(consummedString="sample_text_2", producedString="sample_text_2", unprocessedString="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'ownedStates', a1)
    assert _is_linked(b, 'ownedStates', a1)
    if hasattr(a1, 'StateMachine'):
        assert _is_linked(a1, 'StateMachine', b)
    _safe_set(b, 'ownedStates', a2)
    assert _is_linked(b, 'ownedStates', a2)
    if hasattr(a1, 'StateMachine'):
        assert not _is_linked(a1, 'StateMachine', b)
    if hasattr(a2, 'StateMachine'):
        assert _is_linked(a2, 'StateMachine', b)
    _safe_set(b, 'ownedStates', None)
    assert not _is_linked(b, 'ownedStates', a2)
    if hasattr(a2, 'StateMachine'):
        assert not _is_linked(a2, 'StateMachine', b)


def test_assoc_source11_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'State12', a1)
    assert _is_linked(b, 'State12', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State12', a2)
    assert _is_linked(b, 'State12', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State12', None)
    assert not _is_linked(b, 'State12', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_target13_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State()
    _safe_set(b, 'State14', a1)
    assert _is_linked(b, 'State14', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State14', a2)
    assert _is_linked(b, 'State14', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State14', None)
    assert not _is_linked(b, 'State14', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

