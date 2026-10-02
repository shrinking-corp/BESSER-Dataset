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
    AccessLevel,
    Assignee,
    Call,
    Enum,
    Expression,
    Member,
    NamedElement,
    SingleTypeRef,
    Statement,
    Symbol,
    TypeDeclaration,
    TypeRef,
    TypedDeclaration,
    Value,
    abstractmethod,
    date,
    datetime,
    miniJava_And,
    miniJava_ArrayAccess,
    miniJava_ArrayInstance,
    miniJava_ArrayLength,
    miniJava_ArrayRefValue,
    miniJava_ArrayTypeRef,
    miniJava_Assignee,
    miniJava_Assignment,
    miniJava_Block,
    miniJava_BoolConstant,
    miniJava_BooleanTypeRef,
    miniJava_BooleanValue,
    miniJava_Call,
    miniJava_ClassRef,
    miniJava_Clazz,
    miniJava_ClazzToMethodMap,
    miniJava_Context,
    miniJava_Division,
    miniJava_Equality,
    miniJava_Expression,
    miniJava_Field,
    miniJava_FieldAccess,
    miniJava_FieldBinding,
    miniJava_ForStatement,
    miniJava_Frame,
    miniJava_IfStatement,
    miniJava_Import,
    miniJava_Inequality,
    miniJava_Inferior,
    miniJava_InferiorOrEqual,
    miniJava_IntConstant,
    miniJava_IntegerTypeRef,
    miniJava_IntegerValue,
    miniJava_Interface,
    miniJava_Member,
    miniJava_Method,
    miniJava_MethodCall,
    miniJava_MethodCall2,
    miniJava_Minus,
    miniJava_Modulo,
    miniJava_Multiplication,
    miniJava_NamedElement,
    miniJava_Neg,
    miniJava_NewArray,
    miniJava_NewCall,
    miniJava_NewObject,
    miniJava_Not,
    miniJava_Null,
    miniJava_NullValue,
    miniJava_ObjectInstance,
    miniJava_ObjectRefValue,
    miniJava_Or,
    miniJava_OutputStream,
    miniJava_Parameter,
    miniJava_Plus,
    miniJava_PrintStatement,
    miniJava_Program,
    miniJava_Return,
    miniJava_SingleTypeRef,
    miniJava_State,
    miniJava_Statement,
    miniJava_StringConstant,
    miniJava_StringTypeRef,
    miniJava_StringValue,
    miniJava_Super,
    miniJava_Superior,
    miniJava_SuperiorOrEqual,
    miniJava_Symbol,
    miniJava_SymbolBinding,
    miniJava_SymbolRef,
    miniJava_SymbolToSymbolBindingMap,
    miniJava_This,
    miniJava_TypeDeclaration,
    miniJava_TypeRef,
    miniJava_TypedDeclaration,
    miniJava_Value,
    miniJava_VariableDeclaration,
    miniJava_VoidTypeRef,
    miniJava_WhileStatement,
    time,
)


def test_0():
    var_42 = python_code_.miniJava_ArrayInstance(
        size=-1531, miniJava_ArrayInstance209=set(), miniJava_ArrayInstance214=None
    )
    assert isinstance(var_42, python_code_.miniJava_ArrayInstance)


def test_1():
    var_42 = python_code_.miniJava_ArrayInstance(size=0)
    assert isinstance(var_42, python_code_.miniJava_ArrayInstance)


def test_2():
    var_27 = python_code_.miniJava_Multiplication()
    var_30 = python_code_.miniJava_ArrayInstance(
        size=-214, miniJava_ArrayInstance214=var_27, miniJava_ArrayInstance=var_27
    )
    assert isinstance(var_30, python_code_.miniJava_ArrayInstance)


def test_3():
    python_code_.miniJava_OutputStream(stream="miniJava_Clazz")


def test_4():
    var_62 = python_code_.miniJava_State()
    python_code_.miniJava_OutputStream(
        stream="^s\x0c:nc?[7", miniJava_OutputStream=var_62
    )


