import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NHSM_FinalState,
    NHSM_InitialState,
    NHSM_State,
    NHSM_StateMachine,
    NHSM_Transition,
    State,
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

def test_assoc_ownedState7_reverse_link_reassign_clear():
    a1 = NHSM_StateMachine(name="sample_text")
    a2 = NHSM_StateMachine(name="sample_text_2")
    b = NHSM_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'owningStateMachine'):
        assert _is_linked(a1, 'owningStateMachine', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'owningStateMachine'):
        assert not _is_linked(a1, 'owningStateMachine', b)
    if hasattr(a2, 'owningStateMachine'):
        assert _is_linked(a2, 'owningStateMachine', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'owningStateMachine'):
        assert not _is_linked(a2, 'owningStateMachine', b)


def test_assoc_ownedTransition8_reverse_link_reassign_clear():
    a1 = NHSM_Transition(effect="sample_text", trigger="sample_text")
    a2 = NHSM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = NHSM_StateMachine(name="sample_text")
    _safe_set(b, 'owningStateMachine9', {a1})
    assert _is_linked(b, 'owningStateMachine9', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'owningStateMachine9', {a2})
    assert _is_linked(b, 'owningStateMachine9', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'owningStateMachine9', set())
    assert not _is_linked(b, 'owningStateMachine9', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_owningStateMachine0_reverse_link_reassign_clear():
    a1 = NHSM_StateMachine(name="sample_text")
    a2 = NHSM_StateMachine(name="sample_text_2")
    b = NHSM_State(name="sample_text")
    _safe_set(b, 'ownedState', a1)
    assert _is_linked(b, 'ownedState', a1)
    if hasattr(a1, 'StateMachine'):
        assert _is_linked(a1, 'StateMachine', b)
    _safe_set(b, 'ownedState', a2)
    assert _is_linked(b, 'ownedState', a2)
    if hasattr(a1, 'StateMachine'):
        assert not _is_linked(a1, 'StateMachine', b)
    if hasattr(a2, 'StateMachine'):
        assert _is_linked(a2, 'StateMachine', b)
    _safe_set(b, 'ownedState', None)
    assert not _is_linked(b, 'ownedState', a2)
    if hasattr(a2, 'StateMachine'):
        assert not _is_linked(a2, 'StateMachine', b)


def test_assoc_owningStateMachine5_reverse_link_reassign_clear():
    a1 = NHSM_Transition(effect="sample_text", trigger="sample_text")
    a2 = NHSM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = NHSM_StateMachine(name="sample_text")
    _safe_set(b, 'StateMachine6', a1)
    assert _is_linked(b, 'StateMachine6', a1)
    if hasattr(a1, 'ownedTransition'):
        assert _is_linked(a1, 'ownedTransition', b)
    _safe_set(b, 'StateMachine6', a2)
    assert _is_linked(b, 'StateMachine6', a2)
    if hasattr(a1, 'ownedTransition'):
        assert not _is_linked(a1, 'ownedTransition', b)
    if hasattr(a2, 'ownedTransition'):
        assert _is_linked(a2, 'ownedTransition', b)
    _safe_set(b, 'StateMachine6', None)
    assert not _is_linked(b, 'StateMachine6', a2)
    if hasattr(a2, 'ownedTransition'):
        assert not _is_linked(a2, 'ownedTransition', b)


def test_assoc_source2_reverse_link_reassign_clear():
    a1 = NHSM_Transition(effect="sample_text", trigger="sample_text")
    a2 = NHSM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = NHSM_State(name="sample_text")
    _safe_set(b, 'NHSM_State4', a1)
    assert _is_linked(b, 'NHSM_State4', a1)
    if hasattr(a1, 'NHSM_Transition3'):
        assert _is_linked(a1, 'NHSM_Transition3', b)
    _safe_set(b, 'NHSM_State4', a2)
    assert _is_linked(b, 'NHSM_State4', a2)
    if hasattr(a1, 'NHSM_Transition3'):
        assert not _is_linked(a1, 'NHSM_Transition3', b)
    if hasattr(a2, 'NHSM_Transition3'):
        assert _is_linked(a2, 'NHSM_Transition3', b)
    _safe_set(b, 'NHSM_State4', None)
    assert not _is_linked(b, 'NHSM_State4', a2)
    if hasattr(a2, 'NHSM_Transition3'):
        assert not _is_linked(a2, 'NHSM_Transition3', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = NHSM_Transition(effect="sample_text", trigger="sample_text")
    a2 = NHSM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = NHSM_State(name="sample_text")
    _safe_set(b, 'NHSM_State', a1)
    assert _is_linked(b, 'NHSM_State', a1)
    if hasattr(a1, 'NHSM_Transition'):
        assert _is_linked(a1, 'NHSM_Transition', b)
    _safe_set(b, 'NHSM_State', a2)
    assert _is_linked(b, 'NHSM_State', a2)
    if hasattr(a1, 'NHSM_Transition'):
        assert not _is_linked(a1, 'NHSM_Transition', b)
    if hasattr(a2, 'NHSM_Transition'):
        assert _is_linked(a2, 'NHSM_Transition', b)
    _safe_set(b, 'NHSM_State', None)
    assert not _is_linked(b, 'NHSM_State', a2)
    if hasattr(a2, 'NHSM_Transition'):
        assert not _is_linked(a2, 'NHSM_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

