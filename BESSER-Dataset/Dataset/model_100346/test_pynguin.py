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
    Enum,
    EventContext,
    State,
    TimedZone,
    Transition,
    abstractmethod,
    automaton_AtomicEventPattern,
    automaton_Automaton,
    automaton_EpsilonTransition,
    automaton_Event,
    automaton_EventPattern,
    automaton_EventToken,
    automaton_FinalState,
    automaton_Guard,
    automaton_HoldsFor,
    automaton_InitState,
    automaton_InternalModel,
    automaton_State,
    automaton_TimedZone,
    automaton_Transition,
    automaton_TrapState,
    automaton_TypedTransition,
    automaton_Within,
    date,
    datetime,
    time,
)


def test_0():
    var_3 = python_code_.automaton_TimedZone(time="EventToken")
    assert isinstance(var_3, python_code_.automaton_TimedZone)


def test_1():
    var_25 = python_code_.automaton_State(
        label="Gu-gI)x", preState=set(), inState=set(), outState=set(), State40=None
    )
    assert isinstance(var_25, python_code_.automaton_State)
    var_26 = python_code_.automaton_TimedZone(
        time=":s",
        automaton_TimedZone19=None,
        automaton_TimedZone=var_25,
        TimedZone=var_25,
    )
    assert isinstance(var_26, python_code_.automaton_TimedZone)


def test_2():
    var_23 = python_code_.automaton_TimedZone(time=True, automaton_TimedZone19=False)
    assert isinstance(var_23, python_code_.automaton_TimedZone)


@pytest.mark.xfail(strict=True)
def test_3():
    var_25 = python_code_.automaton_State(
        label="E\tB\x0cC%8/Y#WZ?6I6", State=None, State31=None
    )
    assert isinstance(var_25, python_code_.automaton_State)
    python_code_.automaton_TimedZone(
        time={"=$\x0b`J:,i!_u#D": False, "prw(k": False, "": True},
        TimedZone=var_25,
        TimedZone29=var_25,
        outStateOf=var_25,
    )


def test_4():
    var_23 = python_code_.automaton_TimedZone(
        time="-_hO", automaton_TimedZone19=None, TimedZone29=None
    )
    assert isinstance(var_23, python_code_.automaton_TimedZone)
    var_26 = python_code_.automaton_TimedZone(
        time=0, automaton_TimedZone19=var_23, automaton_TimedZone=var_23, outStateOf=[]
    )
    assert var_26.outStateOf == []


def test_5():
    var_25 = python_code_.automaton_State(
        label="automaton_Transition",
        State=None,
        State31=None,
        State33=None,
        automaton_State25=None,
        State38=None,
    )
    assert isinstance(var_25, python_code_.automaton_State)


def test_6():
    var_25 = python_code_.automaton_State(
        label="State40",
        State=None,
        postState=set(),
        preState={-4785, 3008.14, False},
        State38=None,
        State40=None,
    )
    assert isinstance(var_25, python_code_.automaton_State)


def test_7():
    var_25 = python_code_.automaton_State(
        label=".i%!L2ge",
        automaton_State=None,
        inState=set(),
        outState={False},
        State31=None,
        currentState={False, 1325, True},
        automaton_State25=None,
    )
    assert isinstance(var_25, python_code_.automaton_State)


def test_8():
    var_19 = {}
    var_28 = python_code_.automaton_State(
        label="7",
        postState={1431, "_automaton_TimedZone__automaton_TimedZone19"},
        State31=var_19,
        State40=var_19,
    )
    assert isinstance(var_28, python_code_.automaton_State)


def test_9():
    var_1 = python_code_.State()
    var_32 = python_code_.automaton_State(
        label="-fY",
        postState={var_1, var_1},
        preState=set(),
        automaton_State=var_1,
        inState=set(),
        outState={var_1, "&miE~\r", var_1},
        State33=var_1,
        State40=None,
    )
    assert isinstance(var_32, python_code_.automaton_State)


def test_10():
    var_26 = python_code_.automaton_InternalModel(
        context=[-1268.16], automaton_InternalModel=[984, 3252.7, -222]
    )
    assert isinstance(var_26, python_code_.automaton_InternalModel)


def test_11():
    python_code_.automaton_Within()


def test_12():
    var_25 = python_code_.automaton_State(
        label="]-@!^!'W:l1!\t_9c?J",
        postState=set(),
        outState={1629.2, True},
        automaton_State25=None,
    )
    assert isinstance(var_25, python_code_.automaton_State)


def test_13():
    var_19 = {}
    var_20 = python_code_.automaton_State(
        label="n)GgJ6'Y/",
        State=var_19,
        postState={"EventToken"},
        preState=set(),
        inState={-977.69},
        State33=None,
    )
    assert isinstance(var_20, python_code_.automaton_State)


