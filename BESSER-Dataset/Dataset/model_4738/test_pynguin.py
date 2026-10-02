#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    DynamicPage,
    Enum,
    Link,
    Page,
    SWMLTypes,
    abstractmethod,
    date,
    datetime,
    swml_Attribute,
    swml_CLink,
    swml_Class,
    swml_ContentLayer,
    swml_DetailsPage,
    swml_DynamicPage,
    swml_HypertextLayer,
    swml_IndexPage,
    swml_Link,
    swml_NCLink,
    swml_Page,
    swml_StaticPage,
    swml_WebModel,
    time,
)


def test_0():
    python_code_.swml_Attribute(name="", type='&l$RW"Ku(')


def test_1():
    var_5 = python_code_.swml_Class(name="^kM.ZO)<]M")
    assert isinstance(var_5, python_code_.swml_Class)
    var_9 = python_code_.swml_Attribute(
        name='I\x0bw\x0c;{@3y"4P', type="$", swml_Attribute=var_5
    )
    assert isinstance(var_9, python_code_.swml_Attribute)


def test_2():
    var_22 = python_code_.swml_Class
    var_23 = python_code_.swml_Attribute(
        name='RgrXBB7"\rfVC',
        type="38:2>",
        swml_Attribute=var_22,
        swml_Attribute14=var_22,
    )
    assert isinstance(var_23, python_code_.swml_Attribute)


def test_3():
    var_5 = python_code_.swml_Class(name="n#g\x0cc}G=2|\t]b^:", swml_Class11=set())
    assert isinstance(var_5, python_code_.swml_Class)


def test_4():
    var_5 = python_code_.swml_Class(
        name="swml_Attribute", swml_Class=None, swml_Class13=None
    )
    assert isinstance(var_5, python_code_.swml_Class)


def test_5():
    var_5 = python_code_.swml_ContentLayer()
    var_7 = python_code_.swml_Class(
        name=complex(1280.721215, -2378.25717), swml_Class=var_5
    )
    assert isinstance(var_7, python_code_.swml_Class)


def test_6():
    var_16 = python_code_.swml_Class(name=False, swml_Class18={})
    assert isinstance(var_16, python_code_.swml_Class)


def test_7():
    var_10 = python_code_.swml_Page(
        name="swml_Link _swml_Class__swml_Class13 _swml_WebModel__swml_WebModel",
        swml_Page=None,
        swml_Page16={778.71, "bP5n\\`"},
    )
    assert isinstance(var_10, python_code_.swml_Page)


def test_8():
    var_10 = python_code_.swml_Page(name=(False,))
    assert isinstance(var_10, python_code_.swml_Page)


def test_9():
    var_2 = python_code_.swml_HypertextLayer()
    var_3 = python_code_.swml_Page(name=";mfVGSYH", swml_Page21=var_2)
    assert isinstance(var_3, python_code_.swml_Page)


def test_10():
    var_11 = python_code_.swml_Page(
        name=[], swml_Page16=(-3526.87, True), swml_Page7=set()
    )
    assert isinstance(var_11, python_code_.swml_Page)


def test_11():
    var_15 = python_code_.swml_Page(name=-1417.69, swml_Page=(-452, -1757.06))
    assert isinstance(var_15, python_code_.swml_Page)


def test_12():
    python_code_.swml_WebModel(
        name="_swml_Page__swml_Page7,_swml_WebModel__swml_WebModel,_swml_Page__swml_Page16,_swml_Page__swml_Page21",
        swml_WebModel=None,
        swml_WebModel2=None,
    )


def test_13():
    var_4 = "U%b6N|xc-9\tY g{"
    var_6 = python_code_.swml_WebModel(
        name=var_4, swml_WebModel=var_4, swml_WebModel2=-297.38
    )
    assert isinstance(var_6, python_code_.swml_WebModel)


def test_14():
    python_code_.SWMLTypes.String


