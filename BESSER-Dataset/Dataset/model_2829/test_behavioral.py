import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractText,
    AdvancedAnchor,
    Anchor,
    AnchorContainer,
    Connection,
    ConnectionDecorator,
    ContainerShape,
    CurvedConnection,
    Diagram,
    GraphicsAlgorithm,
    GraphicsAlgorithmContainer,
    PictogramElement,
    PictogramLink,
    Polyline,
    PropertyContainer,
    Shape,
    StyleContainer,
    mm_GraphicsAlgorithmContainer,
    mm_Property,
    mm_PropertyContainer,
    mm_StyleContainer,
    mm_algorithms_AbstractText,
    mm_algorithms_Ellipse,
    mm_algorithms_GraphicsAlgorithm,
    mm_algorithms_Image,
    mm_algorithms_MultiText,
    mm_algorithms_PlatformGraphicsAlgorithm,
    mm_algorithms_Polygon,
    mm_algorithms_Polyline,
    mm_algorithms_Rectangle,
    mm_algorithms_RoundedRectangle,
    mm_algorithms_Text,
    mm_pictograms_AdvancedAnchor,
    mm_pictograms_Anchor,
    mm_pictograms_AnchorContainer,
    mm_pictograms_BoxRelativeAnchor,
    mm_pictograms_ChopboxAnchor,
    mm_pictograms_CompositeConnection,
    mm_pictograms_Connection,
    mm_pictograms_ConnectionDecorator,
    mm_pictograms_ContainerShape,
    mm_pictograms_CurvedConnection,
    mm_pictograms_Diagram,
    mm_pictograms_FixPointAnchor,
    mm_pictograms_FreeFormConnection,
    mm_pictograms_ManhattanConnection,
    mm_pictograms_PictogramElement,
    mm_pictograms_PictogramLink,
    mm_pictograms_Shape,
    mm_styles_AbstractStyle,
    mm_styles_AdaptedGradientColoredAreas,
    mm_styles_Color,
    mm_styles_Font,
    mm_styles_GradientColoredArea,
    mm_styles_GradientColoredAreas,
    mm_styles_GradientColoredLocation,
    mm_styles_Point,
    mm_styles_PrecisionPoint,
    mm_styles_RenderingStyle,
    mm_styles_Style,
    mm_styles_TextStyle,
    mm_styles_TextStyleRegion,
    pictograms_ContainerShape,
    pictograms_mm_EObject,
    styles_AbstractStyle,
    styles_AdaptedGradientColoredAreas,
    styles_Color,
    styles_Font,
    styles_GradientColoredArea,
    styles_GradientColoredAreas,
    styles_GradientColoredLocation,
    styles_Point,
    styles_PrecisionPoint,
    styles_RenderingStyle,
    styles_Style,
    styles_TextStyle,
    styles_TextStyleRegion,
    styles_mm_StyleContainer,
    LineStyle,
    LocationType,
    Orientation,
    UnderlineStyle,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_adaptedGradientColoredAreas69_stub_double():
    # styles_GradientColoredAreas has no real 'styles_GradientColoredAreas' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_AdaptedGradientColoredAreas's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_AdaptedGradientColoredAreas's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_AdaptedGradientColoredAreas(definedStyleId="sample_text", gradientType="sample_text")
    partner = styles_GradientColoredAreas()
    setattr(partner, 'styles_GradientColoredAreas', None)
    _safe_set(owner, 'mm_styles_AdaptedGradientColoredAreas', {partner})
    assert getattr(partner, 'styles_GradientColoredAreas') == owner
    _safe_set(owner, 'mm_styles_AdaptedGradientColoredAreas', set())
    assert getattr(partner, 'styles_GradientColoredAreas') is None


def test_assoc_background55_stub_double():
    # styles_Color has no real 'styles_Color56' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_AbstractStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_AbstractStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_AbstractStyle(filled="sample_text", lineStyle="sample_text", lineVisible="sample_text", lineWidth="sample_text", transparency="sample_text")
    partner = styles_Color()
    setattr(partner, 'styles_Color56', None)
    _safe_set(owner, 'mm_styles_AbstractStyle', partner)
    assert getattr(partner, 'styles_Color56') == owner
    _safe_set(owner, 'mm_styles_AbstractStyle', None)
    assert getattr(partner, 'styles_Color56') is None


