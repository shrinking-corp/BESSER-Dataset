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
    MDAIntermediateStateMachine_Automaton,
    MDAIntermediateStateMachine_Content,
    MDAIntermediateStateMachine_Message,
    MDAIntermediateStateMachine_MessageSequence,
    MDAIntermediateStateMachine_Operation,
    MDAIntermediateStateMachine_Participant,
    MDAIntermediateStateMachine_State,
    MDAIntermediateStateMachine_Transition,
    MDAIntermediateStateMachine_Value,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.MDAIntermediateStateMachine_Value(
        value="8oJ", MDAIntermediateStateMachine_Value=None
    )


def test_1():
    var_36 = tuple
    var_37 = python_code_.MDAIntermediateStateMachine_Value(
        value=var_36, MDAIntermediateStateMachine_Value41=set()
    )
    assert isinstance(var_37, python_code_.MDAIntermediateStateMachine_Value)


def test_2():
    var_19 = python_code_.MDAIntermediateStateMachine_Value(
        value=None, MDAIntermediateStateMachine_Value={False}
    )
    assert isinstance(var_19, python_code_.MDAIntermediateStateMachine_Value)


def test_3():
    python_code_.MDAIntermediateStateMachine_Participant(
        name="1k41dV",
        MDAIntermediateStateMachine_Participant=None,
        MDAIntermediateStateMachine_Participant38=None,
    )


def test_4():
    var_0 = "_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton _MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value MDAIntermediateStateMachine_Transition26 _MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content6"
    var_1 = python_code_.MDAIntermediateStateMachine_Participant(
        name=var_0, MDAIntermediateStateMachine_Participant=var_0
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Participant)


def test_5():
    var_11 = python_code_.MDAIntermediateStateMachine_Message()
    python_code_.MDAIntermediateStateMachine_Participant(
        name=b"\xed\x81\xf2\xfcD\xdb\x04\xa6\xbfF)",
        MDAIntermediateStateMachine_Participant38=var_11,
    )


def test_6():
    var_0 = python_code_.MDAIntermediateStateMachine_MessageSequence()
    python_code_.MDAIntermediateStateMachine_Participant(
        name=None, MDAIntermediateStateMachine_Participant21=var_0
    )


def test_7():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content2-MDAIntermediateStateMachine_Transition29-_MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value41-_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant38",
        MDAIntermediateStateMachine_Automaton15={592, "j1]!P-^)Xd]}"},
        MDAIntermediateStateMachine_Automaton18=set(),
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)


def test_8():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content.MDAIntermediateStateMachine_State13._MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30",
        MDAIntermediateStateMachine_Automaton20=None,
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)


def test_9():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content2,_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content4",
        MDAIntermediateStateMachine_Automaton12=None,
        MDAIntermediateStateMachine_Automaton18=set(),
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)


def test_10():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name="MDAIntermediateStateMachine_Content,_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30,MDAIntermediateStateMachine_Transition23",
        MDAIntermediateStateMachine_Content8={31, -1041, 3},
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)
    var_10 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="*?u;",
        MDAIntermediateStateMachine_Automaton=var_5,
        MDAIntermediateStateMachine_Automaton15={"+V&m]D%<82T~Rsk", 227.95},
        MDAIntermediateStateMachine_Automaton12=var_5,
    )
    assert isinstance(var_10, python_code_.MDAIntermediateStateMachine_Automaton)


