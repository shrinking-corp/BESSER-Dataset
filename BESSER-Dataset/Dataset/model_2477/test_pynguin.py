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
    time,
    traceability_Category,
    traceability_DiffCategory,
    traceability_EObject,
    traceability_LogEntry,
    traceability_Trace,
    traceability_TraceComment,
    traceability_TraceDiff,
    traceability_TraceDiffs,
    traceability_Traces,
)


def test_0():
    var_1 = python_code_.traceability_Category(
        name="_traceability_TraceDiff__traceability_TraceDiff30"
    )
    assert isinstance(var_1, python_code_.traceability_Category)


def test_1():
    var_0 = python_code_.traceability_DiffCategory(
        name="_traceability_TraceComment__traceability_TraceComment36",
        modelIndex=1727,
        unequal=False,
        traceability_DiffCategory={"t<#4~", "ej"},
    )
    assert isinstance(var_0, python_code_.traceability_DiffCategory)


def test_2():
    var_0 = python_code_.traceability_DiffCategory(
        name="parent_traceability_Traces__traceability_Traces22traceability_EObject17_traceability_Trace__Trace8",
        modelIndex=1793,
        unequal=False,
    )
    assert isinstance(var_0, python_code_.traceability_DiffCategory)


def test_3():
    var_58 = python_code_.traceability_Traces(
        username="VZ\\.:..F0=$9\nL",
        fullName='+"-w-(gAXyaQS?q',
        date=None,
        location="\n<FQ2+f",
        comments="t\x0by9l?'\\2d95kyhRE",
        uriMap="_traceability_LogEntry__traceability_LogEntry-_traceability_Trace__traceability_Trace10-_traceability_Trace__traceability_Trace",
        originalSourceURL="E\x0cx",
        traceability_Traces22={2631.63, -1488.84, ""},
    )
    assert isinstance(var_58, python_code_.traceability_Traces)


def test_4():
    var_58 = python_code_.traceability_Traces(
        username="'cv+g8`7",
        fullName="traceability_EObject34",
        date=None,
        location="traceability_TraceDiff,_traceability_Trace__traceability_Trace10,traceability_EObject17,children",
        comments="-#}\rkS^",
        uriMap="`GkCQ",
        originalSourceURL="/!/+",
        traceability_Traces=None,
        traceability_Traces19=None,
    )
    assert isinstance(var_58, python_code_.traceability_Traces)


def test_5():
    var_34 = python_code_.traceability_LogEntry(
        message="_traceability_Category__traceability_Category _traceability_Traces__traceability_Traces traceability_EObject23 _traceability_Traces__traceability_Traces19",
        severity=266,
        messageType=-1956,
        comment="traceability_TraceDiffs,_traceability_Trace__traceability_Trace2",
        traceability_LogEntry={"vv#E_OCJy@f._6f", "=7k", "_nx$Yk"},
    )
    assert isinstance(var_34, python_code_.traceability_LogEntry)


def test_6():
    var_34 = python_code_.traceability_LogEntry(
        message="_traceability_TraceComment__traceability_TraceComment28._traceability_TraceComment__traceability_TraceComment28._traceability_LogEntry__traceability_LogEntry14.children",
        severity=1,
        messageType=1040,
        comment="j?EkNwh\x0cM$>Yk^:X",
    )
    assert isinstance(var_34, python_code_.traceability_LogEntry)


def test_7():
    python_code_.traceability_TraceComment(
        comment="_traceability_Trace__Trace",
        username='t&OPAI!\x0c_vzimNk\n)7"',
        date=None,
        column='*<PA"p\x0b$',
        traceability_TraceComment28=None,
    )


def test_8():
    var_60 = python_code_.traceability_TraceDiff(
        comment="ZqX=", traceability_TraceDiff={1}, traceability_TraceDiff30=None
    )
    assert isinstance(var_60, python_code_.traceability_TraceDiff)


def test_9():
    var_35 = python_code_.traceability_TraceDiff(
        comment=[], traceability_TraceDiff27="-{`l !>"
    )
    assert isinstance(var_35, python_code_.traceability_TraceDiff)