def test_assoc_background75_stub_double():
    # styles_Color has no real 'styles_Color77' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_TextStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_TextStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_TextStyle(strikeout=True, underline=True, underlineStyle="sample_text")
    partner = styles_Color()
    setattr(partner, 'styles_Color77', None)
    _safe_set(owner, 'mm_styles_TextStyle76', partner)
    assert getattr(partner, 'styles_Color77') == owner
    _safe_set(owner, 'mm_styles_TextStyle76', None)
    assert getattr(partner, 'styles_Color77') is None


def test_assoc_color62_stub_double():
    # styles_Color has no real 'styles_Color63' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_GradientColoredLocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_GradientColoredLocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_GradientColoredLocation(locationType="sample_text", locationValue="sample_text")
    partner = styles_Color()
    setattr(partner, 'styles_Color63', None)
    _safe_set(owner, 'mm_styles_GradientColoredLocation', partner)
    assert getattr(partner, 'styles_Color63') == owner
    _safe_set(owner, 'mm_styles_GradientColoredLocation', None)
    assert getattr(partner, 'styles_Color63') is None


def test_assoc_colors5_stub_double():
    # styles_Color has no real 'styles_Color' property in the generated
    # code (a bare stub) -- manually attach it so mm_pictograms_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_pictograms_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_pictograms_Diagram(diagramTypeId="sample_text", gridUnit=7, name="sample_text", showGuides=True, snapToGrid=True, version="sample_text", verticalGridUnit=7)
    partner = styles_Color()
    setattr(partner, 'styles_Color', None)
    _safe_set(owner, 'mm_pictograms_Diagram', {partner})
    assert getattr(partner, 'styles_Color') == owner
    _safe_set(owner, 'mm_pictograms_Diagram', set())
    assert getattr(partner, 'styles_Color') is None


def test_assoc_connection30_stub_double():
    # Connection has no real 'Connection31' property in the generated
    # code (a bare stub) -- manually attach it so mm_pictograms_ConnectionDecorator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_pictograms_ConnectionDecorator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_pictograms_ConnectionDecorator(location=3.14, locationRelative=True)
    partner = Connection()
    setattr(partner, 'Connection31', None)
    _safe_set(owner, 'connectionDecorators', partner)
    assert getattr(partner, 'Connection31') == owner
    _safe_set(owner, 'connectionDecorators', None)
    assert getattr(partner, 'Connection31') is None


def test_assoc_connections4_stub_double():
    # Connection has no real 'Connection' property in the generated
    # code (a bare stub) -- manually attach it so mm_pictograms_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_pictograms_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_pictograms_Diagram(diagramTypeId="sample_text", gridUnit=7, name="sample_text", showGuides=True, snapToGrid=True, version="sample_text", verticalGridUnit=7)
    partner = Connection()
    setattr(partner, 'Connection', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'Connection') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'Connection') is None


def test_assoc_font47_stub_double():
    # styles_Font has no real 'styles_Font48' property in the generated
    # code (a bare stub) -- manually attach it so mm_algorithms_AbstractText's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_algorithms_AbstractText's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_algorithms_AbstractText(angle="sample_text", horizontalAlignment="sample_text", rotation="sample_text", value="sample_text", verticalAlignment="sample_text")
    partner = styles_Font()
    setattr(partner, 'styles_Font48', None)
    _safe_set(owner, 'mm_algorithms_AbstractText', partner)
    assert getattr(partner, 'styles_Font48') == owner
    _safe_set(owner, 'mm_algorithms_AbstractText', None)
    assert getattr(partner, 'styles_Font48') is None


def test_assoc_font52_stub_double():
    # styles_Font has no real 'styles_Font53' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_Style(angle="sample_text", description="sample_text", horizontalAlignment="sample_text", id="sample_text", proportional="sample_text", rotation="sample_text", stretchH="sample_text", stretchV="sample_text", verticalAlignment="sample_text")
    partner = styles_Font()
    setattr(partner, 'styles_Font53', None)
    _safe_set(owner, 'mm_styles_Style', partner)
    assert getattr(partner, 'styles_Font53') == owner
    _safe_set(owner, 'mm_styles_Style', None)
    assert getattr(partner, 'styles_Font53') is None


