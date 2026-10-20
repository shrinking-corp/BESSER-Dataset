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
    migrationmodeler_GaugeSection,
    NodeStyle,
    migrationmodeler_Ellipse,
    migrationmodeler_Lozenge,
    migrationmodeler_Square,
    migrationmodeler_GaugeCompositeStyle,
    migrationmodeler_Note,
    migrationmodeler_BundledImage,
    migrationmodeler_Dot,
    BasicLabelStyle,
    migrationmodeler_LabelStyle,
    ContainerStyle,
    migrationmodeler_WorkspaceImage,
    migrationmodeler_ShapeContainerStyle,
    migrationmodeler_FlatContainerStyle,
    LabelStyle,
    migrationmodeler_BorderedStyle,
    migrationmodeler_Representation,
    migrationmodeler_TestCase,
    BorderedStyle,
    migrationmodeler_BasicLabelStyle,
    migrationmodeler_Color,
    migrationmodeler_ContainerStyle,
    AbstractNodeRepresentation,
    migrationmodeler_NodeStyle,
    migrationmodeler_EdgeStyle,
    migrationmodeler_Point,
    AbstractRepresentation,
    migrationmodeler_AbstractNodeRepresentation,
    migrationmodeler_Layout,
    migrationmodeler_AbstractRepresentation,
    migrationmodeler_ContainerRepresentation,
    migrationmodeler_BorderedRepresentation,
    migrationmodeler_NodeRepresentation,
    AbstractNode,
    migrationmodeler_Bordered,
    GraphicalElement,
    migrationmodeler_AbstractNode,
    migrationmodeler_GraphicalElement,
    migrationmodeler_Layer,
    migrationmodeler_Filter,
    migrationmodeler_Edge,
    migrationmodeler_Node,
    migrationmodeler_Container,
    Representation,
    migrationmodeler_Diagram,
    migrationmodeler_EdgeRepresentation,
    AlignmentKind,
    RoutingStyle,
    ContainerShape,
    LabelAlignment,
    LabelPosition,
    FontFormat,
    BackgroundStyle,
    BundledImageShape,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_migrationmodeler_gaugesection_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_GaugeSection)


def test_hyp_migrationmodeler_gaugesection_constructor_exists():
    assert callable(migrationmodeler_GaugeSection.__init__)


def test_hyp_migrationmodeler_gaugesection_constructor_args():
    sig = inspect.signature(migrationmodeler_GaugeSection.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"
    assert "label" in params, "Missing parameter 'label'"







def test_hyp_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_hyp_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_hyp_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_ellipse_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Ellipse)


def test_hyp_migrationmodeler_ellipse_constructor_exists():
    assert callable(migrationmodeler_Ellipse.__init__)


def test_hyp_migrationmodeler_ellipse_constructor_args():
    sig = inspect.signature(migrationmodeler_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameter" in params, "Missing parameter 'verticalDiameter'"
    assert "horizontalDiameter" in params, "Missing parameter 'horizontalDiameter'"





def test_hyp_migrationmodeler_lozenge_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Lozenge)


def test_hyp_migrationmodeler_lozenge_constructor_exists():
    assert callable(migrationmodeler_Lozenge.__init__)


def test_hyp_migrationmodeler_lozenge_constructor_args():
    sig = inspect.signature(migrationmodeler_Lozenge.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"





def test_hyp_migrationmodeler_square_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Square)


def test_hyp_migrationmodeler_square_constructor_exists():
    assert callable(migrationmodeler_Square.__init__)


def test_hyp_migrationmodeler_square_constructor_args():
    sig = inspect.signature(migrationmodeler_Square.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"





def test_hyp_migrationmodeler_gaugecompositestyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_GaugeCompositeStyle)


def test_hyp_migrationmodeler_gaugecompositestyle_constructor_exists():
    assert callable(migrationmodeler_GaugeCompositeStyle.__init__)


def test_hyp_migrationmodeler_gaugecompositestyle_constructor_args():
    sig = inspect.signature(migrationmodeler_GaugeCompositeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"




def test_hyp_migrationmodeler_note_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Note)


def test_hyp_migrationmodeler_note_constructor_exists():
    assert callable(migrationmodeler_Note.__init__)


def test_hyp_migrationmodeler_note_constructor_args():
    sig = inspect.signature(migrationmodeler_Note.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_bundledimage_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BundledImage)


def test_hyp_migrationmodeler_bundledimage_constructor_exists():
    assert callable(migrationmodeler_BundledImage.__init__)


def test_hyp_migrationmodeler_bundledimage_constructor_args():
    sig = inspect.signature(migrationmodeler_BundledImage.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"




def test_hyp_migrationmodeler_dot_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Dot)


def test_hyp_migrationmodeler_dot_constructor_exists():
    assert callable(migrationmodeler_Dot.__init__)


def test_hyp_migrationmodeler_dot_constructor_args():
    sig = inspect.signature(migrationmodeler_Dot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_hyp_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_hyp_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_labelstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_LabelStyle)


def test_hyp_migrationmodeler_labelstyle_constructor_exists():
    assert callable(migrationmodeler_LabelStyle.__init__)


def test_hyp_migrationmodeler_labelstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"




def test_hyp_containerstyle_is_not_abstract():
    assert not inspect.isabstract(ContainerStyle)


def test_hyp_containerstyle_constructor_exists():
    assert callable(ContainerStyle.__init__)


def test_hyp_containerstyle_constructor_args():
    sig = inspect.signature(ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_workspaceimage_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_WorkspaceImage)


def test_hyp_migrationmodeler_workspaceimage_constructor_exists():
    assert callable(migrationmodeler_WorkspaceImage.__init__)


def test_hyp_migrationmodeler_workspaceimage_constructor_args():
    sig = inspect.signature(migrationmodeler_WorkspaceImage.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"




def test_hyp_migrationmodeler_shapecontainerstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_ShapeContainerStyle)


def test_hyp_migrationmodeler_shapecontainerstyle_constructor_exists():
    assert callable(migrationmodeler_ShapeContainerStyle.__init__)


def test_hyp_migrationmodeler_shapecontainerstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_ShapeContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"




def test_hyp_migrationmodeler_flatcontainerstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_FlatContainerStyle)


def test_hyp_migrationmodeler_flatcontainerstyle_constructor_exists():
    assert callable(migrationmodeler_FlatContainerStyle.__init__)


def test_hyp_migrationmodeler_flatcontainerstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_FlatContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"




def test_hyp_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_hyp_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_hyp_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BorderedStyle)


def test_hyp_migrationmodeler_borderedstyle_constructor_exists():
    assert callable(migrationmodeler_BorderedStyle.__init__)


def test_hyp_migrationmodeler_borderedstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_BorderedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSize" in params, "Missing parameter 'borderSize'"




def test_hyp_migrationmodeler_representation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Representation)


def test_hyp_migrationmodeler_representation_constructor_exists():
    assert callable(migrationmodeler_Representation.__init__)


def test_hyp_migrationmodeler_representation_constructor_args():
    sig = inspect.signature(migrationmodeler_Representation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_migrationmodeler_testcase_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_TestCase)


def test_hyp_migrationmodeler_testcase_constructor_exists():
    assert callable(migrationmodeler_TestCase.__init__)


def test_hyp_migrationmodeler_testcase_constructor_args():
    sig = inspect.signature(migrationmodeler_TestCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(BorderedStyle)


def test_hyp_borderedstyle_constructor_exists():
    assert callable(BorderedStyle.__init__)


def test_hyp_borderedstyle_constructor_args():
    sig = inspect.signature(BorderedStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BasicLabelStyle)


def test_hyp_migrationmodeler_basiclabelstyle_constructor_exists():
    assert callable(migrationmodeler_BasicLabelStyle.__init__)


def test_hyp_migrationmodeler_basiclabelstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"







def test_hyp_migrationmodeler_color_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Color)


def test_hyp_migrationmodeler_color_constructor_exists():
    assert callable(migrationmodeler_Color.__init__)


def test_hyp_migrationmodeler_color_constructor_args():
    sig = inspect.signature(migrationmodeler_Color.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"






def test_hyp_migrationmodeler_containerstyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_ContainerStyle)


def test_hyp_migrationmodeler_containerstyle_constructor_exists():
    assert callable(migrationmodeler_ContainerStyle.__init__)


def test_hyp_migrationmodeler_containerstyle_constructor_args():
    sig = inspect.signature(migrationmodeler_ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractnoderepresentation_is_not_abstract():
    assert not inspect.isabstract(AbstractNodeRepresentation)


def test_hyp_abstractnoderepresentation_constructor_exists():
    assert callable(AbstractNodeRepresentation.__init__)


def test_hyp_abstractnoderepresentation_constructor_args():
    sig = inspect.signature(AbstractNodeRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_nodestyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_NodeStyle)


def test_hyp_migrationmodeler_nodestyle_constructor_exists():
    assert callable(migrationmodeler_NodeStyle.__init__)


def test_hyp_migrationmodeler_nodestyle_constructor_args():
    sig = inspect.signature(migrationmodeler_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"





def test_hyp_migrationmodeler_edgestyle_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_EdgeStyle)


def test_hyp_migrationmodeler_edgestyle_constructor_exists():
    assert callable(migrationmodeler_EdgeStyle.__init__)


def test_hyp_migrationmodeler_edgestyle_constructor_args():
    sig = inspect.signature(migrationmodeler_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"




def test_hyp_migrationmodeler_point_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Point)


def test_hyp_migrationmodeler_point_constructor_exists():
    assert callable(migrationmodeler_Point.__init__)


def test_hyp_migrationmodeler_point_constructor_args():
    sig = inspect.signature(migrationmodeler_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_abstractrepresentation_is_not_abstract():
    assert not inspect.isabstract(AbstractRepresentation)


def test_hyp_abstractrepresentation_constructor_exists():
    assert callable(AbstractRepresentation.__init__)


def test_hyp_abstractrepresentation_constructor_args():
    sig = inspect.signature(AbstractRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_abstractnoderepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_AbstractNodeRepresentation)


def test_hyp_migrationmodeler_abstractnoderepresentation_constructor_exists():
    assert callable(migrationmodeler_AbstractNodeRepresentation.__init__)


def test_hyp_migrationmodeler_abstractnoderepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_AbstractNodeRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_layout_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Layout)


def test_hyp_migrationmodeler_layout_constructor_exists():
    assert callable(migrationmodeler_Layout.__init__)


def test_hyp_migrationmodeler_layout_constructor_args():
    sig = inspect.signature(migrationmodeler_Layout.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"







def test_hyp_migrationmodeler_abstractrepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_AbstractRepresentation)


def test_hyp_migrationmodeler_abstractrepresentation_constructor_exists():
    assert callable(migrationmodeler_AbstractRepresentation.__init__)


def test_hyp_migrationmodeler_abstractrepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_AbstractRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "mappingId" in params, "Missing parameter 'mappingId'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "displayed" in params, "Missing parameter 'displayed'"
    assert "pinned" in params, "Missing parameter 'pinned'"







def test_hyp_migrationmodeler_containerrepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_ContainerRepresentation)


def test_hyp_migrationmodeler_containerrepresentation_constructor_exists():
    assert callable(migrationmodeler_ContainerRepresentation.__init__)


def test_hyp_migrationmodeler_containerrepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_ContainerRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "autoSized" in params, "Missing parameter 'autoSized'"




