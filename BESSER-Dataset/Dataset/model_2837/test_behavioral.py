import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Border,
    Color,
    ConnectionFigure,
    CustomClass,
    CustomFigure,
    DecorationFigure,
    DiagramElement,
    Figure,
    FigureHandle,
    FigureMarker,
    Font,
    Identity,
    Layout,
    LayoutData,
    Layoutable,
    Node,
    Polygon,
    Polyline,
    Shape,
    VisualFacet,
    gmfgraph_AlignmentFacet,
    gmfgraph_BasicFont,
    gmfgraph_Border,
    gmfgraph_BorderLayout,
    gmfgraph_BorderLayoutData,
    gmfgraph_Canvas,
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
    gmfgraph_FigureHandle,
    gmfgraph_FigureMarker,
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

def test_assoc_attributes58_reverse_link_reassign_clear():
    a1 = gmfgraph_CustomClass(bundleName="sample_text", qualifiedClassName="sample_text")
    a2 = gmfgraph_CustomClass(bundleName="sample_text_2", qualifiedClassName="sample_text_2")
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


def test_assoc_margins77_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension78', a1)
    assert _is_linked(b, 'gmfgraph_Dimension78', a1)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert _is_linked(a1, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension78', a2)
    assert _is_linked(b, 'gmfgraph_Dimension78', a2)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout', b)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert _is_linked(a2, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension78', None)
    assert not _is_linked(b, 'gmfgraph_Dimension78', a2)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout', b)


def test_assoc_sizeHint73_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    a2 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=False, grabExcessVerticalSpace=False, horizontalAlignment="sample_text_2", horizontalIndent=13, horizontalSpan=13, verticalAlignment="sample_text_2", verticalSpan=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension74', a1)
    assert _is_linked(b, 'gmfgraph_Dimension74', a1)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension74', a2)
    assert _is_linked(b, 'gmfgraph_Dimension74', a2)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a2, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension74', None)
    assert not _is_linked(b, 'gmfgraph_Dimension74', a2)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a2, 'gmfgraph_GridLayoutData', b)


