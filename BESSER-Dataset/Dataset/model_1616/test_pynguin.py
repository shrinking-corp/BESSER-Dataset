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
    Annotation,
    Arc,
    ArithmeticBinaryOperator,
    ArithmeticExpression,
    BooleanExpression,
    CSS2Color,
    CSS2FontFamily,
    CSS2FontSize,
    CSS2FontStyle,
    CSS2FontWeight,
    ComparisonOperator,
    Coordinate,
    Distribution,
    Enum,
    EvaluationType,
    Expression,
    FontAlign,
    FontDecoration,
    GSPNArcType,
    GSPNTransition,
    GSPNTransitionType,
    Gradient,
    Graphics,
    Label,
    LineShape,
    LineStyle,
    LogicalExpression,
    Node,
    PNType,
    PlaceNode,
    PnObject,
    Transition,
    TransitionNode,
    abstractmethod,
    date,
    datetime,
    ptnet_Annotation,
    ptnet_AnnotationGraphics,
    ptnet_AnyObject,
    ptnet_Arc,
    ptnet_ArcGraphics,
    ptnet_ArithmeticBinaryOperator,
    ptnet_ArithmeticExpression,
    ptnet_Attribute,
    ptnet_BooleanExpression,
    ptnet_ComparisonOperator,
    ptnet_Coordinate,
    ptnet_Deterministic,
    ptnet_Dimension,
    ptnet_Distribution,
    ptnet_EvaluationList,
    ptnet_EvaluationType,
    ptnet_Exponential,
    ptnet_Expression,
    ptnet_Fill,
    ptnet_Font,
    ptnet_GSPNArc,
    ptnet_GSPNImmediateTransition,
    ptnet_GSPNTimedTransition,
    ptnet_GSPNTransition,
    ptnet_Gamma,
    ptnet_Gaussian,
    ptnet_Graphics,
    ptnet_IfThenElse,
    ptnet_InstantOfTime,
    ptnet_IntervalOfTime,
    ptnet_IntervalOfTimeAveraged,
    ptnet_Label,
    ptnet_Line,
    ptnet_LogicalExpression,
    ptnet_MarkingExpression,
    ptnet_Measure,
    ptnet_Name,
    ptnet_Node,
    ptnet_NodeGraphics,
    ptnet_Offset,
    ptnet_OpAnd,
    ptnet_OpDivide,
    ptnet_OpEqual,
    ptnet_OpFalse,
    ptnet_OpGreater,
    ptnet_OpGreaterEqual,
    ptnet_OpLess,
    ptnet_OpLessEqual,
    ptnet_OpMinus,
    ptnet_OpMultiply,
    ptnet_OpNot,
    ptnet_OpOr,
    ptnet_OpSum,
    ptnet_OpTrue,
    ptnet_PTArcAnnotation,
    ptnet_PTMarking,
    ptnet_Page,
    ptnet_PetriNet,
    ptnet_PetriNetDoc,
    ptnet_Place,
    ptnet_PlaceNode,
    ptnet_PnObject,
    ptnet_Position,
    ptnet_RefPlace,
    ptnet_RefTransition,
    ptnet_SteadyState,
    ptnet_Study,
    ptnet_ToolInfo,
    ptnet_Transition,
    ptnet_TransitionNode,
    ptnet_Uniform,
    ptnet_ValueExpression,
    ptnet_Variable,
    ptnet_VariableExpression,
    ptnet_VariableValues,
    ptnet_Weibull,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.ptnet_OpFalse()
    var_1 = python_code_.ptnet_ArithmeticBinaryOperator()
    var_3 = "SMALL"
    var_5 = python_code_.ptnet_Page()
    var_6 = python_code_.ptnet_PnObject(
        id=" *`H",
        PnObject23=None,
        containerNamePnObject=var_0,
        containerPnObject={var_1},
        PnObject28=var_3,
    )
    assert isinstance(var_6, python_code_.ptnet_PnObject)
    python_code_.ptnet_Name(
        text='tVwq#QyUqa"Gl5o0Q', name=var_5, name22=var_6, Name14=var_6
    )


def test_1():
    var_3 = "\x0cOOxoy`=#|FY;"
    var_6 = python_code_.ptnet_PnObject(id=var_3)
    assert isinstance(var_6, python_code_.ptnet_PnObject)


@pytest.mark.xfail(strict=True)
def test_2():
    var_38 = python_code_.ptnet_Page()
    var_40 = python_code_.ptnet_TransitionNode()
    var_42 = python_code_.Label()
    var_50 = python_code_.ptnet_GSPNImmediateTransition(Priority=var_42, Weight=746)
    assert isinstance(var_50, python_code_.ptnet_GSPNImmediateTransition)
    var_60 = python_code_.ptnet_Gaussian
    var_65 = "d"
    var_66 = python_code_.ptnet_PnObject(id=var_50, PnObject23=var_60, PnObject=var_38)
    assert isinstance(var_66, python_code_.ptnet_PnObject)
    var_67 = python_code_.ptnet_AnyObject()
    python_code_.ptnet_ToolInfo(
        tool=var_65,
        version={},
        formattedXMLBuffer=var_40,
        toolInfoGrammarURI=None,
        toolspecifics27=var_66,
        ToolInfo104=var_67,
    )


