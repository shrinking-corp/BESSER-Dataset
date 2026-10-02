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
    Agent,
    FlowOfEvents,
    Statement,
    Step,
    abstractmethod,
    date,
    datetime,
    textualusecase_Action,
    textualusecase_Actor,
    textualusecase_Agent,
    textualusecase_AlternativeFlow,
    textualusecase_BasicFlow,
    textualusecase_Condition,
    textualusecase_ConditionalStatement,
    textualusecase_FlowOfEvents,
    textualusecase_Include,
    textualusecase_LoopStatement,
    textualusecase_Statement,
    textualusecase_Step,
    textualusecase_Subject,
    textualusecase_UseCase,
    textualusecase_UseCaseModel,
    time,
)


def test_0():
    var_4 = python_code_.textualusecase_FlowOfEvents(
        name="_textualusecase_Step__steps30", flowOfEvents=set()
    )
    assert isinstance(var_4, python_code_.textualusecase_FlowOfEvents)


def test_1():
    var_4 = python_code_.textualusecase_FlowOfEvents(name=',"?BHF+k', FlowOfEvents=None)
    assert isinstance(var_4, python_code_.textualusecase_FlowOfEvents)


@pytest.mark.xfail(strict=True)
def test_2():
    var_13 = "textualusecase_Condition13,_textualusecase_UseCase__useCase8,_textualusecase_UseCase__textualusecase_UseCase,AlternativeFlow27"
    var_14 = python_code_.textualusecase_Step(name=[])
    assert isinstance(var_14, python_code_.textualusecase_Step)
    var_15 = python_code_.textualusecase_FlowOfEvents
    python_code_.textualusecase_FlowOfEvents(
        name=var_13, FlowOfEvents=var_14, flowOfEvents=var_15
    )


def test_3():
    var_0 = python_code_.FlowOfEvents()
    var_16 = "agentagent"
    var_17 = python_code_.textualusecase_FlowOfEvents(
        name="_textualusecase_Step__Step:textualusecase_Condition13:_textualusecase_Agent__Agent",
        FlowOfEvents=var_0,
    )
    assert isinstance(var_17, python_code_.textualusecase_FlowOfEvents)
    var_18 = python_code_.textualusecase_Step(name=var_16, Step25=var_17)
    assert isinstance(var_18, python_code_.textualusecase_Step)
    var_21 = python_code_.textualusecase_Agent(name="dk)", Agent=None)
    assert isinstance(var_21, python_code_.textualusecase_Agent)


def test_4():
    var_27 = python_code_.textualusecase_Action(
        description=b"t\x8d\xf5G\x97H\xa7\xa8\xbc\xa6\xe5\xca4\x13{", Action=False
    )
    assert isinstance(var_27, python_code_.textualusecase_Action)


def test_5():
    var_9 = "_textualusecase2UseCase__textualEusecase_UseCase12"
    var_10 = python_code_.textualusecase_Action(
        description=var_9, Action={"\rO": -3308.13}, actions=var_9
    )
    assert isinstance(var_10, python_code_.textualusecase_Action)


def test_6():
    var_12 = python_code_.textualusecase_Action(
        description="_textualusecase_UseCase__useCase6textualusecase_Include",
        Action=None,
    )
    assert isinstance(var_12, python_code_.textualusecase_Action)


def test_7():
    var_11 = python_code_.textualusecase_Agent(name="w")
    assert isinstance(var_11, python_code_.textualusecase_Agent)


def test_8():
    var_11 = python_code_.textualusecase_Agent(name="n/8 ?{X\x0cUw#U^f*", agent=set())
    assert isinstance(var_11, python_code_.textualusecase_Agent)


def test_9():
    var_12 = "_textualusecase_UseCase__useCase6,textualusecase_Statement,Agent,textualusecase_Agent"
    var_13 = python_code_.textualusecase_Agent(name=var_12, Agent=var_12)
    assert isinstance(var_13, python_code_.textualusecase_Agent)
    var_14 = python_code_.textualusecase_Action(description=var_12, Action=var_13)
    assert isinstance(var_14, python_code_.textualusecase_Action)


def test_10():
    python_code_.textualusecase_Condition(
        expression="a1b^)+",
        textualusecase_Condition33=None,
        textualusecase_Condition20=None,
    )


