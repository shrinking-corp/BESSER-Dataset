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
    AbstractActor,
    Block,
    Connection,
    Declaration,
    Expression,
    ExpressionCall,
    LambdaExpression,
    LiteralExpression,
    Node,
    PortAccess,
    Scope,
    Statement,
    Type,
    Variable,
    date,
    datetime,
    ir_AbstractActor,
    ir_Action,
    ir_Actor,
    ir_ActorInstance,
    ir_Annotation,
    ir_AnnotationArgument,
    ir_Assign,
    ir_BinaryExpression,
    ir_Block,
    ir_BooleanLiteral,
    ir_Connection,
    ir_Declaration,
    ir_Expression,
    ir_ExpressionCall,
    ir_ExternalActor,
    ir_FloatLiteral,
    ir_ForEach,
    ir_ForwardDeclaration,
    ir_FromSource,
    ir_FunctionCall,
    ir_Generator,
    ir_Guard,
    ir_IfExpression,
    ir_IfStatement,
    ir_IntegerLiteral,
    ir_LambdaExpression,
    ir_ListExpression,
    ir_LiteralExpression,
    ir_Member,
    ir_Namespace,
    ir_Network,
    ir_Node,
    ir_Point2PointConnection,
    ir_Port,
    ir_PortAccess,
    ir_PortInstance,
    ir_PortPeek,
    ir_PortRead,
    ir_PortWrite,
    ir_ProcCall,
    ir_ProcExpression,
    ir_ReturnValue,
    ir_Schedule,
    ir_Scope,
    ir_State,
    ir_Statement,
    ir_StringLiteral,
    ir_TaggedExpression,
    ir_ToSink,
    ir_Type,
    ir_TypeActor,
    ir_TypeBool,
    ir_TypeConstructor,
    ir_TypeConstructorCall,
    ir_TypeDeclaration,
    ir_TypeDeclarationImport,
    ir_TypeExternal,
    ir_TypeFloat,
    ir_TypeInt,
    ir_TypeLambda,
    ir_TypeList,
    ir_TypeProc,
    ir_TypeRecord,
    ir_TypeString,
    ir_TypeUint,
    ir_TypeUndef,
    ir_TypeUser,
    ir_UnaryExpression,
    ir_Variable,
    ir_VariableExpression,
    ir_VariableExternal,
    ir_VariableImport,
    ir_VariableReference,
    ir_WhileLoop,
    time,
)


def test_0():
    var_0 = "ir_Action._ir_PortInstance__ir_PortInstance98.ir_Actor18"
    python_code_.ir_AnnotationArgument(id=var_0, value=var_0)


@pytest.mark.xfail(strict=True)
def test_1():
    var_3 = python_code_.Statement()
    var_15 = "_ir_Declaration__ir_Declaration93"
    var_16 = "o8uS&@d"
    var_17 = python_code_.ir_Actor()
    var_18 = python_code_.ir_Generator
    var_19 = python_code_.ir_State(
        name=var_3, PriorityGraph=var_15, Action2TargetMap=var_18
    )
    var_20 = {var_19, var_19, var_19}
    var_21 = python_code_.ir_Schedule(
        PriorityGraph=var_15, ir_Schedule=var_17, ir_Schedule248=var_20
    )
    assert isinstance(var_21, python_code_.ir_Schedule)
    python_code_.ir_State(
        name=var_15, PriorityGraph=var_16, Action2TargetMap=var_15, ir_State254=var_21
    )


def test_2():
    var_0 = python_code_.ir_Connection()
    var_1 = lambda *args, **kwargs: "FE"
    var_2 = "mJNs0];(?\x0c6i"
    var_3 = python_code_.ir_ActorInstance()
    var_4 = python_code_.ir_Connection()
    var_5 = python_code_.ir_TaggedExpression(
        tag=var_2,
        ir_TaggedExpression=var_3,
        ir_TaggedExpression55=var_1,
        ir_TaggedExpression96=var_4,
        ir_TaggedExpression176=var_4,
    )
    var_6 = {var_5, var_5, var_5}
    var_7 = python_code_.ir_TypeExternal(
        name=var_1, scopeName=var_1, ir_TypeExternal=var_6
    )
    assert isinstance(var_7, python_code_.ir_TypeExternal)
    python_code_.ir_TaggedExpression(
        tag=True, ir_TaggedExpression55=var_0, ir_TaggedExpression213=var_7
    )
    var_9 = python_code_.ir_PortInstance(
        name=var_2,
        ir_PortInstance40=[],
        ir_PortInstance44=b"\xfa*\x9d\x16\xb2\xb9J\xde\x16\x9e\x1bk",
        ir_PortInstance108=var_7,
    )
    assert isinstance(var_9, python_code_.ir_PortInstance)


