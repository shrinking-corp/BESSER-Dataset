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
    AbstractFigure,
    AbstractNode,
    Alignment,
    Border,
    Color,
    ColorConstants,
    ConnectionFigure,
    CustomClass,
    CustomFigure,
    DecorationFigure,
    DiagramElement,
    Direction,
    Enum,
    Figure,
    Font,
    FontStyle,
    Identity,
    Layout,
    LayoutData,
    Layoutable,
    LineKind,
    Node,
    Polygon,
    Polyline,
    RealFigure,
    Shape,
    VisualFacet,
    abstractmethod,
    date,
    datetime,
    gmfgraph_AbstractFigure,
    gmfgraph_AbstractNode,
    gmfgraph_AlignmentFacet,
    gmfgraph_BasicFont,
    gmfgraph_Border,
    gmfgraph_BorderLayout,
    gmfgraph_BorderLayoutData,
    gmfgraph_BorderRef,
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
    gmfgraph_LayoutRef,
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
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_67 = python_code_.CustomClass()
    var_68 = True
    var_69 = python_code_.gmfgraph_GridLayout(numColumns=var_67, equalWidth=var_68)
    assert isinstance(var_69, python_code_.gmfgraph_GridLayout)
    var_78 = 627
    var_80 = python_code_.gmfgraph_Figure()
    python_code_.gmfgraph_Dimension(
        dx=var_68,
        dy=var_78,
        gmfgraph_Dimension=None,
        gmfgraph_Dimension40=var_80,
        gmfgraph_Dimension93=var_69,
    )


def test_1():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_45 = python_code_.CustomClass()
    var_46 = True
    var_47 = python_code_.gmfgraph_GridLayout(numColumns=var_45, equalWidth=var_46)
    assert isinstance(var_47, python_code_.gmfgraph_GridLayout)
    var_49 = -1697
    var_57 = -913
    var_59 = True
    var_60 = '\\K4"|q<Q-80D`'
    var_62 = 757
    var_63 = python_code_.gmfgraph_GridLayoutData(
        grabExcessHorizontalSpace=b"O\xba\x18\xf8in\x96#5\xb8",
        grabExcessVerticalSpace=var_59,
        verticalAlignment=var_60,
        horizontalAlignment=var_60,
        verticalSpan=var_62,
        horizontalSpan=var_49,
        horizontalIndent=var_57,
    )
    assert isinstance(var_63, python_code_.gmfgraph_GridLayoutData)


def test_2():
    var_0 = -1515
    var_1 = python_code_.gmfgraph_RGBColor(
        red=var_0, green=b'U\xe3t\xe4\xc3"K_\x10N\x9b\x9c\x01\x81', blue=var_0
    )
    assert isinstance(var_1, python_code_.gmfgraph_RGBColor)
    var_2 = python_code_.DiagramElement
    var_3 = "gmfgraph_DiagramLabel_gmfgraph_Shape__gmfgraph_Shape"
    var_4 = True
    var_5 = python_code_.gmfgraph_FlowLayout(
        forceSingleLine=var_2,
        majorAlignment=var_1,
        minorAlignment=var_3,
        majorSpacing=var_0,
        minorSpacing=var_0,
        vertical=complex(1750.0, 3259.7551528),
        matchMinorSize=var_4,
    )
    assert isinstance(var_5, python_code_.gmfgraph_FlowLayout)
    var_10 = python_code_.CustomClass()
    var_11 = True
    var_12 = python_code_.gmfgraph_GridLayout(numColumns=var_10, equalWidth=var_11)
    assert isinstance(var_12, python_code_.gmfgraph_GridLayout)
    var_36 = -912
    python_code_.gmfgraph_GridLayout(
        numColumns=var_36, equalWidth=var_2, gmfgraph_GridLayout=var_2
    )


def test_3():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_49 = -1697
    var_57 = -887
    var_59 = True
    var_60 = '\\K4"|q<Q-80D`'
    var_62 = 758
    var_63 = python_code_.gmfgraph_GridLayoutData(
        grabExcessHorizontalSpace=b"O\xba\x18\xf8in\x96#5\xb8",
        grabExcessVerticalSpace=var_59,
        verticalAlignment=var_60,
        horizontalAlignment=var_60,
        verticalSpan=var_62,
        horizontalSpan=var_49,
        horizontalIndent=var_57,
    )
    assert isinstance(var_63, python_code_.gmfgraph_GridLayoutData)


def test_4():
    var_1 = python_code_.gmfgraph_LineBorder(width=-598)
    assert isinstance(var_1, python_code_.gmfgraph_LineBorder)
    var_40 = "_gmfgraph_FigureGallery__gmfgraph_FigureGallery10"
    var_41 = python_code_.gmfgraph_Label(text=var_40)
    assert isinstance(var_41, python_code_.gmfgraph_Label)


def test_5():
    var_1 = -1
    var_17 = python_code_.gmfgraph_LineBorder(
        width=var_1, gmfgraph_LineBorder=[".e<$kc#*", False, -4066]
    )
    assert isinstance(var_17, python_code_.gmfgraph_LineBorder)


def test_6():
    python_code_.gmfgraph_FigureAccessor(
        accessor="g5r7pXj[.\x0brbr", gmfgraph_FigureAccessor=None
    )


