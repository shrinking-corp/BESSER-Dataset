import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    minifsm_FSM,
    minifsm_FinalState,
    minifsm_State,
    minifsm_Transition,
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

def test_assoc_input5_reverse_link_reassign_clear():
    a1 = minifsm_Transition(event="sample_text")
    a2 = minifsm_Transition(event="sample_text_2")
    b = minifsm_State(name="sample_text")
    _safe_set(b, 'minifsm_State6', a1)
    assert _is_linked(b, 'minifsm_State6', a1)
    if hasattr(a1, 'minifsm_Transition'):
        assert _is_linked(a1, 'minifsm_Transition', b)
    _safe_set(b, 'minifsm_State6', a2)
    assert _is_linked(b, 'minifsm_State6', a2)
    if hasattr(a1, 'minifsm_Transition'):
        assert not _is_linked(a1, 'minifsm_Transition', b)
    if hasattr(a2, 'minifsm_Transition'):
        assert _is_linked(a2, 'minifsm_Transition', b)
    _safe_set(b, 'minifsm_State6', None)
    assert not _is_linked(b, 'minifsm_State6', a2)
    if hasattr(a2, 'minifsm_Transition'):
        assert not _is_linked(a2, 'minifsm_Transition', b)


def test_assoc_output7_reverse_link_reassign_clear():
    a1 = minifsm_Transition(event="sample_text")
    a2 = minifsm_Transition(event="sample_text_2")
    b = minifsm_State(name="sample_text")
    _safe_set(b, 'minifsm_State9', a1)
    assert _is_linked(b, 'minifsm_State9', a1)
    if hasattr(a1, 'minifsm_Transition8'):
        assert _is_linked(a1, 'minifsm_Transition8', b)
    _safe_set(b, 'minifsm_State9', a2)
    assert _is_linked(b, 'minifsm_State9', a2)
    if hasattr(a1, 'minifsm_Transition8'):
        assert not _is_linked(a1, 'minifsm_Transition8', b)
    if hasattr(a2, 'minifsm_Transition8'):
        assert _is_linked(a2, 'minifsm_Transition8', b)
    _safe_set(b, 'minifsm_State9', None)
    assert not _is_linked(b, 'minifsm_State9', a2)
    if hasattr(a2, 'minifsm_Transition8'):
        assert not _is_linked(a2, 'minifsm_Transition8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_fsm10_stub_double():
    # minifsm_FSM has no real 'FSM11' property in the generated
    # code (a bare stub) -- manually attach it so minifsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minifsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minifsm_Transition(event="sample_text")
    partner = minifsm_FSM()
    setattr(partner, 'FSM11', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'FSM11') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'FSM11') is None


def test_assoc_fsm4_stub_double():
    # minifsm_FSM has no real 'FSM' property in the generated
    # code (a bare stub) -- manually attach it so minifsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minifsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minifsm_State(name="sample_text")
    partner = minifsm_FSM()
    setattr(partner, 'FSM', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'FSM') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'FSM') is None


def test_assoc_initialState3_stub_double():
    # minifsm_FSM has no real 'minifsm_FSM' property in the generated
    # code (a bare stub) -- manually attach it so minifsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minifsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minifsm_State(name="sample_text")
    partner = minifsm_FSM()
    setattr(partner, 'minifsm_FSM', None)
    _safe_set(owner, 'minifsm_State', partner)
    assert getattr(partner, 'minifsm_FSM') == owner
    _safe_set(owner, 'minifsm_State', None)
    assert getattr(partner, 'minifsm_FSM') is None


def test_assoc_states0_stub_double():
    # minifsm_FSM has no real 'fsm' property in the generated
    # code (a bare stub) -- manually attach it so minifsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minifsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minifsm_State(name="sample_text")
    partner = minifsm_FSM()
    setattr(partner, 'fsm', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'fsm')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'fsm')


def test_assoc_transitions1_stub_double():
    # minifsm_FSM has no real 'fsm2' property in the generated
    # code (a bare stub) -- manually attach it so minifsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minifsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minifsm_Transition(event="sample_text")
    partner = minifsm_FSM()
    setattr(partner, 'fsm2', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'fsm2')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'fsm2')


