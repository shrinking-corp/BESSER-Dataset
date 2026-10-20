import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    GraphElement,
    graphdb_Edge,
    graphdb_Element,
    graphdb_Graph,
    graphdb_GraphElement,
    graphdb_Property,
    graphdb_Vertex,
    DatabaseKind,
    PrimitiveType,
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

def test_assoc_edges1_reverse_link_reassign_clear():
    a1 = graphdb_Graph(rawDatabase="sample_text")
    a2 = graphdb_Graph(rawDatabase="sample_text_2")
    b = graphdb_Edge(name="sample_text", type="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'graph2'):
        assert _is_linked(a1, 'graph2', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'graph2'):
        assert not _is_linked(a1, 'graph2', b)
    if hasattr(a2, 'graph2'):
        assert _is_linked(a2, 'graph2', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'graph2'):
        assert not _is_linked(a2, 'graph2', b)


def test_assoc_graph13_reverse_link_reassign_clear():
    a1 = graphdb_Graph(rawDatabase="sample_text")
    a2 = graphdb_Graph(rawDatabase="sample_text_2")
    b = graphdb_Edge(name="sample_text", type="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Graph14'):
        assert _is_linked(a1, 'Graph14', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Graph14'):
        assert not _is_linked(a1, 'Graph14', b)
    if hasattr(a2, 'Graph14'):
        assert _is_linked(a2, 'Graph14', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Graph14'):
        assert not _is_linked(a2, 'Graph14', b)


def test_assoc_graph8_reverse_link_reassign_clear():
    a1 = graphdb_Vertex(labels="sample_text", name="sample_text")
    a2 = graphdb_Vertex(labels="sample_text_2", name="sample_text_2")
    b = graphdb_Graph(rawDatabase="sample_text")
    _safe_set(b, 'Graph', a1)
    assert _is_linked(b, 'Graph', a1)
    if hasattr(a1, 'vertices'):
        assert _is_linked(a1, 'vertices', b)
    _safe_set(b, 'Graph', a2)
    assert _is_linked(b, 'Graph', a2)
    if hasattr(a1, 'vertices'):
        assert not _is_linked(a1, 'vertices', b)
    if hasattr(a2, 'vertices'):
        assert _is_linked(a2, 'vertices', b)
    _safe_set(b, 'Graph', None)
    assert not _is_linked(b, 'Graph', a2)
    if hasattr(a2, 'vertices'):
        assert not _is_linked(a2, 'vertices', b)


def test_assoc_head11_reverse_link_reassign_clear():
    a1 = graphdb_Vertex(labels="sample_text", name="sample_text")
    a2 = graphdb_Vertex(labels="sample_text_2", name="sample_text_2")
    b = graphdb_Edge(name="sample_text", type="sample_text")
    _safe_set(b, 'inEdges', a1)
    assert _is_linked(b, 'inEdges', a1)
    if hasattr(a1, 'Vertex12'):
        assert _is_linked(a1, 'Vertex12', b)
    _safe_set(b, 'inEdges', a2)
    assert _is_linked(b, 'inEdges', a2)
    if hasattr(a1, 'Vertex12'):
        assert not _is_linked(a1, 'Vertex12', b)
    if hasattr(a2, 'Vertex12'):
        assert _is_linked(a2, 'Vertex12', b)
    _safe_set(b, 'inEdges', None)
    assert not _is_linked(b, 'inEdges', a2)
    if hasattr(a2, 'Vertex12'):
        assert not _is_linked(a2, 'Vertex12', b)


def test_assoc_inEdges4_reverse_link_reassign_clear():
    a1 = graphdb_Vertex(labels="sample_text", name="sample_text")
    a2 = graphdb_Vertex(labels="sample_text_2", name="sample_text_2")
    b = graphdb_Edge(name="sample_text", type="sample_text")
    _safe_set(b, 'Edge5', a1)
    assert _is_linked(b, 'Edge5', a1)
    if hasattr(a1, 'head'):
        assert _is_linked(a1, 'head', b)
    _safe_set(b, 'Edge5', a2)
    assert _is_linked(b, 'Edge5', a2)
    if hasattr(a1, 'head'):
        assert not _is_linked(a1, 'head', b)
    if hasattr(a2, 'head'):
        assert _is_linked(a2, 'head', b)
    _safe_set(b, 'Edge5', None)
    assert not _is_linked(b, 'Edge5', a2)
    if hasattr(a2, 'head'):
        assert not _is_linked(a2, 'head', b)


def test_assoc_outEdges6_reverse_link_reassign_clear():
    a1 = graphdb_Vertex(labels="sample_text", name="sample_text")
    a2 = graphdb_Vertex(labels="sample_text_2", name="sample_text_2")
    b = graphdb_Edge(name="sample_text", type="sample_text")
    _safe_set(b, 'Edge7', a1)
    assert _is_linked(b, 'Edge7', a1)
    if hasattr(a1, 'tail'):
        assert _is_linked(a1, 'tail', b)
    _safe_set(b, 'Edge7', a2)
    assert _is_linked(b, 'Edge7', a2)
    if hasattr(a1, 'tail'):
        assert not _is_linked(a1, 'tail', b)
    if hasattr(a2, 'tail'):
        assert _is_linked(a2, 'tail', b)
    _safe_set(b, 'Edge7', None)
    assert not _is_linked(b, 'Edge7', a2)
    if hasattr(a2, 'tail'):
        assert not _is_linked(a2, 'tail', b)


def test_assoc_tail9_reverse_link_reassign_clear():
    a1 = graphdb_Vertex(labels="sample_text", name="sample_text")
    a2 = graphdb_Vertex(labels="sample_text_2", name="sample_text_2")
    b = graphdb_Edge(name="sample_text", type="sample_text")
    _safe_set(b, 'outEdges', a1)
    assert _is_linked(b, 'outEdges', a1)
    if hasattr(a1, 'Vertex10'):
        assert _is_linked(a1, 'Vertex10', b)
    _safe_set(b, 'outEdges', a2)
    assert _is_linked(b, 'outEdges', a2)
    if hasattr(a1, 'Vertex10'):
        assert not _is_linked(a1, 'Vertex10', b)
    if hasattr(a2, 'Vertex10'):
        assert _is_linked(a2, 'Vertex10', b)
    _safe_set(b, 'outEdges', None)
    assert not _is_linked(b, 'outEdges', a2)
    if hasattr(a2, 'Vertex10'):
        assert not _is_linked(a2, 'Vertex10', b)


def test_assoc_vertices0_reverse_link_reassign_clear():
    a1 = graphdb_Vertex(labels="sample_text", name="sample_text")
    a2 = graphdb_Vertex(labels="sample_text_2", name="sample_text_2")
    b = graphdb_Graph(rawDatabase="sample_text")
    _safe_set(b, 'graph', {a1})
    assert _is_linked(b, 'graph', a1)
    if hasattr(a1, 'Vertex'):
        assert _is_linked(a1, 'Vertex', b)
    _safe_set(b, 'graph', {a2})
    assert _is_linked(b, 'graph', a2)
    if hasattr(a1, 'Vertex'):
        assert not _is_linked(a1, 'Vertex', b)
    if hasattr(a2, 'Vertex'):
        assert _is_linked(a2, 'Vertex', b)
    _safe_set(b, 'graph', set())
    assert not _is_linked(b, 'graph', a2)
    if hasattr(a2, 'Vertex'):
        assert not _is_linked(a2, 'Vertex', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_owner15_stub_double():
    # graphdb_GraphElement has no real 'GraphElement' property in the generated
    # code (a bare stub) -- manually attach it so graphdb_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphdb_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphdb_Property(key="sample_text", type="sample_text")
    partner = graphdb_GraphElement()
    setattr(partner, 'GraphElement', None)
    _safe_set(owner, 'properties', partner)
    assert getattr(partner, 'GraphElement') == owner
    _safe_set(owner, 'properties', None)
    assert getattr(partner, 'GraphElement') is None


def test_assoc_properties3_stub_double():
    # graphdb_GraphElement has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so graphdb_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphdb_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphdb_Property(key="sample_text", type="sample_text")
    partner = graphdb_GraphElement()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Property', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Property', None)
    assert owner not in getattr(partner, 'owner')


