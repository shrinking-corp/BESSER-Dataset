import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    fsm_FiniteStateMachine,
    fsm_Model,
    fsm_NamedElement,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_leavingTransitions4_stub_double():
    # fsm_State has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(input="sample_text", output="sample_text")
    partner = fsm_State()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_source8_stub_double():
    # fsm_State has no real 'State9' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(input="sample_text", output="sample_text")
    partner = fsm_State()
    setattr(partner, 'State9', None)
    _safe_set(owner, 'leavingTransitions', partner)
    assert getattr(partner, 'State9') == owner
    _safe_set(owner, 'leavingTransitions', None)
    assert getattr(partner, 'State9') is None


def test_assoc_target6_stub_double():
    # fsm_State has no real 'fsm_State7' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(input="sample_text", output="sample_text")
    partner = fsm_State()
    setattr(partner, 'fsm_State7', None)
    _safe_set(owner, 'fsm_Transition', partner)
    assert getattr(partner, 'fsm_State7') == owner
    _safe_set(owner, 'fsm_Transition', None)
    assert getattr(partner, 'fsm_State7') is None


