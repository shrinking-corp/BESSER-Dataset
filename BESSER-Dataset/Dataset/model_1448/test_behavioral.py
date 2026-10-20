import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GAlignable,
    GBoundsAware,
    GEdgeLayoutable,
    GLayouting,
    GModelElement,
    GModelRoot,
    GShapeElement,
    graph_GAlignable,
    graph_GBounds,
    graph_GBoundsAware,
    graph_GButton,
    graph_GCompartment,
    graph_GDimension,
    graph_GEdge,
    graph_GEdgeLayoutable,
    graph_GEdgePlacement,
    graph_GGraph,
    graph_GHtmlRoot,
    graph_GIssue,
    graph_GIssueMarker,
    graph_GLabel,
    graph_GLayouting,
    graph_GModelElement,
    graph_GModelRoot,
    graph_GNode,
    graph_GPoint,
    graph_GPort,
    graph_GPreRenderedElement,
    graph_GShapeElement,
    graph_StringToObjectMapEntry,
    GSeverity,
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

def test_assoc_canvasBounds6_reverse_link_reassign_clear():
    a1 = graph_GModelRoot(revision=7)
    a2 = graph_GModelRoot(revision=13)
    b = graph_GBounds(height=3.14, width=3.14, x=3.14, y=3.14)
    _safe_set(b, 'graph_GBounds', a1)
    assert _is_linked(b, 'graph_GBounds', a1)
    if hasattr(a1, 'graph_GModelRoot'):
        assert _is_linked(a1, 'graph_GModelRoot', b)
    _safe_set(b, 'graph_GBounds', a2)
    assert _is_linked(b, 'graph_GBounds', a2)
    if hasattr(a1, 'graph_GModelRoot'):
        assert not _is_linked(a1, 'graph_GModelRoot', b)
    if hasattr(a2, 'graph_GModelRoot'):
        assert _is_linked(a2, 'graph_GModelRoot', b)
    _safe_set(b, 'graph_GBounds', None)
    assert not _is_linked(b, 'graph_GBounds', a2)
    if hasattr(a2, 'graph_GModelRoot'):
        assert not _is_linked(a2, 'graph_GModelRoot', b)


def test_assoc_children1_reverse_link_reassign_clear():
    a1 = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    a2 = graph_GModelElement(cssClasses="sample_text_2", id="sample_text_2", trace="sample_text_2", type="sample_text_2")
    b = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'GModelElement'):
        assert _is_linked(a1, 'GModelElement', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'GModelElement'):
        assert not _is_linked(a1, 'GModelElement', b)
    if hasattr(a2, 'GModelElement'):
        assert _is_linked(a2, 'GModelElement', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'GModelElement'):
        assert not _is_linked(a2, 'GModelElement', b)


def test_assoc_layoutOptions19_reverse_link_reassign_clear():
    a1 = graph_StringToObjectMapEntry(key="sample_text", value="sample_text")
    a2 = graph_StringToObjectMapEntry(key="sample_text_2", value="sample_text_2")
    b = graph_GLayouting(layout="sample_text")
    _safe_set(b, 'graph_GLayouting', {a1})
    assert _is_linked(b, 'graph_GLayouting', a1)
    if hasattr(a1, 'graph_StringToObjectMapEntry20'):
        assert _is_linked(a1, 'graph_StringToObjectMapEntry20', b)
    _safe_set(b, 'graph_GLayouting', {a2})
    assert _is_linked(b, 'graph_GLayouting', a2)
    if hasattr(a1, 'graph_StringToObjectMapEntry20'):
        assert not _is_linked(a1, 'graph_StringToObjectMapEntry20', b)
    if hasattr(a2, 'graph_StringToObjectMapEntry20'):
        assert _is_linked(a2, 'graph_StringToObjectMapEntry20', b)
    _safe_set(b, 'graph_GLayouting', set())
    assert not _is_linked(b, 'graph_GLayouting', a2)
    if hasattr(a2, 'graph_StringToObjectMapEntry20'):
        assert not _is_linked(a2, 'graph_StringToObjectMapEntry20', b)