def test_3():
    var_45 = "\x0c|[[*W"
    var_46 = python_code_.ptnet_PnObject(id=var_45, objects=var_45)
    assert isinstance(var_46, python_code_.ptnet_PnObject)
    var_63 = "hB#Aar~(3"
    python_code_.ptnet_VariableValues(values=None)
    var_70 = python_code_.ptnet_OpGreater()
    var_73 = python_code_.ptnet_Coordinate(x=var_63, y=var_70)
    assert isinstance(var_73, python_code_.ptnet_Coordinate)
    var_74 = python_code_.ptnet_PTArcAnnotation(text=var_63)
    assert isinstance(var_74, python_code_.ptnet_PTArcAnnotation)


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.ptnet_OpFalse()
    var_4 = tuple
    var_5 = python_code_.ptnet_Page()
    python_code_.ptnet_PnObject(
        id=b"\xb1\xe0\xf2\x8f({\xa42\xbb\xfb\xcd\x1a\xc1Dh\xcdX",
        PnObject=var_0,
        containerPnObject=var_4,
        objects=var_5,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_2 = "\rNPw|}{PH4>R|$?A="
    var_3 = "\x0cOOxoy`=3|FY;"
    var_5 = python_code_.ptnet_Page()
    var_15 = '\'a\x0c"@+}"C&8ty?'
    var_16 = python_code_.ptnet_PetriNetDoc(xmlns=var_3)
    var_17 = python_code_.ptnet_ToolInfo(
        tool=var_2,
        version="",
        formattedXMLBuffer=var_2,
        toolInfoGrammarURI=var_3,
        toolspecifics30=var_5,
    )
    python_code_.ptnet_PetriNet(
        id=var_15,
        type={"bM}f4\x0b9SjVtR \x0ck~10"},
        nets=None,
        PetriNet=var_16,
        PetriNet25=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_3 = "\x0cOOxoy`=3|FY;"
    var_4 = tuple
    var_15 = '\'a\x0c"@+}"C&8ty?'
    var_16 = python_code_.ptnet_PetriNetDoc(xmlns=var_3)
    var_17 = python_code_.ptnet_ToolInfo(
        tool=complex(1534.9756742, -36.0),
        version=None,
        formattedXMLBuffer=var_3,
        toolInfoGrammarURI=var_4,
        containerToolInfo=var_4,
    )
    python_code_.ptnet_PetriNet(
        id=var_15,
        type={"bM}f4\x0b9SjVtR \x0ck~10"},
        nets=None,
        PetriNet=var_16,
        PetriNet25=var_17,
    )


def test_7():
    python_code_.ptnet_Variable(name=[])
    var_36 = "\x0c|[[*W"
    python_code_.ptnet_PetriNet(
        id={3, "#n~;W+@Dp\x0ci\x0c2z>%", "_ptnet_PnObject__containerNamePnObject"},
        type={
            "3": 1091,
            "_ptnet_PetriNet__containerPetriNetLINETHROUGHcontainerPageGSPN": False,
        },
        nets=var_36,
    )
    var_48 = 627.34
    var_50 = python_code_.ptnet_Gaussian(Mean=var_48, Variance=var_48)
    assert isinstance(var_50, python_code_.ptnet_Gaussian)


@pytest.mark.xfail(strict=True)
def test_8():
    var_3 = "\x0cOOxoy`=#|FY;"
    var_4 = python_code_.ptnet_NodeGraphics
    var_5 = python_code_.ptnet_Page()
    var_6 = python_code_.ptnet_PnObject(id=var_3)
    assert isinstance(var_6, python_code_.ptnet_PnObject)
    var_7 = python_code_.ptnet_Name(text=var_3, name=var_4)
    assert isinstance(var_7, python_code_.ptnet_Name)
    var_8 = python_code_.ptnet_PetriNetDoc(
        xmlns=var_7, PetriNetDoc=b"\xd1\x9eN\xba\x9a\xa6VW'\xdbx!\xec\x01\x18-3"
    )
    python_code_.ptnet_PetriNet(
        id=var_3,
        type=var_4,
        containerNamePetriNet=var_7,
        PetriNet=var_8,
        containerPetriNet=var_5,
        PetriNet20=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_17 = "8'd}.Dz8e"
    var_18 = python_code_.ptnet_Name(text=var_17)
    assert isinstance(var_18, python_code_.ptnet_Name)
    var_23 = "<3=FE\t'(Ss*b|:"
    var_24 = ";25SraB='@Io"
    var_25 = python_code_.ptnet_PetriNetDoc(xmlns=var_24, containerPetriNetDoc=())
    python_code_.ptnet_PetriNet(
        id=var_23,
        type={},
        containerNamePetriNet=var_18,
        nets=var_25,
        PetriNet=var_25,
        PetriNet20=var_18,
        PetriNet25=var_18,
    )


def test_10():
    python_code_.ptnet_PetriNetDoc(xmlns="t^QQdFV")


def test_11():
    var_0 = python_code_.ptnet_ValueExpression
    var_12 = "\x0cOOxy`=3|FY;"
    var_17 = python_code_.ptnet_PetriNetDoc(xmlns="t^QQdFV")
    python_code_.ptnet_ToolInfo(
        tool=var_12,
        version="LINE-HORIZONTAL-OVERLINE",
        formattedXMLBuffer="containerNamePnObjectptnet_Variablenormal",
        toolInfoGrammarURI=var_12,
        ToolInfo=var_0,
        ToolInfo16=None,
        toolspecifics=var_0,
        ToolInfo33=var_17,
    )


def test_12():
    var_15 = "\x0cOOxoy`=3o|FY;"
    var_16 = tuple
    python_code_.ptnet_PetriNetDoc(xmlns=var_15)
    python_code_.ptnet_ToolInfo(
        tool=complex(1534.9756742, -36.0),
        version=None,
        formattedXMLBuffer=var_15,
        toolInfoGrammarURI=var_16,
        containerToolInfo=var_16,
    )


def test_13():
    var_0 = python_code_.ComparisonOperator()
    var_2 = python_code_.ptnet_InstantOfTime()
    var_4 = python_code_.ptnet_GSPNTimedTransition()
    var_9 = lambda *args, **kwargs: True
    var_10 = "1p,{sU62I"
    var_12 = "_ptnet_Fill__Fill52"
    var_17 = python_code_.ptnet_ValueExpression(value=var_2)
    assert isinstance(var_17, python_code_.ptnet_ValueExpression)
    python_code_.ptnet_ToolInfo(
        tool=var_12,
        version=var_0,
        formattedXMLBuffer=var_9,
        toolInfoGrammarURI=1923.59,
        ToolInfo33=var_17,
        ToolInfo104=var_4,
    )
    var_26 = python_code_.ptnet_Name(text=var_10, name22=-5766.47)
    assert isinstance(var_26, python_code_.ptnet_Name)
    var_30 = python_code_.ptnet_PTMarking(text=var_10)
    assert isinstance(var_30, python_code_.ptnet_PTMarking)


def test_14():
    var_2 = "_ptnet_PnObject__objects-_ptnet_PnObject__PnObject28-LEFT"
    var_3 = python_code_.ptnet_VariableExpression()
    python_code_.ptnet_Variable(name=var_2, ptnet_Variable159=var_3)
    var_5 = python_code_.ptnet_EvaluationList()
    python_code_.ptnet_Measure(name=var_2, ptnet_Measure=var_5)
    var_7 = python_code_.ptnet_PTArcAnnotation(text=var_2)
    assert isinstance(var_7, python_code_.ptnet_PTArcAnnotation)


def test_15():
    var_2 = python_code_.ptnet_InstantOfTime()
    var_4 = python_code_.ptnet_GSPNTimedTransition()
    var_7 = python_code_.ptnet_AnnotationGraphics()
    var_9 = lambda *args, **kwargs: True
    var_10 = "1p,{sU62I"
    var_11 = "ptnet_PnObject,MAROON,ARIAL"
    var_12 = "_ptnet_Fill__Fill52"
    python_code_.ptnet_Font(
        align=var_9,
        decoration=var_4,
        family=var_10,
        rotation=var_11,
        size=var_10,
        style="toolspecifics LIGHTER _ptnet_PetriNet__PetriNet20",
        weight=var_12,
        Font=var_7,
    )
    python_code_.ptnet_PetriNetDoc(xmlns=var_2)
    var_33 = python_code_.ptnet_Arc()
    var_34 = python_code_.ptnet_PTArcAnnotation(
        text=var_10, inscription=var_33, PTArcAnnotation=var_33
    )
    assert isinstance(var_34, python_code_.ptnet_PTArcAnnotation)
    var_37 = python_code_.ptnet_Page()
    var_38 = python_code_.ptnet_GSPNTransition()
    var_39 = python_code_.ptnet_NodeGraphics()
    var_40 = python_code_.ptnet_ArcGraphics()
    python_code_.ptnet_Line(
        color=var_10,
        shape={
            "ptnet_Arctoolspecifics27": -1870.11,
            "_ptnet_Measure__ptnet_Measure114-_ptnet_Measure__ptnet_Measure114": True,
            "Mn&C=`A;015STVL<,": False,
        },
        width=var_38,
        style=var_37,
        line=var_39,
        line67=var_40,
    )


def test_16():
    var_2 = "\rNPw|}{PH4R|$?A="
    var_20 = python_code_.ptnet_Arc()
    var_21 = python_code_.ptnet_PTArcAnnotation(text=var_2, inscription=var_20)
    assert isinstance(var_21, python_code_.ptnet_PTArcAnnotation)


def test_17():
    var_1 = python_code_.ptnet_ArithmeticBinaryOperator()
    var_3 = "\x0cOOxoy`=#|FY;"
    var_4 = python_code_.ptnet_NodeGraphics
    var_6 = python_code_.ptnet_PnObject(id=var_3)
    assert isinstance(var_6, python_code_.ptnet_PnObject)
    var_7 = python_code_.ptnet_Name(text=var_3, name=var_4)
    assert isinstance(var_7, python_code_.ptnet_Name)
    var_16 = python_code_.ptnet_PTArcAnnotation(text=var_7)
    assert isinstance(var_16, python_code_.ptnet_PTArcAnnotation)
    var_17 = python_code_.ptnet_PTMarking(text=var_1)
    assert isinstance(var_17, python_code_.ptnet_PTMarking)


def test_18():
    var_35 = "Phk!RSfJ\n0;wWVr`KS"
    var_36 = python_code_.ptnet_EvaluationList()
    python_code_.ptnet_Study(name=var_35, ptnet_Study=var_36)
    var_20 = "1p,{sU62I"
    var_30 = python_code_.ptnet_Name(text=var_20, name22=-5766.47)
    assert isinstance(var_30, python_code_.ptnet_Name)
    var_32 = python_code_.ptnet_PTMarking(text=var_20)
    assert isinstance(var_32, python_code_.ptnet_PTMarking)


def test_19():
    var_11 = python_code_.PlaceNode()
    var_18 = python_code_.ptnet_Name(
        text="containerPetriNet6-_ptnet_Line__Line76", Name=None, Name14=var_11
    )
    assert isinstance(var_18, python_code_.ptnet_Name)


def test_20():
    var_1 = python_code_.ptnet_Gaussian(Mean=1183.26, Variance=972.14)
    assert isinstance(var_1, python_code_.ptnet_Gaussian)
    var_2 = "_ptnet_PnObject__objects-_ptnet_PnObject__PnObject28-LEFT"
    var_3 = python_code_.ptnet_VariableExpression()
    python_code_.ptnet_Variable(name=var_2, ptnet_Variable159=var_3)


def test_21():
    var_0 = "AnnotationGraphics63-RED"
    python_code_.ptnet_Line(
        color=var_0,
        shape="LEX",
        width="LIGHTER",
        style=var_0,
        Line55=var_0,
        line67=var_0,
        Line=var_0,
        Line76=None,
    )
    var_3 = "ptnet_Arc,_ptnet_PetriNet__containerPetriNet6"
    python_code_.ptnet_Measure(name=var_3, ptnet_Measure=None)


def test_22():
    var_0 = python_code_.Expression
    var_1 = python_code_.ptnet_Gaussian(Mean=var_0, Variance=var_0)
    assert isinstance(var_1, python_code_.ptnet_Gaussian)
    var_2 = "_ptnet_PnObject__objects-_ptnet_PnObject__PnObject28-LEFT"
    var_3 = python_code_.ptnet_VariableExpression()
    python_code_.ptnet_Variable(name=var_2, ptnet_Variable159=var_3)
    var_5 = python_code_.ptnet_EvaluationList()
    python_code_.ptnet_Measure(name=var_2, ptnet_Measure=var_5)


def test_23():
    var_3 = "ptnet_Arc,_ptnet_PetriNet__containerPetriNet6"
    var_4 = python_code_.ptnet_Measure(name=var_3)
    var_6 = "x#T"
    var_7 = (
        "_ptnet_Name__name,NodeGraphics60,_ptnet_ToolInfo__ToolInfo104,containerPlace"
    )
    var_8 = "CROi[(\np%aWZ<|"
    var_9 = python_code_.ptnet_OpLess
    python_code_.ptnet_Font(
        align=var_3,
        decoration=var_6,
        family=var_7,
        rotation=var_8,
        size=var_9,
        style=var_6,
        weight=var_4,
        Font=var_3,
    )
    var_47 = 627.34
    var_49 = python_code_.ptnet_Gaussian(Mean=var_47, Variance=var_47)
    assert isinstance(var_49, python_code_.ptnet_Gaussian)


def test_24():
    var_0 = True
    var_2 = "_ptnet_PnObject__objects-_ptnet_PnObject__PnObject28-LEFT"
    var_3 = python_code_.ptnet_VariableExpression()
    python_code_.ptnet_Variable(name=var_2, ptnet_Variable159=var_3)
    python_code_.ptnet_Line(
        color="%'\ndwiG ",
        shape=var_2,
        width=">a\t\x0b%7?>`I",
        style="TEAL",
        line67=None,
        line70=var_0,
    )


def test_25():
    var_0 = "AnnotationGraphics63-RED"
    python_code_.ptnet_Line(
        color=var_0,
        shape="|",
        width="D&WU6",
        style='R~\\76$`po78"-~\x0b)f\rA',
        Line55=None,
        Line=var_0,
    )
    var_3 = "ptnet_Arc,_ptnet_PetriNet__containerPetriNet6"
    python_code_.ptnet_Measure(name=var_3, ptnet_Measure=None)


def test_26():
    var_0 = True
    var_1 = python_code_.ptnet_Gaussian(Mean=var_0, Variance=var_0)
    assert isinstance(var_1, python_code_.ptnet_Gaussian)
    var_2 = "_ptnet_PnObject__objects-_ptnet_PnObject__PnObject28-LEFT"
    var_3 = python_code_.ptnet_VariableExpression()
    python_code_.ptnet_Variable(name=var_2, ptnet_Variable159=var_3)
    var_8 = python_code_.ptnet_ArcGraphics()
    var_9 = python_code_.ptnet_OpNot
    python_code_.ptnet_Line(
        color=None,
        shape=var_9,
        width={
            "normal,_ptnet_PTMarking__initialMarking,ptnet_VariableValues157,_ptnet_PTArcAnnotation__inscription": 106.32,
            "BLACK._ptnet_Name__name22.ToolInfo": 3884.74,
        },
        style=var_9,
        Line55=var_2,
        line=var_0,
        line70=False,
        Line76=var_8,
    )


def test_27():
    python_code_.GSPNArcType.inhibitor


def test_28():
    var_0 = python_code_.EvaluationType()
    var_3 = python_code_.ptnet_Offset()
    var_4 = -3854.98
    var_5 = python_code_.ptnet_Uniform(Lower=var_0, Upper=var_4)
    assert isinstance(var_5, python_code_.ptnet_Uniform)
    var_7 = 738.83
    var_8 = python_code_.ptnet_Gamma(Alpha=var_7, Beta=complex(721.0, -1159.7))
    assert isinstance(var_8, python_code_.ptnet_Gamma)
    var_14 = "eD["
    var_15 = python_code_.ptnet_Name(text=var_14)
    assert isinstance(var_15, python_code_.ptnet_Name)
    var_19 = python_code_.ptnet_Exponential(Rate=var_3)
    assert isinstance(var_19, python_code_.ptnet_Exponential)


def test_29():
    var_0 = python_code_.GSPNArcType.inhibitor
    var_2 = python_code_.ptnet_Deterministic(Value=var_0)
    assert isinstance(var_2, python_code_.ptnet_Deterministic)


def test_30():
    var_0 = "AnnotationGraphics63-RED"
    var_1 = python_code_.ptnet_Line(
        color=var_0, shape=var_0, width=[3121], style=var_0, Line76=890
    )
    var_3 = "ptnet_Arc,_ptnet_PetriNet__containerPetriNet6"
    var_4 = python_code_.ptnet_Measure(name=var_3)
    var_6 = "x#T"
    var_7 = (
        "_ptnet_Name__name,NodeGraphics60,_ptnet_ToolInfo__ToolInfo104,containerPlace"
    )
    var_8 = "CROi[(\np%aWZ<|"
    var_9 = python_code_.ptnet_OpLess
    python_code_.ptnet_Font(
        align=var_3,
        decoration=var_6,
        family=var_7,
        rotation=var_8,
        size=var_9,
        style=var_6,
        weight=var_4,
        Font=var_3,
    )
    var_12 = python_code_.ptnet_GSPNTransition()
    var_15 = 721.44
    var_16 = python_code_.ptnet_Gamma(Alpha=var_15, Beta=var_1)
    assert isinstance(var_16, python_code_.ptnet_Gamma)
    var_21 = python_code_.ptnet_Arc()
    var_22 = python_code_.ptnet_PTArcAnnotation(
        text=var_7, inscription=var_21, PTArcAnnotation=var_21
    )
    assert isinstance(var_22, python_code_.ptnet_PTArcAnnotation)
    var_23 = python_code_.ptnet_Exponential(Rate=var_22)
    assert isinstance(var_23, python_code_.ptnet_Exponential)
    var_25 = python_code_.ptnet_Page()
    var_26 = python_code_.ptnet_Deterministic(Value=var_15)
    assert isinstance(var_26, python_code_.ptnet_Deterministic)
    var_28 = python_code_.ptnet_NodeGraphics()
    var_29 = python_code_.ptnet_ArcGraphics()
    python_code_.ptnet_Line(
        color=var_3,
        shape={
            "ptnet_Arctoolspecifics27": -1870.11,
            "_ptnet_Measure__ptnet_Measure114-_ptnet_Measure__ptnet_Measure114": True,
            "Mn&C=`A;015STVL<,": False,
        },
        width=var_12,
        style=var_25,
        line=var_28,
        line67=var_29,
    )
    var_32 = 953
    var_33 = python_code_.ptnet_GSPNImmediateTransition(
        Priority=var_32, Weight="`VWv\rbhxEWhtZ"
    )
    assert isinstance(var_33, python_code_.ptnet_GSPNImmediateTransition)


@pytest.mark.xfail(strict=True)
def test_31():
    var_1 = "0VP^"
    var_4 = python_code_.ptnet_ComparisonOperator()
    python_code_.ptnet_PetriNetDoc(xmlns=var_1)
    var_6 = python_code_.ptnet_ArcGraphics()
    var_8 = python_code_.PNType
    var_9 = python_code_.ptnet_Gaussian(Mean=var_6, Variance=var_8)
    assert isinstance(var_9, python_code_.ptnet_Gaussian)
    var_12 = -1736.05
    var_13 = python_code_.ptnet_Uniform(Lower=(-1206.82, "", 2119), Upper=var_12)
    assert isinstance(var_13, python_code_.ptnet_Uniform)
    var_18 = python_code_.Label()
    var_21 = "g!"
    var_22 = python_code_.ptnet_PetriNet(
        id=["e}U\\$}3)nF"], type=var_21, PetriNet25=var_18
    )
    var_23 = python_code_.ptnet_AnyObject()
    python_code_.ptnet_ToolInfo(
        tool=var_4,
        version=True,
        formattedXMLBuffer=var_9,
        toolInfoGrammarURI=var_21,
        toolspecifics=var_22,
        toolspecifics27=var_8,
        ToolInfo104=var_23,
    )


@pytest.mark.xfail(strict=True)
def test_32():
    var_0 = python_code_.ptnet_LogicalExpression()
    var_1 = lambda *args, **kwargs: -1
    var_11 = -2487.39
    var_43 = python_code_.ptnet_Uniform(Lower=var_11, Upper=var_11)
    assert isinstance(var_43, python_code_.ptnet_Uniform)
    var_47 = "$\nn6(u1+"
    var_48 = python_code_.ptnet_Page()
    var_49 = python_code_.ptnet_PetriNet(
        id=var_47, type=var_0, PetriNet10=var_48, PetriNet25=var_1
    )
    python_code_.ptnet_PetriNetDoc(xmlns=var_47, PetriNetDoc=var_49)


def test_33():
    var_10 = "1p,{sU62I"
    var_26 = python_code_.ptnet_Name(text=var_10, name22=-5766.47)
    assert isinstance(var_26, python_code_.ptnet_Name)
    var_30 = python_code_.ptnet_PTMarking(text=var_10)
    assert isinstance(var_30, python_code_.ptnet_PTMarking)


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = python_code_.ptnet_OpFalse()
    var_6 = python_code_.ptnet_PnObject(
        id="eW\tfs%i\\_|x5VG]b",
        PnObject23=None,
        containerNamePnObject=var_0,
        PnObject28=None,
    )
    assert isinstance(var_6, python_code_.ptnet_PnObject)
    python_code_.ptnet_Name(text="(^>1CM@oa5]", Name=var_6, Name14=var_6)


@pytest.mark.xfail(strict=True)
def test_35():
    var_3 = 'e(Tt<\x0b=7:Lz%l^vmH"'
    var_6 = python_code_.ptnet_PnObject(id=var_3)
    assert isinstance(var_6, python_code_.ptnet_PnObject)
    python_code_.ptnet_Name(text=1825.68, Name14=var_6)


def test_36():
    var_2 = python_code_.PnObject()
    var_5 = python_code_.ptnet_IfThenElse()
    var_11 = python_code_.PlaceNode()
    var_13 = "hB#Aar~(3"
    python_code_.ptnet_Measure(
        name=var_13, ptnet_Measure117=var_5, ptnet_Measure=var_11
    )
    python_code_.ptnet_VariableValues(values=None)
    var_20 = python_code_.ptnet_VariableExpression()
    var_23 = python_code_.ptnet_OpGreater()
    var_26 = python_code_.ptnet_Coordinate(x=var_13, y=var_23)
    assert isinstance(var_26, python_code_.ptnet_Coordinate)
    var_27 = python_code_.ptnet_PTArcAnnotation(text=var_13)
    assert isinstance(var_27, python_code_.ptnet_PTArcAnnotation)
    var_28 = python_code_.ptnet_Place()
    var_29 = python_code_.ptnet_PTMarking(
        text=var_2, initialMarking=var_20, PTMarking=var_28
    )
    assert isinstance(var_29, python_code_.ptnet_PTMarking)


def test_37():
    var_20 = "_ptnet_PnObject__objects-_ptnet_PnObject__PnObject28-LEFT"
    python_code_.ptnet_Variable(name="_ptnet_PnObject__PnObject23,MEDIUM,OVERLINE")
    python_code_.ptnet_Study(name="7+Y}Ds\r")
    var_26 = python_code_.ptnet_GSPNArc(type=var_20, ptnet_GSPNArc=[])
    assert isinstance(var_26, python_code_.ptnet_GSPNArc)


def test_38():
    var_0 = -2235.82
    python_code_.ptnet_VariableValues(values=var_0)


def test_39():
    python_code_.ptnet_Variable(name=[])
    var_5 = python_code_.ptnet_IfThenElse()
    var_11 = python_code_.PlaceNode()
    var_13 = "hB#Aar~(3"
    python_code_.ptnet_Measure(
        name=var_13, ptnet_Measure117=var_5, ptnet_Measure=var_11
    )
    var_15 = python_code_.ptnet_VariableValues(values=None)
    var_18 = 2451.41
    var_19 = python_code_.ptnet_Gaussian(Mean=var_18, Variance=var_15)
    assert isinstance(var_19, python_code_.ptnet_Gaussian)
    var_23 = python_code_.ptnet_OpGreater()
    var_26 = python_code_.ptnet_Coordinate(x=var_13, y=var_23)
    assert isinstance(var_26, python_code_.ptnet_Coordinate)
    var_27 = python_code_.ptnet_PTArcAnnotation(text=var_13)
    assert isinstance(var_27, python_code_.ptnet_PTArcAnnotation)


def test_40():
    var_0 = "AnnotationGraphics63-RED"
    var_1 = python_code_.ptnet_Line(
        color=var_0, shape=var_0, width=[3121], style=var_0, Line76=890
    )
    var_2 = python_code_.ptnet_GSPNTransition()
    var_3 = "ptnet_Arc,_ptnet_PetriNet__containerPetriNet6"
    var_4 = python_code_.ptnet_Measure(name=var_3)
    var_6 = "x#T"
    var_7 = (
        "_ptnet_Name__name,NodeGraphics60,_ptnet_ToolInfo__ToolInfo104,containerPlace"
    )
    var_8 = "CROi[(\np%aWZ<|"
    var_9 = python_code_.ptnet_OpLess
    python_code_.ptnet_Font(
        align=var_3,
        decoration=var_6,
        family=var_7,
        rotation=var_8,
        size=var_9,
        style=var_6,
        weight=var_4,
        Font=var_3,
    )
    var_34 = 721.44
    var_35 = python_code_.ptnet_Gamma(Alpha=var_34, Beta=var_1)
    assert isinstance(var_35, python_code_.ptnet_Gamma)
    var_40 = python_code_.ptnet_Arc()
    var_41 = python_code_.ptnet_PTArcAnnotation(
        text=var_0, inscription=var_40, PTArcAnnotation=var_40
    )
    assert isinstance(var_41, python_code_.ptnet_PTArcAnnotation)
    var_42 = python_code_.ptnet_Exponential(Rate=var_41)
    assert isinstance(var_42, python_code_.ptnet_Exponential)
    var_44 = python_code_.ptnet_Page()
    var_45 = python_code_.ptnet_Deterministic(Value=var_34)
    assert isinstance(var_45, python_code_.ptnet_Deterministic)
    var_47 = python_code_.ptnet_NodeGraphics()
    var_48 = python_code_.ptnet_ArcGraphics()
    python_code_.ptnet_Line(
        color=var_3,
        shape={
            "ptnet_Arctoolspecifics27": -1870.11,
            "_ptnet_Measure__ptnet_Measure114-_ptnet_Measure__ptnet_Measure114": True,
            "Mn&C=`A;015STVL<,": False,
        },
        width=var_2,
        style=var_44,
        line=var_47,
        line67=var_48,
    )
    var_51 = 953
    var_52 = python_code_.ptnet_GSPNImmediateTransition(
        Priority=var_51, Weight="`VWv\rbhxEWhtZ"
    )
    assert isinstance(var_52, python_code_.ptnet_GSPNImmediateTransition)
    var_54 = 3994.1
    var_55 = python_code_.ptnet_Weibull(Alpha={}, Beta=var_54)
    assert isinstance(var_55, python_code_.ptnet_Weibull)


def test_41():
    var_0 = "AnnotationGraphics63-RED"
    var_1 = python_code_.ptnet_Line(
        color=var_0, shape=var_0, width=[3121], style=var_0, Line76=890
    )
    python_code_.ptnet_Measure(name=var_0, ptnet_Measure114=var_1)
    var_8 = "CROi[(\np%aWZ<|"
    var_44 = python_code_.ptnet_PnObject(id=var_8)
    assert isinstance(var_44, python_code_.ptnet_PnObject)


@pytest.mark.xfail(strict=True)
def test_42():
    var_1 = "0VP^"
    var_2 = "l7,!O"
    var_3 = python_code_.ptnet_Coordinate(x=var_1, y=var_2)
    assert isinstance(var_3, python_code_.ptnet_Coordinate)
    python_code_.ptnet_PetriNetDoc(xmlns=var_1)
    var_6 = python_code_.ptnet_ArcGraphics()
    var_8 = python_code_.PNType
    var_9 = python_code_.ptnet_Gaussian(Mean=var_6, Variance=var_8)
    assert isinstance(var_9, python_code_.ptnet_Gaussian)
    var_12 = -1736.05
    var_13 = python_code_.ptnet_Uniform(Lower=(-1206.82, "", 2119), Upper=var_12)
    assert isinstance(var_13, python_code_.ptnet_Uniform)
    var_16 = python_code_.ptnet_RefTransition()
    var_33 = python_code_.ptnet_Name(text={}, name22=var_6)
    assert isinstance(var_33, python_code_.ptnet_Name)
    python_code_.ptnet_PnObject(id=var_16, PnObject23=var_33, PnObject28=None)


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = python_code_.ptnet_Variable(name=[])
    var_5 = python_code_.ptnet_IfThenElse()
    var_11 = python_code_.PlaceNode()
    var_13 = "hB#Aar~(3"
    python_code_.ptnet_Measure(
        name=var_13, ptnet_Measure117=var_5, ptnet_Measure=var_11
    )
    python_code_.ptnet_VariableValues(values=-444.76, ptnet_VariableValues157=var_0)


def test_44():
    var_1 = python_code_.ptnet_ArithmeticBinaryOperator()
    var_2 = "\rNPw|M{PH4R|$?A="
    var_3 = "\x0cOOxoy`=#|FY;"
    var_4 = python_code_.ptnet_NodeGraphics
    var_6 = python_code_.ptnet_PnObject(id=var_3)
    assert isinstance(var_6, python_code_.ptnet_PnObject)
    var_7 = python_code_.ptnet_Name(text=var_3, name=var_4)
    assert isinstance(var_7, python_code_.ptnet_Name)
    var_14 = python_code_.ptnet_EvaluationList()
    var_16 = python_code_.ptnet_PTArcAnnotation(text=var_7)
    assert isinstance(var_16, python_code_.ptnet_PTArcAnnotation)
    python_code_.ptnet_Measure(name=var_2, ptnet_Measure=var_14)
    var_18 = python_code_.ptnet_GSPNArc(type=var_14)
    assert isinstance(var_18, python_code_.ptnet_GSPNArc)
    var_17 = python_code_.ptnet_PTMarking(text=var_1)
    assert isinstance(var_17, python_code_.ptnet_PTMarking)


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = python_code_.ptnet_ComparisonOperator()
    var_1 = python_code_.ptnet_Exponential(Rate=var_0)
    assert isinstance(var_1, python_code_.ptnet_Exponential)
    var_7 = "!'w)8pd"
    var_9 = lambda *args, **kwargs: 2
    var_10 = "ToolInfo-_ptnet_PnObject__PnObject"
    python_code_.ptnet_Measure(name=var_10)
    var_17 = -1285.34
    var_18 = python_code_.ptnet_VariableValues(
        values=var_17, ptnet_VariableValues157=1704.42, ptnet_VariableValues=var_9
    )
    python_code_.ptnet_Variable(name=var_7, ptnet_Variable=var_18)


def test_46():
    var_2 = python_code_.ptnet_InstantOfTime()
    var_4 = python_code_.ptnet_GSPNTimedTransition()
    var_7 = python_code_.ptnet_AnnotationGraphics()
    var_9 = lambda *args, **kwargs: True
    var_10 = "1p,{sU62I"
    var_11 = "ptnet_PnObject,MAROON,ARIAL"
    var_12 = "_ptnet_Fill__Fill52"
    python_code_.ptnet_Font(
        align=var_9,
        decoration=var_4,
        family=var_10,
        rotation=var_11,
        size=var_10,
        style="toolspecifics LIGHTER _ptnet_PetriNet__PetriNet20",
        weight=var_12,
        Font=var_7,
    )
    python_code_.ptnet_PetriNetDoc(xmlns=var_2)
    var_33 = python_code_.ptnet_Arc()
    var_34 = python_code_.ptnet_PTArcAnnotation(
        text=var_10, inscription=var_33, PTArcAnnotation=var_33
    )
    assert isinstance(var_34, python_code_.ptnet_PTArcAnnotation)
    var_44 = "containerNodeGraphics38"
    var_45 = "_ptnet_Name__Name"
    var_46 = python_code_.ptnet_Coordinate
    python_code_.ptnet_ToolInfo(
        tool=var_44,
        version={"_ptnet_PetriNet__PetriNet:ptnet_Place"},
        formattedXMLBuffer=True,
        toolInfoGrammarURI=var_45,
        ToolInfo16=var_9,
        toolspecifics=var_46,
        ToolInfo104="\x0b",
    )


def test_47():
    python_code_.ptnet_Study(name="/l/n-@p,H6A8;y2", ptnet_Study112=set())