def test_10():
    var_0 = python_code_.traceability_DiffCategory(
        name='5"Ku\x0cVK~u?QD', modelIndex=-487, unequal=False
    )
    assert isinstance(var_0, python_code_.traceability_DiffCategory)
    var_31 = python_code_.traceability_TraceDiff(
        comment="&6;?Cx/^(,", traceability_TraceDiff30=var_0
    )
    assert isinstance(var_31, python_code_.traceability_TraceDiff)


def test_11():
    var_17 = "traceability_EObject20:_traceability_Category__traceability_Category"
    var_21 = python_code_.traceability_Trace(
        description="traceability_EObject23",
        value="Trace8",
        comment=var_17,
        traceability_Trace={var_17},
        Trace8=var_17,
        traceability_Trace10=set(),
    )
    assert isinstance(var_21, python_code_.traceability_Trace)


def test_12():
    var_17 = "\x0bu;'\x0bO66.N$Lqn"
    var_21 = python_code_.traceability_Trace(
        description="traceability_Trace10",
        value="tsRD",
        comment=var_17,
        children=var_17,
        traceability_Trace10=set(),
    )
    assert isinstance(var_21, python_code_.traceability_Trace)


def test_13():
    var_17 = "\x0bu;'\x0bO66.N$Lq"
    var_21 = python_code_.traceability_Trace(
        description=var_17,
        value=var_17,
        comment="_traceability_LogEntry__traceability_LogEntry,traceability_EObject,_traceability_TraceComment__traceability_TraceComment28",
        traceability_Trace={False, var_17},
        traceability_Trace2={
            0,
            -890,
            "_traceability_DiffCategory__traceability_DiffCategory,traceability_TraceDiff30,traceability_EObject17,traceability_TraceDiff27",
        },
        Trace8=None,
    )
    assert isinstance(var_21, python_code_.traceability_Trace)


def test_14():
    var_17 = "\x0bu;'\x0bhO66.N$Lqn"
    var_21 = python_code_.traceability_Trace(
        description=var_17,
        value=var_17,
        comment="_traceability_Traces__traceability_Traces19",
    )
    assert isinstance(var_21, python_code_.traceability_Trace)


@pytest.mark.xfail(strict=True)
def test_15():
    var_18 = python_code_.traceability_EObject()
    var_19 = "[j@]20WV"
    var_20 = "\r80RFe"
    var_21 = python_code_.traceability_Trace(
        description=var_19, value=var_20, comment=var_18
    )
    assert isinstance(var_21, python_code_.traceability_Trace)
    python_code_.traceability_Trace(
        description=var_19, value=var_19, comment=2711.48, Trace=var_21, Trace8=var_21
    )


def test_16():
    var_35 = "z\n\x0b:Y\tzlkj"
    var_38 = python_code_.traceability_Trace(
        description=var_35,
        value='vbSISA]gD"N41',
        comment="['lwKWe",
        Trace=var_35,
        Trace8=var_35,
        children=var_35,
    )
    assert isinstance(var_38, python_code_.traceability_Trace)


def test_17():
    var_1 = b"A\xef\xdc]\xb7\xd2\xaf\x87\x892g"
    var_58 = python_code_.traceability_Traces(
        username="_traceability_Trace__parent traceability_TraceDiff27 _traceability_DiffCategory__traceability_DiffCategory",
        fullName="_traceability_TraceComment__traceability_TraceComment28",
        date=None,
        location="j",
        comments="_traceability_Trace__traceability_Trace10",
        uriMap="Q]AkJ*D$cnL",
        originalSourceURL="<uq8=kKaev|G'u\x0c2[vq",
        traceability_Traces=var_1,
        traceability_Traces19=None,
    )
    assert isinstance(var_58, python_code_.traceability_Traces)
    var_59 = python_code_.traceability_TraceDiff(
        comment={"yU": -5584}, traceability_TraceDiff30=var_1
    )
    assert isinstance(var_59, python_code_.traceability_TraceDiff)


def test_18():
    var_34 = python_code_.traceability_LogEntry(
        message="traceability_TraceDiff30,_traceability_Trace__parent,_traceability_Trace__children",
        severity=-4445,
        messageType=3,
        comment="-hwDf!v156Ej\\%",
        traceability_LogEntry14={"\txjU4sG"},
    )
    assert isinstance(var_34, python_code_.traceability_LogEntry)


