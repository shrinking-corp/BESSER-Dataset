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
    AbstractConnector,
    Action,
    AnnotatedElement,
    ElmtProperty,
    Event,
    Expression,
    Handler,
    Port,
    ReferencedElmt,
    Region,
    Source,
    State,
    Type,
    Variable,
    ViewSource,
    abstractmethod,
    date,
    datetime,
    thingML_AbstractConnector,
    thingML_Action,
    thingML_ActionBlock,
    thingML_AndExpression,
    thingML_AnnotatedElement,
    thingML_ArrayIndex,
    thingML_ArrayParamRef,
    thingML_BooleanLiteral,
    thingML_CompositeState,
    thingML_ConditionalAction,
    thingML_ConfigPropertyAssign,
    thingML_Configuration,
    thingML_Connector,
    thingML_Decrement,
    thingML_DivExpression,
    thingML_DoubleLiteral,
    thingML_ElmtProperty,
    thingML_EnumLiteralRef,
    thingML_Enumeration,
    thingML_EnumerationLiteral,
    thingML_EqualsExpression,
    thingML_ErrorAction,
    thingML_Event,
    thingML_Expression,
    thingML_ExternExpression,
    thingML_ExternStatement,
    thingML_ExternalConnector,
    thingML_Filter,
    thingML_FinalState,
    thingML_Function,
    thingML_FunctionCallExpression,
    thingML_FunctionCallStatement,
    thingML_GreaterExpression,
    thingML_GreaterOrEqualExpression,
    thingML_Handler,
    thingML_Import,
    thingML_Increment,
    thingML_Instance,
    thingML_InstanceRef,
    thingML_IntegerLiteral,
    thingML_InternalPort,
    thingML_InternalTransition,
    thingML_JoinSources,
    thingML_LengthArray,
    thingML_LengthWindow,
    thingML_LocalVariable,
    thingML_LoopAction,
    thingML_LowerExpression,
    thingML_LowerOrEqualExpression,
    thingML_MergeSources,
    thingML_Message,
    thingML_MessageParameter,
    thingML_MinusExpression,
    thingML_ModExpression,
    thingML_NotEqualsExpression,
    thingML_NotExpression,
    thingML_ObjectType,
    thingML_OrExpression,
    thingML_ParallelRegion,
    thingML_Parameter,
    thingML_PlatformAnnotation,
    thingML_PlusExpression,
    thingML_Port,
    thingML_PrimitiveType,
    thingML_PrintAction,
    thingML_Property,
    thingML_PropertyAssign,
    thingML_PropertyReference,
    thingML_Protocol,
    thingML_ProvidedPort,
    thingML_ReceiveMessage,
    thingML_Reference,
    thingML_ReferencedElmt,
    thingML_Region,
    thingML_RequiredPort,
    thingML_ReturnAction,
    thingML_SendAction,
    thingML_Session,
    thingML_SimpleParamRef,
    thingML_SimpleSource,
    thingML_Source,
    thingML_StartSession,
    thingML_State,
    thingML_Stream,
    thingML_StringLiteral,
    thingML_Thing,
    thingML_ThingMLModel,
    thingML_TimeWindow,
    thingML_TimesExpression,
    thingML_Transition,
    thingML_Type,
    thingML_TypeRef,
    thingML_UnaryMinus,
    thingML_Variable,
    thingML_VariableAssignment,
    thingML_ViewSource,
    time,
)


def test_0():
    var_0 = python_code_.thingML_ConfigPropertyAssign()
    var_2 = python_code_.thingML_MessageParameter(name=var_0)
    assert isinstance(var_2, python_code_.thingML_MessageParameter)
    var_4 = python_code_.thingML_ExternStatement
    var_6 = "l6oUj!*r]-H?D[D"
    var_10 = "thingML_ConigPropertyAssign256._thingML_CompositeState__thingML_CompositeState118.thingML_Session.thingML_State"
    python_code_.thingML_PlatformAnnotation(
        name=-138, value=var_10, thingML_PlatformAnnotation15=[]
    )
    var_20 = bool
    var_21 = python_code_.thingML_MessageParameter(
        name=var_4, thingML_MessageParameter=var_20
    )
    assert isinstance(var_21, python_code_.thingML_MessageParameter)
    var_23 = python_code_.thingML_ExternStatement(statement=var_6)
    assert isinstance(var_23, python_code_.thingML_ExternStatement)


