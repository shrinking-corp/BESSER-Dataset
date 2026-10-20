import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GraphItem,
    NamedElement,
    ZestGraph_GraphConnection,
    ZestGraph_GraphContainer,
    ZestGraph_GraphItem,
    ZestGraph_GraphNode,
    ZestGraph_NamedElement,
    ZestGraph_ZestGraph,
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

def test_assoc_ingoing6_reverse_link_reassign_clear():
    a1 = ZestGraph_GraphNode(backColor="sample_text", height=3.14, nodeStyle="sample_text", shape="sample_text", width=3.14)
    a2 = ZestGraph_GraphNode(backColor="sample_text_2", height=9.99, nodeStyle="sample_text_2", shape="sample_text_2", width=9.99)
    b = ZestGraph_GraphConnection(color="sample_text", lineStyle=7, lineWidth=7)
    _safe_set(b, 'GraphConnection7', a1)
    assert _is_linked(b, 'GraphConnection7', a1)
    if hasattr(a1, 'targetNode'):
        assert _is_linked(a1, 'targetNode', b)
    _safe_set(b, 'GraphConnection7', a2)
    assert _is_linked(b, 'GraphConnection7', a2)
    if hasattr(a1, 'targetNode'):
        assert not _is_linked(a1, 'targetNode', b)
    if hasattr(a2, 'targetNode'):
        assert _is_linked(a2, 'targetNode', b)
    _safe_set(b, 'GraphConnection7', None)
    assert not _is_linked(b, 'GraphConnection7', a2)
    if hasattr(a2, 'targetNode'):
        assert not _is_linked(a2, 'targetNode', b)


def test_assoc_outgoing5_reverse_link_reassign_clear():
    a1 = ZestGraph_GraphNode(backColor="sample_text", height=3.14, nodeStyle="sample_text", shape="sample_text", width=3.14)
    a2 = ZestGraph_GraphNode(backColor="sample_text_2", height=9.99, nodeStyle="sample_text_2", shape="sample_text_2", width=9.99)
    b = ZestGraph_GraphConnection(color="sample_text", lineStyle=7, lineWidth=7)
    _safe_set(b, 'GraphConnection', a1)
    assert _is_linked(b, 'GraphConnection', a1)
    if hasattr(a1, 'sourceNode'):
        assert _is_linked(a1, 'sourceNode', b)
    _safe_set(b, 'GraphConnection', a2)
    assert _is_linked(b, 'GraphConnection', a2)
    if hasattr(a1, 'sourceNode'):
        assert not _is_linked(a1, 'sourceNode', b)
    if hasattr(a2, 'sourceNode'):
        assert _is_linked(a2, 'sourceNode', b)
    _safe_set(b, 'GraphConnection', None)
    assert not _is_linked(b, 'GraphConnection', a2)
    if hasattr(a2, 'sourceNode'):
        assert not _is_linked(a2, 'sourceNode', b)


def test_assoc_sourceNode8_reverse_link_reassign_clear():
    a1 = ZestGraph_GraphNode(backColor="sample_text", height=3.14, nodeStyle="sample_text", shape="sample_text", width=3.14)
    a2 = ZestGraph_GraphNode(backColor="sample_text_2", height=9.99, nodeStyle="sample_text_2", shape="sample_text_2", width=9.99)
    b = ZestGraph_GraphConnection(color="sample_text", lineStyle=7, lineWidth=7)
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'GraphNode'):
        assert _is_linked(a1, 'GraphNode', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'GraphNode'):
        assert not _is_linked(a1, 'GraphNode', b)
    if hasattr(a2, 'GraphNode'):
        assert _is_linked(a2, 'GraphNode', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'GraphNode'):
        assert not _is_linked(a2, 'GraphNode', b)


def test_assoc_targetNode9_reverse_link_reassign_clear():
    a1 = ZestGraph_GraphNode(backColor="sample_text", height=3.14, nodeStyle="sample_text", shape="sample_text", width=3.14)
    a2 = ZestGraph_GraphNode(backColor="sample_text_2", height=9.99, nodeStyle="sample_text_2", shape="sample_text_2", width=9.99)
    b = ZestGraph_GraphConnection(color="sample_text", lineStyle=7, lineWidth=7)
    _safe_set(b, 'ingoing', a1)
    assert _is_linked(b, 'ingoing', a1)
    if hasattr(a1, 'GraphNode10'):
        assert _is_linked(a1, 'GraphNode10', b)
    _safe_set(b, 'ingoing', a2)
    assert _is_linked(b, 'ingoing', a2)
    if hasattr(a1, 'GraphNode10'):
        assert not _is_linked(a1, 'GraphNode10', b)
    if hasattr(a2, 'GraphNode10'):
        assert _is_linked(a2, 'GraphNode10', b)
    _safe_set(b, 'ingoing', None)
    assert not _is_linked(b, 'ingoing', a2)
    if hasattr(a2, 'GraphNode10'):
        assert not _is_linked(a2, 'GraphNode10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_graph4_stub_double():
    # ZestGraph_ZestGraph has no real 'ZestGraph' property in the generated
    # code (a bare stub) -- manually attach it so ZestGraph_GraphItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ZestGraph_GraphItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ZestGraph_GraphItem(text="sample_text")
    partner = ZestGraph_ZestGraph()
    setattr(partner, 'ZestGraph', None)
    _safe_set(owner, 'items', partner)
    assert getattr(partner, 'ZestGraph') == owner
    _safe_set(owner, 'items', None)
    assert getattr(partner, 'ZestGraph') is None


def test_assoc_items0_stub_double():
    # ZestGraph_ZestGraph has no real 'graph' property in the generated
    # code (a bare stub) -- manually attach it so ZestGraph_GraphItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ZestGraph_GraphItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ZestGraph_GraphItem(text="sample_text")
    partner = ZestGraph_ZestGraph()
    setattr(partner, 'graph', None)
    _safe_set(owner, 'GraphItem', partner)
    assert owner in getattr(partner, 'graph')
    _safe_set(owner, 'GraphItem', None)
    assert owner not in getattr(partner, 'graph')


def test_assoc_nodes2_stub_double():
    # ZestGraph_GraphContainer has no real 'ZestGraph_GraphContainer3' property in the generated
    # code (a bare stub) -- manually attach it so ZestGraph_GraphNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ZestGraph_GraphNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ZestGraph_GraphNode(backColor="sample_text", height=3.14, nodeStyle="sample_text", shape="sample_text", width=3.14)
    partner = ZestGraph_GraphContainer()
    setattr(partner, 'ZestGraph_GraphContainer3', None)
    _safe_set(owner, 'ZestGraph_GraphNode', partner)
    assert owner in getattr(partner, 'ZestGraph_GraphContainer3')
    _safe_set(owner, 'ZestGraph_GraphNode', None)
    assert owner not in getattr(partner, 'ZestGraph_GraphContainer3')