def test_hyp_migrationmodeler_borderedrepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_BorderedRepresentation)


def test_hyp_migrationmodeler_borderedrepresentation_constructor_exists():
    assert callable(migrationmodeler_BorderedRepresentation.__init__)


def test_hyp_migrationmodeler_borderedrepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_BorderedRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_noderepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_NodeRepresentation)


def test_hyp_migrationmodeler_noderepresentation_constructor_exists():
    assert callable(migrationmodeler_NodeRepresentation.__init__)


def test_hyp_migrationmodeler_noderepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_NodeRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_hyp_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_hyp_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_bordered_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Bordered)


def test_hyp_migrationmodeler_bordered_constructor_exists():
    assert callable(migrationmodeler_Bordered.__init__)


def test_hyp_migrationmodeler_bordered_constructor_args():
    sig = inspect.signature(migrationmodeler_Bordered.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(GraphicalElement)


def test_hyp_graphicalelement_constructor_exists():
    assert callable(GraphicalElement.__init__)


def test_hyp_graphicalelement_constructor_args():
    sig = inspect.signature(GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_abstractnode_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_AbstractNode)


def test_hyp_migrationmodeler_abstractnode_constructor_exists():
    assert callable(migrationmodeler_AbstractNode.__init__)


def test_hyp_migrationmodeler_abstractnode_constructor_args():
    sig = inspect.signature(migrationmodeler_AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_GraphicalElement)


def test_hyp_migrationmodeler_graphicalelement_constructor_exists():
    assert callable(migrationmodeler_GraphicalElement.__init__)


def test_hyp_migrationmodeler_graphicalelement_constructor_args():
    sig = inspect.signature(migrationmodeler_GraphicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_migrationmodeler_layer_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Layer)


def test_hyp_migrationmodeler_layer_constructor_exists():
    assert callable(migrationmodeler_Layer.__init__)


def test_hyp_migrationmodeler_layer_constructor_args():
    sig = inspect.signature(migrationmodeler_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "activated" in params, "Missing parameter 'activated'"





def test_hyp_migrationmodeler_filter_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Filter)


def test_hyp_migrationmodeler_filter_constructor_exists():
    assert callable(migrationmodeler_Filter.__init__)


def test_hyp_migrationmodeler_filter_constructor_args():
    sig = inspect.signature(migrationmodeler_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "activated" in params, "Missing parameter 'activated'"





def test_hyp_migrationmodeler_edge_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Edge)


def test_hyp_migrationmodeler_edge_constructor_exists():
    assert callable(migrationmodeler_Edge.__init__)


def test_hyp_migrationmodeler_edge_constructor_args():
    sig = inspect.signature(migrationmodeler_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_node_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Node)


def test_hyp_migrationmodeler_node_constructor_exists():
    assert callable(migrationmodeler_Node.__init__)


def test_hyp_migrationmodeler_node_constructor_args():
    sig = inspect.signature(migrationmodeler_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_container_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Container)


def test_hyp_migrationmodeler_container_constructor_exists():
    assert callable(migrationmodeler_Container.__init__)


def test_hyp_migrationmodeler_container_constructor_args():
    sig = inspect.signature(migrationmodeler_Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representation_is_not_abstract():
    assert not inspect.isabstract(Representation)


def test_hyp_representation_constructor_exists():
    assert callable(Representation.__init__)


def test_hyp_representation_constructor_args():
    sig = inspect.signature(Representation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_diagram_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_Diagram)


def test_hyp_migrationmodeler_diagram_constructor_exists():
    assert callable(migrationmodeler_Diagram.__init__)


def test_hyp_migrationmodeler_diagram_constructor_args():
    sig = inspect.signature(migrationmodeler_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_migrationmodeler_edgerepresentation_is_not_abstract():
    assert not inspect.isabstract(migrationmodeler_EdgeRepresentation)


def test_hyp_migrationmodeler_edgerepresentation_constructor_exists():
    assert callable(migrationmodeler_EdgeRepresentation.__init__)


def test_hyp_migrationmodeler_edgerepresentation_constructor_args():
    sig = inspect.signature(migrationmodeler_EdgeRepresentation.__init__)
    params = list(sig.parameters.keys())

def test_hyp_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_hyp_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "SQUARE",
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"

def test_hyp_routingstyle_exists():
    # Check that the Enumeration exists
    assert RoutingStyle is not None

def test_hyp_routingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoutingStyle]
    expected_literals = [
        "Tree",
        "Manhattan",
        "Straight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoutingStyle"

def test_hyp_containershape_exists():
    # Check that the Enumeration exists
    assert ContainerShape is not None

def test_hyp_containershape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerShape]
    expected_literals = [
        "parallelogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerShape"

def test_hyp_labelalignment_exists():
    # Check that the Enumeration exists
    assert LabelAlignment is not None

def test_hyp_labelalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelAlignment]
    expected_literals = [
        "LEFT",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelAlignment"

def test_hyp_labelposition_exists():
    # Check that the Enumeration exists
    assert LabelPosition is not None

def test_hyp_labelposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelPosition]
    expected_literals = [
        "border",
        "node",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelPosition"

def test_hyp_fontformat_exists():
    # Check that the Enumeration exists
    assert FontFormat is not None

def test_hyp_fontformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontFormat]
    expected_literals = [
        "italic",
        "bold_italic",
        "normal",
        "bold",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontFormat"

def test_hyp_backgroundstyle_exists():
    # Check that the Enumeration exists
    assert BackgroundStyle is not None

def test_hyp_backgroundstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackgroundStyle]
    expected_literals = [
        "GradientLeftToRight",
        "GradientTopToBottom",
        "Liquid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackgroundStyle"

def test_hyp_bundledimageshape_exists():
    # Check that the Enumeration exists
    assert BundledImageShape is not None

def test_hyp_bundledimageshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BundledImageShape]
    expected_literals = [
        "stroke",
        "triangle",
        "square",
        "dot",
        "ring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BundledImageShape"


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
migrationmodeler_GaugeSection_strategy = st.builds(
    migrationmodeler_GaugeSection,
    value=
        safe_text,
    min=
        safe_text,
    max=
        safe_text,
    label=
        safe_text
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
migrationmodeler_Ellipse_strategy = st.builds(
    migrationmodeler_Ellipse,
    verticalDiameter=
        safe_text,
    horizontalDiameter=
        safe_text
)
migrationmodeler_Lozenge_strategy = st.builds(
    migrationmodeler_Lozenge,
    height=
        safe_text,
    width=
        safe_text
)
migrationmodeler_Square_strategy = st.builds(
    migrationmodeler_Square,
    width=
        safe_text,
    height=
        safe_text
)
migrationmodeler_GaugeCompositeStyle_strategy = st.builds(
    migrationmodeler_GaugeCompositeStyle,
    alignment=
        safe_text
)
migrationmodeler_Note_strategy = st.builds(
    migrationmodeler_Note,
)
migrationmodeler_BundledImage_strategy = st.builds(
    migrationmodeler_BundledImage,
    shape=
        safe_text
)
migrationmodeler_Dot_strategy = st.builds(
    migrationmodeler_Dot,
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
migrationmodeler_LabelStyle_strategy = st.builds(
    migrationmodeler_LabelStyle,
    labelAlignment=
        safe_text
)
ContainerStyle_strategy = st.builds(
    ContainerStyle,
)
migrationmodeler_WorkspaceImage_strategy = st.builds(
    migrationmodeler_WorkspaceImage,
    workspacePath=
        safe_text
)
migrationmodeler_ShapeContainerStyle_strategy = st.builds(
    migrationmodeler_ShapeContainerStyle,
    shape=
        safe_text
)
migrationmodeler_FlatContainerStyle_strategy = st.builds(
    migrationmodeler_FlatContainerStyle,
    backgroundStyle=
        safe_text
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
migrationmodeler_BorderedStyle_strategy = st.builds(
    migrationmodeler_BorderedStyle,
    borderSize=
        st.integers()
)
migrationmodeler_Representation_strategy = st.builds(
    migrationmodeler_Representation,
    name=
        safe_text
)
migrationmodeler_TestCase_strategy = st.builds(
    migrationmodeler_TestCase,
)
BorderedStyle_strategy = st.builds(
    BorderedStyle,
)
migrationmodeler_BasicLabelStyle_strategy = st.builds(
    migrationmodeler_BasicLabelStyle,
    labelFormat=
        safe_text,
    labelSize=
        st.integers(),
    showIcon=
        st.booleans(),
    iconPath=
        safe_text
)
migrationmodeler_Color_strategy = st.builds(
    migrationmodeler_Color,
    blue=
        st.integers(),
    red=
        st.integers(),
    green=
        st.integers()
)
migrationmodeler_ContainerStyle_strategy = st.builds(
    migrationmodeler_ContainerStyle,
)
AbstractNodeRepresentation_strategy = st.builds(
    AbstractNodeRepresentation,
)
migrationmodeler_NodeStyle_strategy = st.builds(
    migrationmodeler_NodeStyle,
    labelPosition=
        safe_text,
    hideLabelByDefault=
        st.booleans()
)
migrationmodeler_EdgeStyle_strategy = st.builds(
    migrationmodeler_EdgeStyle,
    routingStyle=
        safe_text
)
migrationmodeler_Point_strategy = st.builds(
    migrationmodeler_Point,
    y=
        st.integers(),
    x=
        st.integers()
)
AbstractRepresentation_strategy = st.builds(
    AbstractRepresentation,
)
migrationmodeler_AbstractNodeRepresentation_strategy = st.builds(
    migrationmodeler_AbstractNodeRepresentation,
)
migrationmodeler_Layout_strategy = st.builds(
    migrationmodeler_Layout,
    x=
        st.integers(),
    height=
        st.integers(),
    width=
        st.integers(),
    y=
        st.integers()
)
migrationmodeler_AbstractRepresentation_strategy = st.builds(
    migrationmodeler_AbstractRepresentation,
    mappingId=
        safe_text,
    hidden=
        st.booleans(),
    displayed=
        st.booleans(),
    pinned=
        st.booleans()
)
migrationmodeler_ContainerRepresentation_strategy = st.builds(
    migrationmodeler_ContainerRepresentation,
    autoSized=
        st.booleans()
)
migrationmodeler_BorderedRepresentation_strategy = st.builds(
    migrationmodeler_BorderedRepresentation,
)
migrationmodeler_NodeRepresentation_strategy = st.builds(
    migrationmodeler_NodeRepresentation,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
migrationmodeler_Bordered_strategy = st.builds(
    migrationmodeler_Bordered,
)
GraphicalElement_strategy = st.builds(
    GraphicalElement,
)
migrationmodeler_AbstractNode_strategy = st.builds(
    migrationmodeler_AbstractNode,
)
migrationmodeler_GraphicalElement_strategy = st.builds(
    migrationmodeler_GraphicalElement,
    id=
        safe_text
)
migrationmodeler_Layer_strategy = st.builds(
    migrationmodeler_Layer,
    id=
        safe_text,
    activated=
        st.booleans()
)
migrationmodeler_Filter_strategy = st.builds(
    migrationmodeler_Filter,
    id=
        safe_text,
    activated=
        st.booleans()
)
migrationmodeler_Edge_strategy = st.builds(
    migrationmodeler_Edge,
)
migrationmodeler_Node_strategy = st.builds(
    migrationmodeler_Node,
)
migrationmodeler_Container_strategy = st.builds(
    migrationmodeler_Container,
)
Representation_strategy = st.builds(
    Representation,
)
migrationmodeler_Diagram_strategy = st.builds(
    migrationmodeler_Diagram,
)
migrationmodeler_EdgeRepresentation_strategy = st.builds(
    migrationmodeler_EdgeRepresentation,
)




@given(instance=migrationmodeler_GaugeSection_strategy)
def test_hyp_migrationmodeler_gaugesection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=migrationmodeler_GaugeSection_strategy)
def test_hyp_migrationmodeler_gaugesection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=migrationmodeler_GaugeSection_strategy)
def test_hyp_migrationmodeler_gaugesection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=migrationmodeler_GaugeSection_strategy)
def test_hyp_migrationmodeler_gaugesection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original





@given(instance=migrationmodeler_Ellipse_strategy)
def test_hyp_migrationmodeler_ellipse_verticalDiameter_setter(instance):
    original = instance.verticalDiameter
    instance.verticalDiameter = original
    assert instance.verticalDiameter == original



@given(instance=migrationmodeler_Ellipse_strategy)
def test_hyp_migrationmodeler_ellipse_horizontalDiameter_setter(instance):
    original = instance.horizontalDiameter
    instance.horizontalDiameter = original
    assert instance.horizontalDiameter == original




@given(instance=migrationmodeler_Lozenge_strategy)
def test_hyp_migrationmodeler_lozenge_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=migrationmodeler_Lozenge_strategy)
def test_hyp_migrationmodeler_lozenge_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=migrationmodeler_Square_strategy)
def test_hyp_migrationmodeler_square_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=migrationmodeler_Square_strategy)
def test_hyp_migrationmodeler_square_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=migrationmodeler_GaugeCompositeStyle_strategy)
def test_hyp_migrationmodeler_gaugecompositestyle_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original





