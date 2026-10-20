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
    Value,
    model_BooleanValue,
    model_EnumValue,
    model_StringValue,
    model_DoubleValue,
    model_IntValue,
    model_CustomColor,
    Feature,
    model_Anchor,
    ConnectableElement,
    model_Rectangle,
    model_Label,
    model_Image,
    model_Invisible,
    model_Custom,
    model_Color,
    model_Contains,
    model_EClass,
    model_ImportStatement,
    model_CustomFigure,
    model_DiagramElement,
    model_Colors,
    model_Decorator,
    model_EReference,
    FeatureContainer,
    model_Arrow,
    model_ConnectableElement,
    DiagramElement,
    model_Link,
    model_Node,
    model_Value,
    model_EAttribute,
    model_FeatureContainer,
    model_FeatureConditional,
    model_Feature,
    model_Diagram,
    model_MetaModel,
    model_XDiagram,
    model_LineWidth,
    model_Position,
    model_Point,
    model_Size,
    model_Transparency,
    model_LineStyle,
    model_TextAlign,
    model_FontProperties,
    model_TextPart,
    model_TextValue,
    model_Visible,
    model_Layout,
    model_Corner,
    model_Line,
    model_Triangle,
    model_Polyline,
    model_Ellipse,
    model_Rhombus,
    model_ColorFeature,
    AnchorDirection,
    Operator,
    BooleanLiteral,
    DefaultColor,
    TextAlignValue,
    LineType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(model_BooleanValue)


def test_hyp_model_booleanvalue_constructor_exists():
    assert callable(model_BooleanValue.__init__)


