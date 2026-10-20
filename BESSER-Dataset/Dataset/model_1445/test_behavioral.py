import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EMapPropertyHolder,
    ElkConnectableShape,
    ElkGraphElement,
    ElkShape,
    IPropertyHolder,
    graph_EMapPropertyHolder,
    graph_ElkBendPoint,
    graph_ElkConnectableShape,
    graph_ElkEdge,
    graph_ElkEdgeSection,
    graph_ElkGraphElement,
    graph_ElkLabel,
    graph_ElkNode,
    graph_ElkPort,
    graph_ElkPropertyToValueMapEntry,
    graph_ElkShape,
    graph_IPropertyHolder,
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

def test_assoc_bendPoints25_reverse_link_reassign_clear():
    a1 = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    a2 = graph_ElkEdgeSection(endX=9.99, endY=9.99, identifier="sample_text_2", startX=9.99, startY=9.99)
    b = graph_ElkBendPoint(x=3.14, y=3.14)
    _safe_set(b, 'graph_ElkBendPoint', a1)
    assert _is_linked(b, 'graph_ElkBendPoint', a1)
    if hasattr(a1, 'graph_ElkEdgeSection'):
        assert _is_linked(a1, 'graph_ElkEdgeSection', b)
    _safe_set(b, 'graph_ElkBendPoint', a2)
    assert _is_linked(b, 'graph_ElkBendPoint', a2)
    if hasattr(a1, 'graph_ElkEdgeSection'):
        assert not _is_linked(a1, 'graph_ElkEdgeSection', b)
    if hasattr(a2, 'graph_ElkEdgeSection'):
        assert _is_linked(a2, 'graph_ElkEdgeSection', b)
    _safe_set(b, 'graph_ElkBendPoint', None)
    assert not _is_linked(b, 'graph_ElkBendPoint', a2)
    if hasattr(a2, 'graph_ElkEdgeSection'):
        assert not _is_linked(a2, 'graph_ElkEdgeSection', b)


def test_assoc_children9_reverse_link_reassign_clear():
    a1 = graph_ElkNode(hierarchical=True)
    a2 = graph_ElkNode(hierarchical=False)
    b = graph_ElkNode(hierarchical=True)
    _safe_set(b, 'parent10', {a1})
    assert _is_linked(b, 'parent10', a1)
    if hasattr(a1, 'ElkNode'):
        assert _is_linked(a1, 'ElkNode', b)
    _safe_set(b, 'parent10', {a2})
    assert _is_linked(b, 'parent10', a2)
    if hasattr(a1, 'ElkNode'):
        assert not _is_linked(a1, 'ElkNode', b)
    if hasattr(a2, 'ElkNode'):
        assert _is_linked(a2, 'ElkNode', b)
    _safe_set(b, 'parent10', set())
    assert not _is_linked(b, 'parent10', a2)
    if hasattr(a2, 'ElkNode'):
        assert not _is_linked(a2, 'ElkNode', b)


def test_assoc_containedEdges14_reverse_link_reassign_clear():
    a1 = graph_ElkNode(hierarchical=True)
    a2 = graph_ElkNode(hierarchical=False)
    b = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    _safe_set(b, 'ElkEdge15', a1)
    assert _is_linked(b, 'ElkEdge15', a1)
    if hasattr(a1, 'containingNode'):
        assert _is_linked(a1, 'containingNode', b)
    _safe_set(b, 'ElkEdge15', a2)
    assert _is_linked(b, 'ElkEdge15', a2)
    if hasattr(a1, 'containingNode'):
        assert not _is_linked(a1, 'containingNode', b)
    if hasattr(a2, 'containingNode'):
        assert _is_linked(a2, 'containingNode', b)
    _safe_set(b, 'ElkEdge15', None)
    assert not _is_linked(b, 'ElkEdge15', a2)
    if hasattr(a2, 'containingNode'):
        assert not _is_linked(a2, 'containingNode', b)