def test_5():
    var_18 = python_code_.miniJava_Method(
        isabstract=True, isstatic=False, miniJava_Method15=set()
    )
    assert isinstance(var_18, python_code_.miniJava_Method)


def test_6():
    var_18 = python_code_.miniJava_Method(
        isabstract=True, isstatic=True, miniJava_Method13=None, miniJava_Method=set()
    )
    assert isinstance(var_18, python_code_.miniJava_Method)


def test_7():
    var_18 = python_code_.miniJava_Method(
        isabstract=True, isstatic=False, miniJava_Method226=None
    )
    assert isinstance(var_18, python_code_.miniJava_Method)


def test_8():
    var_66 = sorted
    var_73 = python_code_.miniJava_Method(
        isabstract=var_66, isstatic=[421.32, True], miniJava_Method226=var_66
    )
    assert isinstance(var_73, python_code_.miniJava_Method)


def test_9():
    var_57 = python_code_.miniJava_FieldAccess
    var_58 = False
    var_59 = python_code_.miniJava_Method(
        isabstract=var_57,
        isstatic=var_58,
        miniJava_Method135=var_58,
        miniJava_Method226={"DR*\t}R_BiU\x0b#xgv}", 2798},
    )
    assert isinstance(var_59, python_code_.miniJava_Method)


def test_10():
    var_73 = python_code_.miniJava_ClazzToMethodMap()
    var_74 = python_code_.miniJava_Method(
        isabstract=False, isstatic=True, miniJava_Method13=var_73
    )
    assert isinstance(var_74, python_code_.miniJava_Method)


def test_11():
    var_67 = python_code_.miniJava_Clazz(
        isabstract=False, miniJava_Clazz=None, miniJava_Clazz9=None
    )
    assert isinstance(var_67, python_code_.miniJava_Clazz)


def test_12():
    var_66 = sorted
    var_67 = python_code_.miniJava_Clazz(isabstract=3, miniJava_Clazz140=var_66)
    assert isinstance(var_67, python_code_.miniJava_Clazz)


def test_13():
    var_66 = sorted
    var_67 = python_code_.miniJava_Clazz(
        isabstract=False, miniJava_Clazz9=var_66, miniJava_Clazz207=var_66
    )
    assert isinstance(var_67, python_code_.miniJava_Clazz)


def test_14():
    var_0 = python_code_.miniJava_Member(access="jOB(8*9n%", miniJava_Member=None)
    assert isinstance(var_0, python_code_.miniJava_Member)


def test_15():
    var_35 = python_code_.miniJava_TypeDeclaration(
        accessLevel="Lj$`zPJ\r8?_l_+)y\r",
        miniJava_TypeDeclaration6={False, "HToc8Yi{Jx\t_XSc|=", False},
    )
    assert isinstance(var_35, python_code_.miniJava_TypeDeclaration)


def test_16():
    var_35 = python_code_.miniJava_TypeDeclaration(
        accessLevel="g\\", miniJava_TypeDeclaration=None
    )
    assert isinstance(var_35, python_code_.miniJava_TypeDeclaration)


def test_17():
    var_27 = python_code_.miniJava_Multiplication()
    var_33 = python_code_.miniJava_Minus
    var_34 = set()
    var_35 = python_code_.miniJava_ClassRef()
    var_36 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_27,
        miniJava_TypeDeclaration=var_33,
        miniJava_TypeDeclaration6=var_34,
        miniJava_TypeDeclaration47=var_35,
    )
    assert isinstance(var_36, python_code_.miniJava_TypeDeclaration)
    var_37 = "miniJava_ClazzToMethodMap225"
    var_38 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_37,
        miniJava_TypeDeclaration=var_33,
        miniJava_TypeDeclaration47="_miniJava_TypeDeclaration__miniJava_TypeDeclaration8,_miniJava_Method__miniJava_Method135",
    )
    assert isinstance(var_38, python_code_.miniJava_TypeDeclaration)
    var_39 = python_code_.miniJava_TypeDeclaration(
        accessLevel={
            "_miniJava_Program__miniJava_Program4": True,
            "miniJava_Interface miniJava_TypeDeclaration": "b1t",
            "\nY}VU\rg!\x0c.14": 2355.91,
        }
    )
    var_40 = {var_36, var_38, var_39, var_38, var_39}
    var_41 = python_code_.miniJava_State()
    var_42 = python_code_.miniJava_Program(
        name=var_27, miniJava_Program2=var_40, miniJava_Program4=var_41
    )
    assert isinstance(var_42, python_code_.miniJava_Program)


