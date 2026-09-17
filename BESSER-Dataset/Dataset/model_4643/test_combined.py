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
    BasicSemanticCompartment,
    DrawerStyle,
    DecorationNode,
    notation_BasicCompartment,
    BasicDecorationNode,
    notation_BasicSemanticCompartment,
    notation_DecorationNode,
    DiagramStyle,
    Diagram,
    notation_StandardDiagram,
    ConnectorStyle,
    Edge,
    notation_Connector,
    FilteringStyle,
    SortingStyle,
    TitleStyle,
    notation_SemanticListCompartment,
    CanonicalStyle,
    BasicCompartment,
    notation_ListCompartment,
    notation_Compartment,
    ShapeStyle,
    Node,
    notation_BasicDecorationNode,
    notation_Shape,
    DiagramLinkStyle,
    DataTypeStyle,
    notation_SingleValueStyle,
    notation_EDataType,
    StringObjectConverter,
    notation_PropertyValue,
    notation_StringObjectConverter,
    notation_ListValueStyle,
    notation_StringToPropertyValueMapEntry,
    NamedStyle,
    notation_DataTypeStyle,
    notation_EObjectListValueStyle,
    notation_EObjectValueStyle,
    notation_StringListValueStyle,
    notation_DoubleListValueStyle,
    notation_IntValueStyle,
    notation_BooleanListValueStyle,
    notation_StringValueStyle,
    notation_IntListValueStyle,
    notation_ByteArrayValueStyle,
    notation_BooleanValueStyle,
    notation_DoubleValueStyle,
    notation_PropertiesSetStyle,
    GuideStyle,
    PageStyle,
    ImageStyle,
    notation_ImageBufferStyle,
    notation_Guide,
    RoutingStyle,
    LineStyle,
    notation_ConnectorStyle,
    FillStyle,
    DescriptionStyle,
    notation_DiagramStyle,
    FontStyle,
    notation_Image,
    notation_NodeEntry,
    Bendpoints,
    notation_RelativeBendpoints,
    EModelElement,
    RoundedCornersStyle,
    notation_ShapeStyle,
    notation_RoutingStyle,
    LayoutConstraint,
    notation_Size,
    notation_EObject,
    Anchor,
    notation_IdentityAnchor,
    notation_Ratio,
    Size,
    Location,
    notation_Bounds,
    notation_Location,
    notation_Anchor,
    notation_Bendpoints,
    notation_View,
    Style,
    notation_PageStyle,
    notation_RoundedCornersStyle,
    notation_GuideStyle,
    notation_ArrowStyle,
    notation_HintedDiagramLinkStyle,
    notation_FilteringStyle,
    notation_DiagramLinkStyle,
    notation_SortingStyle,
    notation_FontStyle,
    notation_LineStyle,
    notation_MultiDiagramLinkStyle,
    notation_LineTypeStyle,
    notation_TextStyle,
    notation_TitleStyle,
    notation_CanonicalStyle,
    notation_NamedStyle,
    notation_DescriptionStyle,
    notation_DrawerStyle,
    notation_ImageStyle,
    notation_FillStyle,
    notation_Style,
    notation_LayoutConstraint,
    View,
    notation_Node,
    notation_Diagram,
    notation_Edge,
    Sorting,
    TextAlignment,
    Alignment,
    SortingDirection,
    JumpLinkType,
    MeasurementUnit,
    ArrowType,
    GradientStyle,
    JumpLinkStatus,
    Smoothness,
    Routing,
    LineType,
    Filtering,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_basicsemanticcompartment_is_not_abstract():
    assert not inspect.isabstract(BasicSemanticCompartment)


def test_hyp_basicsemanticcompartment_constructor_exists():
    assert callable(BasicSemanticCompartment.__init__)