def test_14():
    var_26 = python_code_.automaton_InternalModel(context="H\x0cNLnjg=\nF")
    assert isinstance(var_26, python_code_.automaton_InternalModel)


@pytest.mark.xfail(strict=True)
def test_15():
    var_25 = python_code_.automaton_State(
        label="Gu-gI)x", preState=set(), inState=set(), outState=set(), State40=None
    )
    assert isinstance(var_25, python_code_.automaton_State)
    python_code_.automaton_TimedZone(
        time="H0-m;",
        automaton_TimedZone19=None,
        automaton_TimedZone=None,
        inStateOf=var_25,
    )


def test_16():
    var_25 = python_code_.automaton_State(
        label="x-i})'KyR)5e\n",
        postState={True, '"dLXy3<s\\4{e', False},
        automaton_State=None,
        inState=set(),
        State31=None,
        State33=None,
        automaton_State25=None,
        State40=None,
    )
    assert isinstance(var_25, python_code_.automaton_State)
    var_30 = python_code_.automaton_TimedZone(
        time="V&!m1tMws$~8;", automaton_TimedZone=var_25
    )
    assert isinstance(var_30, python_code_.automaton_TimedZone)
    var_31 = "U:"
    var_32 = python_code_.automaton_Automaton()
    var_33 = python_code_.automaton_TimedZone(
        time=var_30, TimedZone=var_25, TimedZone29={False, 1482}, inStateOf=var_31
    )
    assert isinstance(var_33, python_code_.automaton_TimedZone)
    var_34 = {var_30, var_33}
    var_35 = python_code_.automaton_Event()
    var_36 = python_code_.automaton_State(
        label=var_31,
        automaton_State=var_32,
        inState=var_34,
        outState=b"l\xc3\x96\t\xa5f\xdb\x00\xf8\x00w\x00\xe8\xc9\xaeD\xe3_\x8f",
        automaton_State25=var_35,
    )
    assert isinstance(var_36, python_code_.automaton_State)


def test_17():
    var_25 = python_code_.automaton_State(
        label="eventTokens", State=None, postState={True, -187}, State40=None
    )
    assert isinstance(var_25, python_code_.automaton_State)
    var_28 = python_code_.automaton_TimedZone(time="b32/ZvtYG=R|j7", TimedZone29=var_25)
    assert isinstance(var_28, python_code_.automaton_TimedZone)


def test_18():
    var_1 = python_code_.automaton_Transition()
    var_8 = python_code_.automaton_State(
        label='XJ&x,P:&?GmTSs(v+"6',
        State=None,
        inState={-2670, var_1, var_1},
        State31=None,
        currentState={2},
        automaton_State25=var_1,
    )
    assert isinstance(var_8, python_code_.automaton_State)


def test_19():
    var_1 = python_code_.State()
    var_32 = python_code_.automaton_State(
        label="\nH?}7*]@|w$Z_s",
        postState={var_1},
        automaton_State=var_1,
        outState={var_1, 0},
        State31=None,
        State38=var_1,
        State40=None,
    )
    assert isinstance(var_32, python_code_.automaton_State)


def test_20():
    var_1 = python_code_.State()
    var_34 = python_code_.automaton_InternalModel(
        context=var_1, automaton_InternalModel2=b"\x7f2\xe0\x04/\xc2\xa7\x8f"
    )
    assert isinstance(var_34, python_code_.automaton_InternalModel)


def test_21():
    var_32 = lambda *args, **kwargs: "-+l=EMee) `2E~M"
    var_33 = "{;>"
    var_34 = python_code_.automaton_TimedZone(time=var_33, TimedZone=var_32)
    assert isinstance(var_34, python_code_.automaton_TimedZone)
    var_35 = {var_34}
    var_36 = python_code_.automaton_State(
        label="_automaton_InternalModel__automaton_InternalModel2",
        postState=var_35,
        inState=var_35,
        State31=None,
        State33=var_35,
        currentState=set(),
        automaton_State25=None,
    )
    assert isinstance(var_36, python_code_.automaton_State)


def test_22():
    var_23 = python_code_.automaton_TimedZone(
        time="\nf,q,Y0}j\tM9fblg|%+", TimedZone29=None
    )
    assert isinstance(var_23, python_code_.automaton_TimedZone)
    python_code_.automaton_TimedZone(
        time="automaton_EventToken", automaton_TimedZone=var_23, TimedZone=var_23
    )


def test_23():
    var_28 = python_code_.automaton_Transition()
    var_29 = python_code_.Transition()
    var_31 = "_automaton_InternalModel__automaton_InternalModel2"
    var_32 = python_code_.automaton_TimedZone(
        time=var_31, TimedZone=var_29, inStateOf=var_28
    )
    assert isinstance(var_32, python_code_.automaton_TimedZone)
    var_37 = {var_32, -1022}
    var_38 = [var_32]
    var_39 = python_code_.automaton_State(
        label=var_31,
        State=complex(-3573.2023, 898.6304),
        inState=var_37,
        State33=var_28,
        currentState=var_38,
        automaton_State25=set(),
    )
    assert isinstance(var_39, python_code_.automaton_State)


