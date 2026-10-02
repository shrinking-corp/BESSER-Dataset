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
    Event,
    KeyValuePair,
    NewEnum1,
    Node,
    State,
    abstractmethod,
    date,
    datetime,
    statesml_Attribute,
    statesml_Attributes,
    statesml_ChangeEvent,
    statesml_Constant,
    statesml_DataType,
    statesml_DataTypeLibrary,
    statesml_Edge,
    statesml_Event,
    statesml_Events,
    statesml_Function,
    statesml_InitialState,
    statesml_KeyValuePair,
    statesml_NewEClass21,
    statesml_NewEClass22,
    statesml_NewEClass3,
    statesml_NewEClass4,
    statesml_Node,
    statesml_Parameter,
    statesml_RegularState,
    statesml_SelectionConvergence,
    statesml_SelectionDivergence,
    statesml_State,
    statesml_StatesMLModel,
    statesml_SystemUnit,
    statesml_SystemUnitLibrary,
    statesml_TerminalState,
    statesml_Transition,
    statesml_Trigger,
    time,
)


def test_0():
    var_7 = python_code_.statesml_DataTypeLibrary(
        name="statesml_Node18", statesml_DataTypeLibrary={-631, False}
    )
    assert isinstance(var_7, python_code_.statesml_DataTypeLibrary)


def test_1():
    var_7 = python_code_.statesml_DataTypeLibrary(
        name="_statesml_DataType__statesml_DataType37"
    )
    assert isinstance(var_7, python_code_.statesml_DataTypeLibrary)


def test_2():
    var_5 = python_code_.statesml_SystemUnitLibrary(
        name="_statesml_SystemUnit__statesml_SystemUnit27:_statesml_Function__statesml_Function28:statesml_DataType37"
    )
    assert isinstance(var_5, python_code_.statesml_SystemUnitLibrary)


@pytest.mark.xfail(strict=True)
def test_3():
    var_4 = python_code_.statesml_Trigger(statesml_Trigger11=(242.45,))
    assert isinstance(var_4, python_code_.statesml_Trigger)
    var_5 = python_code_.Event
    var_6 = python_code_.statesml_ChangeEvent
    var_7 = python_code_.statesml_SystemUnit(
        name=var_5, statesml_SystemUnit=var_6, statesml_SystemUnit39=var_5
    )
    assert isinstance(var_7, python_code_.statesml_SystemUnit)
    var_9 = python_code_.statesml_Parameter()
    var_10 = "?_5Z|SoG`r"
    python_code_.statesml_Edge(name=var_10)
    var_12 = python_code_.statesml_DataType(name=False, statesml_DataType37=False)
    assert isinstance(var_12, python_code_.statesml_DataType)
    var_13 = python_code_.statesml_Function(
        name=var_9, statesml_Function28=var_7, statesml_Function35=var_12
    )
    assert isinstance(var_13, python_code_.statesml_Function)
    var_17 = python_code_.statesml_KeyValuePair(name=var_10)
    assert isinstance(var_17, python_code_.statesml_KeyValuePair)
    var_20 = python_code_.statesml_DataTypeLibrary(name=var_7)
    assert isinstance(var_20, python_code_.statesml_DataTypeLibrary)
    python_code_.statesml_KeyValuePair(name="pG0vj", statesml_KeyValuePair=var_12)


def test_4():
    var_12 = python_code_.statesml_KeyValuePair(
        name="ilPu/p\x0c;", statesml_KeyValuePair=True
    )
    assert isinstance(var_12, python_code_.statesml_KeyValuePair)


def test_5():
    var_20 = python_code_.statesml_KeyValuePair(name=())
    assert isinstance(var_20, python_code_.statesml_KeyValuePair)


def test_6():
    var_18 = python_code_.statesml_DataType(name="statesml_KeyValuePair")
    assert isinstance(var_18, python_code_.statesml_DataType)


def test_7():
    var_7 = python_code_.statesml_DataTypeLibrary(
        name="statesml_Attribute25-LITERAL1-_statesml_Event__statesml_Event"
    )
    assert isinstance(var_7, python_code_.statesml_DataTypeLibrary)
    var_18 = python_code_.statesml_DataType(name=var_7, statesml_DataType41=var_7)
    assert isinstance(var_18, python_code_.statesml_DataType)