def test_19():
    var_1 = b"\xaaFY\x7f0\xc5\xfdixq\xf60"
    var_59 = python_code_.traceability_TraceComment(
        comment="Si:N",
        username="_traceability_TraceComment__traceability_TraceComment traceability_TraceComment15",
        date=None,
        column="traceability_TraceComment15",
        traceability_TraceComment=var_1,
        traceability_TraceComment28=var_1,
    )
    assert isinstance(var_59, python_code_.traceability_TraceComment)


def test_20():
    var_36 = python_code_.traceability_Trace
    var_37 = ",RM"
    var_38 = python_code_.traceability_TraceComment(
        comment=var_36,
        username=-756,
        date=[-3800, True],
        column=var_37,
        traceability_TraceComment36=(0, 5046.7, 1671.24),
    )
    assert isinstance(var_38, python_code_.traceability_TraceComment)


def test_21():
    var_34 = python_code_.traceability_LogEntry(
        message="\\K", severity=4489, messageType=217, comment="6,nu\nTli}&H`r[xk"
    )
    assert isinstance(var_34, python_code_.traceability_LogEntry)
    var_36 = python_code_.traceability_TraceDiff
    var_37 = python_code_.traceability_TraceComment(
        comment=" (~mA",
        username="2fS1bx7qY`K=`GyPhR",
        date=var_36,
        column="~TwGa?d[|ZS]g;2Ht}",
        traceability_TraceComment=None,
        traceability_TraceComment15=var_34,
    )
    assert isinstance(var_37, python_code_.traceability_TraceComment)


def test_22():
    var_37 = "_-s0OhS*{"
    var_38 = python_code_.traceability_Trace(
        description=var_37,
        value=var_37,
        comment="hL.+i+q\"('",
        traceability_Trace=set(),
        parent={620.59, "children", -179.4},
    )
    assert isinstance(var_38, python_code_.traceability_Trace)


def test_23():
    var_0 = "CFfaP8kPv>"
    var_1 = "}Nh6X*^~[h"
    var_2 = python_code_.traceability_EObject()
    var_3 = python_code_.traceability_TraceComment(
        comment={"qHM}xay{8/9\\": -292},
        username=var_0,
        date=[],
        column=var_1,
        traceability_TraceComment15=var_1,
        traceability_TraceComment36=var_2,
    )
    assert isinstance(var_3, python_code_.traceability_TraceComment)
    var_4 = python_code_.traceability_Category(name=var_3)
    assert isinstance(var_4, python_code_.traceability_Category)
    var_5 = "_traceability_TraceDiff__traceability_TraceDiff30"
    var_6 = set
    var_7 = "R~vbywQ"
    var_8 = python_code_.traceability_TraceDiff(comment=var_7)
    assert isinstance(var_8, python_code_.traceability_TraceDiff)
    var_9 = python_code_.traceability_TraceComment(
        comment=None,
        username=var_6,
        date=var_0,
        column=var_5,
        traceability_TraceComment28=var_8,
    )
    assert isinstance(var_9, python_code_.traceability_TraceComment)
    var_10 = {var_9, var_9, var_9, var_9}
    var_11 = python_code_.traceability_Trace(
        description=var_5,
        value=var_0,
        comment=var_5,
        parent=b"\x14\x0bdp",
        Trace8=["traceability_EObject17 traceability_TraceDiff30"],
        traceability_Trace10=var_10,
    )
    assert isinstance(var_11, python_code_.traceability_Trace)
    var_12 = python_code_.traceability_TraceComment(
        comment=var_6,
        username=var_0,
        date=var_2,
        column=var_11,
        traceability_TraceComment=var_11,
        traceability_TraceComment28=True,
    )
    assert isinstance(var_12, python_code_.traceability_TraceComment)
    var_23 = "K{]U|JF84$<\x0b"
    var_24 = python_code_.traceability_LogEntry(
        message=var_23,
        severity=var_4,
        messageType=var_23,
        comment=var_5,
        traceability_LogEntry="",
        traceability_LogEntry14=var_10,
    )
    assert isinstance(var_24, python_code_.traceability_LogEntry)


