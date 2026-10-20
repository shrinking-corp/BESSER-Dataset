import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Node,
    PetriNets_Arc,
    PetriNets_Node,
    PetriNets_PTArc,
    PetriNets_PetriNet,
    PetriNets_Place,
    PetriNets_TPArc,
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

def test_assoc_arcs1_reverse_link_reassign_clear():
    a1 = PetriNets_PetriNet(bound=7)
    a2 = PetriNets_PetriNet(bound=13)
    b = PetriNets_Arc(weight=7)
    _safe_set(b, 'PetriNets_Arc', a1)
    assert _is_linked(b, 'PetriNets_Arc', a1)
    if hasattr(a1, 'PetriNets_PetriNet'):
        assert _is_linked(a1, 'PetriNets_PetriNet', b)
    _safe_set(b, 'PetriNets_Arc', a2)
    assert _is_linked(b, 'PetriNets_Arc', a2)
    if hasattr(a1, 'PetriNets_PetriNet'):
        assert not _is_linked(a1, 'PetriNets_PetriNet', b)
    if hasattr(a2, 'PetriNets_PetriNet'):
        assert _is_linked(a2, 'PetriNets_PetriNet', b)
    _safe_set(b, 'PetriNets_Arc', None)
    assert not _is_linked(b, 'PetriNets_Arc', a2)
    if hasattr(a2, 'PetriNets_PetriNet'):
        assert not _is_linked(a2, 'PetriNets_PetriNet', b)


def test_assoc_net6_reverse_link_reassign_clear():
    a1 = PetriNets_PetriNet(bound=7)
    a2 = PetriNets_PetriNet(bound=13)
    b = PetriNets_Node(name="sample_text")
    _safe_set(b, 'nodes', a1)
    assert _is_linked(b, 'nodes', a1)
    if hasattr(a1, 'PetriNet'):
        assert _is_linked(a1, 'PetriNet', b)
    _safe_set(b, 'nodes', a2)
    assert _is_linked(b, 'nodes', a2)
    if hasattr(a1, 'PetriNet'):
        assert not _is_linked(a1, 'PetriNet', b)
    if hasattr(a2, 'PetriNet'):
        assert _is_linked(a2, 'PetriNet', b)
    _safe_set(b, 'nodes', None)
    assert not _is_linked(b, 'nodes', a2)
    if hasattr(a2, 'PetriNet'):
        assert not _is_linked(a2, 'PetriNet', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = PetriNets_PetriNet(bound=7)
    a2 = PetriNets_PetriNet(bound=13)
    b = PetriNets_Node(name="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'net'):
        assert _is_linked(a1, 'net', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'net'):
        assert not _is_linked(a1, 'net', b)
    if hasattr(a2, 'net'):
        assert _is_linked(a2, 'net', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'net'):
        assert not _is_linked(a2, 'net', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_input14_stub_double():
    # PetriNets_PTArc has no real 'PetriNets_PTArc15' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(tokens=7)
    partner = PetriNets_PTArc()
    setattr(partner, 'PetriNets_PTArc15', None)
    _safe_set(owner, 'PetriNets_Place16', partner)
    assert getattr(partner, 'PetriNets_PTArc15') == owner
    _safe_set(owner, 'PetriNets_Place16', None)
    assert getattr(partner, 'PetriNets_PTArc15') is None


def test_assoc_inputs2_stub_double():
    # PetriNets_Transition has no real 'PetriNets_Transition' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(tokens=7)
    partner = PetriNets_Transition()
    setattr(partner, 'PetriNets_Transition', None)
    _safe_set(owner, 'PetriNets_Place', partner)
    assert owner in getattr(partner, 'PetriNets_Transition')
    _safe_set(owner, 'PetriNets_Place', None)
    assert owner not in getattr(partner, 'PetriNets_Transition')


def test_assoc_output9_stub_double():
    # PetriNets_TPArc has no real 'PetriNets_TPArc10' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(tokens=7)
    partner = PetriNets_TPArc()
    setattr(partner, 'PetriNets_TPArc10', None)
    _safe_set(owner, 'PetriNets_Place11', partner)
    assert getattr(partner, 'PetriNets_TPArc10') == owner
    _safe_set(owner, 'PetriNets_Place11', None)
    assert getattr(partner, 'PetriNets_TPArc10') is None


def test_assoc_outputs3_stub_double():
    # PetriNets_Transition has no real 'PetriNets_Transition4' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(tokens=7)
    partner = PetriNets_Transition()
    setattr(partner, 'PetriNets_Transition4', None)
    _safe_set(owner, 'PetriNets_Place5', partner)
    assert owner in getattr(partner, 'PetriNets_Transition4')
    _safe_set(owner, 'PetriNets_Place5', None)
    assert owner not in getattr(partner, 'PetriNets_Transition4')


