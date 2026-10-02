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
    date,
    datetime,
    stateMachineActions_Action,
    stateMachineActions_Assignment,
    stateMachineActions_EXPRESSION,
    stateMachineActions_EventAction,
    stateMachineActions_Model,
    stateMachineActions_Parameters,
    stateMachineActions_TERM,
    time,
)


def test_0():
    var_0 = "ixdb-Ot89wJm5B#Z"
    var_1 = -108
    python_code_.stateMachineActions_TERM(variable=var_0, constant=var_1)
    var_3 = python_code_.stateMachineActions_Parameters(
        param=var_0,
        stateMachineActions_Parameters19=903,
        stateMachineActions_Parameters17=set(),
    )
    assert var_3.stateMachineActions_Parameters19 == 903
    var_4 = python_code_.stateMachineActions_TERM(
        variable=var_1, constant=var_3, stateMachineActions_TERM11=var_1
    )
    assert isinstance(var_4, python_code_.stateMachineActions_TERM)


def test_1():
    var_1 = "]bU$_mJ[1dW>?\n<:*h"
    var_2 = repr
    var_3 = python_code_.stateMachineActions_EventAction(
        eventName=var_1, eventExtension=var_2, stateMachineActions_EventAction=var_2
    )
    assert isinstance(var_3, python_code_.stateMachineActions_EventAction)
    python_code_.stateMachineActions_Parameters(
        param=var_1, stateMachineActions_Parameters19=None
    )


def test_2():
    var_15 = python_code_.stateMachineActions_Parameters(
        param=True,
        stateMachineActions_Parameters17=False,
        stateMachineActions_Parameters=b"\x89F",
    )
    assert isinstance(var_15, python_code_.stateMachineActions_Parameters)


