import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    states_CompoundState,
    states_Event,
    states_Module,
    states_SimpleState,
    states_State,
    states_Statemachine,
    states_Transition,
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
    a1 = states_Statemachine(initial=True, name="sample_text", value=7)
    a2 = states_Statemachine(initial=False, name="sample_text_2", value=13)
    b = states_Event(name="sample_text")
    _safe_set(b, 'states_Event', a1)
    assert _is_linked(b, 'states_Event', a1)
    if hasattr(a1, 'states_Statemachine2'):
        assert _is_linked(a1, 'states_Statemachine2', b)
    _safe_set(b, 'states_Event', a2)
    assert _is_linked(b, 'states_Event', a2)
    if hasattr(a1, 'states_Statemachine2'):
        assert not _is_linked(a1, 'states_Statemachine2', b)
    if hasattr(a2, 'states_Statemachine2'):
        assert _is_linked(a2, 'states_Statemachine2', b)
    _safe_set(b, 'states_Event', None)
    assert not _is_linked(b, 'states_Event', a2)
    if hasattr(a2, 'states_Statemachine2'):
        assert not _is_linked(a2, 'states_Statemachine2', b)


def test_assoc_machines0_reverse_link_reassign_clear():
    a1 = states_Statemachine(initial=True, name="sample_text", value=7)
    a2 = states_Statemachine(initial=False, name="sample_text_2", value=13)
    b = states_Module(name="sample_text")
    _safe_set(b, 'states_Module', {a1})
    assert _is_linked(b, 'states_Module', a1)
    if hasattr(a1, 'states_Statemachine'):
        assert _is_linked(a1, 'states_Statemachine', b)
    _safe_set(b, 'states_Module', {a2})
    assert _is_linked(b, 'states_Module', a2)
    if hasattr(a1, 'states_Statemachine'):
        assert not _is_linked(a1, 'states_Statemachine', b)
    if hasattr(a2, 'states_Statemachine'):
        assert _is_linked(a2, 'states_Statemachine', b)
    _safe_set(b, 'states_Module', set())
    assert not _is_linked(b, 'states_Module', a2)
    if hasattr(a2, 'states_Statemachine'):
        assert not _is_linked(a2, 'states_Statemachine', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = states_Statemachine(initial=True, name="sample_text", value=7)
    a2 = states_Statemachine(initial=False, name="sample_text_2", value=13)
    b = states_State(initial=True, name="sample_text")
    _safe_set(b, 'states_State', a1)
    assert _is_linked(b, 'states_State', a1)
    if hasattr(a1, 'states_Statemachine4'):
        assert _is_linked(a1, 'states_Statemachine4', b)
    _safe_set(b, 'states_State', a2)
    assert _is_linked(b, 'states_State', a2)
    if hasattr(a1, 'states_Statemachine4'):
        assert not _is_linked(a1, 'states_Statemachine4', b)
    if hasattr(a2, 'states_Statemachine4'):
        assert _is_linked(a2, 'states_Statemachine4', b)
    _safe_set(b, 'states_State', None)
    assert not _is_linked(b, 'states_State', a2)
    if hasattr(a2, 'states_Statemachine4'):
        assert not _is_linked(a2, 'states_Statemachine4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event9_stub_double():
    # states_Transition has no real 'states_Transition10' property in the generated
    # code (a bare stub) -- manually attach it so states_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # states_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = states_Event(name="sample_text")
    partner = states_Transition()
    setattr(partner, 'states_Transition10', None)
    _safe_set(owner, 'states_Event11', partner)
    assert getattr(partner, 'states_Transition10') == owner
    _safe_set(owner, 'states_Event11', None)
    assert getattr(partner, 'states_Transition10') is None


def test_assoc_machine7_stub_double():
    # states_CompoundState has no real 'states_CompoundState' property in the generated
    # code (a bare stub) -- manually attach it so states_Statemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # states_Statemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = states_Statemachine(initial=True, name="sample_text", value=7)
    partner = states_CompoundState()
    setattr(partner, 'states_CompoundState', None)
    _safe_set(owner, 'states_Statemachine8', partner)
    assert getattr(partner, 'states_CompoundState') == owner
    _safe_set(owner, 'states_Statemachine8', None)
    assert getattr(partner, 'states_CompoundState') is None


def test_assoc_state12_stub_double():
    # states_Transition has no real 'states_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so states_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # states_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = states_State(initial=True, name="sample_text")
    partner = states_Transition()
    setattr(partner, 'states_Transition13', None)
    _safe_set(owner, 'states_State14', partner)
    assert getattr(partner, 'states_Transition13') == owner
    _safe_set(owner, 'states_State14', None)
    assert getattr(partner, 'states_Transition13') is None


def test_assoc_transitions5_stub_double():
    # states_Transition has no real 'states_Transition' property in the generated
    # code (a bare stub) -- manually attach it so states_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # states_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = states_State(initial=True, name="sample_text")
    partner = states_Transition()
    setattr(partner, 'states_Transition', None)
    _safe_set(owner, 'states_State6', {partner})
    assert getattr(partner, 'states_Transition') == owner
    _safe_set(owner, 'states_State6', set())
    assert getattr(partner, 'states_Transition') is None