def test_7():
    var_0 = -1515
    var_1 = python_code_.gmfgraph_RGBColor(
        red=var_0, green=b'U\xe3t\xe4\xc3"K_\x10N\x9b\x9c\x01\x81', blue=var_0
    )
    assert isinstance(var_1, python_code_.gmfgraph_RGBColor)
    var_2 = python_code_.DiagramElement
    var_3 = "gmfgraph_DiagramLabel_gmfgraph_Shape__gmfgraph_Shape"
    var_4 = True
    var_5 = python_code_.gmfgraph_FlowLayout(
        forceSingleLine=var_2,
        majorAlignment=var_1,
        minorAlignment=var_3,
        majorSpacing=var_0,
        minorSpacing=var_0,
        vertical=complex(1750.0, 3259.7551528),
        matchMinorSize=var_4,
    )
    assert isinstance(var_5, python_code_.gmfgraph_FlowLayout)
    var_10 = python_code_.CustomClass()
    var_11 = True
    var_12 = python_code_.gmfgraph_GridLayout(numColumns=var_10, equalWidth=var_11)
    assert isinstance(var_12, python_code_.gmfgraph_GridLayout)
    var_27 = True
    var_28 = "\x0b,#u7`SXv*h("
    var_29 = python_code_.gmfgraph_GridLayoutData(
        grabExcessHorizontalSpace=var_27,
        grabExcessVerticalSpace=True,
        verticalAlignment=var_28,
        horizontalAlignment=var_28,
        verticalSpan=var_2,
        horizontalSpan=var_2,
        horizontalIndent=var_28,
    )
    assert isinstance(var_29, python_code_.gmfgraph_GridLayoutData)
    python_code_.gmfgraph_FigureAccessor(accessor=var_28, gmfgraph_FigureAccessor=var_2)


def test_8():
    var_2 = -1406
    var_7 = False
    python_code_.gmfgraph_CustomAttribute(
        name=None,
        value=var_2,
        directAccess=var_7,
        multiStatementValue=(
            "e{0\t(C",
            "gmfgraph_MarginBorder",
            "gmfgraph_Figure-LINE_SOLID",
        ),
    )


def test_9():
    var_0 = python_code_.DiagramElement()
    var_2 = python_code_.gmfgraph_Label(text=False)
    assert isinstance(var_2, python_code_.gmfgraph_Label)
    var_5 = python_code_.gmfgraph_Border
    var_9 = python_code_.gmfgraph_PolylineConnection()
    var_14 = python_code_.gmfgraph_BorderLayoutData(alignment=var_9, vertical=var_5)
    assert isinstance(var_14, python_code_.gmfgraph_BorderLayoutData)
    var_15 = python_code_.gmfgraph_CustomClass(qualifiedClassName=var_0)
    assert isinstance(var_15, python_code_.gmfgraph_CustomClass)


def test_10():
    var_1 = 957
    var_2 = -1406
    var_3 = -237
    var_4 = python_code_.gmfgraph_Figure()
    python_code_.gmfgraph_Insets(
        top=var_1, left=var_2, bottom=var_2, right=var_3, gmfgraph_Insets=var_4
    )
    var_7 = False
    python_code_.gmfgraph_CustomAttribute(
        name=None,
        value=var_2,
        directAccess=var_7,
        multiStatementValue=(
            "e{0\t(C",
            "gmfgraph_MarginBorder",
            "gmfgraph_Figure-LINE_SOLID",
        ),
    )
    var_53 = "_gmfgraph_FigureGallery__gmfgraph_FigureGallery10"
    var_54 = python_code_.gmfgraph_Label(text=var_53)
    assert isinstance(var_54, python_code_.gmfgraph_Label)


def test_11():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_36 = python_code_.gmfgraph_Figure()
    var_37 = "gmfgraph_GridLayoutData"
    var_40 = python_code_.gmfgraph_LabeledContainer()
    var_48 = python_code_.gmfgraph_Dimension(
        dx=74,
        dy=-675,
        gmfgraph_Dimension=None,
        gmfgraph_Dimension102=None,
        gmfgraph_Dimension85=var_37,
        gmfgraph_Dimension90=None,
        gmfgraph_Dimension95=None,
        gmfgraph_Dimension100=var_36,
    )
    var_49 = 541
    var_50 = python_code_.gmfgraph_MarginBorder()
    python_code_.gmfgraph_Insets(
        top=var_48, left=True, bottom=var_40, right=var_49, gmfgraph_Insets77=var_50
    )
    var_55 = python_code_.gmfgraph_RoundedRectangle(
        cornerWidth=-1281, cornerHeight=var_49
    )
    assert isinstance(var_55, python_code_.gmfgraph_RoundedRectangle)


def test_12():
    var_0 = lambda *args, **kwargs: False
    var_3 = True
    var_6 = "gmfgraph_GridLayoutData"
    var_7 = python_code_.gmfgraph_GradientFacet(direction=var_6)
    assert isinstance(var_7, python_code_.gmfgraph_GradientFacet)
    var_14 = python_code_.gmfgraph_DefaultSizeFacet()
    var_15 = python_code_.gmfgraph_CustomConnection()
    python_code_.gmfgraph_Dimension(
        dx=var_3,
        dy=var_0,
        gmfgraph_Dimension102=var_14,
        gmfgraph_Dimension95=var_0,
        gmfgraph_Dimension100=750.44,
    )
    var_32 = "_gmfgraph_FigureGallery__gmfgraph_FigureGallery10"
    var_33 = python_code_.gmfgraph_Label(text=var_32)
    assert isinstance(var_33, python_code_.gmfgraph_Label)
    python_code_.gmfgraph_Point(x="blue", y=var_0)
    var_36 = python_code_.gmfgraph_GeneralFacet(identifier=var_15, data=1170)
    assert isinstance(var_36, python_code_.gmfgraph_GeneralFacet)