def test_11():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content2-MDAIntermediateStateMachine_Content6",
        MDAIntermediateStateMachine_Automaton=None,
        MDAIntermediateStateMachine_Automaton12=None,
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)
    python_code_.MDAIntermediateStateMachine_State(
        name="l1F", MDAIntermediateStateMachine_State13=var_1
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


def test_12():
    python_code_.MDAIntermediateStateMachine_State(
        name="MDAIntermediateStateMachine_Automaton15._MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value41._MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content4._MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton20",
        MDAIntermediateStateMachine_State10={
            "MDAIntermediateStateMachine_Transition32",
            True,
        },
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


def test_13():
    python_code_.MDAIntermediateStateMachine_State(
        name="8_yfGauP1qUmv%]Qn",
        MDAIntermediateStateMachine_State=None,
        MDAIntermediateStateMachine_State27=None,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


def test_14():
    python_code_.MDAIntermediateStateMachine_State(
        name=None, MDAIntermediateStateMachine_State24=33.41
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


def test_15():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="U\x0cd",
        MDAIntermediateStateMachine_Automaton12=None,
        MDAIntermediateStateMachine_Automaton20=None,
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)
    python_code_.MDAIntermediateStateMachine_State(
        name='/}8j|-P"@g^!@Dp=e',
        MDAIntermediateStateMachine_State16=var_1,
        MDAIntermediateStateMachine_State10=set(),
        MDAIntermediateStateMachine_State13=var_1,
        MDAIntermediateStateMachine_State27=var_1,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


def test_16():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name="MDAIntermediateStateMachine_Message,MDAIntermediateStateMachine_Operation",
        MDAIntermediateStateMachine_Content6={"bw]3RQN28X"},
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)
    var_8 = "MDAIntermediateStateMachine_Participant_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton20_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton20"
    var_10 = "W!{\nBH0a"
    var_11 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=None,
        MDAIntermediateStateMachine_Automaton=True,
        MDAIntermediateStateMachine_Automaton18={},
    )
    assert isinstance(var_11, python_code_.MDAIntermediateStateMachine_Automaton)
    var_12 = python_code_.MDAIntermediateStateMachine_Transition()
    var_13 = python_code_.MDAIntermediateStateMachine_State(
        name=var_10,
        MDAIntermediateStateMachine_State="-2&Uh2yL~S",
        MDAIntermediateStateMachine_State16=var_11,
        MDAIntermediateStateMachine_State24=var_8,
        MDAIntermediateStateMachine_State27=var_12,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_14 = lambda *args, **kwargs: 1240
    var_15 = python_code_.MDAIntermediateStateMachine_State(
        name=var_14,
        MDAIntermediateStateMachine_State13=var_12,
        MDAIntermediateStateMachine_State27=var_12,
    )
    var_16 = {var_13, var_15, var_13, var_13}
    python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_8,
        MDAIntermediateStateMachine_Automaton=var_5,
        MDAIntermediateStateMachine_Automaton15=var_16,
        MDAIntermediateStateMachine_Automaton20="8\\\\1\rf.1",
    )


def test_17():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name="3ozw\n8XCuO\x0b@)",
        MDAIntermediateStateMachine_Content={2324, "/U'jm1", -160.84},
        MDAIntermediateStateMachine_Content8=set(),
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)


def test_18():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name=complex(-1020.376, -2056.14)
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)


def test_19():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name="|",
        MDAIntermediateStateMachine_Content2=set(),
        MDAIntermediateStateMachine_Content4=set(),
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)


def test_20():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name="_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30-_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30-MDAIntermediateStateMachine_Automaton15",
        MDAIntermediateStateMachine_Content2={-1417.93, -246, -2498},
        MDAIntermediateStateMachine_Content4=set(),
        MDAIntermediateStateMachine_Content6={False},
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)


@pytest.mark.xfail(strict=True)
def test_21():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content2,_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content4",
        MDAIntermediateStateMachine_Automaton12=None,
        MDAIntermediateStateMachine_Automaton18=set(),
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)
    var_3 = "tz[OQ!wbeyT"
    var_4 = python_code_.MDAIntermediateStateMachine_Operation(
        name=var_3, MDAIntermediateStateMachine_Operation=set()
    )
    assert isinstance(var_4, python_code_.MDAIntermediateStateMachine_Operation)
    var_5 = ";\\"
    var_6 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_5, MDAIntermediateStateMachine_Content8={4005, True, 2412.0}
    )
    assert isinstance(var_6, python_code_.MDAIntermediateStateMachine_Content)
    var_7 = python_code_.MDAIntermediateStateMachine_Operation(
        name=var_1, MDAIntermediateStateMachine_Operation=var_6
    )
    assert isinstance(var_7, python_code_.MDAIntermediateStateMachine_Operation)
    var_8 = {var_4, var_7}
    python_code_.MDAIntermediateStateMachine_Content(
        name=var_1,
        MDAIntermediateStateMachine_Content4=var_8,
        MDAIntermediateStateMachine_Content8=var_1,
    )


def test_22():
    python_code_.MDAIntermediateStateMachine_Operation(
        name=b"\x8a1T0\xc9\xa0\x08\x0c\xf1>L\x86\xa25\xb1\x91"
    )


def test_23():
    var_0 = lambda *args, **kwargs: "MXbXE_\x0cVMJI"
    python_code_.MDAIntermediateStateMachine_Operation(
        name=(-1396,), MDAIntermediateStateMachine_Operation=var_0
    )


