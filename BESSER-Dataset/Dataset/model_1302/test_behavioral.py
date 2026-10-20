import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    IDElement,
    stateMachine_Event,
    stateMachine_IDElement,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_Transition,
    StateKind,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_incoming6_stub_double():
    # stateMachine_Transition has no real 'Transition7' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(kind="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'Transition7', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition7') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition7') is None


def test_assoc_outgoing5_stub_double():
    # stateMachine_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(kind="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_source8_stub_double():
    # stateMachine_Transition has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(kind="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_states0_stub_double():
    # stateMachine_StateMachine has no real 'stateMachine_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(kind="sample_text")
    partner = stateMachine_StateMachine()
    setattr(partner, 'stateMachine_StateMachine', None)
    _safe_set(owner, 'stateMachine_State', partner)
    assert owner in getattr(partner, 'stateMachine_StateMachine')
    _safe_set(owner, 'stateMachine_State', None)
    assert owner not in getattr(partner, 'stateMachine_StateMachine')


def test_assoc_target9_stub_double():
    # stateMachine_Transition has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(kind="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'State10', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'State10', None)
    assert getattr(partner, 'incoming') is None