def test_3():
    var_8 = python_code_.ir_PortPeek(position=2)
    assert isinstance(var_8, python_code_.ir_PortPeek)


def test_4():
    var_2 = -292
    var_3 = python_code_.ir_VariableReference()
    var_4 = python_code_.ir_PortPeek(
        position=var_2, ir_PortPeek211=var_2, ir_PortPeek=var_3
    )
    assert isinstance(var_4, python_code_.ir_PortPeek)


def test_5():
    var_0 = python_code_.ir_TypeList()
    var_1 = python_code_.ir_TypeDeclarationImport(namespace=var_0)
    assert isinstance(var_1, python_code_.ir_TypeDeclarationImport)
    var_21 = python_code_.LiteralExpression()
    var_23 = python_code_.ir_Expression()
    var_24 = {var_23, var_23, var_23}
    var_25 = python_code_.ir_TypeConstructorCall(
        name=None, ir_TypeConstructorCall=var_24
    )
    assert isinstance(var_25, python_code_.ir_TypeConstructorCall)
    var_26 = False
    var_27 = python_code_.ir_BooleanLiteral(value=var_26)
    assert isinstance(var_27, python_code_.ir_BooleanLiteral)
    var_31 = python_code_.ir_Variable(
        constant=var_26, parameter=True, ir_Variable=None, ir_Variable186=var_21
    )
    assert isinstance(var_31, python_code_.ir_Variable)


def test_6():
    var_25 = "ir_Annotation"
    var_27 = python_code_.ir_TypeConstructorCall(name=var_25)
    assert isinstance(var_27, python_code_.ir_TypeConstructorCall)


def test_7():
    var_3 = "ir_VariableReference170:_ir_Variable__ir_Variable197:_ir_TypeActor__ir_TypeActor:_ir_PortIHnstance__ir_PortInstance47"
    var_4 = "_ir_Port__ir_Port34"
    var_5 = python_code_.ir_TypeActor(namespace=var_3, name=var_4)
    assert isinstance(var_5, python_code_.ir_TypeActor)
    var_6 = python_code_.ir_VariableImport(namespace=var_4)
    assert isinstance(var_6, python_code_.ir_VariableImport)
    python_code_.ir_Annotation(name=var_4)
    var_13 = python_code_.ir_Namespace(name=var_4)
    assert isinstance(var_13, python_code_.ir_Namespace)
    var_14 = python_code_.ir_TypeConstructorCall(
        name=var_4, ir_TypeConstructorCall92=var_6
    )
    assert isinstance(var_14, python_code_.ir_TypeConstructorCall)
    var_16 = python_code_.ir_Port(name=var_4, ir_Port=None)
    assert isinstance(var_16, python_code_.ir_Port)
    var_51 = python_code_.ir_AbstractActor()
    var_52 = {var_51, var_51}
    python_code_.ir_Namespace(name=True, ir_Namespace=var_52)


def test_8():
    var_0 = "ir_Action._ir_PortInstance__ir_PortInstance98.ir_Actor18"
    var_1 = python_code_.ir_UnaryExpression(operator=var_0)
    assert isinstance(var_1, python_code_.ir_UnaryExpression)
    python_code_.ir_AnnotationArgument(id=var_0, value=var_0)


def test_9():
    var_1 = python_code_.ir_PortRead()
    var_4 = "R*Fph93\x0cG"
    var_8 = python_code_.ir_VariableExpression()
    var_9 = python_code_.ir_PortPeek(position=var_1, ir_PortPeek=var_1)
    assert isinstance(var_9, python_code_.ir_PortPeek)
    var_10 = python_code_.PortAccess()
    var_13 = "YEl<"
    python_code_.ir_AnnotationArgument(id=var_13, value=var_4)
    var_17 = python_code_.ir_UnaryExpression(operator=var_10, ir_UnaryExpression=var_8)
    assert isinstance(var_17, python_code_.ir_UnaryExpression)
    var_46 = python_code_.ir_ForwardDeclaration()
    var_47 = python_code_.ir_Declaration(name=-2469, ir_Declaration178=var_46)
    assert isinstance(var_47, python_code_.ir_Declaration)


def test_10():
    var_20 = "ir_Guard210-_ir_Declaration__ir_Declaration"
    var_21 = python_code_.ir_Expression()
    var_22 = python_code_.ir_TypeList
    var_23 = python_code_.ir_BinaryExpression(
        operator=var_20, ir_BinaryExpression=var_21, ir_BinaryExpression80=var_22
    )
    assert isinstance(var_23, python_code_.ir_BinaryExpression)


