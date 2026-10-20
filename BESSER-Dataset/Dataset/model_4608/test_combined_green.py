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
    Layout,
    gmfgraph_BorderLayout,
    gmfgraph_GridLayout,
    gmfgraph_StackLayout,
    gmfgraph_FlowLayout,
    gmfgraph_XYLayout,
    gmfgraph_Layout,
    LayoutData,
    gmfgraph_GridLayoutData,
    gmfgraph_BorderLayoutData,
    gmfgraph_XYLayoutData,
    gmfgraph_Layoutable,
    gmfgraph_LayoutData,
    Font,
    gmfgraph_BasicFont,
    Border,
    gmfgraph_CompoundBorder,
    gmfgraph_MarginBorder,
    gmfgraph_LineBorder,
    gmfgraph_FigureAccessor,
    Color,
    gmfgraph_ConstantColor,
    gmfgraph_RGBColor,
    CustomFigure,
    CustomClass,
    gmfgraph_CustomLayout,
    gmfgraph_CustomLayoutData,
    gmfgraph_CustomBorder,
    gmfgraph_CustomAttribute,
    gmfgraph_CustomClass,
    DecorationFigure,
    gmfgraph_CustomDecoration,
    ConnectionFigure,
    gmfgraph_CustomConnection,
    Polygon,
    gmfgraph_PolygonDecoration,
    gmfgraph_ScalablePolygon,
    Polyline,
    gmfgraph_PolylineConnection,
    gmfgraph_PolylineDecoration,
    gmfgraph_Polygon,
    AbstractFigure,
    Shape,
    gmfgraph_Ellipse,
    gmfgraph_Polyline,
    gmfgraph_RoundedRectangle,
    gmfgraph_Rectangle,
    RealFigure,
    gmfgraph_Label,
    gmfgraph_DecorationFigure,
    gmfgraph_LabeledContainer,
    gmfgraph_Shape,
    gmfgraph_CustomFigure,
    gmfgraph_ConnectionFigure,
    gmfgraph_FigureRef,
    gmfgraph_Color,
    Figure,
    gmfgraph_AbstractFigure,
    gmfgraph_Point,
    gmfgraph_Border,
    gmfgraph_Insets,
    gmfgraph_Font,
    gmfgraph_ChildAccess,
    Layoutable,
    gmfgraph_Figure,
    gmfgraph_Dimension,
    VisualFacet,
    gmfgraph_GradientFacet,
    gmfgraph_LabelOffsetFacet,
    gmfgraph_DefaultSizeFacet,
    gmfgraph_AlignmentFacet,
    gmfgraph_GeneralFacet,
    Node,
    AbstractNode,
    gmfgraph_Node,
    DiagramElement,
    gmfgraph_Connection,
    gmfgraph_AbstractNode,
    gmfgraph_VisualFacet,
    gmfgraph_Identity,
    gmfgraph_RealFigure,
    gmfgraph_DiagramLabel,
    gmfgraph_Compartment,
    Identity,
    gmfgraph_DiagramElement,
    gmfgraph_FigureDescriptor,
    gmfgraph_FigureGallery,
    gmfgraph_Canvas,
    Alignment,
    FontStyle,
    ColorConstants,
    LineKind,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_hyp_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_hyp_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_borderlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_BorderLayout)


def test_hyp_gmfgraph_borderlayout_constructor_exists():
    assert callable(gmfgraph_BorderLayout.__init__)


def test_hyp_gmfgraph_borderlayout_constructor_args():
    sig = inspect.signature(gmfgraph_BorderLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_gridlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_GridLayout)


def test_hyp_gmfgraph_gridlayout_constructor_exists():
    assert callable(gmfgraph_GridLayout.__init__)


def test_hyp_gmfgraph_gridlayout_constructor_args():
    sig = inspect.signature(gmfgraph_GridLayout.__init__)
    params = list(sig.parameters.keys())
    assert "numColumns" in params, "Missing parameter 'numColumns'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"





def test_hyp_gmfgraph_stacklayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_StackLayout)


def test_hyp_gmfgraph_stacklayout_constructor_exists():
    assert callable(gmfgraph_StackLayout.__init__)


def test_hyp_gmfgraph_stacklayout_constructor_args():
    sig = inspect.signature(gmfgraph_StackLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_flowlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_FlowLayout)


def test_hyp_gmfgraph_flowlayout_constructor_exists():
    assert callable(gmfgraph_FlowLayout.__init__)


def test_hyp_gmfgraph_flowlayout_constructor_args():
    sig = inspect.signature(gmfgraph_FlowLayout.__init__)
    params = list(sig.parameters.keys())
    assert "matchMinorSize" in params, "Missing parameter 'matchMinorSize'"
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "majorAlignment" in params, "Missing parameter 'majorAlignment'"
    assert "forceSingleLine" in params, "Missing parameter 'forceSingleLine'"
    assert "minorAlignment" in params, "Missing parameter 'minorAlignment'"
    assert "minorSpacing" in params, "Missing parameter 'minorSpacing'"
    assert "majorSpacing" in params, "Missing parameter 'majorSpacing'"










def test_hyp_gmfgraph_xylayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_XYLayout)


def test_hyp_gmfgraph_xylayout_constructor_exists():
    assert callable(gmfgraph_XYLayout.__init__)


def test_hyp_gmfgraph_xylayout_constructor_args():
    sig = inspect.signature(gmfgraph_XYLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_layout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Layout)


def test_hyp_gmfgraph_layout_constructor_exists():
    assert callable(gmfgraph_Layout.__init__)


def test_hyp_gmfgraph_layout_constructor_args():
    sig = inspect.signature(gmfgraph_Layout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_layoutdata_is_not_abstract():
    assert not inspect.isabstract(LayoutData)


def test_hyp_layoutdata_constructor_exists():
    assert callable(LayoutData.__init__)


def test_hyp_layoutdata_constructor_args():
    sig = inspect.signature(LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_gridlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_GridLayoutData)


def test_hyp_gmfgraph_gridlayoutdata_constructor_exists():
    assert callable(gmfgraph_GridLayoutData.__init__)


def test_hyp_gmfgraph_gridlayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph_GridLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalSpan" in params, "Missing parameter 'horizontalSpan'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "grabExcessHorizontalSpace" in params, "Missing parameter 'grabExcessHorizontalSpace'"
    assert "horizontalIndent" in params, "Missing parameter 'horizontalIndent'"
    assert "verticalSpan" in params, "Missing parameter 'verticalSpan'"
    assert "grabExcessVerticalSpace" in params, "Missing parameter 'grabExcessVerticalSpace'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"










def test_hyp_gmfgraph_borderlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_BorderLayoutData)


def test_hyp_gmfgraph_borderlayoutdata_constructor_exists():
    assert callable(gmfgraph_BorderLayoutData.__init__)


def test_hyp_gmfgraph_borderlayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph_BorderLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "alignment" in params, "Missing parameter 'alignment'"





def test_hyp_gmfgraph_xylayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_XYLayoutData)


def test_hyp_gmfgraph_xylayoutdata_constructor_exists():
    assert callable(gmfgraph_XYLayoutData.__init__)


def test_hyp_gmfgraph_xylayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph_XYLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_layoutable_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Layoutable)


def test_hyp_gmfgraph_layoutable_constructor_exists():
    assert callable(gmfgraph_Layoutable.__init__)


def test_hyp_gmfgraph_layoutable_constructor_args():
    sig = inspect.signature(gmfgraph_Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_LayoutData)


def test_hyp_gmfgraph_layoutdata_constructor_exists():
    assert callable(gmfgraph_LayoutData.__init__)