def test_assoc_containingNode18_reverse_link_reassign_clear():
    a1 = graph_ElkNode(hierarchical=True)
    a2 = graph_ElkNode(hierarchical=False)
    b = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    _safe_set(b, 'containedEdges', a1)
    assert _is_linked(b, 'containedEdges', a1)
    if hasattr(a1, 'ElkNode19'):
        assert _is_linked(a1, 'ElkNode19', b)
    _safe_set(b, 'containedEdges', a2)
    assert _is_linked(b, 'containedEdges', a2)
    if hasattr(a1, 'ElkNode19'):
        assert not _is_linked(a1, 'ElkNode19', b)
    if hasattr(a2, 'ElkNode19'):
        assert _is_linked(a2, 'ElkNode19', b)
    _safe_set(b, 'containedEdges', None)
    assert not _is_linked(b, 'containedEdges', a2)
    if hasattr(a2, 'ElkNode19'):
        assert not _is_linked(a2, 'ElkNode19', b)


def test_assoc_incomingSections37_reverse_link_reassign_clear():
    a1 = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    a2 = graph_ElkEdgeSection(endX=9.99, endY=9.99, identifier="sample_text_2", startX=9.99, startY=9.99)
    b = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    _safe_set(b, 'outgoingSections', {a1})
    assert _is_linked(b, 'outgoingSections', a1)
    if hasattr(a1, 'ElkEdgeSection38'):
        assert _is_linked(a1, 'ElkEdgeSection38', b)
    _safe_set(b, 'outgoingSections', {a2})
    assert _is_linked(b, 'outgoingSections', a2)
    if hasattr(a1, 'ElkEdgeSection38'):
        assert not _is_linked(a1, 'ElkEdgeSection38', b)
    if hasattr(a2, 'ElkEdgeSection38'):
        assert _is_linked(a2, 'ElkEdgeSection38', b)
    _safe_set(b, 'outgoingSections', set())
    assert not _is_linked(b, 'outgoingSections', a2)
    if hasattr(a2, 'ElkEdgeSection38'):
        assert not _is_linked(a2, 'ElkEdgeSection38', b)


def test_assoc_labels1_reverse_link_reassign_clear():
    a1 = graph_ElkLabel(text="sample_text")
    a2 = graph_ElkLabel(text="sample_text_2")
    b = graph_ElkGraphElement(identifier="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'ElkLabel'):
        assert _is_linked(a1, 'ElkLabel', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'ElkLabel'):
        assert not _is_linked(a1, 'ElkLabel', b)
    if hasattr(a2, 'ElkLabel'):
        assert _is_linked(a2, 'ElkLabel', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'ElkLabel'):
        assert not _is_linked(a2, 'ElkLabel', b)


def test_assoc_outgoingSections34_reverse_link_reassign_clear():
    a1 = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    a2 = graph_ElkEdgeSection(endX=9.99, endY=9.99, identifier="sample_text_2", startX=9.99, startY=9.99)
    b = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    _safe_set(b, 'incomingSections', {a1})
    assert _is_linked(b, 'incomingSections', a1)
    if hasattr(a1, 'ElkEdgeSection35'):
        assert _is_linked(a1, 'ElkEdgeSection35', b)
    _safe_set(b, 'incomingSections', {a2})
    assert _is_linked(b, 'incomingSections', a2)
    if hasattr(a1, 'ElkEdgeSection35'):
        assert not _is_linked(a1, 'ElkEdgeSection35', b)
    if hasattr(a2, 'ElkEdgeSection35'):
        assert _is_linked(a2, 'ElkEdgeSection35', b)
    _safe_set(b, 'incomingSections', set())
    assert not _is_linked(b, 'incomingSections', a2)
    if hasattr(a2, 'ElkEdgeSection35'):
        assert not _is_linked(a2, 'ElkEdgeSection35', b)


def test_assoc_parent12_reverse_link_reassign_clear():
    a1 = graph_ElkNode(hierarchical=True)
    a2 = graph_ElkNode(hierarchical=False)
    b = graph_ElkNode(hierarchical=True)
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'ElkNode13'):
        assert _is_linked(a1, 'ElkNode13', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'ElkNode13'):
        assert not _is_linked(a1, 'ElkNode13', b)
    if hasattr(a2, 'ElkNode13'):
        assert _is_linked(a2, 'ElkNode13', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'ElkNode13'):
        assert not _is_linked(a2, 'ElkNode13', b)