def test_18():
    var_35 = python_code_.miniJava_TypeDeclaration(
        accessLevel="`F\\",
        miniJava_TypeDeclaration=None,
        miniJava_TypeDeclaration6=set(),
        miniJava_TypeDeclaration47=None,
    )
    assert isinstance(var_35, python_code_.miniJava_TypeDeclaration)
    var_37 = "c%"
    var_38 = {var_35, var_35}
    var_39 = python_code_.miniJava_Program(name=var_37, miniJava_Program2=var_38)
    assert isinstance(var_39, python_code_.miniJava_Program)


def test_19():
    python_code_.miniJava_Import(importedNamespace=True)


def test_20():
    var_76 = python_code_.miniJava_Import(
        importedNamespace=[
            "miniJava_TypeDeclaration,miniJava_ClassRef,miniJava_Block",
            "JZ4.M&IM",
        ],
        miniJava_Import="_miniJava_Method__miniJava_Method",
    )
    assert isinstance(var_76, python_code_.miniJava_Import)
    var_77 = {var_76}
    var_78 = python_code_.miniJava_Program(
        name=3813.83,
        miniJava_Program=var_77,
        miniJava_Program2=var_77,
        miniJava_Program4=[-558],
    )
    assert isinstance(var_78, python_code_.miniJava_Program)


def test_21():
    var_7 = sorted
    var_8 = python_code_.miniJava_Clazz(
        isabstract=True,
        miniJava_Clazz=None,
        miniJava_Clazz9=None,
        miniJava_Clazz207=None,
    )
    assert isinstance(var_8, python_code_.miniJava_Clazz)
    var_19 = python_code_.miniJava_Program(
        name="_miniJava_Program__miniJava_Program2,_miniJava_Method__miniJava_Method135",
        miniJava_Program="Jv3",
        miniJava_Program2={
            "miniJava_ClazzToMethodMap225:_miniJava_Program__miniJava_Program2:miniJava_Block": True
        },
        miniJava_Program4=var_7,
    )
    assert isinstance(var_19, python_code_.miniJava_Program)
    var_20 = python_code_.miniJava_IntegerValue(value=0)
    assert isinstance(var_20, python_code_.miniJava_IntegerValue)


def test_22():
    var_73 = python_code_.miniJava_Program(name="Wa_+ju}rC}|[H g")
    assert isinstance(var_73, python_code_.miniJava_Program)


@pytest.mark.xfail(strict=True)
def test_23():
    var_0 = lambda *args, **kwargs: []
    var_1 = python_code_.miniJava_State()
    python_code_.miniJava_OutputStream(stream=var_0, miniJava_OutputStream=var_1)
    var_9 = False
    var_10 = python_code_.miniJava_BooleanValue(value=var_9)
    assert isinstance(var_10, python_code_.miniJava_BooleanValue)
    var_11 = True
    var_12 = python_code_.miniJava_Clazz(
        isabstract=var_11, miniJava_Clazz=1202.27, miniJava_Clazz9={}
    )
    assert isinstance(var_12, python_code_.miniJava_Clazz)
    var_13 = python_code_.miniJava_ClazzToMethodMap()
    python_code_.miniJava_Clazz(
        isabstract=var_9, miniJava_Clazz9=var_12, miniJava_Clazz223=var_13
    )