def test_11():
    var_21 = "m8(s5nQ"
    var_22 = "ir_Guard210-_ir_Declaration__ir_Declaration"
    var_23 = python_code_.ir_Expression()
    var_24 = python_code_.ir_TypeList
    var_25 = python_code_.ir_BinaryExpression(
        operator=var_22, ir_BinaryExpression=var_23, ir_BinaryExpression80=var_24
    )
    assert isinstance(var_25, python_code_.ir_BinaryExpression)
    python_code_.ir_BinaryExpression(operator=var_21)


def test_12():
    var_23 = python_code_.ir_ProcExpression()
    var_29 = "wOI'p,ql4"
    var_30 = python_code_.ir_Schedule(PriorityGraph=var_29, ir_Schedule=False)
    assert isinstance(var_30, python_code_.ir_Schedule)
    var_31 = python_code_.ir_IntegerLiteral
    var_33 = python_code_.ir_Variable(
        constant=False,
        parameter=True,
        ir_Variable183=None,
        ir_Variable197=var_23,
        ir_Variable240=None,
    )
    assert isinstance(var_33, python_code_.ir_Variable)
    python_code_.ir_State(
        name="M(a>}< 1tLS", PriorityGraph=None, Action2TargetMap=var_31
    )
    var_44 = python_code_.ir_ForwardDeclaration()
    var_45 = python_code_.ir_Declaration(name=-2469, ir_Declaration178=var_44)
    assert isinstance(var_45, python_code_.ir_Declaration)


def test_13():
    var_23 = python_code_.ir_ProcExpression()
    var_30 = python_code_.ir_Schedule(PriorityGraph="_ir_Annotation__ir_Annotation")
    assert isinstance(var_30, python_code_.ir_Schedule)
    var_31 = python_code_.ir_IntegerLiteral
    var_33 = python_code_.ir_Variable(
        constant=False,
        parameter=True,
        ir_Variable183=None,
        ir_Variable197=var_23,
        ir_Variable240=None,
    )
    assert isinstance(var_33, python_code_.ir_Variable)
    python_code_.ir_State(
        name="M(a>}< 1tLS", PriorityGraph=None, Action2TargetMap=var_31
    )
    var_44 = python_code_.ir_ForwardDeclaration()
    var_45 = python_code_.ir_Declaration(name=-2469, ir_Declaration178=var_44)
    assert isinstance(var_45, python_code_.ir_Declaration)


def test_14():
    var_46 = python_code_.ir_Type
    var_47 = python_code_.ir_Action(tag=("z%",), ir_Action251=var_46)
    assert isinstance(var_47, python_code_.ir_Action)


@pytest.mark.xfail(strict=True)
def test_15():
    var_2 = python_code_.ir_StringLiteral(value=5421)
    assert isinstance(var_2, python_code_.ir_StringLiteral)
    var_3 = python_code_.ir_TypeFloat
    var_4 = python_code_.ir_Type()
    var_5 = python_code_.ir_ToSink()
    var_6 = python_code_.ir_Port(name=var_3, ir_Port34=var_4, ir_Port111=var_5)
    assert isinstance(var_6, python_code_.ir_Port)
    var_8 = True
    var_9 = python_code_.ir_LambdaExpression()
    var_10 = python_code_.ir_TypeRecord()
    var_11 = python_code_.ir_Variable(
        constant=var_8, parameter=var_3, ir_Variable189=var_9, ir_Variable224=var_10
    )
    assert isinstance(var_11, python_code_.ir_Variable)
    var_12 = python_code_.ir_TypeConstructorCall(name=var_10)
    assert isinstance(var_12, python_code_.ir_TypeConstructorCall)
    var_14 = python_code_.ir_TypeDeclarationImport(namespace=var_3)
    assert isinstance(var_14, python_code_.ir_TypeDeclarationImport)
    python_code_.ir_Action(tag=complex(-4159.37573, -467.15), ir_Action32=var_3)


def test_16():
    var_23 = python_code_.ir_AbstractActor()
    var_24 = {var_23, var_23}
    var_25 = python_code_.ir_Namespace(name=True, ir_Namespace=var_24)
    assert isinstance(var_25, python_code_.ir_Namespace)


def test_17():
    var_0 = python_code_.ir_TypeList()
    var_3 = "ir_VariableReference1;70:_ir_Variable__ir_Variable197:_ir_TypeActor__ir_TypeActor:_ir_PortInstance__ir_PortInstance47"
    var_4 = False
    var_5 = python_code_.ir_TypeActor(namespace=var_3, name=var_4)
    assert isinstance(var_5, python_code_.ir_TypeActor)
    var_6 = python_code_.ir_VariableImport(namespace=var_4)
    assert isinstance(var_6, python_code_.ir_VariableImport)
    var_8 = python_code_.ir_PortPeek(position=var_4, ir_PortPeek211=var_0)
    assert isinstance(var_8, python_code_.ir_PortPeek)
    var_54 = python_code_.ir_Namespace(name="{W&dhdaj")
    assert isinstance(var_54, python_code_.ir_Namespace)