def test_13():
    var_72 = '"vQzH0*'
    var_74 = python_code_.CustomFigure
    var_76 = -2057
    var_77 = ""
    var_78 = python_code_.gmfgraph_BasicFont(
        faceName=var_72, height=var_76, style=var_77
    )
    assert isinstance(var_78, python_code_.gmfgraph_BasicFont)
    var_80 = python_code_.gmfgraph_Identity(name=var_72)
    assert isinstance(var_80, python_code_.gmfgraph_Identity)
    var_81 = True
    var_82 = python_code_.gmfgraph_CustomAttribute(
        name=var_77, value=var_72, directAccess=var_74, multiStatementValue=var_81
    )
    var_87 = python_code_.gmfgraph_Figure()
    var_89 = set()
    var_90 = python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_72,
        gmfgraph_FigureGallery=var_77,
        gmfgraph_FigureGallery12=var_89,
    )
    assert isinstance(var_90, python_code_.gmfgraph_FigureGallery)
    var_91 = python_code_.gmfgraph_GridLayout(
        numColumns=var_74,
        equalWidth="_gmfgraph_FigureGallery__gmfgraph_FigureGallery12",
    )
    assert isinstance(var_91, python_code_.gmfgraph_GridLayout)
    var_92 = python_code_.gmfgraph_BorderRef
    python_code_.gmfgraph_Dimension(
        dx=var_81,
        dy={},
        gmfgraph_Dimension40=var_92,
        gmfgraph_Dimension43=var_87,
        gmfgraph_Dimension100=var_82,
    )
    var_97 = python_code_.gmfgraph_LineBorder(width=var_77)
    assert isinstance(var_97, python_code_.gmfgraph_LineBorder)
    var_99 = python_code_.gmfgraph_Figure()
    python_code_.gmfgraph_Dimension(
        dx=3,
        dy=var_76,
        gmfgraph_Dimension=None,
        gmfgraph_Dimension43=var_99,
        gmfgraph_Dimension90=None,
    )
    var_119 = "\\sm{xW"
    var_120 = python_code_.gmfgraph_Node(
        resizeConstraint=144, affixedParentSide=var_119
    )
    assert isinstance(var_120, python_code_.gmfgraph_Node)


def test_14():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_37 = python_code_.Shape()
    var_38 = False
    var_39 = (True, "gmfgraph_Dimension90", 1389)
    var_40 = python_code_.gmfgraph_DiagramLabel(elementIcon=var_38, external=var_39)
    assert isinstance(var_40, python_code_.gmfgraph_DiagramLabel)
    var_41 = 3342
    var_42 = python_code_.gmfgraph_LayoutData
    python_code_.gmfgraph_Point(
        x=var_41,
        y=var_40,
        gmfgraph_Point=var_37,
        gmfgraph_Point64=var_42,
        gmfgraph_Point97=-1051,
    )


@pytest.mark.xfail(strict=True)
def test_15():
    var_41 = python_code_.gmfgraph_Label(text=False)
    assert isinstance(var_41, python_code_.gmfgraph_Label)
    var_48 = False
    var_49 = python_code_.gmfgraph_DiagramLabel(elementIcon=3, external=var_48)
    assert isinstance(var_49, python_code_.gmfgraph_DiagramLabel)
    var_58 = python_code_.gmfgraph_FigureDescriptor()
    var_66 = python_code_.gmfgraph_Compartment(collapsible=var_48, needsTitle=var_48)
    assert isinstance(var_66, python_code_.gmfgraph_Compartment)
    var_68 = python_code_.gmfgraph_AlignmentFacet(alignment=None)
    assert isinstance(var_68, python_code_.gmfgraph_AlignmentFacet)
    python_code_.gmfgraph_ChildAccess(
        accessor={-811.08}, gmfgraph_ChildAccess25=var_66, accessors=var_58
    )


def test_16():
    var_6 = python_code_.gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert isinstance(var_6, python_code_.gmfgraph_Compartment)


@pytest.mark.xfail(strict=True)
def test_17():
    var_1 = python_code_.gmfgraph_Figure()
    var_2 = python_code_.gmfgraph_Label(text=False)
    assert isinstance(var_2, python_code_.gmfgraph_Label)
    var_56 = "NORTH_EAST:_gmfgraph_FigureGallery__gmfgraph_FigureGallery10:_gmfgraph_RealFigure__gmfgraph_RealFigure71:lightGreen"
    var_57 = "\\sm{xW"
    var_58 = python_code_.gmfgraph_Node(resizeConstraint=144, affixedParentSide=var_57)
    assert isinstance(var_58, python_code_.gmfgraph_Node)
    var_59 = python_code_.gmfgraph_FigureDescriptor()
    python_code_.gmfgraph_ChildAccess(
        accessor=var_56,
        gmfgraph_ChildAccess=var_58,
        accessors=var_59,
        gmfgraph_ChildAccess113=var_1,
    )


