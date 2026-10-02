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
    Comparation,
    Enum,
    NamedElement,
    Node,
    Protocol,
    abstractmethod,
    dataflownet_Channel,
    dataflownet_DataflowNet,
    dataflownet_DataflowSystem,
    dataflownet_FiringRule,
    dataflownet_NamedElement,
    dataflownet_Node,
    dataflownet_Process,
    dataflownet_StateMachine,
    dataflownet_StateMachineState,
    dataflownet_StateMachineTransition,
    dataflownet_Token,
    dataflownet_Type,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.dataflownet_Token(
        value="_dataflownet_StateMachineTransition__dataflownet_StateMachineTransition28_dataflownet_Process__dataflownet_Process50",
        dataflownet_Token=None,
    )


def test_1():
    var_1 = python_code_.dataflownet_Node()
    var_2 = python_code_.dataflownet_NamedElement(name=var_1)
    assert isinstance(var_2, python_code_.dataflownet_NamedElement)
    var_3 = python_code_.dataflownet_Type()
    python_code_.dataflownet_Token(
        value={}, dataflownet_Token=var_2, dataflownet_Token38=var_3
    )


def test_2():
    var_16 = python_code_.dataflownet_Process(
        host="toState dataflownet_Channel47 dataflownet_DataflowNet dataflownet_Type41"
    )
    assert isinstance(var_16, python_code_.dataflownet_Process)


def test_3():
    var_21 = python_code_.dataflownet_Process(
        host=b"\x0fE+",
        dataflownet_Process50=complex(1241.3176517, -502.77),
        dataflownet_Process=3,
    )
    assert isinstance(var_21, python_code_.dataflownet_Process)


def test_4():
    var_11 = python_code_.dataflownet_DataflowSystem(
        protocol="j.9Bxq<Z",
        dataflownet_DataflowSystem43={-3439.44, "dataflownet_FiringRule36", 907},
        dataflownet_DataflowSystem49={2273, "cGwZ:VcNs,XpU&lR"},
        dataflownet_DataflowSystem=set(),
    )
    assert isinstance(var_11, python_code_.dataflownet_DataflowSystem)


def test_5():
    var_11 = python_code_.dataflownet_DataflowSystem(protocol="dataflownet_Type41")
    assert isinstance(var_11, python_code_.dataflownet_DataflowSystem)


def test_6():
    var_20 = python_code_.dataflownet_DataflowSystem(
        protocol="dataflownet_Type:_dataflownet_DataflowSystem__dataflownet_DataflowSystem:_dataflownet_DataflowSystem__dataflownet_DataflowSystem",
        dataflownet_DataflowSystem46={408},
    )
    assert isinstance(var_20, python_code_.dataflownet_DataflowSystem)


def test_7():
    var_11 = python_code_.dataflownet_DataflowSystem(
        protocol="hq1:", dataflownet_DataflowSystem={"|b\n.", -3510.25, -1755}
    )
    assert isinstance(var_11, python_code_.dataflownet_DataflowSystem)


def test_8():
    var_8 = python_code_.dataflownet_FiringRule(
        compType="_dataflownet_StateMachineTransition__StateMachineTransition",
        dataflownet_FiringRule26=None,
    )
    assert isinstance(var_8, python_code_.dataflownet_FiringRule)


def test_9():
    var_11 = python_code_.dataflownet_DataflowSystem(
        protocol="_dataflownet_StateMachineTransition__inputTransitions"
    )
    assert isinstance(var_11, python_code_.dataflownet_DataflowSystem)
    var_12 = python_code_.dataflownet_FiringRule(
        compType=b"\xb5\xac\xc0\xc2\xa1\x93m\xb6\xe9\x1f+\xae\xb8!0\xa5\t\xdae",
        dataflownet_FiringRule=var_11,
        dataflownet_FiringRule36=(-1554,),
    )
    assert isinstance(var_12, python_code_.dataflownet_FiringRule)


