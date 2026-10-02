#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    Alignment,
    Anchor,
    ArrowType,
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
    Enum,
    FillStyle,
    Filtering,
    FilteringStyle,
    FontStyle,
    GradientStyle,
    GuideStyle,
    ImageStyle,
    JumpLinkStatus,
    JumpLinkType,
    LayoutConstraint,
    LineStyle,
    LineType,
    Location,
    MeasurementUnit,
    NamedStyle,
    Node,
    PageStyle,
    RoundedCornersStyle,
    Routing,
    RoutingStyle,
    ShapeStyle,
    Size,
    Smoothness,
    Sorting,
    SortingDirection,
    SortingStyle,
    StringObjectConverter,
    Style,
    TextAlignment,
    TitleStyle,
    View,
    abstractmethod,
    date,
    datetime,
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
    time,
)


def test_0():
    var_3 = python_code_.ConnectorStyle()
    var_17 = python_code_.notation_PropertyValue(
        rawValue="", notation_PropertyValue49=var_3
    )
    assert isinstance(var_17, python_code_.notation_PropertyValue)


def test_1():
    var_8 = python_code_.notation_PropertyValue(rawValue={True, "jD+", -380.19})
    assert isinstance(var_8, python_code_.notation_PropertyValue)
    var_9 = python_code_.notation_CanonicalStyle
    var_8.setValue(notation_newValue=var_9)


def test_2():
    var_37 = python_code_.notation_PropertiesSetStyle(notation_PropertiesSetStyle=set())
    assert isinstance(var_37, python_code_.notation_PropertiesSetStyle)
    var_37.hasProperty(notation_propertyName=var_37)


def test_3():
    var_4 = python_code_.notation_DescriptionStyle(description=())
    assert isinstance(var_4, python_code_.notation_DescriptionStyle)
    var_48 = True
    var_50 = "EG%L ]rYb}"
    var_52 = python_code_.notation_EDataType()
    var_53 = python_code_.notation_PropertyValue(
        rawValue=var_4, notation_PropertyValue49=var_52
    )
    assert isinstance(var_53, python_code_.notation_PropertyValue)
    var_54 = var_53.getValue()
    var_55 = python_code_.notation_PropertiesSetStyle(
        notation_PropertiesSetStyle=var_54
    )
    assert isinstance(var_55, python_code_.notation_PropertiesSetStyle)
    var_55.setProperty(notation_propertyName=var_50, notation_newValue=var_48)


def test_4():
    var_5 = 2872
    var_6 = python_code_.notation_Guide(
        position=var_5, notation_Guide37={2619.47, False}, notation_Guide=var_5
    )
    assert isinstance(var_6, python_code_.notation_Guide)


def test_5():
    var_3 = python_code_.ConnectorStyle()
    python_code_.notation_NodeEntry(value=var_3, notation_NodeEntry=var_3)


def test_6():
    var_3 = python_code_.notation_DrawerStyle(collapsed=True)
    assert isinstance(var_3, python_code_.notation_DrawerStyle)
    var_4 = python_code_.notation_DescriptionStyle(description=())
    assert isinstance(var_4, python_code_.notation_DescriptionStyle)
    var_5 = python_code_.notation_NamedStyle(name=var_3)
    assert isinstance(var_5, python_code_.notation_NamedStyle)
    python_code_.notation_NodeEntry(value="P")


def test_7():
    var_5 = -262
    var_14 = True
    var_15 = python_code_.notation_View(
        visible=var_14, type=var_14, mutable=var_14, notation_View19=var_5
    )
    assert isinstance(var_15, python_code_.notation_View)
    var_16 = lambda *args, **kwargs: [1983.09, False]
    var_17 = var_15.getStyle(notation_eClass=var_16)
    var_15.getNamedStyle(notation_name=var_16, notation_eClass=var_17)


@pytest.mark.xfail(strict=True)
def test_8():
    var_2 = python_code_.notation_PropertiesSetStyle(notation_PropertiesSetStyle=set())
    assert isinstance(var_2, python_code_.notation_PropertiesSetStyle)
    var_2.hasProperty(notation_propertyName=var_2)
    var_46 = False
    var_48 = "\x0b+\\K,;2MsBsR}:r"
    var_50 = python_code_.notation_View(
        visible=var_46,
        type=var_48,
        mutable=True,
        View=var_46,
        View2=None,
        target=set(),
        notation_View17={var_48, var_2},
        notation_View19=None,
    )
    assert isinstance(var_50, python_code_.notation_View)
    python_code_.notation_Edge(sourceEdges=var_50)