def test_8():
    var_7 = python_code_.statesml_DataTypeLibrary(name="Z}Bn")
    assert isinstance(var_7, python_code_.statesml_DataTypeLibrary)
    var_12 = python_code_.statesml_Node
    var_13 = python_code_.statesml_DataType(
        name="@qB9~4aEz2<.Xa5/*", statesml_DataType37=var_12
    )
    assert isinstance(var_13, python_code_.statesml_DataType)


@pytest.mark.xfail(strict=True)
def test_9():
    var_17 = python_code_.statesml_SystemUnit(name="|/.", statesml_SystemUnit=None)
    assert isinstance(var_17, python_code_.statesml_SystemUnit)
    var_29 = python_code_.statesml_Event(name=var_17)
    assert isinstance(var_29, python_code_.statesml_Event)
    python_code_.statesml_Trigger(statesml_Trigger=['p"N'], statesml_Trigger11=var_29)


def test_10():
    var_18 = python_code_.statesml_Event(name="5gsd?4r0^VC)")
    assert isinstance(var_18, python_code_.statesml_Event)


def test_11():
    var_8 = python_code_.statesml_Function(
        name="statesml_Transition_statesml_Function__statesml_Function35_statesml_DataType__statesml_DataType37statesml_Node"
    )
    assert isinstance(var_8, python_code_.statesml_Function)


def test_12():
    var_6 = "?_Z|dS-G`r"
    var_8 = python_code_.statesml_Function(name=var_6, statesml_Function28=var_6)
    assert isinstance(var_8, python_code_.statesml_Function)


def test_13():
    var_6 = "?_5Z|dS-G`rb"
    var_8 = python_code_.statesml_Function(
        name="statesml_Node21:statesml_StatesMLModel2:_statesml_Node__Node",
        statesml_Function=var_6,
        statesml_Function32=var_6,
        statesml_Function35=var_6,
    )
    assert isinstance(var_8, python_code_.statesml_Function)


def test_14():
    python_code_.statesml_Edge(name=" -bi-1d", statesml_Edge20=None)


def test_15():
    var_17 = python_code_.statesml_SystemUnit(name="|/.", statesml_SystemUnit=None)
    assert isinstance(var_17, python_code_.statesml_SystemUnit)


def test_16():
    var_20 = python_code_.statesml_Event(name=[])
    assert isinstance(var_20, python_code_.statesml_Event)
    var_21 = var_20.eventOccured()
    var_22 = python_code_.statesml_SystemUnit(
        name=-2312,
        statesml_SystemUnit="kQo['&",
        statesml_SystemUnit24=var_21,
        statesml_SystemUnit39=var_20,
    )
    assert isinstance(var_22, python_code_.statesml_SystemUnit)


def test_17():
    var_5 = python_code_.statesml_Node(
        name="_statesml_SystemUnitLibrary__statesml_SystemUnitLibrary",
        node=set(),
        statesml_Node18=None,
    )
    assert isinstance(var_5, python_code_.statesml_Node)


def test_18():
    var_5 = python_code_.statesml_Node(name=set())
    assert isinstance(var_5, python_code_.statesml_Node)


def test_19():
    var_10 = python_code_.statesml_NewEClass4()
    var_11 = python_code_.statesml_Node(
        name="X{$", statesml_Node=var_10, statesml_Node18=None
    )
    assert isinstance(var_11, python_code_.statesml_Node)


def test_20():
    var_11 = python_code_.statesml_Node(
        name=b"\xb3\xe4\x85\xb3\x89G\x00+\xbd\x8d\xb8\x10x\xd7*\x92", Node=()
    )
    assert isinstance(var_11, python_code_.statesml_Node)


def test_21():
    var_7 = python_code_.statesml_Node(
        name="l#|\x0b5+$r=`}Nu^u19",
        statesml_Node18=b"\x97\x7fc\xb4\x9a\xb5\xabL]\\\x1b\xfb\xda\xaaq\xf9\x10\xa2\x9e",
    )
    assert isinstance(var_7, python_code_.statesml_Node)


def test_22():
    python_code_.statesml_Trigger()