def test_10():
    var_17 = python_code_.dataflownet_FiringRule(
        compType=None, dataflownet_FiringRule26=-215.89, dataflownet_FiringRule29=set()
    )
    assert isinstance(var_17, python_code_.dataflownet_FiringRule)


def test_11():
    var_23 = python_code_.dataflownet_StateMachineTransition(
        priority=-1, inputTransitions=None, dataflownet_StateMachineTransition=set()
    )
    assert isinstance(var_23, python_code_.dataflownet_StateMachineTransition)


def test_12():
    var_23 = python_code_.dataflownet_StateMachineTransition(
        priority=-2993,
        StateMachineTransition=None,
        StateMachineTransition18=None,
        inputTransitions=None,
    )
    assert isinstance(var_23, python_code_.dataflownet_StateMachineTransition)


def test_13():
    var_23 = python_code_.dataflownet_StateMachineTransition(
        priority=3,
        StateMachineTransition18=None,
        dataflownet_StateMachineTransition28=set(),
    )
    assert isinstance(var_23, python_code_.dataflownet_StateMachineTransition)


def test_14():
    var_12 = bytes
    var_13 = python_code_.dataflownet_StateMachineTransition(
        priority=-1386, StateMachineTransition=var_12, outputTransitions=var_12
    )
    assert isinstance(var_13, python_code_.dataflownet_StateMachineTransition)


def test_15():
    var_0 = -1688
    var_19 = python_code_.dataflownet_StateMachineTransition(
        priority=-2791,
        StateMachineTransition=None,
        outputTransitions=var_0,
        inputTransitions=var_0,
    )
    assert isinstance(var_19, python_code_.dataflownet_StateMachineTransition)


def test_16():
    var_0 = -1667
    var_30 = python_code_.dataflownet_StateMachineTransition(
        priority=var_0,
        StateMachineTransition=var_0,
        StateMachineTransition18=var_0,
        outputTransitions=None,
        inputTransitions=var_0,
        dataflownet_StateMachineTransition28={False, var_0},
    )
    assert isinstance(var_30, python_code_.dataflownet_StateMachineTransition)


def test_17():
    python_code_.dataflownet_DataflowNet()


def test_18():
    var_15 = tuple
    var_16 = python_code_.dataflownet_Process(
        host=var_15, dataflownet_Process50=(), dataflownet_Process=var_15
    )
    assert isinstance(var_16, python_code_.dataflownet_Process)
    var_17 = {var_16, var_16, var_16, var_16}
    var_14 = python_code_.dataflownet_DataflowSystem(
        protocol=var_15, dataflownet_DataflowSystem49=var_17
    )
    assert isinstance(var_14, python_code_.dataflownet_DataflowSystem)


def test_19():
    var_11 = python_code_.dataflownet_DataflowSystem(
        protocol="dataflownet_DataflowSystem49",
        dataflownet_DataflowSystem43={"!m0Z2V`Wj"},
    )
    assert isinstance(var_11, python_code_.dataflownet_DataflowSystem)
    var_13 = python_code_.dataflownet_Process(
        host=3905.78, dataflownet_Process50=var_11
    )
    assert isinstance(var_13, python_code_.dataflownet_Process)


def test_20():
    var_0 = -1657
    var_33 = python_code_.dataflownet_FiringRule(compType="MUE@")
    assert isinstance(var_33, python_code_.dataflownet_FiringRule)
    var_37 = {var_33, "eoPkgW!<1(pwK"}
    var_38 = python_code_.dataflownet_StateMachineTransition(
        priority=-1515,
        outputTransitions=None,
        dataflownet_StateMachineTransition28=var_37,
    )
    assert isinstance(var_38, python_code_.dataflownet_StateMachineTransition)
    var_39 = python_code_.dataflownet_StateMachineTransition(
        priority=var_0,
        dataflownet_StateMachineTransition=var_37,
        dataflownet_StateMachineTransition28=var_37,
    )
    assert isinstance(var_39, python_code_.dataflownet_StateMachineTransition)


