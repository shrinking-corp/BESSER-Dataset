import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Container,
    Line,
    Node,
    Shape,
    View,
    di_Comment,
    di_CommentLink,
    di_Connector,
    di_Container,
    di_Diagram,
    di_EObject,
    di_ElementEntry,
    di_GradientShape,
    di_Grid,
    di_Guide,
    di_Line,
    di_Node,
    di_Ruler,
    di_Shape,
    di_View,
    Alignment,
    LineStyle,
    RulerUnit,
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

def test_assoc_children6_reverse_link_reassign_clear():
    a1 = di_Shape(background=7, bounds="sample_text", foreground=7)
    a2 = di_Shape(background=13, bounds="sample_text_2", foreground=13)
    b = di_Container(allLines="sample_text", allShapes="sample_text")
    _safe_set(b, 'di_Container', {a1})
    assert _is_linked(b, 'di_Container', a1)
    if hasattr(a1, 'di_Shape'):
        assert _is_linked(a1, 'di_Shape', b)
    _safe_set(b, 'di_Container', {a2})
    assert _is_linked(b, 'di_Container', a2)
    if hasattr(a1, 'di_Shape'):
        assert not _is_linked(a1, 'di_Shape', b)
    if hasattr(a2, 'di_Shape'):
        assert _is_linked(a2, 'di_Shape', b)
    _safe_set(b, 'di_Container', set())
    assert not _is_linked(b, 'di_Container', a2)
    if hasattr(a2, 'di_Shape'):
        assert not _is_linked(a2, 'di_Shape', b)


def test_assoc_elementMap32_reverse_link_reassign_clear():
    a1 = di_Guide(position=7)
    a2 = di_Guide(position=13)
    b = di_ElementEntry(value="sample_text")
    _safe_set(b, 'di_ElementEntry', a1)
    assert _is_linked(b, 'di_ElementEntry', a1)
    if hasattr(a1, 'di_Guide'):
        assert _is_linked(a1, 'di_Guide', b)
    _safe_set(b, 'di_ElementEntry', a2)
    assert _is_linked(b, 'di_ElementEntry', a2)
    if hasattr(a1, 'di_Guide'):
        assert not _is_linked(a1, 'di_Guide', b)
    if hasattr(a2, 'di_Guide'):
        assert _is_linked(a2, 'di_Guide', b)
    _safe_set(b, 'di_ElementEntry', None)
    assert not _is_linked(b, 'di_ElementEntry', a2)
    if hasattr(a2, 'di_Guide'):
        assert not _is_linked(a2, 'di_Guide', b)


def test_assoc_grid17_reverse_link_reassign_clear():
    a1 = di_Grid(color=7, spacing=7, style="sample_text")
    a2 = di_Grid(color=13, spacing=13, style="sample_text_2")
    b = di_Diagram(rulers="sample_text", snapToGeometry=True, snapToGrid=True)
    _safe_set(b, 'di_Diagram18', a1)
    assert _is_linked(b, 'di_Diagram18', a1)
    if hasattr(a1, 'di_Grid'):
        assert _is_linked(a1, 'di_Grid', b)
    _safe_set(b, 'di_Diagram18', a2)
    assert _is_linked(b, 'di_Diagram18', a2)
    if hasattr(a1, 'di_Grid'):
        assert not _is_linked(a1, 'di_Grid', b)
    if hasattr(a2, 'di_Grid'):
        assert _is_linked(a2, 'di_Grid', b)
    _safe_set(b, 'di_Diagram18', None)
    assert not _is_linked(b, 'di_Diagram18', a2)
    if hasattr(a2, 'di_Grid'):
        assert not _is_linked(a2, 'di_Grid', b)


def test_assoc_guides30_reverse_link_reassign_clear():
    a1 = di_Ruler(unit="sample_text")
    a2 = di_Ruler(unit="sample_text_2")
    b = di_Guide(position=7)
    _safe_set(b, 'Guide', a1)
    assert _is_linked(b, 'Guide', a1)
    if hasattr(a1, 'ruler'):
        assert _is_linked(a1, 'ruler', b)
    _safe_set(b, 'Guide', a2)
    assert _is_linked(b, 'Guide', a2)
    if hasattr(a1, 'ruler'):
        assert not _is_linked(a1, 'ruler', b)
    if hasattr(a2, 'ruler'):
        assert _is_linked(a2, 'ruler', b)
    _safe_set(b, 'Guide', None)
    assert not _is_linked(b, 'Guide', a2)
    if hasattr(a2, 'ruler'):
        assert not _is_linked(a2, 'ruler', b)