def test_24():
    var_1 = "_Zraceability_Trace__traceability_Trace2"
    var_59 = "Y[v"
    var_60 = lambda *args, **kwargs: True
    var_61 = python_code_.traceability_TraceDiff(comment=False)
    assert isinstance(var_61, python_code_.traceability_TraceDiff)
    var_62 = python_code_.traceability_TraceComment(
        comment=var_59,
        username=var_60,
        date=var_60,
        column=var_60,
        traceability_TraceComment28=var_61,
        traceability_TraceComment36=var_1,
    )
    assert isinstance(var_62, python_code_.traceability_TraceComment)


def test_25():
    var_0 = tuple
    var_21 = python_code_.traceability_TraceDiff(
        comment=(), traceability_TraceDiff30=var_0
    )
    assert isinstance(var_21, python_code_.traceability_TraceDiff)
    var_22 = {var_21}
    var_23 = python_code_.traceability_DiffCategory(
        name=var_0,
        modelIndex=(-601.36, -523.26),
        unequal=var_0,
        traceability_DiffCategory=var_22,
    )
    assert isinstance(var_23, python_code_.traceability_DiffCategory)


def test_26():
    var_36 = bool
    var_37 = "'-s0OhS*{"
    var_38 = python_code_.traceability_Trace(
        description=-471, value=var_37, comment=var_36, children=var_37
    )
    assert isinstance(var_38, python_code_.traceability_Trace)
    var_39 = python_code_.traceability_TraceComment(
        comment=var_36,
        username=True,
        date=[],
        column=var_37,
        traceability_TraceComment=var_38,
        traceability_TraceComment15=-1991,
        traceability_TraceComment28=(),
    )
    assert isinstance(var_39, python_code_.traceability_TraceComment)


def test_27():
    var_35 = "z\n\x0b:Y\tzlkj"
    var_36 = python_code_.traceability_TraceDiff
    var_37 = python_code_.traceability_TraceComment(
        comment=var_35,
        username=var_35,
        date=True,
        column=var_36,
        traceability_TraceComment={"|`K4_'k}\tb": 245.96, "E{e'wLHF": "$F/ids)Y=`m"},
        traceability_TraceComment28=var_36,
    )
    assert isinstance(var_37, python_code_.traceability_TraceComment)


def test_28():
    var_1 = python_code_.traceability_Category(
        name="P|\n?CxY}p\r\\-b$ 0:T", traceability_Category=set()
    )
    assert isinstance(var_1, python_code_.traceability_Category)


def test_29():
    var_1 = b"Mw\x0e\t\xa1i\x19\xb6\xb1f\xf30\x17\xbfa"
    var_58 = python_code_.traceability_Traces(
        username="Trace8traceability_EObject25",
        fullName="t\x0cr\x0c%.~:j3WUO&-zj",
        date=None,
        location="_traceability_Trace__traceability_Trace",
        comments="\tY=ROWW\x0c?\rC",
        uriMap="6",
        originalSourceURL="_traceability_TraceDiff__traceability_TraceDifftraceability_EObject34",
        traceability_Traces19=var_1,
    )
    assert isinstance(var_58, python_code_.traceability_Traces)


def test_30():
    var_1 = b"\xd9cp"
    var_58 = python_code_.traceability_Traces(
        username="G]BT;*!}ux GO:",
        fullName="13",
        date=None,
        location="^1o\t",
        comments='"i0FgPR`A@',
        uriMap=" +h&1\rkYPx;MOu<X",
        originalSourceURL="_traceability_TraceDiff__traceability_TraceDiff30.traceability_EObject17",
        traceability_Traces22=set(),
        traceability_Traces32=var_1,
    )
    assert isinstance(var_58, python_code_.traceability_Traces)


def test_31():
    var_1 = b"%#j\x90?"
    var_58 = python_code_.traceability_Traces(
        username="_traceability_Trace__traceability_Trace traceability_EObject17 _traceability_Traces__traceability_Traces32 _traceability_DiffCategory__traceability_DiffCategory",
        fullName="D^]\nE8>8ysj0HvM",
        date=None,
        location="6e",
        comments="k\t5",
        uriMap="Trace8 _traceability_TraceComment__traceability_TraceComment15",
        originalSourceURL="~!`nl^G7d1\n",
        traceability_Traces=var_1,
        traceability_Traces19=None,
    )
    assert isinstance(var_58, python_code_.traceability_Traces)


