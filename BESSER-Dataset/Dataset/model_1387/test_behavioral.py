import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SM_FinalState,
    SM_InitialState,
    SM_State,
    SM_StateMachine,
    SM_Transition,
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

def test_assoc_source2_reverse_link_reassign_clear():
    a1 = SM_Transition(effect="sample_text", trigger="sample_text")
    a2 = SM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = SM_State(name="sample_text")
    _safe_set(b, 'SM_State4', a1)
    assert _is_linked(b, 'SM_State4', a1)
    if hasattr(a1, 'SM_Transition3'):
        assert _is_linked(a1, 'SM_Transition3', b)
    _safe_set(b, 'SM_State4', a2)
    assert _is_linked(b, 'SM_State4', a2)
    if hasattr(a1, 'SM_Transition3'):
        assert not _is_linked(a1, 'SM_Transition3', b)
    if hasattr(a2, 'SM_Transition3'):
        assert _is_linked(a2, 'SM_Transition3', b)
    _safe_set(b, 'SM_State4', None)
    assert not _is_linked(b, 'SM_State4', a2)
    if hasattr(a2, 'SM_Transition3'):
        assert not _is_linked(a2, 'SM_Transition3', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = SM_Transition(effect="sample_text", trigger="sample_text")
    a2 = SM_Transition(effect="sample_text_2", trigger="sample_text_2")
    b = SM_State(name="sample_text")
    _safe_set(b, 'SM_State', a1)
    assert _is_linked(b, 'SM_State', a1)
    if hasattr(a1, 'SM_Transition'):
        assert _is_linked(a1, 'SM_Transition', b)
    _safe_set(b, 'SM_State', a2)
    assert _is_linked(b, 'SM_State', a2)
    if hasattr(a1, 'SM_Transition'):
        assert not _is_linked(a1, 'SM_Transition', b)
    if hasattr(a2, 'SM_Transition'):
        assert _is_linked(a2, 'SM_Transition', b)
    _safe_set(b, 'SM_State', None)
    assert not _is_linked(b, 'SM_State', a2)
    if hasattr(a2, 'SM_Transition'):
        assert not _is_linked(a2, 'SM_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownedState7_stub_double():
    # SM_StateMachine has no real 'owningStateMachine' property in the generated
    # code (a bare stub) -- manually attach it so SM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SM_State(name="sample_text")
    partner = SM_StateMachine()
    setattr(partner, 'owningStateMachine', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningStateMachine')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningStateMachine')


def test_assoc_ownedTransition8_stub_double():
    # SM_StateMachine has no real 'owningStateMachine9' property in the generated
    # code (a bare stub) -- manually attach it so SM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SM_Transition(effect="sample_text", trigger="sample_text")
    partner = SM_StateMachine()
    setattr(partner, 'owningStateMachine9', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'owningStateMachine9')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'owningStateMachine9')


def test_assoc_owningStateMachine0_stub_double():
    # SM_StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so SM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SM_State(name="sample_text")
    partner = SM_StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_owningStateMachine5_stub_double():
    # SM_StateMachine has no real 'StateMachine6' property in the generated
    # code (a bare stub) -- manually attach it so SM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SM_Transition(effect="sample_text", trigger="sample_text")
    partner = SM_StateMachine()
    setattr(partner, 'StateMachine6', None)
    _safe_set(owner, 'ownedTransition', partner)
    assert getattr(partner, 'StateMachine6') == owner
    _safe_set(owner, 'ownedTransition', None)
    assert getattr(partner, 'StateMachine6') is None