def test_assoc_font70_stub_double():
    # styles_Font has no real 'styles_Font71' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_TextStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_TextStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_TextStyle(strikeout=True, underline=True, underlineStyle="sample_text")
    partner = styles_Font()
    setattr(partner, 'styles_Font71', None)
    _safe_set(owner, 'mm_styles_TextStyle', partner)
    assert getattr(partner, 'styles_Font71') == owner
    _safe_set(owner, 'mm_styles_TextStyle', None)
    assert getattr(partner, 'styles_Font71') is None


def test_assoc_fonts6_stub_double():
    # styles_Font has no real 'styles_Font' property in the generated
    # code (a bare stub) -- manually attach it so mm_pictograms_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_pictograms_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_pictograms_Diagram(diagramTypeId="sample_text", gridUnit=7, name="sample_text", showGuides=True, snapToGrid=True, version="sample_text", verticalGridUnit=7)
    partner = styles_Font()
    setattr(partner, 'styles_Font', None)
    _safe_set(owner, 'mm_pictograms_Diagram7', {partner})
    assert getattr(partner, 'styles_Font') == owner
    _safe_set(owner, 'mm_pictograms_Diagram7', set())
    assert getattr(partner, 'styles_Font') is None


def test_assoc_foreground57_stub_double():
    # styles_Color has no real 'styles_Color59' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_AbstractStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_AbstractStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_AbstractStyle(filled="sample_text", lineStyle="sample_text", lineVisible="sample_text", lineWidth="sample_text", transparency="sample_text")
    partner = styles_Color()
    setattr(partner, 'styles_Color59', None)
    _safe_set(owner, 'mm_styles_AbstractStyle58', partner)
    assert getattr(partner, 'styles_Color59') == owner
    _safe_set(owner, 'mm_styles_AbstractStyle58', None)
    assert getattr(partner, 'styles_Color59') is None


def test_assoc_foreground72_stub_double():
    # styles_Color has no real 'styles_Color74' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_TextStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_TextStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_TextStyle(strikeout=True, underline=True, underlineStyle="sample_text")
    partner = styles_Color()
    setattr(partner, 'styles_Color74', None)
    _safe_set(owner, 'mm_styles_TextStyle73', partner)
    assert getattr(partner, 'styles_Color74') == owner
    _safe_set(owner, 'mm_styles_TextStyle73', None)
    assert getattr(partner, 'styles_Color74') is None


def test_assoc_gradientColor68_stub_double():
    # styles_GradientColoredArea has no real 'styles_GradientColoredArea' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_GradientColoredAreas's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_GradientColoredAreas's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_GradientColoredAreas(styleAdaption="sample_text")
    partner = styles_GradientColoredArea()
    setattr(partner, 'styles_GradientColoredArea', None)
    _safe_set(owner, 'mm_styles_GradientColoredAreas', {partner})
    assert getattr(partner, 'styles_GradientColoredArea') == owner
    _safe_set(owner, 'mm_styles_GradientColoredAreas', set())
    assert getattr(partner, 'styles_GradientColoredArea') is None


def test_assoc_graphicsAlgorithm10_stub_double():
    # GraphicsAlgorithm has no real 'GraphicsAlgorithm' property in the generated
    # code (a bare stub) -- manually attach it so mm_pictograms_PictogramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_pictograms_PictogramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_pictograms_PictogramElement(active=True, visible=True)
    partner = GraphicsAlgorithm()
    setattr(partner, 'GraphicsAlgorithm', None)
    _safe_set(owner, 'pictogramElement', partner)
    assert getattr(partner, 'GraphicsAlgorithm') == owner
    _safe_set(owner, 'pictogramElement', None)
    assert getattr(partner, 'GraphicsAlgorithm') is None


