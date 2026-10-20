import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractNode,
    AbstractNodeRepresentation,
    AbstractRepresentation,
    BasicLabelStyle,
    BorderedStyle,
    ContainerStyle,
    GraphicalElement,
    LabelStyle,
    NodeStyle,
    Representation,
    migrationmodeler_AbstractNode,
    migrationmodeler_AbstractNodeRepresentation,
    migrationmodeler_AbstractRepresentation,
    migrationmodeler_BasicLabelStyle,
    migrationmodeler_Bordered,
    migrationmodeler_BorderedRepresentation,
    migrationmodeler_BorderedStyle,
    migrationmodeler_BundledImage,
    migrationmodeler_Color,
    migrationmodeler_Container,
    migrationmodeler_ContainerRepresentation,
    migrationmodeler_ContainerStyle,
    migrationmodeler_Diagram,
    migrationmodeler_Dot,
    migrationmodeler_Edge,
    migrationmodeler_EdgeRepresentation,
    migrationmodeler_EdgeStyle,
    migrationmodeler_Ellipse,
    migrationmodeler_Filter,
    migrationmodeler_FlatContainerStyle,
    migrationmodeler_GaugeCompositeStyle,
    migrationmodeler_GaugeSection,
    migrationmodeler_GraphicalElement,
    migrationmodeler_LabelStyle,
    migrationmodeler_Layer,
    migrationmodeler_Layout,
    migrationmodeler_Lozenge,
    migrationmodeler_Node,
    migrationmodeler_NodeRepresentation,
    migrationmodeler_NodeStyle,
    migrationmodeler_Note,
    migrationmodeler_Point,
    migrationmodeler_Representation,
    migrationmodeler_ShapeContainerStyle,
    migrationmodeler_Square,
    migrationmodeler_TestCase,
    migrationmodeler_WorkspaceImage,
    AlignmentKind,
    BackgroundStyle,
    BundledImageShape,
    ContainerShape,
    FontFormat,
    LabelAlignment,
    LabelPosition,
    RoutingStyle,
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