def test_18():
    var_0 = python_code_.ir_TypeList()
    var_1 = python_code_.ir_TypeDeclarationImport(namespace=var_0)
    assert isinstance(var_1, python_code_.ir_TypeDeclarationImport)
    var_2 = False
    var_3 = python_code_.ir_BooleanLiteral(value=var_2)
    assert isinstance(var_3, python_code_.ir_BooleanLiteral)
    var_4 = "H573/,;$"
    var_5 = python_code_.ir_Connection()
    python_code_.ir_TaggedExpression(tag=var_4, ir_TaggedExpression96=var_5)
    python_code_.ir_TaggedExpression(tag=var_4)
    var_10 = 3571
    var_11 = python_code_.ir_PortPeek(position=var_10)
    assert isinstance(var_11, python_code_.ir_PortPeek)
    var_12 = python_code_.ir_PortPeek(position=var_2, ir_PortPeek=())
    assert isinstance(var_12, python_code_.ir_PortPeek)
    var_14 = python_code_.ir_AbstractActor()
    var_15 = {var_14, var_14}
    var_16 = python_code_.ir_Namespace(name=True, ir_Namespace=var_15)
    assert isinstance(var_16, python_code_.ir_Namespace)


def test_19():
    var_31 = "ir_Annotation"
    var_32 = sorted
    var_33 = python_code_.ir_TypeActor(
        namespace=var_31, name=var_31, ir_TypeActor=var_32
    )
    assert isinstance(var_33, python_code_.ir_TypeActor)
    var_45 = python_code_.ir_TypeConstructorCall(name=var_31)
    assert isinstance(var_45, python_code_.ir_TypeConstructorCall)
    var_49 = python_code_.ir_Member(
        name="ir_AbstractActor12:ir_TypeConstructor:ir_Schedule250", ir_Member119=var_33
    )
    assert isinstance(var_49, python_code_.ir_Member)
    var_52 = "ir_ProcExpression196"
    var_53 = python_code_.ir_IntegerLiteral(value=var_52)
    assert isinstance(var_53, python_code_.ir_IntegerLiteral)
    var_54 = python_code_.ir_UnaryExpression(operator=var_31)
    assert isinstance(var_54, python_code_.ir_UnaryExpression)
    var_55 = "G;$*1T8.8|\x0cI"
    var_56 = "*#U[{"
    var_57 = python_code_.ir_Annotation(name=var_56, ir_Annotation=var_54)
    var_58 = python_code_.ir_AnnotationArgument(
        id=var_55, value=var_32, ir_AnnotationArgument=var_57
    )
    assert isinstance(var_58, python_code_.ir_AnnotationArgument)


def test_20():
    var_2 = python_code_.ir_StringLiteral(value=5421)
    assert isinstance(var_2, python_code_.ir_StringLiteral)
    var_4 = python_code_.ir_Type()
    var_6 = python_code_.ir_Port(name=";&\r_O", ir_Port106=var_4, ir_Port159=None)
    assert isinstance(var_6, python_code_.ir_Port)
    var_35 = ")"
    var_36 = "iFFU"
    var_37 = set()
    var_38 = python_code_.ir_Annotation(name=var_36, ir_Annotation256=var_37)
    var_39 = python_code_.ir_AnnotationArgument(
        id=var_36, value=var_35, ir_AnnotationArgument=var_38
    )
    assert isinstance(var_39, python_code_.ir_AnnotationArgument)


def test_21():
    var_0 = "ir_Action._ir_PortInstance__ir_PortInstance98.ir_Actor18"
    var_1 = python_code_.ir_UnaryExpression(operator=var_0)
    assert isinstance(var_1, python_code_.ir_UnaryExpression)
    python_code_.ir_Node(id=var_0)


def test_22():
    var_3 = "ir_VariableReference170:_ir_Variable__ir_Variable197:_ir_TypeActor__ir_TypeActor:_ir_PortInstance__ir_PortInstance47"
    var_7 = python_code_.ir_StringLiteral(value=var_3)
    assert isinstance(var_7, python_code_.ir_StringLiteral)
    var_8 = python_code_.ir_PortPeek(position=2)
    assert isinstance(var_8, python_code_.ir_PortPeek)
    var_18 = "_ireMember__ir_Member"
    var_19 = python_code_.ir_Scope()
    var_20 = python_code_.ir_TypeUser()
    var_21 = python_code_.ir_Declaration(
        name=var_18,
        ir_Declaration=var_7,
        ir_Declaration137=[3527.09],
        ir_Declaration172=var_19,
        ir_Declaration226=var_20,
    )
    assert isinstance(var_21, python_code_.ir_Declaration)
    var_44 = python_code_.ir_Namespace(name="ir_PortWrite")
    assert isinstance(var_44, python_code_.ir_Namespace)