def test_1():
    var_1 = python_code_.thingML_InternalPort()
    var_2 = python_code_.thingML_StartSession()
    var_3 = "Pb-\n~`tP(\x0c%+"
    var_5 = python_code_.thingML_Handler(name=var_3, thingML_Handler150=None)
    assert isinstance(var_5, python_code_.thingML_Handler)
    var_6 = python_code_.thingML_AbstractConnector(
        name=var_3, thingML_AbstractConnector=var_1
    )
    assert isinstance(var_6, python_code_.thingML_AbstractConnector)
    var_7 = python_code_.thingML_ReferencedElmt()
    python_code_.thingML_AbstractConnector(name=var_2)
    var_9 = -251.06
    var_10 = python_code_.thingML_DoubleLiteral(doubleValue=var_9)
    assert isinstance(var_10, python_code_.thingML_DoubleLiteral)
    var_12 = python_code_.thingML_TimesExpression()
    var_14 = python_code_.thingML_SimpleSource(name=var_2)
    assert isinstance(var_14, python_code_.thingML_SimpleSource)
    var_15 = "thingML_ConfigPropertyAssign256"
    var_16 = python_code_.thingML_StringLiteral(stringValue=var_15)
    assert isinstance(var_16, python_code_.thingML_StringLiteral)
    var_21 = python_code_.thingML_JoinSources(
        name=var_15,
        thingML_JoinSources75=var_12,
        thingML_JoinSources78={var_15, var_7, var_5},
    )
    assert isinstance(var_21, python_code_.thingML_JoinSources)
    var_22 = python_code_.thingML_PrimitiveType(ByteSize=None)
    assert isinstance(var_22, python_code_.thingML_PrimitiveType)


def test_2():
    var_5 = lambda *args, **kwargs: "lmsFmKN"
    var_6 = python_code_.thingML_ReceiveMessage(
        name=var_5, thingML_ReceiveMessage156={}
    )
    assert isinstance(var_6, python_code_.thingML_ReceiveMessage)
    var_7 = python_code_.thingML_Instance(name=var_5)
    assert isinstance(var_7, python_code_.thingML_Instance)


def test_3():
    var_3 = "A~0YqB_PPu!p~'7'9"
    var_4 = python_code_.thingML_MergeSources(name=var_3, thingML_MergeSources=())
    assert isinstance(var_4, python_code_.thingML_MergeSources)


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.ElmtProperty()
    var_1 = python_code_.thingML_InternalPort()
    var_2 = python_code_.thingML_StartSession()
    var_3 = "Pb-\n~`tP(\x0c%+"
    var_4 = python_code_.thingML_Action()
    var_5 = python_code_.thingML_Handler(name=var_3, thingML_Handler150=var_4)
    assert isinstance(var_5, python_code_.thingML_Handler)
    var_6 = python_code_.thingML_AbstractConnector(
        name=var_3, thingML_AbstractConnector=var_1
    )
    assert isinstance(var_6, python_code_.thingML_AbstractConnector)
    python_code_.thingML_AbstractConnector(name=var_2)
    var_9 = -251.06
    var_10 = python_code_.thingML_DoubleLiteral(doubleValue=var_9)
    assert isinstance(var_10, python_code_.thingML_DoubleLiteral)
    var_14 = python_code_.thingML_SimpleSource(name=var_2)
    assert isinstance(var_14, python_code_.thingML_SimpleSource)
    var_15 = "thingML_ConfigPropertyAssign256"
    var_16 = python_code_.thingML_StringLiteral(stringValue=var_15)
    assert isinstance(var_16, python_code_.thingML_StringLiteral)
    python_code_.thingML_JoinSources(
        name=b"V\xde\x18r\x91\xe3\xd4\x1aZj\xcf\x85d)4\xfd",
        thingML_JoinSources78=var_0,
        thingML_JoinSources81=2827.28,
    )


def test_5():
    python_code_.thingML_Import(importURI=b"\xb4`\xd3E")
    var_7 = "~0[~^\\A8"
    var_8 = python_code_.thingML_Enumeration()
    var_9 = python_code_.thingML_EnumerationLiteral(
        name=var_7, thingML_EnumerationLiteral=var_8
    )
    assert isinstance(var_9, python_code_.thingML_EnumerationLiteral)
    var_10 = lambda *args, **kwargs: "lmsFmKN"
    var_12 = python_code_.thingML_Instance(name=var_10)
    assert isinstance(var_12, python_code_.thingML_Instance)