def test_18():
    var_0 = python_code_.Direction.SOUTH_WEST
    var_1 = python_code_.gmfgraph_DiagramLabel(
        elementIcon=[],
        external=var_0,
        gmfgraph_DiagramLabel=var_0,
        gmfgraph_DiagramLabel30=var_0,
    )
    assert isinstance(var_1, python_code_.gmfgraph_DiagramLabel)
    var_4 = python_code_.gmfgraph_FigureDescriptor()
    var_7 = "\\anz?pR?a|"
    python_code_.gmfgraph_ChildAccess(
        accessor=var_7, gmfgraph_ChildAccess31=var_7, ChildAccess=var_1, accessors=var_4
    )
    var_9 = -1787
    var_10 = -1263
    var_40 = python_code_.gmfgraph_Figure()
    python_code_.gmfgraph_Insets(
        top=var_10, left=var_10, bottom=var_10, right=var_9, gmfgraph_Insets=var_40
    )
    var_43 = False
    python_code_.gmfgraph_CustomAttribute(
        name=None,
        value=var_10,
        directAccess=var_43,
        multiStatementValue=(
            "e{0\t(C",
            "gmfgraph_MarginBorder",
            "gmfgraph_Figure-LINE_SOLID",
        ),
    )
    var_49 = "_gmfgraph_FigureGallery__gmfgraph_FigureGallery10"
    var_50 = python_code_.gmfgraph_Label(text=var_49)
    assert isinstance(var_50, python_code_.gmfgraph_Label)


def test_19():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_36 = "r\\2sVRBE5tfM,,+"
    var_37 = "&@n\\*@\\zf'qQ\nu:_"
    var_38 = python_code_.gmfgraph_Node(
        resizeConstraint=var_36, affixedParentSide=var_37
    )
    assert isinstance(var_38, python_code_.gmfgraph_Node)


def test_20():
    var_0 = python_code_.Alignment.CENTER
    var_2 = '4RK/~Ya;*rpMxSc">'
    var_3 = python_code_.gmfgraph_GeneralFacet(identifier=var_0, data=var_2)
    assert isinstance(var_3, python_code_.gmfgraph_GeneralFacet)
    var_12 = False
    var_13 = python_code_.gmfgraph_Compartment(collapsible=var_12, needsTitle=var_12)
    assert isinstance(var_13, python_code_.gmfgraph_Compartment)
    var_17 = "r[l<dX~=-G\t6ICOK<e"
    var_19 = python_code_.gmfgraph_Identity(name=var_17)
    assert isinstance(var_19, python_code_.gmfgraph_Identity)
    var_23 = python_code_.gmfgraph_Canvas()
    var_24 = python_code_.gmfgraph_Node(
        resizeConstraint=var_17, affixedParentSide=var_2, gmfgraph_Node=var_23
    )
    assert isinstance(var_24, python_code_.gmfgraph_Node)


def test_21():
    var_1 = python_code_.gmfgraph_GradientFacet(direction=[])
    assert isinstance(var_1, python_code_.gmfgraph_GradientFacet)
    python_code_.gmfgraph_FigureAccessor(accessor="xG")
    var_3 = "k*Gu"
    var_4 = python_code_.gmfgraph_Canvas()
    var_5 = python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_3, gmfgraph_FigureGallery=var_4
    )
    assert isinstance(var_5, python_code_.gmfgraph_FigureGallery)


def test_22():
    var_0 = python_code_.DiagramElement()
    var_2 = python_code_.gmfgraph_Label(text=False)
    assert isinstance(var_2, python_code_.gmfgraph_Label)
    var_5 = python_code_.gmfgraph_Border
    var_9 = python_code_.gmfgraph_PolylineConnection()
    var_11 = ""
    var_12 = python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_11, gmfgraph_FigureGallery14={}
    )
    assert isinstance(var_12, python_code_.gmfgraph_FigureGallery)
    var_14 = python_code_.gmfgraph_BorderLayoutData(alignment=var_9, vertical=var_5)
    assert isinstance(var_14, python_code_.gmfgraph_BorderLayoutData)
    var_15 = python_code_.gmfgraph_CustomClass(qualifiedClassName=var_0)
    assert isinstance(var_15, python_code_.gmfgraph_CustomClass)
    var_53 = "r[l<dX~=-G\t6ICOK<e"
    var_54 = python_code_.gmfgraph_Identity(name=var_53)
    assert isinstance(var_54, python_code_.gmfgraph_Identity)
    var_63 = "RE"
    var_64 = True
    var_65 = python_code_.gmfgraph_CustomAttribute(
        name=complex(1270.2477, -4661.32),
        value=var_63,
        directAccess=var_64,
        multiStatementValue=var_5,
        gmfgraph_CustomAttribute=var_15,
    )
    assert isinstance(var_65, python_code_.gmfgraph_CustomAttribute)


def test_23():
    python_code_.gmfgraph_CompoundBorder()