@pytest.mark.xfail(strict=True)
def test_23():
    var_1 = python_code_.ir_PortRead()
    var_2 = "_ir_Port__ir_Port159,ir_State254,_ir_Port__ir_Port13"
    var_4 = "R*Fph93\x0cG"
    var_5 = python_code_.ir_TypeActor(namespace=var_2, name=var_4)
    assert isinstance(var_5, python_code_.ir_TypeActor)
    var_8 = python_code_.ir_VariableExpression()
    var_9 = python_code_.ir_PortPeek(position=var_1, ir_PortPeek=var_1)
    assert isinstance(var_9, python_code_.ir_PortPeek)
    var_10 = python_code_.PortAccess()
    var_12 = python_code_.ir_TypeUndef()
    var_13 = "YEl<"
    var_14 = python_code_.ir_AnnotationArgument(id=var_13, value=var_4)
    var_17 = python_code_.ir_UnaryExpression(operator=var_10, ir_UnaryExpression=var_8)
    assert isinstance(var_17, python_code_.ir_UnaryExpression)
    var_28 = "o7c[U9=$90,e,%i"
    var_29 = python_code_.ir_TypeDeclarationImport(namespace=var_28)
    assert isinstance(var_29, python_code_.ir_TypeDeclarationImport)
    var_31 = "_ir_TypeConstructorCall__ir_TypeConstructorCall92"
    python_code_.ir_Member(name=var_14, ir_Member72=var_12, ir_Member75=var_31)


def test_24():
    var_2 = "ir_Annotation"
    var_3 = sorted
    var_4 = python_code_.ir_TypeActor(namespace=var_2, name=var_2, ir_TypeActor=var_3)
    assert isinstance(var_4, python_code_.ir_TypeActor)
    var_6 = python_code_.ir_TypeConstructorCall(name=var_2)
    assert isinstance(var_6, python_code_.ir_TypeConstructorCall)
    python_code_.ir_Node(id=var_2)
    var_12 = python_code_.ir_Member(
        name={}, ir_Member119=var_3, ir_Member=b"\x1c\xa0\xea"
    )
    assert isinstance(var_12, python_code_.ir_Member)


def test_25():
    var_2 = "ir_Annotation"
    var_3 = sorted
    var_4 = python_code_.ir_TypeActor(namespace=var_2, name=var_2, ir_TypeActor=var_3)
    assert isinstance(var_4, python_code_.ir_TypeActor)
    var_6 = python_code_.ir_TypeConstructorCall(name=var_2)
    assert isinstance(var_6, python_code_.ir_TypeConstructorCall)
    var_10 = python_code_.ir_Statement()
    python_code_.ir_Node(id=var_2)
    var_12 = python_code_.ir_Member(
        name="(ZKZGG,1lu", ir_Member119=None, ir_Member75=var_10, ir_Member=None
    )
    assert isinstance(var_12, python_code_.ir_Member)


def test_26():
    var_1 = python_code_.ir_FromSource()
    var_3 = "ir_VariableReference170:_ir_Variable__ir_Variable197:_ir_TypeActor__ir_TypeActor:_ir_PortInstance__ir_PortInstance47"
    var_7 = python_code_.ir_StringLiteral(value=var_3)
    assert isinstance(var_7, python_code_.ir_StringLiteral)
    var_18 = "_ir_Member__ir_Member"
    var_19 = python_code_.ir_Scope()
    var_20 = python_code_.ir_TypeUser()
    var_21 = python_code_.ir_Declaration(
        name=var_18,
        ir_Declaration=var_7,
        ir_Declaration137=[3527.09],
        ir_Declaration172=var_19,
        ir_Declaration226=var_20,
    )
    assert isinstance(var_21, python_code_.ir_Declaration)
    var_23 = "E}<V4Ef+ lxU"
    var_24 = python_code_.ir_Point2PointConnection()
    var_25 = python_code_.ir_PortInstance(
        name=var_23,
        ir_PortInstance=var_1,
        ir_PortInstance98=var_23,
        ir_PortInstance101=var_24,
    )
    assert isinstance(var_25, python_code_.ir_PortInstance)


def test_27():
    var_7 = lambda *args, **kwargs: "p\t5XyGQGD5!4"
    var_8 = python_code_.ir_PortPeek(position=1506, ir_PortPeek211=var_7)
    assert isinstance(var_8, python_code_.ir_PortPeek)
    var_51 = python_code_.ir_Point2PointConnection()
    var_55 = "_ir_Action__irz_Action28"
    var_56 = set()
    var_57 = python_code_.ir_PortInstance(
        name=var_55,
        ir_PortInstance40=var_55,
        ir_PortInstance44=var_56,
        ir_PortInstance98=var_51,
    )
    assert isinstance(var_57, python_code_.ir_PortInstance)


