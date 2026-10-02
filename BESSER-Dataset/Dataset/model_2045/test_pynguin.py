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
    ActorCommunicationType,
    ActorContainerClass,
    ActorContainerRef,
    CommunicationType,
    ComplexType,
    DataType,
    Enum,
    InterfaceItem,
    NonInitialTransition,
    Operation,
    RoomClass,
    SAPoint,
    State,
    StateGraphItem,
    StateGraphNode,
    StructureClass,
    TrPoint,
    Transition,
    TransitionChainStartTransition,
    TransitionTerminal,
    date,
    datetime,
    room_ActorClass,
    room_ActorContainerClass,
    room_ActorContainerRef,
    room_ActorInstancePath,
    room_ActorRef,
    room_Annotation,
    room_Attribute,
    room_BaseState,
    room_Binding,
    room_BindingEndPoint,
    room_CPBranchTransition,
    room_ChoicePoint,
    room_ChoicepointTerminal,
    room_ComplexType,
    room_ContinuationTransition,
    room_DataClass,
    room_DataType,
    room_DetailCode,
    room_Documentation,
    room_EntryPoint,
    room_ExitPoint,
    room_ExternalPort,
    room_ExternalType,
    room_Guard,
    room_GuardedTransition,
    room_Import,
    room_InitialTransition,
    room_InterfaceItem,
    room_KeyValue,
    room_LayerConnection,
    room_LogicalSystem,
    room_LogicalThread,
    room_Message,
    room_MessageFromIf,
    room_MessageHandler,
    room_NonInitialTransition,
    room_Operation,
    room_Port,
    room_PortClass,
    room_PortOperation,
    room_PrimitiveType,
    room_ProtocolClass,
    room_ProtocolSemantics,
    room_RefSAPoint,
    room_RefableType,
    room_RefinedState,
    room_RelaySAPoint,
    room_RoomClass,
    room_RoomModel,
    room_SAPRef,
    room_SAPoint,
    room_SPPRef,
    room_SPPoint,
    room_SemanticsRule,
    room_ServiceImplementation,
    room_StandardOperation,
    room_State,
    room_StateGraph,
    room_StateGraphItem,
    room_StateGraphNode,
    room_StateTerminal,
    room_StructureClass,
    room_SubStateTrPointTerminal,
    room_SubSystemClass,
    room_SubSystemRef,
    room_TrPoint,
    room_TrPointTerminal,
    room_Transition,
    room_TransitionChainStartTransition,
    room_TransitionPoint,
    room_TransitionTerminal,
    room_Trigger,
    room_TriggeredTransition,
    room_VarDecl,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.room_DataClass()
    var_1 = python_code_.TrPoint()
    var_2 = python_code_.room_Import(
        importedNamespace=var_0, importURI=var_1, room_Import=var_1
    )
    var_3 = True
    var_4 = python_code_.room_TransitionPoint(handler=var_3)
    assert isinstance(var_4, python_code_.room_TransitionPoint)
    var_6 = python_code_.RoomClass()
    var_7 = python_code_.room_LayerConnection()
    var_13 = python_code_.room_RoomClass(name=var_7)
    var_14 = True
    var_15 = lambda *args, **kwargs: 1637
    var_16 = python_code_.room_ProtocolClass(
        commType=689.18,
        room_ProtocolClass=var_0,
        room_ProtocolClass72=var_15,
        room_ProtocolClass77=var_2,
        room_ProtocolClass89=complex(-2234.0, 1185.3157),
    )
    assert isinstance(var_16, python_code_.room_ProtocolClass)
    python_code_.room_Message(priv=var_14, name=var_6, room_Message87=var_16)
    python_code_.room_Documentation(
        text=1511.61,
        room_Documentation18=var_13,
        room_Documentation133=var_6,
        room_Documentation160=None,
    )


