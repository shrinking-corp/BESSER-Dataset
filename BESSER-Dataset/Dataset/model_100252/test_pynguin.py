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
    CaseStyle,
    Enum,
    FontOption,
    Parameter,
    Pattern,
    Styling_Basic,
    Styling_BooleanParameter,
    Styling_CaseStyle,
    Styling_ConstantPattern,
    Styling_Default,
    Styling_EObject,
    Styling_EObjectParameter,
    Styling_IPredicate,
    Styling_Icon,
    Styling_IntParameter,
    Styling_ModelPattern,
    Styling_OperationPattern,
    Styling_Parameter,
    Styling_Pattern,
    Styling_Segment,
    Styling_StringParameter,
    Styling_Style,
    Styling_Styling,
    Styling_StylingModel,
    Styling_StylingPredicate,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_21 = python_code_.Styling_Parameter(name="rl5&W`?")
    assert isinstance(var_21, python_code_.Styling_Parameter)


def test_1():
    var_27 = python_code_.Styling_OperationPattern(
        operation="_Styling_Segment__Styling_Segment11:Styling_CaseStyle:_Styling_CaseStyle__Styling_CaseStyle13"
    )
    assert isinstance(var_27, python_code_.Styling_OperationPattern)
    var_28 = python_code_.Styling_Parameter(
        name="Styling_Styling.Styling_Parameter", Styling_Parameter=var_27
    )
    assert isinstance(var_28, python_code_.Styling_Parameter)


def test_2():
    var_26 = python_code_.Styling_OperationPattern(
        operation=b"*\x04g\xc4k>\xef\xcdg\xe0D\x81"
    )
    assert isinstance(var_26, python_code_.Styling_OperationPattern)


def test_3():
    var_30 = python_code_.Styling_OperationPattern(
        operation="Styling_Segment8", Styling_OperationPattern=set()
    )
    assert isinstance(var_30, python_code_.Styling_OperationPattern)


@pytest.mark.xfail(strict=True)
def test_4():
    var_24 = python_code_.Styling_Segment()
    python_code_.Styling_Pattern(Styling_Pattern=var_24)


def test_5():
    var_31 = python_code_.Styling_Pattern()
    assert var_31.Styling_Pattern is None


def test_6():
    python_code_.Styling_Segment()


def test_7():
    var_27 = python_code_.Styling_Segment(
        Styling_Segment=True,
        Styling_Segment11="Styling_OperationPattern Styling_CaseStyle",
    )
    assert var_27.Styling_Segment is True


def test_8():
    var_25 = python_code_.Styling_CaseStyle(Styling_CaseStyle10=set())
    assert isinstance(var_25, python_code_.Styling_CaseStyle)
    var_27 = python_code_.Styling_Segment(
        Styling_Segment=None, Styling_Segment8=var_25, Styling_Segment11=var_25
    )
    assert isinstance(var_27, python_code_.Styling_Segment)


def test_9():
    var_7 = python_code_.Styling_CaseStyle(
        Styling_CaseStyle13=None, Styling_CaseStyle=None
    )
    assert isinstance(var_7, python_code_.Styling_CaseStyle)


def test_10():
    var_27 = python_code_.Styling_CaseStyle(Styling_CaseStyle13=True)
    assert isinstance(var_27, python_code_.Styling_CaseStyle)


def test_11():
    var_27 = python_code_.Styling_CaseStyle(
        Styling_CaseStyle=b"\xf8\x9d\xdc\xc8p\xa6\x12"
    )
    assert isinstance(var_27, python_code_.Styling_CaseStyle)


def test_12():
    var_1 = python_code_.Styling_StylingModel(
        modeName="_Styling_Segment__Styling_Segment11"
    )
    assert isinstance(var_1, python_code_.Styling_StylingModel)


def test_13():
    var_23 = python_code_.Styling_StylingModel(
        modeName=("_Styling_Pattern__Styling_Pattern-STRIKE",),
        Styling_StylingModel15=-374.46,
    )
    assert isinstance(var_23, python_code_.Styling_StylingModel)


def test_14():
    var_26 = python_code_.Styling_StylingModel(
        modeName=complex(2241.0, -2126.875), Styling_StylingModel4="3t"
    )
    assert isinstance(var_26, python_code_.Styling_StylingModel)


def test_15():
    python_code_.Pattern()


def test_16():
    var_33 = python_code_.Styling_StringParameter(value="B/")
    assert isinstance(var_33, python_code_.Styling_StringParameter)


def test_17():
    var_31 = python_code_.Styling_BooleanParameter(value=False)
    assert isinstance(var_31, python_code_.Styling_BooleanParameter)


