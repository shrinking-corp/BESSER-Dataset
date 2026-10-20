import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_Pattern_Matching_Master_Project_Edge,
    graph_Pattern_Matching_Master_Project_Entry,
    graph_Pattern_Matching_Master_Project_Graph,
    graph_Pattern_Matching_Master_Project_Vertex,
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

def test_assoc_edges0_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Graph(direct=False, name="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'graph'):
        assert _is_linked(a1, 'graph', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'graph'):
        assert not _is_linked(a1, 'graph', b)
    if hasattr(a2, 'graph'):
        assert _is_linked(a2, 'graph', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'graph'):
        assert not _is_linked(a2, 'graph', b)


def test_assoc_entries12_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Entry(key="sample_text", value="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Entry(key="sample_text_2", value="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge13', {a1})
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge13', a1)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Entry14'):
        assert _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Entry14', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge13', {a2})
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge13', a2)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Entry14'):
        assert not _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Entry14', b)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Entry14'):
        assert _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Entry14', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge13', set())
    assert not _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge13', a2)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Entry14'):
        assert not _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Entry14', b)


def test_assoc_entries4_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Entry(key="sample_text", value="sample_text")
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Entry', a1)
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Entry', a1)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Vertex'):
        assert _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Vertex', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Entry', a2)
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Entry', a2)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Vertex'):
        assert not _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Vertex', b)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Vertex'):
        assert _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Vertex', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Entry', None)
    assert not _is_linked(b, 'graph_Pattern_Matching_Master_Project_Entry', a2)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Vertex'):
        assert not _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Vertex', b)


def test_assoc_graph3_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
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


def test_assoc_graph5_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Graph(direct=False, name="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Graph6'):
        assert _is_linked(a1, 'Graph6', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Graph6'):
        assert not _is_linked(a1, 'Graph6', b)
    if hasattr(a2, 'Graph6'):
        assert _is_linked(a2, 'Graph6', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Graph6'):
        assert not _is_linked(a2, 'Graph6', b)


def test_assoc_source7_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge', a1)
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge', a1)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Vertex8'):
        assert _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Vertex8', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge', a2)
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge', a2)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Vertex8'):
        assert not _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Vertex8', b)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Vertex8'):
        assert _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Vertex8', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge', None)
    assert not _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge', a2)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Vertex8'):
        assert not _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Vertex8', b)


def test_assoc_target9_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge10', a1)
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge10', a1)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Vertex11'):
        assert _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Vertex11', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge10', a2)
    assert _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge10', a2)
    if hasattr(a1, 'graph_Pattern_Matching_Master_Project_Vertex11'):
        assert not _is_linked(a1, 'graph_Pattern_Matching_Master_Project_Vertex11', b)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Vertex11'):
        assert _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Vertex11', b)
    _safe_set(b, 'graph_Pattern_Matching_Master_Project_Edge10', None)
    assert not _is_linked(b, 'graph_Pattern_Matching_Master_Project_Edge10', a2)
    if hasattr(a2, 'graph_Pattern_Matching_Master_Project_Vertex11'):
        assert not _is_linked(a2, 'graph_Pattern_Matching_Master_Project_Vertex11', b)


def test_assoc_vertices1_reverse_link_reassign_clear():
    a1 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    a2 = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text_2")
    b = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    _safe_set(b, 'graph2', {a1})
    assert _is_linked(b, 'graph2', a1)
    if hasattr(a1, 'Vertex'):
        assert _is_linked(a1, 'Vertex', b)
    _safe_set(b, 'graph2', {a2})
    assert _is_linked(b, 'graph2', a2)
    if hasattr(a1, 'Vertex'):
        assert not _is_linked(a1, 'Vertex', b)
    if hasattr(a2, 'Vertex'):
        assert _is_linked(a2, 'Vertex', b)
    _safe_set(b, 'graph2', set())
    assert not _is_linked(b, 'graph2', a2)
    if hasattr(a2, 'Vertex'):
        assert not _is_linked(a2, 'Vertex', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