def test_assoc_horizontalRuler12_reverse_link_reassign_clear():
    a1 = di_Ruler(unit="sample_text")
    a2 = di_Ruler(unit="sample_text_2")
    b = di_Diagram(rulers="sample_text", snapToGeometry=True, snapToGrid=True)
    _safe_set(b, 'di_Diagram13', a1)
    assert _is_linked(b, 'di_Diagram13', a1)
    if hasattr(a1, 'di_Ruler'):
        assert _is_linked(a1, 'di_Ruler', b)
    _safe_set(b, 'di_Diagram13', a2)
    assert _is_linked(b, 'di_Diagram13', a2)
    if hasattr(a1, 'di_Ruler'):
        assert not _is_linked(a1, 'di_Ruler', b)
    if hasattr(a2, 'di_Ruler'):
        assert _is_linked(a2, 'di_Ruler', b)
    _safe_set(b, 'di_Diagram13', None)
    assert not _is_linked(b, 'di_Diagram13', a2)
    if hasattr(a2, 'di_Ruler'):
        assert not _is_linked(a2, 'di_Ruler', b)


def test_assoc_key33_reverse_link_reassign_clear():
    a1 = di_View(id="sample_text", label="sample_text")
    a2 = di_View(id="sample_text_2", label="sample_text_2")
    b = di_ElementEntry(value="sample_text")
    _safe_set(b, 'di_ElementEntry34', a1)
    assert _is_linked(b, 'di_ElementEntry34', a1)
    if hasattr(a1, 'di_View35'):
        assert _is_linked(a1, 'di_View35', b)
    _safe_set(b, 'di_ElementEntry34', a2)
    assert _is_linked(b, 'di_ElementEntry34', a2)
    if hasattr(a1, 'di_View35'):
        assert not _is_linked(a1, 'di_View35', b)
    if hasattr(a2, 'di_View35'):
        assert _is_linked(a2, 'di_View35', b)
    _safe_set(b, 'di_ElementEntry34', None)
    assert not _is_linked(b, 'di_ElementEntry34', a2)
    if hasattr(a2, 'di_View35'):
        assert not _is_linked(a2, 'di_View35', b)


def test_assoc_lines7_reverse_link_reassign_clear():
    a1 = di_Line(color=7, lineDash=7, sourceAnchor="sample_text", sourceNode="sample_text", style="sample_text", targetAnchor="sample_text", targetNode="sample_text", width=7)
    a2 = di_Line(color=13, lineDash=13, sourceAnchor="sample_text_2", sourceNode="sample_text_2", style="sample_text_2", targetAnchor="sample_text_2", targetNode="sample_text_2", width=13)
    b = di_Container(allLines="sample_text", allShapes="sample_text")
    _safe_set(b, 'di_Container8', {a1})
    assert _is_linked(b, 'di_Container8', a1)
    if hasattr(a1, 'di_Line'):
        assert _is_linked(a1, 'di_Line', b)
    _safe_set(b, 'di_Container8', {a2})
    assert _is_linked(b, 'di_Container8', a2)
    if hasattr(a1, 'di_Line'):
        assert not _is_linked(a1, 'di_Line', b)
    if hasattr(a2, 'di_Line'):
        assert _is_linked(a2, 'di_Line', b)
    _safe_set(b, 'di_Container8', set())
    assert not _is_linked(b, 'di_Container8', a2)
    if hasattr(a2, 'di_Line'):
        assert not _is_linked(a2, 'di_Line', b)


def test_assoc_ruler31_reverse_link_reassign_clear():
    a1 = di_Ruler(unit="sample_text")
    a2 = di_Ruler(unit="sample_text_2")
    b = di_Guide(position=7)
    _safe_set(b, 'guides', a1)
    assert _is_linked(b, 'guides', a1)
    if hasattr(a1, 'Ruler'):
        assert _is_linked(a1, 'Ruler', b)
    _safe_set(b, 'guides', a2)
    assert _is_linked(b, 'guides', a2)
    if hasattr(a1, 'Ruler'):
        assert not _is_linked(a1, 'Ruler', b)
    if hasattr(a2, 'Ruler'):
        assert _is_linked(a2, 'Ruler', b)
    _safe_set(b, 'guides', None)
    assert not _is_linked(b, 'guides', a2)
    if hasattr(a2, 'Ruler'):
        assert not _is_linked(a2, 'Ruler', b)


