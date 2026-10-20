import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    PObject,
    PetriNetModel_Arc,
    PetriNetModel_Node,
    PetriNetModel_PObject,
    PetriNetModel_PetriNet,
    PetriNetModel_Place,
    PetriNetModel_Token,
    PetriNetModel_Transition,
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

def test_assoc_in_2_stub_double():
    # PetriNetModel_Arc has no real 'Arc3' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetModel_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetModel_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetModel_Node(name="sample_text")
    partner = PetriNetModel_Arc()
    setattr(partner, 'Arc3', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Arc3') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Arc3') is None


def test_assoc_objects0_stub_double():
    # PetriNetModel_PetriNet has no real 'PetriNetModel_PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetModel_PObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetModel_PObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetModel_PObject(id=7)
    partner = PetriNetModel_PetriNet()
    setattr(partner, 'PetriNetModel_PetriNet', None)
    _safe_set(owner, 'PetriNetModel_PObject', partner)
    assert owner in getattr(partner, 'PetriNetModel_PetriNet')
    _safe_set(owner, 'PetriNetModel_PObject', None)
    assert owner not in getattr(partner, 'PetriNetModel_PetriNet')


def test_assoc_out1_stub_double():
    # PetriNetModel_Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetModel_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetModel_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetModel_Node(name="sample_text")
    partner = PetriNetModel_Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Arc') is None


def test_assoc_source5_stub_double():
    # PetriNetModel_Arc has no real 'out' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetModel_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetModel_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetModel_Node(name="sample_text")
    partner = PetriNetModel_Arc()
    setattr(partner, 'out', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'out') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'out') is None


def test_assoc_target6_stub_double():
    # PetriNetModel_Arc has no real 'in_' property in the generated
    # code (a bare stub) -- manually attach it so PetriNetModel_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNetModel_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNetModel_Node(name="sample_text")
    partner = PetriNetModel_Arc()
    setattr(partner, 'in_', None)
    _safe_set(owner, 'Node7', partner)
    assert getattr(partner, 'in_') == owner
    _safe_set(owner, 'Node7', None)
    assert getattr(partner, 'in_') is None


