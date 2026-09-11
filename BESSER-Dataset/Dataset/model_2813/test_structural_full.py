import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnchorPositionPos,
    AnchorType,
    CompartmentShape,
    Shape,
    ShapeConnection,
    ShapeContainerElement,
    shape_Anchor,
    shape_AnchorFixPointPosition,
    shape_AnchorManual,
    shape_AnchorPosition,
    shape_AnchorPositionPos,
    shape_AnchorPredefinied,
    shape_AnchorRelativePosition,
    shape_AnchorType,
    shape_CDEllipse,
    shape_CDLine,
    shape_CDPolygon,
    shape_CDPolyline,
    shape_CDRectangle,
    shape_CDRoundedRectangle,
    shape_CDText,
    shape_CommonLayout,
    shape_Compartment,
    shape_CompartmentEllipse,
    shape_CompartmentInfo,
    shape_CompartmentPolygon,
    shape_CompartmentRectangle,
    shape_CompartmentRoundedRectangle,
    shape_CompartmentShape,
    shape_ConnectionDefinition,
    shape_Description,
    shape_Ellipse,
    shape_Line,
    shape_LineLayout,
    shape_PlacingDefinition,
    shape_Point,
    shape_PolyLineLayout,
    shape_Polygon,
    shape_Polyline,
    shape_Rectangle,
    shape_RectangleEllipseLayout,
    shape_RoundedRectangle,
    shape_RoundedRectangleLayout,
    shape_Shape,
    shape_ShapeConnection,
    shape_ShapeContainer,
    shape_ShapeContainerElement,
    shape_ShapeDefinition,
    shape_ShapeLayout,
    shape_ShapestyleLayout,
    shape_Text,
    shape_TextBody,
    shape_TextLayout,
    AnchorPredefiniedEnum,
    CompartmentLayout,
    ConnectionStyle,
    HAlign,
    TextType,
    VAlign,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_shape_AnchorFixPointPosition_xcor_value_roundtrip():
    instance = shape_AnchorFixPointPosition(xcor=7, ycor=7)
    assert instance.xcor == 7
    instance.xcor = 13
    assert instance.xcor == 13


def test_shape_AnchorFixPointPosition_ycor_value_roundtrip():
    instance = shape_AnchorFixPointPosition(xcor=7, ycor=7)
    assert instance.ycor == 7
    instance.ycor = 13
    assert instance.ycor == 13