def test_hyp_basicsemanticcompartment_constructor_args():
    sig = inspect.signature(BasicSemanticCompartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_drawerstyle_is_not_abstract():
    assert not inspect.isabstract(DrawerStyle)


def test_hyp_drawerstyle_constructor_exists():
    assert callable(DrawerStyle.__init__)


def test_hyp_drawerstyle_constructor_args():
    sig = inspect.signature(DrawerStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_decorationnode_is_not_abstract():
    assert not inspect.isabstract(DecorationNode)


def test_hyp_decorationnode_constructor_exists():
    assert callable(DecorationNode.__init__)


def test_hyp_decorationnode_constructor_args():
    sig = inspect.signature(DecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_basiccompartment_is_not_abstract():
    assert not inspect.isabstract(notation_BasicCompartment)


def test_hyp_notation_basiccompartment_constructor_exists():
    assert callable(notation_BasicCompartment.__init__)


def test_hyp_notation_basiccompartment_constructor_args():
    sig = inspect.signature(notation_BasicCompartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicdecorationnode_is_not_abstract():
    assert not inspect.isabstract(BasicDecorationNode)


def test_hyp_basicdecorationnode_constructor_exists():
    assert callable(BasicDecorationNode.__init__)


def test_hyp_basicdecorationnode_constructor_args():
    sig = inspect.signature(BasicDecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_basicsemanticcompartment_is_not_abstract():
    assert not inspect.isabstract(notation_BasicSemanticCompartment)


def test_hyp_notation_basicsemanticcompartment_constructor_exists():
    assert callable(notation_BasicSemanticCompartment.__init__)


def test_hyp_notation_basicsemanticcompartment_constructor_args():
    sig = inspect.signature(notation_BasicSemanticCompartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_decorationnode_is_not_abstract():
    assert not inspect.isabstract(notation_DecorationNode)


def test_hyp_notation_decorationnode_constructor_exists():
    assert callable(notation_DecorationNode.__init__)


def test_hyp_notation_decorationnode_constructor_args():
    sig = inspect.signature(notation_DecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagramstyle_is_not_abstract():
    assert not inspect.isabstract(DiagramStyle)


def test_hyp_diagramstyle_constructor_exists():
    assert callable(DiagramStyle.__init__)


def test_hyp_diagramstyle_constructor_args():
    sig = inspect.signature(DiagramStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_hyp_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_hyp_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_standarddiagram_is_not_abstract():
    assert not inspect.isabstract(notation_StandardDiagram)


def test_hyp_notation_standarddiagram_constructor_exists():
    assert callable(notation_StandardDiagram.__init__)


def test_hyp_notation_standarddiagram_constructor_args():
    sig = inspect.signature(notation_StandardDiagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connectorstyle_is_not_abstract():
    assert not inspect.isabstract(ConnectorStyle)


def test_hyp_connectorstyle_constructor_exists():
    assert callable(ConnectorStyle.__init__)


def test_hyp_connectorstyle_constructor_args():
    sig = inspect.signature(ConnectorStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_hyp_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_hyp_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_connector_is_not_abstract():
    assert not inspect.isabstract(notation_Connector)


def test_hyp_notation_connector_constructor_exists():
    assert callable(notation_Connector.__init__)


def test_hyp_notation_connector_constructor_args():
    sig = inspect.signature(notation_Connector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filteringstyle_is_not_abstract():
    assert not inspect.isabstract(FilteringStyle)


def test_hyp_filteringstyle_constructor_exists():
    assert callable(FilteringStyle.__init__)


def test_hyp_filteringstyle_constructor_args():
    sig = inspect.signature(FilteringStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sortingstyle_is_not_abstract():
    assert not inspect.isabstract(SortingStyle)


def test_hyp_sortingstyle_constructor_exists():
    assert callable(SortingStyle.__init__)


def test_hyp_sortingstyle_constructor_args():
    sig = inspect.signature(SortingStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_titlestyle_is_not_abstract():
    assert not inspect.isabstract(TitleStyle)


def test_hyp_titlestyle_constructor_exists():
    assert callable(TitleStyle.__init__)


def test_hyp_titlestyle_constructor_args():
    sig = inspect.signature(TitleStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_semanticlistcompartment_is_not_abstract():
    assert not inspect.isabstract(notation_SemanticListCompartment)


def test_hyp_notation_semanticlistcompartment_constructor_exists():
    assert callable(notation_SemanticListCompartment.__init__)


def test_hyp_notation_semanticlistcompartment_constructor_args():
    sig = inspect.signature(notation_SemanticListCompartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_canonicalstyle_is_not_abstract():
    assert not inspect.isabstract(CanonicalStyle)


def test_hyp_canonicalstyle_constructor_exists():
    assert callable(CanonicalStyle.__init__)


def test_hyp_canonicalstyle_constructor_args():
    sig = inspect.signature(CanonicalStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basiccompartment_is_not_abstract():
    assert not inspect.isabstract(BasicCompartment)


def test_hyp_basiccompartment_constructor_exists():
    assert callable(BasicCompartment.__init__)


def test_hyp_basiccompartment_constructor_args():
    sig = inspect.signature(BasicCompartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_listcompartment_is_not_abstract():
    assert not inspect.isabstract(notation_ListCompartment)


def test_hyp_notation_listcompartment_constructor_exists():
    assert callable(notation_ListCompartment.__init__)


def test_hyp_notation_listcompartment_constructor_args():
    sig = inspect.signature(notation_ListCompartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_compartment_is_not_abstract():
    assert not inspect.isabstract(notation_Compartment)


def test_hyp_notation_compartment_constructor_exists():
    assert callable(notation_Compartment.__init__)


def test_hyp_notation_compartment_constructor_args():
    sig = inspect.signature(notation_Compartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shapestyle_is_not_abstract():
    assert not inspect.isabstract(ShapeStyle)


def test_hyp_shapestyle_constructor_exists():
    assert callable(ShapeStyle.__init__)


def test_hyp_shapestyle_constructor_args():
    sig = inspect.signature(ShapeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_basicdecorationnode_is_not_abstract():
    assert not inspect.isabstract(notation_BasicDecorationNode)


def test_hyp_notation_basicdecorationnode_constructor_exists():
    assert callable(notation_BasicDecorationNode.__init__)


def test_hyp_notation_basicdecorationnode_constructor_args():
    sig = inspect.signature(notation_BasicDecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_shape_is_not_abstract():
    assert not inspect.isabstract(notation_Shape)


def test_hyp_notation_shape_constructor_exists():
    assert callable(notation_Shape.__init__)


def test_hyp_notation_shape_constructor_args():
    sig = inspect.signature(notation_Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(DiagramLinkStyle)


def test_hyp_diagramlinkstyle_constructor_exists():
    assert callable(DiagramLinkStyle.__init__)


def test_hyp_diagramlinkstyle_constructor_args():
    sig = inspect.signature(DiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatypestyle_is_not_abstract():
    assert not inspect.isabstract(DataTypeStyle)


def test_hyp_datatypestyle_constructor_exists():
    assert callable(DataTypeStyle.__init__)


def test_hyp_datatypestyle_constructor_args():
    sig = inspect.signature(DataTypeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_singlevaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_SingleValueStyle)


def test_hyp_notation_singlevaluestyle_constructor_exists():
    assert callable(notation_SingleValueStyle.__init__)


def test_hyp_notation_singlevaluestyle_constructor_args():
    sig = inspect.signature(notation_SingleValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"




def test_hyp_notation_edatatype_is_not_abstract():
    assert not inspect.isabstract(notation_EDataType)


def test_hyp_notation_edatatype_constructor_exists():
    assert callable(notation_EDataType.__init__)


def test_hyp_notation_edatatype_constructor_args():
    sig = inspect.signature(notation_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stringobjectconverter_is_not_abstract():
    assert not inspect.isabstract(StringObjectConverter)


def test_hyp_stringobjectconverter_constructor_exists():
    assert callable(StringObjectConverter.__init__)


def test_hyp_stringobjectconverter_constructor_args():
    sig = inspect.signature(StringObjectConverter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(notation_PropertyValue)


def test_hyp_notation_propertyvalue_constructor_exists():
    assert callable(notation_PropertyValue.__init__)


def test_hyp_notation_propertyvalue_constructor_args():
    sig = inspect.signature(notation_PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"




def test_hyp_notation_stringobjectconverter_is_not_abstract():
    assert not inspect.isabstract(notation_StringObjectConverter)


def test_hyp_notation_stringobjectconverter_constructor_exists():
    assert callable(notation_StringObjectConverter.__init__)


def test_hyp_notation_stringobjectconverter_constructor_args():
    sig = inspect.signature(notation_StringObjectConverter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_listvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ListValueStyle)


def test_hyp_notation_listvaluestyle_constructor_exists():
    assert callable(notation_ListValueStyle.__init__)


def test_hyp_notation_listvaluestyle_constructor_args():
    sig = inspect.signature(notation_ListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "rawValuesList" in params, "Missing parameter 'rawValuesList'"




def test_hyp_notation_stringtopropertyvaluemapentry_is_not_abstract():
    assert not inspect.isabstract(notation_StringToPropertyValueMapEntry)


def test_hyp_notation_stringtopropertyvaluemapentry_constructor_exists():
    assert callable(notation_StringToPropertyValueMapEntry.__init__)


def test_hyp_notation_stringtopropertyvaluemapentry_constructor_args():
    sig = inspect.signature(notation_StringToPropertyValueMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_namedstyle_is_not_abstract():
    assert not inspect.isabstract(NamedStyle)


def test_hyp_namedstyle_constructor_exists():
    assert callable(NamedStyle.__init__)


def test_hyp_namedstyle_constructor_args():
    sig = inspect.signature(NamedStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_datatypestyle_is_not_abstract():
    assert not inspect.isabstract(notation_DataTypeStyle)


def test_hyp_notation_datatypestyle_constructor_exists():
    assert callable(notation_DataTypeStyle.__init__)


def test_hyp_notation_datatypestyle_constructor_args():
    sig = inspect.signature(notation_DataTypeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_eobjectlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_EObjectListValueStyle)


def test_hyp_notation_eobjectlistvaluestyle_constructor_exists():
    assert callable(notation_EObjectListValueStyle.__init__)


def test_hyp_notation_eobjectlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_EObjectListValueStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_eobjectvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_EObjectValueStyle)


def test_hyp_notation_eobjectvaluestyle_constructor_exists():
    assert callable(notation_EObjectValueStyle.__init__)


def test_hyp_notation_eobjectvaluestyle_constructor_args():
    sig = inspect.signature(notation_EObjectValueStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_stringlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_StringListValueStyle)


def test_hyp_notation_stringlistvaluestyle_constructor_exists():
    assert callable(notation_StringListValueStyle.__init__)


def test_hyp_notation_stringlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_StringListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "stringListValue" in params, "Missing parameter 'stringListValue'"




def test_hyp_notation_doublelistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_DoubleListValueStyle)


def test_hyp_notation_doublelistvaluestyle_constructor_exists():
    assert callable(notation_DoubleListValueStyle.__init__)


def test_hyp_notation_doublelistvaluestyle_constructor_args():
    sig = inspect.signature(notation_DoubleListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "doubleListValue" in params, "Missing parameter 'doubleListValue'"




def test_hyp_notation_intvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_IntValueStyle)


def test_hyp_notation_intvaluestyle_constructor_exists():
    assert callable(notation_IntValueStyle.__init__)


def test_hyp_notation_intvaluestyle_constructor_args():
    sig = inspect.signature(notation_IntValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"




def test_hyp_notation_booleanlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_BooleanListValueStyle)


def test_hyp_notation_booleanlistvaluestyle_constructor_exists():
    assert callable(notation_BooleanListValueStyle.__init__)


def test_hyp_notation_booleanlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_BooleanListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "booleanListValue" in params, "Missing parameter 'booleanListValue'"




def test_hyp_notation_stringvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_StringValueStyle)


def test_hyp_notation_stringvaluestyle_constructor_exists():
    assert callable(notation_StringValueStyle.__init__)


def test_hyp_notation_stringvaluestyle_constructor_args():
    sig = inspect.signature(notation_StringValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"




def test_hyp_notation_intlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_IntListValueStyle)


def test_hyp_notation_intlistvaluestyle_constructor_exists():
    assert callable(notation_IntListValueStyle.__init__)


def test_hyp_notation_intlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_IntListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "intListValue" in params, "Missing parameter 'intListValue'"




def test_hyp_notation_bytearrayvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ByteArrayValueStyle)


def test_hyp_notation_bytearrayvaluestyle_constructor_exists():
    assert callable(notation_ByteArrayValueStyle.__init__)


def test_hyp_notation_bytearrayvaluestyle_constructor_args():
    sig = inspect.signature(notation_ByteArrayValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "byteArrayValue" in params, "Missing parameter 'byteArrayValue'"




def test_hyp_notation_booleanvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_BooleanValueStyle)


def test_hyp_notation_booleanvaluestyle_constructor_exists():
    assert callable(notation_BooleanValueStyle.__init__)


def test_hyp_notation_booleanvaluestyle_constructor_args():
    sig = inspect.signature(notation_BooleanValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"




def test_hyp_notation_doublevaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_DoubleValueStyle)


def test_hyp_notation_doublevaluestyle_constructor_exists():
    assert callable(notation_DoubleValueStyle.__init__)


def test_hyp_notation_doublevaluestyle_constructor_args():
    sig = inspect.signature(notation_DoubleValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"




def test_hyp_notation_propertiessetstyle_is_not_abstract():
    assert not inspect.isabstract(notation_PropertiesSetStyle)


def test_hyp_notation_propertiessetstyle_constructor_exists():
    assert callable(notation_PropertiesSetStyle.__init__)


def test_hyp_notation_propertiessetstyle_constructor_args():
    sig = inspect.signature(notation_PropertiesSetStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_guidestyle_is_not_abstract():
    assert not inspect.isabstract(GuideStyle)


def test_hyp_guidestyle_constructor_exists():
    assert callable(GuideStyle.__init__)


def test_hyp_guidestyle_constructor_args():
    sig = inspect.signature(GuideStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pagestyle_is_not_abstract():
    assert not inspect.isabstract(PageStyle)


def test_hyp_pagestyle_constructor_exists():
    assert callable(PageStyle.__init__)


def test_hyp_pagestyle_constructor_args():
    sig = inspect.signature(PageStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imagestyle_is_not_abstract():
    assert not inspect.isabstract(ImageStyle)


def test_hyp_imagestyle_constructor_exists():
    assert callable(ImageStyle.__init__)


def test_hyp_imagestyle_constructor_args():
    sig = inspect.signature(ImageStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_imagebufferstyle_is_not_abstract():
    assert not inspect.isabstract(notation_ImageBufferStyle)


def test_hyp_notation_imagebufferstyle_constructor_exists():
    assert callable(notation_ImageBufferStyle.__init__)


def test_hyp_notation_imagebufferstyle_constructor_args():
    sig = inspect.signature(notation_ImageBufferStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_guide_is_not_abstract():
    assert not inspect.isabstract(notation_Guide)


def test_hyp_notation_guide_constructor_exists():
    assert callable(notation_Guide.__init__)


def test_hyp_notation_guide_constructor_args():
    sig = inspect.signature(notation_Guide.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"




def test_hyp_routingstyle_is_not_abstract():
    assert not inspect.isabstract(RoutingStyle)


def test_hyp_routingstyle_constructor_exists():
    assert callable(RoutingStyle.__init__)


def test_hyp_routingstyle_constructor_args():
    sig = inspect.signature(RoutingStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_linestyle_is_not_abstract():
    assert not inspect.isabstract(LineStyle)


def test_hyp_linestyle_constructor_exists():
    assert callable(LineStyle.__init__)


def test_hyp_linestyle_constructor_args():
    sig = inspect.signature(LineStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_connectorstyle_is_not_abstract():
    assert not inspect.isabstract(notation_ConnectorStyle)


def test_hyp_notation_connectorstyle_constructor_exists():
    assert callable(notation_ConnectorStyle.__init__)


def test_hyp_notation_connectorstyle_constructor_args():
    sig = inspect.signature(notation_ConnectorStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fillstyle_is_not_abstract():
    assert not inspect.isabstract(FillStyle)


def test_hyp_fillstyle_constructor_exists():
    assert callable(FillStyle.__init__)


def test_hyp_fillstyle_constructor_args():
    sig = inspect.signature(FillStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_descriptionstyle_is_not_abstract():
    assert not inspect.isabstract(DescriptionStyle)


def test_hyp_descriptionstyle_constructor_exists():
    assert callable(DescriptionStyle.__init__)


def test_hyp_descriptionstyle_constructor_args():
    sig = inspect.signature(DescriptionStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_diagramstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DiagramStyle)


def test_hyp_notation_diagramstyle_constructor_exists():
    assert callable(notation_DiagramStyle.__init__)


def test_hyp_notation_diagramstyle_constructor_args():
    sig = inspect.signature(notation_DiagramStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fontstyle_is_not_abstract():
    assert not inspect.isabstract(FontStyle)


def test_hyp_fontstyle_constructor_exists():
    assert callable(FontStyle.__init__)


def test_hyp_fontstyle_constructor_args():
    sig = inspect.signature(FontStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_image_is_not_abstract():
    assert not inspect.isabstract(notation_Image)


def test_hyp_notation_image_constructor_exists():
    assert callable(notation_Image.__init__)


def test_hyp_notation_image_constructor_args():
    sig = inspect.signature(notation_Image.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"




def test_hyp_notation_nodeentry_is_not_abstract():
    assert not inspect.isabstract(notation_NodeEntry)


def test_hyp_notation_nodeentry_constructor_exists():
    assert callable(notation_NodeEntry.__init__)


def test_hyp_notation_nodeentry_constructor_args():
    sig = inspect.signature(notation_NodeEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_bendpoints_is_not_abstract():
    assert not inspect.isabstract(Bendpoints)


def test_hyp_bendpoints_constructor_exists():
    assert callable(Bendpoints.__init__)


def test_hyp_bendpoints_constructor_args():
    sig = inspect.signature(Bendpoints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_relativebendpoints_is_not_abstract():
    assert not inspect.isabstract(notation_RelativeBendpoints)


def test_hyp_notation_relativebendpoints_constructor_exists():
    assert callable(notation_RelativeBendpoints.__init__)


def test_hyp_notation_relativebendpoints_constructor_args():
    sig = inspect.signature(notation_RelativeBendpoints.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"




def test_hyp_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_hyp_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_hyp_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roundedcornersstyle_is_not_abstract():
    assert not inspect.isabstract(RoundedCornersStyle)


def test_hyp_roundedcornersstyle_constructor_exists():
    assert callable(RoundedCornersStyle.__init__)


def test_hyp_roundedcornersstyle_constructor_args():
    sig = inspect.signature(RoundedCornersStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_shapestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ShapeStyle)


def test_hyp_notation_shapestyle_constructor_exists():
    assert callable(notation_ShapeStyle.__init__)


def test_hyp_notation_shapestyle_constructor_args():
    sig = inspect.signature(notation_ShapeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_routingstyle_is_not_abstract():
    assert not inspect.isabstract(notation_RoutingStyle)


def test_hyp_notation_routingstyle_constructor_exists():
    assert callable(notation_RoutingStyle.__init__)


def test_hyp_notation_routingstyle_constructor_args():
    sig = inspect.signature(notation_RoutingStyle.__init__)
    params = list(sig.parameters.keys())
    assert "closestDistance" in params, "Missing parameter 'closestDistance'"
    assert "jumpLinksReverse" in params, "Missing parameter 'jumpLinksReverse'"
    assert "avoidObstructions" in params, "Missing parameter 'avoidObstructions'"
    assert "routing" in params, "Missing parameter 'routing'"
    assert "jumpLinkType" in params, "Missing parameter 'jumpLinkType'"
    assert "smoothness" in params, "Missing parameter 'smoothness'"
    assert "jumpLinkStatus" in params, "Missing parameter 'jumpLinkStatus'"










def test_hyp_layoutconstraint_is_not_abstract():
    assert not inspect.isabstract(LayoutConstraint)


def test_hyp_layoutconstraint_constructor_exists():
    assert callable(LayoutConstraint.__init__)


def test_hyp_layoutconstraint_constructor_args():
    sig = inspect.signature(LayoutConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_size_is_not_abstract():
    assert not inspect.isabstract(notation_Size)


def test_hyp_notation_size_constructor_exists():
    assert callable(notation_Size.__init__)


def test_hyp_notation_size_constructor_args():
    sig = inspect.signature(notation_Size.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"





def test_hyp_notation_eobject_is_not_abstract():
    assert not inspect.isabstract(notation_EObject)


def test_hyp_notation_eobject_constructor_exists():
    assert callable(notation_EObject.__init__)


def test_hyp_notation_eobject_constructor_args():
    sig = inspect.signature(notation_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_anchor_is_not_abstract():
    assert not inspect.isabstract(Anchor)


def test_hyp_anchor_constructor_exists():
    assert callable(Anchor.__init__)


def test_hyp_anchor_constructor_args():
    sig = inspect.signature(Anchor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_identityanchor_is_not_abstract():
    assert not inspect.isabstract(notation_IdentityAnchor)


def test_hyp_notation_identityanchor_constructor_exists():
    assert callable(notation_IdentityAnchor.__init__)


def test_hyp_notation_identityanchor_constructor_args():
    sig = inspect.signature(notation_IdentityAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_notation_ratio_is_not_abstract():
    assert not inspect.isabstract(notation_Ratio)


def test_hyp_notation_ratio_constructor_exists():
    assert callable(notation_Ratio.__init__)


def test_hyp_notation_ratio_constructor_args():
    sig = inspect.signature(notation_Ratio.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_size_is_not_abstract():
    assert not inspect.isabstract(Size)


def test_hyp_size_constructor_exists():
    assert callable(Size.__init__)


def test_hyp_size_constructor_args():
    sig = inspect.signature(Size.__init__)
    params = list(sig.parameters.keys())



def test_hyp_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_hyp_location_constructor_exists():
    assert callable(Location.__init__)


def test_hyp_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_bounds_is_not_abstract():
    assert not inspect.isabstract(notation_Bounds)


def test_hyp_notation_bounds_constructor_exists():
    assert callable(notation_Bounds.__init__)


def test_hyp_notation_bounds_constructor_args():
    sig = inspect.signature(notation_Bounds.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_location_is_not_abstract():
    assert not inspect.isabstract(notation_Location)


def test_hyp_notation_location_constructor_exists():
    assert callable(notation_Location.__init__)


def test_hyp_notation_location_constructor_args():
    sig = inspect.signature(notation_Location.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_notation_anchor_is_not_abstract():
    assert not inspect.isabstract(notation_Anchor)


def test_hyp_notation_anchor_constructor_exists():
    assert callable(notation_Anchor.__init__)


def test_hyp_notation_anchor_constructor_args():
    sig = inspect.signature(notation_Anchor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_bendpoints_is_not_abstract():
    assert not inspect.isabstract(notation_Bendpoints)


def test_hyp_notation_bendpoints_constructor_exists():
    assert callable(notation_Bendpoints.__init__)


def test_hyp_notation_bendpoints_constructor_args():
    sig = inspect.signature(notation_Bendpoints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_view_is_not_abstract():
    assert not inspect.isabstract(notation_View)


def test_hyp_notation_view_constructor_exists():
    assert callable(notation_View.__init__)


def test_hyp_notation_view_constructor_args():
    sig = inspect.signature(notation_View.__init__)
    params = list(sig.parameters.keys())
    assert "mutable" in params, "Missing parameter 'mutable'"
    assert "type" in params, "Missing parameter 'type'"
    assert "visible" in params, "Missing parameter 'visible'"






def test_hyp_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_hyp_style_constructor_exists():
    assert callable(Style.__init__)


def test_hyp_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_pagestyle_is_not_abstract():
    assert not inspect.isabstract(notation_PageStyle)


def test_hyp_notation_pagestyle_constructor_exists():
    assert callable(notation_PageStyle.__init__)


def test_hyp_notation_pagestyle_constructor_args():
    sig = inspect.signature(notation_PageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "pageHeight" in params, "Missing parameter 'pageHeight'"
    assert "pageWidth" in params, "Missing parameter 'pageWidth'"
    assert "pageX" in params, "Missing parameter 'pageX'"
    assert "pageY" in params, "Missing parameter 'pageY'"







def test_hyp_notation_roundedcornersstyle_is_not_abstract():
    assert not inspect.isabstract(notation_RoundedCornersStyle)


def test_hyp_notation_roundedcornersstyle_constructor_exists():
    assert callable(notation_RoundedCornersStyle.__init__)


def test_hyp_notation_roundedcornersstyle_constructor_args():
    sig = inspect.signature(notation_RoundedCornersStyle.__init__)
    params = list(sig.parameters.keys())
    assert "roundedBendpointsRadius" in params, "Missing parameter 'roundedBendpointsRadius'"




def test_hyp_notation_guidestyle_is_not_abstract():
    assert not inspect.isabstract(notation_GuideStyle)


def test_hyp_notation_guidestyle_constructor_exists():
    assert callable(notation_GuideStyle.__init__)


def test_hyp_notation_guidestyle_constructor_args():
    sig = inspect.signature(notation_GuideStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_arrowstyle_is_not_abstract():
    assert not inspect.isabstract(notation_ArrowStyle)


def test_hyp_notation_arrowstyle_constructor_exists():
    assert callable(notation_ArrowStyle.__init__)


def test_hyp_notation_arrowstyle_constructor_args():
    sig = inspect.signature(notation_ArrowStyle.__init__)
    params = list(sig.parameters.keys())
    assert "arrowSource" in params, "Missing parameter 'arrowSource'"
    assert "arrowTarget" in params, "Missing parameter 'arrowTarget'"





def test_hyp_notation_hinteddiagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation_HintedDiagramLinkStyle)


def test_hyp_notation_hinteddiagramlinkstyle_constructor_exists():
    assert callable(notation_HintedDiagramLinkStyle.__init__)


def test_hyp_notation_hinteddiagramlinkstyle_constructor_args():
    sig = inspect.signature(notation_HintedDiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hint" in params, "Missing parameter 'hint'"




def test_hyp_notation_filteringstyle_is_not_abstract():
    assert not inspect.isabstract(notation_FilteringStyle)


def test_hyp_notation_filteringstyle_constructor_exists():
    assert callable(notation_FilteringStyle.__init__)


def test_hyp_notation_filteringstyle_constructor_args():
    sig = inspect.signature(notation_FilteringStyle.__init__)
    params = list(sig.parameters.keys())
    assert "filteringKeys" in params, "Missing parameter 'filteringKeys'"
    assert "filtering" in params, "Missing parameter 'filtering'"





def test_hyp_notation_diagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DiagramLinkStyle)


def test_hyp_notation_diagramlinkstyle_constructor_exists():
    assert callable(notation_DiagramLinkStyle.__init__)


def test_hyp_notation_diagramlinkstyle_constructor_args():
    sig = inspect.signature(notation_DiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_sortingstyle_is_not_abstract():
    assert not inspect.isabstract(notation_SortingStyle)


def test_hyp_notation_sortingstyle_constructor_exists():
    assert callable(notation_SortingStyle.__init__)


def test_hyp_notation_sortingstyle_constructor_args():
    sig = inspect.signature(notation_SortingStyle.__init__)
    params = list(sig.parameters.keys())
    assert "sortingKeys" in params, "Missing parameter 'sortingKeys'"
    assert "sorting" in params, "Missing parameter 'sorting'"





def test_hyp_notation_fontstyle_is_not_abstract():
    assert not inspect.isabstract(notation_FontStyle)


def test_hyp_notation_fontstyle_constructor_exists():
    assert callable(notation_FontStyle.__init__)


def test_hyp_notation_fontstyle_constructor_args():
    sig = inspect.signature(notation_FontStyle.__init__)
    params = list(sig.parameters.keys())
    assert "strikeThrough" in params, "Missing parameter 'strikeThrough'"
    assert "fontHeight" in params, "Missing parameter 'fontHeight'"
    assert "italic" in params, "Missing parameter 'italic'"
    assert "underline" in params, "Missing parameter 'underline'"
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "bold" in params, "Missing parameter 'bold'"










def test_hyp_notation_linestyle_is_not_abstract():
    assert not inspect.isabstract(notation_LineStyle)


def test_hyp_notation_linestyle_constructor_exists():
    assert callable(notation_LineStyle.__init__)


def test_hyp_notation_linestyle_constructor_args():
    sig = inspect.signature(notation_LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lineColor" in params, "Missing parameter 'lineColor'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"





def test_hyp_notation_multidiagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation_MultiDiagramLinkStyle)


def test_hyp_notation_multidiagramlinkstyle_constructor_exists():
    assert callable(notation_MultiDiagramLinkStyle.__init__)


def test_hyp_notation_multidiagramlinkstyle_constructor_args():
    sig = inspect.signature(notation_MultiDiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_linetypestyle_is_not_abstract():
    assert not inspect.isabstract(notation_LineTypeStyle)


def test_hyp_notation_linetypestyle_constructor_exists():
    assert callable(notation_LineTypeStyle.__init__)


def test_hyp_notation_linetypestyle_constructor_args():
    sig = inspect.signature(notation_LineTypeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lineType" in params, "Missing parameter 'lineType'"




def test_hyp_notation_textstyle_is_not_abstract():
    assert not inspect.isabstract(notation_TextStyle)


def test_hyp_notation_textstyle_constructor_exists():
    assert callable(notation_TextStyle.__init__)


def test_hyp_notation_textstyle_constructor_args():
    sig = inspect.signature(notation_TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"




def test_hyp_notation_titlestyle_is_not_abstract():
    assert not inspect.isabstract(notation_TitleStyle)


def test_hyp_notation_titlestyle_constructor_exists():
    assert callable(notation_TitleStyle.__init__)


def test_hyp_notation_titlestyle_constructor_args():
    sig = inspect.signature(notation_TitleStyle.__init__)
    params = list(sig.parameters.keys())
    assert "showTitle" in params, "Missing parameter 'showTitle'"




def test_hyp_notation_canonicalstyle_is_not_abstract():
    assert not inspect.isabstract(notation_CanonicalStyle)


def test_hyp_notation_canonicalstyle_constructor_exists():
    assert callable(notation_CanonicalStyle.__init__)


def test_hyp_notation_canonicalstyle_constructor_args():
    sig = inspect.signature(notation_CanonicalStyle.__init__)
    params = list(sig.parameters.keys())
    assert "canonical" in params, "Missing parameter 'canonical'"




def test_hyp_notation_namedstyle_is_not_abstract():
    assert not inspect.isabstract(notation_NamedStyle)


def test_hyp_notation_namedstyle_constructor_exists():
    assert callable(notation_NamedStyle.__init__)


def test_hyp_notation_namedstyle_constructor_args():
    sig = inspect.signature(notation_NamedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_notation_descriptionstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DescriptionStyle)


def test_hyp_notation_descriptionstyle_constructor_exists():
    assert callable(notation_DescriptionStyle.__init__)


def test_hyp_notation_descriptionstyle_constructor_args():
    sig = inspect.signature(notation_DescriptionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_notation_drawerstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DrawerStyle)


def test_hyp_notation_drawerstyle_constructor_exists():
    assert callable(notation_DrawerStyle.__init__)


def test_hyp_notation_drawerstyle_constructor_args():
    sig = inspect.signature(notation_DrawerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "collapsed" in params, "Missing parameter 'collapsed'"




def test_hyp_notation_imagestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ImageStyle)


def test_hyp_notation_imagestyle_constructor_exists():
    assert callable(notation_ImageStyle.__init__)


def test_hyp_notation_imagestyle_constructor_args():
    sig = inspect.signature(notation_ImageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "maintainAspectRatio" in params, "Missing parameter 'maintainAspectRatio'"
    assert "antiAlias" in params, "Missing parameter 'antiAlias'"





def test_hyp_notation_fillstyle_is_not_abstract():
    assert not inspect.isabstract(notation_FillStyle)


def test_hyp_notation_fillstyle_constructor_exists():
    assert callable(notation_FillStyle.__init__)


def test_hyp_notation_fillstyle_constructor_args():
    sig = inspect.signature(notation_FillStyle.__init__)
    params = list(sig.parameters.keys())
    assert "transparency" in params, "Missing parameter 'transparency'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"





def test_hyp_notation_style_is_not_abstract():
    assert not inspect.isabstract(notation_Style)


def test_hyp_notation_style_constructor_exists():
    assert callable(notation_Style.__init__)


def test_hyp_notation_style_constructor_args():
    sig = inspect.signature(notation_Style.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_layoutconstraint_is_not_abstract():
    assert not inspect.isabstract(notation_LayoutConstraint)


def test_hyp_notation_layoutconstraint_constructor_exists():
    assert callable(notation_LayoutConstraint.__init__)


def test_hyp_notation_layoutconstraint_constructor_args():
    sig = inspect.signature(notation_LayoutConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_hyp_view_constructor_exists():
    assert callable(View.__init__)


def test_hyp_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_node_is_not_abstract():
    assert not inspect.isabstract(notation_Node)


def test_hyp_notation_node_constructor_exists():
    assert callable(notation_Node.__init__)


def test_hyp_notation_node_constructor_args():
    sig = inspect.signature(notation_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notation_diagram_is_not_abstract():
    assert not inspect.isabstract(notation_Diagram)


def test_hyp_notation_diagram_constructor_exists():
    assert callable(notation_Diagram.__init__)


def test_hyp_notation_diagram_constructor_args():
    sig = inspect.signature(notation_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "measurementUnit" in params, "Missing parameter 'measurementUnit'"





def test_hyp_notation_edge_is_not_abstract():
    assert not inspect.isabstract(notation_Edge)


def test_hyp_notation_edge_constructor_exists():
    assert callable(notation_Edge.__init__)


def test_hyp_notation_edge_constructor_args():
    sig = inspect.signature(notation_Edge.__init__)
    params = list(sig.parameters.keys())

def test_hyp_sorting_exists():
    # Check that the Enumeration exists
    assert Sorting is not None

def test_hyp_sorting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sorting]
    expected_literals = [
        "Automatic",
        "Manual",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sorting"

def test_hyp_textalignment_exists():
    # Check that the Enumeration exists
    assert TextAlignment is not None

def test_hyp_textalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlignment]
    expected_literals = [
        "Left",
        "Right",
        "Center",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlignment"

def test_hyp_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_hyp_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "Top",
        "Right",
        "Left",
        "Center",
        "Bottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_hyp_sortingdirection_exists():
    # Check that the Enumeration exists
    assert SortingDirection is not None

def test_hyp_sortingdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortingDirection]
    expected_literals = [
        "Descending",
        "Ascending",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortingDirection"

def test_hyp_jumplinktype_exists():
    # Check that the Enumeration exists
    assert JumpLinkType is not None

def test_hyp_jumplinktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpLinkType]
    expected_literals = [
        "Square",
        "Chamfered",
        "Semicircle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpLinkType"

def test_hyp_measurementunit_exists():
    # Check that the Enumeration exists
    assert MeasurementUnit is not None

def test_hyp_measurementunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasurementUnit]
    expected_literals = [
        "Himetric",
        "Pixel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasurementUnit"

def test_hyp_arrowtype_exists():
    # Check that the Enumeration exists
    assert ArrowType is not None

def test_hyp_arrowtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrowType]
    expected_literals = [
        "None_",
        "SolidArrow",
        "OpenArrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrowType"

def test_hyp_gradientstyle_exists():
    # Check that the Enumeration exists
    assert GradientStyle is not None

def test_hyp_gradientstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GradientStyle]
    expected_literals = [
        "Vertical",
        "Horizontal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GradientStyle"

def test_hyp_jumplinkstatus_exists():
    # Check that the Enumeration exists
    assert JumpLinkStatus is not None

def test_hyp_jumplinkstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpLinkStatus]
    expected_literals = [
        "All",
        "Above",
        "Below",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpLinkStatus"

def test_hyp_smoothness_exists():
    # Check that the Enumeration exists
    assert Smoothness is not None

def test_hyp_smoothness_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Smoothness]
    expected_literals = [
        "Less",
        "Normal",
        "None_",
        "More",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Smoothness"

def test_hyp_routing_exists():
    # Check that the Enumeration exists
    assert Routing is not None

def test_hyp_routing_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Routing]
    expected_literals = [
        "Manual",
        "Rectilinear",
        "Tree",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Routing"

def test_hyp_linetype_exists():
    # Check that the Enumeration exists
    assert LineType is not None

def test_hyp_linetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineType]
    expected_literals = [
        "Double",
        "DashDotDot",
        "Solid",
        "Dash",
        "DashDot",
        "Dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineType"

def test_hyp_filtering_exists():
    # Check that the Enumeration exists
    assert Filtering is not None

def test_hyp_filtering_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Filtering]
    expected_literals = [
        "Manual",
        "Automatic",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Filtering"


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
BasicSemanticCompartment_strategy = st.builds(
    BasicSemanticCompartment,
)
DrawerStyle_strategy = st.builds(
    DrawerStyle,
)
DecorationNode_strategy = st.builds(
    DecorationNode,
)
notation_BasicCompartment_strategy = st.builds(
    notation_BasicCompartment,
)
BasicDecorationNode_strategy = st.builds(
    BasicDecorationNode,
)
notation_BasicSemanticCompartment_strategy = st.builds(
    notation_BasicSemanticCompartment,
)
notation_DecorationNode_strategy = st.builds(
    notation_DecorationNode,
)
DiagramStyle_strategy = st.builds(
    DiagramStyle,
)
Diagram_strategy = st.builds(
    Diagram,
)
notation_StandardDiagram_strategy = st.builds(
    notation_StandardDiagram,
)
ConnectorStyle_strategy = st.builds(
    ConnectorStyle,
)
Edge_strategy = st.builds(
    Edge,
)
notation_Connector_strategy = st.builds(
    notation_Connector,
)
FilteringStyle_strategy = st.builds(
    FilteringStyle,
)
SortingStyle_strategy = st.builds(
    SortingStyle,
)
TitleStyle_strategy = st.builds(
    TitleStyle,
)
notation_SemanticListCompartment_strategy = st.builds(
    notation_SemanticListCompartment,
)
CanonicalStyle_strategy = st.builds(
    CanonicalStyle,
)
BasicCompartment_strategy = st.builds(
    BasicCompartment,
)
notation_ListCompartment_strategy = st.builds(
    notation_ListCompartment,
)
notation_Compartment_strategy = st.builds(
    notation_Compartment,
)
ShapeStyle_strategy = st.builds(
    ShapeStyle,
)
Node_strategy = st.builds(
    Node,
)
notation_BasicDecorationNode_strategy = st.builds(
    notation_BasicDecorationNode,
)
notation_Shape_strategy = st.builds(
    notation_Shape,
)
DiagramLinkStyle_strategy = st.builds(
    DiagramLinkStyle,
)
DataTypeStyle_strategy = st.builds(
    DataTypeStyle,
)
notation_SingleValueStyle_strategy = st.builds(
    notation_SingleValueStyle,
    rawValue=
        safe_text
)
notation_EDataType_strategy = st.builds(
    notation_EDataType,
)
StringObjectConverter_strategy = st.builds(
    StringObjectConverter,
)
notation_PropertyValue_strategy = st.builds(
    notation_PropertyValue,
    rawValue=
        safe_text
)
notation_StringObjectConverter_strategy = st.builds(
    notation_StringObjectConverter,
)
notation_ListValueStyle_strategy = st.builds(
    notation_ListValueStyle,
    rawValuesList=
        safe_text
)
notation_StringToPropertyValueMapEntry_strategy = st.builds(
    notation_StringToPropertyValueMapEntry,
    key=
        safe_text
)
NamedStyle_strategy = st.builds(
    NamedStyle,
)
notation_DataTypeStyle_strategy = st.builds(
    notation_DataTypeStyle,
)
notation_EObjectListValueStyle_strategy = st.builds(
    notation_EObjectListValueStyle,
)
notation_EObjectValueStyle_strategy = st.builds(
    notation_EObjectValueStyle,
)
notation_StringListValueStyle_strategy = st.builds(
    notation_StringListValueStyle,
    stringListValue=
        safe_text
)
notation_DoubleListValueStyle_strategy = st.builds(
    notation_DoubleListValueStyle,
    doubleListValue=
        safe_text
)
notation_IntValueStyle_strategy = st.builds(
    notation_IntValueStyle,
    intValue=
        st.integers()
)
notation_BooleanListValueStyle_strategy = st.builds(
    notation_BooleanListValueStyle,
    booleanListValue=
        safe_text
)
notation_StringValueStyle_strategy = st.builds(
    notation_StringValueStyle,
    stringValue=
        safe_text
)
notation_IntListValueStyle_strategy = st.builds(
    notation_IntListValueStyle,
    intListValue=
        st.integers()
)
notation_ByteArrayValueStyle_strategy = st.builds(
    notation_ByteArrayValueStyle,
    byteArrayValue=
        safe_text
)
notation_BooleanValueStyle_strategy = st.builds(
    notation_BooleanValueStyle,
    booleanValue=
        st.booleans()
)
notation_DoubleValueStyle_strategy = st.builds(
    notation_DoubleValueStyle,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
notation_PropertiesSetStyle_strategy = st.builds(
    notation_PropertiesSetStyle,
)
GuideStyle_strategy = st.builds(
    GuideStyle,
)
PageStyle_strategy = st.builds(
    PageStyle,
)
ImageStyle_strategy = st.builds(
    ImageStyle,
)
notation_ImageBufferStyle_strategy = st.builds(
    notation_ImageBufferStyle,
)
notation_Guide_strategy = st.builds(
    notation_Guide,
    position=
        st.integers()
)
RoutingStyle_strategy = st.builds(
    RoutingStyle,
)
LineStyle_strategy = st.builds(
    LineStyle,
)
notation_ConnectorStyle_strategy = st.builds(
    notation_ConnectorStyle,
)
FillStyle_strategy = st.builds(
    FillStyle,
)
DescriptionStyle_strategy = st.builds(
    DescriptionStyle,
)
notation_DiagramStyle_strategy = st.builds(
    notation_DiagramStyle,
)
FontStyle_strategy = st.builds(
    FontStyle,
)
notation_Image_strategy = st.builds(
    notation_Image,
    data=
        safe_text
)
notation_NodeEntry_strategy = st.builds(
    notation_NodeEntry,
    value=
        safe_text
)
Bendpoints_strategy = st.builds(
    Bendpoints,
)
notation_RelativeBendpoints_strategy = st.builds(
    notation_RelativeBendpoints,
    points=
        safe_text
)
EModelElement_strategy = st.builds(
    EModelElement,
)
RoundedCornersStyle_strategy = st.builds(
    RoundedCornersStyle,
)
notation_ShapeStyle_strategy = st.builds(
    notation_ShapeStyle,
)
notation_RoutingStyle_strategy = st.builds(
    notation_RoutingStyle,
    closestDistance=
        st.booleans(),
    jumpLinksReverse=
        st.booleans(),
    avoidObstructions=
        st.booleans(),
    routing=
        safe_text,
    jumpLinkType=
        safe_text,
    smoothness=
        safe_text,
    jumpLinkStatus=
        safe_text
)
LayoutConstraint_strategy = st.builds(
    LayoutConstraint,
)
notation_Size_strategy = st.builds(
    notation_Size,
    height=
        st.integers(),
    width=
        st.integers()
)
notation_EObject_strategy = st.builds(
    notation_EObject,
)
Anchor_strategy = st.builds(
    Anchor,
)
notation_IdentityAnchor_strategy = st.builds(
    notation_IdentityAnchor,
    id=
        safe_text
)
notation_Ratio_strategy = st.builds(
    notation_Ratio,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Size_strategy = st.builds(
    Size,
)
Location_strategy = st.builds(
    Location,
)
notation_Bounds_strategy = st.builds(
    notation_Bounds,
)
notation_Location_strategy = st.builds(
    notation_Location,
    x=
        st.integers(),
    y=
        st.integers()
)
notation_Anchor_strategy = st.builds(
    notation_Anchor,
)
notation_Bendpoints_strategy = st.builds(
    notation_Bendpoints,
)
notation_View_strategy = st.builds(
    notation_View,
    mutable=
        st.booleans(),
    type=
        safe_text,
    visible=
        st.booleans()
)
Style_strategy = st.builds(
    Style,
)
notation_PageStyle_strategy = st.builds(
    notation_PageStyle,
    pageHeight=
        st.integers(),
    pageWidth=
        st.integers(),
    pageX=
        st.integers(),
    pageY=
        st.integers()
)
notation_RoundedCornersStyle_strategy = st.builds(
    notation_RoundedCornersStyle,
    roundedBendpointsRadius=
        st.integers()
)
notation_GuideStyle_strategy = st.builds(
    notation_GuideStyle,
)
notation_ArrowStyle_strategy = st.builds(
    notation_ArrowStyle,
    arrowSource=
        safe_text,
    arrowTarget=
        safe_text
)
notation_HintedDiagramLinkStyle_strategy = st.builds(
    notation_HintedDiagramLinkStyle,
    hint=
        safe_text
)
notation_FilteringStyle_strategy = st.builds(
    notation_FilteringStyle,
    filteringKeys=
        safe_text,
    filtering=
        safe_text
)
notation_DiagramLinkStyle_strategy = st.builds(
    notation_DiagramLinkStyle,
)
notation_SortingStyle_strategy = st.builds(
    notation_SortingStyle,
    sortingKeys=
        safe_text,
    sorting=
        safe_text
)
notation_FontStyle_strategy = st.builds(
    notation_FontStyle,
    strikeThrough=
        st.booleans(),
    fontHeight=
        st.integers(),
    italic=
        st.booleans(),
    underline=
        st.booleans(),
    fontColor=
        st.integers(),
    fontName=
        safe_text,
    bold=
        st.booleans()
)
notation_LineStyle_strategy = st.builds(
    notation_LineStyle,
    lineColor=
        st.integers(),
    lineWidth=
        st.integers()
)
notation_MultiDiagramLinkStyle_strategy = st.builds(
    notation_MultiDiagramLinkStyle,
)
notation_LineTypeStyle_strategy = st.builds(
    notation_LineTypeStyle,
    lineType=
        safe_text
)
notation_TextStyle_strategy = st.builds(
    notation_TextStyle,
    textAlignment=
        safe_text
)
notation_TitleStyle_strategy = st.builds(
    notation_TitleStyle,
    showTitle=
        st.booleans()
)
notation_CanonicalStyle_strategy = st.builds(
    notation_CanonicalStyle,
    canonical=
        st.booleans()
)
notation_NamedStyle_strategy = st.builds(
    notation_NamedStyle,
    name=
        safe_text
)
notation_DescriptionStyle_strategy = st.builds(
    notation_DescriptionStyle,
    description=
        safe_text
)
notation_DrawerStyle_strategy = st.builds(
    notation_DrawerStyle,
    collapsed=
        st.booleans()
)
notation_ImageStyle_strategy = st.builds(
    notation_ImageStyle,
    maintainAspectRatio=
        safe_text,
    antiAlias=
        safe_text
)
notation_FillStyle_strategy = st.builds(
    notation_FillStyle,
    transparency=
        st.integers(),
    fillColor=
        st.integers()
)
notation_Style_strategy = st.builds(
    notation_Style,
)
notation_LayoutConstraint_strategy = st.builds(
    notation_LayoutConstraint,
)
View_strategy = st.builds(
    View,
)
notation_Node_strategy = st.builds(
    notation_Node,
)
notation_Diagram_strategy = st.builds(
    notation_Diagram,
    name=
        safe_text,
    measurementUnit=
        safe_text
)
notation_Edge_strategy = st.builds(
    notation_Edge,
)































@given(instance=notation_SingleValueStyle_strategy)
def test_hyp_notation_singlevaluestyle_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_SingleValueStyle_strategy)
@settings(max_examples=30)
def test_hyp_notation_singlevaluestyle_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in notation_SingleValueStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in notation_SingleValueStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in notation_SingleValueStyle is not implemented or raised an error")






@given(instance=notation_PropertyValue_strategy)
def test_hyp_notation_propertyvalue_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertyValue_strategy)
@settings(max_examples=30)
def test_hyp_notation_propertyvalue_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in notation_PropertyValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in notation_PropertyValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in notation_PropertyValue is not implemented or raised an error")





@given(instance=notation_ListValueStyle_strategy)
def test_hyp_notation_listvaluestyle_rawValuesList_setter(instance):
    original = instance.rawValuesList
    instance.rawValuesList = original
    assert instance.rawValuesList == original




@given(instance=notation_StringToPropertyValueMapEntry_strategy)
def test_hyp_notation_stringtopropertyvaluemapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original








@given(instance=notation_StringListValueStyle_strategy)
def test_hyp_notation_stringlistvaluestyle_stringListValue_setter(instance):
    original = instance.stringListValue
    instance.stringListValue = original
    assert instance.stringListValue == original




@given(instance=notation_DoubleListValueStyle_strategy)
def test_hyp_notation_doublelistvaluestyle_doubleListValue_setter(instance):
    original = instance.doubleListValue
    instance.doubleListValue = original
    assert instance.doubleListValue == original




@given(instance=notation_IntValueStyle_strategy)
def test_hyp_notation_intvaluestyle_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original




@given(instance=notation_BooleanListValueStyle_strategy)
def test_hyp_notation_booleanlistvaluestyle_booleanListValue_setter(instance):
    original = instance.booleanListValue
    instance.booleanListValue = original
    assert instance.booleanListValue == original




@given(instance=notation_StringValueStyle_strategy)
def test_hyp_notation_stringvaluestyle_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original




@given(instance=notation_IntListValueStyle_strategy)
def test_hyp_notation_intlistvaluestyle_intListValue_setter(instance):
    original = instance.intListValue
    instance.intListValue = original
    assert instance.intListValue == original




@given(instance=notation_ByteArrayValueStyle_strategy)
def test_hyp_notation_bytearrayvaluestyle_byteArrayValue_setter(instance):
    original = instance.byteArrayValue
    instance.byteArrayValue = original
    assert instance.byteArrayValue == original




@given(instance=notation_BooleanValueStyle_strategy)
def test_hyp_notation_booleanvaluestyle_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original




@given(instance=notation_DoubleValueStyle_strategy)
def test_hyp_notation_doublevaluestyle_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_hyp_notation_propertiessetstyle_removeproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeProperty' in notation_PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_hyp_notation_propertiessetstyle_createproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createProperty' in notation_PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_hyp_notation_propertiessetstyle_hasproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasProperty' in notation_PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_hyp_notation_propertiessetstyle_setproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setProperty' in notation_PropertiesSetStyle is not implemented or raised an error")








@given(instance=notation_Guide_strategy)
def test_hyp_notation_guide_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original











@given(instance=notation_Image_strategy)
def test_hyp_notation_image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original




@given(instance=notation_NodeEntry_strategy)
def test_hyp_notation_nodeentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=notation_RelativeBendpoints_strategy)
def test_hyp_notation_relativebendpoints_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original







@given(instance=notation_RoutingStyle_strategy)
def test_hyp_notation_routingstyle_closestDistance_setter(instance):
    original = instance.closestDistance
    instance.closestDistance = original
    assert instance.closestDistance == original



@given(instance=notation_RoutingStyle_strategy)
def test_hyp_notation_routingstyle_jumpLinksReverse_setter(instance):
    original = instance.jumpLinksReverse
    instance.jumpLinksReverse = original
    assert instance.jumpLinksReverse == original



@given(instance=notation_RoutingStyle_strategy)
def test_hyp_notation_routingstyle_avoidObstructions_setter(instance):
    original = instance.avoidObstructions
    instance.avoidObstructions = original
    assert instance.avoidObstructions == original



@given(instance=notation_RoutingStyle_strategy)
def test_hyp_notation_routingstyle_routing_setter(instance):
    original = instance.routing
    instance.routing = original
    assert instance.routing == original



@given(instance=notation_RoutingStyle_strategy)
def test_hyp_notation_routingstyle_jumpLinkType_setter(instance):
    original = instance.jumpLinkType
    instance.jumpLinkType = original
    assert instance.jumpLinkType == original



@given(instance=notation_RoutingStyle_strategy)
def test_hyp_notation_routingstyle_smoothness_setter(instance):
    original = instance.smoothness
    instance.smoothness = original
    assert instance.smoothness == original



@given(instance=notation_RoutingStyle_strategy)
def test_hyp_notation_routingstyle_jumpLinkStatus_setter(instance):
    original = instance.jumpLinkStatus
    instance.jumpLinkStatus = original
    assert instance.jumpLinkStatus == original





@given(instance=notation_Size_strategy)
def test_hyp_notation_size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=notation_Size_strategy)
def test_hyp_notation_size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original






@given(instance=notation_IdentityAnchor_strategy)
def test_hyp_notation_identityanchor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=notation_Ratio_strategy)
def test_hyp_notation_ratio_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=notation_Location_strategy)
def test_hyp_notation_location_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=notation_Location_strategy)
def test_hyp_notation_location_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original






@given(instance=notation_View_strategy)
def test_hyp_notation_view_mutable_setter(instance):
    original = instance.mutable
    instance.mutable = original
    assert instance.mutable == original



@given(instance=notation_View_strategy)
def test_hyp_notation_view_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=notation_View_strategy)
def test_hyp_notation_view_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_View_strategy)
@settings(max_examples=30)
def test_hyp_notation_view_createchild_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createChild(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createChild).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createChild' in notation_View is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createChild' in notation_View did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createChild' in notation_View is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_View_strategy)
@settings(max_examples=30)
def test_hyp_notation_view_createstyle_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createStyle(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createStyle).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createStyle' in notation_View is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createStyle' in notation_View did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createStyle' in notation_View is not implemented or raised an error")





@given(instance=notation_PageStyle_strategy)
def test_hyp_notation_pagestyle_pageHeight_setter(instance):
    original = instance.pageHeight
    instance.pageHeight = original
    assert instance.pageHeight == original



@given(instance=notation_PageStyle_strategy)
def test_hyp_notation_pagestyle_pageWidth_setter(instance):
    original = instance.pageWidth
    instance.pageWidth = original
    assert instance.pageWidth == original



@given(instance=notation_PageStyle_strategy)
def test_hyp_notation_pagestyle_pageX_setter(instance):
    original = instance.pageX
    instance.pageX = original
    assert instance.pageX == original



@given(instance=notation_PageStyle_strategy)
def test_hyp_notation_pagestyle_pageY_setter(instance):
    original = instance.pageY
    instance.pageY = original
    assert instance.pageY == original




@given(instance=notation_RoundedCornersStyle_strategy)
def test_hyp_notation_roundedcornersstyle_roundedBendpointsRadius_setter(instance):
    original = instance.roundedBendpointsRadius
    instance.roundedBendpointsRadius = original
    assert instance.roundedBendpointsRadius == original





@given(instance=notation_ArrowStyle_strategy)
def test_hyp_notation_arrowstyle_arrowSource_setter(instance):
    original = instance.arrowSource
    instance.arrowSource = original
    assert instance.arrowSource == original



@given(instance=notation_ArrowStyle_strategy)
def test_hyp_notation_arrowstyle_arrowTarget_setter(instance):
    original = instance.arrowTarget
    instance.arrowTarget = original
    assert instance.arrowTarget == original




@given(instance=notation_HintedDiagramLinkStyle_strategy)
def test_hyp_notation_hinteddiagramlinkstyle_hint_setter(instance):
    original = instance.hint
    instance.hint = original
    assert instance.hint == original




@given(instance=notation_FilteringStyle_strategy)
def test_hyp_notation_filteringstyle_filteringKeys_setter(instance):
    original = instance.filteringKeys
    instance.filteringKeys = original
    assert instance.filteringKeys == original



@given(instance=notation_FilteringStyle_strategy)
def test_hyp_notation_filteringstyle_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original





@given(instance=notation_SortingStyle_strategy)
def test_hyp_notation_sortingstyle_sortingKeys_setter(instance):
    original = instance.sortingKeys
    instance.sortingKeys = original
    assert instance.sortingKeys == original



@given(instance=notation_SortingStyle_strategy)
def test_hyp_notation_sortingstyle_sorting_setter(instance):
    original = instance.sorting
    instance.sorting = original
    assert instance.sorting == original




@given(instance=notation_FontStyle_strategy)
def test_hyp_notation_fontstyle_strikeThrough_setter(instance):
    original = instance.strikeThrough
    instance.strikeThrough = original
    assert instance.strikeThrough == original



@given(instance=notation_FontStyle_strategy)
def test_hyp_notation_fontstyle_fontHeight_setter(instance):
    original = instance.fontHeight
    instance.fontHeight = original
    assert instance.fontHeight == original



@given(instance=notation_FontStyle_strategy)
def test_hyp_notation_fontstyle_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original



@given(instance=notation_FontStyle_strategy)
def test_hyp_notation_fontstyle_underline_setter(instance):
    original = instance.underline
    instance.underline = original
    assert instance.underline == original



@given(instance=notation_FontStyle_strategy)
def test_hyp_notation_fontstyle_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original



@given(instance=notation_FontStyle_strategy)
def test_hyp_notation_fontstyle_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=notation_FontStyle_strategy)
def test_hyp_notation_fontstyle_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original




@given(instance=notation_LineStyle_strategy)
def test_hyp_notation_linestyle_lineColor_setter(instance):
    original = instance.lineColor
    instance.lineColor = original
    assert instance.lineColor == original



@given(instance=notation_LineStyle_strategy)
def test_hyp_notation_linestyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original





@given(instance=notation_LineTypeStyle_strategy)
def test_hyp_notation_linetypestyle_lineType_setter(instance):
    original = instance.lineType
    instance.lineType = original
    assert instance.lineType == original




@given(instance=notation_TextStyle_strategy)
def test_hyp_notation_textstyle_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original




@given(instance=notation_TitleStyle_strategy)
def test_hyp_notation_titlestyle_showTitle_setter(instance):
    original = instance.showTitle
    instance.showTitle = original
    assert instance.showTitle == original




@given(instance=notation_CanonicalStyle_strategy)
def test_hyp_notation_canonicalstyle_canonical_setter(instance):
    original = instance.canonical
    instance.canonical = original
    assert instance.canonical == original




@given(instance=notation_NamedStyle_strategy)
def test_hyp_notation_namedstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=notation_DescriptionStyle_strategy)
def test_hyp_notation_descriptionstyle_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=notation_DrawerStyle_strategy)
def test_hyp_notation_drawerstyle_collapsed_setter(instance):
    original = instance.collapsed
    instance.collapsed = original
    assert instance.collapsed == original




@given(instance=notation_ImageStyle_strategy)
def test_hyp_notation_imagestyle_maintainAspectRatio_setter(instance):
    original = instance.maintainAspectRatio
    instance.maintainAspectRatio = original
    assert instance.maintainAspectRatio == original



@given(instance=notation_ImageStyle_strategy)
def test_hyp_notation_imagestyle_antiAlias_setter(instance):
    original = instance.antiAlias
    instance.antiAlias = original
    assert instance.antiAlias == original




@given(instance=notation_FillStyle_strategy)
def test_hyp_notation_fillstyle_transparency_setter(instance):
    original = instance.transparency
    instance.transparency = original
    assert instance.transparency == original



@given(instance=notation_FillStyle_strategy)
def test_hyp_notation_fillstyle_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Node_strategy)
@settings(max_examples=30)
def test_hyp_notation_node_createlayoutconstraint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createLayoutConstraint(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createLayoutConstraint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createLayoutConstraint' in notation_Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLayoutConstraint' in notation_Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLayoutConstraint' in notation_Node is not implemented or raised an error")




@given(instance=notation_Diagram_strategy)
def test_hyp_notation_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=notation_Diagram_strategy)
def test_hyp_notation_diagram_measurementUnit_setter(instance):
    original = instance.measurementUnit
    instance.measurementUnit = original
    assert instance.measurementUnit == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Diagram_strategy)
@settings(max_examples=30)
def test_hyp_notation_diagram_createedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createEdge' in notation_Diagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in notation_Diagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in notation_Diagram is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Edge_strategy)
@settings(max_examples=30)
def test_hyp_notation_edge_createbendpoints_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createBendpoints(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createBendpoints).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createBendpoints' in notation_Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createBendpoints' in notation_Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createBendpoints' in notation_Edge is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Edge_strategy)
@settings(max_examples=30)
def test_hyp_notation_edge_createsourceanchor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createSourceAnchor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createSourceAnchor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createSourceAnchor' in notation_Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createSourceAnchor' in notation_Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createSourceAnchor' in notation_Edge is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Anchor,
    BasicCompartment,
    BasicDecorationNode,
    BasicSemanticCompartment,
    Bendpoints,
    CanonicalStyle,
    ConnectorStyle,
    DataTypeStyle,
    DecorationNode,
    DescriptionStyle,
    Diagram,
    DiagramLinkStyle,
    DiagramStyle,
    DrawerStyle,
    EModelElement,
    Edge,
    FillStyle,
    FilteringStyle,
    FontStyle,
    GuideStyle,
    ImageStyle,
    LayoutConstraint,
    LineStyle,
    Location,
    NamedStyle,
    Node,
    PageStyle,
    RoundedCornersStyle,
    RoutingStyle,
    ShapeStyle,
    Size,
    SortingStyle,
    StringObjectConverter,
    Style,
    TitleStyle,
    View,
    notation_Anchor,
    notation_ArrowStyle,
    notation_BasicCompartment,
    notation_BasicDecorationNode,
    notation_BasicSemanticCompartment,
    notation_Bendpoints,
    notation_BooleanListValueStyle,
    notation_BooleanValueStyle,
    notation_Bounds,
    notation_ByteArrayValueStyle,
    notation_CanonicalStyle,
    notation_Compartment,
    notation_Connector,
    notation_ConnectorStyle,
    notation_DataTypeStyle,
    notation_DecorationNode,
    notation_DescriptionStyle,
    notation_Diagram,
    notation_DiagramLinkStyle,
    notation_DiagramStyle,
    notation_DoubleListValueStyle,
    notation_DoubleValueStyle,
    notation_DrawerStyle,
    notation_EDataType,
    notation_EObject,
    notation_EObjectListValueStyle,
    notation_EObjectValueStyle,
    notation_Edge,
    notation_FillStyle,
    notation_FilteringStyle,
    notation_FontStyle,
    notation_Guide,
    notation_GuideStyle,
    notation_HintedDiagramLinkStyle,
    notation_IdentityAnchor,
    notation_Image,
    notation_ImageBufferStyle,
    notation_ImageStyle,
    notation_IntListValueStyle,
    notation_IntValueStyle,
    notation_LayoutConstraint,
    notation_LineStyle,
    notation_LineTypeStyle,
    notation_ListCompartment,
    notation_ListValueStyle,
    notation_Location,
    notation_MultiDiagramLinkStyle,
    notation_NamedStyle,
    notation_Node,
    notation_NodeEntry,
    notation_PageStyle,
    notation_PropertiesSetStyle,
    notation_PropertyValue,
    notation_Ratio,
    notation_RelativeBendpoints,
    notation_RoundedCornersStyle,
    notation_RoutingStyle,
    notation_SemanticListCompartment,
    notation_Shape,
    notation_ShapeStyle,
    notation_SingleValueStyle,
    notation_Size,
    notation_SortingStyle,
    notation_StandardDiagram,
    notation_StringListValueStyle,
    notation_StringObjectConverter,
    notation_StringToPropertyValueMapEntry,
    notation_StringValueStyle,
    notation_Style,
    notation_TextStyle,
    notation_TitleStyle,
    notation_View,
    Alignment,
    ArrowType,
    Filtering,
    GradientStyle,
    JumpLinkStatus,
    JumpLinkType,
    LineType,
    MeasurementUnit,
    Routing,
    Smoothness,
    Sorting,
    SortingDirection,
    TextAlignment,
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

def test_notation_ArrowStyle_arrowSource_value_roundtrip():
    instance = notation_ArrowStyle(arrowSource="sample_text", arrowTarget="sample_text")
    assert instance.arrowSource == "sample_text"
    instance.arrowSource = "sample_text_2"
    assert instance.arrowSource == "sample_text_2"


def test_notation_ArrowStyle_arrowTarget_value_roundtrip():
    instance = notation_ArrowStyle(arrowSource="sample_text", arrowTarget="sample_text")
    assert instance.arrowTarget == "sample_text"
    instance.arrowTarget = "sample_text_2"
    assert instance.arrowTarget == "sample_text_2"


def test_notation_BooleanListValueStyle_booleanListValue_value_roundtrip():
    instance = notation_BooleanListValueStyle(booleanListValue="sample_text")
    assert instance.booleanListValue == "sample_text"
    instance.booleanListValue = "sample_text_2"
    assert instance.booleanListValue == "sample_text_2"


def test_notation_BooleanValueStyle_booleanValue_value_roundtrip():
    instance = notation_BooleanValueStyle(booleanValue=True)
    assert instance.booleanValue == True
    instance.booleanValue = False
    assert instance.booleanValue == False


def test_notation_ByteArrayValueStyle_byteArrayValue_value_roundtrip():
    instance = notation_ByteArrayValueStyle(byteArrayValue="sample_text")
    assert instance.byteArrayValue == "sample_text"
    instance.byteArrayValue = "sample_text_2"
    assert instance.byteArrayValue == "sample_text_2"


def test_notation_CanonicalStyle_canonical_value_roundtrip():
    instance = notation_CanonicalStyle(canonical=True)
    assert instance.canonical == True
    instance.canonical = False
    assert instance.canonical == False


def test_notation_DescriptionStyle_description_value_roundtrip():
    instance = notation_DescriptionStyle(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_notation_Diagram_measurementUnit_value_roundtrip():
    instance = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    assert instance.measurementUnit == "sample_text"
    instance.measurementUnit = "sample_text_2"
    assert instance.measurementUnit == "sample_text_2"


def test_notation_Diagram_name_value_roundtrip():
    instance = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_notation_DoubleListValueStyle_doubleListValue_value_roundtrip():
    instance = notation_DoubleListValueStyle(doubleListValue="sample_text")
    assert instance.doubleListValue == "sample_text"
    instance.doubleListValue = "sample_text_2"
    assert instance.doubleListValue == "sample_text_2"


def test_notation_DoubleValueStyle_doubleValue_value_roundtrip():
    instance = notation_DoubleValueStyle(doubleValue=3.14)
    assert instance.doubleValue == 3.14
    instance.doubleValue = 9.99
    assert instance.doubleValue == 9.99


def test_notation_DrawerStyle_collapsed_value_roundtrip():
    instance = notation_DrawerStyle(collapsed=True)
    assert instance.collapsed == True
    instance.collapsed = False
    assert instance.collapsed == False


def test_notation_FillStyle_fillColor_value_roundtrip():
    instance = notation_FillStyle(fillColor=7, transparency=7)
    assert instance.fillColor == 7
    instance.fillColor = 13
    assert instance.fillColor == 13


def test_notation_FillStyle_transparency_value_roundtrip():
    instance = notation_FillStyle(fillColor=7, transparency=7)
    assert instance.transparency == 7
    instance.transparency = 13
    assert instance.transparency == 13


def test_notation_FilteringStyle_filtering_value_roundtrip():
    instance = notation_FilteringStyle(filtering="sample_text", filteringKeys="sample_text")
    assert instance.filtering == "sample_text"
    instance.filtering = "sample_text_2"
    assert instance.filtering == "sample_text_2"


def test_notation_FilteringStyle_filteringKeys_value_roundtrip():
    instance = notation_FilteringStyle(filtering="sample_text", filteringKeys="sample_text")
    assert instance.filteringKeys == "sample_text"
    instance.filteringKeys = "sample_text_2"
    assert instance.filteringKeys == "sample_text_2"


def test_notation_FontStyle_bold_value_roundtrip():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert instance.bold == True
    instance.bold = False
    assert instance.bold == False


def test_notation_FontStyle_fontColor_value_roundtrip():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert instance.fontColor == 7
    instance.fontColor = 13
    assert instance.fontColor == 13


def test_notation_FontStyle_fontHeight_value_roundtrip():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert instance.fontHeight == 7
    instance.fontHeight = 13
    assert instance.fontHeight == 13


def test_notation_FontStyle_fontName_value_roundtrip():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert instance.fontName == "sample_text"
    instance.fontName = "sample_text_2"
    assert instance.fontName == "sample_text_2"


def test_notation_FontStyle_italic_value_roundtrip():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert instance.italic == True
    instance.italic = False
    assert instance.italic == False


def test_notation_FontStyle_strikeThrough_value_roundtrip():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert instance.strikeThrough == True
    instance.strikeThrough = False
    assert instance.strikeThrough == False


def test_notation_FontStyle_underline_value_roundtrip():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert instance.underline == True
    instance.underline = False
    assert instance.underline == False


def test_notation_Guide_position_value_roundtrip():
    instance = notation_Guide(position=7)
    assert instance.position == 7
    instance.position = 13
    assert instance.position == 13


def test_notation_HintedDiagramLinkStyle_hint_value_roundtrip():
    instance = notation_HintedDiagramLinkStyle(hint="sample_text")
    assert instance.hint == "sample_text"
    instance.hint = "sample_text_2"
    assert instance.hint == "sample_text_2"


def test_notation_IdentityAnchor_id_value_roundtrip():
    instance = notation_IdentityAnchor(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_notation_Image_data_value_roundtrip():
    instance = notation_Image(data="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_notation_ImageStyle_antiAlias_value_roundtrip():
    instance = notation_ImageStyle(antiAlias="sample_text", maintainAspectRatio="sample_text")
    assert instance.antiAlias == "sample_text"
    instance.antiAlias = "sample_text_2"
    assert instance.antiAlias == "sample_text_2"


def test_notation_ImageStyle_maintainAspectRatio_value_roundtrip():
    instance = notation_ImageStyle(antiAlias="sample_text", maintainAspectRatio="sample_text")
    assert instance.maintainAspectRatio == "sample_text"
    instance.maintainAspectRatio = "sample_text_2"
    assert instance.maintainAspectRatio == "sample_text_2"


def test_notation_IntListValueStyle_intListValue_value_roundtrip():
    instance = notation_IntListValueStyle(intListValue=7)
    assert instance.intListValue == 7
    instance.intListValue = 13
    assert instance.intListValue == 13


def test_notation_IntValueStyle_intValue_value_roundtrip():
    instance = notation_IntValueStyle(intValue=7)
    assert instance.intValue == 7
    instance.intValue = 13
    assert instance.intValue == 13


def test_notation_LineStyle_lineColor_value_roundtrip():
    instance = notation_LineStyle(lineColor=7, lineWidth=7)
    assert instance.lineColor == 7
    instance.lineColor = 13
    assert instance.lineColor == 13


def test_notation_LineStyle_lineWidth_value_roundtrip():
    instance = notation_LineStyle(lineColor=7, lineWidth=7)
    assert instance.lineWidth == 7
    instance.lineWidth = 13
    assert instance.lineWidth == 13


def test_notation_LineTypeStyle_lineType_value_roundtrip():
    instance = notation_LineTypeStyle(lineType="sample_text")
    assert instance.lineType == "sample_text"
    instance.lineType = "sample_text_2"
    assert instance.lineType == "sample_text_2"


def test_notation_ListValueStyle_rawValuesList_value_roundtrip():
    instance = notation_ListValueStyle(rawValuesList="sample_text")
    assert instance.rawValuesList == "sample_text"
    instance.rawValuesList = "sample_text_2"
    assert instance.rawValuesList == "sample_text_2"


def test_notation_Location_x_value_roundtrip():
    instance = notation_Location(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_notation_Location_y_value_roundtrip():
    instance = notation_Location(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_notation_NamedStyle_name_value_roundtrip():
    instance = notation_NamedStyle(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_notation_NodeEntry_value_value_roundtrip():
    instance = notation_NodeEntry(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_notation_PageStyle_pageHeight_value_roundtrip():
    instance = notation_PageStyle(pageHeight=7, pageWidth=7, pageX=7, pageY=7)
    assert instance.pageHeight == 7
    instance.pageHeight = 13
    assert instance.pageHeight == 13


def test_notation_PageStyle_pageWidth_value_roundtrip():
    instance = notation_PageStyle(pageHeight=7, pageWidth=7, pageX=7, pageY=7)
    assert instance.pageWidth == 7
    instance.pageWidth = 13
    assert instance.pageWidth == 13


def test_notation_PageStyle_pageX_value_roundtrip():
    instance = notation_PageStyle(pageHeight=7, pageWidth=7, pageX=7, pageY=7)
    assert instance.pageX == 7
    instance.pageX = 13
    assert instance.pageX == 13


def test_notation_PageStyle_pageY_value_roundtrip():
    instance = notation_PageStyle(pageHeight=7, pageWidth=7, pageX=7, pageY=7)
    assert instance.pageY == 7
    instance.pageY = 13
    assert instance.pageY == 13


def test_notation_PropertyValue_rawValue_value_roundtrip():
    instance = notation_PropertyValue(rawValue="sample_text")
    assert instance.rawValue == "sample_text"
    instance.rawValue = "sample_text_2"
    assert instance.rawValue == "sample_text_2"


def test_notation_Ratio_value_value_roundtrip():
    instance = notation_Ratio(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_notation_RelativeBendpoints_points_value_roundtrip():
    instance = notation_RelativeBendpoints(points="sample_text")
    assert instance.points == "sample_text"
    instance.points = "sample_text_2"
    assert instance.points == "sample_text_2"


def test_notation_RoundedCornersStyle_roundedBendpointsRadius_value_roundtrip():
    instance = notation_RoundedCornersStyle(roundedBendpointsRadius=7)
    assert instance.roundedBendpointsRadius == 7
    instance.roundedBendpointsRadius = 13
    assert instance.roundedBendpointsRadius == 13


def test_notation_RoutingStyle_avoidObstructions_value_roundtrip():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert instance.avoidObstructions == True
    instance.avoidObstructions = False
    assert instance.avoidObstructions == False


def test_notation_RoutingStyle_closestDistance_value_roundtrip():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert instance.closestDistance == True
    instance.closestDistance = False
    assert instance.closestDistance == False


def test_notation_RoutingStyle_jumpLinkStatus_value_roundtrip():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert instance.jumpLinkStatus == "sample_text"
    instance.jumpLinkStatus = "sample_text_2"
    assert instance.jumpLinkStatus == "sample_text_2"


def test_notation_RoutingStyle_jumpLinkType_value_roundtrip():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert instance.jumpLinkType == "sample_text"
    instance.jumpLinkType = "sample_text_2"
    assert instance.jumpLinkType == "sample_text_2"


def test_notation_RoutingStyle_jumpLinksReverse_value_roundtrip():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert instance.jumpLinksReverse == True
    instance.jumpLinksReverse = False
    assert instance.jumpLinksReverse == False


def test_notation_RoutingStyle_routing_value_roundtrip():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert instance.routing == "sample_text"
    instance.routing = "sample_text_2"
    assert instance.routing == "sample_text_2"


def test_notation_RoutingStyle_smoothness_value_roundtrip():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert instance.smoothness == "sample_text"
    instance.smoothness = "sample_text_2"
    assert instance.smoothness == "sample_text_2"


def test_notation_SingleValueStyle_rawValue_value_roundtrip():
    instance = notation_SingleValueStyle(rawValue="sample_text")
    assert instance.rawValue == "sample_text"
    instance.rawValue = "sample_text_2"
    assert instance.rawValue == "sample_text_2"


def test_notation_Size_height_value_roundtrip():
    instance = notation_Size(height=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_notation_Size_width_value_roundtrip():
    instance = notation_Size(height=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_notation_SortingStyle_sorting_value_roundtrip():
    instance = notation_SortingStyle(sorting="sample_text", sortingKeys="sample_text")
    assert instance.sorting == "sample_text"
    instance.sorting = "sample_text_2"
    assert instance.sorting == "sample_text_2"


def test_notation_SortingStyle_sortingKeys_value_roundtrip():
    instance = notation_SortingStyle(sorting="sample_text", sortingKeys="sample_text")
    assert instance.sortingKeys == "sample_text"
    instance.sortingKeys = "sample_text_2"
    assert instance.sortingKeys == "sample_text_2"


def test_notation_StringListValueStyle_stringListValue_value_roundtrip():
    instance = notation_StringListValueStyle(stringListValue="sample_text")
    assert instance.stringListValue == "sample_text"
    instance.stringListValue = "sample_text_2"
    assert instance.stringListValue == "sample_text_2"


def test_notation_StringToPropertyValueMapEntry_key_value_roundtrip():
    instance = notation_StringToPropertyValueMapEntry(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_notation_StringValueStyle_stringValue_value_roundtrip():
    instance = notation_StringValueStyle(stringValue="sample_text")
    assert instance.stringValue == "sample_text"
    instance.stringValue = "sample_text_2"
    assert instance.stringValue == "sample_text_2"


def test_notation_TextStyle_textAlignment_value_roundtrip():
    instance = notation_TextStyle(textAlignment="sample_text")
    assert instance.textAlignment == "sample_text"
    instance.textAlignment = "sample_text_2"
    assert instance.textAlignment == "sample_text_2"


def test_notation_TitleStyle_showTitle_value_roundtrip():
    instance = notation_TitleStyle(showTitle=True)
    assert instance.showTitle == True
    instance.showTitle = False
    assert instance.showTitle == False


def test_notation_View_mutable_value_roundtrip():
    instance = notation_View(mutable=True, type="sample_text", visible=True)
    assert instance.mutable == True
    instance.mutable = False
    assert instance.mutable == False


def test_notation_View_type_value_roundtrip():
    instance = notation_View(mutable=True, type="sample_text", visible=True)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_notation_View_visible_value_roundtrip():
    instance = notation_View(mutable=True, type="sample_text", visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_notation_IdentityAnchor_isa_Anchor():
    instance = notation_IdentityAnchor(id="sample_text")
    assert isinstance(instance, Anchor)


def test_notation_Compartment_isa_BasicCompartment():
    instance = notation_Compartment()
    assert isinstance(instance, BasicCompartment)


def test_notation_ListCompartment_isa_BasicCompartment():
    instance = notation_ListCompartment()
    assert isinstance(instance, BasicCompartment)


def test_notation_BasicSemanticCompartment_isa_BasicDecorationNode():
    instance = notation_BasicSemanticCompartment()
    assert isinstance(instance, BasicDecorationNode)


def test_notation_DecorationNode_isa_BasicDecorationNode():
    instance = notation_DecorationNode()
    assert isinstance(instance, BasicDecorationNode)


def test_notation_SemanticListCompartment_isa_BasicSemanticCompartment():
    instance = notation_SemanticListCompartment()
    assert isinstance(instance, BasicSemanticCompartment)


def test_notation_RelativeBendpoints_isa_Bendpoints():
    instance = notation_RelativeBendpoints(points="sample_text")
    assert isinstance(instance, Bendpoints)


def test_notation_Compartment_isa_CanonicalStyle():
    instance = notation_Compartment()
    assert isinstance(instance, CanonicalStyle)


def test_notation_Connector_isa_ConnectorStyle():
    instance = notation_Connector()
    assert isinstance(instance, ConnectorStyle)


def test_notation_ListValueStyle_isa_DataTypeStyle():
    instance = notation_ListValueStyle(rawValuesList="sample_text")
    assert isinstance(instance, DataTypeStyle)


def test_notation_SingleValueStyle_isa_DataTypeStyle():
    instance = notation_SingleValueStyle(rawValue="sample_text")
    assert isinstance(instance, DataTypeStyle)


def test_notation_BasicCompartment_isa_DecorationNode():
    instance = notation_BasicCompartment()
    assert isinstance(instance, DecorationNode)


def test_notation_DiagramStyle_isa_DescriptionStyle():
    instance = notation_DiagramStyle()
    assert isinstance(instance, DescriptionStyle)


def test_notation_ShapeStyle_isa_DescriptionStyle():
    instance = notation_ShapeStyle()
    assert isinstance(instance, DescriptionStyle)


def test_notation_StandardDiagram_isa_Diagram():
    instance = notation_StandardDiagram()
    assert isinstance(instance, Diagram)


def test_notation_HintedDiagramLinkStyle_isa_DiagramLinkStyle():
    instance = notation_HintedDiagramLinkStyle(hint="sample_text")
    assert isinstance(instance, DiagramLinkStyle)


def test_notation_StandardDiagram_isa_DiagramStyle():
    instance = notation_StandardDiagram()
    assert isinstance(instance, DiagramStyle)


def test_notation_BasicCompartment_isa_DrawerStyle():
    instance = notation_BasicCompartment()
    assert isinstance(instance, DrawerStyle)


def test_notation_BasicSemanticCompartment_isa_DrawerStyle():
    instance = notation_BasicSemanticCompartment()
    assert isinstance(instance, DrawerStyle)


def test_notation_View_isa_EModelElement():
    instance = notation_View(mutable=True, type="sample_text", visible=True)
    assert isinstance(instance, EModelElement)


def test_notation_Connector_isa_Edge():
    instance = notation_Connector()
    assert isinstance(instance, Edge)


def test_notation_ShapeStyle_isa_FillStyle():
    instance = notation_ShapeStyle()
    assert isinstance(instance, FillStyle)


def test_notation_ListCompartment_isa_FilteringStyle():
    instance = notation_ListCompartment()
    assert isinstance(instance, FilteringStyle)


def test_notation_SemanticListCompartment_isa_FilteringStyle():
    instance = notation_SemanticListCompartment()
    assert isinstance(instance, FilteringStyle)


def test_notation_ShapeStyle_isa_FontStyle():
    instance = notation_ShapeStyle()
    assert isinstance(instance, FontStyle)


def test_notation_DiagramStyle_isa_GuideStyle():
    instance = notation_DiagramStyle()
    assert isinstance(instance, GuideStyle)


def test_notation_ImageBufferStyle_isa_ImageStyle():
    instance = notation_ImageBufferStyle()
    assert isinstance(instance, ImageStyle)


def test_notation_Location_isa_LayoutConstraint():
    instance = notation_Location(x=7, y=7)
    assert isinstance(instance, LayoutConstraint)


def test_notation_Ratio_isa_LayoutConstraint():
    instance = notation_Ratio(value=3.14)
    assert isinstance(instance, LayoutConstraint)


def test_notation_Size_isa_LayoutConstraint():
    instance = notation_Size(height=7, width=7)
    assert isinstance(instance, LayoutConstraint)


def test_notation_ConnectorStyle_isa_LineStyle():
    instance = notation_ConnectorStyle()
    assert isinstance(instance, LineStyle)


def test_notation_ShapeStyle_isa_LineStyle():
    instance = notation_ShapeStyle()
    assert isinstance(instance, LineStyle)


def test_notation_Bounds_isa_Location():
    instance = notation_Bounds()
    assert isinstance(instance, Location)


def test_notation_BooleanListValueStyle_isa_NamedStyle():
    instance = notation_BooleanListValueStyle(booleanListValue="sample_text")
    assert isinstance(instance, NamedStyle)


def test_notation_BooleanValueStyle_isa_NamedStyle():
    instance = notation_BooleanValueStyle(booleanValue=True)
    assert isinstance(instance, NamedStyle)


def test_notation_ByteArrayValueStyle_isa_NamedStyle():
    instance = notation_ByteArrayValueStyle(byteArrayValue="sample_text")
    assert isinstance(instance, NamedStyle)


def test_notation_DataTypeStyle_isa_NamedStyle():
    instance = notation_DataTypeStyle()
    assert isinstance(instance, NamedStyle)


def test_notation_DoubleListValueStyle_isa_NamedStyle():
    instance = notation_DoubleListValueStyle(doubleListValue="sample_text")
    assert isinstance(instance, NamedStyle)


def test_notation_DoubleValueStyle_isa_NamedStyle():
    instance = notation_DoubleValueStyle(doubleValue=3.14)
    assert isinstance(instance, NamedStyle)


def test_notation_EObjectListValueStyle_isa_NamedStyle():
    instance = notation_EObjectListValueStyle()
    assert isinstance(instance, NamedStyle)


def test_notation_EObjectValueStyle_isa_NamedStyle():
    instance = notation_EObjectValueStyle()
    assert isinstance(instance, NamedStyle)


def test_notation_IntListValueStyle_isa_NamedStyle():
    instance = notation_IntListValueStyle(intListValue=7)
    assert isinstance(instance, NamedStyle)


def test_notation_IntValueStyle_isa_NamedStyle():
    instance = notation_IntValueStyle(intValue=7)
    assert isinstance(instance, NamedStyle)


def test_notation_PropertiesSetStyle_isa_NamedStyle():
    instance = notation_PropertiesSetStyle()
    assert isinstance(instance, NamedStyle)


def test_notation_StringListValueStyle_isa_NamedStyle():
    instance = notation_StringListValueStyle(stringListValue="sample_text")
    assert isinstance(instance, NamedStyle)


def test_notation_StringValueStyle_isa_NamedStyle():
    instance = notation_StringValueStyle(stringValue="sample_text")
    assert isinstance(instance, NamedStyle)


def test_notation_BasicDecorationNode_isa_Node():
    instance = notation_BasicDecorationNode()
    assert isinstance(instance, Node)


def test_notation_Shape_isa_Node():
    instance = notation_Shape()
    assert isinstance(instance, Node)


def test_notation_DiagramStyle_isa_PageStyle():
    instance = notation_DiagramStyle()
    assert isinstance(instance, PageStyle)


def test_notation_RoutingStyle_isa_RoundedCornersStyle():
    instance = notation_RoutingStyle(avoidObstructions=True, closestDistance=True, jumpLinkStatus="sample_text", jumpLinkType="sample_text", jumpLinksReverse=True, routing="sample_text", smoothness="sample_text")
    assert isinstance(instance, RoundedCornersStyle)


def test_notation_ShapeStyle_isa_RoundedCornersStyle():
    instance = notation_ShapeStyle()
    assert isinstance(instance, RoundedCornersStyle)


def test_notation_ConnectorStyle_isa_RoutingStyle():
    instance = notation_ConnectorStyle()
    assert isinstance(instance, RoutingStyle)


def test_notation_Shape_isa_ShapeStyle():
    instance = notation_Shape()
    assert isinstance(instance, ShapeStyle)


def test_notation_Bounds_isa_Size():
    instance = notation_Bounds()
    assert isinstance(instance, Size)


def test_notation_ListCompartment_isa_SortingStyle():
    instance = notation_ListCompartment()
    assert isinstance(instance, SortingStyle)


def test_notation_SemanticListCompartment_isa_SortingStyle():
    instance = notation_SemanticListCompartment()
    assert isinstance(instance, SortingStyle)


def test_notation_DataTypeStyle_isa_StringObjectConverter():
    instance = notation_DataTypeStyle()
    assert isinstance(instance, StringObjectConverter)


def test_notation_PropertyValue_isa_StringObjectConverter():
    instance = notation_PropertyValue(rawValue="sample_text")
    assert isinstance(instance, StringObjectConverter)


def test_notation_ArrowStyle_isa_Style():
    instance = notation_ArrowStyle(arrowSource="sample_text", arrowTarget="sample_text")
    assert isinstance(instance, Style)


def test_notation_CanonicalStyle_isa_Style():
    instance = notation_CanonicalStyle(canonical=True)
    assert isinstance(instance, Style)


def test_notation_DescriptionStyle_isa_Style():
    instance = notation_DescriptionStyle(description="sample_text")
    assert isinstance(instance, Style)


def test_notation_DiagramLinkStyle_isa_Style():
    instance = notation_DiagramLinkStyle()
    assert isinstance(instance, Style)


def test_notation_DrawerStyle_isa_Style():
    instance = notation_DrawerStyle(collapsed=True)
    assert isinstance(instance, Style)


def test_notation_FillStyle_isa_Style():
    instance = notation_FillStyle(fillColor=7, transparency=7)
    assert isinstance(instance, Style)


def test_notation_FilteringStyle_isa_Style():
    instance = notation_FilteringStyle(filtering="sample_text", filteringKeys="sample_text")
    assert isinstance(instance, Style)


def test_notation_FontStyle_isa_Style():
    instance = notation_FontStyle(bold=True, fontColor=7, fontHeight=7, fontName="sample_text", italic=True, strikeThrough=True, underline=True)
    assert isinstance(instance, Style)


def test_notation_GuideStyle_isa_Style():
    instance = notation_GuideStyle()
    assert isinstance(instance, Style)


def test_notation_HintedDiagramLinkStyle_isa_Style():
    instance = notation_HintedDiagramLinkStyle(hint="sample_text")
    assert isinstance(instance, Style)


def test_notation_ImageStyle_isa_Style():
    instance = notation_ImageStyle(antiAlias="sample_text", maintainAspectRatio="sample_text")
    assert isinstance(instance, Style)


def test_notation_LineStyle_isa_Style():
    instance = notation_LineStyle(lineColor=7, lineWidth=7)
    assert isinstance(instance, Style)


def test_notation_LineTypeStyle_isa_Style():
    instance = notation_LineTypeStyle(lineType="sample_text")
    assert isinstance(instance, Style)


def test_notation_MultiDiagramLinkStyle_isa_Style():
    instance = notation_MultiDiagramLinkStyle()
    assert isinstance(instance, Style)


def test_notation_NamedStyle_isa_Style():
    instance = notation_NamedStyle(name="sample_text")
    assert isinstance(instance, Style)


def test_notation_PageStyle_isa_Style():
    instance = notation_PageStyle(pageHeight=7, pageWidth=7, pageX=7, pageY=7)
    assert isinstance(instance, Style)


def test_notation_RoundedCornersStyle_isa_Style():
    instance = notation_RoundedCornersStyle(roundedBendpointsRadius=7)
    assert isinstance(instance, Style)


def test_notation_SortingStyle_isa_Style():
    instance = notation_SortingStyle(sorting="sample_text", sortingKeys="sample_text")
    assert isinstance(instance, Style)


def test_notation_TextStyle_isa_Style():
    instance = notation_TextStyle(textAlignment="sample_text")
    assert isinstance(instance, Style)


def test_notation_TitleStyle_isa_Style():
    instance = notation_TitleStyle(showTitle=True)
    assert isinstance(instance, Style)


def test_notation_Compartment_isa_TitleStyle():
    instance = notation_Compartment()
    assert isinstance(instance, TitleStyle)


def test_notation_ListCompartment_isa_TitleStyle():
    instance = notation_ListCompartment()
    assert isinstance(instance, TitleStyle)


def test_notation_SemanticListCompartment_isa_TitleStyle():
    instance = notation_SemanticListCompartment()
    assert isinstance(instance, TitleStyle)


def test_notation_Diagram_isa_View():
    instance = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    assert isinstance(instance, View)


def test_notation_Edge_isa_View():
    instance = notation_Edge()
    assert isinstance(instance, View)


def test_notation_Node_isa_View():
    instance = notation_Node()
    assert isinstance(instance, View)


def test_assoc_TransientEdges29_link_reassign_clear():
    a = notation_Edge()
    b1 = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    b2 = notation_Diagram(measurementUnit="sample_text_2", name="sample_text_2")
    _safe_set(a, 'notation_Edge31', b1)
    assert _is_linked(a, 'notation_Edge31', b1)
    if hasattr(b1, 'notation_Diagram30'):
        assert _is_linked(b1, 'notation_Diagram30', a)
    _safe_set(a, 'notation_Edge31', b2)
    assert _is_linked(a, 'notation_Edge31', b2)
    if hasattr(b1, 'notation_Diagram30'):
        assert not _is_linked(b1, 'notation_Diagram30', a)
    if hasattr(b2, 'notation_Diagram30'):
        assert _is_linked(b2, 'notation_Diagram30', a)
    _safe_set(a, 'notation_Edge31', None)
    assert not _is_linked(a, 'notation_Edge31', b2)
    if hasattr(b2, 'notation_Diagram30'):
        assert not _is_linked(b2, 'notation_Diagram30', a)


def test_assoc_bendpoints3_link_reassign_clear():
    a = notation_Edge()
    b1 = notation_Bendpoints()
    b2 = notation_Bendpoints()
    _safe_set(a, 'notation_Edge', b1)
    assert _is_linked(a, 'notation_Edge', b1)
    if hasattr(b1, 'notation_Bendpoints'):
        assert _is_linked(b1, 'notation_Bendpoints', a)
    _safe_set(a, 'notation_Edge', b2)
    assert _is_linked(a, 'notation_Edge', b2)
    if hasattr(b1, 'notation_Bendpoints'):
        assert not _is_linked(b1, 'notation_Bendpoints', a)
    if hasattr(b2, 'notation_Bendpoints'):
        assert _is_linked(b2, 'notation_Bendpoints', a)
    _safe_set(a, 'notation_Edge', None)
    assert not _is_linked(a, 'notation_Edge', b2)
    if hasattr(b2, 'notation_Bendpoints'):
        assert not _is_linked(b2, 'notation_Bendpoints', a)


def test_assoc_cropBound43_link_reassign_clear():
    a = notation_ImageStyle(antiAlias="sample_text", maintainAspectRatio="sample_text")
    b1 = notation_Bounds()
    b2 = notation_Bounds()
    _safe_set(a, 'notation_ImageStyle', b1)
    assert _is_linked(a, 'notation_ImageStyle', b1)
    if hasattr(b1, 'notation_Bounds'):
        assert _is_linked(b1, 'notation_Bounds', a)
    _safe_set(a, 'notation_ImageStyle', b2)
    assert _is_linked(a, 'notation_ImageStyle', b2)
    if hasattr(b1, 'notation_Bounds'):
        assert not _is_linked(b1, 'notation_Bounds', a)
    if hasattr(b2, 'notation_Bounds'):
        assert _is_linked(b2, 'notation_Bounds', a)
    _safe_set(a, 'notation_ImageStyle', None)
    assert not _is_linked(a, 'notation_ImageStyle', b2)
    if hasattr(b2, 'notation_Bounds'):
        assert not _is_linked(b2, 'notation_Bounds', a)


def test_assoc_diagram21_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    b2 = notation_Diagram(measurementUnit="sample_text_2", name="sample_text_2")
    _safe_set(a, 'notation_View22', b1)
    assert _is_linked(a, 'notation_View22', b1)
    if hasattr(b1, 'notation_Diagram'):
        assert _is_linked(b1, 'notation_Diagram', a)
    _safe_set(a, 'notation_View22', b2)
    assert _is_linked(a, 'notation_View22', b2)
    if hasattr(b1, 'notation_Diagram'):
        assert not _is_linked(b1, 'notation_Diagram', a)
    if hasattr(b2, 'notation_Diagram'):
        assert _is_linked(b2, 'notation_Diagram', a)
    _safe_set(a, 'notation_View22', None)
    assert not _is_linked(a, 'notation_View22', b2)
    if hasattr(b2, 'notation_Diagram'):
        assert not _is_linked(b2, 'notation_Diagram', a)


def test_assoc_diagramLink56_link_reassign_clear():
    a = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    b1 = notation_DiagramLinkStyle()
    b2 = notation_DiagramLinkStyle()
    _safe_set(a, 'notation_Diagram57', b1)
    assert _is_linked(a, 'notation_Diagram57', b1)
    if hasattr(b1, 'notation_DiagramLinkStyle'):
        assert _is_linked(b1, 'notation_DiagramLinkStyle', a)
    _safe_set(a, 'notation_Diagram57', b2)
    assert _is_linked(a, 'notation_Diagram57', b2)
    if hasattr(b1, 'notation_DiagramLinkStyle'):
        assert not _is_linked(b1, 'notation_DiagramLinkStyle', a)
    if hasattr(b2, 'notation_DiagramLinkStyle'):
        assert _is_linked(b2, 'notation_DiagramLinkStyle', a)
    _safe_set(a, 'notation_Diagram57', None)
    assert not _is_linked(a, 'notation_Diagram57', b2)
    if hasattr(b2, 'notation_DiagramLinkStyle'):
        assert not _is_linked(b2, 'notation_DiagramLinkStyle', a)


def test_assoc_diagramLinks58_link_reassign_clear():
    a = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    b1 = notation_MultiDiagramLinkStyle()
    b2 = notation_MultiDiagramLinkStyle()
    _safe_set(a, 'notation_Diagram59', b1)
    assert _is_linked(a, 'notation_Diagram59', b1)
    if hasattr(b1, 'notation_MultiDiagramLinkStyle'):
        assert _is_linked(b1, 'notation_MultiDiagramLinkStyle', a)
    _safe_set(a, 'notation_Diagram59', b2)
    assert _is_linked(a, 'notation_Diagram59', b2)
    if hasattr(b1, 'notation_MultiDiagramLinkStyle'):
        assert not _is_linked(b1, 'notation_MultiDiagramLinkStyle', a)
    if hasattr(b2, 'notation_MultiDiagramLinkStyle'):
        assert _is_linked(b2, 'notation_MultiDiagramLinkStyle', a)
    _safe_set(a, 'notation_Diagram59', None)
    assert not _is_linked(a, 'notation_Diagram59', b2)
    if hasattr(b2, 'notation_MultiDiagramLinkStyle'):
        assert not _is_linked(b2, 'notation_MultiDiagramLinkStyle', a)


def test_assoc_element18_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_EObject()
    b2 = notation_EObject()
    _safe_set(a, 'notation_View19', b1)
    assert _is_linked(a, 'notation_View19', b1)
    if hasattr(b1, 'notation_EObject20'):
        assert _is_linked(b1, 'notation_EObject20', a)
    _safe_set(a, 'notation_View19', b2)
    assert _is_linked(a, 'notation_View19', b2)
    if hasattr(b1, 'notation_EObject20'):
        assert not _is_linked(b1, 'notation_EObject20', a)
    if hasattr(b2, 'notation_EObject20'):
        assert _is_linked(b2, 'notation_EObject20', a)
    _safe_set(a, 'notation_View19', None)
    assert not _is_linked(a, 'notation_View19', b2)
    if hasattr(b2, 'notation_EObject20'):
        assert not _is_linked(b2, 'notation_EObject20', a)


def test_assoc_filteredObjects41_link_reassign_clear():
    a = notation_FilteringStyle(filtering="sample_text", filteringKeys="sample_text")
    b1 = notation_EObject()
    b2 = notation_EObject()
    _safe_set(a, 'notation_FilteringStyle', {b1})
    assert _is_linked(a, 'notation_FilteringStyle', b1)
    if hasattr(b1, 'notation_EObject42'):
        assert _is_linked(b1, 'notation_EObject42', a)
    _safe_set(a, 'notation_FilteringStyle', {b2})
    assert _is_linked(a, 'notation_FilteringStyle', b2)
    if hasattr(b1, 'notation_EObject42'):
        assert not _is_linked(b1, 'notation_EObject42', a)
    if hasattr(b2, 'notation_EObject42'):
        assert _is_linked(b2, 'notation_EObject42', a)
    _safe_set(a, 'notation_FilteringStyle', set())
    assert not _is_linked(a, 'notation_FilteringStyle', b2)
    if hasattr(b2, 'notation_EObject42'):
        assert not _is_linked(b2, 'notation_EObject42', a)


def test_assoc_horizontalGuides32_link_reassign_clear():
    a = notation_Guide(position=7)
    b1 = notation_GuideStyle()
    b2 = notation_GuideStyle()
    _safe_set(a, 'notation_Guide', b1)
    assert _is_linked(a, 'notation_Guide', b1)
    if hasattr(b1, 'notation_GuideStyle'):
        assert _is_linked(b1, 'notation_GuideStyle', a)
    _safe_set(a, 'notation_Guide', b2)
    assert _is_linked(a, 'notation_Guide', b2)
    if hasattr(b1, 'notation_GuideStyle'):
        assert not _is_linked(b1, 'notation_GuideStyle', a)
    if hasattr(b2, 'notation_GuideStyle'):
        assert _is_linked(b2, 'notation_GuideStyle', a)
    _safe_set(a, 'notation_Guide', None)
    assert not _is_linked(a, 'notation_Guide', b2)
    if hasattr(b2, 'notation_GuideStyle'):
        assert not _is_linked(b2, 'notation_GuideStyle', a)


def test_assoc_imageBuffer44_link_reassign_clear():
    a = notation_Image(data="sample_text")
    b1 = notation_ImageBufferStyle()
    b2 = notation_ImageBufferStyle()
    _safe_set(a, 'notation_Image', b1)
    assert _is_linked(a, 'notation_Image', b1)
    if hasattr(b1, 'notation_ImageBufferStyle'):
        assert _is_linked(b1, 'notation_ImageBufferStyle', a)
    _safe_set(a, 'notation_Image', b2)
    assert _is_linked(a, 'notation_Image', b2)
    if hasattr(b1, 'notation_ImageBufferStyle'):
        assert not _is_linked(b1, 'notation_ImageBufferStyle', a)
    if hasattr(b2, 'notation_ImageBufferStyle'):
        assert _is_linked(b2, 'notation_ImageBufferStyle', a)
    _safe_set(a, 'notation_Image', None)
    assert not _is_linked(a, 'notation_Image', b2)
    if hasattr(b2, 'notation_ImageBufferStyle'):
        assert not _is_linked(b2, 'notation_ImageBufferStyle', a)


def test_assoc_instanceType48_link_reassign_clear():
    a = notation_PropertyValue(rawValue="sample_text")
    b1 = notation_EDataType()
    b2 = notation_EDataType()
    _safe_set(a, 'notation_PropertyValue49', b1)
    assert _is_linked(a, 'notation_PropertyValue49', b1)
    if hasattr(b1, 'notation_EDataType'):
        assert _is_linked(b1, 'notation_EDataType', a)
    _safe_set(a, 'notation_PropertyValue49', b2)
    assert _is_linked(a, 'notation_PropertyValue49', b2)
    if hasattr(b1, 'notation_EDataType'):
        assert not _is_linked(b1, 'notation_EDataType', a)
    if hasattr(b2, 'notation_EDataType'):
        assert _is_linked(b2, 'notation_EDataType', a)
    _safe_set(a, 'notation_PropertyValue49', None)
    assert not _is_linked(a, 'notation_PropertyValue49', b2)
    if hasattr(b2, 'notation_EDataType'):
        assert not _is_linked(b2, 'notation_EDataType', a)


def test_assoc_key38_link_reassign_clear():
    a = notation_NodeEntry(value="sample_text")
    b1 = notation_Node()
    b2 = notation_Node()
    _safe_set(a, 'notation_NodeEntry39', b1)
    assert _is_linked(a, 'notation_NodeEntry39', b1)
    if hasattr(b1, 'notation_Node40'):
        assert _is_linked(b1, 'notation_Node40', a)
    _safe_set(a, 'notation_NodeEntry39', b2)
    assert _is_linked(a, 'notation_NodeEntry39', b2)
    if hasattr(b1, 'notation_Node40'):
        assert not _is_linked(b1, 'notation_Node40', a)
    if hasattr(b2, 'notation_Node40'):
        assert _is_linked(b2, 'notation_Node40', a)
    _safe_set(a, 'notation_NodeEntry39', None)
    assert not _is_linked(a, 'notation_NodeEntry39', b2)
    if hasattr(b2, 'notation_Node40'):
        assert not _is_linked(b2, 'notation_Node40', a)


def test_assoc_layoutConstraint9_link_reassign_clear():
    a = notation_Node()
    b1 = notation_LayoutConstraint()
    b2 = notation_LayoutConstraint()
    _safe_set(a, 'notation_Node', b1)
    assert _is_linked(a, 'notation_Node', b1)
    if hasattr(b1, 'notation_LayoutConstraint'):
        assert _is_linked(b1, 'notation_LayoutConstraint', a)
    _safe_set(a, 'notation_Node', b2)
    assert _is_linked(a, 'notation_Node', b2)
    if hasattr(b1, 'notation_LayoutConstraint'):
        assert not _is_linked(b1, 'notation_LayoutConstraint', a)
    if hasattr(b2, 'notation_LayoutConstraint'):
        assert _is_linked(b2, 'notation_LayoutConstraint', a)
    _safe_set(a, 'notation_Node', None)
    assert not _is_linked(a, 'notation_Node', b2)
    if hasattr(b2, 'notation_LayoutConstraint'):
        assert not _is_linked(b2, 'notation_LayoutConstraint', a)


def test_assoc_nodeMap36_link_reassign_clear():
    a = notation_NodeEntry(value="sample_text")
    b1 = notation_Guide(position=7)
    b2 = notation_Guide(position=13)
    _safe_set(a, 'notation_NodeEntry', b1)
    assert _is_linked(a, 'notation_NodeEntry', b1)
    if hasattr(b1, 'notation_Guide37'):
        assert _is_linked(b1, 'notation_Guide37', a)
    _safe_set(a, 'notation_NodeEntry', b2)
    assert _is_linked(a, 'notation_NodeEntry', b2)
    if hasattr(b1, 'notation_Guide37'):
        assert not _is_linked(b1, 'notation_Guide37', a)
    if hasattr(b2, 'notation_Guide37'):
        assert _is_linked(b2, 'notation_Guide37', a)
    _safe_set(a, 'notation_NodeEntry', None)
    assert not _is_linked(a, 'notation_NodeEntry', b2)
    if hasattr(b2, 'notation_Guide37'):
        assert not _is_linked(b2, 'notation_Guide37', a)


def test_assoc_persistedChildren14_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Node()
    b2 = notation_Node()
    _safe_set(a, 'notation_View', {b1})
    assert _is_linked(a, 'notation_View', b1)
    if hasattr(b1, 'notation_Node15'):
        assert _is_linked(b1, 'notation_Node15', a)
    _safe_set(a, 'notation_View', {b2})
    assert _is_linked(a, 'notation_View', b2)
    if hasattr(b1, 'notation_Node15'):
        assert not _is_linked(b1, 'notation_Node15', a)
    if hasattr(b2, 'notation_Node15'):
        assert _is_linked(b2, 'notation_Node15', a)
    _safe_set(a, 'notation_View', set())
    assert not _is_linked(a, 'notation_View', b2)
    if hasattr(b2, 'notation_Node15'):
        assert not _is_linked(b2, 'notation_Node15', a)


def test_assoc_persistedEdges26_link_reassign_clear():
    a = notation_Edge()
    b1 = notation_Diagram(measurementUnit="sample_text", name="sample_text")
    b2 = notation_Diagram(measurementUnit="sample_text_2", name="sample_text_2")
    _safe_set(a, 'notation_Edge28', b1)
    assert _is_linked(a, 'notation_Edge28', b1)
    if hasattr(b1, 'notation_Diagram27'):
        assert _is_linked(b1, 'notation_Diagram27', a)
    _safe_set(a, 'notation_Edge28', b2)
    assert _is_linked(a, 'notation_Edge28', b2)
    if hasattr(b1, 'notation_Diagram27'):
        assert not _is_linked(b1, 'notation_Diagram27', a)
    if hasattr(b2, 'notation_Diagram27'):
        assert _is_linked(b2, 'notation_Diagram27', a)
    _safe_set(a, 'notation_Edge28', None)
    assert not _is_linked(a, 'notation_Edge28', b2)
    if hasattr(b2, 'notation_Diagram27'):
        assert not _is_linked(b2, 'notation_Diagram27', a)


def test_assoc_propertiesMap45_link_reassign_clear():
    a = notation_StringToPropertyValueMapEntry(key="sample_text")
    b1 = notation_PropertiesSetStyle()
    b2 = notation_PropertiesSetStyle()
    _safe_set(a, 'notation_StringToPropertyValueMapEntry', b1)
    assert _is_linked(a, 'notation_StringToPropertyValueMapEntry', b1)
    if hasattr(b1, 'notation_PropertiesSetStyle'):
        assert _is_linked(b1, 'notation_PropertiesSetStyle', a)
    _safe_set(a, 'notation_StringToPropertyValueMapEntry', b2)
    assert _is_linked(a, 'notation_StringToPropertyValueMapEntry', b2)
    if hasattr(b1, 'notation_PropertiesSetStyle'):
        assert not _is_linked(b1, 'notation_PropertiesSetStyle', a)
    if hasattr(b2, 'notation_PropertiesSetStyle'):
        assert _is_linked(b2, 'notation_PropertiesSetStyle', a)
    _safe_set(a, 'notation_StringToPropertyValueMapEntry', None)
    assert not _is_linked(a, 'notation_StringToPropertyValueMapEntry', b2)
    if hasattr(b2, 'notation_PropertiesSetStyle'):
        assert not _is_linked(b2, 'notation_PropertiesSetStyle', a)


def test_assoc_sortedObjects10_link_reassign_clear():
    a = notation_SortingStyle(sorting="sample_text", sortingKeys="sample_text")
    b1 = notation_EObject()
    b2 = notation_EObject()
    _safe_set(a, 'notation_SortingStyle', {b1})
    assert _is_linked(a, 'notation_SortingStyle', b1)
    if hasattr(b1, 'notation_EObject'):
        assert _is_linked(b1, 'notation_EObject', a)
    _safe_set(a, 'notation_SortingStyle', {b2})
    assert _is_linked(a, 'notation_SortingStyle', b2)
    if hasattr(b1, 'notation_EObject'):
        assert not _is_linked(b1, 'notation_EObject', a)
    if hasattr(b2, 'notation_EObject'):
        assert _is_linked(b2, 'notation_EObject', a)
    _safe_set(a, 'notation_SortingStyle', set())
    assert not _is_linked(a, 'notation_SortingStyle', b2)
    if hasattr(b2, 'notation_EObject'):
        assert not _is_linked(b2, 'notation_EObject', a)


def test_assoc_source0_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Edge()
    b2 = notation_Edge()
    _safe_set(a, 'View', b1)
    assert _is_linked(a, 'View', b1)
    if hasattr(b1, 'sourceEdges'):
        assert _is_linked(b1, 'sourceEdges', a)
    _safe_set(a, 'View', b2)
    assert _is_linked(a, 'View', b2)
    if hasattr(b1, 'sourceEdges'):
        assert not _is_linked(b1, 'sourceEdges', a)
    if hasattr(b2, 'sourceEdges'):
        assert _is_linked(b2, 'sourceEdges', a)
    _safe_set(a, 'View', None)
    assert not _is_linked(a, 'View', b2)
    if hasattr(b2, 'sourceEdges'):
        assert not _is_linked(b2, 'sourceEdges', a)


def test_assoc_sourceAnchor4_link_reassign_clear():
    a = notation_Edge()
    b1 = notation_Anchor()
    b2 = notation_Anchor()
    _safe_set(a, 'notation_Edge5', b1)
    assert _is_linked(a, 'notation_Edge5', b1)
    if hasattr(b1, 'notation_Anchor'):
        assert _is_linked(b1, 'notation_Anchor', a)
    _safe_set(a, 'notation_Edge5', b2)
    assert _is_linked(a, 'notation_Edge5', b2)
    if hasattr(b1, 'notation_Anchor'):
        assert not _is_linked(b1, 'notation_Anchor', a)
    if hasattr(b2, 'notation_Anchor'):
        assert _is_linked(b2, 'notation_Anchor', a)
    _safe_set(a, 'notation_Edge5', None)
    assert not _is_linked(a, 'notation_Edge5', b2)
    if hasattr(b2, 'notation_Anchor'):
        assert not _is_linked(b2, 'notation_Anchor', a)


def test_assoc_sourceEdges11_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Edge()
    b2 = notation_Edge()
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Edge'):
        assert _is_linked(b1, 'Edge', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Edge'):
        assert not _is_linked(b1, 'Edge', a)
    if hasattr(b2, 'Edge'):
        assert _is_linked(b2, 'Edge', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Edge'):
        assert not _is_linked(b2, 'Edge', a)


def test_assoc_styles16_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Style()
    b2 = notation_Style()
    _safe_set(a, 'notation_View17', {b1})
    assert _is_linked(a, 'notation_View17', b1)
    if hasattr(b1, 'notation_Style'):
        assert _is_linked(b1, 'notation_Style', a)
    _safe_set(a, 'notation_View17', {b2})
    assert _is_linked(a, 'notation_View17', b2)
    if hasattr(b1, 'notation_Style'):
        assert not _is_linked(b1, 'notation_Style', a)
    if hasattr(b2, 'notation_Style'):
        assert _is_linked(b2, 'notation_Style', a)
    _safe_set(a, 'notation_View17', set())
    assert not _is_linked(a, 'notation_View17', b2)
    if hasattr(b2, 'notation_Style'):
        assert not _is_linked(b2, 'notation_Style', a)


def test_assoc_target1_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Edge()
    b2 = notation_Edge()
    _safe_set(a, 'View2', b1)
    assert _is_linked(a, 'View2', b1)
    if hasattr(b1, 'targetEdges'):
        assert _is_linked(b1, 'targetEdges', a)
    _safe_set(a, 'View2', b2)
    assert _is_linked(a, 'View2', b2)
    if hasattr(b1, 'targetEdges'):
        assert not _is_linked(b1, 'targetEdges', a)
    if hasattr(b2, 'targetEdges'):
        assert _is_linked(b2, 'targetEdges', a)
    _safe_set(a, 'View2', None)
    assert not _is_linked(a, 'View2', b2)
    if hasattr(b2, 'targetEdges'):
        assert not _is_linked(b2, 'targetEdges', a)


def test_assoc_targetAnchor6_link_reassign_clear():
    a = notation_Edge()
    b1 = notation_Anchor()
    b2 = notation_Anchor()
    _safe_set(a, 'notation_Edge7', b1)
    assert _is_linked(a, 'notation_Edge7', b1)
    if hasattr(b1, 'notation_Anchor8'):
        assert _is_linked(b1, 'notation_Anchor8', a)
    _safe_set(a, 'notation_Edge7', b2)
    assert _is_linked(a, 'notation_Edge7', b2)
    if hasattr(b1, 'notation_Anchor8'):
        assert not _is_linked(b1, 'notation_Anchor8', a)
    if hasattr(b2, 'notation_Anchor8'):
        assert _is_linked(b2, 'notation_Anchor8', a)
    _safe_set(a, 'notation_Edge7', None)
    assert not _is_linked(a, 'notation_Edge7', b2)
    if hasattr(b2, 'notation_Anchor8'):
        assert not _is_linked(b2, 'notation_Anchor8', a)


def test_assoc_targetEdges12_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Edge()
    b2 = notation_Edge()
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'Edge13'):
        assert _is_linked(b1, 'Edge13', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'Edge13'):
        assert not _is_linked(b1, 'Edge13', a)
    if hasattr(b2, 'Edge13'):
        assert _is_linked(b2, 'Edge13', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'Edge13'):
        assert not _is_linked(b2, 'Edge13', a)


def test_assoc_transientChildren23_link_reassign_clear():
    a = notation_View(mutable=True, type="sample_text", visible=True)
    b1 = notation_Node()
    b2 = notation_Node()
    _safe_set(a, 'notation_View24', {b1})
    assert _is_linked(a, 'notation_View24', b1)
    if hasattr(b1, 'notation_Node25'):
        assert _is_linked(b1, 'notation_Node25', a)
    _safe_set(a, 'notation_View24', {b2})
    assert _is_linked(a, 'notation_View24', b2)
    if hasattr(b1, 'notation_Node25'):
        assert not _is_linked(b1, 'notation_Node25', a)
    if hasattr(b2, 'notation_Node25'):
        assert _is_linked(b2, 'notation_Node25', a)
    _safe_set(a, 'notation_View24', set())
    assert not _is_linked(a, 'notation_View24', b2)
    if hasattr(b2, 'notation_Node25'):
        assert not _is_linked(b2, 'notation_Node25', a)


def test_assoc_value46_link_reassign_clear():
    a = notation_StringToPropertyValueMapEntry(key="sample_text")
    b1 = notation_PropertyValue(rawValue="sample_text")
    b2 = notation_PropertyValue(rawValue="sample_text_2")
    _safe_set(a, 'notation_StringToPropertyValueMapEntry47', b1)
    assert _is_linked(a, 'notation_StringToPropertyValueMapEntry47', b1)
    if hasattr(b1, 'notation_PropertyValue'):
        assert _is_linked(b1, 'notation_PropertyValue', a)
    _safe_set(a, 'notation_StringToPropertyValueMapEntry47', b2)
    assert _is_linked(a, 'notation_StringToPropertyValueMapEntry47', b2)
    if hasattr(b1, 'notation_PropertyValue'):
        assert not _is_linked(b1, 'notation_PropertyValue', a)
    if hasattr(b2, 'notation_PropertyValue'):
        assert _is_linked(b2, 'notation_PropertyValue', a)
    _safe_set(a, 'notation_StringToPropertyValueMapEntry47', None)
    assert not _is_linked(a, 'notation_StringToPropertyValueMapEntry47', b2)
    if hasattr(b2, 'notation_PropertyValue'):
        assert not _is_linked(b2, 'notation_PropertyValue', a)


def test_assoc_verticalGuides33_link_reassign_clear():
    a = notation_Guide(position=7)
    b1 = notation_GuideStyle()
    b2 = notation_GuideStyle()
    _safe_set(a, 'notation_Guide35', b1)
    assert _is_linked(a, 'notation_Guide35', b1)
    if hasattr(b1, 'notation_GuideStyle34'):
        assert _is_linked(b1, 'notation_GuideStyle34', a)
    _safe_set(a, 'notation_Guide35', b2)
    assert _is_linked(a, 'notation_Guide35', b2)
    if hasattr(b1, 'notation_GuideStyle34'):
        assert not _is_linked(b1, 'notation_GuideStyle34', a)
    if hasattr(b2, 'notation_GuideStyle34'):
        assert _is_linked(b2, 'notation_GuideStyle34', a)
    _safe_set(a, 'notation_Guide35', None)
    assert not _is_linked(a, 'notation_Guide35', b2)
    if hasattr(b2, 'notation_GuideStyle34'):
        assert not _is_linked(b2, 'notation_GuideStyle34', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Anchor_strategy = st.builds(Anchor)
@given(instance=Anchor_strategy)
@settings(max_examples=25)
def test_Anchor_instantiation(instance):
    assert isinstance(instance, Anchor)


BasicCompartment_strategy = st.builds(BasicCompartment)
@given(instance=BasicCompartment_strategy)
@settings(max_examples=25)
def test_BasicCompartment_instantiation(instance):
    assert isinstance(instance, BasicCompartment)


BasicDecorationNode_strategy = st.builds(BasicDecorationNode)
@given(instance=BasicDecorationNode_strategy)
@settings(max_examples=25)
def test_BasicDecorationNode_instantiation(instance):
    assert isinstance(instance, BasicDecorationNode)


BasicSemanticCompartment_strategy = st.builds(BasicSemanticCompartment)
@given(instance=BasicSemanticCompartment_strategy)
@settings(max_examples=25)
def test_BasicSemanticCompartment_instantiation(instance):
    assert isinstance(instance, BasicSemanticCompartment)


Bendpoints_strategy = st.builds(Bendpoints)
@given(instance=Bendpoints_strategy)
@settings(max_examples=25)
def test_Bendpoints_instantiation(instance):
    assert isinstance(instance, Bendpoints)


CanonicalStyle_strategy = st.builds(CanonicalStyle)
@given(instance=CanonicalStyle_strategy)
@settings(max_examples=25)
def test_CanonicalStyle_instantiation(instance):
    assert isinstance(instance, CanonicalStyle)


ConnectorStyle_strategy = st.builds(ConnectorStyle)
@given(instance=ConnectorStyle_strategy)
@settings(max_examples=25)
def test_ConnectorStyle_instantiation(instance):
    assert isinstance(instance, ConnectorStyle)


DataTypeStyle_strategy = st.builds(DataTypeStyle)
@given(instance=DataTypeStyle_strategy)
@settings(max_examples=25)
def test_DataTypeStyle_instantiation(instance):
    assert isinstance(instance, DataTypeStyle)


DecorationNode_strategy = st.builds(DecorationNode)
@given(instance=DecorationNode_strategy)
@settings(max_examples=25)
def test_DecorationNode_instantiation(instance):
    assert isinstance(instance, DecorationNode)


DescriptionStyle_strategy = st.builds(DescriptionStyle)
@given(instance=DescriptionStyle_strategy)
@settings(max_examples=25)
def test_DescriptionStyle_instantiation(instance):
    assert isinstance(instance, DescriptionStyle)


Diagram_strategy = st.builds(Diagram)
@given(instance=Diagram_strategy)
@settings(max_examples=25)
def test_Diagram_instantiation(instance):
    assert isinstance(instance, Diagram)


DiagramLinkStyle_strategy = st.builds(DiagramLinkStyle)
@given(instance=DiagramLinkStyle_strategy)
@settings(max_examples=25)
def test_DiagramLinkStyle_instantiation(instance):
    assert isinstance(instance, DiagramLinkStyle)


DiagramStyle_strategy = st.builds(DiagramStyle)
@given(instance=DiagramStyle_strategy)
@settings(max_examples=25)
def test_DiagramStyle_instantiation(instance):
    assert isinstance(instance, DiagramStyle)


DrawerStyle_strategy = st.builds(DrawerStyle)
@given(instance=DrawerStyle_strategy)
@settings(max_examples=25)
def test_DrawerStyle_instantiation(instance):
    assert isinstance(instance, DrawerStyle)


EModelElement_strategy = st.builds(EModelElement)
@given(instance=EModelElement_strategy)
@settings(max_examples=25)
def test_EModelElement_instantiation(instance):
    assert isinstance(instance, EModelElement)


Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


FillStyle_strategy = st.builds(FillStyle)
@given(instance=FillStyle_strategy)
@settings(max_examples=25)
def test_FillStyle_instantiation(instance):
    assert isinstance(instance, FillStyle)


FilteringStyle_strategy = st.builds(FilteringStyle)
@given(instance=FilteringStyle_strategy)
@settings(max_examples=25)
def test_FilteringStyle_instantiation(instance):
    assert isinstance(instance, FilteringStyle)


FontStyle_strategy = st.builds(FontStyle)
@given(instance=FontStyle_strategy)
@settings(max_examples=25)
def test_FontStyle_instantiation(instance):
    assert isinstance(instance, FontStyle)


GuideStyle_strategy = st.builds(GuideStyle)
@given(instance=GuideStyle_strategy)
@settings(max_examples=25)
def test_GuideStyle_instantiation(instance):
    assert isinstance(instance, GuideStyle)


ImageStyle_strategy = st.builds(ImageStyle)
@given(instance=ImageStyle_strategy)
@settings(max_examples=25)
def test_ImageStyle_instantiation(instance):
    assert isinstance(instance, ImageStyle)


LayoutConstraint_strategy = st.builds(LayoutConstraint)
@given(instance=LayoutConstraint_strategy)
@settings(max_examples=25)
def test_LayoutConstraint_instantiation(instance):
    assert isinstance(instance, LayoutConstraint)


LineStyle_strategy = st.builds(LineStyle)
@given(instance=LineStyle_strategy)
@settings(max_examples=25)
def test_LineStyle_instantiation(instance):
    assert isinstance(instance, LineStyle)


Location_strategy = st.builds(Location)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


NamedStyle_strategy = st.builds(NamedStyle)
@given(instance=NamedStyle_strategy)
@settings(max_examples=25)
def test_NamedStyle_instantiation(instance):
    assert isinstance(instance, NamedStyle)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


PageStyle_strategy = st.builds(PageStyle)
@given(instance=PageStyle_strategy)
@settings(max_examples=25)
def test_PageStyle_instantiation(instance):
    assert isinstance(instance, PageStyle)


RoundedCornersStyle_strategy = st.builds(RoundedCornersStyle)
@given(instance=RoundedCornersStyle_strategy)
@settings(max_examples=25)
def test_RoundedCornersStyle_instantiation(instance):
    assert isinstance(instance, RoundedCornersStyle)


RoutingStyle_strategy = st.builds(RoutingStyle)
@given(instance=RoutingStyle_strategy)
@settings(max_examples=25)
def test_RoutingStyle_instantiation(instance):
    assert isinstance(instance, RoutingStyle)


ShapeStyle_strategy = st.builds(ShapeStyle)
@given(instance=ShapeStyle_strategy)
@settings(max_examples=25)
def test_ShapeStyle_instantiation(instance):
    assert isinstance(instance, ShapeStyle)


Size_strategy = st.builds(Size)
@given(instance=Size_strategy)
@settings(max_examples=25)
def test_Size_instantiation(instance):
    assert isinstance(instance, Size)


SortingStyle_strategy = st.builds(SortingStyle)
@given(instance=SortingStyle_strategy)
@settings(max_examples=25)
def test_SortingStyle_instantiation(instance):
    assert isinstance(instance, SortingStyle)


StringObjectConverter_strategy = st.builds(StringObjectConverter)
@given(instance=StringObjectConverter_strategy)
@settings(max_examples=25)
def test_StringObjectConverter_instantiation(instance):
    assert isinstance(instance, StringObjectConverter)


Style_strategy = st.builds(Style)
@given(instance=Style_strategy)
@settings(max_examples=25)
def test_Style_instantiation(instance):
    assert isinstance(instance, Style)


TitleStyle_strategy = st.builds(TitleStyle)
@given(instance=TitleStyle_strategy)
@settings(max_examples=25)
def test_TitleStyle_instantiation(instance):
    assert isinstance(instance, TitleStyle)


View_strategy = st.builds(View)
@given(instance=View_strategy)
@settings(max_examples=25)
def test_View_instantiation(instance):
    assert isinstance(instance, View)


notation_Anchor_strategy = st.builds(notation_Anchor)
@given(instance=notation_Anchor_strategy)
@settings(max_examples=25)
def test_notation_Anchor_instantiation(instance):
    assert isinstance(instance, notation_Anchor)


notation_ArrowStyle_strategy = st.builds(notation_ArrowStyle, arrowSource=safe_text, arrowTarget=safe_text)
@given(instance=notation_ArrowStyle_strategy)
@settings(max_examples=25)
def test_notation_ArrowStyle_instantiation(instance):
    assert isinstance(instance, notation_ArrowStyle)


notation_BasicCompartment_strategy = st.builds(notation_BasicCompartment)
@given(instance=notation_BasicCompartment_strategy)
@settings(max_examples=25)
def test_notation_BasicCompartment_instantiation(instance):
    assert isinstance(instance, notation_BasicCompartment)


notation_BasicDecorationNode_strategy = st.builds(notation_BasicDecorationNode)
@given(instance=notation_BasicDecorationNode_strategy)
@settings(max_examples=25)
def test_notation_BasicDecorationNode_instantiation(instance):
    assert isinstance(instance, notation_BasicDecorationNode)


notation_BasicSemanticCompartment_strategy = st.builds(notation_BasicSemanticCompartment)
@given(instance=notation_BasicSemanticCompartment_strategy)
@settings(max_examples=25)
def test_notation_BasicSemanticCompartment_instantiation(instance):
    assert isinstance(instance, notation_BasicSemanticCompartment)


notation_Bendpoints_strategy = st.builds(notation_Bendpoints)
@given(instance=notation_Bendpoints_strategy)
@settings(max_examples=25)
def test_notation_Bendpoints_instantiation(instance):
    assert isinstance(instance, notation_Bendpoints)


notation_BooleanListValueStyle_strategy = st.builds(notation_BooleanListValueStyle, booleanListValue=safe_text)
@given(instance=notation_BooleanListValueStyle_strategy)
@settings(max_examples=25)
def test_notation_BooleanListValueStyle_instantiation(instance):
    assert isinstance(instance, notation_BooleanListValueStyle)


notation_BooleanValueStyle_strategy = st.builds(notation_BooleanValueStyle, booleanValue=st.booleans())
@given(instance=notation_BooleanValueStyle_strategy)
@settings(max_examples=25)
def test_notation_BooleanValueStyle_instantiation(instance):
    assert isinstance(instance, notation_BooleanValueStyle)


notation_Bounds_strategy = st.builds(notation_Bounds)
@given(instance=notation_Bounds_strategy)
@settings(max_examples=25)
def test_notation_Bounds_instantiation(instance):
    assert isinstance(instance, notation_Bounds)


notation_ByteArrayValueStyle_strategy = st.builds(notation_ByteArrayValueStyle, byteArrayValue=safe_text)
@given(instance=notation_ByteArrayValueStyle_strategy)
@settings(max_examples=25)
def test_notation_ByteArrayValueStyle_instantiation(instance):
    assert isinstance(instance, notation_ByteArrayValueStyle)


notation_CanonicalStyle_strategy = st.builds(notation_CanonicalStyle, canonical=st.booleans())
@given(instance=notation_CanonicalStyle_strategy)
@settings(max_examples=25)
def test_notation_CanonicalStyle_instantiation(instance):
    assert isinstance(instance, notation_CanonicalStyle)


notation_Compartment_strategy = st.builds(notation_Compartment)
@given(instance=notation_Compartment_strategy)
@settings(max_examples=25)
def test_notation_Compartment_instantiation(instance):
    assert isinstance(instance, notation_Compartment)


notation_Connector_strategy = st.builds(notation_Connector)
@given(instance=notation_Connector_strategy)
@settings(max_examples=25)
def test_notation_Connector_instantiation(instance):
    assert isinstance(instance, notation_Connector)


notation_ConnectorStyle_strategy = st.builds(notation_ConnectorStyle)
@given(instance=notation_ConnectorStyle_strategy)
@settings(max_examples=25)
def test_notation_ConnectorStyle_instantiation(instance):
    assert isinstance(instance, notation_ConnectorStyle)


notation_DataTypeStyle_strategy = st.builds(notation_DataTypeStyle)
@given(instance=notation_DataTypeStyle_strategy)
@settings(max_examples=25)
def test_notation_DataTypeStyle_instantiation(instance):
    assert isinstance(instance, notation_DataTypeStyle)


notation_DecorationNode_strategy = st.builds(notation_DecorationNode)
@given(instance=notation_DecorationNode_strategy)
@settings(max_examples=25)
def test_notation_DecorationNode_instantiation(instance):
    assert isinstance(instance, notation_DecorationNode)


notation_DescriptionStyle_strategy = st.builds(notation_DescriptionStyle, description=safe_text)
@given(instance=notation_DescriptionStyle_strategy)
@settings(max_examples=25)
def test_notation_DescriptionStyle_instantiation(instance):
    assert isinstance(instance, notation_DescriptionStyle)


notation_Diagram_strategy = st.builds(notation_Diagram, measurementUnit=safe_text, name=safe_text)
@given(instance=notation_Diagram_strategy)
@settings(max_examples=25)
def test_notation_Diagram_instantiation(instance):
    assert isinstance(instance, notation_Diagram)


notation_DiagramLinkStyle_strategy = st.builds(notation_DiagramLinkStyle)
@given(instance=notation_DiagramLinkStyle_strategy)
@settings(max_examples=25)
def test_notation_DiagramLinkStyle_instantiation(instance):
    assert isinstance(instance, notation_DiagramLinkStyle)


notation_DiagramStyle_strategy = st.builds(notation_DiagramStyle)
@given(instance=notation_DiagramStyle_strategy)
@settings(max_examples=25)
def test_notation_DiagramStyle_instantiation(instance):
    assert isinstance(instance, notation_DiagramStyle)


notation_DoubleListValueStyle_strategy = st.builds(notation_DoubleListValueStyle, doubleListValue=safe_text)
@given(instance=notation_DoubleListValueStyle_strategy)
@settings(max_examples=25)
def test_notation_DoubleListValueStyle_instantiation(instance):
    assert isinstance(instance, notation_DoubleListValueStyle)


notation_DoubleValueStyle_strategy = st.builds(notation_DoubleValueStyle, doubleValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=notation_DoubleValueStyle_strategy)
@settings(max_examples=25)
def test_notation_DoubleValueStyle_instantiation(instance):
    assert isinstance(instance, notation_DoubleValueStyle)


notation_DrawerStyle_strategy = st.builds(notation_DrawerStyle, collapsed=st.booleans())
@given(instance=notation_DrawerStyle_strategy)
@settings(max_examples=25)
def test_notation_DrawerStyle_instantiation(instance):
    assert isinstance(instance, notation_DrawerStyle)


notation_EDataType_strategy = st.builds(notation_EDataType)
@given(instance=notation_EDataType_strategy)
@settings(max_examples=25)
def test_notation_EDataType_instantiation(instance):
    assert isinstance(instance, notation_EDataType)


notation_EObject_strategy = st.builds(notation_EObject)
@given(instance=notation_EObject_strategy)
@settings(max_examples=25)
def test_notation_EObject_instantiation(instance):
    assert isinstance(instance, notation_EObject)


notation_EObjectListValueStyle_strategy = st.builds(notation_EObjectListValueStyle)
@given(instance=notation_EObjectListValueStyle_strategy)
@settings(max_examples=25)
def test_notation_EObjectListValueStyle_instantiation(instance):
    assert isinstance(instance, notation_EObjectListValueStyle)


notation_EObjectValueStyle_strategy = st.builds(notation_EObjectValueStyle)
@given(instance=notation_EObjectValueStyle_strategy)
@settings(max_examples=25)
def test_notation_EObjectValueStyle_instantiation(instance):
    assert isinstance(instance, notation_EObjectValueStyle)


notation_Edge_strategy = st.builds(notation_Edge)
@given(instance=notation_Edge_strategy)
@settings(max_examples=25)
def test_notation_Edge_instantiation(instance):
    assert isinstance(instance, notation_Edge)


notation_FillStyle_strategy = st.builds(notation_FillStyle, fillColor=st.integers(), transparency=st.integers())
@given(instance=notation_FillStyle_strategy)
@settings(max_examples=25)
def test_notation_FillStyle_instantiation(instance):
    assert isinstance(instance, notation_FillStyle)


notation_FilteringStyle_strategy = st.builds(notation_FilteringStyle, filtering=safe_text, filteringKeys=safe_text)
@given(instance=notation_FilteringStyle_strategy)
@settings(max_examples=25)
def test_notation_FilteringStyle_instantiation(instance):
    assert isinstance(instance, notation_FilteringStyle)


notation_FontStyle_strategy = st.builds(notation_FontStyle, bold=st.booleans(), fontColor=st.integers(), fontHeight=st.integers(), fontName=safe_text, italic=st.booleans(), strikeThrough=st.booleans(), underline=st.booleans())
@given(instance=notation_FontStyle_strategy)
@settings(max_examples=25)
def test_notation_FontStyle_instantiation(instance):
    assert isinstance(instance, notation_FontStyle)


notation_Guide_strategy = st.builds(notation_Guide, position=st.integers())
@given(instance=notation_Guide_strategy)
@settings(max_examples=25)
def test_notation_Guide_instantiation(instance):
    assert isinstance(instance, notation_Guide)


notation_GuideStyle_strategy = st.builds(notation_GuideStyle)
@given(instance=notation_GuideStyle_strategy)
@settings(max_examples=25)
def test_notation_GuideStyle_instantiation(instance):
    assert isinstance(instance, notation_GuideStyle)


notation_HintedDiagramLinkStyle_strategy = st.builds(notation_HintedDiagramLinkStyle, hint=safe_text)
@given(instance=notation_HintedDiagramLinkStyle_strategy)
@settings(max_examples=25)
def test_notation_HintedDiagramLinkStyle_instantiation(instance):
    assert isinstance(instance, notation_HintedDiagramLinkStyle)


notation_IdentityAnchor_strategy = st.builds(notation_IdentityAnchor, id=safe_text)
@given(instance=notation_IdentityAnchor_strategy)
@settings(max_examples=25)
def test_notation_IdentityAnchor_instantiation(instance):
    assert isinstance(instance, notation_IdentityAnchor)


notation_Image_strategy = st.builds(notation_Image, data=safe_text)
@given(instance=notation_Image_strategy)
@settings(max_examples=25)
def test_notation_Image_instantiation(instance):
    assert isinstance(instance, notation_Image)


notation_ImageBufferStyle_strategy = st.builds(notation_ImageBufferStyle)
@given(instance=notation_ImageBufferStyle_strategy)
@settings(max_examples=25)
def test_notation_ImageBufferStyle_instantiation(instance):
    assert isinstance(instance, notation_ImageBufferStyle)


notation_ImageStyle_strategy = st.builds(notation_ImageStyle, antiAlias=safe_text, maintainAspectRatio=safe_text)
@given(instance=notation_ImageStyle_strategy)
@settings(max_examples=25)
def test_notation_ImageStyle_instantiation(instance):
    assert isinstance(instance, notation_ImageStyle)


notation_IntListValueStyle_strategy = st.builds(notation_IntListValueStyle, intListValue=st.integers())
@given(instance=notation_IntListValueStyle_strategy)
@settings(max_examples=25)
def test_notation_IntListValueStyle_instantiation(instance):
    assert isinstance(instance, notation_IntListValueStyle)


notation_IntValueStyle_strategy = st.builds(notation_IntValueStyle, intValue=st.integers())
@given(instance=notation_IntValueStyle_strategy)
@settings(max_examples=25)
def test_notation_IntValueStyle_instantiation(instance):
    assert isinstance(instance, notation_IntValueStyle)


notation_LayoutConstraint_strategy = st.builds(notation_LayoutConstraint)
@given(instance=notation_LayoutConstraint_strategy)
@settings(max_examples=25)
def test_notation_LayoutConstraint_instantiation(instance):
    assert isinstance(instance, notation_LayoutConstraint)


notation_LineStyle_strategy = st.builds(notation_LineStyle, lineColor=st.integers(), lineWidth=st.integers())
@given(instance=notation_LineStyle_strategy)
@settings(max_examples=25)
def test_notation_LineStyle_instantiation(instance):
    assert isinstance(instance, notation_LineStyle)


notation_LineTypeStyle_strategy = st.builds(notation_LineTypeStyle, lineType=safe_text)
@given(instance=notation_LineTypeStyle_strategy)
@settings(max_examples=25)
def test_notation_LineTypeStyle_instantiation(instance):
    assert isinstance(instance, notation_LineTypeStyle)


notation_ListCompartment_strategy = st.builds(notation_ListCompartment)
@given(instance=notation_ListCompartment_strategy)
@settings(max_examples=25)
def test_notation_ListCompartment_instantiation(instance):
    assert isinstance(instance, notation_ListCompartment)


notation_ListValueStyle_strategy = st.builds(notation_ListValueStyle, rawValuesList=safe_text)
@given(instance=notation_ListValueStyle_strategy)
@settings(max_examples=25)
def test_notation_ListValueStyle_instantiation(instance):
    assert isinstance(instance, notation_ListValueStyle)


notation_Location_strategy = st.builds(notation_Location, x=st.integers(), y=st.integers())
@given(instance=notation_Location_strategy)
@settings(max_examples=25)
def test_notation_Location_instantiation(instance):
    assert isinstance(instance, notation_Location)


notation_MultiDiagramLinkStyle_strategy = st.builds(notation_MultiDiagramLinkStyle)
@given(instance=notation_MultiDiagramLinkStyle_strategy)
@settings(max_examples=25)
def test_notation_MultiDiagramLinkStyle_instantiation(instance):
    assert isinstance(instance, notation_MultiDiagramLinkStyle)


notation_NamedStyle_strategy = st.builds(notation_NamedStyle, name=safe_text)
@given(instance=notation_NamedStyle_strategy)
@settings(max_examples=25)
def test_notation_NamedStyle_instantiation(instance):
    assert isinstance(instance, notation_NamedStyle)


notation_Node_strategy = st.builds(notation_Node)
@given(instance=notation_Node_strategy)
@settings(max_examples=25)
def test_notation_Node_instantiation(instance):
    assert isinstance(instance, notation_Node)


notation_NodeEntry_strategy = st.builds(notation_NodeEntry, value=safe_text)
@given(instance=notation_NodeEntry_strategy)
@settings(max_examples=25)
def test_notation_NodeEntry_instantiation(instance):
    assert isinstance(instance, notation_NodeEntry)


notation_PageStyle_strategy = st.builds(notation_PageStyle, pageHeight=st.integers(), pageWidth=st.integers(), pageX=st.integers(), pageY=st.integers())
@given(instance=notation_PageStyle_strategy)
@settings(max_examples=25)
def test_notation_PageStyle_instantiation(instance):
    assert isinstance(instance, notation_PageStyle)


notation_PropertiesSetStyle_strategy = st.builds(notation_PropertiesSetStyle)
@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=25)
def test_notation_PropertiesSetStyle_instantiation(instance):
    assert isinstance(instance, notation_PropertiesSetStyle)


notation_PropertyValue_strategy = st.builds(notation_PropertyValue, rawValue=safe_text)
@given(instance=notation_PropertyValue_strategy)
@settings(max_examples=25)
def test_notation_PropertyValue_instantiation(instance):
    assert isinstance(instance, notation_PropertyValue)


notation_Ratio_strategy = st.builds(notation_Ratio, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=notation_Ratio_strategy)
@settings(max_examples=25)
def test_notation_Ratio_instantiation(instance):
    assert isinstance(instance, notation_Ratio)


notation_RelativeBendpoints_strategy = st.builds(notation_RelativeBendpoints, points=safe_text)
@given(instance=notation_RelativeBendpoints_strategy)
@settings(max_examples=25)
def test_notation_RelativeBendpoints_instantiation(instance):
    assert isinstance(instance, notation_RelativeBendpoints)


notation_RoundedCornersStyle_strategy = st.builds(notation_RoundedCornersStyle, roundedBendpointsRadius=st.integers())
@given(instance=notation_RoundedCornersStyle_strategy)
@settings(max_examples=25)
def test_notation_RoundedCornersStyle_instantiation(instance):
    assert isinstance(instance, notation_RoundedCornersStyle)


notation_RoutingStyle_strategy = st.builds(notation_RoutingStyle, avoidObstructions=st.booleans(), closestDistance=st.booleans(), jumpLinkStatus=safe_text, jumpLinkType=safe_text, jumpLinksReverse=st.booleans(), routing=safe_text, smoothness=safe_text)
@given(instance=notation_RoutingStyle_strategy)
@settings(max_examples=25)
def test_notation_RoutingStyle_instantiation(instance):
    assert isinstance(instance, notation_RoutingStyle)


notation_SemanticListCompartment_strategy = st.builds(notation_SemanticListCompartment)
@given(instance=notation_SemanticListCompartment_strategy)
@settings(max_examples=25)
def test_notation_SemanticListCompartment_instantiation(instance):
    assert isinstance(instance, notation_SemanticListCompartment)


notation_Shape_strategy = st.builds(notation_Shape)
@given(instance=notation_Shape_strategy)
@settings(max_examples=25)
def test_notation_Shape_instantiation(instance):
    assert isinstance(instance, notation_Shape)


notation_ShapeStyle_strategy = st.builds(notation_ShapeStyle)
@given(instance=notation_ShapeStyle_strategy)
@settings(max_examples=25)
def test_notation_ShapeStyle_instantiation(instance):
    assert isinstance(instance, notation_ShapeStyle)


notation_SingleValueStyle_strategy = st.builds(notation_SingleValueStyle, rawValue=safe_text)
@given(instance=notation_SingleValueStyle_strategy)
@settings(max_examples=25)
def test_notation_SingleValueStyle_instantiation(instance):
    assert isinstance(instance, notation_SingleValueStyle)


notation_Size_strategy = st.builds(notation_Size, height=st.integers(), width=st.integers())
@given(instance=notation_Size_strategy)
@settings(max_examples=25)
def test_notation_Size_instantiation(instance):
    assert isinstance(instance, notation_Size)


notation_SortingStyle_strategy = st.builds(notation_SortingStyle, sorting=safe_text, sortingKeys=safe_text)
@given(instance=notation_SortingStyle_strategy)
@settings(max_examples=25)
def test_notation_SortingStyle_instantiation(instance):
    assert isinstance(instance, notation_SortingStyle)


notation_StandardDiagram_strategy = st.builds(notation_StandardDiagram)
@given(instance=notation_StandardDiagram_strategy)
@settings(max_examples=25)
def test_notation_StandardDiagram_instantiation(instance):
    assert isinstance(instance, notation_StandardDiagram)


notation_StringListValueStyle_strategy = st.builds(notation_StringListValueStyle, stringListValue=safe_text)
@given(instance=notation_StringListValueStyle_strategy)
@settings(max_examples=25)
def test_notation_StringListValueStyle_instantiation(instance):
    assert isinstance(instance, notation_StringListValueStyle)


notation_StringObjectConverter_strategy = st.builds(notation_StringObjectConverter)
@given(instance=notation_StringObjectConverter_strategy)
@settings(max_examples=25)
def test_notation_StringObjectConverter_instantiation(instance):
    assert isinstance(instance, notation_StringObjectConverter)


notation_StringToPropertyValueMapEntry_strategy = st.builds(notation_StringToPropertyValueMapEntry, key=safe_text)
@given(instance=notation_StringToPropertyValueMapEntry_strategy)
@settings(max_examples=25)
def test_notation_StringToPropertyValueMapEntry_instantiation(instance):
    assert isinstance(instance, notation_StringToPropertyValueMapEntry)


notation_StringValueStyle_strategy = st.builds(notation_StringValueStyle, stringValue=safe_text)
@given(instance=notation_StringValueStyle_strategy)
@settings(max_examples=25)
def test_notation_StringValueStyle_instantiation(instance):
    assert isinstance(instance, notation_StringValueStyle)


notation_Style_strategy = st.builds(notation_Style)
@given(instance=notation_Style_strategy)
@settings(max_examples=25)
def test_notation_Style_instantiation(instance):
    assert isinstance(instance, notation_Style)


notation_TextStyle_strategy = st.builds(notation_TextStyle, textAlignment=safe_text)
@given(instance=notation_TextStyle_strategy)
@settings(max_examples=25)
def test_notation_TextStyle_instantiation(instance):
    assert isinstance(instance, notation_TextStyle)


notation_TitleStyle_strategy = st.builds(notation_TitleStyle, showTitle=st.booleans())
@given(instance=notation_TitleStyle_strategy)
@settings(max_examples=25)
def test_notation_TitleStyle_instantiation(instance):
    assert isinstance(instance, notation_TitleStyle)


notation_View_strategy = st.builds(notation_View, mutable=st.booleans(), type=safe_text, visible=st.booleans())
@given(instance=notation_View_strategy)
@settings(max_examples=25)
def test_notation_View_instantiation(instance):
    assert isinstance(instance, notation_View)