def test_32():
    var_59 = list
    var_60 = ",\x0brZ'"
    var_61 = '";38|j\x0bI[u,!` H2b\r'
    var_62 = "JNu8"
    var_63 = python_code_.traceability_Trace(
        description=b"\xd8\x81\x13e(\xa7e\xefe", value=None, comment=var_62
    )
    assert isinstance(var_63, python_code_.traceability_Trace)
    var_64 = python_code_.traceability_Trace(
        description=var_59,
        value=None,
        comment=var_61,
        traceability_Trace2=var_60,
        Trace=var_63,
    )
    assert isinstance(var_64, python_code_.traceability_Trace)


def test_33():
    var_14 = "70}#;Olc-RKc"
    var_15 = "\x0cmjRAOAw*G2]8\x0c"
    var_16 = python_code_.traceability_EObject
    var_17 = "[{H~A%jd\n"
    var_18 = python_code_.traceability_TraceComment(
        comment=var_14,
        username=var_15,
        date=var_16,
        column=var_17,
        traceability_TraceComment15=var_14,
    )
    assert isinstance(var_18, python_code_.traceability_TraceComment)
    var_19 = {var_18, var_18, var_18, var_18}
    var_20 = python_code_.traceability_LogEntry(
        message=var_14,
        severity=None,
        messageType=var_14,
        comment=var_14,
        traceability_LogEntry14=var_19,
    )
    assert isinstance(var_20, python_code_.traceability_LogEntry)


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = python_code_.traceability_DiffCategory(
        name="_traceability_TraceComment__traceability_TraceComment28._traceability_TraceComment__traceability_TraceComment",
        modelIndex=474,
        unequal=False,
    )
    assert isinstance(var_0, python_code_.traceability_DiffCategory)
    var_30 = "\n"
    var_31 = object
    var_40 = "MxbNK.>,hP]JjA"
    var_41 = -2048
    var_42 = True
    var_32 = python_code_.traceability_DiffCategory(
        name=var_40, modelIndex=var_41, unequal=var_42
    )
    var_34 = python_code_.traceability_LogEntry(
        message=var_31,
        severity=748.6,
        messageType=var_32,
        comment=var_30,
        traceability_LogEntry14=[],
    )
    assert isinstance(var_34, python_code_.traceability_LogEntry)
    var_35 = python_code_.traceability_TraceComment(
        comment=-3229.24,
        username={0, 949},
        date=var_30,
        column={
            "": 0,
            "*YY'F\x0byR06mf#=Z\"u$": "traceability_LogEntry14,_traceability_Trace__Trace,traceability_LogEntry",
        },
        traceability_TraceComment15=var_34,
    )
    assert isinstance(var_35, python_code_.traceability_TraceComment)
    python_code_.traceability_TraceDiff(
        comment=var_30, traceability_TraceDiff=-2429.16, traceability_TraceDiff30=var_32
    )


def test_35():
    var_0 = python_code_.traceability_DiffCategory
    var_17 = "\x0b{u;'\x0b?O66.N$Lqn"
    var_19 = python_code_.traceability_Trace(
        description="_traceability_TraceComment__traceability_TraceComment15",
        value="rn",
        comment=var_17,
        traceability_Trace2={var_0, False},
        traceability_Trace10={var_17, var_17},
    )
    assert isinstance(var_19, python_code_.traceability_Trace)
    var_21 = python_code_.traceability_TraceDiff(
        comment=(), traceability_TraceDiff30=var_0
    )
    assert isinstance(var_21, python_code_.traceability_TraceDiff)
    var_22 = {var_21}
    var_23 = python_code_.traceability_DiffCategory(
        name=var_0,
        modelIndex=(-601.36, -523.26),
        unequal=var_0,
        traceability_DiffCategory=var_22,
    )
    assert isinstance(var_23, python_code_.traceability_DiffCategory)