def test_24():
    var_13 = python_code_.MDAIntermediateStateMachine_Operation(
        name=None,
        MDAIntermediateStateMachine_Operation35=b"y\xf8\xa5\x82\x8cp\xb5y\x9c\xc0\x06\xfa",
    )
    assert isinstance(var_13, python_code_.MDAIntermediateStateMachine_Operation)


def test_25():
    var_32 = python_code_.MDAIntermediateStateMachine_Transition()
    python_code_.MDAIntermediateStateMachine_Operation(
        name=b"?\xc9\x01b\xda\x1b\x0b29", MDAIntermediateStateMachine_Operation30=var_32
    )


def test_26():
    python_code_.MDAIntermediateStateMachine_MessageSequence()


def test_27():
    var_13 = python_code_.MDAIntermediateStateMachine_Value(
        value="_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content4"
    )
    var_15 = "_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton12-MDAIntermediateStateMachine_Operation-MDAIntermediateStateMachine_Content"
    var_16 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="MDAIntermediateStateMachine_Content6",
        MDAIntermediateStateMachine_Automaton15={var_15, 808.24},
        MDAIntermediateStateMachine_Automaton12=var_13,
    )
    assert isinstance(var_16, python_code_.MDAIntermediateStateMachine_Automaton)
    var_17 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_15, MDAIntermediateStateMachine_Automaton20=()
    )
    assert isinstance(var_17, python_code_.MDAIntermediateStateMachine_Automaton)
    var_19 = python_code_.MDAIntermediateStateMachine_Content(
        name="Yf8an@P))N[$Y", MDAIntermediateStateMachine_Content6={var_15, -1104}
    )
    assert isinstance(var_19, python_code_.MDAIntermediateStateMachine_Content)
    var_20 = python_code_.MDAIntermediateStateMachine_Participant
    var_21 = python_code_.MDAIntermediateStateMachine_Transition()
    var_22 = python_code_.MDAIntermediateStateMachine_State(
        name=var_15,
        MDAIntermediateStateMachine_State=var_19,
        MDAIntermediateStateMachine_State13=var_20,
        MDAIntermediateStateMachine_State24=var_21,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_23 = {var_22, var_22, var_22}
    python_code_.MDAIntermediateStateMachine_Content(
        name=var_15, MDAIntermediateStateMachine_Content=var_23
    )


def test_28():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name="MDAIntermediateStateMachine_Content,_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30,MDAIntermediateStateMachine_Transition23",
        MDAIntermediateStateMachine_Content8={31, -1041, 3},
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)
    var_6 = python_code_.MDAIntermediateStateMachine_Participant(
        name=var_5,
        MDAIntermediateStateMachine_Participant=var_5,
        MDAIntermediateStateMachine_Participant21=None,
    )
    assert isinstance(var_6, python_code_.MDAIntermediateStateMachine_Participant)


def test_29():
    var_38 = "K$+Ikl04ej&"
    var_39 = python_code_.MDAIntermediateStateMachine_Content(
        name=b"/L\xd8.|\xd1\xde\xfep\xb9\xed9"
    )
    assert isinstance(var_39, python_code_.MDAIntermediateStateMachine_Content)
    var_40 = python_code_.MDAIntermediateStateMachine_Operation(
        name=var_38, MDAIntermediateStateMachine_Operation=var_39
    )
    assert isinstance(var_40, python_code_.MDAIntermediateStateMachine_Operation)


@pytest.mark.xfail(strict=True)
def test_30():
    var_6 = "]w="
    var_7 = "MDAIntermediateStateMachine_Transition29"
    var_8 = python_code_.MDAIntermediateStateMachine_Message()
    var_9 = python_code_.MDAIntermediateStateMachine_Operation(
        name=var_7, MDAIntermediateStateMachine_Operation35=var_8
    )
    var_10 = {var_9, var_9, var_9, var_9, var_9}
    var_11 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_6,
        MDAIntermediateStateMachine_Content=var_6,
        MDAIntermediateStateMachine_Content4=var_10,
    )
    assert isinstance(var_11, python_code_.MDAIntermediateStateMachine_Content)
    var_12 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_7, MDAIntermediateStateMachine_Automaton=var_11
    )
    assert isinstance(var_12, python_code_.MDAIntermediateStateMachine_Automaton)
    python_code_.MDAIntermediateStateMachine_Participant(
        name=var_6,
        MDAIntermediateStateMachine_Participant=var_11,
        MDAIntermediateStateMachine_Participant21=var_12,
    )


