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
    DataType,
    DataTypes,
    Enum,
    Feature,
    InternalDSLType,
    Reference,
    date,
    datetime,
    time,
    titan_DataType,
    titan_Entity,
    titan_Feature,
    titan_Module,
    titan_MultiDataType,
    titan_MultiReference,
    titan_Package,
    titan_Reference,
    titan_SingleDataType,
    titan_SingleReference,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.titan_Module(
        name={"Kf": -272.3, "titan_Module": True}, type=None
    )
    assert isinstance(var_0, python_code_.titan_Module)
    var_25 = "titan_DataType:_titan_Module__titan_Module:_titan_Entity__titan_Entity:titan_Feature"
    var_34 = python_code_.titan_MultiDataType(
        unique={
            "_titan_Feature__titan_Feature:_titan_Entity__titan_Entity5": "A@$c><stx9E0WJ:`gQ",
            "MX\r>": -479.99,
        }
    )
    assert isinstance(var_34, python_code_.titan_MultiDataType)
    var_38 = True
    var_39 = python_code_.titan_MultiDataType(unique=var_38)
    python_code_.titan_DataType(type=var_25, titan_DataType=var_39)


def test_1():
    var_25 = python_code_.titan_Reference(unique=True)
    assert isinstance(var_25, python_code_.titan_Reference)


@pytest.mark.xfail(strict=True)
def test_2():
    var_27 = python_code_.Feature()
    var_29 = python_code_.titan_Entity(
        name="\tLw}1b10Q\x0b|<[.\tEYZR", titan_Entity7={-172, True, var_27}
    )
    assert isinstance(var_29, python_code_.titan_Entity)
    python_code_.titan_Reference(unique=(), titan_Reference=var_29)


def test_3():
    var_55 = python_code_.titan_Reference(unique=False, titan_Reference11=None)
    assert isinstance(var_55, python_code_.titan_Reference)
    var_56 = python_code_.titan_Reference(
        unique=var_55, titan_Reference=772.75, titan_Reference11=var_55
    )
    assert isinstance(var_56, python_code_.titan_Reference)


def test_4():
    var_26 = python_code_.titan_MultiDataType(unique=-2182.36)
    assert isinstance(var_26, python_code_.titan_MultiDataType)


def test_5():
    var_42 = python_code_.titan_MultiDataType(
        unique="_titan_DataType__titan_DataType", titan_MultiDataType=[True]
    )
    assert isinstance(var_42, python_code_.titan_MultiDataType)


def test_6():
    python_code_.titan_Feature(
        name="_titan_DataType__titan_DataType._titan_Package__titan_Package"
    )


def test_7():
    var_24 = python_code_.titan_Entity(
        name="_d*s%mMsP?aa*'PT:", titan_Entity5=None, titan_Entity7=set()
    )
    assert isinstance(var_24, python_code_.titan_Entity)


def test_8():
    var_24 = python_code_.titan_Entity(name="_titan_Package__titan_Package2")
    assert isinstance(var_24, python_code_.titan_Entity)


@pytest.mark.xfail(strict=True)
def test_9():
    var_25 = ()
    var_40 = python_code_.titan_Entity(name=[False, False], titan_Entity3=var_25)
    assert isinstance(var_40, python_code_.titan_Entity)
    python_code_.titan_Entity(name=var_25, titan_Entity5=var_40)


def test_10():
    var_17 = python_code_.DataType()
    var_24 = python_code_.titan_Entity(
        name="_titan_Module__titan_Module-_titan_Entity__titan_Entity9",
        titan_Entity=var_17,
        titan_Entity5=var_17,
        titan_Entity3=var_17,
        titan_Entity7=set(),
    )
    assert isinstance(var_24, python_code_.titan_Entity)


def test_11():
    var_40 = "j.WQ"
    var_41 = python_code_.titan_Module(name=var_40, type=())
    assert isinstance(var_41, python_code_.titan_Module)
    var_42 = "NnLx"
    var_43 = python_code_.titan_Feature(name=var_42)
    var_44 = {var_43, var_43, var_43}
    var_45 = python_code_.titan_Entity(
        name=var_40,
        titan_Entity=var_41,
        titan_Entity5=-1764.71,
        titan_Entity7=var_44,
        titan_Entity9=var_41,
    )
    assert isinstance(var_45.titan_Entity9, python_code_.titan_Module)
    var_46 = {var_45, var_45, var_45, var_45}
    var_47 = python_code_.titan_Package(
        name=None, titan_Package=var_41, titan_Package2=var_46
    )
    assert isinstance(var_47, python_code_.titan_Package)