def test_28():
    var_2 = python_code_.ir_StringLiteral(value=5421)
    assert isinstance(var_2, python_code_.ir_StringLiteral)
    var_3 = python_code_.ir_TypeFloat
    var_4 = python_code_.ir_Type()
    var_5 = python_code_.ir_ToSink()
    var_6 = python_code_.ir_Port(name=var_3, ir_Port34=var_4, ir_Port111=var_5)
    assert isinstance(var_6, python_code_.ir_Port)
    var_8 = True
    var_9 = python_code_.ir_LambdaExpression()
    var_10 = python_code_.ir_TypeRecord()
    var_11 = python_code_.ir_Variable(
        constant=var_8, parameter=var_3, ir_Variable189=var_9, ir_Variable224=var_10
    )
    assert isinstance(var_11, python_code_.ir_Variable)
    var_12 = python_code_.ir_TypeConstructorCall(name=var_10)
    assert isinstance(var_12, python_code_.ir_TypeConstructorCall)


def test_29():
    var_2 = python_code_.ir_StringLiteral(value=5421)
    assert isinstance(var_2, python_code_.ir_StringLiteral)
    var_3 = python_code_.ir_TypeFloat
    var_4 = python_code_.ir_Type()
    var_5 = python_code_.ir_ToSink()
    var_6 = python_code_.ir_Port(name=var_3, ir_Port34=var_4, ir_Port111=var_5)
    assert isinstance(var_6, python_code_.ir_Port)


def test_30():
    var_8 = python_code_.ir_VariableExpression()
    var_57 = python_code_.ir_IfExpression()
    var_58 = python_code_.ir_Type()
    var_59 = python_code_.ir_Port(name=var_57, ir_Port=var_8, ir_Port34=var_58)
    assert isinstance(var_59, python_code_.ir_Port)


def test_31():
    var_0 = "ir_Action._ir_PortInstance__ir_PortInstance98.ir_Actor18"
    var_1 = python_code_.ir_UnaryExpression(operator=var_0)
    assert isinstance(var_1, python_code_.ir_UnaryExpression)
    python_code_.ir_AnnotationArgument(id=var_0, value=var_0)
    var_10 = python_code_.ir_FromSource()
    var_11 = python_code_.LiteralExpression
    var_12 = python_code_.ir_PortAccess()
    var_13 = python_code_.ir_Port(
        name=var_0, ir_Port106=var_10, ir_Port34=var_11, ir_Port159=var_12
    )
    assert isinstance(var_13, python_code_.ir_Port)


def test_32():
    var_3 = "ir_VariableReference170:_ir_Variable__ir_Variable197:_ir_TypeActor__ir_TypeActor:_ir_PortInstance__ir_PortInstance47"
    var_4 = "_ir_Port__ir_Port34"
    var_5 = python_code_.ir_TypeActor(namespace=var_3, name=var_4)
    assert isinstance(var_5, python_code_.ir_TypeActor)
    var_6 = python_code_.ir_VariableImport(namespace=var_4)
    assert isinstance(var_6, python_code_.ir_VariableImport)
    var_7 = lambda *args, **kwargs: "p\t5XyGQGD5!4"
    var_8 = python_code_.ir_PortPeek(position=1506, ir_PortPeek211=var_7)
    assert isinstance(var_8, python_code_.ir_PortPeek)
    python_code_.ir_Annotation(name=var_4)
    var_13 = python_code_.ir_Namespace(name=var_4)
    assert isinstance(var_13, python_code_.ir_Namespace)
    var_14 = python_code_.ir_TypeConstructorCall(
        name=var_4, ir_TypeConstructorCall92=var_6
    )
    assert isinstance(var_14, python_code_.ir_TypeConstructorCall)
    var_16 = python_code_.ir_Port(
        name=var_5,
        ir_Port=var_13,
        ir_Port13={
            "SPK^^#g": False,
            "Qe0mvVWI-r-c!9x+6": "BDuZB1 %_g;v>",
            "\n'\\i6#l/p2a;\t\x0c": True,
        },
        ir_Port106=var_14,
    )
    assert isinstance(var_16, python_code_.ir_Port)
    var_40 = python_code_.ir_Expression()
    var_41 = {var_40, var_40, var_40}
    python_code_.ir_TypeConstructorCall(name=None, ir_TypeConstructorCall=var_41)
    var_43 = False
    var_44 = python_code_.ir_BooleanLiteral(value=var_43)
    assert isinstance(var_44, python_code_.ir_BooleanLiteral)
    var_47 = "m8(s5nQ"
    var_48 = python_code_.ir_BinaryExpression(
        operator=var_47, ir_BinaryExpression=var_40
    )
    assert isinstance(var_48, python_code_.ir_BinaryExpression)