def test_24():
    var_0 = -1515
    var_1 = python_code_.gmfgraph_RGBColor(
        red=var_0, green=b'U\xe3t\xe4\xc3"K_\x10N\x9b\x9c\x01\x81', blue=var_0
    )
    assert isinstance(var_1, python_code_.gmfgraph_RGBColor)
    var_2 = python_code_.DiagramElement
    var_3 = "gmfgraph_DiagramLabel_gmfgraph_Shape__gmfgraph_Shape"
    var_4 = True
    var_5 = python_code_.gmfgraph_FlowLayout(
        forceSingleLine=var_2,
        majorAlignment=var_1,
        minorAlignment=var_3,
        majorSpacing=var_0,
        minorSpacing=var_0,
        vertical=complex(1750.0, 3259.7551528),
        matchMinorSize=var_4,
    )
    assert isinstance(var_5, python_code_.gmfgraph_FlowLayout)
    var_45 = False
    var_46 = python_code_.gmfgraph_Compartment(
        collapsible=True, needsTitle=True, gmfgraph_Compartment=var_5
    )
    assert isinstance(var_46, python_code_.gmfgraph_Compartment)
    var_49 = "r[l<dX~=-G\t6ICOK<e"
    var_50 = python_code_.gmfgraph_BorderLayoutData(
        alignment=",AvjR1]Z= 7n", vertical=var_45
    )
    assert isinstance(var_50, python_code_.gmfgraph_BorderLayoutData)
    var_51 = python_code_.gmfgraph_Identity(name=var_49)
    assert isinstance(var_51, python_code_.gmfgraph_Identity)
    var_55 = python_code_.gmfgraph_Canvas()
    var_56 = python_code_.gmfgraph_Node(
        resizeConstraint=var_49, affixedParentSide=var_49, gmfgraph_Node=var_55
    )
    assert isinstance(var_56, python_code_.gmfgraph_Node)


def test_25():
    var_0 = python_code_.DiagramElement()
    var_2 = python_code_.gmfgraph_Label(text=False)
    assert isinstance(var_2, python_code_.gmfgraph_Label)
    var_5 = python_code_.gmfgraph_Border
    var_9 = python_code_.gmfgraph_PolylineConnection()
    var_11 = ""
    var_12 = python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_11, gmfgraph_FigureGallery14={}
    )
    assert isinstance(var_12, python_code_.gmfgraph_FigureGallery)
    var_14 = python_code_.gmfgraph_BorderLayoutData(alignment=var_9, vertical=var_5)
    assert isinstance(var_14, python_code_.gmfgraph_BorderLayoutData)
    var_15 = python_code_.gmfgraph_CustomClass(qualifiedClassName=var_0)
    assert isinstance(var_15, python_code_.gmfgraph_CustomClass)
    var_16 = 677
    var_17 = python_code_.gmfgraph_RoundedRectangle(
        cornerWidth=var_16, cornerHeight=3592.79
    )
    assert isinstance(var_17, python_code_.gmfgraph_RoundedRectangle)
    var_18 = False
    python_code_.gmfgraph_CustomAttribute(
        name=var_11, value=True, directAccess={}, multiStatementValue=var_18
    )
    var_22 = python_code_.gmfgraph_Identity(name=var_15)
    assert isinstance(var_22, python_code_.gmfgraph_Identity)
    var_28 = False
    var_29 = python_code_.gmfgraph_DiagramLabel(elementIcon=var_18, external=var_28)
    assert isinstance(var_29, python_code_.gmfgraph_DiagramLabel)
    var_30 = "X7NVZY4\x0bD"
    var_31 = -4009
    var_32 = python_code_.gmfgraph_BasicFont(
        faceName=var_30, height=var_31, style=var_29
    )
    assert isinstance(var_32, python_code_.gmfgraph_BasicFont)


def test_26():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_1 = python_code_.gmfgraph_LineBorder(
        width={
            ";x.0A": 852,
            "gmfgraph_Figure52gmfgraph_ChildAccess28_gmfgraph_FigureAccessor__gmfgraph_FigureAccessor73gray": True,
        }
    )
    assert isinstance(var_1, python_code_.gmfgraph_LineBorder)
    var_4 = python_code_.Color()
    var_5 = "_gmfgraph_FigureGallery__gmfgraph_FigureGallery10"
    var_6 = python_code_.gmfgraph_Label(text=var_5)
    assert isinstance(var_6, python_code_.gmfgraph_Label)
    var_7 = python_code_.gmfgraph_ConstantColor(value=var_4)
    assert isinstance(var_7, python_code_.gmfgraph_ConstantColor)
    var_9 = False
    var_10 = python_code_.gmfgraph_DiagramLabel(
        elementIcon=0, external=var_9, gmfgraph_DiagramLabel30=complex(-798.9, -1253.25)
    )
    assert isinstance(var_10, python_code_.gmfgraph_DiagramLabel)
    var_21 = "8oH4Mn4Dn9o>>+3)\\"
    var_22 = python_code_.gmfgraph_GradientFacet(direction=var_21)
    assert isinstance(var_22, python_code_.gmfgraph_GradientFacet)


def test_27():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_36 = python_code_.Shape()
    var_46 = False
    var_47 = True
    var_48 = python_code_.gmfgraph_DiagramLabel(elementIcon=var_46, external=var_47)
    assert isinstance(var_48, python_code_.gmfgraph_DiagramLabel)
    var_49 = python_code_.gmfgraph_RGBColor(red=var_36, green=var_47, blue=var_46)
    assert isinstance(var_49, python_code_.gmfgraph_RGBColor)


def test_28():
    var_0 = python_code_.AbstractFigure
    var_1 = -1
    var_2 = python_code_.gmfgraph_RoundedRectangle(
        cornerWidth=var_0, cornerHeight=var_1
    )
    assert isinstance(var_2, python_code_.gmfgraph_RoundedRectangle)
    var_17 = python_code_.gmfgraph_LineBorder(
        width=var_1, gmfgraph_LineBorder=[".e<$kc#*", False, -4066]
    )
    assert isinstance(var_17, python_code_.gmfgraph_LineBorder)