def test_12():
    var_49 = python_code_.titan_Entity(name="i", titan_Entity=[])
    assert isinstance(var_49, python_code_.titan_Entity)


def test_13():
    var_19 = python_code_.titan_Package(
        name="5n*.\r", titan_Package=None, titan_Package2={1180.76}
    )
    assert isinstance(var_19, python_code_.titan_Package)


def test_14():
    var_19 = python_code_.titan_Package(name="")
    assert isinstance(var_19, python_code_.titan_Package)


def test_15():
    var_26 = python_code_.titan_Package(name=1, titan_Package=False)
    assert isinstance(var_26, python_code_.titan_Package)


def test_16():
    var_0 = python_code_.titan_Module(
        name="titan_Entity3", type='{^2L",7]7m', titan_Module=set()
    )
    assert isinstance(var_0, python_code_.titan_Module)


def test_17():
    var_0 = python_code_.titan_Module(name="Q)qO4=mp;", type="*\\)D\x0chh")
    assert isinstance(var_0, python_code_.titan_Module)


def test_18():
    python_code_.titan_SingleDataType()


def test_19():
    var_24 = python_code_.titan_DataType(
        type=[
            False,
            "titan_MultiDataType.titan_Entity9._titan_Package__titan_Package._titan_Reference__titan_Reference11",
            5642.8,
        ]
    )
    assert isinstance(var_24, python_code_.titan_DataType)


def test_20():
    var_19 = python_code_.titan_Package(name="zgF<M&5)k", titan_Package=None)
    assert isinstance(var_19, python_code_.titan_Package)
    var_27 = {var_19, var_19, var_19, var_19}
    var_28 = python_code_.titan_Module(name=var_19, type=var_19, titan_Module=var_27)
    assert isinstance(var_28, python_code_.titan_Module)


def test_21():
    var_0 = python_code_.titan_Module(
        name="ASKa1RYogMl_PR%", type='UlrYS"xN', titan_Module={0}
    )
    assert isinstance(var_0, python_code_.titan_Module)
    var_19 = python_code_.titan_Package(name='y1Gl%2\x0b\n]V!q"!E', titan_Package=var_0)
    assert isinstance(var_19, python_code_.titan_Package)


def test_22():
    var_49 = python_code_.titan_Entity(
        name="7#B0Zrf", titan_Entity=None, titan_Entity3=None
    )
    assert isinstance(var_49, python_code_.titan_Entity)
    var_54 = python_code_.titan_Feature(name='Q>b\tNx]w@:(w":NL', titan_Feature=var_49)
    assert isinstance(var_54, python_code_.titan_Feature)


def test_23():
    var_49 = python_code_.titan_Entity(
        name="titan_Entity9-_titan_DataType__titan_DataType-titan_Entity7-_titan_Package__titan_Package",
        titan_Entity=None,
        titan_Entity3=None,
    )
    assert isinstance(var_49, python_code_.titan_Entity)
    var_56 = python_code_.titan_Package(
        name="j:f\r>rBy\x0c`oQ7#", titan_Package=None, titan_Package2={var_49, var_49}
    )
    assert isinstance(var_56, python_code_.titan_Package)


def test_24():
    var_19 = python_code_.titan_Package(
        name="titan_Package2,_titan_Entity__titan_Entity5,titan_Entity7,_titan_Package__titan_Package",
        titan_Package=None,
    )
    assert isinstance(var_19, python_code_.titan_Package)
    var_26 = python_code_.titan_Entity(
        name=var_19, titan_Entity=var_19, titan_Entity3=var_19
    )
    assert isinstance(var_26, python_code_.titan_Entity)


def test_25():
    var_0 = python_code_.titan_Module(
        name="titan_Entity3",
        type="_titan_Package__titan_Package2._titan_Entity__titan_Entity5",
        titan_Module={False},
    )
    assert isinstance(var_0, python_code_.titan_Module)
    var_27 = python_code_.titan_Feature(name="Tn{H*y/BCYnU?Qh$;[", titan_Feature=var_0)
    var_30 = {var_27}
    var_31 = python_code_.titan_Entity(
        name=True, titan_Entity3={322.92}, titan_Entity7=var_30
    )
    assert isinstance(var_31, python_code_.titan_Entity)


def test_26():
    var_32 = python_code_.titan_Reference(unique={2875, 2456}, titan_Reference11=-2872)
    assert isinstance(var_32, python_code_.titan_Reference)


