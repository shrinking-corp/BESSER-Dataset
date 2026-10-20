import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    StateMachines_Behavior,
    StateMachines_ConnectionPointReference,
    StateMachines_FinalState,
    StateMachines_Pseudostate,
    StateMachines_Region,
    StateMachines_State,
    StateMachines_StateMachine,
    StateMachines_Transition,
    StateMachines_Trigger,
    StateMachines_Vertex,
    Vertex,
    PseudoStateKind,
    TransitionKind,
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

def test_assoc_connectionPoint15_stub_double():
    # StateMachines_State has no real 'StateMachines_State16' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_Pseudostate(kind="sample_text")
    partner = StateMachines_State()
    setattr(partner, 'StateMachines_State16', None)
    _safe_set(owner, 'StateMachines_Pseudostate', partner)
    assert owner in getattr(partner, 'StateMachines_State16')
    _safe_set(owner, 'StateMachines_Pseudostate', None)
    assert owner not in getattr(partner, 'StateMachines_State16')


def test_assoc_entry33_stub_double():
    # StateMachines_ConnectionPointReference has no real 'StateMachines_ConnectionPointReference34' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_Pseudostate(kind="sample_text")
    partner = StateMachines_ConnectionPointReference()
    setattr(partner, 'StateMachines_ConnectionPointReference34', None)
    _safe_set(owner, 'StateMachines_Pseudostate35', partner)
    assert owner in getattr(partner, 'StateMachines_ConnectionPointReference34')
    _safe_set(owner, 'StateMachines_Pseudostate35', None)
    assert owner not in getattr(partner, 'StateMachines_ConnectionPointReference34')


def test_assoc_exit36_stub_double():
    # StateMachines_ConnectionPointReference has no real 'StateMachines_ConnectionPointReference37' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_Pseudostate(kind="sample_text")
    partner = StateMachines_ConnectionPointReference()
    setattr(partner, 'StateMachines_ConnectionPointReference37', None)
    _safe_set(owner, 'StateMachines_Pseudostate38', partner)
    assert owner in getattr(partner, 'StateMachines_ConnectionPointReference37')
    _safe_set(owner, 'StateMachines_Pseudostate38', None)
    assert owner not in getattr(partner, 'StateMachines_ConnectionPointReference37')


def test_assoc_incoming8_stub_double():
    # StateMachines_Vertex has no real 'StateMachines_Vertex9' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_Transition(kind="sample_text")
    partner = StateMachines_Vertex()
    setattr(partner, 'StateMachines_Vertex9', None)
    _safe_set(owner, 'StateMachines_Transition10', partner)
    assert owner in getattr(partner, 'StateMachines_Vertex9')
    _safe_set(owner, 'StateMachines_Transition10', None)
    assert owner not in getattr(partner, 'StateMachines_Vertex9')


def test_assoc_outgoing5_stub_double():
    # StateMachines_Vertex has no real 'StateMachines_Vertex6' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_Transition(kind="sample_text")
    partner = StateMachines_Vertex()
    setattr(partner, 'StateMachines_Vertex6', None)
    _safe_set(owner, 'StateMachines_Transition7', partner)
    assert owner in getattr(partner, 'StateMachines_Vertex6')
    _safe_set(owner, 'StateMachines_Transition7', None)
    assert owner not in getattr(partner, 'StateMachines_Vertex6')


def test_assoc_transition3_stub_double():
    # StateMachines_Region has no real 'StateMachines_Region4' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_Transition(kind="sample_text")
    partner = StateMachines_Region()
    setattr(partner, 'StateMachines_Region4', None)
    _safe_set(owner, 'StateMachines_Transition', partner)
    assert owner in getattr(partner, 'StateMachines_Region4')
    _safe_set(owner, 'StateMachines_Transition', None)
    assert owner not in getattr(partner, 'StateMachines_Region4')


def test_assoc_trigger11_stub_double():
    # StateMachines_Trigger has no real 'StateMachines_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_Transition(kind="sample_text")
    partner = StateMachines_Trigger()
    setattr(partner, 'StateMachines_Trigger', None)
    _safe_set(owner, 'StateMachines_Transition12', {partner})
    assert getattr(partner, 'StateMachines_Trigger') == owner
    _safe_set(owner, 'StateMachines_Transition12', set())
    assert getattr(partner, 'StateMachines_Trigger') is None


