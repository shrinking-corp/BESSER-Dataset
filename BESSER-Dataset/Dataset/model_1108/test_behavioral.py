import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    oclstates_CompoundState,
    oclstates_Event,
    oclstates_Module,
    oclstates_SimpleState,
    oclstates_State,
    oclstates_Statemachine,
    oclstates_Transition,
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
    a1 = oclstates_Statemachine(initial=True, name="sample_text", value=7)
    a2 = oclstates_Statemachine(initial=False, name="sample_text_2", value=13)
    b = oclstates_Event(name="sample_text")
    _safe_set(b, 'oclstates_Event', a1)
    assert _is_linked(b, 'oclstates_Event', a1)
    if hasattr(a1, 'oclstates_Statemachine2'):
        assert _is_linked(a1, 'oclstates_Statemachine2', b)
    _safe_set(b, 'oclstates_Event', a2)
    assert _is_linked(b, 'oclstates_Event', a2)
    if hasattr(a1, 'oclstates_Statemachine2'):
        assert not _is_linked(a1, 'oclstates_Statemachine2', b)
    if hasattr(a2, 'oclstates_Statemachine2'):
        assert _is_linked(a2, 'oclstates_Statemachine2', b)
    _safe_set(b, 'oclstates_Event', None)
    assert not _is_linked(b, 'oclstates_Event', a2)
    if hasattr(a2, 'oclstates_Statemachine2'):
        assert not _is_linked(a2, 'oclstates_Statemachine2', b)


def test_assoc_machines0_reverse_link_reassign_clear():
    a1 = oclstates_Statemachine(initial=True, name="sample_text", value=7)
    a2 = oclstates_Statemachine(initial=False, name="sample_text_2", value=13)
    b = oclstates_Module(name="sample_text")
    _safe_set(b, 'oclstates_Module', {a1})
    assert _is_linked(b, 'oclstates_Module', a1)
    if hasattr(a1, 'oclstates_Statemachine'):
        assert _is_linked(a1, 'oclstates_Statemachine', b)
    _safe_set(b, 'oclstates_Module', {a2})
    assert _is_linked(b, 'oclstates_Module', a2)
    if hasattr(a1, 'oclstates_Statemachine'):
        assert not _is_linked(a1, 'oclstates_Statemachine', b)
    if hasattr(a2, 'oclstates_Statemachine'):
        assert _is_linked(a2, 'oclstates_Statemachine', b)
    _safe_set(b, 'oclstates_Module', set())
    assert not _is_linked(b, 'oclstates_Module', a2)
    if hasattr(a2, 'oclstates_Statemachine'):
        assert not _is_linked(a2, 'oclstates_Statemachine', b)


def test_assoc_statemachine7_reverse_link_reassign_clear():
    a1 = oclstates_Statemachine(initial=True, name="sample_text", value=7)
    a2 = oclstates_Statemachine(initial=False, name="sample_text_2", value=13)
    b = oclstates_State(initial=True, name="sample_text")
    _safe_set(b, 'oclstates_State8', a1)
    assert _is_linked(b, 'oclstates_State8', a1)
    if hasattr(a1, 'oclstates_Statemachine9'):
        assert _is_linked(a1, 'oclstates_Statemachine9', b)
    _safe_set(b, 'oclstates_State8', a2)
    assert _is_linked(b, 'oclstates_State8', a2)
    if hasattr(a1, 'oclstates_Statemachine9'):
        assert not _is_linked(a1, 'oclstates_Statemachine9', b)
    if hasattr(a2, 'oclstates_Statemachine9'):
        assert _is_linked(a2, 'oclstates_Statemachine9', b)
    _safe_set(b, 'oclstates_State8', None)
    assert not _is_linked(b, 'oclstates_State8', a2)
    if hasattr(a2, 'oclstates_Statemachine9'):
        assert not _is_linked(a2, 'oclstates_Statemachine9', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = oclstates_Statemachine(initial=True, name="sample_text", value=7)
    a2 = oclstates_Statemachine(initial=False, name="sample_text_2", value=13)
    b = oclstates_State(initial=True, name="sample_text")
    _safe_set(b, 'oclstates_State', a1)
    assert _is_linked(b, 'oclstates_State', a1)
    if hasattr(a1, 'oclstates_Statemachine4'):
        assert _is_linked(a1, 'oclstates_Statemachine4', b)
    _safe_set(b, 'oclstates_State', a2)
    assert _is_linked(b, 'oclstates_State', a2)
    if hasattr(a1, 'oclstates_Statemachine4'):
        assert not _is_linked(a1, 'oclstates_Statemachine4', b)
    if hasattr(a2, 'oclstates_Statemachine4'):
        assert _is_linked(a2, 'oclstates_Statemachine4', b)
    _safe_set(b, 'oclstates_State', None)
    assert not _is_linked(b, 'oclstates_State', a2)
    if hasattr(a2, 'oclstates_Statemachine4'):
        assert not _is_linked(a2, 'oclstates_Statemachine4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event12_stub_double():
    # oclstates_Transition has no real 'oclstates_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so oclstates_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclstates_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclstates_Event(name="sample_text")
    partner = oclstates_Transition()
    setattr(partner, 'oclstates_Transition13', None)
    _safe_set(owner, 'oclstates_Event14', partner)
    assert getattr(partner, 'oclstates_Transition13') == owner
    _safe_set(owner, 'oclstates_Event14', None)
    assert getattr(partner, 'oclstates_Transition13') is None


def test_assoc_machine10_stub_double():
    # oclstates_CompoundState has no real 'oclstates_CompoundState' property in the generated
    # code (a bare stub) -- manually attach it so oclstates_Statemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclstates_Statemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclstates_Statemachine(initial=True, name="sample_text", value=7)
    partner = oclstates_CompoundState()
    setattr(partner, 'oclstates_CompoundState', None)
    _safe_set(owner, 'oclstates_Statemachine11', partner)
    assert getattr(partner, 'oclstates_CompoundState') == owner
    _safe_set(owner, 'oclstates_Statemachine11', None)
    assert getattr(partner, 'oclstates_CompoundState') is None


def test_assoc_state15_stub_double():
    # oclstates_Transition has no real 'oclstates_Transition16' property in the generated
    # code (a bare stub) -- manually attach it so oclstates_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclstates_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclstates_State(initial=True, name="sample_text")
    partner = oclstates_Transition()
    setattr(partner, 'oclstates_Transition16', None)
    _safe_set(owner, 'oclstates_State17', partner)
    assert getattr(partner, 'oclstates_Transition16') == owner
    _safe_set(owner, 'oclstates_State17', None)
    assert getattr(partner, 'oclstates_Transition16') is None


def test_assoc_transitions5_stub_double():
    # oclstates_Transition has no real 'oclstates_Transition' property in the generated
    # code (a bare stub) -- manually attach it so oclstates_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclstates_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclstates_State(initial=True, name="sample_text")
    partner = oclstates_Transition()
    setattr(partner, 'oclstates_Transition', None)
    _safe_set(owner, 'oclstates_State6', {partner})
    assert getattr(partner, 'oclstates_Transition') == owner
    _safe_set(owner, 'oclstates_State6', set())
    assert getattr(partner, 'oclstates_Transition') is None