@pytest.mark.xfail(strict=True)
def test_6():
    var_1 = "thingML_ViewSource93-thingML_ThingMLModel6"
    var_2 = python_code_.thingML_GreaterOrEqualExpression
    var_3 = python_code_.thingML_Function(
        name=var_1,
        thingML_Function44=var_1,
        thingML_Function47=var_1,
        thingML_Function214=var_2,
    )
    assert isinstance(var_3, python_code_.thingML_Function)
    var_7 = "_thingML_Stream__thingML_Stream69,thingML_Parameter56,thingML_ConfigPropertyAssign247"
    var_8 = False
    var_9 = python_code_.thingML_TypeRef(isArray=var_8, thingML_TypeRef59=var_2)
    python_code_.thingML_Type(name=var_7, thingML_Type9=var_9)


def test_7():
    python_code_.thingML_Import(importURI=b"\xb4`\xd3E")
    var_12 = python_code_.thingML_Thing(
        fragment=("5k.Mz@! U5['37X",), thingML_Thing=2, thingML_Thing21=()
    )
    assert isinstance(var_12, python_code_.thingML_Thing)


def test_8():
    var_1 = python_code_.thingML_InternalPort()
    var_2 = python_code_.thingML_StartSession()
    var_3 = "Pb-\n~`tP(\x0c%+"
    var_4 = python_code_.thingML_Action()
    var_5 = python_code_.thingML_Handler(name=var_3, thingML_Handler150=var_4)
    assert isinstance(var_5, python_code_.thingML_Handler)
    var_6 = python_code_.thingML_AbstractConnector(
        name=var_3, thingML_AbstractConnector=var_1
    )
    assert isinstance(var_6, python_code_.thingML_AbstractConnector)
    python_code_.thingML_AbstractConnector(name=var_2)
    var_9 = -251.06
    var_10 = python_code_.thingML_DoubleLiteral(doubleValue=var_9)
    assert isinstance(var_10, python_code_.thingML_DoubleLiteral)
    var_28 = python_code_.thingML_Thing(
        fragment=("5k.Mz@! U5['37X",), thingML_Thing=2, thingML_Thing21=()
    )
    assert isinstance(var_28, python_code_.thingML_Thing)


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.thingML_DoubleLiteral(doubleValue="thingML_InstanceRef276")
    assert isinstance(var_0, python_code_.thingML_DoubleLiteral)
    var_2 = True
    var_3 = python_code_.thingML_LocalVariable(changeable=var_2, name=var_2)
    assert isinstance(var_3, python_code_.thingML_LocalVariable)
    var_5 = "_thingML_Session__thingML_Session212"
    var_6 = set()
    var_7 = python_code_.thingML_Port(name=var_5, thingML_Port64=var_6)
    assert isinstance(var_7, python_code_.thingML_Port)
    python_code_.thingML_Session(
        maxInstances=var_2, thingML_Session122=var_2, thingML_Session125=var_7
    )


def test_10():
    var_0 = "_thingML_Instnce__thingML_Instance"
    var_1 = python_code_.thingML_Session(maxInstances=var_0)
    assert isinstance(var_1, python_code_.thingML_Session)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = "_thingML_Instance__thingML_Instance"
    var_1 = python_code_.thingML_Session(maxInstances=var_0)
    assert isinstance(var_1, python_code_.thingML_Session)
    var_4 = lambda *args, **kwargs: "8Amx,K|43wZ]"
    var_5 = python_code_.thingML_InternalTransition()
    var_6 = {var_5, var_5, var_5, var_5}
    python_code_.thingML_State(
        name=var_4,
        thingML_State120=var_1,
        thingML_State123=var_4,
        thingML_State134=var_4,
        thingML_State142=var_6,
    )


def test_12():
    python_code_.thingML_Import(importURI=b"\xb4`\xd3E")
    var_1 = python_code_.thingML_Expression()
    var_2 = python_code_.thingML_Configuration(name=var_1)
    assert isinstance(var_2, python_code_.thingML_Configuration)


def test_13():
    var_9 = python_code_.thingML_ReturnAction()
    var_11 = False
    var_12 = python_code_.thingML_LocalVariable(changeable=var_11, name=var_9)
    assert isinstance(var_12, python_code_.thingML_LocalVariable)


@pytest.mark.xfail(strict=True)
def test_14():
    python_code_.thingML_Stream(
        name=[True, True], thingML_Stream69=complex(-2523.02729, 1943.0316727)
    )


@pytest.mark.xfail(strict=True)
def test_15():
    var_2 = python_code_.thingML_UnaryMinus()
    var_3 = "A~0YqB_PPu!p~'7'9"
    var_4 = python_code_.thingML_MergeSources(name=var_3, thingML_MergeSources=())
    assert isinstance(var_4, python_code_.thingML_MergeSources)
    var_5 = "thingML_Source83 _thingML_JoinSources__thingML_JoinSources thingML_Session thingML_Parameter"
    var_6 = python_code_.thingML_ViewSource
    python_code_.thingML_Message(
        name=var_5,
        thingML_Message55=var_2,
        thingML_Message86=var_4,
        thingML_Message107=var_3,
        thingML_Message=var_6,
    )


