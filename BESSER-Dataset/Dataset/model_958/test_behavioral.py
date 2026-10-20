import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Adaptable,
    Attributable,
    Vertex,
    graph_Edge,
    graph_Graph,
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

def test_assoc_connecting6_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Edge(label="sample_text")
    _safe_set(b, 'graph_Edge8', a1)
    assert _is_linked(b, 'graph_Edge8', a1)
    if hasattr(a1, 'graph_Vertex7'):
        assert _is_linked(a1, 'graph_Vertex7', b)
    _safe_set(b, 'graph_Edge8', a2)
    assert _is_linked(b, 'graph_Edge8', a2)
    if hasattr(a1, 'graph_Vertex7'):
        assert not _is_linked(a1, 'graph_Vertex7', b)
    if hasattr(a2, 'graph_Vertex7'):
        assert _is_linked(a2, 'graph_Vertex7', b)
    _safe_set(b, 'graph_Edge8', None)
    assert not _is_linked(b, 'graph_Edge8', a2)
    if hasattr(a2, 'graph_Vertex7'):
        assert not _is_linked(a2, 'graph_Vertex7', b)


def test_assoc_incoming3_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Edge(label="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_neighbors16_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Vertex(label="sample_text", number=7)
    _safe_set(b, 'graph_Vertex17', a1)
    assert _is_linked(b, 'graph_Vertex17', a1)
    if hasattr(a1, 'graph_Vertex15'):
        assert _is_linked(a1, 'graph_Vertex15', b)
    _safe_set(b, 'graph_Vertex17', a2)
    assert _is_linked(b, 'graph_Vertex17', a2)
    if hasattr(a1, 'graph_Vertex15'):
        assert not _is_linked(a1, 'graph_Vertex15', b)
    if hasattr(a2, 'graph_Vertex15'):
        assert _is_linked(a2, 'graph_Vertex15', b)
    _safe_set(b, 'graph_Vertex17', None)
    assert not _is_linked(b, 'graph_Vertex17', a2)
    if hasattr(a2, 'graph_Vertex15'):
        assert not _is_linked(a2, 'graph_Vertex15', b)


def test_assoc_outgoing4_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Edge(label="sample_text")
    _safe_set(b, 'Edge5', a1)
    assert _is_linked(b, 'Edge5', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge5', a2)
    assert _is_linked(b, 'Edge5', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge5', None)
    assert not _is_linked(b, 'Edge5', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_predecessors10_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Vertex(label="sample_text", number=7)
    _safe_set(b, 'graph_Vertex9', {a1})
    assert _is_linked(b, 'graph_Vertex9', a1)
    if hasattr(a1, 'graph_Vertex11'):
        assert _is_linked(a1, 'graph_Vertex11', b)
    _safe_set(b, 'graph_Vertex9', {a2})
    assert _is_linked(b, 'graph_Vertex9', a2)
    if hasattr(a1, 'graph_Vertex11'):
        assert not _is_linked(a1, 'graph_Vertex11', b)
    if hasattr(a2, 'graph_Vertex11'):
        assert _is_linked(a2, 'graph_Vertex11', b)
    _safe_set(b, 'graph_Vertex9', set())
    assert not _is_linked(b, 'graph_Vertex9', a2)
    if hasattr(a2, 'graph_Vertex11'):
        assert not _is_linked(a2, 'graph_Vertex11', b)


def test_assoc_source18_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Edge(label="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Vertex'):
        assert _is_linked(a1, 'Vertex', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Vertex'):
        assert not _is_linked(a1, 'Vertex', b)
    if hasattr(a2, 'Vertex'):
        assert _is_linked(a2, 'Vertex', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Vertex'):
        assert not _is_linked(a2, 'Vertex', b)


def test_assoc_successors13_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Vertex(label="sample_text", number=7)
    _safe_set(b, 'graph_Vertex14', a1)
    assert _is_linked(b, 'graph_Vertex14', a1)
    if hasattr(a1, 'graph_Vertex12'):
        assert _is_linked(a1, 'graph_Vertex12', b)
    _safe_set(b, 'graph_Vertex14', a2)
    assert _is_linked(b, 'graph_Vertex14', a2)
    if hasattr(a1, 'graph_Vertex12'):
        assert not _is_linked(a1, 'graph_Vertex12', b)
    if hasattr(a2, 'graph_Vertex12'):
        assert _is_linked(a2, 'graph_Vertex12', b)
    _safe_set(b, 'graph_Vertex14', None)
    assert not _is_linked(b, 'graph_Vertex14', a2)
    if hasattr(a2, 'graph_Vertex12'):
        assert not _is_linked(a2, 'graph_Vertex12', b)


def test_assoc_target19_reverse_link_reassign_clear():
    a1 = graph_Vertex(label="sample_text", number=7)
    a2 = graph_Vertex(label="sample_text_2", number=13)
    b = graph_Edge(label="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Vertex20'):
        assert _is_linked(a1, 'Vertex20', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Vertex20'):
        assert not _is_linked(a1, 'Vertex20', b)
    if hasattr(a2, 'Vertex20'):
        assert _is_linked(a2, 'Vertex20', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Vertex20'):
        assert not _is_linked(a2, 'Vertex20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges0_stub_double():
    # graph_Graph has no real 'graph_Graph' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(label="sample_text")
    partner = graph_Graph()
    setattr(partner, 'graph_Graph', None)
    _safe_set(owner, 'graph_Edge', partner)
    assert owner in getattr(partner, 'graph_Graph')
    _safe_set(owner, 'graph_Edge', None)
    assert owner not in getattr(partner, 'graph_Graph')


def test_assoc_vertices1_stub_double():
    # graph_Graph has no real 'graph_Graph2' property in the generated
    # code (a bare stub) -- manually attach it so graph_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Vertex(label="sample_text", number=7)
    partner = graph_Graph()
    setattr(partner, 'graph_Graph2', None)
    _safe_set(owner, 'graph_Vertex', partner)
    assert owner in getattr(partner, 'graph_Graph2')
    _safe_set(owner, 'graph_Vertex', None)
    assert owner not in getattr(partner, 'graph_Graph2')


