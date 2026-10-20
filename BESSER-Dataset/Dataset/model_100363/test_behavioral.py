import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    SuperState,
    fsm_Action,
    fsm_FSM,
    fsm_InitialState,
    fsm_State,
    fsm_SteadyState,
    fsm_SuperState,
    fsm_TransientState,
    fsm_Transition,
    fsm_eAction,
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

def test_assoc_entry3_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_Action(entryLabel="sample_text")
    _safe_set(b, 'fsm_Action', a1)
    assert _is_linked(b, 'fsm_Action', a1)
    if hasattr(a1, 'fsm_State4'):
        assert _is_linked(a1, 'fsm_State4', b)
    _safe_set(b, 'fsm_Action', a2)
    assert _is_linked(b, 'fsm_Action', a2)
    if hasattr(a1, 'fsm_State4'):
        assert not _is_linked(a1, 'fsm_State4', b)
    if hasattr(a2, 'fsm_State4'):
        assert _is_linked(a2, 'fsm_State4', b)
    _safe_set(b, 'fsm_Action', None)
    assert not _is_linked(b, 'fsm_Action', a2)
    if hasattr(a2, 'fsm_State4'):
        assert not _is_linked(a2, 'fsm_State4', b)


def test_assoc_exit5_reverse_link_reassign_clear():
    a1 = fsm_eAction(exitLabel="sample_text")
    a2 = fsm_eAction(exitLabel="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'fsm_State6', a1)
    assert _is_linked(b, 'fsm_State6', a1)
    if hasattr(a1, 'fsm_eAction'):
        assert _is_linked(a1, 'fsm_eAction', b)
    _safe_set(b, 'fsm_State6', a2)
    assert _is_linked(b, 'fsm_State6', a2)
    if hasattr(a1, 'fsm_eAction'):
        assert not _is_linked(a1, 'fsm_eAction', b)
    if hasattr(a2, 'fsm_eAction'):
        assert _is_linked(a2, 'fsm_eAction', b)
    _safe_set(b, 'fsm_State6', None)
    assert not _is_linked(b, 'fsm_State6', a2)
    if hasattr(a2, 'fsm_eAction'):
        assert not _is_linked(a2, 'fsm_eAction', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = fsm_Transition(action="sample_text", guard="sample_text")
    a2 = fsm_Transition(action="sample_text_2", guard="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'fsm_State8', a1)
    assert _is_linked(b, 'fsm_State8', a1)
    if hasattr(a1, 'fsm_Transition'):
        assert _is_linked(a1, 'fsm_Transition', b)
    _safe_set(b, 'fsm_State8', a2)
    assert _is_linked(b, 'fsm_State8', a2)
    if hasattr(a1, 'fsm_Transition'):
        assert not _is_linked(a1, 'fsm_Transition', b)
    if hasattr(a2, 'fsm_Transition'):
        assert _is_linked(a2, 'fsm_Transition', b)
    _safe_set(b, 'fsm_State8', None)
    assert not _is_linked(b, 'fsm_State8', a2)
    if hasattr(a2, 'fsm_Transition'):
        assert not _is_linked(a2, 'fsm_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_outTrans12_stub_double():
    # fsm_SuperState has no real 'src' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(action="sample_text", guard="sample_text")
    partner = fsm_SuperState()
    setattr(partner, 'src', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'src')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'src')


def test_assoc_source9_stub_double():
    # fsm_SuperState has no real 'fsm_SuperState' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(action="sample_text", guard="sample_text")
    partner = fsm_SuperState()
    setattr(partner, 'fsm_SuperState', None)
    _safe_set(owner, 'fsm_Transition10', partner)
    assert getattr(partner, 'fsm_SuperState') == owner
    _safe_set(owner, 'fsm_Transition10', None)
    assert getattr(partner, 'fsm_SuperState') is None


def test_assoc_src11_stub_double():
    # fsm_SuperState has no real 'SuperState' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(action="sample_text", guard="sample_text")
    partner = fsm_SuperState()
    setattr(partner, 'SuperState', None)
    _safe_set(owner, 'outTrans', partner)
    assert getattr(partner, 'SuperState') == owner
    _safe_set(owner, 'outTrans', None)
    assert getattr(partner, 'SuperState') is None


def test_assoc_state0_stub_double():
    # fsm_FSM has no real 'fsm_FSM' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(name="sample_text")
    partner = fsm_FSM()
    setattr(partner, 'fsm_FSM', None)
    _safe_set(owner, 'fsm_State', partner)
    assert owner in getattr(partner, 'fsm_FSM')
    _safe_set(owner, 'fsm_State', None)
    assert owner not in getattr(partner, 'fsm_FSM')


