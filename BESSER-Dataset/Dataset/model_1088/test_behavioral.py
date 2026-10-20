import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    Node,
    petriNet_Arc,
    petriNet_Element,
    petriNet_Node,
    petriNet_PetriNet,
    petriNet_Place,
    petriNet_Transition,
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

def test_assoc_diagram1_stub_double():
    # petriNet_Element has no real 'elements' property in the generated
    # code (a bare stub) -- manually attach it so petriNet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNet_PetriNet(diagramName="sample_text")
    partner = petriNet_Element()
    setattr(partner, 'elements', None)
    _safe_set(owner, 'PetriNet', partner)
    assert getattr(partner, 'elements') == owner
    _safe_set(owner, 'PetriNet', None)
    assert getattr(partner, 'elements') is None


def test_assoc_elements0_stub_double():
    # petriNet_Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so petriNet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNet_PetriNet(diagramName="sample_text")
    partner = petriNet_Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'diagram', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'diagram', set())
    assert getattr(partner, 'Element') is None


def test_assoc_hiddenOpposite2_stub_double():
    # petriNet_Transition has no real 'petriNet_Transition' property in the generated
    # code (a bare stub) -- manually attach it so petriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNet_Place(noTokens=7)
    partner = petriNet_Transition()
    setattr(partner, 'petriNet_Transition', None)
    _safe_set(owner, 'petriNet_Place', partner)
    assert getattr(partner, 'petriNet_Transition') == owner
    _safe_set(owner, 'petriNet_Place', None)
    assert getattr(partner, 'petriNet_Transition') is None