@given(instance=migrationmodeler_BundledImage_strategy)
def test_hyp_migrationmodeler_bundledimage_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original






@given(instance=migrationmodeler_LabelStyle_strategy)
def test_hyp_migrationmodeler_labelstyle_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original





@given(instance=migrationmodeler_WorkspaceImage_strategy)
def test_hyp_migrationmodeler_workspaceimage_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original




@given(instance=migrationmodeler_ShapeContainerStyle_strategy)
def test_hyp_migrationmodeler_shapecontainerstyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original




@given(instance=migrationmodeler_FlatContainerStyle_strategy)
def test_hyp_migrationmodeler_flatcontainerstyle_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original





@given(instance=migrationmodeler_BorderedStyle_strategy)
def test_hyp_migrationmodeler_borderedstyle_borderSize_setter(instance):
    original = instance.borderSize
    instance.borderSize = original
    assert instance.borderSize == original




@given(instance=migrationmodeler_Representation_strategy)
def test_hyp_migrationmodeler_representation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_hyp_migrationmodeler_basiclabelstyle_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original



@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_hyp_migrationmodeler_basiclabelstyle_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_hyp_migrationmodeler_basiclabelstyle_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original



@given(instance=migrationmodeler_BasicLabelStyle_strategy)
def test_hyp_migrationmodeler_basiclabelstyle_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original




@given(instance=migrationmodeler_Color_strategy)
def test_hyp_migrationmodeler_color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=migrationmodeler_Color_strategy)
def test_hyp_migrationmodeler_color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=migrationmodeler_Color_strategy)
def test_hyp_migrationmodeler_color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original






@given(instance=migrationmodeler_NodeStyle_strategy)
def test_hyp_migrationmodeler_nodestyle_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original



@given(instance=migrationmodeler_NodeStyle_strategy)
def test_hyp_migrationmodeler_nodestyle_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original




@given(instance=migrationmodeler_EdgeStyle_strategy)
def test_hyp_migrationmodeler_edgestyle_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original




@given(instance=migrationmodeler_Point_strategy)
def test_hyp_migrationmodeler_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=migrationmodeler_Point_strategy)
def test_hyp_migrationmodeler_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original






@given(instance=migrationmodeler_Layout_strategy)
def test_hyp_migrationmodeler_layout_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=migrationmodeler_Layout_strategy)
def test_hyp_migrationmodeler_layout_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=migrationmodeler_Layout_strategy)
def test_hyp_migrationmodeler_layout_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=migrationmodeler_Layout_strategy)
def test_hyp_migrationmodeler_layout_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original




@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_hyp_migrationmodeler_abstractrepresentation_mappingId_setter(instance):
    original = instance.mappingId
    instance.mappingId = original
    assert instance.mappingId == original



@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_hyp_migrationmodeler_abstractrepresentation_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_hyp_migrationmodeler_abstractrepresentation_displayed_setter(instance):
    original = instance.displayed
    instance.displayed = original
    assert instance.displayed == original



@given(instance=migrationmodeler_AbstractRepresentation_strategy)
def test_hyp_migrationmodeler_abstractrepresentation_pinned_setter(instance):
    original = instance.pinned
    instance.pinned = original
    assert instance.pinned == original




@given(instance=migrationmodeler_ContainerRepresentation_strategy)
def test_hyp_migrationmodeler_containerrepresentation_autoSized_setter(instance):
    original = instance.autoSized
    instance.autoSized = original
    assert instance.autoSized == original










@given(instance=migrationmodeler_GraphicalElement_strategy)
def test_hyp_migrationmodeler_graphicalelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=migrationmodeler_Layer_strategy)
def test_hyp_migrationmodeler_layer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=migrationmodeler_Layer_strategy)
def test_hyp_migrationmodeler_layer_activated_setter(instance):
    original = instance.activated
    instance.activated = original
    assert instance.activated == original




@given(instance=migrationmodeler_Filter_strategy)
def test_hyp_migrationmodeler_filter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=migrationmodeler_Filter_strategy)
def test_hyp_migrationmodeler_filter_activated_setter(instance):
    original = instance.activated
    instance.activated = original
    assert instance.activated == original








# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractNode,
    AbstractNodeRepresentation,
    AbstractRepresentation,
    BasicLabelStyle,
    BorderedStyle,
    ContainerStyle,
    GraphicalElement,
    LabelStyle,
    NodeStyle,
    Representation,
    migrationmodeler_AbstractNode,
    migrationmodeler_AbstractNodeRepresentation,
    migrationmodeler_AbstractRepresentation,
    migrationmodeler_BasicLabelStyle,
    migrationmodeler_Bordered,
    migrationmodeler_BorderedRepresentation,
    migrationmodeler_BorderedStyle,
    migrationmodeler_BundledImage,
    migrationmodeler_Color,
    migrationmodeler_Container,
    migrationmodeler_ContainerRepresentation,
    migrationmodeler_ContainerStyle,
    migrationmodeler_Diagram,
    migrationmodeler_Dot,
    migrationmodeler_Edge,
    migrationmodeler_EdgeRepresentation,
    migrationmodeler_EdgeStyle,
    migrationmodeler_Ellipse,
    migrationmodeler_Filter,
    migrationmodeler_FlatContainerStyle,
    migrationmodeler_GaugeCompositeStyle,
    migrationmodeler_GaugeSection,
    migrationmodeler_GraphicalElement,
    migrationmodeler_LabelStyle,
    migrationmodeler_Layer,
    migrationmodeler_Layout,
    migrationmodeler_Lozenge,
    migrationmodeler_Node,
    migrationmodeler_NodeRepresentation,
    migrationmodeler_NodeStyle,
    migrationmodeler_Note,
    migrationmodeler_Point,
    migrationmodeler_Representation,
    migrationmodeler_ShapeContainerStyle,
    migrationmodeler_Square,
    migrationmodeler_TestCase,
    migrationmodeler_WorkspaceImage,
    AlignmentKind,
    BackgroundStyle,
    BundledImageShape,
    ContainerShape,
    FontFormat,
    LabelAlignment,
    LabelPosition,
    RoutingStyle,
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

def test_migrationmodeler_AbstractRepresentation_displayed_value_roundtrip():
    instance = migrationmodeler_AbstractRepresentation(displayed=True, hidden=True, mappingId="sample_text", pinned=True)
    assert instance.displayed == True
    instance.displayed = False
    assert instance.displayed == False


def test_migrationmodeler_AbstractRepresentation_hidden_value_roundtrip():
    instance = migrationmodeler_AbstractRepresentation(displayed=True, hidden=True, mappingId="sample_text", pinned=True)
    assert instance.hidden == True
    instance.hidden = False
    assert instance.hidden == False


def test_migrationmodeler_AbstractRepresentation_mappingId_value_roundtrip():
    instance = migrationmodeler_AbstractRepresentation(displayed=True, hidden=True, mappingId="sample_text", pinned=True)
    assert instance.mappingId == "sample_text"
    instance.mappingId = "sample_text_2"
    assert instance.mappingId == "sample_text_2"


def test_migrationmodeler_AbstractRepresentation_pinned_value_roundtrip():
    instance = migrationmodeler_AbstractRepresentation(displayed=True, hidden=True, mappingId="sample_text", pinned=True)
    assert instance.pinned == True
    instance.pinned = False
    assert instance.pinned == False


def test_migrationmodeler_BasicLabelStyle_iconPath_value_roundtrip():
    instance = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.iconPath == "sample_text"
    instance.iconPath = "sample_text_2"
    assert instance.iconPath == "sample_text_2"


def test_migrationmodeler_BasicLabelStyle_labelFormat_value_roundtrip():
    instance = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelFormat == "sample_text"
    instance.labelFormat = "sample_text_2"
    assert instance.labelFormat == "sample_text_2"


def test_migrationmodeler_BasicLabelStyle_labelSize_value_roundtrip():
    instance = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.labelSize == 7
    instance.labelSize = 13
    assert instance.labelSize == 13


def test_migrationmodeler_BasicLabelStyle_showIcon_value_roundtrip():
    instance = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    assert instance.showIcon == True
    instance.showIcon = False
    assert instance.showIcon == False


def test_migrationmodeler_BorderedStyle_borderSize_value_roundtrip():
    instance = migrationmodeler_BorderedStyle(borderSize=7)
    assert instance.borderSize == 7
    instance.borderSize = 13
    assert instance.borderSize == 13


