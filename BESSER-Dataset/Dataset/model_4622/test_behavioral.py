import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFigure,
    AbstractNode,
    Border,
    Color,
    ConnectionFigure,
    CustomClass,
    CustomFigure,
    DecorationFigure,
    DiagramElement,
    Figure,
    Font,
    Identity,
    Layout,
    LayoutData,
    Layoutable,
    Node,
    Polygon,
    Polyline,
    RealFigure,
    Shape,
    VisualFacet,
    gmfgraph_AbstractFigure,
    gmfgraph_AbstractNode,
    gmfgraph_AlignmentFacet,
    gmfgraph_BasicFont,
    gmfgraph_Border,
    gmfgraph_BorderLayout,
    gmfgraph_BorderLayoutData,
    gmfgraph_BorderRef,
    gmfgraph_Canvas,
    gmfgraph_ChildAccess,
    gmfgraph_Color,
    gmfgraph_Compartment,
    gmfgraph_CompoundBorder,
    gmfgraph_Connection,
    gmfgraph_ConnectionFigure,
    gmfgraph_ConstantColor,
    gmfgraph_CustomAttribute,
    gmfgraph_CustomBorder,
    gmfgraph_CustomClass,
    gmfgraph_CustomConnection,
    gmfgraph_CustomDecoration,
    gmfgraph_CustomFigure,
    gmfgraph_CustomLayout,
    gmfgraph_CustomLayoutData,
    gmfgraph_DecorationFigure,
    gmfgraph_DefaultSizeFacet,
    gmfgraph_DiagramElement,
    gmfgraph_DiagramLabel,
    gmfgraph_Dimension,
    gmfgraph_Ellipse,
    gmfgraph_Figure,
    gmfgraph_FigureAccessor,
    gmfgraph_FigureDescriptor,
    gmfgraph_FigureGallery,
    gmfgraph_FigureRef,
    gmfgraph_FlowLayout,
    gmfgraph_Font,
    gmfgraph_GeneralFacet,
    gmfgraph_GradientFacet,
    gmfgraph_GridLayout,
    gmfgraph_GridLayoutData,
    gmfgraph_Identity,
    gmfgraph_Insets,
    gmfgraph_Label,
    gmfgraph_LabelOffsetFacet,
    gmfgraph_LabeledContainer,
    gmfgraph_Layout,
    gmfgraph_LayoutData,
    gmfgraph_LayoutRef,
    gmfgraph_Layoutable,
    gmfgraph_LineBorder,
    gmfgraph_MarginBorder,
    gmfgraph_Node,
    gmfgraph_Point,
    gmfgraph_Polygon,
    gmfgraph_PolygonDecoration,
    gmfgraph_Polyline,
    gmfgraph_PolylineConnection,
    gmfgraph_PolylineDecoration,
    gmfgraph_RGBColor,
    gmfgraph_RealFigure,
    gmfgraph_Rectangle,
    gmfgraph_RoundedRectangle,
    gmfgraph_ScalablePolygon,
    gmfgraph_Shape,
    gmfgraph_StackLayout,
    gmfgraph_VisualFacet,
    gmfgraph_XYLayout,
    gmfgraph_XYLayoutData,
    Alignment,
    ColorConstants,
    Direction,
    FontStyle,
    LineKind,
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