def test_24():
    var_14 = python_code_.miniJava_TypeDeclaration(
        accessLevel=None,
        miniJava_TypeDeclaration6="miniJava_TypeDeclaration8.miniJava_ClassRef._miniJava_Clazz__miniJava_Clazz223._miniJava_ArrayInstance__miniJava_ArrayInstance209",
        miniJava_TypeDeclaration8={" iP&PvF": -505.01, "5T9DC\x0b3i1v6Q .": -359},
    )
    assert isinstance(var_14, python_code_.miniJava_TypeDeclaration)
    var_15 = python_code_.miniJava_State()
    var_18 = python_code_.miniJava_Clazz(isabstract=var_15)
    assert isinstance(var_18, python_code_.miniJava_Clazz)
    var_19 = "iB"
    var_20 = python_code_.miniJava_StringValue(value=var_19)
    assert isinstance(var_20, python_code_.miniJava_StringValue)
    var_25 = lambda *args, **kwargs: True
    var_26 = python_code_.miniJava_OutputStream(
        stream=var_25, miniJava_OutputStream="i|]rZ6FVfU|J\r]/DYz\x0b"
    )
    assert isinstance(var_26, python_code_.miniJava_OutputStream)


def test_25():
    var_49 = python_code_.miniJava_IntegerValue(value=None)
    assert isinstance(var_49, python_code_.miniJava_IntegerValue)


def test_26():
    var_50 = python_code_.miniJava_StringConstant(value=complex(2326.6, 920.68))
    assert isinstance(var_50, python_code_.miniJava_StringConstant)


def test_27():
    var_6 = python_code_.miniJava_NewCall
    var_7 = python_code_.miniJava_IntConstant(value=var_6)
    assert isinstance(var_7, python_code_.miniJava_IntConstant)
    var_9 = '(8.>)=/{8|@$\x0bE@">'
    var_10 = python_code_.miniJava_StringConstant(value=var_9)
    assert isinstance(var_10, python_code_.miniJava_StringConstant)


def test_28():
    var_0 = python_code_.miniJava_BoolConstant(value={})
    assert isinstance(var_0, python_code_.miniJava_BoolConstant)


def test_29():
    python_code_.miniJava_OutputStream(stream="_miniJava_Program__miniJava_Program4")
    var_4 = python_code_.miniJava_NewObject
    var_5 = "_miniJava_TypeDeclaration__miniJavar_TypeDeclaration6"
    var_6 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_5, miniJava_TypeDeclaration8=var_5
    )
    assert isinstance(var_6, python_code_.miniJava_TypeDeclaration)
    var_7 = python_code_.miniJava_Member(access=var_4, miniJava_Member=var_6)
    assert isinstance(var_7, python_code_.miniJava_Member)
    var_9 = "`\n_7d%x%D1KhnW\r\\"
    var_10 = {var_7}
    var_11 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_9,
        miniJava_TypeDeclaration6="9sN@OB&kc",
        miniJava_TypeDeclaration8=var_10,
    )
    assert isinstance(var_11, python_code_.miniJava_TypeDeclaration)
    python_code_.miniJava_NamedElement(name=b"8,\x02\xf4\xfa\x91")


def test_30():
    var_29 = -820
    var_30 = python_code_.miniJava_ArrayInstance(
        size=924, miniJava_ArrayInstance214=var_29
    )
    assert isinstance(var_30, python_code_.miniJava_ArrayInstance)


def test_31():
    var_47 = "\x0c3i["
    var_49 = python_code_.miniJava_Member(
        access="_miniJava_Import__miniJava_ImportminiJava_Program_miniJava_Program__miniJava_Program2"
    )
    assert isinstance(var_49, python_code_.miniJava_Member)
    var_50 = {var_49}
    var_51 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_47, miniJava_TypeDeclaration8=var_50
    )
    assert isinstance(var_51, python_code_.miniJava_TypeDeclaration)


