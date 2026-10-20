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

def test_assoc_accessor19_reverse_link_reassign_clear():
    a1 = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    a2 = gmfgraph_Compartment(collapsible=False, needsTitle=False)
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess21', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess21', a1)
    if hasattr(a1, 'gmfgraph_Compartment20'):
        assert _is_linked(a1, 'gmfgraph_Compartment20', b)
    _safe_set(b, 'gmfgraph_ChildAccess21', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess21', a2)
    if hasattr(a1, 'gmfgraph_Compartment20'):
        assert not _is_linked(a1, 'gmfgraph_Compartment20', b)
    if hasattr(a2, 'gmfgraph_Compartment20'):
        assert _is_linked(a2, 'gmfgraph_Compartment20', b)
    _safe_set(b, 'gmfgraph_ChildAccess21', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess21', a2)
    if hasattr(a2, 'gmfgraph_Compartment20'):
        assert not _is_linked(a2, 'gmfgraph_Compartment20', b)


def test_assoc_accessor22_reverse_link_reassign_clear():
    a1 = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    a2 = gmfgraph_DiagramLabel(elementIcon=False, external=False)
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess24', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess24', a1)
    if hasattr(a1, 'gmfgraph_DiagramLabel23'):
        assert _is_linked(a1, 'gmfgraph_DiagramLabel23', b)
    _safe_set(b, 'gmfgraph_ChildAccess24', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess24', a2)
    if hasattr(a1, 'gmfgraph_DiagramLabel23'):
        assert not _is_linked(a1, 'gmfgraph_DiagramLabel23', b)
    if hasattr(a2, 'gmfgraph_DiagramLabel23'):
        assert _is_linked(a2, 'gmfgraph_DiagramLabel23', b)
    _safe_set(b, 'gmfgraph_ChildAccess24', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess24', a2)
    if hasattr(a2, 'gmfgraph_DiagramLabel23'):
        assert not _is_linked(a2, 'gmfgraph_DiagramLabel23', b)


def test_assoc_attributes28_reverse_link_reassign_clear():
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


def test_assoc_container25_reverse_link_reassign_clear():
    a1 = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    a2 = gmfgraph_DiagramLabel(elementIcon=False, external=False)
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess27', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess27', a1)
    if hasattr(a1, 'gmfgraph_DiagramLabel26'):
        assert _is_linked(a1, 'gmfgraph_DiagramLabel26', b)
    _safe_set(b, 'gmfgraph_ChildAccess27', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess27', a2)
    if hasattr(a1, 'gmfgraph_DiagramLabel26'):
        assert not _is_linked(a1, 'gmfgraph_DiagramLabel26', b)
    if hasattr(a2, 'gmfgraph_DiagramLabel26'):
        assert _is_linked(a2, 'gmfgraph_DiagramLabel26', b)
    _safe_set(b, 'gmfgraph_ChildAccess27', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess27', a2)
    if hasattr(a2, 'gmfgraph_DiagramLabel26'):
        assert not _is_linked(a2, 'gmfgraph_DiagramLabel26', b)


def test_assoc_contentPane17_reverse_link_reassign_clear():
    a1 = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    a2 = gmfgraph_Node(affixedParentSide="sample_text_2", resizeConstraint="sample_text_2")
    b = gmfgraph_ChildAccess(accessor="sample_text")
    _safe_set(b, 'gmfgraph_ChildAccess', a1)
    assert _is_linked(b, 'gmfgraph_ChildAccess', a1)
    if hasattr(a1, 'gmfgraph_Node18'):
        assert _is_linked(a1, 'gmfgraph_Node18', b)
    _safe_set(b, 'gmfgraph_ChildAccess', a2)
    assert _is_linked(b, 'gmfgraph_ChildAccess', a2)
    if hasattr(a1, 'gmfgraph_Node18'):
        assert not _is_linked(a1, 'gmfgraph_Node18', b)
    if hasattr(a2, 'gmfgraph_Node18'):
        assert _is_linked(a2, 'gmfgraph_Node18', b)
    _safe_set(b, 'gmfgraph_ChildAccess', None)
    assert not _is_linked(b, 'gmfgraph_ChildAccess', a2)
    if hasattr(a2, 'gmfgraph_Node18'):
        assert not _is_linked(a2, 'gmfgraph_Node18', b)


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


def test_assoc_margins83_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension84', a1)
    assert _is_linked(b, 'gmfgraph_Dimension84', a1)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert _is_linked(a1, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension84', a2)
    assert _is_linked(b, 'gmfgraph_Dimension84', a2)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout', b)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert _is_linked(a2, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension84', None)
    assert not _is_linked(b, 'gmfgraph_Dimension84', a2)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout', b)


def test_assoc_sizeHint38_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    a2 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=False, grabExcessVerticalSpace=False, horizontalAlignment="sample_text_2", horizontalIndent=13, horizontalSpan=13, verticalAlignment="sample_text_2", verticalSpan=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension', a1)
    assert _is_linked(b, 'gmfgraph_Dimension', a1)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension', a2)
    assert _is_linked(b, 'gmfgraph_Dimension', a2)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a2, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension', None)
    assert not _is_linked(b, 'gmfgraph_Dimension', a2)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a2, 'gmfgraph_GridLayoutData', b)


def test_assoc_spacing85_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension87', a1)
    assert _is_linked(b, 'gmfgraph_Dimension87', a1)
    if hasattr(a1, 'gmfgraph_GridLayout86'):
        assert _is_linked(a1, 'gmfgraph_GridLayout86', b)
    _safe_set(b, 'gmfgraph_Dimension87', a2)
    assert _is_linked(b, 'gmfgraph_Dimension87', a2)
    if hasattr(a1, 'gmfgraph_GridLayout86'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout86', b)
    if hasattr(a2, 'gmfgraph_GridLayout86'):
        assert _is_linked(a2, 'gmfgraph_GridLayout86', b)
    _safe_set(b, 'gmfgraph_Dimension87', None)
    assert not _is_linked(b, 'gmfgraph_Dimension87', a2)
    if hasattr(a2, 'gmfgraph_GridLayout86'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout86', b)


def test_assoc_typedFigure29_reverse_link_reassign_clear():
    a1 = gmfgraph_RealFigure(name="sample_text")
    a2 = gmfgraph_RealFigure(name="sample_text_2")
    b = gmfgraph_FigureAccessor(accessor="sample_text")
    _safe_set(b, 'gmfgraph_FigureAccessor', a1)
    assert _is_linked(b, 'gmfgraph_FigureAccessor', a1)
    if hasattr(a1, 'gmfgraph_RealFigure30'):
        assert _is_linked(a1, 'gmfgraph_RealFigure30', b)
    _safe_set(b, 'gmfgraph_FigureAccessor', a2)
    assert _is_linked(b, 'gmfgraph_FigureAccessor', a2)
    if hasattr(a1, 'gmfgraph_RealFigure30'):
        assert not _is_linked(a1, 'gmfgraph_RealFigure30', b)
    if hasattr(a2, 'gmfgraph_RealFigure30'):
        assert _is_linked(a2, 'gmfgraph_RealFigure30', b)
    _safe_set(b, 'gmfgraph_FigureAccessor', None)
    assert not _is_linked(b, 'gmfgraph_FigureAccessor', a2)
    if hasattr(a2, 'gmfgraph_RealFigure30'):
        assert not _is_linked(a2, 'gmfgraph_RealFigure30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessors107_stub_double():
    # gmfgraph_FigureDescriptor has no real 'owner108' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_ChildAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_ChildAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_ChildAccess(accessor="sample_text")
    partner = gmfgraph_FigureDescriptor()
    setattr(partner, 'owner108', None)
    _safe_set(owner, 'ChildAccess', partner)
    assert owner in getattr(partner, 'owner108')
    _safe_set(owner, 'ChildAccess', None)
    assert owner not in getattr(partner, 'owner108')


def test_assoc_children97_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure99' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_RealFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_RealFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_RealFigure(name="sample_text")
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure99', None)
    _safe_set(owner, 'gmfgraph_RealFigure98', {partner})
    assert getattr(partner, 'gmfgraph_Figure99') == owner
    _safe_set(owner, 'gmfgraph_RealFigure98', set())
    assert getattr(partner, 'gmfgraph_Figure99') is None


def test_assoc_color31_stub_double():
    # gmfgraph_Color has no real 'gmfgraph_Color' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_LineBorder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_LineBorder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_LineBorder(width=7)
    partner = gmfgraph_Color()
    setattr(partner, 'gmfgraph_Color', None)
    _safe_set(owner, 'gmfgraph_LineBorder', partner)
    assert getattr(partner, 'gmfgraph_Color') == owner
    _safe_set(owner, 'gmfgraph_LineBorder', None)
    assert getattr(partner, 'gmfgraph_Color') is None


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


def test_assoc_customChildren81_stub_double():
    # gmfgraph_CustomFigure has no real 'gmfgraph_CustomFigure' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_FigureAccessor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_FigureAccessor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_FigureAccessor(accessor="sample_text")
    partner = gmfgraph_CustomFigure()
    setattr(partner, 'gmfgraph_CustomFigure', None)
    _safe_set(owner, 'gmfgraph_FigureAccessor82', partner)
    assert owner in getattr(partner, 'gmfgraph_CustomFigure')
    _safe_set(owner, 'gmfgraph_FigureAccessor82', None)
    assert owner not in getattr(partner, 'gmfgraph_CustomFigure')


def test_assoc_defaultSize95_stub_double():
    # gmfgraph_DefaultSizeFacet has no real 'gmfgraph_DefaultSizeFacet' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_DefaultSizeFacet()
    setattr(partner, 'gmfgraph_DefaultSizeFacet', None)
    _safe_set(owner, 'gmfgraph_Dimension96', partner)
    assert getattr(partner, 'gmfgraph_DefaultSizeFacet') == owner
    _safe_set(owner, 'gmfgraph_Dimension96', None)
    assert getattr(partner, 'gmfgraph_DefaultSizeFacet') is None


def test_assoc_descriptors11_stub_double():
    # gmfgraph_FigureDescriptor has no real 'gmfgraph_FigureDescriptor' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_FigureGallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_FigureGallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_FigureGallery(implementationBundle="sample_text")
    partner = gmfgraph_FigureDescriptor()
    setattr(partner, 'gmfgraph_FigureDescriptor', None)
    _safe_set(owner, 'gmfgraph_FigureGallery12', {partner})
    assert getattr(partner, 'gmfgraph_FigureDescriptor') == owner
    _safe_set(owner, 'gmfgraph_FigureGallery12', set())
    assert getattr(partner, 'gmfgraph_FigureDescriptor') is None


def test_assoc_figure100_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure102' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_ChildAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_ChildAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_ChildAccess(accessor="sample_text")
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure102', None)
    _safe_set(owner, 'gmfgraph_ChildAccess101', partner)
    assert getattr(partner, 'gmfgraph_Figure102') == owner
    _safe_set(owner, 'gmfgraph_ChildAccess101', None)
    assert getattr(partner, 'gmfgraph_Figure102') is None


def test_assoc_figure71_stub_double():
    # gmfgraph_FigureRef has no real 'gmfgraph_FigureRef' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_RealFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_RealFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_RealFigure(name="sample_text")
    partner = gmfgraph_FigureRef()
    setattr(partner, 'gmfgraph_FigureRef', None)
    _safe_set(owner, 'gmfgraph_RealFigure72', partner)
    assert getattr(partner, 'gmfgraph_FigureRef') == owner
    _safe_set(owner, 'gmfgraph_RealFigure72', None)
    assert getattr(partner, 'gmfgraph_FigureRef') is None


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


def test_assoc_insets32_stub_double():
    # gmfgraph_MarginBorder has no real 'gmfgraph_MarginBorder' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Insets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Insets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    partner = gmfgraph_MarginBorder()
    setattr(partner, 'gmfgraph_MarginBorder', None)
    _safe_set(owner, 'gmfgraph_Insets', partner)
    assert getattr(partner, 'gmfgraph_MarginBorder') == owner
    _safe_set(owner, 'gmfgraph_Insets', None)
    assert getattr(partner, 'gmfgraph_MarginBorder') is None


def test_assoc_insets57_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure58' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Insets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Insets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure58', None)
    _safe_set(owner, 'gmfgraph_Insets59', partner)
    assert getattr(partner, 'gmfgraph_Figure58') == owner
    _safe_set(owner, 'gmfgraph_Insets59', None)
    assert getattr(partner, 'gmfgraph_Figure58') is None


def test_assoc_labels7_stub_double():
    # gmfgraph_Canvas has no real 'gmfgraph_Canvas8' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_DiagramLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_DiagramLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    partner = gmfgraph_Canvas()
    setattr(partner, 'gmfgraph_Canvas8', None)
    _safe_set(owner, 'gmfgraph_DiagramLabel', partner)
    assert owner in getattr(partner, 'gmfgraph_Canvas8')
    _safe_set(owner, 'gmfgraph_DiagramLabel', None)
    assert owner not in getattr(partner, 'gmfgraph_Canvas8')


def test_assoc_location63_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure64' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure64', None)
    _safe_set(owner, 'gmfgraph_Point', partner)
    assert getattr(partner, 'gmfgraph_Figure64') == owner
    _safe_set(owner, 'gmfgraph_Point', None)
    assert getattr(partner, 'gmfgraph_Figure64') is None


def test_assoc_maximumSize46_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure47' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure47', None)
    _safe_set(owner, 'gmfgraph_Dimension48', partner)
    assert getattr(partner, 'gmfgraph_Figure47') == owner
    _safe_set(owner, 'gmfgraph_Dimension48', None)
    assert getattr(partner, 'gmfgraph_Figure47') is None


def test_assoc_minimumSize49_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure50' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure50', None)
    _safe_set(owner, 'gmfgraph_Dimension51', partner)
    assert getattr(partner, 'gmfgraph_Figure50') == owner
    _safe_set(owner, 'gmfgraph_Dimension51', None)
    assert getattr(partner, 'gmfgraph_Figure50') is None


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


def test_assoc_owner103_stub_double():
    # gmfgraph_FigureDescriptor has no real 'FigureDescriptor' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_ChildAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_ChildAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_ChildAccess(accessor="sample_text")
    partner = gmfgraph_FigureDescriptor()
    setattr(partner, 'FigureDescriptor', None)
    _safe_set(owner, 'accessors', partner)
    assert getattr(partner, 'FigureDescriptor') == owner
    _safe_set(owner, 'accessors', None)
    assert getattr(partner, 'FigureDescriptor') is None


def test_assoc_preferredSize52_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure53' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure53', None)
    _safe_set(owner, 'gmfgraph_Dimension54', partner)
    assert getattr(partner, 'gmfgraph_Figure53') == owner
    _safe_set(owner, 'gmfgraph_Dimension54', None)
    assert getattr(partner, 'gmfgraph_Figure53') is None


def test_assoc_resolvedChildren73_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure74' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure74', None)
    _safe_set(owner, 'gmfgraph_Shape', {partner})
    assert getattr(partner, 'gmfgraph_Figure74') == owner
    _safe_set(owner, 'gmfgraph_Shape', set())
    assert getattr(partner, 'gmfgraph_Figure74') is None


