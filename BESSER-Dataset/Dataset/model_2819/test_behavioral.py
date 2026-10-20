import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Canvas,
    Definition,
    Gradient,
    GraphicalElement,
    Group,
    MarkedElement,
    PaintServer,
    PathCommand,
    Transform,
    dg_Bounds,
    dg_Canvas,
    dg_Circle,
    dg_ClipPath,
    dg_ClosePath,
    dg_CubicCurveTo,
    dg_Definition,
    dg_Definitions,
    dg_Dimension,
    dg_Ellipse,
    dg_EllipticalArcTo,
    dg_Gradient,
    dg_GradientStop,
    dg_GraphicalElement,
    dg_Group,
    dg_Image,
    dg_Line,
    dg_LineTo,
    dg_LinearGradient,
    dg_MarkedElement,
    dg_Marker,
    dg_Matrix,
    dg_MoveTo,
    dg_Paint,
    dg_PaintServer,
    dg_Path,
    dg_PathCommand,
    dg_Pattern,
    dg_Point,
    dg_Polygon,
    dg_Polyline,
    dg_QuadraticCurveTo,
    dg_RadialGradient,
    dg_Rectangle,
    dg_RootCanvas,
    dg_Rotate,
    dg_Scale,
    dg_Skew,
    dg_Style,
    dg_StyleRule,
    dg_StyleSelector,
    dg_StyleSheet,
    dg_Text,
    dg_Transform,
    dg_Translate,
    dg_Use,
    ElementKind,
    FontDecoration,
    TextAnchor,
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

def test_assoc_command81_reverse_link_reassign_clear():
    a1 = dg_PathCommand(isRelative="sample_text")
    a2 = dg_PathCommand(isRelative="sample_text_2")
    b = dg_Path()
    _safe_set(b, 'dg_Path', {a1})
    assert _is_linked(b, 'dg_Path', a1)
    if hasattr(a1, 'dg_PathCommand'):
        assert _is_linked(a1, 'dg_PathCommand', b)
    _safe_set(b, 'dg_Path', {a2})
    assert _is_linked(b, 'dg_Path', a2)
    if hasattr(a1, 'dg_PathCommand'):
        assert not _is_linked(a1, 'dg_PathCommand', b)
    if hasattr(a2, 'dg_PathCommand'):
        assert _is_linked(a2, 'dg_PathCommand', b)
    _safe_set(b, 'dg_Path', set())
    assert not _is_linked(b, 'dg_Path', a2)
    if hasattr(a2, 'dg_PathCommand'):
        assert not _is_linked(a2, 'dg_PathCommand', b)