def test_29():
    var_0 = python_code_.Alignment.CENTER
    var_2 = '4RK/~Ya;*rpMxSc">'
    var_3 = python_code_.gmfgraph_GeneralFacet(identifier=var_0, data=var_2)
    assert isinstance(var_3, python_code_.gmfgraph_GeneralFacet)
    var_12 = False
    var_13 = python_code_.gmfgraph_Compartment(collapsible=var_12, needsTitle=var_12)
    assert isinstance(var_13, python_code_.gmfgraph_Compartment)
    var_27 = 677
    var_28 = python_code_.gmfgraph_RoundedRectangle(
        cornerWidth=var_27, cornerHeight=3592.79
    )
    assert isinstance(var_28, python_code_.gmfgraph_RoundedRectangle)
    var_33 = python_code_.gmfgraph_LineBorder(
        width=var_27, gmfgraph_LineBorder=[".e<$kc#*", False, -4066]
    )
    assert isinstance(var_33, python_code_.gmfgraph_LineBorder)


def test_30():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_37 = "gm-fgraph_GridLayoutData"
    var_38 = python_code_.gmfgraph_GradientFacet(direction=var_37)
    assert isinstance(var_38, python_code_.gmfgraph_GradientFacet)
    python_code_.gmfgraph_Dimension(
        dx=380,
        dy=-572,
        gmfgraph_Dimension40=None,
        gmfgraph_Dimension93=None,
        gmfgraph_Dimension95=None,
        gmfgraph_Dimension100=None,
    )
    var_49 = 541
    python_code_.gmfgraph_Insets(
        top=var_49, left=var_49, bottom=-331, right=var_49, gmfgraph_Insets=None
    )
    var_55 = python_code_.gmfgraph_RoundedRectangle(
        cornerWidth=-1281, cornerHeight=var_49
    )
    assert isinstance(var_55, python_code_.gmfgraph_RoundedRectangle)


@pytest.mark.xfail(strict=True)
def test_31():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_44 = python_code_.DiagramElement
    var_49 = python_code_.CustomClass()
    var_50 = True
    var_51 = python_code_.gmfgraph_GridLayout(numColumns=var_49, equalWidth=var_50)
    assert isinstance(var_51, python_code_.gmfgraph_GridLayout)
    var_54 = -1697
    var_55 = python_code_.gmfgraph_RGBColor(
        red=var_54, green=var_44, blue=b".\x07\xfa\xaa(\x1e\xb0\x14\x05\xcf\xedc`\x84e"
    )
    assert isinstance(var_55, python_code_.gmfgraph_RGBColor)
    var_65 = 627
    var_69 = python_code_.gmfgraph_Figure()
    python_code_.gmfgraph_Dimension(
        dx=None,
        dy=var_65,
        gmfgraph_Dimension40=var_69,
        gmfgraph_Dimension43=[3884, 783],
        gmfgraph_Dimension90=var_51,
    )


def test_32():
    var_0 = -1515
    var_1 = python_code_.gmfgraph_RGBColor(
        red=var_0, green=b'U\xe3t\xe4\xc3"K_\x10N\x9b\x9c\x01\x81', blue=var_0
    )
    assert isinstance(var_1, python_code_.gmfgraph_RGBColor)
    var_2 = python_code_.DiagramElement
    var_3 = "gmfgraph_DiagramLabel_gmfgraph_Shape__gmfgraph_Shape"
    var_4 = True
    var_5 = python_code_.gmfgraph_FlowLayout(
        forceSingleLine=var_2,
        majorAlignment=var_1,
        minorAlignment=var_3,
        majorSpacing=var_0,
        minorSpacing=var_0,
        vertical=complex(1750.0, 3259.7551528),
        matchMinorSize=var_4,
    )
    assert isinstance(var_5, python_code_.gmfgraph_FlowLayout)
    var_10 = python_code_.CustomClass()
    var_11 = True
    var_12 = python_code_.gmfgraph_GridLayout(numColumns=var_10, equalWidth=var_11)
    assert isinstance(var_12, python_code_.gmfgraph_GridLayout)
    var_50 = "\\sm{xW"
    var_51 = python_code_.gmfgraph_Node(resizeConstraint=144, affixedParentSide=var_50)
    assert isinstance(var_51, python_code_.gmfgraph_Node)
    var_53 = python_code_.gmfgraph_GeneralFacet(identifier=var_3, data=var_2)
    assert isinstance(var_53, python_code_.gmfgraph_GeneralFacet)
    var_54 = True
    var_55 = python_code_.gmfgraph_DiagramLabel(elementIcon=var_54, external=None)
    assert isinstance(var_55, python_code_.gmfgraph_DiagramLabel)
    var_57 = "darkGray:gmfgraph_Dimension90:gmfgraph_CustomFigure"
    python_code_.gmfgraph_Node(
        resizeConstraint=var_57, affixedParentSide=var_3, gmfgraph_Node22=var_57
    )


def test_33():
    var_4 = python_code_.Polyline
    var_5 = python_code_.gmfgraph_Canvas()
    var_6 = python_code_.gmfgraph_Compartment(
        collapsible=var_4, needsTitle=var_4, gmfgraph_Compartment=var_5
    )
    assert isinstance(var_6, python_code_.gmfgraph_Compartment)


