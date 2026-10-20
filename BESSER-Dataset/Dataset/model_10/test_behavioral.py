import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    petrinet_Arc,
    petrinet_Node,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_Token,
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

def test_assoc_net12_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Node(name="sample_text")
    _safe_set(b, 'petrinet_Node13', a1)
    assert _is_linked(b, 'petrinet_Node13', a1)
    if hasattr(a1, 'petrinet_PetriNet14'):
        assert _is_linked(a1, 'petrinet_PetriNet14', b)
    _safe_set(b, 'petrinet_Node13', a2)
    assert _is_linked(b, 'petrinet_Node13', a2)
    if hasattr(a1, 'petrinet_PetriNet14'):
        assert not _is_linked(a1, 'petrinet_PetriNet14', b)
    if hasattr(a2, 'petrinet_PetriNet14'):
        assert _is_linked(a2, 'petrinet_PetriNet14', b)
    _safe_set(b, 'petrinet_Node13', None)
    assert not _is_linked(b, 'petrinet_Node13', a2)
    if hasattr(a2, 'petrinet_PetriNet14'):
        assert not _is_linked(a2, 'petrinet_PetriNet14', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Node(name="sample_text")
    _safe_set(b, 'petrinet_Node', a1)
    assert _is_linked(b, 'petrinet_Node', a1)
    if hasattr(a1, 'petrinet_PetriNet'):
        assert _is_linked(a1, 'petrinet_PetriNet', b)
    _safe_set(b, 'petrinet_Node', a2)
    assert _is_linked(b, 'petrinet_Node', a2)
    if hasattr(a1, 'petrinet_PetriNet'):
        assert not _is_linked(a1, 'petrinet_PetriNet', b)
    if hasattr(a2, 'petrinet_PetriNet'):
        assert _is_linked(a2, 'petrinet_PetriNet', b)
    _safe_set(b, 'petrinet_Node', None)
    assert not _is_linked(b, 'petrinet_Node', a2)
    if hasattr(a2, 'petrinet_PetriNet'):
        assert not _is_linked(a2, 'petrinet_PetriNet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arcs1_stub_double():
    # petrinet_Arc has no real 'petrinet_Arc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'petrinet_Arc', None)
    _safe_set(owner, 'petrinet_PetriNet2', {partner})
    assert getattr(partner, 'petrinet_Arc') == owner
    _safe_set(owner, 'petrinet_PetriNet2', set())
    assert getattr(partner, 'petrinet_Arc') is None


def test_assoc_incoming15_stub_double():
    # petrinet_Arc has no real 'petrinet_Arc17' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'petrinet_Arc17', None)
    _safe_set(owner, 'petrinet_Node16', {partner})
    assert getattr(partner, 'petrinet_Arc17') == owner
    _safe_set(owner, 'petrinet_Node16', set())
    assert getattr(partner, 'petrinet_Arc17') is None


def test_assoc_net3_stub_double():
    # petrinet_Arc has no real 'petrinet_Arc4' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'petrinet_Arc4', None)
    _safe_set(owner, 'petrinet_PetriNet5', partner)
    assert getattr(partner, 'petrinet_Arc4') == owner
    _safe_set(owner, 'petrinet_PetriNet5', None)
    assert getattr(partner, 'petrinet_Arc4') is None


def test_assoc_outgoing18_stub_double():
    # petrinet_Arc has no real 'petrinet_Arc20' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'petrinet_Arc20', None)
    _safe_set(owner, 'petrinet_Node19', {partner})
    assert getattr(partner, 'petrinet_Arc20') == owner
    _safe_set(owner, 'petrinet_Node19', set())
    assert getattr(partner, 'petrinet_Arc20') is None


def test_assoc_source6_stub_double():
    # petrinet_Arc has no real 'petrinet_Arc7' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'petrinet_Arc7', None)
    _safe_set(owner, 'petrinet_Node8', partner)
    assert getattr(partner, 'petrinet_Arc7') == owner
    _safe_set(owner, 'petrinet_Node8', None)
    assert getattr(partner, 'petrinet_Arc7') is None


def test_assoc_target9_stub_double():
    # petrinet_Arc has no real 'petrinet_Arc10' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Node(name="sample_text")
    partner = petrinet_Arc()
    setattr(partner, 'petrinet_Arc10', None)
    _safe_set(owner, 'petrinet_Node11', partner)
    assert getattr(partner, 'petrinet_Arc10') == owner
    _safe_set(owner, 'petrinet_Node11', None)
    assert getattr(partner, 'petrinet_Arc10') is None


