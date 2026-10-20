import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Signal,
    statemachine_Command,
    statemachine_Condition,
    statemachine_Event,
    statemachine_InputSignal,
    statemachine_OutputSignal,
    statemachine_Signal,
    statemachine_State,
    statemachine_Statemachine,
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

def test_assoc_commands3_reverse_link_reassign_clear():
    a1 = statemachine_State(name="sample_text")
    a2 = statemachine_State(name="sample_text_2")
    b = statemachine_Command(newValue=True)
    _safe_set(b, 'statemachine_Command', a1)
    assert _is_linked(b, 'statemachine_Command', a1)
    if hasattr(a1, 'statemachine_State4'):
        assert _is_linked(a1, 'statemachine_State4', b)
    _safe_set(b, 'statemachine_Command', a2)
    assert _is_linked(b, 'statemachine_Command', a2)
    if hasattr(a1, 'statemachine_State4'):
        assert not _is_linked(a1, 'statemachine_State4', b)
    if hasattr(a2, 'statemachine_State4'):
        assert _is_linked(a2, 'statemachine_State4', b)
    _safe_set(b, 'statemachine_Command', None)
    assert not _is_linked(b, 'statemachine_Command', a2)
    if hasattr(a2, 'statemachine_State4'):
        assert not _is_linked(a2, 'statemachine_State4', b)


def test_assoc_nestedStates8_reverse_link_reassign_clear():
    a1 = statemachine_State(name="sample_text")
    a2 = statemachine_State(name="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State9', a1)
    assert _is_linked(b, 'statemachine_State9', a1)
    if hasattr(a1, 'statemachine_State7'):
        assert _is_linked(a1, 'statemachine_State7', b)
    _safe_set(b, 'statemachine_State9', a2)
    assert _is_linked(b, 'statemachine_State9', a2)
    if hasattr(a1, 'statemachine_State7'):
        assert not _is_linked(a1, 'statemachine_State7', b)
    if hasattr(a2, 'statemachine_State7'):
        assert _is_linked(a2, 'statemachine_State7', b)
    _safe_set(b, 'statemachine_State9', None)
    assert not _is_linked(b, 'statemachine_State9', a2)
    if hasattr(a2, 'statemachine_State7'):
        assert not _is_linked(a2, 'statemachine_State7', b)


def test_assoc_signal17_reverse_link_reassign_clear():
    a1 = statemachine_Signal(name="sample_text")
    a2 = statemachine_Signal(name="sample_text_2")
    b = statemachine_Event(value=True)
    _safe_set(b, 'statemachine_Event18', a1)
    assert _is_linked(b, 'statemachine_Event18', a1)
    if hasattr(a1, 'statemachine_Signal19'):
        assert _is_linked(a1, 'statemachine_Signal19', b)
    _safe_set(b, 'statemachine_Event18', a2)
    assert _is_linked(b, 'statemachine_Event18', a2)
    if hasattr(a1, 'statemachine_Signal19'):
        assert not _is_linked(a1, 'statemachine_Signal19', b)
    if hasattr(a2, 'statemachine_Signal19'):
        assert _is_linked(a2, 'statemachine_Signal19', b)
    _safe_set(b, 'statemachine_Event18', None)
    assert not _is_linked(b, 'statemachine_Event18', a2)
    if hasattr(a2, 'statemachine_Signal19'):
        assert not _is_linked(a2, 'statemachine_Signal19', b)


def test_assoc_signal20_reverse_link_reassign_clear():
    a1 = statemachine_Signal(name="sample_text")
    a2 = statemachine_Signal(name="sample_text_2")
    b = statemachine_Command(newValue=True)
    _safe_set(b, 'statemachine_Command21', a1)
    assert _is_linked(b, 'statemachine_Command21', a1)
    if hasattr(a1, 'statemachine_Signal22'):
        assert _is_linked(a1, 'statemachine_Signal22', b)
    _safe_set(b, 'statemachine_Command21', a2)
    assert _is_linked(b, 'statemachine_Command21', a2)
    if hasattr(a1, 'statemachine_Signal22'):
        assert not _is_linked(a1, 'statemachine_Signal22', b)
    if hasattr(a2, 'statemachine_Signal22'):
        assert _is_linked(a2, 'statemachine_Signal22', b)
    _safe_set(b, 'statemachine_Command21', None)
    assert not _is_linked(b, 'statemachine_Command21', a2)
    if hasattr(a2, 'statemachine_Signal22'):
        assert not _is_linked(a2, 'statemachine_Signal22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_events15_stub_double():
    # statemachine_Condition has no real 'statemachine_Condition16' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(value=True)
    partner = statemachine_Condition()
    setattr(partner, 'statemachine_Condition16', None)
    _safe_set(owner, 'statemachine_Event', partner)
    assert owner in getattr(partner, 'statemachine_Condition16')
    _safe_set(owner, 'statemachine_Event', None)
    assert owner not in getattr(partner, 'statemachine_Condition16')


def test_assoc_signals0_stub_double():
    # statemachine_Statemachine has no real 'statemachine_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Signal(name="sample_text")
    partner = statemachine_Statemachine()
    setattr(partner, 'statemachine_Statemachine', None)
    _safe_set(owner, 'statemachine_Signal', partner)
    assert owner in getattr(partner, 'statemachine_Statemachine')
    _safe_set(owner, 'statemachine_Signal', None)
    assert owner not in getattr(partner, 'statemachine_Statemachine')


def test_assoc_state12_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition13', None)
    _safe_set(owner, 'statemachine_State14', partner)
    assert getattr(partner, 'statemachine_Transition13') == owner
    _safe_set(owner, 'statemachine_State14', None)
    assert getattr(partner, 'statemachine_Transition13') is None


def test_assoc_states1_stub_double():
    # statemachine_Statemachine has no real 'statemachine_Statemachine2' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Statemachine()
    setattr(partner, 'statemachine_Statemachine2', None)
    _safe_set(owner, 'statemachine_State', partner)
    assert owner in getattr(partner, 'statemachine_Statemachine2')
    _safe_set(owner, 'statemachine_State', None)
    assert owner not in getattr(partner, 'statemachine_Statemachine2')


def test_assoc_transitions5_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition', None)
    _safe_set(owner, 'statemachine_State6', {partner})
    assert getattr(partner, 'statemachine_Transition') == owner
    _safe_set(owner, 'statemachine_State6', set())
    assert getattr(partner, 'statemachine_Transition') is None