def test_23():
    var_21 = python_code_.statesml_Trigger(statesml_Trigger11=())
    assert isinstance(var_21, python_code_.statesml_Trigger)


def test_24():
    var_13 = python_code_.statesml_Trigger(statesml_Trigger=3115.72)
    assert isinstance(var_13, python_code_.statesml_Trigger)


def test_25():
    python_code_.statesml_Attributes()


def test_26():
    var_7 = python_code_.statesml_DataTypeLibrary(
        name="statesml_Attribute25-LITERAL1-_statesml_Event__statesml_Event"
    )
    assert isinstance(var_7, python_code_.statesml_DataTypeLibrary)
    var_18 = python_code_.statesml_DataType(name=var_7, statesml_DataType41=var_7)
    assert isinstance(var_18, python_code_.statesml_DataType)
    var_19 = python_code_.statesml_Function(name=var_7, statesml_Function35=var_18)
    assert isinstance(var_19, python_code_.statesml_Function)


def test_27():
    var_4 = "%?Bsz"
    var_6 = python_code_.statesml_SystemUnit(name="s")
    assert isinstance(var_6, python_code_.statesml_SystemUnit)
    var_7 = python_code_.statesml_Function(name=var_4, statesml_Function28=var_6)
    assert isinstance(var_7, python_code_.statesml_Function)


def test_28():
    var_0 = python_code_.statesml_NewEClass22()
    var_2 = python_code_.statesml_Transition()
    var_3 = python_code_.statesml_Trigger(statesml_Trigger=var_2)
    var_3.fire(statesml_event=var_0)
    python_code_.statesml_Edge(name=b"\xd0>")


def test_29():
    var_18 = python_code_.statesml_DataType(
        name="\x0b..t", statesml_DataType=set(), statesml_DataType37=None
    )
    assert isinstance(var_18, python_code_.statesml_DataType)


def test_30():
    var_3 = python_code_.statesml_Attributes()
    var_8 = python_code_.statesml_Node(
        name=var_3, statesml_Node={}, statesml_Node21="Qq"
    )
    assert isinstance(var_8, python_code_.statesml_Node)


def test_31():
    var_4 = python_code_.statesml_Transition()
    var_5 = python_code_.statesml_Trigger(statesml_Trigger=var_4)
    python_code_.statesml_Edge(name=b"\xd0>")
    var_9 = python_code_.statesml_Constant
    var_10 = var_5.fire(statesml_event=set())
    var_11 = python_code_.statesml_DataType(
        name=var_9, statesml_DataType=var_10, statesml_DataType41=(-2620, 2026, True)
    )
    assert isinstance(var_11, python_code_.statesml_DataType)


@pytest.mark.xfail(strict=True)
def test_32():
    var_17 = python_code_.statesml_SystemUnit(
        name="_statesml_Edge__statesml_Edge20 _statesml_Function__statesml_Function",
        statesml_SystemUnit=None,
    )
    assert isinstance(var_17, python_code_.statesml_SystemUnit)
    var_31 = python_code_.statesml_NewEClass22()
    var_32 = python_code_.statesml_Event(
        name=complex(-1248.4328, 215.82149), statesml_Event=var_31
    )
    assert isinstance(var_32, python_code_.statesml_Event)
    python_code_.statesml_Trigger(statesml_Trigger11=var_32)


def test_33():
    var_2 = python_code_.KeyValuePair()
    var_3 = float
    var_4 = python_code_.statesml_Edge(
        name=var_3, statesml_Edge=var_3, statesml_Edge17=var_2
    )
    assert isinstance(var_4, python_code_.statesml_Edge)


@pytest.mark.xfail(strict=True)
def test_34():
    var_4 = "qHIJ_p\n3ZJZPpG-"
    var_5 = python_code_.statesml_Node(name=set())
    assert isinstance(var_5, python_code_.statesml_Node)
    python_code_.statesml_Edge(name=var_4, statesml_Edge=var_4, statesml_Edge20=var_5)


def test_35():
    var_17 = python_code_.statesml_SystemUnit(
        name="`FSD\t4]#wH", statesml_SystemUnit24=set()
    )
    assert isinstance(var_17, python_code_.statesml_SystemUnit)
    var_20 = "_statesml_Node__Node"
    var_21 = python_code_.statesml_DataTypeLibrary(name=var_20)
    assert isinstance(var_21, python_code_.statesml_DataTypeLibrary)
    var_22 = python_code_.State
    python_code_.statesml_Edge(name=var_20, statesml_Edge20=var_22)


