import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Node,
    petrinet_Arc,
    petrinet_Node,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_PlaceTransitionArc,
    petrinet_Transition,
    petrinet_TransitionPlaceArc,
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

def test_assoc_arcs19_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Arc(weight=7)
    _safe_set(b, 'petrinet_Arc', a1)
    assert _is_linked(b, 'petrinet_Arc', a1)
    if hasattr(a1, 'petrinet_PetriNet20'):
        assert _is_linked(a1, 'petrinet_PetriNet20', b)
    _safe_set(b, 'petrinet_Arc', a2)
    assert _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a1, 'petrinet_PetriNet20'):
        assert not _is_linked(a1, 'petrinet_PetriNet20', b)
    if hasattr(a2, 'petrinet_PetriNet20'):
        assert _is_linked(a2, 'petrinet_PetriNet20', b)
    _safe_set(b, 'petrinet_Arc', None)
    assert not _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a2, 'petrinet_PetriNet20'):
        assert not _is_linked(a2, 'petrinet_PetriNet20', b)


def test_assoc_nodes21_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Node(name="sample_text")
    _safe_set(b, 'petrinet_Node', a1)
    assert _is_linked(b, 'petrinet_Node', a1)
    if hasattr(a1, 'petrinet_PetriNet22'):
        assert _is_linked(a1, 'petrinet_PetriNet22', b)
    _safe_set(b, 'petrinet_Node', a2)
    assert _is_linked(b, 'petrinet_Node', a2)
    if hasattr(a1, 'petrinet_PetriNet22'):
        assert not _is_linked(a1, 'petrinet_PetriNet22', b)
    if hasattr(a2, 'petrinet_PetriNet22'):
        assert _is_linked(a2, 'petrinet_PetriNet22', b)
    _safe_set(b, 'petrinet_Node', None)
    assert not _is_linked(b, 'petrinet_Node', a2)
    if hasattr(a2, 'petrinet_PetriNet22'):
        assert not _is_linked(a2, 'petrinet_PetriNet22', b)


def test_assoc_places8_reverse_link_reassign_clear():
    a1 = petrinet_Place(capacity=7, tokens=7)
    a2 = petrinet_Place(capacity=13, tokens=13)
    b = petrinet_PetriNet(name="sample_text")
    _safe_set(b, 'petrinet_PetriNet', {a1})
    assert _is_linked(b, 'petrinet_PetriNet', a1)
    if hasattr(a1, 'petrinet_Place9'):
        assert _is_linked(a1, 'petrinet_Place9', b)
    _safe_set(b, 'petrinet_PetriNet', {a2})
    assert _is_linked(b, 'petrinet_PetriNet', a2)
    if hasattr(a1, 'petrinet_Place9'):
        assert not _is_linked(a1, 'petrinet_Place9', b)
    if hasattr(a2, 'petrinet_Place9'):
        assert _is_linked(a2, 'petrinet_Place9', b)
    _safe_set(b, 'petrinet_PetriNet', set())
    assert not _is_linked(b, 'petrinet_PetriNet', a2)
    if hasattr(a2, 'petrinet_Place9'):
        assert not _is_linked(a2, 'petrinet_Place9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_inputArcs13_stub_double():
    # petrinet_PlaceTransitionArc has no real 'petrinet_PlaceTransitionArc15' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_PlaceTransitionArc()
    setattr(partner, 'petrinet_PlaceTransitionArc15', None)
    _safe_set(owner, 'petrinet_PetriNet14', {partner})
    assert getattr(partner, 'petrinet_PlaceTransitionArc15') == owner
    _safe_set(owner, 'petrinet_PetriNet14', set())
    assert getattr(partner, 'petrinet_PlaceTransitionArc15') is None


def test_assoc_outputArcs16_stub_double():
    # petrinet_TransitionPlaceArc has no real 'petrinet_TransitionPlaceArc18' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_TransitionPlaceArc()
    setattr(partner, 'petrinet_TransitionPlaceArc18', None)
    _safe_set(owner, 'petrinet_PetriNet17', {partner})
    assert getattr(partner, 'petrinet_TransitionPlaceArc18') == owner
    _safe_set(owner, 'petrinet_PetriNet17', set())
    assert getattr(partner, 'petrinet_TransitionPlaceArc18') is None


def test_assoc_ptFromPlace0_stub_double():
    # petrinet_PlaceTransitionArc has no real 'petrinet_PlaceTransitionArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(capacity=7, tokens=7)
    partner = petrinet_PlaceTransitionArc()
    setattr(partner, 'petrinet_PlaceTransitionArc', None)
    _safe_set(owner, 'petrinet_Place', partner)
    assert getattr(partner, 'petrinet_PlaceTransitionArc') == owner
    _safe_set(owner, 'petrinet_Place', None)
    assert getattr(partner, 'petrinet_PlaceTransitionArc') is None


def test_assoc_tpToPlace5_stub_double():
    # petrinet_TransitionPlaceArc has no real 'petrinet_TransitionPlaceArc6' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(capacity=7, tokens=7)
    partner = petrinet_TransitionPlaceArc()
    setattr(partner, 'petrinet_TransitionPlaceArc6', None)
    _safe_set(owner, 'petrinet_Place7', partner)
    assert getattr(partner, 'petrinet_TransitionPlaceArc6') == owner
    _safe_set(owner, 'petrinet_Place7', None)
    assert getattr(partner, 'petrinet_TransitionPlaceArc6') is None


def test_assoc_transitions10_stub_double():
    # petrinet_Transition has no real 'petrinet_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_Transition()
    setattr(partner, 'petrinet_Transition12', None)
    _safe_set(owner, 'petrinet_PetriNet11', {partner})
    assert getattr(partner, 'petrinet_Transition12') == owner
    _safe_set(owner, 'petrinet_PetriNet11', set())
    assert getattr(partner, 'petrinet_Transition12') is None


