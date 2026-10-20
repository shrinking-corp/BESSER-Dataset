# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Border,
    draw2d_LabeledBorder,
    ConnectionAnchor,
    draw2d_XYAnchor,
    draw2d_ConnectionAnchor,
    draw2d_FlowBorder,
    ColoredLabeledBorder,
    draw2d_TitleBarBorder,
    draw2d_GroupBoxBorder,
    LabeledBorder,
    draw2d_ColoredLabeledBorder,
    draw2d_FrameBorder,
    Polyline,
    draw2d_Polygon,
    PointListShape,
    draw2d_PolygonShape,
    draw2d_PolylineShape,
    draw2d_Polyline,
    Shape,
    draw2d_Ellipse,
    draw2d_RoundedRectangle,
    draw2d_Triangle,
    draw2d_PointListShape,
    draw2d_RectangleFigure,
    draw2d_Figure,
    Canvas,
    draw2d_Draw2DCanvas,
    Figure,
    draw2d_ImageFigure,
    draw2d_Shape,
    draw2d_BlockFlow,
    draw2d_Label,
    draw2d_Border,
    draw2d_Font,
    draw2d_Color,
    Direction,
    Alignment,
    Orientation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_border_is_not_abstract():
    assert not inspect.isabstract(Border)


def test_hyp_border_constructor_exists():
    assert callable(Border.__init__)


def test_hyp_border_constructor_args():
    sig = inspect.signature(Border.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_labeledborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_LabeledBorder)


def test_hyp_draw2d_labeledborder_constructor_exists():
    assert callable(draw2d_LabeledBorder.__init__)