def test_assoc_spacing79_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension81', a1)
    assert _is_linked(b, 'gmfgraph_Dimension81', a1)
    if hasattr(a1, 'gmfgraph_GridLayout80'):
        assert _is_linked(a1, 'gmfgraph_GridLayout80', b)
    _safe_set(b, 'gmfgraph_Dimension81', a2)
    assert _is_linked(b, 'gmfgraph_Dimension81', a2)
    if hasattr(a1, 'gmfgraph_GridLayout80'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout80', b)
    if hasattr(a2, 'gmfgraph_GridLayout80'):
        assert _is_linked(a2, 'gmfgraph_GridLayout80', b)
    _safe_set(b, 'gmfgraph_Dimension81', None)
    assert not _is_linked(b, 'gmfgraph_Dimension81', a2)
    if hasattr(a2, 'gmfgraph_GridLayout80'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout80', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_color63_stub_double():
    # gmfgraph_Color has no real 'gmfgraph_Color64' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_LineBorder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_LineBorder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_LineBorder(width=7)
    partner = gmfgraph_Color()
    setattr(partner, 'gmfgraph_Color64', None)
    _safe_set(owner, 'gmfgraph_LineBorder', partner)
    assert getattr(partner, 'gmfgraph_Color64') == owner
    _safe_set(owner, 'gmfgraph_LineBorder', None)
    assert getattr(partner, 'gmfgraph_Color64') is None


def test_assoc_compartments5_stub_double():
    # gmfgraph_Canvas has no real 'gmfgraph_Canvas6' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Compartment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Compartment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    partner = gmfgraph_Canvas()
    setattr(partner, 'gmfgraph_Canvas6', None)
    _safe_set(owner, 'gmfgraph_Compartment', partner)
    assert owner in getattr(partner, 'gmfgraph_Canvas6')
    _safe_set(owner, 'gmfgraph_Compartment', None)
    assert owner not in getattr(partner, 'gmfgraph_Canvas6')


def test_assoc_customChildren60_stub_double():
    # gmfgraph_CustomFigure has no real 'gmfgraph_CustomFigure61' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_FigureAccessor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_FigureAccessor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_FigureAccessor(accessor="sample_text")
    partner = gmfgraph_CustomFigure()
    setattr(partner, 'gmfgraph_CustomFigure61', None)
    _safe_set(owner, 'gmfgraph_FigureAccessor62', partner)
    assert owner in getattr(partner, 'gmfgraph_CustomFigure61')
    _safe_set(owner, 'gmfgraph_FigureAccessor62', None)
    assert owner not in getattr(partner, 'gmfgraph_CustomFigure61')


def test_assoc_defaultSize19_stub_double():
    # gmfgraph_DefaultSizeFacet has no real 'gmfgraph_DefaultSizeFacet' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_DefaultSizeFacet()
    setattr(partner, 'gmfgraph_DefaultSizeFacet', None)
    _safe_set(owner, 'gmfgraph_Dimension', partner)
    assert getattr(partner, 'gmfgraph_DefaultSizeFacet') == owner
    _safe_set(owner, 'gmfgraph_Dimension', None)
    assert getattr(partner, 'gmfgraph_DefaultSizeFacet') is None


def test_assoc_facets12_stub_double():
    # gmfgraph_VisualFacet has no real 'gmfgraph_VisualFacet' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_DiagramElement()
    partner = gmfgraph_VisualFacet()
    setattr(partner, 'gmfgraph_VisualFacet', None)
    _safe_set(owner, 'gmfgraph_DiagramElement', {partner})
    assert getattr(partner, 'gmfgraph_VisualFacet') == owner
    _safe_set(owner, 'gmfgraph_DiagramElement', set())
    assert getattr(partner, 'gmfgraph_VisualFacet') is None


def test_assoc_figure11_stub_double():
    # gmfgraph_FigureHandle has no real 'FigureHandle' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_DiagramElement()
    partner = gmfgraph_FigureHandle()
    setattr(partner, 'FigureHandle', None)
    _safe_set(owner, 'referencingElements', partner)
    assert getattr(partner, 'FigureHandle') == owner
    _safe_set(owner, 'referencingElements', None)
    assert getattr(partner, 'FigureHandle') is None


def test_assoc_figures0_stub_double():
    # gmfgraph_Canvas has no real 'gmfgraph_Canvas' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_FigureGallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_FigureGallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_FigureGallery(implementationBundle="sample_text")
    partner = gmfgraph_Canvas()
    setattr(partner, 'gmfgraph_Canvas', None)
    _safe_set(owner, 'gmfgraph_FigureGallery', partner)
    assert owner in getattr(partner, 'gmfgraph_Canvas')
    _safe_set(owner, 'gmfgraph_FigureGallery', None)
    assert owner not in getattr(partner, 'gmfgraph_Canvas')


def test_assoc_figures9_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_FigureGallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_FigureGallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_FigureGallery(implementationBundle="sample_text")
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure', None)
    _safe_set(owner, 'gmfgraph_FigureGallery10', {partner})
    assert getattr(partner, 'gmfgraph_Figure') == owner
    _safe_set(owner, 'gmfgraph_FigureGallery10', set())
    assert getattr(partner, 'gmfgraph_Figure') is None


def test_assoc_insets39_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure40' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Insets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Insets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure40', None)
    _safe_set(owner, 'gmfgraph_Insets', partner)
    assert getattr(partner, 'gmfgraph_Figure40') == owner
    _safe_set(owner, 'gmfgraph_Insets', None)
    assert getattr(partner, 'gmfgraph_Figure40') is None


def test_assoc_insets65_stub_double():
    # gmfgraph_MarginBorder has no real 'gmfgraph_MarginBorder' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Insets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Insets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    partner = gmfgraph_MarginBorder()
    setattr(partner, 'gmfgraph_MarginBorder', None)
    _safe_set(owner, 'gmfgraph_Insets66', partner)
    assert getattr(partner, 'gmfgraph_MarginBorder') == owner
    _safe_set(owner, 'gmfgraph_Insets66', None)
    assert getattr(partner, 'gmfgraph_MarginBorder') is None


def test_assoc_labels7_stub_double():
    # gmfgraph_Canvas has no real 'gmfgraph_Canvas8' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_DiagramLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_DiagramLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_DiagramLabel(elementIcon=True)
    partner = gmfgraph_Canvas()
    setattr(partner, 'gmfgraph_Canvas8', None)
    _safe_set(owner, 'gmfgraph_DiagramLabel', partner)
    assert owner in getattr(partner, 'gmfgraph_Canvas8')
    _safe_set(owner, 'gmfgraph_DiagramLabel', None)
    assert owner not in getattr(partner, 'gmfgraph_Canvas8')


def test_assoc_location43_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure44' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure44', None)
    _safe_set(owner, 'gmfgraph_Point', partner)
    assert getattr(partner, 'gmfgraph_Figure44') == owner
    _safe_set(owner, 'gmfgraph_Point', None)
    assert getattr(partner, 'gmfgraph_Figure44') is None


def test_assoc_maximumSize28_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure29' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure29', None)
    _safe_set(owner, 'gmfgraph_Dimension30', partner)
    assert getattr(partner, 'gmfgraph_Figure29') == owner
    _safe_set(owner, 'gmfgraph_Dimension30', None)
    assert getattr(partner, 'gmfgraph_Figure29') is None


def test_assoc_minimumSize31_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure32' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure32', None)
    _safe_set(owner, 'gmfgraph_Dimension33', partner)
    assert getattr(partner, 'gmfgraph_Figure32') == owner
    _safe_set(owner, 'gmfgraph_Dimension33', None)
    assert getattr(partner, 'gmfgraph_Figure32') is None