def test_33():
    var_24 = ";{]_LLy''o,"
    var_9 = python_code_.ir_TypeActor(namespace=var_24, name=(), ir_TypeActor=var_24)
    assert isinstance(var_9, python_code_.ir_TypeActor)


def test_34():
    var_1 = ">Meq"
    var_3 = sorted
    var_4 = python_code_.ir_TypeActor(
        namespace="ir_Actor21 ir_TypeUser _ir_Variable__ir_Variable197",
        name="PHBh>m_[zN.i?<r",
    )
    assert isinstance(var_4, python_code_.ir_TypeActor)
    var_21 = python_code_.ir_TypeConstructorCall(name=var_1)
    assert isinstance(var_21, python_code_.ir_TypeConstructorCall)
    python_code_.ir_Node(id=var_1)
    var_27 = python_code_.ir_Member(
        name={}, ir_Member119=var_3, ir_Member=b"\x1c\xa0\xea"
    )
    assert isinstance(var_27, python_code_.ir_Member)


def test_35():
    python_code_.LambdaExpression()


def test_36():
    var_2 = python_code_.ir_StringLiteral(value=5421)
    assert isinstance(var_2, python_code_.ir_StringLiteral)
    var_27 = 3571
    var_28 = python_code_.ir_PortPeek(position=var_27)
    assert isinstance(var_28, python_code_.ir_PortPeek)


def test_37():
    var_0 = ":Oe844Qr@q*|"
    var_1 = python_code_.ir_StringLiteral(value=var_0)
    assert isinstance(var_1, python_code_.ir_StringLiteral)
    var_2 = python_code_.ir_VariableImport(namespace=[])
    assert isinstance(var_2, python_code_.ir_VariableImport)
    var_7 = python_code_.PortAccess()
    python_code_.ir_AnnotationArgument(id=set(), value=var_0)
    var_12 = python_code_.ir_Namespace(name="Y w<'\\\r7\tnBGX7F\rf")
    assert isinstance(var_12, python_code_.ir_Namespace)
    var_14 = "'\"Nv\x0c!1R0ZG"
    var_18 = "%ZXiQBJl\x0b,"
    var_19 = python_code_.ir_State(
        name=var_18,
        PriorityGraph=var_14,
        Action2TargetMap=var_7,
        ir_State=b"\xae\x0c\xcc",
    )
    assert isinstance(var_19, python_code_.ir_State)
    var_38 = "o7c[U9=$90,e,%i"
    var_39 = python_code_.ir_TypeDeclarationImport(namespace=var_38)
    assert isinstance(var_39, python_code_.ir_TypeDeclarationImport)


def test_38():
    var_0 = python_code_.ir_TypeList()
    var_1 = python_code_.ir_TypeDeclarationImport(namespace=var_0)
    assert isinstance(var_1, python_code_.ir_TypeDeclarationImport)
    var_2 = False
    var_3 = python_code_.ir_BooleanLiteral(value=var_2)
    assert isinstance(var_3, python_code_.ir_BooleanLiteral)
    var_4 = "H573/,;$"
    var_5 = python_code_.ir_Connection()
    python_code_.ir_TaggedExpression(tag=var_4, ir_TaggedExpression96=var_5)
    python_code_.ir_TaggedExpression(
        tag=var_4, ir_TaggedExpression55=None, ir_TaggedExpression213=var_5
    )
    var_17 = python_code_.ir_Point2PointConnection()
    var_21 = "_ir_Action__ir_Action28"
    var_22 = set()
    var_23 = python_code_.ir_PortInstance(
        name=var_21,
        ir_PortInstance40=var_21,
        ir_PortInstance44=var_22,
        ir_PortInstance98=var_17,
    )
    assert isinstance(var_23, python_code_.ir_PortInstance)


def test_39():
    var_0 = python_code_.ir_TypeUndef()
    var_2 = python_code_.ir_Network
    var_3 = python_code_.ir_Variable(
        constant=var_0, parameter=None, ir_Variable224="w(", ir_Variable240=var_2
    )
    assert isinstance(var_3, python_code_.ir_Variable)
    var_8 = "T{\\NS(.Vve3S=4G"
    var_9 = python_code_.ir_TypeExternal(name=var_8, scopeName=var_8)
    assert isinstance(var_9, python_code_.ir_TypeExternal)
    var_13 = python_code_.ir_VariableImport(namespace=var_8)
    assert isinstance(var_13, python_code_.ir_VariableImport)
    var_35 = python_code_.ir_AbstractActor()
    var_36 = {var_35, var_35}
    var_37 = python_code_.ir_Namespace(name=True, ir_Namespace=var_36)
    assert isinstance(var_37, python_code_.ir_Namespace)


