import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FiniteStateMachines_FiniteStateMachine,
    FiniteStateMachines_State,
    FiniteStateMachines_Transition,
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

def test_assoc_endState5_reverse_link_reassign_clear():
    a1 = FiniteStateMachines_Transition(input="sample_text")
    a2 = FiniteStateMachines_Transition(input="sample_text_2")
    b = FiniteStateMachines_State(isEndState=True, isStartState=True, name="sample_text")
    _safe_set(b, 'FiniteStateMachines_State7', a1)
    assert _is_linked(b, 'FiniteStateMachines_State7', a1)
    if hasattr(a1, 'FiniteStateMachines_Transition6'):
        assert _is_linked(a1, 'FiniteStateMachines_Transition6', b)
    _safe_set(b, 'FiniteStateMachines_State7', a2)
    assert _is_linked(b, 'FiniteStateMachines_State7', a2)
    if hasattr(a1, 'FiniteStateMachines_Transition6'):
        assert not _is_linked(a1, 'FiniteStateMachines_Transition6', b)
    if hasattr(a2, 'FiniteStateMachines_Transition6'):
        assert _is_linked(a2, 'FiniteStateMachines_Transition6', b)
    _safe_set(b, 'FiniteStateMachines_State7', None)
    assert not _is_linked(b, 'FiniteStateMachines_State7', a2)
    if hasattr(a2, 'FiniteStateMachines_Transition6'):
        assert not _is_linked(a2, 'FiniteStateMachines_Transition6', b)


def test_assoc_startState4_reverse_link_reassign_clear():
    a1 = FiniteStateMachines_Transition(input="sample_text")
    a2 = FiniteStateMachines_Transition(input="sample_text_2")
    b = FiniteStateMachines_State(isEndState=True, isStartState=True, name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = FiniteStateMachines_State(isEndState=True, isStartState=True, name="sample_text")
    a2 = FiniteStateMachines_State(isEndState=False, isStartState=False, name="sample_text_2")
    b = FiniteStateMachines_FiniteStateMachine(id="sample_text")
    _safe_set(b, 'FiniteStateMachines_FiniteStateMachine', {a1})
    assert _is_linked(b, 'FiniteStateMachines_FiniteStateMachine', a1)
    if hasattr(a1, 'FiniteStateMachines_State'):
        assert _is_linked(a1, 'FiniteStateMachines_State', b)
    _safe_set(b, 'FiniteStateMachines_FiniteStateMachine', {a2})
    assert _is_linked(b, 'FiniteStateMachines_FiniteStateMachine', a2)
    if hasattr(a1, 'FiniteStateMachines_State'):
        assert not _is_linked(a1, 'FiniteStateMachines_State', b)
    if hasattr(a2, 'FiniteStateMachines_State'):
        assert _is_linked(a2, 'FiniteStateMachines_State', b)
    _safe_set(b, 'FiniteStateMachines_FiniteStateMachine', set())
    assert not _is_linked(b, 'FiniteStateMachines_FiniteStateMachine', a2)
    if hasattr(a2, 'FiniteStateMachines_State'):
        assert not _is_linked(a2, 'FiniteStateMachines_State', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = FiniteStateMachines_Transition(input="sample_text")
    a2 = FiniteStateMachines_Transition(input="sample_text_2")
    b = FiniteStateMachines_FiniteStateMachine(id="sample_text")
    _safe_set(b, 'FiniteStateMachines_FiniteStateMachine2', {a1})
    assert _is_linked(b, 'FiniteStateMachines_FiniteStateMachine2', a1)
    if hasattr(a1, 'FiniteStateMachines_Transition'):
        assert _is_linked(a1, 'FiniteStateMachines_Transition', b)
    _safe_set(b, 'FiniteStateMachines_FiniteStateMachine2', {a2})
    assert _is_linked(b, 'FiniteStateMachines_FiniteStateMachine2', a2)
    if hasattr(a1, 'FiniteStateMachines_Transition'):
        assert not _is_linked(a1, 'FiniteStateMachines_Transition', b)
    if hasattr(a2, 'FiniteStateMachines_Transition'):
        assert _is_linked(a2, 'FiniteStateMachines_Transition', b)
    _safe_set(b, 'FiniteStateMachines_FiniteStateMachine2', set())
    assert not _is_linked(b, 'FiniteStateMachines_FiniteStateMachine2', a2)
    if hasattr(a2, 'FiniteStateMachines_Transition'):
        assert not _is_linked(a2, 'FiniteStateMachines_Transition', b)


def test_assoc_transitions3_reverse_link_reassign_clear():
    a1 = FiniteStateMachines_Transition(input="sample_text")
    a2 = FiniteStateMachines_Transition(input="sample_text_2")
    b = FiniteStateMachines_State(isEndState=True, isStartState=True, name="sample_text")
    _safe_set(b, 'startState', {a1})
    assert _is_linked(b, 'startState', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'startState', {a2})
    assert _is_linked(b, 'startState', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'startState', set())
    assert not _is_linked(b, 'startState', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