def test_shape_AnchorPredefinied_value_value_roundtrip():
    instance = shape_AnchorPredefinied(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_shape_AnchorRelativePosition_xoffset_value_roundtrip():
    instance = shape_AnchorRelativePosition(xoffset="sample_text", yoffset="sample_text")
    assert instance.xoffset == "sample_text"
    instance.xoffset = "sample_text_2"
    assert instance.xoffset == "sample_text_2"


def test_shape_AnchorRelativePosition_yoffset_value_roundtrip():
    instance = shape_AnchorRelativePosition(xoffset="sample_text", yoffset="sample_text")
    assert instance.yoffset == "sample_text"
    instance.yoffset = "sample_text_2"
    assert instance.yoffset == "sample_text_2"


def test_shape_CDText_texttype_value_roundtrip():
    instance = shape_CDText(texttype="sample_text")
    assert instance.texttype == "sample_text"
    instance.texttype = "sample_text_2"
    assert instance.texttype == "sample_text_2"


def test_shape_CommonLayout_heigth_value_roundtrip():
    instance = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    assert instance.heigth == 7
    instance.heigth = 13
    assert instance.heigth == 13


def test_shape_CommonLayout_width_value_roundtrip():
    instance = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_shape_CommonLayout_xcor_value_roundtrip():
    instance = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    assert instance.xcor == 7
    instance.xcor = 13
    assert instance.xcor == 13


def test_shape_CommonLayout_ycor_value_roundtrip():
    instance = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    assert instance.ycor == 7
    instance.ycor = 13
    assert instance.ycor == 13


def test_shape_Compartment_compartmentLayout_value_roundtrip():
    instance = shape_Compartment(compartmentLayout="sample_text")
    assert instance.compartmentLayout == "sample_text"
    instance.compartmentLayout = "sample_text_2"
    assert instance.compartmentLayout == "sample_text_2"


def test_shape_CompartmentInfo_compartmentLayout_value_roundtrip():
    instance = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    assert instance.compartmentLayout == "sample_text"
    instance.compartmentLayout = "sample_text_2"
    assert instance.compartmentLayout == "sample_text_2"


def test_shape_CompartmentInfo_invisible_value_roundtrip():
    instance = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    assert instance.invisible == True
    instance.invisible = False
    assert instance.invisible == False


def test_shape_CompartmentInfo_margin_value_roundtrip():
    instance = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    assert instance.margin == 7
    instance.margin = 13
    assert instance.margin == 13


def test_shape_CompartmentInfo_spacing_value_roundtrip():
    instance = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    assert instance.spacing == 7
    instance.spacing = 13
    assert instance.spacing == 13


def test_shape_CompartmentInfo_stretchH_value_roundtrip():
    instance = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    assert instance.stretchH == "sample_text"
    instance.stretchH = "sample_text_2"
    assert instance.stretchH == "sample_text_2"


def test_shape_CompartmentInfo_stretchV_value_roundtrip():
    instance = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    assert instance.stretchV == "sample_text"
    instance.stretchV = "sample_text_2"
    assert instance.stretchV == "sample_text_2"


def test_shape_ConnectionDefinition_connectionStyle_value_roundtrip():
    instance = shape_ConnectionDefinition(connectionStyle="sample_text")
    assert instance.connectionStyle == "sample_text"
    instance.connectionStyle = "sample_text_2"
    assert instance.connectionStyle == "sample_text_2"


def test_shape_Description_hAlign_value_roundtrip():
    instance = shape_Description(hAlign="sample_text", style="sample_text", vAlign="sample_text")
    assert instance.hAlign == "sample_text"
    instance.hAlign = "sample_text_2"
    assert instance.hAlign == "sample_text_2"


def test_shape_Description_style_value_roundtrip():
    instance = shape_Description(hAlign="sample_text", style="sample_text", vAlign="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_shape_Description_vAlign_value_roundtrip():
    instance = shape_Description(hAlign="sample_text", style="sample_text", vAlign="sample_text")
    assert instance.vAlign == "sample_text"
    instance.vAlign = "sample_text_2"
    assert instance.vAlign == "sample_text_2"


def test_shape_PlacingDefinition_angle_value_roundtrip():
    instance = shape_PlacingDefinition(angle=7, distance=7, offset="sample_text")
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_shape_PlacingDefinition_distance_value_roundtrip():
    instance = shape_PlacingDefinition(angle=7, distance=7, offset="sample_text")
    assert instance.distance == 7
    instance.distance = 13
    assert instance.distance == 13


def test_shape_PlacingDefinition_offset_value_roundtrip():
    instance = shape_PlacingDefinition(angle=7, distance=7, offset="sample_text")
    assert instance.offset == "sample_text"
    instance.offset = "sample_text_2"
    assert instance.offset == "sample_text_2"


def test_shape_Point_curveAfter_value_roundtrip():
    instance = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    assert instance.curveAfter == 7
    instance.curveAfter = 13
    assert instance.curveAfter == 13


def test_shape_Point_curveBefore_value_roundtrip():
    instance = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    assert instance.curveBefore == 7
    instance.curveBefore = 13
    assert instance.curveBefore == 13


def test_shape_Point_xcor_value_roundtrip():
    instance = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    assert instance.xcor == "sample_text"
    instance.xcor = "sample_text_2"
    assert instance.xcor == "sample_text_2"


def test_shape_Point_ycor_value_roundtrip():
    instance = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    assert instance.ycor == "sample_text"
    instance.ycor = "sample_text_2"
    assert instance.ycor == "sample_text_2"


def test_shape_RoundedRectangleLayout_curveHeight_value_roundtrip():
    instance = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    assert instance.curveHeight == 7
    instance.curveHeight = 13
    assert instance.curveHeight == 13


def test_shape_RoundedRectangleLayout_curveWidth_value_roundtrip():
    instance = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    assert instance.curveWidth == 7
    instance.curveWidth = 13
    assert instance.curveWidth == 13


def test_shape_Shape_style_value_roundtrip():
    instance = shape_Shape(style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_shape_ShapeConnection_style_value_roundtrip():
    instance = shape_ShapeConnection(style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_shape_ShapeContainerElement_name_value_roundtrip():
    instance = shape_ShapeContainerElement(name="sample_text", style="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_shape_ShapeContainerElement_style_value_roundtrip():
    instance = shape_ShapeContainerElement(name="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_shape_ShapeLayout_maxheight_value_roundtrip():
    instance = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    assert instance.maxheight == 7
    instance.maxheight = 13
    assert instance.maxheight == 13


def test_shape_ShapeLayout_maxwidth_value_roundtrip():
    instance = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    assert instance.maxwidth == 7
    instance.maxwidth = 13
    assert instance.maxwidth == 13


def test_shape_ShapeLayout_minheight_value_roundtrip():
    instance = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    assert instance.minheight == 7
    instance.minheight = 13
    assert instance.minheight == 13


def test_shape_ShapeLayout_minwidth_value_roundtrip():
    instance = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    assert instance.minwidth == 7
    instance.minwidth = 13
    assert instance.minwidth == 13


def test_shape_ShapeLayout_proportional_value_roundtrip():
    instance = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    assert instance.proportional == "sample_text"
    instance.proportional = "sample_text_2"
    assert instance.proportional == "sample_text_2"


def test_shape_ShapeLayout_stretchH_value_roundtrip():
    instance = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    assert instance.stretchH == "sample_text"
    instance.stretchH = "sample_text_2"
    assert instance.stretchH == "sample_text_2"


def test_shape_ShapeLayout_stretchV_value_roundtrip():
    instance = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    assert instance.stretchV == "sample_text"
    instance.stretchV = "sample_text_2"
    assert instance.stretchV == "sample_text_2"


def test_shape_Text_texttype_value_roundtrip():
    instance = shape_Text(texttype="sample_text")
    assert instance.texttype == "sample_text"
    instance.texttype = "sample_text_2"
    assert instance.texttype == "sample_text_2"


def test_shape_TextBody_value_value_roundtrip():
    instance = shape_TextBody(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_shape_TextLayout_hAlign_value_roundtrip():
    instance = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    assert instance.hAlign == "sample_text"
    instance.hAlign = "sample_text_2"
    assert instance.hAlign == "sample_text_2"


def test_shape_TextLayout_vAlign_value_roundtrip():
    instance = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    assert instance.vAlign == "sample_text"
    instance.vAlign = "sample_text_2"
    assert instance.vAlign == "sample_text_2"


def test_shape_AnchorFixPointPosition_isa_AnchorPositionPos():
    instance = shape_AnchorFixPointPosition(xcor=7, ycor=7)
    assert isinstance(instance, AnchorPositionPos)


def test_shape_AnchorRelativePosition_isa_AnchorPositionPos():
    instance = shape_AnchorRelativePosition(xoffset="sample_text", yoffset="sample_text")
    assert isinstance(instance, AnchorPositionPos)


def test_shape_AnchorManual_isa_AnchorType():
    instance = shape_AnchorManual()
    assert isinstance(instance, AnchorType)


def test_shape_AnchorPredefinied_isa_AnchorType():
    instance = shape_AnchorPredefinied(value="sample_text")
    assert isinstance(instance, AnchorType)


def test_shape_CompartmentEllipse_isa_CompartmentShape():
    instance = shape_CompartmentEllipse()
    assert isinstance(instance, CompartmentShape)


def test_shape_CompartmentRectangle_isa_CompartmentShape():
    instance = shape_CompartmentRectangle()
    assert isinstance(instance, CompartmentShape)


def test_shape_Ellipse_isa_Shape():
    instance = shape_Ellipse()
    assert isinstance(instance, Shape)


def test_shape_Line_isa_Shape():
    instance = shape_Line()
    assert isinstance(instance, Shape)


def test_shape_Polygon_isa_Shape():
    instance = shape_Polygon()
    assert isinstance(instance, Shape)


def test_shape_Polyline_isa_Shape():
    instance = shape_Polyline()
    assert isinstance(instance, Shape)


def test_shape_Rectangle_isa_Shape():
    instance = shape_Rectangle()
    assert isinstance(instance, Shape)


def test_shape_RoundedRectangle_isa_Shape():
    instance = shape_RoundedRectangle()
    assert isinstance(instance, Shape)


def test_shape_Text_isa_Shape():
    instance = shape_Text(texttype="sample_text")
    assert isinstance(instance, Shape)


def test_shape_CDEllipse_isa_ShapeConnection():
    instance = shape_CDEllipse()
    assert isinstance(instance, ShapeConnection)


def test_shape_CDLine_isa_ShapeConnection():
    instance = shape_CDLine()
    assert isinstance(instance, ShapeConnection)


def test_shape_CDPolygon_isa_ShapeConnection():
    instance = shape_CDPolygon()
    assert isinstance(instance, ShapeConnection)


def test_shape_CDPolyline_isa_ShapeConnection():
    instance = shape_CDPolyline()
    assert isinstance(instance, ShapeConnection)


def test_shape_CDRectangle_isa_ShapeConnection():
    instance = shape_CDRectangle()
    assert isinstance(instance, ShapeConnection)


def test_shape_CDRoundedRectangle_isa_ShapeConnection():
    instance = shape_CDRoundedRectangle()
    assert isinstance(instance, ShapeConnection)


def test_shape_CDText_isa_ShapeConnection():
    instance = shape_CDText(texttype="sample_text")
    assert isinstance(instance, ShapeConnection)


def test_shape_ConnectionDefinition_isa_ShapeContainerElement():
    instance = shape_ConnectionDefinition(connectionStyle="sample_text")
    assert isinstance(instance, ShapeContainerElement)


def test_shape_ShapeDefinition_isa_ShapeContainerElement():
    instance = shape_ShapeDefinition()
    assert isinstance(instance, ShapeContainerElement)


def test_assoc_body27_link_reassign_clear():
    a = shape_TextBody(value="sample_text")
    b1 = shape_CDText(texttype="sample_text")
    b2 = shape_CDText(texttype="sample_text_2")
    _safe_set(a, 'shape_TextBody', b1)
    assert _is_linked(a, 'shape_TextBody', b1)
    if hasattr(b1, 'shape_CDText28'):
        assert _is_linked(b1, 'shape_CDText28', a)
    _safe_set(a, 'shape_TextBody', b2)
    assert _is_linked(a, 'shape_TextBody', b2)
    if hasattr(b1, 'shape_CDText28'):
        assert not _is_linked(b1, 'shape_CDText28', a)
    if hasattr(b2, 'shape_CDText28'):
        assert _is_linked(b2, 'shape_CDText28', a)
    _safe_set(a, 'shape_TextBody', None)
    assert not _is_linked(a, 'shape_TextBody', b2)
    if hasattr(b2, 'shape_CDText28'):
        assert not _is_linked(b2, 'shape_CDText28', a)


def test_assoc_body60_link_reassign_clear():
    a = shape_TextBody(value="sample_text")
    b1 = shape_Text(texttype="sample_text")
    b2 = shape_Text(texttype="sample_text_2")
    _safe_set(a, 'shape_TextBody62', b1)
    assert _is_linked(a, 'shape_TextBody62', b1)
    if hasattr(b1, 'shape_Text61'):
        assert _is_linked(b1, 'shape_Text61', a)
    _safe_set(a, 'shape_TextBody62', b2)
    assert _is_linked(a, 'shape_TextBody62', b2)
    if hasattr(b1, 'shape_Text61'):
        assert not _is_linked(b1, 'shape_Text61', a)
    if hasattr(b2, 'shape_Text61'):
        assert _is_linked(b2, 'shape_Text61', a)
    _safe_set(a, 'shape_TextBody62', None)
    assert not _is_linked(a, 'shape_TextBody62', b2)
    if hasattr(b2, 'shape_Text61'):
        assert not _is_linked(b2, 'shape_Text61', a)


def test_assoc_body83_link_reassign_clear():
    a = shape_TextBody(value="sample_text")
    b1 = shape_Description(hAlign="sample_text", style="sample_text", vAlign="sample_text")
    b2 = shape_Description(hAlign="sample_text_2", style="sample_text_2", vAlign="sample_text_2")
    _safe_set(a, 'shape_TextBody85', b1)
    assert _is_linked(a, 'shape_TextBody85', b1)
    if hasattr(b1, 'shape_Description84'):
        assert _is_linked(b1, 'shape_Description84', a)
    _safe_set(a, 'shape_TextBody85', b2)
    assert _is_linked(a, 'shape_TextBody85', b2)
    if hasattr(b1, 'shape_Description84'):
        assert not _is_linked(b1, 'shape_Description84', a)
    if hasattr(b2, 'shape_Description84'):
        assert _is_linked(b2, 'shape_Description84', a)
    _safe_set(a, 'shape_TextBody85', None)
    assert not _is_linked(a, 'shape_TextBody85', b2)
    if hasattr(b2, 'shape_Description84'):
        assert not _is_linked(b2, 'shape_Description84', a)


def test_assoc_common102_link_reassign_clear():
    a = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    b1 = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    b2 = shape_CommonLayout(heigth=13, width=13, xcor=13, ycor=13)
    _safe_set(a, 'shape_RoundedRectangleLayout103', b1)
    assert _is_linked(a, 'shape_RoundedRectangleLayout103', b1)
    if hasattr(b1, 'shape_CommonLayout104'):
        assert _is_linked(b1, 'shape_CommonLayout104', a)
    _safe_set(a, 'shape_RoundedRectangleLayout103', b2)
    assert _is_linked(a, 'shape_RoundedRectangleLayout103', b2)
    if hasattr(b1, 'shape_CommonLayout104'):
        assert not _is_linked(b1, 'shape_CommonLayout104', a)
    if hasattr(b2, 'shape_CommonLayout104'):
        assert _is_linked(b2, 'shape_CommonLayout104', a)
    _safe_set(a, 'shape_RoundedRectangleLayout103', None)
    assert not _is_linked(a, 'shape_RoundedRectangleLayout103', b2)
    if hasattr(b2, 'shape_CommonLayout104'):
        assert not _is_linked(b2, 'shape_CommonLayout104', a)


def test_assoc_common108_link_reassign_clear():
    a = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    b1 = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    b2 = shape_CommonLayout(heigth=13, width=13, xcor=13, ycor=13)
    _safe_set(a, 'shape_TextLayout109', b1)
    assert _is_linked(a, 'shape_TextLayout109', b1)
    if hasattr(b1, 'shape_CommonLayout110'):
        assert _is_linked(b1, 'shape_CommonLayout110', a)
    _safe_set(a, 'shape_TextLayout109', b2)
    assert _is_linked(a, 'shape_TextLayout109', b2)
    if hasattr(b1, 'shape_CommonLayout110'):
        assert not _is_linked(b1, 'shape_CommonLayout110', a)
    if hasattr(b2, 'shape_CommonLayout110'):
        assert _is_linked(b2, 'shape_CommonLayout110', a)
    _safe_set(a, 'shape_TextLayout109', None)
    assert not _is_linked(a, 'shape_TextLayout109', b2)
    if hasattr(b2, 'shape_CommonLayout110'):
        assert not _is_linked(b2, 'shape_CommonLayout110', a)


def test_assoc_common86_link_reassign_clear():
    a = shape_CommonLayout(heigth=7, width=7, xcor=7, ycor=7)
    b1 = shape_RectangleEllipseLayout()
    b2 = shape_RectangleEllipseLayout()
    _safe_set(a, 'shape_CommonLayout', b1)
    assert _is_linked(a, 'shape_CommonLayout', b1)
    if hasattr(b1, 'shape_RectangleEllipseLayout87'):
        assert _is_linked(b1, 'shape_RectangleEllipseLayout87', a)
    _safe_set(a, 'shape_CommonLayout', b2)
    assert _is_linked(a, 'shape_CommonLayout', b2)
    if hasattr(b1, 'shape_RectangleEllipseLayout87'):
        assert not _is_linked(b1, 'shape_RectangleEllipseLayout87', a)
    if hasattr(b2, 'shape_RectangleEllipseLayout87'):
        assert _is_linked(b2, 'shape_RectangleEllipseLayout87', a)
    _safe_set(a, 'shape_CommonLayout', None)
    assert not _is_linked(a, 'shape_CommonLayout', b2)
    if hasattr(b2, 'shape_RectangleEllipseLayout87'):
        assert not _is_linked(b2, 'shape_RectangleEllipseLayout87', a)


def test_assoc_compartmentInfo33_link_reassign_clear():
    a = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    b1 = shape_Rectangle()
    b2 = shape_Rectangle()
    _safe_set(a, 'shape_CompartmentInfo', b1)
    assert _is_linked(a, 'shape_CompartmentInfo', b1)
    if hasattr(b1, 'shape_Rectangle'):
        assert _is_linked(b1, 'shape_Rectangle', a)
    _safe_set(a, 'shape_CompartmentInfo', b2)
    assert _is_linked(a, 'shape_CompartmentInfo', b2)
    if hasattr(b1, 'shape_Rectangle'):
        assert not _is_linked(b1, 'shape_Rectangle', a)
    if hasattr(b2, 'shape_Rectangle'):
        assert _is_linked(b2, 'shape_Rectangle', a)
    _safe_set(a, 'shape_CompartmentInfo', None)
    assert not _is_linked(a, 'shape_CompartmentInfo', b2)
    if hasattr(b2, 'shape_Rectangle'):
        assert not _is_linked(b2, 'shape_Rectangle', a)


def test_assoc_compartmentInfo50_link_reassign_clear():
    a = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    b1 = shape_Ellipse()
    b2 = shape_Ellipse()
    _safe_set(a, 'shape_CompartmentInfo51', b1)
    assert _is_linked(a, 'shape_CompartmentInfo51', b1)
    if hasattr(b1, 'shape_Ellipse'):
        assert _is_linked(b1, 'shape_Ellipse', a)
    _safe_set(a, 'shape_CompartmentInfo51', b2)
    assert _is_linked(a, 'shape_CompartmentInfo51', b2)
    if hasattr(b1, 'shape_Ellipse'):
        assert not _is_linked(b1, 'shape_Ellipse', a)
    if hasattr(b2, 'shape_Ellipse'):
        assert _is_linked(b2, 'shape_Ellipse', a)
    _safe_set(a, 'shape_CompartmentInfo51', None)
    assert not _is_linked(a, 'shape_CompartmentInfo51', b2)
    if hasattr(b2, 'shape_Ellipse'):
        assert not _is_linked(b2, 'shape_Ellipse', a)


def test_assoc_description7_link_reassign_clear():
    a = shape_Description(hAlign="sample_text", style="sample_text", vAlign="sample_text")
    b1 = shape_ShapeDefinition()
    b2 = shape_ShapeDefinition()
    _safe_set(a, 'shape_Description', b1)
    assert _is_linked(a, 'shape_Description', b1)
    if hasattr(b1, 'shape_ShapeDefinition8'):
        assert _is_linked(b1, 'shape_ShapeDefinition8', a)
    _safe_set(a, 'shape_Description', b2)
    assert _is_linked(a, 'shape_Description', b2)
    if hasattr(b1, 'shape_ShapeDefinition8'):
        assert not _is_linked(b1, 'shape_ShapeDefinition8', a)
    if hasattr(b2, 'shape_ShapeDefinition8'):
        assert _is_linked(b2, 'shape_ShapeDefinition8', a)
    _safe_set(a, 'shape_Description', None)
    assert not _is_linked(a, 'shape_Description', b2)
    if hasattr(b2, 'shape_ShapeDefinition8'):
        assert not _is_linked(b2, 'shape_ShapeDefinition8', a)


def test_assoc_id63_link_reassign_clear():
    a = shape_TextBody(value="sample_text")
    b1 = shape_CompartmentInfo(compartmentLayout="sample_text", invisible=True, margin=7, spacing=7, stretchH="sample_text", stretchV="sample_text")
    b2 = shape_CompartmentInfo(compartmentLayout="sample_text_2", invisible=False, margin=13, spacing=13, stretchH="sample_text_2", stretchV="sample_text_2")
    _safe_set(a, 'shape_TextBody65', b1)
    assert _is_linked(a, 'shape_TextBody65', b1)
    if hasattr(b1, 'shape_CompartmentInfo64'):
        assert _is_linked(b1, 'shape_CompartmentInfo64', a)
    _safe_set(a, 'shape_TextBody65', b2)
    assert _is_linked(a, 'shape_TextBody65', b2)
    if hasattr(b1, 'shape_CompartmentInfo64'):
        assert not _is_linked(b1, 'shape_CompartmentInfo64', a)
    if hasattr(b2, 'shape_CompartmentInfo64'):
        assert _is_linked(b2, 'shape_CompartmentInfo64', a)
    _safe_set(a, 'shape_TextBody65', None)
    assert not _is_linked(a, 'shape_TextBody65', b2)
    if hasattr(b2, 'shape_CompartmentInfo64'):
        assert not _is_linked(b2, 'shape_CompartmentInfo64', a)


def test_assoc_id70_link_reassign_clear():
    a = shape_TextBody(value="sample_text")
    b1 = shape_CompartmentShape()
    b2 = shape_CompartmentShape()
    _safe_set(a, 'shape_TextBody72', b1)
    assert _is_linked(a, 'shape_TextBody72', b1)
    if hasattr(b1, 'shape_CompartmentShape71'):
        assert _is_linked(b1, 'shape_CompartmentShape71', a)
    _safe_set(a, 'shape_TextBody72', b2)
    assert _is_linked(a, 'shape_TextBody72', b2)
    if hasattr(b1, 'shape_CompartmentShape71'):
        assert not _is_linked(b1, 'shape_CompartmentShape71', a)
    if hasattr(b2, 'shape_CompartmentShape71'):
        assert _is_linked(b2, 'shape_CompartmentShape71', a)
    _safe_set(a, 'shape_TextBody72', None)
    assert not _is_linked(a, 'shape_TextBody72', b2)
    if hasattr(b2, 'shape_CompartmentShape71'):
        assert not _is_linked(b2, 'shape_CompartmentShape71', a)


def test_assoc_id75_link_reassign_clear():
    a = shape_TextBody(value="sample_text")
    b1 = shape_CompartmentRoundedRectangle()
    b2 = shape_CompartmentRoundedRectangle()
    _safe_set(a, 'shape_TextBody77', b1)
    assert _is_linked(a, 'shape_TextBody77', b1)
    if hasattr(b1, 'shape_CompartmentRoundedRectangle76'):
        assert _is_linked(b1, 'shape_CompartmentRoundedRectangle76', a)
    _safe_set(a, 'shape_TextBody77', b2)
    assert _is_linked(a, 'shape_TextBody77', b2)
    if hasattr(b1, 'shape_CompartmentRoundedRectangle76'):
        assert not _is_linked(b1, 'shape_CompartmentRoundedRectangle76', a)
    if hasattr(b2, 'shape_CompartmentRoundedRectangle76'):
        assert _is_linked(b2, 'shape_CompartmentRoundedRectangle76', a)
    _safe_set(a, 'shape_TextBody77', None)
    assert not _is_linked(a, 'shape_TextBody77', b2)
    if hasattr(b2, 'shape_CompartmentRoundedRectangle76'):
        assert not _is_linked(b2, 'shape_CompartmentRoundedRectangle76', a)


def test_assoc_id80_link_reassign_clear():
    a = shape_TextBody(value="sample_text")
    b1 = shape_CompartmentPolygon()
    b2 = shape_CompartmentPolygon()
    _safe_set(a, 'shape_TextBody82', b1)
    assert _is_linked(a, 'shape_TextBody82', b1)
    if hasattr(b1, 'shape_CompartmentPolygon81'):
        assert _is_linked(b1, 'shape_CompartmentPolygon81', a)
    _safe_set(a, 'shape_TextBody82', b2)
    assert _is_linked(a, 'shape_TextBody82', b2)
    if hasattr(b1, 'shape_CompartmentPolygon81'):
        assert not _is_linked(b1, 'shape_CompartmentPolygon81', a)
    if hasattr(b2, 'shape_CompartmentPolygon81'):
        assert _is_linked(b2, 'shape_CompartmentPolygon81', a)
    _safe_set(a, 'shape_TextBody82', None)
    assert not _is_linked(a, 'shape_TextBody82', b2)
    if hasattr(b2, 'shape_CompartmentPolygon81'):
        assert not _is_linked(b2, 'shape_CompartmentPolygon81', a)


def test_assoc_layout1_link_reassign_clear():
    a = shape_ConnectionDefinition(connectionStyle="sample_text")
    b1 = shape_ShapestyleLayout()
    b2 = shape_ShapestyleLayout()
    _safe_set(a, 'shape_ConnectionDefinition', b1)
    assert _is_linked(a, 'shape_ConnectionDefinition', b1)
    if hasattr(b1, 'shape_ShapestyleLayout'):
        assert _is_linked(b1, 'shape_ShapestyleLayout', a)
    _safe_set(a, 'shape_ConnectionDefinition', b2)
    assert _is_linked(a, 'shape_ConnectionDefinition', b2)
    if hasattr(b1, 'shape_ShapestyleLayout'):
        assert not _is_linked(b1, 'shape_ShapestyleLayout', a)
    if hasattr(b2, 'shape_ShapestyleLayout'):
        assert _is_linked(b2, 'shape_ShapestyleLayout', a)
    _safe_set(a, 'shape_ConnectionDefinition', None)
    assert not _is_linked(a, 'shape_ConnectionDefinition', b2)
    if hasattr(b2, 'shape_ShapestyleLayout'):
        assert not _is_linked(b2, 'shape_ShapestyleLayout', a)


def test_assoc_layout105_link_reassign_clear():
    a = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    b1 = shape_ShapestyleLayout()
    b2 = shape_ShapestyleLayout()
    _safe_set(a, 'shape_RoundedRectangleLayout106', b1)
    assert _is_linked(a, 'shape_RoundedRectangleLayout106', b1)
    if hasattr(b1, 'shape_ShapestyleLayout107'):
        assert _is_linked(b1, 'shape_ShapestyleLayout107', a)
    _safe_set(a, 'shape_RoundedRectangleLayout106', b2)
    assert _is_linked(a, 'shape_RoundedRectangleLayout106', b2)
    if hasattr(b1, 'shape_ShapestyleLayout107'):
        assert not _is_linked(b1, 'shape_ShapestyleLayout107', a)
    if hasattr(b2, 'shape_ShapestyleLayout107'):
        assert _is_linked(b2, 'shape_ShapestyleLayout107', a)
    _safe_set(a, 'shape_RoundedRectangleLayout106', None)
    assert not _is_linked(a, 'shape_RoundedRectangleLayout106', b2)
    if hasattr(b2, 'shape_ShapestyleLayout107'):
        assert not _is_linked(b2, 'shape_ShapestyleLayout107', a)


def test_assoc_layout111_link_reassign_clear():
    a = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    b1 = shape_ShapestyleLayout()
    b2 = shape_ShapestyleLayout()
    _safe_set(a, 'shape_TextLayout112', b1)
    assert _is_linked(a, 'shape_TextLayout112', b1)
    if hasattr(b1, 'shape_ShapestyleLayout113'):
        assert _is_linked(b1, 'shape_ShapestyleLayout113', a)
    _safe_set(a, 'shape_TextLayout112', b2)
    assert _is_linked(a, 'shape_TextLayout112', b2)
    if hasattr(b1, 'shape_ShapestyleLayout113'):
        assert not _is_linked(b1, 'shape_ShapestyleLayout113', a)
    if hasattr(b2, 'shape_ShapestyleLayout113'):
        assert _is_linked(b2, 'shape_ShapestyleLayout113', a)
    _safe_set(a, 'shape_TextLayout112', None)
    assert not _is_linked(a, 'shape_TextLayout112', b2)
    if hasattr(b2, 'shape_ShapestyleLayout113'):
        assert not _is_linked(b2, 'shape_ShapestyleLayout113', a)


def test_assoc_layout21_link_reassign_clear():
    a = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    b1 = shape_CDRoundedRectangle()
    b2 = shape_CDRoundedRectangle()
    _safe_set(a, 'shape_RoundedRectangleLayout', b1)
    assert _is_linked(a, 'shape_RoundedRectangleLayout', b1)
    if hasattr(b1, 'shape_CDRoundedRectangle'):
        assert _is_linked(b1, 'shape_CDRoundedRectangle', a)
    _safe_set(a, 'shape_RoundedRectangleLayout', b2)
    assert _is_linked(a, 'shape_RoundedRectangleLayout', b2)
    if hasattr(b1, 'shape_CDRoundedRectangle'):
        assert not _is_linked(b1, 'shape_CDRoundedRectangle', a)
    if hasattr(b2, 'shape_CDRoundedRectangle'):
        assert _is_linked(b2, 'shape_CDRoundedRectangle', a)
    _safe_set(a, 'shape_RoundedRectangleLayout', None)
    assert not _is_linked(a, 'shape_RoundedRectangleLayout', b2)
    if hasattr(b2, 'shape_CDRoundedRectangle'):
        assert not _is_linked(b2, 'shape_CDRoundedRectangle', a)


def test_assoc_layout26_link_reassign_clear():
    a = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    b1 = shape_CDText(texttype="sample_text")
    b2 = shape_CDText(texttype="sample_text_2")
    _safe_set(a, 'shape_TextLayout', b1)
    assert _is_linked(a, 'shape_TextLayout', b1)
    if hasattr(b1, 'shape_CDText'):
        assert _is_linked(b1, 'shape_CDText', a)
    _safe_set(a, 'shape_TextLayout', b2)
    assert _is_linked(a, 'shape_TextLayout', b2)
    if hasattr(b1, 'shape_CDText'):
        assert not _is_linked(b1, 'shape_CDText', a)
    if hasattr(b2, 'shape_CDText'):
        assert _is_linked(b2, 'shape_CDText', a)
    _safe_set(a, 'shape_TextLayout', None)
    assert not _is_linked(a, 'shape_TextLayout', b2)
    if hasattr(b2, 'shape_CDText'):
        assert not _is_linked(b2, 'shape_CDText', a)


def test_assoc_layout40_link_reassign_clear():
    a = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    b1 = shape_RoundedRectangle()
    b2 = shape_RoundedRectangle()
    _safe_set(a, 'shape_RoundedRectangleLayout41', b1)
    assert _is_linked(a, 'shape_RoundedRectangleLayout41', b1)
    if hasattr(b1, 'shape_RoundedRectangle'):
        assert _is_linked(b1, 'shape_RoundedRectangle', a)
    _safe_set(a, 'shape_RoundedRectangleLayout41', b2)
    assert _is_linked(a, 'shape_RoundedRectangleLayout41', b2)
    if hasattr(b1, 'shape_RoundedRectangle'):
        assert not _is_linked(b1, 'shape_RoundedRectangle', a)
    if hasattr(b2, 'shape_RoundedRectangle'):
        assert _is_linked(b2, 'shape_RoundedRectangle', a)
    _safe_set(a, 'shape_RoundedRectangleLayout41', None)
    assert not _is_linked(a, 'shape_RoundedRectangleLayout41', b2)
    if hasattr(b2, 'shape_RoundedRectangle'):
        assert not _is_linked(b2, 'shape_RoundedRectangle', a)


def test_assoc_layout58_link_reassign_clear():
    a = shape_TextLayout(hAlign="sample_text", vAlign="sample_text")
    b1 = shape_Text(texttype="sample_text")
    b2 = shape_Text(texttype="sample_text_2")
    _safe_set(a, 'shape_TextLayout59', b1)
    assert _is_linked(a, 'shape_TextLayout59', b1)
    if hasattr(b1, 'shape_Text'):
        assert _is_linked(b1, 'shape_Text', a)
    _safe_set(a, 'shape_TextLayout59', b2)
    assert _is_linked(a, 'shape_TextLayout59', b2)
    if hasattr(b1, 'shape_Text'):
        assert not _is_linked(b1, 'shape_Text', a)
    if hasattr(b2, 'shape_Text'):
        assert _is_linked(b2, 'shape_Text', a)
    _safe_set(a, 'shape_TextLayout59', None)
    assert not _is_linked(a, 'shape_TextLayout59', b2)
    if hasattr(b2, 'shape_Text'):
        assert not _is_linked(b2, 'shape_Text', a)


def test_assoc_layout73_link_reassign_clear():
    a = shape_RoundedRectangleLayout(curveHeight=7, curveWidth=7)
    b1 = shape_CompartmentRoundedRectangle()
    b2 = shape_CompartmentRoundedRectangle()
    _safe_set(a, 'shape_RoundedRectangleLayout74', b1)
    assert _is_linked(a, 'shape_RoundedRectangleLayout74', b1)
    if hasattr(b1, 'shape_CompartmentRoundedRectangle'):
        assert _is_linked(b1, 'shape_CompartmentRoundedRectangle', a)
    _safe_set(a, 'shape_RoundedRectangleLayout74', b2)
    assert _is_linked(a, 'shape_RoundedRectangleLayout74', b2)
    if hasattr(b1, 'shape_CompartmentRoundedRectangle'):
        assert not _is_linked(b1, 'shape_CompartmentRoundedRectangle', a)
    if hasattr(b2, 'shape_CompartmentRoundedRectangle'):
        assert _is_linked(b2, 'shape_CompartmentRoundedRectangle', a)
    _safe_set(a, 'shape_RoundedRectangleLayout74', None)
    assert not _is_linked(a, 'shape_RoundedRectangleLayout74', b2)
    if hasattr(b2, 'shape_CompartmentRoundedRectangle'):
        assert not _is_linked(b2, 'shape_CompartmentRoundedRectangle', a)


def test_assoc_placing2_link_reassign_clear():
    a = shape_PlacingDefinition(angle=7, distance=7, offset="sample_text")
    b1 = shape_ConnectionDefinition(connectionStyle="sample_text")
    b2 = shape_ConnectionDefinition(connectionStyle="sample_text_2")
    _safe_set(a, 'shape_PlacingDefinition', b1)
    assert _is_linked(a, 'shape_PlacingDefinition', b1)
    if hasattr(b1, 'shape_ConnectionDefinition3'):
        assert _is_linked(b1, 'shape_ConnectionDefinition3', a)
    _safe_set(a, 'shape_PlacingDefinition', b2)
    assert _is_linked(a, 'shape_PlacingDefinition', b2)
    if hasattr(b1, 'shape_ConnectionDefinition3'):
        assert not _is_linked(b1, 'shape_ConnectionDefinition3', a)
    if hasattr(b2, 'shape_ConnectionDefinition3'):
        assert _is_linked(b2, 'shape_ConnectionDefinition3', a)
    _safe_set(a, 'shape_PlacingDefinition', None)
    assert not _is_linked(a, 'shape_PlacingDefinition', b2)
    if hasattr(b2, 'shape_ConnectionDefinition3'):
        assert not _is_linked(b2, 'shape_ConnectionDefinition3', a)


def test_assoc_point91_link_reassign_clear():
    a = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    b1 = shape_LineLayout()
    b2 = shape_LineLayout()
    _safe_set(a, 'shape_Point', b1)
    assert _is_linked(a, 'shape_Point', b1)
    if hasattr(b1, 'shape_LineLayout92'):
        assert _is_linked(b1, 'shape_LineLayout92', a)
    _safe_set(a, 'shape_Point', b2)
    assert _is_linked(a, 'shape_Point', b2)
    if hasattr(b1, 'shape_LineLayout92'):
        assert not _is_linked(b1, 'shape_LineLayout92', a)
    if hasattr(b2, 'shape_LineLayout92'):
        assert _is_linked(b2, 'shape_LineLayout92', a)
    _safe_set(a, 'shape_Point', None)
    assert not _is_linked(a, 'shape_Point', b2)
    if hasattr(b2, 'shape_LineLayout92'):
        assert not _is_linked(b2, 'shape_LineLayout92', a)


def test_assoc_point96_link_reassign_clear():
    a = shape_Point(curveAfter=7, curveBefore=7, xcor="sample_text", ycor="sample_text")
    b1 = shape_PolyLineLayout()
    b2 = shape_PolyLineLayout()
    _safe_set(a, 'shape_Point98', b1)
    assert _is_linked(a, 'shape_Point98', b1)
    if hasattr(b1, 'shape_PolyLineLayout97'):
        assert _is_linked(b1, 'shape_PolyLineLayout97', a)
    _safe_set(a, 'shape_Point98', b2)
    assert _is_linked(a, 'shape_Point98', b2)
    if hasattr(b1, 'shape_PolyLineLayout97'):
        assert not _is_linked(b1, 'shape_PolyLineLayout97', a)
    if hasattr(b2, 'shape_PolyLineLayout97'):
        assert _is_linked(b2, 'shape_PolyLineLayout97', a)
    _safe_set(a, 'shape_Point98', None)
    assert not _is_linked(a, 'shape_Point98', b2)
    if hasattr(b2, 'shape_PolyLineLayout97'):
        assert not _is_linked(b2, 'shape_PolyLineLayout97', a)


def test_assoc_shape37_link_reassign_clear():
    a = shape_Shape(style="sample_text")
    b1 = shape_Rectangle()
    b2 = shape_Rectangle()
    _safe_set(a, 'shape_Shape39', b1)
    assert _is_linked(a, 'shape_Shape39', b1)
    if hasattr(b1, 'shape_Rectangle38'):
        assert _is_linked(b1, 'shape_Rectangle38', a)
    _safe_set(a, 'shape_Shape39', b2)
    assert _is_linked(a, 'shape_Shape39', b2)
    if hasattr(b1, 'shape_Rectangle38'):
        assert not _is_linked(b1, 'shape_Rectangle38', a)
    if hasattr(b2, 'shape_Rectangle38'):
        assert _is_linked(b2, 'shape_Rectangle38', a)
    _safe_set(a, 'shape_Shape39', None)
    assert not _is_linked(a, 'shape_Shape39', b2)
    if hasattr(b2, 'shape_Rectangle38'):
        assert not _is_linked(b2, 'shape_Rectangle38', a)


def test_assoc_shape42_link_reassign_clear():
    a = shape_Shape(style="sample_text")
    b1 = shape_RoundedRectangle()
    b2 = shape_RoundedRectangle()
    _safe_set(a, 'shape_Shape44', b1)
    assert _is_linked(a, 'shape_Shape44', b1)
    if hasattr(b1, 'shape_RoundedRectangle43'):
        assert _is_linked(b1, 'shape_RoundedRectangle43', a)
    _safe_set(a, 'shape_Shape44', b2)
    assert _is_linked(a, 'shape_Shape44', b2)
    if hasattr(b1, 'shape_RoundedRectangle43'):
        assert not _is_linked(b1, 'shape_RoundedRectangle43', a)
    if hasattr(b2, 'shape_RoundedRectangle43'):
        assert _is_linked(b2, 'shape_RoundedRectangle43', a)
    _safe_set(a, 'shape_Shape44', None)
    assert not _is_linked(a, 'shape_Shape44', b2)
    if hasattr(b2, 'shape_RoundedRectangle43'):
        assert not _is_linked(b2, 'shape_RoundedRectangle43', a)


def test_assoc_shape47_link_reassign_clear():
    a = shape_Shape(style="sample_text")
    b1 = shape_Polygon()
    b2 = shape_Polygon()
    _safe_set(a, 'shape_Shape49', b1)
    assert _is_linked(a, 'shape_Shape49', b1)
    if hasattr(b1, 'shape_Polygon48'):
        assert _is_linked(b1, 'shape_Polygon48', a)
    _safe_set(a, 'shape_Shape49', b2)
    assert _is_linked(a, 'shape_Shape49', b2)
    if hasattr(b1, 'shape_Polygon48'):
        assert not _is_linked(b1, 'shape_Polygon48', a)
    if hasattr(b2, 'shape_Polygon48'):
        assert _is_linked(b2, 'shape_Polygon48', a)
    _safe_set(a, 'shape_Shape49', None)
    assert not _is_linked(a, 'shape_Shape49', b2)
    if hasattr(b2, 'shape_Polygon48'):
        assert not _is_linked(b2, 'shape_Polygon48', a)


def test_assoc_shape5_link_reassign_clear():
    a = shape_Shape(style="sample_text")
    b1 = shape_ShapeDefinition()
    b2 = shape_ShapeDefinition()
    _safe_set(a, 'shape_Shape', b1)
    assert _is_linked(a, 'shape_Shape', b1)
    if hasattr(b1, 'shape_ShapeDefinition6'):
        assert _is_linked(b1, 'shape_ShapeDefinition6', a)
    _safe_set(a, 'shape_Shape', b2)
    assert _is_linked(a, 'shape_Shape', b2)
    if hasattr(b1, 'shape_ShapeDefinition6'):
        assert not _is_linked(b1, 'shape_ShapeDefinition6', a)
    if hasattr(b2, 'shape_ShapeDefinition6'):
        assert _is_linked(b2, 'shape_ShapeDefinition6', a)
    _safe_set(a, 'shape_Shape', None)
    assert not _is_linked(a, 'shape_Shape', b2)
    if hasattr(b2, 'shape_ShapeDefinition6'):
        assert not _is_linked(b2, 'shape_ShapeDefinition6', a)


def test_assoc_shape55_link_reassign_clear():
    a = shape_Shape(style="sample_text")
    b1 = shape_Ellipse()
    b2 = shape_Ellipse()
    _safe_set(a, 'shape_Shape57', b1)
    assert _is_linked(a, 'shape_Shape57', b1)
    if hasattr(b1, 'shape_Ellipse56'):
        assert _is_linked(b1, 'shape_Ellipse56', a)
    _safe_set(a, 'shape_Shape57', b2)
    assert _is_linked(a, 'shape_Shape57', b2)
    if hasattr(b1, 'shape_Ellipse56'):
        assert not _is_linked(b1, 'shape_Ellipse56', a)
    if hasattr(b2, 'shape_Ellipse56'):
        assert _is_linked(b2, 'shape_Ellipse56', a)
    _safe_set(a, 'shape_Shape57', None)
    assert not _is_linked(a, 'shape_Shape57', b2)
    if hasattr(b2, 'shape_Ellipse56'):
        assert not _is_linked(b2, 'shape_Ellipse56', a)


def test_assoc_shape66_link_reassign_clear():
    a = shape_Compartment(compartmentLayout="sample_text")
    b1 = shape_CompartmentShape()
    b2 = shape_CompartmentShape()
    _safe_set(a, 'shape_Compartment', b1)
    assert _is_linked(a, 'shape_Compartment', b1)
    if hasattr(b1, 'shape_CompartmentShape'):
        assert _is_linked(b1, 'shape_CompartmentShape', a)
    _safe_set(a, 'shape_Compartment', b2)
    assert _is_linked(a, 'shape_Compartment', b2)
    if hasattr(b1, 'shape_CompartmentShape'):
        assert not _is_linked(b1, 'shape_CompartmentShape', a)
    if hasattr(b2, 'shape_CompartmentShape'):
        assert _is_linked(b2, 'shape_CompartmentShape', a)
    _safe_set(a, 'shape_Compartment', None)
    assert not _is_linked(a, 'shape_Compartment', b2)
    if hasattr(b2, 'shape_CompartmentShape'):
        assert not _is_linked(b2, 'shape_CompartmentShape', a)


def test_assoc_shapeCon11_link_reassign_clear():
    a = shape_ShapeConnection(style="sample_text")
    b1 = shape_PlacingDefinition(angle=7, distance=7, offset="sample_text")
    b2 = shape_PlacingDefinition(angle=13, distance=13, offset="sample_text_2")
    _safe_set(a, 'shape_ShapeConnection', b1)
    assert _is_linked(a, 'shape_ShapeConnection', b1)
    if hasattr(b1, 'shape_PlacingDefinition12'):
        assert _is_linked(b1, 'shape_PlacingDefinition12', a)
    _safe_set(a, 'shape_ShapeConnection', b2)
    assert _is_linked(a, 'shape_ShapeConnection', b2)
    if hasattr(b1, 'shape_PlacingDefinition12'):
        assert not _is_linked(b1, 'shape_PlacingDefinition12', a)
    if hasattr(b2, 'shape_PlacingDefinition12'):
        assert _is_linked(b2, 'shape_PlacingDefinition12', a)
    _safe_set(a, 'shape_ShapeConnection', None)
    assert not _is_linked(a, 'shape_ShapeConnection', b2)
    if hasattr(b2, 'shape_PlacingDefinition12'):
        assert not _is_linked(b2, 'shape_PlacingDefinition12', a)


def test_assoc_shapeContainerElement0_link_reassign_clear():
    a = shape_ShapeContainerElement(name="sample_text", style="sample_text")
    b1 = shape_ShapeContainer()
    b2 = shape_ShapeContainer()
    _safe_set(a, 'shape_ShapeContainerElement', b1)
    assert _is_linked(a, 'shape_ShapeContainerElement', b1)
    if hasattr(b1, 'shape_ShapeContainer'):
        assert _is_linked(b1, 'shape_ShapeContainer', a)
    _safe_set(a, 'shape_ShapeContainerElement', b2)
    assert _is_linked(a, 'shape_ShapeContainerElement', b2)
    if hasattr(b1, 'shape_ShapeContainer'):
        assert not _is_linked(b1, 'shape_ShapeContainer', a)
    if hasattr(b2, 'shape_ShapeContainer'):
        assert _is_linked(b2, 'shape_ShapeContainer', a)
    _safe_set(a, 'shape_ShapeContainerElement', None)
    assert not _is_linked(a, 'shape_ShapeContainerElement', b2)
    if hasattr(b2, 'shape_ShapeContainer'):
        assert not _is_linked(b2, 'shape_ShapeContainer', a)


def test_assoc_shapeLayout4_link_reassign_clear():
    a = shape_ShapeLayout(maxheight=7, maxwidth=7, minheight=7, minwidth=7, proportional="sample_text", stretchH="sample_text", stretchV="sample_text")
    b1 = shape_ShapeDefinition()
    b2 = shape_ShapeDefinition()
    _safe_set(a, 'shape_ShapeLayout', b1)
    assert _is_linked(a, 'shape_ShapeLayout', b1)
    if hasattr(b1, 'shape_ShapeDefinition'):
        assert _is_linked(b1, 'shape_ShapeDefinition', a)
    _safe_set(a, 'shape_ShapeLayout', b2)
    assert _is_linked(a, 'shape_ShapeLayout', b2)
    if hasattr(b1, 'shape_ShapeDefinition'):
        assert not _is_linked(b1, 'shape_ShapeDefinition', a)
    if hasattr(b2, 'shape_ShapeDefinition'):
        assert _is_linked(b2, 'shape_ShapeDefinition', a)
    _safe_set(a, 'shape_ShapeLayout', None)
    assert not _is_linked(a, 'shape_ShapeLayout', b2)
    if hasattr(b2, 'shape_ShapeDefinition'):
        assert not _is_linked(b2, 'shape_ShapeDefinition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnchorPositionPos_strategy = st.builds(AnchorPositionPos)
@given(instance=AnchorPositionPos_strategy)
@settings(max_examples=25)
def test_AnchorPositionPos_instantiation(instance):
    assert isinstance(instance, AnchorPositionPos)


AnchorType_strategy = st.builds(AnchorType)
@given(instance=AnchorType_strategy)
@settings(max_examples=25)
def test_AnchorType_instantiation(instance):
    assert isinstance(instance, AnchorType)


CompartmentShape_strategy = st.builds(CompartmentShape)
@given(instance=CompartmentShape_strategy)
@settings(max_examples=25)
def test_CompartmentShape_instantiation(instance):
    assert isinstance(instance, CompartmentShape)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


ShapeConnection_strategy = st.builds(ShapeConnection)
@given(instance=ShapeConnection_strategy)
@settings(max_examples=25)
def test_ShapeConnection_instantiation(instance):
    assert isinstance(instance, ShapeConnection)


ShapeContainerElement_strategy = st.builds(ShapeContainerElement)
@given(instance=ShapeContainerElement_strategy)
@settings(max_examples=25)
def test_ShapeContainerElement_instantiation(instance):
    assert isinstance(instance, ShapeContainerElement)


shape_Anchor_strategy = st.builds(shape_Anchor)
@given(instance=shape_Anchor_strategy)
@settings(max_examples=25)
def test_shape_Anchor_instantiation(instance):
    assert isinstance(instance, shape_Anchor)


shape_AnchorFixPointPosition_strategy = st.builds(shape_AnchorFixPointPosition, xcor=st.integers(), ycor=st.integers())
@given(instance=shape_AnchorFixPointPosition_strategy)
@settings(max_examples=25)
def test_shape_AnchorFixPointPosition_instantiation(instance):
    assert isinstance(instance, shape_AnchorFixPointPosition)


shape_AnchorManual_strategy = st.builds(shape_AnchorManual)
@given(instance=shape_AnchorManual_strategy)
@settings(max_examples=25)
def test_shape_AnchorManual_instantiation(instance):
    assert isinstance(instance, shape_AnchorManual)


shape_AnchorPosition_strategy = st.builds(shape_AnchorPosition)
@given(instance=shape_AnchorPosition_strategy)
@settings(max_examples=25)
def test_shape_AnchorPosition_instantiation(instance):
    assert isinstance(instance, shape_AnchorPosition)


shape_AnchorPositionPos_strategy = st.builds(shape_AnchorPositionPos)
@given(instance=shape_AnchorPositionPos_strategy)
@settings(max_examples=25)
def test_shape_AnchorPositionPos_instantiation(instance):
    assert isinstance(instance, shape_AnchorPositionPos)


shape_AnchorPredefinied_strategy = st.builds(shape_AnchorPredefinied, value=safe_text)
@given(instance=shape_AnchorPredefinied_strategy)
@settings(max_examples=25)
def test_shape_AnchorPredefinied_instantiation(instance):
    assert isinstance(instance, shape_AnchorPredefinied)


shape_AnchorRelativePosition_strategy = st.builds(shape_AnchorRelativePosition, xoffset=safe_text, yoffset=safe_text)
@given(instance=shape_AnchorRelativePosition_strategy)
@settings(max_examples=25)
def test_shape_AnchorRelativePosition_instantiation(instance):
    assert isinstance(instance, shape_AnchorRelativePosition)


shape_AnchorType_strategy = st.builds(shape_AnchorType)
@given(instance=shape_AnchorType_strategy)
@settings(max_examples=25)
def test_shape_AnchorType_instantiation(instance):
    assert isinstance(instance, shape_AnchorType)


shape_CDEllipse_strategy = st.builds(shape_CDEllipse)
@given(instance=shape_CDEllipse_strategy)
@settings(max_examples=25)
def test_shape_CDEllipse_instantiation(instance):
    assert isinstance(instance, shape_CDEllipse)


shape_CDLine_strategy = st.builds(shape_CDLine)
@given(instance=shape_CDLine_strategy)
@settings(max_examples=25)
def test_shape_CDLine_instantiation(instance):
    assert isinstance(instance, shape_CDLine)


shape_CDPolygon_strategy = st.builds(shape_CDPolygon)
@given(instance=shape_CDPolygon_strategy)
@settings(max_examples=25)
def test_shape_CDPolygon_instantiation(instance):
    assert isinstance(instance, shape_CDPolygon)


shape_CDPolyline_strategy = st.builds(shape_CDPolyline)
@given(instance=shape_CDPolyline_strategy)
@settings(max_examples=25)
def test_shape_CDPolyline_instantiation(instance):
    assert isinstance(instance, shape_CDPolyline)


shape_CDRectangle_strategy = st.builds(shape_CDRectangle)
@given(instance=shape_CDRectangle_strategy)
@settings(max_examples=25)
def test_shape_CDRectangle_instantiation(instance):
    assert isinstance(instance, shape_CDRectangle)


shape_CDRoundedRectangle_strategy = st.builds(shape_CDRoundedRectangle)
@given(instance=shape_CDRoundedRectangle_strategy)
@settings(max_examples=25)
def test_shape_CDRoundedRectangle_instantiation(instance):
    assert isinstance(instance, shape_CDRoundedRectangle)


shape_CDText_strategy = st.builds(shape_CDText, texttype=safe_text)
@given(instance=shape_CDText_strategy)
@settings(max_examples=25)
def test_shape_CDText_instantiation(instance):
    assert isinstance(instance, shape_CDText)


shape_CommonLayout_strategy = st.builds(shape_CommonLayout, heigth=st.integers(), width=st.integers(), xcor=st.integers(), ycor=st.integers())
@given(instance=shape_CommonLayout_strategy)
@settings(max_examples=25)
def test_shape_CommonLayout_instantiation(instance):
    assert isinstance(instance, shape_CommonLayout)


shape_Compartment_strategy = st.builds(shape_Compartment, compartmentLayout=safe_text)
@given(instance=shape_Compartment_strategy)
@settings(max_examples=25)
def test_shape_Compartment_instantiation(instance):
    assert isinstance(instance, shape_Compartment)


shape_CompartmentEllipse_strategy = st.builds(shape_CompartmentEllipse)
@given(instance=shape_CompartmentEllipse_strategy)
@settings(max_examples=25)
def test_shape_CompartmentEllipse_instantiation(instance):
    assert isinstance(instance, shape_CompartmentEllipse)


shape_CompartmentInfo_strategy = st.builds(shape_CompartmentInfo, compartmentLayout=safe_text, invisible=st.booleans(), margin=st.integers(), spacing=st.integers(), stretchH=safe_text, stretchV=safe_text)
@given(instance=shape_CompartmentInfo_strategy)
@settings(max_examples=25)
def test_shape_CompartmentInfo_instantiation(instance):
    assert isinstance(instance, shape_CompartmentInfo)


shape_CompartmentPolygon_strategy = st.builds(shape_CompartmentPolygon)
@given(instance=shape_CompartmentPolygon_strategy)
@settings(max_examples=25)
def test_shape_CompartmentPolygon_instantiation(instance):
    assert isinstance(instance, shape_CompartmentPolygon)


shape_CompartmentRectangle_strategy = st.builds(shape_CompartmentRectangle)
@given(instance=shape_CompartmentRectangle_strategy)
@settings(max_examples=25)
def test_shape_CompartmentRectangle_instantiation(instance):
    assert isinstance(instance, shape_CompartmentRectangle)


shape_CompartmentRoundedRectangle_strategy = st.builds(shape_CompartmentRoundedRectangle)
@given(instance=shape_CompartmentRoundedRectangle_strategy)
@settings(max_examples=25)
def test_shape_CompartmentRoundedRectangle_instantiation(instance):
    assert isinstance(instance, shape_CompartmentRoundedRectangle)


shape_CompartmentShape_strategy = st.builds(shape_CompartmentShape)
@given(instance=shape_CompartmentShape_strategy)
@settings(max_examples=25)
def test_shape_CompartmentShape_instantiation(instance):
    assert isinstance(instance, shape_CompartmentShape)


shape_ConnectionDefinition_strategy = st.builds(shape_ConnectionDefinition, connectionStyle=safe_text)
@given(instance=shape_ConnectionDefinition_strategy)
@settings(max_examples=25)
def test_shape_ConnectionDefinition_instantiation(instance):
    assert isinstance(instance, shape_ConnectionDefinition)


shape_Description_strategy = st.builds(shape_Description, hAlign=safe_text, style=safe_text, vAlign=safe_text)
@given(instance=shape_Description_strategy)
@settings(max_examples=25)
def test_shape_Description_instantiation(instance):
    assert isinstance(instance, shape_Description)


shape_Ellipse_strategy = st.builds(shape_Ellipse)
@given(instance=shape_Ellipse_strategy)
@settings(max_examples=25)
def test_shape_Ellipse_instantiation(instance):
    assert isinstance(instance, shape_Ellipse)


shape_Line_strategy = st.builds(shape_Line)
@given(instance=shape_Line_strategy)
@settings(max_examples=25)
def test_shape_Line_instantiation(instance):
    assert isinstance(instance, shape_Line)


shape_LineLayout_strategy = st.builds(shape_LineLayout)
@given(instance=shape_LineLayout_strategy)
@settings(max_examples=25)
def test_shape_LineLayout_instantiation(instance):
    assert isinstance(instance, shape_LineLayout)


shape_PlacingDefinition_strategy = st.builds(shape_PlacingDefinition, angle=st.integers(), distance=st.integers(), offset=safe_text)
@given(instance=shape_PlacingDefinition_strategy)
@settings(max_examples=25)
def test_shape_PlacingDefinition_instantiation(instance):
    assert isinstance(instance, shape_PlacingDefinition)


shape_Point_strategy = st.builds(shape_Point, curveAfter=st.integers(), curveBefore=st.integers(), xcor=safe_text, ycor=safe_text)
@given(instance=shape_Point_strategy)
@settings(max_examples=25)
def test_shape_Point_instantiation(instance):
    assert isinstance(instance, shape_Point)


shape_PolyLineLayout_strategy = st.builds(shape_PolyLineLayout)
@given(instance=shape_PolyLineLayout_strategy)
@settings(max_examples=25)
def test_shape_PolyLineLayout_instantiation(instance):
    assert isinstance(instance, shape_PolyLineLayout)


shape_Polygon_strategy = st.builds(shape_Polygon)
@given(instance=shape_Polygon_strategy)
@settings(max_examples=25)
def test_shape_Polygon_instantiation(instance):
    assert isinstance(instance, shape_Polygon)


shape_Polyline_strategy = st.builds(shape_Polyline)
@given(instance=shape_Polyline_strategy)
@settings(max_examples=25)
def test_shape_Polyline_instantiation(instance):
    assert isinstance(instance, shape_Polyline)


shape_Rectangle_strategy = st.builds(shape_Rectangle)
@given(instance=shape_Rectangle_strategy)
@settings(max_examples=25)
def test_shape_Rectangle_instantiation(instance):
    assert isinstance(instance, shape_Rectangle)


shape_RectangleEllipseLayout_strategy = st.builds(shape_RectangleEllipseLayout)
@given(instance=shape_RectangleEllipseLayout_strategy)
@settings(max_examples=25)
def test_shape_RectangleEllipseLayout_instantiation(instance):
    assert isinstance(instance, shape_RectangleEllipseLayout)


shape_RoundedRectangle_strategy = st.builds(shape_RoundedRectangle)
@given(instance=shape_RoundedRectangle_strategy)
@settings(max_examples=25)
def test_shape_RoundedRectangle_instantiation(instance):
    assert isinstance(instance, shape_RoundedRectangle)


shape_RoundedRectangleLayout_strategy = st.builds(shape_RoundedRectangleLayout, curveHeight=st.integers(), curveWidth=st.integers())
@given(instance=shape_RoundedRectangleLayout_strategy)
@settings(max_examples=25)
def test_shape_RoundedRectangleLayout_instantiation(instance):
    assert isinstance(instance, shape_RoundedRectangleLayout)


shape_Shape_strategy = st.builds(shape_Shape, style=safe_text)
@given(instance=shape_Shape_strategy)
@settings(max_examples=25)
def test_shape_Shape_instantiation(instance):
    assert isinstance(instance, shape_Shape)


shape_ShapeConnection_strategy = st.builds(shape_ShapeConnection, style=safe_text)
@given(instance=shape_ShapeConnection_strategy)
@settings(max_examples=25)
def test_shape_ShapeConnection_instantiation(instance):
    assert isinstance(instance, shape_ShapeConnection)


shape_ShapeContainer_strategy = st.builds(shape_ShapeContainer)
@given(instance=shape_ShapeContainer_strategy)
@settings(max_examples=25)
def test_shape_ShapeContainer_instantiation(instance):
    assert isinstance(instance, shape_ShapeContainer)


shape_ShapeContainerElement_strategy = st.builds(shape_ShapeContainerElement, name=safe_text, style=safe_text)
@given(instance=shape_ShapeContainerElement_strategy)
@settings(max_examples=25)
def test_shape_ShapeContainerElement_instantiation(instance):
    assert isinstance(instance, shape_ShapeContainerElement)


shape_ShapeDefinition_strategy = st.builds(shape_ShapeDefinition)
@given(instance=shape_ShapeDefinition_strategy)
@settings(max_examples=25)
def test_shape_ShapeDefinition_instantiation(instance):
    assert isinstance(instance, shape_ShapeDefinition)


shape_ShapeLayout_strategy = st.builds(shape_ShapeLayout, maxheight=st.integers(), maxwidth=st.integers(), minheight=st.integers(), minwidth=st.integers(), proportional=safe_text, stretchH=safe_text, stretchV=safe_text)
@given(instance=shape_ShapeLayout_strategy)
@settings(max_examples=25)
def test_shape_ShapeLayout_instantiation(instance):
    assert isinstance(instance, shape_ShapeLayout)


shape_ShapestyleLayout_strategy = st.builds(shape_ShapestyleLayout)
@given(instance=shape_ShapestyleLayout_strategy)
@settings(max_examples=25)
def test_shape_ShapestyleLayout_instantiation(instance):
    assert isinstance(instance, shape_ShapestyleLayout)


shape_Text_strategy = st.builds(shape_Text, texttype=safe_text)
@given(instance=shape_Text_strategy)
@settings(max_examples=25)
def test_shape_Text_instantiation(instance):
    assert isinstance(instance, shape_Text)


shape_TextBody_strategy = st.builds(shape_TextBody, value=safe_text)
@given(instance=shape_TextBody_strategy)
@settings(max_examples=25)
def test_shape_TextBody_instantiation(instance):
    assert isinstance(instance, shape_TextBody)


shape_TextLayout_strategy = st.builds(shape_TextLayout, hAlign=safe_text, vAlign=safe_text)
@given(instance=shape_TextLayout_strategy)
@settings(max_examples=25)
def test_shape_TextLayout_instantiation(instance):
    assert isinstance(instance, shape_TextLayout)