def test_9():
    var_2 = python_code_.notation_PropertiesSetStyle(notation_PropertiesSetStyle=set())
    assert isinstance(var_2, python_code_.notation_PropertiesSetStyle)
    var_2.hasProperty(notation_propertyName=var_2)
    var_46 = False
    var_47 = int
    var_48 = "\x0b+\\K,;2MsBsR}:r"
    var_50 = python_code_.notation_View(
        visible=var_46,
        type=var_48,
        mutable=True,
        View=var_46,
        View2=None,
        target=set(),
        notation_View17={var_48, var_2},
        notation_View19=None,
    )
    assert isinstance(var_50, python_code_.notation_View)
    python_code_.notation_Image(data=var_47)


def test_10():
    var_2 = python_code_.View()
    var_4 = python_code_.notation_Node()
    var_5 = var_4.createLayoutConstraint(notation_eClass={-1056.58, True, -298.11})
    var_7 = "_notation_View__target_notation_Diagram__notation_Diagram57"
    var_8 = python_code_.notation_ArrowStyle(arrowSource=var_2, arrowTarget=var_7)
    assert isinstance(var_8, python_code_.notation_ArrowStyle)
    var_9 = python_code_.notation_SingleValueStyle(rawValue=True)
    assert isinstance(var_9, python_code_.notation_SingleValueStyle)
    var_9.setValue(notation_newValue=-80)
    var_11 = python_code_.notation_EDataType()
    var_13 = True
    var_14 = False
    var_15 = lambda *args, **kwargs: "None_:_notation_Edge__Edge13:Left"
    var_16 = python_code_.notation_View(
        visible=var_13,
        type=var_11,
        mutable=var_14,
        notation_View19=False,
        notation_View22=var_15,
    )
    assert isinstance(var_16, python_code_.notation_View)
    var_16.createChild(notation_eClass=var_5)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = 1110
    var_1 = python_code_.notation_Location(x=var_0, y=b"\xc4\x85\xb1\x11\x9f}")
    assert isinstance(var_1, python_code_.notation_Location)
    var_2 = "3$"
    var_3 = python_code_.notation_LineTypeStyle(lineType=var_2)
    assert isinstance(var_3, python_code_.notation_LineTypeStyle)
    var_5 = False
    var_6 = python_code_.notation_Bendpoints()
    var_7 = python_code_.notation_BasicSemanticCompartment
    var_8 = python_code_.notation_SingleValueStyle(rawValue=var_7)
    assert isinstance(var_8, python_code_.notation_SingleValueStyle)
    var_10 = python_code_.notation_View(
        visible=var_5, type=var_2, mutable=var_7, View=var_8, View2=var_2
    )
    assert isinstance(var_10, python_code_.notation_View)
    var_10.createStyle(notation_eClass=-1307.39)
    var_14 = python_code_.notation_Edge(notation_Edge=var_6, Edge13=var_10)
    assert isinstance(var_14, python_code_.notation_Edge)
    python_code_.notation_View(
        visible=var_0, type=var_2, mutable=var_5, View2=var_14, notation_View=var_5
    )


def test_12():
    var_0 = 1110
    var_1 = python_code_.notation_Location(x=var_0, y=b"\xc4\x85\xb1\x11\x9f}")
    assert isinstance(var_1, python_code_.notation_Location)
    var_2 = "3$"
    var_3 = python_code_.notation_LineTypeStyle(lineType=var_2)
    assert isinstance(var_3, python_code_.notation_LineTypeStyle)
    var_5 = True
    var_7 = python_code_.notation_DescriptionStyle
    var_8 = python_code_.notation_SingleValueStyle(rawValue=var_7)
    assert isinstance(var_8, python_code_.notation_SingleValueStyle)
    var_10 = python_code_.notation_View(
        visible=var_5, type=var_2, mutable=var_7, View=var_8, View2=var_2
    )
    assert isinstance(var_10, python_code_.notation_View)
    var_10.createStyle(notation_eClass=-1307.39)
    var_16 = python_code_.notation_MultiDiagramLinkStyle()
    var_17 = python_code_.notation_Diagram(
        name=var_7,
        measurementUnit={" N4KAO<juL@I>33E": True, "_notation_Edge__sourceEdges": True},
        notation_Diagram59=var_16,
    )
    assert isinstance(var_17, python_code_.notation_Diagram)
    var_43 = "Chamferednotation_Diagramnotation_Diagram30"
    python_code_.notation_Diagram(name=var_2, measurementUnit=var_43)