def test_24():
    var_25 = python_code_.automaton_State(
        label="_automaton_TimedZone__automaton_TimedZone",
        postState={"PE?z#&", "Z1v'4$SWGA~.A}y"},
        preState={True},
    )
    assert isinstance(var_25, python_code_.automaton_State)
    var_33 = python_code_.automaton_TimedZone(
        time=" &^U`[T60,#", TimedZone29=var_25, inStateOf=None
    )
    assert isinstance(var_33, python_code_.automaton_TimedZone)
    var_34 = {var_33}
    var_35 = python_code_.Transition()
    python_code_.automaton_State(
        label=["L}U ", False], State=var_33, outState=var_34, State40=var_35
    )


@pytest.mark.xfail(strict=True)
def test_25():
    var_7 = "_automaton_State__State38"
    var_8 = "7(}znTB"
    var_9 = python_code_.automaton_Event()
    var_10 = python_code_.automaton_Transition()
    var_11 = python_code_.automaton_Transition()
    var_12 = {var_10, var_11}
    var_13 = python_code_.automaton_State(
        label=var_8,
        postState=var_12,
        preState=var_12,
        inState=None,
        State31=var_10,
        State38="gu]U';h \tn.xC+PI%]",
    )
    assert isinstance(var_13, python_code_.automaton_State)
    var_14 = lambda *args, **kwargs: -580
    var_15 = python_code_.automaton_TimedZone(
        time=var_7, TimedZone=var_13, inStateOf=var_14
    )
    assert isinstance(var_15, python_code_.automaton_TimedZone)
    python_code_.automaton_State(
        label=var_8,
        State=var_7,
        postState=var_7,
        automaton_State=var_8,
        outState=var_7,
        automaton_State25=var_9,
        State38=var_15,
    )


def test_26():
    var_7 = python_code_.automaton_Automaton()
    var_8 = python_code_.EventContext
    var_9 = python_code_.automaton_State(
        label=var_7,
        State=var_8,
        preState={"_automaton_State__preState": -87},
        outState=var_8,
        automaton_State25=complex(432.7, -262.2),
    )
    assert isinstance(var_9, python_code_.automaton_State)
    var_10 = python_code_.automaton_TimedZone(
        time=-1324.15, automaton_TimedZone=var_7, TimedZone=var_8, TimedZone29=var_9
    )
    assert isinstance(var_10, python_code_.automaton_TimedZone)


@pytest.mark.xfail(strict=True)
def test_27():
    var_7 = python_code_.automaton_EpsilonTransition()
    var_11 = "$)D3!@IU8gXm-o8"
    var_13 = python_code_.automaton_Transition()
    var_14 = {var_13, var_13}
    var_15 = python_code_.automaton_State(
        label=var_11,
        State=var_7,
        postState=var_14,
        inState=var_14,
        currentState=(),
        State38=-122,
    )
    assert isinstance(var_15, python_code_.automaton_State)
    python_code_.automaton_TimedZone(
        time=var_7, TimedZone29=None, inStateOf=var_15, outStateOf=var_15
    )


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = "State40,automaton_EventToken"
    var_1 = float
    var_2 = python_code_.automaton_State(
        label=var_0, State=var_1, automaton_State=var_1, State38=var_0
    )
    assert isinstance(var_2, python_code_.automaton_State)
    var_4 = python_code_.automaton_Guard()
    var_14 = python_code_.automaton_Event()
    var_15 = python_code_.automaton_State(
        label=var_0,
        State=var_4,
        preState=var_0,
        automaton_State25=var_14,
        State40=var_1,
    )
    assert isinstance(var_15, python_code_.automaton_State)
    python_code_.automaton_TimedZone(time=var_2, outStateOf=var_15)


def test_29():
    var_41 = "-mbPI"
    var_42 = lambda *args, **kwargs: [
        "STRICT_IMMEDIATE automaton_EventToken18 TimedZone29",
        True,
    ]
    var_43 = python_code_.automaton_EventToken()
    var_44 = python_code_.automaton_TimedZone(
        time=var_42, automaton_TimedZone19=var_43, TimedZone29=var_43
    )
    assert isinstance(var_44, python_code_.automaton_TimedZone)
    var_45 = {var_44, var_44, var_44, var_44, var_44}
    var_46 = python_code_.automaton_Event()
    var_47 = python_code_.automaton_State(
        label=var_41,
        inState=[],
        outState=var_45,
        State31=var_42,
        State33=None,
        automaton_State25=var_46,
    )
    assert isinstance(var_47, python_code_.automaton_State)
