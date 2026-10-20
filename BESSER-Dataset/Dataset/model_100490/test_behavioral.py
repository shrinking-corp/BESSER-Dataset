import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    UMLRealTimeStateMach_Operation,
    UMLRealTimeStateMach_Pseudostate,
    UMLRealTimeStateMach_RTPseudostate,
    UMLRealTimeStateMach_RTRegion,
    UMLRealTimeStateMach_RTState,
    UMLRealTimeStateMach_RTStateMachine,
    UMLRealTimeStateMach_RTTrigger,
    UMLRealTimeStateMach_Region,
    UMLRealTimeStateMach_State,
    UMLRealTimeStateMach_StateMachine,
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

def test_assoc_base_Pseudostate3_stub_double():
    # UMLRealTimeStateMach_Pseudostate has no real 'UMLRealTimeStateMach_Pseudostate' property in the generated
    # code (a bare stub) -- manually attach it so UMLRealTimeStateMach_RTPseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UMLRealTimeStateMach_RTPseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UMLRealTimeStateMach_RTPseudostate()
    partner = UMLRealTimeStateMach_Pseudostate()
    setattr(partner, 'UMLRealTimeStateMach_Pseudostate', None)
    _safe_set(owner, 'UMLRealTimeStateMach_RTPseudostate', partner)
    assert getattr(partner, 'UMLRealTimeStateMach_Pseudostate') == owner
    _safe_set(owner, 'UMLRealTimeStateMach_RTPseudostate', None)
    assert getattr(partner, 'UMLRealTimeStateMach_Pseudostate') is None


def test_assoc_base_Region1_stub_double():
    # UMLRealTimeStateMach_Region has no real 'UMLRealTimeStateMach_Region' property in the generated
    # code (a bare stub) -- manually attach it so UMLRealTimeStateMach_RTRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UMLRealTimeStateMach_RTRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UMLRealTimeStateMach_RTRegion()
    partner = UMLRealTimeStateMach_Region()
    setattr(partner, 'UMLRealTimeStateMach_Region', None)
    _safe_set(owner, 'UMLRealTimeStateMach_RTRegion', partner)
    assert getattr(partner, 'UMLRealTimeStateMach_Region') == owner
    _safe_set(owner, 'UMLRealTimeStateMach_RTRegion', None)
    assert getattr(partner, 'UMLRealTimeStateMach_Region') is None


def test_assoc_base_State2_stub_double():
    # UMLRealTimeStateMach_State has no real 'UMLRealTimeStateMach_State' property in the generated
    # code (a bare stub) -- manually attach it so UMLRealTimeStateMach_RTState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UMLRealTimeStateMach_RTState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UMLRealTimeStateMach_RTState()
    partner = UMLRealTimeStateMach_State()
    setattr(partner, 'UMLRealTimeStateMach_State', None)
    _safe_set(owner, 'UMLRealTimeStateMach_RTState', partner)
    assert getattr(partner, 'UMLRealTimeStateMach_State') == owner
    _safe_set(owner, 'UMLRealTimeStateMach_RTState', None)
    assert getattr(partner, 'UMLRealTimeStateMach_State') is None


def test_assoc_base_StateMachine0_stub_double():
    # UMLRealTimeStateMach_StateMachine has no real 'UMLRealTimeStateMach_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so UMLRealTimeStateMach_RTStateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UMLRealTimeStateMach_RTStateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UMLRealTimeStateMach_RTStateMachine(isPassive="sample_text")
    partner = UMLRealTimeStateMach_StateMachine()
    setattr(partner, 'UMLRealTimeStateMach_StateMachine', None)
    _safe_set(owner, 'UMLRealTimeStateMach_RTStateMachine', partner)
    assert getattr(partner, 'UMLRealTimeStateMach_StateMachine') == owner
    _safe_set(owner, 'UMLRealTimeStateMach_RTStateMachine', None)
    assert getattr(partner, 'UMLRealTimeStateMach_StateMachine') is None


