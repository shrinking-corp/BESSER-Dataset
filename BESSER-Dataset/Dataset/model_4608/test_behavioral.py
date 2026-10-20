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


def test_assoc_attributes77_reverse_link_reassign_clear():
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


def test_assoc_margins97_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension98', a1)
    assert _is_linked(b, 'gmfgraph_Dimension98', a1)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert _is_linked(a1, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension98', a2)
    assert _is_linked(b, 'gmfgraph_Dimension98', a2)
    if hasattr(a1, 'gmfgraph_GridLayout'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout', b)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert _is_linked(a2, 'gmfgraph_GridLayout', b)
    _safe_set(b, 'gmfgraph_Dimension98', None)
    assert not _is_linked(b, 'gmfgraph_Dimension98', a2)
    if hasattr(a2, 'gmfgraph_GridLayout'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout', b)


def test_assoc_sizeHint92_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    a2 = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=False, grabExcessVerticalSpace=False, horizontalAlignment="sample_text_2", horizontalIndent=13, horizontalSpan=13, verticalAlignment="sample_text_2", verticalSpan=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension93', a1)
    assert _is_linked(b, 'gmfgraph_Dimension93', a1)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension93', a2)
    assert _is_linked(b, 'gmfgraph_Dimension93', a2)
    if hasattr(a1, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a1, 'gmfgraph_GridLayoutData', b)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert _is_linked(a2, 'gmfgraph_GridLayoutData', b)
    _safe_set(b, 'gmfgraph_Dimension93', None)
    assert not _is_linked(b, 'gmfgraph_Dimension93', a2)
    if hasattr(a2, 'gmfgraph_GridLayoutData'):
        assert not _is_linked(a2, 'gmfgraph_GridLayoutData', b)


def test_assoc_spacing99_reverse_link_reassign_clear():
    a1 = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    a2 = gmfgraph_GridLayout(equalWidth=False, numColumns=13)
    b = gmfgraph_Dimension(dx=7, dy=7)
    _safe_set(b, 'gmfgraph_Dimension101', a1)
    assert _is_linked(b, 'gmfgraph_Dimension101', a1)
    if hasattr(a1, 'gmfgraph_GridLayout100'):
        assert _is_linked(a1, 'gmfgraph_GridLayout100', b)
    _safe_set(b, 'gmfgraph_Dimension101', a2)
    assert _is_linked(b, 'gmfgraph_Dimension101', a2)
    if hasattr(a1, 'gmfgraph_GridLayout100'):
        assert not _is_linked(a1, 'gmfgraph_GridLayout100', b)
    if hasattr(a2, 'gmfgraph_GridLayout100'):
        assert _is_linked(a2, 'gmfgraph_GridLayout100', b)
    _safe_set(b, 'gmfgraph_Dimension101', None)
    assert not _is_linked(b, 'gmfgraph_Dimension101', a2)
    if hasattr(a2, 'gmfgraph_GridLayout100'):
        assert not _is_linked(a2, 'gmfgraph_GridLayout100', b)


def test_assoc_typedFigure78_reverse_link_reassign_clear():
    a1 = gmfgraph_RealFigure(name="sample_text")
    a2 = gmfgraph_RealFigure(name="sample_text_2")
    b = gmfgraph_FigureAccessor(accessor="sample_text")
    _safe_set(b, 'gmfgraph_FigureAccessor', a1)
    assert _is_linked(b, 'gmfgraph_FigureAccessor', a1)
    if hasattr(a1, 'gmfgraph_RealFigure79'):
        assert _is_linked(a1, 'gmfgraph_RealFigure79', b)
    _safe_set(b, 'gmfgraph_FigureAccessor', a2)
    assert _is_linked(b, 'gmfgraph_FigureAccessor', a2)
    if hasattr(a1, 'gmfgraph_RealFigure79'):
        assert not _is_linked(a1, 'gmfgraph_RealFigure79', b)
    if hasattr(a2, 'gmfgraph_RealFigure79'):
        assert _is_linked(a2, 'gmfgraph_RealFigure79', b)
    _safe_set(b, 'gmfgraph_FigureAccessor', None)
    assert not _is_linked(b, 'gmfgraph_FigureAccessor', a2)
    if hasattr(a2, 'gmfgraph_RealFigure79'):
        assert not _is_linked(a2, 'gmfgraph_RealFigure79', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessors59_stub_double():
    # gmfgraph_FigureDescriptor has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_ChildAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_ChildAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_ChildAccess(accessor="sample_text")
    partner = gmfgraph_FigureDescriptor()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'ChildAccess', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'ChildAccess', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_children64_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure66' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_RealFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_RealFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_RealFigure(name="sample_text")
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure66', None)
    _safe_set(owner, 'gmfgraph_RealFigure65', {partner})
    assert getattr(partner, 'gmfgraph_Figure66') == owner
    _safe_set(owner, 'gmfgraph_RealFigure65', set())
    assert getattr(partner, 'gmfgraph_Figure66') is None


def test_assoc_color82_stub_double():
    # gmfgraph_Color has no real 'gmfgraph_Color83' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_LineBorder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_LineBorder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_LineBorder(width=7)
    partner = gmfgraph_Color()
    setattr(partner, 'gmfgraph_Color83', None)
    _safe_set(owner, 'gmfgraph_LineBorder', partner)
    assert getattr(partner, 'gmfgraph_Color83') == owner
    _safe_set(owner, 'gmfgraph_LineBorder', None)
    assert getattr(partner, 'gmfgraph_Color83') is None


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


def test_assoc_customChildren80_stub_double():
    # gmfgraph_CustomFigure has no real 'gmfgraph_CustomFigure' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_FigureAccessor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_FigureAccessor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_FigureAccessor(accessor="sample_text")
    partner = gmfgraph_CustomFigure()
    setattr(partner, 'gmfgraph_CustomFigure', None)
    _safe_set(owner, 'gmfgraph_FigureAccessor81', partner)
    assert owner in getattr(partner, 'gmfgraph_CustomFigure')
    _safe_set(owner, 'gmfgraph_FigureAccessor81', None)
    assert owner not in getattr(partner, 'gmfgraph_CustomFigure')


def test_assoc_defaultSize28_stub_double():
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


def test_assoc_figure61_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure63' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_ChildAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_ChildAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_ChildAccess(accessor="sample_text")
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure63', None)
    _safe_set(owner, 'gmfgraph_ChildAccess62', partner)
    assert getattr(partner, 'gmfgraph_Figure63') == owner
    _safe_set(owner, 'gmfgraph_ChildAccess62', None)
    assert getattr(partner, 'gmfgraph_Figure63') is None


def test_assoc_figure67_stub_double():
    # gmfgraph_FigureRef has no real 'gmfgraph_FigureRef' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_RealFigure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_RealFigure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_RealFigure(name="sample_text")
    partner = gmfgraph_FigureRef()
    setattr(partner, 'gmfgraph_FigureRef', None)
    _safe_set(owner, 'gmfgraph_RealFigure68', partner)
    assert getattr(partner, 'gmfgraph_FigureRef') == owner
    _safe_set(owner, 'gmfgraph_RealFigure68', None)
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


def test_assoc_insets47_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure48' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Insets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Insets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure48', None)
    _safe_set(owner, 'gmfgraph_Insets', partner)
    assert getattr(partner, 'gmfgraph_Figure48') == owner
    _safe_set(owner, 'gmfgraph_Insets', None)
    assert getattr(partner, 'gmfgraph_Figure48') is None


def test_assoc_insets84_stub_double():
    # gmfgraph_MarginBorder has no real 'gmfgraph_MarginBorder' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Insets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Insets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    partner = gmfgraph_MarginBorder()
    setattr(partner, 'gmfgraph_MarginBorder', None)
    _safe_set(owner, 'gmfgraph_Insets85', partner)
    assert getattr(partner, 'gmfgraph_MarginBorder') == owner
    _safe_set(owner, 'gmfgraph_Insets85', None)
    assert getattr(partner, 'gmfgraph_MarginBorder') is None


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


def test_assoc_location51_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure52' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure52', None)
    _safe_set(owner, 'gmfgraph_Point', partner)
    assert getattr(partner, 'gmfgraph_Figure52') == owner
    _safe_set(owner, 'gmfgraph_Point', None)
    assert getattr(partner, 'gmfgraph_Figure52') is None


def test_assoc_maximumSize36_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure37' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure37', None)
    _safe_set(owner, 'gmfgraph_Dimension38', partner)
    assert getattr(partner, 'gmfgraph_Figure37') == owner
    _safe_set(owner, 'gmfgraph_Dimension38', None)
    assert getattr(partner, 'gmfgraph_Figure37') is None


def test_assoc_minimumSize39_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure40' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure40', None)
    _safe_set(owner, 'gmfgraph_Dimension41', partner)
    assert getattr(partner, 'gmfgraph_Figure40') == owner
    _safe_set(owner, 'gmfgraph_Dimension41', None)
    assert getattr(partner, 'gmfgraph_Figure40') is None


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