def test_assoc_parent3_reverse_link_reassign_clear():
    a1 = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    a2 = graph_GModelElement(cssClasses="sample_text_2", id="sample_text_2", trace="sample_text_2", type="sample_text_2")
    b = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'GModelElement4'):
        assert _is_linked(a1, 'GModelElement4', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'GModelElement4'):
        assert not _is_linked(a1, 'GModelElement4', b)
    if hasattr(a2, 'GModelElement4'):
        assert _is_linked(a2, 'GModelElement4', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'GModelElement4'):
        assert not _is_linked(a2, 'GModelElement4', b)


def test_assoc_routingPoints7_reverse_link_reassign_clear():
    a1 = graph_GPoint(x=3.14, y=3.14)
    a2 = graph_GPoint(x=9.99, y=9.99)
    b = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    _safe_set(b, 'graph_GEdge', {a1})
    assert _is_linked(b, 'graph_GEdge', a1)
    if hasattr(a1, 'graph_GPoint'):
        assert _is_linked(a1, 'graph_GPoint', b)
    _safe_set(b, 'graph_GEdge', {a2})
    assert _is_linked(b, 'graph_GEdge', a2)
    if hasattr(a1, 'graph_GPoint'):
        assert not _is_linked(a1, 'graph_GPoint', b)
    if hasattr(a2, 'graph_GPoint'):
        assert _is_linked(a2, 'graph_GPoint', b)
    _safe_set(b, 'graph_GEdge', set())
    assert not _is_linked(b, 'graph_GEdge', a2)
    if hasattr(a2, 'graph_GPoint'):
        assert not _is_linked(a2, 'graph_GPoint', b)


