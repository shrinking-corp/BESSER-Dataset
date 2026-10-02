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
    CompositeState,
    Data,
    Enum,
    ExpressionElement,
    Operator,
    SimplStateMachine_Assignment,
    SimplStateMachine_BooleanData,
    SimplStateMachine_BooleanVariable,
    SimplStateMachine_CompositeState,
    SimplStateMachine_Data,
    SimplStateMachine_Event,
    SimplStateMachine_Expression,
    SimplStateMachine_ExpressionElement,
    SimplStateMachine_InitialState,
    SimplStateMachine_IntegerData,
    SimplStateMachine_IntegerVariable,
    SimplStateMachine_Operation,
    SimplStateMachine_State,
    SimplStateMachine_StateMachine,
    SimplStateMachine_Transition,
    SimplStateMachine_Variable,
    SimplStateMachine_VariableReference,
    State,
    Variable,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_11 = python_code_.SimplStateMachine_Assignment(
        _name=1, SimplStateMachine_Assignment33=-1263
    )
    assert isinstance(var_11, python_code_.SimplStateMachine_Assignment)


def test_1():
    var_18 = python_code_.SimplStateMachine_IntegerData
    python_code_.SimplStateMachine_Assignment(
        _name=complex(-756.068338, 171.0), SimplStateMachine_Assignment=var_18
    )


def test_2():
    python_code_.SimplStateMachine_Assignment(_name='v9a\x0c/\x0bp}ie-n-r5"7i')


def test_3():
    var_8 = "yE/Ay[z$Dk][Of?\n"
    var_9 = python_code_.SimplStateMachine_Assignment(
        _name=var_8, SimplStateMachine_Assignment36=()
    )
    assert isinstance(var_9, python_code_.SimplStateMachine_Assignment)


@pytest.mark.xfail(strict=True)
def test_4():
    var_22 = python_code_.SimplStateMachine_Variable(
        name="", SimplStateMachine_Variable=None, SimplStateMachine_Variable39=None
    )
    assert isinstance(var_22, python_code_.SimplStateMachine_Variable)
    python_code_.SimplStateMachine_VariableReference(
        _name={""}, SimplStateMachine_VariableReference=var_22
    )


def test_5():
    var_24 = python_code_.SimplStateMachine_VariableReference(
        _name={":": 1682, "b7~+cR<[i5": 2246.89}
    )
    assert isinstance(var_24, python_code_.SimplStateMachine_VariableReference)


def test_6():
    var_0 = repr
    var_1 = python_code_.SimplStateMachine_Operation()
    var_2 = python_code_.SimplStateMachine_CompositeState(container=set())
    assert isinstance(var_2, python_code_.SimplStateMachine_CompositeState)
    var_3 = python_code_.SimplStateMachine_Transition()
    var_4 = python_code_.SimplStateMachine_State(
        name=var_0,
        isActive=var_0,
        SimplStateMachine_State=var_1,
        State=var_2,
        SimplStateMachine_State17=var_3,
    )
    assert isinstance(var_4, python_code_.SimplStateMachine_State)
    var_6 = "SimpltateMachine_Assignment36"
    var_7 = python_code_.SimplStateMachine_VariableReference(
        _name=var_6,
        SimplStateMachine_VariableReference=complex(-661.796958, -1653.31987),
    )
    assert isinstance(var_7, python_code_.SimplStateMachine_VariableReference)


def test_7():
    var_22 = python_code_.SimplStateMachine_Expression(
        operator="jI\tL/TWu4h]H", _name="", SimplStateMachine_Expression26=None
    )
    assert isinstance(var_22, python_code_.SimplStateMachine_Expression)


def test_8():
    var_21 = python_code_.SimplStateMachine_Transition()
    var_22 = python_code_.SimplStateMachine_Expression(
        operator="8y(y\x0ci1t",
        _name="Kbp).i ",
        SimplStateMachine_Expression24=var_21,
        SimplStateMachine_Expression26=None,
    )
    assert isinstance(var_22, python_code_.SimplStateMachine_Expression)