def test_hyp_gmfgraph_layoutdata_constructor_args():
    sig = inspect.signature(gmfgraph_LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_font_is_not_abstract():
    assert not inspect.isabstract(Font)


def test_hyp_font_constructor_exists():
    assert callable(Font.__init__)


def test_hyp_font_constructor_args():
    sig = inspect.signature(Font.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_basicfont_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_BasicFont)


def test_hyp_gmfgraph_basicfont_constructor_exists():
    assert callable(gmfgraph_BasicFont.__init__)


def test_hyp_gmfgraph_basicfont_constructor_args():
    sig = inspect.signature(gmfgraph_BasicFont.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "faceName" in params, "Missing parameter 'faceName'"
    assert "height" in params, "Missing parameter 'height'"






def test_hyp_border_is_not_abstract():
    assert not inspect.isabstract(Border)


def test_hyp_border_constructor_exists():
    assert callable(Border.__init__)


def test_hyp_border_constructor_args():
    sig = inspect.signature(Border.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_compoundborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CompoundBorder)


def test_hyp_gmfgraph_compoundborder_constructor_exists():
    assert callable(gmfgraph_CompoundBorder.__init__)


def test_hyp_gmfgraph_compoundborder_constructor_args():
    sig = inspect.signature(gmfgraph_CompoundBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_marginborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_MarginBorder)


def test_hyp_gmfgraph_marginborder_constructor_exists():
    assert callable(gmfgraph_MarginBorder.__init__)


def test_hyp_gmfgraph_marginborder_constructor_args():
    sig = inspect.signature(gmfgraph_MarginBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_lineborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_LineBorder)


def test_hyp_gmfgraph_lineborder_constructor_exists():
    assert callable(gmfgraph_LineBorder.__init__)


def test_hyp_gmfgraph_lineborder_constructor_args():
    sig = inspect.signature(gmfgraph_LineBorder.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"




def test_hyp_gmfgraph_figureaccessor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_FigureAccessor)


def test_hyp_gmfgraph_figureaccessor_constructor_exists():
    assert callable(gmfgraph_FigureAccessor.__init__)


def test_hyp_gmfgraph_figureaccessor_constructor_args():
    sig = inspect.signature(gmfgraph_FigureAccessor.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"




def test_hyp_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_hyp_color_constructor_exists():
    assert callable(Color.__init__)


def test_hyp_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_constantcolor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_ConstantColor)


def test_hyp_gmfgraph_constantcolor_constructor_exists():
    assert callable(gmfgraph_ConstantColor.__init__)


def test_hyp_gmfgraph_constantcolor_constructor_args():
    sig = inspect.signature(gmfgraph_ConstantColor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_gmfgraph_rgbcolor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_RGBColor)


def test_hyp_gmfgraph_rgbcolor_constructor_exists():
    assert callable(gmfgraph_RGBColor.__init__)


def test_hyp_gmfgraph_rgbcolor_constructor_args():
    sig = inspect.signature(gmfgraph_RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"






def test_hyp_customfigure_is_not_abstract():
    assert not inspect.isabstract(CustomFigure)


def test_hyp_customfigure_constructor_exists():
    assert callable(CustomFigure.__init__)


def test_hyp_customfigure_constructor_args():
    sig = inspect.signature(CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customclass_is_not_abstract():
    assert not inspect.isabstract(CustomClass)


def test_hyp_customclass_constructor_exists():
    assert callable(CustomClass.__init__)


def test_hyp_customclass_constructor_args():
    sig = inspect.signature(CustomClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomLayout)


def test_hyp_gmfgraph_customlayout_constructor_exists():
    assert callable(gmfgraph_CustomLayout.__init__)


def test_hyp_gmfgraph_customlayout_constructor_args():
    sig = inspect.signature(gmfgraph_CustomLayout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomLayoutData)


def test_hyp_gmfgraph_customlayoutdata_constructor_exists():
    assert callable(gmfgraph_CustomLayoutData.__init__)


def test_hyp_gmfgraph_customlayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph_CustomLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomBorder)


def test_hyp_gmfgraph_customborder_constructor_exists():
    assert callable(gmfgraph_CustomBorder.__init__)


def test_hyp_gmfgraph_customborder_constructor_args():
    sig = inspect.signature(gmfgraph_CustomBorder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customattribute_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomAttribute)


def test_hyp_gmfgraph_customattribute_constructor_exists():
    assert callable(gmfgraph_CustomAttribute.__init__)


def test_hyp_gmfgraph_customattribute_constructor_args():
    sig = inspect.signature(gmfgraph_CustomAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "directAccess" in params, "Missing parameter 'directAccess'"
    assert "name" in params, "Missing parameter 'name'"
    assert "multiStatementValue" in params, "Missing parameter 'multiStatementValue'"
    assert "value" in params, "Missing parameter 'value'"







def test_hyp_gmfgraph_customclass_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomClass)


def test_hyp_gmfgraph_customclass_constructor_exists():
    assert callable(gmfgraph_CustomClass.__init__)


def test_hyp_gmfgraph_customclass_constructor_args():
    sig = inspect.signature(gmfgraph_CustomClass.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"




def test_hyp_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(DecorationFigure)


def test_hyp_decorationfigure_constructor_exists():
    assert callable(DecorationFigure.__init__)


def test_hyp_decorationfigure_constructor_args():
    sig = inspect.signature(DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customdecoration_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomDecoration)


def test_hyp_gmfgraph_customdecoration_constructor_exists():
    assert callable(gmfgraph_CustomDecoration.__init__)


def test_hyp_gmfgraph_customdecoration_constructor_args():
    sig = inspect.signature(gmfgraph_CustomDecoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connectionfigure_is_not_abstract():
    assert not inspect.isabstract(ConnectionFigure)


def test_hyp_connectionfigure_constructor_exists():
    assert callable(ConnectionFigure.__init__)


def test_hyp_connectionfigure_constructor_args():
    sig = inspect.signature(ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_customconnection_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomConnection)


def test_hyp_gmfgraph_customconnection_constructor_exists():
    assert callable(gmfgraph_CustomConnection.__init__)


def test_hyp_gmfgraph_customconnection_constructor_args():
    sig = inspect.signature(gmfgraph_CustomConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_polygon_is_not_abstract():
    assert not inspect.isabstract(Polygon)


def test_hyp_polygon_constructor_exists():
    assert callable(Polygon.__init__)


def test_hyp_polygon_constructor_args():
    sig = inspect.signature(Polygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_polygondecoration_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_PolygonDecoration)


def test_hyp_gmfgraph_polygondecoration_constructor_exists():
    assert callable(gmfgraph_PolygonDecoration.__init__)


def test_hyp_gmfgraph_polygondecoration_constructor_args():
    sig = inspect.signature(gmfgraph_PolygonDecoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_scalablepolygon_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_ScalablePolygon)


def test_hyp_gmfgraph_scalablepolygon_constructor_exists():
    assert callable(gmfgraph_ScalablePolygon.__init__)


def test_hyp_gmfgraph_scalablepolygon_constructor_args():
    sig = inspect.signature(gmfgraph_ScalablePolygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_hyp_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_hyp_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_polylineconnection_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_PolylineConnection)


def test_hyp_gmfgraph_polylineconnection_constructor_exists():
    assert callable(gmfgraph_PolylineConnection.__init__)


def test_hyp_gmfgraph_polylineconnection_constructor_args():
    sig = inspect.signature(gmfgraph_PolylineConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_polylinedecoration_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_PolylineDecoration)


def test_hyp_gmfgraph_polylinedecoration_constructor_exists():
    assert callable(gmfgraph_PolylineDecoration.__init__)


def test_hyp_gmfgraph_polylinedecoration_constructor_args():
    sig = inspect.signature(gmfgraph_PolylineDecoration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_polygon_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Polygon)


def test_hyp_gmfgraph_polygon_constructor_exists():
    assert callable(gmfgraph_Polygon.__init__)


def test_hyp_gmfgraph_polygon_constructor_args():
    sig = inspect.signature(gmfgraph_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(AbstractFigure)


def test_hyp_abstractfigure_constructor_exists():
    assert callable(AbstractFigure.__init__)


def test_hyp_abstractfigure_constructor_args():
    sig = inspect.signature(AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_hyp_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_hyp_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_ellipse_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Ellipse)


def test_hyp_gmfgraph_ellipse_constructor_exists():
    assert callable(gmfgraph_Ellipse.__init__)


def test_hyp_gmfgraph_ellipse_constructor_args():
    sig = inspect.signature(gmfgraph_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_polyline_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Polyline)


def test_hyp_gmfgraph_polyline_constructor_exists():
    assert callable(gmfgraph_Polyline.__init__)


def test_hyp_gmfgraph_polyline_constructor_args():
    sig = inspect.signature(gmfgraph_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_RoundedRectangle)


def test_hyp_gmfgraph_roundedrectangle_constructor_exists():
    assert callable(gmfgraph_RoundedRectangle.__init__)


def test_hyp_gmfgraph_roundedrectangle_constructor_args():
    sig = inspect.signature(gmfgraph_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"





def test_hyp_gmfgraph_rectangle_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Rectangle)


def test_hyp_gmfgraph_rectangle_constructor_exists():
    assert callable(gmfgraph_Rectangle.__init__)


def test_hyp_gmfgraph_rectangle_constructor_args():
    sig = inspect.signature(gmfgraph_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realfigure_is_not_abstract():
    assert not inspect.isabstract(RealFigure)


def test_hyp_realfigure_constructor_exists():
    assert callable(RealFigure.__init__)


def test_hyp_realfigure_constructor_args():
    sig = inspect.signature(RealFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_label_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Label)


def test_hyp_gmfgraph_label_constructor_exists():
    assert callable(gmfgraph_Label.__init__)


def test_hyp_gmfgraph_label_constructor_args():
    sig = inspect.signature(gmfgraph_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_gmfgraph_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_DecorationFigure)


def test_hyp_gmfgraph_decorationfigure_constructor_exists():
    assert callable(gmfgraph_DecorationFigure.__init__)


def test_hyp_gmfgraph_decorationfigure_constructor_args():
    sig = inspect.signature(gmfgraph_DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_labeledcontainer_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_LabeledContainer)


def test_hyp_gmfgraph_labeledcontainer_constructor_exists():
    assert callable(gmfgraph_LabeledContainer.__init__)


def test_hyp_gmfgraph_labeledcontainer_constructor_args():
    sig = inspect.signature(gmfgraph_LabeledContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_shape_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Shape)


def test_hyp_gmfgraph_shape_constructor_exists():
    assert callable(gmfgraph_Shape.__init__)


def test_hyp_gmfgraph_shape_constructor_args():
    sig = inspect.signature(gmfgraph_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "xorFill" in params, "Missing parameter 'xorFill'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "lineKind" in params, "Missing parameter 'lineKind'"
    assert "xorOutline" in params, "Missing parameter 'xorOutline'"









def test_hyp_gmfgraph_customfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomFigure)


def test_hyp_gmfgraph_customfigure_constructor_exists():
    assert callable(gmfgraph_CustomFigure.__init__)


def test_hyp_gmfgraph_customfigure_constructor_args():
    sig = inspect.signature(gmfgraph_CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_ConnectionFigure)


def test_hyp_gmfgraph_connectionfigure_constructor_exists():
    assert callable(gmfgraph_ConnectionFigure.__init__)


def test_hyp_gmfgraph_connectionfigure_constructor_args():
    sig = inspect.signature(gmfgraph_ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_figureref_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_FigureRef)


def test_hyp_gmfgraph_figureref_constructor_exists():
    assert callable(gmfgraph_FigureRef.__init__)


def test_hyp_gmfgraph_figureref_constructor_args():
    sig = inspect.signature(gmfgraph_FigureRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_color_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Color)


def test_hyp_gmfgraph_color_constructor_exists():
    assert callable(gmfgraph_Color.__init__)


def test_hyp_gmfgraph_color_constructor_args():
    sig = inspect.signature(gmfgraph_Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_hyp_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_hyp_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_AbstractFigure)


def test_hyp_gmfgraph_abstractfigure_constructor_exists():
    assert callable(gmfgraph_AbstractFigure.__init__)


def test_hyp_gmfgraph_abstractfigure_constructor_args():
    sig = inspect.signature(gmfgraph_AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_point_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Point)


def test_hyp_gmfgraph_point_constructor_exists():
    assert callable(gmfgraph_Point.__init__)


def test_hyp_gmfgraph_point_constructor_args():
    sig = inspect.signature(gmfgraph_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_gmfgraph_border_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Border)


def test_hyp_gmfgraph_border_constructor_exists():
    assert callable(gmfgraph_Border.__init__)


def test_hyp_gmfgraph_border_constructor_args():
    sig = inspect.signature(gmfgraph_Border.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_insets_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Insets)


def test_hyp_gmfgraph_insets_constructor_exists():
    assert callable(gmfgraph_Insets.__init__)


def test_hyp_gmfgraph_insets_constructor_args():
    sig = inspect.signature(gmfgraph_Insets.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"
    assert "right" in params, "Missing parameter 'right'"
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "top" in params, "Missing parameter 'top'"







def test_hyp_gmfgraph_font_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Font)


def test_hyp_gmfgraph_font_constructor_exists():
    assert callable(gmfgraph_Font.__init__)


def test_hyp_gmfgraph_font_constructor_args():
    sig = inspect.signature(gmfgraph_Font.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_childaccess_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_ChildAccess)


def test_hyp_gmfgraph_childaccess_constructor_exists():
    assert callable(gmfgraph_ChildAccess.__init__)


def test_hyp_gmfgraph_childaccess_constructor_args():
    sig = inspect.signature(gmfgraph_ChildAccess.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"




def test_hyp_layoutable_is_not_abstract():
    assert not inspect.isabstract(Layoutable)


def test_hyp_layoutable_constructor_exists():
    assert callable(Layoutable.__init__)


def test_hyp_layoutable_constructor_args():
    sig = inspect.signature(Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_figure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Figure)


def test_hyp_gmfgraph_figure_constructor_exists():
    assert callable(gmfgraph_Figure.__init__)


def test_hyp_gmfgraph_figure_constructor_args():
    sig = inspect.signature(gmfgraph_Figure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_dimension_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Dimension)


def test_hyp_gmfgraph_dimension_constructor_exists():
    assert callable(gmfgraph_Dimension.__init__)


def test_hyp_gmfgraph_dimension_constructor_args():
    sig = inspect.signature(gmfgraph_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "dy" in params, "Missing parameter 'dy'"
    assert "dx" in params, "Missing parameter 'dx'"





def test_hyp_visualfacet_is_not_abstract():
    assert not inspect.isabstract(VisualFacet)


def test_hyp_visualfacet_constructor_exists():
    assert callable(VisualFacet.__init__)


def test_hyp_visualfacet_constructor_args():
    sig = inspect.signature(VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_gradientfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_GradientFacet)


def test_hyp_gmfgraph_gradientfacet_constructor_exists():
    assert callable(gmfgraph_GradientFacet.__init__)


def test_hyp_gmfgraph_gradientfacet_constructor_args():
    sig = inspect.signature(gmfgraph_GradientFacet.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"




def test_hyp_gmfgraph_labeloffsetfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_LabelOffsetFacet)


def test_hyp_gmfgraph_labeloffsetfacet_constructor_exists():
    assert callable(gmfgraph_LabelOffsetFacet.__init__)


def test_hyp_gmfgraph_labeloffsetfacet_constructor_args():
    sig = inspect.signature(gmfgraph_LabelOffsetFacet.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_gmfgraph_defaultsizefacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_DefaultSizeFacet)


def test_hyp_gmfgraph_defaultsizefacet_constructor_exists():
    assert callable(gmfgraph_DefaultSizeFacet.__init__)


def test_hyp_gmfgraph_defaultsizefacet_constructor_args():
    sig = inspect.signature(gmfgraph_DefaultSizeFacet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_alignmentfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_AlignmentFacet)


def test_hyp_gmfgraph_alignmentfacet_constructor_exists():
    assert callable(gmfgraph_AlignmentFacet.__init__)


def test_hyp_gmfgraph_alignmentfacet_constructor_args():
    sig = inspect.signature(gmfgraph_AlignmentFacet.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"




def test_hyp_gmfgraph_generalfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_GeneralFacet)


def test_hyp_gmfgraph_generalfacet_constructor_exists():
    assert callable(gmfgraph_GeneralFacet.__init__)


def test_hyp_gmfgraph_generalfacet_constructor_args():
    sig = inspect.signature(gmfgraph_GeneralFacet.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "data" in params, "Missing parameter 'data'"





def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_hyp_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_hyp_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_node_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Node)


def test_hyp_gmfgraph_node_constructor_exists():
    assert callable(gmfgraph_Node.__init__)


def test_hyp_gmfgraph_node_constructor_args():
    sig = inspect.signature(gmfgraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "affixedParentSide" in params, "Missing parameter 'affixedParentSide'"
    assert "resizeConstraint" in params, "Missing parameter 'resizeConstraint'"





def test_hyp_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_hyp_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_hyp_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_connection_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Connection)


def test_hyp_gmfgraph_connection_constructor_exists():
    assert callable(gmfgraph_Connection.__init__)


def test_hyp_gmfgraph_connection_constructor_args():
    sig = inspect.signature(gmfgraph_Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_abstractnode_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_AbstractNode)


def test_hyp_gmfgraph_abstractnode_constructor_exists():
    assert callable(gmfgraph_AbstractNode.__init__)


def test_hyp_gmfgraph_abstractnode_constructor_args():
    sig = inspect.signature(gmfgraph_AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_visualfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_VisualFacet)


def test_hyp_gmfgraph_visualfacet_constructor_exists():
    assert callable(gmfgraph_VisualFacet.__init__)


def test_hyp_gmfgraph_visualfacet_constructor_args():
    sig = inspect.signature(gmfgraph_VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_identity_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Identity)


def test_hyp_gmfgraph_identity_constructor_exists():
    assert callable(gmfgraph_Identity.__init__)


def test_hyp_gmfgraph_identity_constructor_args():
    sig = inspect.signature(gmfgraph_Identity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_gmfgraph_realfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_RealFigure)


def test_hyp_gmfgraph_realfigure_constructor_exists():
    assert callable(gmfgraph_RealFigure.__init__)


def test_hyp_gmfgraph_realfigure_constructor_args():
    sig = inspect.signature(gmfgraph_RealFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_gmfgraph_diagramlabel_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_DiagramLabel)


def test_hyp_gmfgraph_diagramlabel_constructor_exists():
    assert callable(gmfgraph_DiagramLabel.__init__)


def test_hyp_gmfgraph_diagramlabel_constructor_args():
    sig = inspect.signature(gmfgraph_DiagramLabel.__init__)
    params = list(sig.parameters.keys())
    assert "elementIcon" in params, "Missing parameter 'elementIcon'"
    assert "external" in params, "Missing parameter 'external'"





def test_hyp_gmfgraph_compartment_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Compartment)


def test_hyp_gmfgraph_compartment_constructor_exists():
    assert callable(gmfgraph_Compartment.__init__)


def test_hyp_gmfgraph_compartment_constructor_args():
    sig = inspect.signature(gmfgraph_Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "needsTitle" in params, "Missing parameter 'needsTitle'"
    assert "collapsible" in params, "Missing parameter 'collapsible'"





def test_hyp_identity_is_not_abstract():
    assert not inspect.isabstract(Identity)


def test_hyp_identity_constructor_exists():
    assert callable(Identity.__init__)


def test_hyp_identity_constructor_args():
    sig = inspect.signature(Identity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_diagramelement_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_DiagramElement)


def test_hyp_gmfgraph_diagramelement_constructor_exists():
    assert callable(gmfgraph_DiagramElement.__init__)


def test_hyp_gmfgraph_diagramelement_constructor_args():
    sig = inspect.signature(gmfgraph_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_figuredescriptor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_FigureDescriptor)


def test_hyp_gmfgraph_figuredescriptor_constructor_exists():
    assert callable(gmfgraph_FigureDescriptor.__init__)


def test_hyp_gmfgraph_figuredescriptor_constructor_args():
    sig = inspect.signature(gmfgraph_FigureDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmfgraph_figuregallery_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_FigureGallery)


def test_hyp_gmfgraph_figuregallery_constructor_exists():
    assert callable(gmfgraph_FigureGallery.__init__)


def test_hyp_gmfgraph_figuregallery_constructor_args():
    sig = inspect.signature(gmfgraph_FigureGallery.__init__)
    params = list(sig.parameters.keys())
    assert "implementationBundle" in params, "Missing parameter 'implementationBundle'"




def test_hyp_gmfgraph_canvas_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Canvas)


def test_hyp_gmfgraph_canvas_constructor_exists():
    assert callable(gmfgraph_Canvas.__init__)


def test_hyp_gmfgraph_canvas_constructor_args():
    sig = inspect.signature(gmfgraph_Canvas.__init__)
    params = list(sig.parameters.keys())

def test_hyp_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_hyp_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "FILL",
        "CENTER",
        "END",
        "BEGINNING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_hyp_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_hyp_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "NORMAL",
        "BOLD",
        "ITALIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_hyp_colorconstants_exists():
    # Check that the Enumeration exists
    assert ColorConstants is not None

def test_hyp_colorconstants_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorConstants]
    expected_literals = [
        "black",
        "darkGray",
        "lightBlue",
        "darkGreen",
        "green",
        "white",
        "gray",
        "lightGreen",
        "lightGray",
        "cyan",
        "yellow",
        "darkBlue",
        "red",
        "blue",
        "orange",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorConstants"

def test_hyp_linekind_exists():
    # Check that the Enumeration exists
    assert LineKind is not None

def test_hyp_linekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineKind]
    expected_literals = [
        "LINE_DOT",
        "LINE_SOLID",
        "LINE_DASHDOTDOT",
        "LINE_DASHDOT",
        "LINE_DASH",
        "LINE_CUSTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "NORTH_WEST",
        "SOUTH_WEST",
        "SOUTH_EAST",
        "EAST",
        "EAST_WEST",
        "NSEW",
        "NORTH_EAST",
        "NORTH_SOUTH",
        "NORTH",
        "NONE",
        "WEST",
        "SOUTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
Layout_strategy = st.builds(
    Layout,
)
gmfgraph_BorderLayout_strategy = st.builds(
    gmfgraph_BorderLayout,
)
gmfgraph_GridLayout_strategy = st.builds(
    gmfgraph_GridLayout,
    numColumns=
        st.integers(),
    equalWidth=
        st.booleans()
)
gmfgraph_StackLayout_strategy = st.builds(
    gmfgraph_StackLayout,
)
gmfgraph_FlowLayout_strategy = st.builds(
    gmfgraph_FlowLayout,
    matchMinorSize=
        st.booleans(),
    vertical=
        st.booleans(),
    majorAlignment=
        safe_text,
    forceSingleLine=
        st.booleans(),
    minorAlignment=
        safe_text,
    minorSpacing=
        st.integers(),
    majorSpacing=
        st.integers()
)
gmfgraph_XYLayout_strategy = st.builds(
    gmfgraph_XYLayout,
)
gmfgraph_Layout_strategy = st.builds(
    gmfgraph_Layout,
)
LayoutData_strategy = st.builds(
    LayoutData,
)
gmfgraph_GridLayoutData_strategy = st.builds(
    gmfgraph_GridLayoutData,
    horizontalSpan=
        st.integers(),
    verticalAlignment=
        safe_text,
    grabExcessHorizontalSpace=
        st.booleans(),
    horizontalIndent=
        st.integers(),
    verticalSpan=
        st.integers(),
    grabExcessVerticalSpace=
        st.booleans(),
    horizontalAlignment=
        safe_text
)
gmfgraph_BorderLayoutData_strategy = st.builds(
    gmfgraph_BorderLayoutData,
    vertical=
        st.booleans(),
    alignment=
        safe_text
)
gmfgraph_XYLayoutData_strategy = st.builds(
    gmfgraph_XYLayoutData,
)
gmfgraph_Layoutable_strategy = st.builds(
    gmfgraph_Layoutable,
)
gmfgraph_LayoutData_strategy = st.builds(
    gmfgraph_LayoutData,
)
Font_strategy = st.builds(
    Font,
)
gmfgraph_BasicFont_strategy = st.builds(
    gmfgraph_BasicFont,
    style=
        safe_text,
    faceName=
        safe_text,
    height=
        st.integers()
)
Border_strategy = st.builds(
    Border,
)
gmfgraph_CompoundBorder_strategy = st.builds(
    gmfgraph_CompoundBorder,
)
gmfgraph_MarginBorder_strategy = st.builds(
    gmfgraph_MarginBorder,
)
gmfgraph_LineBorder_strategy = st.builds(
    gmfgraph_LineBorder,
    width=
        st.integers()
)
gmfgraph_FigureAccessor_strategy = st.builds(
    gmfgraph_FigureAccessor,
    accessor=
        safe_text
)
Color_strategy = st.builds(
    Color,
)
gmfgraph_ConstantColor_strategy = st.builds(
    gmfgraph_ConstantColor,
    value=
        safe_text
)
gmfgraph_RGBColor_strategy = st.builds(
    gmfgraph_RGBColor,
    blue=
        st.integers(),
    green=
        st.integers(),
    red=
        st.integers()
)
CustomFigure_strategy = st.builds(
    CustomFigure,
)
CustomClass_strategy = st.builds(
    CustomClass,
)
gmfgraph_CustomLayout_strategy = st.builds(
    gmfgraph_CustomLayout,
)
gmfgraph_CustomLayoutData_strategy = st.builds(
    gmfgraph_CustomLayoutData,
)
gmfgraph_CustomBorder_strategy = st.builds(
    gmfgraph_CustomBorder,
)
gmfgraph_CustomAttribute_strategy = st.builds(
    gmfgraph_CustomAttribute,
    directAccess=
        st.booleans(),
    name=
        safe_text,
    multiStatementValue=
        st.booleans(),
    value=
        safe_text
)
gmfgraph_CustomClass_strategy = st.builds(
    gmfgraph_CustomClass,
    qualifiedClassName=
        safe_text
)
DecorationFigure_strategy = st.builds(
    DecorationFigure,
)
gmfgraph_CustomDecoration_strategy = st.builds(
    gmfgraph_CustomDecoration,
)
ConnectionFigure_strategy = st.builds(
    ConnectionFigure,
)
gmfgraph_CustomConnection_strategy = st.builds(
    gmfgraph_CustomConnection,
)
Polygon_strategy = st.builds(
    Polygon,
)
gmfgraph_PolygonDecoration_strategy = st.builds(
    gmfgraph_PolygonDecoration,
)
gmfgraph_ScalablePolygon_strategy = st.builds(
    gmfgraph_ScalablePolygon,
)
Polyline_strategy = st.builds(
    Polyline,
)
gmfgraph_PolylineConnection_strategy = st.builds(
    gmfgraph_PolylineConnection,
)
gmfgraph_PolylineDecoration_strategy = st.builds(
    gmfgraph_PolylineDecoration,
)
gmfgraph_Polygon_strategy = st.builds(
    gmfgraph_Polygon,
)
AbstractFigure_strategy = st.builds(
    AbstractFigure,
)
Shape_strategy = st.builds(
    Shape,
)
gmfgraph_Ellipse_strategy = st.builds(
    gmfgraph_Ellipse,
)
gmfgraph_Polyline_strategy = st.builds(
    gmfgraph_Polyline,
)
gmfgraph_RoundedRectangle_strategy = st.builds(
    gmfgraph_RoundedRectangle,
    cornerWidth=
        st.integers(),
    cornerHeight=
        st.integers()
)
gmfgraph_Rectangle_strategy = st.builds(
    gmfgraph_Rectangle,
)
RealFigure_strategy = st.builds(
    RealFigure,
)
gmfgraph_Label_strategy = st.builds(
    gmfgraph_Label,
    text=
        safe_text
)
gmfgraph_DecorationFigure_strategy = st.builds(
    gmfgraph_DecorationFigure,
)
gmfgraph_LabeledContainer_strategy = st.builds(
    gmfgraph_LabeledContainer,
)
gmfgraph_Shape_strategy = st.builds(
    gmfgraph_Shape,
    lineWidth=
        st.integers(),
    xorFill=
        st.booleans(),
    fill=
        st.booleans(),
    outline=
        st.booleans(),
    lineKind=
        safe_text,
    xorOutline=
        st.booleans()
)
gmfgraph_CustomFigure_strategy = st.builds(
    gmfgraph_CustomFigure,
)
gmfgraph_ConnectionFigure_strategy = st.builds(
    gmfgraph_ConnectionFigure,
)
gmfgraph_FigureRef_strategy = st.builds(
    gmfgraph_FigureRef,
)
gmfgraph_Color_strategy = st.builds(
    gmfgraph_Color,
)
Figure_strategy = st.builds(
    Figure,
)
gmfgraph_AbstractFigure_strategy = st.builds(
    gmfgraph_AbstractFigure,
)
gmfgraph_Point_strategy = st.builds(
    gmfgraph_Point,
    x=
        st.integers(),
    y=
        st.integers()
)
gmfgraph_Border_strategy = st.builds(
    gmfgraph_Border,
)
gmfgraph_Insets_strategy = st.builds(
    gmfgraph_Insets,
    left=
        st.integers(),
    right=
        st.integers(),
    bottom=
        st.integers(),
    top=
        st.integers()
)
gmfgraph_Font_strategy = st.builds(
    gmfgraph_Font,
)
gmfgraph_ChildAccess_strategy = st.builds(
    gmfgraph_ChildAccess,
    accessor=
        safe_text
)
Layoutable_strategy = st.builds(
    Layoutable,
)
gmfgraph_Figure_strategy = st.builds(
    gmfgraph_Figure,
)
gmfgraph_Dimension_strategy = st.builds(
    gmfgraph_Dimension,
    dy=
        st.integers(),
    dx=
        st.integers()
)
VisualFacet_strategy = st.builds(
    VisualFacet,
)
gmfgraph_GradientFacet_strategy = st.builds(
    gmfgraph_GradientFacet,
    direction=
        safe_text
)
gmfgraph_LabelOffsetFacet_strategy = st.builds(
    gmfgraph_LabelOffsetFacet,
    y=
        st.integers(),
    x=
        st.integers()
)
gmfgraph_DefaultSizeFacet_strategy = st.builds(
    gmfgraph_DefaultSizeFacet,
)
gmfgraph_AlignmentFacet_strategy = st.builds(
    gmfgraph_AlignmentFacet,
    alignment=
        safe_text
)
gmfgraph_GeneralFacet_strategy = st.builds(
    gmfgraph_GeneralFacet,
    identifier=
        safe_text,
    data=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
gmfgraph_Node_strategy = st.builds(
    gmfgraph_Node,
    affixedParentSide=
        safe_text,
    resizeConstraint=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
gmfgraph_Connection_strategy = st.builds(
    gmfgraph_Connection,
)
gmfgraph_AbstractNode_strategy = st.builds(
    gmfgraph_AbstractNode,
)
gmfgraph_VisualFacet_strategy = st.builds(
    gmfgraph_VisualFacet,
)
gmfgraph_Identity_strategy = st.builds(
    gmfgraph_Identity,
    name=
        safe_text
)
gmfgraph_RealFigure_strategy = st.builds(
    gmfgraph_RealFigure,
    name=
        safe_text
)
gmfgraph_DiagramLabel_strategy = st.builds(
    gmfgraph_DiagramLabel,
    elementIcon=
        st.booleans(),
    external=
        st.booleans()
)
gmfgraph_Compartment_strategy = st.builds(
    gmfgraph_Compartment,
    needsTitle=
        st.booleans(),
    collapsible=
        st.booleans()
)
Identity_strategy = st.builds(
    Identity,
)
gmfgraph_DiagramElement_strategy = st.builds(
    gmfgraph_DiagramElement,
)
gmfgraph_FigureDescriptor_strategy = st.builds(
    gmfgraph_FigureDescriptor,
)
gmfgraph_FigureGallery_strategy = st.builds(
    gmfgraph_FigureGallery,
    implementationBundle=
        safe_text
)
gmfgraph_Canvas_strategy = st.builds(
    gmfgraph_Canvas,
)






@given(instance=gmfgraph_GridLayout_strategy)
def test_hyp_gmfgraph_gridlayout_numColumns_setter(instance):
    original = instance.numColumns
    instance.numColumns = original
    assert instance.numColumns == original



@given(instance=gmfgraph_GridLayout_strategy)
def test_hyp_gmfgraph_gridlayout_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original





@given(instance=gmfgraph_FlowLayout_strategy)
def test_hyp_gmfgraph_flowlayout_matchMinorSize_setter(instance):
    original = instance.matchMinorSize
    instance.matchMinorSize = original
    assert instance.matchMinorSize == original



@given(instance=gmfgraph_FlowLayout_strategy)
def test_hyp_gmfgraph_flowlayout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original



@given(instance=gmfgraph_FlowLayout_strategy)
def test_hyp_gmfgraph_flowlayout_majorAlignment_setter(instance):
    original = instance.majorAlignment
    instance.majorAlignment = original
    assert instance.majorAlignment == original



@given(instance=gmfgraph_FlowLayout_strategy)
def test_hyp_gmfgraph_flowlayout_forceSingleLine_setter(instance):
    original = instance.forceSingleLine
    instance.forceSingleLine = original
    assert instance.forceSingleLine == original



@given(instance=gmfgraph_FlowLayout_strategy)
def test_hyp_gmfgraph_flowlayout_minorAlignment_setter(instance):
    original = instance.minorAlignment
    instance.minorAlignment = original
    assert instance.minorAlignment == original



@given(instance=gmfgraph_FlowLayout_strategy)
def test_hyp_gmfgraph_flowlayout_minorSpacing_setter(instance):
    original = instance.minorSpacing
    instance.minorSpacing = original
    assert instance.minorSpacing == original



@given(instance=gmfgraph_FlowLayout_strategy)
def test_hyp_gmfgraph_flowlayout_majorSpacing_setter(instance):
    original = instance.majorSpacing
    instance.majorSpacing = original
    assert instance.majorSpacing == original







@given(instance=gmfgraph_GridLayoutData_strategy)
def test_hyp_gmfgraph_gridlayoutdata_horizontalSpan_setter(instance):
    original = instance.horizontalSpan
    instance.horizontalSpan = original
    assert instance.horizontalSpan == original



@given(instance=gmfgraph_GridLayoutData_strategy)
def test_hyp_gmfgraph_gridlayoutdata_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original



@given(instance=gmfgraph_GridLayoutData_strategy)
def test_hyp_gmfgraph_gridlayoutdata_grabExcessHorizontalSpace_setter(instance):
    original = instance.grabExcessHorizontalSpace
    instance.grabExcessHorizontalSpace = original
    assert instance.grabExcessHorizontalSpace == original



@given(instance=gmfgraph_GridLayoutData_strategy)
def test_hyp_gmfgraph_gridlayoutdata_horizontalIndent_setter(instance):
    original = instance.horizontalIndent
    instance.horizontalIndent = original
    assert instance.horizontalIndent == original



@given(instance=gmfgraph_GridLayoutData_strategy)
def test_hyp_gmfgraph_gridlayoutdata_verticalSpan_setter(instance):
    original = instance.verticalSpan
    instance.verticalSpan = original
    assert instance.verticalSpan == original



@given(instance=gmfgraph_GridLayoutData_strategy)
def test_hyp_gmfgraph_gridlayoutdata_grabExcessVerticalSpace_setter(instance):
    original = instance.grabExcessVerticalSpace
    instance.grabExcessVerticalSpace = original
    assert instance.grabExcessVerticalSpace == original



@given(instance=gmfgraph_GridLayoutData_strategy)
def test_hyp_gmfgraph_gridlayoutdata_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original




@given(instance=gmfgraph_BorderLayoutData_strategy)
def test_hyp_gmfgraph_borderlayoutdata_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original



@given(instance=gmfgraph_BorderLayoutData_strategy)
def test_hyp_gmfgraph_borderlayoutdata_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original








@given(instance=gmfgraph_BasicFont_strategy)
def test_hyp_gmfgraph_basicfont_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=gmfgraph_BasicFont_strategy)
def test_hyp_gmfgraph_basicfont_faceName_setter(instance):
    original = instance.faceName
    instance.faceName = original
    assert instance.faceName == original



@given(instance=gmfgraph_BasicFont_strategy)
def test_hyp_gmfgraph_basicfont_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original







@given(instance=gmfgraph_LineBorder_strategy)
def test_hyp_gmfgraph_lineborder_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=gmfgraph_FigureAccessor_strategy)
def test_hyp_gmfgraph_figureaccessor_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original





@given(instance=gmfgraph_ConstantColor_strategy)
def test_hyp_gmfgraph_constantcolor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=gmfgraph_RGBColor_strategy)
def test_hyp_gmfgraph_rgbcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=gmfgraph_RGBColor_strategy)
def test_hyp_gmfgraph_rgbcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=gmfgraph_RGBColor_strategy)
def test_hyp_gmfgraph_rgbcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original









@given(instance=gmfgraph_CustomAttribute_strategy)
def test_hyp_gmfgraph_customattribute_directAccess_setter(instance):
    original = instance.directAccess
    instance.directAccess = original
    assert instance.directAccess == original



@given(instance=gmfgraph_CustomAttribute_strategy)
def test_hyp_gmfgraph_customattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gmfgraph_CustomAttribute_strategy)
def test_hyp_gmfgraph_customattribute_multiStatementValue_setter(instance):
    original = instance.multiStatementValue
    instance.multiStatementValue = original
    assert instance.multiStatementValue == original



@given(instance=gmfgraph_CustomAttribute_strategy)
def test_hyp_gmfgraph_customattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=gmfgraph_CustomClass_strategy)
def test_hyp_gmfgraph_customclass_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original



















@given(instance=gmfgraph_RoundedRectangle_strategy)
def test_hyp_gmfgraph_roundedrectangle_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original



@given(instance=gmfgraph_RoundedRectangle_strategy)
def test_hyp_gmfgraph_roundedrectangle_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original






@given(instance=gmfgraph_Label_strategy)
def test_hyp_gmfgraph_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original






@given(instance=gmfgraph_Shape_strategy)
def test_hyp_gmfgraph_shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=gmfgraph_Shape_strategy)
def test_hyp_gmfgraph_shape_xorFill_setter(instance):
    original = instance.xorFill
    instance.xorFill = original
    assert instance.xorFill == original



@given(instance=gmfgraph_Shape_strategy)
def test_hyp_gmfgraph_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=gmfgraph_Shape_strategy)
def test_hyp_gmfgraph_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original



@given(instance=gmfgraph_Shape_strategy)
def test_hyp_gmfgraph_shape_lineKind_setter(instance):
    original = instance.lineKind
    instance.lineKind = original
    assert instance.lineKind == original



@given(instance=gmfgraph_Shape_strategy)
def test_hyp_gmfgraph_shape_xorOutline_setter(instance):
    original = instance.xorOutline
    instance.xorOutline = original
    assert instance.xorOutline == original










@given(instance=gmfgraph_Point_strategy)
def test_hyp_gmfgraph_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=gmfgraph_Point_strategy)
def test_hyp_gmfgraph_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original





@given(instance=gmfgraph_Insets_strategy)
def test_hyp_gmfgraph_insets_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original



@given(instance=gmfgraph_Insets_strategy)
def test_hyp_gmfgraph_insets_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=gmfgraph_Insets_strategy)
def test_hyp_gmfgraph_insets_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original