def test_11():
    var_4 = python_code_.textualusecase_AlternativeFlow()
    python_code_.textualusecase_Condition(
        expression="Oy2o$-g", textualusecase_Condition20=var_4
    )


@pytest.mark.xfail(strict=True)
def test_12():
    var_12 = python_code_.Agent()
    var_13 = python_code_.textualusecase_BasicFlow
    var_14 = python_code_.textualusecase_Condition(
        expression=var_12, textualusecase_Condition13=-1581
    )
    assert isinstance(var_14, python_code_.textualusecase_Condition)
    python_code_.textualusecase_UseCase(
        name=var_13,
        description=var_13,
        UseCase47=None,
        UseCase42=var_12,
        useCase6=b"\x9e\xc9\x1b\n\xf4\x884\x16J_\xff\xc0u\x04",
        textualusecase_UseCase=var_14,
    )


def test_13():
    var_0 = python_code_.textualusecase_AlternativeFlow
    var_4 = lambda *args, **kwargs: False
    python_code_.textualusecase_Condition(
        expression=complex(777.414, -65.2),
        textualusecase_Condition=var_0,
        textualusecase_Condition13=var_4,
    )


def test_14():
    var_4 = python_code_.textualusecase_AlternativeFlow()
    python_code_.textualusecase_Condition(
        expression="textualusecase_Condition13,statement,textualusecase_BasicFlow,Step25",
        textualusecase_Condition33=var_4,
    )


def test_15():
    var_48 = python_code_.textualusecase_Step(
        name="_textualusecase_FlowOfEvents__FlowOfEvents",
        Step25=None,
        branchingStep=set(),
    )
    assert isinstance(var_48, python_code_.textualusecase_Step)


def test_16():
    var_48 = python_code_.textualusecase_Step(name="<):S", Step35=None, steps30=None)
    assert isinstance(var_48, python_code_.textualusecase_Step)


def test_17():
    var_0 = python_code_.textualusecase_BasicFlow()
    var_47 = python_code_.textualusecase_Step(name=var_0, Step=var_0, steps=var_0)
    assert isinstance(var_47, python_code_.textualusecase_Step)


def test_18():
    var_0 = python_code_.textualusecase_BasicFlow()
    var_47 = python_code_.textualusecase_Step(
        name="_textualusecase_Condition__textualusecase_Condition20.includes.FlowOfEvents._textualusecase_UseCase__UseCase42",
        steps30=var_0,
        steps=var_0,
    )
    assert isinstance(var_47, python_code_.textualusecase_Step)


def test_19():
    var_0 = python_code_.textualusecase_BasicFlow()
    var_48 = python_code_.textualusecase_Step(
        name="Rlh'SKHOYgTi\\G+!(^L", Step25=var_0, steps=None
    )
    assert isinstance(var_48, python_code_.textualusecase_Step)


def test_20():
    var_12 = "FlowOfEvents:_textualusecase_Step__Step:Step25"
    var_15 = python_code_.textualusecase_UseCase(
        name="_textualusecase_UseCase__useCase",
        description="textualusecase_UseCase12-_textualusecase_Action__Action-Action",
        useCase8={var_12, False},
        useCase={-1, var_12},
        textualusecase_UseCase12=var_12,
    )
    assert isinstance(var_15, python_code_.textualusecase_UseCase)


def test_21():
    var_49 = "#0\x0cEwGp?.fSm|/G<H"
    var_51 = python_code_.textualusecase_UseCase(
        name=var_49,
        description="_textualusecase_Agent__agent_textualusecase_Step__branchingSteptextualusecase_BasicFlow",
        UseCase=None,
        textualusecase_UseCase=var_49,
    )
    assert isinstance(var_51, python_code_.textualusecase_UseCase)


def test_22():
    var_0 = python_code_.FlowOfEvents()
    var_17 = python_code_.textualusecase_LoopStatement()
    var_19 = python_code_.textualusecase_UseCase(
        name="<,HVmo:DV",
        description=")OgJs(9N",
        useCase6=None,
        UseCase23=None,
        useCase17={var_17, var_0},
        UseCase37=None,
    )
    assert isinstance(var_19, python_code_.textualusecase_UseCase)