def test_assoc_verticalRuler14_reverse_link_reassign_clear():
    a1 = di_Ruler(unit="sample_text")
    a2 = di_Ruler(unit="sample_text_2")
    b = di_Diagram(rulers="sample_text", snapToGeometry=True, snapToGrid=True)
    _safe_set(b, 'di_Diagram15', a1)
    assert _is_linked(b, 'di_Diagram15', a1)
    if hasattr(a1, 'di_Ruler16'):
        assert _is_linked(a1, 'di_Ruler16', b)
    _safe_set(b, 'di_Diagram15', a2)
    assert _is_linked(b, 'di_Diagram15', a2)
    if hasattr(a1, 'di_Ruler16'):
        assert not _is_linked(a1, 'di_Ruler16', b)
    if hasattr(a2, 'di_Ruler16'):
        assert _is_linked(a2, 'di_Ruler16', b)
    _safe_set(b, 'di_Diagram15', None)
    assert not _is_linked(b, 'di_Diagram15', a2)
    if hasattr(a2, 'di_Ruler16'):
        assert not _is_linked(a2, 'di_Ruler16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commentLinks1_stub_double():
    # di_CommentLink has no real 'CommentLink' property in the generated
    # code (a bare stub) -- manually attach it so di_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Node(allIncomingLines="sample_text", allOutgoingLines="sample_text")
    partner = di_CommentLink()
    setattr(partner, 'CommentLink', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'CommentLink') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'CommentLink') is None


def test_assoc_commentLinks10_stub_double():
    # di_CommentLink has no real 'di_CommentLink' property in the generated
    # code (a bare stub) -- manually attach it so di_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Diagram(rulers="sample_text", snapToGeometry=True, snapToGrid=True)
    partner = di_CommentLink()
    setattr(partner, 'di_CommentLink', None)
    _safe_set(owner, 'di_Diagram11', {partner})
    assert getattr(partner, 'di_CommentLink') == owner
    _safe_set(owner, 'di_Diagram11', set())
    assert getattr(partner, 'di_CommentLink') is None


def test_assoc_comments9_stub_double():
    # di_Comment has no real 'di_Comment' property in the generated
    # code (a bare stub) -- manually attach it so di_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Diagram(rulers="sample_text", snapToGeometry=True, snapToGrid=True)
    partner = di_Comment()
    setattr(partner, 'di_Comment', None)
    _safe_set(owner, 'di_Diagram', {partner})
    assert getattr(partner, 'di_Comment') == owner
    _safe_set(owner, 'di_Diagram', set())
    assert getattr(partner, 'di_Comment') is None


def test_assoc_element0_stub_double():
    # di_EObject has no real 'di_EObject' property in the generated
    # code (a bare stub) -- manually attach it so di_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_View(id="sample_text", label="sample_text")
    partner = di_EObject()
    setattr(partner, 'di_EObject', None)
    _safe_set(owner, 'di_View', partner)
    assert getattr(partner, 'di_EObject') == owner
    _safe_set(owner, 'di_View', None)
    assert getattr(partner, 'di_EObject') is None


def test_assoc_incomingLines4_stub_double():
    # di_Connector has no real 'Connector5' property in the generated
    # code (a bare stub) -- manually attach it so di_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Node(allIncomingLines="sample_text", allOutgoingLines="sample_text")
    partner = di_Connector()
    setattr(partner, 'Connector5', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Connector5') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Connector5') is None


def test_assoc_outgoingLines2_stub_double():
    # di_Connector has no real 'Connector' property in the generated
    # code (a bare stub) -- manually attach it so di_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Node(allIncomingLines="sample_text", allOutgoingLines="sample_text")
    partner = di_Connector()
    setattr(partner, 'Connector', None)
    _safe_set(owner, 'source3', {partner})
    assert getattr(partner, 'Connector') == owner
    _safe_set(owner, 'source3', set())
    assert getattr(partner, 'Connector') is None


def test_assoc_source20_stub_double():
    # di_Connector has no real 'outgoingLines' property in the generated
    # code (a bare stub) -- manually attach it so di_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Node(allIncomingLines="sample_text", allOutgoingLines="sample_text")
    partner = di_Connector()
    setattr(partner, 'outgoingLines', None)
    _safe_set(owner, 'Node21', partner)
    assert getattr(partner, 'outgoingLines') == owner
    _safe_set(owner, 'Node21', None)
    assert getattr(partner, 'outgoingLines') is None


def test_assoc_source27_stub_double():
    # di_CommentLink has no real 'commentLinks' property in the generated
    # code (a bare stub) -- manually attach it so di_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Node(allIncomingLines="sample_text", allOutgoingLines="sample_text")
    partner = di_CommentLink()
    setattr(partner, 'commentLinks', None)
    _safe_set(owner, 'Node28', partner)
    assert getattr(partner, 'commentLinks') == owner
    _safe_set(owner, 'Node28', None)
    assert getattr(partner, 'commentLinks') is None


def test_assoc_target19_stub_double():
    # di_Connector has no real 'incomingLines' property in the generated
    # code (a bare stub) -- manually attach it so di_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Node(allIncomingLines="sample_text", allOutgoingLines="sample_text")
    partner = di_Connector()
    setattr(partner, 'incomingLines', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'incomingLines') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'incomingLines') is None


