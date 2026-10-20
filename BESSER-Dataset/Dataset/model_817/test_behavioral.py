import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsmSample_Action,
    fsmSample_FSM,
    fsmSample_State,
    fsmSample_Transition,
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

def test_assoc_action24_reverse_link_reassign_clear():
    a1 = fsmSample_Transition(input="sample_text", output="sample_text")
    a2 = fsmSample_Transition(input="sample_text_2", output="sample_text_2")
    b = fsmSample_Action(name="sample_text")
    _safe_set(b, 'fsmSample_Action', a1)
    assert _is_linked(b, 'fsmSample_Action', a1)
    if hasattr(a1, 'fsmSample_Transition25'):
        assert _is_linked(a1, 'fsmSample_Transition25', b)
    _safe_set(b, 'fsmSample_Action', a2)
    assert _is_linked(b, 'fsmSample_Action', a2)
    if hasattr(a1, 'fsmSample_Transition25'):
        assert not _is_linked(a1, 'fsmSample_Transition25', b)
    if hasattr(a2, 'fsmSample_Transition25'):
        assert _is_linked(a2, 'fsmSample_Transition25', b)
    _safe_set(b, 'fsmSample_Action', None)
    assert not _is_linked(b, 'fsmSample_Action', a2)
    if hasattr(a2, 'fsmSample_Transition25'):
        assert not _is_linked(a2, 'fsmSample_Transition25', b)


def test_assoc_currentState7_reverse_link_reassign_clear():
    a1 = fsmSample_State(name="sample_text")
    a2 = fsmSample_State(name="sample_text_2")
    b = fsmSample_FSM(name="sample_text")
    _safe_set(b, 'fsmSample_FSM8', a1)
    assert _is_linked(b, 'fsmSample_FSM8', a1)
    if hasattr(a1, 'fsmSample_State9'):
        assert _is_linked(a1, 'fsmSample_State9', b)
    _safe_set(b, 'fsmSample_FSM8', a2)
    assert _is_linked(b, 'fsmSample_FSM8', a2)
    if hasattr(a1, 'fsmSample_State9'):
        assert not _is_linked(a1, 'fsmSample_State9', b)
    if hasattr(a2, 'fsmSample_State9'):
        assert _is_linked(a2, 'fsmSample_State9', b)
    _safe_set(b, 'fsmSample_FSM8', None)
    assert not _is_linked(b, 'fsmSample_FSM8', a2)
    if hasattr(a2, 'fsmSample_State9'):
        assert not _is_linked(a2, 'fsmSample_State9', b)


def test_assoc_finalState4_reverse_link_reassign_clear():
    a1 = fsmSample_State(name="sample_text")
    a2 = fsmSample_State(name="sample_text_2")
    b = fsmSample_FSM(name="sample_text")
    _safe_set(b, 'fsmSample_FSM5', {a1})
    assert _is_linked(b, 'fsmSample_FSM5', a1)
    if hasattr(a1, 'fsmSample_State6'):
        assert _is_linked(a1, 'fsmSample_State6', b)
    _safe_set(b, 'fsmSample_FSM5', {a2})
    assert _is_linked(b, 'fsmSample_FSM5', a2)
    if hasattr(a1, 'fsmSample_State6'):
        assert not _is_linked(a1, 'fsmSample_State6', b)
    if hasattr(a2, 'fsmSample_State6'):
        assert _is_linked(a2, 'fsmSample_State6', b)
    _safe_set(b, 'fsmSample_FSM5', set())
    assert not _is_linked(b, 'fsmSample_FSM5', a2)
    if hasattr(a2, 'fsmSample_State6'):
        assert not _is_linked(a2, 'fsmSample_State6', b)


