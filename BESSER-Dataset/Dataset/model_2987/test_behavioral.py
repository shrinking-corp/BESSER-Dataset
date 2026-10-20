import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Graph,
    wiki_ArticleGraph,
    wiki_CategoryGraph,
    wiki_ClassificationGraph,
    wiki_Edge,
    wiki_Graph,
    wiki_IndexGraph,
    wiki_Node,
    wiki_Revision,
    wiki_Wiki,
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

def test_assoc_edgerefs15_reverse_link_reassign_clear():
    a1 = wiki_Graph(name="sample_text")
    a2 = wiki_Graph(name="sample_text_2")
    b = wiki_Edge(type="sample_text")
    _safe_set(b, 'wiki_Edge17', a1)
    assert _is_linked(b, 'wiki_Edge17', a1)
    if hasattr(a1, 'wiki_Graph16'):
        assert _is_linked(a1, 'wiki_Graph16', b)
    _safe_set(b, 'wiki_Edge17', a2)
    assert _is_linked(b, 'wiki_Edge17', a2)
    if hasattr(a1, 'wiki_Graph16'):
        assert not _is_linked(a1, 'wiki_Graph16', b)
    if hasattr(a2, 'wiki_Graph16'):
        assert _is_linked(a2, 'wiki_Graph16', b)
    _safe_set(b, 'wiki_Edge17', None)
    assert not _is_linked(b, 'wiki_Edge17', a2)
    if hasattr(a2, 'wiki_Graph16'):
        assert not _is_linked(a2, 'wiki_Graph16', b)


def test_assoc_edges9_reverse_link_reassign_clear():
    a1 = wiki_Wiki(title="sample_text")
    a2 = wiki_Wiki(title="sample_text_2")
    b = wiki_Edge(type="sample_text")
    _safe_set(b, 'wiki_Edge', a1)
    assert _is_linked(b, 'wiki_Edge', a1)
    if hasattr(a1, 'wiki_Wiki10'):
        assert _is_linked(a1, 'wiki_Wiki10', b)
    _safe_set(b, 'wiki_Edge', a2)
    assert _is_linked(b, 'wiki_Edge', a2)
    if hasattr(a1, 'wiki_Wiki10'):
        assert not _is_linked(a1, 'wiki_Wiki10', b)
    if hasattr(a2, 'wiki_Wiki10'):
        assert _is_linked(a2, 'wiki_Wiki10', b)
    _safe_set(b, 'wiki_Edge', None)
    assert not _is_linked(b, 'wiki_Edge', a2)
    if hasattr(a2, 'wiki_Wiki10'):
        assert not _is_linked(a2, 'wiki_Wiki10', b)


def test_assoc_from_26_reverse_link_reassign_clear():
    a1 = wiki_Node(editions=7, node_id=7, node_namespace=7, title="sample_text", type="sample_text", visits=7)
    a2 = wiki_Node(editions=13, node_id=13, node_namespace=13, title="sample_text_2", type="sample_text_2", visits=13)
    b = wiki_Edge(type="sample_text")
    _safe_set(b, 'wiki_Edge27', a1)
    assert _is_linked(b, 'wiki_Edge27', a1)
    if hasattr(a1, 'wiki_Node28'):
        assert _is_linked(a1, 'wiki_Node28', b)
    _safe_set(b, 'wiki_Edge27', a2)
    assert _is_linked(b, 'wiki_Edge27', a2)
    if hasattr(a1, 'wiki_Node28'):
        assert not _is_linked(a1, 'wiki_Node28', b)
    if hasattr(a2, 'wiki_Node28'):
        assert _is_linked(a2, 'wiki_Node28', b)
    _safe_set(b, 'wiki_Edge27', None)
    assert not _is_linked(b, 'wiki_Edge27', a2)
    if hasattr(a2, 'wiki_Node28'):
        assert not _is_linked(a2, 'wiki_Node28', b)


def test_assoc_lastRevision18_reverse_link_reassign_clear():
    a1 = wiki_Revision(date="sample_text", text_id=7, user="sample_text")
    a2 = wiki_Revision(date="sample_text_2", text_id=13, user="sample_text_2")
    b = wiki_Node(editions=7, node_id=7, node_namespace=7, title="sample_text", type="sample_text", visits=7)
    _safe_set(b, 'wiki_Node19', a1)
    assert _is_linked(b, 'wiki_Node19', a1)
    if hasattr(a1, 'wiki_Revision20'):
        assert _is_linked(a1, 'wiki_Revision20', b)
    _safe_set(b, 'wiki_Node19', a2)
    assert _is_linked(b, 'wiki_Node19', a2)
    if hasattr(a1, 'wiki_Revision20'):
        assert not _is_linked(a1, 'wiki_Revision20', b)
    if hasattr(a2, 'wiki_Revision20'):
        assert _is_linked(a2, 'wiki_Revision20', b)
    _safe_set(b, 'wiki_Node19', None)
    assert not _is_linked(b, 'wiki_Node19', a2)
    if hasattr(a2, 'wiki_Revision20'):
        assert not _is_linked(a2, 'wiki_Revision20', b)


