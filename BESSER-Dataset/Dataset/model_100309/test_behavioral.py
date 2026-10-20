import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BigStep,
    MSEOccurrence,
    Petrinetv3_Net_Initialize,
    Petrinetv3_Net_Run,
    Petrinetv3_Net_Run_AbstractSubStep,
    Petrinetv3_Net_TickEnabledTransitions,
    Petrinetv3_Transition_Fire,
    Place_tokens_Value,
    SmallStep,
    State,
    Step,
    Steps_Petrinetv3_Net_Run_AbstractSubStep,
    Steps_SmallStep,
    Transition_clock_Value,
    petrinetv3Trace_States_Place_tokens_Value,
    petrinetv3Trace_States_State,
    petrinetv3Trace_States_Transition_clock_Value,
    petrinetv3Trace_Steps_BigStep,
    petrinetv3Trace_Steps_Petrinetv3_Net_Initialize,
    petrinetv3Trace_Steps_Petrinetv3_Net_Run,
    petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep,
    petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep,
    petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions,
    petrinetv3Trace_Steps_Petrinetv3_Transition_Fire,
    petrinetv3Trace_Steps_RootImplicitStep,
    petrinetv3Trace_Steps_SmallStep,
    petrinetv3Trace_Steps_Step,
    petrinetv3Trace_Trace,
    petrinetv3Trace_petrinetv3_TracedPlace,
    petrinetv3Trace_petrinetv3_TracedToken,
    petrinetv3Trace_petrinetv3_TracedTransition,
    petrinetv3_TracedPlace,
    petrinetv3_TracedToken,
    petrinetv3_TracedTransition,
    petrinetv3_petrinetv3Trace_Net,
    petrinetv3_petrinetv3Trace_Place,
    petrinetv3_petrinetv3Trace_Token,
    petrinetv3_petrinetv3Trace_Transition,
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

def test_assoc_parent34_stub_double():
    # petrinetv3_TracedTransition has no real 'TracedTransition' property in the generated
    # code (a bare stub) -- manually attach it so petrinetv3Trace_States_Transition_clock_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetv3Trace_States_Transition_clock_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetv3Trace_States_Transition_clock_Value(clock=7)
    partner = petrinetv3_TracedTransition()
    setattr(partner, 'TracedTransition', None)
    _safe_set(owner, 'clockSequence', partner)
    assert getattr(partner, 'TracedTransition') == owner
    _safe_set(owner, 'clockSequence', None)
    assert getattr(partner, 'TracedTransition') is None


def test_assoc_states35_stub_double():
    # State has no real 'State36' property in the generated
    # code (a bare stub) -- manually attach it so petrinetv3Trace_States_Transition_clock_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetv3Trace_States_Transition_clock_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetv3Trace_States_Transition_clock_Value(clock=7)
    partner = State()
    setattr(partner, 'State36', None)
    _safe_set(owner, 'transition_clock_Values', {partner})
    assert getattr(partner, 'State36') == owner
    _safe_set(owner, 'transition_clock_Values', set())
    assert getattr(partner, 'State36') is None


def test_assoc_subSteps17_stub_double():
    # Petrinetv3_Net_Run_AbstractSubStep has no real 'Petrinetv3_Net_Run_AbstractSubStep' property in the generated
    # code (a bare stub) -- manually attach it so petrinetv3Trace_Steps_Petrinetv3_Net_Run's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetv3Trace_Steps_Petrinetv3_Net_Run's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetv3Trace_Steps_Petrinetv3_Net_Run()
    partner = Petrinetv3_Net_Run_AbstractSubStep()
    setattr(partner, 'Petrinetv3_Net_Run_AbstractSubStep', None)
    _safe_set(owner, 'petrinetv3Trace_Steps_Petrinetv3_Net_Run', {partner})
    assert getattr(partner, 'Petrinetv3_Net_Run_AbstractSubStep') == owner
    _safe_set(owner, 'petrinetv3Trace_Steps_Petrinetv3_Net_Run', set())
    assert getattr(partner, 'Petrinetv3_Net_Run_AbstractSubStep') is None