def test_32():
    var_47 = "\x0c3i["
    var_48 = lambda *args, **kwargs: True
    var_49 = python_code_.miniJava_Member(access=var_47, miniJava_Member=var_48)
    assert isinstance(var_49, python_code_.miniJava_Member)
    var_50 = {var_49, var_49}
    var_51 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_47, miniJava_TypeDeclaration8=var_50
    )
    assert isinstance(var_51, python_code_.miniJava_TypeDeclaration)


@pytest.mark.xfail(strict=True)
def test_33():
    var_35 = python_code_.miniJava_TypeDeclaration(
        accessLevel="`F\\",
        miniJava_TypeDeclaration=None,
        miniJava_TypeDeclaration6=set(),
        miniJava_TypeDeclaration47=None,
    )
    assert isinstance(var_35, python_code_.miniJava_TypeDeclaration)
    var_36 = False
    var_37 = python_code_.miniJava_Clazz(isabstract=var_36)
    assert isinstance(var_37, python_code_.miniJava_Clazz)
    python_code_.miniJava_Clazz(isabstract=var_36, miniJava_Clazz=var_37)


def test_34():
    var_7 = sorted
    var_8 = python_code_.miniJava_Clazz(isabstract=True, miniJava_Clazz=var_7)
    assert isinstance(var_8, python_code_.miniJava_Clazz)


def test_35():
    var_66 = sorted
    var_67 = python_code_.miniJava_Clazz(
        isabstract=False, miniJava_Clazz=None, miniJava_Clazz223=var_66
    )
    assert isinstance(var_67, python_code_.miniJava_Clazz)


def test_36():
    var_66 = sorted
    var_67 = python_code_.miniJava_Clazz(
        isabstract=True, miniJava_Clazz9=var_66, miniJava_Clazz140=None
    )
    assert isinstance(var_67, python_code_.miniJava_Clazz)


def test_37():
    var_74 = ":"
    var_76 = python_code_.miniJava_SymbolRef()
    var_77 = python_code_.miniJava_ClassRef()
    var_78 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_74,
        miniJava_TypeDeclaration=var_76,
        miniJava_TypeDeclaration47=var_77,
    )
    assert isinstance(var_78, python_code_.miniJava_TypeDeclaration)


def test_38():
    var_18 = python_code_.miniJava_Method(
        isabstract=True, isstatic=False, miniJava_Method13=None, miniJava_Method226=None
    )
    assert isinstance(var_18, python_code_.miniJava_Method)
    var_20 = python_code_.miniJava_State()
    var_21 = python_code_.miniJava_Program(
        name=b"\xda\xc7\x8b\xe7\xcf\x8dt\xe6[\xaa\xb6\x8e]B", miniJava_Program4=var_20
    )
    assert isinstance(var_21, python_code_.miniJava_Program)


def test_39():
    var_35 = python_code_.miniJava_TypeDeclaration(
        accessLevel="v@.6L",
        miniJava_TypeDeclaration=None,
        miniJava_TypeDeclaration8=set(),
    )
    assert isinstance(var_35, python_code_.miniJava_TypeDeclaration)


@pytest.mark.xfail(strict=True)
def test_40():
    var_1 = python_code_.miniJava_IntConstant(value=-1115.33)
    assert isinstance(var_1, python_code_.miniJava_IntConstant)
    var_3 = python_code_.miniJava_Context()
    var_7 = python_code_.Assignee()
    python_code_.miniJava_OutputStream(stream=var_3)
    var_24 = True
    var_25 = False
    var_26 = python_code_.miniJava_Clazz(
        isabstract=var_25, miniJava_Clazz9="pk].", miniJava_Clazz207=var_1
    )
    assert isinstance(var_26, python_code_.miniJava_Clazz)
    python_code_.miniJava_Clazz(
        isabstract=var_24, miniJava_Clazz=var_26, miniJava_Clazz207=var_7
    )