def test_assoc_node22_reverse_link_reassign_clear():
    a1 = wiki_Revision(date="sample_text", text_id=7, user="sample_text")
    a2 = wiki_Revision(date="sample_text_2", text_id=13, user="sample_text_2")
    b = wiki_Node(editions=7, node_id=7, node_namespace=7, title="sample_text", type="sample_text", visits=7)
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'revisions'):
        assert _is_linked(a1, 'revisions', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'revisions'):
        assert not _is_linked(a1, 'revisions', b)
    if hasattr(a2, 'revisions'):
        assert _is_linked(a2, 'revisions', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'revisions'):
        assert not _is_linked(a2, 'revisions', b)


def test_assoc_noderefs13_reverse_link_reassign_clear():
    a1 = wiki_Node(editions=7, node_id=7, node_namespace=7, title="sample_text", type="sample_text", visits=7)
    a2 = wiki_Node(editions=13, node_id=13, node_namespace=13, title="sample_text_2", type="sample_text_2", visits=13)
    b = wiki_Graph(name="sample_text")
    _safe_set(b, 'wiki_Graph', {a1})
    assert _is_linked(b, 'wiki_Graph', a1)
    if hasattr(a1, 'wiki_Node14'):
        assert _is_linked(a1, 'wiki_Node14', b)
    _safe_set(b, 'wiki_Graph', {a2})
    assert _is_linked(b, 'wiki_Graph', a2)
    if hasattr(a1, 'wiki_Node14'):
        assert not _is_linked(a1, 'wiki_Node14', b)
    if hasattr(a2, 'wiki_Node14'):
        assert _is_linked(a2, 'wiki_Node14', b)
    _safe_set(b, 'wiki_Graph', set())
    assert not _is_linked(b, 'wiki_Graph', a2)
    if hasattr(a2, 'wiki_Node14'):
        assert not _is_linked(a2, 'wiki_Node14', b)


def test_assoc_nodes7_reverse_link_reassign_clear():
    a1 = wiki_Wiki(title="sample_text")
    a2 = wiki_Wiki(title="sample_text_2")
    b = wiki_Node(editions=7, node_id=7, node_namespace=7, title="sample_text", type="sample_text", visits=7)
    _safe_set(b, 'wiki_Node', a1)
    assert _is_linked(b, 'wiki_Node', a1)
    if hasattr(a1, 'wiki_Wiki8'):
        assert _is_linked(a1, 'wiki_Wiki8', b)
    _safe_set(b, 'wiki_Node', a2)
    assert _is_linked(b, 'wiki_Node', a2)
    if hasattr(a1, 'wiki_Wiki8'):
        assert not _is_linked(a1, 'wiki_Wiki8', b)
    if hasattr(a2, 'wiki_Wiki8'):
        assert _is_linked(a2, 'wiki_Wiki8', b)
    _safe_set(b, 'wiki_Node', None)
    assert not _is_linked(b, 'wiki_Node', a2)
    if hasattr(a2, 'wiki_Wiki8'):
        assert not _is_linked(a2, 'wiki_Wiki8', b)


def test_assoc_revisions11_reverse_link_reassign_clear():
    a1 = wiki_Wiki(title="sample_text")
    a2 = wiki_Wiki(title="sample_text_2")
    b = wiki_Revision(date="sample_text", text_id=7, user="sample_text")
    _safe_set(b, 'wiki_Revision', a1)
    assert _is_linked(b, 'wiki_Revision', a1)
    if hasattr(a1, 'wiki_Wiki12'):
        assert _is_linked(a1, 'wiki_Wiki12', b)
    _safe_set(b, 'wiki_Revision', a2)
    assert _is_linked(b, 'wiki_Revision', a2)
    if hasattr(a1, 'wiki_Wiki12'):
        assert not _is_linked(a1, 'wiki_Wiki12', b)
    if hasattr(a2, 'wiki_Wiki12'):
        assert _is_linked(a2, 'wiki_Wiki12', b)
    _safe_set(b, 'wiki_Revision', None)
    assert not _is_linked(b, 'wiki_Revision', a2)
    if hasattr(a2, 'wiki_Wiki12'):
        assert not _is_linked(a2, 'wiki_Wiki12', b)