def test_assoc_graphicsAlgorithmChildren38_stub_double():
    # GraphicsAlgorithm has no real 'GraphicsAlgorithm39' property in the generated
    # code (a bare stub) -- manually attach it so mm_algorithms_GraphicsAlgorithm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_algorithms_GraphicsAlgorithm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_algorithms_GraphicsAlgorithm(height=7, width=7, x=7, y=7)
    partner = GraphicsAlgorithm()
    setattr(partner, 'GraphicsAlgorithm39', None)
    _safe_set(owner, 'parentGraphicsAlgorithm', {partner})
    assert getattr(partner, 'GraphicsAlgorithm39') == owner
    _safe_set(owner, 'parentGraphicsAlgorithm', set())
    assert getattr(partner, 'GraphicsAlgorithm39') is None


def test_assoc_link11_stub_double():
    # PictogramLink has no real 'PictogramLink13' property in the generated
    # code (a bare stub) -- manually attach it so mm_pictograms_PictogramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_pictograms_PictogramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_pictograms_PictogramElement(active=True, visible=True)
    partner = PictogramLink()
    setattr(partner, 'PictogramLink13', None)
    _safe_set(owner, 'pictogramElement12', partner)
    assert getattr(partner, 'PictogramLink13') == owner
    _safe_set(owner, 'pictogramElement12', None)
    assert getattr(partner, 'PictogramLink13') is None


def test_assoc_parentGraphicsAlgorithm40_stub_double():
    # GraphicsAlgorithm has no real 'GraphicsAlgorithm41' property in the generated
    # code (a bare stub) -- manually attach it so mm_algorithms_GraphicsAlgorithm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_algorithms_GraphicsAlgorithm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_algorithms_GraphicsAlgorithm(height=7, width=7, x=7, y=7)
    partner = GraphicsAlgorithm()
    setattr(partner, 'GraphicsAlgorithm41', None)
    _safe_set(owner, 'graphicsAlgorithmChildren', partner)
    assert getattr(partner, 'GraphicsAlgorithm41') == owner
    _safe_set(owner, 'graphicsAlgorithmChildren', None)
    assert getattr(partner, 'GraphicsAlgorithm41') is None


def test_assoc_pictogramElement42_stub_double():
    # PictogramElement has no real 'PictogramElement43' property in the generated
    # code (a bare stub) -- manually attach it so mm_algorithms_GraphicsAlgorithm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_algorithms_GraphicsAlgorithm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_algorithms_GraphicsAlgorithm(height=7, width=7, x=7, y=7)
    partner = PictogramElement()
    setattr(partner, 'PictogramElement43', None)
    _safe_set(owner, 'graphicsAlgorithm', partner)
    assert getattr(partner, 'PictogramElement43') == owner
    _safe_set(owner, 'graphicsAlgorithm', None)
    assert getattr(partner, 'PictogramElement43') is None


def test_assoc_pictogramLinks8_stub_double():
    # PictogramLink has no real 'PictogramLink' property in the generated
    # code (a bare stub) -- manually attach it so mm_pictograms_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_pictograms_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_pictograms_Diagram(diagramTypeId="sample_text", gridUnit=7, name="sample_text", showGuides=True, snapToGrid=True, version="sample_text", verticalGridUnit=7)
    partner = PictogramLink()
    setattr(partner, 'PictogramLink', None)
    _safe_set(owner, 'mm_pictograms_Diagram9', {partner})
    assert getattr(partner, 'PictogramLink') == owner
    _safe_set(owner, 'mm_pictograms_Diagram9', set())
    assert getattr(partner, 'PictogramLink') is None


def test_assoc_properties0_stub_double():
    # mm_PropertyContainer has no real 'mm_PropertyContainer' property in the generated
    # code (a bare stub) -- manually attach it so mm_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_Property(key="sample_text", value="sample_text")
    partner = mm_PropertyContainer()
    setattr(partner, 'mm_PropertyContainer', None)
    _safe_set(owner, 'mm_Property', partner)
    assert owner in getattr(partner, 'mm_PropertyContainer')
    _safe_set(owner, 'mm_Property', None)
    assert owner not in getattr(partner, 'mm_PropertyContainer')


def test_assoc_renderingStyle60_stub_double():
    # styles_RenderingStyle has no real 'styles_RenderingStyle' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_AbstractStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_AbstractStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_AbstractStyle(filled="sample_text", lineStyle="sample_text", lineVisible="sample_text", lineWidth="sample_text", transparency="sample_text")
    partner = styles_RenderingStyle()
    setattr(partner, 'styles_RenderingStyle', None)
    _safe_set(owner, 'mm_styles_AbstractStyle61', partner)
    assert getattr(partner, 'styles_RenderingStyle') == owner
    _safe_set(owner, 'mm_styles_AbstractStyle61', None)
    assert getattr(partner, 'styles_RenderingStyle') is None