def test_41():
    python_code_.miniJava_OutputStream(stream="miniJava_MethodCall")
    var_4 = python_code_.miniJava_NewObject
    var_5 = "_miniJava_TypeDeclaration__miniJava_TypeDeclaration6"
    var_6 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_5, miniJava_TypeDeclaration8=var_5
    )
    assert isinstance(var_6, python_code_.miniJava_TypeDeclaration)
    var_7 = python_code_.miniJava_Member(access=var_4, miniJava_Member=var_6)
    assert isinstance(var_7, python_code_.miniJava_Member)


def test_42():
    var_14 = python_code_.miniJava_Statement
    var_15 = "eo~?*{"
    var_16 = set()
    var_17 = python_code_.miniJava_TypeDeclaration(
        accessLevel=None,
        miniJava_TypeDeclaration=var_14,
        miniJava_TypeDeclaration6=var_16,
    )
    assert isinstance(var_17, python_code_.miniJava_TypeDeclaration)
    var_18 = {var_17, var_17, var_17, var_17, var_17}
    var_19 = python_code_.miniJava_Program(name=var_15, miniJava_Program=var_18)
    assert isinstance(var_19, python_code_.miniJava_Program)
    var_20 = python_code_.miniJava_Import(
        importedNamespace=var_14, miniJava_Import=var_19
    )
    assert isinstance(var_20, python_code_.miniJava_Import)
    var_22 = "miniJava_TypeDeclaration.miniJava_ClazzToMethodMap.miniJava_Value"
    var_23 = {var_20}
    python_code_.miniJava_Program(
        name=var_22, miniJava_Program=var_23, miniJava_Program4=var_14
    )


def test_43():
    python_code_.miniJava_OutputStream(stream="_miniJava_Program__miniJava_Program4")
    var_4 = python_code_.miniJava_NewObject
    var_5 = "_miniJava_TypeDeclaration__miniJavar_TypeDeclaration6"
    var_6 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_5, miniJava_TypeDeclaration8=var_5
    )
    assert isinstance(var_6, python_code_.miniJava_TypeDeclaration)
    var_7 = python_code_.miniJava_Member(access=var_4, miniJava_Member=var_6)
    assert isinstance(var_7, python_code_.miniJava_Member)
    var_14 = "`\n_7d%x%D1KhnW\r\\"
    var_15 = {var_7}
    var_16 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_14,
        miniJava_TypeDeclaration6="9sN@OB&kc",
        miniJava_TypeDeclaration8=var_15,
    )
    assert isinstance(var_16, python_code_.miniJava_TypeDeclaration)


def test_44():
    var_73 = python_code_.miniJava_Program(
        name="_miniJava_Program__miniJava_Program2", miniJava_Program4=None
    )
    assert isinstance(var_73, python_code_.miniJava_Program)
    var_74 = python_code_.miniJava_TypeDeclaration(
        accessLevel="miniJava_Program",
        miniJava_TypeDeclaration=None,
        miniJava_TypeDeclaration6=set(),
        miniJava_TypeDeclaration47=var_73,
    )
    assert isinstance(var_74, python_code_.miniJava_TypeDeclaration)


def test_45():
    python_code_.miniJava_OutputStream(stream="_miniJava_Program__miniJava_Program4")
    var_4 = python_code_.miniJava_NewObject
    var_6 = python_code_.miniJava_TypeDeclaration(
        accessLevel="aPa59",
        miniJava_TypeDeclaration=None,
        miniJava_TypeDeclaration47=None,
    )
    assert isinstance(var_6, python_code_.miniJava_TypeDeclaration)
    var_7 = python_code_.miniJava_Member(access=var_4, miniJava_Member=var_6)
    assert isinstance(var_7, python_code_.miniJava_Member)
    var_14 = "Ug)9zRnH\r[%mYEo]"
    var_15 = {var_7}
    var_16 = python_code_.miniJava_TypeDeclaration(
        accessLevel=var_14,
        miniJava_TypeDeclaration6="9sN@OB&kc",
        miniJava_TypeDeclaration8=var_15,
    )
    assert isinstance(var_16, python_code_.miniJava_TypeDeclaration)