def test_1():
    var_0 = python_code_.room_DataClass()
    var_1 = python_code_.TrPoint()
    var_2 = python_code_.room_Import(
        importedNamespace=var_0, importURI=var_1, room_Import=var_1
    )
    var_3 = True
    var_4 = python_code_.room_TransitionPoint(handler=var_3)
    assert isinstance(var_4, python_code_.room_TransitionPoint)
    var_6 = python_code_.RoomClass()
    var_7 = python_code_.room_LayerConnection()
    python_code_.room_RoomClass(name=var_7)
    var_14 = True
    var_15 = lambda *args, **kwargs: 1637
    var_16 = python_code_.room_ProtocolClass(
        commType=689.18,
        room_ProtocolClass=var_0,
        room_ProtocolClass72=var_15,
        room_ProtocolClass77=var_2,
        room_ProtocolClass89=complex(-2234.0, 1185.3157),
    )
    assert isinstance(var_16, python_code_.room_ProtocolClass)
    python_code_.room_Message(priv=var_14, name=var_6, room_Message87=var_16)
    var_31 = python_code_.room_StateGraph()
    var_32 = python_code_.room_StateGraphItem()
    var_32.getName()
    var_34 = python_code_.room_State(room_State221=var_31)
    assert isinstance(var_34, python_code_.room_State)
    var_34.getName()


