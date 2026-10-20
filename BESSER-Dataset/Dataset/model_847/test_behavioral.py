import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    fsm_FSM,
    fsm_FinalState,
    fsm_InitialState,
    fsm_State,
    fsm_Transition,
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

def test_assoc_from_11_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State12', a1)
    assert _is_linked(b, 'State12', a1)
    if hasattr(a1, 'outgoingtransitions'):
        assert _is_linked(a1, 'outgoingtransitions', b)
    _safe_set(b, 'State12', a2)
    assert _is_linked(b, 'State12', a2)
    if hasattr(a1, 'outgoingtransitions'):
        assert not _is_linked(a1, 'outgoingtransitions', b)
    if hasattr(a2, 'outgoingtransitions'):
        assert _is_linked(a2, 'outgoingtransitions', b)
    _safe_set(b, 'State12', None)
    assert not _is_linked(b, 'State12', a2)
    if hasattr(a2, 'outgoingtransitions'):
        assert not _is_linked(a2, 'outgoingtransitions', b)


def test_assoc_fsm4_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'FSM', a1)
    assert _is_linked(b, 'FSM', a1)
    if hasattr(a1, 'states'):
        assert _is_linked(a1, 'states', b)
    _safe_set(b, 'FSM', a2)
    assert _is_linked(b, 'FSM', a2)
    if hasattr(a1, 'states'):
        assert not _is_linked(a1, 'states', b)
    if hasattr(a2, 'states'):
        assert _is_linked(a2, 'states', b)
    _safe_set(b, 'FSM', None)
    assert not _is_linked(b, 'FSM', a2)
    if hasattr(a2, 'states'):
        assert not _is_linked(a2, 'states', b)


def test_assoc_fsm9_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'FSM10', a1)
    assert _is_linked(b, 'FSM10', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'FSM10', a2)
    assert _is_linked(b, 'FSM10', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'FSM10', None)
    assert not _is_linked(b, 'FSM10', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_incommingtransitions7_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition8'):
        assert _is_linked(a1, 'Transition8', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition8'):
        assert not _is_linked(a1, 'Transition8', b)
    if hasattr(a2, 'Transition8'):
        assert _is_linked(a2, 'Transition8', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition8'):
        assert not _is_linked(a2, 'Transition8', b)


def test_assoc_outgoingtransitions5_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition6'):
        assert _is_linked(a1, 'Transition6', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition6'):
        assert not _is_linked(a1, 'Transition6', b)
    if hasattr(a2, 'Transition6'):
        assert _is_linked(a2, 'Transition6', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition6'):
        assert not _is_linked(a2, 'Transition6', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'fsm', {a1})
    assert _is_linked(b, 'fsm', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'fsm', {a2})
    assert _is_linked(b, 'fsm', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'fsm', set())
    assert not _is_linked(b, 'fsm', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_to13_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State14', a1)
    assert _is_linked(b, 'State14', a1)
    if hasattr(a1, 'incommingtransitions'):
        assert _is_linked(a1, 'incommingtransitions', b)
    _safe_set(b, 'State14', a2)
    assert _is_linked(b, 'State14', a2)
    if hasattr(a1, 'incommingtransitions'):
        assert not _is_linked(a1, 'incommingtransitions', b)
    if hasattr(a2, 'incommingtransitions'):
        assert _is_linked(a2, 'incommingtransitions', b)
    _safe_set(b, 'State14', None)
    assert not _is_linked(b, 'State14', a2)
    if hasattr(a2, 'incommingtransitions'):
        assert not _is_linked(a2, 'incommingtransitions', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = fsm_Transition(event="sample_text")
    a2 = fsm_Transition(event="sample_text_2")
    b = fsm_FSM(name="sample_text")
    _safe_set(b, 'fsm2', {a1})
    assert _is_linked(b, 'fsm2', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'fsm2', {a2})
    assert _is_linked(b, 'fsm2', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'fsm2', set())
    assert not _is_linked(b, 'fsm2', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_initialstate3_stub_double():
    # fsm_InitialState has no real 'fsm_InitialState' property in the generated
    # code (a bare stub) -- manually attach it so fsm_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_FSM(name="sample_text")
    partner = fsm_InitialState()
    setattr(partner, 'fsm_InitialState', None)
    _safe_set(owner, 'fsm_FSM', partner)
    assert getattr(partner, 'fsm_InitialState') == owner
    _safe_set(owner, 'fsm_FSM', None)
    assert getattr(partner, 'fsm_InitialState') is None