def test_21():
    var_23 = python_code_.dataflownet_StateMachineTransition(priority=-2249)
    assert isinstance(var_23, python_code_.dataflownet_StateMachineTransition)
    var_25 = "q~aH"
    var_26 = python_code_.dataflownet_FiringRule(
        compType=var_25, dataflownet_FiringRule26=var_23
    )
    assert isinstance(var_26, python_code_.dataflownet_FiringRule)


def test_22():
    var_14 = python_code_.dataflownet_DataflowSystem(
        protocol="dataflownet_FiringRule.dataflownet_FiringRule",
        dataflownet_DataflowSystem46=set(),
        dataflownet_DataflowSystem={"Equal"},
    )
    assert isinstance(var_14, python_code_.dataflownet_DataflowSystem)
    var_15 = python_code_.dataflownet_StateMachineTransition(
        priority=0,
        StateMachineTransition18=var_14,
        outputTransitions=var_14,
        dataflownet_StateMachineTransition=set(),
        dataflownet_StateMachineTransition28=set(),
    )
    assert isinstance(var_15, python_code_.dataflownet_StateMachineTransition)
    var_16 = python_code_.dataflownet_FiringRule(
        compType=var_14, dataflownet_FiringRule29=var_15
    )
    assert isinstance(var_16, python_code_.dataflownet_FiringRule)


def test_23():
    var_23 = python_code_.dataflownet_NamedElement(name="n\tu\n\n?M?\r' uIg2ohNm")
    assert isinstance(var_23, python_code_.dataflownet_NamedElement)


def test_24():
    var_1 = tuple
    var_2 = python_code_.dataflownet_DataflowSystem(
        protocol=var_1, dataflownet_DataflowSystem49="K~"
    )
    assert isinstance(var_2, python_code_.dataflownet_DataflowSystem)
    var_13 = "[znC>:FrWJyrq"
    var_14 = python_code_.dataflownet_DataflowNet()
    var_15 = python_code_.dataflownet_Process(
        host=var_13, dataflownet_Process50=var_2, dataflownet_Process=var_14
    )
    assert isinstance(var_15, python_code_.dataflownet_Process)
    var_21 = python_code_.dataflownet_Token(value=var_13, dataflownet_Token={})
    assert isinstance(var_21, python_code_.dataflownet_Token)


def test_25():
    var_11 = python_code_.dataflownet_DataflowSystem(
        protocol="_dataflownet_StateMachineTransition__inputTransitions"
    )
    assert isinstance(var_11, python_code_.dataflownet_DataflowSystem)
    var_12 = python_code_.dataflownet_FiringRule(
        compType="dataflownet_StateMachine4",
        dataflownet_FiringRule=var_11,
        dataflownet_FiringRule26=None,
        dataflownet_FiringRule29=None,
        dataflownet_FiringRule33=var_11,
        dataflownet_FiringRule36=var_11,
    )
    assert isinstance(var_12, python_code_.dataflownet_FiringRule)


def test_26():
    var_40 = python_code_.dataflownet_Token(
        value=610, dataflownet_Token38=complex(-1896.48895, 504.0)
    )
    assert isinstance(var_40, python_code_.dataflownet_Token)


def test_27():
    var_0 = -1657
    var_31 = python_code_.dataflownet_StateMachineState()
    var_40 = python_code_.dataflownet_StateMachineTransition(
        priority=var_0,
        StateMachineTransition=var_31,
        dataflownet_StateMachineTransition=set(),
        dataflownet_StateMachineTransition28=set(),
    )
    assert isinstance(var_40, python_code_.dataflownet_StateMachineTransition)
    var_41 = python_code_.dataflownet_FiringRule(
        compType='E"TWmn^-"2?>jSp', dataflownet_FiringRule26=var_40
    )
    assert isinstance(var_41, python_code_.dataflownet_FiringRule)
    var_42 = {var_41}
    python_code_.dataflownet_StateMachineTransition(
        priority=var_41,
        StateMachineTransition18=var_31,
        dataflownet_StateMachineTransition=var_42,
    )