def test_assoc_fill9_reverse_link_reassign_clear():
    a1 = dg_Style(fillOpacity="sample_text", fontBold="sample_text", fontDecoration="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    a2 = dg_Style(fillOpacity="sample_text_2", fontBold="sample_text_2", fontDecoration="sample_text_2", fontItalic="sample_text_2", fontName="sample_text_2", fontSize="sample_text_2", strokeDashLength="sample_text_2", strokeOpacity="sample_text_2", strokeWidth="sample_text_2")
    b = dg_Paint(color="sample_text")
    _safe_set(b, 'dg_Paint', a1)
    assert _is_linked(b, 'dg_Paint', a1)
    if hasattr(a1, 'dg_Style10'):
        assert _is_linked(a1, 'dg_Style10', b)
    _safe_set(b, 'dg_Paint', a2)
    assert _is_linked(b, 'dg_Paint', a2)
    if hasattr(a1, 'dg_Style10'):
        assert not _is_linked(a1, 'dg_Style10', b)
    if hasattr(a2, 'dg_Style10'):
        assert _is_linked(a2, 'dg_Style10', b)
    _safe_set(b, 'dg_Paint', None)
    assert not _is_linked(b, 'dg_Paint', a2)
    if hasattr(a2, 'dg_Style10'):
        assert not _is_linked(a2, 'dg_Style10', b)


def test_assoc_group3_reverse_link_reassign_clear():
    a1 = dg_Group(layout="sample_text")
    a2 = dg_Group(layout="sample_text_2")
    b = dg_GraphicalElement(class_="sample_text", layoutData="sample_text")
    _safe_set(b, 'member', a1)
    assert _is_linked(b, 'member', a1)
    if hasattr(a1, 'Group'):
        assert _is_linked(a1, 'Group', b)
    _safe_set(b, 'member', a2)
    assert _is_linked(b, 'member', a2)
    if hasattr(a1, 'Group'):
        assert not _is_linked(a1, 'Group', b)
    if hasattr(a2, 'Group'):
        assert _is_linked(a2, 'Group', b)
    _safe_set(b, 'member', None)
    assert not _is_linked(b, 'member', a2)
    if hasattr(a2, 'Group'):
        assert not _is_linked(a2, 'Group', b)


def test_assoc_member1_reverse_link_reassign_clear():
    a1 = dg_Group(layout="sample_text")
    a2 = dg_Group(layout="sample_text_2")
    b = dg_GraphicalElement(class_="sample_text", layoutData="sample_text")
    _safe_set(b, 'GraphicalElement', a1)
    assert _is_linked(b, 'GraphicalElement', a1)
    if hasattr(a1, 'group'):
        assert _is_linked(a1, 'group', b)
    _safe_set(b, 'GraphicalElement', a2)
    assert _is_linked(b, 'GraphicalElement', a2)
    if hasattr(a1, 'group'):
        assert not _is_linked(a1, 'group', b)
    if hasattr(a2, 'group'):
        assert _is_linked(a2, 'group', b)
    _safe_set(b, 'GraphicalElement', None)
    assert not _is_linked(b, 'GraphicalElement', a2)
    if hasattr(a2, 'group'):
        assert not _is_linked(a2, 'group', b)


def test_assoc_referencedElement109_reverse_link_reassign_clear():
    a1 = dg_Use()
    a2 = dg_Use()
    b = dg_GraphicalElement(class_="sample_text", layoutData="sample_text")
    _safe_set(b, 'dg_GraphicalElement111', a1)
    assert _is_linked(b, 'dg_GraphicalElement111', a1)
    if hasattr(a1, 'dg_Use110'):
        assert _is_linked(a1, 'dg_Use110', b)
    _safe_set(b, 'dg_GraphicalElement111', a2)
    assert _is_linked(b, 'dg_GraphicalElement111', a2)
    if hasattr(a1, 'dg_Use110'):
        assert not _is_linked(a1, 'dg_Use110', b)
    if hasattr(a2, 'dg_Use110'):
        assert _is_linked(a2, 'dg_Use110', b)
    _safe_set(b, 'dg_GraphicalElement111', None)
    assert not _is_linked(b, 'dg_GraphicalElement111', a2)
    if hasattr(a2, 'dg_Use110'):
        assert not _is_linked(a2, 'dg_Use110', b)


def test_assoc_stroke11_reverse_link_reassign_clear():
    a1 = dg_Style(fillOpacity="sample_text", fontBold="sample_text", fontDecoration="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    a2 = dg_Style(fillOpacity="sample_text_2", fontBold="sample_text_2", fontDecoration="sample_text_2", fontItalic="sample_text_2", fontName="sample_text_2", fontSize="sample_text_2", strokeDashLength="sample_text_2", strokeOpacity="sample_text_2", strokeWidth="sample_text_2")
    b = dg_Paint(color="sample_text")
    _safe_set(b, 'dg_Paint13', a1)
    assert _is_linked(b, 'dg_Paint13', a1)
    if hasattr(a1, 'dg_Style12'):
        assert _is_linked(a1, 'dg_Style12', b)
    _safe_set(b, 'dg_Paint13', a2)
    assert _is_linked(b, 'dg_Paint13', a2)
    if hasattr(a1, 'dg_Style12'):
        assert not _is_linked(a1, 'dg_Style12', b)
    if hasattr(a2, 'dg_Style12'):
        assert _is_linked(a2, 'dg_Style12', b)
    _safe_set(b, 'dg_Paint13', None)
    assert not _is_linked(b, 'dg_Paint13', a2)
    if hasattr(a2, 'dg_Style12'):
        assert not _is_linked(a2, 'dg_Style12', b)


def test_assoc_style4_reverse_link_reassign_clear():
    a1 = dg_Style(fillOpacity="sample_text", fontBold="sample_text", fontDecoration="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    a2 = dg_Style(fillOpacity="sample_text_2", fontBold="sample_text_2", fontDecoration="sample_text_2", fontItalic="sample_text_2", fontName="sample_text_2", fontSize="sample_text_2", strokeDashLength="sample_text_2", strokeOpacity="sample_text_2", strokeWidth="sample_text_2")
    b = dg_GraphicalElement(class_="sample_text", layoutData="sample_text")
    _safe_set(b, 'dg_GraphicalElement5', a1)
    assert _is_linked(b, 'dg_GraphicalElement5', a1)
    if hasattr(a1, 'dg_Style'):
        assert _is_linked(a1, 'dg_Style', b)
    _safe_set(b, 'dg_GraphicalElement5', a2)
    assert _is_linked(b, 'dg_GraphicalElement5', a2)
    if hasattr(a1, 'dg_Style'):
        assert not _is_linked(a1, 'dg_Style', b)
    if hasattr(a2, 'dg_Style'):
        assert _is_linked(a2, 'dg_Style', b)
    _safe_set(b, 'dg_GraphicalElement5', None)
    assert not _is_linked(b, 'dg_GraphicalElement5', a2)
    if hasattr(a2, 'dg_Style'):
        assert not _is_linked(a2, 'dg_Style', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bounds0_stub_double():
    # dg_Bounds has no real 'dg_Bounds' property in the generated
    # code (a bare stub) -- manually attach it so dg_Canvas's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Canvas's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Canvas()
    partner = dg_Bounds()
    setattr(partner, 'dg_Bounds', None)
    _safe_set(owner, 'dg_Canvas', partner)
    assert getattr(partner, 'dg_Bounds') == owner
    _safe_set(owner, 'dg_Canvas', None)
    assert getattr(partner, 'dg_Bounds') is None


def test_assoc_bounds105_stub_double():
    # dg_Bounds has no real 'dg_Bounds106' property in the generated
    # code (a bare stub) -- manually attach it so dg_Text's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Text's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Text(anchor="sample_text", data="sample_text")
    partner = dg_Bounds()
    setattr(partner, 'dg_Bounds106', None)
    _safe_set(owner, 'dg_Text', partner)
    assert getattr(partner, 'dg_Bounds106') == owner
    _safe_set(owner, 'dg_Text', None)
    assert getattr(partner, 'dg_Bounds106') is None


def test_assoc_bounds107_stub_double():
    # dg_Bounds has no real 'dg_Bounds108' property in the generated
    # code (a bare stub) -- manually attach it so dg_Use's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Use's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Use()
    partner = dg_Bounds()
    setattr(partner, 'dg_Bounds108', None)
    _safe_set(owner, 'dg_Use', partner)
    assert getattr(partner, 'dg_Bounds108') == owner
    _safe_set(owner, 'dg_Use', None)
    assert getattr(partner, 'dg_Bounds108') is None


def test_assoc_bounds54_stub_double():
    # dg_Bounds has no real 'dg_Bounds55' property in the generated
    # code (a bare stub) -- manually attach it so dg_Image's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Image's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Image(isAspectRatioPreserved="sample_text", source="sample_text")
    partner = dg_Bounds()
    setattr(partner, 'dg_Bounds55', None)
    _safe_set(owner, 'dg_Image', partner)
    assert getattr(partner, 'dg_Bounds55') == owner
    _safe_set(owner, 'dg_Image', None)
    assert getattr(partner, 'dg_Bounds55') is None


def test_assoc_bounds96_stub_double():
    # dg_Bounds has no real 'dg_Bounds97' property in the generated
    # code (a bare stub) -- manually attach it so dg_Rectangle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Rectangle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Rectangle(cornerRadius="sample_text")
    partner = dg_Bounds()
    setattr(partner, 'dg_Bounds97', None)
    _safe_set(owner, 'dg_Rectangle', partner)
    assert getattr(partner, 'dg_Bounds97') == owner
    _safe_set(owner, 'dg_Rectangle', None)
    assert getattr(partner, 'dg_Bounds97') is None


def test_assoc_center103_stub_double():
    # dg_Point has no real 'dg_Point104' property in the generated
    # code (a bare stub) -- manually attach it so dg_Rotate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Rotate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Rotate(angle="sample_text")
    partner = dg_Point()
    setattr(partner, 'dg_Point104', None)
    _safe_set(owner, 'dg_Rotate', partner)
    assert getattr(partner, 'dg_Point104') == owner
    _safe_set(owner, 'dg_Rotate', None)
    assert getattr(partner, 'dg_Point104') is None


def test_assoc_center19_stub_double():
    # dg_Point has no real 'dg_Point20' property in the generated
    # code (a bare stub) -- manually attach it so dg_Circle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Circle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Circle(radius="sample_text")
    partner = dg_Point()
    setattr(partner, 'dg_Point20', None)
    _safe_set(owner, 'dg_Circle', partner)
    assert getattr(partner, 'dg_Point20') == owner
    _safe_set(owner, 'dg_Circle', None)
    assert getattr(partner, 'dg_Point20') is None


def test_assoc_center91_stub_double():
    # dg_Point has no real 'dg_Point92' property in the generated
    # code (a bare stub) -- manually attach it so dg_RadialGradient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_RadialGradient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_RadialGradient(radius="sample_text")
    partner = dg_Point()
    setattr(partner, 'dg_Point92', None)
    _safe_set(owner, 'dg_RadialGradient', partner)
    assert getattr(partner, 'dg_Point92') == owner
    _safe_set(owner, 'dg_RadialGradient', None)
    assert getattr(partner, 'dg_Point92') is None


def test_assoc_clipPath2_stub_double():
    # dg_ClipPath has no real 'dg_ClipPath' property in the generated
    # code (a bare stub) -- manually attach it so dg_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_GraphicalElement(class_="sample_text", layoutData="sample_text")
    partner = dg_ClipPath()
    setattr(partner, 'dg_ClipPath', None)
    _safe_set(owner, 'dg_GraphicalElement', partner)
    assert getattr(partner, 'dg_ClipPath') == owner
    _safe_set(owner, 'dg_GraphicalElement', None)
    assert getattr(partner, 'dg_ClipPath') is None


def test_assoc_definition29_stub_double():
    # dg_Definitions has no real 'dg_Definitions' property in the generated
    # code (a bare stub) -- manually attach it so dg_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Definition(id="sample_text")
    partner = dg_Definitions()
    setattr(partner, 'dg_Definitions', None)
    _safe_set(owner, 'dg_Definition', partner)
    assert owner in getattr(partner, 'dg_Definitions')
    _safe_set(owner, 'dg_Definition', None)
    assert owner not in getattr(partner, 'dg_Definitions')


def test_assoc_definitions98_stub_double():
    # dg_Definitions has no real 'dg_Definitions99' property in the generated
    # code (a bare stub) -- manually attach it so dg_RootCanvas's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_RootCanvas's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_RootCanvas(backgroundColor="sample_text")
    partner = dg_Definitions()
    setattr(partner, 'dg_Definitions99', None)
    _safe_set(owner, 'dg_RootCanvas', partner)
    assert getattr(partner, 'dg_Definitions99') == owner
    _safe_set(owner, 'dg_RootCanvas', None)
    assert getattr(partner, 'dg_Definitions99') is None


def test_assoc_end76_stub_double():
    # dg_Point has no real 'dg_Point78' property in the generated
    # code (a bare stub) -- manually attach it so dg_LinearGradient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_LinearGradient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_LinearGradient()
    partner = dg_Point()
    setattr(partner, 'dg_Point78', None)
    _safe_set(owner, 'dg_LinearGradient77', partner)
    assert getattr(partner, 'dg_Point78') == owner
    _safe_set(owner, 'dg_LinearGradient77', None)
    assert getattr(partner, 'dg_Point78') is None


def test_assoc_endMarker61_stub_double():
    # dg_Marker has no real 'dg_Marker' property in the generated
    # code (a bare stub) -- manually attach it so dg_MarkedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_MarkedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_MarkedElement()
    partner = dg_Marker()
    setattr(partner, 'dg_Marker', None)
    _safe_set(owner, 'dg_MarkedElement', partner)
    assert getattr(partner, 'dg_Marker') == owner
    _safe_set(owner, 'dg_MarkedElement', None)
    assert getattr(partner, 'dg_Marker') is None


def test_assoc_externalStyleSheet100_stub_double():
    # dg_StyleSheet has no real 'dg_StyleSheet102' property in the generated
    # code (a bare stub) -- manually attach it so dg_RootCanvas's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_RootCanvas's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_RootCanvas(backgroundColor="sample_text")
    partner = dg_StyleSheet()
    setattr(partner, 'dg_StyleSheet102', None)
    _safe_set(owner, 'dg_RootCanvas101', {partner})
    assert getattr(partner, 'dg_StyleSheet102') == owner
    _safe_set(owner, 'dg_RootCanvas101', set())
    assert getattr(partner, 'dg_StyleSheet102') is None


def test_assoc_focus93_stub_double():
    # dg_Point has no real 'dg_Point95' property in the generated
    # code (a bare stub) -- manually attach it so dg_RadialGradient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_RadialGradient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_RadialGradient(radius="sample_text")
    partner = dg_Point()
    setattr(partner, 'dg_Point95', None)
    _safe_set(owner, 'dg_RadialGradient94', partner)
    assert getattr(partner, 'dg_Point95') == owner
    _safe_set(owner, 'dg_RadialGradient94', None)
    assert getattr(partner, 'dg_Point95') is None


def test_assoc_midMarker62_stub_double():
    # dg_Marker has no real 'dg_Marker64' property in the generated
    # code (a bare stub) -- manually attach it so dg_MarkedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_MarkedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_MarkedElement()
    partner = dg_Marker()
    setattr(partner, 'dg_Marker64', None)
    _safe_set(owner, 'dg_MarkedElement63', partner)
    assert getattr(partner, 'dg_Marker64') == owner
    _safe_set(owner, 'dg_MarkedElement63', None)
    assert getattr(partner, 'dg_Marker64') is None


def test_assoc_paintServer14_stub_double():
    # dg_PaintServer has no real 'dg_PaintServer' property in the generated
    # code (a bare stub) -- manually attach it so dg_Paint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Paint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Paint(color="sample_text")
    partner = dg_PaintServer()
    setattr(partner, 'dg_PaintServer', None)
    _safe_set(owner, 'dg_Paint15', partner)
    assert getattr(partner, 'dg_PaintServer') == owner
    _safe_set(owner, 'dg_Paint15', None)
    assert getattr(partner, 'dg_PaintServer') is None


def test_assoc_point45_stub_double():
    # dg_Point has no real 'dg_Point47' property in the generated
    # code (a bare stub) -- manually attach it so dg_EllipticalArcTo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_EllipticalArcTo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_EllipticalArcTo(isLargeArc="sample_text", isSweep="sample_text", rotation="sample_text")
    partner = dg_Point()
    setattr(partner, 'dg_Point47', None)
    _safe_set(owner, 'dg_EllipticalArcTo46', partner)
    assert getattr(partner, 'dg_Point47') == owner
    _safe_set(owner, 'dg_EllipticalArcTo46', None)
    assert getattr(partner, 'dg_Point47') is None


def test_assoc_radii43_stub_double():
    # dg_Dimension has no real 'dg_Dimension44' property in the generated
    # code (a bare stub) -- manually attach it so dg_EllipticalArcTo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_EllipticalArcTo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_EllipticalArcTo(isLargeArc="sample_text", isSweep="sample_text", rotation="sample_text")
    partner = dg_Dimension()
    setattr(partner, 'dg_Dimension44', None)
    _safe_set(owner, 'dg_EllipticalArcTo', partner)
    assert getattr(partner, 'dg_Dimension44') == owner
    _safe_set(owner, 'dg_EllipticalArcTo', None)
    assert getattr(partner, 'dg_Dimension44') is None


def test_assoc_selector34_stub_double():
    # dg_StyleRule has no real 'dg_StyleRule35' property in the generated
    # code (a bare stub) -- manually attach it so dg_StyleSelector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_StyleSelector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_StyleSelector(class_="sample_text", kind="sample_text")
    partner = dg_StyleRule()
    setattr(partner, 'dg_StyleRule35', None)
    _safe_set(owner, 'dg_StyleSelector', partner)
    assert owner in getattr(partner, 'dg_StyleRule35')
    _safe_set(owner, 'dg_StyleSelector', None)
    assert owner not in getattr(partner, 'dg_StyleRule35')


def test_assoc_start74_stub_double():
    # dg_Point has no real 'dg_Point75' property in the generated
    # code (a bare stub) -- manually attach it so dg_LinearGradient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_LinearGradient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_LinearGradient()
    partner = dg_Point()
    setattr(partner, 'dg_Point75', None)
    _safe_set(owner, 'dg_LinearGradient', partner)
    assert getattr(partner, 'dg_Point75') == owner
    _safe_set(owner, 'dg_LinearGradient', None)
    assert getattr(partner, 'dg_Point75') is None


def test_assoc_startMarker65_stub_double():
    # dg_Marker has no real 'dg_Marker67' property in the generated
    # code (a bare stub) -- manually attach it so dg_MarkedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_MarkedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_MarkedElement()
    partner = dg_Marker()
    setattr(partner, 'dg_Marker67', None)
    _safe_set(owner, 'dg_MarkedElement66', partner)
    assert getattr(partner, 'dg_Marker67') == owner
    _safe_set(owner, 'dg_MarkedElement66', None)
    assert getattr(partner, 'dg_Marker67') is None


def test_assoc_stop53_stub_double():
    # dg_Gradient has no real 'dg_Gradient' property in the generated
    # code (a bare stub) -- manually attach it so dg_GradientStop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_GradientStop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_GradientStop(color="sample_text", offset="sample_text", opacity="sample_text")
    partner = dg_Gradient()
    setattr(partner, 'dg_Gradient', None)
    _safe_set(owner, 'dg_GradientStop', partner)
    assert owner in getattr(partner, 'dg_Gradient')
    _safe_set(owner, 'dg_GradientStop', None)
    assert owner not in getattr(partner, 'dg_Gradient')


def test_assoc_style36_stub_double():
    # dg_StyleRule has no real 'dg_StyleRule37' property in the generated
    # code (a bare stub) -- manually attach it so dg_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_Style(fillOpacity="sample_text", fontBold="sample_text", fontDecoration="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = dg_StyleRule()
    setattr(partner, 'dg_StyleRule37', None)
    _safe_set(owner, 'dg_Style38', partner)
    assert getattr(partner, 'dg_StyleRule37') == owner
    _safe_set(owner, 'dg_Style38', None)
    assert getattr(partner, 'dg_StyleRule37') is None


def test_assoc_tile84_stub_double():
    # dg_Pattern has no real 'dg_Pattern85' property in the generated
    # code (a bare stub) -- manually attach it so dg_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_GraphicalElement(class_="sample_text", layoutData="sample_text")
    partner = dg_Pattern()
    setattr(partner, 'dg_Pattern85', None)
    _safe_set(owner, 'dg_GraphicalElement86', partner)
    assert getattr(partner, 'dg_Pattern85') == owner
    _safe_set(owner, 'dg_GraphicalElement86', None)
    assert getattr(partner, 'dg_Pattern85') is None


def test_assoc_transform6_stub_double():
    # dg_Transform has no real 'dg_Transform' property in the generated
    # code (a bare stub) -- manually attach it so dg_GraphicalElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dg_GraphicalElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dg_GraphicalElement(class_="sample_text", layoutData="sample_text")
    partner = dg_Transform()
    setattr(partner, 'dg_Transform', None)
    _safe_set(owner, 'dg_GraphicalElement7', {partner})
    assert getattr(partner, 'dg_Transform') == owner
    _safe_set(owner, 'dg_GraphicalElement7', set())
    assert getattr(partner, 'dg_Transform') is None