def test_34():
    var_0 = python_code_.gmfgraph_Layoutable()
    var_2 = "SOUTHgmfgraph_Compartment24"
    var_3 = python_code_.gmfgraph_Layoutable
    var_4 = python_code_.gmfgraph_Figure()
    var_5 = {var_4, var_4, var_4, var_4, var_4}
    var_6 = python_code_.gmfgraph_RealFigure(
        name=var_2, gmfgraph_RealFigure=var_3, gmfgraph_RealFigure104=var_5
    )
    assert isinstance(var_6, python_code_.gmfgraph_RealFigure)
    var_7 = python_code_.gmfgraph_StackLayout()
    var_11 = '\x0c`wM>?9cz(AaX8["'
    var_12 = python_code_.gmfgraph_GradientFacet(direction=var_11)
    assert isinstance(var_12, python_code_.gmfgraph_GradientFacet)
    var_13 = ""
    python_code_.gmfgraph_CustomAttribute(
        name=var_13, value=var_2, directAccess=var_7, multiStatementValue=var_3
    )
    var_15 = python_code_.gmfgraph_RGBColor(red=var_3, green=var_0, blue=var_7)
    assert isinstance(var_15, python_code_.gmfgraph_RGBColor)
    var_24 = python_code_.gmfgraph_CustomClass(
        qualifiedClassName=None, gmfgraph_CustomClass=var_5
    )
    assert isinstance(var_24, python_code_.gmfgraph_CustomClass)
    var_26 = python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_2, gmfgraph_FigureGallery12=var_5
    )
    assert isinstance(var_26, python_code_.gmfgraph_FigureGallery)
    var_28 = python_code_.gmfgraph_Label(text=870)
    assert isinstance(var_28, python_code_.gmfgraph_Label)
    var_32 = False
    var_33 = python_code_.gmfgraph_GridLayout(numColumns=var_3, equalWidth=var_32)
    assert isinstance(var_33, python_code_.gmfgraph_GridLayout)
    var_34 = python_code_.gmfgraph_FlowLayout(
        forceSingleLine=var_15,
        majorAlignment=var_13,
        minorAlignment=123,
        majorSpacing=var_32,
        minorSpacing=var_32,
        vertical=0,
        matchMinorSize=var_32,
    )
    assert isinstance(var_34, python_code_.gmfgraph_FlowLayout)
    var_36 = python_code_.gmfgraph_RoundedRectangle(
        cornerWidth=var_3, cornerHeight=var_28
    )
    assert isinstance(var_36, python_code_.gmfgraph_RoundedRectangle)
    var_37 = "53`[-_\n>SPHzc \\I"
    var_38 = python_code_.gmfgraph_BasicFont(
        faceName=var_32, height=var_32, style=var_37
    )
    assert isinstance(var_38, python_code_.gmfgraph_BasicFont)
    python_code_.gmfgraph_RealFigure(name=None, gmfgraph_RealFigure60=648.62)
    var_46 = python_code_.gmfgraph_Identity(name=var_3)
    assert isinstance(var_46, python_code_.gmfgraph_Identity)


def test_35():
    var_0 = python_code_.Direction.SOUTH_WEST
    var_1 = python_code_.gmfgraph_DiagramLabel(
        elementIcon=[],
        external=var_0,
        gmfgraph_DiagramLabel=var_0,
        gmfgraph_DiagramLabel30=var_0,
    )
    assert isinstance(var_1, python_code_.gmfgraph_DiagramLabel)
    var_2 = python_code_.gmfgraph_Connection()
    var_4 = python_code_.gmfgraph_FigureDescriptor()
    var_7 = "\\anz?pR?a|"
    python_code_.gmfgraph_ChildAccess(
        accessor=var_7, gmfgraph_ChildAccess31=var_7, ChildAccess=var_1, accessors=var_4
    )
    var_9 = -1787
    var_10 = -1263
    var_11 = python_code_.gmfgraph_RGBColor(
        red=complex(-12.918723, 1900.13325), green=var_9, blue=var_10
    )
    assert isinstance(var_11, python_code_.gmfgraph_RGBColor)
    var_22 = python_code_.gmfgraph_XYLayoutData()
    python_code_.gmfgraph_Dimension(dx=var_9, dy=var_10, gmfgraph_Dimension100=var_22)
    var_25 = lambda *args, **kwargs: -1042
    var_26 = False
    var_27 = python_code_.gmfgraph_Compartment(collapsible=var_25, needsTitle=var_26)
    assert isinstance(var_27, python_code_.gmfgraph_Compartment)
    var_29 = python_code_.gmfgraph_ConstantColor(value=True)
    assert isinstance(var_29, python_code_.gmfgraph_ConstantColor)
    var_30 = python_code_.Layoutable()
    var_31 = python_code_.gmfgraph_Label(text=())
    assert isinstance(var_31, python_code_.gmfgraph_Label)
    var_34 = python_code_.gmfgraph_RealFigure(
        name=False,
        gmfgraph_RealFigure=var_30,
        gmfgraph_RealFigure104={1213},
        gmfgraph_RealFigure60={},
    )
    assert isinstance(var_34, python_code_.gmfgraph_RealFigure)
    var_35 = python_code_.Layout()
    var_36 = -2285
    var_37 = python_code_.gmfgraph_RGBColor(red=var_25, green=var_36, blue=var_35)
    var_38 = 1523
    python_code_.gmfgraph_Insets(top=var_2, left=var_37, bottom=var_38, right=var_36)


