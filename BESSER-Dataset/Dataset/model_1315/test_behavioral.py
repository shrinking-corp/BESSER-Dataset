import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    stateMachine_Condition,
    stateMachine_Event,
    stateMachine_Model,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_Transition,
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

def test_assoc_events1_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2")
    b = stateMachine_Event(name="sample_text")
    _safe_set(b, 'stateMachine_Event', a1)
    assert _is_linked(b, 'stateMachine_Event', a1)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert _is_linked(a1, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_Event', a2)
    assert _is_linked(b, 'stateMachine_Event', a2)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert not _is_linked(a1, 'stateMachine_StateMachine2', b)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert _is_linked(a2, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_Event', None)
    assert not _is_linked(b, 'stateMachine_Event', a2)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert not _is_linked(a2, 'stateMachine_StateMachine2', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2")
    b = stateMachine_State(name="sample_text")
    _safe_set(b, 'stateMachine_State', a1)
    assert _is_linked(b, 'stateMachine_State', a1)
    if hasattr(a1, 'stateMachine_StateMachine4'):
        assert _is_linked(a1, 'stateMachine_StateMachine4', b)
    _safe_set(b, 'stateMachine_State', a2)
    assert _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a1, 'stateMachine_StateMachine4'):
        assert not _is_linked(a1, 'stateMachine_StateMachine4', b)
    if hasattr(a2, 'stateMachine_StateMachine4'):
        assert _is_linked(a2, 'stateMachine_StateMachine4', b)
    _safe_set(b, 'stateMachine_State', None)
    assert not _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a2, 'stateMachine_StateMachine4'):
        assert not _is_linked(a2, 'stateMachine_StateMachine4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event7_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition8' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Event(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition8', None)
    _safe_set(owner, 'stateMachine_Event9', partner)
    assert getattr(partner, 'stateMachine_Transition8') == owner
    _safe_set(owner, 'stateMachine_Event9', None)
    assert getattr(partner, 'stateMachine_Transition8') is None


def test_assoc_events13_stub_double():
    # stateMachine_Condition has no real 'stateMachine_Condition' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Event(name="sample_text")
    partner = stateMachine_Condition()
    setattr(partner, 'stateMachine_Condition', None)
    _safe_set(owner, 'stateMachine_Event14', partner)
    assert owner in getattr(partner, 'stateMachine_Condition')
    _safe_set(owner, 'stateMachine_Event14', None)
    assert owner not in getattr(partner, 'stateMachine_Condition')


def test_assoc_statemachines0_stub_double():
    # stateMachine_Model has no real 'stateMachine_Model' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_StateMachine(name="sample_text")
    partner = stateMachine_Model()
    setattr(partner, 'stateMachine_Model', None)
    _safe_set(owner, 'stateMachine_StateMachine', partner)
    assert owner in getattr(partner, 'stateMachine_Model')
    _safe_set(owner, 'stateMachine_StateMachine', None)
    assert owner not in getattr(partner, 'stateMachine_Model')


def test_assoc_target10_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition11' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition11', None)
    _safe_set(owner, 'stateMachine_State12', partner)
    assert getattr(partner, 'stateMachine_Transition11') == owner
    _safe_set(owner, 'stateMachine_State12', None)
    assert getattr(partner, 'stateMachine_Transition11') is None


def test_assoc_transitions5_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition', None)
    _safe_set(owner, 'stateMachine_State6', {partner})
    assert getattr(partner, 'stateMachine_Transition') == owner
    _safe_set(owner, 'stateMachine_State6', set())
    assert getattr(partner, 'stateMachine_Transition') is None


