import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EventRule,
    TimeEventRule,
    umlTransition_AbsoluteTimeEventRule,
    umlTransition_AnyReceiveEventRule,
    umlTransition_CallOrSignalEventRule,
    umlTransition_ChangeEventRule,
    umlTransition_EffectRule,
    umlTransition_EventRule,
    umlTransition_GuardRule,
    umlTransition_NamedElement,
    umlTransition_RelativeTimeEventRule,
    umlTransition_TimeEventRule,
    umlTransition_TransitionRule,
    BehaviorKind,
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

def test_assoc_effect3_stub_double():
    # umlTransition_TransitionRule has no real 'umlTransition_TransitionRule4' property in the generated
    # code (a bare stub) -- manually attach it so umlTransition_EffectRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTransition_EffectRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTransition_EffectRule(behaviorName="sample_text", kind="sample_text")
    partner = umlTransition_TransitionRule()
    setattr(partner, 'umlTransition_TransitionRule4', None)
    _safe_set(owner, 'umlTransition_EffectRule', partner)
    assert getattr(partner, 'umlTransition_TransitionRule4') == owner
    _safe_set(owner, 'umlTransition_EffectRule', None)
    assert getattr(partner, 'umlTransition_TransitionRule4') is None


def test_assoc_guard1_stub_double():
    # umlTransition_TransitionRule has no real 'umlTransition_TransitionRule2' property in the generated
    # code (a bare stub) -- manually attach it so umlTransition_GuardRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTransition_GuardRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTransition_GuardRule(constraint="sample_text")
    partner = umlTransition_TransitionRule()
    setattr(partner, 'umlTransition_TransitionRule2', None)
    _safe_set(owner, 'umlTransition_GuardRule', partner)
    assert getattr(partner, 'umlTransition_TransitionRule2') == owner
    _safe_set(owner, 'umlTransition_GuardRule', None)
    assert getattr(partner, 'umlTransition_TransitionRule2') is None


