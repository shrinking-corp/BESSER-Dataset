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
    Constraint,
    Expression,
    PrologExpression,
    date,
    datetime,
    tExp_AndExpr,
    tExp_AtomExpression,
    tExp_Cardinality,
    tExp_CatExpr,
    tExp_Channel,
    tExp_Constraint,
    tExp_Domainmodel,
    tExp_EventType,
    tExp_Expression,
    tExp_FilterExpr,
    tExp_ListExpression,
    tExp_Msg,
    tExp_NumberExpression,
    tExp_Partition,
    tExp_PrologExpression,
    tExp_Role,
    tExp_SeqExpr,
    tExp_ShuffleExpr,
    tExp_Singletons,
    tExp_Size,
    tExp_StringExpression,
    tExp_Term,
    tExp_TerminalExpr,
    tExp_Together,
    tExp_TraceExpression,
    tExp_UnionExpr,
    tExp_VarExpr,
    tExp_VariableExpression,
    time,
)


def test_0():
    var_4 = -1
    var_5 = python_code_.tExp_Cardinality(minCardinality=var_4, maxCardinality=var_4)
    assert isinstance(var_5, python_code_.tExp_Cardinality)
    var_23 = python_code_.tExp_AtomExpression(atom=-2599.61)
    assert isinstance(var_23, python_code_.tExp_AtomExpression)


def test_1():
    var_0 = 3451
    var_1 = python_code_.tExp_Cardinality(minCardinality=1795, maxCardinality=var_0)
    assert isinstance(var_1, python_code_.tExp_Cardinality)
    var_3 = python_code_.tExp_VarExpr()
    var_8 = python_code_.tExp_AtomExpression(
        atom="e$G{F/K|j<T", tExp_AtomExpression=var_3
    )
    assert isinstance(var_8, python_code_.tExp_AtomExpression)


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = python_code_.tExp_VariableExpression(name=None)
    assert isinstance(var_1, python_code_.tExp_VariableExpression)
    var_3 = python_code_.tExp_ShuffleExpr()
    var_5 = 964
    var_6 = python_code_.tExp_Cardinality(minCardinality=var_3, maxCardinality=var_5)
    assert isinstance(var_6, python_code_.tExp_Cardinality)
    var_7 = "tExp_Msg59 tExp_PrologExpression31 tExp_PrologExpression3 tExp_Role60"
    var_8 = lambda *args, **kwargs: [274.1, "#k]wG{g&tFSA+"]
    var_9 = python_code_.tExp_Channel(name=var_7, reliability=var_8)
    var_11 = python_code_.tExp_FilterExpr()
    var_15 = python_code_.tExp_Expression(
        operator="%euZ~ \t \x0c",
        eps=var_7,
        variable="tExp_PrologExpression72tExp_UnionExpr102tExp_ListExpression",
        tExp_Expression24=var_9,
        tExp_Expression30={1805.66, "]fyF\t\x0b1`t6fZJCx%{g"},
        tExp_Expression34=None,
        tExp_Expression40=None,
        tExp_Expression98=var_3,
        tExp_Expression100=None,
    )
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    python_code_.tExp_Expression(
        operator=complex(1348.91167, 1941.759151),
        eps={},
        variable=var_7,
        tExp_Expression22=var_15,
        tExp_Expression32=var_15,
        tExp_Expression95=var_8,
        tExp_Expression117=var_11,
        tExp_Expression100='^"vm uK\x0c',
    )