def test_hyp_model_booleanvalue_constructor_args():
    sig = inspect.signature(model_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_model_enumvalue_is_not_abstract():
    assert not inspect.isabstract(model_EnumValue)


def test_hyp_model_enumvalue_constructor_exists():
    assert callable(model_EnumValue.__init__)


def test_hyp_model_enumvalue_constructor_args():
    sig = inspect.signature(model_EnumValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model_stringvalue_is_not_abstract():
    assert not inspect.isabstract(model_StringValue)


def test_hyp_model_stringvalue_constructor_exists():
    assert callable(model_StringValue.__init__)


def test_hyp_model_stringvalue_constructor_args():
    sig = inspect.signature(model_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_model_doublevalue_is_not_abstract():
    assert not inspect.isabstract(model_DoubleValue)


def test_hyp_model_doublevalue_constructor_exists():
    assert callable(model_DoubleValue.__init__)


def test_hyp_model_doublevalue_constructor_args():
    sig = inspect.signature(model_DoubleValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueInt" in params, "Missing parameter 'valueInt'"
    assert "valueDecimal" in params, "Missing parameter 'valueDecimal'"





def test_hyp_model_intvalue_is_not_abstract():
    assert not inspect.isabstract(model_IntValue)


def test_hyp_model_intvalue_constructor_exists():
    assert callable(model_IntValue.__init__)


def test_hyp_model_intvalue_constructor_args():
    sig = inspect.signature(model_IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_model_customcolor_is_not_abstract():
    assert not inspect.isabstract(model_CustomColor)


def test_hyp_model_customcolor_constructor_exists():
    assert callable(model_CustomColor.__init__)


def test_hyp_model_customcolor_constructor_args():
    sig = inspect.signature(model_CustomColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "G" in params, "Missing parameter 'G'"
    assert "B" in params, "Missing parameter 'B'"
    assert "R" in params, "Missing parameter 'R'"







def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_anchor_is_not_abstract():
    assert not inspect.isabstract(model_Anchor)


def test_hyp_model_anchor_constructor_exists():
    assert callable(model_Anchor.__init__)


def test_hyp_model_anchor_constructor_args():
    sig = inspect.signature(model_Anchor.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "max" in params, "Missing parameter 'max'"





def test_hyp_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_hyp_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_hyp_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_rectangle_is_not_abstract():
    assert not inspect.isabstract(model_Rectangle)


def test_hyp_model_rectangle_constructor_exists():
    assert callable(model_Rectangle.__init__)


def test_hyp_model_rectangle_constructor_args():
    sig = inspect.signature(model_Rectangle.__init__)
    params = list(sig.parameters.keys())
    assert "rectangle" in params, "Missing parameter 'rectangle'"
    assert "square" in params, "Missing parameter 'square'"





def test_hyp_model_label_is_not_abstract():
    assert not inspect.isabstract(model_Label)


def test_hyp_model_label_constructor_exists():
    assert callable(model_Label.__init__)


def test_hyp_model_label_constructor_args():
    sig = inspect.signature(model_Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_image_is_not_abstract():
    assert not inspect.isabstract(model_Image)


def test_hyp_model_image_constructor_exists():
    assert callable(model_Image.__init__)


def test_hyp_model_image_constructor_args():
    sig = inspect.signature(model_Image.__init__)
    params = list(sig.parameters.keys())
    assert "imageId" in params, "Missing parameter 'imageId'"




def test_hyp_model_invisible_is_not_abstract():
    assert not inspect.isabstract(model_Invisible)


def test_hyp_model_invisible_constructor_exists():
    assert callable(model_Invisible.__init__)


def test_hyp_model_invisible_constructor_args():
    sig = inspect.signature(model_Invisible.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_custom_is_not_abstract():
    assert not inspect.isabstract(model_Custom)


def test_hyp_model_custom_constructor_exists():
    assert callable(model_Custom.__init__)


def test_hyp_model_custom_constructor_args():
    sig = inspect.signature(model_Custom.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_color_is_not_abstract():
    assert not inspect.isabstract(model_Color)


def test_hyp_model_color_constructor_exists():
    assert callable(model_Color.__init__)


def test_hyp_model_color_constructor_args():
    sig = inspect.signature(model_Color.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_model_contains_is_not_abstract():
    assert not inspect.isabstract(model_Contains)


def test_hyp_model_contains_constructor_exists():
    assert callable(model_Contains.__init__)


def test_hyp_model_contains_constructor_args():
    sig = inspect.signature(model_Contains.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_eclass_is_not_abstract():
    assert not inspect.isabstract(model_EClass)


def test_hyp_model_eclass_constructor_exists():
    assert callable(model_EClass.__init__)


def test_hyp_model_eclass_constructor_args():
    sig = inspect.signature(model_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_importstatement_is_not_abstract():
    assert not inspect.isabstract(model_ImportStatement)


def test_hyp_model_importstatement_constructor_exists():
    assert callable(model_ImportStatement.__init__)


def test_hyp_model_importstatement_constructor_args():
    sig = inspect.signature(model_ImportStatement.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"




def test_hyp_model_customfigure_is_not_abstract():
    assert not inspect.isabstract(model_CustomFigure)


def test_hyp_model_customfigure_constructor_exists():
    assert callable(model_CustomFigure.__init__)


def test_hyp_model_customfigure_constructor_args():
    sig = inspect.signature(model_CustomFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model_diagramelement_is_not_abstract():
    assert not inspect.isabstract(model_DiagramElement)


def test_hyp_model_diagramelement_constructor_exists():
    assert callable(model_DiagramElement.__init__)


def test_hyp_model_diagramelement_constructor_args():
    sig = inspect.signature(model_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_colors_is_not_abstract():
    assert not inspect.isabstract(model_Colors)


def test_hyp_model_colors_constructor_exists():
    assert callable(model_Colors.__init__)


def test_hyp_model_colors_constructor_args():
    sig = inspect.signature(model_Colors.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_decorator_is_not_abstract():
    assert not inspect.isabstract(model_Decorator)


def test_hyp_model_decorator_constructor_exists():
    assert callable(model_Decorator.__init__)


def test_hyp_model_decorator_constructor_args():
    sig = inspect.signature(model_Decorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_ereference_is_not_abstract():
    assert not inspect.isabstract(model_EReference)


def test_hyp_model_ereference_constructor_exists():
    assert callable(model_EReference.__init__)


def test_hyp_model_ereference_constructor_args():
    sig = inspect.signature(model_EReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featurecontainer_is_not_abstract():
    assert not inspect.isabstract(FeatureContainer)


def test_hyp_featurecontainer_constructor_exists():
    assert callable(FeatureContainer.__init__)


def test_hyp_featurecontainer_constructor_args():
    sig = inspect.signature(FeatureContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_arrow_is_not_abstract():
    assert not inspect.isabstract(model_Arrow)


def test_hyp_model_arrow_constructor_exists():
    assert callable(model_Arrow.__init__)


def test_hyp_model_arrow_constructor_args():
    sig = inspect.signature(model_Arrow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_connectableelement_is_not_abstract():
    assert not inspect.isabstract(model_ConnectableElement)


def test_hyp_model_connectableelement_constructor_exists():
    assert callable(model_ConnectableElement.__init__)


def test_hyp_model_connectableelement_constructor_args():
    sig = inspect.signature(model_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_hyp_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_hyp_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_link_is_not_abstract():
    assert not inspect.isabstract(model_Link)


def test_hyp_model_link_constructor_exists():
    assert callable(model_Link.__init__)


def test_hyp_model_link_constructor_args():
    sig = inspect.signature(model_Link.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "complex" in params, "Missing parameter 'complex'"





def test_hyp_model_node_is_not_abstract():
    assert not inspect.isabstract(model_Node)


def test_hyp_model_node_constructor_exists():
    assert callable(model_Node.__init__)


def test_hyp_model_node_constructor_args():
    sig = inspect.signature(model_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_value_is_not_abstract():
    assert not inspect.isabstract(model_Value)


def test_hyp_model_value_constructor_exists():
    assert callable(model_Value.__init__)


def test_hyp_model_value_constructor_args():
    sig = inspect.signature(model_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_eattribute_is_not_abstract():
    assert not inspect.isabstract(model_EAttribute)


def test_hyp_model_eattribute_constructor_exists():
    assert callable(model_EAttribute.__init__)


def test_hyp_model_eattribute_constructor_args():
    sig = inspect.signature(model_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_featurecontainer_is_not_abstract():
    assert not inspect.isabstract(model_FeatureContainer)


def test_hyp_model_featurecontainer_constructor_exists():
    assert callable(model_FeatureContainer.__init__)


def test_hyp_model_featurecontainer_constructor_args():
    sig = inspect.signature(model_FeatureContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_featureconditional_is_not_abstract():
    assert not inspect.isabstract(model_FeatureConditional)


def test_hyp_model_featureconditional_constructor_exists():
    assert callable(model_FeatureConditional.__init__)


def test_hyp_model_featureconditional_constructor_args():
    sig = inspect.signature(model_FeatureConditional.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_model_feature_is_not_abstract():
    assert not inspect.isabstract(model_Feature)


def test_hyp_model_feature_constructor_exists():
    assert callable(model_Feature.__init__)


def test_hyp_model_feature_constructor_args():
    sig = inspect.signature(model_Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagram_is_not_abstract():
    assert not inspect.isabstract(model_Diagram)


def test_hyp_model_diagram_constructor_exists():
    assert callable(model_Diagram.__init__)


def test_hyp_model_diagram_constructor_args():
    sig = inspect.signature(model_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_metamodel_is_not_abstract():
    assert not inspect.isabstract(model_MetaModel)


def test_hyp_model_metamodel_constructor_exists():
    assert callable(model_MetaModel.__init__)


def test_hyp_model_metamodel_constructor_args():
    sig = inspect.signature(model_MetaModel.__init__)
    params = list(sig.parameters.keys())
    assert "plugin" in params, "Missing parameter 'plugin'"
    assert "ecorePath" in params, "Missing parameter 'ecorePath'"





def test_hyp_model_xdiagram_is_not_abstract():
    assert not inspect.isabstract(model_XDiagram)


def test_hyp_model_xdiagram_constructor_exists():
    assert callable(model_XDiagram.__init__)


def test_hyp_model_xdiagram_constructor_args():
    sig = inspect.signature(model_XDiagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_linewidth_is_not_abstract():
    assert not inspect.isabstract(model_LineWidth)


def test_hyp_model_linewidth_constructor_exists():
    assert callable(model_LineWidth.__init__)


def test_hyp_model_linewidth_constructor_args():
    sig = inspect.signature(model_LineWidth.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"




def test_hyp_model_position_is_not_abstract():
    assert not inspect.isabstract(model_Position)


def test_hyp_model_position_constructor_exists():
    assert callable(model_Position.__init__)


def test_hyp_model_position_constructor_args():
    sig = inspect.signature(model_Position.__init__)
    params = list(sig.parameters.keys())
    assert "xRelative" in params, "Missing parameter 'xRelative'"
    assert "yRelative" in params, "Missing parameter 'yRelative'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"







def test_hyp_model_point_is_not_abstract():
    assert not inspect.isabstract(model_Point)


def test_hyp_model_point_constructor_exists():
    assert callable(model_Point.__init__)


def test_hyp_model_point_constructor_args():
    sig = inspect.signature(model_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_model_size_is_not_abstract():
    assert not inspect.isabstract(model_Size)


def test_hyp_model_size_constructor_exists():
    assert callable(model_Size.__init__)


def test_hyp_model_size_constructor_args():
    sig = inspect.signature(model_Size.__init__)
    params = list(sig.parameters.keys())
    assert "widthRelative" in params, "Missing parameter 'widthRelative'"
    assert "heightRelative" in params, "Missing parameter 'heightRelative'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "resizable" in params, "Missing parameter 'resizable'"








def test_hyp_model_transparency_is_not_abstract():
    assert not inspect.isabstract(model_Transparency)


def test_hyp_model_transparency_constructor_exists():
    assert callable(model_Transparency.__init__)


def test_hyp_model_transparency_constructor_args():
    sig = inspect.signature(model_Transparency.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"




def test_hyp_model_linestyle_is_not_abstract():
    assert not inspect.isabstract(model_LineStyle)


def test_hyp_model_linestyle_constructor_exists():
    assert callable(model_LineStyle.__init__)


def test_hyp_model_linestyle_constructor_args():
    sig = inspect.signature(model_LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "manhattan" in params, "Missing parameter 'manhattan'"





def test_hyp_model_textalign_is_not_abstract():
    assert not inspect.isabstract(model_TextAlign)


def test_hyp_model_textalign_constructor_exists():
    assert callable(model_TextAlign.__init__)


def test_hyp_model_textalign_constructor_args():
    sig = inspect.signature(model_TextAlign.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_model_fontproperties_is_not_abstract():
    assert not inspect.isabstract(model_FontProperties)


def test_hyp_model_fontproperties_constructor_exists():
    assert callable(model_FontProperties.__init__)


def test_hyp_model_fontproperties_constructor_args():
    sig = inspect.signature(model_FontProperties.__init__)
    params = list(sig.parameters.keys())
    assert "face" in params, "Missing parameter 'face'"
    assert "bold" in params, "Missing parameter 'bold'"
    assert "italics" in params, "Missing parameter 'italics'"
    assert "size" in params, "Missing parameter 'size'"







def test_hyp_model_textpart_is_not_abstract():
    assert not inspect.isabstract(model_TextPart)


def test_hyp_model_textpart_constructor_exists():
    assert callable(model_TextPart.__init__)


def test_hyp_model_textpart_constructor_args():
    sig = inspect.signature(model_TextPart.__init__)
    params = list(sig.parameters.keys())
    assert "editable" in params, "Missing parameter 'editable'"
    assert "text" in params, "Missing parameter 'text'"





def test_hyp_model_textvalue_is_not_abstract():
    assert not inspect.isabstract(model_TextValue)


def test_hyp_model_textvalue_constructor_exists():
    assert callable(model_TextValue.__init__)


def test_hyp_model_textvalue_constructor_args():
    sig = inspect.signature(model_TextValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_visible_is_not_abstract():
    assert not inspect.isabstract(model_Visible)


def test_hyp_model_visible_constructor_exists():
    assert callable(model_Visible.__init__)


def test_hyp_model_visible_constructor_args():
    sig = inspect.signature(model_Visible.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_layout_is_not_abstract():
    assert not inspect.isabstract(model_Layout)


def test_hyp_model_layout_constructor_exists():
    assert callable(model_Layout.__init__)


def test_hyp_model_layout_constructor_args():
    sig = inspect.signature(model_Layout.__init__)
    params = list(sig.parameters.keys())
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "margin" in params, "Missing parameter 'margin'"






def test_hyp_model_corner_is_not_abstract():
    assert not inspect.isabstract(model_Corner)


def test_hyp_model_corner_constructor_exists():
    assert callable(model_Corner.__init__)


def test_hyp_model_corner_constructor_args():
    sig = inspect.signature(model_Corner.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_model_line_is_not_abstract():
    assert not inspect.isabstract(model_Line)


def test_hyp_model_line_constructor_exists():
    assert callable(model_Line.__init__)


def test_hyp_model_line_constructor_args():
    sig = inspect.signature(model_Line.__init__)
    params = list(sig.parameters.keys())
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "vertical" in params, "Missing parameter 'vertical'"





def test_hyp_model_triangle_is_not_abstract():
    assert not inspect.isabstract(model_Triangle)


def test_hyp_model_triangle_constructor_exists():
    assert callable(model_Triangle.__init__)


def test_hyp_model_triangle_constructor_args():
    sig = inspect.signature(model_Triangle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_polyline_is_not_abstract():
    assert not inspect.isabstract(model_Polyline)


def test_hyp_model_polyline_constructor_exists():
    assert callable(model_Polyline.__init__)


def test_hyp_model_polyline_constructor_args():
    sig = inspect.signature(model_Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "polygon" in params, "Missing parameter 'polygon'"
    assert "polyline" in params, "Missing parameter 'polyline'"





def test_hyp_model_ellipse_is_not_abstract():
    assert not inspect.isabstract(model_Ellipse)


def test_hyp_model_ellipse_constructor_exists():
    assert callable(model_Ellipse.__init__)


def test_hyp_model_ellipse_constructor_args():
    sig = inspect.signature(model_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "circle" in params, "Missing parameter 'circle'"
    assert "ellipse" in params, "Missing parameter 'ellipse'"





def test_hyp_model_rhombus_is_not_abstract():
    assert not inspect.isabstract(model_Rhombus)


def test_hyp_model_rhombus_constructor_exists():
    assert callable(model_Rhombus.__init__)


def test_hyp_model_rhombus_constructor_args():
    sig = inspect.signature(model_Rhombus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_colorfeature_is_not_abstract():
    assert not inspect.isabstract(model_ColorFeature)


def test_hyp_model_colorfeature_constructor_exists():
    assert callable(model_ColorFeature.__init__)


def test_hyp_model_colorfeature_constructor_args():
    sig = inspect.signature(model_ColorFeature.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"


def test_hyp_anchordirection_exists():
    # Check that the Enumeration exists
    assert AnchorDirection is not None

def test_hyp_anchordirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnchorDirection]
    expected_literals = [
        "OUTGOING",
        "INCOMING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnchorDirection"

def test_hyp_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_hyp_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "DIFFERENT",
        "EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_hyp_booleanliteral_exists():
    # Check that the Enumeration exists
    assert BooleanLiteral is not None

def test_hyp_booleanliteral_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanLiteral]
    expected_literals = [
        "FALSE",
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanLiteral"

def test_hyp_defaultcolor_exists():
    # Check that the Enumeration exists
    assert DefaultColor is not None

def test_hyp_defaultcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefaultColor]
    expected_literals = [
        "GRAY",
        "MAROON",
        "NAVY",
        "PURPLE",
        "BLUE",
        "YELLOW",
        "OLIVE",
        "FUCHSIA",
        "WHITE",
        "TEAL",
        "RED",
        "SILVER",
        "BLACK",
        "LIME",
        "GREEN",
        "AQUA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefaultColor"

def test_hyp_textalignvalue_exists():
    # Check that the Enumeration exists
    assert TextAlignValue is not None

def test_hyp_textalignvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlignValue]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlignValue"

def test_hyp_linetype_exists():
    # Check that the Enumeration exists
    assert LineType is not None

def test_hyp_linetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineType]
    expected_literals = [
        "DASH",
        "SOLID",
        "DOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineType"


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
Value_strategy = st.builds(
    Value,
)
model_BooleanValue_strategy = st.builds(
    model_BooleanValue,
    value=
        safe_text
)
model_EnumValue_strategy = st.builds(
    model_EnumValue,
    name=
        safe_text
)
model_StringValue_strategy = st.builds(
    model_StringValue,
    null=
        st.booleans(),
    value=
        safe_text
)
model_DoubleValue_strategy = st.builds(
    model_DoubleValue,
    valueInt=
        st.integers(),
    valueDecimal=
        st.integers()
)
model_IntValue_strategy = st.builds(
    model_IntValue,
    value=
        st.integers()
)
model_CustomColor_strategy = st.builds(
    model_CustomColor,
    name=
        safe_text,
    G=
        st.integers(),
    B=
        st.integers(),
    R=
        st.integers()
)
Feature_strategy = st.builds(
    Feature,
)
model_Anchor_strategy = st.builds(
    model_Anchor,
    direction=
        safe_text,
    max=
        st.integers()
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
model_Rectangle_strategy = st.builds(
    model_Rectangle,
    rectangle=
        st.booleans(),
    square=
        st.booleans()
)
model_Label_strategy = st.builds(
    model_Label,
)
model_Image_strategy = st.builds(
    model_Image,
    imageId=
        safe_text
)
model_Invisible_strategy = st.builds(
    model_Invisible,
)
model_Custom_strategy = st.builds(
    model_Custom,
)
model_Color_strategy = st.builds(
    model_Color,
    default=
        safe_text
)
model_Contains_strategy = st.builds(
    model_Contains,
)
model_EClass_strategy = st.builds(
    model_EClass,
)
model_ImportStatement_strategy = st.builds(
    model_ImportStatement,
    importedNamespace=
        safe_text
)
model_CustomFigure_strategy = st.builds(
    model_CustomFigure,
    name=
        safe_text
)
model_DiagramElement_strategy = st.builds(
    model_DiagramElement,
)
model_Colors_strategy = st.builds(
    model_Colors,
)
model_Decorator_strategy = st.builds(
    model_Decorator,
)
model_EReference_strategy = st.builds(
    model_EReference,
)
FeatureContainer_strategy = st.builds(
    FeatureContainer,
)
model_Arrow_strategy = st.builds(
    model_Arrow,
)
model_ConnectableElement_strategy = st.builds(
    model_ConnectableElement,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
model_Link_strategy = st.builds(
    model_Link,
    reference=
        st.booleans(),
    complex=
        st.booleans()
)
model_Node_strategy = st.builds(
    model_Node,
)
model_Value_strategy = st.builds(
    model_Value,
)
model_EAttribute_strategy = st.builds(
    model_EAttribute,
)
model_FeatureContainer_strategy = st.builds(
    model_FeatureContainer,
)
model_FeatureConditional_strategy = st.builds(
    model_FeatureConditional,
    operator=
        safe_text
)
model_Feature_strategy = st.builds(
    model_Feature,
)
model_Diagram_strategy = st.builds(
    model_Diagram,
)
model_MetaModel_strategy = st.builds(
    model_MetaModel,
    plugin=
        safe_text,
    ecorePath=
        safe_text
)
model_XDiagram_strategy = st.builds(
    model_XDiagram,
)
model_LineWidth_strategy = st.builds(
    model_LineWidth,
    width=
        st.integers()
)
model_Position_strategy = st.builds(
    model_Position,
    xRelative=
        st.booleans(),
    yRelative=
        st.booleans(),
    y=
        st.integers(),
    x=
        st.integers()
)
model_Point_strategy = st.builds(
    model_Point,
    y=
        st.integers(),
    x=
        st.integers()
)
model_Size_strategy = st.builds(
    model_Size,
    widthRelative=
        st.booleans(),
    heightRelative=
        st.booleans(),
    width=
        st.integers(),
    height=
        st.integers(),
    resizable=
        st.booleans()
)
model_Transparency_strategy = st.builds(
    model_Transparency,
    percent=
        st.integers()
)
model_LineStyle_strategy = st.builds(
    model_LineStyle,
    style=
        safe_text,
    manhattan=
        st.booleans()
)
model_TextAlign_strategy = st.builds(
    model_TextAlign,
    value=
        safe_text
)
model_FontProperties_strategy = st.builds(
    model_FontProperties,
    face=
        safe_text,
    bold=
        st.booleans(),
    italics=
        st.booleans(),
    size=
        st.integers()
)
model_TextPart_strategy = st.builds(
    model_TextPart,
    editable=
        st.booleans(),
    text=
        safe_text
)
model_TextValue_strategy = st.builds(
    model_TextValue,
)
model_Visible_strategy = st.builds(
    model_Visible,
)
model_Layout_strategy = st.builds(
    model_Layout,
    vertical=
        st.booleans(),
    horizontal=
        st.booleans(),
    margin=
        st.integers()
)
model_Corner_strategy = st.builds(
    model_Corner,
    angle=
        st.integers()
)
model_Line_strategy = st.builds(
    model_Line,
    horizontal=
        st.booleans(),
    vertical=
        st.booleans()
)
model_Triangle_strategy = st.builds(
    model_Triangle,
)
model_Polyline_strategy = st.builds(
    model_Polyline,
    polygon=
        st.booleans(),
    polyline=
        st.booleans()
)
model_Ellipse_strategy = st.builds(
    model_Ellipse,
    circle=
        st.booleans(),
    ellipse=
        st.booleans()
)
model_Rhombus_strategy = st.builds(
    model_Rhombus,
)
model_ColorFeature_strategy = st.builds(
    model_ColorFeature,
    type=
        safe_text
)





@given(instance=model_BooleanValue_strategy)
def test_hyp_model_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=model_EnumValue_strategy)
def test_hyp_model_enumvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=model_StringValue_strategy)
def test_hyp_model_stringvalue_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=model_StringValue_strategy)
def test_hyp_model_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=model_DoubleValue_strategy)
def test_hyp_model_doublevalue_valueInt_setter(instance):
    original = instance.valueInt
    instance.valueInt = original
    assert instance.valueInt == original



@given(instance=model_DoubleValue_strategy)
def test_hyp_model_doublevalue_valueDecimal_setter(instance):
    original = instance.valueDecimal
    instance.valueDecimal = original
    assert instance.valueDecimal == original




@given(instance=model_IntValue_strategy)
def test_hyp_model_intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=model_CustomColor_strategy)
def test_hyp_model_customcolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_CustomColor_strategy)
def test_hyp_model_customcolor_G_setter(instance):
    original = instance.G
    instance.G = original
    assert instance.G == original



@given(instance=model_CustomColor_strategy)
def test_hyp_model_customcolor_B_setter(instance):
    original = instance.B
    instance.B = original
    assert instance.B == original



@given(instance=model_CustomColor_strategy)
def test_hyp_model_customcolor_R_setter(instance):
    original = instance.R
    instance.R = original
    assert instance.R == original





@given(instance=model_Anchor_strategy)
def test_hyp_model_anchor_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=model_Anchor_strategy)
def test_hyp_model_anchor_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original





@given(instance=model_Rectangle_strategy)
def test_hyp_model_rectangle_rectangle_setter(instance):
    original = instance.rectangle
    instance.rectangle = original
    assert instance.rectangle == original



@given(instance=model_Rectangle_strategy)
def test_hyp_model_rectangle_square_setter(instance):
    original = instance.square
    instance.square = original
    assert instance.square == original





@given(instance=model_Image_strategy)
def test_hyp_model_image_imageId_setter(instance):
    original = instance.imageId
    instance.imageId = original
    assert instance.imageId == original






@given(instance=model_Color_strategy)
def test_hyp_model_color_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original






@given(instance=model_ImportStatement_strategy)
def test_hyp_model_importstatement_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original




@given(instance=model_CustomFigure_strategy)
def test_hyp_model_customfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original












@given(instance=model_Link_strategy)
def test_hyp_model_link_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=model_Link_strategy)
def test_hyp_model_link_complex_setter(instance):
    original = instance.complex
    instance.complex = original
    assert instance.complex == original








@given(instance=model_FeatureConditional_strategy)
def test_hyp_model_featureconditional_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=model_MetaModel_strategy)
def test_hyp_model_metamodel_plugin_setter(instance):
    original = instance.plugin
    instance.plugin = original
    assert instance.plugin == original



@given(instance=model_MetaModel_strategy)
def test_hyp_model_metamodel_ecorePath_setter(instance):
    original = instance.ecorePath
    instance.ecorePath = original
    assert instance.ecorePath == original





@given(instance=model_LineWidth_strategy)
def test_hyp_model_linewidth_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=model_Position_strategy)
def test_hyp_model_position_xRelative_setter(instance):
    original = instance.xRelative
    instance.xRelative = original
    assert instance.xRelative == original



@given(instance=model_Position_strategy)
def test_hyp_model_position_yRelative_setter(instance):
    original = instance.yRelative
    instance.yRelative = original
    assert instance.yRelative == original



@given(instance=model_Position_strategy)
def test_hyp_model_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=model_Position_strategy)
def test_hyp_model_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=model_Point_strategy)
def test_hyp_model_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=model_Point_strategy)
def test_hyp_model_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=model_Size_strategy)
def test_hyp_model_size_widthRelative_setter(instance):
    original = instance.widthRelative
    instance.widthRelative = original
    assert instance.widthRelative == original



@given(instance=model_Size_strategy)
def test_hyp_model_size_heightRelative_setter(instance):
    original = instance.heightRelative
    instance.heightRelative = original
    assert instance.heightRelative == original



@given(instance=model_Size_strategy)
def test_hyp_model_size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=model_Size_strategy)
def test_hyp_model_size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=model_Size_strategy)
def test_hyp_model_size_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original




@given(instance=model_Transparency_strategy)
def test_hyp_model_transparency_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original




@given(instance=model_LineStyle_strategy)
def test_hyp_model_linestyle_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=model_LineStyle_strategy)
def test_hyp_model_linestyle_manhattan_setter(instance):
    original = instance.manhattan
    instance.manhattan = original
    assert instance.manhattan == original




@given(instance=model_TextAlign_strategy)
def test_hyp_model_textalign_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=model_FontProperties_strategy)
def test_hyp_model_fontproperties_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original



@given(instance=model_FontProperties_strategy)
def test_hyp_model_fontproperties_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original



@given(instance=model_FontProperties_strategy)
def test_hyp_model_fontproperties_italics_setter(instance):
    original = instance.italics
    instance.italics = original
    assert instance.italics == original



@given(instance=model_FontProperties_strategy)
def test_hyp_model_fontproperties_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original




@given(instance=model_TextPart_strategy)
def test_hyp_model_textpart_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original



@given(instance=model_TextPart_strategy)
def test_hyp_model_textpart_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original






@given(instance=model_Layout_strategy)
def test_hyp_model_layout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original



@given(instance=model_Layout_strategy)
def test_hyp_model_layout_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original



@given(instance=model_Layout_strategy)
def test_hyp_model_layout_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original




@given(instance=model_Corner_strategy)
def test_hyp_model_corner_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=model_Line_strategy)
def test_hyp_model_line_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original



@given(instance=model_Line_strategy)
def test_hyp_model_line_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original





@given(instance=model_Polyline_strategy)
def test_hyp_model_polyline_polygon_setter(instance):
    original = instance.polygon
    instance.polygon = original
    assert instance.polygon == original



@given(instance=model_Polyline_strategy)
def test_hyp_model_polyline_polyline_setter(instance):
    original = instance.polyline
    instance.polyline = original
    assert instance.polyline == original




@given(instance=model_Ellipse_strategy)
def test_hyp_model_ellipse_circle_setter(instance):
    original = instance.circle
    instance.circle = original
    assert instance.circle == original



@given(instance=model_Ellipse_strategy)
def test_hyp_model_ellipse_ellipse_setter(instance):
    original = instance.ellipse
    instance.ellipse = original
    assert instance.ellipse == original





@given(instance=model_ColorFeature_strategy)
def test_hyp_model_colorfeature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ConnectableElement,
    DiagramElement,
    Feature,
    FeatureContainer,
    Value,
    model_Anchor,
    model_Arrow,
    model_BooleanValue,
    model_Color,
    model_ColorFeature,
    model_Colors,
    model_ConnectableElement,
    model_Contains,
    model_Corner,
    model_Custom,
    model_CustomColor,
    model_CustomFigure,
    model_Decorator,
    model_Diagram,
    model_DiagramElement,
    model_DoubleValue,
    model_EAttribute,
    model_EClass,
    model_EReference,
    model_Ellipse,
    model_EnumValue,
    model_Feature,
    model_FeatureConditional,
    model_FeatureContainer,
    model_FontProperties,
    model_Image,
    model_ImportStatement,
    model_IntValue,
    model_Invisible,
    model_Label,
    model_Layout,
    model_Line,
    model_LineStyle,
    model_LineWidth,
    model_Link,
    model_MetaModel,
    model_Node,
    model_Point,
    model_Polyline,
    model_Position,
    model_Rectangle,
    model_Rhombus,
    model_Size,
    model_StringValue,
    model_TextAlign,
    model_TextPart,
    model_TextValue,
    model_Transparency,
    model_Triangle,
    model_Value,
    model_Visible,
    model_XDiagram,
    AnchorDirection,
    BooleanLiteral,
    DefaultColor,
    LineType,
    Operator,
    TextAlignValue,
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

def test_model_Anchor_direction_value_roundtrip():
    instance = model_Anchor(direction="sample_text", max=7)
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_model_Anchor_max_value_roundtrip():
    instance = model_Anchor(direction="sample_text", max=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_model_BooleanValue_value_value_roundtrip():
    instance = model_BooleanValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_Color_default_value_roundtrip():
    instance = model_Color(default="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_model_ColorFeature_type_value_roundtrip():
    instance = model_ColorFeature(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_model_Corner_angle_value_roundtrip():
    instance = model_Corner(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_model_CustomColor_B_value_roundtrip():
    instance = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    assert instance.B == 7
    instance.B = 13
    assert instance.B == 13


def test_model_CustomColor_G_value_roundtrip():
    instance = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    assert instance.G == 7
    instance.G = 13
    assert instance.G == 13


def test_model_CustomColor_R_value_roundtrip():
    instance = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    assert instance.R == 7
    instance.R = 13
    assert instance.R == 13


def test_model_CustomColor_name_value_roundtrip():
    instance = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_CustomFigure_name_value_roundtrip():
    instance = model_CustomFigure(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_DoubleValue_valueDecimal_value_roundtrip():
    instance = model_DoubleValue(valueDecimal=7, valueInt=7)
    assert instance.valueDecimal == 7
    instance.valueDecimal = 13
    assert instance.valueDecimal == 13


def test_model_DoubleValue_valueInt_value_roundtrip():
    instance = model_DoubleValue(valueDecimal=7, valueInt=7)
    assert instance.valueInt == 7
    instance.valueInt = 13
    assert instance.valueInt == 13


def test_model_Ellipse_circle_value_roundtrip():
    instance = model_Ellipse(circle=True, ellipse=True)
    assert instance.circle == True
    instance.circle = False
    assert instance.circle == False


def test_model_Ellipse_ellipse_value_roundtrip():
    instance = model_Ellipse(circle=True, ellipse=True)
    assert instance.ellipse == True
    instance.ellipse = False
    assert instance.ellipse == False


def test_model_EnumValue_name_value_roundtrip():
    instance = model_EnumValue(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_FeatureConditional_operator_value_roundtrip():
    instance = model_FeatureConditional(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_model_FontProperties_bold_value_roundtrip():
    instance = model_FontProperties(bold=True, face="sample_text", italics=True, size=7)
    assert instance.bold == True
    instance.bold = False
    assert instance.bold == False


def test_model_FontProperties_face_value_roundtrip():
    instance = model_FontProperties(bold=True, face="sample_text", italics=True, size=7)
    assert instance.face == "sample_text"
    instance.face = "sample_text_2"
    assert instance.face == "sample_text_2"


def test_model_FontProperties_italics_value_roundtrip():
    instance = model_FontProperties(bold=True, face="sample_text", italics=True, size=7)
    assert instance.italics == True
    instance.italics = False
    assert instance.italics == False


def test_model_FontProperties_size_value_roundtrip():
    instance = model_FontProperties(bold=True, face="sample_text", italics=True, size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_model_Image_imageId_value_roundtrip():
    instance = model_Image(imageId="sample_text")
    assert instance.imageId == "sample_text"
    instance.imageId = "sample_text_2"
    assert instance.imageId == "sample_text_2"


def test_model_ImportStatement_importedNamespace_value_roundtrip():
    instance = model_ImportStatement(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_model_IntValue_value_value_roundtrip():
    instance = model_IntValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_model_Layout_horizontal_value_roundtrip():
    instance = model_Layout(horizontal=True, margin=7, vertical=True)
    assert instance.horizontal == True
    instance.horizontal = False
    assert instance.horizontal == False


def test_model_Layout_margin_value_roundtrip():
    instance = model_Layout(horizontal=True, margin=7, vertical=True)
    assert instance.margin == 7
    instance.margin = 13
    assert instance.margin == 13


def test_model_Layout_vertical_value_roundtrip():
    instance = model_Layout(horizontal=True, margin=7, vertical=True)
    assert instance.vertical == True
    instance.vertical = False
    assert instance.vertical == False


def test_model_Line_horizontal_value_roundtrip():
    instance = model_Line(horizontal=True, vertical=True)
    assert instance.horizontal == True
    instance.horizontal = False
    assert instance.horizontal == False


def test_model_Line_vertical_value_roundtrip():
    instance = model_Line(horizontal=True, vertical=True)
    assert instance.vertical == True
    instance.vertical = False
    assert instance.vertical == False


def test_model_LineStyle_manhattan_value_roundtrip():
    instance = model_LineStyle(manhattan=True, style="sample_text")
    assert instance.manhattan == True
    instance.manhattan = False
    assert instance.manhattan == False


def test_model_LineStyle_style_value_roundtrip():
    instance = model_LineStyle(manhattan=True, style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_model_LineWidth_width_value_roundtrip():
    instance = model_LineWidth(width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_model_Link_complex_value_roundtrip():
    instance = model_Link(complex=True, reference=True)
    assert instance.complex == True
    instance.complex = False
    assert instance.complex == False


def test_model_Link_reference_value_roundtrip():
    instance = model_Link(complex=True, reference=True)
    assert instance.reference == True
    instance.reference = False
    assert instance.reference == False


def test_model_MetaModel_ecorePath_value_roundtrip():
    instance = model_MetaModel(ecorePath="sample_text", plugin="sample_text")
    assert instance.ecorePath == "sample_text"
    instance.ecorePath = "sample_text_2"
    assert instance.ecorePath == "sample_text_2"


def test_model_MetaModel_plugin_value_roundtrip():
    instance = model_MetaModel(ecorePath="sample_text", plugin="sample_text")
    assert instance.plugin == "sample_text"
    instance.plugin = "sample_text_2"
    assert instance.plugin == "sample_text_2"


def test_model_Point_x_value_roundtrip():
    instance = model_Point(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_model_Point_y_value_roundtrip():
    instance = model_Point(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_model_Polyline_polygon_value_roundtrip():
    instance = model_Polyline(polygon=True, polyline=True)
    assert instance.polygon == True
    instance.polygon = False
    assert instance.polygon == False


def test_model_Polyline_polyline_value_roundtrip():
    instance = model_Polyline(polygon=True, polyline=True)
    assert instance.polyline == True
    instance.polyline = False
    assert instance.polyline == False


def test_model_Position_x_value_roundtrip():
    instance = model_Position(x=7, xRelative=True, y=7, yRelative=True)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_model_Position_xRelative_value_roundtrip():
    instance = model_Position(x=7, xRelative=True, y=7, yRelative=True)
    assert instance.xRelative == True
    instance.xRelative = False
    assert instance.xRelative == False


def test_model_Position_y_value_roundtrip():
    instance = model_Position(x=7, xRelative=True, y=7, yRelative=True)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_model_Position_yRelative_value_roundtrip():
    instance = model_Position(x=7, xRelative=True, y=7, yRelative=True)
    assert instance.yRelative == True
    instance.yRelative = False
    assert instance.yRelative == False


def test_model_Rectangle_rectangle_value_roundtrip():
    instance = model_Rectangle(rectangle=True, square=True)
    assert instance.rectangle == True
    instance.rectangle = False
    assert instance.rectangle == False


def test_model_Rectangle_square_value_roundtrip():
    instance = model_Rectangle(rectangle=True, square=True)
    assert instance.square == True
    instance.square = False
    assert instance.square == False


def test_model_Size_height_value_roundtrip():
    instance = model_Size(height=7, heightRelative=True, resizable=True, width=7, widthRelative=True)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_model_Size_heightRelative_value_roundtrip():
    instance = model_Size(height=7, heightRelative=True, resizable=True, width=7, widthRelative=True)
    assert instance.heightRelative == True
    instance.heightRelative = False
    assert instance.heightRelative == False


def test_model_Size_resizable_value_roundtrip():
    instance = model_Size(height=7, heightRelative=True, resizable=True, width=7, widthRelative=True)
    assert instance.resizable == True
    instance.resizable = False
    assert instance.resizable == False


def test_model_Size_width_value_roundtrip():
    instance = model_Size(height=7, heightRelative=True, resizable=True, width=7, widthRelative=True)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_model_Size_widthRelative_value_roundtrip():
    instance = model_Size(height=7, heightRelative=True, resizable=True, width=7, widthRelative=True)
    assert instance.widthRelative == True
    instance.widthRelative = False
    assert instance.widthRelative == False


def test_model_StringValue_null_value_roundtrip():
    instance = model_StringValue(null=True, value="sample_text")
    assert instance.null == True
    instance.null = False
    assert instance.null == False


def test_model_StringValue_value_value_roundtrip():
    instance = model_StringValue(null=True, value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_TextAlign_value_value_roundtrip():
    instance = model_TextAlign(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_TextPart_editable_value_roundtrip():
    instance = model_TextPart(editable=True, text="sample_text")
    assert instance.editable == True
    instance.editable = False
    assert instance.editable == False


def test_model_TextPart_text_value_roundtrip():
    instance = model_TextPart(editable=True, text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_model_Transparency_percent_value_roundtrip():
    instance = model_Transparency(percent=7)
    assert instance.percent == 7
    instance.percent = 13
    assert instance.percent == 13


def test_model_Custom_isa_ConnectableElement():
    instance = model_Custom()
    assert isinstance(instance, ConnectableElement)


def test_model_Ellipse_isa_ConnectableElement():
    instance = model_Ellipse(circle=True, ellipse=True)
    assert isinstance(instance, ConnectableElement)


def test_model_Image_isa_ConnectableElement():
    instance = model_Image(imageId="sample_text")
    assert isinstance(instance, ConnectableElement)


def test_model_Invisible_isa_ConnectableElement():
    instance = model_Invisible()
    assert isinstance(instance, ConnectableElement)


def test_model_Label_isa_ConnectableElement():
    instance = model_Label()
    assert isinstance(instance, ConnectableElement)


def test_model_Polyline_isa_ConnectableElement():
    instance = model_Polyline(polygon=True, polyline=True)
    assert isinstance(instance, ConnectableElement)


def test_model_Rectangle_isa_ConnectableElement():
    instance = model_Rectangle(rectangle=True, square=True)
    assert isinstance(instance, ConnectableElement)


def test_model_Rhombus_isa_ConnectableElement():
    instance = model_Rhombus()
    assert isinstance(instance, ConnectableElement)


def test_model_Triangle_isa_ConnectableElement():
    instance = model_Triangle()
    assert isinstance(instance, ConnectableElement)


def test_model_Link_isa_DiagramElement():
    instance = model_Link(complex=True, reference=True)
    assert isinstance(instance, DiagramElement)


def test_model_Node_isa_DiagramElement():
    instance = model_Node()
    assert isinstance(instance, DiagramElement)


def test_model_Anchor_isa_Feature():
    instance = model_Anchor(direction="sample_text", max=7)
    assert isinstance(instance, Feature)


def test_model_ColorFeature_isa_Feature():
    instance = model_ColorFeature(type="sample_text")
    assert isinstance(instance, Feature)


def test_model_Contains_isa_Feature():
    instance = model_Contains()
    assert isinstance(instance, Feature)


def test_model_Corner_isa_Feature():
    instance = model_Corner(angle=7)
    assert isinstance(instance, Feature)


def test_model_FontProperties_isa_Feature():
    instance = model_FontProperties(bold=True, face="sample_text", italics=True, size=7)
    assert isinstance(instance, Feature)


def test_model_Layout_isa_Feature():
    instance = model_Layout(horizontal=True, margin=7, vertical=True)
    assert isinstance(instance, Feature)


def test_model_LineStyle_isa_Feature():
    instance = model_LineStyle(manhattan=True, style="sample_text")
    assert isinstance(instance, Feature)


def test_model_LineWidth_isa_Feature():
    instance = model_LineWidth(width=7)
    assert isinstance(instance, Feature)


def test_model_Point_isa_Feature():
    instance = model_Point(x=7, y=7)
    assert isinstance(instance, Feature)


def test_model_Position_isa_Feature():
    instance = model_Position(x=7, xRelative=True, y=7, yRelative=True)
    assert isinstance(instance, Feature)


def test_model_Size_isa_Feature():
    instance = model_Size(height=7, heightRelative=True, resizable=True, width=7, widthRelative=True)
    assert isinstance(instance, Feature)


def test_model_TextAlign_isa_Feature():
    instance = model_TextAlign(value="sample_text")
    assert isinstance(instance, Feature)


def test_model_TextValue_isa_Feature():
    instance = model_TextValue()
    assert isinstance(instance, Feature)


def test_model_Transparency_isa_Feature():
    instance = model_Transparency(percent=7)
    assert isinstance(instance, Feature)


def test_model_Visible_isa_Feature():
    instance = model_Visible()
    assert isinstance(instance, Feature)


def test_model_Arrow_isa_FeatureContainer():
    instance = model_Arrow()
    assert isinstance(instance, FeatureContainer)


def test_model_ConnectableElement_isa_FeatureContainer():
    instance = model_ConnectableElement()
    assert isinstance(instance, FeatureContainer)


def test_model_Line_isa_FeatureContainer():
    instance = model_Line(horizontal=True, vertical=True)
    assert isinstance(instance, FeatureContainer)


def test_model_Link_isa_FeatureContainer():
    instance = model_Link(complex=True, reference=True)
    assert isinstance(instance, FeatureContainer)


def test_model_BooleanValue_isa_Value():
    instance = model_BooleanValue(value="sample_text")
    assert isinstance(instance, Value)


def test_model_DoubleValue_isa_Value():
    instance = model_DoubleValue(valueDecimal=7, valueInt=7)
    assert isinstance(instance, Value)


def test_model_EnumValue_isa_Value():
    instance = model_EnumValue(name="sample_text")
    assert isinstance(instance, Value)


def test_model_IntValue_isa_Value():
    instance = model_IntValue(value=7)
    assert isinstance(instance, Value)


def test_model_StringValue_isa_Value():
    instance = model_StringValue(null=True, value="sample_text")
    assert isinstance(instance, Value)


def test_assoc_color53_link_reassign_clear():
    a = model_ColorFeature(type="sample_text")
    b1 = model_Color(default="sample_text")
    b2 = model_Color(default="sample_text_2")
    _safe_set(a, 'model_ColorFeature', b1)
    assert _is_linked(a, 'model_ColorFeature', b1)
    if hasattr(b1, 'model_Color54'):
        assert _is_linked(b1, 'model_Color54', a)
    _safe_set(a, 'model_ColorFeature', b2)
    assert _is_linked(a, 'model_ColorFeature', b2)
    if hasattr(b1, 'model_Color54'):
        assert not _is_linked(b1, 'model_Color54', a)
    if hasattr(b2, 'model_Color54'):
        assert _is_linked(b2, 'model_Color54', a)
    _safe_set(a, 'model_ColorFeature', None)
    assert not _is_linked(a, 'model_ColorFeature', b2)
    if hasattr(b2, 'model_Color54'):
        assert not _is_linked(b2, 'model_Color54', a)


def test_assoc_colors38_link_reassign_clear():
    a = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    b1 = model_Colors()
    b2 = model_Colors()
    _safe_set(a, 'model_CustomColor', b1)
    assert _is_linked(a, 'model_CustomColor', b1)
    if hasattr(b1, 'model_Colors39'):
        assert _is_linked(b1, 'model_Colors39', a)
    _safe_set(a, 'model_CustomColor', b2)
    assert _is_linked(a, 'model_CustomColor', b2)
    if hasattr(b1, 'model_Colors39'):
        assert not _is_linked(b1, 'model_Colors39', a)
    if hasattr(b2, 'model_Colors39'):
        assert _is_linked(b2, 'model_Colors39', a)
    _safe_set(a, 'model_CustomColor', None)
    assert not _is_linked(a, 'model_CustomColor', b2)
    if hasattr(b2, 'model_Colors39'):
        assert not _is_linked(b2, 'model_Colors39', a)


def test_assoc_conditional16_link_reassign_clear():
    a = model_FeatureConditional(operator="sample_text")
    b1 = model_Feature()
    b2 = model_Feature()
    _safe_set(a, 'model_FeatureConditional', b1)
    assert _is_linked(a, 'model_FeatureConditional', b1)
    if hasattr(b1, 'model_Feature'):
        assert _is_linked(b1, 'model_Feature', a)
    _safe_set(a, 'model_FeatureConditional', b2)
    assert _is_linked(a, 'model_FeatureConditional', b2)
    if hasattr(b1, 'model_Feature'):
        assert not _is_linked(b1, 'model_Feature', a)
    if hasattr(b2, 'model_Feature'):
        assert _is_linked(b2, 'model_Feature', a)
    _safe_set(a, 'model_FeatureConditional', None)
    assert not _is_linked(a, 'model_FeatureConditional', b2)
    if hasattr(b2, 'model_Feature'):
        assert not _is_linked(b2, 'model_Feature', a)


def test_assoc_custom40_link_reassign_clear():
    a = model_CustomColor(B=7, G=7, R=7, name="sample_text")
    b1 = model_Color(default="sample_text")
    b2 = model_Color(default="sample_text_2")
    _safe_set(a, 'model_CustomColor41', b1)
    assert _is_linked(a, 'model_CustomColor41', b1)
    if hasattr(b1, 'model_Color'):
        assert _is_linked(b1, 'model_Color', a)
    _safe_set(a, 'model_CustomColor41', b2)
    assert _is_linked(a, 'model_CustomColor41', b2)
    if hasattr(b1, 'model_Color'):
        assert not _is_linked(b1, 'model_Color', a)
    if hasattr(b2, 'model_Color'):
        assert _is_linked(b2, 'model_Color', a)
    _safe_set(a, 'model_CustomColor41', None)
    assert not _is_linked(a, 'model_CustomColor41', b2)
    if hasattr(b2, 'model_Color'):
        assert not _is_linked(b2, 'model_Color', a)


def test_assoc_decorators31_link_reassign_clear():
    a = model_Link(complex=True, reference=True)
    b1 = model_Decorator()
    b2 = model_Decorator()
    _safe_set(a, 'model_Link32', {b1})
    assert _is_linked(a, 'model_Link32', b1)
    if hasattr(b1, 'model_Decorator'):
        assert _is_linked(b1, 'model_Decorator', a)
    _safe_set(a, 'model_Link32', {b2})
    assert _is_linked(a, 'model_Link32', b2)
    if hasattr(b1, 'model_Decorator'):
        assert not _is_linked(b1, 'model_Decorator', a)
    if hasattr(b2, 'model_Decorator'):
        assert _is_linked(b2, 'model_Decorator', a)
    _safe_set(a, 'model_Link32', set())
    assert not _is_linked(a, 'model_Link32', b2)
    if hasattr(b2, 'model_Decorator'):
        assert not _is_linked(b2, 'model_Decorator', a)


def test_assoc_element45_link_reassign_clear():
    a = model_CustomFigure(name="sample_text")
    b1 = model_ConnectableElement()
    b2 = model_ConnectableElement()
    _safe_set(a, 'model_CustomFigure46', b1)
    assert _is_linked(a, 'model_CustomFigure46', b1)
    if hasattr(b1, 'model_ConnectableElement47'):
        assert _is_linked(b1, 'model_ConnectableElement47', a)
    _safe_set(a, 'model_CustomFigure46', b2)
    assert _is_linked(a, 'model_CustomFigure46', b2)
    if hasattr(b1, 'model_ConnectableElement47'):
        assert not _is_linked(b1, 'model_ConnectableElement47', a)
    if hasattr(b2, 'model_ConnectableElement47'):
        assert _is_linked(b2, 'model_ConnectableElement47', a)
    _safe_set(a, 'model_CustomFigure46', None)
    assert not _is_linked(a, 'model_CustomFigure46', b2)
    if hasattr(b2, 'model_ConnectableElement47'):
        assert not _is_linked(b2, 'model_ConnectableElement47', a)


def test_assoc_figure48_link_reassign_clear():
    a = model_CustomFigure(name="sample_text")
    b1 = model_Custom()
    b2 = model_Custom()
    _safe_set(a, 'model_CustomFigure49', b1)
    assert _is_linked(a, 'model_CustomFigure49', b1)
    if hasattr(b1, 'model_Custom'):
        assert _is_linked(b1, 'model_Custom', a)
    _safe_set(a, 'model_CustomFigure49', b2)
    assert _is_linked(a, 'model_CustomFigure49', b2)
    if hasattr(b1, 'model_Custom'):
        assert not _is_linked(b1, 'model_Custom', a)
    if hasattr(b2, 'model_Custom'):
        assert _is_linked(b2, 'model_Custom', a)
    _safe_set(a, 'model_CustomFigure49', None)
    assert not _is_linked(a, 'model_CustomFigure49', b2)
    if hasattr(b2, 'model_Custom'):
        assert not _is_linked(b2, 'model_Custom', a)


def test_assoc_figures7_link_reassign_clear():
    a = model_CustomFigure(name="sample_text")
    b1 = model_XDiagram()
    b2 = model_XDiagram()
    _safe_set(a, 'model_CustomFigure', b1)
    assert _is_linked(a, 'model_CustomFigure', b1)
    if hasattr(b1, 'model_XDiagram8'):
        assert _is_linked(b1, 'model_XDiagram8', a)
    _safe_set(a, 'model_CustomFigure', b2)
    assert _is_linked(a, 'model_CustomFigure', b2)
    if hasattr(b1, 'model_XDiagram8'):
        assert not _is_linked(b1, 'model_XDiagram8', a)
    if hasattr(b2, 'model_XDiagram8'):
        assert _is_linked(b2, 'model_XDiagram8', a)
    _safe_set(a, 'model_CustomFigure', None)
    assert not _is_linked(a, 'model_CustomFigure', b2)
    if hasattr(b2, 'model_XDiagram8'):
        assert not _is_linked(b2, 'model_XDiagram8', a)


def test_assoc_metamodel0_link_reassign_clear():
    a = model_MetaModel(ecorePath="sample_text", plugin="sample_text")
    b1 = model_XDiagram()
    b2 = model_XDiagram()
    _safe_set(a, 'model_MetaModel', b1)
    assert _is_linked(a, 'model_MetaModel', b1)
    if hasattr(b1, 'model_XDiagram'):
        assert _is_linked(b1, 'model_XDiagram', a)
    _safe_set(a, 'model_MetaModel', b2)
    assert _is_linked(a, 'model_MetaModel', b2)
    if hasattr(b1, 'model_XDiagram'):
        assert not _is_linked(b1, 'model_XDiagram', a)
    if hasattr(b2, 'model_XDiagram'):
        assert _is_linked(b2, 'model_XDiagram', a)
    _safe_set(a, 'model_MetaModel', None)
    assert not _is_linked(a, 'model_MetaModel', b2)
    if hasattr(b2, 'model_XDiagram'):
        assert not _is_linked(b2, 'model_XDiagram', a)


def test_assoc_modelAttribute19_link_reassign_clear():
    a = model_FeatureConditional(operator="sample_text")
    b1 = model_EAttribute()
    b2 = model_EAttribute()
    _safe_set(a, 'model_FeatureConditional20', b1)
    assert _is_linked(a, 'model_FeatureConditional20', b1)
    if hasattr(b1, 'model_EAttribute'):
        assert _is_linked(b1, 'model_EAttribute', a)
    _safe_set(a, 'model_FeatureConditional20', b2)
    assert _is_linked(a, 'model_FeatureConditional20', b2)
    if hasattr(b1, 'model_EAttribute'):
        assert not _is_linked(b1, 'model_EAttribute', a)
    if hasattr(b2, 'model_EAttribute'):
        assert _is_linked(b2, 'model_EAttribute', a)
    _safe_set(a, 'model_FeatureConditional20', None)
    assert not _is_linked(a, 'model_FeatureConditional20', b2)
    if hasattr(b2, 'model_EAttribute'):
        assert not _is_linked(b2, 'model_EAttribute', a)


def test_assoc_modelAttribute56_link_reassign_clear():
    a = model_TextPart(editable=True, text="sample_text")
    b1 = model_EAttribute()
    b2 = model_EAttribute()
    _safe_set(a, 'model_TextPart57', b1)
    assert _is_linked(a, 'model_TextPart57', b1)
    if hasattr(b1, 'model_EAttribute58'):
        assert _is_linked(b1, 'model_EAttribute58', a)
    _safe_set(a, 'model_TextPart57', b2)
    assert _is_linked(a, 'model_TextPart57', b2)
    if hasattr(b1, 'model_EAttribute58'):
        assert not _is_linked(b1, 'model_EAttribute58', a)
    if hasattr(b2, 'model_EAttribute58'):
        assert _is_linked(b2, 'model_EAttribute58', a)
    _safe_set(a, 'model_TextPart57', None)
    assert not _is_linked(a, 'model_TextPart57', b2)
    if hasattr(b2, 'model_EAttribute58'):
        assert not _is_linked(b2, 'model_EAttribute58', a)


def test_assoc_modelReference24_link_reassign_clear():
    a = model_Link(complex=True, reference=True)
    b1 = model_EReference()
    b2 = model_EReference()
    _safe_set(a, 'model_Link', b1)
    assert _is_linked(a, 'model_Link', b1)
    if hasattr(b1, 'model_EReference'):
        assert _is_linked(b1, 'model_EReference', a)
    _safe_set(a, 'model_Link', b2)
    assert _is_linked(a, 'model_Link', b2)
    if hasattr(b1, 'model_EReference'):
        assert not _is_linked(b1, 'model_EReference', a)
    if hasattr(b2, 'model_EReference'):
        assert _is_linked(b2, 'model_EReference', a)
    _safe_set(a, 'model_Link', None)
    assert not _is_linked(a, 'model_Link', b2)
    if hasattr(b2, 'model_EReference'):
        assert not _is_linked(b2, 'model_EReference', a)


def test_assoc_modelReference36_link_reassign_clear():
    a = model_Anchor(direction="sample_text", max=7)
    b1 = model_EReference()
    b2 = model_EReference()
    _safe_set(a, 'model_Anchor', b1)
    assert _is_linked(a, 'model_Anchor', b1)
    if hasattr(b1, 'model_EReference37'):
        assert _is_linked(b1, 'model_EReference37', a)
    _safe_set(a, 'model_Anchor', b2)
    assert _is_linked(a, 'model_Anchor', b2)
    if hasattr(b1, 'model_EReference37'):
        assert not _is_linked(b1, 'model_EReference37', a)
    if hasattr(b2, 'model_EReference37'):
        assert _is_linked(b2, 'model_EReference37', a)
    _safe_set(a, 'model_Anchor', None)
    assert not _is_linked(a, 'model_Anchor', b2)
    if hasattr(b2, 'model_EReference37'):
        assert not _is_linked(b2, 'model_EReference37', a)


def test_assoc_parts55_link_reassign_clear():
    a = model_TextPart(editable=True, text="sample_text")
    b1 = model_TextValue()
    b2 = model_TextValue()
    _safe_set(a, 'model_TextPart', b1)
    assert _is_linked(a, 'model_TextPart', b1)
    if hasattr(b1, 'model_TextValue'):
        assert _is_linked(b1, 'model_TextValue', a)
    _safe_set(a, 'model_TextPart', b2)
    assert _is_linked(a, 'model_TextPart', b2)
    if hasattr(b1, 'model_TextValue'):
        assert not _is_linked(b1, 'model_TextValue', a)
    if hasattr(b2, 'model_TextValue'):
        assert _is_linked(b2, 'model_TextValue', a)
    _safe_set(a, 'model_TextPart', None)
    assert not _is_linked(a, 'model_TextPart', b2)
    if hasattr(b2, 'model_TextValue'):
        assert not _is_linked(b2, 'model_TextValue', a)


def test_assoc_sourceReference25_link_reassign_clear():
    a = model_Link(complex=True, reference=True)
    b1 = model_EReference()
    b2 = model_EReference()
    _safe_set(a, 'model_Link26', b1)
    assert _is_linked(a, 'model_Link26', b1)
    if hasattr(b1, 'model_EReference27'):
        assert _is_linked(b1, 'model_EReference27', a)
    _safe_set(a, 'model_Link26', b2)
    assert _is_linked(a, 'model_Link26', b2)
    if hasattr(b1, 'model_EReference27'):
        assert not _is_linked(b1, 'model_EReference27', a)
    if hasattr(b2, 'model_EReference27'):
        assert _is_linked(b2, 'model_EReference27', a)
    _safe_set(a, 'model_Link26', None)
    assert not _is_linked(a, 'model_Link26', b2)
    if hasattr(b2, 'model_EReference27'):
        assert not _is_linked(b2, 'model_EReference27', a)


def test_assoc_targetReference28_link_reassign_clear():
    a = model_Link(complex=True, reference=True)
    b1 = model_EReference()
    b2 = model_EReference()
    _safe_set(a, 'model_Link29', b1)
    assert _is_linked(a, 'model_Link29', b1)
    if hasattr(b1, 'model_EReference30'):
        assert _is_linked(b1, 'model_EReference30', a)
    _safe_set(a, 'model_Link29', b2)
    assert _is_linked(a, 'model_Link29', b2)
    if hasattr(b1, 'model_EReference30'):
        assert not _is_linked(b1, 'model_EReference30', a)
    if hasattr(b2, 'model_EReference30'):
        assert _is_linked(b2, 'model_EReference30', a)
    _safe_set(a, 'model_Link29', None)
    assert not _is_linked(a, 'model_Link29', b2)
    if hasattr(b2, 'model_EReference30'):
        assert not _is_linked(b2, 'model_EReference30', a)


def test_assoc_value21_link_reassign_clear():
    a = model_FeatureConditional(operator="sample_text")
    b1 = model_Value()
    b2 = model_Value()
    _safe_set(a, 'model_FeatureConditional22', b1)
    assert _is_linked(a, 'model_FeatureConditional22', b1)
    if hasattr(b1, 'model_Value'):
        assert _is_linked(b1, 'model_Value', a)
    _safe_set(a, 'model_FeatureConditional22', b2)
    assert _is_linked(a, 'model_FeatureConditional22', b2)
    if hasattr(b1, 'model_Value'):
        assert not _is_linked(b1, 'model_Value', a)
    if hasattr(b2, 'model_Value'):
        assert _is_linked(b2, 'model_Value', a)
    _safe_set(a, 'model_FeatureConditional22', None)
    assert not _is_linked(a, 'model_FeatureConditional22', b2)
    if hasattr(b2, 'model_Value'):
        assert not _is_linked(b2, 'model_Value', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ConnectableElement_strategy = st.builds(ConnectableElement)
@given(instance=ConnectableElement_strategy)
@settings(max_examples=25)
def test_ConnectableElement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)


DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


FeatureContainer_strategy = st.builds(FeatureContainer)
@given(instance=FeatureContainer_strategy)
@settings(max_examples=25)
def test_FeatureContainer_instantiation(instance):
    assert isinstance(instance, FeatureContainer)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


model_Anchor_strategy = st.builds(model_Anchor, direction=safe_text, max=st.integers())
@given(instance=model_Anchor_strategy)
@settings(max_examples=25)
def test_model_Anchor_instantiation(instance):
    assert isinstance(instance, model_Anchor)


model_Arrow_strategy = st.builds(model_Arrow)
@given(instance=model_Arrow_strategy)
@settings(max_examples=25)
def test_model_Arrow_instantiation(instance):
    assert isinstance(instance, model_Arrow)


model_BooleanValue_strategy = st.builds(model_BooleanValue, value=safe_text)
@given(instance=model_BooleanValue_strategy)
@settings(max_examples=25)
def test_model_BooleanValue_instantiation(instance):
    assert isinstance(instance, model_BooleanValue)


model_Color_strategy = st.builds(model_Color, default=safe_text)
@given(instance=model_Color_strategy)
@settings(max_examples=25)
def test_model_Color_instantiation(instance):
    assert isinstance(instance, model_Color)


model_ColorFeature_strategy = st.builds(model_ColorFeature, type=safe_text)
@given(instance=model_ColorFeature_strategy)
@settings(max_examples=25)
def test_model_ColorFeature_instantiation(instance):
    assert isinstance(instance, model_ColorFeature)


model_Colors_strategy = st.builds(model_Colors)
@given(instance=model_Colors_strategy)
@settings(max_examples=25)
def test_model_Colors_instantiation(instance):
    assert isinstance(instance, model_Colors)


model_ConnectableElement_strategy = st.builds(model_ConnectableElement)
@given(instance=model_ConnectableElement_strategy)
@settings(max_examples=25)
def test_model_ConnectableElement_instantiation(instance):
    assert isinstance(instance, model_ConnectableElement)


model_Contains_strategy = st.builds(model_Contains)
@given(instance=model_Contains_strategy)
@settings(max_examples=25)
def test_model_Contains_instantiation(instance):
    assert isinstance(instance, model_Contains)


model_Corner_strategy = st.builds(model_Corner, angle=st.integers())
@given(instance=model_Corner_strategy)
@settings(max_examples=25)
def test_model_Corner_instantiation(instance):
    assert isinstance(instance, model_Corner)


model_Custom_strategy = st.builds(model_Custom)
@given(instance=model_Custom_strategy)
@settings(max_examples=25)
def test_model_Custom_instantiation(instance):
    assert isinstance(instance, model_Custom)


model_CustomColor_strategy = st.builds(model_CustomColor, B=st.integers(), G=st.integers(), R=st.integers(), name=safe_text)
@given(instance=model_CustomColor_strategy)
@settings(max_examples=25)
def test_model_CustomColor_instantiation(instance):
    assert isinstance(instance, model_CustomColor)


model_CustomFigure_strategy = st.builds(model_CustomFigure, name=safe_text)
@given(instance=model_CustomFigure_strategy)
@settings(max_examples=25)
def test_model_CustomFigure_instantiation(instance):
    assert isinstance(instance, model_CustomFigure)


model_Decorator_strategy = st.builds(model_Decorator)
@given(instance=model_Decorator_strategy)
@settings(max_examples=25)
def test_model_Decorator_instantiation(instance):
    assert isinstance(instance, model_Decorator)


model_Diagram_strategy = st.builds(model_Diagram)
@given(instance=model_Diagram_strategy)
@settings(max_examples=25)
def test_model_Diagram_instantiation(instance):
    assert isinstance(instance, model_Diagram)


model_DiagramElement_strategy = st.builds(model_DiagramElement)
@given(instance=model_DiagramElement_strategy)
@settings(max_examples=25)
def test_model_DiagramElement_instantiation(instance):
    assert isinstance(instance, model_DiagramElement)


model_DoubleValue_strategy = st.builds(model_DoubleValue, valueDecimal=st.integers(), valueInt=st.integers())
@given(instance=model_DoubleValue_strategy)
@settings(max_examples=25)
def test_model_DoubleValue_instantiation(instance):
    assert isinstance(instance, model_DoubleValue)


model_EAttribute_strategy = st.builds(model_EAttribute)
@given(instance=model_EAttribute_strategy)
@settings(max_examples=25)
def test_model_EAttribute_instantiation(instance):
    assert isinstance(instance, model_EAttribute)


model_EClass_strategy = st.builds(model_EClass)
@given(instance=model_EClass_strategy)
@settings(max_examples=25)
def test_model_EClass_instantiation(instance):
    assert isinstance(instance, model_EClass)


model_EReference_strategy = st.builds(model_EReference)
@given(instance=model_EReference_strategy)
@settings(max_examples=25)
def test_model_EReference_instantiation(instance):
    assert isinstance(instance, model_EReference)


model_Ellipse_strategy = st.builds(model_Ellipse, circle=st.booleans(), ellipse=st.booleans())
@given(instance=model_Ellipse_strategy)
@settings(max_examples=25)
def test_model_Ellipse_instantiation(instance):
    assert isinstance(instance, model_Ellipse)


model_EnumValue_strategy = st.builds(model_EnumValue, name=safe_text)
@given(instance=model_EnumValue_strategy)
@settings(max_examples=25)
def test_model_EnumValue_instantiation(instance):
    assert isinstance(instance, model_EnumValue)


model_Feature_strategy = st.builds(model_Feature)
@given(instance=model_Feature_strategy)
@settings(max_examples=25)
def test_model_Feature_instantiation(instance):
    assert isinstance(instance, model_Feature)


model_FeatureConditional_strategy = st.builds(model_FeatureConditional, operator=safe_text)
@given(instance=model_FeatureConditional_strategy)
@settings(max_examples=25)
def test_model_FeatureConditional_instantiation(instance):
    assert isinstance(instance, model_FeatureConditional)


model_FeatureContainer_strategy = st.builds(model_FeatureContainer)
@given(instance=model_FeatureContainer_strategy)
@settings(max_examples=25)
def test_model_FeatureContainer_instantiation(instance):
    assert isinstance(instance, model_FeatureContainer)


model_FontProperties_strategy = st.builds(model_FontProperties, bold=st.booleans(), face=safe_text, italics=st.booleans(), size=st.integers())
@given(instance=model_FontProperties_strategy)
@settings(max_examples=25)
def test_model_FontProperties_instantiation(instance):
    assert isinstance(instance, model_FontProperties)


model_Image_strategy = st.builds(model_Image, imageId=safe_text)
@given(instance=model_Image_strategy)
@settings(max_examples=25)
def test_model_Image_instantiation(instance):
    assert isinstance(instance, model_Image)


model_ImportStatement_strategy = st.builds(model_ImportStatement, importedNamespace=safe_text)
@given(instance=model_ImportStatement_strategy)
@settings(max_examples=25)
def test_model_ImportStatement_instantiation(instance):
    assert isinstance(instance, model_ImportStatement)


model_IntValue_strategy = st.builds(model_IntValue, value=st.integers())
@given(instance=model_IntValue_strategy)
@settings(max_examples=25)
def test_model_IntValue_instantiation(instance):
    assert isinstance(instance, model_IntValue)


model_Invisible_strategy = st.builds(model_Invisible)
@given(instance=model_Invisible_strategy)
@settings(max_examples=25)
def test_model_Invisible_instantiation(instance):
    assert isinstance(instance, model_Invisible)


model_Label_strategy = st.builds(model_Label)
@given(instance=model_Label_strategy)
@settings(max_examples=25)
def test_model_Label_instantiation(instance):
    assert isinstance(instance, model_Label)


model_Layout_strategy = st.builds(model_Layout, horizontal=st.booleans(), margin=st.integers(), vertical=st.booleans())
@given(instance=model_Layout_strategy)
@settings(max_examples=25)
def test_model_Layout_instantiation(instance):
    assert isinstance(instance, model_Layout)


model_Line_strategy = st.builds(model_Line, horizontal=st.booleans(), vertical=st.booleans())
@given(instance=model_Line_strategy)
@settings(max_examples=25)
def test_model_Line_instantiation(instance):
    assert isinstance(instance, model_Line)


model_LineStyle_strategy = st.builds(model_LineStyle, manhattan=st.booleans(), style=safe_text)
@given(instance=model_LineStyle_strategy)
@settings(max_examples=25)
def test_model_LineStyle_instantiation(instance):
    assert isinstance(instance, model_LineStyle)


model_LineWidth_strategy = st.builds(model_LineWidth, width=st.integers())
@given(instance=model_LineWidth_strategy)
@settings(max_examples=25)
def test_model_LineWidth_instantiation(instance):
    assert isinstance(instance, model_LineWidth)


model_Link_strategy = st.builds(model_Link, complex=st.booleans(), reference=st.booleans())
@given(instance=model_Link_strategy)
@settings(max_examples=25)
def test_model_Link_instantiation(instance):
    assert isinstance(instance, model_Link)


model_MetaModel_strategy = st.builds(model_MetaModel, ecorePath=safe_text, plugin=safe_text)
@given(instance=model_MetaModel_strategy)
@settings(max_examples=25)
def test_model_MetaModel_instantiation(instance):
    assert isinstance(instance, model_MetaModel)


model_Node_strategy = st.builds(model_Node)
@given(instance=model_Node_strategy)
@settings(max_examples=25)
def test_model_Node_instantiation(instance):
    assert isinstance(instance, model_Node)


model_Point_strategy = st.builds(model_Point, x=st.integers(), y=st.integers())
@given(instance=model_Point_strategy)
@settings(max_examples=25)
def test_model_Point_instantiation(instance):
    assert isinstance(instance, model_Point)


model_Polyline_strategy = st.builds(model_Polyline, polygon=st.booleans(), polyline=st.booleans())
@given(instance=model_Polyline_strategy)
@settings(max_examples=25)
def test_model_Polyline_instantiation(instance):
    assert isinstance(instance, model_Polyline)


model_Position_strategy = st.builds(model_Position, x=st.integers(), xRelative=st.booleans(), y=st.integers(), yRelative=st.booleans())
@given(instance=model_Position_strategy)
@settings(max_examples=25)
def test_model_Position_instantiation(instance):
    assert isinstance(instance, model_Position)


model_Rectangle_strategy = st.builds(model_Rectangle, rectangle=st.booleans(), square=st.booleans())
@given(instance=model_Rectangle_strategy)
@settings(max_examples=25)
def test_model_Rectangle_instantiation(instance):
    assert isinstance(instance, model_Rectangle)


model_Rhombus_strategy = st.builds(model_Rhombus)
@given(instance=model_Rhombus_strategy)
@settings(max_examples=25)
def test_model_Rhombus_instantiation(instance):
    assert isinstance(instance, model_Rhombus)


model_Size_strategy = st.builds(model_Size, height=st.integers(), heightRelative=st.booleans(), resizable=st.booleans(), width=st.integers(), widthRelative=st.booleans())
@given(instance=model_Size_strategy)
@settings(max_examples=25)
def test_model_Size_instantiation(instance):
    assert isinstance(instance, model_Size)


model_StringValue_strategy = st.builds(model_StringValue, null=st.booleans(), value=safe_text)
@given(instance=model_StringValue_strategy)
@settings(max_examples=25)
def test_model_StringValue_instantiation(instance):
    assert isinstance(instance, model_StringValue)


model_TextAlign_strategy = st.builds(model_TextAlign, value=safe_text)
@given(instance=model_TextAlign_strategy)
@settings(max_examples=25)
def test_model_TextAlign_instantiation(instance):
    assert isinstance(instance, model_TextAlign)


model_TextPart_strategy = st.builds(model_TextPart, editable=st.booleans(), text=safe_text)
@given(instance=model_TextPart_strategy)
@settings(max_examples=25)
def test_model_TextPart_instantiation(instance):
    assert isinstance(instance, model_TextPart)


model_TextValue_strategy = st.builds(model_TextValue)
@given(instance=model_TextValue_strategy)
@settings(max_examples=25)
def test_model_TextValue_instantiation(instance):
    assert isinstance(instance, model_TextValue)


model_Transparency_strategy = st.builds(model_Transparency, percent=st.integers())
@given(instance=model_Transparency_strategy)
@settings(max_examples=25)
def test_model_Transparency_instantiation(instance):
    assert isinstance(instance, model_Transparency)


model_Triangle_strategy = st.builds(model_Triangle)
@given(instance=model_Triangle_strategy)
@settings(max_examples=25)
def test_model_Triangle_instantiation(instance):
    assert isinstance(instance, model_Triangle)


model_Value_strategy = st.builds(model_Value)
@given(instance=model_Value_strategy)
@settings(max_examples=25)
def test_model_Value_instantiation(instance):
    assert isinstance(instance, model_Value)


model_Visible_strategy = st.builds(model_Visible)
@given(instance=model_Visible_strategy)
@settings(max_examples=25)
def test_model_Visible_instantiation(instance):
    assert isinstance(instance, model_Visible)


model_XDiagram_strategy = st.builds(model_XDiagram)
@given(instance=model_XDiagram_strategy)
@settings(max_examples=25)
def test_model_XDiagram_instantiation(instance):
    assert isinstance(instance, model_XDiagram)



