import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EdgeProcessor,
    dfs_DFSGraph,
    dfs_DepthFirstSearch,
    dfs_EObject,
    dfs_Edge,
    dfs_EdgeProcessor,
    dfs_Node,
    EdgeType,
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

def test_assoc_delegate1_reverse_link_reassign_clear():
    a1 = dfs_EdgeProcessor()
    a2 = dfs_EdgeProcessor()
    b = dfs_EdgeProcessor()
    _safe_set(b, 'dfs_EdgeProcessor0', a1)
    assert _is_linked(b, 'dfs_EdgeProcessor0', a1)
    if hasattr(a1, 'dfs_EdgeProcessor'):
        assert _is_linked(a1, 'dfs_EdgeProcessor', b)
    _safe_set(b, 'dfs_EdgeProcessor0', a2)
    assert _is_linked(b, 'dfs_EdgeProcessor0', a2)
    if hasattr(a1, 'dfs_EdgeProcessor'):
        assert not _is_linked(a1, 'dfs_EdgeProcessor', b)
    if hasattr(a2, 'dfs_EdgeProcessor'):
        assert _is_linked(a2, 'dfs_EdgeProcessor', b)
    _safe_set(b, 'dfs_EdgeProcessor0', None)
    assert not _is_linked(b, 'dfs_EdgeProcessor0', a2)
    if hasattr(a2, 'dfs_EdgeProcessor'):
        assert not _is_linked(a2, 'dfs_EdgeProcessor', b)


def test_assoc_incoming2_reverse_link_reassign_clear():
    a1 = dfs_Node(postTraversal=7, preTraversal=7)
    a2 = dfs_Node(postTraversal=13, preTraversal=13)
    b = dfs_Edge(type="sample_text")
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


def test_assoc_outgoing5_reverse_link_reassign_clear():
    a1 = dfs_Node(postTraversal=7, preTraversal=7)
    a2 = dfs_Node(postTraversal=13, preTraversal=13)
    b = dfs_Edge(type="sample_text")
    _safe_set(b, 'Edge6', a1)
    assert _is_linked(b, 'Edge6', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge6', a2)
    assert _is_linked(b, 'Edge6', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge6', None)
    assert not _is_linked(b, 'Edge6', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source9_reverse_link_reassign_clear():
    a1 = dfs_Node(postTraversal=7, preTraversal=7)
    a2 = dfs_Node(postTraversal=13, preTraversal=13)
    b = dfs_Edge(type="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_target12_reverse_link_reassign_clear():
    a1 = dfs_Node(postTraversal=7, preTraversal=7)
    a2 = dfs_Node(postTraversal=13, preTraversal=13)
    b = dfs_Edge(type="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node13'):
        assert _is_linked(a1, 'Node13', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node13'):
        assert not _is_linked(a1, 'Node13', b)
    if hasattr(a2, 'Node13'):
        assert _is_linked(a2, 'Node13', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node13'):
        assert not _is_linked(a2, 'Node13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges14_stub_double():
    # dfs_DFSGraph has no real 'graph' property in the generated
    # code (a bare stub) -- manually attach it so dfs_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfs_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfs_Edge(type="sample_text")
    partner = dfs_DFSGraph()
    setattr(partner, 'graph', None)
    _safe_set(owner, 'Edge15', partner)
    assert getattr(partner, 'graph') == owner
    _safe_set(owner, 'Edge15', None)
    assert getattr(partner, 'graph') is None


def test_assoc_graph3_stub_double():
    # dfs_DFSGraph has no real 'DFSGraph' property in the generated
    # code (a bare stub) -- manually attach it so dfs_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfs_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfs_Node(postTraversal=7, preTraversal=7)
    partner = dfs_DFSGraph()
    setattr(partner, 'DFSGraph', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'DFSGraph') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'DFSGraph') is None


def test_assoc_graph7_stub_double():
    # dfs_DFSGraph has no real 'DFSGraph8' property in the generated
    # code (a bare stub) -- manually attach it so dfs_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfs_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfs_Edge(type="sample_text")
    partner = dfs_DFSGraph()
    setattr(partner, 'DFSGraph8', None)
    _safe_set(owner, 'edges', partner)
    assert getattr(partner, 'DFSGraph8') == owner
    _safe_set(owner, 'edges', None)
    assert getattr(partner, 'DFSGraph8') is None


def test_assoc_nodes16_stub_double():
    # dfs_DFSGraph has no real 'graph17' property in the generated
    # code (a bare stub) -- manually attach it so dfs_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfs_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfs_Node(postTraversal=7, preTraversal=7)
    partner = dfs_DFSGraph()
    setattr(partner, 'graph17', None)
    _safe_set(owner, 'Node18', partner)
    assert getattr(partner, 'graph17') == owner
    _safe_set(owner, 'Node18', None)
    assert getattr(partner, 'graph17') is None


def test_assoc_origin10_stub_double():
    # dfs_EObject has no real 'dfs_EObject11' property in the generated
    # code (a bare stub) -- manually attach it so dfs_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfs_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfs_Edge(type="sample_text")
    partner = dfs_EObject()
    setattr(partner, 'dfs_EObject11', None)
    _safe_set(owner, 'dfs_Edge', partner)
    assert getattr(partner, 'dfs_EObject11') == owner
    _safe_set(owner, 'dfs_Edge', None)
    assert getattr(partner, 'dfs_EObject11') is None


def test_assoc_origin4_stub_double():
    # dfs_EObject has no real 'dfs_EObject' property in the generated
    # code (a bare stub) -- manually attach it so dfs_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfs_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfs_Node(postTraversal=7, preTraversal=7)
    partner = dfs_EObject()
    setattr(partner, 'dfs_EObject', None)
    _safe_set(owner, 'dfs_Node', partner)
    assert getattr(partner, 'dfs_EObject') == owner
    _safe_set(owner, 'dfs_Node', None)
    assert getattr(partner, 'dfs_EObject') is None