def test_3():
    var_2 = ""
    var_3 = False
    var_6 = python_code_.tExp_Partition()
    var_7 = {var_6, var_6, var_6, var_6}
    var_15 = "PNoG!^Nf8\x0c6"
    python_code_.tExp_EventType(name=var_15, tExp_EventType54=[], tExp_EventType25={})
    var_17 = python_code_.tExp_CatExpr()
    var_18 = python_code_.tExp_Expression(
        operator=b"x\x95\xdb\xcbZ\xa6\x16'_.)\xabyJ\x91\x11\x13",
        eps=var_7,
        variable=None,
        tExp_Expression=(-2068.49,),
        tExp_Expression36=var_3,
        tExp_Expression46=var_6,
        tExp_Expression108={"", False},
        tExp_Expression113=var_17,
    )
    assert isinstance(var_18, python_code_.tExp_Expression)
    var_24 = python_code_.tExp_AtomExpression(atom=var_2)
    assert isinstance(var_24, python_code_.tExp_AtomExpression)


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.tExp_Together()
    var_2 = 2657
    var_3 = python_code_.tExp_Cardinality(minCardinality={}, maxCardinality=var_2)
    assert isinstance(var_3, python_code_.tExp_Cardinality)
    var_4 = python_code_.tExp_CatExpr()
    var_6 = python_code_.tExp_StringExpression(value=var_3)
    assert isinstance(var_6, python_code_.tExp_StringExpression)
    var_7 = ""
    python_code_.tExp_Channel(name=var_0, reliability=var_7, tExp_Channel57=-619)
    var_12 = python_code_.Constraint
    var_13 = "tExp_PrologExpression88_tExp_Expression__tExp_Expression_tExp_PrologExpression__tExp_PrologExpression75"
    var_14 = ""
    var_15 = python_code_.tExp_Expression(
        operator=var_6,
        eps=[],
        variable=var_14,
        tExp_Expression20=var_12,
        tExp_Expression95={},
        tExp_Expression100=var_12,
        tExp_Expression110=662.5,
    )
    var_16 = lambda *args, **kwargs: True
    var_17 = python_code_.tExp_AndExpr()
    python_code_.tExp_Expression(
        operator=var_13,
        eps=var_4,
        variable=var_14,
        tExp_Expression20=var_15,
        tExp_Expression32="J!T",
        tExp_Expression40=True,
        tExp_Expression46=var_13,
        tExp_Expression44=var_15,
        tExp_Expression117=var_16,
        tExp_Expression98=None,
        tExp_Expression105=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_1 = python_code_.tExp_VariableExpression(name=None)
    assert isinstance(var_1, python_code_.tExp_VariableExpression)
    var_2 = python_code_.tExp_SeqExpr()
    var_3 = python_code_.tExp_ShuffleExpr()
    var_4 = python_code_.PrologExpression()
    var_5 = 964
    var_6 = python_code_.tExp_Cardinality(minCardinality=var_3, maxCardinality=var_5)
    assert isinstance(var_6, python_code_.tExp_Cardinality)
    var_7 = "tExp_Msg59 tExp_PrologExpression31 tExp_PrologExpression3 tExp_Role60"
    var_8 = lambda *args, **kwargs: [274.1, "#k]wG{g&tFSA+"]
    python_code_.tExp_Channel(name=var_7, reliability=var_8)
    var_10 = "q0j/U,/\rgX%h"
    var_11 = python_code_.tExp_FilterExpr()
    var_12 = python_code_.tExp_AndExpr()
    var_13 = python_code_.tExp_AndExpr()
    var_14 = python_code_.tExp_CatExpr()
    var_15 = python_code_.tExp_Expression(
        operator=var_10,
        eps=var_10,
        variable=var_7,
        tExp_Expression32=var_4,
        tExp_Expression38=var_2,
        tExp_Expression95=var_4,
        tExp_Expression117=var_11,
        tExp_Expression98=var_3,
        tExp_Expression100={},
        tExp_Expression103=var_8,
        tExp_Expression105=var_12,
        tExp_Expression108=var_13,
        tExp_Expression110=var_7,
        tExp_Expression113=var_14,
    )
    assert isinstance(var_15.tExp_Expression38, python_code_.tExp_SeqExpr)
    python_code_.tExp_Expression(
        operator=complex(1348.91167, 1941.759151),
        eps={},
        variable=var_7,
        tExp_Expression22=var_15,
        tExp_Expression32=var_15,
        tExp_Expression95=var_8,
        tExp_Expression117=var_11,
        tExp_Expression100='^"vm uK\x0c',
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_1 = python_code_.tExp_VariableExpression(name=None)
    assert isinstance(var_1, python_code_.tExp_VariableExpression)
    var_2 = python_code_.tExp_SeqExpr()
    var_3 = python_code_.tExp_ShuffleExpr()
    var_4 = python_code_.PrologExpression()
    var_5 = 964
    var_6 = python_code_.tExp_Cardinality(minCardinality=var_3, maxCardinality=var_5)
    assert isinstance(var_6, python_code_.tExp_Cardinality)
    var_7 = "tExp_Msg59 tExp_PrologExpression31 tExp_PrologExpression3 tExp_Role60"
    var_8 = lambda *args, **kwargs: [274.1, "#k]wG{g&tFSA+"]
    python_code_.tExp_Channel(name=var_7, reliability=var_8)
    var_10 = "q0j/U,/\rgX%h"
    var_11 = python_code_.tExp_FilterExpr()
    var_12 = python_code_.tExp_AndExpr()
    var_13 = python_code_.tExp_AndExpr()
    var_14 = python_code_.tExp_CatExpr()
    var_15 = python_code_.tExp_Expression(
        operator=var_10,
        eps=var_10,
        variable=var_7,
        tExp_Expression32=var_4,
        tExp_Expression38=var_2,
        tExp_Expression95=var_4,
        tExp_Expression117=var_11,
        tExp_Expression98=var_3,
        tExp_Expression100={},
        tExp_Expression103=var_8,
        tExp_Expression105=var_12,
        tExp_Expression108=var_13,
        tExp_Expression110=var_7,
        tExp_Expression113=var_14,
    )
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    python_code_.tExp_Expression(
        operator=complex(1348.91167, 1941.759151),
        eps={},
        variable=var_7,
        tExp_Expression22=var_15,
        tExp_Expression32=var_15,
        tExp_Expression95=var_8,
        tExp_Expression117=var_11,
        tExp_Expression100='^"vm uK\x0c',
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_2 = 2657
    var_3 = python_code_.tExp_Cardinality(minCardinality={}, maxCardinality=var_2)
    assert isinstance(var_3, python_code_.tExp_Cardinality)
    var_4 = python_code_.tExp_CatExpr()
    var_6 = python_code_.tExp_StringExpression(value=var_3)
    assert isinstance(var_6, python_code_.tExp_StringExpression)
    var_22 = ';B"j?.[!#?-f'
    var_23 = "eJ<yFYFlUZ"
    var_24 = bool
    var_25 = 'Web".d:'
    var_26 = python_code_.tExp_ListExpression()
    var_27 = "tExp_PrologExpression49"
    var_28 = python_code_.tExp_SeqExpr()
    var_29 = python_code_.tExp_Expression(
        operator=b"\xc1\xd4\xcbD\xb0\xbc\xa6\x10\x8e[\xe1.\xc7\xd1\xc6\xfc",
        eps=var_24,
        variable=var_22,
        tExp_Expression34=var_4,
        tExp_Expression119=var_2,
        tExp_Expression121=False,
        tExp_Expression115=var_28,
    )
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    var_30 = "+he_Z0]"
    var_31 = python_code_.tExp_PrologExpression(
        op=var_30, tExp_PrologExpression28=var_4, tExp_PrologExpression93=var_26
    )
    var_32 = python_code_.tExp_ShuffleExpr()
    python_code_.tExp_Expression(
        operator=var_23,
        eps=b"\x93\xb5\xcb7oG{\x0b\x9a\x85a",
        variable=var_27,
        tExp_Expression=var_25,
        tExp_Expression22=var_29,
        tExp_Expression27=var_31,
        tExp_Expression42=(),
        tExp_Expression95=var_32,
        tExp_Expression117=var_2,
        tExp_Expression108=var_24,
        tExp_Expression110=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = "_Hsh}daFJ3=t<{i"
    var_1 = "_tExp_Role__tExp_Role86tExp_PrologExpression52tExp_Expression24_tExp_Expression__tExp_Expression44"
    var_2 = lambda *args, **kwargs: False
    var_3 = "M{JC2U?2Jnn*8L"
    var_4 = "_tExp_TraceExpression__tExp_TraceExpression15._tExp_Expression__tExp_Expression103.tExp_Constraint85._tExp_Expression__tExp_Expression121"
    var_5 = python_code_.Expression
    var_6 = "_tExp_TraceExpression__tExp_TraceExpression7"
    var_7 = '\rG"'
    var_8 = python_code_.tExp_Domainmodel()
    var_9 = python_code_.tExp_TraceExpression(
        name=var_3,
        bodyL=var_3,
        rolesL=var_0,
        typesL=1865,
        modulesL=var_4,
        modules=var_0,
        decentralizedL=False,
        decentralized=var_1,
        partitionL=var_5,
        constraintsL=var_5,
        guiL=var_0,
        gui=var_6,
        minimalL=var_7,
        minimal=var_3,
        thresholdL=var_3,
        threshold=var_3,
        channelsL=var_5,
        tExp_TraceExpression=var_8,
    )
    var_10 = python_code_.tExp_EventType(name=None, tExp_EventType=var_9)
    var_11 = python_code_.tExp_ShuffleExpr()
    var_12 = python_code_.tExp_SeqExpr()
    python_code_.tExp_Expression(
        operator=var_0,
        eps=var_0,
        variable=var_1,
        tExp_Expression=set(),
        tExp_Expression22=var_2,
        tExp_Expression20=complex(1131.0811047, -3322.2),
        tExp_Expression24=var_10,
        tExp_Expression32=var_4,
        tExp_Expression98=var_11,
        tExp_Expression115=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_4 = ""
    var_5 = python_code_.tExp_PrologExpression
    python_code_.tExp_Channel(name=var_4, reliability="?[IRNc", tExp_Channel57=None)
    var_8 = python_code_.tExp_AtomExpression(atom=1787)
    assert isinstance(var_8, python_code_.tExp_AtomExpression)
    var_13 = "_tExp_TraceExpression__tExp_TraceExpression7"
    var_14 = lambda *args, **kwargs: "5"
    var_15 = python_code_.tExp_Expression(
        operator=b"A\xb5T-.\xc7#\xe2\xa0\xb4",
        eps=var_13,
        variable=True,
        tExp_Expression22=None,
        tExp_Expression27=var_14,
        tExp_Expression34=var_4,
        tExp_Expression36=var_8,
        tExp_Expression40=var_5,
        tExp_Expression42=var_5,
        tExp_Expression44=None,
        tExp_Expression95=None,
        tExp_Expression117=None,
        tExp_Expression119=None,
        tExp_Expression121=None,
    )
    assert isinstance(var_15, python_code_.tExp_Expression)
    python_code_.tExp_EventType(
        name=-1506.24, tExp_EventType37=var_15, tExp_EventType51=var_15
    )


def test_10():
    var_0 = python_code_.tExp_AndExpr()
    var_1 = python_code_.tExp_Cardinality(minCardinality=True, maxCardinality=var_0)
    assert isinstance(var_1, python_code_.tExp_Cardinality)
    var_4 = ';B"j?.[!#?-f'
    var_34 = "tExp_Msg59 tExp_PrologExpression31 tExp_PrologExpression3 tExp_Role60"
    var_35 = lambda *args, **kwargs: [274.1, "#k]wG{g&tFSA+"]
    var_36 = python_code_.tExp_Channel(name=var_34, reliability=var_35)
    var_37 = "q0j/U,/\rgX%h"
    var_41 = python_code_.tExp_CatExpr()
    python_code_.tExp_EventType(name=var_36)
    python_code_.tExp_Msg(
        performative=var_35, tExp_Msg59=var_35, tExp_Msg62=(True, -1342.56)
    )
    var_46 = python_code_.tExp_VariableExpression(name=b"^y\xcf")
    assert isinstance(var_46, python_code_.tExp_VariableExpression)
    var_49 = python_code_.tExp_ShuffleExpr()
    var_61 = python_code_.tExp_UnionExpr()
    python_code_.tExp_Expression(
        operator=None,
        eps=var_37,
        variable=var_35,
        tExp_Expression34=var_35,
        tExp_Expression36=var_41,
        tExp_Expression40=var_35,
        tExp_Expression44=var_35,
        tExp_Expression95=var_49,
        tExp_Expression100=var_61,
        tExp_Expression110=b"\xe8\xf5<",
    )
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    python_code_.tExp_Term(name=var_4)
    python_code_.tExp_StringExpression(value=var_35)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = "_Hsh}daFJ3=t<{i"
    var_1 = "_tExp_Role__tExp_Role86tExp_PrologExpression52tExp_Expression24_tExp_Expression__tExp_Expression44"
    var_2 = lambda *args, **kwargs: False
    var_3 = "M{JC2U?2Jnn*8L"
    var_4 = "_tExp_TraceExpression__tExp_TraceExpression15._tExp_Expression__tExp_Expression103.tExp_Constraint85._tExp_Expression__tExp_Expression121"
    var_5 = python_code_.Expression
    var_6 = "_tExp_TraceExpression__tExp_TraceExpression7"
    var_7 = '\rG"'
    var_8 = python_code_.tExp_Domainmodel()
    var_9 = python_code_.tExp_TraceExpression(
        name=var_3,
        bodyL=var_3,
        rolesL=var_0,
        typesL=1865,
        modulesL=var_4,
        modules=var_0,
        decentralizedL=False,
        decentralized=var_1,
        partitionL=var_5,
        constraintsL=var_5,
        guiL=var_0,
        gui=var_6,
        minimalL=var_7,
        minimal=var_3,
        thresholdL=var_3,
        threshold=var_3,
        channelsL=var_5,
        tExp_TraceExpression=var_8,
    )
    var_10 = python_code_.tExp_EventType(name=None, tExp_EventType=var_9)
    var_11 = python_code_.tExp_ShuffleExpr()
    var_12 = python_code_.tExp_SeqExpr()
    python_code_.tExp_Expression(
        operator=var_0,
        eps=var_0,
        variable=var_1,
        tExp_Expression=set(),
        tExp_Expression22=var_2,
        tExp_Expression20=complex(1131.0811047, -3322.2),
        tExp_Expression24=var_10,
        tExp_Expression32=var_4,
        tExp_Expression98=var_11,
        tExp_Expression115=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.tExp_Together()
    var_2 = 2657
    var_3 = python_code_.tExp_Cardinality(minCardinality={}, maxCardinality=var_2)
    assert isinstance(var_3, python_code_.tExp_Cardinality)
    var_4 = python_code_.tExp_CatExpr()
    var_5 = python_code_.tExp_UnionExpr()
    var_6 = python_code_.tExp_StringExpression(value="TZ:<Yv-C <g-kt")
    assert isinstance(var_6, python_code_.tExp_StringExpression)
    var_7 = ""
    var_8 = python_code_.tExp_Channel(
        name=var_0, reliability=var_7, tExp_Channel57=-619
    )
    var_9 = python_code_.tExp_FilterExpr()
    var_15 = python_code_.tExp_Expression(
        operator=var_7,
        eps="H#CFlxI\\OQ;TO",
        variable="l:'",
        tExp_Expression42=None,
        tExp_Expression46=var_8,
        tExp_Expression117=None,
        tExp_Expression119=var_7,
        tExp_Expression121=None,
        tExp_Expression98=var_8,
        tExp_Expression100=var_5,
        tExp_Expression108=var_3,
        tExp_Expression113=var_4,
        tExp_Expression115=var_9,
    )
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    var_21 = python_code_.tExp_ListExpression()
    python_code_.tExp_PrologExpression(
        op=b"*",
        tExp_PrologExpression90=var_21,
        tExp_PrologExpression1={-1184.7, -297, 2215},
        tExp_PrologExpression28=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_1 = python_code_.tExp_VariableExpression(name=None)
    assert isinstance(var_1, python_code_.tExp_VariableExpression)
    var_3 = python_code_.tExp_ShuffleExpr()
    var_5 = 964
    var_6 = python_code_.tExp_Cardinality(minCardinality=var_3, maxCardinality=var_5)
    assert isinstance(var_6, python_code_.tExp_Cardinality)
    var_7 = "tExp_Msg59 tExp_PrologExpression31 tExp_PrologExpression3 tExp_Role60"
    var_8 = lambda *args, **kwargs: [274.1, "#k]wG{g&tFSA+"]
    python_code_.tExp_Channel(name=var_7, reliability=var_8)
    var_13 = python_code_.tExp_AndExpr()
    var_51 = "tExp_Constraint85,_tExp_Role__tExp_Role,_tExp_PrologExpression__tExp_PrologExpression72,_tExp_Expression__tExp_Expression24"
    var_52 = "5Q}e\rP|0h"
    var_53 = "_tExp_Role__tExp_Role"
    var_54 = "tExp_Expression42-tExp_PrologExpression75-_tExp_EventType__tExp_EventType51-_tExp_PrologExpression__tExp_PrologExpression3"
    var_55 = python_code_.tExp_Expression(
        operator=var_52,
        eps=var_53,
        variable=var_54,
        tExp_Expression22=var_7,
        tExp_Expression38=var_8,
        tExp_Expression42=var_8,
        tExp_Expression100=var_13,
        tExp_Expression108=var_13,
    )
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    python_code_.tExp_Term(name=var_51, tExp_Term19=var_55)


def test_14():
    var_0 = "vr#"
    var_1 = "E:LdE5]P%\n>Du7"
    var_2 = "hi0p6\tD;.*Gp81O"
    var_3 = "h'?hpmxwr#86#{SG"
    var_4 = lambda *args, **kwargs: "tExp_Term,_tExp_Expression__tExp_Expression38"
    var_5 = "+SKxa*~HJ"
    var_6 = "9CjU8xxIp"
    var_7 = "MDr"
    var_8 = python_code_.tExp_Channel(name=var_7, reliability=None, tExp_Channel=var_0)
    var_9 = {var_8, var_8}
    python_code_.tExp_TraceExpression(
        name=var_1,
        bodyL=var_2,
        rolesL=var_2,
        typesL=var_3,
        modulesL=var_0,
        modules=set(),
        decentralizedL=var_4,
        decentralized=(),
        partitionL="_tExp_Role__tExp_Role83",
        constraintsL=var_4,
        guiL=var_3,
        gui=var_1,
        minimalL=var_5,
        minimal=[],
        thresholdL=var_4,
        threshold=var_6,
        channelsL=var_2,
        tExp_TraceExpression17=var_9,
        tExp_TraceExpression7=var_9,
    )


def test_15():
    var_0 = python_code_.tExp_Together()
    var_2 = 2657
    var_3 = python_code_.tExp_Cardinality(minCardinality={}, maxCardinality=var_2)
    assert isinstance(var_3, python_code_.tExp_Cardinality)
    var_6 = python_code_.tExp_StringExpression(value=var_3)
    assert isinstance(var_6, python_code_.tExp_StringExpression)
    var_7 = "r"
    python_code_.tExp_Channel(name=var_0, reliability=var_7, tExp_Channel57=-619)
    var_23 = python_code_.tExp_NumberExpression(value=complex(2048.0, -990.4324))
    assert isinstance(var_23, python_code_.tExp_NumberExpression)
    var_24 = 4339
    var_25 = 1525
    var_26 = python_code_.tExp_Size(minSize=var_24, maxSize=var_25)
    assert isinstance(var_26, python_code_.tExp_Size)


def test_16():
    var_5 = python_code_.tExp_ListExpression()
    var_7 = "_tExp_TraceExpression__tExp_TraceExpression17:_tExp_TraceExpression__tExp_TraceExpression17:tExp_PrologExpression31:tExp_AndExpr107"
    python_code_.tExp_Msg(performative=var_7, tExp_Msg68=var_5)
    var_32 = "tExp_Msg59 tExp_PrologExpression31 tExp_PrologExpression3 tExp_Role60"
    var_33 = lambda *args, **kwargs: [274.1, "#k]wG{g&tFSA+"]
    python_code_.tExp_Channel(name=var_32, reliability=var_33)


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = ".I1>hL?9DAmJ"
    var_1 = (
        "_tExp_EventType__tExp_EventType56-tExp_Msg68-_tExp_EventType__tExp_EventType51"
    )
    var_2 = ""
    var_3 = "tExp_PrologExpression31,tExp_Expression27"
    var_4 = ")kLL"
    var_5 = list
    var_6 = python_code_.tExp_Partition()
    var_7 = {var_6, var_6, var_6, var_6}
    var_8 = python_code_.tExp_TraceExpression(
        name=var_0,
        bodyL=var_1,
        rolesL=["yUc;.O#G?(y<X", -86, 4684],
        typesL=var_2,
        modulesL=var_2,
        modules=var_2,
        decentralizedL=var_1,
        decentralized={},
        partitionL=var_1,
        constraintsL=var_3,
        guiL=var_3,
        gui=var_4,
        minimalL=var_3,
        minimal=var_2,
        thresholdL=var_3,
        threshold=var_5,
        channelsL=-307.15,
        tExp_TraceExpression13=var_7,
        tExp_TraceExpression7=var_7,
        tExp_TraceExpression9=var_7,
    )
    var_9 = python_code_.PrologExpression
    var_10 = python_code_.tExp_Role(
        name=var_8, class_=var_5, args=var_4, tExp_Role86=var_9, tExp_Role60=2752.74
    )
    python_code_.tExp_Msg(performative=var_2, tExp_Msg=var_5, tExp_Msg68=var_10)


def test_18():
    var_2 = 2657
    var_3 = python_code_.tExp_Cardinality(minCardinality={}, maxCardinality=var_2)
    assert isinstance(var_3, python_code_.tExp_Cardinality)
    var_25 = python_code_.Constraint
    var_28 = python_code_.tExp_Size(minSize=2020, maxSize=1963)
    assert isinstance(var_28, python_code_.tExp_Size)
    var_30 = "d<s=(1?Y"
    python_code_.tExp_Channel(name=var_30, reliability=b"\xfc\xe7\x0fJ")
    python_code_.tExp_Msg(
        performative=var_30,
        tExp_Msg62=var_25,
        tExp_Msg71=[],
        tExp_Msg74=complex(2956.028, 960.327),
    )
    var_34 = python_code_.tExp_AtomExpression(atom=var_25)
    assert isinstance(var_34, python_code_.tExp_AtomExpression)


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = python_code_.tExp_Together()
    var_1 = lambda *args, **kwargs: False
    var_2 = python_code_.tExp_AtomExpression(atom=var_1, tExp_AtomExpression=var_1)
    assert isinstance(var_2, python_code_.tExp_AtomExpression)
    python_code_.tExp_Term(name=var_0, tExp_Term43="z")
    var_5 = python_code_.tExp_ListExpression()
    var_6 = ">BshVe\x0bL_<h/00PGxF"
    var_7 = "_tExp_TraceExpression__tExp_TraceExpression17:_tExp_TraceExpression__tExp_TraceExpression17:tExp_PrologExpression31:tExp_AndExpr107"
    var_8 = python_code_.tExp_Msg(performative=var_7, tExp_Msg68=var_5)
    python_code_.tExp_Role(
        name=var_6,
        class_=complex(-270.0, -2663.746708),
        args=var_7,
        tExp_Role83=-1060.78,
        tExp_Role63=var_8,
    )


def test_20():
    var_1 = python_code_.tExp_Cardinality(minCardinality=-1, maxCardinality=-4036)
    assert isinstance(var_1, python_code_.tExp_Cardinality)
    var_12 = "~]$J}\\\r\x0cW\tN:RcY*Ix"
    python_code_.tExp_EventType(name=var_12, tExp_EventType48=1519)


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = python_code_.tExp_NumberExpression(value=134)
    assert isinstance(var_0, python_code_.tExp_NumberExpression)
    var_1 = python_code_.tExp_ShuffleExpr()
    var_2 = python_code_.PrologExpression()
    var_3 = python_code_.tExp_UnionExpr()
    var_4 = '9*oa~"2r'
    var_5 = "$<=gx4>\x0cL53`}"
    var_6 = "_tExp_PrologExpression__tExp_PrologExpression"
    var_7 = python_code_.tExp_ListExpression
    python_code_.tExp_TraceExpression(
        name=var_4,
        bodyL=var_5,
        rolesL=(
            ".VR#./<=,4`8QaIWu",
            "_tExp_EventType__tExp_EventType25 tExp_EventType56",
            413.72,
        ),
        typesL=var_6,
        modulesL=None,
        modules=var_1,
        decentralizedL="zl",
        decentralized=var_4,
        partitionL=var_7,
        constraintsL=var_3,
        guiL=True,
        gui=var_1,
        minimalL=var_4,
        minimal=var_4,
        thresholdL=var_0,
        threshold=var_6,
        channelsL=var_7,
    )
    var_11 = "qfs("
    var_13 = set()
    var_14 = python_code_.tExp_EventType(
        name=set(), tExp_EventType54=var_13, tExp_EventType51={}
    )
    var_15 = python_code_.tExp_PrologExpression(
        op=var_11,
        tExp_PrologExpression31=var_7,
        tExp_PrologExpression93=var_7,
        tExp_PrologExpression72=var_3,
    )
    python_code_.tExp_PrologExpression(
        op="_tExp_PrologExpression__tExp_PrologExpression",
        tExp_PrologExpression3=var_15,
    )
    python_code_.tExp_PrologExpression(
        op=var_13,
        tExp_PrologExpression=var_0,
        tExp_PrologExpression1=var_15,
        tExp_PrologExpression3=var_13,
        tExp_PrologExpression28=var_14,
        tExp_PrologExpression52=var_2,
        tExp_PrologExpression72=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = python_code_.tExp_NumberExpression(value=["tExp_PrologExpression5"])
    assert isinstance(var_0, python_code_.tExp_NumberExpression)
    var_1 = python_code_.tExp_CatExpr()
    var_2 = python_code_.tExp_PrologExpression
    var_3 = python_code_.tExp_Msg(performative=var_2)
    var_4 = "_tExp_Msg__tExp_Msg"
    var_5 = python_code_.tExp_Expression(
        operator=var_0,
        eps=var_3,
        variable=(True, "!TZn\r-)o"),
        tExp_Expression36=var_3,
        tExp_Expression42=b"\x16\x0b]N\x17J\x02\x07\xb0~\xbc\xdc\xd8~RVl\xd8",
        tExp_Expression46=var_3,
        tExp_Expression44=var_2,
        tExp_Expression100=var_4,
        tExp_Expression108={2500},
    )
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    var_6 = "D+,]W)rH/"
    var_7 = '/?0L1_`/"2r$'
    var_8 = "9JY"
    var_9 = "_tExp_Expression__tExp_Expression"
    var_10 = python_code_.tExp_TraceExpression(
        name=var_8,
        bodyL=b"\xf2",
        rolesL=var_4,
        typesL=var_1,
        modulesL=var_7,
        modules=None,
        decentralizedL={},
        decentralized=var_8,
        partitionL=var_6,
        constraintsL=var_2,
        guiL=var_7,
        gui=var_3,
        minimalL=var_2,
        minimal=var_3,
        thresholdL=var_6,
        threshold=var_8,
        channelsL=var_9,
        tExp_TraceExpression9=("+th&7\x0b]YvL", 'k1F"D6[eZ9', "tExp_Role66"),
    )
    var_11 = python_code_.tExp_EventType(
        name=var_7, tExp_EventType54=b"\xf1\xfc8<t]\xdcP", tExp_EventType=var_10
    )
    python_code_.tExp_PrologExpression(
        op=var_2,
        tExp_PrologExpression5=var_2,
        tExp_PrologExpression49=var_11,
        tExp_PrologExpression72=var_5,
        tExp_PrologExpression75=var_2,
    )


def test_23():
    var_1 = python_code_.tExp_Cardinality(minCardinality=-1, maxCardinality=-4036)
    assert isinstance(var_1, python_code_.tExp_Cardinality)
    var_3 = python_code_.tExp_ListExpression()
    var_4 = ';B"j?.[!#?-f'
    var_5 = "tExp_Role66.tExp_Together79.tExp_Domainmodel"
    var_6 = python_code_.tExp_EventType(name=var_5, tExp_EventType37=-1162)
    python_code_.tExp_PrologExpression(
        op=var_4,
        tExp_PrologExpression90=var_3,
        tExp_PrologExpression52=var_6,
        tExp_PrologExpression93=var_3,
    )
    assert isinstance(
        python_code_.tExp_PrologExpression.tExp_PrologExpression3,
        python_code_.tExp_PrologExpression,
    )
    var_12 = "~]$J}\\\r\x0cW\tN:RcY*Ix"
    python_code_.tExp_EventType(name=var_12, tExp_EventType48=1519)


def test_24():
    var_0 = "_Hsh}daFJ3=t<{i"
    var_1 = "_tExp_Role__tExp_Role86tExp_PrologExpression52tExp_Expression24_tExp_Expression__tExp_Expression44"
    var_3 = "M{JC2U?2Jnn*8L"
    var_4 = "_tExp_TraceExpression__tExp_TraceExpression15._tExp_Expression__tExp_Expression103.tExp_Constraint85._tExp_Expression__tExp_Expression121"
    var_5 = python_code_.Expression
    var_6 = "_tExp_TraceExpression__tExp_TraceExpression7"
    var_7 = '\rG"'
    var_8 = python_code_.tExp_Domainmodel()
    var_9 = python_code_.tExp_TraceExpression(
        name=var_3,
        bodyL=var_3,
        rolesL=var_0,
        typesL=1865,
        modulesL=var_4,
        modules=var_0,
        decentralizedL=False,
        decentralized=var_1,
        partitionL=var_5,
        constraintsL=var_5,
        guiL=var_0,
        gui=var_6,
        minimalL=var_7,
        minimal=var_3,
        thresholdL=var_3,
        threshold=var_3,
        channelsL=var_5,
        tExp_TraceExpression=var_8,
    )
    python_code_.tExp_EventType(name=None, tExp_EventType=var_9)
    python_code_.tExp_Term(name=var_4)


def test_25():
    var_1 = python_code_.tExp_VariableExpression(name=None)
    assert isinstance(var_1, python_code_.tExp_VariableExpression)
    var_48 = python_code_.tExp_AtomExpression
    var_58 = "_tExp_Channel__tExp_Channel"
    var_59 = "-g 0P?\\ Nc)Yl\nvZU6_"
    python_code_.tExp_Role(
        name=var_58, class_=[-3565, -3802, 382.07], args=var_59, tExp_Role69=var_48
    )


def test_26():
    var_0 = -542
    var_1 = python_code_.tExp_Cardinality(minCardinality=var_0, maxCardinality=var_0)
    assert isinstance(var_1, python_code_.tExp_Cardinality)
    var_4 = ""
    var_5 = python_code_.tExp_Expression
    python_code_.tExp_Channel(name=var_4, reliability=var_5, tExp_Channel=2872)
    var_8 = python_code_.tExp_AtomExpression(atom=1787)
    assert isinstance(var_8, python_code_.tExp_AtomExpression)
    var_9 = python_code_.tExp_Singletons
    var_11 = python_code_.tExp_ListExpression()
    var_34 = "tExp_Role66.tExp_Together79.tExp_Domainmodel"
    var_35 = python_code_.tExp_EventType(name=var_34, tExp_EventType37=-1162)
    python_code_.tExp_PrologExpression(
        op=var_4,
        tExp_PrologExpression90=var_11,
        tExp_PrologExpression52=var_35,
        tExp_PrologExpression93=var_11,
    )
    var_39 = "~]$J}\\\r\x0cW\tN:RcY*Ix"
    python_code_.tExp_EventType(name=var_39, tExp_EventType48=1519)
    var_44 = "7Z4"
    var_45 = "Egd@[Q0U6v%"
    python_code_.tExp_Role(
        name=var_44, class_=var_45, args=var_9, tExp_Role83=var_9, tExp_Role60=set()
    )


def test_27():
    var_1 = "E:LdE5]P%\n>Du7"
    var_12 = "!A2s6;E\nj/dXU6"
    var_13 = "_tExp_TrceExpression__tExp_TraceExpression13"
    var_16 = python_code_.tExp_Role(
        name=var_1,
        class_="_tExp_TraceExpression__tExp_TraceExpression9",
        args=var_12,
        tExp_Role83=var_1,
        tExp_Role63=None,
    )
    var_19 = {var_16}
    python_code_.tExp_Constraint(
        together=var_13,
        split=var_12,
        parMin=var_12,
        parMax={2360.33},
        tExp_Constraint82=var_19,
    )


def test_28():
    var_1 = "_tExp_Role__tExp_Role86tExp_PrologExpression52tExp_Expression24_tExp_Expression__tExp_Expression44"
    var_5 = python_code_.Expression
    python_code_.tExp_Term(name=var_5, tExp_Term43=var_1)


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = python_code_.tExp_StringExpression(
        value=b"'*\xf8\x9c\xf9\xe2\x0c\xdf\x17t\x121s\rp\xfe\x86\x02"
    )
    assert isinstance(var_0, python_code_.tExp_StringExpression)
    var_2 = lambda *args, **kwargs: 1494
    var_3 = python_code_.tExp_Size(
        minSize=var_2, maxSize=complex(2005.30797, 2423.602418)
    )
    assert isinstance(var_3, python_code_.tExp_Size)
    var_4 = -1
    var_5 = python_code_.tExp_Cardinality(minCardinality=var_4, maxCardinality=var_4)
    assert isinstance(var_5, python_code_.tExp_Cardinality)
    var_7 = python_code_.tExp_PrologExpression(
        op=var_2,
        tExp_PrologExpression1=2,
        tExp_PrologExpression49=var_4,
        tExp_PrologExpression93={},
    )
    python_code_.tExp_PrologExpression(
        op=var_3,
        tExp_PrologExpression5=var_7,
        tExp_PrologExpression3=var_7,
        tExp_PrologExpression28=var_3,
    )
    assert isinstance(var_7.tExp_PrologExpression3, python_code_.tExp_PrologExpression)
    python_code_.tExp_EventType(
        name=var_2, tExp_EventType54=var_2, tExp_EventType48=var_7
    )


def test_30():
    var_0 = python_code_.tExp_StringExpression(
        value=b"'*\xf8\x9c\xf9\xe2\x0c\xdf\x17t\x121s\rp\xfe\x86\x02"
    )
    assert isinstance(var_0, python_code_.tExp_StringExpression)
    var_2 = lambda *args, **kwargs: 1494
    var_3 = python_code_.tExp_Size(
        minSize=var_2, maxSize=complex(2005.30797, 2423.602418)
    )
    assert isinstance(var_3, python_code_.tExp_Size)
    var_4 = -1
    var_5 = python_code_.tExp_Cardinality(minCardinality=var_4, maxCardinality=var_4)
    assert isinstance(var_5, python_code_.tExp_Cardinality)
    var_7 = python_code_.tExp_PrologExpression(
        op=var_2,
        tExp_PrologExpression1=2,
        tExp_PrologExpression49=var_4,
        tExp_PrologExpression93={},
    )
    python_code_.tExp_PrologExpression(
        op=var_3,
        tExp_PrologExpression5=var_7,
        tExp_PrologExpression3=var_7,
        tExp_PrologExpression28=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_31():
    var_0 = -542
    var_1 = python_code_.tExp_Cardinality(minCardinality=var_0, maxCardinality=var_0)
    assert isinstance(var_1, python_code_.tExp_Cardinality)
    var_2 = python_code_.Constraint()
    var_4 = ""
    var_5 = python_code_.tExp_Expression
    python_code_.tExp_Channel(name=var_4, reliability=var_5, tExp_Channel=2872)
    python_code_.tExp_Term(name=None)
    var_8 = python_code_.tExp_AtomExpression(atom=1787)
    assert isinstance(var_8, python_code_.tExp_AtomExpression)
    var_10 = "m3L;"
    var_11 = python_code_.tExp_ListExpression()
    var_13 = "_tExp_TraceExpression__tExp_TraceExpression7"
    var_14 = lambda *args, **kwargs: "5"
    var_15 = python_code_.tExp_Expression(
        operator=b"A\xb5T-.\xc7#\xe2\xa0\xb4",
        eps=var_13,
        variable=True,
        tExp_Expression22=None,
        tExp_Expression27=var_14,
        tExp_Expression34=var_4,
        tExp_Expression36=var_8,
        tExp_Expression40=var_5,
        tExp_Expression42=var_5,
        tExp_Expression44=None,
        tExp_Expression95=None,
        tExp_Expression117=None,
        tExp_Expression119=None,
        tExp_Expression121=None,
    )
    assert isinstance(var_15, python_code_.tExp_Expression)
    var_16 = python_code_.tExp_PrologExpression(
        op=True,
        tExp_PrologExpression=var_2,
        tExp_PrologExpression31=var_15,
        tExp_PrologExpression93=var_11,
    )
    assert isinstance(var_16, python_code_.tExp_PrologExpression)
    assert isinstance(
        python_code_.tExp_PrologExpression.tExp_PrologExpression3,
        python_code_.tExp_PrologExpression,
    )
    var_17 = {var_16, var_16}
    var_18 = python_code_.tExp_ShuffleExpr()
    var_19 = python_code_.tExp_AndExpr()
    var_20 = python_code_.tExp_CatExpr()
    python_code_.tExp_Expression(
        operator=var_11,
        eps=-227.35,
        variable=-1567.29,
        tExp_Expression22=var_5,
        tExp_Expression27=var_5,
        tExp_Expression30=var_17,
        tExp_Expression98=var_18,
        tExp_Expression105=var_5,
        tExp_Expression108=var_19,
        tExp_Expression110=[906, 105],
        tExp_Expression113=var_20,
    )
    python_code_.tExp_EventType(
        name=var_10,
        tExp_EventType37=var_15,
        tExp_EventType48="_T^}gM/d\n",
        tExp_EventType51=var_19,
    )


def test_32():
    var_0 = python_code_.tExp_AndExpr()
    var_1 = python_code_.tExp_Cardinality(minCardinality=True, maxCardinality=var_0)
    assert isinstance(var_1, python_code_.tExp_Cardinality)


def test_33():
    var_0 = python_code_.tExp_StringExpression(
        value=b"'*\xf8\x9c\xf9\xe2\x0c\xdf\x17t\x121s\rp\xfe\x86\x02"
    )
    assert isinstance(var_0, python_code_.tExp_StringExpression)
    var_3 = python_code_.tExp_Size(minSize=1813, maxSize=-290)
    assert isinstance(var_3, python_code_.tExp_Size)
    var_4 = -1
    var_5 = python_code_.tExp_Cardinality(minCardinality=var_4, maxCardinality=var_4)
    assert isinstance(var_5, python_code_.tExp_Cardinality)
    var_23 = python_code_.tExp_AtomExpression(atom=-2599.61)
    assert isinstance(var_23, python_code_.tExp_AtomExpression)


def test_34():
    var_1 = lambda *args, **kwargs: False
    var_5 = python_code_.tExp_ListExpression()
    var_7 = "_tExp_TraceExpression__tExp_TraceExpression17:_tExp_TraceExpression__tExp_TraceExpression17:tExp_PrologExpression31:tExp_AndExpr107"
    python_code_.tExp_Msg(performative=var_7, tExp_Msg68=var_5)
    var_13 = python_code_.tExp_AtomExpression(atom=True, tExp_AtomExpression=var_1)
    assert isinstance(var_13, python_code_.tExp_AtomExpression)
    var_14 = python_code_.tExp_Cardinality(minCardinality=None, maxCardinality={})
    assert isinstance(var_14, python_code_.tExp_Cardinality)
    var_15 = python_code_.tExp_NumberExpression(value=complex(2048.0, -990.4324))
    assert isinstance(var_15, python_code_.tExp_NumberExpression)
    var_16 = 4339
    var_17 = 1525
    var_18 = python_code_.tExp_Size(minSize=var_16, maxSize=var_17)
    assert isinstance(var_18, python_code_.tExp_Size)


@pytest.mark.xfail(strict=True)
def test_35():
    var_3 = "_tExp_Expression__tExp_Expression20:_tExp_Expression__tExp_Expression"
    var_6 = "NwXN0D~q}\x0c"
    python_code_.tExp_Term(
        name="'%cBU20_!we_J3t>4/\t", tExp_Term19=var_6, tExp_Term43=var_3
    )
    var_8 = ""
    var_55 = "_tExp_PrologExpression__tExp_PrologExpression93"
    var_56 = "hKeGwA6\x0b~l>kQ\x0b\x0b_["
    var_57 = "Cb()p$:G@yl,'i"
    var_58 = python_code_.tExp_PrologExpression(op=var_57, tExp_PrologExpression90=())
    var_59 = {var_58, var_58, var_58, var_58, var_58}
    var_60 = "8"
    var_61 = python_code_.tExp_Term(name=var_60)
    var_62 = python_code_.tExp_ShuffleExpr()
    var_63 = python_code_.tExp_UnionExpr()
    var_64 = python_code_.tExp_CatExpr()
    python_code_.tExp_Expression(
        operator=var_8,
        eps=var_55,
        variable=var_56,
        tExp_Expression30=var_59,
        tExp_Expression42=var_61,
        tExp_Expression46=var_57,
        tExp_Expression95=var_62,
        tExp_Expression117=var_56,
        tExp_Expression103=var_63,
        tExp_Expression110=var_64,
        tExp_Expression115=1379.46,
    )


@pytest.mark.xfail(strict=True)
def test_36():
    var_4 = ""
    var_5 = python_code_.tExp_Expression
    python_code_.tExp_Channel(name=var_4, reliability=var_5, tExp_Channel=2872)
    var_8 = python_code_.tExp_AtomExpression(atom=1787)
    assert isinstance(var_8, python_code_.tExp_AtomExpression)
    var_13 = "_tExp_TraceExpression__tExp_TraceExpression7"
    var_14 = lambda *args, **kwargs: "5"
    var_15 = python_code_.tExp_Expression(
        operator=b"A\xb5T-.\xc7#\xe2\xa0\xb4",
        eps=var_13,
        variable=True,
        tExp_Expression22=None,
        tExp_Expression27=var_14,
        tExp_Expression34=var_4,
        tExp_Expression36=var_8,
        tExp_Expression40=var_5,
        tExp_Expression42=var_5,
        tExp_Expression44=None,
        tExp_Expression95=None,
        tExp_Expression117=None,
        tExp_Expression119=None,
        tExp_Expression121=None,
    )
    assert isinstance(var_15, python_code_.tExp_Expression)
    python_code_.tExp_EventType(
        name=-1506.24, tExp_EventType37=var_15, tExp_EventType51=var_15
    )


def test_37():
    var_0 = python_code_.tExp_AndExpr()
    var_1 = python_code_.tExp_Cardinality(minCardinality=True, maxCardinality=var_0)
    assert isinstance(var_1, python_code_.tExp_Cardinality)
    var_23 = "{'# m^=ZcP{"
    var_24 = "yq,X8sELRh\\"
    python_code_.tExp_Constraint(
        together=var_23, split=None, parMin=-1561.23, parMax=var_24
    )


@pytest.mark.xfail(strict=True)
def test_38():
    var_17 = "?"
    var_19 = python_code_.Constraint
    var_22 = python_code_.tExp_Size(minSize=2020, maxSize=1963)
    assert isinstance(var_22, python_code_.tExp_Size)
    var_24 = "d<s=(1?Y"
    python_code_.tExp_Channel(name=var_24, reliability=b"\xfc\xe7\x0fJ")
    var_26 = python_code_.tExp_Msg(
        performative=var_24,
        tExp_Msg62=var_19,
        tExp_Msg71=[],
        tExp_Msg74=complex(2956.028, 960.327),
    )
    python_code_.tExp_Role(
        name=var_17,
        class_=var_19,
        args=var_19,
        tExp_Role60=var_26,
        tExp_Role66=var_26,
        tExp_Role69=var_26,
    )


@pytest.mark.xfail(strict=True)
def test_39():
    var_0 = "O"
    var_1 = python_code_.tExp_StringExpression
    var_2 = 'gT7=\tL\\|+O"kdhZ{'
    var_3 = "_tExp_Expression__tExp_Expression20:_tExp_Expression__tExp_Expression"
    var_5 = "_tExp_TraceExpression__tExp_TraceExpression7:tExp_Expression24:_tExp_TraceExpression__tExp_TraceExpression13:_tExp_Role__tExp_Role80"
    var_6 = "NwXN0D~q}\x0c"
    var_7 = python_code_.tExp_Term(name=-69, tExp_Term=var_1, tExp_Term43=None)
    var_8 = ""
    var_9 = python_code_.tExp_UnionExpr()
    var_10 = python_code_.tExp_Expression(
        operator=var_0,
        eps=var_1,
        variable=var_8,
        tExp_Expression24=var_5,
        tExp_Expression27="c",
        tExp_Expression34=var_5,
        tExp_Expression95=1653,
        tExp_Expression117=var_1,
        tExp_Expression98=var_2,
        tExp_Expression100=var_0,
        tExp_Expression103=var_9,
    )
    assert isinstance(var_10, python_code_.tExp_Expression)
    assert isinstance(
        python_code_.tExp_Expression.tExp_Expression38, python_code_.tExp_Expression
    )
    var_11 = python_code_.tExp_VarExpr()
    python_code_.tExp_Expression(
        operator={-1578},
        eps=var_2,
        variable=var_6,
        tExp_Expression=var_7,
        tExp_Expression30=var_3,
        tExp_Expression32=var_5,
        tExp_Expression46=var_10,
        tExp_Expression119=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_40():
    var_2 = "Hy<S*?T\tJ!4G"
    var_3 = python_code_.tExp_Cardinality(minCardinality={}, maxCardinality=var_2)
    assert isinstance(var_3, python_code_.tExp_Cardinality)
    var_4 = python_code_.tExp_CatExpr()
    var_6 = python_code_.tExp_StringExpression(value=var_3)
    assert isinstance(var_6, python_code_.tExp_StringExpression)
    var_12 = python_code_.Constraint
    var_13 = "tExp_PrologExpression88_tExp_Expression__tExp_Expression_tExp_PrologExpression__tExp_PrologExpression75"
    var_14 = ""
    var_15 = python_code_.tExp_Expression(
        operator=var_6,
        eps=[],
        variable=var_14,
        tExp_Expression20=var_12,
        tExp_Expression95={},
        tExp_Expression100=var_12,
        tExp_Expression110=662.5,
    )
    var_16 = lambda *args, **kwargs: True
    var_17 = python_code_.tExp_AndExpr()
    python_code_.tExp_Expression(
        operator=var_13,
        eps=var_4,
        variable=var_14,
        tExp_Expression20=var_15,
        tExp_Expression32="J!T",
        tExp_Expression40=True,
        tExp_Expression46=var_13,
        tExp_Expression44=var_15,
        tExp_Expression117=var_16,
        tExp_Expression98=None,
        tExp_Expression105=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_1 = python_code_.tExp_StringExpression
    var_3 = "_tExp_Expression__tExp_Expression20:_tExp_Expression__tExp_Expression"
    var_4 = '?"\r[+!VZyVd@R.)G>U$'
    var_6 = "NwXN0D~q}\x0c"
    python_code_.tExp_Term(
        name="'%cBU20_!we_J3t>4/\t", tExp_Term19=var_6, tExp_Term43=var_3
    )
    var_57 = "Cb()p$:G@yl,'i"
    var_58 = python_code_.tExp_PrologExpression(op=var_57, tExp_PrologExpression90=())
    assert isinstance(
        python_code_.tExp_PrologExpression.tExp_PrologExpression3,
        python_code_.tExp_PrologExpression,
    )
    var_59 = {var_58, var_58, var_58, var_58, var_58}
    var_60 = "8"
    python_code_.tExp_Term(name=var_60)
    var_62 = python_code_.tExp_ShuffleExpr()
    var_64 = python_code_.tExp_CatExpr()
    var_15 = python_code_.tExp_ShuffleExpr
    var_67 = "Ig,m^IDN/ujt85&$"
    var_68 = "eO][\x0c\x0bUi@S\t,$U "
    var_69 = "tExp_Role86"
    python_code_.tExp_TraceExpression(
        name=None,
        bodyL=var_64,
        rolesL=var_60,
        typesL=var_1,
        modulesL=var_67,
        modules=var_68,
        decentralizedL=var_4,
        decentralized=var_1,
        partitionL=var_62,
        constraintsL=b"_FD\xd8b\xa9\xf8",
        guiL=(),
        gui=var_69,
        minimalL=var_15,
        minimal={},
        thresholdL=var_1,
        threshold={"": False},
        channelsL=var_3,
        tExp_TraceExpression15=var_59,
        tExp_TraceExpression7=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_42():
    var_0 = python_code_.tExp_ShuffleExpr()
    var_2 = "{Wd"
    var_3 = python_code_.tExp_AtomExpression(atom=var_2)
    assert isinstance(var_3, python_code_.tExp_AtomExpression)
    var_4 = -4054
    var_5 = python_code_.tExp_Size(minSize=var_4, maxSize=var_4)
    assert isinstance(var_5, python_code_.tExp_Size)
    var_6 = python_code_.tExp_Singletons(minSingletons=var_5, maxSingletons=var_4)
    assert isinstance(var_6, python_code_.tExp_Singletons)
    var_7 = python_code_.tExp_Term(name=var_2)
    var_8 = "v6L7OC@T0DNV\n_1"
    var_9 = python_code_.tExp_NumberExpression(value=var_8)
    assert isinstance(var_9, python_code_.tExp_NumberExpression)
    var_10 = "lA::]J02i<0n]P"
    python_code_.tExp_Expression(
        operator=var_3,
        eps=None,
        variable=var_10,
        tExp_Expression=var_7,
        tExp_Expression42=var_4,
        tExp_Expression119=var_0,
        tExp_Expression98="Xi[ 534$",
        tExp_Expression103={True, False},
    )