def test_36():
    var_17 = python_code_.statesml_SystemUnit(
        name="pM-9w%<*G-%usw",
        statesml_SystemUnit27={"Tk>^yEzCwZTk5j\rt6T", 260},
        statesml_SystemUnit39=None,
    )
    assert isinstance(var_17, python_code_.statesml_SystemUnit)


def test_37():
    var_5 = python_code_.statesml_SystemUnitLibrary(
        name="_statesml_Function__statesml_Function35_statesml_KeyValuePair__statesml_KeyValuePair",
        statesml_SystemUnitLibrary={True, 129.48},
    )
    assert isinstance(var_5, python_code_.statesml_SystemUnitLibrary)


def test_38():
    var_17 = python_code_.statesml_SystemUnit(
        name="F&sq,~nRk",
        statesml_SystemUnit24={5434.23, "statesml_SystemUnit39"},
        statesml_SystemUnit39=None,
    )
    assert isinstance(var_17, python_code_.statesml_SystemUnit)


@pytest.mark.xfail(strict=True)
def test_39():
    var_1 = "statesml_RegularState"
    var_2 = python_code_.statesml_SystemUnitLibrary(name=var_1)
    assert isinstance(var_2, python_code_.statesml_SystemUnitLibrary)
    var_6 = python_code_.statesml_Trigger(statesml_Trigger11=-4005.81)
    assert isinstance(var_6, python_code_.statesml_Trigger)
    var_11 = "_statesml_Function__statesml_Function35,statesml_Edge,_statesml_KeyValuePair__statesml_KeyValuePair,_statesml_Node__Node"
    var_12 = hash
    var_13 = python_code_.statesml_KeyValuePair(
        name=var_11, statesml_KeyValuePair=var_12
    )
    assert isinstance(var_13, python_code_.statesml_KeyValuePair)
    python_code_.statesml_DataType(name=var_1, statesml_DataType37=var_13)


@pytest.mark.xfail(strict=True)
def test_40():
    python_code_.statesml_Trigger(statesml_Trigger11=None)
    var_18 = python_code_.statesml_Node(
        name='N9"J\x0coI\\L6.W-rL', statesml_Node21=None
    )
    assert isinstance(var_18, python_code_.statesml_Node)
    python_code_.statesml_Edge(
        name="_statesml_Node__statesml_Node21 Transition _statesml_Node__node",
        statesml_Edge17=var_18,
    )


def test_41():
    var_5 = python_code_.statesml_SystemUnitLibrary(name="statesml_SystemUnit39")
    assert isinstance(var_5, python_code_.statesml_SystemUnitLibrary)
    var_7 = python_code_.NewEnum1.LITERAL1
    var_8 = "LRlouwrgDT!lwPKq"
    var_9 = python_code_.statesml_SystemUnit(
        name=var_8,
        statesml_SystemUnit=var_7,
        statesml_SystemUnit27=var_8,
        statesml_SystemUnit39=var_5,
    )
    assert isinstance(var_9, python_code_.statesml_SystemUnit)


def test_42():
    var_8 = python_code_.statesml_Function(
        name="_statesml_Edge__statesml_Edge20-_statesml_Event__statesml_Event-statesml_DataType",
        statesml_Function=None,
        statesml_Function30=set(),
    )
    assert isinstance(var_8, python_code_.statesml_Function)


@pytest.mark.xfail(strict=True)
def test_43():
    var_7 = python_code_.statesml_DataTypeLibrary(
        name="``'BH@U\"=\rwc0\n^;", statesml_DataTypeLibrary={283.09}
    )
    assert isinstance(var_7, python_code_.statesml_DataTypeLibrary)
    var_16 = "statesml_StatesMLModel_statesml_KeyValuePair__statesml_KeyValuePair"
    var_17 = python_code_.statesml_Trigger(statesml_Trigger11=var_16)
    assert isinstance(var_17, python_code_.statesml_Trigger)
    python_code_.statesml_Event(name=var_16, statesml_Event=var_17)


