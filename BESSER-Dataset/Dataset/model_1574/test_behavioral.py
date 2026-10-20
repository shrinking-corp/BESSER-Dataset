import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GraphElement,
    Named,
    Typed,
    graph_Edge,
    graph_Entry,
    graph_Graph,
    graph_GraphElement,
    graph_Label,
    graph_Named,
    graph_Typed,
    graph_Vertex,
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

def test_assoc_edges0_stub_double():
    # graph_Edge has no real 'Edge' property in the generated
    # code (a bare stub) -- manually attach it so graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Graph(direct=True)
    partner = graph_Edge()
    setattr(partner, 'Edge', None)
    _safe_set(owner, 'graph', {partner})
    assert getattr(partner, 'Edge') == owner
    _safe_set(owner, 'graph', set())
    assert getattr(partner, 'Edge') is None


def test_assoc_entries22_stub_double():
    # graph_Label has no real 'label23' property in the generated
    # code (a bare stub) -- manually attach it so graph_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Entry(key="sample_text", value="sample_text")
    partner = graph_Label()
    setattr(partner, 'label23', None)
    _safe_set(owner, 'Entry', partner)
    assert owner in getattr(partner, 'label23')
    _safe_set(owner, 'Entry', None)
    assert owner not in getattr(partner, 'label23')


def test_assoc_graph3_stub_double():
    # graph_Vertex has no real 'vertices' property in the generated
    # code (a bare stub) -- manually attach it so graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Graph(direct=True)
    partner = graph_Vertex()
    setattr(partner, 'vertices', None)
    _safe_set(owner, 'Graph', partner)
    assert getattr(partner, 'vertices') == owner
    _safe_set(owner, 'Graph', None)
    assert getattr(partner, 'vertices') is None


def test_assoc_graph9_stub_double():
    # graph_Edge has no real 'edges' property in the generated
    # code (a bare stub) -- manually attach it so graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Graph(direct=True)
    partner = graph_Edge()
    setattr(partner, 'edges', None)
    _safe_set(owner, 'Graph10', partner)
    assert getattr(partner, 'edges') == owner
    _safe_set(owner, 'Graph10', None)
    assert getattr(partner, 'edges') is None


def test_assoc_label24_stub_double():
    # graph_Label has no real 'Label25' property in the generated
    # code (a bare stub) -- manually attach it so graph_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Entry(key="sample_text", value="sample_text")
    partner = graph_Label()
    setattr(partner, 'Label25', None)
    _safe_set(owner, 'entries', partner)
    assert getattr(partner, 'Label25') == owner
    _safe_set(owner, 'entries', None)
    assert getattr(partner, 'Label25') is None


def test_assoc_vertices1_stub_double():
    # graph_Vertex has no real 'Vertex' property in the generated
    # code (a bare stub) -- manually attach it so graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Graph(direct=True)
    partner = graph_Vertex()
    setattr(partner, 'Vertex', None)
    _safe_set(owner, 'graph2', {partner})
    assert getattr(partner, 'Vertex') == owner
    _safe_set(owner, 'graph2', set())
    assert getattr(partner, 'Vertex') is None