def test_13():
    var_18 = python_code_.Sorting.Manual
    var_28 = python_code_.notation_Bounds()
    var_29 = python_code_.notation_ImageStyle(
        antiAlias=b"g\x98\x16\x972\xfc\xa9J\x1d\xd6\xad\x1c2\x86",
        maintainAspectRatio=var_18,
        notation_ImageStyle=var_28,
    )
    assert isinstance(var_29, python_code_.notation_ImageStyle)


def test_14():
    var_15 = python_code_.notation_Node(notation_Node=-1)
    assert isinstance(var_15, python_code_.notation_Node)
    var_4 = var_15.createLayoutConstraint(notation_eClass=var_15)
    var_8 = python_code_.notation_PropertyValue(
        rawValue="notation_Bounds_notation_Edge__Edge13",
        notation_PropertyValue=var_4,
        notation_PropertyValue49=None,
    )
    assert isinstance(var_8, python_code_.notation_PropertyValue)
    var_9 = python_code_.notation_CanonicalStyle
    var_8.setValue(notation_newValue=var_9)


def test_15():
    var_0 = python_code_.Location()
    var_1 = python_code_.notation_Node(notation_Node15=var_0)
    assert isinstance(var_1, python_code_.notation_Node)
    var_1.createLayoutConstraint(notation_eClass=(True,))


def test_16():
    var_12 = "1,\\(4Q*,.K[H("
    var_13 = float
    var_14 = python_code_.notation_Diagram(
        name=var_13, measurementUnit=var_12, notation_Diagram=complex(-3892.5, -2030.93)
    )
    assert isinstance(var_14, python_code_.notation_Diagram)


def test_17():
    var_0 = python_code_.DecorationNode()
    var_2 = False
    var_4 = python_code_.notation_Edge(targetEdges=var_0)
    assert isinstance(var_4, python_code_.notation_Edge)
    var_11 = "EGL ]rYb}"
    var_12 = True
    var_13 = python_code_.notation_RoutingStyle(
        routing=var_4,
        smoothness=var_11,
        avoidObstructions=var_4,
        closestDistance=var_2,
        jumpLinkStatus=var_2,
        jumpLinkType=complex(4100.0, -1235.44),
        jumpLinksReverse=var_12,
    )
    assert isinstance(var_13, python_code_.notation_RoutingStyle)
    var_4.createSourceAnchor(notation_eClass=None)


def test_18():
    var_0 = "~Cn%$hQp"
    var_1 = python_code_.notation_DoubleListValueStyle(doubleListValue=var_0)
    assert isinstance(var_1, python_code_.notation_DoubleListValueStyle)
    var_2 = python_code_.Filtering
    var_3 = python_code_.notation_DrawerStyle(collapsed=var_2)
    assert isinstance(var_3, python_code_.notation_DrawerStyle)
    var_4 = python_code_.notation_DescriptionStyle(description=())
    assert isinstance(var_4, python_code_.notation_DescriptionStyle)
    var_5 = python_code_.notation_NamedStyle(name=var_3)
    assert isinstance(var_5, python_code_.notation_NamedStyle)
    var_8 = python_code_.notation_NodeEntry(value=var_2)
    var_11 = True
    var_12 = "V\x0b"
    var_13 = False
    var_14 = python_code_.notation_RoutingStyle(
        routing=var_0,
        smoothness=var_0,
        avoidObstructions=var_11,
        closestDistance=var_0,
        jumpLinkStatus=var_12,
        jumpLinkType=var_8,
        jumpLinksReverse=var_13,
    )
    assert isinstance(var_14, python_code_.notation_RoutingStyle)
    var_15 = python_code_.notation_StringObjectConverter()
    var_15.getStringFromObject(notation_objectValue=var_0)
    var_17 = python_code_.notation_Edge(
        targetEdges=var_3, notation_Edge=var_2, notation_Edge7=[True]
    )
    assert isinstance(var_17, python_code_.notation_Edge)
    var_50 = python_code_.notation_SingleValueStyle(rawValue=var_2)
    assert isinstance(var_50, python_code_.notation_SingleValueStyle)