def test_31():
    var_0 = lambda *args, **kwargs: "MXbXE_\x0cVMJI"
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="MDAIntermediateStateMachine_Content.MDAIntermediateStateMachine_Operation._MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State13",
        MDAIntermediateStateMachine_Automaton=var_0,
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)
    python_code_.MDAIntermediateStateMachine_Operation(
        name=(-1396,), MDAIntermediateStateMachine_Operation=var_0
    )


def test_32():
    var_0 = lambda *args, **kwargs: "MXbXE_\x0cVMJI"
    var_3 = "Jcg\\FEgV/y@e"
    python_code_.MDAIntermediateStateMachine_Participant(name=var_3)
    var_5 = "MDAIntermediateStateMachine_Content4 _MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30 _MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value MDAIntermediateStateMachine_Content6"
    var_6 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=2033,
        MDAIntermediateStateMachine_Automaton=var_0,
        MDAIntermediateStateMachine_Automaton12=var_5,
    )
    assert isinstance(var_6, python_code_.MDAIntermediateStateMachine_Automaton)
    var_7 = {var_6, var_6, var_6, var_6, var_6}
    var_8 = python_code_.MDAIntermediateStateMachine_Content(
        name={
            "_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State10": True,
            "sf\x0cp|;": False,
            ":AK/j\\l^M": 4388,
        },
        MDAIntermediateStateMachine_Content2=var_7,
    )
    assert isinstance(var_8, python_code_.MDAIntermediateStateMachine_Content)
    python_code_.MDAIntermediateStateMachine_State(
        name=var_5,
        MDAIntermediateStateMachine_State10=(),
        MDAIntermediateStateMachine_State13=var_6,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


def test_33():
    var_0 = lambda *args, **kwargs: "MXbXE_\x0cVMJI"
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="[]gdCZ}o!Qwm7^\x0cl Q",
        MDAIntermediateStateMachine_Automaton18={
            'P\x0b^8"oe^5J5YH\\+:GHL',
            var_0,
            var_0,
        },
        MDAIntermediateStateMachine_Automaton20=var_0,
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)


def test_34():
    var_5 = python_code_.MDAIntermediateStateMachine_Content(
        name="t>Nj^Z", MDAIntermediateStateMachine_Content2={True, "q4E@1EXF>"}
    )
    assert isinstance(var_5, python_code_.MDAIntermediateStateMachine_Content)


def test_35():
    var_7 = '"SV\r,R7M(#YvI=XJ(G2'
    var_12 = "_MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value41MDAIntermediateStateMachine_State16"
    var_13 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_12, MDAIntermediateStateMachine_Automaton=b"\x00\xb2\x864("
    )
    assert isinstance(var_13, python_code_.MDAIntermediateStateMachine_Automaton)
    var_14 = {var_13}
    var_15 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_7,
        MDAIntermediateStateMachine_Content2=var_14,
        MDAIntermediateStateMachine_Content4=[
            "#54>Cs_X.hEB6wo(w",
            '52%%7~,Ekb"j+gP_',
            1252,
        ],
    )
    assert isinstance(var_15, python_code_.MDAIntermediateStateMachine_Content)


def test_36():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="C7+c!\n\x0c",
        MDAIntermediateStateMachine_Automaton=None,
        MDAIntermediateStateMachine_Automaton12=None,
        MDAIntermediateStateMachine_Automaton20=None,
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)
    var_6 = {var_1, var_1}
    var_7 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_1,
        MDAIntermediateStateMachine_Content2=var_6,
        MDAIntermediateStateMachine_Content8=var_6,
    )
    assert isinstance(var_7, python_code_.MDAIntermediateStateMachine_Content)


@pytest.mark.xfail(strict=True)
def test_37():
    var_1 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="TF", MDAIntermediateStateMachine_Automaton=None
    )
    assert isinstance(var_1, python_code_.MDAIntermediateStateMachine_Automaton)
    python_code_.MDAIntermediateStateMachine_Participant(
        name=var_1, MDAIntermediateStateMachine_Participant21=var_1
    )


