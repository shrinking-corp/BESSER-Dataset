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
    Declaration,
    State,
    abstractmethod,
    date,
    datetime,
    statemachine_Action,
    statemachine_Declaration,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_NormalState,
    statemachine_State,
    statemachine_StateMachine,
    statemachine_StateMachineVariable,
    statemachine_Transition,
    time,
)


def test_0():
    python_code_.statemachine_Action(
        actionLabel="_statemachine_State__statemachine_State7",
        actionStatement="statemachine_Transition",
    )


def test_1():
    var_53 = python_code_.statemachine_Action(
        actionLabel='SYn02"Ic\x0c7B8',
        actionStatement=complex(1296.8, -1843.364216),
        statemachine_Action=("J", 2399),
    )
    assert isinstance(var_53, python_code_.statemachine_Action)


def test_2():
    var_20 = python_code_.statemachine_State(
        label="i,#M\rtM`cno^\\#Y",
        id=1,
        statemachine_State=None,
        statemachine_State7={
            "statemachine_State,statemachine_Transition,statemachine_StateMachineVariable,_statemachine_Action__statemachine_Action"
        },
        statemachine_State12=None,
    )
    assert isinstance(var_20, python_code_.statemachine_State)


def test_3():
    var_20 = python_code_.statemachine_State(
        label='5c&FKImbGohq"LVfIc', id=2182, statemachine_State9=None
    )
    assert isinstance(var_20, python_code_.statemachine_State)


def test_4():
    var_20 = python_code_.statemachine_State(
        label="_statemachine_StateMachine__statemachine_StateMachine2",
        id=2392,
        statemachine_State7=set(),
        statemachine_State10=set(),
    )
    assert isinstance(var_20, python_code_.statemachine_State)


def test_5():
    var_20 = python_code_.statemachine_State(
        label="statemachine_Declarationstatemachine_State6",
        id=-1019,
        statemachine_State9=None,
    )
    assert isinstance(var_20, python_code_.statemachine_State)
    var_44 = python_code_.statemachine_State(
        label="4z)QnF/I(",
        id=-1,
        statemachine_State9=var_20,
        statemachine_State12=var_20,
    )
    assert isinstance(var_44, python_code_.statemachine_State)


@pytest.mark.xfail(strict=True)
def test_6():
    var_20 = python_code_.statemachine_State(
        label="statemachine_Declarationstatemachine_State6",
        id=-1019,
        statemachine_State9=None,
    )
    assert isinstance(var_20, python_code_.statemachine_State)
    var_44 = python_code_.statemachine_State(
        label="4z)QnF/I(",
        id=-1,
        statemachine_State9=var_20,
        statemachine_State12=var_20,
    )
    assert isinstance(var_44, python_code_.statemachine_State)
    var_48 = "3nm"
    var_49 = python_code_.statemachine_State(
        label="*Jj71", id=var_48, statemachine_State7=var_48
    )
    assert isinstance(var_49, python_code_.statemachine_State)
    python_code_.statemachine_Transition(
        label="",
        sourceLabel=var_48,
        targetLabel="",
        guardLabel=var_48,
        actionLabel="_statemachine_State__statemachine_State9 statemachine_Transition5",
        guardExpression=var_48,
        actionStatement="B",
        statemachine_Transition=var_44,
    )


def test_7():
    var_20 = python_code_.statemachine_State(
        label="L{w*DR}493zS>_R",
        id=1842,
        statemachine_State6=None,
        statemachine_State7={True, 2574, 1385},
        statemachine_State12=None,
    )
    assert isinstance(var_20, python_code_.statemachine_State)
    var_44 = python_code_.statemachine_State(
        label="statemachine_State6:statemachine_State6:statemachine_State",
        id=3436,
        statemachine_State=var_20,
        statemachine_State6=var_20,
        statemachine_State7={var_20},
        statemachine_State12=None,
        statemachine_State10=set(),
    )
    assert isinstance(var_44, python_code_.statemachine_State)