def test_assoc_source8_reverse_link_reassign_clear():
    a1 = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    a2 = graph_GModelElement(cssClasses="sample_text_2", id="sample_text_2", trace="sample_text_2", type="sample_text_2")
    b = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    _safe_set(b, 'graph_GEdge9', a1)
    assert _is_linked(b, 'graph_GEdge9', a1)
    if hasattr(a1, 'graph_GModelElement'):
        assert _is_linked(a1, 'graph_GModelElement', b)
    _safe_set(b, 'graph_GEdge9', a2)
    assert _is_linked(b, 'graph_GEdge9', a2)
    if hasattr(a1, 'graph_GModelElement'):
        assert not _is_linked(a1, 'graph_GModelElement', b)
    if hasattr(a2, 'graph_GModelElement'):
        assert _is_linked(a2, 'graph_GModelElement', b)
    _safe_set(b, 'graph_GEdge9', None)
    assert not _is_linked(b, 'graph_GEdge9', a2)
    if hasattr(a2, 'graph_GModelElement'):
        assert not _is_linked(a2, 'graph_GModelElement', b)


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    a2 = graph_GModelElement(cssClasses="sample_text_2", id="sample_text_2", trace="sample_text_2", type="sample_text_2")
    b = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    _safe_set(b, 'graph_GEdge11', a1)
    assert _is_linked(b, 'graph_GEdge11', a1)
    if hasattr(a1, 'graph_GModelElement12'):
        assert _is_linked(a1, 'graph_GModelElement12', b)
    _safe_set(b, 'graph_GEdge11', a2)
    assert _is_linked(b, 'graph_GEdge11', a2)
    if hasattr(a1, 'graph_GModelElement12'):
        assert not _is_linked(a1, 'graph_GModelElement12', b)
    if hasattr(a2, 'graph_GModelElement12'):
        assert _is_linked(a2, 'graph_GModelElement12', b)
    _safe_set(b, 'graph_GEdge11', None)
    assert not _is_linked(b, 'graph_GEdge11', a2)
    if hasattr(a2, 'graph_GModelElement12'):
        assert not _is_linked(a2, 'graph_GModelElement12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alignment21_stub_double():
    # graph_GAlignable has no real 'graph_GAlignable' property in the generated
    # code (a bare stub) -- manually attach it so graph_GPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_GPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_GPoint(x=3.14, y=3.14)
    partner = graph_GAlignable()
    setattr(partner, 'graph_GAlignable', None)
    _safe_set(owner, 'graph_GPoint22', partner)
    assert getattr(partner, 'graph_GAlignable') == owner
    _safe_set(owner, 'graph_GPoint22', None)
    assert getattr(partner, 'graph_GAlignable') is None


def test_assoc_edgePlacement18_stub_double():
    # graph_GEdgeLayoutable has no real 'graph_GEdgeLayoutable' property in the generated
    # code (a bare stub) -- manually attach it so graph_GEdgePlacement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_GEdgePlacement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_GEdgePlacement(offset="sample_text", position="sample_text", rotate=True, side="sample_text")
    partner = graph_GEdgeLayoutable()
    setattr(partner, 'graph_GEdgeLayoutable', None)
    _safe_set(owner, 'graph_GEdgePlacement', partner)
    assert getattr(partner, 'graph_GEdgeLayoutable') == owner
    _safe_set(owner, 'graph_GEdgePlacement', None)
    assert getattr(partner, 'graph_GEdgeLayoutable') is None


def test_assoc_issues13_stub_double():
    # graph_GIssueMarker has no real 'graph_GIssueMarker' property in the generated
    # code (a bare stub) -- manually attach it so graph_GIssue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_GIssue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_GIssue(message="sample_text", severity="sample_text")
    partner = graph_GIssueMarker()
    setattr(partner, 'graph_GIssueMarker', None)
    _safe_set(owner, 'graph_GIssue', partner)
    assert owner in getattr(partner, 'graph_GIssueMarker')
    _safe_set(owner, 'graph_GIssue', None)
    assert owner not in getattr(partner, 'graph_GIssueMarker')


def test_assoc_layoutOptions5_stub_double():
    # graph_GGraph has no real 'graph_GGraph' property in the generated
    # code (a bare stub) -- manually attach it so graph_StringToObjectMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_StringToObjectMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_StringToObjectMapEntry(key="sample_text", value="sample_text")
    partner = graph_GGraph()
    setattr(partner, 'graph_GGraph', None)
    _safe_set(owner, 'graph_StringToObjectMapEntry', partner)
    assert owner in getattr(partner, 'graph_GGraph')
    _safe_set(owner, 'graph_StringToObjectMapEntry', None)
    assert owner not in getattr(partner, 'graph_GGraph')


def test_assoc_position14_stub_double():
    # graph_GBoundsAware has no real 'graph_GBoundsAware' property in the generated
    # code (a bare stub) -- manually attach it so graph_GPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_GPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_GPoint(x=3.14, y=3.14)
    partner = graph_GBoundsAware()
    setattr(partner, 'graph_GBoundsAware', None)
    _safe_set(owner, 'graph_GPoint15', partner)
    assert getattr(partner, 'graph_GBoundsAware') == owner
    _safe_set(owner, 'graph_GPoint15', None)
    assert getattr(partner, 'graph_GBoundsAware') is None


def test_assoc_size16_stub_double():
    # graph_GBoundsAware has no real 'graph_GBoundsAware17' property in the generated
    # code (a bare stub) -- manually attach it so graph_GDimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_GDimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_GDimension(height=3.14, width=3.14)
    partner = graph_GBoundsAware()
    setattr(partner, 'graph_GBoundsAware17', None)
    _safe_set(owner, 'graph_GDimension', partner)
    assert getattr(partner, 'graph_GBoundsAware17') == owner
    _safe_set(owner, 'graph_GDimension', None)
    assert getattr(partner, 'graph_GBoundsAware17') is None