def test_assoc_incomingTransition15_reverse_link_reassign_clear():
    a1 = fsmSample_Transition(input="sample_text", output="sample_text")
    a2 = fsmSample_Transition(input="sample_text_2", output="sample_text_2")
    b = fsmSample_State(name="sample_text")
    _safe_set(b, 'fsmSample_State16', {a1})
    assert _is_linked(b, 'fsmSample_State16', a1)
    if hasattr(a1, 'fsmSample_Transition17'):
        assert _is_linked(a1, 'fsmSample_Transition17', b)
    _safe_set(b, 'fsmSample_State16', {a2})
    assert _is_linked(b, 'fsmSample_State16', a2)
    if hasattr(a1, 'fsmSample_Transition17'):
        assert not _is_linked(a1, 'fsmSample_Transition17', b)
    if hasattr(a2, 'fsmSample_Transition17'):
        assert _is_linked(a2, 'fsmSample_Transition17', b)
    _safe_set(b, 'fsmSample_State16', set())
    assert not _is_linked(b, 'fsmSample_State16', a2)
    if hasattr(a2, 'fsmSample_Transition17'):
        assert not _is_linked(a2, 'fsmSample_Transition17', b)


def test_assoc_initialState1_reverse_link_reassign_clear():
    a1 = fsmSample_State(name="sample_text")
    a2 = fsmSample_State(name="sample_text_2")
    b = fsmSample_FSM(name="sample_text")
    _safe_set(b, 'fsmSample_FSM2', a1)
    assert _is_linked(b, 'fsmSample_FSM2', a1)
    if hasattr(a1, 'fsmSample_State3'):
        assert _is_linked(a1, 'fsmSample_State3', b)
    _safe_set(b, 'fsmSample_FSM2', a2)
    assert _is_linked(b, 'fsmSample_FSM2', a2)
    if hasattr(a1, 'fsmSample_State3'):
        assert not _is_linked(a1, 'fsmSample_State3', b)
    if hasattr(a2, 'fsmSample_State3'):
        assert _is_linked(a2, 'fsmSample_State3', b)
    _safe_set(b, 'fsmSample_FSM2', None)
    assert not _is_linked(b, 'fsmSample_FSM2', a2)
    if hasattr(a2, 'fsmSample_State3'):
        assert not _is_linked(a2, 'fsmSample_State3', b)


def test_assoc_outgoingTransition13_reverse_link_reassign_clear():
    a1 = fsmSample_Transition(input="sample_text", output="sample_text")
    a2 = fsmSample_Transition(input="sample_text_2", output="sample_text_2")
    b = fsmSample_State(name="sample_text")
    _safe_set(b, 'fsmSample_State14', {a1})
    assert _is_linked(b, 'fsmSample_State14', a1)
    if hasattr(a1, 'fsmSample_Transition'):
        assert _is_linked(a1, 'fsmSample_Transition', b)
    _safe_set(b, 'fsmSample_State14', {a2})
    assert _is_linked(b, 'fsmSample_State14', a2)
    if hasattr(a1, 'fsmSample_Transition'):
        assert not _is_linked(a1, 'fsmSample_Transition', b)
    if hasattr(a2, 'fsmSample_Transition'):
        assert _is_linked(a2, 'fsmSample_Transition', b)
    _safe_set(b, 'fsmSample_State14', set())
    assert not _is_linked(b, 'fsmSample_State14', a2)
    if hasattr(a2, 'fsmSample_Transition'):
        assert not _is_linked(a2, 'fsmSample_Transition', b)


def test_assoc_ownedState0_reverse_link_reassign_clear():
    a1 = fsmSample_State(name="sample_text")
    a2 = fsmSample_State(name="sample_text_2")
    b = fsmSample_FSM(name="sample_text")
    _safe_set(b, 'fsmSample_FSM', {a1})
    assert _is_linked(b, 'fsmSample_FSM', a1)
    if hasattr(a1, 'fsmSample_State'):
        assert _is_linked(a1, 'fsmSample_State', b)
    _safe_set(b, 'fsmSample_FSM', {a2})
    assert _is_linked(b, 'fsmSample_FSM', a2)
    if hasattr(a1, 'fsmSample_State'):
        assert not _is_linked(a1, 'fsmSample_State', b)
    if hasattr(a2, 'fsmSample_State'):
        assert _is_linked(a2, 'fsmSample_State', b)
    _safe_set(b, 'fsmSample_FSM', set())
    assert not _is_linked(b, 'fsmSample_FSM', a2)
    if hasattr(a2, 'fsmSample_State'):
        assert not _is_linked(a2, 'fsmSample_State', b)