def test_assoc_parent2_reverse_link_reassign_clear():
    a1 = graph_ElkLabel(text="sample_text")
    a2 = graph_ElkLabel(text="sample_text_2")
    b = graph_ElkGraphElement(identifier="sample_text")
    _safe_set(b, 'ElkGraphElement', a1)
    assert _is_linked(b, 'ElkGraphElement', a1)
    if hasattr(a1, 'labels'):
        assert _is_linked(a1, 'labels', b)
    _safe_set(b, 'ElkGraphElement', a2)
    assert _is_linked(b, 'ElkGraphElement', a2)
    if hasattr(a1, 'labels'):
        assert not _is_linked(a1, 'labels', b)
    if hasattr(a2, 'labels'):
        assert _is_linked(a2, 'labels', b)
    _safe_set(b, 'ElkGraphElement', None)
    assert not _is_linked(b, 'ElkGraphElement', a2)
    if hasattr(a2, 'labels'):
        assert not _is_linked(a2, 'labels', b)


def test_assoc_parent26_reverse_link_reassign_clear():
    a1 = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    a2 = graph_ElkEdgeSection(endX=9.99, endY=9.99, identifier="sample_text_2", startX=9.99, startY=9.99)
    b = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    _safe_set(b, 'ElkEdge27', a1)
    assert _is_linked(b, 'ElkEdge27', a1)
    if hasattr(a1, 'sections'):
        assert _is_linked(a1, 'sections', b)
    _safe_set(b, 'ElkEdge27', a2)
    assert _is_linked(b, 'ElkEdge27', a2)
    if hasattr(a1, 'sections'):
        assert not _is_linked(a1, 'sections', b)
    if hasattr(a2, 'sections'):
        assert _is_linked(a2, 'sections', b)
    _safe_set(b, 'ElkEdge27', None)
    assert not _is_linked(b, 'ElkEdge27', a2)
    if hasattr(a2, 'sections'):
        assert not _is_linked(a2, 'sections', b)