def test_18():
    var_26 = python_code_.Styling_IntParameter(value=3109)
    assert isinstance(var_26, python_code_.Styling_IntParameter)


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = "_Styling_OperationPattern__Styling_OperationPattern"
    var_1 = python_code_.Styling_Styling()
    var_2 = python_code_.Styling_Parameter(
        name="Styling_Segment11", Styling_Parameter=var_0
    )
    assert isinstance(var_2, python_code_.Styling_Parameter)
    var_3 = var_2.getObjectValue()
    var_4 = python_code_.Styling_StylingModel(
        modeName=var_0, Styling_StylingModel15=var_1, Styling_StylingModel=var_3
    )
    assert isinstance(var_4, python_code_.Styling_StylingModel)
    var_5 = python_code_.Styling_Pattern()
    python_code_.Styling_Segment(Styling_Segment8=var_5)
    assert isinstance(var_5.Styling_Pattern, python_code_.Styling_Segment)


def test_20():
    var_1 = python_code_.Styling_StylingModel(
        modeName="=zSXP",
        Styling_StylingModel={-2404.55, 724.26, '=x*n>\x0bNt.$M-\nN" j<o'},
    )
    assert isinstance(var_1, python_code_.Styling_StylingModel)
    var_2 = python_code_.Styling_OperationPattern(
        operation=b"*\x04g\xc4k>\xef\xcdg\xe0D\x81"
    )
    assert isinstance(var_2, python_code_.Styling_OperationPattern)
    var_3 = python_code_.Styling_StringParameter(value=complex(-1765.151809, -2224.077))
    assert isinstance(var_3, python_code_.Styling_StringParameter)
    python_code_.Styling_Segment()
    var_8 = python_code_.Styling_OperationPattern
    var_9 = python_code_.Styling_StringParameter(value=var_8)
    var_10 = python_code_.Styling_ConstantPattern(
        value="Styling_Default-_Styling_StylingModel__Styling_StylingModel2-_Styling_Style__Styling_Style-Styling_Style"
    )
    assert isinstance(var_10, python_code_.Styling_ConstantPattern)
    var_11 = python_code_.Styling_StylingPredicate()
    var_13 = "vG~*__d|ZMrW+"
    var_14 = python_code_.Styling_Icon(image=var_13, Styling_Icon="Styling_Styling")
    assert isinstance(var_14, python_code_.Styling_Icon)
    var_15 = python_code_.Styling_Pattern()
    assert var_15.Styling_Pattern is None
    var_15.getPatternValue(Styling_object=var_11)
    var_18 = python_code_.Styling_OperationPattern(
        operation=var_9, Styling_OperationPattern=var_13
    )
    assert isinstance(var_18, python_code_.Styling_OperationPattern)


def test_21():
    var_20 = python_code_.Styling_StringParameter(
        value=complex(-1765.151809, -2224.077)
    )
    assert isinstance(var_20, python_code_.Styling_StringParameter)
    var_21 = python_code_.Styling_Segment()
    var_21.getColor()
    var_23 = python_code_.Styling_CaseStyle(
        Styling_CaseStyle10=set(), Styling_CaseStyle13=None
    )
    assert isinstance(var_23, python_code_.Styling_CaseStyle)


def test_22():
    var_1 = python_code_.Styling_IntParameter(
        value={"Styling_Segment11": -330.85, "`'N": -1803}
    )
    assert isinstance(var_1, python_code_.Styling_IntParameter)
    var_2 = "|$HDUN\x0c*HT"
    var_3 = python_code_.Styling_OperationPattern(operation=var_2)
    assert isinstance(var_3, python_code_.Styling_OperationPattern)
    var_4 = python_code_.Styling_Parameter(name=var_2, Styling_Parameter=var_3)
    assert isinstance(var_4, python_code_.Styling_Parameter)
    var_4.getObjectValue()
    var_6 = python_code_.Styling_Segment(Styling_Segment8=var_4)
    var_6.setColor(Styling_color=var_1)
    var_8 = python_code_.Styling_BooleanParameter(value=False)
    assert isinstance(var_8, python_code_.Styling_BooleanParameter)
    var_9 = python_code_.Styling_Pattern()
    assert var_9.Styling_Pattern is None
    var_13 = python_code_.Styling_CaseStyle(Styling_CaseStyle13=var_8)
    assert isinstance(var_13, python_code_.Styling_CaseStyle)
    var_13.getStyledString(Styling_object=())
    python_code_.Styling_CaseStyle()
    var_6.getFont()
    var_6.getColor()


def test_23():
    var_22 = python_code_.Styling_Segment()
    var_22.getFont()
    var_25 = "vZ\rM+4EO8a"
    var_26 = python_code_.Styling_StringParameter(value=var_25)
    assert isinstance(var_26, python_code_.Styling_StringParameter)
    var_27 = python_code_.Styling_Styling()
    var_28 = python_code_.Styling_StylingModel(
        modeName=334, Styling_StylingModel15=var_27
    )
    assert isinstance(var_28, python_code_.Styling_StylingModel)
    python_code_.Styling_Icon(image=[",_yo", "Styling_Default"])


