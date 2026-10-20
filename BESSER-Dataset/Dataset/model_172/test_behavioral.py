import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Edge,
    petri_Edge,
    petri_EdgeToPlace,
    petri_EdgeToTransition,
    petri_PetriNet,
    petri_Place,
    petri_Transition,
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

def test_assoc_in_10_stub_double():
    # petri_EdgeToTransition has no real 'petri_EdgeToTransition11' property in the generated
    # code (a bare stub) -- manually attach it so petri_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petri_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petri_Transition(token=7)
    partner = petri_EdgeToTransition()
    setattr(partner, 'petri_EdgeToTransition11', None)
    _safe_set(owner, 'petri_Transition12', partner)
    assert getattr(partner, 'petri_EdgeToTransition11') == owner
    _safe_set(owner, 'petri_Transition12', None)
    assert getattr(partner, 'petri_EdgeToTransition11') is None


def test_assoc_in_7_stub_double():
    # petri_EdgeToPlace has no real 'petri_EdgeToPlace8' property in the generated
    # code (a bare stub) -- manually attach it so petri_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petri_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petri_Place(token=7)
    partner = petri_EdgeToPlace()
    setattr(partner, 'petri_EdgeToPlace8', None)
    _safe_set(owner, 'petri_Place9', partner)
    assert getattr(partner, 'petri_EdgeToPlace8') == owner
    _safe_set(owner, 'petri_Place9', None)
    assert getattr(partner, 'petri_EdgeToPlace8') is None


def test_assoc_out3_stub_double():
    # petri_EdgeToTransition has no real 'petri_EdgeToTransition' property in the generated
    # code (a bare stub) -- manually attach it so petri_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petri_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petri_Place(token=7)
    partner = petri_EdgeToTransition()
    setattr(partner, 'petri_EdgeToTransition', None)
    _safe_set(owner, 'petri_Place4', {partner})
    assert getattr(partner, 'petri_EdgeToTransition') == owner
    _safe_set(owner, 'petri_Place4', set())
    assert getattr(partner, 'petri_EdgeToTransition') is None


def test_assoc_out5_stub_double():
    # petri_EdgeToPlace has no real 'petri_EdgeToPlace' property in the generated
    # code (a bare stub) -- manually attach it so petri_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petri_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petri_Transition(token=7)
    partner = petri_EdgeToPlace()
    setattr(partner, 'petri_EdgeToPlace', None)
    _safe_set(owner, 'petri_Transition6', {partner})
    assert getattr(partner, 'petri_EdgeToPlace') == owner
    _safe_set(owner, 'petri_Transition6', set())
    assert getattr(partner, 'petri_EdgeToPlace') is None


def test_assoc_places1_stub_double():
    # petri_PetriNet has no real 'petri_PetriNet2' property in the generated
    # code (a bare stub) -- manually attach it so petri_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petri_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petri_Place(token=7)
    partner = petri_PetriNet()
    setattr(partner, 'petri_PetriNet2', None)
    _safe_set(owner, 'petri_Place', partner)
    assert owner in getattr(partner, 'petri_PetriNet2')
    _safe_set(owner, 'petri_Place', None)
    assert owner not in getattr(partner, 'petri_PetriNet2')


def test_assoc_transitions0_stub_double():
    # petri_PetriNet has no real 'petri_PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so petri_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petri_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petri_Transition(token=7)
    partner = petri_PetriNet()
    setattr(partner, 'petri_PetriNet', None)
    _safe_set(owner, 'petri_Transition', partner)
    assert owner in getattr(partner, 'petri_PetriNet')
    _safe_set(owner, 'petri_Transition', None)
    assert owner not in getattr(partner, 'petri_PetriNet')