def test_3():
    python_code_.stateMachineActions_Parameters(
        param="P](SK$T`cY`QVcc?3", stateMachineActions_Parameters17=None
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_15 = python_code_.stateMachineActions_Assignment
    var_16 = python_code_.stateMachineActions_Parameters(
        param=(-2247.89,), stateMachineActions_Parameters17=var_15
    )
    var_17 = python_code_.stateMachineActions_EventAction(
        eventName=var_16,
        eventExtension=b"\xdam\x9f\x92(\x81b=\x9f\xa1'\xc8\xad",
        stateMachineActions_EventAction16={
            "&F\t": "%}ym\x0bA8R!I<Ye>",
            "stateMachineActions_Action4": -1,
            "_stateMachineActions_TERM__stateMachineActions_TERM14": -2400,
        },
    )
    assert isinstance(var_17, python_code_.stateMachineActions_EventAction)
    python_code_.stateMachineActions_Parameters(
        param=var_15, stateMachineActions_Parameters=var_17
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_5 = "bS^&"
    var_6 = tuple
    var_7 = python_code_.stateMachineActions_TERM(variable=var_6, constant=var_6)
    python_code_.stateMachineActions_EXPRESSION(
        operator=var_5,
        stateMachineActions_EXPRESSION8=var_5,
        stateMachineActions_EXPRESSION10=var_7,
        stateMachineActions_EXPRESSION13=var_5,
    )


def test_6():
    var_2 = 2973
    var_3 = python_code_.stateMachineActions_EXPRESSION(
        operator="1\\(5|,r~\tkj}\tjKm",
        stateMachineActions_EXPRESSION8=None,
        stateMachineActions_EXPRESSION13=var_2,
    )
    assert isinstance(var_3, python_code_.stateMachineActions_EXPRESSION)


@pytest.mark.xfail(strict=True)
def test_7():
    var_5 = "_stateMachineActions_Parameters__stateMachineActions_Parameters17stateMachineActions_Parameters17stateMachineActions_TERM11_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION10"
    var_6 = python_code_.stateMachineActions_EXPRESSION(
        operator=var_5,
        stateMachineActions_EXPRESSION={
            "-,\"d'ynz3j[8Y-\nb&TE": -30.14,
            "dEi_pH4B9[.^By": "_stateMachineActions_Assignment__stateMachineActions_Assignment:stateMachineActions_Action4",
        },
    )
    assert isinstance(var_6, python_code_.stateMachineActions_EXPRESSION)
    python_code_.stateMachineActions_Assignment(
        leftvar=var_5, stateMachineActions_Assignment6=var_6
    )


def test_8():
    python_code_.stateMachineActions_Assignment(leftvar="&b}@G\x0c!bj")
    var_14 = python_code_.stateMachineActions_EXPRESSION(
        operator=b"\xebF\xd7\xf7\xa3\x1d@\xa7 \xc9Z\x89",
        stateMachineActions_EXPRESSION=True,
    )
    assert isinstance(var_14, python_code_.stateMachineActions_EXPRESSION)


@pytest.mark.xfail(strict=True)
def test_9():
    var_12 = python_code_.stateMachineActions_TERM(
        variable="stateMachineActions_EXPRESSION8",
        constant=-1240,
        stateMachineActions_TERM11=None,
    )
    python_code_.stateMachineActions_EXPRESSION(
        operator="stateMachineActions_EXPRESSION10._stateMachineActions_Assignment__stateMachineActions_Assignment6",
        stateMachineActions_EXPRESSION13=var_12,
        stateMachineActions_EXPRESSION=None,
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_1 = ""
    var_2 = python_code_.stateMachineActions_TERM(
        variable="stateMachineActions_Assignment",
        constant=1519,
        stateMachineActions_TERM14=var_1,
    )
    assert isinstance(var_2, python_code_.stateMachineActions_TERM)
    var_3 = "stateMachineActions_Parameters"
    var_4 = python_code_.stateMachineActions_Assignment(
        leftvar=var_3,
        stateMachineActions_Assignment=var_2,
        stateMachineActions_Assignment6=[
            "stateMachineActions_Assignment6,stateMachineActions_EXPRESSION13,_stateMachineActions_Assignment__stateMachineActions_Assignment6,stateMachineActions_TERM14",
            -910,
        ],
    )
    assert isinstance(var_4, python_code_.stateMachineActions_Assignment)
    python_code_.stateMachineActions_EXPRESSION(
        operator=var_1,
        stateMachineActions_EXPRESSION8=[],
        stateMachineActions_EXPRESSION=var_4,
    )


def test_11():
    python_code_.stateMachineActions_EventAction(
        eventName="Igz8", eventExtension="|$7\\b"
    )


def test_12():
    var_15 = "stateMacyhineActions_EXPRESSION-_stateMachineActions_Parameters__stateMachineActions_Parameters19-stateMachineActions_EXPRESSION8-stateMachineActions_TERM"
    var_16 = python_code_.stateMachineActions_EventAction(
        eventName=var_15,
        eventExtension="0",
        stateMachineActions_EventAction=var_15,
        stateMachineActions_EventAction16=var_15,
    )
    assert isinstance(var_16, python_code_.stateMachineActions_EventAction)


def test_13():
    var_0 = float
    var_1 = python_code_.stateMachineActions_EventAction(
        eventName="stateMachineActions_EXPRESSION-_stateMachineActions_EventAction__stateMachineActions_EventAction16-_stateMachineActions_Assignment__stateMachineActions_Assignment6",
        eventExtension="~H=0I|ExP(|knk",
        stateMachineActions_EventAction16=var_0,
    )
    assert isinstance(var_1, python_code_.stateMachineActions_EventAction)


def test_14():
    python_code_.stateMachineActions_Assignment(
        leftvar="stateMachineActions_Parameters17", stateMachineActions_Assignment=None
    )


def test_15():
    var_15 = object
    var_16 = python_code_.stateMachineActions_Assignment(
        leftvar=var_15,
        stateMachineActions_Assignment=var_15,
        stateMachineActions_Assignment6=var_15,
    )
    assert isinstance(var_16, python_code_.stateMachineActions_Assignment)


def test_16():
    python_code_.stateMachineActions_TERM(variable="8{Z", constant=1198)


def test_17():
    var_1 = ""
    var_2 = python_code_.stateMachineActions_TERM(
        variable="stateMachineActions_Assignment",
        constant=1519,
        stateMachineActions_TERM14=var_1,
    )
    assert isinstance(var_2, python_code_.stateMachineActions_TERM)


def test_18():
    var_15 = "stateMacyhineActions_EXPRESSION-_stateMachineActions_Parameters__stateMachineActions_Parameters19-stateMachineActions_EmPRESSIO8-stateMachineActions_TERM"
    var_17 = python_code_.stateMachineActions_EventAction(
        eventName="stateMachineActions_Action stateMachineActions_Parameters17",
        eventExtension=var_15,
        stateMachineActions_EventAction=var_15,
        stateMachineActions_EventAction16=None,
    )
    assert isinstance(var_17, python_code_.stateMachineActions_EventAction)
    var_18 = -1465
    var_19 = python_code_.stateMachineActions_TERM(
        variable=2499, constant=var_18, stateMachineActions_TERM11=var_15
    )
    assert isinstance(var_19, python_code_.stateMachineActions_TERM)


@pytest.mark.xfail(strict=True)
def test_19():
    var_10 = python_code_.stateMachineActions_Assignment(
        leftvar="stateMachineActions_Parameters19 stateMachineActions_EXPRESSION13 _stateMachineActions_TERM__stateMachineActions_TERM14"
    )
    var_17 = python_code_.stateMachineActions_Action()
    var_18 = ""
    var_19 = python_code_.stateMachineActions_Parameters(
        param=False, stateMachineActions_Parameters=var_18
    )
    assert isinstance(var_19, python_code_.stateMachineActions_Parameters)
    python_code_.stateMachineActions_Parameters(
        param=var_18,
        stateMachineActions_Parameters19={},
        stateMachineActions_Parameters17=var_19,
    )
    assert isinstance(
        var_19.stateMachineActions_Parameters19,
        python_code_.stateMachineActions_Parameters,
    )
    python_code_.stateMachineActions_EventAction(
        eventName=-782,
        eventExtension=var_10,
        stateMachineActions_EventAction=var_17,
        stateMachineActions_EventAction16=var_19,
    )


@pytest.mark.xfail(strict=True)
def test_20():
    var_4 = python_code_.stateMachineActions_EventAction(
        eventName="stateMachineActions_Parameters19.stateMachineActions_Parameters17._stateMachineActions_TERM__stateMachineActions_TERM",
        eventExtension=":q",
    )
    var_5 = python_code_.stateMachineActions_Action()
    var_6 = python_code_.stateMachineActions_Assignment(
        leftvar=var_4,
        stateMachineActions_Assignment=var_5,
        stateMachineActions_Assignment6="4!>o[H-.Y\t-Ngt0",
    )
    assert isinstance(var_6, python_code_.stateMachineActions_Assignment)
    var_7 = python_code_.stateMachineActions_Parameters
    python_code_.stateMachineActions_TERM(
        variable=var_7, constant=var_7, stateMachineActions_TERM11=var_7
    )
    var_9 = "f^D!f.'"
    var_10 = python_code_.stateMachineActions_EXPRESSION(
        operator=var_9,
        stateMachineActions_EXPRESSION8={},
        stateMachineActions_EXPRESSION10=var_7,
    )
    assert isinstance(var_10, python_code_.stateMachineActions_EXPRESSION)
    python_code_.stateMachineActions_TERM(
        variable=var_9, constant=var_5, stateMachineActions_TERM11=var_10
    )
    assert isinstance(
        var_10.stateMachineActions_EXPRESSION10, python_code_.stateMachineActions_TERM
    )


def test_21():
    var_7 = "stateMachineActions_Action2:stateMachineActions_Assignment:stateMachineActions_TEfRM:stateMachineActions_EventAction"
    var_8 = python_code_.stateMachineActions_Assignment
    var_9 = python_code_.stateMachineActions_Parameters(
        param=(-2247.89,), stateMachineActions_Parameters17=var_8
    )
    python_code_.stateMachineActions_Parameters(
        param=var_7,
        stateMachineActions_Parameters19=var_9,
        stateMachineActions_Parameters=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_22():
    var_15 = "MY!(-h6r7%/\\\tL"
    var_16 = python_code_.stateMachineActions_EventAction(
        eventName=var_15, eventExtension=var_15
    )
    var_18 = "stateMachineActions_EventAction16-stateMachineActions_Parameters"
    var_19 = python_code_.stateMachineActions_TERM(
        variable=var_15,
        constant=-27.7,
        stateMachineActions_TERM=var_15,
        stateMachineActions_TERM11=False,
        stateMachineActions_TERM14=var_16,
    )
    assert isinstance(var_19, python_code_.stateMachineActions_TERM)
    python_code_.stateMachineActions_EXPRESSION(
        operator=var_18,
        stateMachineActions_EXPRESSION8=var_15,
        stateMachineActions_EXPRESSION10={
            "BLN84": -1064.48,
            "96^MS\\~": -2212,
            ",": 2311.54,
        },
        stateMachineActions_EXPRESSION13=var_19,
        stateMachineActions_EXPRESSION="B_Ke4eR)kj4&5~X",
    )


@pytest.mark.xfail(strict=True)
def test_23():
    var_1 = python_code_.stateMachineActions_TERM(variable="8{Z", constant=1198)
    python_code_.stateMachineActions_EXPRESSION(
        operator="9Z0Bl!\x0ce^WswM",
        stateMachineActions_EXPRESSION8=var_1,
        stateMachineActions_EXPRESSION10=None,
    )


@pytest.mark.xfail(strict=True)
def test_24():
    var_0 = python_code_.stateMachineActions_Parameters
    var_1 = python_code_.stateMachineActions_TERM(
        variable="_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION8",
        constant=-1,
        stateMachineActions_TERM=var_0,
    )
    python_code_.stateMachineActions_EXPRESSION(
        operator="9Z0Bl!\x0ce^WswM",
        stateMachineActions_EXPRESSION8=var_1,
        stateMachineActions_EXPRESSION10=None,
    )


@pytest.mark.xfail(strict=True)
def test_25():
    var_0 = python_code_.stateMachineActions_Action()
    var_1 = "]bU$_mJ[1dW>?\n<:*"
    var_3 = python_code_.stateMachineActions_EventAction(
        eventName="stateMachineActions_TERM stateMachineActions_Action _stateMachineActions_TERM__stateMachineActions_TERM14 _stateMachineActions_EventAction__stateMachineActions_EventAction16",
        eventExtension=var_1,
        stateMachineActions_EventAction=var_0,
    )
    python_code_.stateMachineActions_Parameters(
        param=var_1, stateMachineActions_Parameters19=None
    )
    var_6 = "_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION10"
    var_8 = python_code_.stateMachineActions_EXPRESSION(
        operator=var_6,
        stateMachineActions_EXPRESSION10={
            -189,
            "_stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION _stateMachineActions_EXPRESSION__stateMachineActions_EXPRESSION13 stateMachineActions_Action2",
        },
    )
    assert isinstance(var_8, python_code_.stateMachineActions_EXPRESSION)
    python_code_.stateMachineActions_TERM(
        variable=var_0, constant=var_3, stateMachineActions_TERM11=var_8
    )
    assert isinstance(
        var_8.stateMachineActions_EXPRESSION10, python_code_.stateMachineActions_TERM
    )


@pytest.mark.xfail(strict=True)
def test_26():
    var_1 = "stateMachineActions_Action2"
    var_2 = -969
    var_3 = python_code_.stateMachineActions_EXPRESSION(
        operator={
            "uCSo9M~T\t*`T{bG": 2724.53,
            '\r"C~CJQzgoFBkSO': True,
            "*BIK<38mZyNu/3;": "stateMachineActions_TERM14,stateMachineActions_TERM14",
        },
        stateMachineActions_EXPRESSION8=complex(-4459.3, -170.99952),
    )
    assert isinstance(var_3, python_code_.stateMachineActions_EXPRESSION)
    python_code_.stateMachineActions_TERM(
        variable=var_1,
        constant=var_2,
        stateMachineActions_TERM=var_3,
        stateMachineActions_TERM11=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = "_stateMachineActions_EventAction__stateMachineActions_EventAction"
    var_1 = 3
    var_2 = python_code_.stateMachineActions_TERM(
        variable=var_0,
        constant=var_1,
        stateMachineActions_TERM11={
            True,
            "_stateMachineActions_Parameters__stateMachineActions_Parameters19",
            0,
        },
    )
    assert isinstance(var_2, python_code_.stateMachineActions_TERM)
    var_3 = python_code_.stateMachineActions_Assignment(
        leftvar=var_0, stateMachineActions_Assignment=var_0
    )
    assert isinstance(var_3, python_code_.stateMachineActions_Assignment)
    python_code_.stateMachineActions_EXPRESSION(
        operator="\nya,$Bi(Q",
        stateMachineActions_EXPRESSION8={},
        stateMachineActions_EXPRESSION10=var_2,
        stateMachineActions_EXPRESSION=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_28():
    var_17 = python_code_.stateMachineActions_Assignment(leftvar="a@i<UH*GsswT(YYghY'")
    var_18 = python_code_.stateMachineActions_Model()
    var_19 = "stateMachineActions_Action.stateMachineActions_TERM14"
    var_20 = python_code_.stateMachineActions_EventAction
    var_21 = python_code_.stateMachineActions_EXPRESSION(
        operator=var_18,
        stateMachineActions_EXPRESSION13=var_20,
        stateMachineActions_EXPRESSION=var_20,
    )
    python_code_.stateMachineActions_TERM(
        variable=var_19,
        constant=var_17,
        stateMachineActions_TERM=set(),
        stateMachineActions_TERM11="R,",
        stateMachineActions_TERM14=var_21,
    )