def test_24():
    var_7 = python_code_.Styling_CaseStyle(Styling_CaseStyle=None)
    assert isinstance(var_7, python_code_.Styling_CaseStyle)
    var_20 = python_code_.Styling_Segment(Styling_Segment11=var_7)
    assert isinstance(var_20, python_code_.Styling_Segment)


def test_25():
    var_7 = python_code_.Styling_CaseStyle(Styling_CaseStyle=None)
    assert isinstance(var_7, python_code_.Styling_CaseStyle)
    var_21 = python_code_.Styling_StylingModel(
        modeName="",
        Styling_StylingModel2=None,
        Styling_StylingModel={var_7, 49.91, var_7},
    )
    assert isinstance(var_21, python_code_.Styling_StylingModel)
    var_22 = python_code_.Styling_CaseStyle(Styling_CaseStyle=var_21)
    assert isinstance(var_22, python_code_.Styling_CaseStyle)
    var_7.getImage()


def test_26():
    var_2 = python_code_.Styling_StylingModel(
        modeName="Styling_Parameter _Styling_Segment__Styling_Segment11 _Styling_StylingModel__Styling_StylingModel _Styling_Style__Styling_Style"
    )
    assert isinstance(var_2, python_code_.Styling_StylingModel)
    var_3 = python_code_.Styling_CaseStyle(Styling_CaseStyle=var_2)
    assert isinstance(var_3, python_code_.Styling_CaseStyle)
    var_3.getStyledString(Styling_object=-666)


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = python_code_.Styling_Styling()
    var_2 = python_code_.Styling_Pattern(Styling_Pattern=var_0)
    assert isinstance(var_2, python_code_.Styling_Pattern)
    python_code_.Styling_Segment(Styling_Segment8=var_2, Styling_Segment11=var_2)
    assert isinstance(var_2.Styling_Pattern, python_code_.Styling_Segment)


def test_28():
    python_code_.Styling_Icon(
        image="_Styling_StylingModel__Styling_StylingModel4,Styling_StylingModel,Styling_Segment11,_Styling_OperationPattern__Styling_OperationPattern"
    )


def test_29():
    var_7 = python_code_.Styling_CaseStyle(Styling_CaseStyle10={False, 703.51})
    assert isinstance(var_7, python_code_.Styling_CaseStyle)


def test_30():
    var_38 = python_code_.Styling_StylingModel(
        modeName=complex(-1302.0911, 2392.0),
        Styling_StylingModel2={-3831.34, -2117.59, 2508.66},
    )
    assert isinstance(var_38, python_code_.Styling_StylingModel)


def test_31():
    var_21 = python_code_.Styling_ConstantPattern(value=2989)
    assert isinstance(var_21, python_code_.Styling_ConstantPattern)


def test_32():
    var_32 = python_code_.Styling_ModelPattern(attributeName=None)
    assert isinstance(var_32, python_code_.Styling_ModelPattern)


def test_33():
    python_code_.Styling_Style(
        appliedFonts=(
            "Styling_CaseStyle10,_Styling_Style__Styling_Style,Styling_Pattern",
            True,
            3,
        ),
        color=set(),
    )


def test_34():
    var_33 = python_code_.Styling_Style(
        appliedFonts={1320.2, -594.88}, color=[], Styling_Style=-43.26
    )
    assert isinstance(var_33, python_code_.Styling_Style)


def test_35():
    var_20 = python_code_.Styling_Pattern()
    assert var_20.Styling_Pattern is None
    var_20.getPattern()


def test_36():
    var_1 = python_code_.Styling_Styling()
    python_code_.Styling_Icon(image="Styling_Segment", Styling_Icon=var_1)


def test_37():
    var_1 = python_code_.Styling_StylingModel(
        modeName="_Styling_CaseStyle__Styling_CaseStyle13.Styling_Basic",
        Styling_StylingModel={1954.64, 3220},
    )
    assert isinstance(var_1, python_code_.Styling_StylingModel)


@pytest.mark.xfail(strict=True)
def test_38():
    var_30 = python_code_.Styling_OperationPattern(
        operation="Styling_Segment8", Styling_OperationPattern=set()
    )
    assert isinstance(var_30, python_code_.Styling_OperationPattern)
    var_31 = "Styling_Parameter"
    var_32 = python_code_.Styling_Style(appliedFonts=var_31, color=var_30)
    python_code_.Styling_Segment(Styling_Segment=var_32, Styling_Segment8=var_30)