def test_19():
    python_code_.ConnectorStyle()


def test_20():
    var_18 = python_code_.Sorting.Manual
    python_code_.notation_StringObjectConverter()
    var_24 = python_code_.notation_Bounds()
    var_25 = python_code_.notation_ImageStyle(
        antiAlias=b"g\x98\x16\x972\xfc\xa9J\x1d\xd6\xad\x1c2\x86",
        maintainAspectRatio=var_18,
        notation_ImageStyle=var_24,
    )
    assert isinstance(var_25, python_code_.notation_ImageStyle)


def test_21():
    var_0 = 628
    var_1 = python_code_.notation_Size(width=var_0, height=var_0)
    assert isinstance(var_1, python_code_.notation_Size)
    var_4 = 2065
    var_5 = -1875
    var_8 = lambda *args, **kwargs: []
    var_9 = "Normal"
    var_10 = True
    var_11 = python_code_.notation_FontStyle(
        underline=var_8,
        strikeThrough=var_8,
        fontColor=var_0,
        fontName=var_9,
        fontHeight=var_4,
        bold=var_10,
        italic=var_5,
    )
    assert isinstance(var_11, python_code_.notation_FontStyle)


def test_22():
    var_12 = "1,\\(4Q*,.K[H("
    var_18 = python_code_.notation_DoubleListValueStyle
    var_20 = -3591
    var_21 = python_code_.notation_PageStyle(
        pageWidth=var_18, pageHeight=var_20, pageX=var_12, pageY=var_20
    )
    assert isinstance(var_21, python_code_.notation_PageStyle)
    var_22 = python_code_.notation_PropertyValue(rawValue=())
    assert isinstance(var_22, python_code_.notation_PropertyValue)


def test_23():
    var_2 = python_code_.JumpLinkType.Semicircle
    var_17 = True
    var_18 = python_code_.notation_DoubleListValueStyle
    var_19 = python_code_.notation_FontStyle(
        underline=var_17,
        strikeThrough=var_2,
        fontColor=b"\x7fp\xff\xfd\x84=N\xae\x15",
        fontName={"": "G~\x0b ", ";pU5\tk-q\x0c": 0, "Himetric": -362},
        fontHeight={
            "None_ Ascending": "v?h",
            "_notation_Node__notation_Node25": -2283.63,
            "_notation_Node__notation_Node40Descendingnotation_EObjectnotation_Node25": "notation_EDataType",
        },
        bold=var_18,
        italic=b"\xea",
    )
    assert isinstance(var_19, python_code_.notation_FontStyle)


def test_24():
    var_0 = "~Cn%$hQp"
    var_1 = python_code_.notation_DoubleListValueStyle(doubleListValue=var_0)
    assert isinstance(var_1, python_code_.notation_DoubleListValueStyle)
    var_2 = python_code_.Filtering
    var_3 = python_code_.notation_DrawerStyle(collapsed=var_2)
    assert isinstance(var_3, python_code_.notation_DrawerStyle)
    var_4 = python_code_.notation_DescriptionStyle(description=())
    assert isinstance(var_4, python_code_.notation_DescriptionStyle)
    var_5 = python_code_.notation_NamedStyle(name=var_3)
    assert isinstance(var_5, python_code_.notation_NamedStyle)
    var_8 = python_code_.notation_NodeEntry(value=var_2)
    var_10 = python_code_.Sorting.Manual
    var_11 = True
    var_12 = "V\x0b"
    var_13 = False
    var_14 = python_code_.notation_RoutingStyle(
        routing=var_0,
        smoothness=var_0,
        avoidObstructions=var_11,
        closestDistance=var_0,
        jumpLinkStatus=var_12,
        jumpLinkType=var_8,
        jumpLinksReverse=var_13,
    )
    assert isinstance(var_14, python_code_.notation_RoutingStyle)
    var_15 = python_code_.notation_StringObjectConverter()
    var_15.getStringFromObject(notation_objectValue=var_0)
    var_17 = python_code_.notation_Edge(
        targetEdges=var_3, notation_Edge=var_2, notation_Edge7=[True]
    )
    assert isinstance(var_17, python_code_.notation_Edge)
    var_17.createTargetAnchor(notation_eClass=complex(-315.0, -62.36))
    var_19 = python_code_.notation_Bounds()
    var_20 = python_code_.notation_ImageStyle(
        antiAlias=b"g\x98\x16\x972\xfc\xa9J\x1d\xd6\xad\x1c2\x86",
        maintainAspectRatio=var_10,
        notation_ImageStyle=var_19,
    )
    assert isinstance(var_20, python_code_.notation_ImageStyle)
    var_23 = python_code_.notation_SingleValueStyle(rawValue=var_2)
    assert isinstance(var_23, python_code_.notation_SingleValueStyle)
    var_23.setValue(notation_newValue=var_2)