def test_38():
    var_0 = python_code_.MDAIntermediateStateMachine_MessageSequence()
    var_2 = ""
    python_code_.MDAIntermediateStateMachine_State(
        name=var_2,
        MDAIntermediateStateMachine_State16=var_0,
        MDAIntermediateStateMachine_State27=set(),
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


def test_39():
    var_35 = "_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton15 _MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State27 MDAIntermediateStateMachine_MessageSequence _MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation35"
    var_36 = python_code_.MDAIntermediateStateMachine_Participant(
        name="_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant21",
        MDAIntermediateStateMachine_Participant=complex(-1908.2, -1043.961437),
    )
    assert isinstance(var_36, python_code_.MDAIntermediateStateMachine_Participant)
    var_37 = {var_36, var_36}
    var_38 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_35,
        MDAIntermediateStateMachine_Content2=var_37,
        MDAIntermediateStateMachine_Content6=var_37,
    )
    assert isinstance(var_38, python_code_.MDAIntermediateStateMachine_Content)


def test_40():
    python_code_.MDAIntermediateStateMachine_Value(
        value="_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30:MDAIntermediateStateMachine_Content6"
    )
    var_14 = "MDAIntermediateStateMachine_State:MDAIntermediateStateMachine_Automaton20:_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation:MDAIntermediateStateMachine_Message40"
    var_15 = "64qT0VC[leaWy6sWN"
    var_16 = int
    var_17 = python_code_.MDAIntermediateStateMachine_State(
        name=var_15, MDAIntermediateStateMachine_State16=var_16
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_18 = {var_17}
    python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_14,
        MDAIntermediateStateMachine_Automaton15=var_18,
        MDAIntermediateStateMachine_Automaton20=b"\xad$\x15)\xda\xa1.\xc8",
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_2 = lambda *args, **kwargs: -1633
    var_5 = ")e2< S\txc/b*##n>"
    var_6 = python_code_.MDAIntermediateStateMachine_State(
        name=var_5,
        MDAIntermediateStateMachine_State16=var_2,
        MDAIntermediateStateMachine_State13=var_2,
        MDAIntermediateStateMachine_State27=var_2,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_7 = python_code_.MDAIntermediateStateMachine_Participant(
        name=var_5, MDAIntermediateStateMachine_Participant38=269
    )
    python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_2,
        MDAIntermediateStateMachine_Automaton12=var_6,
        MDAIntermediateStateMachine_Automaton20=var_7,
    )


def test_42():
    var_28 = python_code_.MDAIntermediateStateMachine_Value
    var_29 = python_code_.MDAIntermediateStateMachine_Content
    var_30 = "Xx1S|\tPj.&T"
    var_31 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_30, MDAIntermediateStateMachine_Automaton=var_28
    )
    assert isinstance(var_31, python_code_.MDAIntermediateStateMachine_Automaton)
    python_code_.MDAIntermediateStateMachine_State(
        name=var_28,
        MDAIntermediateStateMachine_State=var_29,
        MDAIntermediateStateMachine_State13=var_31,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_28 = "#JckJwV-]"
    var_29 = python_code_.MDAIntermediateStateMachine_State(
        name=var_28, MDAIntermediateStateMachine_State="zO^pf 4$V,9V>(L"
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_30 = {var_29, var_29, var_29}
    python_code_.MDAIntermediateStateMachine_Content(
        name=var_28,
        MDAIntermediateStateMachine_Content=var_30,
        MDAIntermediateStateMachine_Content4=var_29,
        MDAIntermediateStateMachine_Content6=[],
        MDAIntermediateStateMachine_Content8=var_30,
    )


def test_44():
    python_code_.MDAIntermediateStateMachine_State(
        name="MDAIntermediateStateMachine_Participant21_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State10_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State13MDAIntermediateStateMachine_Automaton12",
        MDAIntermediateStateMachine_State16=None,
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_11 = "_MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value41MDAIntermediateStateMachine_State16"
    var_12 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_11, MDAIntermediateStateMachine_Automaton=b"\x00\xb2\x864("
    )
    var_13 = set()
    python_code_.MDAIntermediateStateMachine_Content(
        name=var_11,
        MDAIntermediateStateMachine_Content2=var_13,
        MDAIntermediateStateMachine_Content4=[
            "#54>Cs_X.hEB6wo(w",
            '52%%7~,Ekb"j+gP_',
            1252,
        ],
    )
    var_15 = "_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant38:MDAIntermediateStateMachine_Transition32:MDAIntermediateStateMachine_Transition29:_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton"
    var_16 = set()
    var_17 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_15,
        MDAIntermediateStateMachine_Content4=var_16,
        MDAIntermediateStateMachine_Content6=b"WP\xf8\xb0\x9a\xb8:\x90",
    )
    python_code_.MDAIntermediateStateMachine_Participant(
        name=var_12, MDAIntermediateStateMachine_Participant=var_17
    )


@pytest.mark.xfail(strict=True)
def test_45():
    var_9 = '"SV\r,R7M(#YvI=XJ(G2'
    var_10 = sorted
    var_11 = python_code_.MDAIntermediateStateMachine_Message()
    var_13 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="S,}pW0~li\x0bQ7IZ",
        MDAIntermediateStateMachine_Automaton=None,
        MDAIntermediateStateMachine_Automaton12=var_10,
    )
    assert isinstance(var_13, python_code_.MDAIntermediateStateMachine_Automaton)
    var_14 = {var_13}
    var_15 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_9,
        MDAIntermediateStateMachine_Content2=var_14,
        MDAIntermediateStateMachine_Content4=[
            "#54>Cs_X.hEB6wo(w",
            '52%%7~,Ekb"j+gP_',
            1252,
        ],
    )
    assert isinstance(var_15, python_code_.MDAIntermediateStateMachine_Content)
    python_code_.MDAIntermediateStateMachine_Operation(name=None)
    var_17 = 'dg0R_><B\x0c5`$"_'
    python_code_.MDAIntermediateStateMachine_Content(
        name=var_17,
        MDAIntermediateStateMachine_Content2=var_14,
        MDAIntermediateStateMachine_Content6=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_1 = python_code_.MDAIntermediateStateMachine_MessageSequence()
    python_code_.MDAIntermediateStateMachine_Value(
        value={"/.!k2Z": -1718.35, "SENSYqh\tL`a{+!G?nf\\": 2031.96}
    )
    var_28 = python_code_.MDAIntermediateStateMachine_Message()
    python_code_.MDAIntermediateStateMachine_Operation(
        name=var_1, MDAIntermediateStateMachine_Operation35=var_28
    )
    var_30 = ".T3}V\n'GD"
    var_31 = python_code_.MDAIntermediateStateMachine_Transition()
    var_32 = python_code_.MDAIntermediateStateMachine_Transition()
    var_33 = {var_31, var_32, var_32, var_32}
    var_34 = lambda *args, **kwargs: "Bx<+ V\n~$?-zC2[dW62"
    var_35 = python_code_.MDAIntermediateStateMachine_Participant(
        name="EJb[R!,+'mCbj(*",
        MDAIntermediateStateMachine_Participant=var_34,
        MDAIntermediateStateMachine_Participant21=b"\xf0V\x01\xee\xad\x87\xean\xe5",
    )
    assert isinstance(var_35, python_code_.MDAIntermediateStateMachine_Participant)
    python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_30,
        MDAIntermediateStateMachine_Automaton18=var_33,
        MDAIntermediateStateMachine_Automaton20=var_35,
    )