def test_40():
    var_1 = python_code_.ir_TypeDeclarationImport(namespace="%Htm;2w=\\6z")
    assert isinstance(var_1, python_code_.ir_TypeDeclarationImport)
    var_2 = True
    var_3 = python_code_.ir_BooleanLiteral(value=var_2)
    assert isinstance(var_3, python_code_.ir_BooleanLiteral)
    var_4 = "H573/k;$"
    var_5 = python_code_.ir_Connection()
    python_code_.ir_TaggedExpression(tag=var_4, ir_TaggedExpression96=var_5)
    python_code_.ir_TaggedExpression(tag=var_4)
    var_10 = 3571
    var_11 = python_code_.ir_PortPeek(position=var_10)
    assert isinstance(var_11, python_code_.ir_PortPeek)
    var_12 = python_code_.ir_PortPeek(position=var_2, ir_PortPeek=())
    assert isinstance(var_12, python_code_.ir_PortPeek)
    var_19 = python_code_.ir_FloatLiteral(value=())
    assert isinstance(var_19, python_code_.ir_FloatLiteral)


def test_41():
    var_0 = python_code_.ir_Expression()
    var_29 = "wOI'p,ql4"
    var_30 = python_code_.ir_Schedule(PriorityGraph=var_29, ir_Schedule=False)
    assert isinstance(var_30, python_code_.ir_Schedule)
    var_31 = python_code_.ir_IntegerLiteral
    var_33 = python_code_.ir_Variable(
        constant=True,
        parameter=True,
        ir_Variable=None,
        ir_Variable183=var_0,
        ir_Variable197=None,
    )
    assert isinstance(var_33, python_code_.ir_Variable)
    python_code_.ir_State(
        name="M(a>}< 1tLS", PriorityGraph=None, Action2TargetMap=var_31
    )
    var_44 = python_code_.ir_ForwardDeclaration()
    var_45 = python_code_.ir_Declaration(name=-2469, ir_Declaration178=var_44)
    assert isinstance(var_45, python_code_.ir_Declaration)


def test_42():
    var_0 = python_code_.ir_TypeUser()
    var_1 = python_code_.ir_Point2PointConnection()
    var_2 = python_code_.ir_IfExpression()
    var_3 = False
    var_4 = python_code_.ir_BinaryExpression
    var_5 = python_code_.ir_ProcExpression()
    var_6 = python_code_.ir_TypeConstructor()
    var_7 = python_code_.ir_Variable(
        constant=var_3,
        parameter=var_0,
        ir_Variable183=var_2,
        ir_Variable186=var_4,
        ir_Variable197=var_5,
        ir_Variable224=var_1,
        ir_Variable240=var_6,
    )
    assert isinstance(var_7, python_code_.ir_Variable)
    var_12 = python_code_.ir_UnaryExpression(operator=var_4)
    assert isinstance(var_12, python_code_.ir_UnaryExpression)
    python_code_.ir_Node(id=var_4)
    var_19 = " 8w#L3N)b&?1yr"
    var_20 = python_code_.ir_Schedule(
        PriorityGraph=var_19, ir_Schedule="\tTBHQO", ir_Schedule253=";-eZz+k[vjj*fg]6-X"
    )
    assert isinstance(var_20, python_code_.ir_Schedule)


def test_43():
    var_1 = ">Meq"
    var_2 = "ir_Annotation"
    var_3 = sorted
    var_4 = python_code_.ir_TypeActor(namespace=var_2, name=var_2, ir_TypeActor=var_3)
    assert isinstance(var_4, python_code_.ir_TypeActor)
    var_6 = python_code_.ir_TypeConstructorCall(name=var_2)
    assert isinstance(var_6, python_code_.ir_TypeConstructorCall)
    var_12 = python_code_.ir_Member(
        name={}, ir_Member119=var_3, ir_Member=b"\x1c\xa0\xea"
    )
    assert isinstance(var_12, python_code_.ir_Member)
    var_17 = "ir_ProcExpression196"
    var_18 = python_code_.ir_IntegerLiteral(value=var_17)
    assert isinstance(var_18, python_code_.ir_IntegerLiteral)
    var_19 = python_code_.ir_UnaryExpression(operator=var_1)
    assert isinstance(var_19, python_code_.ir_UnaryExpression)


@pytest.mark.xfail(strict=True)
def test_44():
    var_1 = "V~Ma8fU\nT WLNJ"
    var_2 = python_code_.ir_VariableExpression
    python_code_.ir_Schedule(PriorityGraph=var_1, ir_Schedule250=var_2)