def test_23():
    var_17 = python_code_.textualusecase_LoopStatement()
    var_18 = []
    var_19 = python_code_.textualusecase_UseCase(
        name=var_18,
        description=var_18,
        UseCase=None,
        UseCase23=var_17,
        textualusecase_UseCase12=None,
        useCase15=None,
        useCase17=set(),
        UseCase37=var_17,
    )
    assert isinstance(var_19, python_code_.textualusecase_UseCase)


def test_24():
    var_17 = python_code_.textualusecase_LoopStatement()
    var_18 = "&uj\ncDd<%zS_dy^M"
    var_19 = python_code_.textualusecase_UseCase(
        name="_textualusecase_Condition__textualusecase_Condition20",
        description="Action-flowOfEvents",
        UseCase47=var_17,
        textualusecase_UseCase=None,
        textualusecase_UseCase12=var_17,
        useCase17=set(),
    )
    assert isinstance(var_19, python_code_.textualusecase_UseCase)
    python_code_.textualusecase_Condition(
        expression=var_18, textualusecase_Condition33=var_19
    )


def test_25():
    var_10 = "z"
    var_11 = "_textualusecase_Condition__textualusecase_Condition33"
    var_12 = python_code_.textualusecase_Statement
    var_13 = python_code_.textualusecase_Condition(
        expression=var_10, textualusecase_Condition33=var_12
    )
    var_15 = python_code_.textualusecase_UseCase(
        name=var_11, description=var_11, useCase15=var_10, UseCase37=var_13
    )
    assert isinstance(var_15, python_code_.textualusecase_UseCase)


def test_26():
    var_0 = "textualusecase_UseCase12-Include-_textualusecase_Step__Step"
    var_1 = python_code_.textualusecase_UseCaseModel()
    var_2 = python_code_.textualusecase_AlternativeFlow()
    var_3 = {var_2, var_2}
    var_4 = python_code_.textualusecase_UseCase(
        name=var_0,
        description=var_0,
        useCase6=[],
        UseCase=var_1,
        useCase=var_3,
        UseCase23=var_2,
        UseCase37=328.0,
    )
    assert isinstance(var_4, python_code_.textualusecase_UseCase)


def test_27():
    var_0 = python_code_.FlowOfEvents()
    var_19 = python_code_.textualusecase_UseCase(
        name="5lO[{,\\\rU\n7y<A",
        description="textualusecase_ActorStatement_textualusecase_Condition__textualusecase_Condition",
        useCase8={-2172},
        UseCase=var_0,
    )
    assert isinstance(var_19, python_code_.textualusecase_UseCase)


def test_28():
    python_code_.textualusecase_AlternativeFlow()


@pytest.mark.xfail(strict=True)
def test_29():
    var_1 = python_code_.textualusecase_Action(description=())
    assert isinstance(var_1, python_code_.textualusecase_Action)
    var_2 = lambda *args, **kwargs: 2
    var_3 = python_code_.textualusecase_Agent(name=var_2)
    assert isinstance(var_3, python_code_.textualusecase_Agent)
    var_5 = python_code_.Agent()
    var_6 = "+i"
    var_7 = python_code_.textualusecase_UseCase(
        name=var_6,
        description="_textualusecase_Condition__textualusecase_Condition-_textualusecase_Agent__Agent-alternativeFlow",
        useCase6=var_1,
        useCase15=var_2,
        UseCase37=var_5,
    )
    assert isinstance(var_7, python_code_.textualusecase_UseCase)
    var_13 = "/G``ReQ^K@}^"
    var_14 = python_code_.textualusecase_FlowOfEvents(name=var_13)
    assert isinstance(var_14, python_code_.textualusecase_FlowOfEvents)
    var_19 = python_code_.textualusecase_FlowOfEvents(name=var_13, FlowOfEvents=var_6)
    assert isinstance(var_19, python_code_.textualusecase_FlowOfEvents)
    python_code_.textualusecase_Condition(expression=var_13)
    var_27 = python_code_.textualusecase_Statement()
    python_code_.textualusecase_Step(name=var_1, steps30=var_19, steps=var_27)


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = python_code_.FlowOfEvents()
    var_12 = "satement UseCaseModel"
    var_13 = python_code_.textualusecase_Agent(name=var_0)
    assert isinstance(var_13, python_code_.textualusecase_Agent)
    python_code_.textualusecase_Action(description=var_12, actions=var_13)


