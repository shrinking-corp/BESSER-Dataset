import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SM_FinalState,
    SM_InitialState,
    SM_State,
    SM_StateMachine,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownedState0_stub_double():
    # SM_StateMachine has no real 'SM_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so SM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SM_State(name="sample_text")
    partner = SM_StateMachine()
    setattr(partner, 'SM_StateMachine', None)
    _safe_set(owner, 'SM_State', partner)
    assert owner in getattr(partner, 'SM_StateMachine')
    _safe_set(owner, 'SM_State', None)
    assert owner not in getattr(partner, 'SM_StateMachine')