def test_47():
    var_0 = python_code_.MDAIntermediateStateMachine_Participant(
        name="_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State24"
    )
    var_1 = {var_0, var_0, var_0}
    var_2 = python_code_.MDAIntermediateStateMachine_Content(
        name="PR<#v:",
        MDAIntermediateStateMachine_Content2=set(),
        MDAIntermediateStateMachine_Content4=var_1,
        MDAIntermediateStateMachine_Content6=var_1,
    )
    assert isinstance(var_2, python_code_.MDAIntermediateStateMachine_Content)
    var_3 = python_code_.MDAIntermediateStateMachine_Content(
        name=[
            907,
            "_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State13.MDAIntermediateStateMachine_Transition29._MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton20",
        ],
        MDAIntermediateStateMachine_Content=var_1,
        MDAIntermediateStateMachine_Content6=var_1,
    )
    assert isinstance(var_3, python_code_.MDAIntermediateStateMachine_Content)
    python_code_.MDAIntermediateStateMachine_Value(value="]G%H/MYLI?-PvVo")
    var_17 = python_code_.MDAIntermediateStateMachine_Automaton(
        name="*?u;",
        MDAIntermediateStateMachine_Automaton=var_2,
        MDAIntermediateStateMachine_Automaton15={"+V&m]D%<82T~Rsk", 227.95},
        MDAIntermediateStateMachine_Automaton12=var_2,
    )
    assert isinstance(var_17, python_code_.MDAIntermediateStateMachine_Automaton)