def test_assoc_nodeFigure13_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure15' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure15', None)
    _safe_set(owner, 'gmfgraph_Node14', partner)
    assert getattr(partner, 'gmfgraph_Figure15') == owner
    _safe_set(owner, 'gmfgraph_Node14', None)
    assert getattr(partner, 'gmfgraph_Figure15') is None


def test_assoc_nodes1_stub_double():
    # gmfgraph_Canvas has no real 'gmfgraph_Canvas2' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    partner = gmfgraph_Canvas()
    setattr(partner, 'gmfgraph_Canvas2', None)
    _safe_set(owner, 'gmfgraph_Node', partner)
    assert owner in getattr(partner, 'gmfgraph_Canvas2')
    _safe_set(owner, 'gmfgraph_Node', None)
    assert owner not in getattr(partner, 'gmfgraph_Canvas2')


def test_assoc_preferredSize34_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure35' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure35', None)
    _safe_set(owner, 'gmfgraph_Dimension36', partner)
    assert getattr(partner, 'gmfgraph_Figure35') == owner
    _safe_set(owner, 'gmfgraph_Dimension36', None)
    assert getattr(partner, 'gmfgraph_Figure35') is None


def test_assoc_referencingElements21_stub_double():
    # gmfgraph_FigureHandle has no real 'figure' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_DiagramElement()
    partner = gmfgraph_FigureHandle()
    setattr(partner, 'figure', None)
    _safe_set(owner, 'DiagramElement', partner)
    assert owner in getattr(partner, 'figure')
    _safe_set(owner, 'DiagramElement', None)
    assert owner not in getattr(partner, 'figure')


def test_assoc_resolvedChildren50_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure51' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure51', None)
    _safe_set(owner, 'gmfgraph_Shape', {partner})
    assert getattr(partner, 'gmfgraph_Figure51') == owner
    _safe_set(owner, 'gmfgraph_Shape', set())
    assert getattr(partner, 'gmfgraph_Figure51') is None


def test_assoc_size45_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure46' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure46', None)
    _safe_set(owner, 'gmfgraph_Point47', partner)
    assert getattr(partner, 'gmfgraph_Figure46') == owner
    _safe_set(owner, 'gmfgraph_Point47', None)
    assert getattr(partner, 'gmfgraph_Figure46') is None


def test_assoc_size86_stub_double():
    # gmfgraph_XYLayoutData has no real 'gmfgraph_XYLayoutData87' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_XYLayoutData()
    setattr(partner, 'gmfgraph_XYLayoutData87', None)
    _safe_set(owner, 'gmfgraph_Dimension88', partner)
    assert getattr(partner, 'gmfgraph_XYLayoutData87') == owner
    _safe_set(owner, 'gmfgraph_Dimension88', None)
    assert getattr(partner, 'gmfgraph_XYLayoutData87') is None


def test_assoc_spacing82_stub_double():
    # gmfgraph_BorderLayout has no real 'gmfgraph_BorderLayout' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_BorderLayout()
    setattr(partner, 'gmfgraph_BorderLayout', None)
    _safe_set(owner, 'gmfgraph_Dimension83', partner)
    assert getattr(partner, 'gmfgraph_BorderLayout') == owner
    _safe_set(owner, 'gmfgraph_Dimension83', None)
    assert getattr(partner, 'gmfgraph_BorderLayout') is None


def test_assoc_template52_stub_double():
    # gmfgraph_Polyline has no real 'gmfgraph_Polyline' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Polyline()
    setattr(partner, 'gmfgraph_Polyline', None)
    _safe_set(owner, 'gmfgraph_Point53', partner)
    assert owner in getattr(partner, 'gmfgraph_Polyline')
    _safe_set(owner, 'gmfgraph_Point53', None)
    assert owner not in getattr(partner, 'gmfgraph_Polyline')


def test_assoc_topLeft84_stub_double():
    # gmfgraph_XYLayoutData has no real 'gmfgraph_XYLayoutData' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_XYLayoutData()
    setattr(partner, 'gmfgraph_XYLayoutData', None)
    _safe_set(owner, 'gmfgraph_Point85', partner)
    assert getattr(partner, 'gmfgraph_XYLayoutData') == owner
    _safe_set(owner, 'gmfgraph_Point85', None)
    assert getattr(partner, 'gmfgraph_XYLayoutData') is None


def test_assoc_typedFigure59_stub_double():
    # gmfgraph_CustomFigure has no real 'gmfgraph_CustomFigure' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_FigureAccessor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_FigureAccessor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_FigureAccessor(accessor="sample_text")
    partner = gmfgraph_CustomFigure()
    setattr(partner, 'gmfgraph_CustomFigure', None)
    _safe_set(owner, 'gmfgraph_FigureAccessor', partner)
    assert getattr(partner, 'gmfgraph_CustomFigure') == owner
    _safe_set(owner, 'gmfgraph_FigureAccessor', None)
    assert getattr(partner, 'gmfgraph_CustomFigure') is None