def test_36():
    var_60 = python_code_.traceability_TraceDiff(
        comment="ZqX=", traceability_TraceDiff={1}, traceability_TraceDiff30=None
    )
    assert isinstance(var_60, python_code_.traceability_TraceDiff)
    var_62 = "XZf2q"
    var_63 = python_code_.traceability_Trace(
        description=var_62,
        value=var_62,
        comment="3RGdb|a",
        traceability_Trace2=set(),
        parent=set(),
        children=var_62,
    )
    assert isinstance(var_63, python_code_.traceability_Trace)
    var_67 = 'x2"v'
    var_68 = 0
    var_69 = False
    var_70 = "traceability_EObject17._traceability_Trace__children"
    var_71 = bool
    var_72 = "_traceability_Trace__parent,traceability_DiffCategory,_traceability_Category__traceability_Category"
    var_73 = set()
    var_74 = python_code_.traceability_TraceDiff(
        comment=var_72, traceability_TraceDiff=var_73
    )
    var_75 = {var_60, var_60, var_74, var_60}
    var_76 = python_code_.traceability_DiffCategory(
        name=False, modelIndex={False}, unequal=var_71, traceability_DiffCategory=var_75
    )
    assert isinstance(var_76, python_code_.traceability_DiffCategory)
    var_77 = python_code_.traceability_TraceDiff(
        comment=var_70, traceability_TraceDiff30=var_76
    )
    var_78 = {var_74, var_74, var_77, var_77}
    python_code_.traceability_DiffCategory(
        name=var_67, modelIndex=var_68, unequal=var_69, traceability_DiffCategory=var_78
    )


def test_37():
    var_36 = 'Z"0,[^8m-Bc:ZO'
    var_37 = python_code_.traceability_Trace(
        description=var_36,
        value=var_36,
        comment=var_36,
        traceability_Trace=var_36,
        Trace8={"traceability_EObject34": False, "fBK@|s\x0bC;": -1183, "2": -1030.88},
    )
    assert isinstance(var_37, python_code_.traceability_Trace)
    var_38 = "(D=R\x0b<S"
    var_39 = python_code_.traceability_EObject()
    var_40 = python_code_.traceability_EObject()
    var_41 = {var_39, var_39, var_40}
    var_42 = python_code_.traceability_Trace(
        description=var_36,
        value=var_38,
        comment=var_37,
        traceability_Trace=var_41,
        Trace=var_37,
        parent=var_41,
        children=var_39,
    )
    assert isinstance(var_42, python_code_.traceability_Trace)
    var_43 = {var_37, var_37, var_42}
    python_code_.traceability_Trace(
        description=(),
        value={-2020.93, -459},
        comment=complex(-1194.9, -687.5064),
        traceability_Trace=[-1355.03],
        parent=var_43,
    )
    var_45 = python_code_.traceability_Category(name=var_38)
    assert isinstance(var_45, python_code_.traceability_Category)


@pytest.mark.xfail(strict=True)
def test_38():
    var_35 = python_code_.traceability_Category(name="16ez7>")
    assert isinstance(var_35, python_code_.traceability_Category)
    var_36 = "traceability_EObject17traceability_Trace"
    var_37 = float
    var_38 = python_code_.traceability_EObject()
    var_39 = {var_38, var_38, var_38, var_38, var_38}
    var_40 = python_code_.traceability_Trace(
        description=var_36,
        value=2490.08,
        comment=var_36,
        traceability_Trace2=var_39,
        Trace="",
        parent=var_39,
    )
    assert isinstance(var_40, python_code_.traceability_Trace)
    var_41 = {var_40, var_40, var_40}
    var_42 = "_traceability_Traces__traceability_Traces"
    python_code_.traceability_Trace(
        description=var_37,
        value=var_42,
        comment=1179.95,
        parent=var_41,
        Trace8=False,
        children=var_40,
    )


def test_39():
    var_0 = python_code_.traceability_DiffCategory(
        name='5"Ku\x0cVK~u?QD', modelIndex=-487, unequal=False
    )
    assert isinstance(var_0, python_code_.traceability_DiffCategory)
    var_31 = python_code_.traceability_TraceDiff(
        comment="&6;?Cx/^(,", traceability_TraceDiff30=var_0
    )
    assert isinstance(var_31, python_code_.traceability_TraceDiff)
    var_32 = "_traceability_Trace__traceability_Trace10-_traceability_Trace__Trace8-traceability_Trace10-traceability_TraceComment15"
    var_33 = python_code_.traceability_Trace
    var_34 = python_code_.traceability_TraceComment(
        comment=var_31,
        username=var_31,
        date={False},
        column=var_32,
        traceability_TraceComment=var_33,
    )
    assert isinstance(var_34, python_code_.traceability_TraceComment)