@pytest.mark.xfail(strict=True)
def test_48():
    var_38 = python_code_.MDAIntermediateStateMachine_State(
        name="^;zrQ1PlYZ#8Vbg",
        MDAIntermediateStateMachine_State=None,
        MDAIntermediateStateMachine_State10={
            "_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State27-_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content",
            -1684.36,
        },
    )
    assert isinstance(var_38, python_code_.MDAIntermediateStateMachine_State)
    var_39 = "#ho\x0bX]"
    var_40 = python_code_.MDAIntermediateStateMachine_State
    var_41 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_39,
        MDAIntermediateStateMachine_Automaton12=var_40,
        MDAIntermediateStateMachine_Automaton20="E",
    )
    assert isinstance(var_41, python_code_.MDAIntermediateStateMachine_Automaton)
    python_code_.MDAIntermediateStateMachine_Participant(
        name=var_39, MDAIntermediateStateMachine_Participant21=var_41
    )


@pytest.mark.xfail(strict=True)
def test_49():
    var_0 = "m2"
    python_code_.MDAIntermediateStateMachine_Value(value=var_0)
    var_2 = python_code_.MDAIntermediateStateMachine_Operation(
        name=var_0, MDAIntermediateStateMachine_Operation=var_0
    )
    assert isinstance(var_2, python_code_.MDAIntermediateStateMachine_Operation)
    var_3 = set()
    var_4 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_0, MDAIntermediateStateMachine_Automaton18=var_3
    )
    assert isinstance(var_4, python_code_.MDAIntermediateStateMachine_Automaton)
    var_6 = "MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_Automaton15.MDAIntermediateStateMachine_State16"
    var_7 = python_code_.MDAIntermediateStateMachine_State(
        name=var_6, MDAIntermediateStateMachine_State13=(-298, -538.36, 417)
    )
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_8 = python_code_.MDAIntermediateStateMachine_Operation
    python_code_.MDAIntermediateStateMachine_Automaton(
        name={}, MDAIntermediateStateMachine_Automaton12=var_8
    )
    var_10 = "I?[H79"
    var_11 = python_code_.MDAIntermediateStateMachine_Participant(name=var_10)
    var_13 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_0,
        MDAIntermediateStateMachine_Content=(1435,),
        MDAIntermediateStateMachine_Content2=var_6,
        MDAIntermediateStateMachine_Content8=var_3,
    )
    assert isinstance(var_13, python_code_.MDAIntermediateStateMachine_Content)
    python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_0,
        MDAIntermediateStateMachine_Automaton=var_13,
        MDAIntermediateStateMachine_Automaton15=var_11,
        MDAIntermediateStateMachine_Automaton12=var_7,
        MDAIntermediateStateMachine_Automaton20=b"M\xd7 \xfaK*=\xe9\xacn\x08",
    )


def test_50():
    var_35 = "MDAIntermediateStateMachine_Automaton"
    var_36 = python_code_.MDAIntermediateStateMachine_Participant(
        name="_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant21",
        MDAIntermediateStateMachine_Participant=complex(-1908.2, -1043.961437),
    )
    assert isinstance(var_36, python_code_.MDAIntermediateStateMachine_Participant)
    var_37 = set()
    var_38 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_35,
        MDAIntermediateStateMachine_Content=var_37,
        MDAIntermediateStateMachine_Content2=var_37,
        MDAIntermediateStateMachine_Content8={var_36, var_35},
    )
    assert isinstance(var_38, python_code_.MDAIntermediateStateMachine_Content)
    var_39 = python_code_.MDAIntermediateStateMachine_Transition()
    var_40 = python_code_.MDAIntermediateStateMachine_State(
        name=var_35,
        MDAIntermediateStateMachine_State16=var_35,
        MDAIntermediateStateMachine_State27=var_39,
    )
    assert isinstance(var_40, python_code_.MDAIntermediateStateMachine_State)
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_41 = set()
    var_29 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_35,
        MDAIntermediateStateMachine_Automaton15=var_41,
        MDAIntermediateStateMachine_Automaton18=var_41,
    )
    assert isinstance(var_29, python_code_.MDAIntermediateStateMachine_Automaton)
    var_30 = (
        "MDAIntermediateStateMachine_Contet4-MDAIntermediateSt\rteXMachine_Automaton12"
    )
    var_31 = python_code_.MDAIntermediateStateMachine_Content(
        name=var_30,
        MDAIntermediateStateMachine_Content4={
            "MDAIntermediateStateMachine_Transition23,_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant38": -686.97,
            "3$:#$<tY\rJHbdA}#5": "f-;/lFT)LUp-p|?#3\\",
            "_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation.MDAIntermediateStateMachine_Transition32.MDAIntermediateStateMachine_Content": 240.52,
        },
    )
    assert isinstance(var_31, python_code_.MDAIntermediateStateMachine_Content)
    var_32 = python_code_.MDAIntermediateStateMachine_Participant(
        name=var_29, MDAIntermediateStateMachine_Participant=var_31
    )
    assert isinstance(var_32, python_code_.MDAIntermediateStateMachine_Participant)
    var_49 = python_code_.MDAIntermediateStateMachine_State(
        name='/}8j|-P"@g^!@Dp=e',
        MDAIntermediateStateMachine_State16=var_29,
        MDAIntermediateStateMachine_State10=set(),
        MDAIntermediateStateMachine_State13=var_29,
        MDAIntermediateStateMachine_State27=var_29,
    )
    assert isinstance(var_49, python_code_.MDAIntermediateStateMachine_State)
    var_50 = python_code_.MDAIntermediateStateMachine_Participant(
        name=var_41,
        MDAIntermediateStateMachine_Participant21=False,
        MDAIntermediateStateMachine_Participant38=-3133,
    )
    assert isinstance(var_50, python_code_.MDAIntermediateStateMachine_Participant)
    var_51 = python_code_.MDAIntermediateStateMachine_Operation(
        name=var_35,
        MDAIntermediateStateMachine_Operation=var_31,
        MDAIntermediateStateMachine_Operation35=var_50,
    )
    assert isinstance(var_51, python_code_.MDAIntermediateStateMachine_Operation)