def test_27():
    var_19 = python_code_.titan_Package(
        name="titan_Entity9:_titan_Package__titan_Package2"
    )
    assert isinstance(var_19, python_code_.titan_Package)
    var_26 = python_code_.titan_Entity(
        name=var_19, titan_Entity=var_19, titan_Entity3=var_19
    )
    assert isinstance(var_26, python_code_.titan_Entity)
    python_code_.titan_Package(
        name="j:f\r>rBy\x0c`oQ7#", titan_Package=None, titan_Package2={var_26, var_26}
    )


def test_28():
    var_27 = python_code_.titan_Feature(
        name={
            "_titan_Feature__titan_Feature_titan_Entity__titan_Entity5titan_Module": False,
            "3E9m!n:bo}t27f": True,
        }
    )
    var_30 = {var_27}
    var_31 = python_code_.titan_Entity(
        name=True, titan_Entity3={322.92}, titan_Entity7=var_30
    )
    assert isinstance(var_31, python_code_.titan_Entity)


@pytest.mark.xfail(strict=True)
def test_29():
    var_6 = "@5\x0b^.-?l[{7vwc%,"
    var_7 = python_code_.titan_Entity(name=var_6, titan_Entity5=())
    assert isinstance(var_7, python_code_.titan_Entity)
    var_8 = set()
    var_9 = False
    var_10 = python_code_.titan_Reference(unique=var_9)
    assert isinstance(var_10, python_code_.titan_Reference)
    python_code_.titan_Entity(
        name=-80.23, titan_Entity3=var_7, titan_Entity7=var_8, titan_Entity9=var_10
    )


def test_30():
    var_40 = python_code_.titan_Entity(name="(&20", titan_Entity3=None)
    assert isinstance(var_40, python_code_.titan_Entity)
    var_47 = "_titan_Entity__titan_Entity3,titan_Reference,Integer"
    var_48 = python_code_.titan_Entity(name=var_47, titan_Entity5=var_47)
    assert isinstance(var_48, python_code_.titan_Entity)
    var_49 = python_code_.titan_Feature(name=var_47)
    var_50 = "t_qE:D|"
    var_51 = "b:Z_y!I"
    var_52 = "qJ+3o?"
    var_53 = python_code_.titan_Package(name=var_52, titan_Package=var_49)
    assert isinstance(var_53, python_code_.titan_Package)
    var_54 = {var_53, var_53}
    var_55 = python_code_.titan_Module(name=var_51, type=var_47, titan_Module=var_54)
    assert isinstance(var_55, python_code_.titan_Module)
    var_56 = python_code_.titan_Package(name=var_50, titan_Package=var_55)
    assert isinstance(var_56, python_code_.titan_Package)


def test_31():
    var_29 = "\r,2f:UBW+o"
    var_30 = python_code_.titan_Entity(
        name=var_29, titan_Entity5=complex(935.31, -2426.9)
    )
    assert isinstance(var_30, python_code_.titan_Entity)
    var_31 = python_code_.Feature()
    var_33 = "<WK[{r"
    var_34 = python_code_.titan_Package(name=var_33)
    assert isinstance(var_34, python_code_.titan_Package)
    var_35 = "8m&}hIZS\tyu@gE+F"
    var_36 = python_code_.titan_Module(name="Jt", type="g2?mfPp!JvD`")
    assert isinstance(var_36, python_code_.titan_Module)
    var_37 = {var_30, var_30, "]_5(_|;*ay+<`}k@"}
    var_38 = python_code_.titan_Package(
        name=var_35, titan_Package=var_36, titan_Package2=var_37
    )
    assert isinstance(var_38, python_code_.titan_Package)
    var_39 = {var_34, var_34, var_34, var_38, var_38}
    python_code_.titan_Module(name=var_31, type=False, titan_Module=var_39)
    var_41 = python_code_.titan_DataType(type=var_30)
    assert isinstance(var_41, python_code_.titan_DataType)


@pytest.mark.xfail(strict=True)
def test_32():
    var_1 = "?"
    var_2 = python_code_.titan_Feature(
        name=var_1,
        titan_Feature={
            "?'\n\x0c0uCq\rjYr88R7M+": "titan_MultiReference",
            "BP%?)(,r\rm%(+~O}pBS": False,
            '33VIq#m)K"BW.pg': "E>31?a#Xh",
        },
    )
    assert isinstance(var_2, python_code_.titan_Feature)
    var_4 = python_code_.titan_Entity(name=var_1, titan_Entity9=var_1)
    assert isinstance(var_4, python_code_.titan_Entity)
    python_code_.titan_Reference(unique=var_2, titan_Reference=var_4)
    assert isinstance(var_4.titan_Entity9, python_code_.titan_Reference)


