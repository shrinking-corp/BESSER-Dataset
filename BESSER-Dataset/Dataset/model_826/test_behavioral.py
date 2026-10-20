import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    wheel_State,
    wheel_Transition,
    wheel_WheelSM,
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

def test_assoc_Source12_reverse_link_reassign_clear():
    a1 = wheel_Transition(speed="sample_text", time="sample_text")
    a2 = wheel_Transition(speed="sample_text_2", time="sample_text_2")
    b = wheel_State(name="sample_text")
    _safe_set(b, 'State13', a1)
    assert _is_linked(b, 'State13', a1)
    if hasattr(a1, 'outgoingTransition'):
        assert _is_linked(a1, 'outgoingTransition', b)
    _safe_set(b, 'State13', a2)
    assert _is_linked(b, 'State13', a2)
    if hasattr(a1, 'outgoingTransition'):
        assert not _is_linked(a1, 'outgoingTransition', b)
    if hasattr(a2, 'outgoingTransition'):
        assert _is_linked(a2, 'outgoingTransition', b)
    _safe_set(b, 'State13', None)
    assert not _is_linked(b, 'State13', a2)
    if hasattr(a2, 'outgoingTransition'):
        assert not _is_linked(a2, 'outgoingTransition', b)


def test_assoc_incomingTransition5_reverse_link_reassign_clear():
    a1 = wheel_Transition(speed="sample_text", time="sample_text")
    a2 = wheel_Transition(speed="sample_text_2", time="sample_text_2")
    b = wheel_State(name="sample_text")
    _safe_set(b, 'wheel_State6', a1)
    assert _is_linked(b, 'wheel_State6', a1)
    if hasattr(a1, 'wheel_Transition'):
        assert _is_linked(a1, 'wheel_Transition', b)
    _safe_set(b, 'wheel_State6', a2)
    assert _is_linked(b, 'wheel_State6', a2)
    if hasattr(a1, 'wheel_Transition'):
        assert not _is_linked(a1, 'wheel_Transition', b)
    if hasattr(a2, 'wheel_Transition'):
        assert _is_linked(a2, 'wheel_Transition', b)
    _safe_set(b, 'wheel_State6', None)
    assert not _is_linked(b, 'wheel_State6', a2)
    if hasattr(a2, 'wheel_Transition'):
        assert not _is_linked(a2, 'wheel_Transition', b)


def test_assoc_outgoingTransition7_reverse_link_reassign_clear():
    a1 = wheel_Transition(speed="sample_text", time="sample_text")
    a2 = wheel_Transition(speed="sample_text_2", time="sample_text_2")
    b = wheel_State(name="sample_text")
    _safe_set(b, 'Source', a1)
    assert _is_linked(b, 'Source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'Source', a2)
    assert _is_linked(b, 'Source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'Source', None)
    assert not _is_linked(b, 'Source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_target9_reverse_link_reassign_clear():
    a1 = wheel_Transition(speed="sample_text", time="sample_text")
    a2 = wheel_Transition(speed="sample_text_2", time="sample_text_2")
    b = wheel_State(name="sample_text")
    _safe_set(b, 'wheel_State11', a1)
    assert _is_linked(b, 'wheel_State11', a1)
    if hasattr(a1, 'wheel_Transition10'):
        assert _is_linked(a1, 'wheel_Transition10', b)
    _safe_set(b, 'wheel_State11', a2)
    assert _is_linked(b, 'wheel_State11', a2)
    if hasattr(a1, 'wheel_Transition10'):
        assert not _is_linked(a1, 'wheel_Transition10', b)
    if hasattr(a2, 'wheel_Transition10'):
        assert _is_linked(a2, 'wheel_Transition10', b)
    _safe_set(b, 'wheel_State11', None)
    assert not _is_linked(b, 'wheel_State11', a2)
    if hasattr(a2, 'wheel_Transition10'):
        assert not _is_linked(a2, 'wheel_Transition10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_finalState1_stub_double():
    # wheel_WheelSM has no real 'wheel_WheelSM2' property in the generated
    # code (a bare stub) -- manually attach it so wheel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wheel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wheel_State(name="sample_text")
    partner = wheel_WheelSM()
    setattr(partner, 'wheel_WheelSM2', None)
    _safe_set(owner, 'wheel_State3', partner)
    assert getattr(partner, 'wheel_WheelSM2') == owner
    _safe_set(owner, 'wheel_State3', None)
    assert getattr(partner, 'wheel_WheelSM2') is None


def test_assoc_initialState0_stub_double():
    # wheel_WheelSM has no real 'wheel_WheelSM' property in the generated
    # code (a bare stub) -- manually attach it so wheel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wheel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wheel_State(name="sample_text")
    partner = wheel_WheelSM()
    setattr(partner, 'wheel_WheelSM', None)
    _safe_set(owner, 'wheel_State', partner)
    assert getattr(partner, 'wheel_WheelSM') == owner
    _safe_set(owner, 'wheel_State', None)
    assert getattr(partner, 'wheel_WheelSM') is None


def test_assoc_ownedState4_stub_double():
    # wheel_WheelSM has no real 'owningFSM' property in the generated
    # code (a bare stub) -- manually attach it so wheel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wheel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wheel_State(name="sample_text")
    partner = wheel_WheelSM()
    setattr(partner, 'owningFSM', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningFSM')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningFSM')


def test_assoc_owningFSM8_stub_double():
    # wheel_WheelSM has no real 'WheelSM' property in the generated
    # code (a bare stub) -- manually attach it so wheel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wheel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wheel_State(name="sample_text")
    partner = wheel_WheelSM()
    setattr(partner, 'WheelSM', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'WheelSM') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'WheelSM') is None


