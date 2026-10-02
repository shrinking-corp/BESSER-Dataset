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
    BindingType,
    BooleanType,
    ConfigType,
    Delegation,
    Enum,
    PriorityTypeMember0,
    SignalType,
    TypeTypeMember1,
    date,
    datetime,
    jpdl32_ActionType,
    jpdl32_AssignmentType,
    jpdl32_CancelTimerType,
    jpdl32_ConditionType,
    jpdl32_CreateTimerType,
    jpdl32_DecisionType,
    jpdl32_Delegation,
    jpdl32_DocumentRoot,
    jpdl32_EStringToStringMapEntry,
    jpdl32_EndStateType,
    jpdl32_EventType,
    jpdl32_ExceptionHandlerType,
    jpdl32_ForkType,
    jpdl32_JoinType,
    jpdl32_MailNodeType,
    jpdl32_MailType,
    jpdl32_NodeType,
    jpdl32_ProcessDefinitionType,
    jpdl32_ProcessStateType,
    jpdl32_ReminderType,
    jpdl32_ScriptType,
    jpdl32_StartStateType,
    jpdl32_StateType,
    jpdl32_SubProcessType,
    jpdl32_SuperStateType,
    jpdl32_SwimlaneType,
    jpdl32_TaskNodeType,
    jpdl32_TaskType,
    jpdl32_TimerType,
    jpdl32_TransitionType,
    jpdl32_VariableType,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = "_jpdl32_JoinType__jpdl32_JoinType"
    var_1 = ""
    var_2 = python_code_.ConfigType
    var_3 = python_code_.jpdl32_StartStateType(
        group=var_2, description=None, name=var_0, jpdl32_StartStateType=var_2
    )
    var_4 = {var_3, var_3}
    var_5 = python_code_.jpdl32_ProcessDefinitionType(
        group=var_1,
        description=var_0,
        name=var_0,
        jpdl32_ProcessDefinitionType=var_0,
        jpdl32_ProcessDefinitionType171=var_4,
        jpdl32_ProcessDefinitionType180=var_4,
        jpdl32_ProcessDefinitionType186=var_2,
        jpdl32_ProcessDefinitionType204=var_4,
        jpdl32_ProcessDefinitionType216=var_0,
    )
    var_6 = python_code_.jpdl32_ScriptType(
        mixed=var_1,
        any=var_2,
        acceptPropagatedEvents="J0QQ\x0c[ sH6_JB",
        name=complex(456.254603, 1993.5),
        jpdl32_ScriptType145=var_2,
        jpdl32_ScriptType208=var_5,
    )
    var_7 = "?UOIt\\i\r+Unms"
    var_8 = "jpdl32_CreateTimerType211 _jpdl32_TransitionType__jpdl32_TransitionType243 _jpdl32_MailType__jpdl32_MailType217"
    var_9 = "w[f2OC)"
    var_10 = python_code_.jpdl32_DocumentRoot(
        mixed=[
            "jpdl32_ProcessDefinitionType195-jpdl32_ProcessDefinitionType177-_jpdl32_SwimlaneType__jpdl32_SwimlaneType169-jpdl32_EventType118"
        ],
        description=set(),
        recipients=var_8,
        subject="[61-n4n7jf1v",
        template=var_9,
        text=True,
        to={},
        jpdl32_DocumentRoot43=var_4,
        jpdl32_DocumentRoot45=var_4,
        jpdl32_DocumentRoot47=var_4,
        jpdl32_DocumentRoot53=var_4,
        jpdl32_DocumentRoot=var_4,
        jpdl32_DocumentRoot20=var_1,
        jpdl32_DocumentRoot28=var_4,
        jpdl32_DocumentRoot33=var_2,
        jpdl32_DocumentRoot68={True, 628.89, False},
        jpdl32_DocumentRoot70=var_4,
    )
    var_11 = python_code_.jpdl32_ActionType(
        mixed=var_1,
        any=[],
        acceptPropagatedEvents=var_7,
        async_=var_2,
        class_=None,
        configType=var_4,
        expression=var_0,
        name=var_4,
        refName=var_4,
        jpdl32_ActionType16=var_10,
        jpdl32_ActionType97={
            "o": "Z:g8nC",
            "LKHaagr#DC": 380.51,
            "_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType109": False,
        },
        jpdl32_ActionType361=True,
    )
    assert isinstance(var_11, python_code_.jpdl32_ActionType)
    python_code_.jpdl32_NodeType(
        description=var_0,
        async_=var_0,
        name=var_0,
        nodeContentElements=var_1,
        jpdl32_NodeType144=var_6,
        jpdl32_NodeType162=var_4,
        jpdl32_NodeType141=var_11,
    )