@pytest.mark.xfail(strict=True)
def test_8():
    var_20 = python_code_.statemachine_State(
        label="statemachine_State12",
        id=3357,
        statemachine_State6=None,
        statemachine_State9=None,
    )
    assert isinstance(var_20, python_code_.statemachine_State)
    python_code_.statemachine_Transition(
        label="statemachine_StateMachine2-_statemachine_StateMachine__statemachine_StateMachine-statemachine_State6-statemachine_State12",
        sourceLabel="statemachine_Declaration-statemachine_State12-statemachine_State",
        targetLabel="_statemachine_State__statemachine_State12-_statemachine_Transition__statemachine_Transition",
        guardLabel="_statemachine_StateMachine__statemachine_StateMachine",
        actionLabel="X+QYzG6\rqNeN",
        guardExpression="(*OFD>{gE)8W5\x0c{D_",
        actionStatement="statemachine_State10 _statemachine_StateMachine__statemachine_StateMachine2 _statemachine_StateMachine__statemachine_StateMachine2",
        statemachine_Transition5=var_20,
    )


def test_9():
    var_0 = "th-d4g\t["
    var_1 = "_statemachine_State]_statemachine_State6"
    var_2 = "x7"
    var_9 = python_code_.statemachine_Transition(
        label=var_0,
        sourceLabel=var_2,
        targetLabel=var_2,
        guardLabel="cMg",
        actionLabel="zEnr'-anH%CT@4",
        guardExpression=var_2,
        actionStatement=var_1,
        statemachine_Transition=var_0,
        statemachine_Transition5=var_0,
    )
    assert var_9.statemachine_Transition5 == "th-d4g\t["
    var_10 = python_code_.statemachine_InitialState
    var_11 = python_code_.statemachine_State(
        label=var_2, id=var_9, statemachine_State9=var_10, statemachine_State12=var_10
    )
    assert isinstance(var_11, python_code_.statemachine_State)


def test_10():
    python_code_.statemachine_StateMachineVariable(type="VW", name="0diG[\n]\x0bDFqQ8")


def test_11():
    var_48 = python_code_.statemachine_StateMachine(statemachine_StateMachine=set())
    assert isinstance(var_48, python_code_.statemachine_StateMachine)
    var_50 = "statemachine_State6-_statemachine_Transition__statemachine_Transition5-statemachine_State9-_statemachine_StateMachine__statemachine_StateMachine2"
    var_51 = python_code_.statemachine_StateMachineVariable(
        type="t-1g<\r?}gpd\x0bh", name=var_50, statemachine_StateMachineVariable=var_48
    )
    assert isinstance(var_51, python_code_.statemachine_StateMachineVariable)


def test_12():
    var_44 = python_code_.statemachine_StateMachine(
        statemachine_StateMachine2={577, 249.28, 1412.65}
    )
    assert isinstance(var_44, python_code_.statemachine_StateMachine)


def test_13():
    var_10 = python_code_.statemachine_StateMachine()
    assert isinstance(var_10, python_code_.statemachine_StateMachine)


def test_14():
    python_code_.statemachine_Declaration()


def test_15():
    var_20 = python_code_.statemachine_State(
        label='5c&FKImbGohq"LVfIc', id=2182, statemachine_State9=None
    )
    assert isinstance(var_20, python_code_.statemachine_State)
    var_20.printReachable()


def test_16():
    var_20 = python_code_.statemachine_State(
        label="=5Rn{L1,xUd",
        id=-1275,
        statemachine_State12=None,
        statemachine_State10=set(),
    )
    assert isinstance(var_20, python_code_.statemachine_State)
    var_44 = python_code_.statemachine_State(
        label="0>vfhkih&-gE",
        id=1404,
        statemachine_State9=var_20,
        statemachine_State12=None,
    )
    assert isinstance(var_44, python_code_.statemachine_State)
    var_45 = var_20.printReachable()
    var_46 = python_code_.statemachine_StateMachine(statemachine_StateMachine=var_45)
    assert isinstance(var_46, python_code_.statemachine_StateMachine)
    var_46.printReachable()


def test_17():
    var_44 = python_code_.statemachine_FinalState()
    var_45 = lambda *args, **kwargs: []
    var_46 = python_code_.statemachine_StateMachine()
    assert isinstance(var_46, python_code_.statemachine_StateMachine)
    var_47 = python_code_.statemachine_Declaration(statemachine_Declaration=var_46)
    assert isinstance(var_47, python_code_.statemachine_Declaration)
    var_48 = var_47.printReachable()
    var_49 = python_code_.statemachine_State(
        label=set(), id=var_44, statemachine_State9=var_45, statemachine_State10=var_48
    )
    assert isinstance(var_49, python_code_.statemachine_State)