def test_25():
    var_0 = python_code_.notation_Shape
    python_code_.notation_Image(data=var_0)


def test_26():
    var_0 = True
    var_1 = True
    var_2 = 1173
    var_3 = "<g))h+nZ"
    var_4 = 490
    var_5 = False
    var_6 = python_code_.notation_FontStyle(
        underline=var_0,
        strikeThrough=var_1,
        fontColor=var_2,
        fontName=var_3,
        fontHeight=var_4,
        bold=var_5,
        italic=var_2,
    )
    assert isinstance(var_6, python_code_.notation_FontStyle)
    var_7 = python_code_.notation_DrawerStyle(collapsed=var_5)
    assert isinstance(var_7, python_code_.notation_DrawerStyle)
    var_8 = python_code_.notation_DoubleValueStyle(doubleValue=False)
    assert isinstance(var_8, python_code_.notation_DoubleValueStyle)
    var_9 = python_code_.notation_BooleanListValueStyle
    var_10 = python_code_.notation_TitleStyle(showTitle=var_9)
    assert isinstance(var_10, python_code_.notation_TitleStyle)
    var_13 = "targetEdges"
    var_14 = "IF*2"
    var_15 = python_code_.notation_Diagram(
        name=var_13, measurementUnit=var_14, notation_Diagram27=(-170.86,)
    )
    assert isinstance(var_15, python_code_.notation_Diagram)


def test_27():
    var_5 = python_code_.JumpLinkType.Chamfered
    var_6 = "Left-All"
    var_7 = python_code_.notation_PropertyValue(
        rawValue=var_6, notation_PropertyValue49=var_5
    )
    assert isinstance(var_7, python_code_.notation_PropertyValue)
    var_8 = var_7.setValue(
        notation_newValue={-500.95, True, "C^2,\x0bMT\tgIJnM4D(=#\\"}
    )
    var_9 = python_code_.notation_FilteringStyle(
        filtering=2127.29,
        filteringKeys=b"9\n@\xe6\x99\xd6",
        notation_FilteringStyle=var_8,
    )
    assert isinstance(var_9, python_code_.notation_FilteringStyle)
    var_12 = python_code_.notation_ArrowStyle(
        arrowSource=var_6, arrowTarget=complex(1162.29, -636.1)
    )
    assert isinstance(var_12, python_code_.notation_ArrowStyle)
    var_13 = python_code_.notation_RelativeBendpoints(points=-665.03)
    assert isinstance(var_13, python_code_.notation_RelativeBendpoints)
    var_14 = python_code_.Alignment.Right
    var_15 = python_code_.notation_ConnectorStyle()
    var_16 = python_code_.notation_HintedDiagramLinkStyle(hint=var_6)
    assert isinstance(var_16, python_code_.notation_HintedDiagramLinkStyle)
    var_18 = 120
    var_19 = python_code_.notation_View
    var_20 = python_code_.notation_PageStyle(
        pageWidth=var_18, pageHeight=var_18, pageX=var_18, pageY=var_19
    )
    assert isinstance(var_20, python_code_.notation_PageStyle)
    var_21 = True
    var_22 = python_code_.notation_FontStyle(
        underline=var_21,
        strikeThrough=var_14,
        fontColor=var_21,
        fontName="\t4r0\x0c^K.$/&Wm*ZaG",
        fontHeight=var_21,
        bold="(4R/llt^i$",
        italic=var_21,
    )
    assert isinstance(var_22, python_code_.notation_FontStyle)
    var_23 = python_code_.notation_PropertiesSetStyle()
    assert isinstance(var_23, python_code_.notation_PropertiesSetStyle)
    var_23.getProperty(notation_propertyName=var_15)