@pytest.mark.xfail(strict=True)
def test_33():
    var_1 = lambda *args, **kwargs: False
    python_code_.titan_Feature(name=[])
    var_12 = python_code_.titan_MultiReference()
    var_42 = python_code_.titan_Reference(unique=var_1, titan_Reference=var_1)
    assert isinstance(var_42, python_code_.titan_Reference)
    python_code_.titan_Entity(name=var_12, titan_Entity9=var_42)


def test_34():
    var_37 = "8m&}hIZS\tyu@gE+F"
    var_38 = python_code_.titan_Module(name="Jt", type="g2?mfPp!JvD`")
    assert isinstance(var_38, python_code_.titan_Module)
    var_39 = python_code_.titan_Package(name=var_37, titan_Package2=[])
    assert isinstance(var_39, python_code_.titan_Package)
    var_40 = python_code_.titan_Package
    var_41 = python_code_.titan_Feature(name=var_40)
    var_42 = {var_41, var_41}
    var_43 = python_code_.titan_Entity(
        name=b"e\xb8\x0f}\xcdeHr\x9a\x17\xd5\x9a\xc5",
        titan_Entity=var_39,
        titan_Entity3="_titan_Package__titan_Package2:titan_MultiReference:NestedFunctions:titan_Package2",
        titan_Entity7=var_42,
        titan_Entity9="titan_Feature",
    )
    assert var_43.titan_Entity9 == "titan_Feature"


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = "_titan_Feature__titan_Feature _titan_Reference__titan_Reference"
    var_1 = python_code_.titan_Reference
    var_2 = python_code_.titan_Module(name=var_1, type=var_0, titan_Module=var_0)
    assert isinstance(var_2, python_code_.titan_Module)
    var_3 = python_code_.titan_Package(name=var_0, titan_Package=var_2)
    assert isinstance(var_3, python_code_.titan_Package)
    python_code_.titan_Package(name=None)
    var_10 = {var_3, var_3, var_3}
    var_11 = python_code_.titan_Module(name=var_0, type=var_0, titan_Module=var_10)
    assert isinstance(var_11, python_code_.titan_Module)
    var_12 = python_code_.titan_MultiDataType(unique=var_1)
    assert isinstance(var_12, python_code_.titan_MultiDataType)
    var_13 = python_code_.titan_DataType(type=var_3, titan_DataType=var_12)
    var_21 = python_code_.titan_MultiReference()
    var_25 = python_code_.titan_Module(name=var_0, type=var_13)
    var_26 = "/RH_"
    python_code_.titan_Module(name=var_26, type=4209, titan_Module=var_10)
    python_code_.titan_Reference(unique=var_25)
    python_code_.titan_Reference(unique={}, titan_Reference11=var_21)


def test_36():
    var_49 = python_code_.titan_Entity(name="w/q\nS}!9PhU2Jx6,on", titan_Entity3=None)
    assert isinstance(var_49, python_code_.titan_Entity)
    var_59 = "q"
    var_60 = python_code_.titan_Feature(name=-452.41, titan_Feature=var_49)
    assert isinstance(var_60, python_code_.titan_Feature)
    var_61 = {var_60}
    python_code_.titan_Entity(name=var_59, titan_Entity7=var_61)


def test_37():
    var_2 = "titan_MultiReference:_titan_DataType__titan_DataType:Boolean:_titan_Module__titan_Module"
    var_3 = python_code_.titan_DataType(type=var_2)
    assert isinstance(var_3, python_code_.titan_DataType)
    var_5 = python_code_.InternalDSLType.NestedFunctions
    var_8 = lambda *args, **kwargs: 3
    var_9 = python_code_.titan_Module(name=[-892.31], type=var_8)
    assert isinstance(var_9, python_code_.titan_Module)
    var_10 = False
    var_11 = python_code_.titan_MultiDataType(unique=var_10)
    assert isinstance(var_11, python_code_.titan_MultiDataType)
    var_15 = python_code_.titan_Entity(name=var_2, titan_Entity7={})
    assert isinstance(
        python_code_.titan_Entity.titan_Entity9, python_code_.titan_Reference
    )
    python_code_.titan_Feature(name=None, titan_Feature=var_15)
    python_code_.titan_Package(name=var_5)
    python_code_.titan_Feature(name=var_8)
    python_code_.titan_Reference(unique=None)
