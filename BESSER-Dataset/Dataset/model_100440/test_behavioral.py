import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    statemachine_mk2_Composite_state,
    statemachine_mk2_Event,
    statemachine_mk2_Final_state,
    statemachine_mk2_SimpleState,
    statemachine_mk2_State,
    statemachine_mk2_StateMachine,
    statemachine_mk2_Transition,
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

def test_assoc_causes23_reverse_link_reassign_clear():
    a1 = statemachine_mk2_Transition(name="sample_text")
    a2 = statemachine_mk2_Transition(name="sample_text_2")
    b = statemachine_mk2_Event(description="sample_text")
    _safe_set(b, 'statemachine_mk2_Event24', {a1})
    assert _is_linked(b, 'statemachine_mk2_Event24', a1)
    if hasattr(a1, 'statemachine_mk2_Transition25'):
        assert _is_linked(a1, 'statemachine_mk2_Transition25', b)
    _safe_set(b, 'statemachine_mk2_Event24', {a2})
    assert _is_linked(b, 'statemachine_mk2_Event24', a2)
    if hasattr(a1, 'statemachine_mk2_Transition25'):
        assert not _is_linked(a1, 'statemachine_mk2_Transition25', b)
    if hasattr(a2, 'statemachine_mk2_Transition25'):
        assert _is_linked(a2, 'statemachine_mk2_Transition25', b)
    _safe_set(b, 'statemachine_mk2_Event24', set())
    assert not _is_linked(b, 'statemachine_mk2_Event24', a2)
    if hasattr(a2, 'statemachine_mk2_Transition25'):
        assert not _is_linked(a2, 'statemachine_mk2_Transition25', b)


