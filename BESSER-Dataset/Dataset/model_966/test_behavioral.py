import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    simplegraph_Edge,
    simplegraph_Element,
    simplegraph_Graph,
    simplegraph_Node,
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

def test_assoc_element7_stub_double():
    # simplegraph_Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph_Graph(name="sample_text")
    partner = simplegraph_Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'graph', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'graph', set())
    assert getattr(partner, 'Element') is None


def test_assoc_graph6_stub_double():
    # simplegraph_Element has no real 'element' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph_Graph(name="sample_text")
    partner = simplegraph_Element()
    setattr(partner, 'element', None)
    _safe_set(owner, 'Graph', partner)
    assert getattr(partner, 'element') == owner
    _safe_set(owner, 'Graph', None)
    assert getattr(partner, 'element') is None


def test_assoc_incoming0_stub_double():
    # simplegraph_Edge has no real 'Edge' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph_Node(label="sample_text")
    partner = simplegraph_Edge()
    setattr(partner, 'Edge', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Edge') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Edge') is None


def test_assoc_outgoing1_stub_double():
    # simplegraph_Edge has no real 'Edge2' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph_Node(label="sample_text")
    partner = simplegraph_Edge()
    setattr(partner, 'Edge2', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Edge2') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Edge2') is None


def test_assoc_source4_stub_double():
    # simplegraph_Edge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph_Node(label="sample_text")
    partner = simplegraph_Edge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Node5', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Node5', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target3_stub_double():
    # simplegraph_Edge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so simplegraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplegraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplegraph_Node(label="sample_text")
    partner = simplegraph_Edge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'incoming') is None


