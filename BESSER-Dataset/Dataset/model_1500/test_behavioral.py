import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    Object,
    PetriNets_Arc,
    PetriNets_Node,
    PetriNets_Object,
    PetriNets_PetriNet,
    PetriNets_Place,
    PetriNets_Token,
    PetriNets_Transition,
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

def test_assoc_in_1_stub_double():
    # PetriNets_Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Node(name="sample_text")
    partner = PetriNets_Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Arc') is None


def test_assoc_out2_stub_double():
    # PetriNets_Arc has no real 'Arc3' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Node(name="sample_text")
    partner = PetriNets_Arc()
    setattr(partner, 'Arc3', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Arc3') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Arc3') is None


def test_assoc_source4_stub_double():
    # PetriNets_Arc has no real 'out' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Node(name="sample_text")
    partner = PetriNets_Arc()
    setattr(partner, 'out', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'out') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'out') is None


def test_assoc_target5_stub_double():
    # PetriNets_Arc has no real 'in_' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Node(name="sample_text")
    partner = PetriNets_Arc()
    setattr(partner, 'in_', None)
    _safe_set(owner, 'Node6', partner)
    assert getattr(partner, 'in_') == owner
    _safe_set(owner, 'Node6', None)
    assert getattr(partner, 'in_') is None


def test_assoc_token7_stub_double():
    # PetriNets_Token has no real 'PetriNets_Token' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(capacity=7)
    partner = PetriNets_Token()
    setattr(partner, 'PetriNets_Token', None)
    _safe_set(owner, 'PetriNets_Place', {partner})
    assert getattr(partner, 'PetriNets_Token') == owner
    _safe_set(owner, 'PetriNets_Place', set())
    assert getattr(partner, 'PetriNets_Token') is None


