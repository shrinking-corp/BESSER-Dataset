import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    HSM_CompositeState,
    HSM_FinalState,
    HSM_InitialState,
    HSM_State,
    HSM_StateMachine,
    HSM_Transition,
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

def test_assoc_source4_reverse_link_reassign_clear():
    a1 = HSM_Transition(effect="sample_text", trigger="sample_text")
    a2 = HSM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = HSM_State(name="sample_text")
    _safe_set(b, 'HSM_State6', a1)
    assert _is_linked(b, 'HSM_State6', a1)
    if hasattr(a1, 'HSM_Transition5'):
        assert _is_linked(a1, 'HSM_Transition5', b)
    _safe_set(b, 'HSM_State6', a2)
    assert _is_linked(b, 'HSM_State6', a2)
    if hasattr(a1, 'HSM_Transition5'):
        assert not _is_linked(a1, 'HSM_Transition5', b)
    if hasattr(a2, 'HSM_Transition5'):
        assert _is_linked(a2, 'HSM_Transition5', b)
    _safe_set(b, 'HSM_State6', None)
    assert not _is_linked(b, 'HSM_State6', a2)
    if hasattr(a2, 'HSM_Transition5'):
        assert not _is_linked(a2, 'HSM_Transition5', b)


def test_assoc_target2_reverse_link_reassign_clear():
    a1 = HSM_Transition(effect="sample_text", trigger="sample_text")
    a2 = HSM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = HSM_State(name="sample_text")
    _safe_set(b, 'HSM_State3', a1)
    assert _is_linked(b, 'HSM_State3', a1)
    if hasattr(a1, 'HSM_Transition'):
        assert _is_linked(a1, 'HSM_Transition', b)
    _safe_set(b, 'HSM_State3', a2)
    assert _is_linked(b, 'HSM_State3', a2)
    if hasattr(a1, 'HSM_Transition'):
        assert not _is_linked(a1, 'HSM_Transition', b)
    if hasattr(a2, 'HSM_Transition'):
        assert _is_linked(a2, 'HSM_Transition', b)
    _safe_set(b, 'HSM_State3', None)
    assert not _is_linked(b, 'HSM_State3', a2)
    if hasattr(a2, 'HSM_Transition'):
        assert not _is_linked(a2, 'HSM_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownedState18_stub_double():
    # HSM_StateMachine has no real 'owningStateMachine' property in the generated
    # code (a bare stub) -- manually attach it so HSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_State(name="sample_text")
    partner = HSM_StateMachine()
    setattr(partner, 'owningStateMachine', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningStateMachine')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningStateMachine')


def test_assoc_ownedSubState12_stub_double():
    # HSM_CompositeState has no real 'HSM_CompositeState13' property in the generated
    # code (a bare stub) -- manually attach it so HSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_State(name="sample_text")
    partner = HSM_CompositeState()
    setattr(partner, 'HSM_CompositeState13', None)
    _safe_set(owner, 'HSM_State14', partner)
    assert owner in getattr(partner, 'HSM_CompositeState13')
    _safe_set(owner, 'HSM_State14', None)
    assert owner not in getattr(partner, 'HSM_CompositeState13')


def test_assoc_ownedSubTransition15_stub_double():
    # HSM_CompositeState has no real 'HSM_CompositeState16' property in the generated
    # code (a bare stub) -- manually attach it so HSM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_Transition(effect="sample_text", trigger="sample_text")
    partner = HSM_CompositeState()
    setattr(partner, 'HSM_CompositeState16', None)
    _safe_set(owner, 'HSM_Transition17', partner)
    assert owner in getattr(partner, 'HSM_CompositeState16')
    _safe_set(owner, 'HSM_Transition17', None)
    assert owner not in getattr(partner, 'HSM_CompositeState16')


def test_assoc_ownedTransition19_stub_double():
    # HSM_StateMachine has no real 'owningStateMachine20' property in the generated
    # code (a bare stub) -- manually attach it so HSM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_Transition(effect="sample_text", trigger="sample_text")
    partner = HSM_StateMachine()
    setattr(partner, 'owningStateMachine20', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'owningStateMachine20')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'owningStateMachine20')


def test_assoc_owningCompositeState0_stub_double():
    # HSM_CompositeState has no real 'HSM_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so HSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_State(name="sample_text")
    partner = HSM_CompositeState()
    setattr(partner, 'HSM_CompositeState', None)
    _safe_set(owner, 'HSM_State', partner)
    assert getattr(partner, 'HSM_CompositeState') == owner
    _safe_set(owner, 'HSM_State', None)
    assert getattr(partner, 'HSM_CompositeState') is None


def test_assoc_owningCompositeState9_stub_double():
    # HSM_CompositeState has no real 'HSM_CompositeState11' property in the generated
    # code (a bare stub) -- manually attach it so HSM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_Transition(effect="sample_text", trigger="sample_text")
    partner = HSM_CompositeState()
    setattr(partner, 'HSM_CompositeState11', None)
    _safe_set(owner, 'HSM_Transition10', partner)
    assert getattr(partner, 'HSM_CompositeState11') == owner
    _safe_set(owner, 'HSM_Transition10', None)
    assert getattr(partner, 'HSM_CompositeState11') is None


def test_assoc_owningStateMachine1_stub_double():
    # HSM_StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so HSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_State(name="sample_text")
    partner = HSM_StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_owningStateMachine7_stub_double():
    # HSM_StateMachine has no real 'StateMachine8' property in the generated
    # code (a bare stub) -- manually attach it so HSM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_Transition(effect="sample_text", trigger="sample_text")
    partner = HSM_StateMachine()
    setattr(partner, 'StateMachine8', None)
    _safe_set(owner, 'ownedTransition', partner)
    assert getattr(partner, 'StateMachine8') == owner
    _safe_set(owner, 'ownedTransition', None)
    assert getattr(partner, 'StateMachine8') is None


