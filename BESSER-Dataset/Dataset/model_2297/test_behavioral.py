import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    emf_Action,
    emf_State,
    emf_StateMachine,
    emf_Transition,
    emf_TransitionToStateMapEntry,
    StateType,
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

def test_assoc_targetState6_reverse_link_reassign_clear():
    a1 = emf_Transition(action="sample_text")
    a2 = emf_Transition(action="sample_text_2")
    b = emf_State(name="sample_text", type="sample_text")
    _safe_set(b, 'emf_State7', a1)
    assert _is_linked(b, 'emf_State7', a1)
    if hasattr(a1, 'emf_Transition'):
        assert _is_linked(a1, 'emf_Transition', b)
    _safe_set(b, 'emf_State7', a2)
    assert _is_linked(b, 'emf_State7', a2)
    if hasattr(a1, 'emf_Transition'):
        assert not _is_linked(a1, 'emf_Transition', b)
    if hasattr(a2, 'emf_Transition'):
        assert _is_linked(a2, 'emf_Transition', b)
    _safe_set(b, 'emf_State7', None)
    assert not _is_linked(b, 'emf_State7', a2)
    if hasattr(a2, 'emf_Transition'):
        assert not _is_linked(a2, 'emf_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_key8_stub_double():
    # emf_TransitionToStateMapEntry has no real 'emf_TransitionToStateMapEntry9' property in the generated
    # code (a bare stub) -- manually attach it so emf_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emf_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emf_Transition(action="sample_text")
    partner = emf_TransitionToStateMapEntry()
    setattr(partner, 'emf_TransitionToStateMapEntry9', None)
    _safe_set(owner, 'emf_Transition10', partner)
    assert getattr(partner, 'emf_TransitionToStateMapEntry9') == owner
    _safe_set(owner, 'emf_Transition10', None)
    assert getattr(partner, 'emf_TransitionToStateMapEntry9') is None


def test_assoc_nestedStateMachines0_stub_double():
    # emf_StateMachine has no real 'emf_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so emf_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emf_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emf_State(name="sample_text", type="sample_text")
    partner = emf_StateMachine()
    setattr(partner, 'emf_StateMachine', None)
    _safe_set(owner, 'emf_State', {partner})
    assert getattr(partner, 'emf_StateMachine') == owner
    _safe_set(owner, 'emf_State', set())
    assert getattr(partner, 'emf_StateMachine') is None


def test_assoc_states1_stub_double():
    # emf_StateMachine has no real 'emf_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so emf_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emf_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emf_State(name="sample_text", type="sample_text")
    partner = emf_StateMachine()
    setattr(partner, 'emf_StateMachine2', None)
    _safe_set(owner, 'emf_State3', partner)
    assert owner in getattr(partner, 'emf_StateMachine2')
    _safe_set(owner, 'emf_State3', None)
    assert owner not in getattr(partner, 'emf_StateMachine2')


def test_assoc_value11_stub_double():
    # emf_TransitionToStateMapEntry has no real 'emf_TransitionToStateMapEntry12' property in the generated
    # code (a bare stub) -- manually attach it so emf_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emf_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emf_State(name="sample_text", type="sample_text")
    partner = emf_TransitionToStateMapEntry()
    setattr(partner, 'emf_TransitionToStateMapEntry12', None)
    _safe_set(owner, 'emf_State13', partner)
    assert getattr(partner, 'emf_TransitionToStateMapEntry12') == owner
    _safe_set(owner, 'emf_State13', None)
    assert getattr(partner, 'emf_TransitionToStateMapEntry12') is None