def test_36():
    python_code_.gmfgraph_FigureAccessor(accessor=-1684.4)
    var_37 = python_code_.Shape()
    var_39 = False
    var_40 = python_code_.gmfgraph_DiagramLabel(
        elementIcon=False,
        external=True,
        gmfgraph_DiagramLabel=var_39,
        gmfgraph_DiagramLabel27=var_39,
    )
    assert isinstance(var_40, python_code_.gmfgraph_DiagramLabel)
    var_41 = 3353
    var_42 = python_code_.gmfgraph_LayoutData
    python_code_.gmfgraph_Point(
        x=var_41,
        y=var_40,
        gmfgraph_Point=var_37,
        gmfgraph_Point64=var_42,
        gmfgraph_Point97=-1051,
    )


@pytest.mark.xfail(strict=True)
def test_37():
    var_6 = python_code_.gmfgraph_Compartment(collapsible=True, needsTitle=True)
    assert isinstance(var_6, python_code_.gmfgraph_Compartment)
    python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_6, gmfgraph_FigureGallery16=complex(-2414.0, 2799.64)
    )


@pytest.mark.xfail(strict=True)
def test_38():
    var_0 = python_code_.Direction.SOUTH_EAST
    var_1 = python_code_.gmfgraph_DiagramLabel(
        elementIcon=[],
        external=var_0,
        gmfgraph_DiagramLabel=var_0,
        gmfgraph_DiagramLabel30=var_0,
    )
    assert isinstance(var_1, python_code_.gmfgraph_DiagramLabel)
    var_2 = python_code_.gmfgraph_Connection()
    var_4 = python_code_.gmfgraph_FigureDescriptor()
    var_5 = lambda *args, **kwargs: "*q7!\x0bT3@{B`lv"
    var_6 = python_code_.gmfgraph_LabelOffsetFacet(x=var_2, y=var_5)
    assert isinstance(var_6, python_code_.gmfgraph_LabelOffsetFacet)
    var_7 = "\\anz?pR?a|"
    python_code_.gmfgraph_ChildAccess(
        accessor=var_7, gmfgraph_ChildAccess31=var_7, ChildAccess=var_1, accessors=var_4
    )
    var_9 = -1808
    var_10 = -1263
    var_11 = python_code_.gmfgraph_RGBColor(
        red=complex(-12.918723, 1900.13325), green=var_9, blue=var_10
    )
    assert isinstance(var_11, python_code_.gmfgraph_RGBColor)
    var_15 = python_code_.gmfgraph_FigureDescriptor()
    var_16 = {var_4, var_4, var_15, var_15, var_4}
    python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_5,
        gmfgraph_FigureGallery16=var_5,
        gmfgraph_FigureGallery12=var_16,
    )


@pytest.mark.xfail(strict=True)
def test_39():
    var_4 = "vIP"
    var_5 = python_code_.gmfgraph_FigureAccessor(accessor=b"\x08\x89m\xda")
    python_code_.gmfgraph_RealFigure(name=var_4, gmfgraph_RealFigure71=var_5)


@pytest.mark.xfail(strict=True)
def test_40():
    var_2 = True
    var_3 = python_code_.gmfgraph_Compartment(
        collapsible=var_2, needsTitle=complex(678.0, 213.162089)
    )
    assert isinstance(var_3, python_code_.gmfgraph_Compartment)
    var_4 = lambda *args, **kwargs: [0, -3837.78]
    var_5 = ">I[KI\n"
    var_6 = python_code_.gmfgraph_CustomAttribute(
        name=var_4, value=var_5, directAccess=None, multiStatementValue=var_2
    )
    var_7 = python_code_.gmfgraph_PolylineDecoration()
    var_8 = python_code_.gmfgraph_Canvas()
    var_9 = python_code_.DiagramElement()
    var_13 = "]*eVgKWxm="
    var_14 = python_code_.gmfgraph_GridLayoutData(
        grabExcessHorizontalSpace=var_7,
        grabExcessVerticalSpace=var_2,
        verticalAlignment=var_13,
        horizontalAlignment=var_4,
        verticalSpan=var_2,
        horizontalSpan=3,
        horizontalIndent=var_2,
        gmfgraph_GridLayoutData=-1011.29,
    )
    assert isinstance(var_14, python_code_.gmfgraph_GridLayoutData)
    var_16 = python_code_.gmfgraph_GeneralFacet(identifier=var_13, data=var_2)
    assert isinstance(var_16, python_code_.gmfgraph_GeneralFacet)
    var_18 = python_code_.gmfgraph_RGBColor(red=var_4, green=var_6, blue=True)
    assert isinstance(var_18, python_code_.gmfgraph_RGBColor)
    python_code_.gmfgraph_FigureGallery(
        implementationBundle=var_4,
        gmfgraph_FigureGallery=var_9,
        gmfgraph_FigureGallery10=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_0 = python_code_.gmfgraph_DefaultSizeFacet()
    var_2 = python_code_.Alignment.BEGINNING
    var_3 = python_code_.gmfgraph_DecorationFigure()
    var_5 = -678
    python_code_.gmfgraph_Insets(top=var_5, left=var_2, bottom=var_5, right=-581)
    var_10 = -345
    var_11 = True
    var_12 = python_code_.gmfgraph_Dimension(
        dx=None,
        dy=var_3,
        gmfgraph_Dimension=var_0,
        gmfgraph_Dimension43=False,
        gmfgraph_Dimension102=var_11,
        gmfgraph_Dimension100=b"$^\xb3\xb6,",
    )
    python_code_.gmfgraph_GridLayout(
        numColumns=var_10, equalWidth=var_11, gmfgraph_GridLayout=var_12
    )