@pytest.mark.xfail(strict=True)
def test_2():
    var_2 = True
    var_3 = "room_SubSystemClass178room_ChoicePoint_room_ActorClass__room_ActorClass150"
    var_4 = python_code_.room_ChoicePoint(name=var_3)
    assert isinstance(var_4, python_code_.room_ChoicePoint)
    var_6 = python_code_.room_State(room_State=var_4, room_State218=var_2)
    assert isinstance(var_6, python_code_.room_State)
    var_6.getName()
    var_14 = "+_[q"
    var_15 = python_code_.room_Transition(name=var_14, room_Transition=-1)
    assert isinstance(var_15, python_code_.room_Transition)
    python_code_.room_Documentation(
        text="c3(h",
        room_Documentation148=set(),
        room_Documentation57={
            "_room_TrPoint__room_TrPoint": 1891,
            "Og3'i\x0b$0@\\\x0b#9?o)": "or[T-'6Ar$U6N$E@f ",
        },
        room_Documentation240=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = "=ON3*# HYe,\x0b1|%6\\"
    var_1 = True
    var_2 = "2Iv3+&\t7!BX p"
    var_3 = lambda *args, **kwargs: 4717
    var_4 = python_code_.room_StateGraph()
    var_5 = python_code_.room_State(
        room_State215=var_3, room_State221=var_4, room_State225=var_4
    )
    assert isinstance(var_5, python_code_.room_State)
    var_6 = var_5.getName()
    var_7 = python_code_.room_RoomModel(
        name=var_0, room_RoomModel2=var_2, room_RoomModel16=var_6
    )
    assert isinstance(var_7, python_code_.room_RoomModel)
    var_8 = var_5.getName()
    var_9 = python_code_.room_ActorClass(
        abstract=var_1,
        commType=var_2,
        room_ActorClass=var_7,
        room_ActorClass135=var_8,
        room_ActorClass155=var_4,
        room_ActorClass208=var_3,
    )
    assert isinstance(var_9, python_code_.room_ActorClass)
    python_code_.room_Documentation(
        text=var_0,
        room_Documentation=None,
        room_Documentation133=var_9,
        room_Documentation210=var_5,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    python_code_.room_ActorInstancePath(segments={})
    var_10 = "\\Sle'z?"
    var_11 = python_code_.room_Transition(name="7\x0cph(|\nT}8")
    assert isinstance(var_11, python_code_.room_Transition)
    var_13 = python_code_.ActorCommunicationType.DATA_DRIVEN
    var_17 = 1
    var_18 = python_code_.room_Attribute(
        name=var_10,
        size=var_17,
        defaultValueLiteral="?SZc58Wuc\nH\\TK4YKP&",
        room_Attribute145=var_10,
    )
    python_code_.room_Documentation(text=var_13, room_Documentation57=var_18)


def test_5():
    python_code_.room_ActorInstancePath(segments={})
    var_1 = "room_Documentation148"
    python_code_.room_Operation(name=var_1, room_Operation61={2779.41, 2443, -38.31})
    var_6 = python_code_.ActorCommunicationType
    python_code_.room_RefableType(ref=var_6)
    var_9 = python_code_.room_RoomModel(
        name=var_6, room_RoomModel8=var_6, room_RoomModel10=var_6
    )
    assert isinstance(var_9, python_code_.room_RoomModel)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.room_StateGraphItem()
    var_1 = var_0.getName()
    python_code_.room_InterfaceItem(name=940.34, room_InterfaceItem=var_1)
    var_10 = "qZ]D"
    python_code_.room_Documentation(text=var_10)
    var_20 = python_code_.room_StandardOperation()
    var_25 = "LV{t%-fw"
    var_26 = python_code_.room_ProtocolSemantics
    python_code_.room_RoomModel(
        name=var_25,
        room_RoomModel=var_26,
        room_RoomModel6=var_20,
        room_RoomModel12=var_1,
    )


def test_7():
    var_1 = python_code_.room_StateGraphItem()
    var_2 = var_1.getName()
    var_3 = python_code_.room_State(
        room_State225={
            "_room_Message__room_Message122:room_ActorClass130": "_room_RoomModel__room_RoomModel4._room_Operation__room_Operation67._room_TrPoint__room_TrPoint254",
            "room_SemanticsRule121": 3565,
            "_room_DetailCode__room_DetailCode274 _room_VarDecl__room_VarDecl59 room_PortClass102": 3,
        }
    )
    assert isinstance(var_3, python_code_.room_State)
    var_4 = var_3.getName()
    var_5 = var_3.getName()
    var_6 = python_code_.room_RoomModel(
        name={79.45, False},
        room_RoomModel2=var_2,
        room_RoomModel4=var_4,
        room_RoomModel10=var_5,
    )
    assert isinstance(var_6, python_code_.room_RoomModel)
    var_23 = (
        "_room_ProtocolClass__room_ProtocolClass83:_room_Transition__room_Transition237"
    )
    var_24 = python_code_.room_StateGraph()
    python_code_.room_State(
        room_State=-1507, room_State221=var_24, room_State225=var_24
    )
    var_26 = python_code_.room_PrimitiveType(
        targetName=True, castName=var_23, defaultValueLiteral=var_4
    )
    assert isinstance(var_26, python_code_.room_PrimitiveType)


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = "_room_ActorClass__room_ActorClass138"
    var_1 = python_code_.room_Annotation(name=var_0)
    var_6 = python_code_.room_Transition(name="7\x0cph(|\nT}8")
    assert isinstance(var_6, python_code_.room_Transition)
    var_8 = python_code_.ActorCommunicationType.DATA_DRIVEN
    var_10 = python_code_.room_BaseState(name=var_1)
    assert isinstance(var_10, python_code_.room_BaseState)
    var_11 = "iP k\r\\C\r.l=\rPt"
    var_12 = float
    var_13 = 1
    var_14 = python_code_.room_Attribute(
        name=var_12, size=var_13, defaultValueLiteral=var_11
    )
    python_code_.room_Documentation(text=var_8, room_Documentation57=var_14)


def test_9():
    var_1 = python_code_.room_ActorContainerClass
    var_2 = python_code_.room_BaseState(name=[";1D{k1k"], room_BaseState259=var_1)
    assert isinstance(var_2, python_code_.room_BaseState)
    var_3 = python_code_.room_TrPoint(
        name=var_1, room_TrPoint=complex(-3223.8864101, 2329.88658)
    )
    assert isinstance(var_3, python_code_.room_TrPoint)
    var_5 = python_code_.room_GuardedTransition()
    var_6 = "/Vfuq3"
    python_code_.room_InterfaceItem(name=var_6)
    var_8 = python_code_.room_SubStateTrPointTerminal()
    var_9 = python_code_.room_ExternalPort()
    var_10 = python_code_.room_Port(conjugated=var_1, multiplicity=var_8)
    assert isinstance(var_10, python_code_.room_Port)
    var_11 = python_code_.SAPoint()
    var_12 = python_code_.room_DataClass()
    var_13 = python_code_.room_MessageHandler()
    python_code_.room_DetailCode(
        commands=var_6,
        room_DetailCode41=var_11,
        room_DetailCode47=var_12,
        room_DetailCode117=var_13,
        room_DetailCode75=var_9,
        room_DetailCode243=False,
        room_DetailCode219=var_1,
        room_DetailCode248=var_5,
    )
    python_code_.room_State()
    var_20 = False
    var_21 = python_code_.DataType
    python_code_.room_Message(
        priv=var_20,
        name=var_21,
        room_Message114=var_21,
        room_Message122=var_1,
        room_Message87=var_21,
    )


@pytest.mark.xfail(strict=True)
def test_10():
    python_code_.room_ActorInstancePath(segments={})
    var_10 = python_code_.room_Transition(name="7\x0cph(|\nT}8")
    assert isinstance(var_10, python_code_.room_Transition)
    var_15 = float
    python_code_.room_LogicalThread(name=[], prio="`x|=S")
    python_code_.room_RefableType(ref=var_15)
    python_code_.room_RoomModel(
        name=var_15, room_RoomModel8=var_15, room_RoomModel10=var_15
    )


def test_11():
    var_3 = lambda *args, **kwargs: 4717
    var_4 = python_code_.room_StateGraph()
    var_5 = python_code_.room_State(
        room_State215=var_3, room_State221=var_4, room_State225=var_4
    )
    assert isinstance(var_5, python_code_.room_State)
    var_5.getName()


def test_12():
    var_0 = "room_Operation61:room_Documentation57:room_RoomModel:_room_DetailCode__room_DetailCode250"
    python_code_.room_Annotation(name=var_0)
    var_46 = python_code_.room_StateGraph()
    var_47 = python_code_.room_State(
        room_State=-1507, room_State221=var_46, room_State225=var_46
    )
    assert isinstance(var_47, python_code_.room_State)
    var_48 = "st!$A"
    var_49 = "room_State"
    var_50 = python_code_.room_VarDecl
    var_51 = python_code_.room_Operation(
        name=var_49, room_Operation64=(), room_Operation67=var_50
    )
    python_code_.room_VarDecl(name=var_48, room_VarDecl59=var_51)


def test_13():
    var_0 = python_code_.room_SubStateTrPointTerminal()
    var_3 = python_code_.room_State(
        room_State212=var_0, room_State215=None, room_State225=None
    )
    assert isinstance(var_3, python_code_.room_State)
    var_3.getName()
    var_26 = python_code_.room_StateGraph()
    python_code_.room_State(
        room_State=-1507, room_State221=var_26, room_State225=var_26
    )


def test_14():
    var_14 = "+_[q"
    var_15 = python_code_.room_Transition(name=var_14, room_Transition=-1)
    assert isinstance(var_15, python_code_.room_Transition)
    var_33 = float
    var_34 = 1
    python_code_.room_Attribute(name=var_33, size=var_34, defaultValueLiteral=var_14)


def test_15():
    python_code_.room_ActorInstancePath(segments={})


def test_16():
    var_0 = "room_Operation61:room_Documentation57:room_RoomModel:_room_DetailCode__room_DetailCode250"
    python_code_.room_Annotation(name=var_0)


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = python_code_.RoomClass()
    var_4 = -1824
    var_5 = python_code_.room_StateGraph()
    var_6 = python_code_.room_State(room_State225=var_5)
    assert isinstance(var_6, python_code_.room_State)
    var_7 = var_6.getName()
    var_8 = var_6.getName()
    python_code_.room_ActorClass(
        abstract=var_4,
        commType=[-2669, 1706.14, False],
        room_ActorClass=var_0,
        room_ActorClass128="8l<\n!V?XUXMO`usOo",
        room_ActorClass135=var_7,
        room_ActorClass144=var_5,
        room_ActorClass150=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = python_code_.room_ActorInstancePath(segments={})
    var_1 = "room_Documentation148"
    var_2 = True
    var_3 = python_code_.room_Operation(
        name=var_1, room_Operation61={2779.41, 2443, -38.31}
    )
    python_code_.room_RefableType(
        ref=var_2, room_RefableType54=var_0, room_RefableType62=var_3
    )


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = python_code_.room_TriggeredTransition()
    var_4 = python_code_.ActorContainerClass()
    var_5 = False
    var_6 = "yr"
    var_7 = python_code_.room_Attribute(
        name=True,
        size=var_5,
        defaultValueLiteral=var_6,
        room_Attribute145=var_4,
        room_Attribute=set(),
        room_Attribute56=var_0,
    )
    var_8 = lambda *args, **kwargs: "_room_Message__room_Message122room_DetailCode213"
    python_code_.room_RefableType(
        ref=var_5, room_RefableType54=var_7, room_RefableType62=var_8
    )


@pytest.mark.xfail(strict=True)
def test_20():
    var_1 = python_code_.room_ActorContainerClass
    var_2 = python_code_.room_BaseState(name=[";1D{k1k"], room_BaseState259=var_1)
    assert isinstance(var_2, python_code_.room_BaseState)
    var_3 = python_code_.room_TrPoint(
        name=var_1, room_TrPoint=complex(-3223.8864101, 2329.88658)
    )
    assert isinstance(var_3, python_code_.room_TrPoint)
    var_5 = python_code_.room_GuardedTransition()
    var_6 = "/Vfuq3"
    python_code_.room_InterfaceItem(name=var_6)
    var_8 = python_code_.room_SubStateTrPointTerminal()
    var_9 = python_code_.room_ExternalPort()
    var_10 = python_code_.room_Port(conjugated=var_1, multiplicity=var_8)
    assert isinstance(var_10, python_code_.room_Port)
    var_11 = python_code_.SAPoint()
    var_12 = python_code_.room_DataClass()
    var_13 = python_code_.room_MessageHandler()
    python_code_.room_DetailCode(
        commands=var_6,
        room_DetailCode41=var_11,
        room_DetailCode47=var_12,
        room_DetailCode117=var_13,
        room_DetailCode75=var_9,
        room_DetailCode243=False,
        room_DetailCode219=var_1,
        room_DetailCode248=var_5,
    )
    python_code_.room_Operation(name=var_6, room_Operation67=var_6)
    python_code_.room_State()
    var_20 = False
    var_21 = python_code_.DataType
    python_code_.room_Message(
        priv=var_20,
        name=var_21,
        room_Message114=var_21,
        room_Message122=var_1,
        room_Message87=var_21,
    )
    var_10.isReplicated()
    python_code_.room_LogicalThread(name=[], prio="`x|=S")
    var_27 = "}o\\O\x0cf%\nk"
    python_code_.room_Attribute(
        name=var_5,
        size=b"\x80\x88\xb9v/\xeb\x1f\xd9Ob\xd3\xe0}",
        defaultValueLiteral=var_27,
        room_Attribute53=var_1,
    )
    python_code_.room_RefableType(ref=var_1)
    python_code_.room_RoomModel(
        name=var_1, room_RoomModel8=var_1, room_RoomModel10=var_21
    )


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = python_code_.room_SubStateTrPointTerminal()
    var_3 = python_code_.room_State(
        room_State212=var_0, room_State215=None, room_State225=None
    )
    assert isinstance(var_3, python_code_.room_State)
    var_3.getName()
    var_24 = python_code_.room_DataClass()
    var_29 = python_code_.room_MessageHandler()
    var_30 = lambda *args, **kwargs: False
    var_31 = python_code_.room_PortClass()
    var_32 = python_code_.room_Guard()
    python_code_.room_DetailCode(
        commands=var_30,
        room_DetailCode47=var_24,
        room_DetailCode117=var_29,
        room_DetailCode103=var_31,
        room_DetailCode213=var_30,
        room_DetailCode274=var_32,
        room_DetailCode219=var_3,
        room_DetailCode250={
            "8/&wy": True,
            "dy&3dX$&xT2~A5$J": 2177,
            "-^.aK`T4K9Z2[&": -188,
        },
    )


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = "_room_DetailCode__room_DetailCode78._room_ActorClass__room_ActorClass128._room_Documentation__room_Documentation18"
    var_1 = python_code_.room_StateGraphItem()
    var_2 = var_1.getName()
    python_code_.room_ProtocolClass(
        commType=var_0,
        room_ProtocolClass72=[-981, -3853, 452],
        room_ProtocolClass83=var_2,
        room_ProtocolClass86=True,
        room_ProtocolClass89=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_23():
    python_code_.room_ActorInstancePath(segments="_room_Attribute__room_Attribute")
    var_1 = "room_Documentation148"
    python_code_.room_Operation(name=var_1, room_Operation61={2779.41, 2443, -38.31})
    var_6 = python_code_.ActorCommunicationType
    var_8 = python_code_.room_RefableType(ref=var_6)
    var_9 = python_code_.room_RoomModel(
        name=var_6, room_RoomModel8=var_6, room_RoomModel10=var_6
    )
    assert isinstance(var_9, python_code_.room_RoomModel)
    var_12 = "8\\E/M8Z4%|N+Nvtm"
    python_code_.room_ProtocolClass(
        commType=var_12,
        room_ProtocolClass74=var_8,
        room_ProtocolClass83=complex(2139.7796, -524.59),
    )


def test_24():
    var_1 = python_code_.room_StateGraphItem()
    var_2 = var_1.getName()
    var_3 = python_code_.room_State(
        room_State225={
            "_room_Message__room_Message122:room_ActorClass130": "_room_RoomModel__room_RoomModel4._room_Operation__room_Operation67._room_TrPoint__room_TrPoint254",
            "room_SemanticsRule121": 3565,
            "_room_DetailCode__room_DetailCode274 _room_VarDecl__room_VarDecl59 room_PortClass102": 3,
        }
    )
    assert isinstance(var_3, python_code_.room_State)
    var_4 = var_3.getName()
    var_5 = var_3.getName()
    var_6 = python_code_.room_RoomModel(
        name={79.45, False},
        room_RoomModel2=var_2,
        room_RoomModel4=var_4,
        room_RoomModel10=var_5,
    )
    assert isinstance(var_6, python_code_.room_RoomModel)


@pytest.mark.xfail(strict=True)
def test_25():
    var_0 = "_room_ActorClass__room_ActorClass138"
    python_code_.room_Annotation(name=var_0)
    var_31 = python_code_.room_ActorContainerClass()
    var_32 = python_code_.room_PortClass()
    var_47 = python_code_.room_StandardOperation()
    var_48 = python_code_.room_SemanticsRule()
    var_55 = (
        "_room_ProtocolClass__room_ProtocolClass83:_room_Transition__room_Transition237"
    )
    var_56 = python_code_.room_DetailCode(
        commands=var_47,
        room_DetailCode=-391,
        room_DetailCode27=var_31,
        room_DetailCode81=var_32,
        room_DetailCode216=var_32,
        room_DetailCode219=b"(14w5\xb46\xb7\xec\xc8\xc7\x1aS\xc1U",
        room_DetailCode250=var_48,
    )
    python_code_.room_Operation(name=var_55, room_Operation67=var_56)


@pytest.mark.xfail(strict=True)
def test_26():
    var_0 = "_room_ActorClass__room_ActorClass138"
    python_code_.room_Annotation(name=var_0)
    var_31 = True
    var_32 = python_code_.room_TransitionPoint(handler=var_31)
    assert isinstance(var_32, python_code_.room_TransitionPoint)
    var_35 = python_code_.room_LayerConnection()
    python_code_.room_RoomClass(name=var_35)
    var_43 = lambda *args, **kwargs: 1637
    var_54 = python_code_.room_StateGraphItem()
    var_55 = var_54.getName()
    var_56 = False
    var_57 = python_code_.room_RefableType(ref=var_56)
    var_58 = "&iZzT=l<b<*~/@WD&\t"
    var_59 = python_code_.room_ActorContainerClass()
    var_60 = python_code_.room_ActorContainerClass()
    var_61 = python_code_.room_Guard()
    var_62 = python_code_.room_DetailCode(
        commands=var_58,
        room_DetailCode=var_59,
        room_DetailCode27=var_59,
        room_DetailCode30=var_60,
        room_DetailCode117={1772.72, True, False},
        room_DetailCode274=var_61,
        room_DetailCode219=(),
    )
    python_code_.room_Operation(
        name=var_43,
        room_Operation=var_55,
        room_Operation61=var_57,
        room_Operation67=var_62,
    )


def test_27():
    var_0 = "_room_ActorClass__room_ActorClass138"
    python_code_.room_Annotation(name=var_0)
    python_code_.room_VarDecl(name=var_0)
    var_41 = python_code_.room_TransitionChainStartTransition()
    python_code_.room_ActorInstancePath(segments=var_41)
    python_code_.room_Operation(
        name=(2624, False), room_Operation61=complex(-880.51018, 1235.01)
    )


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = python_code_.room_ExternalPort()
    var_2 = python_code_.room_ChoicepointTerminal()
    var_4 = python_code_.room_SubSystemClass()
    var_7 = python_code_.ActorContainerRef()
    var_10 = python_code_.room_ActorContainerClass()
    var_11 = python_code_.room_StandardOperation
    var_12 = python_code_.room_ProtocolClass(
        commType=1251,
        room_ProtocolClass157=var_11,
        room_ProtocolClass74=var_10,
        room_ProtocolClass77=var_7,
        room_ProtocolClass94=var_0,
    )
    assert isinstance(var_12, python_code_.room_ProtocolClass)
    var_13 = python_code_.room_Guard()
    var_14 = "V4u{| 6_o{f"
    var_15 = python_code_.room_Transition(name=var_14)
    assert isinstance(var_15, python_code_.room_Transition)
    python_code_.room_DetailCode(
        commands=var_4,
        room_DetailCode=var_10,
        room_DetailCode47=var_11,
        room_DetailCode68=var_2,
        room_DetailCode75=var_12,
        room_DetailCode81=var_11,
        room_DetailCode274=var_13,
        room_DetailCode243=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = python_code_.room_RefSAPoint()
    var_1 = python_code_.room_ActorContainerClass()
    var_3 = python_code_.ActorContainerClass()
    var_6 = "(N;j^a%Ck\x0bZv udiR"
    var_7 = "8hU"
    var_8 = 3
    var_9 = lambda *args, **kwargs: []
    var_10 = python_code_.room_Attribute(
        name=var_7,
        size=var_8,
        defaultValueLiteral=var_9,
        room_Attribute145=var_3,
        room_Attribute=None,
        room_Attribute53=[],
    )
    var_11 = python_code_.room_ChoicePoint(name=var_0)
    assert isinstance(var_11, python_code_.room_ChoicePoint)
    var_12 = python_code_.room_Transition(name=var_7, room_Transition239=var_3)
    assert isinstance(var_12, python_code_.room_Transition)
    python_code_.room_Documentation(
        text=var_6,
        room_Documentation=var_1,
        room_Documentation133=set(),
        room_Documentation170=[],
        room_Documentation57=var_10,
        room_Documentation235=var_11,
        room_Documentation240=var_12,
    )