def test_51():
    var_0 = float
    var_1 = python_code_.MDAIntermediateStateMachine_State(name=b"\xfb")
    assert isinstance(
        python_code_.MDAIntermediateStateMachine_State.MDAIntermediateStateMachine_State13,
        python_code_.MDAIntermediateStateMachine_Automaton,
    )
    var_2 = {var_1, var_1}
    var_3 = python_code_.MDAIntermediateStateMachine_Content(
        name=3,
        MDAIntermediateStateMachine_Content=var_2,
        MDAIntermediateStateMachine_Content6={
            "r\\:Mm7*%[~c+5cF@": -234.26,
            "MDAIntermediateStateMachine_Automaton20": True,
        },
        MDAIntermediateStateMachine_Content8=var_2,
    )
    assert isinstance(var_3, python_code_.MDAIntermediateStateMachine_Content)
    var_4 = python_code_.MDAIntermediateStateMachine_Transition()
    var_5 = python_code_.MDAIntermediateStateMachine_Message()
    var_6 = python_code_.MDAIntermediateStateMachine_Operation(
        name=var_0,
        MDAIntermediateStateMachine_Operation=var_3,
        MDAIntermediateStateMachine_Operation30=var_4,
        MDAIntermediateStateMachine_Operation35=var_5,
    )
    assert isinstance(var_6, python_code_.MDAIntermediateStateMachine_Operation)
    var_7 = python_code_.MDAIntermediateStateMachine_State(
        name=var_3,
        MDAIntermediateStateMachine_State=complex(63.512, -3774.4398),
        MDAIntermediateStateMachine_State27=var_4,
    )
    assert isinstance(var_7, python_code_.MDAIntermediateStateMachine_State)
    var_8 = "MDAIntermediateStateMachine_Message"
    python_code_.MDAIntermediateStateMachine_Value(value=var_8)
    var_10 = python_code_.MDAIntermediateStateMachine_Transition()
    var_12 = python_code_.MDAIntermediateStateMachine_Message()
    python_code_.MDAIntermediateStateMachine_Participant(
        name=-2912, MDAIntermediateStateMachine_Participant38=var_12
    )
    var_15 = "IU7C#!;#+f"
    var_16 = python_code_.MDAIntermediateStateMachine_Automaton(
        name=var_15,
        MDAIntermediateStateMachine_Automaton15=b"\xa7e\x9b\x94\x8b@\x86\x82~\xee\xfa\xa8\x8blR\xb6",
    )
    assert isinstance(var_16, python_code_.MDAIntermediateStateMachine_Automaton)
    var_17 = python_code_.MDAIntermediateStateMachine_State(
        name=var_0, MDAIntermediateStateMachine_State16=var_16
    )
    assert isinstance(var_17, python_code_.MDAIntermediateStateMachine_State)
    var_18 = python_code_.MDAIntermediateStateMachine_Participant(
        name=var_10, MDAIntermediateStateMachine_Participant=var_0
    )
    assert isinstance(var_18, python_code_.MDAIntermediateStateMachine_Participant)