def test_28():
    var_0 = 1225
    var_1 = python_code_.dataflownet_StateMachineState()
    var_2 = python_code_.NamedElement
    var_3 = -1
    var_4 = python_code_.dataflownet_StateMachineTransition(
        priority=var_3, StateMachineTransition=var_1, StateMachineTransition18=var_1
    )
    assert isinstance(var_4, python_code_.dataflownet_StateMachineTransition)
    var_5 = python_code_.dataflownet_FiringRule(
        compType=var_2,
        dataflownet_FiringRule26=var_1,
        dataflownet_FiringRule29=var_4,
        dataflownet_FiringRule36=480.24,
    )
    assert isinstance(var_5, python_code_.dataflownet_FiringRule)
    var_6 = {var_5}
    var_7 = python_code_.dataflownet_StateMachineTransition(
        priority=var_0,
        StateMachineTransition18=var_1,
        dataflownet_StateMachineTransition=var_6,
    )
    assert isinstance(var_7, python_code_.dataflownet_StateMachineTransition)
    var_8 = python_code_.dataflownet_StateMachineTransition(
        priority=[], outputTransitions=var_6, dataflownet_StateMachineTransition28=var_6
    )
    assert isinstance(var_8, python_code_.dataflownet_StateMachineTransition)


@pytest.mark.xfail(strict=True)
def test_29():
    var_19 = python_code_.dataflownet_Token(
        value="StateMachineState22 StateMachineState22"
    )
    var_20 = hash
    python_code_.dataflownet_FiringRule(
        compType=var_20,
        dataflownet_FiringRule=b"v7k\xe8VD?\xc6Fg",
        dataflownet_FiringRule36=var_19,
    )


@pytest.mark.xfail(strict=True)
def test_30():
    var_34 = python_code_.dataflownet_FiringRule
    var_36 = python_code_.dataflownet_FiringRule(
        compType=[False],
        dataflownet_FiringRule29=var_34,
        dataflownet_FiringRule36=var_34,
    )
    assert isinstance(var_36, python_code_.dataflownet_FiringRule)
    var_48 = "8&?v\n-"
    python_code_.dataflownet_Token(value=var_48, dataflownet_Token=var_36)


@pytest.mark.xfail(strict=True)
def test_31():
    var_34 = python_code_.dataflownet_StateMachineTransition
    var_36 = python_code_.dataflownet_FiringRule(
        compType=[False],
        dataflownet_FiringRule29=var_34,
        dataflownet_FiringRule36=var_34,
    )
    assert isinstance(var_36, python_code_.dataflownet_FiringRule)
    var_47 = "8&?v\n-"
    python_code_.dataflownet_Token(value=var_47, dataflownet_Token=var_36)


def test_32():
    var_21 = python_code_.dataflownet_StateMachineState()
    var_23 = python_code_.dataflownet_Channel()
    var_26 = set()
    var_34 = abs
    var_35 = python_code_.dataflownet_FiringRule(
        compType=var_34, dataflownet_FiringRule33=var_23
    )
    assert isinstance(var_35, python_code_.dataflownet_FiringRule)
    var_36 = python_code_.dataflownet_FiringRule(
        compType=var_34, dataflownet_FiringRule=var_34, dataflownet_FiringRule29=var_26
    )
    assert isinstance(var_36, python_code_.dataflownet_FiringRule)
    var_37 = {var_35, var_35, var_36, var_35}
    var_38 = python_code_.dataflownet_StateMachineTransition(
        priority=var_23,
        StateMachineTransition=var_21,
        StateMachineTransition18=[True, True, True],
        dataflownet_StateMachineTransition=var_26,
        dataflownet_StateMachineTransition28=var_37,
    )
    assert isinstance(var_38, python_code_.dataflownet_StateMachineTransition)


def test_33():
    var_33 = python_code_.NamedElement()
    var_34 = python_code_.dataflownet_StateMachineTransition
    var_36 = python_code_.dataflownet_FiringRule(
        compType="(", dataflownet_FiringRule=var_33, dataflownet_FiringRule26=var_34
    )
    assert isinstance(var_36, python_code_.dataflownet_FiringRule)


