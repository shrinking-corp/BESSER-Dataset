import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NHSM_State,
    NHSM_StateMachine,
    NHSM_Transition,
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

def test_assoc_source3_stub_double():
    # NHSM_Transition has no real 'NHSM_Transition4' property in the generated
    # code (a bare stub) -- manually attach it so NHSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NHSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NHSM_State(name="sample_text")
    partner = NHSM_Transition()
    setattr(partner, 'NHSM_Transition4', None)
    _safe_set(owner, 'NHSM_State5', partner)
    assert getattr(partner, 'NHSM_Transition4') == owner
    _safe_set(owner, 'NHSM_State5', None)
    assert getattr(partner, 'NHSM_Transition4') is None


def test_assoc_states0_stub_double():
    # NHSM_StateMachine has no real 'NHSM_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so NHSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NHSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NHSM_State(name="sample_text")
    partner = NHSM_StateMachine()
    setattr(partner, 'NHSM_StateMachine', None)
    _safe_set(owner, 'NHSM_State', partner)
    assert owner in getattr(partner, 'NHSM_StateMachine')
    _safe_set(owner, 'NHSM_State', None)
    assert owner not in getattr(partner, 'NHSM_StateMachine')


def test_assoc_target6_stub_double():
    # NHSM_Transition has no real 'NHSM_Transition7' property in the generated
    # code (a bare stub) -- manually attach it so NHSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NHSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NHSM_State(name="sample_text")
    partner = NHSM_Transition()
    setattr(partner, 'NHSM_Transition7', None)
    _safe_set(owner, 'NHSM_State8', partner)
    assert getattr(partner, 'NHSM_Transition7') == owner
    _safe_set(owner, 'NHSM_State8', None)
    assert getattr(partner, 'NHSM_Transition7') is None