def test_15():
    var_5 = python_code_.swml_Class(name="swml_DynamicPage", swml_Class=None)
    assert isinstance(var_5, python_code_.swml_Class)
    assert isinstance(python_code_.swml_Class.swml_Class13, python_code_.swml_Attribute)
    var_19 = python_code_.swml_Attribute(
        name='I\x0bw\x0c;{@3y"4P', type="$", swml_Attribute=var_5
    )
    assert isinstance(var_19, python_code_.swml_Attribute)
    var_20 = {var_19, var_19, var_5}
    python_code_.swml_Class(name="hs[}45i%", swml_Class11=var_20)


def test_16():
    var_14 = python_code_.swml_IndexPage(
        size={"uJ+8$o|kv-#3GPD": 2845.6, "7:h": 323.09, "\r+\x0c:KK,\rF)e3dR<}y~": ""}
    )
    assert isinstance(var_14, python_code_.swml_IndexPage)


def test_17():
    var_0 = "& q,!fOB\x0c78"
    python_code_.swml_WebModel(name=var_0)
    var_10 = "String"
    var_11 = "_swml_Attribute__swml_Attribute14.swml_HypertextLayer6"
    var_12 = python_code_.swml_Attribute(name=var_10, type=var_11, swml_Attribute={})
    assert isinstance(var_12, python_code_.swml_Attribute)


def test_18():
    var_0 = python_code_.SWMLTypes.Email
    var_3 = python_code_.swml_ContentLayer()
    var_5 = python_code_.swml_Class(
        name=complex(1280.721215, -2378.25717), swml_Class=var_3
    )
    assert isinstance(var_5, python_code_.swml_Class)
    var_6 = python_code_.swml_Attribute(
        name=var_0,
        type=b"\x9c\xcc\xa0\x85\x17\xa3\x86\x18)\xec\xc6\xed",
        swml_Attribute=var_5,
        swml_Attribute14=var_0,
    )
    assert isinstance(var_6, python_code_.swml_Attribute)


def test_19():
    var_7 = python_code_.swml_Attribute(
        name="]%f}}",
        type="_swml_WebModel__swml_WebModel2,_swml_Class__swml_Class13,_swml_Page__swml_Page,_swml_Class__swml_Class13",
        swml_Attribute14=None,
    )
    python_code_.swml_Class(name="o4Ewf^k", swml_Class=var_7, swml_Class13=var_7)


def test_20():
    var_0 = python_code_.SWMLTypes.Email
    var_4 = python_code_.swml_Link
    var_5 = python_code_.swml_Page(name=var_4, swml_Page16={})
    assert isinstance(var_5, python_code_.swml_Page)
    var_7 = "KA+Ye3,& :"
    var_8 = python_code_.swml_Class(name=var_7, swml_Class13=var_0)
    assert isinstance(var_8, python_code_.swml_Class)


def test_21():
    var_0 = set
    var_1 = "Email"
    var_2 = python_code_.swml_Attribute(
        name=var_0, type=var_1, swml_Attribute=var_0, swml_Attribute14=var_1
    )
    assert isinstance(var_2, python_code_.swml_Attribute)
    var_3 = {var_2}
    python_code_.swml_Class(name=set(), swml_Class11=var_3, swml_Class13=var_2)


def test_22():
    var_0 = python_code_.swml_DetailsPage()
    var_1 = "swml_HypertextLayer"
    var_2 = python_code_.swml_Page
    var_3 = "Email.swml_HypertextLayer6"
    var_4 = python_code_.swml_Class(name=var_3, swml_Class13=var_0)
    assert isinstance(var_4, python_code_.swml_Class)
    python_code_.swml_Attribute(name=var_1, type=var_2, swml_Attribute14=var_4)
    assert isinstance(var_4.swml_Class13, python_code_.swml_Attribute)


def test_23():
    var_22 = python_code_.swml_Class
    var_23 = python_code_.swml_Attribute(
        name=var_22, type=var_22, swml_Attribute=var_22
    )
    assert isinstance(var_23, python_code_.swml_Attribute)