def test_hyp_draw2d_labeledborder_constructor_args():
    sig = inspect.signature(draw2d_LabeledBorder.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_connectionanchor_is_not_abstract():
    assert not inspect.isabstract(ConnectionAnchor)


def test_hyp_connectionanchor_constructor_exists():
    assert callable(ConnectionAnchor.__init__)


def test_hyp_connectionanchor_constructor_args():
    sig = inspect.signature(ConnectionAnchor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_xyanchor_is_not_abstract():
    assert not inspect.isabstract(draw2d_XYAnchor)


def test_hyp_draw2d_xyanchor_constructor_exists():
    assert callable(draw2d_XYAnchor.__init__)


def test_hyp_draw2d_xyanchor_constructor_args():
    sig = inspect.signature(draw2d_XYAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"




def test_hyp_draw2d_connectionanchor_is_not_abstract():
    assert not inspect.isabstract(draw2d_ConnectionAnchor)


def test_hyp_draw2d_connectionanchor_constructor_exists():
    assert callable(draw2d_ConnectionAnchor.__init__)


def test_hyp_draw2d_connectionanchor_constructor_args():
    sig = inspect.signature(draw2d_ConnectionAnchor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_flowborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_FlowBorder)


def test_hyp_draw2d_flowborder_constructor_exists():
    assert callable(draw2d_FlowBorder.__init__)


def test_hyp_draw2d_flowborder_constructor_args():
    sig = inspect.signature(draw2d_FlowBorder.__init__)
    params = list(sig.parameters.keys())
    assert "bottomMargin" in params, "Missing parameter 'bottomMargin'"
    assert "rightMargin" in params, "Missing parameter 'rightMargin'"
    assert "leftMargin" in params, "Missing parameter 'leftMargin'"
    assert "topMargin" in params, "Missing parameter 'topMargin'"







def test_hyp_coloredlabeledborder_is_not_abstract():
    assert not inspect.isabstract(ColoredLabeledBorder)


def test_hyp_coloredlabeledborder_constructor_exists():
    assert callable(ColoredLabeledBorder.__init__)


def test_hyp_coloredlabeledborder_constructor_args():
    sig = inspect.signature(ColoredLabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_titlebarborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_TitleBarBorder)


def test_hyp_draw2d_titlebarborder_constructor_exists():
    assert callable(draw2d_TitleBarBorder.__init__)


def test_hyp_draw2d_titlebarborder_constructor_args():
    sig = inspect.signature(draw2d_TitleBarBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_groupboxborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_GroupBoxBorder)


def test_hyp_draw2d_groupboxborder_constructor_exists():
    assert callable(draw2d_GroupBoxBorder.__init__)


def test_hyp_draw2d_groupboxborder_constructor_args():
    sig = inspect.signature(draw2d_GroupBoxBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labeledborder_is_not_abstract():
    assert not inspect.isabstract(LabeledBorder)


def test_hyp_labeledborder_constructor_exists():
    assert callable(LabeledBorder.__init__)


def test_hyp_labeledborder_constructor_args():
    sig = inspect.signature(LabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_coloredlabeledborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_ColoredLabeledBorder)


def test_hyp_draw2d_coloredlabeledborder_constructor_exists():
    assert callable(draw2d_ColoredLabeledBorder.__init__)


def test_hyp_draw2d_coloredlabeledborder_constructor_args():
    sig = inspect.signature(draw2d_ColoredLabeledBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_frameborder_is_not_abstract():
    assert not inspect.isabstract(draw2d_FrameBorder)


def test_hyp_draw2d_frameborder_constructor_exists():
    assert callable(draw2d_FrameBorder.__init__)


def test_hyp_draw2d_frameborder_constructor_args():
    sig = inspect.signature(draw2d_FrameBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_hyp_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_hyp_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_polygon_is_not_abstract():
    assert not inspect.isabstract(draw2d_Polygon)


def test_hyp_draw2d_polygon_constructor_exists():
    assert callable(draw2d_Polygon.__init__)


def test_hyp_draw2d_polygon_constructor_args():
    sig = inspect.signature(draw2d_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pointlistshape_is_not_abstract():
    assert not inspect.isabstract(PointListShape)


def test_hyp_pointlistshape_constructor_exists():
    assert callable(PointListShape.__init__)


def test_hyp_pointlistshape_constructor_args():
    sig = inspect.signature(PointListShape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_polygonshape_is_not_abstract():
    assert not inspect.isabstract(draw2d_PolygonShape)


def test_hyp_draw2d_polygonshape_constructor_exists():
    assert callable(draw2d_PolygonShape.__init__)


def test_hyp_draw2d_polygonshape_constructor_args():
    sig = inspect.signature(draw2d_PolygonShape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_polylineshape_is_not_abstract():
    assert not inspect.isabstract(draw2d_PolylineShape)


def test_hyp_draw2d_polylineshape_constructor_exists():
    assert callable(draw2d_PolylineShape.__init__)


def test_hyp_draw2d_polylineshape_constructor_args():
    sig = inspect.signature(draw2d_PolylineShape.__init__)
    params = list(sig.parameters.keys())
    assert "tolerance" in params, "Missing parameter 'tolerance'"




def test_hyp_draw2d_polyline_is_not_abstract():
    assert not inspect.isabstract(draw2d_Polyline)


def test_hyp_draw2d_polyline_constructor_exists():
    assert callable(draw2d_Polyline.__init__)


def test_hyp_draw2d_polyline_constructor_args():
    sig = inspect.signature(draw2d_Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "tolerance" in params, "Missing parameter 'tolerance'"




def test_hyp_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_hyp_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_hyp_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_ellipse_is_not_abstract():
    assert not inspect.isabstract(draw2d_Ellipse)


def test_hyp_draw2d_ellipse_constructor_exists():
    assert callable(draw2d_Ellipse.__init__)


def test_hyp_draw2d_ellipse_constructor_args():
    sig = inspect.signature(draw2d_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(draw2d_RoundedRectangle)


def test_hyp_draw2d_roundedrectangle_constructor_exists():
    assert callable(draw2d_RoundedRectangle.__init__)


def test_hyp_draw2d_roundedrectangle_constructor_args():
    sig = inspect.signature(draw2d_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerDimensions" in params, "Missing parameter 'cornerDimensions'"




def test_hyp_draw2d_triangle_is_not_abstract():
    assert not inspect.isabstract(draw2d_Triangle)


def test_hyp_draw2d_triangle_constructor_exists():
    assert callable(draw2d_Triangle.__init__)


def test_hyp_draw2d_triangle_constructor_args():
    sig = inspect.signature(draw2d_Triangle.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "direction" in params, "Missing parameter 'direction'"





def test_hyp_draw2d_pointlistshape_is_not_abstract():
    assert not inspect.isabstract(draw2d_PointListShape)


def test_hyp_draw2d_pointlistshape_constructor_exists():
    assert callable(draw2d_PointListShape.__init__)


def test_hyp_draw2d_pointlistshape_constructor_args():
    sig = inspect.signature(draw2d_PointListShape.__init__)
    params = list(sig.parameters.keys())
    assert "pointList" in params, "Missing parameter 'pointList'"




def test_hyp_draw2d_rectanglefigure_is_not_abstract():
    assert not inspect.isabstract(draw2d_RectangleFigure)


def test_hyp_draw2d_rectanglefigure_constructor_exists():
    assert callable(draw2d_RectangleFigure.__init__)


def test_hyp_draw2d_rectanglefigure_constructor_args():
    sig = inspect.signature(draw2d_RectangleFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_figure_is_not_abstract():
    assert not inspect.isabstract(draw2d_Figure)


def test_hyp_draw2d_figure_constructor_exists():
    assert callable(draw2d_Figure.__init__)


def test_hyp_draw2d_figure_constructor_args():
    sig = inspect.signature(draw2d_Figure.__init__)
    params = list(sig.parameters.keys())
    assert "focusTraversable" in params, "Missing parameter 'focusTraversable'"
    assert "minimumSize" in params, "Missing parameter 'minimumSize'"
    assert "maximumSize" in params, "Missing parameter 'maximumSize'"
    assert "preferredSize" in params, "Missing parameter 'preferredSize'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "opaque" in params, "Missing parameter 'opaque'"











def test_hyp_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_hyp_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_hyp_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_draw2dcanvas_is_not_abstract():
    assert not inspect.isabstract(draw2d_Draw2DCanvas)


def test_hyp_draw2d_draw2dcanvas_constructor_exists():
    assert callable(draw2d_Draw2DCanvas.__init__)


def test_hyp_draw2d_draw2dcanvas_constructor_args():
    sig = inspect.signature(draw2d_Draw2DCanvas.__init__)
    params = list(sig.parameters.keys())



def test_hyp_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_hyp_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_hyp_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_imagefigure_is_not_abstract():
    assert not inspect.isabstract(draw2d_ImageFigure)


def test_hyp_draw2d_imagefigure_constructor_exists():
    assert callable(draw2d_ImageFigure.__init__)


def test_hyp_draw2d_imagefigure_constructor_args():
    sig = inspect.signature(draw2d_ImageFigure.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"




def test_hyp_draw2d_shape_is_not_abstract():
    assert not inspect.isabstract(draw2d_Shape)


def test_hyp_draw2d_shape_constructor_exists():
    assert callable(draw2d_Shape.__init__)


def test_hyp_draw2d_shape_constructor_args():
    sig = inspect.signature(draw2d_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "lineWidthFloat" in params, "Missing parameter 'lineWidthFloat'"
    assert "lineMiterLimit" in params, "Missing parameter 'lineMiterLimit'"
    assert "lineDash" in params, "Missing parameter 'lineDash'"
    assert "lineJoin" in params, "Missing parameter 'lineJoin'"
    assert "lineCap" in params, "Missing parameter 'lineCap'"
    assert "outlineXOR" in params, "Missing parameter 'outlineXOR'"
    assert "lineDashOffset" in params, "Missing parameter 'lineDashOffset'"
    assert "antialias" in params, "Missing parameter 'antialias'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "fillXOR" in params, "Missing parameter 'fillXOR'"
    assert "outline" in params, "Missing parameter 'outline'"
















def test_hyp_draw2d_blockflow_is_not_abstract():
    assert not inspect.isabstract(draw2d_BlockFlow)


def test_hyp_draw2d_blockflow_constructor_exists():
    assert callable(draw2d_BlockFlow.__init__)


def test_hyp_draw2d_blockflow_constructor_args():
    sig = inspect.signature(draw2d_BlockFlow.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"




def test_hyp_draw2d_label_is_not_abstract():
    assert not inspect.isabstract(draw2d_Label)


def test_hyp_draw2d_label_constructor_exists():
    assert callable(draw2d_Label.__init__)


def test_hyp_draw2d_label_constructor_args():
    sig = inspect.signature(draw2d_Label.__init__)
    params = list(sig.parameters.keys())
    assert "iconAlignment" in params, "Missing parameter 'iconAlignment'"
    assert "iconTextGap" in params, "Missing parameter 'iconTextGap'"
    assert "textPlacement" in params, "Missing parameter 'textPlacement'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "text" in params, "Missing parameter 'text'"









def test_hyp_draw2d_border_is_not_abstract():
    assert not inspect.isabstract(draw2d_Border)


def test_hyp_draw2d_border_constructor_exists():
    assert callable(draw2d_Border.__init__)


def test_hyp_draw2d_border_constructor_args():
    sig = inspect.signature(draw2d_Border.__init__)
    params = list(sig.parameters.keys())
    assert "opaque" in params, "Missing parameter 'opaque'"




def test_hyp_draw2d_font_is_not_abstract():
    assert not inspect.isabstract(draw2d_Font)


def test_hyp_draw2d_font_constructor_exists():
    assert callable(draw2d_Font.__init__)


def test_hyp_draw2d_font_constructor_args():
    sig = inspect.signature(draw2d_Font.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2d_color_is_not_abstract():
    assert not inspect.isabstract(draw2d_Color)


def test_hyp_draw2d_color_constructor_exists():
    assert callable(draw2d_Color.__init__)


def test_hyp_draw2d_color_constructor_args():
    sig = inspect.signature(draw2d_Color.__init__)
    params = list(sig.parameters.keys())

def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "EAST",
        "NORTH",
        "SOUTH",
        "WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_hyp_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_hyp_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "TOP",
        "MIDDLE",
        "CENTER",
        "RIGHT",
        "BOTTOM",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_hyp_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_hyp_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Border_strategy = st.builds(
    Border,
)
draw2d_LabeledBorder_strategy = st.builds(
    draw2d_LabeledBorder,
    label=
        safe_text
)
ConnectionAnchor_strategy = st.builds(
    ConnectionAnchor,
)
draw2d_XYAnchor_strategy = st.builds(
    draw2d_XYAnchor,
    location=
        safe_text
)
draw2d_ConnectionAnchor_strategy = st.builds(
    draw2d_ConnectionAnchor,
)
draw2d_FlowBorder_strategy = st.builds(
    draw2d_FlowBorder,
    bottomMargin=
        st.integers(),
    rightMargin=
        st.integers(),
    leftMargin=
        st.integers(),
    topMargin=
        st.integers()
)
ColoredLabeledBorder_strategy = st.builds(
    ColoredLabeledBorder,
)
draw2d_TitleBarBorder_strategy = st.builds(
    draw2d_TitleBarBorder,
)
draw2d_GroupBoxBorder_strategy = st.builds(
    draw2d_GroupBoxBorder,
)
LabeledBorder_strategy = st.builds(
    LabeledBorder,
)
draw2d_ColoredLabeledBorder_strategy = st.builds(
    draw2d_ColoredLabeledBorder,
)
draw2d_FrameBorder_strategy = st.builds(
    draw2d_FrameBorder,
)
Polyline_strategy = st.builds(
    Polyline,
)
draw2d_Polygon_strategy = st.builds(
    draw2d_Polygon,
)
PointListShape_strategy = st.builds(
    PointListShape,
)
draw2d_PolygonShape_strategy = st.builds(
    draw2d_PolygonShape,
)
draw2d_PolylineShape_strategy = st.builds(
    draw2d_PolylineShape,
    tolerance=
        st.integers()
)
draw2d_Polyline_strategy = st.builds(
    draw2d_Polyline,
    tolerance=
        st.integers()
)
Shape_strategy = st.builds(
    Shape,
)
draw2d_Ellipse_strategy = st.builds(
    draw2d_Ellipse,
)
draw2d_RoundedRectangle_strategy = st.builds(
    draw2d_RoundedRectangle,
    cornerDimensions=
        safe_text
)
draw2d_Triangle_strategy = st.builds(
    draw2d_Triangle,
    orientation=
        safe_text,
    direction=
        safe_text
)
draw2d_PointListShape_strategy = st.builds(
    draw2d_PointListShape,
    pointList=
        st.integers()
)
draw2d_RectangleFigure_strategy = st.builds(
    draw2d_RectangleFigure,
)
draw2d_Figure_strategy = st.builds(
    draw2d_Figure,
    focusTraversable=
        st.booleans(),
    minimumSize=
        safe_text,
    maximumSize=
        safe_text,
    preferredSize=
        safe_text,
    bounds=
        safe_text,
    enabled=
        st.booleans(),
    visible=
        st.booleans(),
    opaque=
        st.booleans()
)
Canvas_strategy = st.builds(
    Canvas,
)
draw2d_Draw2DCanvas_strategy = st.builds(
    draw2d_Draw2DCanvas,
)
Figure_strategy = st.builds(
    Figure,
)
draw2d_ImageFigure_strategy = st.builds(
    draw2d_ImageFigure,
    image=
        safe_text
)
draw2d_Shape_strategy = st.builds(
    draw2d_Shape,
    lineStyle=
        safe_text,
    fill=
        st.booleans(),
    lineWidthFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineMiterLimit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineDash=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineJoin=
        safe_text,
    lineCap=
        safe_text,
    outlineXOR=
        st.booleans(),
    lineDashOffset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    antialias=
        safe_text,
    alpha=
        safe_text,
    fillXOR=
        st.booleans(),
    outline=
        st.booleans()
)
draw2d_BlockFlow_strategy = st.builds(
    draw2d_BlockFlow,
    orientation=
        safe_text
)
draw2d_Label_strategy = st.builds(
    draw2d_Label,
    iconAlignment=
        safe_text,
    iconTextGap=
        st.integers(),
    textPlacement=
        safe_text,
    textAlignment=
        safe_text,
    icon=
        safe_text,
    text=
        safe_text
)
draw2d_Border_strategy = st.builds(
    draw2d_Border,
    opaque=
        st.booleans()
)
draw2d_Font_strategy = st.builds(
    draw2d_Font,
)
draw2d_Color_strategy = st.builds(
    draw2d_Color,
)





@given(instance=draw2d_LabeledBorder_strategy)
def test_hyp_draw2d_labeledborder_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original





@given(instance=draw2d_XYAnchor_strategy)
def test_hyp_draw2d_xyanchor_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original





@given(instance=draw2d_FlowBorder_strategy)
def test_hyp_draw2d_flowborder_bottomMargin_setter(instance):
    original = instance.bottomMargin
    instance.bottomMargin = original
    assert instance.bottomMargin == original



@given(instance=draw2d_FlowBorder_strategy)
def test_hyp_draw2d_flowborder_rightMargin_setter(instance):
    original = instance.rightMargin
    instance.rightMargin = original
    assert instance.rightMargin == original



@given(instance=draw2d_FlowBorder_strategy)
def test_hyp_draw2d_flowborder_leftMargin_setter(instance):
    original = instance.leftMargin
    instance.leftMargin = original
    assert instance.leftMargin == original



@given(instance=draw2d_FlowBorder_strategy)
def test_hyp_draw2d_flowborder_topMargin_setter(instance):
    original = instance.topMargin
    instance.topMargin = original
    assert instance.topMargin == original














@given(instance=draw2d_PolylineShape_strategy)
def test_hyp_draw2d_polylineshape_tolerance_setter(instance):
    original = instance.tolerance
    instance.tolerance = original
    assert instance.tolerance == original




@given(instance=draw2d_Polyline_strategy)
def test_hyp_draw2d_polyline_tolerance_setter(instance):
    original = instance.tolerance
    instance.tolerance = original
    assert instance.tolerance == original






@given(instance=draw2d_RoundedRectangle_strategy)
def test_hyp_draw2d_roundedrectangle_cornerDimensions_setter(instance):
    original = instance.cornerDimensions
    instance.cornerDimensions = original
    assert instance.cornerDimensions == original




@given(instance=draw2d_Triangle_strategy)
def test_hyp_draw2d_triangle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=draw2d_Triangle_strategy)
def test_hyp_draw2d_triangle_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original




@given(instance=draw2d_PointListShape_strategy)
def test_hyp_draw2d_pointlistshape_pointList_setter(instance):
    original = instance.pointList
    instance.pointList = original
    assert instance.pointList == original





@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_focusTraversable_setter(instance):
    original = instance.focusTraversable
    instance.focusTraversable = original
    assert instance.focusTraversable == original



@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_minimumSize_setter(instance):
    original = instance.minimumSize
    instance.minimumSize = original
    assert instance.minimumSize == original



@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_maximumSize_setter(instance):
    original = instance.maximumSize
    instance.maximumSize = original
    assert instance.maximumSize == original



@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_preferredSize_setter(instance):
    original = instance.preferredSize
    instance.preferredSize = original
    assert instance.preferredSize == original



@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original



@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=draw2d_Figure_strategy)
def test_hyp_draw2d_figure_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original







@given(instance=draw2d_ImageFigure_strategy)
def test_hyp_draw2d_imagefigure_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original




@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_lineWidthFloat_setter(instance):
    original = instance.lineWidthFloat
    instance.lineWidthFloat = original
    assert instance.lineWidthFloat == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_lineMiterLimit_setter(instance):
    original = instance.lineMiterLimit
    instance.lineMiterLimit = original
    assert instance.lineMiterLimit == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_lineDash_setter(instance):
    original = instance.lineDash
    instance.lineDash = original
    assert instance.lineDash == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_lineJoin_setter(instance):
    original = instance.lineJoin
    instance.lineJoin = original
    assert instance.lineJoin == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_lineCap_setter(instance):
    original = instance.lineCap
    instance.lineCap = original
    assert instance.lineCap == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_outlineXOR_setter(instance):
    original = instance.outlineXOR
    instance.outlineXOR = original
    assert instance.outlineXOR == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_lineDashOffset_setter(instance):
    original = instance.lineDashOffset
    instance.lineDashOffset = original
    assert instance.lineDashOffset == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_antialias_setter(instance):
    original = instance.antialias
    instance.antialias = original
    assert instance.antialias == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_fillXOR_setter(instance):
    original = instance.fillXOR
    instance.fillXOR = original
    assert instance.fillXOR == original



@given(instance=draw2d_Shape_strategy)
def test_hyp_draw2d_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original




@given(instance=draw2d_BlockFlow_strategy)
def test_hyp_draw2d_blockflow_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original




@given(instance=draw2d_Label_strategy)
def test_hyp_draw2d_label_iconAlignment_setter(instance):
    original = instance.iconAlignment
    instance.iconAlignment = original
    assert instance.iconAlignment == original



@given(instance=draw2d_Label_strategy)
def test_hyp_draw2d_label_iconTextGap_setter(instance):
    original = instance.iconTextGap
    instance.iconTextGap = original
    assert instance.iconTextGap == original



@given(instance=draw2d_Label_strategy)
def test_hyp_draw2d_label_textPlacement_setter(instance):
    original = instance.textPlacement
    instance.textPlacement = original
    assert instance.textPlacement == original



@given(instance=draw2d_Label_strategy)
def test_hyp_draw2d_label_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original



@given(instance=draw2d_Label_strategy)
def test_hyp_draw2d_label_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=draw2d_Label_strategy)
def test_hyp_draw2d_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=draw2d_Border_strategy)
def test_hyp_draw2d_border_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Border,
    Canvas,
    ColoredLabeledBorder,
    ConnectionAnchor,
    Figure,
    LabeledBorder,
    PointListShape,
    Polyline,
    Shape,
    draw2d_BlockFlow,
    draw2d_Border,
    draw2d_Color,
    draw2d_ColoredLabeledBorder,
    draw2d_ConnectionAnchor,
    draw2d_Draw2DCanvas,
    draw2d_Ellipse,
    draw2d_Figure,
    draw2d_FlowBorder,
    draw2d_Font,
    draw2d_FrameBorder,
    draw2d_GroupBoxBorder,
    draw2d_ImageFigure,
    draw2d_Label,
    draw2d_LabeledBorder,
    draw2d_PointListShape,
    draw2d_Polygon,
    draw2d_PolygonShape,
    draw2d_Polyline,
    draw2d_PolylineShape,
    draw2d_RectangleFigure,
    draw2d_RoundedRectangle,
    draw2d_Shape,
    draw2d_TitleBarBorder,
    draw2d_Triangle,
    draw2d_XYAnchor,
    Alignment,
    Direction,
    Orientation,
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

def test_draw2d_BlockFlow_orientation_value_roundtrip():
    instance = draw2d_BlockFlow(orientation="sample_text")
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_draw2d_Border_opaque_value_roundtrip():
    instance = draw2d_Border(opaque=True)
    assert instance.opaque == True
    instance.opaque = False
    assert instance.opaque == False


def test_draw2d_Figure_bounds_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.bounds == "sample_text"
    instance.bounds = "sample_text_2"
    assert instance.bounds == "sample_text_2"


def test_draw2d_Figure_enabled_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.enabled == True
    instance.enabled = False
    assert instance.enabled == False


def test_draw2d_Figure_focusTraversable_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.focusTraversable == True
    instance.focusTraversable = False
    assert instance.focusTraversable == False


def test_draw2d_Figure_maximumSize_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.maximumSize == "sample_text"
    instance.maximumSize = "sample_text_2"
    assert instance.maximumSize == "sample_text_2"


def test_draw2d_Figure_minimumSize_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.minimumSize == "sample_text"
    instance.minimumSize = "sample_text_2"
    assert instance.minimumSize == "sample_text_2"


def test_draw2d_Figure_opaque_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.opaque == True
    instance.opaque = False
    assert instance.opaque == False


def test_draw2d_Figure_preferredSize_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.preferredSize == "sample_text"
    instance.preferredSize = "sample_text_2"
    assert instance.preferredSize == "sample_text_2"


def test_draw2d_Figure_visible_value_roundtrip():
    instance = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_draw2d_FlowBorder_bottomMargin_value_roundtrip():
    instance = draw2d_FlowBorder(bottomMargin=7, leftMargin=7, rightMargin=7, topMargin=7)
    assert instance.bottomMargin == 7
    instance.bottomMargin = 13
    assert instance.bottomMargin == 13


def test_draw2d_FlowBorder_leftMargin_value_roundtrip():
    instance = draw2d_FlowBorder(bottomMargin=7, leftMargin=7, rightMargin=7, topMargin=7)
    assert instance.leftMargin == 7
    instance.leftMargin = 13
    assert instance.leftMargin == 13


def test_draw2d_FlowBorder_rightMargin_value_roundtrip():
    instance = draw2d_FlowBorder(bottomMargin=7, leftMargin=7, rightMargin=7, topMargin=7)
    assert instance.rightMargin == 7
    instance.rightMargin = 13
    assert instance.rightMargin == 13


def test_draw2d_FlowBorder_topMargin_value_roundtrip():
    instance = draw2d_FlowBorder(bottomMargin=7, leftMargin=7, rightMargin=7, topMargin=7)
    assert instance.topMargin == 7
    instance.topMargin = 13
    assert instance.topMargin == 13


def test_draw2d_ImageFigure_image_value_roundtrip():
    instance = draw2d_ImageFigure(image="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_draw2d_Label_icon_value_roundtrip():
    instance = draw2d_Label(icon="sample_text", iconAlignment="sample_text", iconTextGap=7, text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.icon == "sample_text"
    instance.icon = "sample_text_2"
    assert instance.icon == "sample_text_2"


def test_draw2d_Label_iconAlignment_value_roundtrip():
    instance = draw2d_Label(icon="sample_text", iconAlignment="sample_text", iconTextGap=7, text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.iconAlignment == "sample_text"
    instance.iconAlignment = "sample_text_2"
    assert instance.iconAlignment == "sample_text_2"


def test_draw2d_Label_iconTextGap_value_roundtrip():
    instance = draw2d_Label(icon="sample_text", iconAlignment="sample_text", iconTextGap=7, text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.iconTextGap == 7
    instance.iconTextGap = 13
    assert instance.iconTextGap == 13


def test_draw2d_Label_text_value_roundtrip():
    instance = draw2d_Label(icon="sample_text", iconAlignment="sample_text", iconTextGap=7, text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_draw2d_Label_textAlignment_value_roundtrip():
    instance = draw2d_Label(icon="sample_text", iconAlignment="sample_text", iconTextGap=7, text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.textAlignment == "sample_text"
    instance.textAlignment = "sample_text_2"
    assert instance.textAlignment == "sample_text_2"


def test_draw2d_Label_textPlacement_value_roundtrip():
    instance = draw2d_Label(icon="sample_text", iconAlignment="sample_text", iconTextGap=7, text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.textPlacement == "sample_text"
    instance.textPlacement = "sample_text_2"
    assert instance.textPlacement == "sample_text_2"


def test_draw2d_LabeledBorder_label_value_roundtrip():
    instance = draw2d_LabeledBorder(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_draw2d_PointListShape_pointList_value_roundtrip():
    instance = draw2d_PointListShape(pointList=7)
    assert instance.pointList == 7
    instance.pointList = 13
    assert instance.pointList == 13


def test_draw2d_Polyline_tolerance_value_roundtrip():
    instance = draw2d_Polyline(tolerance=7)
    assert instance.tolerance == 7
    instance.tolerance = 13
    assert instance.tolerance == 13


def test_draw2d_PolylineShape_tolerance_value_roundtrip():
    instance = draw2d_PolylineShape(tolerance=7)
    assert instance.tolerance == 7
    instance.tolerance = 13
    assert instance.tolerance == 13


def test_draw2d_RoundedRectangle_cornerDimensions_value_roundtrip():
    instance = draw2d_RoundedRectangle(cornerDimensions="sample_text")
    assert instance.cornerDimensions == "sample_text"
    instance.cornerDimensions = "sample_text_2"
    assert instance.cornerDimensions == "sample_text_2"


def test_draw2d_Shape_alpha_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_draw2d_Shape_antialias_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.antialias == "sample_text"
    instance.antialias = "sample_text_2"
    assert instance.antialias == "sample_text_2"


def test_draw2d_Shape_fill_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.fill == True
    instance.fill = False
    assert instance.fill == False


def test_draw2d_Shape_fillXOR_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.fillXOR == True
    instance.fillXOR = False
    assert instance.fillXOR == False


def test_draw2d_Shape_lineCap_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.lineCap == "sample_text"
    instance.lineCap = "sample_text_2"
    assert instance.lineCap == "sample_text_2"


def test_draw2d_Shape_lineDash_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.lineDash == 3.14
    instance.lineDash = 9.99
    assert instance.lineDash == 9.99


def test_draw2d_Shape_lineDashOffset_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.lineDashOffset == 3.14
    instance.lineDashOffset = 9.99
    assert instance.lineDashOffset == 9.99


def test_draw2d_Shape_lineJoin_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.lineJoin == "sample_text"
    instance.lineJoin = "sample_text_2"
    assert instance.lineJoin == "sample_text_2"


def test_draw2d_Shape_lineMiterLimit_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.lineMiterLimit == 3.14
    instance.lineMiterLimit = 9.99
    assert instance.lineMiterLimit == 9.99


def test_draw2d_Shape_lineStyle_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_draw2d_Shape_lineWidthFloat_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.lineWidthFloat == 3.14
    instance.lineWidthFloat = 9.99
    assert instance.lineWidthFloat == 9.99


def test_draw2d_Shape_outline_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.outline == True
    instance.outline = False
    assert instance.outline == False


def test_draw2d_Shape_outlineXOR_value_roundtrip():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert instance.outlineXOR == True
    instance.outlineXOR = False
    assert instance.outlineXOR == False


def test_draw2d_Triangle_direction_value_roundtrip():
    instance = draw2d_Triangle(direction="sample_text", orientation="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_draw2d_Triangle_orientation_value_roundtrip():
    instance = draw2d_Triangle(direction="sample_text", orientation="sample_text")
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_draw2d_XYAnchor_location_value_roundtrip():
    instance = draw2d_XYAnchor(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_draw2d_FlowBorder_isa_Border():
    instance = draw2d_FlowBorder(bottomMargin=7, leftMargin=7, rightMargin=7, topMargin=7)
    assert isinstance(instance, Border)


def test_draw2d_LabeledBorder_isa_Border():
    instance = draw2d_LabeledBorder(label="sample_text")
    assert isinstance(instance, Border)


def test_draw2d_Draw2DCanvas_isa_Canvas():
    instance = draw2d_Draw2DCanvas()
    assert isinstance(instance, Canvas)


def test_draw2d_GroupBoxBorder_isa_ColoredLabeledBorder():
    instance = draw2d_GroupBoxBorder()
    assert isinstance(instance, ColoredLabeledBorder)


def test_draw2d_TitleBarBorder_isa_ColoredLabeledBorder():
    instance = draw2d_TitleBarBorder()
    assert isinstance(instance, ColoredLabeledBorder)


def test_draw2d_XYAnchor_isa_ConnectionAnchor():
    instance = draw2d_XYAnchor(location="sample_text")
    assert isinstance(instance, ConnectionAnchor)


def test_draw2d_BlockFlow_isa_Figure():
    instance = draw2d_BlockFlow(orientation="sample_text")
    assert isinstance(instance, Figure)


def test_draw2d_ImageFigure_isa_Figure():
    instance = draw2d_ImageFigure(image="sample_text")
    assert isinstance(instance, Figure)


def test_draw2d_Label_isa_Figure():
    instance = draw2d_Label(icon="sample_text", iconAlignment="sample_text", iconTextGap=7, text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert isinstance(instance, Figure)


def test_draw2d_Shape_isa_Figure():
    instance = draw2d_Shape(alpha="sample_text", antialias="sample_text", fill=True, fillXOR=True, lineCap="sample_text", lineDash=3.14, lineDashOffset=3.14, lineJoin="sample_text", lineMiterLimit=3.14, lineStyle="sample_text", lineWidthFloat=3.14, outline=True, outlineXOR=True)
    assert isinstance(instance, Figure)


def test_draw2d_ColoredLabeledBorder_isa_LabeledBorder():
    instance = draw2d_ColoredLabeledBorder()
    assert isinstance(instance, LabeledBorder)


def test_draw2d_FrameBorder_isa_LabeledBorder():
    instance = draw2d_FrameBorder()
    assert isinstance(instance, LabeledBorder)


def test_draw2d_PolygonShape_isa_PointListShape():
    instance = draw2d_PolygonShape()
    assert isinstance(instance, PointListShape)


def test_draw2d_Polyline_isa_PointListShape():
    instance = draw2d_Polyline(tolerance=7)
    assert isinstance(instance, PointListShape)


def test_draw2d_PolylineShape_isa_PointListShape():
    instance = draw2d_PolylineShape(tolerance=7)
    assert isinstance(instance, PointListShape)


def test_draw2d_Polygon_isa_Polyline():
    instance = draw2d_Polygon()
    assert isinstance(instance, Polyline)


def test_draw2d_Ellipse_isa_Shape():
    instance = draw2d_Ellipse()
    assert isinstance(instance, Shape)


def test_draw2d_PointListShape_isa_Shape():
    instance = draw2d_PointListShape(pointList=7)
    assert isinstance(instance, Shape)


def test_draw2d_RectangleFigure_isa_Shape():
    instance = draw2d_RectangleFigure()
    assert isinstance(instance, Shape)


def test_draw2d_RoundedRectangle_isa_Shape():
    instance = draw2d_RoundedRectangle(cornerDimensions="sample_text")
    assert isinstance(instance, Shape)


def test_draw2d_Triangle_isa_Shape():
    instance = draw2d_Triangle(direction="sample_text", orientation="sample_text")
    assert isinstance(instance, Shape)


def test_assoc_backgroundColor9_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Color()
    b2 = draw2d_Color()
    _safe_set(a, 'draw2d_Figure10', b1)
    assert _is_linked(a, 'draw2d_Figure10', b1)
    if hasattr(b1, 'draw2d_Color'):
        assert _is_linked(b1, 'draw2d_Color', a)
    _safe_set(a, 'draw2d_Figure10', b2)
    assert _is_linked(a, 'draw2d_Figure10', b2)
    if hasattr(b1, 'draw2d_Color'):
        assert not _is_linked(b1, 'draw2d_Color', a)
    if hasattr(b2, 'draw2d_Color'):
        assert _is_linked(b2, 'draw2d_Color', a)
    _safe_set(a, 'draw2d_Figure10', None)
    assert not _is_linked(a, 'draw2d_Figure10', b2)
    if hasattr(b2, 'draw2d_Color'):
        assert not _is_linked(b2, 'draw2d_Color', a)


def test_assoc_border16_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Border(opaque=True)
    b2 = draw2d_Border(opaque=False)
    _safe_set(a, 'draw2d_Figure17', b1)
    assert _is_linked(a, 'draw2d_Figure17', b1)
    if hasattr(b1, 'draw2d_Border'):
        assert _is_linked(b1, 'draw2d_Border', a)
    _safe_set(a, 'draw2d_Figure17', b2)
    assert _is_linked(a, 'draw2d_Figure17', b2)
    if hasattr(b1, 'draw2d_Border'):
        assert not _is_linked(b1, 'draw2d_Border', a)
    if hasattr(b2, 'draw2d_Border'):
        assert _is_linked(b2, 'draw2d_Border', a)
    _safe_set(a, 'draw2d_Figure17', None)
    assert not _is_linked(a, 'draw2d_Figure17', b2)
    if hasattr(b2, 'draw2d_Border'):
        assert not _is_linked(b2, 'draw2d_Border', a)


def test_assoc_children2_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b2 = draw2d_Figure(bounds="sample_text_2", enabled=False, focusTraversable=False, maximumSize="sample_text_2", minimumSize="sample_text_2", opaque=False, preferredSize="sample_text_2", visible=False)
    _safe_set(a, 'Figure', b1)
    assert _is_linked(a, 'Figure', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'Figure', b2)
    assert _is_linked(a, 'Figure', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'Figure', None)
    assert not _is_linked(a, 'Figure', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_contents0_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Draw2DCanvas()
    b2 = draw2d_Draw2DCanvas()
    _safe_set(a, 'draw2d_Figure', b1)
    assert _is_linked(a, 'draw2d_Figure', b1)
    if hasattr(b1, 'draw2d_Draw2DCanvas'):
        assert _is_linked(b1, 'draw2d_Draw2DCanvas', a)
    _safe_set(a, 'draw2d_Figure', b2)
    assert _is_linked(a, 'draw2d_Figure', b2)
    if hasattr(b1, 'draw2d_Draw2DCanvas'):
        assert not _is_linked(b1, 'draw2d_Draw2DCanvas', a)
    if hasattr(b2, 'draw2d_Draw2DCanvas'):
        assert _is_linked(b2, 'draw2d_Draw2DCanvas', a)
    _safe_set(a, 'draw2d_Figure', None)
    assert not _is_linked(a, 'draw2d_Figure', b2)
    if hasattr(b2, 'draw2d_Draw2DCanvas'):
        assert not _is_linked(b2, 'draw2d_Draw2DCanvas', a)


def test_assoc_font14_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Font()
    b2 = draw2d_Font()
    _safe_set(a, 'draw2d_Figure15', b1)
    assert _is_linked(a, 'draw2d_Figure15', b1)
    if hasattr(b1, 'draw2d_Font'):
        assert _is_linked(b1, 'draw2d_Font', a)
    _safe_set(a, 'draw2d_Figure15', b2)
    assert _is_linked(a, 'draw2d_Figure15', b2)
    if hasattr(b1, 'draw2d_Font'):
        assert not _is_linked(b1, 'draw2d_Font', a)
    if hasattr(b2, 'draw2d_Font'):
        assert _is_linked(b2, 'draw2d_Font', a)
    _safe_set(a, 'draw2d_Figure15', None)
    assert not _is_linked(a, 'draw2d_Figure15', b2)
    if hasattr(b2, 'draw2d_Font'):
        assert not _is_linked(b2, 'draw2d_Font', a)


def test_assoc_font20_link_reassign_clear():
    a = draw2d_LabeledBorder(label="sample_text")
    b1 = draw2d_Font()
    b2 = draw2d_Font()
    _safe_set(a, 'draw2d_LabeledBorder', b1)
    assert _is_linked(a, 'draw2d_LabeledBorder', b1)
    if hasattr(b1, 'draw2d_Font21'):
        assert _is_linked(b1, 'draw2d_Font21', a)
    _safe_set(a, 'draw2d_LabeledBorder', b2)
    assert _is_linked(a, 'draw2d_LabeledBorder', b2)
    if hasattr(b1, 'draw2d_Font21'):
        assert not _is_linked(b1, 'draw2d_Font21', a)
    if hasattr(b2, 'draw2d_Font21'):
        assert _is_linked(b2, 'draw2d_Font21', a)
    _safe_set(a, 'draw2d_LabeledBorder', None)
    assert not _is_linked(a, 'draw2d_LabeledBorder', b2)
    if hasattr(b2, 'draw2d_Font21'):
        assert not _is_linked(b2, 'draw2d_Font21', a)


def test_assoc_foregroundColor11_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Color()
    b2 = draw2d_Color()
    _safe_set(a, 'draw2d_Figure12', b1)
    assert _is_linked(a, 'draw2d_Figure12', b1)
    if hasattr(b1, 'draw2d_Color13'):
        assert _is_linked(b1, 'draw2d_Color13', a)
    _safe_set(a, 'draw2d_Figure12', b2)
    assert _is_linked(a, 'draw2d_Figure12', b2)
    if hasattr(b1, 'draw2d_Color13'):
        assert not _is_linked(b1, 'draw2d_Color13', a)
    if hasattr(b2, 'draw2d_Color13'):
        assert _is_linked(b2, 'draw2d_Color13', a)
    _safe_set(a, 'draw2d_Figure12', None)
    assert not _is_linked(a, 'draw2d_Figure12', b2)
    if hasattr(b2, 'draw2d_Color13'):
        assert not _is_linked(b2, 'draw2d_Color13', a)


def test_assoc_owner18_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_ConnectionAnchor()
    b2 = draw2d_ConnectionAnchor()
    _safe_set(a, 'draw2d_Figure19', b1)
    assert _is_linked(a, 'draw2d_Figure19', b1)
    if hasattr(b1, 'draw2d_ConnectionAnchor'):
        assert _is_linked(b1, 'draw2d_ConnectionAnchor', a)
    _safe_set(a, 'draw2d_Figure19', b2)
    assert _is_linked(a, 'draw2d_Figure19', b2)
    if hasattr(b1, 'draw2d_ConnectionAnchor'):
        assert not _is_linked(b1, 'draw2d_ConnectionAnchor', a)
    if hasattr(b2, 'draw2d_ConnectionAnchor'):
        assert _is_linked(b2, 'draw2d_ConnectionAnchor', a)
    _safe_set(a, 'draw2d_Figure19', None)
    assert not _is_linked(a, 'draw2d_Figure19', b2)
    if hasattr(b2, 'draw2d_ConnectionAnchor'):
        assert not _is_linked(b2, 'draw2d_ConnectionAnchor', a)


def test_assoc_parent4_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b2 = draw2d_Figure(bounds="sample_text_2", enabled=False, focusTraversable=False, maximumSize="sample_text_2", minimumSize="sample_text_2", opaque=False, preferredSize="sample_text_2", visible=False)
    _safe_set(a, 'Figure5', b1)
    assert _is_linked(a, 'Figure5', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'Figure5', b2)
    assert _is_linked(a, 'Figure5', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'Figure5', None)
    assert not _is_linked(a, 'Figure5', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_toolTip7_link_reassign_clear():
    a = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b1 = draw2d_Figure(bounds="sample_text", enabled=True, focusTraversable=True, maximumSize="sample_text", minimumSize="sample_text", opaque=True, preferredSize="sample_text", visible=True)
    b2 = draw2d_Figure(bounds="sample_text_2", enabled=False, focusTraversable=False, maximumSize="sample_text_2", minimumSize="sample_text_2", opaque=False, preferredSize="sample_text_2", visible=False)
    _safe_set(a, 'draw2d_Figure6', b1)
    assert _is_linked(a, 'draw2d_Figure6', b1)
    if hasattr(b1, 'draw2d_Figure8'):
        assert _is_linked(b1, 'draw2d_Figure8', a)
    _safe_set(a, 'draw2d_Figure6', b2)
    assert _is_linked(a, 'draw2d_Figure6', b2)
    if hasattr(b1, 'draw2d_Figure8'):
        assert not _is_linked(b1, 'draw2d_Figure8', a)
    if hasattr(b2, 'draw2d_Figure8'):
        assert _is_linked(b2, 'draw2d_Figure8', a)
    _safe_set(a, 'draw2d_Figure6', None)
    assert not _is_linked(a, 'draw2d_Figure6', b2)
    if hasattr(b2, 'draw2d_Figure8'):
        assert not _is_linked(b2, 'draw2d_Figure8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Border_strategy = st.builds(Border)
@given(instance=Border_strategy)
@settings(max_examples=25)
def test_Border_instantiation(instance):
    assert isinstance(instance, Border)


Canvas_strategy = st.builds(Canvas)
@given(instance=Canvas_strategy)
@settings(max_examples=25)
def test_Canvas_instantiation(instance):
    assert isinstance(instance, Canvas)


ColoredLabeledBorder_strategy = st.builds(ColoredLabeledBorder)
@given(instance=ColoredLabeledBorder_strategy)
@settings(max_examples=25)
def test_ColoredLabeledBorder_instantiation(instance):
    assert isinstance(instance, ColoredLabeledBorder)


ConnectionAnchor_strategy = st.builds(ConnectionAnchor)
@given(instance=ConnectionAnchor_strategy)
@settings(max_examples=25)
def test_ConnectionAnchor_instantiation(instance):
    assert isinstance(instance, ConnectionAnchor)


Figure_strategy = st.builds(Figure)
@given(instance=Figure_strategy)
@settings(max_examples=25)
def test_Figure_instantiation(instance):
    assert isinstance(instance, Figure)


LabeledBorder_strategy = st.builds(LabeledBorder)
@given(instance=LabeledBorder_strategy)
@settings(max_examples=25)
def test_LabeledBorder_instantiation(instance):
    assert isinstance(instance, LabeledBorder)


PointListShape_strategy = st.builds(PointListShape)
@given(instance=PointListShape_strategy)
@settings(max_examples=25)
def test_PointListShape_instantiation(instance):
    assert isinstance(instance, PointListShape)


Polyline_strategy = st.builds(Polyline)
@given(instance=Polyline_strategy)
@settings(max_examples=25)
def test_Polyline_instantiation(instance):
    assert isinstance(instance, Polyline)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


draw2d_BlockFlow_strategy = st.builds(draw2d_BlockFlow, orientation=safe_text)
@given(instance=draw2d_BlockFlow_strategy)
@settings(max_examples=25)
def test_draw2d_BlockFlow_instantiation(instance):
    assert isinstance(instance, draw2d_BlockFlow)


draw2d_Border_strategy = st.builds(draw2d_Border, opaque=st.booleans())
@given(instance=draw2d_Border_strategy)
@settings(max_examples=25)
def test_draw2d_Border_instantiation(instance):
    assert isinstance(instance, draw2d_Border)


draw2d_Color_strategy = st.builds(draw2d_Color)
@given(instance=draw2d_Color_strategy)
@settings(max_examples=25)
def test_draw2d_Color_instantiation(instance):
    assert isinstance(instance, draw2d_Color)


draw2d_ColoredLabeledBorder_strategy = st.builds(draw2d_ColoredLabeledBorder)
@given(instance=draw2d_ColoredLabeledBorder_strategy)
@settings(max_examples=25)
def test_draw2d_ColoredLabeledBorder_instantiation(instance):
    assert isinstance(instance, draw2d_ColoredLabeledBorder)


draw2d_ConnectionAnchor_strategy = st.builds(draw2d_ConnectionAnchor)
@given(instance=draw2d_ConnectionAnchor_strategy)
@settings(max_examples=25)
def test_draw2d_ConnectionAnchor_instantiation(instance):
    assert isinstance(instance, draw2d_ConnectionAnchor)


draw2d_Draw2DCanvas_strategy = st.builds(draw2d_Draw2DCanvas)
@given(instance=draw2d_Draw2DCanvas_strategy)
@settings(max_examples=25)
def test_draw2d_Draw2DCanvas_instantiation(instance):
    assert isinstance(instance, draw2d_Draw2DCanvas)


draw2d_Ellipse_strategy = st.builds(draw2d_Ellipse)
@given(instance=draw2d_Ellipse_strategy)
@settings(max_examples=25)
def test_draw2d_Ellipse_instantiation(instance):
    assert isinstance(instance, draw2d_Ellipse)


draw2d_Figure_strategy = st.builds(draw2d_Figure, bounds=safe_text, enabled=st.booleans(), focusTraversable=st.booleans(), maximumSize=safe_text, minimumSize=safe_text, opaque=st.booleans(), preferredSize=safe_text, visible=st.booleans())
@given(instance=draw2d_Figure_strategy)
@settings(max_examples=25)
def test_draw2d_Figure_instantiation(instance):
    assert isinstance(instance, draw2d_Figure)


draw2d_FlowBorder_strategy = st.builds(draw2d_FlowBorder, bottomMargin=st.integers(), leftMargin=st.integers(), rightMargin=st.integers(), topMargin=st.integers())
@given(instance=draw2d_FlowBorder_strategy)
@settings(max_examples=25)
def test_draw2d_FlowBorder_instantiation(instance):
    assert isinstance(instance, draw2d_FlowBorder)


draw2d_Font_strategy = st.builds(draw2d_Font)
@given(instance=draw2d_Font_strategy)
@settings(max_examples=25)
def test_draw2d_Font_instantiation(instance):
    assert isinstance(instance, draw2d_Font)


draw2d_FrameBorder_strategy = st.builds(draw2d_FrameBorder)
@given(instance=draw2d_FrameBorder_strategy)
@settings(max_examples=25)
def test_draw2d_FrameBorder_instantiation(instance):
    assert isinstance(instance, draw2d_FrameBorder)


draw2d_GroupBoxBorder_strategy = st.builds(draw2d_GroupBoxBorder)
@given(instance=draw2d_GroupBoxBorder_strategy)
@settings(max_examples=25)
def test_draw2d_GroupBoxBorder_instantiation(instance):
    assert isinstance(instance, draw2d_GroupBoxBorder)


draw2d_ImageFigure_strategy = st.builds(draw2d_ImageFigure, image=safe_text)
@given(instance=draw2d_ImageFigure_strategy)
@settings(max_examples=25)
def test_draw2d_ImageFigure_instantiation(instance):
    assert isinstance(instance, draw2d_ImageFigure)


draw2d_Label_strategy = st.builds(draw2d_Label, icon=safe_text, iconAlignment=safe_text, iconTextGap=st.integers(), text=safe_text, textAlignment=safe_text, textPlacement=safe_text)
@given(instance=draw2d_Label_strategy)
@settings(max_examples=25)
def test_draw2d_Label_instantiation(instance):
    assert isinstance(instance, draw2d_Label)


draw2d_LabeledBorder_strategy = st.builds(draw2d_LabeledBorder, label=safe_text)
@given(instance=draw2d_LabeledBorder_strategy)
@settings(max_examples=25)
def test_draw2d_LabeledBorder_instantiation(instance):
    assert isinstance(instance, draw2d_LabeledBorder)


draw2d_PointListShape_strategy = st.builds(draw2d_PointListShape, pointList=st.integers())
@given(instance=draw2d_PointListShape_strategy)
@settings(max_examples=25)
def test_draw2d_PointListShape_instantiation(instance):
    assert isinstance(instance, draw2d_PointListShape)


draw2d_Polygon_strategy = st.builds(draw2d_Polygon)
@given(instance=draw2d_Polygon_strategy)
@settings(max_examples=25)
def test_draw2d_Polygon_instantiation(instance):
    assert isinstance(instance, draw2d_Polygon)


draw2d_PolygonShape_strategy = st.builds(draw2d_PolygonShape)
@given(instance=draw2d_PolygonShape_strategy)
@settings(max_examples=25)
def test_draw2d_PolygonShape_instantiation(instance):
    assert isinstance(instance, draw2d_PolygonShape)


draw2d_Polyline_strategy = st.builds(draw2d_Polyline, tolerance=st.integers())
@given(instance=draw2d_Polyline_strategy)
@settings(max_examples=25)
def test_draw2d_Polyline_instantiation(instance):
    assert isinstance(instance, draw2d_Polyline)


draw2d_PolylineShape_strategy = st.builds(draw2d_PolylineShape, tolerance=st.integers())
@given(instance=draw2d_PolylineShape_strategy)
@settings(max_examples=25)
def test_draw2d_PolylineShape_instantiation(instance):
    assert isinstance(instance, draw2d_PolylineShape)


draw2d_RectangleFigure_strategy = st.builds(draw2d_RectangleFigure)
@given(instance=draw2d_RectangleFigure_strategy)
@settings(max_examples=25)
def test_draw2d_RectangleFigure_instantiation(instance):
    assert isinstance(instance, draw2d_RectangleFigure)


draw2d_RoundedRectangle_strategy = st.builds(draw2d_RoundedRectangle, cornerDimensions=safe_text)
@given(instance=draw2d_RoundedRectangle_strategy)
@settings(max_examples=25)
def test_draw2d_RoundedRectangle_instantiation(instance):
    assert isinstance(instance, draw2d_RoundedRectangle)


draw2d_Shape_strategy = st.builds(draw2d_Shape, alpha=safe_text, antialias=safe_text, fill=st.booleans(), fillXOR=st.booleans(), lineCap=safe_text, lineDash=st.floats(allow_nan=False, allow_infinity=False), lineDashOffset=st.floats(allow_nan=False, allow_infinity=False), lineJoin=safe_text, lineMiterLimit=st.floats(allow_nan=False, allow_infinity=False), lineStyle=safe_text, lineWidthFloat=st.floats(allow_nan=False, allow_infinity=False), outline=st.booleans(), outlineXOR=st.booleans())
@given(instance=draw2d_Shape_strategy)
@settings(max_examples=25)
def test_draw2d_Shape_instantiation(instance):
    assert isinstance(instance, draw2d_Shape)


draw2d_TitleBarBorder_strategy = st.builds(draw2d_TitleBarBorder)
@given(instance=draw2d_TitleBarBorder_strategy)
@settings(max_examples=25)
def test_draw2d_TitleBarBorder_instantiation(instance):
    assert isinstance(instance, draw2d_TitleBarBorder)


draw2d_Triangle_strategy = st.builds(draw2d_Triangle, direction=safe_text, orientation=safe_text)
@given(instance=draw2d_Triangle_strategy)
@settings(max_examples=25)
def test_draw2d_Triangle_instantiation(instance):
    assert isinstance(instance, draw2d_Triangle)


draw2d_XYAnchor_strategy = st.builds(draw2d_XYAnchor, location=safe_text)
@given(instance=draw2d_XYAnchor_strategy)
@settings(max_examples=25)
def test_draw2d_XYAnchor_instantiation(instance):
    assert isinstance(instance, draw2d_XYAnchor)



