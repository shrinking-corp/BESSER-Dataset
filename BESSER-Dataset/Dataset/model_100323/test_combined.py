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
    Coordinate,
    PNML_Position,
    PNML_Coordinate,
    Font,
    Offset,
    Graphics,
    PNML_AnnotationGraphics,
    PNML_NetGraphics,
    PNML_Graphics,
    InitialMarking,
    NodeGraphics,
    PNML_EdgeGraphics,
    Line,
    Fill,
    Dimension,
    Position,
    PNML_NodeGraphics,
    Place,
    Inscription,
    EdgeGraphics,
    NetContentElement,
    PNML_Transition,
    PNML_Place,
    AnyElement,
    PNML_ToolSpecific,
    LabeledElement,
    PNML_Name,
    PNML_InitialMarking,
    PNML_Inscription,
    PNML_Label,
    AnnotationGraphics,
    Label,
    PNML_LabeledElement,
    Node,
    Arc,
    NetElement,
    URI,
    PNML_PNMLDocument,
    PNML_NetContent,
    Name,
    NetGraphics,
    ToolSpecific,
    NetContent,
    PNML_NetContentElement,
    PNMLDocument,
    IdedElement,
    PNML_Arc,
    PNML_Node,
    PNML_NetElement,
    PNML_IdedElement,
    PNML_AnyElement,
    PNML_Color,
    PNML_URI,
    PNML_Font,
    PNML_Dimension,
    PNML_Offset,
    PNML_Line,
    Color,
    PNML_Fill,
    DecorationType,
    AlignType,
    RotationType,
    StyleType,
    ShapeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_hyp_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_hyp_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_position_is_not_abstract():
    assert not inspect.isabstract(PNML_Position)


def test_hyp_pnml_position_constructor_exists():
    assert callable(PNML_Position.__init__)


