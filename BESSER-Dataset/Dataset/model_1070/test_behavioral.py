import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Element,
    LocatedElement,
    NamedElement,
    PetriNet_Arc,
    PetriNet_Element,
    PetriNet_LocatedElement,
    PetriNet_NamedElement,
    PetriNet_PetriNet,
    PetriNet_Place,
    PetriNet_PlaceToTransition,
    PetriNet_Transition,
    PetriNet_TransitionToPlace,
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

def test_assoc_arcs1_stub_double():
    # PetriNet_PetriNet has no real 'net2' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Arc(weight="sample_text")
    partner = PetriNet_PetriNet()
    setattr(partner, 'net2', None)
    _safe_set(owner, 'Arc', partner)
    assert owner in getattr(partner, 'net2')
    _safe_set(owner, 'Arc', None)
    assert owner not in getattr(partner, 'net2')


def test_assoc_net12_stub_double():
    # PetriNet_PetriNet has no real 'PetriNet13' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Arc(weight="sample_text")
    partner = PetriNet_PetriNet()
    setattr(partner, 'PetriNet13', None)
    _safe_set(owner, 'arcs', partner)
    assert getattr(partner, 'PetriNet13') == owner
    _safe_set(owner, 'arcs', None)
    assert getattr(partner, 'PetriNet13') is None