def test_28():
    var_5 = python_code_.JumpLinkType.Chamfered
    var_6 = "Left-All"
    var_7 = python_code_.notation_PropertyValue(
        rawValue=var_6, notation_PropertyValue49=var_5
    )
    assert isinstance(var_7, python_code_.notation_PropertyValue)
    var_8 = var_7.setValue(
        notation_newValue={-500.95, True, "C^2,\x0bMT\tgIJnM4D(=#\\"}
    )
    var_9 = python_code_.notation_FilteringStyle(
        filtering=2127.29,
        filteringKeys=b"9\n@\xe6\x99\xd6",
        notation_FilteringStyle=var_8,
    )
    assert isinstance(var_9, python_code_.notation_FilteringStyle)
    var_13 = python_code_.notation_RelativeBendpoints(points=-665.03)
    assert isinstance(var_13, python_code_.notation_RelativeBendpoints)
    var_16 = python_code_.notation_HintedDiagramLinkStyle(hint=var_6)
    assert isinstance(var_16, python_code_.notation_HintedDiagramLinkStyle)


def test_29():
    var_2 = python_code_.notation_PropertiesSetStyle(notation_PropertiesSetStyle=set())
    assert isinstance(var_2, python_code_.notation_PropertiesSetStyle)
    var_2.hasProperty(notation_propertyName=var_2)
    python_code_.notation_Image(data=complex(-5002.49738, 1651.019404))
    var_8 = "iIl:"
    var_13 = python_code_.notation_IdentityAnchor(id=var_8)
    assert isinstance(var_13, python_code_.notation_IdentityAnchor)
    var_20 = python_code_.notation_PropertyValue(
        rawValue=3085.73,
        notation_PropertyValue49=b'\xc1\xfb\xcb\x83\xed\xee\xc9\xf3\xa4o\xfb4"[\x9b\xc5',
    )
    assert isinstance(var_20, python_code_.notation_PropertyValue)


def test_30():
    var_0 = python_code_.DecorationNode()
    var_1 = python_code_.notation_ListCompartment()
    var_4 = python_code_.notation_Edge(targetEdges=var_0)
    assert isinstance(var_4, python_code_.notation_Edge)
    var_4.createSourceAnchor(notation_eClass=None)
    var_15 = "56*Vjf4"
    var_16 = var_4.createBendpoints(notation_eClass=var_1)
    var_17 = python_code_.notation_FilteringStyle(
        filtering=complex(2197.543, -352.4018205),
        filteringKeys=var_15,
        notation_FilteringStyle=var_16,
    )
    assert isinstance(var_17, python_code_.notation_FilteringStyle)


def test_31():
    python_code_.notation_Image(data=complex(-5002.49738, 1651.019404))
    var_17 = "iIl:"
    var_18 = python_code_.Sorting.Automatic
    var_21 = python_code_.notation_IdentityAnchor(id=var_17)
    assert isinstance(var_21, python_code_.notation_IdentityAnchor)
    var_35 = 0
    var_36 = python_code_.notation_FillStyle(fillColor=var_35, transparency=var_18)
    assert isinstance(var_36, python_code_.notation_FillStyle)
    var_28 = python_code_.notation_PropertyValue(
        rawValue=3085.73,
        notation_PropertyValue49=b'\xc1\xfb\xcb\x83\xed\xee\xc9\xf3\xa4o\xfb4"[\x9b\xc5',
    )
    assert isinstance(var_28, python_code_.notation_PropertyValue)
    var_29 = python_code_.notation_EDataType()
    var_31 = True
    var_32 = False
    var_33 = lambda *args, **kwargs: "None_:_notation_Edge__Edge13:Left"
    var_34 = python_code_.notation_View(
        visible=var_31,
        type=var_29,
        mutable=var_32,
        notation_View19=False,
        notation_View22=var_33,
    )
    assert isinstance(var_34, python_code_.notation_View)


def test_32():
    var_0 = python_code_.notation_ImageBufferStyle()
    var_2 = python_code_.notation_PropertiesSetStyle(notation_PropertiesSetStyle=set())
    assert isinstance(var_2, python_code_.notation_PropertiesSetStyle)
    var_2.hasProperty(notation_propertyName=var_2)
    python_code_.notation_Image(data=complex(-5002.49738, 1651.019404))
    var_8 = "iIl:"
    var_13 = python_code_.notation_IdentityAnchor(id=var_8)
    assert isinstance(var_13, python_code_.notation_IdentityAnchor)
    var_20 = python_code_.notation_PropertyValue(
        rawValue=3085.73,
        notation_PropertyValue49=b'\xc1\xfb\xcb\x83\xed\xee\xc9\xf3\xa4o\xfb4"[\x9b\xc5',
    )
    assert isinstance(var_20, python_code_.notation_PropertyValue)
    var_49 = python_code_.notation_IntListValueStyle(intListValue=var_0)
    assert isinstance(var_49, python_code_.notation_IntListValueStyle)


