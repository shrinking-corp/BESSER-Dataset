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
    AnswerType,
    ArtefactType,
    BooleanType,
    ConfigType,
    ConfigTypeType,
    ConfigTypeType1,
    Delegation,
    DoEType,
    Enum,
    HypothesisType,
    MetricType,
    PriorityTypeMember0,
    QuestionnaireType,
    RelationOperator,
    SignalType,
    TypeTypeMember1,
    date,
    datetime,
    jpdl31_ActionType,
    jpdl31_Alternative,
    jpdl31_Artefact,
    jpdl31_AssignmentType,
    jpdl31_CancelTimerType,
    jpdl31_ConditionType,
    jpdl31_CreateTimerType,
    jpdl31_DecisionType,
    jpdl31_Delegation,
    jpdl31_DependentVariable,
    jpdl31_Design,
    jpdl31_DocumentRoot,
    jpdl31_EStringToStringMapEntry,
    jpdl31_EndStateType,
    jpdl31_EventType,
    jpdl31_ExceptionHandlerType,
    jpdl31_ExperimentalPlan,
    jpdl31_Factor,
    jpdl31_ForkType,
    jpdl31_Goal,
    jpdl31_Hyphotesis,
    jpdl31_JoinType,
    jpdl31_Level,
    jpdl31_Metric,
    jpdl31_MetricInfo,
    jpdl31_Model,
    jpdl31_NodeType,
    jpdl31_Parameter,
    jpdl31_ProcessDefinitionType,
    jpdl31_ProcessStateType,
    jpdl31_Question,
    jpdl31_Questionnaire,
    jpdl31_ScriptType,
    jpdl31_StartStateType,
    jpdl31_StateType,
    jpdl31_StatisticalTest,
    jpdl31_SubProcessType,
    jpdl31_Subhypotheses,
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
    var_1 = "ee=#b@\r"
    var_2 = python_code_.jpdl31_Factor(
        name=var_1, isTreament=var_1, jpdl31_Factor411=set()
    )
    assert isinstance(var_2, python_code_.jpdl31_Factor)
    var_3 = ",3[G^Rm <t'JK<-!"
    var_4 = lambda *args, **kwargs: []
    var_5 = '{OZ"t\\k9mE;VJ+m'
    var_6 = "}r4Zd`"
    python_code_.jpdl31_TaskType(
        group=var_3,
        blocking=var_4,
        description=var_5,
        duedate=var_4,
        name=complex(-1822.2580864, -3719.4403),
        priority=var_4,
        signalling=var_2,
        swimlane=var_6,
        jpdl31_TaskType307=var_4,
        jpdl31_TaskType316=b"\x03\x7fp\r\x936\x15r\xd8m(\xa46\xaf@\xb2\x8b",
        jpdl31_TaskType319=var_3,
        jpdl31_TaskType310=-2261,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = "P;'"
    var_1 = float
    var_2 = python_code_.jpdl31_DependentVariable(name=var_0, description=var_1)
    assert isinstance(var_2, python_code_.jpdl31_DependentVariable)
    var_5 = "g_7E"
    var_6 = set()
    var_7 = python_code_.jpdl31_Model()
    python_code_.jpdl31_DocumentRoot(
        mixed=var_5,
        jpdl31_DocumentRoot=var_6,
        jpdl31_DocumentRoot15={},
        jpdl31_DocumentRoot25=2165,
        jpdl31_DocumentRoot28=var_6,
        jpdl31_DocumentRoot45=var_1,
        jpdl31_DocumentRoot54=var_6,
        jpdl31_DocumentRoot70={True, False, 298.04},
        jpdl31_DocumentRoot74=var_6,
        jpdl31_DocumentRoot64=var_6,
        jpdl31_DocumentRoot363=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = "_jpdl31_CancelTimerType__jpdl31_CancelTimerType137"
    var_1 = lambda *args, **kwargs: False
    var_2 = "cX~w\x0b0\x0cet0md"
    var_3 = python_code_.jpdl31_Subhypotheses(
        relationOp=var_2, jpdl31_Subhypotheses=var_1
    )
    python_code_.jpdl31_DependentVariable(
        name=var_0, description=var_1, jpdl31_DependentVariable379=var_3
    )


def test_3():
    python_code_.jpdl31_Subhypotheses(relationOp=[])
    var_1 = python_code_.RelationOperator.different
    var_2 = "jpdl31_ProcessDefinitionType"
    python_code_.jpdl31_CancelTimerType(name=var_2, jpdl31_CancelTimerType358=var_1)


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = "<:"
    var_1 = lambda *args, **kwargs: 2049
    var_2 = "_jpdl31_TaskNodeType__jpdl31_TaskNodeType297"
    var_3 = python_code_.jpdl31_Hyphotesis(
        description=b"\x91\xdf\xa7A\x1d\x8a\x81\xbe\x15\xd2f\xfe\xf9Nb\xe4",
        type=var_1,
        id=var_1,
        relationOp=var_2,
        jpdl31_Hyphotesis369=var_1,
    )
    assert isinstance(var_3, python_code_.jpdl31_Hyphotesis)
    var_4 = python_code_.jpdl31_Subhypotheses(
        relationOp=var_0, jpdl31_Subhypotheses=var_3
    )
    assert isinstance(var_4, python_code_.jpdl31_Subhypotheses)
    var_5 = "jpdl31_TaskNodeType294"
    var_6 = lambda *args, **kwargs: "jpdl31_TransitionType220"
    var_7 = "jpdl31_DocumentRoot52"
    var_8 = "MT,;phT)I"
    var_9 = "_jpdl31_EventType__jpdl31_EventType235:_jpdl31_DependentVariable__jpdl31_DependentVariable381"
    var_10 = python_code_.jpdl31_CancelTimerType(
        name=var_9, jpdl31_CancelTimerType137=("\x0c+ |", 1619.47, -544.9)
    )
    python_code_.jpdl31_NodeType(
        name=var_6,
        description=var_5,
        nodeContentElements=var_7,
        async_=var_8,
        jpdl31_NodeType136=var_10,
        jpdl31_NodeType139=b"\x8c9\xfe\xb3\xda\xcb\x1d",
        jpdl31_NodeType142=var_10,
        jpdl31_NodeType247="jpdl31_TimerType328-_jpdl31_Delegation__jpdl31_Delegation311",
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "3A9"
    var_1 = python_code_.ArtefactType
    var_2 = python_code_.jpdl31_SubProcessType(
        name=var_1, version=var_1, jpdl31_SubProcessType=var_1
    )
    var_3 = "s7\rJ"
    var_4 = python_code_.jpdl31_SubProcessType(name=var_3, version=None)
    var_5 = {var_2, var_4, var_2, var_4}
    var_6 = python_code_.jpdl31_ProcessStateType(
        group=var_1,
        async_=var_0,
        name=var_0,
        jpdl31_ProcessStateType="_jpdl31_ActionType__jpdl31_ActionType95 jpdl31_DocumentRoot49 _jpdl31_CancelTimerType__jpdl31_CancelTimerType92",
        jpdl31_ProcessStateType205=var_5,
        jpdl31_ProcessStateType216=var_1,
        jpdl31_ProcessStateType259=var_4,
    )
    var_7 = python_code_.jpdl31_CancelTimerType(
        name=var_1, jpdl31_CancelTimerType358=var_2
    )
    python_code_.jpdl31_NodeType(
        name=var_6,
        description=set(),
        nodeContentElements=var_3,
        async_=var_4,
        jpdl31_NodeType130=var_1,
        jpdl31_NodeType136=var_7,
        jpdl31_NodeType142=var_5,
        jpdl31_NodeType158=complex(-1965.0, -1789.1),
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = "vzL\x0c["
    var_1 = "_jpdl31_TimerType__jpdl31_TimerType122"
    var_2 = lambda *args, **kwargs: "?oB=&\nm2rtPBn|pCQiN"
    var_3 = python_code_.jpdl31_JoinType(
        nodeContentElements=var_0,
        async_=var_1,
        name={5467.63, False},
        jpdl31_JoinType118={"=4t[\rdxDs}z", "I@"},
        jpdl31_JoinType176=var_2,
    )
    var_4 = "_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType160"
    var_5 = "@"
    var_6 = python_code_.jpdl31_ScriptType(
        mixed=var_4,
        any=var_4,
        acceptPropagatedEvents=var_5,
        name=var_2,
        jpdl31_ScriptType352=var_0,
    )
    var_7 = {var_6, var_6}
    python_code_.jpdl31_TransitionType(
        group=var_0,
        name=var_0,
        to=var_1,
        jpdl31_TransitionType125=var_3,
        jpdl31_TransitionType="V(u$jZ",
        jpdl31_TransitionType334=var_7,
        jpdl31_TransitionType337=var_7,
        jpdl31_TransitionType343=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = "jpdl31_ForkType109equal_jpdl31_DependentVariable__jpdl31_DependentVariable"
    var_1 = python_code_.jpdl31_StatisticalTest
    var_2 = python_code_.jpdl31_Delegation(
        mixed=var_0, any=var_1, class_=var_0, configType=set(), jpdl31_Delegation23=True
    )
    var_3 = {var_2, var_2, var_2, var_2}
    var_4 = python_code_.jpdl31_StateType(
        nodeContentElements=var_3,
        async_=0,
        name=var_2,
        jpdl31_StateType=var_1,
        jpdl31_StateType237={"jpdl31_EventType140.checkBox", 631, 763.29},
    )
    var_5 = {var_4, var_4, var_4, var_4}
    var_6 = python_code_.jpdl31_Model()
    python_code_.jpdl31_DocumentRoot(
        mixed=var_0,
        jpdl31_DocumentRoot22=var_3,
        jpdl31_DocumentRoot31=b"\x1c\xebIyOkg",
        jpdl31_DocumentRoot33=var_1,
        jpdl31_DocumentRoot36=219.34,
        jpdl31_DocumentRoot18=var_0,
        jpdl31_DocumentRoot54=var_5,
        jpdl31_DocumentRoot70=[-3000.99],
        jpdl31_DocumentRoot66=var_5,
        jpdl31_DocumentRoot363=var_6,
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = python_code_.jpdl31_TaskType
    var_3 = ""
    python_code_.jpdl31_DecisionType(
        group=var_3,
        expression=var_0,
        name=var_0,
        async_=var_0,
        jpdl31_DecisionType5=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = abs
    var_1 = "m&lyLI3i"
    var_2 = "^q]LXQC!/"
    var_3 = "\t'CMi"
    var_4 = "GDG'x[wS"
    var_5 = "_jpdl31_CancelTimerType__jpdl31_CancelTimerType194"
    var_6 = python_code_.jpdl31_DecisionType(
        group=(1796.32, False, -2902),
        expression=var_2,
        name=var_0,
        async_=var_1,
        jpdl31_DecisionType5=var_4,
        jpdl31_DecisionType29=var_5,
        jpdl31_DecisionType179=None,
        jpdl31_DecisionType268=complex(-4037.0, -2815.7499852),
    )
    var_7 = python_code_.jpdl31_DecisionType(
        group=-497.23,
        expression=var_4,
        name=var_1,
        async_=var_0,
        jpdl31_DecisionType9="m",
        jpdl31_DecisionType29=var_0,
        jpdl31_DecisionType179=var_0,
        jpdl31_DecisionType268=var_3,
    )
    var_8 = {var_6, var_6, var_6, var_7, var_6}
    python_code_.jpdl31_DocumentRoot(
        mixed={"`~^Ci": -931.83, "": 2},
        jpdl31_DocumentRoot=var_5,
        jpdl31_DocumentRoot15=var_0,
        jpdl31_DocumentRoot28=var_8,
        jpdl31_DocumentRoot43=var_8,
        jpdl31_DocumentRoot74=var_8,
        jpdl31_DocumentRoot60=var_8,
        jpdl31_DocumentRoot62=var_8,
    )