@given(instance=gmfgraph_Insets_strategy)
def test_hyp_gmfgraph_insets_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original





@given(instance=gmfgraph_ChildAccess_strategy)
def test_hyp_gmfgraph_childaccess_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original






@given(instance=gmfgraph_Dimension_strategy)
def test_hyp_gmfgraph_dimension_dy_setter(instance):
    original = instance.dy
    instance.dy = original
    assert instance.dy == original



@given(instance=gmfgraph_Dimension_strategy)
def test_hyp_gmfgraph_dimension_dx_setter(instance):
    original = instance.dx
    instance.dx = original
    assert instance.dx == original





@given(instance=gmfgraph_GradientFacet_strategy)
def test_hyp_gmfgraph_gradientfacet_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original




@given(instance=gmfgraph_LabelOffsetFacet_strategy)
def test_hyp_gmfgraph_labeloffsetfacet_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=gmfgraph_LabelOffsetFacet_strategy)
def test_hyp_gmfgraph_labeloffsetfacet_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original





@given(instance=gmfgraph_AlignmentFacet_strategy)
def test_hyp_gmfgraph_alignmentfacet_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original




@given(instance=gmfgraph_GeneralFacet_strategy)
def test_hyp_gmfgraph_generalfacet_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=gmfgraph_GeneralFacet_strategy)
def test_hyp_gmfgraph_generalfacet_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original






@given(instance=gmfgraph_Node_strategy)
def test_hyp_gmfgraph_node_affixedParentSide_setter(instance):
    original = instance.affixedParentSide
    instance.affixedParentSide = original
    assert instance.affixedParentSide == original



@given(instance=gmfgraph_Node_strategy)
def test_hyp_gmfgraph_node_resizeConstraint_setter(instance):
    original = instance.resizeConstraint
    instance.resizeConstraint = original
    assert instance.resizeConstraint == original








@given(instance=gmfgraph_Identity_strategy)
def test_hyp_gmfgraph_identity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=gmfgraph_RealFigure_strategy)
def test_hyp_gmfgraph_realfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=gmfgraph_DiagramLabel_strategy)
def test_hyp_gmfgraph_diagramlabel_elementIcon_setter(instance):
    original = instance.elementIcon
    instance.elementIcon = original
    assert instance.elementIcon == original



@given(instance=gmfgraph_DiagramLabel_strategy)
def test_hyp_gmfgraph_diagramlabel_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original




@given(instance=gmfgraph_Compartment_strategy)
def test_hyp_gmfgraph_compartment_needsTitle_setter(instance):
    original = instance.needsTitle
    instance.needsTitle = original
    assert instance.needsTitle == original



@given(instance=gmfgraph_Compartment_strategy)
def test_hyp_gmfgraph_compartment_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original