@pytest.mark.xfail(strict=True)
def test_33():
    var_4 = "^3_!HS(9B$nL8\n"
    var_5 = python_code_.notation_StringToPropertyValueMapEntry(key=var_4)
    var_6 = python_code_.notation_PropertiesSetStyle()
    assert isinstance(var_6, python_code_.notation_PropertiesSetStyle)
    var_7 = lambda *args, **kwargs: []
    var_6.createProperty(
        notation_propertyName=("LJ>HJ", -360.5), notation_initialValue=var_7
    )
    var_10 = python_code_.notation_StringListValueStyle(stringListValue=set())
    assert isinstance(var_10, python_code_.notation_StringListValueStyle)
    var_12 = python_code_.notation_StringObjectConverter()
    var_13 = var_12.getObjectFromString(notation_stringValue=var_6)
    var_16 = False
    var_17 = python_code_.notation_EObject()
    python_code_.notation_View(
        visible="`f4",
        type=var_13,
        mutable=var_16,
        View=True,
        notation_View19=var_17,
        notation_View24=var_5,
    )


def test_34():
    var_0 = python_code_.DecorationNode()
    var_4 = python_code_.notation_Edge(targetEdges=var_0)
    assert isinstance(var_4, python_code_.notation_Edge)
    var_14 = python_code_.notation_StringListValueStyle(stringListValue=set())
    assert isinstance(var_14, python_code_.notation_StringListValueStyle)
    var_9 = "View"
    var_10 = python_code_.notation_ListValueStyle(rawValuesList=var_9)
    assert isinstance(var_10, python_code_.notation_ListValueStyle)


def test_35():
    var_2 = python_code_.JumpLinkType.Semicircle
    var_24 = "_notation_View__notation_View24 notation_EObject notation_EObject notation_DiagramLinkStyle"
    var_25 = python_code_.notation_IdentityAnchor(id=var_24)
    assert isinstance(var_25, python_code_.notation_IdentityAnchor)
    var_31 = 2401
    var_32 = python_code_.notation_FillStyle(fillColor=None, transparency=var_31)
    assert isinstance(var_32, python_code_.notation_FillStyle)
    var_33 = python_code_.notation_PropertiesSetStyle()
    assert isinstance(var_33, python_code_.notation_PropertiesSetStyle)
    var_34 = python_code_.notation_SingleValueStyle(rawValue={})
    assert isinstance(var_34, python_code_.notation_SingleValueStyle)
    var_34.getValue()
    var_38 = True
    var_39 = python_code_.notation_DrawerStyle(collapsed=var_38)
    assert isinstance(var_39, python_code_.notation_DrawerStyle)
    var_40 = python_code_.notation_StringObjectConverter()
    var_40.getStringFromObject(notation_objectValue={-1154, 1, True})
    var_43 = True
    var_44 = python_code_.notation_TitleStyle(showTitle=var_43)
    assert isinstance(var_44, python_code_.notation_TitleStyle)
    var_47 = python_code_.LineType
    var_48 = python_code_.notation_DoubleValueStyle(doubleValue=var_47)
    assert isinstance(var_48, python_code_.notation_DoubleValueStyle)
    var_33.hasProperty(notation_propertyName=var_2)


def test_36():
    var_20 = python_code_.notation_Ratio(value={})
    assert isinstance(var_20, python_code_.notation_Ratio)


def test_37():
    var_5 = python_code_.JumpLinkType.Chamfered
    var_6 = "8@D"
    var_7 = python_code_.notation_PropertyValue(
        rawValue=var_6, notation_PropertyValue49=var_5
    )
    assert isinstance(var_7, python_code_.notation_PropertyValue)
    var_7.setValue(notation_newValue={-500.95, True, "C^2,\x0bMT\tgIJnM4D(=#\\"})
    var_9 = python_code_.notation_FilteringStyle(
        filtering="notation_LayoutConstraint-Horizontal",
        filteringKeys=var_6,
        notation_FilteringStyle={True, -1447.66},
    )
    assert isinstance(var_9, python_code_.notation_FilteringStyle)
    var_26 = python_code_.notation_IdentityAnchor(id=var_6)
    assert isinstance(var_26, python_code_.notation_IdentityAnchor)
    var_33 = python_code_.notation_PropertyValue(
        rawValue=3085.73,
        notation_PropertyValue49=b'\xc1\xfb\xcb\x83\xed\xee\xc9\xf3\xa4o\xfb4"[\x9b\xc5',
    )
    assert isinstance(var_33, python_code_.notation_PropertyValue)