def test_39():
    var_7 = python_code_.Styling_CaseStyle(Styling_CaseStyle=True)
    assert isinstance(var_7, python_code_.Styling_CaseStyle)
    var_8 = python_code_.Styling_Segment(Styling_Segment11=var_7)
    assert isinstance(var_8, python_code_.Styling_Segment)
    python_code_.Styling_Segment()
    var_10 = python_code_.Styling_ModelPattern
    var_15 = python_code_.Styling_Style(
        appliedFonts=var_10, color=var_10, Styling_Style=set()
    )
    assert isinstance(var_15, python_code_.Styling_Style)


@pytest.mark.xfail(strict=True)
def test_40():
    var_34 = bool
    var_35 = python_code_.Styling_CaseStyle(Styling_CaseStyle13=var_34)
    assert isinstance(var_35, python_code_.Styling_CaseStyle)
    python_code_.Styling_Icon(image=var_34, Styling_Icon=var_35)


@pytest.mark.xfail(strict=True)
def test_41():
    var_22 = python_code_.Styling_EObject
    var_23 = python_code_.Styling_Icon(image=var_22, Styling_Icon="\t")
    assert isinstance(var_23, python_code_.Styling_Icon)
    python_code_.Styling_CaseStyle(Styling_CaseStyle13=var_23)


def test_42():
    var_21 = python_code_.Styling_StylingModel(
        modeName="Styling_Segment",
        Styling_StylingModel2=None,
        Styling_StylingModel4=None,
        Styling_StylingModel={"xX#m", -2774.34},
    )
    assert isinstance(var_21, python_code_.Styling_StylingModel)
    var_22 = python_code_.Styling_CaseStyle(Styling_CaseStyle=var_21)
    assert isinstance(var_22, python_code_.Styling_CaseStyle)


@pytest.mark.xfail(strict=True)
def test_43():
    var_7 = python_code_.Styling_CaseStyle(
        Styling_CaseStyle10={False, "\np/*x7\\", 1},
        Styling_CaseStyle13=None,
        Styling_CaseStyle=None,
    )
    assert isinstance(var_7, python_code_.Styling_CaseStyle)
    var_22 = "'<p"
    var_23 = python_code_.Styling_Segment(Styling_Segment=())
    assert isinstance(var_23, python_code_.Styling_Segment)
    python_code_.Styling_Style(
        appliedFonts=(-1470.13, True, "Styling_Default"),
        color=var_22,
        Styling_Style=var_23,
    )
    assert isinstance(var_23.Styling_Segment, python_code_.Styling_Style)


@pytest.mark.xfail(strict=True)
def test_44():
    var_26 = python_code_.Styling_Segment(
        Styling_Segment8=[], Styling_Segment11="lu|,<WM=?_w,W"
    )
    assert isinstance(var_26, python_code_.Styling_Segment)
    python_code_.Styling_Pattern(Styling_Pattern=var_26)


def test_45():
    python_code_.Styling_Segment()
    var_1 = python_code_.Styling_CaseStyle(Styling_CaseStyle10=[])
    assert isinstance(var_1, python_code_.Styling_CaseStyle)
    var_2 = python_code_.Styling_Segment(Styling_Segment11=var_1)
    assert isinstance(var_2, python_code_.Styling_Segment)
    var_2.getColor()


def test_46():
    var_28 = python_code_.Styling_Parameter(
        name="Styling_Style:_Styling_StylingModel__Styling_StylingModel2:_Styling_Segment__Styling_Segment8"
    )
    assert isinstance(var_28, python_code_.Styling_Parameter)
    var_31 = python_code_.Styling_Basic()
    var_32 = python_code_.Styling_StylingModel(
        modeName=var_28,
        Styling_StylingModel4=var_31,
        Styling_StylingModel="1H|@\rjLJ!A",
    )
    assert isinstance(var_32, python_code_.Styling_StylingModel)
    var_33 = python_code_.Styling_CaseStyle(Styling_CaseStyle=var_32)
    assert isinstance(var_33, python_code_.Styling_CaseStyle)
    var_34 = False
    var_35 = python_code_.Styling_BooleanParameter(value=var_34)
    assert isinstance(var_35, python_code_.Styling_BooleanParameter)


def test_47():
    var_32 = python_code_.Styling_Segment()
    var_35 = "Styling_CaseStyle10.Styling_OperationPattern._Styling_Icon__Styling_Icon"
    var_36 = python_code_.Styling_OperationPattern(
        operation=var_35,
        Styling_OperationPattern=(
            "_Styling_CaseStyle__Styling_CaseStyle13 UNDERLINE _Styling_CaseStyle__Styling_CaseStyle13 STRIKE",
            "'au{:e [\"B",
        ),
    )
    assert isinstance(var_36, python_code_.Styling_OperationPattern)
    var_37 = python_code_.Styling_Parameter(name=var_32, Styling_Parameter=var_36)
    assert isinstance(var_37, python_code_.Styling_Parameter)
    var_37.getObjectValue()
