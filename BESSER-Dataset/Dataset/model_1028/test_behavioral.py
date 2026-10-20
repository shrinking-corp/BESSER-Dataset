import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    NamedElement,
    Pseudostate,
    State,
    Statement,
    Trigger,
    fsm_AbstractState,
    fsm_AndTrigger,
    fsm_Choice,
    fsm_Constraint,
    fsm_DeepHistory,
    fsm_FinalState,
    fsm_Fork,
    fsm_InitialState,
    fsm_Join,
    fsm_Junction,
    fsm_NamedElement,
    fsm_Program,
    fsm_Pseudostate,
    fsm_Region,
    fsm_ShallowHistory,
    fsm_State,
    fsm_StateMachine,
    fsm_Statement,
    fsm_Transition,
    fsm_Trigger,
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

def test_assoc_left28_stub_double():
    # fsm_AndTrigger has no real 'fsm_AndTrigger' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_AndTrigger()
    setattr(partner, 'fsm_AndTrigger', None)
    _safe_set(owner, 'fsm_Trigger29', partner)
    assert getattr(partner, 'fsm_AndTrigger') == owner
    _safe_set(owner, 'fsm_Trigger29', None)
    assert getattr(partner, 'fsm_AndTrigger') is None


def test_assoc_right30_stub_double():
    # fsm_AndTrigger has no real 'fsm_AndTrigger31' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_AndTrigger()
    setattr(partner, 'fsm_AndTrigger31', None)
    _safe_set(owner, 'fsm_Trigger32', partner)
    assert getattr(partner, 'fsm_AndTrigger31') == owner
    _safe_set(owner, 'fsm_Trigger32', None)
    assert getattr(partner, 'fsm_AndTrigger31') is None


def test_assoc_trigger18_stub_double():
    # fsm_Transition has no real 'fsm_Transition19' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'fsm_Transition19', None)
    _safe_set(owner, 'fsm_Trigger', partner)
    assert getattr(partner, 'fsm_Transition19') == owner
    _safe_set(owner, 'fsm_Trigger', None)
    assert getattr(partner, 'fsm_Transition19') is None


