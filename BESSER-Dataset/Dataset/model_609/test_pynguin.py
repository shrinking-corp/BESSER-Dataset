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
    Behavior,
    Charset,
    ColumnType,
    Enum,
    FormMethod,
    InputType,
    Instruction,
    Tag,
    abstractmethod,
    date,
    datetime,
    time,
    webapp_Action,
    webapp_AppConfig,
    webapp_Attribute,
    webapp_BusinessObject,
    webapp_Check,
    webapp_Column,
    webapp_Constraint,
    webapp_Controller,
    webapp_Detail,
    webapp_Field,
    webapp_File,
    webapp_ForeignKey,
    webapp_Form,
    webapp_Image,
    webapp_Input,
    webapp_Instruction,
    webapp_Library,
    webapp_Mapping,
    webapp_Messages,
    webapp_Model,
    webapp_Navigation,
    webapp_OnDelete,
    webapp_OnUpdate,
    webapp_Page,
    webapp_PrimaryKey,
    webapp_Properties,
    webapp_Resource,
    webapp_Table,
    webapp_TableHTML,
    webapp_Tag,
    webapp_Td,
    webapp_Text,
    webapp_Th,
    webapp_Tr,
    webapp_Unique,
    webapp_Validator,
    webapp_View,
    webapp_WebApp,
    webapp_WebConfig,
)


def test_0():
    var_3 = "P\t(0$Y5W"
    var_5 = "s#ZV$cd9|gR<b@r*="
    python_code_.webapp_Attribute(name=var_5, value=var_3)
    python_code_.webapp_WebConfig(displayName=var_3)


def test_1():
    var_3 = "P\t(0$Y5W"
    var_5 = "s#ZV$cd9|gR<b@r*="
    var_6 = python_code_.webapp_Attribute(
        name=var_5, value="Q';,zjKO5tlEP5\n<e{", webapp_Attribute=var_5
    )
    assert isinstance(var_6, python_code_.webapp_Attribute)
    python_code_.webapp_Check(expr=var_3, webapp_Check=None)
    python_code_.webapp_Navigation(message=(True, True))


def test_2():
    var_1 = "x2v6\x0bZ^d\x0c\x0b6YN|Q"
    var_2 = "u?\n\x0c?$ i2z5Dwupf"
    python_code_.webapp_Model(
        databaseName=var_1, url=var_1, userName=complex(-73.0, 2202.676), password=var_2
    )
    var_5 = python_code_.webapp_Attribute(name=var_1, value=1013)
    var_6 = {var_5, var_5, var_5, var_5}
    var_7 = python_code_.webapp_Td()
    var_8 = python_code_.webapp_Tag(
        _property=complex(1158.0, 1331.5357183),
        webapp_Tag82=var_6,
        webapp_Tag=var_1,
        webapp_Tag103=var_7,
    )
    assert isinstance(var_8, python_code_.webapp_Tag)
    python_code_.webapp_WebApp(
        name=(-1166.54, True, False), framework=var_2, webapp_WebApp6=None
    )
    var_10 = python_code_.webapp_Controller()
    python_code_.webapp_WebApp(
        name=var_5, framework=var_2, webapp_WebApp10=var_10, webapp_WebApp12=var_1
    )
    var_29 = "r|1(H,DE.["
    var_31 = python_code_.webapp_Input(
        type="-", webapp_Input86=var_29, webapp_Input92=None
    )
    assert isinstance(var_31, python_code_.webapp_Input)


def test_3():
    var_0 = python_code_.webapp_Tag(_property=-1206.18)
    assert isinstance(var_0, python_code_.webapp_Tag)


def test_4():
    var_40 = "=Z'3E`GeXSE"
    var_41 = python_code_.webapp_Input(
        type="-", webapp_Input86=var_40, webapp_Input92=None
    )
    assert isinstance(var_41, python_code_.webapp_Input)
    python_code_.webapp_Navigation(message=var_40)
    var_43 = "P\t(0$Y5W"
    python_code_.webapp_Check(expr=var_43)
    var_46 = "|?Cv`"
    var_47 = "_webapp_WebApp__webapp_WebApp8,_webapp_WebApp__webapp_WebApp10,LATIN2"
    var_48 = python_code_.webapp_Form(method=361)
    assert isinstance(var_48, python_code_.webapp_Form)
    var_49 = python_code_.webapp_Tag(_property=var_47, webapp_Tag=var_48)
    assert isinstance(var_49, python_code_.webapp_Tag)
    var_50 = python_code_.webapp_Attribute(
        name=1447.74, value=var_46, webapp_Attribute=var_49
    )
    assert isinstance(var_50, python_code_.webapp_Attribute)