@pytest.mark.xfail(strict=True)
def test_31():
    var_50 = "|`zCP2w^Q}cC 8_]\x0bFz"
    var_51 = hash
    var_52 = python_code_.textualusecase_Condition(
        expression=var_50, textualusecase_Condition33=var_51
    )
    assert isinstance(var_52, python_code_.textualusecase_Condition)
    python_code_.textualusecase_UseCase(
        name=var_50,
        description=var_51,
        UseCase47=set(),
        UseCase23=var_51,
        textualusecase_UseCase=['(4RP2WHY!4\\"h', 1569.82, 1609],
        textualusecase_UseCase12=var_52,
        useCase15=var_51,
    )


def test_32():
    var_4 = python_code_.textualusecase_AlternativeFlow()
    python_code_.textualusecase_Condition(
        expression="AlternativeFlow27",
        textualusecase_Condition20=var_4,
        textualusecase_Condition13=var_4,
    )


def test_33():
    var_0 = python_code_.textualusecase_BasicFlow()
    var_48 = python_code_.textualusecase_Step(
        name="textualusecase_Actor _textualusecase_FlowOfEvents__flowOfEvents _textualusecase_UseCase__useCase6 alternativeFlow",
        Step35=var_0,
        steps=var_0,
    )
    assert isinstance(var_48, python_code_.textualusecase_Step)


@pytest.mark.xfail(strict=True)
def test_34():
    var_11 = "textualusecase_Statementtextualusecase_Condition13"
    var_18 = python_code_.textualusecase_Include()
    var_19 = int
    var_20 = python_code_.textualusecase_Action(description=var_18, Action=var_11)
    assert isinstance(var_20, python_code_.textualusecase_Action)
    var_21 = {var_20, var_20, var_20, var_20, 1379.11}
    python_code_.textualusecase_Agent(name=var_19, agent=var_21, Agent=var_20)


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = python_code_.FlowOfEvents()
    var_20 = python_code_.textualusecase_Agent(name="textualusecase_Agent.Statement")
    assert isinstance(var_20, python_code_.textualusecase_Agent)
    var_21 = lambda *args, **kwargs: True
    var_22 = python_code_.textualusecase_AlternativeFlow()
    var_23 = python_code_.textualusecase_UseCase(
        name=var_0, description=var_0, UseCase47=var_21, textualusecase_UseCase=[]
    )
    assert isinstance(var_23, python_code_.textualusecase_UseCase)
    python_code_.textualusecase_Condition(
        expression=var_21,
        textualusecase_Condition20=var_22,
        textualusecase_Condition=var_23,
    )


def test_36():
    var_4 = python_code_.textualusecase_FlowOfEvents(
        name="a7T", FlowOfEvents=None, flowOfEvents=set()
    )
    assert isinstance(var_4, python_code_.textualusecase_FlowOfEvents)
    var_11 = python_code_.textualusecase_Step(name=var_4, Step25=var_4)
    assert isinstance(var_11, python_code_.textualusecase_Step)


def test_37():
    var_4 = python_code_.textualusecase_FlowOfEvents(
        name="textualusecase_UseCase-_textualusecase_Condition__textualusecase_Condition"
    )
    assert isinstance(var_4, python_code_.textualusecase_FlowOfEvents)
    var_12 = python_code_.Agent
    var_13 = python_code_.textualusecase_UseCase(
        name=var_12, description=var_4, UseCase23=var_12
    )
    assert isinstance(var_13, python_code_.textualusecase_UseCase)


@pytest.mark.xfail(strict=True)
def test_38():
    var_12 = bool
    var_19 = "Action_textualusecase_Step__branchingStep"
    var_20 = python_code_.textualusecase_Step(name=var_19, Step=[-1, False, "QMZ!"])
    assert isinstance(var_20, python_code_.textualusecase_Step)
    var_21 = "e1.(^9FzU^S$$@9e"
    var_22 = python_code_.textualusecase_Agent(name=var_21, Agent=var_12)
    assert isinstance(var_22, python_code_.textualusecase_Agent)
    python_code_.textualusecase_Action(description=var_19, actions=var_22)