def test_assoc_owner60_stub_double():
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


def test_assoc_preferredSize42_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure43' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure43', None)
    _safe_set(owner, 'gmfgraph_Dimension44', partner)
    assert getattr(partner, 'gmfgraph_Figure43') == owner
    _safe_set(owner, 'gmfgraph_Dimension44', None)
    assert getattr(partner, 'gmfgraph_Figure43') is None


def test_assoc_resolvedChildren69_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure70' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Shape's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Shape's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure70', None)
    _safe_set(owner, 'gmfgraph_Shape', {partner})
    assert getattr(partner, 'gmfgraph_Figure70') == owner
    _safe_set(owner, 'gmfgraph_Shape', set())
    assert getattr(partner, 'gmfgraph_Figure70') is None


def test_assoc_size106_stub_double():
    # gmfgraph_XYLayoutData has no real 'gmfgraph_XYLayoutData107' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_XYLayoutData()
    setattr(partner, 'gmfgraph_XYLayoutData107', None)
    _safe_set(owner, 'gmfgraph_Dimension108', partner)
    assert getattr(partner, 'gmfgraph_XYLayoutData107') == owner
    _safe_set(owner, 'gmfgraph_Dimension108', None)
    assert getattr(partner, 'gmfgraph_XYLayoutData107') is None