def test_40():
    var_16 = {}
    var_17 = "\x0bu;'\x0b?O66.N$Lqn"
    var_19 = python_code_.traceability_Trace(
        description=var_17,
        value='vbSISA]gD"N41',
        comment="['lwKWe",
        Trace=var_17,
        Trace8=var_17,
        children=var_17,
    )
    assert isinstance(var_19, python_code_.traceability_Trace)
    var_20 = python_code_.traceability_TraceComment(
        comment="d90V_7G.mCEhWX-Q_C",
        username="M<)h^^@C",
        date=var_16,
        column=var_17,
        traceability_TraceComment28=var_19,
        traceability_TraceComment36=var_19,
    )
    var_21 = {var_20}
    var_22 = python_code_.traceability_TraceDiff(
        comment=var_19, traceability_TraceDiff27=var_21
    )
    assert isinstance(var_22, python_code_.traceability_TraceDiff)


@pytest.mark.xfail(strict=True)
def test_41():
    python_code_.traceability_TraceComment(
        comment="_traceability_Trace__Trace",
        username='t&OPAI!\x0c_vzimNk\n)7"',
        date=None,
        column='*<PA"p\x0b$',
        traceability_TraceComment28=None,
    )
    var_39 = "traceability_TraceDiffs._traceability_TraceDiff__traceability_TraceDiff30._traceability_LogEntry__traceability_LogEntry._traceability_Traces__traceability_Traces22"
    var_43 = "wlVCv@o#bW]DSj.u$V"
    var_44 = "S"
    var_45 = str
    var_46 = python_code_.traceability_Trace(
        description=var_44, value=-1025, comment=var_39, children=var_45
    )
    assert isinstance(var_46, python_code_.traceability_Trace)
    python_code_.traceability_Trace(
        description=var_39, value=var_43, comment=3624, Trace8=var_46, children=var_46
    )


@pytest.mark.xfail(strict=True)
def test_42():
    var_32 = "_traceability_TraceDiff__traceability_TraceDiff27"
    var_33 = python_code_.traceability_TraceDiff
    var_34 = ".?,\x0ckm|8"
    var_35 = set()
    var_36 = python_code_.traceability_Trace(
        description=None,
        value=var_34,
        comment=var_33,
        traceability_Trace=var_35,
        Trace=var_34,
        Trace8=False,
        traceability_Trace10="traceability_LogEntry14-_traceability_Trace__traceability_Trace2-traceability_DiffCategory-traceability_Trace10",
    )
    assert isinstance(var_36, python_code_.traceability_Trace)
    var_37 = ""
    var_38 = "_traceability_Trace__traceability_Trace10"
    python_code_.traceability_Trace(
        description=var_37,
        value=var_32,
        comment=var_38,
        parent=b"\xf0\xbc\x98T\xb7\xf1\x9e\xa4",
        children=var_36,
        traceability_Trace10=var_32,
    )


def test_43():
    var_35 = python_code_.traceability_TraceDiff(comment="L5|wL\ryy23U4bdX3O")
    assert isinstance(var_35, python_code_.traceability_TraceDiff)
    var_37 = ""
    var_38 = complex
    var_39 = python_code_.traceability_TraceComment(
        comment=var_37,
        username=var_38,
        date=var_38,
        column=var_37,
        traceability_TraceComment=var_37,
        traceability_TraceComment15=var_38,
        traceability_TraceComment28=var_35,
    )
    assert isinstance(var_39, python_code_.traceability_TraceComment)
    var_40 = {var_39, var_39, var_39, var_39, var_39}
    var_41 = python_code_.traceability_TraceDiff(
        comment=var_37, traceability_TraceDiff27=var_40, traceability_TraceDiff30=var_38
    )
    assert isinstance(var_41, python_code_.traceability_TraceDiff)
    var_42 = "R"
    var_43 = "V8SR\r\rx\\1-vf^,`_|c:"
    var_44 = ""
    var_45 = python_code_.traceability_TraceDiffs()
    var_46 = python_code_.traceability_Traces(
        username=var_42,
        fullName={-995.15, False, False},
        date='kf5"pdz~DZp$O',
        location=var_42,
        comments=var_43,
        uriMap=var_44,
        originalSourceURL=var_37,
        traceability_Traces32=var_45,
    )
    assert isinstance(var_46, python_code_.traceability_Traces)