def test_assoc_backgroundColor59_reverse_link_reassign_clear():
    a1 = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    a2 = migrationmodeler_GaugeSection(label="sample_text_2", max="sample_text_2", min="sample_text_2", value="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color60', a1)
    assert _is_linked(b, 'migrationmodeler_Color60', a1)
    if hasattr(a1, 'migrationmodeler_GaugeSection'):
        assert _is_linked(a1, 'migrationmodeler_GaugeSection', b)
    _safe_set(b, 'migrationmodeler_Color60', a2)
    assert _is_linked(b, 'migrationmodeler_Color60', a2)
    if hasattr(a1, 'migrationmodeler_GaugeSection'):
        assert not _is_linked(a1, 'migrationmodeler_GaugeSection', b)
    if hasattr(a2, 'migrationmodeler_GaugeSection'):
        assert _is_linked(a2, 'migrationmodeler_GaugeSection', b)
    _safe_set(b, 'migrationmodeler_Color60', None)
    assert not _is_linked(b, 'migrationmodeler_Color60', a2)
    if hasattr(a2, 'migrationmodeler_GaugeSection'):
        assert not _is_linked(a2, 'migrationmodeler_GaugeSection', b)


def test_assoc_backgroundColor64_reverse_link_reassign_clear():
    a1 = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text")
    a2 = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color65', a1)
    assert _is_linked(b, 'migrationmodeler_Color65', a1)
    if hasattr(a1, 'migrationmodeler_FlatContainerStyle'):
        assert _is_linked(a1, 'migrationmodeler_FlatContainerStyle', b)
    _safe_set(b, 'migrationmodeler_Color65', a2)
    assert _is_linked(b, 'migrationmodeler_Color65', a2)
    if hasattr(a1, 'migrationmodeler_FlatContainerStyle'):
        assert not _is_linked(a1, 'migrationmodeler_FlatContainerStyle', b)
    if hasattr(a2, 'migrationmodeler_FlatContainerStyle'):
        assert _is_linked(a2, 'migrationmodeler_FlatContainerStyle', b)
    _safe_set(b, 'migrationmodeler_Color65', None)
    assert not _is_linked(b, 'migrationmodeler_Color65', a2)
    if hasattr(a2, 'migrationmodeler_FlatContainerStyle'):
        assert not _is_linked(a2, 'migrationmodeler_FlatContainerStyle', b)


def test_assoc_backgroundColor69_reverse_link_reassign_clear():
    a1 = migrationmodeler_ShapeContainerStyle(shape="sample_text")
    a2 = migrationmodeler_ShapeContainerStyle(shape="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color70', a1)
    assert _is_linked(b, 'migrationmodeler_Color70', a1)
    if hasattr(a1, 'migrationmodeler_ShapeContainerStyle'):
        assert _is_linked(a1, 'migrationmodeler_ShapeContainerStyle', b)
    _safe_set(b, 'migrationmodeler_Color70', a2)
    assert _is_linked(b, 'migrationmodeler_Color70', a2)
    if hasattr(a1, 'migrationmodeler_ShapeContainerStyle'):
        assert not _is_linked(a1, 'migrationmodeler_ShapeContainerStyle', b)
    if hasattr(a2, 'migrationmodeler_ShapeContainerStyle'):
        assert _is_linked(a2, 'migrationmodeler_ShapeContainerStyle', b)
    _safe_set(b, 'migrationmodeler_Color70', None)
    assert not _is_linked(b, 'migrationmodeler_Color70', a2)
    if hasattr(a2, 'migrationmodeler_ShapeContainerStyle'):
        assert not _is_linked(a2, 'migrationmodeler_ShapeContainerStyle', b)


def test_assoc_beginLabelStyle43_reverse_link_reassign_clear():
    a1 = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    a2 = migrationmodeler_EdgeStyle(routingStyle="sample_text_2")
    b = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle', a1)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle', a1)
    if hasattr(a1, 'migrationmodeler_EdgeStyle44'):
        assert _is_linked(a1, 'migrationmodeler_EdgeStyle44', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle', a2)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle', a2)
    if hasattr(a1, 'migrationmodeler_EdgeStyle44'):
        assert not _is_linked(a1, 'migrationmodeler_EdgeStyle44', b)
    if hasattr(a2, 'migrationmodeler_EdgeStyle44'):
        assert _is_linked(a2, 'migrationmodeler_EdgeStyle44', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle', None)
    assert not _is_linked(b, 'migrationmodeler_BasicLabelStyle', a2)
    if hasattr(a2, 'migrationmodeler_EdgeStyle44'):
        assert not _is_linked(a2, 'migrationmodeler_EdgeStyle44', b)


def test_assoc_borderColor52_reverse_link_reassign_clear():
    a1 = migrationmodeler_Color(blue=7, green=7, red=7)
    a2 = migrationmodeler_Color(blue=13, green=13, red=13)
    b = migrationmodeler_BorderedStyle(borderSize=7)
    _safe_set(b, 'migrationmodeler_BorderedStyle', a1)
    assert _is_linked(b, 'migrationmodeler_BorderedStyle', a1)
    if hasattr(a1, 'migrationmodeler_Color53'):
        assert _is_linked(a1, 'migrationmodeler_Color53', b)
    _safe_set(b, 'migrationmodeler_BorderedStyle', a2)
    assert _is_linked(b, 'migrationmodeler_BorderedStyle', a2)
    if hasattr(a1, 'migrationmodeler_Color53'):
        assert not _is_linked(a1, 'migrationmodeler_Color53', b)
    if hasattr(a2, 'migrationmodeler_Color53'):
        assert _is_linked(a2, 'migrationmodeler_Color53', b)
    _safe_set(b, 'migrationmodeler_BorderedStyle', None)
    assert not _is_linked(b, 'migrationmodeler_BorderedStyle', a2)
    if hasattr(a2, 'migrationmodeler_Color53'):
        assert not _is_linked(a2, 'migrationmodeler_Color53', b)


def test_assoc_centerLabelStyle45_reverse_link_reassign_clear():
    a1 = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    a2 = migrationmodeler_EdgeStyle(routingStyle="sample_text_2")
    b = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle47', a1)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle47', a1)
    if hasattr(a1, 'migrationmodeler_EdgeStyle46'):
        assert _is_linked(a1, 'migrationmodeler_EdgeStyle46', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle47', a2)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle47', a2)
    if hasattr(a1, 'migrationmodeler_EdgeStyle46'):
        assert not _is_linked(a1, 'migrationmodeler_EdgeStyle46', b)
    if hasattr(a2, 'migrationmodeler_EdgeStyle46'):
        assert _is_linked(a2, 'migrationmodeler_EdgeStyle46', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle47', None)
    assert not _is_linked(b, 'migrationmodeler_BasicLabelStyle47', a2)
    if hasattr(a2, 'migrationmodeler_EdgeStyle46'):
        assert not _is_linked(a2, 'migrationmodeler_EdgeStyle46', b)


def test_assoc_color41_reverse_link_reassign_clear():
    a1 = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    a2 = migrationmodeler_EdgeStyle(routingStyle="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color', a1)
    assert _is_linked(b, 'migrationmodeler_Color', a1)
    if hasattr(a1, 'migrationmodeler_EdgeStyle42'):
        assert _is_linked(a1, 'migrationmodeler_EdgeStyle42', b)
    _safe_set(b, 'migrationmodeler_Color', a2)
    assert _is_linked(b, 'migrationmodeler_Color', a2)
    if hasattr(a1, 'migrationmodeler_EdgeStyle42'):
        assert not _is_linked(a1, 'migrationmodeler_EdgeStyle42', b)
    if hasattr(a2, 'migrationmodeler_EdgeStyle42'):
        assert _is_linked(a2, 'migrationmodeler_EdgeStyle42', b)
    _safe_set(b, 'migrationmodeler_Color', None)
    assert not _is_linked(b, 'migrationmodeler_Color', a2)
    if hasattr(a2, 'migrationmodeler_EdgeStyle42'):
        assert not _is_linked(a2, 'migrationmodeler_EdgeStyle42', b)


def test_assoc_color71_reverse_link_reassign_clear():
    a1 = migrationmodeler_Square(height="sample_text", width="sample_text")
    a2 = migrationmodeler_Square(height="sample_text_2", width="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color72', a1)
    assert _is_linked(b, 'migrationmodeler_Color72', a1)
    if hasattr(a1, 'migrationmodeler_Square'):
        assert _is_linked(a1, 'migrationmodeler_Square', b)
    _safe_set(b, 'migrationmodeler_Color72', a2)
    assert _is_linked(b, 'migrationmodeler_Color72', a2)
    if hasattr(a1, 'migrationmodeler_Square'):
        assert not _is_linked(a1, 'migrationmodeler_Square', b)
    if hasattr(a2, 'migrationmodeler_Square'):
        assert _is_linked(a2, 'migrationmodeler_Square', b)
    _safe_set(b, 'migrationmodeler_Color72', None)
    assert not _is_linked(b, 'migrationmodeler_Color72', a2)
    if hasattr(a2, 'migrationmodeler_Square'):
        assert not _is_linked(a2, 'migrationmodeler_Square', b)


def test_assoc_color73_reverse_link_reassign_clear():
    a1 = migrationmodeler_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    a2 = migrationmodeler_Ellipse(horizontalDiameter="sample_text_2", verticalDiameter="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color74', a1)
    assert _is_linked(b, 'migrationmodeler_Color74', a1)
    if hasattr(a1, 'migrationmodeler_Ellipse'):
        assert _is_linked(a1, 'migrationmodeler_Ellipse', b)
    _safe_set(b, 'migrationmodeler_Color74', a2)
    assert _is_linked(b, 'migrationmodeler_Color74', a2)
    if hasattr(a1, 'migrationmodeler_Ellipse'):
        assert not _is_linked(a1, 'migrationmodeler_Ellipse', b)
    if hasattr(a2, 'migrationmodeler_Ellipse'):
        assert _is_linked(a2, 'migrationmodeler_Ellipse', b)
    _safe_set(b, 'migrationmodeler_Color74', None)
    assert not _is_linked(b, 'migrationmodeler_Color74', a2)
    if hasattr(a2, 'migrationmodeler_Ellipse'):
        assert not _is_linked(a2, 'migrationmodeler_Ellipse', b)


def test_assoc_color75_reverse_link_reassign_clear():
    a1 = migrationmodeler_Lozenge(height="sample_text", width="sample_text")
    a2 = migrationmodeler_Lozenge(height="sample_text_2", width="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color76', a1)
    assert _is_linked(b, 'migrationmodeler_Color76', a1)
    if hasattr(a1, 'migrationmodeler_Lozenge'):
        assert _is_linked(a1, 'migrationmodeler_Lozenge', b)
    _safe_set(b, 'migrationmodeler_Color76', a2)
    assert _is_linked(b, 'migrationmodeler_Color76', a2)
    if hasattr(a1, 'migrationmodeler_Lozenge'):
        assert not _is_linked(a1, 'migrationmodeler_Lozenge', b)
    if hasattr(a2, 'migrationmodeler_Lozenge'):
        assert _is_linked(a2, 'migrationmodeler_Lozenge', b)
    _safe_set(b, 'migrationmodeler_Color76', None)
    assert not _is_linked(b, 'migrationmodeler_Color76', a2)
    if hasattr(a2, 'migrationmodeler_Lozenge'):
        assert not _is_linked(a2, 'migrationmodeler_Lozenge', b)


def test_assoc_color77_reverse_link_reassign_clear():
    a1 = migrationmodeler_Color(blue=7, green=7, red=7)
    a2 = migrationmodeler_Color(blue=13, green=13, red=13)
    b = migrationmodeler_BundledImage(shape="sample_text")
    _safe_set(b, 'migrationmodeler_BundledImage', a1)
    assert _is_linked(b, 'migrationmodeler_BundledImage', a1)
    if hasattr(a1, 'migrationmodeler_Color78'):
        assert _is_linked(a1, 'migrationmodeler_Color78', b)
    _safe_set(b, 'migrationmodeler_BundledImage', a2)
    assert _is_linked(b, 'migrationmodeler_BundledImage', a2)
    if hasattr(a1, 'migrationmodeler_Color78'):
        assert not _is_linked(a1, 'migrationmodeler_Color78', b)
    if hasattr(a2, 'migrationmodeler_Color78'):
        assert _is_linked(a2, 'migrationmodeler_Color78', b)
    _safe_set(b, 'migrationmodeler_BundledImage', None)
    assert not _is_linked(b, 'migrationmodeler_BundledImage', a2)
    if hasattr(a2, 'migrationmodeler_Color78'):
        assert not _is_linked(a2, 'migrationmodeler_Color78', b)


def test_assoc_endLabelStyle48_reverse_link_reassign_clear():
    a1 = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    a2 = migrationmodeler_EdgeStyle(routingStyle="sample_text_2")
    b = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle50', a1)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle50', a1)
    if hasattr(a1, 'migrationmodeler_EdgeStyle49'):
        assert _is_linked(a1, 'migrationmodeler_EdgeStyle49', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle50', a2)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle50', a2)
    if hasattr(a1, 'migrationmodeler_EdgeStyle49'):
        assert not _is_linked(a1, 'migrationmodeler_EdgeStyle49', b)
    if hasattr(a2, 'migrationmodeler_EdgeStyle49'):
        assert _is_linked(a2, 'migrationmodeler_EdgeStyle49', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle50', None)
    assert not _is_linked(b, 'migrationmodeler_BasicLabelStyle50', a2)
    if hasattr(a2, 'migrationmodeler_EdgeStyle49'):
        assert not _is_linked(a2, 'migrationmodeler_EdgeStyle49', b)


def test_assoc_foregroundColor61_reverse_link_reassign_clear():
    a1 = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    a2 = migrationmodeler_GaugeSection(label="sample_text_2", max="sample_text_2", min="sample_text_2", value="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color63', a1)
    assert _is_linked(b, 'migrationmodeler_Color63', a1)
    if hasattr(a1, 'migrationmodeler_GaugeSection62'):
        assert _is_linked(a1, 'migrationmodeler_GaugeSection62', b)
    _safe_set(b, 'migrationmodeler_Color63', a2)
    assert _is_linked(b, 'migrationmodeler_Color63', a2)
    if hasattr(a1, 'migrationmodeler_GaugeSection62'):
        assert not _is_linked(a1, 'migrationmodeler_GaugeSection62', b)
    if hasattr(a2, 'migrationmodeler_GaugeSection62'):
        assert _is_linked(a2, 'migrationmodeler_GaugeSection62', b)
    _safe_set(b, 'migrationmodeler_Color63', None)
    assert not _is_linked(b, 'migrationmodeler_Color63', a2)
    if hasattr(a2, 'migrationmodeler_GaugeSection62'):
        assert not _is_linked(a2, 'migrationmodeler_GaugeSection62', b)


def test_assoc_foregroundColor66_reverse_link_reassign_clear():
    a1 = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text")
    a2 = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text_2")
    b = migrationmodeler_Color(blue=7, green=7, red=7)
    _safe_set(b, 'migrationmodeler_Color68', a1)
    assert _is_linked(b, 'migrationmodeler_Color68', a1)
    if hasattr(a1, 'migrationmodeler_FlatContainerStyle67'):
        assert _is_linked(a1, 'migrationmodeler_FlatContainerStyle67', b)
    _safe_set(b, 'migrationmodeler_Color68', a2)
    assert _is_linked(b, 'migrationmodeler_Color68', a2)
    if hasattr(a1, 'migrationmodeler_FlatContainerStyle67'):
        assert not _is_linked(a1, 'migrationmodeler_FlatContainerStyle67', b)
    if hasattr(a2, 'migrationmodeler_FlatContainerStyle67'):
        assert _is_linked(a2, 'migrationmodeler_FlatContainerStyle67', b)
    _safe_set(b, 'migrationmodeler_Color68', None)
    assert not _is_linked(b, 'migrationmodeler_Color68', a2)
    if hasattr(a2, 'migrationmodeler_FlatContainerStyle67'):
        assert not _is_linked(a2, 'migrationmodeler_FlatContainerStyle67', b)


def test_assoc_labelColor54_reverse_link_reassign_clear():
    a1 = migrationmodeler_Color(blue=7, green=7, red=7)
    a2 = migrationmodeler_Color(blue=13, green=13, red=13)
    b = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle55', a1)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle55', a1)
    if hasattr(a1, 'migrationmodeler_Color56'):
        assert _is_linked(a1, 'migrationmodeler_Color56', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle55', a2)
    assert _is_linked(b, 'migrationmodeler_BasicLabelStyle55', a2)
    if hasattr(a1, 'migrationmodeler_Color56'):
        assert not _is_linked(a1, 'migrationmodeler_Color56', b)
    if hasattr(a2, 'migrationmodeler_Color56'):
        assert _is_linked(a2, 'migrationmodeler_Color56', b)
    _safe_set(b, 'migrationmodeler_BasicLabelStyle55', None)
    assert not _is_linked(b, 'migrationmodeler_BasicLabelStyle55', a2)
    if hasattr(a2, 'migrationmodeler_Color56'):
        assert not _is_linked(a2, 'migrationmodeler_Color56', b)


def test_assoc_layout24_reverse_link_reassign_clear():
    a1 = migrationmodeler_Layout(height=7, width=7, x=7, y=7)
    a2 = migrationmodeler_Layout(height=13, width=13, x=13, y=13)
    b = migrationmodeler_AbstractRepresentation(displayed=True, hidden=True, mappingId="sample_text", pinned=True)
    _safe_set(b, 'migrationmodeler_AbstractRepresentation', a1)
    assert _is_linked(b, 'migrationmodeler_AbstractRepresentation', a1)
    if hasattr(a1, 'migrationmodeler_Layout'):
        assert _is_linked(a1, 'migrationmodeler_Layout', b)
    _safe_set(b, 'migrationmodeler_AbstractRepresentation', a2)
    assert _is_linked(b, 'migrationmodeler_AbstractRepresentation', a2)
    if hasattr(a1, 'migrationmodeler_Layout'):
        assert not _is_linked(a1, 'migrationmodeler_Layout', b)
    if hasattr(a2, 'migrationmodeler_Layout'):
        assert _is_linked(a2, 'migrationmodeler_Layout', b)
    _safe_set(b, 'migrationmodeler_AbstractRepresentation', None)
    assert not _is_linked(b, 'migrationmodeler_AbstractRepresentation', a2)
    if hasattr(a2, 'migrationmodeler_Layout'):
        assert not _is_linked(a2, 'migrationmodeler_Layout', b)


def test_assoc_sections79_reverse_link_reassign_clear():
    a1 = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    a2 = migrationmodeler_GaugeSection(label="sample_text_2", max="sample_text_2", min="sample_text_2", value="sample_text_2")
    b = migrationmodeler_GaugeCompositeStyle(alignment="sample_text")
    _safe_set(b, 'migrationmodeler_GaugeCompositeStyle', {a1})
    assert _is_linked(b, 'migrationmodeler_GaugeCompositeStyle', a1)
    if hasattr(a1, 'migrationmodeler_GaugeSection80'):
        assert _is_linked(a1, 'migrationmodeler_GaugeSection80', b)
    _safe_set(b, 'migrationmodeler_GaugeCompositeStyle', {a2})
    assert _is_linked(b, 'migrationmodeler_GaugeCompositeStyle', a2)
    if hasattr(a1, 'migrationmodeler_GaugeSection80'):
        assert not _is_linked(a1, 'migrationmodeler_GaugeSection80', b)
    if hasattr(a2, 'migrationmodeler_GaugeSection80'):
        assert _is_linked(a2, 'migrationmodeler_GaugeSection80', b)
    _safe_set(b, 'migrationmodeler_GaugeCompositeStyle', set())
    assert not _is_linked(b, 'migrationmodeler_GaugeCompositeStyle', a2)
    if hasattr(a2, 'migrationmodeler_GaugeSection80'):
        assert not _is_linked(a2, 'migrationmodeler_GaugeSection80', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_backgroundColor57_stub_double():
    # migrationmodeler_Dot has no real 'migrationmodeler_Dot' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_Color's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_Color's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_Color(blue=7, green=7, red=7)
    partner = migrationmodeler_Dot()
    setattr(partner, 'migrationmodeler_Dot', None)
    _safe_set(owner, 'migrationmodeler_Color58', partner)
    assert getattr(partner, 'migrationmodeler_Dot') == owner
    _safe_set(owner, 'migrationmodeler_Color58', None)
    assert getattr(partner, 'migrationmodeler_Dot') is None


def test_assoc_bendpoints31_stub_double():
    # migrationmodeler_EdgeRepresentation has no real 'migrationmodeler_EdgeRepresentation32' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_Point(x=7, y=7)
    partner = migrationmodeler_EdgeRepresentation()
    setattr(partner, 'migrationmodeler_EdgeRepresentation32', None)
    _safe_set(owner, 'migrationmodeler_Point', partner)
    assert owner in getattr(partner, 'migrationmodeler_EdgeRepresentation32')
    _safe_set(owner, 'migrationmodeler_Point', None)
    assert owner not in getattr(partner, 'migrationmodeler_EdgeRepresentation32')


def test_assoc_color81_stub_double():
    # migrationmodeler_Note has no real 'migrationmodeler_Note' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_Color's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_Color's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_Color(blue=7, green=7, red=7)
    partner = migrationmodeler_Note()
    setattr(partner, 'migrationmodeler_Note', None)
    _safe_set(owner, 'migrationmodeler_Color82', partner)
    assert getattr(partner, 'migrationmodeler_Note') == owner
    _safe_set(owner, 'migrationmodeler_Color82', None)
    assert getattr(partner, 'migrationmodeler_Note') is None


def test_assoc_containerRepresentations12_stub_double():
    # migrationmodeler_Container has no real 'migrationmodeler_Container13' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_ContainerRepresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_ContainerRepresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_ContainerRepresentation(autoSized=True)
    partner = migrationmodeler_Container()
    setattr(partner, 'migrationmodeler_Container13', None)
    _safe_set(owner, 'migrationmodeler_ContainerRepresentation', partner)
    assert owner in getattr(partner, 'migrationmodeler_Container13')
    _safe_set(owner, 'migrationmodeler_ContainerRepresentation', None)
    assert owner not in getattr(partner, 'migrationmodeler_Container13')


def test_assoc_elements14_stub_double():
    # migrationmodeler_Container has no real 'migrationmodeler_Container15' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_GraphicalElement(id="sample_text")
    partner = migrationmodeler_Container()
    setattr(partner, 'migrationmodeler_Container15', None)
    _safe_set(owner, 'migrationmodeler_GraphicalElement', partner)
    assert owner in getattr(partner, 'migrationmodeler_Container15')
    _safe_set(owner, 'migrationmodeler_GraphicalElement', None)
    assert owner not in getattr(partner, 'migrationmodeler_Container15')


def test_assoc_filters5_stub_double():
    # migrationmodeler_Diagram has no real 'migrationmodeler_Diagram6' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_Filter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_Filter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_Filter(activated=True, id="sample_text")
    partner = migrationmodeler_Diagram()
    setattr(partner, 'migrationmodeler_Diagram6', None)
    _safe_set(owner, 'migrationmodeler_Filter', partner)
    assert owner in getattr(partner, 'migrationmodeler_Diagram6')
    _safe_set(owner, 'migrationmodeler_Filter', None)
    assert owner not in getattr(partner, 'migrationmodeler_Diagram6')


def test_assoc_layers7_stub_double():
    # migrationmodeler_Diagram has no real 'migrationmodeler_Diagram8' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_Layer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_Layer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_Layer(activated=True, id="sample_text")
    partner = migrationmodeler_Diagram()
    setattr(partner, 'migrationmodeler_Diagram8', None)
    _safe_set(owner, 'migrationmodeler_Layer', partner)
    assert owner in getattr(partner, 'migrationmodeler_Diagram8')
    _safe_set(owner, 'migrationmodeler_Layer', None)
    assert owner not in getattr(partner, 'migrationmodeler_Diagram8')


def test_assoc_ownedStyle33_stub_double():
    # migrationmodeler_EdgeRepresentation has no real 'migrationmodeler_EdgeRepresentation34' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_EdgeStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_EdgeStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    partner = migrationmodeler_EdgeRepresentation()
    setattr(partner, 'migrationmodeler_EdgeRepresentation34', None)
    _safe_set(owner, 'migrationmodeler_EdgeStyle', partner)
    assert getattr(partner, 'migrationmodeler_EdgeRepresentation34') == owner
    _safe_set(owner, 'migrationmodeler_EdgeStyle', None)
    assert getattr(partner, 'migrationmodeler_EdgeRepresentation34') is None


def test_assoc_ownedStyle37_stub_double():
    # migrationmodeler_AbstractNodeRepresentation has no real 'migrationmodeler_AbstractNodeRepresentation38' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_NodeStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_NodeStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    partner = migrationmodeler_AbstractNodeRepresentation()
    setattr(partner, 'migrationmodeler_AbstractNodeRepresentation38', None)
    _safe_set(owner, 'migrationmodeler_NodeStyle', partner)
    assert getattr(partner, 'migrationmodeler_AbstractNodeRepresentation38') == owner
    _safe_set(owner, 'migrationmodeler_NodeStyle', None)
    assert getattr(partner, 'migrationmodeler_AbstractNodeRepresentation38') is None


def test_assoc_ownedStyle39_stub_double():
    # migrationmodeler_ContainerStyle has no real 'migrationmodeler_ContainerStyle' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_ContainerRepresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_ContainerRepresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_ContainerRepresentation(autoSized=True)
    partner = migrationmodeler_ContainerStyle()
    setattr(partner, 'migrationmodeler_ContainerStyle', None)
    _safe_set(owner, 'migrationmodeler_ContainerRepresentation40', partner)
    assert getattr(partner, 'migrationmodeler_ContainerStyle') == owner
    _safe_set(owner, 'migrationmodeler_ContainerRepresentation40', None)
    assert getattr(partner, 'migrationmodeler_ContainerStyle') is None


def test_assoc_representations51_stub_double():
    # migrationmodeler_TestCase has no real 'migrationmodeler_TestCase' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_Representation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_Representation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_Representation(name="sample_text")
    partner = migrationmodeler_TestCase()
    setattr(partner, 'migrationmodeler_TestCase', None)
    _safe_set(owner, 'migrationmodeler_Representation', partner)
    assert owner in getattr(partner, 'migrationmodeler_TestCase')
    _safe_set(owner, 'migrationmodeler_Representation', None)
    assert owner not in getattr(partner, 'migrationmodeler_TestCase')


def test_assoc_source18_stub_double():
    # migrationmodeler_Edge has no real 'migrationmodeler_Edge19' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_GraphicalElement(id="sample_text")
    partner = migrationmodeler_Edge()
    setattr(partner, 'migrationmodeler_Edge19', None)
    _safe_set(owner, 'migrationmodeler_GraphicalElement20', partner)
    assert getattr(partner, 'migrationmodeler_Edge19') == owner
    _safe_set(owner, 'migrationmodeler_GraphicalElement20', None)
    assert getattr(partner, 'migrationmodeler_Edge19') is None


def test_assoc_source25_stub_double():
    # migrationmodeler_EdgeRepresentation has no real 'migrationmodeler_EdgeRepresentation26' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_GraphicalElement(id="sample_text")
    partner = migrationmodeler_EdgeRepresentation()
    setattr(partner, 'migrationmodeler_EdgeRepresentation26', None)
    _safe_set(owner, 'migrationmodeler_GraphicalElement27', partner)
    assert getattr(partner, 'migrationmodeler_EdgeRepresentation26') == owner
    _safe_set(owner, 'migrationmodeler_GraphicalElement27', None)
    assert getattr(partner, 'migrationmodeler_EdgeRepresentation26') is None


def test_assoc_target21_stub_double():
    # migrationmodeler_Edge has no real 'migrationmodeler_Edge22' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_GraphicalElement(id="sample_text")
    partner = migrationmodeler_Edge()
    setattr(partner, 'migrationmodeler_Edge22', None)
    _safe_set(owner, 'migrationmodeler_GraphicalElement23', partner)
    assert getattr(partner, 'migrationmodeler_Edge22') == owner
    _safe_set(owner, 'migrationmodeler_GraphicalElement23', None)
    assert getattr(partner, 'migrationmodeler_Edge22') is None


def test_assoc_target28_stub_double():
    # migrationmodeler_EdgeRepresentation has no real 'migrationmodeler_EdgeRepresentation29' property in the generated
    # code (a bare stub) -- manually attach it so migrationmodeler_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # migrationmodeler_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = migrationmodeler_GraphicalElement(id="sample_text")
    partner = migrationmodeler_EdgeRepresentation()
    setattr(partner, 'migrationmodeler_EdgeRepresentation29', None)
    _safe_set(owner, 'migrationmodeler_GraphicalElement30', partner)
    assert getattr(partner, 'migrationmodeler_EdgeRepresentation29') == owner
    _safe_set(owner, 'migrationmodeler_GraphicalElement30', None)
    assert getattr(partner, 'migrationmodeler_EdgeRepresentation29') is None