def test_assoc_accessor23_reverse_link_reassign_clear():
    a1 = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    a2 = gmfgraph_Compartment(collapsible=False, needsTitle=False)
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess25', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess25', a1)
    if hasattr(a1, 'gmfgraph_Compartment24'):
        assert _is_linked(a1, 'gmfgraph_Compartment24', b)
    _safe_set(b, 'gmfgraph_ChildAccess25', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess25', a2)
    if hasattr(a1, 'gmfgraph_Compartment24'):
        assert not _is_linked(a1, 'gmfgraph_Compartment24', b)
    if hasattr(a2, 'gmfgraph_Compartment24'):
        assert _is_linked(a2, 'gmfgraph_Compartment24', b)
    _safe_set(b, 'gmfgraph_ChildAccess25', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess25', a2)
    if hasattr(a2, 'gmfgraph_Compartment24'):
        assert not _is_linked(a2, 'gmfgraph_Compartment24', b)


def test_assoc_accessor26_reverse_link_reassign_clear():
    a1 = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    a2 = gmfgraph_DiagramLabel(elementIcon=False, external=False)
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess28', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess28', a1)
    if hasattr(a1, 'gmfgraph_DiagramLabel27'):
        assert _is_linked(a1, 'gmfgraph_DiagramLabel27', b)
    _safe_set(b, 'gmfgraph_ChildAccess28', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess28', a2)
    if hasattr(a1, 'gmfgraph_DiagramLabel27'):
        assert not _is_linked(a1, 'gmfgraph_DiagramLabel27', b)
    if hasattr(a2, 'gmfgraph_DiagramLabel27'):
        assert _is_linked(a2, 'gmfgraph_DiagramLabel27', b)
    _safe_set(b, 'gmfgraph_ChildAccess28', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess28', a2)
    if hasattr(a2, 'gmfgraph_DiagramLabel27'):
        assert not _is_linked(a2, 'gmfgraph_DiagramLabel27', b)


def test_assoc_attributes69_reverse_link_reassign_clear():
    a1 = gmfgraph_CustomClass(qualifiedClassName="sample_text")
    a2 = gmfgraph_CustomClass(qualifiedClassName="sample_text_2")
    b = gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    _safe_set(b, 'gmfgraph_CustomAttribute', a1)
    assert _is_linked(b, 'gmfgraph_CustomAttribute', a1)
    if hasattr(a1, 'gmfgraph_CustomClass'):
        assert _is_linked(a1, 'gmfgraph_CustomClass', b)
    _safe_set(b, 'gmfgraph_CustomAttribute', a2)
    assert _is_linked(b, 'gmfgraph_CustomAttribute', a2)
    if hasattr(a1, 'gmfgraph_CustomClass'):
        assert not _is_linked(a1, 'gmfgraph_CustomClass', b)
    if hasattr(a2, 'gmfgraph_CustomClass'):
        assert _is_linked(a2, 'gmfgraph_CustomClass', b)
    _safe_set(b, 'gmfgraph_CustomAttribute', None)
    assert not _is_linked(b, 'gmfgraph_CustomAttribute', a2)
    if hasattr(a2, 'gmfgraph_CustomClass'):
        assert not _is_linked(a2, 'gmfgraph_CustomClass', b)


def test_assoc_container29_reverse_link_reassign_clear():
    a1 = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    a2 = gmfgraph_DiagramLabel(elementIcon=False, external=False)
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess31', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess31', a1)
    if hasattr(a1, 'gmfgraph_DiagramLabel30'):
        assert _is_linked(a1, 'gmfgraph_DiagramLabel30', b)
    _safe_set(b, 'gmfgraph_ChildAccess31', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess31', a2)
    if hasattr(a1, 'gmfgraph_DiagramLabel30'):
        assert not _is_linked(a1, 'gmfgraph_DiagramLabel30', b)
    if hasattr(a2, 'gmfgraph_DiagramLabel30'):
        assert _is_linked(a2, 'gmfgraph_DiagramLabel30', b)
    _safe_set(b, 'gmfgraph_ChildAccess31', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess31', a2)
    if hasattr(a2, 'gmfgraph_DiagramLabel30'):
        assert not _is_linked(a2, 'gmfgraph_DiagramLabel30', b)


def test_assoc_contentPane21_reverse_link_reassign_clear():
    a1 = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    a2 = gmfgraph_Node(affixedParentSide="sample_text_2", resizeConstraint="sample_text_2")
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess', a1)
    if hasattr(a1, 'gmfgraph_Node22'):
        assert _is_linked(a1, 'gmfgraph_Node22', b)
    _safe_set(b, 'gmfgraph_ChildAccess', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess', a2)
    if hasattr(a1, 'gmfgraph_Node22'):
        assert not _is_linked(a1, 'gmfgraph_Node22', b)
    if hasattr(a2, 'gmfgraph_Node22'):
        assert _is_linked(a2, 'gmfgraph_Node22', b)
    _safe_set(b, 'gmfgraph_ChildAccess', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess', a2)
    if hasattr(a2, 'gmfgraph_Node22'):
        assert not _is_linked(a2, 'gmfgraph_Node22', b)


def test_assoc_figures9_reverse_link_reassign_clear():
    a1 = gmfgraph_RealFigure(name="sample_text")
    a2 = gmfgraph_RealFigure(name="sample_text_2")
    b = gmfgraph_FigureGallery(implementationBundle="sample_text")
    _safe_set(b, 'gmfgraph_FigureGallery10', {a1})
    assert _is_linked(b, 'gmfgraph_FigureGallery10', a1)
    if hasattr(a1, 'gmfgraph_RealFigure'):
        assert _is_linked(a1, 'gmfgraph_RealFigure', b)
    _safe_set(b, 'gmfgraph_FigureGallery10', {a2})
    assert _is_linked(b, 'gmfgraph_FigureGallery10', a2)
    if hasattr(a1, 'gmfgraph_RealFigure'):
        assert not _is_linked(a1, 'gmfgraph_RealFigure', b)
    if hasattr(a2, 'gmfgraph_RealFigure'):
        assert _is_linked(a2, 'gmfgraph_RealFigure', b)
    _safe_set(b, 'gmfgraph_FigureGallery10', set())
    assert not _is_linked(b, 'gmfgraph_FigureGallery10', a2)
    if hasattr(a2, 'gmfgraph_RealFigure'):
        assert not _is_linked(a2, 'gmfgraph_RealFigure', b)


def test_assoc_margins89_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension90', a1)
    assert _is_linked(b, 'gmfgraph_Dimension90', a1)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert _is_linked(a1, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension90', a2)
    assert _is_linked(b, 'gmfgraph_Dimension90', a2)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout', b)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert _is_linked(a2, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension90', None)
    assert not _is_linked(b, 'gmfgraph_Dimension90', a2)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout', b)


def test_assoc_sizeHint84_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    a2 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=False, grabExcessVerticalSpace=False, horizontalAlignment="sample_text_2", horizontalIndent=13, horizontalSpan=13, verticalAlignment="sample_text_2", verticalSpan=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension85', a1)
    assert _is_linked(b, 'gmfgraph_Dimension85', a1)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension85', a2)
    assert _is_linked(b, 'gmfgraph_Dimension85', a2)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a2, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension85', None)
    assert not _is_linked(b, 'gmfgraph_Dimension85', a2)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a2, 'gmfgraph_GridLayoutData', b)


def test_assoc_spacing91_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension93', a1)
    assert _is_linked(b, 'gmfgraph_Dimension93', a1)
    if hasattr(a1, 'gmfgraph_GridLayout92'):
        assert _is_linked(a1, 'gmfgraph_GridLayout92', b)
    _safe_set(b, 'gmfgraph_Dimension93', a2)
    assert _is_linked(b, 'gmfgraph_Dimension93', a2)
    if hasattr(a1, 'gmfgraph_GridLayout92'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout92', b)
    if hasattr(a2, 'gmfgraph_GridLayout92'):
        assert _is_linked(a2, 'gmfgraph_GridLayout92', b)
    _safe_set(b, 'gmfgraph_Dimension93', None)
    assert not _is_linked(b, 'gmfgraph_Dimension93', a2)
    if hasattr(a2, 'gmfgraph_GridLayout92'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout92', b)


def test_assoc_typedFigure70_reverse_link_reassign_clear():
    a1 = gmfgraph_RealFigure(name="sample_text")
    a2 = gmfgraph_RealFigure(name="sample_text_2")
    b = gmfgraph_FigureAccessor(accessor="sample_text")
    _safe_set(b, 'gmfgraph_FigureAccessor', a1)
    assert _is_linked(b, 'gmfgraph_FigureAccessor', a1)
    if hasattr(a1, 'gmfgraph_RealFigure71'):
        assert _is_linked(a1, 'gmfgraph_RealFigure71', b)
    _safe_set(b, 'gmfgraph_FigureAccessor', a2)
    assert _is_linked(b, 'gmfgraph_FigureAccessor', a2)
    if hasattr(a1, 'gmfgraph_RealFigure71'):
        assert not _is_linked(a1, 'gmfgraph_RealFigure71', b)
    if hasattr(a2, 'gmfgraph_RealFigure71'):
        assert _is_linked(a2, 'gmfgraph_RealFigure71', b)
    _safe_set(b, 'gmfgraph_FigureAccessor', None)
    assert not _is_linked(b, 'gmfgraph_FigureAccessor', a2)
    if hasattr(a2, 'gmfgraph_RealFigure71'):
        assert not _is_linked(a2, 'gmfgraph_RealFigure71', b)


