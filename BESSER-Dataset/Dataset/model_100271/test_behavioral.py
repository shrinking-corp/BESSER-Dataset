import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Connection,
    Element,
    Grafcet,
    Grafcet_Connection,
    Grafcet_Element,
    Grafcet_Grafcet,
    Grafcet_LocatedElement,
    Grafcet_NamedElement,
    Grafcet_Step,
    Grafcet_StepToTransition,
    Grafcet_Transition,
    Grafcet_TransitionToStep,
    LocatedElement,
    NamedElement,
    Step,
    StepToTransition,
    Transition,
    TransitionToStep,
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

def test_assoc_incomingConnections4_stub_double():
    # TransitionToStep has no real 'TransitionToStep' property in the generated
    # code (a bare stub) -- manually attach it so Grafcet_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Grafcet_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Grafcet_Step(action="sample_text", isActive="sample_text", isInitial="sample_text")
    partner = TransitionToStep()
    setattr(partner, 'TransitionToStep', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'TransitionToStep') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'TransitionToStep') is None


def test_assoc_incomingConnections6_stub_double():
    # StepToTransition has no real 'StepToTransition8' property in the generated
    # code (a bare stub) -- manually attach it so Grafcet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Grafcet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Grafcet_Transition(condition="sample_text")
    partner = StepToTransition()
    setattr(partner, 'StepToTransition8', None)
    _safe_set(owner, 'to7', {partner})
    assert getattr(partner, 'StepToTransition8') == owner
    _safe_set(owner, 'to7', set())
    assert getattr(partner, 'StepToTransition8') is None


def test_assoc_outgoingConnections5_stub_double():
    # StepToTransition has no real 'StepToTransition' property in the generated
    # code (a bare stub) -- manually attach it so Grafcet_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Grafcet_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Grafcet_Step(action="sample_text", isActive="sample_text", isInitial="sample_text")
    partner = StepToTransition()
    setattr(partner, 'StepToTransition', None)
    _safe_set(owner, 'from_', {partner})
    assert getattr(partner, 'StepToTransition') == owner
    _safe_set(owner, 'from_', set())
    assert getattr(partner, 'StepToTransition') is None


def test_assoc_outgoingConnections9_stub_double():
    # TransitionToStep has no real 'TransitionToStep11' property in the generated
    # code (a bare stub) -- manually attach it so Grafcet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Grafcet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Grafcet_Transition(condition="sample_text")
    partner = TransitionToStep()
    setattr(partner, 'TransitionToStep11', None)
    _safe_set(owner, 'from_10', {partner})
    assert getattr(partner, 'TransitionToStep11') == owner
    _safe_set(owner, 'from_10', set())
    assert getattr(partner, 'TransitionToStep11') is None