@pytest.mark.xfail(strict=True)
def test_44():
    var_0 = python_code_.State()
    var_2 = lambda *args, **kwargs: 2
    var_3 = python_code_.statesml_RegularState()
    var_4 = "DEvy\t:\x0c-(V{N38q1Bcm"
    var_5 = python_code_.statesml_SystemUnit(
        name=var_4,
        statesml_SystemUnit27=("O#\\=1dVcI\x0br};.3", "@rR", True),
        statesml_SystemUnit39=complex(-198.26931, -1115.4693),
    )
    assert isinstance(var_5, python_code_.statesml_SystemUnit)
    var_6 = python_code_.statesml_Function(
        name=var_2, statesml_Function=var_3, statesml_Function28=var_5
    )
    assert isinstance(var_6, python_code_.statesml_Function)
    var_8 = python_code_.statesml_Event(name=var_4)
    assert isinstance(var_8, python_code_.statesml_Event)
    var_10 = python_code_.statesml_SystemUnitLibrary(name=var_0)
    assert isinstance(var_10, python_code_.statesml_SystemUnitLibrary)
    var_16 = python_code_.statesml_KeyValuePair(name=var_4)
    assert isinstance(var_16, python_code_.statesml_KeyValuePair)
    var_17 = python_code_.statesml_DataType(
        name=var_4, statesml_DataType37=complex(695.85127, 652.8312409)
    )
    assert isinstance(var_17, python_code_.statesml_DataType)
    python_code_.statesml_Trigger(statesml_Trigger11=var_8)


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = python_code_.statesml_Parameter()
    var_1 = python_code_.statesml_Event(name=var_0)
    assert isinstance(var_1, python_code_.statesml_Event)
    var_2 = python_code_.statesml_Constant()
    var_3 = python_code_.State
    var_4 = ""
    var_5 = python_code_.statesml_Edge(name=var_4, statesml_Edge20=var_2)
    python_code_.statesml_Node(
        name=("2I_sZx.i", 91), statesml_Node=var_3, statesml_Node21=var_5
    )


def test_46():
    var_20 = "W(F\x0cI2sG~7\tkD"
    var_21 = python_code_.statesml_DataType(name=var_20, statesml_DataType=var_20)
    assert isinstance(var_21, python_code_.statesml_DataType)
    var_22 = python_code_.statesml_Function(name=5979.29, statesml_Function35=var_21)
    assert isinstance(var_22, python_code_.statesml_Function)


@pytest.mark.xfail(strict=True)
def test_47():
    var_4 = "?OQ{yhR+{%|1+t{Az\\]"
    var_5 = python_code_.statesml_Node(name=var_4)
    assert isinstance(var_5, python_code_.statesml_Node)
    var_6 = python_code_.statesml_NewEClass3()
    var_8 = python_code_.statesml_Node(name=var_4, statesml_Node18=var_6)
    python_code_.statesml_Edge(name=var_4, statesml_Edge17=var_8)


@pytest.mark.xfail(strict=True)
def test_48():
    var_0 = "_statesml_Edge__statesml_Edge"
    var_1 = python_code_.statesml_DataTypeLibrary
    var_2 = python_code_.statesml_DataType(name=var_0, statesml_DataType41=var_1)
    assert isinstance(var_2, python_code_.statesml_DataType)
    python_code_.statesml_SystemUnit(
        name=-1027.32, statesml_SystemUnit27=var_1, statesml_SystemUnit39=var_1
    )


@pytest.mark.xfail(strict=True)
def test_49():
    var_17 = python_code_.statesml_SystemUnit(name="Vn-?p", statesml_SystemUnit24=set())
    assert isinstance(var_17, python_code_.statesml_SystemUnit)
    var_35 = '1IO-Ebv*"'
    var_36 = python_code_.statesml_Transition()
    var_37 = python_code_.statesml_StatesMLModel()
    var_38 = python_code_.statesml_Edge(
        name=var_17,
        statesml_Edge=var_37,
        statesml_Edge17=complex(-1181.756, 1111.11872),
    )
    assert isinstance(var_38, python_code_.statesml_Edge)
    python_code_.statesml_Node(name=var_35, Node=var_36, statesml_Node18=var_38)