def test_38():
    var_67 = False
    var_68 = python_code_.notation_BooleanValueStyle(booleanValue=var_67)
    assert isinstance(var_68, python_code_.notation_BooleanValueStyle)
    python_code_.notation_StringObjectConverter()


def test_39():
    var_60 = ""
    python_code_.notation_StringToPropertyValueMapEntry(key=var_60)


def test_40():
    var_6 = python_code_.notation_Anchor()
    var_9 = python_code_.notation_IntValueStyle(intValue=var_6)
    assert isinstance(var_9, python_code_.notation_IntValueStyle)


def test_41():
    var_0 = python_code_.notation_DescriptionStyle(description=None)
    assert isinstance(var_0, python_code_.notation_DescriptionStyle)
    var_1 = python_code_.notation_PropertiesSetStyle()
    assert isinstance(var_1, python_code_.notation_PropertiesSetStyle)
    var_2 = python_code_.notation_TextStyle(textAlignment=True)
    assert isinstance(var_2, python_code_.notation_TextStyle)
    var_3 = 2666
    var_4 = python_code_.notation_Location(x=664.14, y=var_3)
    assert isinstance(var_4, python_code_.notation_Location)
    var_8 = 4156
    var_9 = python_code_.notation_IntListValueStyle(intListValue=var_8)
    assert isinstance(var_9, python_code_.notation_IntListValueStyle)
    var_11 = ",tAKS"
    var_12 = python_code_.notation_PropertyValue(rawValue=var_11)
    assert isinstance(var_12, python_code_.notation_PropertyValue)
    var_12.getValue()
    var_19 = lambda *args, **kwargs: "O<N"
    var_20 = python_code_.notation_ListValueStyle(rawValuesList=var_19)
    assert isinstance(var_20, python_code_.notation_ListValueStyle)
    var_26 = python_code_.notation_DoubleListValueStyle(doubleListValue=var_19)
    assert isinstance(var_26, python_code_.notation_DoubleListValueStyle)
    var_27 = 1691
    var_28 = python_code_.notation_LineStyle(lineColor=var_27, lineWidth=())
    assert isinstance(var_28, python_code_.notation_LineStyle)
    var_1.hasProperty(notation_propertyName=var_19)


def test_42():
    var_4 = python_code_.Smoothness.Normal
    var_8 = python_code_.notation_PropertyValue(
        rawValue="notation_Bounds_notation_Edge__Edge13",
        notation_PropertyValue=var_4,
        notation_PropertyValue49=None,
    )
    assert isinstance(var_8, python_code_.notation_PropertyValue)
    var_9 = python_code_.notation_CanonicalStyle
    var_8.setValue(notation_newValue=var_9)


def test_43():
    var_0 = python_code_.DecorationNode()
    var_2 = False
    var_4 = python_code_.notation_Edge(targetEdges=var_0)
    assert isinstance(var_4, python_code_.notation_Edge)
    var_5 = float
    var_11 = "EGL ]rYb}"
    var_12 = True
    var_13 = python_code_.notation_RoutingStyle(
        routing=var_4,
        smoothness=var_11,
        avoidObstructions=var_4,
        closestDistance=var_2,
        jumpLinkStatus=var_2,
        jumpLinkType=complex(4100.0, -1235.44),
        jumpLinksReverse=var_12,
    )
    assert isinstance(var_13, python_code_.notation_RoutingStyle)
    var_4.createSourceAnchor(notation_eClass=None)
    var_15 = python_code_.notation_PageStyle(
        pageWidth=var_5, pageHeight=var_2, pageX=var_5, pageY=var_2
    )
    assert isinstance(var_15, python_code_.notation_PageStyle)
    var_16 = python_code_.notation_ByteArrayValueStyle(byteArrayValue=var_11)
    assert isinstance(var_16, python_code_.notation_ByteArrayValueStyle)
