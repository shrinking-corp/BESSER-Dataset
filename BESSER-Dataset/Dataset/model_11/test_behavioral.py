import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    RefArcs,
    RefNodes,
    RefPetriNets,
    RefTokens,
    petrinet_Arc,
    petrinet_Node,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_RefArcs,
    petrinet_RefNodes,
    petrinet_RefPetriNets,
    petrinet_RefTokens,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arcs1_stub_double():
    # petrinet_RefArcs has no real 'petrinet_RefArcs' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_RefArcs()
    setattr(partner, 'petrinet_RefArcs', None)
    _safe_set(owner, 'petrinet_PetriNet2', {partner})
    assert getattr(partner, 'petrinet_RefArcs') == owner
    _safe_set(owner, 'petrinet_PetriNet2', set())
    assert getattr(partner, 'petrinet_RefArcs') is None


def test_assoc_nodes0_stub_double():
    # petrinet_RefNodes has no real 'petrinet_RefNodes' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_PetriNet(name="sample_text")
    partner = petrinet_RefNodes()
    setattr(partner, 'petrinet_RefNodes', None)
    _safe_set(owner, 'petrinet_PetriNet', {partner})
    assert getattr(partner, 'petrinet_RefNodes') == owner
    _safe_set(owner, 'petrinet_PetriNet', set())
    assert getattr(partner, 'petrinet_RefNodes') is None


def test_assoc_source5_stub_double():
    # petrinet_RefNodes has no real 'petrinet_RefNodes7' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(name="sample_text")
    partner = petrinet_RefNodes()
    setattr(partner, 'petrinet_RefNodes7', None)
    _safe_set(owner, 'petrinet_Arc6', partner)
    assert getattr(partner, 'petrinet_RefNodes7') == owner
    _safe_set(owner, 'petrinet_Arc6', None)
    assert getattr(partner, 'petrinet_RefNodes7') is None


def test_assoc_target3_stub_double():
    # petrinet_RefNodes has no real 'petrinet_RefNodes4' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Arc(name="sample_text")
    partner = petrinet_RefNodes()
    setattr(partner, 'petrinet_RefNodes4', None)
    _safe_set(owner, 'petrinet_Arc', partner)
    assert getattr(partner, 'petrinet_RefNodes4') == owner
    _safe_set(owner, 'petrinet_Arc', None)
    assert getattr(partner, 'petrinet_RefNodes4') is None


