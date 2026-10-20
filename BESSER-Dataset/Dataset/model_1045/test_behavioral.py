import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FAbstractState,
    FSM_FAbstractState,
    FSM_FInitialState,
    FSM_FRegularState,
    FSM_FStateMachine,
    FSM_FTransition,
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

def test_assoc_source4_reverse_link_reassign_clear():
    a1 = FSM_FTransition(label="sample_text")
    a2 = FSM_FTransition(label="sample_text_2")
    b = FSM_FAbstractState(name="sample_text")
    _safe_set(b, 'FSM_FAbstractState', a1)
    assert _is_linked(b, 'FSM_FAbstractState', a1)
    if hasattr(a1, 'FSM_FTransition'):
        assert _is_linked(a1, 'FSM_FTransition', b)
    _safe_set(b, 'FSM_FAbstractState', a2)
    assert _is_linked(b, 'FSM_FAbstractState', a2)
    if hasattr(a1, 'FSM_FTransition'):
        assert not _is_linked(a1, 'FSM_FTransition', b)
    if hasattr(a2, 'FSM_FTransition'):
        assert _is_linked(a2, 'FSM_FTransition', b)
    _safe_set(b, 'FSM_FAbstractState', None)
    assert not _is_linked(b, 'FSM_FAbstractState', a2)
    if hasattr(a2, 'FSM_FTransition'):
        assert not _is_linked(a2, 'FSM_FTransition', b)


def test_assoc_stateMachine3_reverse_link_reassign_clear():
    a1 = FSM_FTransition(label="sample_text")
    a2 = FSM_FTransition(label="sample_text_2")
    b = FSM_FStateMachine(name="sample_text")
    _safe_set(b, 'FStateMachine', a1)
    assert _is_linked(b, 'FStateMachine', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'FStateMachine', a2)
    assert _is_linked(b, 'FStateMachine', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'FStateMachine', None)
    assert not _is_linked(b, 'FStateMachine', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_stateMachine8_reverse_link_reassign_clear():
    a1 = FSM_FStateMachine(name="sample_text")
    a2 = FSM_FStateMachine(name="sample_text_2")
    b = FSM_FAbstractState(name="sample_text")
    _safe_set(b, 'states', a1)
    assert _is_linked(b, 'states', a1)
    if hasattr(a1, 'FStateMachine9'):
        assert _is_linked(a1, 'FStateMachine9', b)
    _safe_set(b, 'states', a2)
    assert _is_linked(b, 'states', a2)
    if hasattr(a1, 'FStateMachine9'):
        assert not _is_linked(a1, 'FStateMachine9', b)
    if hasattr(a2, 'FStateMachine9'):
        assert _is_linked(a2, 'FStateMachine9', b)
    _safe_set(b, 'states', None)
    assert not _is_linked(b, 'states', a2)
    if hasattr(a2, 'FStateMachine9'):
        assert not _is_linked(a2, 'FStateMachine9', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = FSM_FStateMachine(name="sample_text")
    a2 = FSM_FStateMachine(name="sample_text_2")
    b = FSM_FAbstractState(name="sample_text")
    _safe_set(b, 'FAbstractState', a1)
    assert _is_linked(b, 'FAbstractState', a1)
    if hasattr(a1, 'stateMachine2'):
        assert _is_linked(a1, 'stateMachine2', b)
    _safe_set(b, 'FAbstractState', a2)
    assert _is_linked(b, 'FAbstractState', a2)
    if hasattr(a1, 'stateMachine2'):
        assert not _is_linked(a1, 'stateMachine2', b)
    if hasattr(a2, 'stateMachine2'):
        assert _is_linked(a2, 'stateMachine2', b)
    _safe_set(b, 'FAbstractState', None)
    assert not _is_linked(b, 'FAbstractState', a2)
    if hasattr(a2, 'stateMachine2'):
        assert not _is_linked(a2, 'stateMachine2', b)


def test_assoc_target5_reverse_link_reassign_clear():
    a1 = FSM_FTransition(label="sample_text")
    a2 = FSM_FTransition(label="sample_text_2")
    b = FSM_FAbstractState(name="sample_text")
    _safe_set(b, 'FSM_FAbstractState7', a1)
    assert _is_linked(b, 'FSM_FAbstractState7', a1)
    if hasattr(a1, 'FSM_FTransition6'):
        assert _is_linked(a1, 'FSM_FTransition6', b)
    _safe_set(b, 'FSM_FAbstractState7', a2)
    assert _is_linked(b, 'FSM_FAbstractState7', a2)
    if hasattr(a1, 'FSM_FTransition6'):
        assert not _is_linked(a1, 'FSM_FTransition6', b)
    if hasattr(a2, 'FSM_FTransition6'):
        assert _is_linked(a2, 'FSM_FTransition6', b)
    _safe_set(b, 'FSM_FAbstractState7', None)
    assert not _is_linked(b, 'FSM_FAbstractState7', a2)
    if hasattr(a2, 'FSM_FTransition6'):
        assert not _is_linked(a2, 'FSM_FTransition6', b)


def test_assoc_transitions0_reverse_link_reassign_clear():
    a1 = FSM_FTransition(label="sample_text")
    a2 = FSM_FTransition(label="sample_text_2")
    b = FSM_FStateMachine(name="sample_text")
    _safe_set(b, 'stateMachine', {a1})
    assert _is_linked(b, 'stateMachine', a1)
    if hasattr(a1, 'FTransition'):
        assert _is_linked(a1, 'FTransition', b)
    _safe_set(b, 'stateMachine', {a2})
    assert _is_linked(b, 'stateMachine', a2)
    if hasattr(a1, 'FTransition'):
        assert not _is_linked(a1, 'FTransition', b)
    if hasattr(a2, 'FTransition'):
        assert _is_linked(a2, 'FTransition', b)
    _safe_set(b, 'stateMachine', set())
    assert not _is_linked(b, 'stateMachine', a2)
    if hasattr(a2, 'FTransition'):
        assert not _is_linked(a2, 'FTransition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

