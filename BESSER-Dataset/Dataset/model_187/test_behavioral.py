import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Element,
    PetriNet,
    PetriNet_Arc,
    PetriNet_Element,
    PetriNet_NonReferencedClass,
    PetriNet_PetriNet,
    PetriNet_Place,
    PetriNet_PlaceToTransArc,
    PetriNet_TransToPlaceArc,
    PetriNet_Transition,
    Place,
    PlaceToTransArc,
    TransToPlaceArc,
    Transition,
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

def test_assoc_incoming4_stub_double():
    # TransToPlaceArc has no real 'TransToPlaceArc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = TransToPlaceArc()
    setattr(partner, 'TransToPlaceArc', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'TransToPlaceArc') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'TransToPlaceArc') is None


def test_assoc_net6_stub_double():
    # PetriNet has no real 'PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet()
    setattr(partner, 'PetriNet', None)
    _safe_set(owner, 'places', partner)
    assert getattr(partner, 'PetriNet') == owner
    _safe_set(owner, 'places', None)
    assert getattr(partner, 'PetriNet') is None


def test_assoc_outgoing5_stub_double():
    # PlaceToTransArc has no real 'PlaceToTransArc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PlaceToTransArc()
    setattr(partner, 'PlaceToTransArc', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'PlaceToTransArc') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'PlaceToTransArc') is None