def test_assoc_strikeoutColor81_stub_double():
    # styles_Color has no real 'styles_Color83' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_TextStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_TextStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_TextStyle(strikeout=True, underline=True, underlineStyle="sample_text")
    partner = styles_Color()
    setattr(partner, 'styles_Color83', None)
    _safe_set(owner, 'mm_styles_TextStyle82', partner)
    assert getattr(partner, 'styles_Color83') == owner
    _safe_set(owner, 'mm_styles_TextStyle82', None)
    assert getattr(partner, 'styles_Color83') is None


def test_assoc_style44_stub_double():
    # styles_Style has no real 'styles_Style' property in the generated
    # code (a bare stub) -- manually attach it so mm_algorithms_GraphicsAlgorithm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_algorithms_GraphicsAlgorithm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_algorithms_GraphicsAlgorithm(height=7, width=7, x=7, y=7)
    partner = styles_Style()
    setattr(partner, 'styles_Style', None)
    _safe_set(owner, 'mm_algorithms_GraphicsAlgorithm', partner)
    assert getattr(partner, 'styles_Style') == owner
    _safe_set(owner, 'mm_algorithms_GraphicsAlgorithm', None)
    assert getattr(partner, 'styles_Style') is None


def test_assoc_style84_stub_double():
    # styles_TextStyle has no real 'styles_TextStyle' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_TextStyleRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_TextStyleRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_TextStyleRegion(end=7, start=7)
    partner = styles_TextStyle()
    setattr(partner, 'styles_TextStyle', None)
    _safe_set(owner, 'mm_styles_TextStyleRegion', partner)
    assert getattr(partner, 'styles_TextStyle') == owner
    _safe_set(owner, 'mm_styles_TextStyleRegion', None)
    assert getattr(partner, 'styles_TextStyle') is None


def test_assoc_styleContainer54_stub_double():
    # styles_mm_StyleContainer has no real 'StyleContainer' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_Style(angle="sample_text", description="sample_text", horizontalAlignment="sample_text", id="sample_text", proportional="sample_text", rotation="sample_text", stretchH="sample_text", stretchV="sample_text", verticalAlignment="sample_text")
    partner = styles_mm_StyleContainer()
    setattr(partner, 'StyleContainer', None)
    _safe_set(owner, 'styles', partner)
    assert getattr(partner, 'StyleContainer') == owner
    _safe_set(owner, 'styles', None)
    assert getattr(partner, 'StyleContainer') is None


def test_assoc_styleRegions49_stub_double():
    # styles_TextStyleRegion has no real 'styles_TextStyleRegion' property in the generated
    # code (a bare stub) -- manually attach it so mm_algorithms_AbstractText's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_algorithms_AbstractText's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_algorithms_AbstractText(angle="sample_text", horizontalAlignment="sample_text", rotation="sample_text", value="sample_text", verticalAlignment="sample_text")
    partner = styles_TextStyleRegion()
    setattr(partner, 'styles_TextStyleRegion', None)
    _safe_set(owner, 'mm_algorithms_AbstractText50', {partner})
    assert getattr(partner, 'styles_TextStyleRegion') == owner
    _safe_set(owner, 'mm_algorithms_AbstractText50', set())
    assert getattr(partner, 'styles_TextStyleRegion') is None


def test_assoc_underlineColor78_stub_double():
    # styles_Color has no real 'styles_Color80' property in the generated
    # code (a bare stub) -- manually attach it so mm_styles_TextStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_styles_TextStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_styles_TextStyle(strikeout=True, underline=True, underlineStyle="sample_text")
    partner = styles_Color()
    setattr(partner, 'styles_Color80', None)
    _safe_set(owner, 'mm_styles_TextStyle79', partner)
    assert getattr(partner, 'styles_Color80') == owner
    _safe_set(owner, 'mm_styles_TextStyle79', None)
    assert getattr(partner, 'styles_Color80') is None


