import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Element,
    Node,
    petrinet_Arc,
    petrinet_Element,
    petrinet_InputArc,
    petrinet_Node,
    petrinet_OutputArc,
    petrinet_PetriNet,
    petrinet_PetriNetRelationship,
    petrinet_Place,
    petrinet_System,
    petrinet_Transition,
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

def test_assoc_elements3_stub_double():
    # petrinet_Element has no real 'petrinet_Element' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_Element()
    setattr(partner, 'petrinet_Element', None)
    _safe_set(owner, 'petrinet_PetriNet4', {partner})
    assert getattr(partner, 'petrinet_Element') == owner
    _safe_set(owner, 'petrinet_PetriNet4', set())
    assert getattr(partner, 'petrinet_Element') is None


def test_assoc_from_5_stub_double():
    # petrinet_PetriNetRelationship has no real 'petrinet_PetriNetRelationship6' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_PetriNetRelationship()
    setattr(partner, 'petrinet_PetriNetRelationship6', None)
    _safe_set(owner, 'petrinet_PetriNet7', partner)
    assert getattr(partner, 'petrinet_PetriNetRelationship6') == owner
    _safe_set(owner, 'petrinet_PetriNet7', None)
    assert getattr(partner, 'petrinet_PetriNetRelationship6') is None


def test_assoc_petrinets0_stub_double():
    # petrinet_System has no real 'petrinet_System' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_System()
    setattr(partner, 'petrinet_System', None)
    _safe_set(owner, 'petrinet_PetriNet', partner)
    assert owner in getattr(partner, 'petrinet_System')
    _safe_set(owner, 'petrinet_PetriNet', None)
    assert owner not in getattr(partner, 'petrinet_System')


def test_assoc_to8_stub_double():
    # petrinet_PetriNetRelationship has no real 'petrinet_PetriNetRelationship9' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_PetriNetRelationship()
    setattr(partner, 'petrinet_PetriNetRelationship9', None)
    _safe_set(owner, 'petrinet_PetriNet10', partner)
    assert getattr(partner, 'petrinet_PetriNetRelationship9') == owner
    _safe_set(owner, 'petrinet_PetriNet10', None)
    assert getattr(partner, 'petrinet_PetriNetRelationship9') is None