@pytest.mark.xfail(strict=True)
def test_39():
    var_0 = python_code_.textualusecase_LoopStatement()
    var_1 = lambda *args, **kwargs: []
    var_2 = python_code_.textualusecase_AlternativeFlow()
    var_3 = python_code_.textualusecase_Step(name=var_1, Step=var_2, steps=False)
    assert isinstance(var_3, python_code_.textualusecase_Step)
    var_4 = "_textualusecase_Condition__textualusecase_Condition13"
    var_5 = python_code_.textualusecase_Statement()
    var_6 = python_code_.textualusecase_Step(
        name=var_4, Step=var_1, Step25=var_2, steps=var_5
    )
    var_7 = {var_3, var_3, var_6}
    var_8 = python_code_.textualusecase_FlowOfEvents(name=var_0, flowOfEvents=var_7)
    assert isinstance(var_8, python_code_.textualusecase_FlowOfEvents)
    python_code_.textualusecase_FlowOfEvents(
        name=var_4, FlowOfEvents=var_6, flowOfEvents=var_7
    )


@pytest.mark.xfail(strict=True)
def test_40():
    var_13 = python_code_.textualusecase_LoopStatement()
    var_14 = 'hS^\x0bu42s"c*Huu'
    var_15 = lambda *args, **kwargs: True
    var_16 = python_code_.textualusecase_FlowOfEvents(name=var_15)
    assert isinstance(var_16, python_code_.textualusecase_FlowOfEvents)
    var_17 = python_code_.textualusecase_Step(
        name=var_14,
        Step=None,
        steps30=None,
        Step25=None,
        branchingStep=set(),
        steps=None,
    )
    assert isinstance(var_17, python_code_.textualusecase_Step)
    var_18 = python_code_.textualusecase_Subject()
    var_23 = "/0nkG['O-y7@p400^+"
    var_24 = python_code_.textualusecase_Condition(
        expression=None, textualusecase_Condition13=var_18
    )
    python_code_.textualusecase_UseCase(
        name=b"\xd2>\x12\xe7D\xfa\xbb\xe6*",
        description=var_23,
        UseCase42=var_13,
        UseCase23={},
        textualusecase_UseCase12=var_24,
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_0 = python_code_.textualusecase_Actor()
    var_3 = "FlowOfEvents"
    var_4 = python_code_.textualusecase_Agent(
        name=var_3, agent="bKLtse\r<)3P\x0bno\nA#vh"
    )
    assert isinstance(var_4, python_code_.textualusecase_Agent)
    python_code_.textualusecase_Action(description=var_0, Action=var_4, actions=var_4)


@pytest.mark.xfail(strict=True)
def test_42():
    var_0 = python_code_.textualusecase_AlternativeFlow
    var_20 = "_textualusecase_UseCase__useCase17:_textualusecase_Condition__textualusecase_Condition33:textualusecase_Statement:alternativeFlow22"
    var_21 = python_code_.textualusecase_Agent(
        name=["]4zn_fA|W", "7jWj\r3<]{m;t_lA?", False], Agent=var_0
    )
    assert isinstance(var_21, python_code_.textualusecase_Agent)
    var_22 = python_code_.textualusecase_Action(
        description=var_20,
        Action=var_21,
        actions="textualusecase_Step-FlowOfEvents-_textualusecase_Condition__textualusecase_Condition33-_textualusecase_UseCase__UseCase",
    )
    assert isinstance(var_22, python_code_.textualusecase_Action)
    var_23 = python_code_.textualusecase_Step(name=var_20, steps30=var_0, steps=var_0)
    assert isinstance(var_23, python_code_.textualusecase_Step)
    python_code_.textualusecase_FlowOfEvents(name=var_21, FlowOfEvents=var_23)


@pytest.mark.xfail(strict=True)
def test_43():
    var_15 = python_code_.FlowOfEvents()
    var_21 = python_code_.textualusecase_Agent(
        name="^*L\n/S!yv\x0b%Bs[+<", agent={var_15, var_15}, Agent=var_15
    )
    assert isinstance(var_21, python_code_.textualusecase_Agent)
    var_23 = (
        "_textualusecase_Step__Step _textualusecase_Condition__textualusecase_Condition"
    )
    var_24 = python_code_.textualusecase_FlowOfEvents(name=var_23)
    assert isinstance(var_24, python_code_.textualusecase_FlowOfEvents)
    var_26 = python_code_.textualusecase_Step(name=")AI#^c@U.|*c6o,", steps30=None)
    assert isinstance(var_26, python_code_.textualusecase_Step)
    var_27 = "textualusecase_BasicFlow.textualusecase_FlowOfEvents.textualusecase_BasicFlow.textualusecase_UseCaseModel"
    var_28 = "Statement"
    var_29 = python_code_.textualusecase_Action(description=var_28, actions=())
    assert isinstance(var_29, python_code_.textualusecase_Action)
    python_code_.textualusecase_Agent(name=var_27, Agent=var_29)


@pytest.mark.xfail(strict=True)
def test_44():
    var_0 = python_code_.textualusecase_Subject()
    var_2 = python_code_.textualusecase_ConditionalStatement()
    var_4 = "\\Ew"
    var_5 = python_code_.textualusecase_Action(description=var_4)
    assert isinstance(var_5, python_code_.textualusecase_Action)
    var_6 = python_code_.textualusecase_Condition(
        expression=var_4, textualusecase_Condition=var_0
    )
    var_7 = "|"
    var_8 = python_code_.textualusecase_Include()
    var_9 = python_code_.textualusecase_AlternativeFlow()
    var_10 = python_code_.textualusecase_AlternativeFlow()
    var_11 = {var_9, var_9, var_9, var_10}
    var_12 = python_code_.textualusecase_UseCase(
        name=var_4, description=var_7, UseCase47=var_8, UseCase42=var_5, useCase=var_11
    )
    assert isinstance(var_12, python_code_.textualusecase_UseCase)
    var_13 = "GEJ<xFY^9~jFThFZ)"
    var_14 = python_code_.textualusecase_FlowOfEvents(name="?2))I+-ZFo")
    assert isinstance(var_14, python_code_.textualusecase_FlowOfEvents)
    var_15 = python_code_.textualusecase_Step(name=var_13, Step25=var_14)
    assert isinstance(var_15, python_code_.textualusecase_Step)
    var_19 = lambda *args, **kwargs: ".[WD\tn"
    var_20 = python_code_.textualusecase_Actor()
    var_21 = python_code_.textualusecase_BasicFlow()
    var_22 = python_code_.textualusecase_UseCaseModel()
    var_23 = python_code_.textualusecase_UseCase(
        name=var_7,
        description=var_19,
        UseCase42=var_20,
        useCase6=var_21,
        UseCase=var_22,
        useCase15=-1556.54,
    )
    assert isinstance(var_23, python_code_.textualusecase_UseCase)
    var_26 = "textualusecase_Action"
    python_code_.textualusecase_UseCase(
        name=-1767.71,
        description=var_26,
        useCase=var_11,
        textualusecase_UseCase=var_6,
        UseCase37=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = python_code_.textualusecase_Statement()
    var_1 = "_textualusecase_Agent__agent.Agent.UseCaseModel"
    var_2 = "E2,bFt[\ni.HDRV4"
    var_3 = python_code_.textualusecase_FlowOfEvents(name=var_2)
    assert isinstance(var_3, python_code_.textualusecase_FlowOfEvents)
    var_4 = python_code_.textualusecase_Step(name=var_1, Step25=var_3)
    assert isinstance(var_4, python_code_.textualusecase_Step)
    var_8 = '\r"^Ou&\n'
    var_9 = "9MB5KtlaREyx"
    var_10 = "_textualusecase_Step__Step"
    var_11 = python_code_.textualusecase_UseCase(
        name=var_9, description=var_10, UseCase47=[], textualusecase_UseCase12=var_0
    )
    assert isinstance(var_11, python_code_.textualusecase_UseCase)
    python_code_.textualusecase_Condition(
        expression=var_8, textualusecase_Condition13=var_11
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_2 = "t~M-G3Nqv}"
    var_3 = '"Xy\\{NJ2$}'
    var_4 = "MFj-3"
    var_5 = python_code_.textualusecase_Action(
        description=var_4, Action=complex(1830.3, 407.0)
    )
    assert isinstance(var_5, python_code_.textualusecase_Action)
    var_6 = python_code_.textualusecase_Agent(name=var_3)
    assert isinstance(var_6, python_code_.textualusecase_Agent)
    var_7 = python_code_.textualusecase_Action(description=var_3, Action=var_6)
    assert isinstance(var_7, python_code_.textualusecase_Action)
    var_8 = {var_5, var_7, var_5, var_5}
    python_code_.textualusecase_Agent(name=var_3, agent=var_8)
    python_code_.textualusecase_Action(description=var_2, actions=var_6)