@pytest.mark.xfail(strict=True)
def test_18():
    var_2 = "x7"
    var_4 = python_code_.statemachine_InitialState
    var_10 = python_code_.statemachine_StateMachine()
    assert isinstance(var_10, python_code_.statemachine_StateMachine)
    var_11 = python_code_.statemachine_Declaration(statemachine_Declaration=var_10)
    assert isinstance(var_11, python_code_.statemachine_Declaration)
    var_11.printReachable()
    var_13 = "2"
    var_14 = python_code_.statemachine_Transition(
        label=var_4,
        sourceLabel=var_10,
        targetLabel=var_2,
        guardLabel=var_13,
        actionLabel=var_4,
        guardExpression=var_4,
        actionStatement=var_4,
        statemachine_Transition=[
            "HQ\r)\n)asug\\f",
            "_statemachine_State__statemachine_State12 statemachine_StateMachine2",
        ],
    )
    assert isinstance(var_14, python_code_.statemachine_Transition)
    var_15 = 3
    var_16 = var_10.printReachable()
    python_code_.statemachine_State(
        label=var_13,
        id=var_15,
        statemachine_State=var_14,
        statemachine_State7=var_11,
        statemachine_State10=var_16,
    )


def test_19():
    var_2 = 3082
    var_3 = python_code_.statemachine_State(
        label=None, id=var_2, statemachine_State9=var_2
    )
    assert isinstance(var_3, python_code_.statemachine_State)
    var_6 = -4893
    var_7 = python_code_.statemachine_State(
        label=[],
        id=var_6,
        statemachine_State=["_statemachine_State__statemachine_State9", True],
        statemachine_State6=var_2,
        statemachine_State9=var_3,
    )
    assert isinstance(var_7, python_code_.statemachine_State)
    var_8 = var_7.printReachable()
    var_9 = python_code_.statemachine_StateMachine(
        statemachine_StateMachine2=b"~", statemachine_StateMachine=var_8
    )
    assert isinstance(var_9, python_code_.statemachine_StateMachine)
    var_11 = python_code_.statemachine_Declaration()
    var_12 = python_code_.statemachine_StateMachineVariable(
        type=-3145.44, name=True, statemachine_StateMachineVariable=var_9
    )
    assert isinstance(var_12, python_code_.statemachine_StateMachineVariable)
    var_11.printReachable()
    var_9.printReachable()


def test_20():
    var_44 = python_code_.statemachine_StateMachine(statemachine_StateMachine={False})
    assert isinstance(var_44, python_code_.statemachine_StateMachine)


def test_21():
    var_49 = python_code_.statemachine_Declaration(
        statemachine_Declaration="statemachine_NormalState:statemachine_NormalState:_statemachine_State__statemachine_State12:_statemachine_Action__statemachine_Action"
    )
    assert isinstance(var_49, python_code_.statemachine_Declaration)


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = "NonQ&Gj:"
    var_1 = python_code_.statemachine_Action(
        actionLabel=b"\xefb\x8af\x1cY\x02\x8f", actionStatement=var_0
    )
    var_2 = lambda *args, **kwargs: -4102
    var_3 = python_code_.statemachine_Transition(
        label=var_0,
        sourceLabel=True,
        targetLabel=b"@\xf2\xc4\xbd\xb6e\x99\xa4\x02\xee\xa7",
        guardLabel=var_1,
        actionLabel=var_0,
        guardExpression=var_2,
        actionStatement=var_0,
        statemachine_Transition5=b"hL\xf3\r9\x1b $\x8d3\xd2\xfey}?\xb1k",
    )
    assert isinstance(var_3, python_code_.statemachine_Transition)
    var_4 = "statemachine_State12"
    python_code_.statemachine_State(label=var_4, id={}, statemachine_State6=var_3)
    assert isinstance(var_3.statemachine_Transition5, python_code_.statemachine_State)