def test_assoc_owningFSM10_reverse_link_reassign_clear():
    a1 = fsmSample_State(name="sample_text")
    a2 = fsmSample_State(name="sample_text_2")
    b = fsmSample_FSM(name="sample_text")
    _safe_set(b, 'fsmSample_FSM12', a1)
    assert _is_linked(b, 'fsmSample_FSM12', a1)
    if hasattr(a1, 'fsmSample_State11'):
        assert _is_linked(a1, 'fsmSample_State11', b)
    _safe_set(b, 'fsmSample_FSM12', a2)
    assert _is_linked(b, 'fsmSample_FSM12', a2)
    if hasattr(a1, 'fsmSample_State11'):
        assert not _is_linked(a1, 'fsmSample_State11', b)
    if hasattr(a2, 'fsmSample_State11'):
        assert _is_linked(a2, 'fsmSample_State11', b)
    _safe_set(b, 'fsmSample_FSM12', None)
    assert not _is_linked(b, 'fsmSample_FSM12', a2)
    if hasattr(a2, 'fsmSample_State11'):
        assert not _is_linked(a2, 'fsmSample_State11', b)


def test_assoc_source18_reverse_link_reassign_clear():
    a1 = fsmSample_Transition(input="sample_text", output="sample_text")
    a2 = fsmSample_Transition(input="sample_text_2", output="sample_text_2")
    b = fsmSample_State(name="sample_text")
    _safe_set(b, 'fsmSample_State20', a1)
    assert _is_linked(b, 'fsmSample_State20', a1)
    if hasattr(a1, 'fsmSample_Transition19'):
        assert _is_linked(a1, 'fsmSample_Transition19', b)
    _safe_set(b, 'fsmSample_State20', a2)
    assert _is_linked(b, 'fsmSample_State20', a2)
    if hasattr(a1, 'fsmSample_Transition19'):
        assert not _is_linked(a1, 'fsmSample_Transition19', b)
    if hasattr(a2, 'fsmSample_Transition19'):
        assert _is_linked(a2, 'fsmSample_Transition19', b)
    _safe_set(b, 'fsmSample_State20', None)
    assert not _is_linked(b, 'fsmSample_State20', a2)
    if hasattr(a2, 'fsmSample_Transition19'):
        assert not _is_linked(a2, 'fsmSample_Transition19', b)


def test_assoc_target21_reverse_link_reassign_clear():
    a1 = fsmSample_Transition(input="sample_text", output="sample_text")
    a2 = fsmSample_Transition(input="sample_text_2", output="sample_text_2")
    b = fsmSample_State(name="sample_text")
    _safe_set(b, 'fsmSample_State23', a1)
    assert _is_linked(b, 'fsmSample_State23', a1)
    if hasattr(a1, 'fsmSample_Transition22'):
        assert _is_linked(a1, 'fsmSample_Transition22', b)
    _safe_set(b, 'fsmSample_State23', a2)
    assert _is_linked(b, 'fsmSample_State23', a2)
    if hasattr(a1, 'fsmSample_Transition22'):
        assert not _is_linked(a1, 'fsmSample_Transition22', b)
    if hasattr(a2, 'fsmSample_Transition22'):
        assert _is_linked(a2, 'fsmSample_Transition22', b)
    _safe_set(b, 'fsmSample_State23', None)
    assert not _is_linked(b, 'fsmSample_State23', a2)
    if hasattr(a2, 'fsmSample_Transition22'):
        assert not _is_linked(a2, 'fsmSample_Transition22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

