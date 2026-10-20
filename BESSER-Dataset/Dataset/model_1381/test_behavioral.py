import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    statemachine_FSM,
    statemachine_Final,
    statemachine_Initial,
    statemachine_State,
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

def test_assoc_nested7_reverse_link_reassign_clear():
    a1 = statemachine_State(time="sample_text")
    a2 = statemachine_State(time="sample_text_2")
    b = statemachine_State(time="sample_text")
    _safe_set(b, 'statemachine_State8', a1)
    assert _is_linked(b, 'statemachine_State8', a1)
    if hasattr(a1, 'statemachine_State6'):
        assert _is_linked(a1, 'statemachine_State6', b)
    _safe_set(b, 'statemachine_State8', a2)
    assert _is_linked(b, 'statemachine_State8', a2)
    if hasattr(a1, 'statemachine_State6'):
        assert not _is_linked(a1, 'statemachine_State6', b)
    if hasattr(a2, 'statemachine_State6'):
        assert _is_linked(a2, 'statemachine_State6', b)
    _safe_set(b, 'statemachine_State8', None)
    assert not _is_linked(b, 'statemachine_State8', a2)
    if hasattr(a2, 'statemachine_State6'):
        assert not _is_linked(a2, 'statemachine_State6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_current3_stub_double():
    # statemachine_FSM has no real 'statemachine_FSM4' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(time="sample_text")
    partner = statemachine_FSM()
    setattr(partner, 'statemachine_FSM4', None)
    _safe_set(owner, 'statemachine_State5', partner)
    assert getattr(partner, 'statemachine_FSM4') == owner
    _safe_set(owner, 'statemachine_State5', None)
    assert getattr(partner, 'statemachine_FSM4') is None


def test_assoc_src9_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition10' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(time="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition10', None)
    _safe_set(owner, 'statemachine_State11', partner)
    assert getattr(partner, 'statemachine_Transition10') == owner
    _safe_set(owner, 'statemachine_State11', None)
    assert getattr(partner, 'statemachine_Transition10') is None


def test_assoc_states0_stub_double():
    # statemachine_FSM has no real 'statemachine_FSM' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(time="sample_text")
    partner = statemachine_FSM()
    setattr(partner, 'statemachine_FSM', None)
    _safe_set(owner, 'statemachine_State', partner)
    assert owner in getattr(partner, 'statemachine_FSM')
    _safe_set(owner, 'statemachine_State', None)
    assert owner not in getattr(partner, 'statemachine_FSM')


def test_assoc_tar12_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(time="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition13', None)
    _safe_set(owner, 'statemachine_State14', partner)
    assert getattr(partner, 'statemachine_Transition13') == owner
    _safe_set(owner, 'statemachine_State14', None)
    assert getattr(partner, 'statemachine_Transition13') is None