def test_23():
    var_53 = python_code_.statemachine_Declaration()
    var_54 = python_code_.statemachine_StateMachine(
        statemachine_StateMachine2=set(),
        statemachine_StateMachine={-2656, var_53, var_53},
    )
    assert isinstance(var_54, python_code_.statemachine_StateMachine)


def test_24():
    var_2 = 3066
    var_3 = python_code_.statemachine_State(
        label='N"0llgF{AI:=zsLb3',
        id=var_2,
        statemachine_State6=None,
        statemachine_State12=None,
    )
    assert isinstance(var_3, python_code_.statemachine_State)
    var_3.printReachable()
    var_6 = -4902
    var_7 = python_code_.statemachine_State(
        label=[],
        id=var_6,
        statemachine_State=["_statemachine_State__statemachine_State9", True],
        statemachine_State6=var_2,
        statemachine_State9=var_3,
    )
    assert isinstance(var_7, python_code_.statemachine_State)
    var_9 = python_code_.statemachine_StateMachine()
    assert isinstance(var_9, python_code_.statemachine_StateMachine)
    python_code_.statemachine_Declaration()
    var_43 = python_code_.statemachine_FinalState()
    var_50 = -3451
    var_51 = python_code_.statemachine_State(
        label=None, id=var_50, statemachine_State7={"=2T\\//:vSU/,R": '92s<zz"y1<^m'}
    )
    assert isinstance(var_51, python_code_.statemachine_State)
    var_52 = python_code_.statemachine_NormalState
    var_53 = "_statemachine_Transition__statemachine_Transition"
    python_code_.statemachine_Action(actionLabel=var_52, actionStatement=var_53)
    var_56 = "statemachine_Declaration-_statemachine_State__statemachine_State7-_statemachine_State__statemachine_State12-_statemachine_StateMachine__statemachine_StateMachine"
    python_code_.statemachine_StateMachineVariable(
        type=var_52, name=var_56, statemachine_StateMachineVariable=var_43
    )


@pytest.mark.xfail(strict=True)
def test_25():
    python_code_.statemachine_Action(actionLabel="~^.\t", actionStatement="-'Bb`vty")
    var_51 = python_code_.statemachine_StateMachine()
    assert isinstance(var_51, python_code_.statemachine_StateMachine)
    var_52 = python_code_.statemachine_Declaration()
    var_53 = "statemachine_StateMachine"
    var_54 = int
    var_55 = "statemachine_StateMachineVariable-_statemachine_Action__statemachine_Action-statemachine_NormalState-statemachine_Transition5"
    var_56 = python_code_.statemachine_State(
        label=var_55, id=var_51, statemachine_State10=b"$iT\xaeW\x13d#\x14\xbd\xbc\xc1>"
    )
    assert isinstance(var_56, python_code_.statemachine_State)
    var_57 = python_code_.statemachine_State(
        label=var_54,
        id=set(),
        statemachine_State6=var_54,
        statemachine_State9=var_56,
        statemachine_State12=var_56,
    )
    assert isinstance(var_57, python_code_.statemachine_State)
    python_code_.statemachine_Transition(
        label=278,
        sourceLabel=var_53,
        targetLabel=var_53,
        guardLabel=var_51,
        actionLabel=var_53,
        guardExpression=var_53,
        actionStatement=var_52,
        statemachine_Transition=var_56,
        statemachine_Transition5={},
    )


def test_26():
    python_code_.statemachine_Action(
        actionLabel="_statemachine_State__statemachine_State7",
        actionStatement="statemachine_Transition",
    )
    var_51 = -3785
    var_52 = "[y`I(\x0bK}mCF1\n"
    var_53 = -2896
    var_54 = python_code_.statemachine_StateMachineVariable
    var_55 = python_code_.statemachine_State(
        label=var_52,
        id=var_53,
        statemachine_State6=var_51,
        statemachine_State7=b">=p\x0c4GZ&\xca\xd7\xf1\xc7\xfc\xe3A",
        statemachine_State12=var_54,
    )
    assert isinstance(var_55, python_code_.statemachine_State)
    var_56 = python_code_.statemachine_State(
        label="q\x0c6Si+Z", id=var_51, statemachine_State9=var_55
    )
    assert isinstance(var_56, python_code_.statemachine_State)
    var_55.printReachable()


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = python_code_.statemachine_Declaration()
    var_0.printReachable()
    var_2 = python_code_.Declaration()
    var_3 = "_statemachine_StateMachine__statemachine_StateMachine2,_statemachine_StateMachine__statemachine_StateMachine2,_statemachine_State__statemachine_State9,_statemachine_State__statemachine_State10"
    var_4 = python_code_.statemachine_State(
        label=var_3, id=-941, statemachine_State=False, statemachine_State9=()
    )
    assert isinstance(var_4, python_code_.statemachine_State)
    var_5 = sorted
    var_6 = "_statemachine_StateMachine__statemachine_StateMachine _statemachine_State__statemachine_State statemachine_State statemachine_StateMachine2"
    python_code_.statemachine_Transition(
        label=var_3,
        sourceLabel=var_2,
        targetLabel=var_3,
        guardLabel=set(),
        actionLabel=var_3,
        guardExpression=var_5,
        actionStatement=var_6,
        statemachine_Transition=var_4,
    )