def test_16():
    var_3 = "A~0YqB_PPu!p~'7'9"
    var_4 = python_code_.thingML_MergeSources(name=var_3, thingML_MergeSources=())
    assert isinstance(var_4, python_code_.thingML_MergeSources)
    var_15 = python_code_.thingML_Port(name=var_3)
    assert isinstance(var_15, python_code_.thingML_Port)


def test_17():
    var_0 = python_code_.thingML_DoubleLiteral(doubleValue="thingML_InstanceRef276")
    assert isinstance(var_0, python_code_.thingML_DoubleLiteral)
    var_5 = "_thingML_Session__thingML_Session212"
    var_6 = set()
    var_7 = python_code_.thingML_Port(name=var_5, thingML_Port64=var_6)
    assert isinstance(var_7, python_code_.thingML_Port)
    var_12 = python_code_.thingML_PlusExpression()
    var_18 = python_code_.thingML_RequiredPort(optional=var_12)
    assert isinstance(var_18, python_code_.thingML_RequiredPort)


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = lambda *args, **kwargs: ""
    var_1 = python_code_.thingML_ExternStatement(statement=var_0)
    assert isinstance(var_1, python_code_.thingML_ExternStatement)
    var_3 = python_code_.thingML_StartSession()
    var_5 = python_code_.thingML_SendAction()
    var_6 = python_code_.thingML_Port(
        name=var_3, thingML_Port=var_0, thingML_Port174=var_5, thingML_Port271=var_1
    )
    assert isinstance(var_6, python_code_.thingML_Port)
    var_9 = "thingML_Enumeration"
    var_10 = True
    python_code_.thingML_CompositeState(
        history=var_10,
        thingML_CompositeState118=var_9,
        thingML_CompositeState115=var_10,
    )


def test_19():
    var_0 = python_code_.thingML_ConfigPropertyAssign()
    var_2 = python_code_.thingML_MessageParameter(name=var_0)
    assert isinstance(var_2, python_code_.thingML_MessageParameter)
    var_4 = python_code_.thingML_ExternStatement
    var_6 = "l6oUj!*r]-H?D[D"
    var_10 = "thingML_ConfigPropertyAssign256._thingML_CompositeState__thingML_CompositeState118.thingML_Session.thingML_State"
    python_code_.thingML_PlatformAnnotation(
        name=-138, value=var_10, thingML_PlatformAnnotation15=[]
    )
    var_14 = python_code_.thingML_FunctionCallExpression()
    var_20 = bool
    var_21 = python_code_.thingML_MessageParameter(
        name=var_4, thingML_MessageParameter=var_20
    )
    assert isinstance(var_21, python_code_.thingML_MessageParameter)
    var_23 = python_code_.thingML_ExternStatement(statement=var_6)
    assert isinstance(var_23, python_code_.thingML_ExternStatement)
    var_25 = python_code_.thingML_CompositeState(history=var_14)
    assert isinstance(var_25, python_code_.thingML_CompositeState)


@pytest.mark.xfail(strict=True)
def test_20():
    var_2 = python_code_.thingML_UnaryMinus()
    var_3 = "A~0YqB_PPu!p~'7'9"
    var_4 = python_code_.thingML_MergeSources(name=var_3, thingML_MergeSources=())
    assert isinstance(var_4, python_code_.thingML_MergeSources)
    var_9 = python_code_.thingML_FunctionCallStatement()
    var_12 = "p5~.f4V"
    python_code_.thingML_State(
        name=var_12, thingML_State116=var_9, thingML_State144=var_2
    )


def test_21():
    python_code_.thingML_ActionBlock()


def test_22():
    var_1 = python_code_.thingML_Event()
    var_2 = python_code_.thingML_PrimitiveType(ByteSize=var_1)
    assert isinstance(var_2, python_code_.thingML_PrimitiveType)


def test_23():
    var_0 = "_thingML_Instance__thingML_nstance"
    var_1 = python_code_.thingML_Session(maxInstances=var_0)
    assert isinstance(var_1, python_code_.thingML_Session)
    var_3 = set()
    var_5 = python_code_.thingML_InternalTransition()
    var_6 = {var_5, var_5, var_5}
    var_8 = python_code_.thingML_Thing(
        fragment=False,
        thingML_Thing21=var_6,
        thingML_Thing27=var_3,
        thingML_Thing29=var_6,
    )
    assert isinstance(var_8, python_code_.thingML_Thing)