def test_9():
    var_23 = "sw7"
    var_24 = python_code_.SimplStateMachine_Expression(
        operator=var_23,
        _name="#NDs!O]\\Hz2/9yQKEy",
        SimplStateMachine_Expression24=1975,
        SimplStateMachine_Expression26=complex(608.6886, 1199.0),
    )
    assert isinstance(var_24, python_code_.SimplStateMachine_Expression)


def test_10():
    python_code_.SimplStateMachine_State(
        name="CompositeState:_SimplStateMachine_Event__SimplStateMachine_Event:SimplStateMachine_Data",
        isActive=True,
    )


def test_11():
    var_0 = python_code_.SimplStateMachine_BooleanData(value=False)
    assert isinstance(var_0, python_code_.SimplStateMachine_BooleanData)
    python_code_.SimplStateMachine_State(
        name="{>on6 A^lhyXx", isActive=False, states=var_0, State=var_0
    )


def test_12():
    var_0 = python_code_.SimplStateMachine_BooleanData(value=False)
    assert isinstance(var_0, python_code_.SimplStateMachine_BooleanData)
    python_code_.SimplStateMachine_State(
        name="_SimplStateMachine_Variable__SimplStateMachine_Variable29 SimplStateMachine_Variable",
        isActive=False,
        states=var_0,
        SimplStateMachine_State11=var_0,
        State=None,
        SimplStateMachine_State17=None,
    )


def test_13():
    var_0 = python_code_.SimplStateMachine_BooleanData(value=False)
    assert isinstance(var_0, python_code_.SimplStateMachine_BooleanData)
    python_code_.SimplStateMachine_State(
        name="Tllze,@", isActive=False, State=None, SimplStateMachine_State17=var_0
    )


def test_14():
    var_0 = -652
    var_1 = python_code_.SimplStateMachine_State(
        name="{fJ1V`qU", isActive=False, states=var_0, SimplStateMachine_State=var_0
    )
    assert isinstance(var_1, python_code_.SimplStateMachine_State)


@pytest.mark.xfail(strict=True)
def test_15():
    var_0 = False
    var_1 = python_code_.SimplStateMachine_State(
        name=False, isActive=var_0, SimplStateMachine_State11=b"\xb2\xbe\x7fye"
    )
    assert isinstance(var_1, python_code_.SimplStateMachine_State)
    python_code_.SimplStateMachine_CompositeState(CompositeState=var_1)


def test_16():
    var_22 = python_code_.SimplStateMachine_Variable(name=";yE*8T_9p5}#")
    assert isinstance(var_22, python_code_.SimplStateMachine_Variable)


def test_17():
    var_0 = repr
    var_9 = python_code_.SimplStateMachine_Variable(
        name="8EvC9",
        SimplStateMachine_Variable37=var_0,
        SimplStateMachine_Variable39=var_0,
    )
    assert isinstance(var_9, python_code_.SimplStateMachine_Variable)


def test_18():
    var_27 = python_code_.SimplStateMachine_Data()
    var_30 = python_code_.SimplStateMachine_Variable(
        name="SimplStateMachine_StateMachine,_SimplStateMachine_State__states",
        SimplStateMachine_Variable=var_27,
        SimplStateMachine_Variable37=var_27,
        SimplStateMachine_Variable29=var_27,
    )
    assert isinstance(var_30, python_code_.SimplStateMachine_Variable)


def test_19():
    var_21 = python_code_.SimplStateMachine_Variable(
        name=3151.49, SimplStateMachine_Variable=()
    )
    assert isinstance(var_21, python_code_.SimplStateMachine_Variable)


def test_20():
    python_code_.SimplStateMachine_Event(name=True)


def test_21():
    var_22 = 'Kl">\\Y'
    var_23 = python_code_.SimplStateMachine_Event(
        name=var_22, SimplStateMachine_Event=var_22, SimplStateMachine_Event20=var_22
    )
    assert isinstance(var_23, python_code_.SimplStateMachine_Event)


