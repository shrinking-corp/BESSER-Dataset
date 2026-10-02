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
    BooleanType,
    ConfigType,
    ConfigTypeType,
    ConfigTypeType1,
    Delegation,
    Enum,
    PriorityTypeMember0,
    SignalType,
    TypeTypeMember1,
    date,
    datetime,
    jpdl31_ActionType,
    jpdl31_AssignmentType,
    jpdl31_CancelTimerType,
    jpdl31_ConditionType,
    jpdl31_CreateTimerType,
    jpdl31_DecisionType,
    jpdl31_Delegation,
    jpdl31_DocumentRoot,
    jpdl31_EStringToStringMapEntry,
    jpdl31_EndStateType,
    jpdl31_EventType,
    jpdl31_ExceptionHandlerType,
    jpdl31_ForkType,
    jpdl31_JoinType,
    jpdl31_NodeType,
    jpdl31_ProcessDefinitionType,
    jpdl31_ProcessStateType,
    jpdl31_ScriptType,
    jpdl31_StartStateType,
    jpdl31_StateType,
    jpdl31_SubProcessType,
    jpdl31_SuperStateType,
    jpdl31_SwimlaneType,
    jpdl31_TaskNodeType,
    jpdl31_TaskType,
    jpdl31_TimerType,
    jpdl31_TransitionType,
    jpdl31_TransitionType1,
    jpdl31_VariableType,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.jpdl31_EStringToStringMapEntry()
    var_1 = python_code_.TypeTypeMember1.processStart
    var_2 = "5\t)2L%("
    var_3 = python_code_.jpdl31_JoinType
    python_code_.jpdl31_CreateTimerType(
        duedate=var_2,
        name=var_3,
        repeat=None,
        transition=var_2,
        jpdl31_CreateTimerType26=var_0,
        jpdl31_CreateTimerType185="Yn<b{\x0cr)2)Lv~3",
        jpdl31_CreateTimerType322=var_2,
        jpdl31_CreateTimerType339=var_1,
    )
    var_5 = '|$ymK"{jV5c\n"R"M?K'
    python_code_.jpdl31_CancelTimerType(name=var_5, jpdl31_CancelTimerType188=var_2)
    var_7 = python_code_.SignalType.unsynchronized
    var_8 = "jpdl31_ProcessDefinitionType178"
    var_9 = set()
    var_10 = python_code_.jpdl31_SuperStateType(
        group=var_5,
        async_=var_8,
        name=var_2,
        jpdl31_SuperStateType250=var_3,
        jpdl31_SuperStateType270=var_9,
        jpdl31_SuperStateType276=var_9,
    )
    assert isinstance(var_10, python_code_.jpdl31_SuperStateType)
    var_11 = python_code_.jpdl31_NodeType(
        nodeContentElements=var_7,
        name=var_8,
        async_=var_5,
        jpdl31_NodeType124=var_3,
        jpdl31_NodeType127=var_7,
        jpdl31_NodeType241=var_10,
    )
    assert isinstance(var_11, python_code_.jpdl31_NodeType)
    var_12 = "_jpdl31_CreateTimerType__jpdl31_CreateTimerType83"
    var_13 = "jpdl31_TimerType211:_jpdl31_DocumentRoot__jpdl31_DocumentRoot36:jpdl31_ScriptType182:_jpdl31_DocumentRoot__jpdl31_DocumentRoot49"
    var_14 = ">s{UIy?iv?U>s"
    python_code_.jpdl31_TransitionType(
        group=var_12,
        name=var_13,
        to=var_14,
        jpdl31_TransitionType220=var_14,
        jpdl31_TransitionType318=var_0,
        jpdl31_TransitionType327=var_9,
        jpdl31_TransitionType321=var_5,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_1 = python_code_.ConfigTypeType1
    var_4 = "_jpdl31_DocumentRoot__jpdl31_DocumentRoot41"
    var_5 = "_jpdl31_NodeType__jpdl31_NodeType124"
    var_6 = lambda *args, **kwargs: []
    python_code_.jpdl31_StateType(
        nodeContentElements=var_5,
        async_=var_4,
        name=var_1,
        jpdl31_StateType228=var_5,
        jpdl31_StateType231=var_6,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = "laa)!BRUBY<"
    var_2 = 'P\r3\rA{vbaw"'
    python_code_.jpdl31_StartStateType(group=var_1, name=var_2)
    var_4 = "T:;4A8@~b#."
    var_5 = python_code_.BooleanType
    var_6 = "g?40RKJoIXcJrQ"
    python_code_.jpdl31_EndStateType(name=var_2, group=var_4, jpdl31_EndStateType=var_4)
    var_8 = "z[<V:\\\rRut\\c"
    var_9 = "!s%"
    var_10 = "_jpdl31_NodeType__jpdl31_NodeType136"
    var_11 = "_<&$Jt"
    var_12 = "v7(kr)="
    var_13 = "EfumT\\@LM3Ap|s3"
    var_14 = "06"
    var_15 = python_code_.jpdl31_ActionType(
        mixed=var_8,
        any=var_6,
        acceptPropagatedEvents=var_6,
        async_=var_9,
        class_=var_10,
        configType=var_11,
        expression=var_12,
        name=var_13,
        refName=var_14,
        jpdl31_ActionType122=set(),
        jpdl31_ActionType316=False,
    )
    var_16 = {var_15}
    python_code_.jpdl31_DocumentRoot(
        mixed=var_5,
        jpdl31_DocumentRoot12=var_16,
        jpdl31_DocumentRoot33=var_5,
        jpdl31_DocumentRoot36=var_16,
        jpdl31_DocumentRoot25=complex(82.0, 1448.52407),
        jpdl31_DocumentRoot31=var_16,
        jpdl31_DocumentRoot18=2786.35,
        jpdl31_DocumentRoot20=var_16,
        jpdl31_DocumentRoot64=var_16,
        jpdl31_DocumentRoot56=complex(-1369.385282, 545.1),
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = lambda *args, **kwargs: []
    var_1 = "_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType271"
    var_2 = '"'
    var_3 = "jpdl31_TaskNodeType288"
    var_4 = "jpdl31_ProcessDefinitionType190"
    var_5 = python_code_.jpdl31_ProcessStateType(
        group=var_0, async_="J2:rFD\\", name=set()
    )
    var_6 = "_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerTypejpdl31_ExceptionHandlerType88_jpdl31_TransitionType__jpdl31_TransitionType_jpdl31_ActionType__jpdl31_ActionType310"
    var_7 = "f\x0c+7$`IYI$7<q"
    var_8 = python_code_.jpdl31_ActionType(
        mixed=var_2,
        any=var_6,
        acceptPropagatedEvents=(),
        async_=563.61,
        class_=var_0,
        configType=var_3,
        expression=var_0,
        name=var_4,
        refName=var_7,
        jpdl31_ActionType16=var_5,
        jpdl31_ActionType89=var_7,
        jpdl31_ActionType310=2108.96,
    )
    python_code_.jpdl31_TimerType(
        repeat=complex(268.121, -205.581),
        transition=var_1,
        duedate=var_4,
        name=var_0,
        jpdl31_TimerType211=var_5,
        jpdl31_TimerType309=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = "normal _jpdl31_JoinType__jpdl31_JoinType115 _jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType226 jpdl31_AssignmentType"
    var_1 = python_code_.jpdl31_EndStateType(
        name=var_0, group=var_0, jpdl31_EndStateType176=var_0
    )
    var_2 = "\tV X\n+KxH[_?!y"
    var_3 = python_code_.jpdl31_Delegation(
        mixed=var_0, configType=var_0, any=-30.38, class_=var_0
    )
    var_4 = {var_3, var_3, var_3, var_3}
    var_5 = python_code_.jpdl31_TaskType(
        group=complex(3038.0, 1495.349),
        description=var_0,
        duedate=var_0,
        name=var_0,
        priority=set(),
        signalling=var_1,
        swimlane=[],
        blocking=var_2,
        jpdl31_TaskType=var_2,
        jpdl31_TaskType297=set(),
        jpdl31_TaskType300=var_4,
        jpdl31_TaskType303=var_4,
        jpdl31_TaskType306=var_4,
    )
    assert isinstance(var_5, python_code_.jpdl31_TaskType)
    var_6 = "_jpdl31_TransitionType1__jpdl31_TransitionType1"
    var_7 = python_code_.jpdl31_AssignmentType
    python_code_.jpdl31_TransitionType1(
        group=var_2, name=var_6, to=(), jpdl31_TransitionType1335=var_7
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "i!"
    var_1 = "rHkL&^Nq7"
    var_2 = python_code_.jpdl31_Delegation(
        mixed=var_1,
        configType=var_1,
        any=var_1,
        class_="jpdl31_EventType34.jpdl31_TransitionType1.jpdl31_ExceptionHandlerType91.jpdl31_StartStateType",
        jpdl31_Delegation=var_0,
        jpdl31_Delegation301=var_0,
    )
    var_3 = {var_2, var_2, var_2, var_2}
    var_4 = lambda *args, **kwargs: False
    var_5 = "CKY(?'jy&%Q-5"
    var_6 = python_code_.jpdl31_ActionType(
        mixed=var_2,
        any=True,
        acceptPropagatedEvents=(),
        async_=var_5,
        class_=var_1,
        configType=482.51,
        expression=("]_dGR}eYz_6)0AIM^?S", False, -1178.45),
        name=var_0,
        refName=var_1,
        jpdl31_ActionType=var_4,
        jpdl31_ActionType16=var_0,
        jpdl31_ActionType122=var_0,
    )
    var_7 = "Bt?G.'-EM"
    python_code_.jpdl31_EventType(
        actionElements=var_4,
        type=var_7,
        jpdl31_EventType110=var_4,
        jpdl31_EventType286=-536,
    )
    var_9 = "-t\rC|6bQ"
    python_code_.jpdl31_ProcessDefinitionType(
        group=var_9,
        name=b"\x05o\xfd\xa1.\xfd\x81L\x84\x9d\x9e\x19{s\xa8",
        jpdl31_ProcessDefinitionType=[False],
        jpdl31_ProcessDefinitionType157=(),
        jpdl31_ProcessDefinitionType148=var_4,
        jpdl31_ProcessDefinitionType169=976,
        jpdl31_ProcessDefinitionType196=var_3,
        jpdl31_ProcessDefinitionType187=var_3,
        jpdl31_ProcessDefinitionType190=var_6,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_2 = lambda *args, **kwargs: "3I,"
    var_3 = "jpdl31_JoinType"
    var_4 = python_code_.jpdl31_CancelTimerType(name=var_3)
    var_5 = {var_4, var_4, var_4, var_4, var_4}
    python_code_.jpdl31_DocumentRoot(
        mixed=b"\x0e\x84\xfbjV",
        jpdl31_DocumentRoot33=var_2,
        jpdl31_DocumentRoot36=[],
        jpdl31_DocumentRoot28=var_2,
        jpdl31_DocumentRoot45=var_2,
        jpdl31_DocumentRoot20=var_5,
        jpdl31_DocumentRoot58=3,
        jpdl31_DocumentRoot60=True,
        jpdl31_DocumentRoot62=[True, 'Kwk\\,"33'],
        jpdl31_DocumentRoot68=var_5,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.TypeTypeMember1.taskStart
    var_7 = set()
    python_code_.jpdl31_DocumentRoot(
        mixed=True,
        jpdl31_DocumentRoot41=(),
        jpdl31_DocumentRoot25=var_7,
        jpdl31_DocumentRoot47=b"w\xc6\xf4\xed\x9c",
        jpdl31_DocumentRoot49=var_0,
        jpdl31_DocumentRoot43=var_7,
        jpdl31_DocumentRoot20=var_7,
        jpdl31_DocumentRoot58=None,
        jpdl31_DocumentRoot60=var_7,
        jpdl31_DocumentRoot62=(-830.05, True, False),
        jpdl31_DocumentRoot64=var_7,
        jpdl31_DocumentRoot52=var_7,
        jpdl31_DocumentRoot68=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_1 = "`)KXqqp2"
    var_2 = "jpdl31_TransitionType1338"
    var_3 = python_code_.jpdl31_EStringToStringMapEntry()
    var_4 = {var_3, var_3}
    python_code_.jpdl31_DocumentRoot(
        mixed=var_2,
        jpdl31_DocumentRoot12=var_4,
        jpdl31_DocumentRoot31=var_4,
        jpdl31_DocumentRoot45=[True, -3034.93],
        jpdl31_DocumentRoot49=var_1,
        jpdl31_DocumentRoot64=var_3,
        jpdl31_DocumentRoot56=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = "MwyM.a'MpQG7H,-`"
    var_3 = ",?`&\tZ{"
    python_code_.jpdl31_DecisionType(
        group="?so]gUv",
        expression=var_3,
        name=var_0,
        async_=b"P\xaa\xb6\x9e\xe1Q",
        jpdl31_DecisionType=True,
        jpdl31_DecisionType9=var_0,
    )