def test_28():
    var_20 = python_code_.statemachine_State(
        label="n'\t_U",
        id=2,
        statemachine_State=None,
        statemachine_State7={4185, -2321.11},
    )
    assert isinstance(var_20, python_code_.statemachine_State)
    var_54 = python_code_.statemachine_State(
        label="7(DKc\\.,",
        id=-1,
        statemachine_State9=None,
        statemachine_State12=var_20,
        statemachine_State10={var_20, 3},
    )
    assert isinstance(var_54, python_code_.statemachine_State)
    var_20.printReachable()


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = python_code_.statemachine_StateMachine(
        statemachine_StateMachine2=b'\xb0\xd9"S\xaf\x04\xee`\x1f\x1cx\xeb\xe6\x92Y\xa8a\x1d\x01',
        statemachine_StateMachine={},
    )
    assert isinstance(var_0, python_code_.statemachine_StateMachine)
    var_1 = python_code_.statemachine_Declaration(statemachine_Declaration=var_0)
    assert isinstance(var_1, python_code_.statemachine_Declaration)
    var_1.printReachable()
    var_0.printReachable()
    var_6 = "_statemachine_Transition__statemachine_Transition5 _statemachine_State__statemachine_State _statemachine_State__statemachine_State6"
    var_7 = "statemachine_StateMachineVariable-statemachine_StateMachine-_statemachine_StateMachine__statemachine_StateMachine-_statemachine_State__statemachine_State10"
    var_8 = python_code_.statemachine_State(label=var_1, id=-2251.45)
    assert isinstance(var_8, python_code_.statemachine_State)
    python_code_.statemachine_Transition(
        label=var_6,
        sourceLabel=var_7,
        targetLabel=complex(-1463.573, -967.349),
        guardLabel=var_1,
        actionLabel=2470.87,
        guardExpression=var_7,
        actionStatement=var_1,
        statemachine_Transition=var_8,
        statemachine_Transition5=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = python_code_.statemachine_Declaration()
    var_1 = var_0.printReachable()
    var_2 = "i\x0cR4M&O\rb,mx"
    var_3 = python_code_.statemachine_StateMachineVariable(type=var_1, name=var_2)
    var_5 = -869
    var_6 = python_code_.statemachine_State(
        label=var_3, id=var_5, statemachine_State6=var_2, statemachine_State12=var_2
    )
    assert isinstance(var_6, python_code_.statemachine_State)
    var_7 = var_6.printReachable()
    var_9 = python_code_.statemachine_StateMachineVariable(
        type=var_7, name=var_3, statemachine_StateMachineVariable=()
    )
    assert isinstance(var_9, python_code_.statemachine_StateMachineVariable)
    var_10 = python_code_.statemachine_StateMachine()
    assert isinstance(var_10, python_code_.statemachine_StateMachine)
    var_10.printReachable()
    var_16 = "4e\t:/RZA,>"
    var_17 = "5COg9\r.a\\A"
    var_18 = "\r;Gz-8sD$x\x0b$"
    var_19 = "g'\r?/"
    python_code_.statemachine_Transition(
        label=var_16,
        sourceLabel=var_17,
        targetLabel=var_18,
        guardLabel=878.58,
        actionLabel=var_17,
        guardExpression=var_16,
        actionStatement=var_19,
        statemachine_Transition5=var_6,
    )
