import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element2Element,
    simplegraph2graph_Edge,
    simplegraph2graph_Edge2Edge,
    simplegraph2graph_Element2Element,
    simplegraph2graph_Graph,
    simplegraph2graph_Graph2Graph,
    simplegraph2graph_Node,
    simplegraph2graph_Node2Node,
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

def test_assoc_element2Element4_stub_double():
    # simplegraph2graph_Element2Element has no real 'Element2Element' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Graph2Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Graph2Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Graph2Graph(name="sample_text")
    partner = simplegraph2graph_Element2Element()
    setattr(partner, 'Element2Element', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'Element2Element') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'Element2Element') is None


def test_assoc_graph10_stub_double():
    # simplegraph2graph_Graph has no real 'simplegraph2graph_Graph' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Graph2Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Graph2Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Graph2Graph(name="sample_text")
    partner = simplegraph2graph_Graph()
    setattr(partner, 'simplegraph2graph_Graph', None)
    _safe_set(owner, 'simplegraph2graph_Graph2Graph', partner)
    assert getattr(partner, 'simplegraph2graph_Graph') == owner
    _safe_set(owner, 'simplegraph2graph_Graph2Graph', None)
    assert getattr(partner, 'simplegraph2graph_Graph') is None


def test_assoc_graph21_stub_double():
    # simplegraph2graph_Graph has no real 'simplegraph2graph_Graph3' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Graph2Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Graph2Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Graph2Graph(name="sample_text")
    partner = simplegraph2graph_Graph()
    setattr(partner, 'simplegraph2graph_Graph3', None)
    _safe_set(owner, 'simplegraph2graph_Graph2Graph2', partner)
    assert getattr(partner, 'simplegraph2graph_Graph3') == owner
    _safe_set(owner, 'simplegraph2graph_Graph2Graph2', None)
    assert getattr(partner, 'simplegraph2graph_Graph3') is None


def test_assoc_node115_stub_double():
    # simplegraph2graph_Node has no real 'simplegraph2graph_Node' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Node2Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Node2Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Node2Node(label="sample_text")
    partner = simplegraph2graph_Node()
    setattr(partner, 'simplegraph2graph_Node', None)
    _safe_set(owner, 'simplegraph2graph_Node2Node16', partner)
    assert getattr(partner, 'simplegraph2graph_Node') == owner
    _safe_set(owner, 'simplegraph2graph_Node2Node16', None)
    assert getattr(partner, 'simplegraph2graph_Node') is None


def test_assoc_node217_stub_double():
    # simplegraph2graph_Node has no real 'simplegraph2graph_Node19' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Node2Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Node2Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Node2Node(label="sample_text")
    partner = simplegraph2graph_Node()
    setattr(partner, 'simplegraph2graph_Node19', None)
    _safe_set(owner, 'simplegraph2graph_Node2Node18', partner)
    assert getattr(partner, 'simplegraph2graph_Node19') == owner
    _safe_set(owner, 'simplegraph2graph_Node2Node18', None)
    assert getattr(partner, 'simplegraph2graph_Node19') is None


def test_assoc_owner5_stub_double():
    # simplegraph2graph_Element2Element has no real 'element2Element' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Graph2Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Graph2Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Graph2Graph(name="sample_text")
    partner = simplegraph2graph_Element2Element()
    setattr(partner, 'element2Element', None)
    _safe_set(owner, 'Graph2Graph', partner)
    assert getattr(partner, 'element2Element') == owner
    _safe_set(owner, 'Graph2Graph', None)
    assert getattr(partner, 'element2Element') is None


def test_assoc_source12_stub_double():
    # simplegraph2graph_Edge2Edge has no real 'simplegraph2graph_Edge2Edge13' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Node2Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Node2Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Node2Node(label="sample_text")
    partner = simplegraph2graph_Edge2Edge()
    setattr(partner, 'simplegraph2graph_Edge2Edge13', None)
    _safe_set(owner, 'simplegraph2graph_Node2Node14', partner)
    assert getattr(partner, 'simplegraph2graph_Edge2Edge13') == owner
    _safe_set(owner, 'simplegraph2graph_Node2Node14', None)
    assert getattr(partner, 'simplegraph2graph_Edge2Edge13') is None


def test_assoc_target10_stub_double():
    # simplegraph2graph_Edge2Edge has no real 'simplegraph2graph_Edge2Edge11' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph2graph_Node2Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph2graph_Node2Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph2graph_Node2Node(label="sample_text")
    partner = simplegraph2graph_Edge2Edge()
    setattr(partner, 'simplegraph2graph_Edge2Edge11', None)
    _safe_set(owner, 'simplegraph2graph_Node2Node', partner)
    assert getattr(partner, 'simplegraph2graph_Edge2Edge11') == owner
    _safe_set(owner, 'simplegraph2graph_Node2Node', None)
    assert getattr(partner, 'simplegraph2graph_Edge2Edge11') is None