def test_1():
    var_0 = python_code_.jpdl32_ProcessStateType
    python_code_.jpdl32_EndStateType(
        group=var_0, description=var_0, endCompleteProcess=2, name=var_0
    )
    var_2 = "m\\66"
    python_code_.jpdl32_ReminderType(duedate=False, repeat=var_2)


def test_2():
    var_1 = "DmLjz,\tC1g(Q"
    var_2 = "EKATwX&,"
    var_3 = python_code_.jpdl32_VariableType(
        any=var_1,
        access=var_2,
        mappedName={"pI8#W].iz:mG2XIU", -1892.46},
        name=None,
        jpdl32_VariableType={},
    )
    assert isinstance(var_3, python_code_.jpdl32_VariableType)
    var_4 = {var_3, var_3, var_3, var_3}
    python_code_.jpdl32_ProcessStateType(
        group=var_1,
        async_=var_1,
        binding=var_1,
        name=var_1,
        description=var_1,
        jpdl32_ProcessStateType230=var_4,
        jpdl32_ProcessStateType236=None,
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = lambda *args, **kwargs: "[)TT#kC;**&u|"
    var_1 = "jpdl32_ScriptType103"
    python_code_.jpdl32_VariableType(
        any=var_0, access=var_1, mappedName=var_0, name=var_1
    )
    var_3 = (
        lambda *args, **kwargs: "jpdl32_EventType336.jpdl32_StateType257._jpdl32_TimerType__jpdl32_TimerType264"
    )
    var_4 = "3AGG\r"
    var_5 = "i\t)18RL'6P>Ox> "
    var_6 = ',>,`\rq"?'
    var_8 = "jpdl32_SuperStateType272.nodeEnter.jpdl32_EventType"
    var_9 = "_"
    python_code_.jpdl32_TaskType(
        group=var_5,
        description=var_8,
        blocking=var_9,
        description1="/Rqr![D'YGO\nR",
        duedate=var_3,
        name=var_5,
        notify={"k%T249Z": -766, "Cn|J17~>d3<n*PUB>b+": False},
        priority=var_3,
        signalling={
            "_jpdl32_JoinType__jpdl32_JoinType120jpdl32_TransitionType267": "!cQY<U$F?",
            "ncY%XvSedx": False,
            "jpdl32_SubProcessType": True,
        },
        swimlane=var_1,
        jpdl32_TaskType246=var_4,
    )
    var_11 = "nodeEnter_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType376jpdl32_SuperStateType184"
    var_14 = "jpdl32_CreateTimerType88"
    var_15 = set()
    python_code_.jpdl32_SuperStateType(
        group=(),
        async_=var_6,
        name=var_14,
        description=var_11,
        jpdl32_SuperStateType=var_3,
        jpdl32_SuperStateType184=var_11,
        jpdl32_SuperStateType279=None,
        jpdl32_SuperStateType277=var_3,
        jpdl32_SuperStateType284=var_15,
        jpdl32_SuperStateType296=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = "_jpdl32_MailNodeType__jpdl32_MailNodeType._jpdl32_CreateTimerType__jpdl32_CreateTimerType88"
    var_1 = python_code_.jpdl32_MailType
    var_2 = set()
    var_3 = python_code_.jpdl32_TransitionType(
        group=var_0,
        description=var_0,
        name=var_1,
        to=var_0,
        jpdl32_TransitionType=var_0,
        jpdl32_TransitionType115=var_0,
        jpdl32_TransitionType139=var_1,
        jpdl32_TransitionType372=var_2,
    )
    var_4 = {var_3, var_3, var_3}
    python_code_.jpdl32_JoinType(
        nodeContentElements=var_0,
        description="GA:Iu[:rWPMi",
        async_=set(),
        name=var_0,
        jpdl32_JoinType126=var_4,
        jpdl32_JoinType288=var_2,
    )
    var_6 = "{NQ"
    var_7 = python_code_.jpdl32_AssignmentType(
        actorId=var_1,
        expression=var_6,
        pooledActors=var_6,
        jpdl32_AssignmentType330=complex(314.7, 1768.8198),
    )
    assert isinstance(var_7, python_code_.jpdl32_AssignmentType)
    python_code_.jpdl32_SwimlaneType(
        name={False, False, "nN,"}, jpdl32_SwimlaneType311=var_7
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_1 = python_code_.jpdl32_EStringToStringMapEntry
    var_2 = "K\x0b4u-ZOS/"
    var_3 = "_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType255-jpdl32_EventType300-jpdl32_AssignmentType-jpdl32_SuperStateType305"
    var_4 = "&4a2"
    var_5 = "^>[gi9Op~"
    var_6 = "~Ap}aQ"
    var_7 = python_code_.jpdl32_EndStateType(
        group=var_4, description=var_2, endCompleteProcess=var_5, name=var_6
    )
    var_8 = {var_7, var_7, var_7, var_7, var_7}
    python_code_.jpdl32_SuperStateType(
        group=var_1,
        async_=var_3,
        name=var_2,
        description=var_2,
        jpdl32_SuperStateType293=var_8,
        jpdl32_SuperStateType305=var_1,
        jpdl32_SuperStateType269=b"c\xd7",
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_2 = "jpdl32_DocumentRoot"
    var_4 = python_code_.jpdl32_NodeType
    var_6 = set()
    var_7 = "jpdl32_TaskNodeType320"
    var_8 = "_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType216.jpdl32_SuperStateType272.jpdl32_ProcessStateType233.jpdl32_ActionType142"
    var_9 = 'e9v+ xi\x0bL\\\\g\tc"*B'
    var_10 = "BHQN%*&q+*o^NPo%Fyh"
    var_11 = python_code_.jpdl32_StateType(
        nodeContentElements=var_4,
        description=var_9,
        async_=var_10,
        name=var_4,
        jpdl32_StateType257=var_6,
    )
    python_code_.jpdl32_ExceptionHandlerType(
        group=var_7,
        exceptionClass=var_8,
        jpdl32_ExceptionHandlerType96=1190.66,
        jpdl32_ExceptionHandlerType109=var_2,
        jpdl32_ExceptionHandlerType255={1642, -3632.12, 0},
        jpdl32_ExceptionHandlerType261=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.jpdl32_ReminderType(
        duedate=-878.36, repeat=".v]@:T\x0b+':3p?^{"
    )
    var_1 = int
    var_2 = "( ]Qp\x0c"
    var_4 = "_jpdl32_TransitionType__jpdl32_TransitionType372"
    var_5 = "X\tZydE"
    var_6 = "on.on._jpdl32_TransitionType__jpdl32_TransitionType369.jpdl32_ProcessStateType233"
    var_7 = "/<S'R"
    var_8 = python_code_.jpdl32_ProcessStateType(
        group=-4293.4,
        async_="jpdl32_ExceptionHandlerType321.superstateEnter.jpdl32_SuperStateType",
        binding=var_6,
        name=var_2,
        description=var_7,
        jpdl32_ProcessStateType282=var_5,
        jpdl32_ProcessStateType187=var_2,
        jpdl32_ProcessStateType228=var_4,
    )
    var_9 = {var_8, var_8}
    python_code_.jpdl32_DocumentRoot(
        mixed=-1923.04,
        description=b"\xd4\xb6\xde\x9b\x87:\x87v_h\x9aO\xc6\x97\xb2\xd4W}",
        recipients=var_4,
        subject=var_5,
        template=var_0,
        text=var_1,
        to=var_1,
        jpdl32_DocumentRoot51=var_9,
        jpdl32_DocumentRoot53=2156,
        jpdl32_DocumentRoot56=var_9,
        jpdl32_DocumentRoot=var_9,
        jpdl32_DocumentRoot12=953.38,
        jpdl32_DocumentRoot15=var_1,
        jpdl32_DocumentRoot25=var_9,
        jpdl32_DocumentRoot33=complex(265.0, -2825.642),
        jpdl32_DocumentRoot41=var_1,
        jpdl32_DocumentRoot66=1206.64,
        jpdl32_DocumentRoot70=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_1 = "`#lk&&bX'\n_"
    var_2 = "s;[qw\x0b"
    var_3 = set()
    python_code_.jpdl32_ProcessDefinitionType(
        group=var_1,
        description=121.09,
        name=var_2,
        jpdl32_ProcessDefinitionType183=95.13,
        jpdl32_ProcessDefinitionType204=var_3,
        jpdl32_ProcessDefinitionType189=None,
        jpdl32_ProcessDefinitionType222="_jpdl32_ScriptType__jpdl32_ScriptType_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType213_jpdl32_TaskType__jpdl32_TaskType246",
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.Delegation()
    var_1 = "(\tf`UgV](wg/_gK27"
    var_3 = "\nxiv{c8)5+n"
    var_4 = lambda *args, **kwargs: True
    python_code_.jpdl32_ForkType(
        group=var_1,
        description=var_1,
        async_=var_3,
        name=var_4,
        jpdl32_ForkType=var_0,
        jpdl32_ForkType108=var_4,
        jpdl32_ForkType114=b"\xaf\xb5\r\xda\x98$\xed\x9c\xe9\xd7B\xd1\x9b&W",
    )