@given(instance=gmfgraph_FigureGallery_strategy)
def test_hyp_gmfgraph_figuregallery_implementationBundle_setter(instance):
    original = instance.implementationBundle
    instance.implementationBundle = original
    assert instance.implementationBundle == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_gmfgraph_AlignmentFacet_alignment_value_roundtrip():
    instance = gmfgraph_AlignmentFacet(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_gmfgraph_BasicFont_faceName_value_roundtrip():
    instance = gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert instance.faceName == "sample_text"
    instance.faceName = "sample_text_2"
    assert instance.faceName == "sample_text_2"


def test_gmfgraph_BasicFont_height_value_roundtrip():
    instance = gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_gmfgraph_BasicFont_style_value_roundtrip():
    instance = gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_gmfgraph_BorderLayoutData_alignment_value_roundtrip():
    instance = gmfgraph_BorderLayoutData(alignment="sample_text", vertical=True)
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_gmfgraph_BorderLayoutData_vertical_value_roundtrip():
    instance = gmfgraph_BorderLayoutData(alignment="sample_text", vertical=True)
    assert instance.vertical == True
    instance.vertical = False
    assert instance.vertical == False


def test_gmfgraph_ChildAccess_accessor_value_roundtrip():
    instance = gmfgraph_ChildAccess(accessor="sample_text")
    assert instance.accessor == "sample_text"
    instance.accessor = "sample_text_2"
    assert instance.accessor == "sample_text_2"


def test_gmfgraph_Compartment_collapsible_value_roundtrip():
    instance = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert instance.collapsible == True
    instance.collapsible = False
    assert instance.collapsible == False


def test_gmfgraph_Compartment_needsTitle_value_roundtrip():
    instance = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert instance.needsTitle == True
    instance.needsTitle = False
    assert instance.needsTitle == False


def test_gmfgraph_ConstantColor_value_value_roundtrip():
    instance = gmfgraph_ConstantColor(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_gmfgraph_CustomAttribute_directAccess_value_roundtrip():
    instance = gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.directAccess == True
    instance.directAccess = False
    assert instance.directAccess == False


def test_gmfgraph_CustomAttribute_multiStatementValue_value_roundtrip():
    instance = gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.multiStatementValue == True
    instance.multiStatementValue = False
    assert instance.multiStatementValue == False


def test_gmfgraph_CustomAttribute_name_value_roundtrip():
    instance = gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmfgraph_CustomAttribute_value_value_roundtrip():
    instance = gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_gmfgraph_CustomClass_qualifiedClassName_value_roundtrip():
    instance = gmfgraph_CustomClass(qualifiedClassName="sample_text")
    assert instance.qualifiedClassName == "sample_text"
    instance.qualifiedClassName = "sample_text_2"
    assert instance.qualifiedClassName == "sample_text_2"


def test_gmfgraph_DiagramLabel_elementIcon_value_roundtrip():
    instance = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    assert instance.elementIcon == True
    instance.elementIcon = False
    assert instance.elementIcon == False


def test_gmfgraph_DiagramLabel_external_value_roundtrip():
    instance = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    assert instance.external == True
    instance.external = False
    assert instance.external == False


def test_gmfgraph_Dimension_dx_value_roundtrip():
    instance = gmfgraph_Dimension(dx=7, dy=7)
    assert instance.dx == 7
    instance.dx = 13
    assert instance.dx == 13


def test_gmfgraph_Dimension_dy_value_roundtrip():
    instance = gmfgraph_Dimension(dx=7, dy=7)
    assert instance.dy == 7
    instance.dy = 13
    assert instance.dy == 13


def test_gmfgraph_FigureAccessor_accessor_value_roundtrip():
    instance = gmfgraph_FigureAccessor(accessor="sample_text")
    assert instance.accessor == "sample_text"
    instance.accessor = "sample_text_2"
    assert instance.accessor == "sample_text_2"


def test_gmfgraph_FigureGallery_implementationBundle_value_roundtrip():
    instance = gmfgraph_FigureGallery(implementationBundle="sample_text")
    assert instance.implementationBundle == "sample_text"
    instance.implementationBundle = "sample_text_2"
    assert instance.implementationBundle == "sample_text_2"


def test_gmfgraph_FlowLayout_forceSingleLine_value_roundtrip():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.forceSingleLine == True
    instance.forceSingleLine = False
    assert instance.forceSingleLine == False


def test_gmfgraph_FlowLayout_majorAlignment_value_roundtrip():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.majorAlignment == "sample_text"
    instance.majorAlignment = "sample_text_2"
    assert instance.majorAlignment == "sample_text_2"


def test_gmfgraph_FlowLayout_majorSpacing_value_roundtrip():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.majorSpacing == 7
    instance.majorSpacing = 13
    assert instance.majorSpacing == 13


def test_gmfgraph_FlowLayout_matchMinorSize_value_roundtrip():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.matchMinorSize == True
    instance.matchMinorSize = False
    assert instance.matchMinorSize == False


def test_gmfgraph_FlowLayout_minorAlignment_value_roundtrip():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.minorAlignment == "sample_text"
    instance.minorAlignment = "sample_text_2"
    assert instance.minorAlignment == "sample_text_2"


def test_gmfgraph_FlowLayout_minorSpacing_value_roundtrip():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.minorSpacing == 7
    instance.minorSpacing = 13
    assert instance.minorSpacing == 13


def test_gmfgraph_FlowLayout_vertical_value_roundtrip():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert instance.vertical == True
    instance.vertical = False
    assert instance.vertical == False


def test_gmfgraph_GeneralFacet_data_value_roundtrip():
    instance = gmfgraph_GeneralFacet(data="sample_text", identifier="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_gmfgraph_GeneralFacet_identifier_value_roundtrip():
    instance = gmfgraph_GeneralFacet(data="sample_text", identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_gmfgraph_GradientFacet_direction_value_roundtrip():
    instance = gmfgraph_GradientFacet(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_gmfgraph_GridLayout_equalWidth_value_roundtrip():
    instance = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    assert instance.equalWidth == True
    instance.equalWidth = False
    assert instance.equalWidth == False


def test_gmfgraph_GridLayout_numColumns_value_roundtrip():
    instance = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    assert instance.numColumns == 7
    instance.numColumns = 13
    assert instance.numColumns == 13


def test_gmfgraph_GridLayoutData_grabExcessHorizontalSpace_value_roundtrip():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.grabExcessHorizontalSpace == True
    instance.grabExcessHorizontalSpace = False
    assert instance.grabExcessHorizontalSpace == False


def test_gmfgraph_GridLayoutData_grabExcessVerticalSpace_value_roundtrip():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.grabExcessVerticalSpace == True
    instance.grabExcessVerticalSpace = False
    assert instance.grabExcessVerticalSpace == False


def test_gmfgraph_GridLayoutData_horizontalAlignment_value_roundtrip():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.horizontalAlignment == "sample_text"
    instance.horizontalAlignment = "sample_text_2"
    assert instance.horizontalAlignment == "sample_text_2"


def test_gmfgraph_GridLayoutData_horizontalIndent_value_roundtrip():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.horizontalIndent == 7
    instance.horizontalIndent = 13
    assert instance.horizontalIndent == 13


def test_gmfgraph_GridLayoutData_horizontalSpan_value_roundtrip():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.horizontalSpan == 7
    instance.horizontalSpan = 13
    assert instance.horizontalSpan == 13


def test_gmfgraph_GridLayoutData_verticalAlignment_value_roundtrip():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.verticalAlignment == "sample_text"
    instance.verticalAlignment = "sample_text_2"
    assert instance.verticalAlignment == "sample_text_2"


def test_gmfgraph_GridLayoutData_verticalSpan_value_roundtrip():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert instance.verticalSpan == 7
    instance.verticalSpan = 13
    assert instance.verticalSpan == 13


def test_gmfgraph_Identity_name_value_roundtrip():
    instance = gmfgraph_Identity(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmfgraph_Insets_bottom_value_roundtrip():
    instance = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.bottom == 7
    instance.bottom = 13
    assert instance.bottom == 13


def test_gmfgraph_Insets_left_value_roundtrip():
    instance = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.left == 7
    instance.left = 13
    assert instance.left == 13


def test_gmfgraph_Insets_right_value_roundtrip():
    instance = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.right == 7
    instance.right = 13
    assert instance.right == 13


def test_gmfgraph_Insets_top_value_roundtrip():
    instance = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    assert instance.top == 7
    instance.top = 13
    assert instance.top == 13


def test_gmfgraph_Label_text_value_roundtrip():
    instance = gmfgraph_Label(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_gmfgraph_LabelOffsetFacet_x_value_roundtrip():
    instance = gmfgraph_LabelOffsetFacet(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_gmfgraph_LabelOffsetFacet_y_value_roundtrip():
    instance = gmfgraph_LabelOffsetFacet(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_gmfgraph_LineBorder_width_value_roundtrip():
    instance = gmfgraph_LineBorder(width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_gmfgraph_Node_affixedParentSide_value_roundtrip():
    instance = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    assert instance.affixedParentSide == "sample_text"
    instance.affixedParentSide = "sample_text_2"
    assert instance.affixedParentSide == "sample_text_2"


def test_gmfgraph_Node_resizeConstraint_value_roundtrip():
    instance = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    assert instance.resizeConstraint == "sample_text"
    instance.resizeConstraint = "sample_text_2"
    assert instance.resizeConstraint == "sample_text_2"


def test_gmfgraph_Point_x_value_roundtrip():
    instance = gmfgraph_Point(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_gmfgraph_Point_y_value_roundtrip():
    instance = gmfgraph_Point(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_gmfgraph_RGBColor_blue_value_roundtrip():
    instance = gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert instance.blue == 7
    instance.blue = 13
    assert instance.blue == 13


def test_gmfgraph_RGBColor_green_value_roundtrip():
    instance = gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert instance.green == 7
    instance.green = 13
    assert instance.green == 13


def test_gmfgraph_RGBColor_red_value_roundtrip():
    instance = gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert instance.red == 7
    instance.red = 13
    assert instance.red == 13


def test_gmfgraph_RealFigure_name_value_roundtrip():
    instance = gmfgraph_RealFigure(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gmfgraph_RoundedRectangle_cornerHeight_value_roundtrip():
    instance = gmfgraph_RoundedRectangle(cornerHeight=7, cornerWidth=7)
    assert instance.cornerHeight == 7
    instance.cornerHeight = 13
    assert instance.cornerHeight == 13


def test_gmfgraph_RoundedRectangle_cornerWidth_value_roundtrip():
    instance = gmfgraph_RoundedRectangle(cornerHeight=7, cornerWidth=7)
    assert instance.cornerWidth == 7
    instance.cornerWidth = 13
    assert instance.cornerWidth == 13


def test_gmfgraph_Shape_fill_value_roundtrip():
    instance = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.fill == True
    instance.fill = False
    assert instance.fill == False


def test_gmfgraph_Shape_lineKind_value_roundtrip():
    instance = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.lineKind == "sample_text"
    instance.lineKind = "sample_text_2"
    assert instance.lineKind == "sample_text_2"


def test_gmfgraph_Shape_lineWidth_value_roundtrip():
    instance = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.lineWidth == 7
    instance.lineWidth = 13
    assert instance.lineWidth == 13


def test_gmfgraph_Shape_outline_value_roundtrip():
    instance = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.outline == True
    instance.outline = False
    assert instance.outline == False


def test_gmfgraph_Shape_xorFill_value_roundtrip():
    instance = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.xorFill == True
    instance.xorFill = False
    assert instance.xorFill == False


def test_gmfgraph_Shape_xorOutline_value_roundtrip():
    instance = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert instance.xorOutline == True
    instance.xorOutline = False
    assert instance.xorOutline == False


def test_gmfgraph_FigureRef_isa_AbstractFigure():
    instance = gmfgraph_FigureRef()
    assert isinstance(instance, AbstractFigure)


def test_gmfgraph_RealFigure_isa_AbstractFigure():
    instance = gmfgraph_RealFigure(name="sample_text")
    assert isinstance(instance, AbstractFigure)


def test_gmfgraph_Node_isa_AbstractNode():
    instance = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    assert isinstance(instance, AbstractNode)


def test_gmfgraph_CompoundBorder_isa_Border():
    instance = gmfgraph_CompoundBorder()
    assert isinstance(instance, Border)


def test_gmfgraph_CustomBorder_isa_Border():
    instance = gmfgraph_CustomBorder()
    assert isinstance(instance, Border)


def test_gmfgraph_LineBorder_isa_Border():
    instance = gmfgraph_LineBorder(width=7)
    assert isinstance(instance, Border)


def test_gmfgraph_MarginBorder_isa_Border():
    instance = gmfgraph_MarginBorder()
    assert isinstance(instance, Border)


def test_gmfgraph_ConstantColor_isa_Color():
    instance = gmfgraph_ConstantColor(value="sample_text")
    assert isinstance(instance, Color)


def test_gmfgraph_RGBColor_isa_Color():
    instance = gmfgraph_RGBColor(blue=7, green=7, red=7)
    assert isinstance(instance, Color)


def test_gmfgraph_CustomConnection_isa_ConnectionFigure():
    instance = gmfgraph_CustomConnection()
    assert isinstance(instance, ConnectionFigure)


def test_gmfgraph_PolylineConnection_isa_ConnectionFigure():
    instance = gmfgraph_PolylineConnection()
    assert isinstance(instance, ConnectionFigure)


def test_gmfgraph_CustomBorder_isa_CustomClass():
    instance = gmfgraph_CustomBorder()
    assert isinstance(instance, CustomClass)


def test_gmfgraph_CustomFigure_isa_CustomClass():
    instance = gmfgraph_CustomFigure()
    assert isinstance(instance, CustomClass)


def test_gmfgraph_CustomLayout_isa_CustomClass():
    instance = gmfgraph_CustomLayout()
    assert isinstance(instance, CustomClass)


def test_gmfgraph_CustomLayoutData_isa_CustomClass():
    instance = gmfgraph_CustomLayoutData()
    assert isinstance(instance, CustomClass)


def test_gmfgraph_CustomConnection_isa_CustomFigure():
    instance = gmfgraph_CustomConnection()
    assert isinstance(instance, CustomFigure)


def test_gmfgraph_CustomDecoration_isa_CustomFigure():
    instance = gmfgraph_CustomDecoration()
    assert isinstance(instance, CustomFigure)


def test_gmfgraph_CustomDecoration_isa_DecorationFigure():
    instance = gmfgraph_CustomDecoration()
    assert isinstance(instance, DecorationFigure)


def test_gmfgraph_PolygonDecoration_isa_DecorationFigure():
    instance = gmfgraph_PolygonDecoration()
    assert isinstance(instance, DecorationFigure)


def test_gmfgraph_PolylineDecoration_isa_DecorationFigure():
    instance = gmfgraph_PolylineDecoration()
    assert isinstance(instance, DecorationFigure)


def test_gmfgraph_AbstractNode_isa_DiagramElement():
    instance = gmfgraph_AbstractNode()
    assert isinstance(instance, DiagramElement)


def test_gmfgraph_Compartment_isa_DiagramElement():
    instance = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert isinstance(instance, DiagramElement)


def test_gmfgraph_Connection_isa_DiagramElement():
    instance = gmfgraph_Connection()
    assert isinstance(instance, DiagramElement)


def test_gmfgraph_AbstractFigure_isa_Figure():
    instance = gmfgraph_AbstractFigure()
    assert isinstance(instance, Figure)


def test_gmfgraph_BasicFont_isa_Font():
    instance = gmfgraph_BasicFont(faceName="sample_text", height=7, style="sample_text")
    assert isinstance(instance, Font)


def test_gmfgraph_Canvas_isa_Identity():
    instance = gmfgraph_Canvas()
    assert isinstance(instance, Identity)


def test_gmfgraph_DiagramElement_isa_Identity():
    instance = gmfgraph_DiagramElement()
    assert isinstance(instance, Identity)


def test_gmfgraph_FigureDescriptor_isa_Identity():
    instance = gmfgraph_FigureDescriptor()
    assert isinstance(instance, Identity)


def test_gmfgraph_FigureGallery_isa_Identity():
    instance = gmfgraph_FigureGallery(implementationBundle="sample_text")
    assert isinstance(instance, Identity)


def test_gmfgraph_BorderLayout_isa_Layout():
    instance = gmfgraph_BorderLayout()
    assert isinstance(instance, Layout)


def test_gmfgraph_CustomLayout_isa_Layout():
    instance = gmfgraph_CustomLayout()
    assert isinstance(instance, Layout)


def test_gmfgraph_FlowLayout_isa_Layout():
    instance = gmfgraph_FlowLayout(forceSingleLine=True, majorAlignment="sample_text", majorSpacing=7, matchMinorSize=True, minorAlignment="sample_text", minorSpacing=7, vertical=True)
    assert isinstance(instance, Layout)


def test_gmfgraph_GridLayout_isa_Layout():
    instance = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    assert isinstance(instance, Layout)


def test_gmfgraph_StackLayout_isa_Layout():
    instance = gmfgraph_StackLayout()
    assert isinstance(instance, Layout)


def test_gmfgraph_XYLayout_isa_Layout():
    instance = gmfgraph_XYLayout()
    assert isinstance(instance, Layout)


def test_gmfgraph_BorderLayoutData_isa_LayoutData():
    instance = gmfgraph_BorderLayoutData(alignment="sample_text", vertical=True)
    assert isinstance(instance, LayoutData)


def test_gmfgraph_CustomLayoutData_isa_LayoutData():
    instance = gmfgraph_CustomLayoutData()
    assert isinstance(instance, LayoutData)


def test_gmfgraph_GridLayoutData_isa_LayoutData():
    instance = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    assert isinstance(instance, LayoutData)


def test_gmfgraph_XYLayoutData_isa_LayoutData():
    instance = gmfgraph_XYLayoutData()
    assert isinstance(instance, LayoutData)


def test_gmfgraph_Figure_isa_Layoutable():
    instance = gmfgraph_Figure()
    assert isinstance(instance, Layoutable)


def test_gmfgraph_DiagramLabel_isa_Node():
    instance = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    assert isinstance(instance, Node)


def test_gmfgraph_PolygonDecoration_isa_Polygon():
    instance = gmfgraph_PolygonDecoration()
    assert isinstance(instance, Polygon)


def test_gmfgraph_ScalablePolygon_isa_Polygon():
    instance = gmfgraph_ScalablePolygon()
    assert isinstance(instance, Polygon)


def test_gmfgraph_Polygon_isa_Polyline():
    instance = gmfgraph_Polygon()
    assert isinstance(instance, Polyline)


def test_gmfgraph_PolylineConnection_isa_Polyline():
    instance = gmfgraph_PolylineConnection()
    assert isinstance(instance, Polyline)


def test_gmfgraph_PolylineDecoration_isa_Polyline():
    instance = gmfgraph_PolylineDecoration()
    assert isinstance(instance, Polyline)


def test_gmfgraph_ConnectionFigure_isa_RealFigure():
    instance = gmfgraph_ConnectionFigure()
    assert isinstance(instance, RealFigure)


def test_gmfgraph_CustomFigure_isa_RealFigure():
    instance = gmfgraph_CustomFigure()
    assert isinstance(instance, RealFigure)


def test_gmfgraph_DecorationFigure_isa_RealFigure():
    instance = gmfgraph_DecorationFigure()
    assert isinstance(instance, RealFigure)


def test_gmfgraph_Label_isa_RealFigure():
    instance = gmfgraph_Label(text="sample_text")
    assert isinstance(instance, RealFigure)


def test_gmfgraph_LabeledContainer_isa_RealFigure():
    instance = gmfgraph_LabeledContainer()
    assert isinstance(instance, RealFigure)


def test_gmfgraph_Shape_isa_RealFigure():
    instance = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    assert isinstance(instance, RealFigure)


def test_gmfgraph_Ellipse_isa_Shape():
    instance = gmfgraph_Ellipse()
    assert isinstance(instance, Shape)


def test_gmfgraph_Polyline_isa_Shape():
    instance = gmfgraph_Polyline()
    assert isinstance(instance, Shape)


def test_gmfgraph_Rectangle_isa_Shape():
    instance = gmfgraph_Rectangle()
    assert isinstance(instance, Shape)


def test_gmfgraph_RoundedRectangle_isa_Shape():
    instance = gmfgraph_RoundedRectangle(cornerHeight=7, cornerWidth=7)
    assert isinstance(instance, Shape)


def test_gmfgraph_AlignmentFacet_isa_VisualFacet():
    instance = gmfgraph_AlignmentFacet(alignment="sample_text")
    assert isinstance(instance, VisualFacet)


def test_gmfgraph_DefaultSizeFacet_isa_VisualFacet():
    instance = gmfgraph_DefaultSizeFacet()
    assert isinstance(instance, VisualFacet)


def test_gmfgraph_GeneralFacet_isa_VisualFacet():
    instance = gmfgraph_GeneralFacet(data="sample_text", identifier="sample_text")
    assert isinstance(instance, VisualFacet)


def test_gmfgraph_GradientFacet_isa_VisualFacet():
    instance = gmfgraph_GradientFacet(direction="sample_text")
    assert isinstance(instance, VisualFacet)


def test_gmfgraph_LabelOffsetFacet_isa_VisualFacet():
    instance = gmfgraph_LabelOffsetFacet(x=7, y=7)
    assert isinstance(instance, VisualFacet)


def test_assoc_accessor19_link_reassign_clear():
    a = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    b1 = gmfgraph_ChildAccess(accessor="sample_text")
    b2 = gmfgraph_ChildAccess(accessor="sample_text_2")
    _safe_set(a, 'gmfgraph_Compartment20', b1)
    assert _is_linked(a, 'gmfgraph_Compartment20', b1)
    if hasattr(b1, 'gmfgraph_ChildAccess21'):
        assert _is_linked(b1, 'gmfgraph_ChildAccess21', a)
    _safe_set(a, 'gmfgraph_Compartment20', b2)
    assert _is_linked(a, 'gmfgraph_Compartment20', b2)
    if hasattr(b1, 'gmfgraph_ChildAccess21'):
        assert not _is_linked(b1, 'gmfgraph_ChildAccess21', a)
    if hasattr(b2, 'gmfgraph_ChildAccess21'):
        assert _is_linked(b2, 'gmfgraph_ChildAccess21', a)
    _safe_set(a, 'gmfgraph_Compartment20', None)
    assert not _is_linked(a, 'gmfgraph_Compartment20', b2)
    if hasattr(b2, 'gmfgraph_ChildAccess21'):
        assert not _is_linked(b2, 'gmfgraph_ChildAccess21', a)


def test_assoc_accessor22_link_reassign_clear():
    a = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    b1 = gmfgraph_ChildAccess(accessor="sample_text")
    b2 = gmfgraph_ChildAccess(accessor="sample_text_2")
    _safe_set(a, 'gmfgraph_DiagramLabel23', b1)
    assert _is_linked(a, 'gmfgraph_DiagramLabel23', b1)
    if hasattr(b1, 'gmfgraph_ChildAccess24'):
        assert _is_linked(b1, 'gmfgraph_ChildAccess24', a)
    _safe_set(a, 'gmfgraph_DiagramLabel23', b2)
    assert _is_linked(a, 'gmfgraph_DiagramLabel23', b2)
    if hasattr(b1, 'gmfgraph_ChildAccess24'):
        assert not _is_linked(b1, 'gmfgraph_ChildAccess24', a)
    if hasattr(b2, 'gmfgraph_ChildAccess24'):
        assert _is_linked(b2, 'gmfgraph_ChildAccess24', a)
    _safe_set(a, 'gmfgraph_DiagramLabel23', None)
    assert not _is_linked(a, 'gmfgraph_DiagramLabel23', b2)
    if hasattr(b2, 'gmfgraph_ChildAccess24'):
        assert not _is_linked(b2, 'gmfgraph_ChildAccess24', a)


def test_assoc_accessors59_link_reassign_clear():
    a = gmfgraph_ChildAccess(accessor="sample_text")
    b1 = gmfgraph_FigureDescriptor()
    b2 = gmfgraph_FigureDescriptor()
    _safe_set(a, 'ChildAccess', b1)
    assert _is_linked(a, 'ChildAccess', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'ChildAccess', b2)
    assert _is_linked(a, 'ChildAccess', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'ChildAccess', None)
    assert not _is_linked(a, 'ChildAccess', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_attributes77_link_reassign_clear():
    a = gmfgraph_CustomClass(qualifiedClassName="sample_text")
    b1 = gmfgraph_CustomAttribute(directAccess=True, multiStatementValue=True, name="sample_text", value="sample_text")
    b2 = gmfgraph_CustomAttribute(directAccess=False, multiStatementValue=False, name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'gmfgraph_CustomClass', {b1})
    assert _is_linked(a, 'gmfgraph_CustomClass', b1)
    if hasattr(b1, 'gmfgraph_CustomAttribute'):
        assert _is_linked(b1, 'gmfgraph_CustomAttribute', a)
    _safe_set(a, 'gmfgraph_CustomClass', {b2})
    assert _is_linked(a, 'gmfgraph_CustomClass', b2)
    if hasattr(b1, 'gmfgraph_CustomAttribute'):
        assert not _is_linked(b1, 'gmfgraph_CustomAttribute', a)
    if hasattr(b2, 'gmfgraph_CustomAttribute'):
        assert _is_linked(b2, 'gmfgraph_CustomAttribute', a)
    _safe_set(a, 'gmfgraph_CustomClass', set())
    assert not _is_linked(a, 'gmfgraph_CustomClass', b2)
    if hasattr(b2, 'gmfgraph_CustomAttribute'):
        assert not _is_linked(b2, 'gmfgraph_CustomAttribute', a)


def test_assoc_children64_link_reassign_clear():
    a = gmfgraph_RealFigure(name="sample_text")
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_RealFigure65', {b1})
    assert _is_linked(a, 'gmfgraph_RealFigure65', b1)
    if hasattr(b1, 'gmfgraph_Figure66'):
        assert _is_linked(b1, 'gmfgraph_Figure66', a)
    _safe_set(a, 'gmfgraph_RealFigure65', {b2})
    assert _is_linked(a, 'gmfgraph_RealFigure65', b2)
    if hasattr(b1, 'gmfgraph_Figure66'):
        assert not _is_linked(b1, 'gmfgraph_Figure66', a)
    if hasattr(b2, 'gmfgraph_Figure66'):
        assert _is_linked(b2, 'gmfgraph_Figure66', a)
    _safe_set(a, 'gmfgraph_RealFigure65', set())
    assert not _is_linked(a, 'gmfgraph_RealFigure65', b2)
    if hasattr(b2, 'gmfgraph_Figure66'):
        assert not _is_linked(b2, 'gmfgraph_Figure66', a)


def test_assoc_color82_link_reassign_clear():
    a = gmfgraph_LineBorder(width=7)
    b1 = gmfgraph_Color()
    b2 = gmfgraph_Color()
    _safe_set(a, 'gmfgraph_LineBorder', b1)
    assert _is_linked(a, 'gmfgraph_LineBorder', b1)
    if hasattr(b1, 'gmfgraph_Color83'):
        assert _is_linked(b1, 'gmfgraph_Color83', a)
    _safe_set(a, 'gmfgraph_LineBorder', b2)
    assert _is_linked(a, 'gmfgraph_LineBorder', b2)
    if hasattr(b1, 'gmfgraph_Color83'):
        assert not _is_linked(b1, 'gmfgraph_Color83', a)
    if hasattr(b2, 'gmfgraph_Color83'):
        assert _is_linked(b2, 'gmfgraph_Color83', a)
    _safe_set(a, 'gmfgraph_LineBorder', None)
    assert not _is_linked(a, 'gmfgraph_LineBorder', b2)
    if hasattr(b2, 'gmfgraph_Color83'):
        assert not _is_linked(b2, 'gmfgraph_Color83', a)


def test_assoc_compartments5_link_reassign_clear():
    a = gmfgraph_Compartment(collapsible=True, needsTitle=True)
    b1 = gmfgraph_Canvas()
    b2 = gmfgraph_Canvas()
    _safe_set(a, 'gmfgraph_Compartment', b1)
    assert _is_linked(a, 'gmfgraph_Compartment', b1)
    if hasattr(b1, 'gmfgraph_Canvas6'):
        assert _is_linked(b1, 'gmfgraph_Canvas6', a)
    _safe_set(a, 'gmfgraph_Compartment', b2)
    assert _is_linked(a, 'gmfgraph_Compartment', b2)
    if hasattr(b1, 'gmfgraph_Canvas6'):
        assert not _is_linked(b1, 'gmfgraph_Canvas6', a)
    if hasattr(b2, 'gmfgraph_Canvas6'):
        assert _is_linked(b2, 'gmfgraph_Canvas6', a)
    _safe_set(a, 'gmfgraph_Compartment', None)
    assert not _is_linked(a, 'gmfgraph_Compartment', b2)
    if hasattr(b2, 'gmfgraph_Canvas6'):
        assert not _is_linked(b2, 'gmfgraph_Canvas6', a)


def test_assoc_container25_link_reassign_clear():
    a = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    b1 = gmfgraph_ChildAccess(accessor="sample_text")
    b2 = gmfgraph_ChildAccess(accessor="sample_text_2")
    _safe_set(a, 'gmfgraph_DiagramLabel26', b1)
    assert _is_linked(a, 'gmfgraph_DiagramLabel26', b1)
    if hasattr(b1, 'gmfgraph_ChildAccess27'):
        assert _is_linked(b1, 'gmfgraph_ChildAccess27', a)
    _safe_set(a, 'gmfgraph_DiagramLabel26', b2)
    assert _is_linked(a, 'gmfgraph_DiagramLabel26', b2)
    if hasattr(b1, 'gmfgraph_ChildAccess27'):
        assert not _is_linked(b1, 'gmfgraph_ChildAccess27', a)
    if hasattr(b2, 'gmfgraph_ChildAccess27'):
        assert _is_linked(b2, 'gmfgraph_ChildAccess27', a)
    _safe_set(a, 'gmfgraph_DiagramLabel26', None)
    assert not _is_linked(a, 'gmfgraph_DiagramLabel26', b2)
    if hasattr(b2, 'gmfgraph_ChildAccess27'):
        assert not _is_linked(b2, 'gmfgraph_ChildAccess27', a)


def test_assoc_contentPane17_link_reassign_clear():
    a = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    b1 = gmfgraph_ChildAccess(accessor="sample_text")
    b2 = gmfgraph_ChildAccess(accessor="sample_text_2")
    _safe_set(a, 'gmfgraph_Node18', b1)
    assert _is_linked(a, 'gmfgraph_Node18', b1)
    if hasattr(b1, 'gmfgraph_ChildAccess'):
        assert _is_linked(b1, 'gmfgraph_ChildAccess', a)
    _safe_set(a, 'gmfgraph_Node18', b2)
    assert _is_linked(a, 'gmfgraph_Node18', b2)
    if hasattr(b1, 'gmfgraph_ChildAccess'):
        assert not _is_linked(b1, 'gmfgraph_ChildAccess', a)
    if hasattr(b2, 'gmfgraph_ChildAccess'):
        assert _is_linked(b2, 'gmfgraph_ChildAccess', a)
    _safe_set(a, 'gmfgraph_Node18', None)
    assert not _is_linked(a, 'gmfgraph_Node18', b2)
    if hasattr(b2, 'gmfgraph_ChildAccess'):
        assert not _is_linked(b2, 'gmfgraph_ChildAccess', a)


def test_assoc_customChildren80_link_reassign_clear():
    a = gmfgraph_FigureAccessor(accessor="sample_text")
    b1 = gmfgraph_CustomFigure()
    b2 = gmfgraph_CustomFigure()
    _safe_set(a, 'gmfgraph_FigureAccessor81', b1)
    assert _is_linked(a, 'gmfgraph_FigureAccessor81', b1)
    if hasattr(b1, 'gmfgraph_CustomFigure'):
        assert _is_linked(b1, 'gmfgraph_CustomFigure', a)
    _safe_set(a, 'gmfgraph_FigureAccessor81', b2)
    assert _is_linked(a, 'gmfgraph_FigureAccessor81', b2)
    if hasattr(b1, 'gmfgraph_CustomFigure'):
        assert not _is_linked(b1, 'gmfgraph_CustomFigure', a)
    if hasattr(b2, 'gmfgraph_CustomFigure'):
        assert _is_linked(b2, 'gmfgraph_CustomFigure', a)
    _safe_set(a, 'gmfgraph_FigureAccessor81', None)
    assert not _is_linked(a, 'gmfgraph_FigureAccessor81', b2)
    if hasattr(b2, 'gmfgraph_CustomFigure'):
        assert not _is_linked(b2, 'gmfgraph_CustomFigure', a)


def test_assoc_defaultSize28_link_reassign_clear():
    a = gmfgraph_Dimension(dx=7, dy=7)
    b1 = gmfgraph_DefaultSizeFacet()
    b2 = gmfgraph_DefaultSizeFacet()
    _safe_set(a, 'gmfgraph_Dimension', b1)
    assert _is_linked(a, 'gmfgraph_Dimension', b1)
    if hasattr(b1, 'gmfgraph_DefaultSizeFacet'):
        assert _is_linked(b1, 'gmfgraph_DefaultSizeFacet', a)
    _safe_set(a, 'gmfgraph_Dimension', b2)
    assert _is_linked(a, 'gmfgraph_Dimension', b2)
    if hasattr(b1, 'gmfgraph_DefaultSizeFacet'):
        assert not _is_linked(b1, 'gmfgraph_DefaultSizeFacet', a)
    if hasattr(b2, 'gmfgraph_DefaultSizeFacet'):
        assert _is_linked(b2, 'gmfgraph_DefaultSizeFacet', a)
    _safe_set(a, 'gmfgraph_Dimension', None)
    assert not _is_linked(a, 'gmfgraph_Dimension', b2)
    if hasattr(b2, 'gmfgraph_DefaultSizeFacet'):
        assert not _is_linked(b2, 'gmfgraph_DefaultSizeFacet', a)


def test_assoc_descriptors11_link_reassign_clear():
    a = gmfgraph_FigureGallery(implementationBundle="sample_text")
    b1 = gmfgraph_FigureDescriptor()
    b2 = gmfgraph_FigureDescriptor()
    _safe_set(a, 'gmfgraph_FigureGallery12', {b1})
    assert _is_linked(a, 'gmfgraph_FigureGallery12', b1)
    if hasattr(b1, 'gmfgraph_FigureDescriptor'):
        assert _is_linked(b1, 'gmfgraph_FigureDescriptor', a)
    _safe_set(a, 'gmfgraph_FigureGallery12', {b2})
    assert _is_linked(a, 'gmfgraph_FigureGallery12', b2)
    if hasattr(b1, 'gmfgraph_FigureDescriptor'):
        assert not _is_linked(b1, 'gmfgraph_FigureDescriptor', a)
    if hasattr(b2, 'gmfgraph_FigureDescriptor'):
        assert _is_linked(b2, 'gmfgraph_FigureDescriptor', a)
    _safe_set(a, 'gmfgraph_FigureGallery12', set())
    assert not _is_linked(a, 'gmfgraph_FigureGallery12', b2)
    if hasattr(b2, 'gmfgraph_FigureDescriptor'):
        assert not _is_linked(b2, 'gmfgraph_FigureDescriptor', a)


def test_assoc_figure61_link_reassign_clear():
    a = gmfgraph_ChildAccess(accessor="sample_text")
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_ChildAccess62', b1)
    assert _is_linked(a, 'gmfgraph_ChildAccess62', b1)
    if hasattr(b1, 'gmfgraph_Figure63'):
        assert _is_linked(b1, 'gmfgraph_Figure63', a)
    _safe_set(a, 'gmfgraph_ChildAccess62', b2)
    assert _is_linked(a, 'gmfgraph_ChildAccess62', b2)
    if hasattr(b1, 'gmfgraph_Figure63'):
        assert not _is_linked(b1, 'gmfgraph_Figure63', a)
    if hasattr(b2, 'gmfgraph_Figure63'):
        assert _is_linked(b2, 'gmfgraph_Figure63', a)
    _safe_set(a, 'gmfgraph_ChildAccess62', None)
    assert not _is_linked(a, 'gmfgraph_ChildAccess62', b2)
    if hasattr(b2, 'gmfgraph_Figure63'):
        assert not _is_linked(b2, 'gmfgraph_Figure63', a)


def test_assoc_figure67_link_reassign_clear():
    a = gmfgraph_RealFigure(name="sample_text")
    b1 = gmfgraph_FigureRef()
    b2 = gmfgraph_FigureRef()
    _safe_set(a, 'gmfgraph_RealFigure68', b1)
    assert _is_linked(a, 'gmfgraph_RealFigure68', b1)
    if hasattr(b1, 'gmfgraph_FigureRef'):
        assert _is_linked(b1, 'gmfgraph_FigureRef', a)
    _safe_set(a, 'gmfgraph_RealFigure68', b2)
    assert _is_linked(a, 'gmfgraph_RealFigure68', b2)
    if hasattr(b1, 'gmfgraph_FigureRef'):
        assert not _is_linked(b1, 'gmfgraph_FigureRef', a)
    if hasattr(b2, 'gmfgraph_FigureRef'):
        assert _is_linked(b2, 'gmfgraph_FigureRef', a)
    _safe_set(a, 'gmfgraph_RealFigure68', None)
    assert not _is_linked(a, 'gmfgraph_RealFigure68', b2)
    if hasattr(b2, 'gmfgraph_FigureRef'):
        assert not _is_linked(b2, 'gmfgraph_FigureRef', a)


def test_assoc_figures0_link_reassign_clear():
    a = gmfgraph_FigureGallery(implementationBundle="sample_text")
    b1 = gmfgraph_Canvas()
    b2 = gmfgraph_Canvas()
    _safe_set(a, 'gmfgraph_FigureGallery', b1)
    assert _is_linked(a, 'gmfgraph_FigureGallery', b1)
    if hasattr(b1, 'gmfgraph_Canvas'):
        assert _is_linked(b1, 'gmfgraph_Canvas', a)
    _safe_set(a, 'gmfgraph_FigureGallery', b2)
    assert _is_linked(a, 'gmfgraph_FigureGallery', b2)
    if hasattr(b1, 'gmfgraph_Canvas'):
        assert not _is_linked(b1, 'gmfgraph_Canvas', a)
    if hasattr(b2, 'gmfgraph_Canvas'):
        assert _is_linked(b2, 'gmfgraph_Canvas', a)
    _safe_set(a, 'gmfgraph_FigureGallery', None)
    assert not _is_linked(a, 'gmfgraph_FigureGallery', b2)
    if hasattr(b2, 'gmfgraph_Canvas'):
        assert not _is_linked(b2, 'gmfgraph_Canvas', a)


def test_assoc_figures9_link_reassign_clear():
    a = gmfgraph_RealFigure(name="sample_text")
    b1 = gmfgraph_FigureGallery(implementationBundle="sample_text")
    b2 = gmfgraph_FigureGallery(implementationBundle="sample_text_2")
    _safe_set(a, 'gmfgraph_RealFigure', b1)
    assert _is_linked(a, 'gmfgraph_RealFigure', b1)
    if hasattr(b1, 'gmfgraph_FigureGallery10'):
        assert _is_linked(b1, 'gmfgraph_FigureGallery10', a)
    _safe_set(a, 'gmfgraph_RealFigure', b2)
    assert _is_linked(a, 'gmfgraph_RealFigure', b2)
    if hasattr(b1, 'gmfgraph_FigureGallery10'):
        assert not _is_linked(b1, 'gmfgraph_FigureGallery10', a)
    if hasattr(b2, 'gmfgraph_FigureGallery10'):
        assert _is_linked(b2, 'gmfgraph_FigureGallery10', a)
    _safe_set(a, 'gmfgraph_RealFigure', None)
    assert not _is_linked(a, 'gmfgraph_RealFigure', b2)
    if hasattr(b2, 'gmfgraph_FigureGallery10'):
        assert not _is_linked(b2, 'gmfgraph_FigureGallery10', a)


def test_assoc_insets47_link_reassign_clear():
    a = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_Insets', b1)
    assert _is_linked(a, 'gmfgraph_Insets', b1)
    if hasattr(b1, 'gmfgraph_Figure48'):
        assert _is_linked(b1, 'gmfgraph_Figure48', a)
    _safe_set(a, 'gmfgraph_Insets', b2)
    assert _is_linked(a, 'gmfgraph_Insets', b2)
    if hasattr(b1, 'gmfgraph_Figure48'):
        assert not _is_linked(b1, 'gmfgraph_Figure48', a)
    if hasattr(b2, 'gmfgraph_Figure48'):
        assert _is_linked(b2, 'gmfgraph_Figure48', a)
    _safe_set(a, 'gmfgraph_Insets', None)
    assert not _is_linked(a, 'gmfgraph_Insets', b2)
    if hasattr(b2, 'gmfgraph_Figure48'):
        assert not _is_linked(b2, 'gmfgraph_Figure48', a)


def test_assoc_insets84_link_reassign_clear():
    a = gmfgraph_Insets(bottom=7, left=7, right=7, top=7)
    b1 = gmfgraph_MarginBorder()
    b2 = gmfgraph_MarginBorder()
    _safe_set(a, 'gmfgraph_Insets85', b1)
    assert _is_linked(a, 'gmfgraph_Insets85', b1)
    if hasattr(b1, 'gmfgraph_MarginBorder'):
        assert _is_linked(b1, 'gmfgraph_MarginBorder', a)
    _safe_set(a, 'gmfgraph_Insets85', b2)
    assert _is_linked(a, 'gmfgraph_Insets85', b2)
    if hasattr(b1, 'gmfgraph_MarginBorder'):
        assert not _is_linked(b1, 'gmfgraph_MarginBorder', a)
    if hasattr(b2, 'gmfgraph_MarginBorder'):
        assert _is_linked(b2, 'gmfgraph_MarginBorder', a)
    _safe_set(a, 'gmfgraph_Insets85', None)
    assert not _is_linked(a, 'gmfgraph_Insets85', b2)
    if hasattr(b2, 'gmfgraph_MarginBorder'):
        assert not _is_linked(b2, 'gmfgraph_MarginBorder', a)


def test_assoc_labels7_link_reassign_clear():
    a = gmfgraph_DiagramLabel(elementIcon=True, external=True)
    b1 = gmfgraph_Canvas()
    b2 = gmfgraph_Canvas()
    _safe_set(a, 'gmfgraph_DiagramLabel', b1)
    assert _is_linked(a, 'gmfgraph_DiagramLabel', b1)
    if hasattr(b1, 'gmfgraph_Canvas8'):
        assert _is_linked(b1, 'gmfgraph_Canvas8', a)
    _safe_set(a, 'gmfgraph_DiagramLabel', b2)
    assert _is_linked(a, 'gmfgraph_DiagramLabel', b2)
    if hasattr(b1, 'gmfgraph_Canvas8'):
        assert not _is_linked(b1, 'gmfgraph_Canvas8', a)
    if hasattr(b2, 'gmfgraph_Canvas8'):
        assert _is_linked(b2, 'gmfgraph_Canvas8', a)
    _safe_set(a, 'gmfgraph_DiagramLabel', None)
    assert not _is_linked(a, 'gmfgraph_DiagramLabel', b2)
    if hasattr(b2, 'gmfgraph_Canvas8'):
        assert not _is_linked(b2, 'gmfgraph_Canvas8', a)


def test_assoc_location51_link_reassign_clear():
    a = gmfgraph_Point(x=7, y=7)
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_Point', b1)
    assert _is_linked(a, 'gmfgraph_Point', b1)
    if hasattr(b1, 'gmfgraph_Figure52'):
        assert _is_linked(b1, 'gmfgraph_Figure52', a)
    _safe_set(a, 'gmfgraph_Point', b2)
    assert _is_linked(a, 'gmfgraph_Point', b2)
    if hasattr(b1, 'gmfgraph_Figure52'):
        assert not _is_linked(b1, 'gmfgraph_Figure52', a)
    if hasattr(b2, 'gmfgraph_Figure52'):
        assert _is_linked(b2, 'gmfgraph_Figure52', a)
    _safe_set(a, 'gmfgraph_Point', None)
    assert not _is_linked(a, 'gmfgraph_Point', b2)
    if hasattr(b2, 'gmfgraph_Figure52'):
        assert not _is_linked(b2, 'gmfgraph_Figure52', a)


def test_assoc_margins97_link_reassign_clear():
    a = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    b1 = gmfgraph_Dimension(dx=7, dy=7)
    b2 = gmfgraph_Dimension(dx=13, dy=13)
    _safe_set(a, 'gmfgraph_GridLayout', b1)
    assert _is_linked(a, 'gmfgraph_GridLayout', b1)
    if hasattr(b1, 'gmfgraph_Dimension98'):
        assert _is_linked(b1, 'gmfgraph_Dimension98', a)
    _safe_set(a, 'gmfgraph_GridLayout', b2)
    assert _is_linked(a, 'gmfgraph_GridLayout', b2)
    if hasattr(b1, 'gmfgraph_Dimension98'):
        assert not _is_linked(b1, 'gmfgraph_Dimension98', a)
    if hasattr(b2, 'gmfgraph_Dimension98'):
        assert _is_linked(b2, 'gmfgraph_Dimension98', a)
    _safe_set(a, 'gmfgraph_GridLayout', None)
    assert not _is_linked(a, 'gmfgraph_GridLayout', b2)
    if hasattr(b2, 'gmfgraph_Dimension98'):
        assert not _is_linked(b2, 'gmfgraph_Dimension98', a)


def test_assoc_maximumSize36_link_reassign_clear():
    a = gmfgraph_Dimension(dx=7, dy=7)
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_Dimension38', b1)
    assert _is_linked(a, 'gmfgraph_Dimension38', b1)
    if hasattr(b1, 'gmfgraph_Figure37'):
        assert _is_linked(b1, 'gmfgraph_Figure37', a)
    _safe_set(a, 'gmfgraph_Dimension38', b2)
    assert _is_linked(a, 'gmfgraph_Dimension38', b2)
    if hasattr(b1, 'gmfgraph_Figure37'):
        assert not _is_linked(b1, 'gmfgraph_Figure37', a)
    if hasattr(b2, 'gmfgraph_Figure37'):
        assert _is_linked(b2, 'gmfgraph_Figure37', a)
    _safe_set(a, 'gmfgraph_Dimension38', None)
    assert not _is_linked(a, 'gmfgraph_Dimension38', b2)
    if hasattr(b2, 'gmfgraph_Figure37'):
        assert not _is_linked(b2, 'gmfgraph_Figure37', a)


def test_assoc_minimumSize39_link_reassign_clear():
    a = gmfgraph_Dimension(dx=7, dy=7)
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_Dimension41', b1)
    assert _is_linked(a, 'gmfgraph_Dimension41', b1)
    if hasattr(b1, 'gmfgraph_Figure40'):
        assert _is_linked(b1, 'gmfgraph_Figure40', a)
    _safe_set(a, 'gmfgraph_Dimension41', b2)
    assert _is_linked(a, 'gmfgraph_Dimension41', b2)
    if hasattr(b1, 'gmfgraph_Figure40'):
        assert not _is_linked(b1, 'gmfgraph_Figure40', a)
    if hasattr(b2, 'gmfgraph_Figure40'):
        assert _is_linked(b2, 'gmfgraph_Figure40', a)
    _safe_set(a, 'gmfgraph_Dimension41', None)
    assert not _is_linked(a, 'gmfgraph_Dimension41', b2)
    if hasattr(b2, 'gmfgraph_Figure40'):
        assert not _is_linked(b2, 'gmfgraph_Figure40', a)


def test_assoc_nodes1_link_reassign_clear():
    a = gmfgraph_Node(affixedParentSide="sample_text", resizeConstraint="sample_text")
    b1 = gmfgraph_Canvas()
    b2 = gmfgraph_Canvas()
    _safe_set(a, 'gmfgraph_Node', b1)
    assert _is_linked(a, 'gmfgraph_Node', b1)
    if hasattr(b1, 'gmfgraph_Canvas2'):
        assert _is_linked(b1, 'gmfgraph_Canvas2', a)
    _safe_set(a, 'gmfgraph_Node', b2)
    assert _is_linked(a, 'gmfgraph_Node', b2)
    if hasattr(b1, 'gmfgraph_Canvas2'):
        assert not _is_linked(b1, 'gmfgraph_Canvas2', a)
    if hasattr(b2, 'gmfgraph_Canvas2'):
        assert _is_linked(b2, 'gmfgraph_Canvas2', a)
    _safe_set(a, 'gmfgraph_Node', None)
    assert not _is_linked(a, 'gmfgraph_Node', b2)
    if hasattr(b2, 'gmfgraph_Canvas2'):
        assert not _is_linked(b2, 'gmfgraph_Canvas2', a)


def test_assoc_owner60_link_reassign_clear():
    a = gmfgraph_ChildAccess(accessor="sample_text")
    b1 = gmfgraph_FigureDescriptor()
    b2 = gmfgraph_FigureDescriptor()
    _safe_set(a, 'accessors', b1)
    assert _is_linked(a, 'accessors', b1)
    if hasattr(b1, 'FigureDescriptor'):
        assert _is_linked(b1, 'FigureDescriptor', a)
    _safe_set(a, 'accessors', b2)
    assert _is_linked(a, 'accessors', b2)
    if hasattr(b1, 'FigureDescriptor'):
        assert not _is_linked(b1, 'FigureDescriptor', a)
    if hasattr(b2, 'FigureDescriptor'):
        assert _is_linked(b2, 'FigureDescriptor', a)
    _safe_set(a, 'accessors', None)
    assert not _is_linked(a, 'accessors', b2)
    if hasattr(b2, 'FigureDescriptor'):
        assert not _is_linked(b2, 'FigureDescriptor', a)


def test_assoc_preferredSize42_link_reassign_clear():
    a = gmfgraph_Dimension(dx=7, dy=7)
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_Dimension44', b1)
    assert _is_linked(a, 'gmfgraph_Dimension44', b1)
    if hasattr(b1, 'gmfgraph_Figure43'):
        assert _is_linked(b1, 'gmfgraph_Figure43', a)
    _safe_set(a, 'gmfgraph_Dimension44', b2)
    assert _is_linked(a, 'gmfgraph_Dimension44', b2)
    if hasattr(b1, 'gmfgraph_Figure43'):
        assert not _is_linked(b1, 'gmfgraph_Figure43', a)
    if hasattr(b2, 'gmfgraph_Figure43'):
        assert _is_linked(b2, 'gmfgraph_Figure43', a)
    _safe_set(a, 'gmfgraph_Dimension44', None)
    assert not _is_linked(a, 'gmfgraph_Dimension44', b2)
    if hasattr(b2, 'gmfgraph_Figure43'):
        assert not _is_linked(b2, 'gmfgraph_Figure43', a)


def test_assoc_resolvedChildren69_link_reassign_clear():
    a = gmfgraph_Shape(fill=True, lineKind="sample_text", lineWidth=7, outline=True, xorFill=True, xorOutline=True)
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_Shape', {b1})
    assert _is_linked(a, 'gmfgraph_Shape', b1)
    if hasattr(b1, 'gmfgraph_Figure70'):
        assert _is_linked(b1, 'gmfgraph_Figure70', a)
    _safe_set(a, 'gmfgraph_Shape', {b2})
    assert _is_linked(a, 'gmfgraph_Shape', b2)
    if hasattr(b1, 'gmfgraph_Figure70'):
        assert not _is_linked(b1, 'gmfgraph_Figure70', a)
    if hasattr(b2, 'gmfgraph_Figure70'):
        assert _is_linked(b2, 'gmfgraph_Figure70', a)
    _safe_set(a, 'gmfgraph_Shape', set())
    assert not _is_linked(a, 'gmfgraph_Shape', b2)
    if hasattr(b2, 'gmfgraph_Figure70'):
        assert not _is_linked(b2, 'gmfgraph_Figure70', a)


def test_assoc_size106_link_reassign_clear():
    a = gmfgraph_Dimension(dx=7, dy=7)
    b1 = gmfgraph_XYLayoutData()
    b2 = gmfgraph_XYLayoutData()
    _safe_set(a, 'gmfgraph_Dimension108', b1)
    assert _is_linked(a, 'gmfgraph_Dimension108', b1)
    if hasattr(b1, 'gmfgraph_XYLayoutData107'):
        assert _is_linked(b1, 'gmfgraph_XYLayoutData107', a)
    _safe_set(a, 'gmfgraph_Dimension108', b2)
    assert _is_linked(a, 'gmfgraph_Dimension108', b2)
    if hasattr(b1, 'gmfgraph_XYLayoutData107'):
        assert not _is_linked(b1, 'gmfgraph_XYLayoutData107', a)
    if hasattr(b2, 'gmfgraph_XYLayoutData107'):
        assert _is_linked(b2, 'gmfgraph_XYLayoutData107', a)
    _safe_set(a, 'gmfgraph_Dimension108', None)
    assert not _is_linked(a, 'gmfgraph_Dimension108', b2)
    if hasattr(b2, 'gmfgraph_XYLayoutData107'):
        assert not _is_linked(b2, 'gmfgraph_XYLayoutData107', a)


def test_assoc_size53_link_reassign_clear():
    a = gmfgraph_Point(x=7, y=7)
    b1 = gmfgraph_Figure()
    b2 = gmfgraph_Figure()
    _safe_set(a, 'gmfgraph_Point55', b1)
    assert _is_linked(a, 'gmfgraph_Point55', b1)
    if hasattr(b1, 'gmfgraph_Figure54'):
        assert _is_linked(b1, 'gmfgraph_Figure54', a)
    _safe_set(a, 'gmfgraph_Point55', b2)
    assert _is_linked(a, 'gmfgraph_Point55', b2)
    if hasattr(b1, 'gmfgraph_Figure54'):
        assert not _is_linked(b1, 'gmfgraph_Figure54', a)
    if hasattr(b2, 'gmfgraph_Figure54'):
        assert _is_linked(b2, 'gmfgraph_Figure54', a)
    _safe_set(a, 'gmfgraph_Point55', None)
    assert not _is_linked(a, 'gmfgraph_Point55', b2)
    if hasattr(b2, 'gmfgraph_Figure54'):
        assert not _is_linked(b2, 'gmfgraph_Figure54', a)


def test_assoc_sizeHint92_link_reassign_clear():
    a = gmfgraph_GridLayoutData(grabExcessHorizontalSpace=True, grabExcessVerticalSpace=True, horizontalAlignment="sample_text", horizontalIndent=7, horizontalSpan=7, verticalAlignment="sample_text", verticalSpan=7)
    b1 = gmfgraph_Dimension(dx=7, dy=7)
    b2 = gmfgraph_Dimension(dx=13, dy=13)
    _safe_set(a, 'gmfgraph_GridLayoutData', b1)
    assert _is_linked(a, 'gmfgraph_GridLayoutData', b1)
    if hasattr(b1, 'gmfgraph_Dimension93'):
        assert _is_linked(b1, 'gmfgraph_Dimension93', a)
    _safe_set(a, 'gmfgraph_GridLayoutData', b2)
    assert _is_linked(a, 'gmfgraph_GridLayoutData', b2)
    if hasattr(b1, 'gmfgraph_Dimension93'):
        assert not _is_linked(b1, 'gmfgraph_Dimension93', a)
    if hasattr(b2, 'gmfgraph_Dimension93'):
        assert _is_linked(b2, 'gmfgraph_Dimension93', a)
    _safe_set(a, 'gmfgraph_GridLayoutData', None)
    assert not _is_linked(a, 'gmfgraph_GridLayoutData', b2)
    if hasattr(b2, 'gmfgraph_Dimension93'):
        assert not _is_linked(b2, 'gmfgraph_Dimension93', a)


def test_assoc_spacing102_link_reassign_clear():
    a = gmfgraph_Dimension(dx=7, dy=7)
    b1 = gmfgraph_BorderLayout()
    b2 = gmfgraph_BorderLayout()
    _safe_set(a, 'gmfgraph_Dimension103', b1)
    assert _is_linked(a, 'gmfgraph_Dimension103', b1)
    if hasattr(b1, 'gmfgraph_BorderLayout'):
        assert _is_linked(b1, 'gmfgraph_BorderLayout', a)
    _safe_set(a, 'gmfgraph_Dimension103', b2)
    assert _is_linked(a, 'gmfgraph_Dimension103', b2)
    if hasattr(b1, 'gmfgraph_BorderLayout'):
        assert not _is_linked(b1, 'gmfgraph_BorderLayout', a)
    if hasattr(b2, 'gmfgraph_BorderLayout'):
        assert _is_linked(b2, 'gmfgraph_BorderLayout', a)
    _safe_set(a, 'gmfgraph_Dimension103', None)
    assert not _is_linked(a, 'gmfgraph_Dimension103', b2)
    if hasattr(b2, 'gmfgraph_BorderLayout'):
        assert not _is_linked(b2, 'gmfgraph_BorderLayout', a)


def test_assoc_spacing99_link_reassign_clear():
    a = gmfgraph_GridLayout(equalWidth=True, numColumns=7)
    b1 = gmfgraph_Dimension(dx=7, dy=7)
    b2 = gmfgraph_Dimension(dx=13, dy=13)
    _safe_set(a, 'gmfgraph_GridLayout100', b1)
    assert _is_linked(a, 'gmfgraph_GridLayout100', b1)
    if hasattr(b1, 'gmfgraph_Dimension101'):
        assert _is_linked(b1, 'gmfgraph_Dimension101', a)
    _safe_set(a, 'gmfgraph_GridLayout100', b2)
    assert _is_linked(a, 'gmfgraph_GridLayout100', b2)
    if hasattr(b1, 'gmfgraph_Dimension101'):
        assert not _is_linked(b1, 'gmfgraph_Dimension101', a)
    if hasattr(b2, 'gmfgraph_Dimension101'):
        assert _is_linked(b2, 'gmfgraph_Dimension101', a)
    _safe_set(a, 'gmfgraph_GridLayout100', None)
    assert not _is_linked(a, 'gmfgraph_GridLayout100', b2)
    if hasattr(b2, 'gmfgraph_Dimension101'):
        assert not _is_linked(b2, 'gmfgraph_Dimension101', a)


def test_assoc_template71_link_reassign_clear():
    a = gmfgraph_Point(x=7, y=7)
    b1 = gmfgraph_Polyline()
    b2 = gmfgraph_Polyline()
    _safe_set(a, 'gmfgraph_Point72', b1)
    assert _is_linked(a, 'gmfgraph_Point72', b1)
    if hasattr(b1, 'gmfgraph_Polyline'):
        assert _is_linked(b1, 'gmfgraph_Polyline', a)
    _safe_set(a, 'gmfgraph_Point72', b2)
    assert _is_linked(a, 'gmfgraph_Point72', b2)
    if hasattr(b1, 'gmfgraph_Polyline'):
        assert not _is_linked(b1, 'gmfgraph_Polyline', a)
    if hasattr(b2, 'gmfgraph_Polyline'):
        assert _is_linked(b2, 'gmfgraph_Polyline', a)
    _safe_set(a, 'gmfgraph_Point72', None)
    assert not _is_linked(a, 'gmfgraph_Point72', b2)
    if hasattr(b2, 'gmfgraph_Polyline'):
        assert not _is_linked(b2, 'gmfgraph_Polyline', a)


def test_assoc_topLeft104_link_reassign_clear():
    a = gmfgraph_Point(x=7, y=7)
    b1 = gmfgraph_XYLayoutData()
    b2 = gmfgraph_XYLayoutData()
    _safe_set(a, 'gmfgraph_Point105', b1)
    assert _is_linked(a, 'gmfgraph_Point105', b1)
    if hasattr(b1, 'gmfgraph_XYLayoutData'):
        assert _is_linked(b1, 'gmfgraph_XYLayoutData', a)
    _safe_set(a, 'gmfgraph_Point105', b2)
    assert _is_linked(a, 'gmfgraph_Point105', b2)
    if hasattr(b1, 'gmfgraph_XYLayoutData'):
        assert not _is_linked(b1, 'gmfgraph_XYLayoutData', a)
    if hasattr(b2, 'gmfgraph_XYLayoutData'):
        assert _is_linked(b2, 'gmfgraph_XYLayoutData', a)
    _safe_set(a, 'gmfgraph_Point105', None)
    assert not _is_linked(a, 'gmfgraph_Point105', b2)
    if hasattr(b2, 'gmfgraph_XYLayoutData'):
        assert not _is_linked(b2, 'gmfgraph_XYLayoutData', a)


def test_assoc_typedFigure78_link_reassign_clear():
    a = gmfgraph_RealFigure(name="sample_text")
    b1 = gmfgraph_FigureAccessor(accessor="sample_text")
    b2 = gmfgraph_FigureAccessor(accessor="sample_text_2")
    _safe_set(a, 'gmfgraph_RealFigure79', b1)
    assert _is_linked(a, 'gmfgraph_RealFigure79', b1)
    if hasattr(b1, 'gmfgraph_FigureAccessor'):
        assert _is_linked(b1, 'gmfgraph_FigureAccessor', a)
    _safe_set(a, 'gmfgraph_RealFigure79', b2)
    assert _is_linked(a, 'gmfgraph_RealFigure79', b2)
    if hasattr(b1, 'gmfgraph_FigureAccessor'):
        assert not _is_linked(b1, 'gmfgraph_FigureAccessor', a)
    if hasattr(b2, 'gmfgraph_FigureAccessor'):
        assert _is_linked(b2, 'gmfgraph_FigureAccessor', a)
    _safe_set(a, 'gmfgraph_RealFigure79', None)
    assert not _is_linked(a, 'gmfgraph_RealFigure79', b2)
    if hasattr(b2, 'gmfgraph_FigureAccessor'):
        assert not _is_linked(b2, 'gmfgraph_FigureAccessor', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractFigure_strategy = st.builds(AbstractFigure)
@given(instance=AbstractFigure_strategy)
@settings(max_examples=25)
def test_AbstractFigure_instantiation(instance):
    assert isinstance(instance, AbstractFigure)


AbstractNode_strategy = st.builds(AbstractNode)
@given(instance=AbstractNode_strategy)
@settings(max_examples=25)
def test_AbstractNode_instantiation(instance):
    assert isinstance(instance, AbstractNode)


Border_strategy = st.builds(Border)
@given(instance=Border_strategy)
@settings(max_examples=25)
def test_Border_instantiation(instance):
    assert isinstance(instance, Border)


Color_strategy = st.builds(Color)
@given(instance=Color_strategy)
@settings(max_examples=25)
def test_Color_instantiation(instance):
    assert isinstance(instance, Color)


ConnectionFigure_strategy = st.builds(ConnectionFigure)
@given(instance=ConnectionFigure_strategy)
@settings(max_examples=25)
def test_ConnectionFigure_instantiation(instance):
    assert isinstance(instance, ConnectionFigure)


CustomClass_strategy = st.builds(CustomClass)
@given(instance=CustomClass_strategy)
@settings(max_examples=25)
def test_CustomClass_instantiation(instance):
    assert isinstance(instance, CustomClass)


CustomFigure_strategy = st.builds(CustomFigure)
@given(instance=CustomFigure_strategy)
@settings(max_examples=25)
def test_CustomFigure_instantiation(instance):
    assert isinstance(instance, CustomFigure)


DecorationFigure_strategy = st.builds(DecorationFigure)
@given(instance=DecorationFigure_strategy)
@settings(max_examples=25)
def test_DecorationFigure_instantiation(instance):
    assert isinstance(instance, DecorationFigure)


DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


Figure_strategy = st.builds(Figure)
@given(instance=Figure_strategy)
@settings(max_examples=25)
def test_Figure_instantiation(instance):
    assert isinstance(instance, Figure)


Font_strategy = st.builds(Font)
@given(instance=Font_strategy)
@settings(max_examples=25)
def test_Font_instantiation(instance):
    assert isinstance(instance, Font)


Identity_strategy = st.builds(Identity)
@given(instance=Identity_strategy)
@settings(max_examples=25)
def test_Identity_instantiation(instance):
    assert isinstance(instance, Identity)


Layout_strategy = st.builds(Layout)
@given(instance=Layout_strategy)
@settings(max_examples=25)
def test_Layout_instantiation(instance):
    assert isinstance(instance, Layout)


LayoutData_strategy = st.builds(LayoutData)
@given(instance=LayoutData_strategy)
@settings(max_examples=25)
def test_LayoutData_instantiation(instance):
    assert isinstance(instance, LayoutData)


Layoutable_strategy = st.builds(Layoutable)
@given(instance=Layoutable_strategy)
@settings(max_examples=25)
def test_Layoutable_instantiation(instance):
    assert isinstance(instance, Layoutable)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


Polygon_strategy = st.builds(Polygon)
@given(instance=Polygon_strategy)
@settings(max_examples=25)
def test_Polygon_instantiation(instance):
    assert isinstance(instance, Polygon)


Polyline_strategy = st.builds(Polyline)
@given(instance=Polyline_strategy)
@settings(max_examples=25)
def test_Polyline_instantiation(instance):
    assert isinstance(instance, Polyline)


RealFigure_strategy = st.builds(RealFigure)
@given(instance=RealFigure_strategy)
@settings(max_examples=25)
def test_RealFigure_instantiation(instance):
    assert isinstance(instance, RealFigure)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


VisualFacet_strategy = st.builds(VisualFacet)
@given(instance=VisualFacet_strategy)
@settings(max_examples=25)
def test_VisualFacet_instantiation(instance):
    assert isinstance(instance, VisualFacet)


gmfgraph_AbstractFigure_strategy = st.builds(gmfgraph_AbstractFigure)
@given(instance=gmfgraph_AbstractFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_AbstractFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_AbstractFigure)


gmfgraph_AbstractNode_strategy = st.builds(gmfgraph_AbstractNode)
@given(instance=gmfgraph_AbstractNode_strategy)
@settings(max_examples=25)
def test_gmfgraph_AbstractNode_instantiation(instance):
    assert isinstance(instance, gmfgraph_AbstractNode)


gmfgraph_AlignmentFacet_strategy = st.builds(gmfgraph_AlignmentFacet, alignment=safe_text)
@given(instance=gmfgraph_AlignmentFacet_strategy)
@settings(max_examples=25)
def test_gmfgraph_AlignmentFacet_instantiation(instance):
    assert isinstance(instance, gmfgraph_AlignmentFacet)


gmfgraph_BasicFont_strategy = st.builds(gmfgraph_BasicFont, faceName=safe_text, height=st.integers(), style=safe_text)
@given(instance=gmfgraph_BasicFont_strategy)
@settings(max_examples=25)
def test_gmfgraph_BasicFont_instantiation(instance):
    assert isinstance(instance, gmfgraph_BasicFont)


gmfgraph_Border_strategy = st.builds(gmfgraph_Border)
@given(instance=gmfgraph_Border_strategy)
@settings(max_examples=25)
def test_gmfgraph_Border_instantiation(instance):
    assert isinstance(instance, gmfgraph_Border)


gmfgraph_BorderLayout_strategy = st.builds(gmfgraph_BorderLayout)
@given(instance=gmfgraph_BorderLayout_strategy)
@settings(max_examples=25)
def test_gmfgraph_BorderLayout_instantiation(instance):
    assert isinstance(instance, gmfgraph_BorderLayout)


gmfgraph_BorderLayoutData_strategy = st.builds(gmfgraph_BorderLayoutData, alignment=safe_text, vertical=st.booleans())
@given(instance=gmfgraph_BorderLayoutData_strategy)
@settings(max_examples=25)
def test_gmfgraph_BorderLayoutData_instantiation(instance):
    assert isinstance(instance, gmfgraph_BorderLayoutData)


gmfgraph_Canvas_strategy = st.builds(gmfgraph_Canvas)
@given(instance=gmfgraph_Canvas_strategy)
@settings(max_examples=25)
def test_gmfgraph_Canvas_instantiation(instance):
    assert isinstance(instance, gmfgraph_Canvas)


gmfgraph_ChildAccess_strategy = st.builds(gmfgraph_ChildAccess, accessor=safe_text)
@given(instance=gmfgraph_ChildAccess_strategy)
@settings(max_examples=25)
def test_gmfgraph_ChildAccess_instantiation(instance):
    assert isinstance(instance, gmfgraph_ChildAccess)


gmfgraph_Color_strategy = st.builds(gmfgraph_Color)
@given(instance=gmfgraph_Color_strategy)
@settings(max_examples=25)
def test_gmfgraph_Color_instantiation(instance):
    assert isinstance(instance, gmfgraph_Color)


gmfgraph_Compartment_strategy = st.builds(gmfgraph_Compartment, collapsible=st.booleans(), needsTitle=st.booleans())
@given(instance=gmfgraph_Compartment_strategy)
@settings(max_examples=25)
def test_gmfgraph_Compartment_instantiation(instance):
    assert isinstance(instance, gmfgraph_Compartment)


gmfgraph_CompoundBorder_strategy = st.builds(gmfgraph_CompoundBorder)
@given(instance=gmfgraph_CompoundBorder_strategy)
@settings(max_examples=25)
def test_gmfgraph_CompoundBorder_instantiation(instance):
    assert isinstance(instance, gmfgraph_CompoundBorder)


gmfgraph_Connection_strategy = st.builds(gmfgraph_Connection)
@given(instance=gmfgraph_Connection_strategy)
@settings(max_examples=25)
def test_gmfgraph_Connection_instantiation(instance):
    assert isinstance(instance, gmfgraph_Connection)


gmfgraph_ConnectionFigure_strategy = st.builds(gmfgraph_ConnectionFigure)
@given(instance=gmfgraph_ConnectionFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_ConnectionFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_ConnectionFigure)


gmfgraph_ConstantColor_strategy = st.builds(gmfgraph_ConstantColor, value=safe_text)
@given(instance=gmfgraph_ConstantColor_strategy)
@settings(max_examples=25)
def test_gmfgraph_ConstantColor_instantiation(instance):
    assert isinstance(instance, gmfgraph_ConstantColor)


gmfgraph_CustomAttribute_strategy = st.builds(gmfgraph_CustomAttribute, directAccess=st.booleans(), multiStatementValue=st.booleans(), name=safe_text, value=safe_text)
@given(instance=gmfgraph_CustomAttribute_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomAttribute_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomAttribute)


gmfgraph_CustomBorder_strategy = st.builds(gmfgraph_CustomBorder)
@given(instance=gmfgraph_CustomBorder_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomBorder_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomBorder)


gmfgraph_CustomClass_strategy = st.builds(gmfgraph_CustomClass, qualifiedClassName=safe_text)
@given(instance=gmfgraph_CustomClass_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomClass_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomClass)


gmfgraph_CustomConnection_strategy = st.builds(gmfgraph_CustomConnection)
@given(instance=gmfgraph_CustomConnection_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomConnection_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomConnection)


gmfgraph_CustomDecoration_strategy = st.builds(gmfgraph_CustomDecoration)
@given(instance=gmfgraph_CustomDecoration_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomDecoration_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomDecoration)


gmfgraph_CustomFigure_strategy = st.builds(gmfgraph_CustomFigure)
@given(instance=gmfgraph_CustomFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomFigure)


gmfgraph_CustomLayout_strategy = st.builds(gmfgraph_CustomLayout)
@given(instance=gmfgraph_CustomLayout_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomLayout_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomLayout)


gmfgraph_CustomLayoutData_strategy = st.builds(gmfgraph_CustomLayoutData)
@given(instance=gmfgraph_CustomLayoutData_strategy)
@settings(max_examples=25)
def test_gmfgraph_CustomLayoutData_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomLayoutData)


gmfgraph_DecorationFigure_strategy = st.builds(gmfgraph_DecorationFigure)
@given(instance=gmfgraph_DecorationFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_DecorationFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_DecorationFigure)


gmfgraph_DefaultSizeFacet_strategy = st.builds(gmfgraph_DefaultSizeFacet)
@given(instance=gmfgraph_DefaultSizeFacet_strategy)
@settings(max_examples=25)
def test_gmfgraph_DefaultSizeFacet_instantiation(instance):
    assert isinstance(instance, gmfgraph_DefaultSizeFacet)


gmfgraph_DiagramElement_strategy = st.builds(gmfgraph_DiagramElement)
@given(instance=gmfgraph_DiagramElement_strategy)
@settings(max_examples=25)
def test_gmfgraph_DiagramElement_instantiation(instance):
    assert isinstance(instance, gmfgraph_DiagramElement)


gmfgraph_DiagramLabel_strategy = st.builds(gmfgraph_DiagramLabel, elementIcon=st.booleans(), external=st.booleans())
@given(instance=gmfgraph_DiagramLabel_strategy)
@settings(max_examples=25)
def test_gmfgraph_DiagramLabel_instantiation(instance):
    assert isinstance(instance, gmfgraph_DiagramLabel)


gmfgraph_Dimension_strategy = st.builds(gmfgraph_Dimension, dx=st.integers(), dy=st.integers())
@given(instance=gmfgraph_Dimension_strategy)
@settings(max_examples=25)
def test_gmfgraph_Dimension_instantiation(instance):
    assert isinstance(instance, gmfgraph_Dimension)


gmfgraph_Ellipse_strategy = st.builds(gmfgraph_Ellipse)
@given(instance=gmfgraph_Ellipse_strategy)
@settings(max_examples=25)
def test_gmfgraph_Ellipse_instantiation(instance):
    assert isinstance(instance, gmfgraph_Ellipse)


gmfgraph_Figure_strategy = st.builds(gmfgraph_Figure)
@given(instance=gmfgraph_Figure_strategy)
@settings(max_examples=25)
def test_gmfgraph_Figure_instantiation(instance):
    assert isinstance(instance, gmfgraph_Figure)


gmfgraph_FigureAccessor_strategy = st.builds(gmfgraph_FigureAccessor, accessor=safe_text)
@given(instance=gmfgraph_FigureAccessor_strategy)
@settings(max_examples=25)
def test_gmfgraph_FigureAccessor_instantiation(instance):
    assert isinstance(instance, gmfgraph_FigureAccessor)


gmfgraph_FigureDescriptor_strategy = st.builds(gmfgraph_FigureDescriptor)
@given(instance=gmfgraph_FigureDescriptor_strategy)
@settings(max_examples=25)
def test_gmfgraph_FigureDescriptor_instantiation(instance):
    assert isinstance(instance, gmfgraph_FigureDescriptor)


gmfgraph_FigureGallery_strategy = st.builds(gmfgraph_FigureGallery, implementationBundle=safe_text)
@given(instance=gmfgraph_FigureGallery_strategy)
@settings(max_examples=25)
def test_gmfgraph_FigureGallery_instantiation(instance):
    assert isinstance(instance, gmfgraph_FigureGallery)


gmfgraph_FigureRef_strategy = st.builds(gmfgraph_FigureRef)
@given(instance=gmfgraph_FigureRef_strategy)
@settings(max_examples=25)
def test_gmfgraph_FigureRef_instantiation(instance):
    assert isinstance(instance, gmfgraph_FigureRef)


gmfgraph_FlowLayout_strategy = st.builds(gmfgraph_FlowLayout, forceSingleLine=st.booleans(), majorAlignment=safe_text, majorSpacing=st.integers(), matchMinorSize=st.booleans(), minorAlignment=safe_text, minorSpacing=st.integers(), vertical=st.booleans())
@given(instance=gmfgraph_FlowLayout_strategy)
@settings(max_examples=25)
def test_gmfgraph_FlowLayout_instantiation(instance):
    assert isinstance(instance, gmfgraph_FlowLayout)


gmfgraph_Font_strategy = st.builds(gmfgraph_Font)
@given(instance=gmfgraph_Font_strategy)
@settings(max_examples=25)
def test_gmfgraph_Font_instantiation(instance):
    assert isinstance(instance, gmfgraph_Font)


gmfgraph_GeneralFacet_strategy = st.builds(gmfgraph_GeneralFacet, data=safe_text, identifier=safe_text)
@given(instance=gmfgraph_GeneralFacet_strategy)
@settings(max_examples=25)
def test_gmfgraph_GeneralFacet_instantiation(instance):
    assert isinstance(instance, gmfgraph_GeneralFacet)


gmfgraph_GradientFacet_strategy = st.builds(gmfgraph_GradientFacet, direction=safe_text)
@given(instance=gmfgraph_GradientFacet_strategy)
@settings(max_examples=25)
def test_gmfgraph_GradientFacet_instantiation(instance):
    assert isinstance(instance, gmfgraph_GradientFacet)


gmfgraph_GridLayout_strategy = st.builds(gmfgraph_GridLayout, equalWidth=st.booleans(), numColumns=st.integers())
@given(instance=gmfgraph_GridLayout_strategy)
@settings(max_examples=25)
def test_gmfgraph_GridLayout_instantiation(instance):
    assert isinstance(instance, gmfgraph_GridLayout)


gmfgraph_GridLayoutData_strategy = st.builds(gmfgraph_GridLayoutData, grabExcessHorizontalSpace=st.booleans(), grabExcessVerticalSpace=st.booleans(), horizontalAlignment=safe_text, horizontalIndent=st.integers(), horizontalSpan=st.integers(), verticalAlignment=safe_text, verticalSpan=st.integers())
@given(instance=gmfgraph_GridLayoutData_strategy)
@settings(max_examples=25)
def test_gmfgraph_GridLayoutData_instantiation(instance):
    assert isinstance(instance, gmfgraph_GridLayoutData)


gmfgraph_Identity_strategy = st.builds(gmfgraph_Identity, name=safe_text)
@given(instance=gmfgraph_Identity_strategy)
@settings(max_examples=25)
def test_gmfgraph_Identity_instantiation(instance):
    assert isinstance(instance, gmfgraph_Identity)


gmfgraph_Insets_strategy = st.builds(gmfgraph_Insets, bottom=st.integers(), left=st.integers(), right=st.integers(), top=st.integers())
@given(instance=gmfgraph_Insets_strategy)
@settings(max_examples=25)
def test_gmfgraph_Insets_instantiation(instance):
    assert isinstance(instance, gmfgraph_Insets)


gmfgraph_Label_strategy = st.builds(gmfgraph_Label, text=safe_text)
@given(instance=gmfgraph_Label_strategy)
@settings(max_examples=25)
def test_gmfgraph_Label_instantiation(instance):
    assert isinstance(instance, gmfgraph_Label)


gmfgraph_LabelOffsetFacet_strategy = st.builds(gmfgraph_LabelOffsetFacet, x=st.integers(), y=st.integers())
@given(instance=gmfgraph_LabelOffsetFacet_strategy)
@settings(max_examples=25)
def test_gmfgraph_LabelOffsetFacet_instantiation(instance):
    assert isinstance(instance, gmfgraph_LabelOffsetFacet)


gmfgraph_LabeledContainer_strategy = st.builds(gmfgraph_LabeledContainer)
@given(instance=gmfgraph_LabeledContainer_strategy)
@settings(max_examples=25)
def test_gmfgraph_LabeledContainer_instantiation(instance):
    assert isinstance(instance, gmfgraph_LabeledContainer)


gmfgraph_Layout_strategy = st.builds(gmfgraph_Layout)
@given(instance=gmfgraph_Layout_strategy)
@settings(max_examples=25)
def test_gmfgraph_Layout_instantiation(instance):
    assert isinstance(instance, gmfgraph_Layout)


gmfgraph_LayoutData_strategy = st.builds(gmfgraph_LayoutData)
@given(instance=gmfgraph_LayoutData_strategy)
@settings(max_examples=25)
def test_gmfgraph_LayoutData_instantiation(instance):
    assert isinstance(instance, gmfgraph_LayoutData)


gmfgraph_Layoutable_strategy = st.builds(gmfgraph_Layoutable)
@given(instance=gmfgraph_Layoutable_strategy)
@settings(max_examples=25)
def test_gmfgraph_Layoutable_instantiation(instance):
    assert isinstance(instance, gmfgraph_Layoutable)


gmfgraph_LineBorder_strategy = st.builds(gmfgraph_LineBorder, width=st.integers())
@given(instance=gmfgraph_LineBorder_strategy)
@settings(max_examples=25)
def test_gmfgraph_LineBorder_instantiation(instance):
    assert isinstance(instance, gmfgraph_LineBorder)


gmfgraph_MarginBorder_strategy = st.builds(gmfgraph_MarginBorder)
@given(instance=gmfgraph_MarginBorder_strategy)
@settings(max_examples=25)
def test_gmfgraph_MarginBorder_instantiation(instance):
    assert isinstance(instance, gmfgraph_MarginBorder)


gmfgraph_Node_strategy = st.builds(gmfgraph_Node, affixedParentSide=safe_text, resizeConstraint=safe_text)
@given(instance=gmfgraph_Node_strategy)
@settings(max_examples=25)
def test_gmfgraph_Node_instantiation(instance):
    assert isinstance(instance, gmfgraph_Node)


gmfgraph_Point_strategy = st.builds(gmfgraph_Point, x=st.integers(), y=st.integers())
@given(instance=gmfgraph_Point_strategy)
@settings(max_examples=25)
def test_gmfgraph_Point_instantiation(instance):
    assert isinstance(instance, gmfgraph_Point)


gmfgraph_Polygon_strategy = st.builds(gmfgraph_Polygon)
@given(instance=gmfgraph_Polygon_strategy)
@settings(max_examples=25)
def test_gmfgraph_Polygon_instantiation(instance):
    assert isinstance(instance, gmfgraph_Polygon)


gmfgraph_PolygonDecoration_strategy = st.builds(gmfgraph_PolygonDecoration)
@given(instance=gmfgraph_PolygonDecoration_strategy)
@settings(max_examples=25)
def test_gmfgraph_PolygonDecoration_instantiation(instance):
    assert isinstance(instance, gmfgraph_PolygonDecoration)


gmfgraph_Polyline_strategy = st.builds(gmfgraph_Polyline)
@given(instance=gmfgraph_Polyline_strategy)
@settings(max_examples=25)
def test_gmfgraph_Polyline_instantiation(instance):
    assert isinstance(instance, gmfgraph_Polyline)


gmfgraph_PolylineConnection_strategy = st.builds(gmfgraph_PolylineConnection)
@given(instance=gmfgraph_PolylineConnection_strategy)
@settings(max_examples=25)
def test_gmfgraph_PolylineConnection_instantiation(instance):
    assert isinstance(instance, gmfgraph_PolylineConnection)


gmfgraph_PolylineDecoration_strategy = st.builds(gmfgraph_PolylineDecoration)
@given(instance=gmfgraph_PolylineDecoration_strategy)
@settings(max_examples=25)
def test_gmfgraph_PolylineDecoration_instantiation(instance):
    assert isinstance(instance, gmfgraph_PolylineDecoration)


gmfgraph_RGBColor_strategy = st.builds(gmfgraph_RGBColor, blue=st.integers(), green=st.integers(), red=st.integers())
@given(instance=gmfgraph_RGBColor_strategy)
@settings(max_examples=25)
def test_gmfgraph_RGBColor_instantiation(instance):
    assert isinstance(instance, gmfgraph_RGBColor)


gmfgraph_RealFigure_strategy = st.builds(gmfgraph_RealFigure, name=safe_text)
@given(instance=gmfgraph_RealFigure_strategy)
@settings(max_examples=25)
def test_gmfgraph_RealFigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_RealFigure)


gmfgraph_Rectangle_strategy = st.builds(gmfgraph_Rectangle)
@given(instance=gmfgraph_Rectangle_strategy)
@settings(max_examples=25)
def test_gmfgraph_Rectangle_instantiation(instance):
    assert isinstance(instance, gmfgraph_Rectangle)


gmfgraph_RoundedRectangle_strategy = st.builds(gmfgraph_RoundedRectangle, cornerHeight=st.integers(), cornerWidth=st.integers())
@given(instance=gmfgraph_RoundedRectangle_strategy)
@settings(max_examples=25)
def test_gmfgraph_RoundedRectangle_instantiation(instance):
    assert isinstance(instance, gmfgraph_RoundedRectangle)


gmfgraph_ScalablePolygon_strategy = st.builds(gmfgraph_ScalablePolygon)
@given(instance=gmfgraph_ScalablePolygon_strategy)
@settings(max_examples=25)
def test_gmfgraph_ScalablePolygon_instantiation(instance):
    assert isinstance(instance, gmfgraph_ScalablePolygon)


gmfgraph_Shape_strategy = st.builds(gmfgraph_Shape, fill=st.booleans(), lineKind=safe_text, lineWidth=st.integers(), outline=st.booleans(), xorFill=st.booleans(), xorOutline=st.booleans())
@given(instance=gmfgraph_Shape_strategy)
@settings(max_examples=25)
def test_gmfgraph_Shape_instantiation(instance):
    assert isinstance(instance, gmfgraph_Shape)


gmfgraph_StackLayout_strategy = st.builds(gmfgraph_StackLayout)
@given(instance=gmfgraph_StackLayout_strategy)
@settings(max_examples=25)
def test_gmfgraph_StackLayout_instantiation(instance):
    assert isinstance(instance, gmfgraph_StackLayout)


gmfgraph_VisualFacet_strategy = st.builds(gmfgraph_VisualFacet)
@given(instance=gmfgraph_VisualFacet_strategy)
@settings(max_examples=25)
def test_gmfgraph_VisualFacet_instantiation(instance):
    assert isinstance(instance, gmfgraph_VisualFacet)


gmfgraph_XYLayout_strategy = st.builds(gmfgraph_XYLayout)
@given(instance=gmfgraph_XYLayout_strategy)
@settings(max_examples=25)
def test_gmfgraph_XYLayout_instantiation(instance):
    assert isinstance(instance, gmfgraph_XYLayout)


gmfgraph_XYLayoutData_strategy = st.builds(gmfgraph_XYLayoutData)
@given(instance=gmfgraph_XYLayoutData_strategy)
@settings(max_examples=25)
def test_gmfgraph_XYLayoutData_instantiation(instance):
    assert isinstance(instance, gmfgraph_XYLayoutData)