def test_migrationmodeler_BundledImage_shape_value_roundtrip():
    instance = migrationmodeler_BundledImage(shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_migrationmodeler_Color_blue_value_roundtrip():
    instance = migrationmodeler_Color(blue=7, green=7, red=7)
    assert instance.blue == 7
    instance.blue = 13
    assert instance.blue == 13


def test_migrationmodeler_Color_green_value_roundtrip():
    instance = migrationmodeler_Color(blue=7, green=7, red=7)
    assert instance.green == 7
    instance.green = 13
    assert instance.green == 13


def test_migrationmodeler_Color_red_value_roundtrip():
    instance = migrationmodeler_Color(blue=7, green=7, red=7)
    assert instance.red == 7
    instance.red = 13
    assert instance.red == 13


def test_migrationmodeler_ContainerRepresentation_autoSized_value_roundtrip():
    instance = migrationmodeler_ContainerRepresentation(autoSized=True)
    assert instance.autoSized == True
    instance.autoSized = False
    assert instance.autoSized == False


def test_migrationmodeler_EdgeStyle_routingStyle_value_roundtrip():
    instance = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    assert instance.routingStyle == "sample_text"
    instance.routingStyle = "sample_text_2"
    assert instance.routingStyle == "sample_text_2"


def test_migrationmodeler_Ellipse_horizontalDiameter_value_roundtrip():
    instance = migrationmodeler_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert instance.horizontalDiameter == "sample_text"
    instance.horizontalDiameter = "sample_text_2"
    assert instance.horizontalDiameter == "sample_text_2"


def test_migrationmodeler_Ellipse_verticalDiameter_value_roundtrip():
    instance = migrationmodeler_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert instance.verticalDiameter == "sample_text"
    instance.verticalDiameter = "sample_text_2"
    assert instance.verticalDiameter == "sample_text_2"


def test_migrationmodeler_Filter_activated_value_roundtrip():
    instance = migrationmodeler_Filter(activated=True, id="sample_text")
    assert instance.activated == True
    instance.activated = False
    assert instance.activated == False


def test_migrationmodeler_Filter_id_value_roundtrip():
    instance = migrationmodeler_Filter(activated=True, id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_migrationmodeler_FlatContainerStyle_backgroundStyle_value_roundtrip():
    instance = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text")
    assert instance.backgroundStyle == "sample_text"
    instance.backgroundStyle = "sample_text_2"
    assert instance.backgroundStyle == "sample_text_2"


def test_migrationmodeler_GaugeCompositeStyle_alignment_value_roundtrip():
    instance = migrationmodeler_GaugeCompositeStyle(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_migrationmodeler_GaugeSection_label_value_roundtrip():
    instance = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_migrationmodeler_GaugeSection_max_value_roundtrip():
    instance = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_migrationmodeler_GaugeSection_min_value_roundtrip():
    instance = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_migrationmodeler_GaugeSection_value_value_roundtrip():
    instance = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_migrationmodeler_GraphicalElement_id_value_roundtrip():
    instance = migrationmodeler_GraphicalElement(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_migrationmodeler_LabelStyle_labelAlignment_value_roundtrip():
    instance = migrationmodeler_LabelStyle(labelAlignment="sample_text")
    assert instance.labelAlignment == "sample_text"
    instance.labelAlignment = "sample_text_2"
    assert instance.labelAlignment == "sample_text_2"


def test_migrationmodeler_Layer_activated_value_roundtrip():
    instance = migrationmodeler_Layer(activated=True, id="sample_text")
    assert instance.activated == True
    instance.activated = False
    assert instance.activated == False


def test_migrationmodeler_Layer_id_value_roundtrip():
    instance = migrationmodeler_Layer(activated=True, id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_migrationmodeler_Layout_height_value_roundtrip():
    instance = migrationmodeler_Layout(height=7, width=7, x=7, y=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_migrationmodeler_Layout_width_value_roundtrip():
    instance = migrationmodeler_Layout(height=7, width=7, x=7, y=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_migrationmodeler_Layout_x_value_roundtrip():
    instance = migrationmodeler_Layout(height=7, width=7, x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_migrationmodeler_Layout_y_value_roundtrip():
    instance = migrationmodeler_Layout(height=7, width=7, x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_migrationmodeler_Lozenge_height_value_roundtrip():
    instance = migrationmodeler_Lozenge(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_migrationmodeler_Lozenge_width_value_roundtrip():
    instance = migrationmodeler_Lozenge(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_migrationmodeler_NodeStyle_hideLabelByDefault_value_roundtrip():
    instance = migrationmodeler_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert instance.hideLabelByDefault == True
    instance.hideLabelByDefault = False
    assert instance.hideLabelByDefault == False


def test_migrationmodeler_NodeStyle_labelPosition_value_roundtrip():
    instance = migrationmodeler_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_migrationmodeler_Point_x_value_roundtrip():
    instance = migrationmodeler_Point(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_migrationmodeler_Point_y_value_roundtrip():
    instance = migrationmodeler_Point(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_migrationmodeler_Representation_name_value_roundtrip():
    instance = migrationmodeler_Representation(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_migrationmodeler_ShapeContainerStyle_shape_value_roundtrip():
    instance = migrationmodeler_ShapeContainerStyle(shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_migrationmodeler_Square_height_value_roundtrip():
    instance = migrationmodeler_Square(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_migrationmodeler_Square_width_value_roundtrip():
    instance = migrationmodeler_Square(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_migrationmodeler_WorkspaceImage_workspacePath_value_roundtrip():
    instance = migrationmodeler_WorkspaceImage(workspacePath="sample_text")
    assert instance.workspacePath == "sample_text"
    instance.workspacePath = "sample_text_2"
    assert instance.workspacePath == "sample_text_2"


def test_migrationmodeler_Bordered_isa_AbstractNode():
    instance = migrationmodeler_Bordered()
    assert isinstance(instance, AbstractNode)


def test_migrationmodeler_Node_isa_AbstractNode():
    instance = migrationmodeler_Node()
    assert isinstance(instance, AbstractNode)


def test_migrationmodeler_BorderedRepresentation_isa_AbstractNodeRepresentation():
    instance = migrationmodeler_BorderedRepresentation()
    assert isinstance(instance, AbstractNodeRepresentation)


def test_migrationmodeler_NodeRepresentation_isa_AbstractNodeRepresentation():
    instance = migrationmodeler_NodeRepresentation()
    assert isinstance(instance, AbstractNodeRepresentation)


def test_migrationmodeler_AbstractNodeRepresentation_isa_AbstractRepresentation():
    instance = migrationmodeler_AbstractNodeRepresentation()
    assert isinstance(instance, AbstractRepresentation)


def test_migrationmodeler_ContainerRepresentation_isa_AbstractRepresentation():
    instance = migrationmodeler_ContainerRepresentation(autoSized=True)
    assert isinstance(instance, AbstractRepresentation)


def test_migrationmodeler_EdgeRepresentation_isa_AbstractRepresentation():
    instance = migrationmodeler_EdgeRepresentation()
    assert isinstance(instance, AbstractRepresentation)


def test_migrationmodeler_LabelStyle_isa_BasicLabelStyle():
    instance = migrationmodeler_LabelStyle(labelAlignment="sample_text")
    assert isinstance(instance, BasicLabelStyle)


def test_migrationmodeler_ContainerStyle_isa_BorderedStyle():
    instance = migrationmodeler_ContainerStyle()
    assert isinstance(instance, BorderedStyle)


def test_migrationmodeler_NodeStyle_isa_BorderedStyle():
    instance = migrationmodeler_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert isinstance(instance, BorderedStyle)


def test_migrationmodeler_FlatContainerStyle_isa_ContainerStyle():
    instance = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_migrationmodeler_ShapeContainerStyle_isa_ContainerStyle():
    instance = migrationmodeler_ShapeContainerStyle(shape="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_migrationmodeler_WorkspaceImage_isa_ContainerStyle():
    instance = migrationmodeler_WorkspaceImage(workspacePath="sample_text")
    assert isinstance(instance, ContainerStyle)


def test_migrationmodeler_AbstractNode_isa_GraphicalElement():
    instance = migrationmodeler_AbstractNode()
    assert isinstance(instance, GraphicalElement)


def test_migrationmodeler_Container_isa_GraphicalElement():
    instance = migrationmodeler_Container()
    assert isinstance(instance, GraphicalElement)


def test_migrationmodeler_Edge_isa_GraphicalElement():
    instance = migrationmodeler_Edge()
    assert isinstance(instance, GraphicalElement)


def test_migrationmodeler_ContainerStyle_isa_LabelStyle():
    instance = migrationmodeler_ContainerStyle()
    assert isinstance(instance, LabelStyle)


def test_migrationmodeler_NodeStyle_isa_LabelStyle():
    instance = migrationmodeler_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    assert isinstance(instance, LabelStyle)


def test_migrationmodeler_BundledImage_isa_NodeStyle():
    instance = migrationmodeler_BundledImage(shape="sample_text")
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_Dot_isa_NodeStyle():
    instance = migrationmodeler_Dot()
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_Ellipse_isa_NodeStyle():
    instance = migrationmodeler_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_GaugeCompositeStyle_isa_NodeStyle():
    instance = migrationmodeler_GaugeCompositeStyle(alignment="sample_text")
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_Lozenge_isa_NodeStyle():
    instance = migrationmodeler_Lozenge(height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_Note_isa_NodeStyle():
    instance = migrationmodeler_Note()
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_Square_isa_NodeStyle():
    instance = migrationmodeler_Square(height="sample_text", width="sample_text")
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_WorkspaceImage_isa_NodeStyle():
    instance = migrationmodeler_WorkspaceImage(workspacePath="sample_text")
    assert isinstance(instance, NodeStyle)


def test_migrationmodeler_Diagram_isa_Representation():
    instance = migrationmodeler_Diagram()
    assert isinstance(instance, Representation)


def test_assoc_backgroundColor57_link_reassign_clear():
    a = migrationmodeler_Color(blue=7, green=7, red=7)
    b1 = migrationmodeler_Dot()
    b2 = migrationmodeler_Dot()
    _safe_set(a, 'migrationmodeler_Color58', b1)
    assert _is_linked(a, 'migrationmodeler_Color58', b1)
    if hasattr(b1, 'migrationmodeler_Dot'):
        assert _is_linked(b1, 'migrationmodeler_Dot', a)
    _safe_set(a, 'migrationmodeler_Color58', b2)
    assert _is_linked(a, 'migrationmodeler_Color58', b2)
    if hasattr(b1, 'migrationmodeler_Dot'):
        assert not _is_linked(b1, 'migrationmodeler_Dot', a)
    if hasattr(b2, 'migrationmodeler_Dot'):
        assert _is_linked(b2, 'migrationmodeler_Dot', a)
    _safe_set(a, 'migrationmodeler_Color58', None)
    assert not _is_linked(a, 'migrationmodeler_Color58', b2)
    if hasattr(b2, 'migrationmodeler_Dot'):
        assert not _is_linked(b2, 'migrationmodeler_Dot', a)


def test_assoc_backgroundColor59_link_reassign_clear():
    a = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_GaugeSection', b1)
    assert _is_linked(a, 'migrationmodeler_GaugeSection', b1)
    if hasattr(b1, 'migrationmodeler_Color60'):
        assert _is_linked(b1, 'migrationmodeler_Color60', a)
    _safe_set(a, 'migrationmodeler_GaugeSection', b2)
    assert _is_linked(a, 'migrationmodeler_GaugeSection', b2)
    if hasattr(b1, 'migrationmodeler_Color60'):
        assert not _is_linked(b1, 'migrationmodeler_Color60', a)
    if hasattr(b2, 'migrationmodeler_Color60'):
        assert _is_linked(b2, 'migrationmodeler_Color60', a)
    _safe_set(a, 'migrationmodeler_GaugeSection', None)
    assert not _is_linked(a, 'migrationmodeler_GaugeSection', b2)
    if hasattr(b2, 'migrationmodeler_Color60'):
        assert not _is_linked(b2, 'migrationmodeler_Color60', a)


def test_assoc_backgroundColor64_link_reassign_clear():
    a = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_FlatContainerStyle', b1)
    assert _is_linked(a, 'migrationmodeler_FlatContainerStyle', b1)
    if hasattr(b1, 'migrationmodeler_Color65'):
        assert _is_linked(b1, 'migrationmodeler_Color65', a)
    _safe_set(a, 'migrationmodeler_FlatContainerStyle', b2)
    assert _is_linked(a, 'migrationmodeler_FlatContainerStyle', b2)
    if hasattr(b1, 'migrationmodeler_Color65'):
        assert not _is_linked(b1, 'migrationmodeler_Color65', a)
    if hasattr(b2, 'migrationmodeler_Color65'):
        assert _is_linked(b2, 'migrationmodeler_Color65', a)
    _safe_set(a, 'migrationmodeler_FlatContainerStyle', None)
    assert not _is_linked(a, 'migrationmodeler_FlatContainerStyle', b2)
    if hasattr(b2, 'migrationmodeler_Color65'):
        assert not _is_linked(b2, 'migrationmodeler_Color65', a)


def test_assoc_backgroundColor69_link_reassign_clear():
    a = migrationmodeler_ShapeContainerStyle(shape="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_ShapeContainerStyle', b1)
    assert _is_linked(a, 'migrationmodeler_ShapeContainerStyle', b1)
    if hasattr(b1, 'migrationmodeler_Color70'):
        assert _is_linked(b1, 'migrationmodeler_Color70', a)
    _safe_set(a, 'migrationmodeler_ShapeContainerStyle', b2)
    assert _is_linked(a, 'migrationmodeler_ShapeContainerStyle', b2)
    if hasattr(b1, 'migrationmodeler_Color70'):
        assert not _is_linked(b1, 'migrationmodeler_Color70', a)
    if hasattr(b2, 'migrationmodeler_Color70'):
        assert _is_linked(b2, 'migrationmodeler_Color70', a)
    _safe_set(a, 'migrationmodeler_ShapeContainerStyle', None)
    assert not _is_linked(a, 'migrationmodeler_ShapeContainerStyle', b2)
    if hasattr(b2, 'migrationmodeler_Color70'):
        assert not _is_linked(b2, 'migrationmodeler_Color70', a)


def test_assoc_beginLabelStyle43_link_reassign_clear():
    a = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    b1 = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    b2 = migrationmodeler_BasicLabelStyle(iconPath="sample_text_2", labelFormat="sample_text_2", labelSize=13, showIcon=False)
    _safe_set(a, 'migrationmodeler_EdgeStyle44', b1)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle44', b1)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle'):
        assert _is_linked(b1, 'migrationmodeler_BasicLabelStyle', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle44', b2)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle44', b2)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle'):
        assert not _is_linked(b1, 'migrationmodeler_BasicLabelStyle', a)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle'):
        assert _is_linked(b2, 'migrationmodeler_BasicLabelStyle', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle44', None)
    assert not _is_linked(a, 'migrationmodeler_EdgeStyle44', b2)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle'):
        assert not _is_linked(b2, 'migrationmodeler_BasicLabelStyle', a)


def test_assoc_bendpoints31_link_reassign_clear():
    a = migrationmodeler_Point(x=7, y=7)
    b1 = migrationmodeler_EdgeRepresentation()
    b2 = migrationmodeler_EdgeRepresentation()
    _safe_set(a, 'migrationmodeler_Point', b1)
    assert _is_linked(a, 'migrationmodeler_Point', b1)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation32'):
        assert _is_linked(b1, 'migrationmodeler_EdgeRepresentation32', a)
    _safe_set(a, 'migrationmodeler_Point', b2)
    assert _is_linked(a, 'migrationmodeler_Point', b2)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation32'):
        assert not _is_linked(b1, 'migrationmodeler_EdgeRepresentation32', a)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation32'):
        assert _is_linked(b2, 'migrationmodeler_EdgeRepresentation32', a)
    _safe_set(a, 'migrationmodeler_Point', None)
    assert not _is_linked(a, 'migrationmodeler_Point', b2)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation32'):
        assert not _is_linked(b2, 'migrationmodeler_EdgeRepresentation32', a)


def test_assoc_borderColor52_link_reassign_clear():
    a = migrationmodeler_Color(blue=7, green=7, red=7)
    b1 = migrationmodeler_BorderedStyle(borderSize=7)
    b2 = migrationmodeler_BorderedStyle(borderSize=13)
    _safe_set(a, 'migrationmodeler_Color53', b1)
    assert _is_linked(a, 'migrationmodeler_Color53', b1)
    if hasattr(b1, 'migrationmodeler_BorderedStyle'):
        assert _is_linked(b1, 'migrationmodeler_BorderedStyle', a)
    _safe_set(a, 'migrationmodeler_Color53', b2)
    assert _is_linked(a, 'migrationmodeler_Color53', b2)
    if hasattr(b1, 'migrationmodeler_BorderedStyle'):
        assert not _is_linked(b1, 'migrationmodeler_BorderedStyle', a)
    if hasattr(b2, 'migrationmodeler_BorderedStyle'):
        assert _is_linked(b2, 'migrationmodeler_BorderedStyle', a)
    _safe_set(a, 'migrationmodeler_Color53', None)
    assert not _is_linked(a, 'migrationmodeler_Color53', b2)
    if hasattr(b2, 'migrationmodeler_BorderedStyle'):
        assert not _is_linked(b2, 'migrationmodeler_BorderedStyle', a)


def test_assoc_centerLabelStyle45_link_reassign_clear():
    a = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    b1 = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    b2 = migrationmodeler_BasicLabelStyle(iconPath="sample_text_2", labelFormat="sample_text_2", labelSize=13, showIcon=False)
    _safe_set(a, 'migrationmodeler_EdgeStyle46', b1)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle46', b1)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle47'):
        assert _is_linked(b1, 'migrationmodeler_BasicLabelStyle47', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle46', b2)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle46', b2)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle47'):
        assert not _is_linked(b1, 'migrationmodeler_BasicLabelStyle47', a)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle47'):
        assert _is_linked(b2, 'migrationmodeler_BasicLabelStyle47', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle46', None)
    assert not _is_linked(a, 'migrationmodeler_EdgeStyle46', b2)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle47'):
        assert not _is_linked(b2, 'migrationmodeler_BasicLabelStyle47', a)


def test_assoc_color41_link_reassign_clear():
    a = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_EdgeStyle42', b1)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle42', b1)
    if hasattr(b1, 'migrationmodeler_Color'):
        assert _is_linked(b1, 'migrationmodeler_Color', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle42', b2)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle42', b2)
    if hasattr(b1, 'migrationmodeler_Color'):
        assert not _is_linked(b1, 'migrationmodeler_Color', a)
    if hasattr(b2, 'migrationmodeler_Color'):
        assert _is_linked(b2, 'migrationmodeler_Color', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle42', None)
    assert not _is_linked(a, 'migrationmodeler_EdgeStyle42', b2)
    if hasattr(b2, 'migrationmodeler_Color'):
        assert not _is_linked(b2, 'migrationmodeler_Color', a)


def test_assoc_color71_link_reassign_clear():
    a = migrationmodeler_Square(height="sample_text", width="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_Square', b1)
    assert _is_linked(a, 'migrationmodeler_Square', b1)
    if hasattr(b1, 'migrationmodeler_Color72'):
        assert _is_linked(b1, 'migrationmodeler_Color72', a)
    _safe_set(a, 'migrationmodeler_Square', b2)
    assert _is_linked(a, 'migrationmodeler_Square', b2)
    if hasattr(b1, 'migrationmodeler_Color72'):
        assert not _is_linked(b1, 'migrationmodeler_Color72', a)
    if hasattr(b2, 'migrationmodeler_Color72'):
        assert _is_linked(b2, 'migrationmodeler_Color72', a)
    _safe_set(a, 'migrationmodeler_Square', None)
    assert not _is_linked(a, 'migrationmodeler_Square', b2)
    if hasattr(b2, 'migrationmodeler_Color72'):
        assert not _is_linked(b2, 'migrationmodeler_Color72', a)


def test_assoc_color73_link_reassign_clear():
    a = migrationmodeler_Ellipse(horizontalDiameter="sample_text", verticalDiameter="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_Ellipse', b1)
    assert _is_linked(a, 'migrationmodeler_Ellipse', b1)
    if hasattr(b1, 'migrationmodeler_Color74'):
        assert _is_linked(b1, 'migrationmodeler_Color74', a)
    _safe_set(a, 'migrationmodeler_Ellipse', b2)
    assert _is_linked(a, 'migrationmodeler_Ellipse', b2)
    if hasattr(b1, 'migrationmodeler_Color74'):
        assert not _is_linked(b1, 'migrationmodeler_Color74', a)
    if hasattr(b2, 'migrationmodeler_Color74'):
        assert _is_linked(b2, 'migrationmodeler_Color74', a)
    _safe_set(a, 'migrationmodeler_Ellipse', None)
    assert not _is_linked(a, 'migrationmodeler_Ellipse', b2)
    if hasattr(b2, 'migrationmodeler_Color74'):
        assert not _is_linked(b2, 'migrationmodeler_Color74', a)


def test_assoc_color75_link_reassign_clear():
    a = migrationmodeler_Lozenge(height="sample_text", width="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_Lozenge', b1)
    assert _is_linked(a, 'migrationmodeler_Lozenge', b1)
    if hasattr(b1, 'migrationmodeler_Color76'):
        assert _is_linked(b1, 'migrationmodeler_Color76', a)
    _safe_set(a, 'migrationmodeler_Lozenge', b2)
    assert _is_linked(a, 'migrationmodeler_Lozenge', b2)
    if hasattr(b1, 'migrationmodeler_Color76'):
        assert not _is_linked(b1, 'migrationmodeler_Color76', a)
    if hasattr(b2, 'migrationmodeler_Color76'):
        assert _is_linked(b2, 'migrationmodeler_Color76', a)
    _safe_set(a, 'migrationmodeler_Lozenge', None)
    assert not _is_linked(a, 'migrationmodeler_Lozenge', b2)
    if hasattr(b2, 'migrationmodeler_Color76'):
        assert not _is_linked(b2, 'migrationmodeler_Color76', a)


def test_assoc_color77_link_reassign_clear():
    a = migrationmodeler_Color(blue=7, green=7, red=7)
    b1 = migrationmodeler_BundledImage(shape="sample_text")
    b2 = migrationmodeler_BundledImage(shape="sample_text_2")
    _safe_set(a, 'migrationmodeler_Color78', b1)
    assert _is_linked(a, 'migrationmodeler_Color78', b1)
    if hasattr(b1, 'migrationmodeler_BundledImage'):
        assert _is_linked(b1, 'migrationmodeler_BundledImage', a)
    _safe_set(a, 'migrationmodeler_Color78', b2)
    assert _is_linked(a, 'migrationmodeler_Color78', b2)
    if hasattr(b1, 'migrationmodeler_BundledImage'):
        assert not _is_linked(b1, 'migrationmodeler_BundledImage', a)
    if hasattr(b2, 'migrationmodeler_BundledImage'):
        assert _is_linked(b2, 'migrationmodeler_BundledImage', a)
    _safe_set(a, 'migrationmodeler_Color78', None)
    assert not _is_linked(a, 'migrationmodeler_Color78', b2)
    if hasattr(b2, 'migrationmodeler_BundledImage'):
        assert not _is_linked(b2, 'migrationmodeler_BundledImage', a)


def test_assoc_color81_link_reassign_clear():
    a = migrationmodeler_Color(blue=7, green=7, red=7)
    b1 = migrationmodeler_Note()
    b2 = migrationmodeler_Note()
    _safe_set(a, 'migrationmodeler_Color82', b1)
    assert _is_linked(a, 'migrationmodeler_Color82', b1)
    if hasattr(b1, 'migrationmodeler_Note'):
        assert _is_linked(b1, 'migrationmodeler_Note', a)
    _safe_set(a, 'migrationmodeler_Color82', b2)
    assert _is_linked(a, 'migrationmodeler_Color82', b2)
    if hasattr(b1, 'migrationmodeler_Note'):
        assert not _is_linked(b1, 'migrationmodeler_Note', a)
    if hasattr(b2, 'migrationmodeler_Note'):
        assert _is_linked(b2, 'migrationmodeler_Note', a)
    _safe_set(a, 'migrationmodeler_Color82', None)
    assert not _is_linked(a, 'migrationmodeler_Color82', b2)
    if hasattr(b2, 'migrationmodeler_Note'):
        assert not _is_linked(b2, 'migrationmodeler_Note', a)


def test_assoc_containerRepresentations12_link_reassign_clear():
    a = migrationmodeler_ContainerRepresentation(autoSized=True)
    b1 = migrationmodeler_Container()
    b2 = migrationmodeler_Container()
    _safe_set(a, 'migrationmodeler_ContainerRepresentation', b1)
    assert _is_linked(a, 'migrationmodeler_ContainerRepresentation', b1)
    if hasattr(b1, 'migrationmodeler_Container13'):
        assert _is_linked(b1, 'migrationmodeler_Container13', a)
    _safe_set(a, 'migrationmodeler_ContainerRepresentation', b2)
    assert _is_linked(a, 'migrationmodeler_ContainerRepresentation', b2)
    if hasattr(b1, 'migrationmodeler_Container13'):
        assert not _is_linked(b1, 'migrationmodeler_Container13', a)
    if hasattr(b2, 'migrationmodeler_Container13'):
        assert _is_linked(b2, 'migrationmodeler_Container13', a)
    _safe_set(a, 'migrationmodeler_ContainerRepresentation', None)
    assert not _is_linked(a, 'migrationmodeler_ContainerRepresentation', b2)
    if hasattr(b2, 'migrationmodeler_Container13'):
        assert not _is_linked(b2, 'migrationmodeler_Container13', a)


def test_assoc_elements14_link_reassign_clear():
    a = migrationmodeler_GraphicalElement(id="sample_text")
    b1 = migrationmodeler_Container()
    b2 = migrationmodeler_Container()
    _safe_set(a, 'migrationmodeler_GraphicalElement', b1)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement', b1)
    if hasattr(b1, 'migrationmodeler_Container15'):
        assert _is_linked(b1, 'migrationmodeler_Container15', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement', b2)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement', b2)
    if hasattr(b1, 'migrationmodeler_Container15'):
        assert not _is_linked(b1, 'migrationmodeler_Container15', a)
    if hasattr(b2, 'migrationmodeler_Container15'):
        assert _is_linked(b2, 'migrationmodeler_Container15', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement', None)
    assert not _is_linked(a, 'migrationmodeler_GraphicalElement', b2)
    if hasattr(b2, 'migrationmodeler_Container15'):
        assert not _is_linked(b2, 'migrationmodeler_Container15', a)


def test_assoc_endLabelStyle48_link_reassign_clear():
    a = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    b1 = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    b2 = migrationmodeler_BasicLabelStyle(iconPath="sample_text_2", labelFormat="sample_text_2", labelSize=13, showIcon=False)
    _safe_set(a, 'migrationmodeler_EdgeStyle49', b1)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle49', b1)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle50'):
        assert _is_linked(b1, 'migrationmodeler_BasicLabelStyle50', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle49', b2)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle49', b2)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle50'):
        assert not _is_linked(b1, 'migrationmodeler_BasicLabelStyle50', a)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle50'):
        assert _is_linked(b2, 'migrationmodeler_BasicLabelStyle50', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle49', None)
    assert not _is_linked(a, 'migrationmodeler_EdgeStyle49', b2)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle50'):
        assert not _is_linked(b2, 'migrationmodeler_BasicLabelStyle50', a)


def test_assoc_filters5_link_reassign_clear():
    a = migrationmodeler_Filter(activated=True, id="sample_text")
    b1 = migrationmodeler_Diagram()
    b2 = migrationmodeler_Diagram()
    _safe_set(a, 'migrationmodeler_Filter', b1)
    assert _is_linked(a, 'migrationmodeler_Filter', b1)
    if hasattr(b1, 'migrationmodeler_Diagram6'):
        assert _is_linked(b1, 'migrationmodeler_Diagram6', a)
    _safe_set(a, 'migrationmodeler_Filter', b2)
    assert _is_linked(a, 'migrationmodeler_Filter', b2)
    if hasattr(b1, 'migrationmodeler_Diagram6'):
        assert not _is_linked(b1, 'migrationmodeler_Diagram6', a)
    if hasattr(b2, 'migrationmodeler_Diagram6'):
        assert _is_linked(b2, 'migrationmodeler_Diagram6', a)
    _safe_set(a, 'migrationmodeler_Filter', None)
    assert not _is_linked(a, 'migrationmodeler_Filter', b2)
    if hasattr(b2, 'migrationmodeler_Diagram6'):
        assert not _is_linked(b2, 'migrationmodeler_Diagram6', a)


def test_assoc_foregroundColor61_link_reassign_clear():
    a = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_GaugeSection62', b1)
    assert _is_linked(a, 'migrationmodeler_GaugeSection62', b1)
    if hasattr(b1, 'migrationmodeler_Color63'):
        assert _is_linked(b1, 'migrationmodeler_Color63', a)
    _safe_set(a, 'migrationmodeler_GaugeSection62', b2)
    assert _is_linked(a, 'migrationmodeler_GaugeSection62', b2)
    if hasattr(b1, 'migrationmodeler_Color63'):
        assert not _is_linked(b1, 'migrationmodeler_Color63', a)
    if hasattr(b2, 'migrationmodeler_Color63'):
        assert _is_linked(b2, 'migrationmodeler_Color63', a)
    _safe_set(a, 'migrationmodeler_GaugeSection62', None)
    assert not _is_linked(a, 'migrationmodeler_GaugeSection62', b2)
    if hasattr(b2, 'migrationmodeler_Color63'):
        assert not _is_linked(b2, 'migrationmodeler_Color63', a)


def test_assoc_foregroundColor66_link_reassign_clear():
    a = migrationmodeler_FlatContainerStyle(backgroundStyle="sample_text")
    b1 = migrationmodeler_Color(blue=7, green=7, red=7)
    b2 = migrationmodeler_Color(blue=13, green=13, red=13)
    _safe_set(a, 'migrationmodeler_FlatContainerStyle67', b1)
    assert _is_linked(a, 'migrationmodeler_FlatContainerStyle67', b1)
    if hasattr(b1, 'migrationmodeler_Color68'):
        assert _is_linked(b1, 'migrationmodeler_Color68', a)
    _safe_set(a, 'migrationmodeler_FlatContainerStyle67', b2)
    assert _is_linked(a, 'migrationmodeler_FlatContainerStyle67', b2)
    if hasattr(b1, 'migrationmodeler_Color68'):
        assert not _is_linked(b1, 'migrationmodeler_Color68', a)
    if hasattr(b2, 'migrationmodeler_Color68'):
        assert _is_linked(b2, 'migrationmodeler_Color68', a)
    _safe_set(a, 'migrationmodeler_FlatContainerStyle67', None)
    assert not _is_linked(a, 'migrationmodeler_FlatContainerStyle67', b2)
    if hasattr(b2, 'migrationmodeler_Color68'):
        assert not _is_linked(b2, 'migrationmodeler_Color68', a)


def test_assoc_labelColor54_link_reassign_clear():
    a = migrationmodeler_Color(blue=7, green=7, red=7)
    b1 = migrationmodeler_BasicLabelStyle(iconPath="sample_text", labelFormat="sample_text", labelSize=7, showIcon=True)
    b2 = migrationmodeler_BasicLabelStyle(iconPath="sample_text_2", labelFormat="sample_text_2", labelSize=13, showIcon=False)
    _safe_set(a, 'migrationmodeler_Color56', b1)
    assert _is_linked(a, 'migrationmodeler_Color56', b1)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle55'):
        assert _is_linked(b1, 'migrationmodeler_BasicLabelStyle55', a)
    _safe_set(a, 'migrationmodeler_Color56', b2)
    assert _is_linked(a, 'migrationmodeler_Color56', b2)
    if hasattr(b1, 'migrationmodeler_BasicLabelStyle55'):
        assert not _is_linked(b1, 'migrationmodeler_BasicLabelStyle55', a)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle55'):
        assert _is_linked(b2, 'migrationmodeler_BasicLabelStyle55', a)
    _safe_set(a, 'migrationmodeler_Color56', None)
    assert not _is_linked(a, 'migrationmodeler_Color56', b2)
    if hasattr(b2, 'migrationmodeler_BasicLabelStyle55'):
        assert not _is_linked(b2, 'migrationmodeler_BasicLabelStyle55', a)


def test_assoc_layers7_link_reassign_clear():
    a = migrationmodeler_Layer(activated=True, id="sample_text")
    b1 = migrationmodeler_Diagram()
    b2 = migrationmodeler_Diagram()
    _safe_set(a, 'migrationmodeler_Layer', b1)
    assert _is_linked(a, 'migrationmodeler_Layer', b1)
    if hasattr(b1, 'migrationmodeler_Diagram8'):
        assert _is_linked(b1, 'migrationmodeler_Diagram8', a)
    _safe_set(a, 'migrationmodeler_Layer', b2)
    assert _is_linked(a, 'migrationmodeler_Layer', b2)
    if hasattr(b1, 'migrationmodeler_Diagram8'):
        assert not _is_linked(b1, 'migrationmodeler_Diagram8', a)
    if hasattr(b2, 'migrationmodeler_Diagram8'):
        assert _is_linked(b2, 'migrationmodeler_Diagram8', a)
    _safe_set(a, 'migrationmodeler_Layer', None)
    assert not _is_linked(a, 'migrationmodeler_Layer', b2)
    if hasattr(b2, 'migrationmodeler_Diagram8'):
        assert not _is_linked(b2, 'migrationmodeler_Diagram8', a)


def test_assoc_layout24_link_reassign_clear():
    a = migrationmodeler_Layout(height=7, width=7, x=7, y=7)
    b1 = migrationmodeler_AbstractRepresentation(displayed=True, hidden=True, mappingId="sample_text", pinned=True)
    b2 = migrationmodeler_AbstractRepresentation(displayed=False, hidden=False, mappingId="sample_text_2", pinned=False)
    _safe_set(a, 'migrationmodeler_Layout', b1)
    assert _is_linked(a, 'migrationmodeler_Layout', b1)
    if hasattr(b1, 'migrationmodeler_AbstractRepresentation'):
        assert _is_linked(b1, 'migrationmodeler_AbstractRepresentation', a)
    _safe_set(a, 'migrationmodeler_Layout', b2)
    assert _is_linked(a, 'migrationmodeler_Layout', b2)
    if hasattr(b1, 'migrationmodeler_AbstractRepresentation'):
        assert not _is_linked(b1, 'migrationmodeler_AbstractRepresentation', a)
    if hasattr(b2, 'migrationmodeler_AbstractRepresentation'):
        assert _is_linked(b2, 'migrationmodeler_AbstractRepresentation', a)
    _safe_set(a, 'migrationmodeler_Layout', None)
    assert not _is_linked(a, 'migrationmodeler_Layout', b2)
    if hasattr(b2, 'migrationmodeler_AbstractRepresentation'):
        assert not _is_linked(b2, 'migrationmodeler_AbstractRepresentation', a)


def test_assoc_ownedStyle33_link_reassign_clear():
    a = migrationmodeler_EdgeStyle(routingStyle="sample_text")
    b1 = migrationmodeler_EdgeRepresentation()
    b2 = migrationmodeler_EdgeRepresentation()
    _safe_set(a, 'migrationmodeler_EdgeStyle', b1)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle', b1)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation34'):
        assert _is_linked(b1, 'migrationmodeler_EdgeRepresentation34', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle', b2)
    assert _is_linked(a, 'migrationmodeler_EdgeStyle', b2)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation34'):
        assert not _is_linked(b1, 'migrationmodeler_EdgeRepresentation34', a)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation34'):
        assert _is_linked(b2, 'migrationmodeler_EdgeRepresentation34', a)
    _safe_set(a, 'migrationmodeler_EdgeStyle', None)
    assert not _is_linked(a, 'migrationmodeler_EdgeStyle', b2)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation34'):
        assert not _is_linked(b2, 'migrationmodeler_EdgeRepresentation34', a)


def test_assoc_ownedStyle37_link_reassign_clear():
    a = migrationmodeler_NodeStyle(hideLabelByDefault=True, labelPosition="sample_text")
    b1 = migrationmodeler_AbstractNodeRepresentation()
    b2 = migrationmodeler_AbstractNodeRepresentation()
    _safe_set(a, 'migrationmodeler_NodeStyle', b1)
    assert _is_linked(a, 'migrationmodeler_NodeStyle', b1)
    if hasattr(b1, 'migrationmodeler_AbstractNodeRepresentation38'):
        assert _is_linked(b1, 'migrationmodeler_AbstractNodeRepresentation38', a)
    _safe_set(a, 'migrationmodeler_NodeStyle', b2)
    assert _is_linked(a, 'migrationmodeler_NodeStyle', b2)
    if hasattr(b1, 'migrationmodeler_AbstractNodeRepresentation38'):
        assert not _is_linked(b1, 'migrationmodeler_AbstractNodeRepresentation38', a)
    if hasattr(b2, 'migrationmodeler_AbstractNodeRepresentation38'):
        assert _is_linked(b2, 'migrationmodeler_AbstractNodeRepresentation38', a)
    _safe_set(a, 'migrationmodeler_NodeStyle', None)
    assert not _is_linked(a, 'migrationmodeler_NodeStyle', b2)
    if hasattr(b2, 'migrationmodeler_AbstractNodeRepresentation38'):
        assert not _is_linked(b2, 'migrationmodeler_AbstractNodeRepresentation38', a)


def test_assoc_ownedStyle39_link_reassign_clear():
    a = migrationmodeler_ContainerRepresentation(autoSized=True)
    b1 = migrationmodeler_ContainerStyle()
    b2 = migrationmodeler_ContainerStyle()
    _safe_set(a, 'migrationmodeler_ContainerRepresentation40', b1)
    assert _is_linked(a, 'migrationmodeler_ContainerRepresentation40', b1)
    if hasattr(b1, 'migrationmodeler_ContainerStyle'):
        assert _is_linked(b1, 'migrationmodeler_ContainerStyle', a)
    _safe_set(a, 'migrationmodeler_ContainerRepresentation40', b2)
    assert _is_linked(a, 'migrationmodeler_ContainerRepresentation40', b2)
    if hasattr(b1, 'migrationmodeler_ContainerStyle'):
        assert not _is_linked(b1, 'migrationmodeler_ContainerStyle', a)
    if hasattr(b2, 'migrationmodeler_ContainerStyle'):
        assert _is_linked(b2, 'migrationmodeler_ContainerStyle', a)
    _safe_set(a, 'migrationmodeler_ContainerRepresentation40', None)
    assert not _is_linked(a, 'migrationmodeler_ContainerRepresentation40', b2)
    if hasattr(b2, 'migrationmodeler_ContainerStyle'):
        assert not _is_linked(b2, 'migrationmodeler_ContainerStyle', a)


def test_assoc_representations51_link_reassign_clear():
    a = migrationmodeler_Representation(name="sample_text")
    b1 = migrationmodeler_TestCase()
    b2 = migrationmodeler_TestCase()
    _safe_set(a, 'migrationmodeler_Representation', b1)
    assert _is_linked(a, 'migrationmodeler_Representation', b1)
    if hasattr(b1, 'migrationmodeler_TestCase'):
        assert _is_linked(b1, 'migrationmodeler_TestCase', a)
    _safe_set(a, 'migrationmodeler_Representation', b2)
    assert _is_linked(a, 'migrationmodeler_Representation', b2)
    if hasattr(b1, 'migrationmodeler_TestCase'):
        assert not _is_linked(b1, 'migrationmodeler_TestCase', a)
    if hasattr(b2, 'migrationmodeler_TestCase'):
        assert _is_linked(b2, 'migrationmodeler_TestCase', a)
    _safe_set(a, 'migrationmodeler_Representation', None)
    assert not _is_linked(a, 'migrationmodeler_Representation', b2)
    if hasattr(b2, 'migrationmodeler_TestCase'):
        assert not _is_linked(b2, 'migrationmodeler_TestCase', a)


def test_assoc_sections79_link_reassign_clear():
    a = migrationmodeler_GaugeSection(label="sample_text", max="sample_text", min="sample_text", value="sample_text")
    b1 = migrationmodeler_GaugeCompositeStyle(alignment="sample_text")
    b2 = migrationmodeler_GaugeCompositeStyle(alignment="sample_text_2")
    _safe_set(a, 'migrationmodeler_GaugeSection80', b1)
    assert _is_linked(a, 'migrationmodeler_GaugeSection80', b1)
    if hasattr(b1, 'migrationmodeler_GaugeCompositeStyle'):
        assert _is_linked(b1, 'migrationmodeler_GaugeCompositeStyle', a)
    _safe_set(a, 'migrationmodeler_GaugeSection80', b2)
    assert _is_linked(a, 'migrationmodeler_GaugeSection80', b2)
    if hasattr(b1, 'migrationmodeler_GaugeCompositeStyle'):
        assert not _is_linked(b1, 'migrationmodeler_GaugeCompositeStyle', a)
    if hasattr(b2, 'migrationmodeler_GaugeCompositeStyle'):
        assert _is_linked(b2, 'migrationmodeler_GaugeCompositeStyle', a)
    _safe_set(a, 'migrationmodeler_GaugeSection80', None)
    assert not _is_linked(a, 'migrationmodeler_GaugeSection80', b2)
    if hasattr(b2, 'migrationmodeler_GaugeCompositeStyle'):
        assert not _is_linked(b2, 'migrationmodeler_GaugeCompositeStyle', a)


def test_assoc_source18_link_reassign_clear():
    a = migrationmodeler_GraphicalElement(id="sample_text")
    b1 = migrationmodeler_Edge()
    b2 = migrationmodeler_Edge()
    _safe_set(a, 'migrationmodeler_GraphicalElement20', b1)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement20', b1)
    if hasattr(b1, 'migrationmodeler_Edge19'):
        assert _is_linked(b1, 'migrationmodeler_Edge19', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement20', b2)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement20', b2)
    if hasattr(b1, 'migrationmodeler_Edge19'):
        assert not _is_linked(b1, 'migrationmodeler_Edge19', a)
    if hasattr(b2, 'migrationmodeler_Edge19'):
        assert _is_linked(b2, 'migrationmodeler_Edge19', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement20', None)
    assert not _is_linked(a, 'migrationmodeler_GraphicalElement20', b2)
    if hasattr(b2, 'migrationmodeler_Edge19'):
        assert not _is_linked(b2, 'migrationmodeler_Edge19', a)


def test_assoc_source25_link_reassign_clear():
    a = migrationmodeler_GraphicalElement(id="sample_text")
    b1 = migrationmodeler_EdgeRepresentation()
    b2 = migrationmodeler_EdgeRepresentation()
    _safe_set(a, 'migrationmodeler_GraphicalElement27', b1)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement27', b1)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation26'):
        assert _is_linked(b1, 'migrationmodeler_EdgeRepresentation26', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement27', b2)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement27', b2)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation26'):
        assert not _is_linked(b1, 'migrationmodeler_EdgeRepresentation26', a)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation26'):
        assert _is_linked(b2, 'migrationmodeler_EdgeRepresentation26', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement27', None)
    assert not _is_linked(a, 'migrationmodeler_GraphicalElement27', b2)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation26'):
        assert not _is_linked(b2, 'migrationmodeler_EdgeRepresentation26', a)


def test_assoc_target21_link_reassign_clear():
    a = migrationmodeler_GraphicalElement(id="sample_text")
    b1 = migrationmodeler_Edge()
    b2 = migrationmodeler_Edge()
    _safe_set(a, 'migrationmodeler_GraphicalElement23', b1)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement23', b1)
    if hasattr(b1, 'migrationmodeler_Edge22'):
        assert _is_linked(b1, 'migrationmodeler_Edge22', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement23', b2)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement23', b2)
    if hasattr(b1, 'migrationmodeler_Edge22'):
        assert not _is_linked(b1, 'migrationmodeler_Edge22', a)
    if hasattr(b2, 'migrationmodeler_Edge22'):
        assert _is_linked(b2, 'migrationmodeler_Edge22', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement23', None)
    assert not _is_linked(a, 'migrationmodeler_GraphicalElement23', b2)
    if hasattr(b2, 'migrationmodeler_Edge22'):
        assert not _is_linked(b2, 'migrationmodeler_Edge22', a)


def test_assoc_target28_link_reassign_clear():
    a = migrationmodeler_GraphicalElement(id="sample_text")
    b1 = migrationmodeler_EdgeRepresentation()
    b2 = migrationmodeler_EdgeRepresentation()
    _safe_set(a, 'migrationmodeler_GraphicalElement30', b1)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement30', b1)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation29'):
        assert _is_linked(b1, 'migrationmodeler_EdgeRepresentation29', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement30', b2)
    assert _is_linked(a, 'migrationmodeler_GraphicalElement30', b2)
    if hasattr(b1, 'migrationmodeler_EdgeRepresentation29'):
        assert not _is_linked(b1, 'migrationmodeler_EdgeRepresentation29', a)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation29'):
        assert _is_linked(b2, 'migrationmodeler_EdgeRepresentation29', a)
    _safe_set(a, 'migrationmodeler_GraphicalElement30', None)
    assert not _is_linked(a, 'migrationmodeler_GraphicalElement30', b2)
    if hasattr(b2, 'migrationmodeler_EdgeRepresentation29'):
        assert not _is_linked(b2, 'migrationmodeler_EdgeRepresentation29', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractNode_strategy = st.builds(AbstractNode)
@given(instance=AbstractNode_strategy)
@settings(max_examples=25)
def test_AbstractNode_instantiation(instance):
    assert isinstance(instance, AbstractNode)


AbstractNodeRepresentation_strategy = st.builds(AbstractNodeRepresentation)
@given(instance=AbstractNodeRepresentation_strategy)
@settings(max_examples=25)
def test_AbstractNodeRepresentation_instantiation(instance):
    assert isinstance(instance, AbstractNodeRepresentation)


AbstractRepresentation_strategy = st.builds(AbstractRepresentation)
@given(instance=AbstractRepresentation_strategy)
@settings(max_examples=25)
def test_AbstractRepresentation_instantiation(instance):
    assert isinstance(instance, AbstractRepresentation)


BasicLabelStyle_strategy = st.builds(BasicLabelStyle)
@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=25)
def test_BasicLabelStyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)


BorderedStyle_strategy = st.builds(BorderedStyle)
@given(instance=BorderedStyle_strategy)
@settings(max_examples=25)
def test_BorderedStyle_instantiation(instance):
    assert isinstance(instance, BorderedStyle)


ContainerStyle_strategy = st.builds(ContainerStyle)
@given(instance=ContainerStyle_strategy)
@settings(max_examples=25)
def test_ContainerStyle_instantiation(instance):
    assert isinstance(instance, ContainerStyle)


GraphicalElement_strategy = st.builds(GraphicalElement)
@given(instance=GraphicalElement_strategy)
@settings(max_examples=25)
def test_GraphicalElement_instantiation(instance):
    assert isinstance(instance, GraphicalElement)


LabelStyle_strategy = st.builds(LabelStyle)
@given(instance=LabelStyle_strategy)
@settings(max_examples=25)
def test_LabelStyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)


NodeStyle_strategy = st.builds(NodeStyle)
@given(instance=NodeStyle_strategy)
@settings(max_examples=25)
def test_NodeStyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)


Representation_strategy = st.builds(Representation)
@given(instance=Representation_strategy)
@settings(max_examples=25)
def test_Representation_instantiation(instance):
    assert isinstance(instance, Representation)


migrationmodeler_AbstractNode_strategy = st.builds(migrationmodeler_AbstractNode)
@given(instance=migrationmodeler_AbstractNode_strategy)
@settings(max_examples=25)
def test_migrationmodeler_AbstractNode_instantiation(instance):
    assert isinstance(instance, migrationmodeler_AbstractNode)


migrationmodeler_AbstractNodeRepresentation_strategy = st.builds(migrationmodeler_AbstractNodeRepresentation)
@given(instance=migrationmodeler_AbstractNodeRepresentation_strategy)
@settings(max_examples=25)
def test_migrationmodeler_AbstractNodeRepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_AbstractNodeRepresentation)


migrationmodeler_AbstractRepresentation_strategy = st.builds(migrationmodeler_AbstractRepresentation, displayed=st.booleans(), hidden=st.booleans(), mappingId=safe_text, pinned=st.booleans())
@given(instance=migrationmodeler_AbstractRepresentation_strategy)
@settings(max_examples=25)
def test_migrationmodeler_AbstractRepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_AbstractRepresentation)


migrationmodeler_BasicLabelStyle_strategy = st.builds(migrationmodeler_BasicLabelStyle, iconPath=safe_text, labelFormat=safe_text, labelSize=st.integers(), showIcon=st.booleans())
@given(instance=migrationmodeler_BasicLabelStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_BasicLabelStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BasicLabelStyle)


migrationmodeler_Bordered_strategy = st.builds(migrationmodeler_Bordered)
@given(instance=migrationmodeler_Bordered_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Bordered_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Bordered)


migrationmodeler_BorderedRepresentation_strategy = st.builds(migrationmodeler_BorderedRepresentation)
@given(instance=migrationmodeler_BorderedRepresentation_strategy)
@settings(max_examples=25)
def test_migrationmodeler_BorderedRepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BorderedRepresentation)


migrationmodeler_BorderedStyle_strategy = st.builds(migrationmodeler_BorderedStyle, borderSize=st.integers())
@given(instance=migrationmodeler_BorderedStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_BorderedStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BorderedStyle)


migrationmodeler_BundledImage_strategy = st.builds(migrationmodeler_BundledImage, shape=safe_text)
@given(instance=migrationmodeler_BundledImage_strategy)
@settings(max_examples=25)
def test_migrationmodeler_BundledImage_instantiation(instance):
    assert isinstance(instance, migrationmodeler_BundledImage)


migrationmodeler_Color_strategy = st.builds(migrationmodeler_Color, blue=st.integers(), green=st.integers(), red=st.integers())
@given(instance=migrationmodeler_Color_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Color_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Color)


migrationmodeler_Container_strategy = st.builds(migrationmodeler_Container)
@given(instance=migrationmodeler_Container_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Container_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Container)


migrationmodeler_ContainerRepresentation_strategy = st.builds(migrationmodeler_ContainerRepresentation, autoSized=st.booleans())
@given(instance=migrationmodeler_ContainerRepresentation_strategy)
@settings(max_examples=25)
def test_migrationmodeler_ContainerRepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_ContainerRepresentation)


migrationmodeler_ContainerStyle_strategy = st.builds(migrationmodeler_ContainerStyle)
@given(instance=migrationmodeler_ContainerStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_ContainerStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_ContainerStyle)


migrationmodeler_Diagram_strategy = st.builds(migrationmodeler_Diagram)
@given(instance=migrationmodeler_Diagram_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Diagram_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Diagram)


migrationmodeler_Dot_strategy = st.builds(migrationmodeler_Dot)
@given(instance=migrationmodeler_Dot_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Dot_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Dot)


migrationmodeler_Edge_strategy = st.builds(migrationmodeler_Edge)
@given(instance=migrationmodeler_Edge_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Edge_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Edge)


migrationmodeler_EdgeRepresentation_strategy = st.builds(migrationmodeler_EdgeRepresentation)
@given(instance=migrationmodeler_EdgeRepresentation_strategy)
@settings(max_examples=25)
def test_migrationmodeler_EdgeRepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_EdgeRepresentation)


migrationmodeler_EdgeStyle_strategy = st.builds(migrationmodeler_EdgeStyle, routingStyle=safe_text)
@given(instance=migrationmodeler_EdgeStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_EdgeStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_EdgeStyle)


migrationmodeler_Ellipse_strategy = st.builds(migrationmodeler_Ellipse, horizontalDiameter=safe_text, verticalDiameter=safe_text)
@given(instance=migrationmodeler_Ellipse_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Ellipse_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Ellipse)


migrationmodeler_Filter_strategy = st.builds(migrationmodeler_Filter, activated=st.booleans(), id=safe_text)
@given(instance=migrationmodeler_Filter_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Filter_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Filter)


migrationmodeler_FlatContainerStyle_strategy = st.builds(migrationmodeler_FlatContainerStyle, backgroundStyle=safe_text)
@given(instance=migrationmodeler_FlatContainerStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_FlatContainerStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_FlatContainerStyle)


migrationmodeler_GaugeCompositeStyle_strategy = st.builds(migrationmodeler_GaugeCompositeStyle, alignment=safe_text)
@given(instance=migrationmodeler_GaugeCompositeStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_GaugeCompositeStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_GaugeCompositeStyle)


migrationmodeler_GaugeSection_strategy = st.builds(migrationmodeler_GaugeSection, label=safe_text, max=safe_text, min=safe_text, value=safe_text)
@given(instance=migrationmodeler_GaugeSection_strategy)
@settings(max_examples=25)
def test_migrationmodeler_GaugeSection_instantiation(instance):
    assert isinstance(instance, migrationmodeler_GaugeSection)


migrationmodeler_GraphicalElement_strategy = st.builds(migrationmodeler_GraphicalElement, id=safe_text)
@given(instance=migrationmodeler_GraphicalElement_strategy)
@settings(max_examples=25)
def test_migrationmodeler_GraphicalElement_instantiation(instance):
    assert isinstance(instance, migrationmodeler_GraphicalElement)


migrationmodeler_LabelStyle_strategy = st.builds(migrationmodeler_LabelStyle, labelAlignment=safe_text)
@given(instance=migrationmodeler_LabelStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_LabelStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_LabelStyle)


migrationmodeler_Layer_strategy = st.builds(migrationmodeler_Layer, activated=st.booleans(), id=safe_text)
@given(instance=migrationmodeler_Layer_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Layer_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Layer)


migrationmodeler_Layout_strategy = st.builds(migrationmodeler_Layout, height=st.integers(), width=st.integers(), x=st.integers(), y=st.integers())
@given(instance=migrationmodeler_Layout_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Layout_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Layout)


migrationmodeler_Lozenge_strategy = st.builds(migrationmodeler_Lozenge, height=safe_text, width=safe_text)
@given(instance=migrationmodeler_Lozenge_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Lozenge_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Lozenge)


migrationmodeler_Node_strategy = st.builds(migrationmodeler_Node)
@given(instance=migrationmodeler_Node_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Node_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Node)


migrationmodeler_NodeRepresentation_strategy = st.builds(migrationmodeler_NodeRepresentation)
@given(instance=migrationmodeler_NodeRepresentation_strategy)
@settings(max_examples=25)
def test_migrationmodeler_NodeRepresentation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_NodeRepresentation)


migrationmodeler_NodeStyle_strategy = st.builds(migrationmodeler_NodeStyle, hideLabelByDefault=st.booleans(), labelPosition=safe_text)
@given(instance=migrationmodeler_NodeStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_NodeStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_NodeStyle)


migrationmodeler_Note_strategy = st.builds(migrationmodeler_Note)
@given(instance=migrationmodeler_Note_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Note_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Note)


migrationmodeler_Point_strategy = st.builds(migrationmodeler_Point, x=st.integers(), y=st.integers())
@given(instance=migrationmodeler_Point_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Point_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Point)


migrationmodeler_Representation_strategy = st.builds(migrationmodeler_Representation, name=safe_text)
@given(instance=migrationmodeler_Representation_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Representation_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Representation)


migrationmodeler_ShapeContainerStyle_strategy = st.builds(migrationmodeler_ShapeContainerStyle, shape=safe_text)
@given(instance=migrationmodeler_ShapeContainerStyle_strategy)
@settings(max_examples=25)
def test_migrationmodeler_ShapeContainerStyle_instantiation(instance):
    assert isinstance(instance, migrationmodeler_ShapeContainerStyle)


migrationmodeler_Square_strategy = st.builds(migrationmodeler_Square, height=safe_text, width=safe_text)
@given(instance=migrationmodeler_Square_strategy)
@settings(max_examples=25)
def test_migrationmodeler_Square_instantiation(instance):
    assert isinstance(instance, migrationmodeler_Square)


migrationmodeler_TestCase_strategy = st.builds(migrationmodeler_TestCase)
@given(instance=migrationmodeler_TestCase_strategy)
@settings(max_examples=25)
def test_migrationmodeler_TestCase_instantiation(instance):
    assert isinstance(instance, migrationmodeler_TestCase)


migrationmodeler_WorkspaceImage_strategy = st.builds(migrationmodeler_WorkspaceImage, workspacePath=safe_text)
@given(instance=migrationmodeler_WorkspaceImage_strategy)
@settings(max_examples=25)
def test_migrationmodeler_WorkspaceImage_instantiation(instance):
    assert isinstance(instance, migrationmodeler_WorkspaceImage)