def test_22():
    var_13 = python_code_.SimplStateMachine_CompositeState(
        CompositeState=None, container={False, 335, 4452}
    )
    assert isinstance(var_13, python_code_.SimplStateMachine_CompositeState)


def test_23():
    var_2 = python_code_.SimplStateMachine_CompositeState(
        CompositeState=None, SimplStateMachine_CompositeState=None
    )
    assert isinstance(var_2, python_code_.SimplStateMachine_CompositeState)


def test_24():
    var_13 = python_code_.SimplStateMachine_CompositeState(
        SimplStateMachine_CompositeState=b"\x8evTcZ\xf3\x95\x18\xa6~g"
    )
    assert isinstance(var_13, python_code_.SimplStateMachine_CompositeState)


def test_25():
    var_0 = repr
    var_2 = python_code_.SimplStateMachine_CompositeState(CompositeState=var_0)
    assert isinstance(var_2, python_code_.SimplStateMachine_CompositeState)
    var_7 = "C<7rH\\f?3"
    var_8 = python_code_.SimplStateMachine_Variable(
        name=var_7, SimplStateMachine_Variable37=var_7
    )
    assert isinstance(var_8, python_code_.SimplStateMachine_Variable)


def test_26():
    python_code_.SimplStateMachine_Operation()


def test_27():
    var_25 = python_code_.SimplStateMachine_IntegerData(value=-1149)
    assert isinstance(var_25, python_code_.SimplStateMachine_IntegerData)


def test_28():
    var_0 = python_code_.SimplStateMachine_BooleanData(value=True)
    assert isinstance(var_0, python_code_.SimplStateMachine_BooleanData)


def test_29():
    var_25 = python_code_.SimplStateMachine_CompositeState()
    assert var_25.CompositeState is None
    var_26 = python_code_.SimplStateMachine_State(
        name="_SimplStateMachine_Expression__SimplStateMachine_Expression24,gte,_SimplStateMachine_Expression__SimplStateMachine_Expression24,SimplStateMachine_CompositeState",
        isActive=False,
        states=None,
        State=var_25,
        SimplStateMachine_State17=var_25,
    )
    assert isinstance(var_26, python_code_.SimplStateMachine_State)


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = python_code_.SimplStateMachine_IntegerData(value={})
    assert isinstance(var_0, python_code_.SimplStateMachine_IntegerData)
    var_1 = python_code_.SimplStateMachine_CompositeState(container="26")
    assert isinstance(var_1, python_code_.SimplStateMachine_CompositeState)
    var_1.activeSubTree()
    var_1.unactiveSubTree()
    var_4 = python_code_.SimplStateMachine_VariableReference(
        _name=var_1, SimplStateMachine_VariableReference=var_0
    )
    assert isinstance(var_4, python_code_.SimplStateMachine_VariableReference)
    var_5 = True
    var_6 = python_code_.SimplStateMachine_BooleanData(value=var_5)
    assert isinstance(var_6, python_code_.SimplStateMachine_BooleanData)
    var_7 = "\\p_XQ3"
    var_8 = python_code_.SimplStateMachine_Variable(name=var_7)
    assert isinstance(var_8, python_code_.SimplStateMachine_Variable)
    var_13 = list
    python_code_.SimplStateMachine_Variable(
        name=var_13, SimplStateMachine_Variable39=var_4
    )


def test_31():
    var_25 = python_code_.SimplStateMachine_CompositeState()
    assert var_25.CompositeState is None
    var_26 = python_code_.SimplStateMachine_State(
        name="_SimplStateMachine_Expression__SimplStateMachine_Expression24,gte,_SimplStateMachine_Expression__SimplStateMachine_Expression24,SimplStateMachine_CompositeState",
        isActive=False,
        states=None,
        State=var_25,
        SimplStateMachine_State17=var_25,
    )
    assert isinstance(var_26, python_code_.SimplStateMachine_State)
    var_25.activeSubTree()