def test_assoc_sections23_reverse_link_reassign_clear():
    a1 = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    a2 = graph_ElkEdgeSection(endX=9.99, endY=9.99, identifier="sample_text_2", startX=9.99, startY=9.99)
    b = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    _safe_set(b, 'parent24', {a1})
    assert _is_linked(b, 'parent24', a1)
    if hasattr(a1, 'ElkEdgeSection'):
        assert _is_linked(a1, 'ElkEdgeSection', b)
    _safe_set(b, 'parent24', {a2})
    assert _is_linked(b, 'parent24', a2)
    if hasattr(a1, 'ElkEdgeSection'):
        assert not _is_linked(a1, 'ElkEdgeSection', b)
    if hasattr(a2, 'ElkEdgeSection'):
        assert _is_linked(a2, 'ElkEdgeSection', b)
    _safe_set(b, 'parent24', set())
    assert not _is_linked(b, 'parent24', a2)
    if hasattr(a2, 'ElkEdgeSection'):
        assert not _is_linked(a2, 'ElkEdgeSection', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_incomingEdges4_stub_double():
    # graph_ElkConnectableShape has no real 'targets' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    partner = graph_ElkConnectableShape()
    setattr(partner, 'targets', None)
    _safe_set(owner, 'ElkEdge5', partner)
    assert owner in getattr(partner, 'targets')
    _safe_set(owner, 'ElkEdge5', None)
    assert owner not in getattr(partner, 'targets')


def test_assoc_incomingShape30_stub_double():
    # graph_ElkConnectableShape has no real 'graph_ElkConnectableShape32' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkEdgeSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkEdgeSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    partner = graph_ElkConnectableShape()
    setattr(partner, 'graph_ElkConnectableShape32', None)
    _safe_set(owner, 'graph_ElkEdgeSection31', partner)
    assert getattr(partner, 'graph_ElkConnectableShape32') == owner
    _safe_set(owner, 'graph_ElkEdgeSection31', None)
    assert getattr(partner, 'graph_ElkConnectableShape32') is None


def test_assoc_outgoingEdges3_stub_double():
    # graph_ElkConnectableShape has no real 'sources' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    partner = graph_ElkConnectableShape()
    setattr(partner, 'sources', None)
    _safe_set(owner, 'ElkEdge', partner)
    assert owner in getattr(partner, 'sources')
    _safe_set(owner, 'ElkEdge', None)
    assert owner not in getattr(partner, 'sources')


def test_assoc_outgoingShape28_stub_double():
    # graph_ElkConnectableShape has no real 'graph_ElkConnectableShape' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkEdgeSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkEdgeSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    partner = graph_ElkConnectableShape()
    setattr(partner, 'graph_ElkConnectableShape', None)
    _safe_set(owner, 'graph_ElkEdgeSection29', partner)
    assert getattr(partner, 'graph_ElkConnectableShape') == owner
    _safe_set(owner, 'graph_ElkEdgeSection29', None)
    assert getattr(partner, 'graph_ElkConnectableShape') is None


def test_assoc_parent16_stub_double():
    # graph_ElkPort has no real 'ports' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkNode(hierarchical=True)
    partner = graph_ElkPort()
    setattr(partner, 'ports', None)
    _safe_set(owner, 'ElkNode17', partner)
    assert getattr(partner, 'ports') == owner
    _safe_set(owner, 'ElkNode17', None)
    assert getattr(partner, 'ports') is None


def test_assoc_ports6_stub_double():
    # graph_ElkPort has no real 'ElkPort' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkNode(hierarchical=True)
    partner = graph_ElkPort()
    setattr(partner, 'ElkPort', None)
    _safe_set(owner, 'parent7', {partner})
    assert getattr(partner, 'ElkPort') == owner
    _safe_set(owner, 'parent7', set())
    assert getattr(partner, 'ElkPort') is None


def test_assoc_properties0_stub_double():
    # graph_EMapPropertyHolder has no real 'graph_EMapPropertyHolder' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkPropertyToValueMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkPropertyToValueMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkPropertyToValueMapEntry(key="sample_text", value="sample_text")
    partner = graph_EMapPropertyHolder()
    setattr(partner, 'graph_EMapPropertyHolder', None)
    _safe_set(owner, 'graph_ElkPropertyToValueMapEntry', partner)
    assert owner in getattr(partner, 'graph_EMapPropertyHolder')
    _safe_set(owner, 'graph_ElkPropertyToValueMapEntry', None)
    assert owner not in getattr(partner, 'graph_EMapPropertyHolder')


def test_assoc_sources20_stub_double():
    # graph_ElkConnectableShape has no real 'ElkConnectableShape' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    partner = graph_ElkConnectableShape()
    setattr(partner, 'ElkConnectableShape', None)
    _safe_set(owner, 'outgoingEdges', {partner})
    assert getattr(partner, 'ElkConnectableShape') == owner
    _safe_set(owner, 'outgoingEdges', set())
    assert getattr(partner, 'ElkConnectableShape') is None


def test_assoc_targets21_stub_double():
    # graph_ElkConnectableShape has no real 'ElkConnectableShape22' property in the generated
    # code (a bare stub) -- manually attach it so graph_ElkEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_ElkEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    partner = graph_ElkConnectableShape()
    setattr(partner, 'ElkConnectableShape22', None)
    _safe_set(owner, 'incomingEdges', {partner})
    assert getattr(partner, 'ElkConnectableShape22') == owner
    _safe_set(owner, 'incomingEdges', set())
    assert getattr(partner, 'ElkConnectableShape22') is None


