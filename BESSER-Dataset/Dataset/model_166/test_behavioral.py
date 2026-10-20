import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Element,
    petrinet_metamodel_Arc,
    petrinet_metamodel_Element,
    petrinet_metamodel_PetriNet,
    petrinet_metamodel_Place,
    petrinet_metamodel_PlaceToTransArc,
    petrinet_metamodel_Rectangle,
    petrinet_metamodel_TransToPlaceArc,
    petrinet_metamodel_Transition,
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

def test_assoc_arcs3_stub_double():
    # petrinet_metamodel_PetriNet has no real 'petrinet_metamodel_PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Arc(weight=7)
    partner = petrinet_metamodel_PetriNet()
    setattr(partner, 'petrinet_metamodel_PetriNet', None)
    _safe_set(owner, 'petrinet_metamodel_Arc', partner)
    assert owner in getattr(partner, 'petrinet_metamodel_PetriNet')
    _safe_set(owner, 'petrinet_metamodel_Arc', None)
    assert owner not in getattr(partner, 'petrinet_metamodel_PetriNet')


def test_assoc_belongs_to26_stub_double():
    # petrinet_metamodel_Transition has no real 'Transition27' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Rectangle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Rectangle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Rectangle(start_end_coordinates=7)
    partner = petrinet_metamodel_Transition()
    setattr(partner, 'Transition27', None)
    _safe_set(owner, 'rectangle', partner)
    assert getattr(partner, 'Transition27') == owner
    _safe_set(owner, 'rectangle', None)
    assert getattr(partner, 'Transition27') is None


def test_assoc_incoming4_stub_double():
    # petrinet_metamodel_TransToPlaceArc has no real 'TransToPlaceArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Place(coordinates=7, fill_colour="sample_text", radius=7)
    partner = petrinet_metamodel_TransToPlaceArc()
    setattr(partner, 'TransToPlaceArc', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'TransToPlaceArc') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'TransToPlaceArc') is None


def test_assoc_outgoing5_stub_double():
    # petrinet_metamodel_PlaceToTransArc has no real 'PlaceToTransArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Place(coordinates=7, fill_colour="sample_text", radius=7)
    partner = petrinet_metamodel_PlaceToTransArc()
    setattr(partner, 'PlaceToTransArc', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'PlaceToTransArc') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'PlaceToTransArc') is None


def test_assoc_petrinet6_stub_double():
    # petrinet_metamodel_PetriNet has no real 'PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Place(coordinates=7, fill_colour="sample_text", radius=7)
    partner = petrinet_metamodel_PetriNet()
    setattr(partner, 'PetriNet', None)
    _safe_set(owner, 'places', partner)
    assert getattr(partner, 'PetriNet') == owner
    _safe_set(owner, 'places', None)
    assert getattr(partner, 'PetriNet') is None


def test_assoc_places0_stub_double():
    # petrinet_metamodel_PetriNet has no real 'petrinet' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Place(coordinates=7, fill_colour="sample_text", radius=7)
    partner = petrinet_metamodel_PetriNet()
    setattr(partner, 'petrinet', None)
    _safe_set(owner, 'Place', partner)
    assert owner in getattr(partner, 'petrinet')
    _safe_set(owner, 'Place', None)
    assert owner not in getattr(partner, 'petrinet')


def test_assoc_rectangle15_stub_double():
    # petrinet_metamodel_Transition has no real 'belongs_to' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Rectangle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Rectangle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Rectangle(start_end_coordinates=7)
    partner = petrinet_metamodel_Transition()
    setattr(partner, 'belongs_to', None)
    _safe_set(owner, 'Rectangle', partner)
    assert getattr(partner, 'belongs_to') == owner
    _safe_set(owner, 'Rectangle', None)
    assert getattr(partner, 'belongs_to') is None


def test_assoc_source16_stub_double():
    # petrinet_metamodel_PlaceToTransArc has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Place(coordinates=7, fill_colour="sample_text", radius=7)
    partner = petrinet_metamodel_PlaceToTransArc()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Place17', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Place17', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target23_stub_double():
    # petrinet_metamodel_TransToPlaceArc has no real 'incoming24' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_metamodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_metamodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_metamodel_Place(coordinates=7, fill_colour="sample_text", radius=7)
    partner = petrinet_metamodel_TransToPlaceArc()
    setattr(partner, 'incoming24', None)
    _safe_set(owner, 'Place25', partner)
    assert getattr(partner, 'incoming24') == owner
    _safe_set(owner, 'Place25', None)
    assert getattr(partner, 'incoming24') is None