def test_32():
    var_1 = python_code_.SimplStateMachine_IntegerVariable()
    var_2 = -4301
    var_3 = python_code_.SimplStateMachine_IntegerData(value=var_2)
    assert isinstance(var_3, python_code_.SimplStateMachine_IntegerData)
    var_4 = False
    var_5 = python_code_.SimplStateMachine_BooleanData(value=var_4)
    assert isinstance(var_5, python_code_.SimplStateMachine_BooleanData)
    var_6 = python_code_.SimplStateMachine_CompositeState()
    assert var_6.CompositeState is None
    var_6.activeSubTree()
    var_11 = python_code_.SimplStateMachine_ExpressionElement()
    python_code_.SimplStateMachine_Assignment(_name=var_2)
    var_14 = python_code_.CompositeState()
    var_15 = "_SimplStateMachine_Variable__SimplStateMachine_Variable37._SimplStateMachine_State__SimplStateMachine_State11.SimplStateMachine_Transition22"
    python_code_.SimplStateMachine_State(name=var_15, isActive=var_1)
    var_17 = bool
    var_18 = python_code_.SimplStateMachine_CompositeState(
        SimplStateMachine_CompositeState=var_17
    )
    assert isinstance(var_18, python_code_.SimplStateMachine_CompositeState)
    var_20 = python_code_.SimplStateMachine_CompositeState(
        SimplStateMachine_CompositeState=None
    )
    var_21 = python_code_.State()
    var_24 = python_code_.SimplStateMachine_ExpressionElement()
    var_25 = python_code_.SimplStateMachine_Expression(
        operator=var_3, _name=var_2, SimplStateMachine_Expression26=var_24
    )
    assert isinstance(var_25, python_code_.SimplStateMachine_Expression)
    var_20.unactiveSubTree()
    var_30 = python_code_.ExpressionElement()
    var_32 = "1MnJEzrcH?Qn,7oK$6"
    var_33 = python_code_.SimplStateMachine_Assignment(
        _name=var_32, SimplStateMachine_Assignment33=-1135
    )
    assert isinstance(var_33, python_code_.SimplStateMachine_Assignment)
    python_code_.SimplStateMachine_Event(name=2, SimplStateMachine_Event20=var_14)
    python_code_.SimplStateMachine_Expression(
        operator=var_21, _name=var_30, SimplStateMachine_Expression24=var_11
    )
    var_38 = ";'#~8#i"
    var_45 = python_code_.CompositeState
    var_46 = python_code_.SimplStateMachine_Operation()
    python_code_.SimplStateMachine_State(
        name=var_38,
        isActive=var_4,
        states=var_45,
        SimplStateMachine_State=var_46,
        State=var_45,
    )


@pytest.mark.xfail(strict=True)
def test_33():
    var_11 = 857.83
    var_12 = python_code_.SimplStateMachine_ExpressionElement()
    var_13 = python_code_.SimplStateMachine_Variable(
        name=var_12, SimplStateMachine_Variable29=[-1543.97]
    )
    assert isinstance(var_13, python_code_.SimplStateMachine_Variable)
    python_code_.SimplStateMachine_Assignment(
        _name=var_11,
        SimplStateMachine_Assignment33=var_12,
        SimplStateMachine_Assignment36=var_13,
    )


def test_34():
    var_10 = "PFnG[Q<K"
    var_2 = python_code_.SimplStateMachine_Expression(
        operator=True, _name=var_10, SimplStateMachine_Expression=var_10
    )
    assert isinstance(var_2, python_code_.SimplStateMachine_Expression)


def test_35():
    var_0 = repr
    var_9 = python_code_.SimplStateMachine_Variable(
        name=var_0, SimplStateMachine_Variable37=var_0
    )
    assert isinstance(var_9, python_code_.SimplStateMachine_Variable)


@pytest.mark.xfail(strict=True)
def test_36():
    var_2 = python_code_.Data()
    var_3 = "yE/Ay[z$Dk][Of?\n"
    var_4 = python_code_.SimplStateMachine_Assignment(
        _name=var_3, SimplStateMachine_Assignment36=()
    )
    assert isinstance(var_4, python_code_.SimplStateMachine_Assignment)
    var_5 = python_code_.SimplStateMachine_StateMachine()
    python_code_.SimplStateMachine_Variable(
        name=var_2, SimplStateMachine_Variable=var_5, SimplStateMachine_Variable37=var_4
    )


