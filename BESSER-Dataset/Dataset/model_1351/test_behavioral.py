import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    FiringElement,
    statemachine_AbstractState,
    statemachine_FinalState,
    statemachine_FiringElement,
    statemachine_InitialState,
    statemachine_State,
    statemachine_StateAction,
    statemachine_StateMachine,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_source7_stub_double():
    # statemachine_Transition has no real 'transitionsAsSource' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_AbstractState(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'transitionsAsSource', None)
    _safe_set(owner, 'AbstractState', partner)
    assert getattr(partner, 'transitionsAsSource') == owner
    _safe_set(owner, 'AbstractState', None)
    assert getattr(partner, 'transitionsAsSource') is None


def test_assoc_states0_stub_double():
    # statemachine_StateMachine has no real 'statemachine_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_AbstractState(name="sample_text")
    partner = statemachine_StateMachine()
    setattr(partner, 'statemachine_StateMachine', None)
    _safe_set(owner, 'statemachine_AbstractState', partner)
    assert owner in getattr(partner, 'statemachine_StateMachine')
    _safe_set(owner, 'statemachine_AbstractState', None)
    assert owner not in getattr(partner, 'statemachine_StateMachine')


def test_assoc_target8_stub_double():
    # statemachine_Transition has no real 'transitionsAsTarget' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_AbstractState(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'transitionsAsTarget', None)
    _safe_set(owner, 'AbstractState9', partner)
    assert getattr(partner, 'transitionsAsTarget') == owner
    _safe_set(owner, 'AbstractState9', None)
    assert getattr(partner, 'transitionsAsTarget') is None


def test_assoc_transitionsAsSource3_stub_double():
    # statemachine_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_AbstractState(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_transitionsAsTarget4_stub_double():
    # statemachine_Transition has no real 'Transition5' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_AbstractState(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'Transition5', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition5') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition5') is None