@pytest.mark.xfail(strict=True)
def test_34():
    var_34 = python_code_.NamedElement
    var_35 = python_code_.dataflownet_StateMachineState()
    var_36 = python_code_.dataflownet_FiringRule(
        compType=",kRZuGW(W",
        dataflownet_FiringRule=var_35,
        dataflownet_FiringRule29=None,
    )
    assert isinstance(var_36, python_code_.dataflownet_FiringRule)
    var_46 = python_code_.dataflownet_Process(host="2<X-0dr4@C?!")
    assert isinstance(var_46, python_code_.dataflownet_Process)
    var_47 = "5"
    var_48 = python_code_.dataflownet_StateMachine()
    var_49 = "J%;\\Y~SC}1m*N*|e*."
    var_50 = python_code_.dataflownet_Token(value=var_49, dataflownet_Token=var_34)
    python_code_.dataflownet_FiringRule(
        compType=var_47, dataflownet_FiringRule=var_48, dataflownet_FiringRule36=var_50
    )


def test_35():
    var_20 = python_code_.dataflownet_DataflowSystem(
        protocol="_dataflownet_FiringRule__dataflownet_FiringRule29 Paho _dataflownet_Token__dataflownet_Token"
    )
    assert isinstance(var_20, python_code_.dataflownet_DataflowSystem)
    var_30 = 'GqT,2o;Fn"{'
    var_31 = True
    var_32 = python_code_.dataflownet_Process(host=var_31, dataflownet_Process50=var_20)
    assert isinstance(var_32, python_code_.dataflownet_Process)
    var_33 = {var_32, var_30}
    var_34 = python_code_.dataflownet_DataflowSystem(
        protocol=var_30,
        dataflownet_DataflowSystem43=var_30,
        dataflownet_DataflowSystem49=var_33,
    )
    assert isinstance(var_34, python_code_.dataflownet_DataflowSystem)


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = "2E[aMhJ*m\x0cb"
    var_1 = python_code_.dataflownet_Token(value=var_0)
    var_3 = python_code_.dataflownet_Node()
    var_4 = python_code_.dataflownet_StateMachine()
    var_7 = "|:VP\x0cnH];XGb"
    var_8 = python_code_.dataflownet_Channel()
    var_9 = python_code_.dataflownet_FiringRule(
        compType=var_7, dataflownet_FiringRule26=var_7, dataflownet_FiringRule33=var_8
    )
    assert isinstance(var_9, python_code_.dataflownet_FiringRule)
    var_10 = "dataflownet_Type39.dataflownet_Type39.dataflownet_Type._dataflownet_StateMachineTransition__outputTransitions"
    var_11 = python_code_.dataflownet_Type()
    var_12 = {var_11, var_11, var_11, var_11, var_11}
    var_13 = python_code_.dataflownet_DataflowSystem(
        protocol=var_3,
        dataflownet_DataflowSystem49={
            "dataflownet_Type41": False,
            "dataflownet_StateMachineTransition,dataflownet_Process50,Greater,dataflownet_Channel34": False,
        },
        dataflownet_DataflowSystem=var_12,
    )
    assert isinstance(var_13, python_code_.dataflownet_DataflowSystem)
    var_14 = python_code_.dataflownet_Process(host=var_10, dataflownet_Process50=var_13)
    assert isinstance(var_14, python_code_.dataflownet_Process)
    var_15 = python_code_.dataflownet_Process(host=var_4, dataflownet_Process={})
    assert isinstance(var_15, python_code_.dataflownet_Process)
    var_16 = {var_14, var_15, var_14, var_15}
    var_17 = python_code_.dataflownet_DataflowSystem(
        protocol=var_1, dataflownet_DataflowSystem49=var_16
    )
    assert isinstance(var_17, python_code_.dataflownet_DataflowSystem)
    var_19 = dict
    python_code_.dataflownet_DataflowSystem(
        protocol=var_7,
        dataflownet_DataflowSystem43=var_19,
        dataflownet_DataflowSystem=var_16,
    )