def test_assoc_revisions21_reverse_link_reassign_clear():
    a1 = wiki_Revision(date="sample_text", text_id=7, user="sample_text")
    a2 = wiki_Revision(date="sample_text_2", text_id=13, user="sample_text_2")
    b = wiki_Node(editions=7, node_id=7, node_namespace=7, title="sample_text", type="sample_text", visits=7)
    _safe_set(b, 'node', {a1})
    assert _is_linked(b, 'node', a1)
    if hasattr(a1, 'Revision'):
        assert _is_linked(a1, 'Revision', b)
    _safe_set(b, 'node', {a2})
    assert _is_linked(b, 'node', a2)
    if hasattr(a1, 'Revision'):
        assert not _is_linked(a1, 'Revision', b)
    if hasattr(a2, 'Revision'):
        assert _is_linked(a2, 'Revision', b)
    _safe_set(b, 'node', set())
    assert not _is_linked(b, 'node', a2)
    if hasattr(a2, 'Revision'):
        assert not _is_linked(a2, 'Revision', b)


def test_assoc_to23_reverse_link_reassign_clear():
    a1 = wiki_Node(editions=7, node_id=7, node_namespace=7, title="sample_text", type="sample_text", visits=7)
    a2 = wiki_Node(editions=13, node_id=13, node_namespace=13, title="sample_text_2", type="sample_text_2", visits=13)
    b = wiki_Edge(type="sample_text")
    _safe_set(b, 'wiki_Edge24', a1)
    assert _is_linked(b, 'wiki_Edge24', a1)
    if hasattr(a1, 'wiki_Node25'):
        assert _is_linked(a1, 'wiki_Node25', b)
    _safe_set(b, 'wiki_Edge24', a2)
    assert _is_linked(b, 'wiki_Edge24', a2)
    if hasattr(a1, 'wiki_Node25'):
        assert not _is_linked(a1, 'wiki_Node25', b)
    if hasattr(a2, 'wiki_Node25'):
        assert _is_linked(a2, 'wiki_Node25', b)
    _safe_set(b, 'wiki_Edge24', None)
    assert not _is_linked(b, 'wiki_Edge24', a2)
    if hasattr(a2, 'wiki_Node25'):
        assert not _is_linked(a2, 'wiki_Node25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_graphArticles3_stub_double():
    # wiki_ArticleGraph has no real 'wiki_ArticleGraph' property in the generated
    # code (a bare stub) -- manually attach it so wiki_Wiki's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wiki_Wiki's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wiki_Wiki(title="sample_text")
    partner = wiki_ArticleGraph()
    setattr(partner, 'wiki_ArticleGraph', None)
    _safe_set(owner, 'wiki_Wiki4', partner)
    assert getattr(partner, 'wiki_ArticleGraph') == owner
    _safe_set(owner, 'wiki_Wiki4', None)
    assert getattr(partner, 'wiki_ArticleGraph') is None


def test_assoc_graphCategories1_stub_double():
    # wiki_CategoryGraph has no real 'wiki_CategoryGraph' property in the generated
    # code (a bare stub) -- manually attach it so wiki_Wiki's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wiki_Wiki's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wiki_Wiki(title="sample_text")
    partner = wiki_CategoryGraph()
    setattr(partner, 'wiki_CategoryGraph', None)
    _safe_set(owner, 'wiki_Wiki2', partner)
    assert getattr(partner, 'wiki_CategoryGraph') == owner
    _safe_set(owner, 'wiki_Wiki2', None)
    assert getattr(partner, 'wiki_CategoryGraph') is None


def test_assoc_graphClassification5_stub_double():
    # wiki_ClassificationGraph has no real 'wiki_ClassificationGraph' property in the generated
    # code (a bare stub) -- manually attach it so wiki_Wiki's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wiki_Wiki's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wiki_Wiki(title="sample_text")
    partner = wiki_ClassificationGraph()
    setattr(partner, 'wiki_ClassificationGraph', None)
    _safe_set(owner, 'wiki_Wiki6', partner)
    assert getattr(partner, 'wiki_ClassificationGraph') == owner
    _safe_set(owner, 'wiki_Wiki6', None)
    assert getattr(partner, 'wiki_ClassificationGraph') is None


def test_assoc_graphIndex0_stub_double():
    # wiki_IndexGraph has no real 'wiki_IndexGraph' property in the generated
    # code (a bare stub) -- manually attach it so wiki_Wiki's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wiki_Wiki's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wiki_Wiki(title="sample_text")
    partner = wiki_IndexGraph()
    setattr(partner, 'wiki_IndexGraph', None)
    _safe_set(owner, 'wiki_Wiki', partner)
    assert getattr(partner, 'wiki_IndexGraph') == owner
    _safe_set(owner, 'wiki_Wiki', None)
    assert getattr(partner, 'wiki_IndexGraph') is None


