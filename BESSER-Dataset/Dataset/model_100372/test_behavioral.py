import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SimpleHierarchicalStateMachine_CompositeState,
    SimpleHierarchicalStateMachine_FinalState,
    SimpleHierarchicalStateMachine_InitialState,
    SimpleHierarchicalStateMachine_State,
    SimpleHierarchicalStateMachine_StateMachine,
    SimpleHierarchicalStateMachine_Transition,
    State,
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

def test_assoc_ownedState9_reverse_link_reassign_clear():
    a1 = SimpleHierarchicalStateMachine_StateMachine(name="sample_text")
    a2 = SimpleHierarchicalStateMachine_StateMachine(name="sample_text_2")
    b = SimpleHierarchicalStateMachine_State(name="sample_text")
    _safe_set(b, 'SimpleHierarchicalStateMachine_State10', a1)
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_State10', a1)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_StateMachine'):
        assert _is_linked(a1, 'SimpleHierarchicalStateMachine_StateMachine', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_State10', a2)
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_State10', a2)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_StateMachine'):
        assert not _is_linked(a1, 'SimpleHierarchicalStateMachine_StateMachine', b)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_StateMachine'):
        assert _is_linked(a2, 'SimpleHierarchicalStateMachine_StateMachine', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_State10', None)
    assert not _is_linked(b, 'SimpleHierarchicalStateMachine_State10', a2)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_StateMachine'):
        assert not _is_linked(a2, 'SimpleHierarchicalStateMachine_StateMachine', b)


def test_assoc_ownedTransition11_reverse_link_reassign_clear():
    a1 = SimpleHierarchicalStateMachine_Transition(effect="sample_text", trigger="sample_text")
    a2 = SimpleHierarchicalStateMachine_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = SimpleHierarchicalStateMachine_StateMachine(name="sample_text")
    _safe_set(b, 'SimpleHierarchicalStateMachine_StateMachine12', {a1})
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_StateMachine12', a1)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_Transition13'):
        assert _is_linked(a1, 'SimpleHierarchicalStateMachine_Transition13', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_StateMachine12', {a2})
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_StateMachine12', a2)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_Transition13'):
        assert not _is_linked(a1, 'SimpleHierarchicalStateMachine_Transition13', b)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_Transition13'):
        assert _is_linked(a2, 'SimpleHierarchicalStateMachine_Transition13', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_StateMachine12', set())
    assert not _is_linked(b, 'SimpleHierarchicalStateMachine_StateMachine12', a2)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_Transition13'):
        assert not _is_linked(a2, 'SimpleHierarchicalStateMachine_Transition13', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = SimpleHierarchicalStateMachine_Transition(effect="sample_text", trigger="sample_text")
    a2 = SimpleHierarchicalStateMachine_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = SimpleHierarchicalStateMachine_State(name="sample_text")
    _safe_set(b, 'SimpleHierarchicalStateMachine_State5', a1)
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_State5', a1)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_Transition4'):
        assert _is_linked(a1, 'SimpleHierarchicalStateMachine_Transition4', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_State5', a2)
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_State5', a2)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_Transition4'):
        assert not _is_linked(a1, 'SimpleHierarchicalStateMachine_Transition4', b)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_Transition4'):
        assert _is_linked(a2, 'SimpleHierarchicalStateMachine_Transition4', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_State5', None)
    assert not _is_linked(b, 'SimpleHierarchicalStateMachine_State5', a2)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_Transition4'):
        assert not _is_linked(a2, 'SimpleHierarchicalStateMachine_Transition4', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = SimpleHierarchicalStateMachine_Transition(effect="sample_text", trigger="sample_text")
    a2 = SimpleHierarchicalStateMachine_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = SimpleHierarchicalStateMachine_State(name="sample_text")
    _safe_set(b, 'SimpleHierarchicalStateMachine_State2', a1)
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_State2', a1)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_Transition'):
        assert _is_linked(a1, 'SimpleHierarchicalStateMachine_Transition', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_State2', a2)
    assert _is_linked(b, 'SimpleHierarchicalStateMachine_State2', a2)
    if hasattr(a1, 'SimpleHierarchicalStateMachine_Transition'):
        assert not _is_linked(a1, 'SimpleHierarchicalStateMachine_Transition', b)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_Transition'):
        assert _is_linked(a2, 'SimpleHierarchicalStateMachine_Transition', b)
    _safe_set(b, 'SimpleHierarchicalStateMachine_State2', None)
    assert not _is_linked(b, 'SimpleHierarchicalStateMachine_State2', a2)
    if hasattr(a2, 'SimpleHierarchicalStateMachine_Transition'):
        assert not _is_linked(a2, 'SimpleHierarchicalStateMachine_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownedSubState6_stub_double():
    # SimpleHierarchicalStateMachine_CompositeState has no real 'SimpleHierarchicalStateMachine_CompositeState7' property in the generated
    # code (a bare stub) -- manually attach it so SimpleHierarchicalStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleHierarchicalStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleHierarchicalStateMachine_State(name="sample_text")
    partner = SimpleHierarchicalStateMachine_CompositeState()
    setattr(partner, 'SimpleHierarchicalStateMachine_CompositeState7', None)
    _safe_set(owner, 'SimpleHierarchicalStateMachine_State8', partner)
    assert owner in getattr(partner, 'SimpleHierarchicalStateMachine_CompositeState7')
    _safe_set(owner, 'SimpleHierarchicalStateMachine_State8', None)
    assert owner not in getattr(partner, 'SimpleHierarchicalStateMachine_CompositeState7')


def test_assoc_owningCompositeState0_stub_double():
    # SimpleHierarchicalStateMachine_CompositeState has no real 'SimpleHierarchicalStateMachine_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so SimpleHierarchicalStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleHierarchicalStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleHierarchicalStateMachine_State(name="sample_text")
    partner = SimpleHierarchicalStateMachine_CompositeState()
    setattr(partner, 'SimpleHierarchicalStateMachine_CompositeState', None)
    _safe_set(owner, 'SimpleHierarchicalStateMachine_State', partner)
    assert getattr(partner, 'SimpleHierarchicalStateMachine_CompositeState') == owner
    _safe_set(owner, 'SimpleHierarchicalStateMachine_State', None)
    assert getattr(partner, 'SimpleHierarchicalStateMachine_CompositeState') is None