def test_37():
    var_0 = python_code_.SimplStateMachine_BooleanData(value=True)
    assert isinstance(var_0, python_code_.SimplStateMachine_BooleanData)
    python_code_.SimplStateMachine_State(
        name="_SimplStateMachine_CompositeState__container SimplStateMachine_Variable37 _SimplStateMachine_State__State _SimplStateMachine_CompositeState__SimplStateMachine_CompositeState",
        isActive=True,
        SimplStateMachine_State14=var_0,
        SimplStateMachine_State17=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_38():
    var_0 = True
    var_20 = "_SimplStateMachine_Event__SimplStateMachine_Eventlt_SimplStateMachine_Expression__SimplStateMachine_Expression24SimplStateMachine_VariableReference"
    var_23 = python_code_.SimplStateMachine_BooleanData
    var_24 = python_code_.SimplStateMachine_Variable(
        name=var_23, SimplStateMachine_Variable39=var_0
    )
    assert isinstance(var_24, python_code_.SimplStateMachine_Variable)
    var_25 = python_code_.SimplStateMachine_Variable(
        name=var_20, SimplStateMachine_Variable37=var_23
    )
    python_code_.SimplStateMachine_Assignment(
        _name=complex(500.6122, -1478.1816415), SimplStateMachine_Assignment36=var_25
    )


@pytest.mark.xfail(strict=True)
def test_39():
    var_1 = python_code_.Data()
    var_5 = python_code_.SimplStateMachine_Transition()
    var_7 = python_code_.Operator.lt
    var_8 = python_code_.SimplStateMachine_IntegerData(value=var_7)
    assert isinstance(var_8, python_code_.SimplStateMachine_IntegerData)
    var_9 = python_code_.SimplStateMachine_ExpressionElement
    python_code_.SimplStateMachine_State(
        name=var_9,
        isActive=complex(1698.0, -580.0),
        State=var_1,
        SimplStateMachine_State14=var_5,
    )
    var_11 = python_code_.SimplStateMachine_InitialState()
    var_12 = python_code_.SimplStateMachine_CompositeState(
        CompositeState=var_9, SimplStateMachine_CompositeState=var_11, container=None
    )
    assert isinstance(var_12, python_code_.SimplStateMachine_CompositeState)
    var_12.activeSubTree()
    var_16 = python_code_.SimplStateMachine_VariableReference(
        _name=(), SimplStateMachine_VariableReference=var_9
    )
    assert isinstance(var_16, python_code_.SimplStateMachine_VariableReference)
    var_17 = "_SimplStateMachine_State__states"
    var_18 = True
    var_19 = python_code_.SimplStateMachine_Operation()
    python_code_.SimplStateMachine_State(
        name=var_17,
        isActive=var_18,
        states=var_12,
        SimplStateMachine_State=var_19,
        SimplStateMachine_State14=var_5,
        SimplStateMachine_State17=var_5,
    )
    assert isinstance(var_12.CompositeState, python_code_.SimplStateMachine_State)


def test_40():
    var_2 = python_code_.SimplStateMachine_CompositeState(container={})
    assert isinstance(var_2, python_code_.SimplStateMachine_CompositeState)
    var_3 = python_code_.SimplStateMachine_State(
        name=1206.68, isActive=None, SimplStateMachine_State=1530, State=var_2
    )
    assert isinstance(var_3, python_code_.SimplStateMachine_State)
    var_2.activeSubTree()


@pytest.mark.xfail(strict=True)
def test_41():
    var_21 = python_code_.CompositeState()
    var_22 = python_code_.SimplStateMachine_Variable(
        name="SimplStateMachine_ExpressionElement34",
        SimplStateMachine_Variable=var_21,
        SimplStateMachine_Variable39=var_21,
    )
    assert isinstance(var_22, python_code_.SimplStateMachine_Variable)
    python_code_.SimplStateMachine_VariableReference(
        _name="lte", SimplStateMachine_VariableReference=var_22
    )