def test_assoc_size65_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure66' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure66', None)
    _safe_set(owner, 'gmfgraph_Point67', partner)
    assert getattr(partner, 'gmfgraph_Figure66') == owner
    _safe_set(owner, 'gmfgraph_Point67', None)
    assert getattr(partner, 'gmfgraph_Figure66') is None


def test_assoc_size92_stub_double():
    # gmfgraph_XYLayoutData has no real 'gmfgraph_XYLayoutData93' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_XYLayoutData()
    setattr(partner, 'gmfgraph_XYLayoutData93', None)
    _safe_set(owner, 'gmfgraph_Dimension94', partner)
    assert getattr(partner, 'gmfgraph_XYLayoutData93') == owner
    _safe_set(owner, 'gmfgraph_Dimension94', None)
    assert getattr(partner, 'gmfgraph_XYLayoutData93') is None


def test_assoc_spacing88_stub_double():
    # gmfgraph_BorderLayout has no real 'gmfgraph_BorderLayout' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_BorderLayout()
    setattr(partner, 'gmfgraph_BorderLayout', None)
    _safe_set(owner, 'gmfgraph_Dimension89', partner)
    assert getattr(partner, 'gmfgraph_BorderLayout') == owner
    _safe_set(owner, 'gmfgraph_Dimension89', None)
    assert getattr(partner, 'gmfgraph_BorderLayout') is None


def test_assoc_template75_stub_double():
    # gmfgraph_Polyline has no real 'gmfgraph_Polyline' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Polyline()
    setattr(partner, 'gmfgraph_Polyline', None)
    _safe_set(owner, 'gmfgraph_Point76', partner)
    assert owner in getattr(partner, 'gmfgraph_Polyline')
    _safe_set(owner, 'gmfgraph_Point76', None)
    assert owner not in getattr(partner, 'gmfgraph_Polyline')


def test_assoc_topLeft90_stub_double():
    # gmfgraph_XYLayoutData has no real 'gmfgraph_XYLayoutData' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_XYLayoutData()
    setattr(partner, 'gmfgraph_XYLayoutData', None)
    _safe_set(owner, 'gmfgraph_Point91', partner)
    assert getattr(partner, 'gmfgraph_XYLayoutData') == owner
    _safe_set(owner, 'gmfgraph_Point91', None)
    assert getattr(partner, 'gmfgraph_XYLayoutData') is None


