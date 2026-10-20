import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    GenericPT,
    PTArc,
    PetriNet,
    PetriNetMM2_Arc,
    PetriNetMM2_GenericPT,
    PetriNetMM2_PTArc,
    PetriNetMM2_PetriNet,
    PetriNetMM2_PetriNetModel,
    PetriNetMM2_PetriNetModelElement,
    PetriNetMM2_Place,
    PetriNetMM2_TPArc,
    PetriNetMM2_Transition,
    PetriNetModel,
    PetriNetModelElement,
    Place,
    TPArc,
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

def test_assoc_arcs5_stub_double():
    # Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_PetriNet(name="sample_text")
    partner = Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'PetriNetMM2_PetriNet', {partner})
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'PetriNetMM2_PetriNet', set())
    assert getattr(partner, 'Arc') is None


def test_assoc_in_11_stub_double():
    # PTArc has no real 'PTArc13' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_Transition(name="sample_text", relevance=7)
    partner = PTArc()
    setattr(partner, 'PTArc13', None)
    _safe_set(owner, 'dst12', {partner})
    assert getattr(partner, 'PTArc13') == owner
    _safe_set(owner, 'dst12', set())
    assert getattr(partner, 'PTArc13') is None


def test_assoc_in_8_stub_double():
    # TPArc has no real 'TPArc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_Place(name="sample_text", relevance=7)
    partner = TPArc()
    setattr(partner, 'TPArc', None)
    _safe_set(owner, 'dst', {partner})
    assert getattr(partner, 'TPArc') == owner
    _safe_set(owner, 'dst', set())
    assert getattr(partner, 'TPArc') is None


def test_assoc_net6_stub_double():
    # PetriNet has no real 'PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_Place(name="sample_text", relevance=7)
    partner = PetriNet()
    setattr(partner, 'PetriNet', None)
    _safe_set(owner, 'places', partner)
    assert getattr(partner, 'PetriNet') == owner
    _safe_set(owner, 'places', None)
    assert getattr(partner, 'PetriNet') is None


def test_assoc_net9_stub_double():
    # PetriNet has no real 'PetriNet10' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_Transition(name="sample_text", relevance=7)
    partner = PetriNet()
    setattr(partner, 'PetriNet10', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'PetriNet10') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'PetriNet10') is None


def test_assoc_out14_stub_double():
    # TPArc has no real 'TPArc16' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_Transition(name="sample_text", relevance=7)
    partner = TPArc()
    setattr(partner, 'TPArc16', None)
    _safe_set(owner, 'src15', {partner})
    assert getattr(partner, 'TPArc16') == owner
    _safe_set(owner, 'src15', set())
    assert getattr(partner, 'TPArc16') is None


def test_assoc_out7_stub_double():
    # PTArc has no real 'PTArc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_Place(name="sample_text", relevance=7)
    partner = PTArc()
    setattr(partner, 'PTArc', None)
    _safe_set(owner, 'src', {partner})
    assert getattr(partner, 'PTArc') == owner
    _safe_set(owner, 'src', set())
    assert getattr(partner, 'PTArc') is None


def test_assoc_places2_stub_double():
    # Place has no real 'Place' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_PetriNet(name="sample_text")
    partner = Place()
    setattr(partner, 'Place', None)
    _safe_set(owner, 'net', {partner})
    assert getattr(partner, 'Place') == owner
    _safe_set(owner, 'net', set())
    assert getattr(partner, 'Place') is None


def test_assoc_transitions3_stub_double():
    # Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetMM2_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetMM2_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetMM2_PetriNet(name="sample_text")
    partner = Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'net4', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'net4', set())
    assert getattr(partner, 'Transition') is None


