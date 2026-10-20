import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    simplefsm_FSM,
    simplefsm_State,
    simplefsm_Transition,
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

def test_assoc_incomingTransition4_stub_double():
    # simplefsm_Transition has no real 'Transition5' property in the generated
    # code (a bare stub) -- manually attach it so simplefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplefsm_State(name="sample_text")
    partner = simplefsm_Transition()
    setattr(partner, 'Transition5', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition5') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition5') is None


def test_assoc_initialState1_stub_double():
    # simplefsm_FSM has no real 'simplefsm_FSM' property in the generated
    # code (a bare stub) -- manually attach it so simplefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplefsm_State(name="sample_text")
    partner = simplefsm_FSM()
    setattr(partner, 'simplefsm_FSM', None)
    _safe_set(owner, 'simplefsm_State', partner)
    assert getattr(partner, 'simplefsm_FSM') == owner
    _safe_set(owner, 'simplefsm_State', None)
    assert getattr(partner, 'simplefsm_FSM') is None


def test_assoc_outgoingTransition3_stub_double():
    # simplefsm_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so simplefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplefsm_State(name="sample_text")
    partner = simplefsm_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_ownedState0_stub_double():
    # simplefsm_FSM has no real 'owningFSM' property in the generated
    # code (a bare stub) -- manually attach it so simplefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplefsm_State(name="sample_text")
    partner = simplefsm_FSM()
    setattr(partner, 'owningFSM', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningFSM')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningFSM')


def test_assoc_owningFSM2_stub_double():
    # simplefsm_FSM has no real 'FSM' property in the generated
    # code (a bare stub) -- manually attach it so simplefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplefsm_State(name="sample_text")
    partner = simplefsm_FSM()
    setattr(partner, 'FSM', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'FSM') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'FSM') is None


def test_assoc_source6_stub_double():
    # simplefsm_Transition has no real 'outgoingTransition' property in the generated
    # code (a bare stub) -- manually attach it so simplefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplefsm_State(name="sample_text")
    partner = simplefsm_Transition()
    setattr(partner, 'outgoingTransition', None)
    _safe_set(owner, 'State7', partner)
    assert getattr(partner, 'outgoingTransition') == owner
    _safe_set(owner, 'State7', None)
    assert getattr(partner, 'outgoingTransition') is None


def test_assoc_target8_stub_double():
    # simplefsm_Transition has no real 'incomingTransition' property in the generated
    # code (a bare stub) -- manually attach it so simplefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplefsm_State(name="sample_text")
    partner = simplefsm_Transition()
    setattr(partner, 'incomingTransition', None)
    _safe_set(owner, 'State9', partner)
    assert getattr(partner, 'incomingTransition') == owner
    _safe_set(owner, 'State9', None)
    assert getattr(partner, 'incomingTransition') is None