def test_5():
    var_18 = python_code_.webapp_Form(
        method="2F\n;s7YxQ7\\H7A+m\x0b", webapp_Form=set()
    )
    assert isinstance(var_18, python_code_.webapp_Form)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.FormMethod.GET
    var_1 = "webapp_Controller_webapp_Table__webapp_Table34"
    var_2 = bytes
    python_code_.webapp_Field(
        name=var_2, type=var_1, defaultValue=2, webapp_Field106=var_0
    )
    var_4 = "U@6q5A2[l`"
    python_code_.webapp_BusinessObject(
        name=var_4,
        package=-566,
        webapp_BusinessObject114=var_2,
        webapp_BusinessObject105=var_2,
        webapp_BusinessObject112="~2F\t2",
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.FormMethod.GET
    var_1 = "x2v6\x0bZ^d\x0c\x0b6YN|Q"
    var_2 = "u?\n\x0c?$ i2z5Dwupf"
    python_code_.webapp_Model(
        databaseName=var_1, url=var_1, userName=complex(-73.0, 2202.676), password=var_2
    )
    var_5 = python_code_.webapp_Attribute(name=var_1, value=1013)
    var_6 = {var_5, var_5, var_5, var_5}
    var_7 = python_code_.webapp_Td()
    var_8 = python_code_.webapp_Tag(
        _property=complex(1158.0, 1331.5357183),
        webapp_Tag82=var_6,
        webapp_Tag=var_1,
        webapp_Tag103=var_7,
    )
    assert isinstance(var_8, python_code_.webapp_Tag)
    python_code_.webapp_WebApp(
        name=(-1166.54, True, False), framework=var_2, webapp_WebApp6=None
    )
    var_10 = python_code_.webapp_Controller()
    var_11 = python_code_.webapp_WebApp(
        name=var_5, framework=var_2, webapp_WebApp10=var_10, webapp_WebApp12=var_1
    )
    python_code_.webapp_Action(name=None, returnType=var_11)
    python_code_.webapp_Validator(name=var_2, package=var_2)
    var_18 = python_code_.webapp_Form
    var_19 = python_code_.webapp_Action(
        name=var_18, returnType=var_18, webapp_Action109=var_0
    )
    var_20 = "9"
    var_21 = python_code_.webapp_Field(name=var_2, type=var_20, defaultValue=var_2)
    python_code_.webapp_Input(
        type=var_18, webapp_Input=var_19, webapp_Input86=var_11, webapp_Input92=var_21
    )


def test_8():
    var_3 = "P\t(0$Y5W"
    python_code_.webapp_WebApp(
        name=(-1166.54, True, False), framework=var_3, webapp_WebApp6=None
    )
    var_8 = "r|1(H,DE.["
    var_10 = python_code_.webapp_Input(
        type="-", webapp_Input86=var_8, webapp_Input92=None
    )
    assert isinstance(var_10, python_code_.webapp_Input)


def test_9():
    var_0 = python_code_.Tag()
    var_5 = "_webapp_Tag_webapp_Tag103 UCS2"
    var_7 = "=Z'3E`GeXE"
    var_8 = python_code_.webapp_Input(type=var_5, webapp_Input92=var_0)
    assert isinstance(var_8, python_code_.webapp_Input)
    python_code_.webapp_Navigation(message=var_7)
    python_code_.webapp_Check(expr="GBK")


@pytest.mark.xfail(strict=True)
def test_10():
    var_3 = python_code_.webapp_Image
    var_6 = "r|1(H,DE.["
    var_7 = "=Z'3E`GeXSE"
    var_8 = python_code_.webapp_Input(
        type="-", webapp_Input86=var_6, webapp_Input92=None
    )
    assert isinstance(var_8, python_code_.webapp_Input)
    python_code_.webapp_Mapping(
        left="3iS%RPcU;Z:H,pwDC",
        right=var_7,
        webapp_Mapping=var_3,
        webapp_Mapping90=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_1 = python_code_.webapp_Resource()
    var_2 = python_code_.webapp_AppConfig()
    var_3 = python_code_.webapp_Image
    var_7 = "=Z'3E`GeXSE"
    var_8 = python_code_.webapp_Input(
        type=var_3, webapp_Input89=var_1, webapp_Input94=b"\xc3"
    )
    assert isinstance(var_8, python_code_.webapp_Input)
    python_code_.webapp_Mapping(left=var_2, right=var_7, webapp_Mapping90=var_8)


def test_12():
    var_3 = python_code_.Charset
    var_7 = "=Z'3E`GeXSE"
    python_code_.webapp_WebConfig(displayName=var_7)
    var_16 = "rZ]"
    python_code_.webapp_Validator(
        name=var_16, package=var_3, webapp_Validator67=complex(2924.0, -763.98681)
    )
    var_18 = python_code_.Instruction()
    var_19 = python_code_.webapp_Input(type=var_3, webapp_Input=var_18)
    assert isinstance(var_19, python_code_.webapp_Input)
    python_code_.webapp_OnDelete(behavior=var_16)


def test_13():
    var_0 = "T\r%al9b}KpEr`n{"
    python_code_.webapp_OnDelete(behavior=var_0)


def test_14():
    var_3 = "P\t(0$Y5W"
    python_code_.webapp_Check(expr=var_3)


def test_15():
    python_code_.webapp_Check(expr=[], webapp_Check={})
    var_24 = "TU+R}"
    python_code_.webapp_Mapping(
        left=b"2z|_\xf3\x00",
        right=var_24,
        webapp_Mapping74={
            '@=4t5]\x0bA}U{`#``>"': True,
            "lw]fs": "T+re7-HFsb\ngJ9NupG",
            "_webapp_Navigation__webapp_Navigation120": "0aJb 'qkzlS",
        },
    )
    var_26 = python_code_.webapp_Controller()
    var_28 = "&nzy8"
    python_code_.webapp_Action(
        name=complex(186.8928, -80.5112823), returnType=var_28, webapp_Action=var_26
    )


def test_16():
    var_0 = -3078
    python_code_.webapp_Detail(precision=complex(381.7, -2584.4), scale=var_0)
    var_2 = python_code_.webapp_Resource
    python_code_.webapp_WebConfig(displayName=-2310, webapp_WebConfig=var_2)


def test_17():
    var_0 = python_code_.ColumnType.CHAR
    var_1 = lambda *args, **kwargs: [668.0, 1238, -34.04]
    var_3 = "`?Dd4?;p@-ou;(@$Dl/Z"
    var_4 = "TINYTEXT"
    python_code_.webapp_WebApp(name=False, framework=var_4, webapp_WebApp12=var_3)
    var_7 = python_code_.webapp_Attribute(name=var_0, value=var_1)
    var_8 = {var_7, var_7, False}
    var_9 = python_code_.webapp_Td()
    var_10 = python_code_.webapp_Tag(
        _property=var_3, webapp_Tag82=var_8, webapp_Tag103=var_9
    )
    assert isinstance(var_10, python_code_.webapp_Tag)
    var_11 = python_code_.webapp_View()
    python_code_.webapp_Navigation(
        message=complex(2740.5218687, 1053.0),
        webapp_Navigation=var_11,
        webapp_Navigation120=var_1,
    )
    python_code_.webapp_Column(
        name=var_4,
        isNotNull=True,
        size=1378,
        useZeroFill=False,
        type=var_4,
        defaultValue=".3fL9He^UeT4V",
        webapp_Column62=None,
    )
    python_code_.webapp_Mapping(left=var_4, right=var_4, webapp_Mapping90=(-991.49,))


def test_18():
    var_0 = -3731
    python_code_.webapp_Detail(precision=complex(381.7, -2584.4), scale=var_0)
    var_2 = python_code_.webapp_Column
    python_code_.webapp_WebConfig(displayName=-2310, webapp_WebConfig=var_2)
    var_4 = python_code_.webapp_Resource()
    var_6 = python_code_.webapp_TableHTML()
    var_7 = "webapp_Properties_webapp_Table__webapp_Table36webapp_BusinessObject118"
    var_8 = python_code_.webapp_Properties(
        name=var_6, package=var_4, webapp_Properties71=True
    )
    python_code_.webapp_Mapping(
        left=b"\xfa\xb5\xa3\xceq\x190\xd9\xf3\t\xf8\xf6\xe6]{+",
        right=var_7,
        webapp_Mapping=var_8,
    )
    var_10 = python_code_.webapp_Image()
    var_11 = True
    var_12 = "webapp_Table34:_webapp_Input__webapp_Input89:_webapp_Validator__webapp_Validator"
    var_13 = python_code_.webapp_PrimaryKey()
    var_14 = python_code_.webapp_Column(
        name=var_2,
        isNotNull=var_11,
        size=set(),
        useZeroFill=var_11,
        type=var_2,
        defaultValue=var_12,
        webapp_Column38=var_2,
        webapp_Column49=var_13,
    )
    var_15 = {var_14, var_14, var_14, var_14, var_14}
    var_16 = python_code_.webapp_Constraint()
    python_code_.webapp_Table(
        name=var_7,
        charset=var_7,
        webapp_Table34=var_15,
        webapp_Table36=var_16,
        webapp_Table59=var_10,
    )
    var_20 = python_code_.webapp_Constraint()
    python_code_.webapp_Check(expr="!", webapp_Check=var_20)
    python_code_.webapp_WebConfig(displayName=var_7)
    var_24 = "rZ]"
    python_code_.webapp_Validator(
        name=var_24, package=var_2, webapp_Validator67=complex(2924.0, -763.98681)
    )
    python_code_.webapp_Mapping(left=var_7, right=var_7, webapp_Mapping90=(-991.49,))


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = -3078
    python_code_.webapp_Detail(precision=complex(381.7, -2584.4), scale=var_0)
    var_2 = python_code_.webapp_Column
    python_code_.webapp_WebConfig(displayName=-2310, webapp_WebConfig=var_2)
    var_4 = python_code_.webapp_Resource()
    var_6 = python_code_.webapp_TableHTML()
    var_7 = "webapp_Properties_webapp_Table__webapp_Table6webapp_BusinessObject118"
    var_8 = python_code_.webapp_Properties(
        name=var_6, package=var_4, webapp_Properties71=True
    )
    var_9 = python_code_.webapp_Mapping(
        left=b"\xfa\xb5\xa3\xceq\x190\xd9\xf3\t\xf8\xf6\xe6]{+",
        right=var_7,
        webapp_Mapping=var_8,
    )
    var_11 = True
    var_12 = "webapp_Table34:_webapp_Input__webapp_Input89:_webapp_Validator__webapp_Validator"
    var_13 = python_code_.webapp_PrimaryKey()
    python_code_.webapp_Column(
        name=var_2,
        isNotNull=var_11,
        size=set(),
        useZeroFill=var_11,
        type=var_2,
        defaultValue=var_12,
        webapp_Column38=var_2,
        webapp_Column49=var_13,
    )
    var_20 = python_code_.webapp_Constraint()
    python_code_.webapp_Check(expr="!", webapp_Check=var_20)
    python_code_.webapp_Input(type=-1294.06, webapp_Input86=var_9, webapp_Input94=var_2)


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = python_code_.webapp_File()
    python_code_.webapp_Navigation(message=var_0, webapp_Navigation120=[])
    var_3 = python_code_.webapp_File
    var_6 = " u@j"
    var_7 = python_code_.webapp_TableHTML
    python_code_.webapp_BusinessObject(
        name=var_6,
        package=None,
        webapp_BusinessObject108=var_7,
        webapp_BusinessObject112=var_3,
        webapp_BusinessObject110=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_21():
    var_2 = "webapp_Unique _webapp_Properties__webapp_Pr5perties71 _webapp_WebApp__webapp_WebApp2"
    var_3 = object
    var_4 = "b"
    var_5 = python_code_.webapp_Action(
        name=var_4, returnType=var_3, webapp_Action=var_3
    )
    python_code_.webapp_BusinessObject(
        name=var_2,
        package=var_3,
        webapp_BusinessObject80=var_5,
        webapp_BusinessObject=var_3,
    )


def test_22():
    var_3 = "P\t(0$Y5W"
    python_code_.webapp_Check(expr=var_3)
    var_5 = "2y9Qs?xw"
    var_6 = set()
    python_code_.webapp_Table(name=var_3, charset=var_5, webapp_Table34=var_6)
    var_8 = "17"
    python_code_.webapp_Attribute(name=var_8, value=var_8)


def test_23():
    var_0 = python_code_.Tag()
    var_3 = python_code_.webapp_Image
    var_17 = "r|1(H,DE.["
    var_21 = python_code_.webapp_Table(
        name=var_3,
        charset=complex(144.49369, -91.0),
        webapp_Table36=var_3,
        webapp_Table59=complex(-6991.379, -1076.321787),
    )
    python_code_.webapp_OnUpdate(behavior=var_17, webapp_OnUpdate=var_0)
    python_code_.webapp_Validator(
        name=b"\n\xfcs\xbf\x81\xe6\xb8B'", package=var_17, webapp_Validator95=var_21
    )


def test_24():
    python_code_.webapp_Navigation(message=(True, True))


def test_25():
    var_0 = python_code_.webapp_File()
    python_code_.webapp_Navigation(message=var_0, webapp_Navigation120=[])


def test_26():
    var_0 = "W \tqyQ{s\x0b5B9b"
    var_1 = len
    python_code_.webapp_Page(
        name=var_0, isMain=var_1, webapp_Page73=var_1, webapp_Page124=var_1
    )
    var_10 = python_code_.webapp_Form(method=var_0, webapp_Form={var_0, var_0})
    assert isinstance(var_10, python_code_.webapp_Form)


def test_27():
    var_13 = False
    var_14 = python_code_.webapp_Instruction()
    var_15 = {var_14}
    python_code_.webapp_Page(name=False, isMain=var_13, webapp_Page76=var_15)


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = "W \tqyQ{s\x0b5B9b"
    var_1 = len
    var_2 = python_code_.webapp_Page(
        name=var_0, isMain=var_1, webapp_Page73=var_1, webapp_Page124=var_1
    )
    python_code_.webapp_Validator(
        name=set(), package=b"\xa9\xea\xd5H\x8e\x89", webapp_Validator67=var_2
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = "`e[N4/ 6RT4-"
    var_1 = "$N'B'l\\t/twnYAb"
    var_2 = False
    var_3 = python_code_.webapp_View()
    var_4 = python_code_.webapp_Page(
        name=True, isMain=var_2, webapp_Page=var_3, webapp_Page68=var_3
    )
    python_code_.webapp_Validator(
        name=var_0, package=var_1, webapp_Validator67=var_4, webapp_Validator=var_4
    )


def test_30():
    var_0 = "T\r%al9b}=pEr`n{"
    python_code_.webapp_Mapping(left=var_0, right=var_0, webapp_Mapping90=(-991.49,))


def test_31():
    var_3 = "P\t(0$Y5W"
    var_5 = python_code_.webapp_Image
    var_8 = "r|1(H,DE.["
    var_9 = "=Z'3E`GeXSE"
    var_10 = python_code_.webapp_Input(
        type="-", webapp_Input86=var_8, webapp_Input92=None
    )
    assert isinstance(var_10, python_code_.webapp_Input)
    python_code_.webapp_Mapping(left=var_9, right="", webapp_Mapping=var_3)
    python_code_.webapp_Table(
        name=var_5,
        charset=complex(144.49369, -91.0),
        webapp_Table36=var_5,
        webapp_Table59=complex(-6991.379, -1076.321787),
    )


def test_32():
    var_0 = "EUCJMPS:VARBINARY"
    var_1 = python_code_.webapp_Check(expr=var_0)
    var_2 = python_code_.webapp_Unique()
    python_code_.webapp_Navigation(message=var_2, webapp_Navigation123=var_2)
    var_6 = sorted
    python_code_.webapp_Navigation(
        message=var_0, webapp_Navigation=var_6, webapp_Navigation123=var_1
    )
    var_8 = "4Sz{"
    python_code_.webapp_Properties(name=var_8, package=var_6)


def test_33():
    var_42 = "webapp_View16"
    var_43 = python_code_.webapp_Resource()
    python_code_.webapp_Properties(
        name=var_42,
        package=var_42,
        webapp_Properties32=var_42,
        webapp_Properties=var_43,
    )


def test_34():
    var_0 = -3078
    python_code_.webapp_Detail(precision=complex(381.7, -2584.4), scale=var_0)
    var_2 = python_code_.webapp_Resource
    python_code_.webapp_WebConfig(displayName=-2310, webapp_WebConfig=var_2)
    var_4 = python_code_.webapp_Resource()
    var_6 = python_code_.webapp_TableHTML()
    var_7 = "webapp_Properties_webapp_Table__webapp_Table6webapp_BusinessObject118"
    var_8 = python_code_.webapp_Properties(
        name=var_6, package=var_4, webapp_Properties71=True
    )
    python_code_.webapp_Mapping(
        left="F} M<", right=var_7, webapp_Mapping=var_8, webapp_Mapping87=var_2
    )
    python_code_.webapp_WebConfig(displayName=var_7)


def test_35():
    var_20 = "l%"
    python_code_.webapp_Action(name=var_20, returnType=None, webapp_Action109=-2126)


@pytest.mark.xfail(strict=True)
def test_36():
    var_1 = "ANok%\n"
    var_2 = python_code_.webapp_Text(content=var_1)
    assert isinstance(var_2, python_code_.webapp_Text)
    python_code_.webapp_WebConfig(displayName=var_1)
    python_code_.webapp_OnUpdate(behavior=var_1)
    var_8 = "KEYBCS2"
    var_9 = python_code_.webapp_Form(method=var_8)
    assert isinstance(var_9, python_code_.webapp_Form)
    var_10 = python_code_.webapp_Tag(
        _property=var_1,
        webapp_Tag82=b"\xe7/\xd2\x7f\x9bs\x82\x01`\x14",
        webapp_Tag=var_9,
    )
    assert isinstance(var_10, python_code_.webapp_Tag)
    var_11 = lambda *args, **kwargs: []
    var_12 = python_code_.webapp_BusinessObject(name=var_1, package=var_11)
    python_code_.webapp_Action(
        name=var_1, returnType=var_1, webapp_Action84=651, webapp_Action79=var_12
    )


def test_37():
    var_5 = "_webapp_Tag_webapp_Tag103 UCS2"
    python_code_.webapp_Action(name=var_5, returnType=var_5)
    var_20 = "l%"
    python_code_.webapp_Action(name=var_20, returnType=None, webapp_Action109=-2126)


def test_38():
    var_0 = "L\tF7`&R}&Tfc\t"
    var_10 = python_code_.webapp_Th()
    python_code_.webapp_Validator(
        name=var_0, package=var_10, webapp_Validator={"_webapp_WebApp__webapp_WebApp10"}
    )
    python_code_.webapp_Check(expr=[], webapp_Check={})
    var_24 = "TU+R}"
    python_code_.webapp_Mapping(
        left=b"2z|_\xf3\x00",
        right=var_24,
        webapp_Mapping74={
            '@=4t5]\x0bA}U{`#``>"': True,
            "lw]fs": "T+re7-HFsb\ngJ9NupG",
            "_webapp_Navigation__webapp_Navigation120": "0aJb 'qkzlS",
        },
    )


def test_39():
    var_1 = "x2v6\x0bZ^d\x0c\x0b6YN|Q"
    var_2 = "u?\n\x0c?$ i2z5Dwupf"
    python_code_.webapp_Model(
        databaseName=var_1, url=var_1, userName=complex(-73.0, 2202.676), password=var_2
    )
    python_code_.webapp_Attribute(name=var_1, value=1013)
    python_code_.webapp_Check(expr=var_2)
    python_code_.webapp_WebConfig(displayName=var_2)


@pytest.mark.xfail(strict=True)
def test_40():
    var_18 = "_webapp_Tag_webapp_Tag103 UCS2"
    var_19 = "r|1(H,DE["
    var_21 = python_code_.webapp_Input(
        type="-", webapp_Input86=var_19, webapp_Input92=None
    )
    assert isinstance(var_21, python_code_.webapp_Input)
    python_code_.webapp_Mapping(left=var_18, right=var_18, webapp_Mapping90=(-991.49,))
    var_24 = python_code_.webapp_Controller()
    var_25 = python_code_.webapp_AppConfig()
    var_26 = python_code_.webapp_WebConfig(
        displayName=b"o<8\x17wN\xc3\x85", webapp_WebConfig=927
    )
    python_code_.webapp_WebApp(
        name=var_19,
        framework=None,
        webapp_WebApp10=var_24,
        webapp_WebApp=var_25,
        webapp_WebApp2=var_26,
        webapp_WebApp6=b"\xbb\x82\xc7.\xb4(\xd3\xc3\xe2E\xd5\x9fn\x8b==",
    )


@pytest.mark.xfail(strict=True)
def test_41():
    python_code_.webapp_Check(expr="webapp_Navigation", webapp_Check=None)
    var_11 = "P0J"
    var_12 = python_code_.webapp_Tr
    var_13 = "yFH;X6o4j"
    var_14 = python_code_.InputType
    var_15 = python_code_.webapp_WebApp(
        name=var_13, framework=var_11, webapp_WebApp12=var_14, webapp_WebApp2=()
    )
    python_code_.webapp_Model(
        databaseName=var_12,
        url=var_13,
        userName={},
        password=[],
        webapp_Model18=False,
        webapp_Model=var_15,
    )


def test_42():
    var_3 = "`?Dd4?;p@-ou;(@$Dl/Z"
    var_4 = "TINYTEXT"
    python_code_.webapp_WebApp(name=False, framework=var_4, webapp_WebApp12=var_3)


def test_43():
    python_code_.Charset.KOI8R


@pytest.mark.xfail(strict=True)
def test_44():
    var_3 = "P\t(0$Y5W"
    var_5 = python_code_.webapp_Image
    var_6 = False
    var_7 = "E%fi-}@8"
    var_12 = python_code_.webapp_Table(
        name=var_5,
        charset=complex(144.49369, -91.0),
        webapp_Table36=var_5,
        webapp_Table59=complex(-6991.379, -1076.321787),
    )
    python_code_.webapp_Mapping(left=var_5, right=var_5, webapp_Mapping87=var_7)
    var_15 = python_code_.webapp_Navigation(message=var_5, webapp_Navigation120=var_3)
    python_code_.webapp_Page(
        name=var_12,
        isMain=var_6,
        webapp_Page68=var_5,
        webapp_Page76=var_5,
        webapp_Page121=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = -3731
    python_code_.webapp_Detail(precision=complex(381.7, -2584.4), scale=var_0)
    var_2 = python_code_.webapp_Column
    python_code_.webapp_WebConfig(displayName=-2310, webapp_WebConfig=var_2)
    var_4 = python_code_.webapp_Resource()
    var_6 = python_code_.webapp_TableHTML()
    var_7 = "webapp_Properties_webapp_Table__webapp_Table36webapp_BusinessObject118"
    var_8 = python_code_.webapp_Properties(
        name=var_6, package=var_4, webapp_Properties71=True
    )
    python_code_.webapp_Mapping(
        left=b"\xfa\xb5\xa3\xceq\x190\xd9\xf3\t\xf8\xf6\xe6]{+",
        right=var_7,
        webapp_Mapping=var_8,
    )
    var_10 = python_code_.webapp_Image()
    var_11 = True
    var_12 = "webapp_Table34:_webapp_Input__webapp_Inut89:_webapp_Validator__webapp_Validator"
    var_13 = python_code_.webapp_PrimaryKey()
    var_14 = python_code_.webapp_Column(
        name=var_2,
        isNotNull=var_11,
        size=set(),
        useZeroFill=var_11,
        type=var_2,
        defaultValue=var_12,
        webapp_Column38=var_2,
        webapp_Column49=var_13,
    )
    var_15 = {var_14, var_14, var_14, var_14, var_14}
    var_16 = python_code_.webapp_Constraint()
    python_code_.webapp_Table(
        name=var_7,
        charset=var_7,
        webapp_Table34=var_15,
        webapp_Table36=var_16,
        webapp_Table59=var_10,
    )
    var_20 = python_code_.webapp_Constraint()
    python_code_.webapp_Check(expr="!", webapp_Check=var_20)
    python_code_.webapp_WebConfig(displayName=var_7)
    var_24 = "rZ]"
    var_25 = python_code_.webapp_Validator(
        name=var_24, package=var_2, webapp_Validator67=complex(2924.0, -763.98681)
    )
    python_code_.webapp_Input(type="ufC", webapp_Input=None, webapp_Input94=var_25)


def test_46():
    var_3 = python_code_.webapp_Attribute
    var_16 = python_code_.webapp_Constraint()
    python_code_.webapp_Table(
        name=b"\x86\xc5\x8c\xee",
        charset=var_3,
        webapp_Table=var_3,
        webapp_Table36=var_16,
    )
    var_18 = 3596
    python_code_.webapp_Detail(precision=var_18, scale=True)


def test_47():
    var_0 = python_code_.ColumnType.CHAR
    var_1 = lambda *args, **kwargs: [668.0, 1238, -34.04]
    var_3 = "`?Dd4?;p@-u;(@$Dl/Z"
    var_4 = "TINYTEXT"
    python_code_.webapp_WebApp(name=False, framework=var_4, webapp_WebApp12=var_3)
    var_7 = python_code_.webapp_Attribute(name=var_0, value=var_1)
    var_8 = {var_7, var_7}
    var_9 = python_code_.webapp_Td()
    var_10 = python_code_.webapp_Tag(
        _property=var_3, webapp_Tag82=var_8, webapp_Tag103=var_9
    )
    assert isinstance(var_10, python_code_.webapp_Tag)
    var_11 = python_code_.webapp_View()
    python_code_.webapp_Navigation(
        message=complex(2740.5218687, 1053.0),
        webapp_Navigation=var_11,
        webapp_Navigation120=var_1,
    )
    var_16 = python_code_.webapp_Resource
    var_17 = False
    var_18 = 0
    python_code_.webapp_Column(
        name=var_16,
        isNotNull=var_17,
        size=var_18,
        useZeroFill=var_17,
        type=var_4,
        defaultValue=var_1,
        webapp_Column62=complex(-2766.2080056, -1089.1),
    )
    python_code_.webapp_WebConfig(displayName=var_4)
    python_code_.webapp_Mapping(left=var_4, right=var_4, webapp_Mapping90=(-991.49,))


@pytest.mark.xfail(strict=True)
def test_48():
    var_1 = python_code_.ColumnType.BIGINT
    var_2 = python_code_.Charset.MACROMAN
    var_3 = "0Lt!;7,z$\x0c]K>9\x0cSnIp"
    var_4 = "_webapp_Page__webapp_Page73"
    var_5 = "n?|$X*eY'F'\r&\t\"]}"
    var_6 = python_code_.webapp_Table(
        name=var_4, charset=var_1, webapp_Table36=var_4, webapp_Table59=var_2
    )
    var_7 = {var_6, var_6}
    python_code_.webapp_Model(
        databaseName=var_3,
        url=b"G\xaa\x9fb\xdcl:\x8d-",
        userName=var_4,
        password=var_5,
        webapp_Model18=var_7,
    )
    var_9 = python_code_.webapp_Td
    var_10 = python_code_.webapp_Resource()
    var_11 = python_code_.webapp_Properties(
        name=var_5, package=var_2, webapp_Properties71=var_9, webapp_Properties=var_10
    )
    var_12 = "}n2Lnd"
    var_13 = python_code_.webapp_Properties(
        name=var_12, package=var_3, webapp_Properties=var_11
    )
    var_14 = {var_11, var_11, var_11, var_11, var_13}
    var_15 = python_code_.webapp_Page(name=None, isMain=var_9, webapp_Page70=var_14)
    python_code_.webapp_Mapping(left=var_5, right=var_9, webapp_Mapping74=var_15)


def test_49():
    var_9 = python_code_.webapp_Text(content=None)
    assert isinstance(var_9, python_code_.webapp_Text)


@pytest.mark.xfail(strict=True)
def test_50():
    var_42 = "webapp_View16"
    var_43 = python_code_.webapp_Resource()
    python_code_.webapp_Properties(
        name=var_42,
        package=var_42,
        webapp_Properties32=var_42,
        webapp_Properties=var_43,
    )
    var_45 = "SMALLINT"
    var_46 = (
        lambda *args, **kwargs: "_webapp_Table__webapp_Table59.webapp_Properties71.KEYBCS2.webapp_WebConfig"
    )
    python_code_.webapp_BusinessObject(
        name=var_46,
        package=var_45,
        webapp_BusinessObject118="k3Mx0\\1/",
        webapp_BusinessObject108=var_45,
        webapp_BusinessObject110=-230.92,
    )


def test_51():
    var_17 = "\x0b[TP"
    var_18 = python_code_.webapp_Form(method=var_17)
    assert isinstance(var_18, python_code_.webapp_Form)


def test_52():
    var_20 = python_code_.webapp_Instruction()
    var_32 = "iN"
    python_code_.webapp_OnUpdate(behavior=var_32)
    var_35 = python_code_.webapp_ForeignKey()
    var_44 = python_code_.Behavior.RESTRICT
    var_48 = python_code_.webapp_Input(
        type=var_20, webapp_Input="*p\n@*$Uh,oh'^,v}w\"J"
    )
    assert isinstance(var_48, python_code_.webapp_Input)
    var_50 = python_code_.webapp_Text(content=var_32)
    assert isinstance(var_50, python_code_.webapp_Text)
    python_code_.webapp_Mapping(left=var_44, right=var_35, webapp_Mapping=var_32)
    var_55 = "-;hX>_>~@8<+oH2+j"
    python_code_.webapp_OnUpdate(behavior=var_55, webapp_OnUpdate=var_35)


def test_53():
    var_0 = "T\r%al9b}=pE``n{"
    var_2 = "webapp_View16"
    var_3 = python_code_.webapp_Resource()
    python_code_.webapp_Properties(
        name=var_0, package=var_0, webapp_Properties32=var_0, webapp_Properties=var_3
    )
    var_6 = (
        lambda *args, **kwargs: "_webapp_Table__webapp_Table59.webapp_Properties71.KEYBCS2.webapp_WebConfig"
    )
    var_20 = python_code_.webapp_Action(name=var_2, returnType=var_2)
    python_code_.webapp_Detail(precision=var_6, scale=var_20, webapp_Detail=-294.44)
    var_23 = "l%"
    python_code_.webapp_Action(name=var_23, returnType=None, webapp_Action109=-2126)


@pytest.mark.xfail(strict=True)
def test_54():
    var_1 = python_code_.Behavior.RESTRICT
    var_3 = python_code_.webapp_Resource()
    var_4 = python_code_.webapp_Instruction()
    var_5 = "c^"
    var_6 = python_code_.webapp_BusinessObject
    python_code_.webapp_Attribute(name=var_5, value=var_6)
    python_code_.webapp_Validator(
        name=var_6,
        package=var_6,
        webapp_Validator95="_webapp_Column__webapp_Column",
        webapp_Validator=var_1,
    )
    var_11 = python_code_.webapp_Tag(_property=var_6)
    assert isinstance(var_11, python_code_.webapp_Tag)
    python_code_.webapp_Detail(
        precision="N`P5%WN\x0c)$-R%hSj^", scale=var_11, webapp_Detail=True
    )
    python_code_.webapp_Table(name=var_6, charset=(662.32, True, ".j(w^Y"))
    var_14 = python_code_.webapp_Library()
    var_15 = {var_14, var_14, var_14, var_14, var_14}
    var_16 = python_code_.webapp_WebApp(
        name=var_5, framework=var_4, webapp_WebApp4=var_15
    )
    var_17 = "iN"
    python_code_.webapp_OnUpdate(behavior=var_17)
    var_22 = python_code_.webapp_Constraint()
    python_code_.webapp_Check(expr=var_5, webapp_Check=var_22)
    python_code_.webapp_Navigation(message=var_6, webapp_Navigation123=set())
    var_27 = True
    python_code_.webapp_Column(
        name=var_17,
        isNotNull=var_27,
        size=var_16,
        useZeroFill=var_3,
        type=var_17,
        defaultValue=var_6,
        webapp_Column=var_6,
        webapp_Column38={True, True},
    )
    python_code_.webapp_Table(
        name=var_5, charset=var_1, webapp_Table=set(), webapp_Table34=var_15
    )
    var_33 = python_code_.webapp_Input(type=var_4, webapp_Input="*p\n@*$Uh,oh'^,v}w\"J")
    assert isinstance(var_33, python_code_.webapp_Input)
    var_35 = python_code_.webapp_Text(content=var_17)
    assert isinstance(var_35, python_code_.webapp_Text)
    var_37 = "webapp_BusinessObject80"
    python_code_.webapp_Mapping(left=var_37, right=var_6, webapp_Mapping87=var_33)


@pytest.mark.xfail(strict=True)
def test_55():
    var_0 = python_code_.webapp_Td()
    var_2 = python_code_.webapp_View
    var_3 = False
    var_4 = True
    var_5 = "r:\n1Bq}Hp;dW^[\nMJ;["
    var_6 = python_code_.webapp_ForeignKey()
    python_code_.webapp_Column(
        name=var_2,
        isNotNull=var_3,
        size=var_3,
        useZeroFill=var_4,
        type=var_2,
        defaultValue=var_5,
        webapp_Column62=var_6,
    )
    var_8 = lambda *args, **kwargs: False
    var_9 = python_code_.webapp_WebApp(
        name=b"\xa4y\xe8\x00\xdb\xa8\x0c\x93\x04\x86\xd13\x1f~(\x8f;",
        framework=var_8,
        webapp_WebApp6=var_0,
    )
    var_12 = "W"
    python_code_.webapp_Model(
        databaseName=var_8,
        url="jcLH{E33xY&",
        userName="_webapp_Page__webapp_Page70webapp_Unique64VARCHAR",
        password=var_12,
        webapp_Model=var_9,
    )


@pytest.mark.xfail(strict=True)
def test_56():
    var_1 = "POST"
    var_2 = "\n/JtDzxz(.0mh"
    var_3 = python_code_.webapp_Properties(name=var_2, package=var_1)
    var_4 = python_code_.webapp_Page
    var_5 = True
    var_6 = python_code_.webapp_View()
    var_7 = {var_3, var_3, var_3}
    var_8 = python_code_.webapp_Navigation(message=var_1, webapp_Navigation=var_6)
    python_code_.webapp_Page(
        name=var_4,
        isMain=var_5,
        webapp_Page=var_6,
        webapp_Page68="dbN'TD",
        webapp_Page70=var_7,
        webapp_Page121=var_8,
    )


def test_57():
    var_5 = python_code_.webapp_Image
    python_code_.webapp_OnDelete(behavior=var_5, webapp_OnDelete={-2062, True})


@pytest.mark.xfail(strict=True)
def test_58():
    var_0 = "`e[N4/ 6RT4-"
    var_1 = "$N'B'l\\t/twnYAb"
    var_7 = "webapp_Field117,_webapp_Action__webapp_Action,webapp_Td,POST"
    var_8 = lambda *args, **kwargs: True
    var_9 = python_code_.webapp_BusinessObject(
        name=complex(-125.9, 1859.928), package=var_8, webapp_BusinessObject80=var_0
    )
    python_code_.webapp_Model(
        databaseName=True,
        url=var_7,
        userName=var_0,
        password="9I\x0c=Z_",
        webapp_Model18=var_1,
        webapp_Model115=var_9,
    )


@pytest.mark.xfail(strict=True)
def test_59():
    var_0 = python_code_.FormMethod.GET
    var_1 = "x2v6\x0bZ^d\x0c\x0b6YN|Q"
    var_2 = "u?\n\x0c?$ i2z5Dwupf"
    python_code_.webapp_Model(
        databaseName="lI-\tdVQi :TdQ",
        url=">l`=X\x0csob~m",
        userName=var_2,
        password=" 2\nmM+",
        webapp_Model115=var_1,
    )
    var_5 = python_code_.webapp_Attribute(name=var_1, value=1013)
    var_6 = {var_5, var_5, var_5, var_5}
    var_7 = python_code_.webapp_Td()
    var_8 = python_code_.webapp_Tag(
        _property=complex(1158.0, 1331.5357183),
        webapp_Tag82=var_6,
        webapp_Tag=var_1,
        webapp_Tag103=var_7,
    )
    assert isinstance(var_8, python_code_.webapp_Tag)
    python_code_.webapp_WebApp(
        name=(-1166.54, True, False), framework=var_2, webapp_WebApp6=None
    )
    var_10 = python_code_.webapp_Controller()
    var_11 = python_code_.webapp_WebApp(
        name=var_5, framework=var_2, webapp_WebApp10=var_10, webapp_WebApp12=var_1
    )
    python_code_.webapp_Action(name=None, returnType=var_11)
    python_code_.webapp_Validator(name=var_2, package=var_2)
    var_18 = python_code_.webapp_Form
    var_19 = python_code_.webapp_Action(
        name=var_18, returnType=var_18, webapp_Action109=var_0
    )
    var_20 = "9"
    var_21 = python_code_.webapp_Field(name=var_2, type=var_20, defaultValue=var_2)
    python_code_.webapp_Input(
        type=var_18, webapp_Input=var_19, webapp_Input86=var_11, webapp_Input92=var_21
    )


@pytest.mark.xfail(strict=True)
def test_60():
    var_51 = "webapp_Field117,_webapp_Action__webapp_Action,webapp_Td,POST"
    var_52 = lambda *args, **kwargs: True
    var_62 = python_code_.Instruction()
    var_63 = "\nV5o8@'"
    var_64 = python_code_.webapp_Input(
        type=var_63, webapp_Input=None, webapp_Input86=var_62
    )
    assert isinstance(var_64, python_code_.webapp_Input)
    python_code_.webapp_Field(
        name=var_52, type=var_52, defaultValue=var_51, webapp_Field=var_64
    )