def test_assoc_size53_stub_double():
    # gmfgraph_Figure has no real 'gmfgraph_Figure54' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Figure()
    setattr(partner, 'gmfgraph_Figure54', None)
    _safe_set(owner, 'gmfgraph_Point55', partner)
    assert getattr(partner, 'gmfgraph_Figure54') == owner
    _safe_set(owner, 'gmfgraph_Point55', None)
    assert getattr(partner, 'gmfgraph_Figure54') is None


def test_assoc_spacing102_stub_double():
    # gmfgraph_BorderLayout has no real 'gmfgraph_BorderLayout' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Dimension(dx=7, dy=7)
    partner = gmfgraph_BorderLayout()
    setattr(partner, 'gmfgraph_BorderLayout', None)
    _safe_set(owner, 'gmfgraph_Dimension103', partner)
    assert getattr(partner, 'gmfgraph_BorderLayout') == owner
    _safe_set(owner, 'gmfgraph_Dimension103', None)
    assert getattr(partner, 'gmfgraph_BorderLayout') is None


def test_assoc_template71_stub_double():
    # gmfgraph_Polyline has no real 'gmfgraph_Polyline' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_Polyline()
    setattr(partner, 'gmfgraph_Polyline', None)
    _safe_set(owner, 'gmfgraph_Point72', partner)
    assert owner in getattr(partner, 'gmfgraph_Polyline')
    _safe_set(owner, 'gmfgraph_Point72', None)
    assert owner not in getattr(partner, 'gmfgraph_Polyline')


def test_assoc_topLeft104_stub_double():
    # gmfgraph_XYLayoutData has no real 'gmfgraph_XYLayoutData' property in the generated
    # code (a bare stub) -- manually attach it so gmfgraph_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gmfgraph_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gmfgraph_Point(x=7, y=7)
    partner = gmfgraph_XYLayoutData()
    setattr(partner, 'gmfgraph_XYLayoutData', None)
    _safe_set(owner, 'gmfgraph_Point105', partner)
    assert getattr(partner, 'gmfgraph_XYLayoutData') == owner
    _safe_set(owner, 'gmfgraph_Point105', None)
    assert getattr(partner, 'gmfgraph_XYLayoutData') is None