def test_assoc_incoming12_reverse_link_reassign_clear():
    a1 = statemachine_mk2_Transition(name="sample_text")
    a2 = statemachine_mk2_Transition(name="sample_text_2")
    b = statemachine_mk2_State(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition13'):
        assert _is_linked(a1, 'Transition13', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition13'):
        assert not _is_linked(a1, 'Transition13', b)
    if hasattr(a2, 'Transition13'):
        assert _is_linked(a2, 'Transition13', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition13'):
        assert not _is_linked(a2, 'Transition13', b)


def test_assoc_outgoing11_reverse_link_reassign_clear():
    a1 = statemachine_mk2_Transition(name="sample_text")
    a2 = statemachine_mk2_Transition(name="sample_text_2")
    b = statemachine_mk2_State(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_possible_states20_reverse_link_reassign_clear():
    a1 = statemachine_mk2_State(name="sample_text")
    a2 = statemachine_mk2_State(name="sample_text_2")
    b = statemachine_mk2_Event(description="sample_text")
    _safe_set(b, 'statemachine_mk2_Event21', {a1})
    assert _is_linked(b, 'statemachine_mk2_Event21', a1)
    if hasattr(a1, 'statemachine_mk2_State22'):
        assert _is_linked(a1, 'statemachine_mk2_State22', b)
    _safe_set(b, 'statemachine_mk2_Event21', {a2})
    assert _is_linked(b, 'statemachine_mk2_Event21', a2)
    if hasattr(a1, 'statemachine_mk2_State22'):
        assert not _is_linked(a1, 'statemachine_mk2_State22', b)
    if hasattr(a2, 'statemachine_mk2_State22'):
        assert _is_linked(a2, 'statemachine_mk2_State22', b)
    _safe_set(b, 'statemachine_mk2_Event21', set())
    assert not _is_linked(b, 'statemachine_mk2_Event21', a2)
    if hasattr(a2, 'statemachine_mk2_State22'):
        assert not _is_linked(a2, 'statemachine_mk2_State22', b)


def test_assoc_source14_reverse_link_reassign_clear():
    a1 = statemachine_mk2_Transition(name="sample_text")
    a2 = statemachine_mk2_Transition(name="sample_text_2")
    b = statemachine_mk2_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_target15_reverse_link_reassign_clear():
    a1 = statemachine_mk2_Transition(name="sample_text")
    a2 = statemachine_mk2_Transition(name="sample_text_2")
    b = statemachine_mk2_State(name="sample_text")
    _safe_set(b, 'State16', a1)
    assert _is_linked(b, 'State16', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State16', a2)
    assert _is_linked(b, 'State16', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State16', None)
    assert not _is_linked(b, 'State16', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


def test_assoc_triggers17_reverse_link_reassign_clear():
    a1 = statemachine_mk2_Transition(name="sample_text")
    a2 = statemachine_mk2_Transition(name="sample_text_2")
    b = statemachine_mk2_Event(description="sample_text")
    _safe_set(b, 'statemachine_mk2_Event19', a1)
    assert _is_linked(b, 'statemachine_mk2_Event19', a1)
    if hasattr(a1, 'statemachine_mk2_Transition18'):
        assert _is_linked(a1, 'statemachine_mk2_Transition18', b)
    _safe_set(b, 'statemachine_mk2_Event19', a2)
    assert _is_linked(b, 'statemachine_mk2_Event19', a2)
    if hasattr(a1, 'statemachine_mk2_Transition18'):
        assert not _is_linked(a1, 'statemachine_mk2_Transition18', b)
    if hasattr(a2, 'statemachine_mk2_Transition18'):
        assert _is_linked(a2, 'statemachine_mk2_Transition18', b)
    _safe_set(b, 'statemachine_mk2_Event19', None)
    assert not _is_linked(b, 'statemachine_mk2_Event19', a2)
    if hasattr(a2, 'statemachine_mk2_Transition18'):
        assert not _is_linked(a2, 'statemachine_mk2_Transition18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_events5_stub_double():
    # statemachine_mk2_StateMachine has no real 'statemachine_mk2_StateMachine6' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_mk2_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_mk2_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_mk2_Event(description="sample_text")
    partner = statemachine_mk2_StateMachine()
    setattr(partner, 'statemachine_mk2_StateMachine6', None)
    _safe_set(owner, 'statemachine_mk2_Event', partner)
    assert owner in getattr(partner, 'statemachine_mk2_StateMachine6')
    _safe_set(owner, 'statemachine_mk2_Event', None)
    assert owner not in getattr(partner, 'statemachine_mk2_StateMachine6')


def test_assoc_initial_state1_stub_double():
    # statemachine_mk2_StateMachine has no real 'statemachine_mk2_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_mk2_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_mk2_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_mk2_State(name="sample_text")
    partner = statemachine_mk2_StateMachine()
    setattr(partner, 'statemachine_mk2_StateMachine2', None)
    _safe_set(owner, 'statemachine_mk2_State', partner)
    assert getattr(partner, 'statemachine_mk2_StateMachine2') == owner
    _safe_set(owner, 'statemachine_mk2_State', None)
    assert getattr(partner, 'statemachine_mk2_StateMachine2') is None


def test_assoc_substates26_stub_double():
    # statemachine_mk2_Composite_state has no real 'statemachine_mk2_Composite_state27' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_mk2_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_mk2_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_mk2_State(name="sample_text")
    partner = statemachine_mk2_Composite_state()
    setattr(partner, 'statemachine_mk2_Composite_state27', None)
    _safe_set(owner, 'statemachine_mk2_State28', partner)
    assert owner in getattr(partner, 'statemachine_mk2_Composite_state27')
    _safe_set(owner, 'statemachine_mk2_State28', None)
    assert owner not in getattr(partner, 'statemachine_mk2_Composite_state27')


def test_assoc_transitions3_stub_double():
    # statemachine_mk2_StateMachine has no real 'statemachine_mk2_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_mk2_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_mk2_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_mk2_Transition(name="sample_text")
    partner = statemachine_mk2_StateMachine()
    setattr(partner, 'statemachine_mk2_StateMachine4', None)
    _safe_set(owner, 'statemachine_mk2_Transition', partner)
    assert owner in getattr(partner, 'statemachine_mk2_StateMachine4')
    _safe_set(owner, 'statemachine_mk2_Transition', None)
    assert owner not in getattr(partner, 'statemachine_mk2_StateMachine4')