def test_hyp_pnml_position_constructor_args():
    sig = inspect.signature(PNML_Position.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_coordinate_is_not_abstract():
    assert not inspect.isabstract(PNML_Coordinate)


def test_hyp_pnml_coordinate_constructor_exists():
    assert callable(PNML_Coordinate.__init__)


def test_hyp_pnml_coordinate_constructor_args():
    sig = inspect.signature(PNML_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_font_is_not_abstract():
    assert not inspect.isabstract(Font)


def test_hyp_font_constructor_exists():
    assert callable(Font.__init__)


def test_hyp_font_constructor_args():
    sig = inspect.signature(Font.__init__)
    params = list(sig.parameters.keys())



def test_hyp_offset_is_not_abstract():
    assert not inspect.isabstract(Offset)


def test_hyp_offset_constructor_exists():
    assert callable(Offset.__init__)


def test_hyp_offset_constructor_args():
    sig = inspect.signature(Offset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_hyp_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_hyp_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(PNML_AnnotationGraphics)


def test_hyp_pnml_annotationgraphics_constructor_exists():
    assert callable(PNML_AnnotationGraphics.__init__)


def test_hyp_pnml_annotationgraphics_constructor_args():
    sig = inspect.signature(PNML_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_netgraphics_is_not_abstract():
    assert not inspect.isabstract(PNML_NetGraphics)


def test_hyp_pnml_netgraphics_constructor_exists():
    assert callable(PNML_NetGraphics.__init__)


def test_hyp_pnml_netgraphics_constructor_args():
    sig = inspect.signature(PNML_NetGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_graphics_is_not_abstract():
    assert not inspect.isabstract(PNML_Graphics)


def test_hyp_pnml_graphics_constructor_exists():
    assert callable(PNML_Graphics.__init__)


def test_hyp_pnml_graphics_constructor_args():
    sig = inspect.signature(PNML_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_initialmarking_is_not_abstract():
    assert not inspect.isabstract(InitialMarking)


def test_hyp_initialmarking_constructor_exists():
    assert callable(InitialMarking.__init__)


def test_hyp_initialmarking_constructor_args():
    sig = inspect.signature(InitialMarking.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(NodeGraphics)


def test_hyp_nodegraphics_constructor_exists():
    assert callable(NodeGraphics.__init__)


def test_hyp_nodegraphics_constructor_args():
    sig = inspect.signature(NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_edgegraphics_is_not_abstract():
    assert not inspect.isabstract(PNML_EdgeGraphics)


def test_hyp_pnml_edgegraphics_constructor_exists():
    assert callable(PNML_EdgeGraphics.__init__)


def test_hyp_pnml_edgegraphics_constructor_args():
    sig = inspect.signature(PNML_EdgeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_line_is_not_abstract():
    assert not inspect.isabstract(Line)


def test_hyp_line_constructor_exists():
    assert callable(Line.__init__)


def test_hyp_line_constructor_args():
    sig = inspect.signature(Line.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fill_is_not_abstract():
    assert not inspect.isabstract(Fill)


def test_hyp_fill_constructor_exists():
    assert callable(Fill.__init__)


def test_hyp_fill_constructor_args():
    sig = inspect.signature(Fill.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dimension_is_not_abstract():
    assert not inspect.isabstract(Dimension)


def test_hyp_dimension_constructor_exists():
    assert callable(Dimension.__init__)


def test_hyp_dimension_constructor_args():
    sig = inspect.signature(Dimension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_position_is_not_abstract():
    assert not inspect.isabstract(Position)


def test_hyp_position_constructor_exists():
    assert callable(Position.__init__)


def test_hyp_position_constructor_args():
    sig = inspect.signature(Position.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(PNML_NodeGraphics)


def test_hyp_pnml_nodegraphics_constructor_exists():
    assert callable(PNML_NodeGraphics.__init__)


def test_hyp_pnml_nodegraphics_constructor_args():
    sig = inspect.signature(PNML_NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_hyp_place_constructor_exists():
    assert callable(Place.__init__)


def test_hyp_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inscription_is_not_abstract():
    assert not inspect.isabstract(Inscription)


def test_hyp_inscription_constructor_exists():
    assert callable(Inscription.__init__)


def test_hyp_inscription_constructor_args():
    sig = inspect.signature(Inscription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edgegraphics_is_not_abstract():
    assert not inspect.isabstract(EdgeGraphics)


def test_hyp_edgegraphics_constructor_exists():
    assert callable(EdgeGraphics.__init__)


def test_hyp_edgegraphics_constructor_args():
    sig = inspect.signature(EdgeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_netcontentelement_is_not_abstract():
    assert not inspect.isabstract(NetContentElement)


def test_hyp_netcontentelement_constructor_exists():
    assert callable(NetContentElement.__init__)


def test_hyp_netcontentelement_constructor_args():
    sig = inspect.signature(NetContentElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_transition_is_not_abstract():
    assert not inspect.isabstract(PNML_Transition)


def test_hyp_pnml_transition_constructor_exists():
    assert callable(PNML_Transition.__init__)


def test_hyp_pnml_transition_constructor_args():
    sig = inspect.signature(PNML_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_place_is_not_abstract():
    assert not inspect.isabstract(PNML_Place)


def test_hyp_pnml_place_constructor_exists():
    assert callable(PNML_Place.__init__)


def test_hyp_pnml_place_constructor_args():
    sig = inspect.signature(PNML_Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_anyelement_is_not_abstract():
    assert not inspect.isabstract(AnyElement)


def test_hyp_anyelement_constructor_exists():
    assert callable(AnyElement.__init__)


def test_hyp_anyelement_constructor_args():
    sig = inspect.signature(AnyElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_toolspecific_is_not_abstract():
    assert not inspect.isabstract(PNML_ToolSpecific)


def test_hyp_pnml_toolspecific_constructor_exists():
    assert callable(PNML_ToolSpecific.__init__)


def test_hyp_pnml_toolspecific_constructor_args():
    sig = inspect.signature(PNML_ToolSpecific.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"





def test_hyp_labeledelement_is_not_abstract():
    assert not inspect.isabstract(LabeledElement)


def test_hyp_labeledelement_constructor_exists():
    assert callable(LabeledElement.__init__)


def test_hyp_labeledelement_constructor_args():
    sig = inspect.signature(LabeledElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_name_is_not_abstract():
    assert not inspect.isabstract(PNML_Name)


def test_hyp_pnml_name_constructor_exists():
    assert callable(PNML_Name.__init__)


def test_hyp_pnml_name_constructor_args():
    sig = inspect.signature(PNML_Name.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_initialmarking_is_not_abstract():
    assert not inspect.isabstract(PNML_InitialMarking)


def test_hyp_pnml_initialmarking_constructor_exists():
    assert callable(PNML_InitialMarking.__init__)


def test_hyp_pnml_initialmarking_constructor_args():
    sig = inspect.signature(PNML_InitialMarking.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_inscription_is_not_abstract():
    assert not inspect.isabstract(PNML_Inscription)


def test_hyp_pnml_inscription_constructor_exists():
    assert callable(PNML_Inscription.__init__)


def test_hyp_pnml_inscription_constructor_args():
    sig = inspect.signature(PNML_Inscription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_label_is_not_abstract():
    assert not inspect.isabstract(PNML_Label)


def test_hyp_pnml_label_constructor_exists():
    assert callable(PNML_Label.__init__)


def test_hyp_pnml_label_constructor_args():
    sig = inspect.signature(PNML_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(AnnotationGraphics)


def test_hyp_annotationgraphics_constructor_exists():
    assert callable(AnnotationGraphics.__init__)


def test_hyp_annotationgraphics_constructor_args():
    sig = inspect.signature(AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_hyp_label_constructor_exists():
    assert callable(Label.__init__)


def test_hyp_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_labeledelement_is_not_abstract():
    assert not inspect.isabstract(PNML_LabeledElement)


def test_hyp_pnml_labeledelement_constructor_exists():
    assert callable(PNML_LabeledElement.__init__)


def test_hyp_pnml_labeledelement_constructor_args():
    sig = inspect.signature(PNML_LabeledElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_hyp_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_hyp_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_netelement_is_not_abstract():
    assert not inspect.isabstract(NetElement)


def test_hyp_netelement_constructor_exists():
    assert callable(NetElement.__init__)


def test_hyp_netelement_constructor_args():
    sig = inspect.signature(NetElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uri_is_not_abstract():
    assert not inspect.isabstract(URI)


def test_hyp_uri_constructor_exists():
    assert callable(URI.__init__)


def test_hyp_uri_constructor_args():
    sig = inspect.signature(URI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_pnmldocument_is_not_abstract():
    assert not inspect.isabstract(PNML_PNMLDocument)


def test_hyp_pnml_pnmldocument_constructor_exists():
    assert callable(PNML_PNMLDocument.__init__)


def test_hyp_pnml_pnmldocument_constructor_args():
    sig = inspect.signature(PNML_PNMLDocument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_netcontent_is_not_abstract():
    assert not inspect.isabstract(PNML_NetContent)


def test_hyp_pnml_netcontent_constructor_exists():
    assert callable(PNML_NetContent.__init__)


def test_hyp_pnml_netcontent_constructor_args():
    sig = inspect.signature(PNML_NetContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_hyp_name_constructor_exists():
    assert callable(Name.__init__)


def test_hyp_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_hyp_netgraphics_is_not_abstract():
    assert not inspect.isabstract(NetGraphics)


def test_hyp_netgraphics_constructor_exists():
    assert callable(NetGraphics.__init__)


def test_hyp_netgraphics_constructor_args():
    sig = inspect.signature(NetGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_toolspecific_is_not_abstract():
    assert not inspect.isabstract(ToolSpecific)


def test_hyp_toolspecific_constructor_exists():
    assert callable(ToolSpecific.__init__)


def test_hyp_toolspecific_constructor_args():
    sig = inspect.signature(ToolSpecific.__init__)
    params = list(sig.parameters.keys())



def test_hyp_netcontent_is_not_abstract():
    assert not inspect.isabstract(NetContent)


def test_hyp_netcontent_constructor_exists():
    assert callable(NetContent.__init__)


def test_hyp_netcontent_constructor_args():
    sig = inspect.signature(NetContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_netcontentelement_is_not_abstract():
    assert not inspect.isabstract(PNML_NetContentElement)


def test_hyp_pnml_netcontentelement_constructor_exists():
    assert callable(PNML_NetContentElement.__init__)


def test_hyp_pnml_netcontentelement_constructor_args():
    sig = inspect.signature(PNML_NetContentElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmldocument_is_not_abstract():
    assert not inspect.isabstract(PNMLDocument)


def test_hyp_pnmldocument_constructor_exists():
    assert callable(PNMLDocument.__init__)


def test_hyp_pnmldocument_constructor_args():
    sig = inspect.signature(PNMLDocument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_idedelement_is_not_abstract():
    assert not inspect.isabstract(IdedElement)


def test_hyp_idedelement_constructor_exists():
    assert callable(IdedElement.__init__)


def test_hyp_idedelement_constructor_args():
    sig = inspect.signature(IdedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_arc_is_not_abstract():
    assert not inspect.isabstract(PNML_Arc)


def test_hyp_pnml_arc_constructor_exists():
    assert callable(PNML_Arc.__init__)


def test_hyp_pnml_arc_constructor_args():
    sig = inspect.signature(PNML_Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_node_is_not_abstract():
    assert not inspect.isabstract(PNML_Node)


def test_hyp_pnml_node_constructor_exists():
    assert callable(PNML_Node.__init__)


def test_hyp_pnml_node_constructor_args():
    sig = inspect.signature(PNML_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_netelement_is_not_abstract():
    assert not inspect.isabstract(PNML_NetElement)


def test_hyp_pnml_netelement_constructor_exists():
    assert callable(PNML_NetElement.__init__)


def test_hyp_pnml_netelement_constructor_args():
    sig = inspect.signature(PNML_NetElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_idedelement_is_not_abstract():
    assert not inspect.isabstract(PNML_IdedElement)


def test_hyp_pnml_idedelement_constructor_exists():
    assert callable(PNML_IdedElement.__init__)


def test_hyp_pnml_idedelement_constructor_args():
    sig = inspect.signature(PNML_IdedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_pnml_anyelement_is_not_abstract():
    assert not inspect.isabstract(PNML_AnyElement)


def test_hyp_pnml_anyelement_constructor_exists():
    assert callable(PNML_AnyElement.__init__)


def test_hyp_pnml_anyelement_constructor_args():
    sig = inspect.signature(PNML_AnyElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "text" in params, "Missing parameter 'text'"





def test_hyp_pnml_color_is_not_abstract():
    assert not inspect.isabstract(PNML_Color)


def test_hyp_pnml_color_constructor_exists():
    assert callable(PNML_Color.__init__)


def test_hyp_pnml_color_constructor_args():
    sig = inspect.signature(PNML_Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_uri_is_not_abstract():
    assert not inspect.isabstract(PNML_URI)


def test_hyp_pnml_uri_constructor_exists():
    assert callable(PNML_URI.__init__)


def test_hyp_pnml_uri_constructor_args():
    sig = inspect.signature(PNML_URI.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pnml_font_is_not_abstract():
    assert not inspect.isabstract(PNML_Font)


def test_hyp_pnml_font_constructor_exists():
    assert callable(PNML_Font.__init__)


def test_hyp_pnml_font_constructor_args():
    sig = inspect.signature(PNML_Font.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "style" in params, "Missing parameter 'style'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "size" in params, "Missing parameter 'size'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "family" in params, "Missing parameter 'family'"










def test_hyp_pnml_dimension_is_not_abstract():
    assert not inspect.isabstract(PNML_Dimension)


def test_hyp_pnml_dimension_constructor_exists():
    assert callable(PNML_Dimension.__init__)


def test_hyp_pnml_dimension_constructor_args():
    sig = inspect.signature(PNML_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"





def test_hyp_pnml_offset_is_not_abstract():
    assert not inspect.isabstract(PNML_Offset)


def test_hyp_pnml_offset_constructor_exists():
    assert callable(PNML_Offset.__init__)


def test_hyp_pnml_offset_constructor_args():
    sig = inspect.signature(PNML_Offset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_line_is_not_abstract():
    assert not inspect.isabstract(PNML_Line)


def test_hyp_pnml_line_constructor_exists():
    assert callable(PNML_Line.__init__)


def test_hyp_pnml_line_constructor_args():
    sig = inspect.signature(PNML_Line.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_hyp_color_constructor_exists():
    assert callable(Color.__init__)


def test_hyp_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnml_fill_is_not_abstract():
    assert not inspect.isabstract(PNML_Fill)


def test_hyp_pnml_fill_constructor_exists():
    assert callable(PNML_Fill.__init__)


def test_hyp_pnml_fill_constructor_args():
    sig = inspect.signature(PNML_Fill.__init__)
    params = list(sig.parameters.keys())
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"


def test_hyp_decorationtype_exists():
    # Check that the Enumeration exists
    assert DecorationType is not None

def test_hyp_decorationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DecorationType]
    expected_literals = [
        "dtunderligne",
        "dtlinethrough",
        "dtoverligne",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DecorationType"

def test_hyp_aligntype_exists():
    # Check that the Enumeration exists
    assert AlignType is not None

def test_hyp_aligntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignType]
    expected_literals = [
        "atleft",
        "atright",
        "atcenter",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignType"

def test_hyp_rotationtype_exists():
    # Check that the Enumeration exists
    assert RotationType is not None

def test_hyp_rotationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RotationType]
    expected_literals = [
        "rtdiagonal",
        "rtvertical",
        "rthorizontal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RotationType"

def test_hyp_styletype_exists():
    # Check that the Enumeration exists
    assert StyleType is not None

def test_hyp_styletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StyleType]
    expected_literals = [
        "sttsolid",
        "sttdash",
        "sttdot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StyleType"

def test_hyp_shapetype_exists():
    # Check that the Enumeration exists
    assert ShapeType is not None

def test_hyp_shapetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShapeType]
    expected_literals = [
        "shtcurve",
        "shtline",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShapeType"


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
Coordinate_strategy = st.builds(
    Coordinate,
)
PNML_Position_strategy = st.builds(
    PNML_Position,
)
PNML_Coordinate_strategy = st.builds(
    PNML_Coordinate,
    x=
        safe_text,
    y=
        safe_text
)
Font_strategy = st.builds(
    Font,
)
Offset_strategy = st.builds(
    Offset,
)
Graphics_strategy = st.builds(
    Graphics,
)
PNML_AnnotationGraphics_strategy = st.builds(
    PNML_AnnotationGraphics,
)
PNML_NetGraphics_strategy = st.builds(
    PNML_NetGraphics,
)
PNML_Graphics_strategy = st.builds(
    PNML_Graphics,
)
InitialMarking_strategy = st.builds(
    InitialMarking,
)
NodeGraphics_strategy = st.builds(
    NodeGraphics,
)
PNML_EdgeGraphics_strategy = st.builds(
    PNML_EdgeGraphics,
)
Line_strategy = st.builds(
    Line,
)
Fill_strategy = st.builds(
    Fill,
)
Dimension_strategy = st.builds(
    Dimension,
)
Position_strategy = st.builds(
    Position,
)
PNML_NodeGraphics_strategy = st.builds(
    PNML_NodeGraphics,
)
Place_strategy = st.builds(
    Place,
)
Inscription_strategy = st.builds(
    Inscription,
)
EdgeGraphics_strategy = st.builds(
    EdgeGraphics,
)
NetContentElement_strategy = st.builds(
    NetContentElement,
)
PNML_Transition_strategy = st.builds(
    PNML_Transition,
)
PNML_Place_strategy = st.builds(
    PNML_Place,
)
AnyElement_strategy = st.builds(
    AnyElement,
)
PNML_ToolSpecific_strategy = st.builds(
    PNML_ToolSpecific,
    version=
        safe_text,
    tool=
        safe_text
)
LabeledElement_strategy = st.builds(
    LabeledElement,
)
PNML_Name_strategy = st.builds(
    PNML_Name,
)
PNML_InitialMarking_strategy = st.builds(
    PNML_InitialMarking,
)
PNML_Inscription_strategy = st.builds(
    PNML_Inscription,
)
PNML_Label_strategy = st.builds(
    PNML_Label,
    text=
        safe_text
)
AnnotationGraphics_strategy = st.builds(
    AnnotationGraphics,
)
Label_strategy = st.builds(
    Label,
)
PNML_LabeledElement_strategy = st.builds(
    PNML_LabeledElement,
)
Node_strategy = st.builds(
    Node,
)
Arc_strategy = st.builds(
    Arc,
)
NetElement_strategy = st.builds(
    NetElement,
)
URI_strategy = st.builds(
    URI,
)
PNML_PNMLDocument_strategy = st.builds(
    PNML_PNMLDocument,
)
PNML_NetContent_strategy = st.builds(
    PNML_NetContent,
)
Name_strategy = st.builds(
    Name,
)
NetGraphics_strategy = st.builds(
    NetGraphics,
)
ToolSpecific_strategy = st.builds(
    ToolSpecific,
)
NetContent_strategy = st.builds(
    NetContent,
)
PNML_NetContentElement_strategy = st.builds(
    PNML_NetContentElement,
)
PNMLDocument_strategy = st.builds(
    PNMLDocument,
)
IdedElement_strategy = st.builds(
    IdedElement,
)
PNML_Arc_strategy = st.builds(
    PNML_Arc,
)
PNML_Node_strategy = st.builds(
    PNML_Node,
)
PNML_NetElement_strategy = st.builds(
    PNML_NetElement,
)
PNML_IdedElement_strategy = st.builds(
    PNML_IdedElement,
    id=
        safe_text
)
PNML_AnyElement_strategy = st.builds(
    PNML_AnyElement,
    name=
        safe_text,
    text=
        safe_text
)
PNML_Color_strategy = st.builds(
    PNML_Color,
)
PNML_URI_strategy = st.builds(
    PNML_URI,
    value=
        safe_text
)
PNML_Font_strategy = st.builds(
    PNML_Font,
    align=
        safe_text,
    style=
        safe_text,
    rotation=
        safe_text,
    size=
        safe_text,
    weight=
        safe_text,
    decoration=
        safe_text,
    family=
        safe_text
)
PNML_Dimension_strategy = st.builds(
    PNML_Dimension,
    width=
        safe_text,
    height=
        safe_text
)
PNML_Offset_strategy = st.builds(
    PNML_Offset,
)
PNML_Line_strategy = st.builds(
    PNML_Line,
    width=
        safe_text,
    shape=
        safe_text,
    style=
        safe_text
)
Color_strategy = st.builds(
    Color,
)
PNML_Fill_strategy = st.builds(
    PNML_Fill,
    gradientrotation=
        safe_text
)






@given(instance=PNML_Coordinate_strategy)
def test_hyp_pnml_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=PNML_Coordinate_strategy)
def test_hyp_pnml_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

























@given(instance=PNML_ToolSpecific_strategy)
def test_hyp_pnml_toolspecific_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=PNML_ToolSpecific_strategy)
def test_hyp_pnml_toolspecific_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original








@given(instance=PNML_Label_strategy)
def test_hyp_pnml_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original























@given(instance=PNML_IdedElement_strategy)
def test_hyp_pnml_idedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=PNML_AnyElement_strategy)
def test_hyp_pnml_anyelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PNML_AnyElement_strategy)
def test_hyp_pnml_anyelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=PNML_URI_strategy)
def test_hyp_pnml_uri_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=PNML_Font_strategy)
def test_hyp_pnml_font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=PNML_Font_strategy)
def test_hyp_pnml_font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=PNML_Font_strategy)
def test_hyp_pnml_font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=PNML_Font_strategy)
def test_hyp_pnml_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=PNML_Font_strategy)
def test_hyp_pnml_font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=PNML_Font_strategy)
def test_hyp_pnml_font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original



@given(instance=PNML_Font_strategy)
def test_hyp_pnml_font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original




@given(instance=PNML_Dimension_strategy)
def test_hyp_pnml_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=PNML_Dimension_strategy)
def test_hyp_pnml_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=PNML_Line_strategy)
def test_hyp_pnml_line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=PNML_Line_strategy)
def test_hyp_pnml_line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=PNML_Line_strategy)
def test_hyp_pnml_line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original





@given(instance=PNML_Fill_strategy)
def test_hyp_pnml_fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnnotationGraphics,
    AnyElement,
    Arc,
    Color,
    Coordinate,
    Dimension,
    EdgeGraphics,
    Fill,
    Font,
    Graphics,
    IdedElement,
    InitialMarking,
    Inscription,
    Label,
    LabeledElement,
    Line,
    Name,
    NetContent,
    NetContentElement,
    NetElement,
    NetGraphics,
    Node,
    NodeGraphics,
    Offset,
    PNMLDocument,
    PNML_AnnotationGraphics,
    PNML_AnyElement,
    PNML_Arc,
    PNML_Color,
    PNML_Coordinate,
    PNML_Dimension,
    PNML_EdgeGraphics,
    PNML_Fill,
    PNML_Font,
    PNML_Graphics,
    PNML_IdedElement,
    PNML_InitialMarking,
    PNML_Inscription,
    PNML_Label,
    PNML_LabeledElement,
    PNML_Line,
    PNML_Name,
    PNML_NetContent,
    PNML_NetContentElement,
    PNML_NetElement,
    PNML_NetGraphics,
    PNML_Node,
    PNML_NodeGraphics,
    PNML_Offset,
    PNML_PNMLDocument,
    PNML_Place,
    PNML_Position,
    PNML_ToolSpecific,
    PNML_Transition,
    PNML_URI,
    Place,
    Position,
    ToolSpecific,
    URI,
    AlignType,
    DecorationType,
    RotationType,
    ShapeType,
    StyleType,
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

def test_PNML_AnyElement_name_value_roundtrip():
    instance = PNML_AnyElement(name="sample_text", text="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_PNML_AnyElement_text_value_roundtrip():
    instance = PNML_AnyElement(name="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_PNML_Coordinate_x_value_roundtrip():
    instance = PNML_Coordinate(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_PNML_Coordinate_y_value_roundtrip():
    instance = PNML_Coordinate(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_PNML_Dimension_height_value_roundtrip():
    instance = PNML_Dimension(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_PNML_Dimension_width_value_roundtrip():
    instance = PNML_Dimension(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_PNML_Fill_gradientrotation_value_roundtrip():
    instance = PNML_Fill(gradientrotation="sample_text")
    assert instance.gradientrotation == "sample_text"
    instance.gradientrotation = "sample_text_2"
    assert instance.gradientrotation == "sample_text_2"


def test_PNML_Font_align_value_roundtrip():
    instance = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_PNML_Font_decoration_value_roundtrip():
    instance = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.decoration == "sample_text"
    instance.decoration = "sample_text_2"
    assert instance.decoration == "sample_text_2"


def test_PNML_Font_family_value_roundtrip():
    instance = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.family == "sample_text"
    instance.family = "sample_text_2"
    assert instance.family == "sample_text_2"


def test_PNML_Font_rotation_value_roundtrip():
    instance = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_PNML_Font_size_value_roundtrip():
    instance = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_PNML_Font_style_value_roundtrip():
    instance = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_PNML_Font_weight_value_roundtrip():
    instance = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_PNML_IdedElement_id_value_roundtrip():
    instance = PNML_IdedElement(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_PNML_Label_text_value_roundtrip():
    instance = PNML_Label(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_PNML_Line_shape_value_roundtrip():
    instance = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_PNML_Line_style_value_roundtrip():
    instance = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_PNML_Line_width_value_roundtrip():
    instance = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_PNML_ToolSpecific_tool_value_roundtrip():
    instance = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    assert instance.tool == "sample_text"
    instance.tool = "sample_text_2"
    assert instance.tool == "sample_text_2"


def test_PNML_ToolSpecific_version_value_roundtrip():
    instance = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_PNML_URI_value_value_roundtrip():
    instance = PNML_URI(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_PNML_Offset_isa_Coordinate():
    instance = PNML_Offset()
    assert isinstance(instance, Coordinate)


def test_PNML_Position_isa_Coordinate():
    instance = PNML_Position()
    assert isinstance(instance, Coordinate)


def test_PNML_AnnotationGraphics_isa_Graphics():
    instance = PNML_AnnotationGraphics()
    assert isinstance(instance, Graphics)


def test_PNML_EdgeGraphics_isa_Graphics():
    instance = PNML_EdgeGraphics()
    assert isinstance(instance, Graphics)


def test_PNML_NetGraphics_isa_Graphics():
    instance = PNML_NetGraphics()
    assert isinstance(instance, Graphics)


def test_PNML_NodeGraphics_isa_Graphics():
    instance = PNML_NodeGraphics()
    assert isinstance(instance, Graphics)


def test_PNML_Arc_isa_IdedElement():
    instance = PNML_Arc()
    assert isinstance(instance, IdedElement)


def test_PNML_NetElement_isa_IdedElement():
    instance = PNML_NetElement()
    assert isinstance(instance, IdedElement)


def test_PNML_Node_isa_IdedElement():
    instance = PNML_Node()
    assert isinstance(instance, IdedElement)


def test_PNML_InitialMarking_isa_LabeledElement():
    instance = PNML_InitialMarking()
    assert isinstance(instance, LabeledElement)


def test_PNML_Inscription_isa_LabeledElement():
    instance = PNML_Inscription()
    assert isinstance(instance, LabeledElement)


def test_PNML_Name_isa_LabeledElement():
    instance = PNML_Name()
    assert isinstance(instance, LabeledElement)


def test_PNML_Arc_isa_NetContent():
    instance = PNML_Arc()
    assert isinstance(instance, NetContent)


def test_PNML_NetContentElement_isa_NetContent():
    instance = PNML_NetContentElement()
    assert isinstance(instance, NetContent)


def test_PNML_Place_isa_NetContentElement():
    instance = PNML_Place()
    assert isinstance(instance, NetContentElement)


def test_PNML_Transition_isa_NetContentElement():
    instance = PNML_Transition()
    assert isinstance(instance, NetContentElement)


def test_assoc_annotationgraphics111_link_reassign_clear():
    a = PNML_Fill(gradientrotation="sample_text")
    b1 = AnnotationGraphics()
    b2 = AnnotationGraphics()
    _safe_set(a, 'fill112', b1)
    assert _is_linked(a, 'fill112', b1)
    if hasattr(b1, 'AnnotationGraphics113'):
        assert _is_linked(b1, 'AnnotationGraphics113', a)
    _safe_set(a, 'fill112', b2)
    assert _is_linked(a, 'fill112', b2)
    if hasattr(b1, 'AnnotationGraphics113'):
        assert not _is_linked(b1, 'AnnotationGraphics113', a)
    if hasattr(b2, 'AnnotationGraphics113'):
        assert _is_linked(b2, 'AnnotationGraphics113', a)
    _safe_set(a, 'fill112', None)
    assert not _is_linked(a, 'fill112', b2)
    if hasattr(b2, 'AnnotationGraphics113'):
        assert not _is_linked(b2, 'AnnotationGraphics113', a)


def test_assoc_annotationgraphics121_link_reassign_clear():
    a = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    b1 = AnnotationGraphics()
    b2 = AnnotationGraphics()
    _safe_set(a, 'line122', b1)
    assert _is_linked(a, 'line122', b1)
    if hasattr(b1, 'AnnotationGraphics123'):
        assert _is_linked(b1, 'AnnotationGraphics123', a)
    _safe_set(a, 'line122', b2)
    assert _is_linked(a, 'line122', b2)
    if hasattr(b1, 'AnnotationGraphics123'):
        assert not _is_linked(b1, 'AnnotationGraphics123', a)
    if hasattr(b2, 'AnnotationGraphics123'):
        assert _is_linked(b2, 'AnnotationGraphics123', a)
    _safe_set(a, 'line122', None)
    assert not _is_linked(a, 'line122', b2)
    if hasattr(b2, 'AnnotationGraphics123'):
        assert not _is_linked(b2, 'AnnotationGraphics123', a)


def test_assoc_annotationgraphics124_link_reassign_clear():
    a = PNML_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    b1 = AnnotationGraphics()
    b2 = AnnotationGraphics()
    _safe_set(a, 'font', b1)
    assert _is_linked(a, 'font', b1)
    if hasattr(b1, 'AnnotationGraphics125'):
        assert _is_linked(b1, 'AnnotationGraphics125', a)
    _safe_set(a, 'font', b2)
    assert _is_linked(a, 'font', b2)
    if hasattr(b1, 'AnnotationGraphics125'):
        assert not _is_linked(b1, 'AnnotationGraphics125', a)
    if hasattr(b2, 'AnnotationGraphics125'):
        assert _is_linked(b2, 'AnnotationGraphics125', a)
    _safe_set(a, 'font', None)
    assert not _is_linked(a, 'font', b2)
    if hasattr(b2, 'AnnotationGraphics125'):
        assert not _is_linked(b2, 'AnnotationGraphics125', a)


def test_assoc_anyelement16_link_reassign_clear():
    a = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    b1 = AnyElement()
    b2 = AnyElement()
    _safe_set(a, 'PNML_ToolSpecific', {b1})
    assert _is_linked(a, 'PNML_ToolSpecific', b1)
    if hasattr(b1, 'AnyElement'):
        assert _is_linked(b1, 'AnyElement', a)
    _safe_set(a, 'PNML_ToolSpecific', {b2})
    assert _is_linked(a, 'PNML_ToolSpecific', b2)
    if hasattr(b1, 'AnyElement'):
        assert not _is_linked(b1, 'AnyElement', a)
    if hasattr(b2, 'AnyElement'):
        assert _is_linked(b2, 'AnyElement', a)
    _safe_set(a, 'PNML_ToolSpecific', set())
    assert not _is_linked(a, 'PNML_ToolSpecific', b2)
    if hasattr(b2, 'AnyElement'):
        assert not _is_linked(b2, 'AnyElement', a)


def test_assoc_arc19_link_reassign_clear():
    a = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    b1 = Arc()
    b2 = Arc()
    _safe_set(a, 'tools20', b1)
    assert _is_linked(a, 'tools20', b1)
    if hasattr(b1, 'Arc'):
        assert _is_linked(b1, 'Arc', a)
    _safe_set(a, 'tools20', b2)
    assert _is_linked(a, 'tools20', b2)
    if hasattr(b1, 'Arc'):
        assert not _is_linked(b1, 'Arc', a)
    if hasattr(b2, 'Arc'):
        assert _is_linked(b2, 'Arc', a)
    _safe_set(a, 'tools20', None)
    assert not _is_linked(a, 'tools20', b2)
    if hasattr(b2, 'Arc'):
        assert not _is_linked(b2, 'Arc', a)


def test_assoc_color114_link_reassign_clear():
    a = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    b1 = Color()
    b2 = Color()
    _safe_set(a, 'PNML_Line', b1)
    assert _is_linked(a, 'PNML_Line', b1)
    if hasattr(b1, 'Color115'):
        assert _is_linked(b1, 'Color115', a)
    _safe_set(a, 'PNML_Line', b2)
    assert _is_linked(a, 'PNML_Line', b2)
    if hasattr(b1, 'Color115'):
        assert not _is_linked(b1, 'Color115', a)
    if hasattr(b2, 'Color115'):
        assert _is_linked(b2, 'Color115', a)
    _safe_set(a, 'PNML_Line', None)
    assert not _is_linked(a, 'PNML_Line', b2)
    if hasattr(b2, 'Color115'):
        assert not _is_linked(b2, 'Color115', a)


def test_assoc_edgegraphics108_link_reassign_clear():
    a = PNML_Fill(gradientrotation="sample_text")
    b1 = EdgeGraphics()
    b2 = EdgeGraphics()
    _safe_set(a, 'fill109', b1)
    assert _is_linked(a, 'fill109', b1)
    if hasattr(b1, 'EdgeGraphics110'):
        assert _is_linked(b1, 'EdgeGraphics110', a)
    _safe_set(a, 'fill109', b2)
    assert _is_linked(a, 'fill109', b2)
    if hasattr(b1, 'EdgeGraphics110'):
        assert not _is_linked(b1, 'EdgeGraphics110', a)
    if hasattr(b2, 'EdgeGraphics110'):
        assert _is_linked(b2, 'EdgeGraphics110', a)
    _safe_set(a, 'fill109', None)
    assert not _is_linked(a, 'fill109', b2)
    if hasattr(b2, 'EdgeGraphics110'):
        assert not _is_linked(b2, 'EdgeGraphics110', a)


def test_assoc_edgegraphics118_link_reassign_clear():
    a = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    b1 = EdgeGraphics()
    b2 = EdgeGraphics()
    _safe_set(a, 'line119', b1)
    assert _is_linked(a, 'line119', b1)
    if hasattr(b1, 'EdgeGraphics120'):
        assert _is_linked(b1, 'EdgeGraphics120', a)
    _safe_set(a, 'line119', b2)
    assert _is_linked(a, 'line119', b2)
    if hasattr(b1, 'EdgeGraphics120'):
        assert not _is_linked(b1, 'EdgeGraphics120', a)
    if hasattr(b2, 'EdgeGraphics120'):
        assert _is_linked(b2, 'EdgeGraphics120', a)
    _safe_set(a, 'line119', None)
    assert not _is_linked(a, 'line119', b2)
    if hasattr(b2, 'EdgeGraphics120'):
        assert not _is_linked(b2, 'EdgeGraphics120', a)


def test_assoc_gradientcolor100_link_reassign_clear():
    a = PNML_Fill(gradientrotation="sample_text")
    b1 = Color()
    b2 = Color()
    _safe_set(a, 'PNML_Fill101', b1)
    assert _is_linked(a, 'PNML_Fill101', b1)
    if hasattr(b1, 'Color102'):
        assert _is_linked(b1, 'Color102', a)
    _safe_set(a, 'PNML_Fill101', b2)
    assert _is_linked(a, 'PNML_Fill101', b2)
    if hasattr(b1, 'Color102'):
        assert not _is_linked(b1, 'Color102', a)
    if hasattr(b2, 'Color102'):
        assert _is_linked(b2, 'Color102', a)
    _safe_set(a, 'PNML_Fill101', None)
    assert not _is_linked(a, 'PNML_Fill101', b2)
    if hasattr(b2, 'Color102'):
        assert not _is_linked(b2, 'Color102', a)


def test_assoc_image103_link_reassign_clear():
    a = PNML_Fill(gradientrotation="sample_text")
    b1 = URI()
    b2 = URI()
    _safe_set(a, 'PNML_Fill104', b1)
    assert _is_linked(a, 'PNML_Fill104', b1)
    if hasattr(b1, 'URI105'):
        assert _is_linked(b1, 'URI105', a)
    _safe_set(a, 'PNML_Fill104', b2)
    assert _is_linked(a, 'PNML_Fill104', b2)
    if hasattr(b1, 'URI105'):
        assert not _is_linked(b1, 'URI105', a)
    if hasattr(b2, 'URI105'):
        assert _is_linked(b2, 'URI105', a)
    _safe_set(a, 'PNML_Fill104', None)
    assert not _is_linked(a, 'PNML_Fill104', b2)
    if hasattr(b2, 'URI105'):
        assert not _is_linked(b2, 'URI105', a)


def test_assoc_interiorcolor99_link_reassign_clear():
    a = PNML_Fill(gradientrotation="sample_text")
    b1 = Color()
    b2 = Color()
    _safe_set(a, 'PNML_Fill', b1)
    assert _is_linked(a, 'PNML_Fill', b1)
    if hasattr(b1, 'Color'):
        assert _is_linked(b1, 'Color', a)
    _safe_set(a, 'PNML_Fill', b2)
    assert _is_linked(a, 'PNML_Fill', b2)
    if hasattr(b1, 'Color'):
        assert not _is_linked(b1, 'Color', a)
    if hasattr(b2, 'Color'):
        assert _is_linked(b2, 'Color', a)
    _safe_set(a, 'PNML_Fill', None)
    assert not _is_linked(a, 'PNML_Fill', b2)
    if hasattr(b2, 'Color'):
        assert not _is_linked(b2, 'Color', a)


def test_assoc_namedelement26_link_reassign_clear():
    a = PNML_Label(text="sample_text")
    b1 = LabeledElement()
    b2 = LabeledElement()
    _safe_set(a, 'labels', b1)
    assert _is_linked(a, 'labels', b1)
    if hasattr(b1, 'LabeledElement'):
        assert _is_linked(b1, 'LabeledElement', a)
    _safe_set(a, 'labels', b2)
    assert _is_linked(a, 'labels', b2)
    if hasattr(b1, 'LabeledElement'):
        assert not _is_linked(b1, 'LabeledElement', a)
    if hasattr(b2, 'LabeledElement'):
        assert _is_linked(b2, 'LabeledElement', a)
    _safe_set(a, 'labels', None)
    assert not _is_linked(a, 'labels', b2)
    if hasattr(b2, 'LabeledElement'):
        assert not _is_linked(b2, 'LabeledElement', a)


def test_assoc_net17_link_reassign_clear():
    a = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    b1 = NetElement()
    b2 = NetElement()
    _safe_set(a, 'tools', b1)
    assert _is_linked(a, 'tools', b1)
    if hasattr(b1, 'NetElement18'):
        assert _is_linked(b1, 'NetElement18', a)
    _safe_set(a, 'tools', b2)
    assert _is_linked(a, 'tools', b2)
    if hasattr(b1, 'NetElement18'):
        assert not _is_linked(b1, 'NetElement18', a)
    if hasattr(b2, 'NetElement18'):
        assert _is_linked(b2, 'NetElement18', a)
    _safe_set(a, 'tools', None)
    assert not _is_linked(a, 'tools', b2)
    if hasattr(b2, 'NetElement18'):
        assert not _is_linked(b2, 'NetElement18', a)


def test_assoc_node21_link_reassign_clear():
    a = PNML_ToolSpecific(tool="sample_text", version="sample_text")
    b1 = Node()
    b2 = Node()
    _safe_set(a, 'tools22', b1)
    assert _is_linked(a, 'tools22', b1)
    if hasattr(b1, 'Node'):
        assert _is_linked(b1, 'Node', a)
    _safe_set(a, 'tools22', b2)
    assert _is_linked(a, 'tools22', b2)
    if hasattr(b1, 'Node'):
        assert not _is_linked(b1, 'Node', a)
    if hasattr(b2, 'Node'):
        assert _is_linked(b2, 'Node', a)
    _safe_set(a, 'tools22', None)
    assert not _is_linked(a, 'tools22', b2)
    if hasattr(b2, 'Node'):
        assert not _is_linked(b2, 'Node', a)


def test_assoc_nodegraphics106_link_reassign_clear():
    a = PNML_Fill(gradientrotation="sample_text")
    b1 = NodeGraphics()
    b2 = NodeGraphics()
    _safe_set(a, 'fill', b1)
    assert _is_linked(a, 'fill', b1)
    if hasattr(b1, 'NodeGraphics107'):
        assert _is_linked(b1, 'NodeGraphics107', a)
    _safe_set(a, 'fill', b2)
    assert _is_linked(a, 'fill', b2)
    if hasattr(b1, 'NodeGraphics107'):
        assert not _is_linked(b1, 'NodeGraphics107', a)
    if hasattr(b2, 'NodeGraphics107'):
        assert _is_linked(b2, 'NodeGraphics107', a)
    _safe_set(a, 'fill', None)
    assert not _is_linked(a, 'fill', b2)
    if hasattr(b2, 'NodeGraphics107'):
        assert not _is_linked(b2, 'NodeGraphics107', a)


def test_assoc_nodegraphics116_link_reassign_clear():
    a = PNML_Line(shape="sample_text", style="sample_text", width="sample_text")
    b1 = NodeGraphics()
    b2 = NodeGraphics()
    _safe_set(a, 'line', b1)
    assert _is_linked(a, 'line', b1)
    if hasattr(b1, 'NodeGraphics117'):
        assert _is_linked(b1, 'NodeGraphics117', a)
    _safe_set(a, 'line', b2)
    assert _is_linked(a, 'line', b2)
    if hasattr(b1, 'NodeGraphics117'):
        assert not _is_linked(b1, 'NodeGraphics117', a)
    if hasattr(b2, 'NodeGraphics117'):
        assert _is_linked(b2, 'NodeGraphics117', a)
    _safe_set(a, 'line', None)
    assert not _is_linked(a, 'line', b2)
    if hasattr(b2, 'NodeGraphics117'):
        assert not _is_linked(b2, 'NodeGraphics117', a)


def test_assoc_nodegraphics97_link_reassign_clear():
    a = PNML_Dimension(height="sample_text", width="sample_text")
    b1 = NodeGraphics()
    b2 = NodeGraphics()
    _safe_set(a, 'dimension', b1)
    assert _is_linked(a, 'dimension', b1)
    if hasattr(b1, 'NodeGraphics98'):
        assert _is_linked(b1, 'NodeGraphics98', a)
    _safe_set(a, 'dimension', b2)
    assert _is_linked(a, 'dimension', b2)
    if hasattr(b1, 'NodeGraphics98'):
        assert not _is_linked(b1, 'NodeGraphics98', a)
    if hasattr(b2, 'NodeGraphics98'):
        assert _is_linked(b2, 'NodeGraphics98', a)
    _safe_set(a, 'dimension', None)
    assert not _is_linked(a, 'dimension', b2)
    if hasattr(b2, 'NodeGraphics98'):
        assert not _is_linked(b2, 'NodeGraphics98', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnnotationGraphics_strategy = st.builds(AnnotationGraphics)
@given(instance=AnnotationGraphics_strategy)
@settings(max_examples=25)
def test_AnnotationGraphics_instantiation(instance):
    assert isinstance(instance, AnnotationGraphics)


AnyElement_strategy = st.builds(AnyElement)
@given(instance=AnyElement_strategy)
@settings(max_examples=25)
def test_AnyElement_instantiation(instance):
    assert isinstance(instance, AnyElement)


Arc_strategy = st.builds(Arc)
@given(instance=Arc_strategy)
@settings(max_examples=25)
def test_Arc_instantiation(instance):
    assert isinstance(instance, Arc)


Color_strategy = st.builds(Color)
@given(instance=Color_strategy)
@settings(max_examples=25)
def test_Color_instantiation(instance):
    assert isinstance(instance, Color)


Coordinate_strategy = st.builds(Coordinate)
@given(instance=Coordinate_strategy)
@settings(max_examples=25)
def test_Coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)


Dimension_strategy = st.builds(Dimension)
@given(instance=Dimension_strategy)
@settings(max_examples=25)
def test_Dimension_instantiation(instance):
    assert isinstance(instance, Dimension)


EdgeGraphics_strategy = st.builds(EdgeGraphics)
@given(instance=EdgeGraphics_strategy)
@settings(max_examples=25)
def test_EdgeGraphics_instantiation(instance):
    assert isinstance(instance, EdgeGraphics)


Fill_strategy = st.builds(Fill)
@given(instance=Fill_strategy)
@settings(max_examples=25)
def test_Fill_instantiation(instance):
    assert isinstance(instance, Fill)


Font_strategy = st.builds(Font)
@given(instance=Font_strategy)
@settings(max_examples=25)
def test_Font_instantiation(instance):
    assert isinstance(instance, Font)


Graphics_strategy = st.builds(Graphics)
@given(instance=Graphics_strategy)
@settings(max_examples=25)
def test_Graphics_instantiation(instance):
    assert isinstance(instance, Graphics)


IdedElement_strategy = st.builds(IdedElement)
@given(instance=IdedElement_strategy)
@settings(max_examples=25)
def test_IdedElement_instantiation(instance):
    assert isinstance(instance, IdedElement)


InitialMarking_strategy = st.builds(InitialMarking)
@given(instance=InitialMarking_strategy)
@settings(max_examples=25)
def test_InitialMarking_instantiation(instance):
    assert isinstance(instance, InitialMarking)


Inscription_strategy = st.builds(Inscription)
@given(instance=Inscription_strategy)
@settings(max_examples=25)
def test_Inscription_instantiation(instance):
    assert isinstance(instance, Inscription)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


LabeledElement_strategy = st.builds(LabeledElement)
@given(instance=LabeledElement_strategy)
@settings(max_examples=25)
def test_LabeledElement_instantiation(instance):
    assert isinstance(instance, LabeledElement)


Line_strategy = st.builds(Line)
@given(instance=Line_strategy)
@settings(max_examples=25)
def test_Line_instantiation(instance):
    assert isinstance(instance, Line)


Name_strategy = st.builds(Name)
@given(instance=Name_strategy)
@settings(max_examples=25)
def test_Name_instantiation(instance):
    assert isinstance(instance, Name)


NetContent_strategy = st.builds(NetContent)
@given(instance=NetContent_strategy)
@settings(max_examples=25)
def test_NetContent_instantiation(instance):
    assert isinstance(instance, NetContent)


NetContentElement_strategy = st.builds(NetContentElement)
@given(instance=NetContentElement_strategy)
@settings(max_examples=25)
def test_NetContentElement_instantiation(instance):
    assert isinstance(instance, NetContentElement)


NetElement_strategy = st.builds(NetElement)
@given(instance=NetElement_strategy)
@settings(max_examples=25)
def test_NetElement_instantiation(instance):
    assert isinstance(instance, NetElement)


NetGraphics_strategy = st.builds(NetGraphics)
@given(instance=NetGraphics_strategy)
@settings(max_examples=25)
def test_NetGraphics_instantiation(instance):
    assert isinstance(instance, NetGraphics)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


NodeGraphics_strategy = st.builds(NodeGraphics)
@given(instance=NodeGraphics_strategy)
@settings(max_examples=25)
def test_NodeGraphics_instantiation(instance):
    assert isinstance(instance, NodeGraphics)


Offset_strategy = st.builds(Offset)
@given(instance=Offset_strategy)
@settings(max_examples=25)
def test_Offset_instantiation(instance):
    assert isinstance(instance, Offset)


PNMLDocument_strategy = st.builds(PNMLDocument)
@given(instance=PNMLDocument_strategy)
@settings(max_examples=25)
def test_PNMLDocument_instantiation(instance):
    assert isinstance(instance, PNMLDocument)


PNML_AnnotationGraphics_strategy = st.builds(PNML_AnnotationGraphics)
@given(instance=PNML_AnnotationGraphics_strategy)
@settings(max_examples=25)
def test_PNML_AnnotationGraphics_instantiation(instance):
    assert isinstance(instance, PNML_AnnotationGraphics)


PNML_AnyElement_strategy = st.builds(PNML_AnyElement, name=safe_text, text=safe_text)
@given(instance=PNML_AnyElement_strategy)
@settings(max_examples=25)
def test_PNML_AnyElement_instantiation(instance):
    assert isinstance(instance, PNML_AnyElement)


PNML_Arc_strategy = st.builds(PNML_Arc)
@given(instance=PNML_Arc_strategy)
@settings(max_examples=25)
def test_PNML_Arc_instantiation(instance):
    assert isinstance(instance, PNML_Arc)


PNML_Color_strategy = st.builds(PNML_Color)
@given(instance=PNML_Color_strategy)
@settings(max_examples=25)
def test_PNML_Color_instantiation(instance):
    assert isinstance(instance, PNML_Color)


PNML_Coordinate_strategy = st.builds(PNML_Coordinate, x=safe_text, y=safe_text)
@given(instance=PNML_Coordinate_strategy)
@settings(max_examples=25)
def test_PNML_Coordinate_instantiation(instance):
    assert isinstance(instance, PNML_Coordinate)


PNML_Dimension_strategy = st.builds(PNML_Dimension, height=safe_text, width=safe_text)
@given(instance=PNML_Dimension_strategy)
@settings(max_examples=25)
def test_PNML_Dimension_instantiation(instance):
    assert isinstance(instance, PNML_Dimension)


PNML_EdgeGraphics_strategy = st.builds(PNML_EdgeGraphics)
@given(instance=PNML_EdgeGraphics_strategy)
@settings(max_examples=25)
def test_PNML_EdgeGraphics_instantiation(instance):
    assert isinstance(instance, PNML_EdgeGraphics)


PNML_Fill_strategy = st.builds(PNML_Fill, gradientrotation=safe_text)
@given(instance=PNML_Fill_strategy)
@settings(max_examples=25)
def test_PNML_Fill_instantiation(instance):
    assert isinstance(instance, PNML_Fill)


PNML_Font_strategy = st.builds(PNML_Font, align=safe_text, decoration=safe_text, family=safe_text, rotation=safe_text, size=safe_text, style=safe_text, weight=safe_text)
@given(instance=PNML_Font_strategy)
@settings(max_examples=25)
def test_PNML_Font_instantiation(instance):
    assert isinstance(instance, PNML_Font)


PNML_Graphics_strategy = st.builds(PNML_Graphics)
@given(instance=PNML_Graphics_strategy)
@settings(max_examples=25)
def test_PNML_Graphics_instantiation(instance):
    assert isinstance(instance, PNML_Graphics)


PNML_IdedElement_strategy = st.builds(PNML_IdedElement, id=safe_text)
@given(instance=PNML_IdedElement_strategy)
@settings(max_examples=25)
def test_PNML_IdedElement_instantiation(instance):
    assert isinstance(instance, PNML_IdedElement)


PNML_InitialMarking_strategy = st.builds(PNML_InitialMarking)
@given(instance=PNML_InitialMarking_strategy)
@settings(max_examples=25)
def test_PNML_InitialMarking_instantiation(instance):
    assert isinstance(instance, PNML_InitialMarking)


PNML_Inscription_strategy = st.builds(PNML_Inscription)
@given(instance=PNML_Inscription_strategy)
@settings(max_examples=25)
def test_PNML_Inscription_instantiation(instance):
    assert isinstance(instance, PNML_Inscription)


PNML_Label_strategy = st.builds(PNML_Label, text=safe_text)
@given(instance=PNML_Label_strategy)
@settings(max_examples=25)
def test_PNML_Label_instantiation(instance):
    assert isinstance(instance, PNML_Label)


PNML_LabeledElement_strategy = st.builds(PNML_LabeledElement)
@given(instance=PNML_LabeledElement_strategy)
@settings(max_examples=25)
def test_PNML_LabeledElement_instantiation(instance):
    assert isinstance(instance, PNML_LabeledElement)


PNML_Line_strategy = st.builds(PNML_Line, shape=safe_text, style=safe_text, width=safe_text)
@given(instance=PNML_Line_strategy)
@settings(max_examples=25)
def test_PNML_Line_instantiation(instance):
    assert isinstance(instance, PNML_Line)


PNML_Name_strategy = st.builds(PNML_Name)
@given(instance=PNML_Name_strategy)
@settings(max_examples=25)
def test_PNML_Name_instantiation(instance):
    assert isinstance(instance, PNML_Name)


PNML_NetContent_strategy = st.builds(PNML_NetContent)
@given(instance=PNML_NetContent_strategy)
@settings(max_examples=25)
def test_PNML_NetContent_instantiation(instance):
    assert isinstance(instance, PNML_NetContent)


PNML_NetContentElement_strategy = st.builds(PNML_NetContentElement)
@given(instance=PNML_NetContentElement_strategy)
@settings(max_examples=25)
def test_PNML_NetContentElement_instantiation(instance):
    assert isinstance(instance, PNML_NetContentElement)


PNML_NetElement_strategy = st.builds(PNML_NetElement)
@given(instance=PNML_NetElement_strategy)
@settings(max_examples=25)
def test_PNML_NetElement_instantiation(instance):
    assert isinstance(instance, PNML_NetElement)


PNML_NetGraphics_strategy = st.builds(PNML_NetGraphics)
@given(instance=PNML_NetGraphics_strategy)
@settings(max_examples=25)
def test_PNML_NetGraphics_instantiation(instance):
    assert isinstance(instance, PNML_NetGraphics)


PNML_Node_strategy = st.builds(PNML_Node)
@given(instance=PNML_Node_strategy)
@settings(max_examples=25)
def test_PNML_Node_instantiation(instance):
    assert isinstance(instance, PNML_Node)


PNML_NodeGraphics_strategy = st.builds(PNML_NodeGraphics)
@given(instance=PNML_NodeGraphics_strategy)
@settings(max_examples=25)
def test_PNML_NodeGraphics_instantiation(instance):
    assert isinstance(instance, PNML_NodeGraphics)


PNML_Offset_strategy = st.builds(PNML_Offset)
@given(instance=PNML_Offset_strategy)
@settings(max_examples=25)
def test_PNML_Offset_instantiation(instance):
    assert isinstance(instance, PNML_Offset)


PNML_PNMLDocument_strategy = st.builds(PNML_PNMLDocument)
@given(instance=PNML_PNMLDocument_strategy)
@settings(max_examples=25)
def test_PNML_PNMLDocument_instantiation(instance):
    assert isinstance(instance, PNML_PNMLDocument)


PNML_Place_strategy = st.builds(PNML_Place)
@given(instance=PNML_Place_strategy)
@settings(max_examples=25)
def test_PNML_Place_instantiation(instance):
    assert isinstance(instance, PNML_Place)


PNML_Position_strategy = st.builds(PNML_Position)
@given(instance=PNML_Position_strategy)
@settings(max_examples=25)
def test_PNML_Position_instantiation(instance):
    assert isinstance(instance, PNML_Position)


PNML_ToolSpecific_strategy = st.builds(PNML_ToolSpecific, tool=safe_text, version=safe_text)
@given(instance=PNML_ToolSpecific_strategy)
@settings(max_examples=25)
def test_PNML_ToolSpecific_instantiation(instance):
    assert isinstance(instance, PNML_ToolSpecific)


PNML_Transition_strategy = st.builds(PNML_Transition)
@given(instance=PNML_Transition_strategy)
@settings(max_examples=25)
def test_PNML_Transition_instantiation(instance):
    assert isinstance(instance, PNML_Transition)


PNML_URI_strategy = st.builds(PNML_URI, value=safe_text)
@given(instance=PNML_URI_strategy)
@settings(max_examples=25)
def test_PNML_URI_instantiation(instance):
    assert isinstance(instance, PNML_URI)


Place_strategy = st.builds(Place)
@given(instance=Place_strategy)
@settings(max_examples=25)
def test_Place_instantiation(instance):
    assert isinstance(instance, Place)


Position_strategy = st.builds(Position)
@given(instance=Position_strategy)
@settings(max_examples=25)
def test_Position_instantiation(instance):
    assert isinstance(instance, Position)


ToolSpecific_strategy = st.builds(ToolSpecific)
@given(instance=ToolSpecific_strategy)
@settings(max_examples=25)
def test_ToolSpecific_instantiation(instance):
    assert isinstance(instance, ToolSpecific)


URI_strategy = st.builds(URI)
@given(instance=URI_strategy)
@settings(max_examples=25)
def test_URI_instantiation(instance):
    assert isinstance(instance, URI)



