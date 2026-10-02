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
    Enum,
    SqlExpr,
    SqlSentence,
    TableConstraint,
    TriggerAction,
    TriggerTime,
    Type,
    date,
    datetime,
    sqls_Column,
    sqls_ColumnRef,
    sqls_Delete,
    sqls_DeleteTable,
    sqls_Enum,
    sqls_EnumElement,
    sqls_Function,
    sqls_Get,
    sqls_Import,
    sqls_Insert,
    sqls_InsertStatement,
    sqls_NewColumn,
    sqls_OldColumn,
    sqls_OrderingTerm,
    sqls_ResultColumn,
    sqls_Select,
    sqls_SelectList,
    sqls_SqlBinaryExpr,
    sqls_SqlExpr,
    sqls_SqlFunction,
    sqls_SqlLibrary,
    sqls_SqlMethod,
    sqls_SqlMethodRef,
    sqls_SqlNested,
    sqls_SqlNumberLiteral,
    sqls_SqlParam,
    sqls_SqlPlaceholder,
    sqls_SqlSentence,
    sqls_SqlStringLiteral,
    sqls_SqlType,
    sqls_Table,
    sqls_TableConstraint,
    sqls_TableRef,
    sqls_Tag,
    sqls_Trigger,
    sqls_TriggerAction,
    sqls_TriggerDelete,
    sqls_TriggerInsert,
    sqls_TriggerUpdate,
    sqls_Type,
    sqls_TypeDef,
    sqls_UniqueTableConstraint,
    sqls_Update,
    sqls_UpdateColumnExpression,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_1 = python_code_.sqls_SqlExpr()
    var_6 = python_code_.sqls_UpdateColumnExpression()
    var_8 = python_code_.sqls_SqlNumberLiteral
    var_9 = python_code_.sqls_TableRef(alias=var_8)
    python_code_.sqls_Select(
        all=var_8, sqls_Select50=var_9, sqls_Select52=var_1, sqls_Select58=var_6
    )


def test_1():
    var_3 = python_code_.sqls_TriggerAction()
    python_code_.sqls_TableRef(alias="NfKwKZ$e&m^[D G8V6C", sqls_TableRef126=var_3)


def test_2():
    var_3 = python_code_.sqls_TriggerAction()
    python_code_.sqls_TableRef(alias="_sqls_Column__sqls_Column", sqls_TableRef=var_3)


def test_3():
    python_code_.sqls_TableRef(
        alias="_sqls_Select__sqls_Select61-sqls_Column-_sqls_Tag__sqls_Tag-sqls_Table107"
    )


def test_4():
    var_1 = python_code_.sqls_SqlExpr()
    var_2 = python_code_.sqls_SqlBinaryExpr(
        op="w@(PY3ixmvZD", sqls_SqlBinaryExpr=None, sqls_SqlBinaryExpr117=var_1
    )
    assert isinstance(var_2, python_code_.sqls_SqlBinaryExpr)


def test_5():
    var_1 = python_code_.sqls_SqlExpr()
    var_2 = python_code_.sqls_SqlBinaryExpr(op={}, sqls_SqlBinaryExpr=var_1)
    assert isinstance(var_2, python_code_.sqls_SqlBinaryExpr)
    var_3 = python_code_.sqls_UniqueTableConstraint(
        name=var_1, sqls_UniqueTableConstraint={}
    )
    assert isinstance(var_3, python_code_.sqls_UniqueTableConstraint)


def test_6():
    python_code_.sqls_ResultColumn(name=b'6\x17:\xee"\xe0\xda')


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.sqls_SelectList()
    var_1 = python_code_.sqls_SqlExpr()
    python_code_.sqls_ResultColumn(
        name=[], sqls_ResultColumn46=var_0, sqls_ResultColumn=var_1
    )
    var_5 = "sqls_Trigger106 _sqls_Column__sqls_Column26"
    python_code_.sqls_Tag(name=var_5)
    var_9 = "kCs/yb:%+"
    python_code_.sqls_Trigger(
        name=complex(2868.5798, 850.00564),
        time=var_9,
        sqls_Trigger101=complex(871.18665, -367.6837),
    )


def test_8():
    python_code_.sqls_OrderingTerm(asc=False, desc=False)


def test_9():
    var_6 = True
    var_28 = python_code_.sqls_OrderingTerm(asc=var_6, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_28, python_code_.sqls_OrderingTerm)


def test_10():
    var_0 = python_code_.sqls_Delete()
    python_code_.sqls_ResultColumn(name="p0d,&v9+", sqls_ResultColumn46=var_0)
    var_12 = "o6,"
    var_14 = python_code_.sqls_SqlBinaryExpr(op=var_12)
    assert isinstance(var_14, python_code_.sqls_SqlBinaryExpr)
    var_16 = True
    var_17 = python_code_.sqls_Select(
        all=var_16, sqls_Select=var_0, sqls_Select61=var_12
    )
    assert isinstance(var_17, python_code_.sqls_Select)
    var_20 = python_code_.sqls_OrderingTerm(
        asc=var_16, desc=var_16, sqls_OrderingTerm56=var_17
    )
    assert isinstance(var_20, python_code_.sqls_OrderingTerm)
    var_21 = {var_20, var_20, var_20}
    var_22 = python_code_.sqls_SqlExpr()
    python_code_.sqls_Select(all=var_16, sqls_Select55=var_21, sqls_Select58=var_22)


def test_11():
    var_0 = python_code_.sqls_DeleteTable
    python_code_.sqls_TableRef(alias=(816,), sqls_TableRef126=var_0)
    var_3 = True
    var_4 = python_code_.sqls_OrderingTerm(asc=var_3, desc=False)
    var_5 = {var_4, var_4, var_4}
    var_6 = python_code_.sqls_Select(all=var_3, sqls_Select55=var_5)
    assert isinstance(var_6, python_code_.sqls_Select)
    var_8 = "x/it"
    var_9 = python_code_.sqls_SqlBinaryExpr(op=var_8)
    assert isinstance(var_9, python_code_.sqls_SqlBinaryExpr)


def test_12():
    var_0 = python_code_.sqls_SelectList()
    python_code_.sqls_ResultColumn(name="p0d,&v9+", sqls_ResultColumn46=var_0)
    var_6 = "(0WOx"
    var_8 = {var_6, var_0, var_0}
    var_17 = python_code_.sqls_Select(all=True, sqls_Select55=var_8, sqls_Select58=None)
    assert isinstance(var_17, python_code_.sqls_Select)


def test_13():
    var_1 = lambda *args, **kwargs: 72
    var_2 = python_code_.sqls_SqlExpr()
    var_5 = python_code_.sqls_Select(all=var_1, sqls_Select58=var_2, sqls_Select61=())
    assert isinstance(var_5, python_code_.sqls_Select)


def test_14():
    var_0 = python_code_.sqls_SelectList()
    python_code_.sqls_ResultColumn(name="p0d,&v9+", sqls_ResultColumn46=var_0)
    var_12 = "o6,"
    var_14 = python_code_.sqls_SqlBinaryExpr(op=var_12)
    assert isinstance(var_14, python_code_.sqls_SqlBinaryExpr)
    var_16 = True
    var_17 = python_code_.sqls_Select(
        all=var_16, sqls_Select=var_0, sqls_Select61=var_12
    )
    assert isinstance(var_17, python_code_.sqls_Select)


def test_15():
    var_1 = lambda *args, **kwargs: 72
    var_2 = python_code_.sqls_SqlExpr()
    var_5 = python_code_.sqls_Select(
        all=True,
        sqls_Select=None,
        sqls_Select50=var_1,
        sqls_Select52=None,
        sqls_Select58=var_2,
    )
    assert isinstance(var_5, python_code_.sqls_Select)


def test_16():
    var_7 = ("np?W",)
    var_8 = python_code_.sqls_SqlExpr()
    var_9 = python_code_.sqls_Select(
        all=var_7, sqls_Select52=b"\xf3\x11", sqls_Select58=var_8
    )
    assert isinstance(var_9, python_code_.sqls_Select)


def test_17():
    var_4 = float
    var_5 = "sqls_SqlMethodAFTER"
    var_6 = python_code_.sqls_SqlMethod(
        array=var_4, name=var_5, sqls_SqlMethod131=var_4
    )
    assert isinstance(var_6, python_code_.sqls_SqlMethod)


def test_18():
    var_1 = 82
    var_2 = python_code_.sqls_SqlNumberLiteral(value=var_1)
    assert isinstance(var_2, python_code_.sqls_SqlNumberLiteral)
    var_4 = python_code_.sqls_SqlSentence()
    var_5 = {var_4, var_4, var_4, var_4, var_4}
    var_6 = python_code_.sqls_UniqueTableConstraint
    var_7 = python_code_.sqls_SqlMethod(
        array=var_2, name=234.08, sqls_SqlMethod40=var_5, sqls_SqlMethod=var_6
    )
    assert isinstance(var_7, python_code_.sqls_SqlMethod)


def test_19():
    var_6 = python_code_.sqls_TableRef(
        alias="_sqls_Select__sqls_Select61-sqls_Column-_sqls_Tag__sqls_Tag-sqls_Table107"
    )
    var_28 = python_code_.sqls_SqlSentence()
    var_35 = python_code_.sqls_InsertStatement
    var_36 = python_code_.sqls_SqlMethod(
        array=var_6, name=var_28, sqls_SqlMethod37=None, sqls_SqlMethod=var_35
    )
    assert isinstance(var_36, python_code_.sqls_SqlMethod)


@pytest.mark.xfail(strict=True)
def test_20():
    var_1 = "H|6Hz6F+]$0{s}~"
    var_2 = python_code_.sqls_SqlPlaceholder
    var_3 = -3228
    var_4 = python_code_.sqls_SqlLibrary(
        database=var_2, version=var_3, sqls_SqlLibrary9=var_1, sqls_SqlLibrary11=None
    )
    var_5 = python_code_.sqls_Table(name=var_1, sqls_Table=var_4, sqls_Table71=var_4)
    var_6 = True
    var_7 = python_code_.sqls_NewColumn()
    var_8 = python_code_.sqls_ColumnRef()
    var_9 = python_code_.sqls_TriggerUpdate()
    python_code_.sqls_Column(
        name=var_1,
        null=var_6,
        primaryKey=var_5,
        sqls_Column76={},
        sqls_Column120=var_7,
        sqls_Column26={
            "Er'wn\\{G#gjT\x0b": -2387,
            "*j}h$*xW\t=_luQE-": "sqls_SqlLibrary13sqls_TriggerUpdate",
            "_sqls_Tag__sqls_Tag": 200,
        },
        sqls_Column129=var_8,
        sqls_Column135=var_9,
    )
    python_code_.sqls_ResultColumn(name=b'6\x17:\xee"\xe0\xda')
    var_13 = "(W7x"
    var_14 = python_code_.sqls_SqlMethod(
        array=var_4, name=var_13, sqls_SqlMethod37=b"P\x9e!\xa0\xbb\xe9h"
    )
    assert isinstance(var_14, python_code_.sqls_SqlMethod)
    python_code_.sqls_Table(name=var_2, sqls_Table38=var_14)


def test_21():
    var_2 = False
    var_3 = python_code_.sqls_SqlExpr()
    var_4 = python_code_.sqls_Select(
        all=var_2, sqls_Select50=-2158.65, sqls_Select61=var_3
    )
    assert isinstance(var_4, python_code_.sqls_Select)
    var_5 = "_sqls_Table__sqls_Table107sqls_Table22_sqls_Table__sqls_Table38sqls_TriggerUpdate"
    var_6 = "_sqls_TableRef__sqls_TableRef126:_sqls_Table__sqls_Table19"
    var_7 = set()
    var_8 = python_code_.sqls_Trigger(name=var_6, time=var_3, sqls_Trigger109=var_7)
    var_9 = python_code_.sqls_Tag(name=var_5, sqls_Tag102=var_8, sqls_Tag20=[])
    assert isinstance(var_9, python_code_.sqls_Tag)
    var_10 = python_code_.sqls_SqlMethod(
        array=None,
        name=var_5,
        sqls_SqlMethod34=var_7,
        sqls_SqlMethod37=var_9,
        sqls_SqlMethod40=None,
    )
    assert isinstance(var_10, python_code_.sqls_SqlMethod)


def test_22():
    var_1 = "H|6Hz6F+]d$0{s}~"
    var_3 = -3228
    var_4 = python_code_.sqls_SqlLibrary(
        database="J?W2u\rl;m)", version=var_3, sqls_SqlLibrary4=set()
    )
    python_code_.sqls_Table(name=var_1, sqls_Table=var_4, sqls_Table71=var_4)
    python_code_.sqls_Trigger(name=2, time=var_1)


def test_23():
    var_0 = python_code_.sqls_Function()
    var_10 = True
    python_code_.sqls_Column(
        name=None,
        null=var_10,
        primaryKey=-3339.35,
        sqls_Column32=var_0,
        sqls_Column129="sqls_TriggerUpdate_sqls_TableRef__sqls_TableRef126_sqls_ResultColumn__sqls_ResultColumnsqls_TableConstraint",
    )


def test_24():
    var_6 = False
    var_8 = python_code_.sqls_ColumnRef()
    var_28 = python_code_.sqls_OrderingTerm(asc=var_6, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_28, python_code_.sqls_OrderingTerm)
    var_29 = python_code_.sqls_SqlFunction()
    var_32 = "-A;'V6zIR)Xs0?i"
    var_33 = python_code_.sqls_InsertStatement()
    var_34 = python_code_.sqls_NewColumn()
    python_code_.sqls_Column(
        name=var_32,
        null=False,
        primaryKey=var_29,
        sqls_Column76=var_33,
        sqls_Column120=var_34,
        sqls_Column26=b"\xa6j\xca\xc8\xa9\x8d!\xadA\xc4L\x1c\x0b\xe1\xf5",
        sqls_Column129=var_8,
        sqls_Column135={";L]J[YW9mv\x0c"},
    )


def test_25():
    var_0 = python_code_.sqls_OldColumn()
    var_1 = python_code_.sqls_TableRef(alias=var_0)
    var_2 = python_code_.sqls_ColumnRef()
    var_3 = python_code_.sqls_SqlParam(name=var_1)
    assert isinstance(var_3, python_code_.sqls_SqlParam)
    var_4 = python_code_.sqls_SqlExpr()
    var_5 = python_code_.sqls_SqlBinaryExpr(
        op=b"\x85;\tP\x04\x91\n\xe6\x8b\xc9$ZM-5\xf1", sqls_SqlBinaryExpr=var_4
    )
    assert isinstance(var_5, python_code_.sqls_SqlBinaryExpr)
    var_8 = "sqls_OrderingTerm56_sqls_Table__sqls_Table99_sqls_Column__sqls_Column29"
    var_9 = "_=muSQ`sgjyMBN"
    python_code_.sqls_Trigger(name=var_8, time=var_9)
    var_11 = "kI|2<UO\\h?bi|A\\[l"
    var_12 = python_code_.sqls_Get()
    var_13 = python_code_.sqls_DeleteTable()
    var_14 = set()
    var_15 = python_code_.sqls_Table(
        name=var_9,
        sqls_Table73={False, -121.78},
        sqls_Table86=var_11,
        sqls_Table99=var_12,
        sqls_Table133=var_13,
        sqls_Table22=var_14,
    )
    var_16 = python_code_.sqls_TriggerUpdate()
    var_17 = python_code_.sqls_Column(
        name=var_11,
        null=(),
        primaryKey=var_8,
        sqls_Column122=var_0,
        sqls_Column=var_15,
        sqls_Column26=var_12,
        sqls_Column129=var_2,
        sqls_Column135=var_16,
    )
    assert isinstance(var_17, python_code_.sqls_Column)


@pytest.mark.xfail(strict=True)
def test_26():
    var_0 = python_code_.SqlExpr()
    var_2 = "_sqls_Table__sqls_Table81"
    var_3 = False
    var_4 = python_code_.sqls_TriggerUpdate()
    python_code_.sqls_Column(
        name=var_2, null=var_0, primaryKey=var_3, sqls_Column135=var_4
    )
    var_6 = python_code_.sqls_SqlFunction()
    var_9 = python_code_.sqls_Delete()
    var_10 = python_code_.sqls_Insert
    python_code_.sqls_Table(
        name=var_0,
        sqls_Table81=var_9,
        sqls_Table73=var_10,
        sqls_Table107=False,
        sqls_Table19=var_3,
        sqls_Table22=var_6,
    )


def test_27():
    var_36 = "sqls_SqlExpr42._sqls_Select_sqls_Select52.sqls_UpdateColumnExpression"
    var_39 = python_code_.sqls_SqlMethodRef()
    var_40 = python_code_.TriggerTime
    python_code_.sqls_EnumElement(name=var_40, text=False)
    var_44 = python_code_.sqls_TriggerInsert
    python_code_.sqls_Column(
        name=var_44,
        null=var_39,
        primaryKey=var_36,
        sqls_Column29=var_44,
        sqls_Column26=var_44,
    )
    python_code_.sqls_ResultColumn(name=True)
    var_49 = False
    var_50 = "2S*q>UEzBTle4k"
    var_51 = python_code_.sqls_UniqueTableConstraint(name=var_50)
    assert isinstance(var_51, python_code_.sqls_UniqueTableConstraint)
    var_52 = python_code_.sqls_Column(
        name=var_40,
        null=var_40,
        primaryKey=var_49,
        sqls_Column94=var_40,
        sqls_Column32=var_51,
        sqls_Column=var_50,
    )
    assert isinstance(var_52, python_code_.sqls_Column)


def test_28():
    var_20 = "~xi~u\r{eCPXH0\n82\r"
    var_21 = python_code_.sqls_Get()
    python_code_.sqls_Table(name=var_20, sqls_Table99=var_21)


@pytest.mark.xfail(strict=True)
def test_29():
    var_17 = "\nC;I_ZEqtog"
    var_18 = python_code_.sqls_TableRef(alias=var_17)
    python_code_.sqls_Table(
        name="sqls_Type7",
        sqls_Table="_sqls_Table__sqls_Table24.sqls_Trigger106.sqls_SqlExpr59._sqls_Table__sqls_Table24",
        sqls_Table38=True,
        sqls_Table65=var_18,
        sqls_Table107=var_17,
        sqls_Table19=var_18,
        sqls_Table22=set(),
    )


def test_30():
    var_1 = "H|6Hz6F+]$0{s}~"
    var_3 = -3228
    var_4 = python_code_.sqls_SqlLibrary(
        database="#t`f5\x0c", version=var_3, sqls_SqlLibrary={var_3, "h}"}
    )
    python_code_.sqls_Table(name=var_1, sqls_Table=var_4, sqls_Table71=var_4)
    python_code_.sqls_ResultColumn(name=";M`]76\r")


def test_31():
    var_2 = "sqls_SqlLibrary2"
    python_code_.sqls_TableRef(alias=var_2, sqls_TableRef=None, sqls_TableRef126=None)
    var_4 = "ZdW|."
    var_5 = True
    var_6 = python_code_.sqls_Delete
    var_7 = python_code_.sqls_SqlMethod(array=var_5, name=var_6)
    assert isinstance(var_7, python_code_.sqls_SqlMethod)
    var_8 = python_code_.sqls_Tag(name=var_4, sqls_Tag35=var_7)
    assert isinstance(var_8, python_code_.sqls_Tag)
    var_9 = {var_8}
    var_11 = python_code_.sqls_SqlParam(name=var_2)
    assert isinstance(var_11, python_code_.sqls_SqlParam)
    var_13 = python_code_.sqls_SqlLibrary(
        database=var_2,
        version=var_9,
        sqls_SqlLibrary9=var_9,
        sqls_SqlLibrary6=var_9,
        sqls_SqlLibrary11=var_9,
    )
    python_code_.sqls_Trigger(name=-2329.26, time=var_2, sqls_Trigger=var_13)
    var_17 = python_code_.sqls_UniqueTableConstraint(
        name=var_9, sqls_UniqueTableConstraint=(-786,)
    )
    assert isinstance(var_17, python_code_.sqls_UniqueTableConstraint)
    var_23 = python_code_.sqls_SqlStringLiteral(value=var_11)
    assert isinstance(var_23, python_code_.sqls_SqlStringLiteral)
    python_code_.sqls_ResultColumn(
        name="sqls_SqlExpr_sqls_Tag__sqls_Tag35sqls_SelectList48_sqls_Trigger__sqls_Trigger104"
    )


def test_32():
    var_17 = python_code_.sqls_TriggerUpdate()
    var_18 = python_code_.sqls_Type()
    var_19 = {var_18}
    python_code_.sqls_SqlLibrary(
        database=False, version=var_17, sqls_SqlLibrary4=var_19
    )


def test_33():
    var_1 = "H|6Hz6F+]$0{s}~"
    var_4 = python_code_.sqls_SqlLibrary(database=var_1, version=4062)
    python_code_.sqls_Table(name=var_1, sqls_Table=var_4, sqls_Table71=var_4)


@pytest.mark.xfail(strict=True)
def test_34():
    var_2 = python_code_.sqls_Import()
    var_4 = ""
    python_code_.sqls_ResultColumn(name=var_4)
    var_7 = bool
    var_8 = {var_2, var_2, var_2, var_2}
    python_code_.sqls_SqlLibrary(
        database=var_4,
        version=var_7,
        sqls_SqlLibrary9=var_4,
        sqls_SqlLibrary=var_8,
        sqls_SqlLibrary13=var_7,
    )


def test_35():
    python_code_.sqls_SelectList()


def test_36():
    var_17 = python_code_.sqls_SqlNumberLiteral(value={False})
    assert isinstance(var_17, python_code_.sqls_SqlNumberLiteral)


def test_37():
    var_1 = "H|6Hz6F+]d$0{s}~"
    var_3 = -3228
    var_4 = python_code_.sqls_SqlLibrary(
        database="#t`f5\x0c", version=var_3, sqls_SqlLibrary={var_3, "h}"}
    )
    python_code_.sqls_Table(name=var_1, sqls_Table=var_4, sqls_Table71=var_4)
    python_code_.sqls_Trigger(name=2, time=var_1)
    var_28 = python_code_.sqls_SqlStringLiteral(value=var_1)
    assert isinstance(var_28, python_code_.sqls_SqlStringLiteral)


def test_38():
    var_6 = "sqls_OrderingTerm56_sqls_Table__sqls_Table99_sqls_Column__sqls_Column29"
    var_7 = "_=muSQ`sgjyMBN"
    python_code_.sqls_Trigger(name=var_6, time=var_7)
    var_9 = "kI|2<UO\\h?bi|A\\[l"
    var_10 = python_code_.sqls_Get()
    var_11 = python_code_.sqls_DeleteTable()
    var_12 = set()
    python_code_.sqls_Table(
        name=var_7,
        sqls_Table73={False, -121.78},
        sqls_Table86=var_9,
        sqls_Table99=var_10,
        sqls_Table133=var_11,
        sqls_Table22=var_12,
    )


def test_39():
    var_7 = "_sqls_Trigger__sqls_Trigger104:sqls_InsertStatement75:_sqls_Trigger__sqls_Trigger104"
    var_8 = python_code_.sqls_SqlBinaryExpr(op=var_7)
    assert isinstance(var_8, python_code_.sqls_SqlBinaryExpr)
    var_13 = False
    var_14 = python_code_.sqls_OrderingTerm(asc=var_13, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_14, python_code_.sqls_OrderingTerm)
    python_code_.sqls_Trigger(name=var_7, time=var_7, sqls_Trigger104=1945)


def test_40():
    var_1 = python_code_.sqls_SqlExpr()
    var_3 = python_code_.sqls_UniqueTableConstraint(
        name=var_1, sqls_UniqueTableConstraint={}
    )
    assert isinstance(var_3, python_code_.sqls_UniqueTableConstraint)


def test_41():
    var_17 = lambda *args, **kwargs: 72
    var_19 = python_code_.sqls_SqlType()
    var_20 = "_sqls_Trigger__sqls_Trigger104:sqls_InsertStatement75:_sqls_Trigger__sqls_Trigger104"
    var_21 = python_code_.sqls_SqlBinaryExpr(op=var_20)
    assert isinstance(var_21, python_code_.sqls_SqlBinaryExpr)
    var_26 = False
    var_27 = python_code_.sqls_OrderingTerm(asc=var_26, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_27, python_code_.sqls_OrderingTerm)
    python_code_.sqls_Trigger(
        name=var_20,
        time=var_20,
        sqls_Trigger101=set(),
        sqls_Trigger104=var_19,
        sqls_Trigger106=None,
        sqls_Trigger109=set(),
        sqls_Trigger=var_17,
    )


def test_42():
    var_0 = python_code_.sqls_Delete()
    python_code_.sqls_ResultColumn(name="p0d,&v9+", sqls_ResultColumn46=var_0)


def test_43():
    var_6 = python_code_.sqls_SqlType()
    var_7 = "_sqls_Trigger__sqls_Trigger104:sqls_InsertStatement75:_sqls_Trigger__sqls_Trigger104"
    var_8 = python_code_.sqls_SqlBinaryExpr(op=var_7)
    assert isinstance(var_8, python_code_.sqls_SqlBinaryExpr)
    var_13 = False
    var_14 = python_code_.sqls_OrderingTerm(asc=var_13, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_14, python_code_.sqls_OrderingTerm)
    python_code_.sqls_Trigger(
        name="o<(<X}7",
        time=var_7,
        sqls_Trigger106=var_8,
        sqls_Trigger109=set(),
        sqls_Trigger=var_6,
    )


def test_44():
    var_1 = 82
    var_2 = python_code_.sqls_SqlNumberLiteral(value=var_1)
    assert isinstance(var_2, python_code_.sqls_SqlNumberLiteral)
    var_4 = python_code_.sqls_SqlSentence()
    var_8 = python_code_.sqls_OrderingTerm
    var_9 = python_code_.sqls_Tag(name=var_8)
    var_10 = {var_9}
    var_11 = python_code_.sqls_SqlMethod(
        array=var_1,
        name=var_4,
        sqls_SqlMethod34=var_10,
        sqls_SqlMethod={
            "#xvv'": -873.91,
            "sqls_Update": 1908,
            "sqls_NewColumn,_sqls_Table__sqls_Table73,sqls_Delete": "WN\\{nGv@}EC>/icNw5",
        },
    )
    assert isinstance(var_11, python_code_.sqls_SqlMethod)


def test_45():
    var_5 = python_code_.sqls_UniqueTableConstraint
    python_code_.sqls_EnumElement(name=set(), text=var_5)
    var_9 = "_sqls_Table__sqls_Table24-_sqls_Trigger__sqls_Trigger104"
    python_code_.sqls_Tag(name=var_9)


def test_46():
    var_3 = python_code_.sqls_TriggerAction()
    python_code_.sqls_TableRef(alias="_sqls_Column__sqls_Column", sqls_TableRef=var_3)
    var_38 = python_code_.sqls_UniqueTableConstraint(name=b"H\x9f\xb2\x98\x19")
    assert isinstance(var_38, python_code_.sqls_UniqueTableConstraint)


def test_47():
    var_5 = python_code_.sqls_UniqueTableConstraint
    python_code_.sqls_EnumElement(name=set(), text=var_5)


def test_48():
    var_5 = python_code_.sqls_UniqueTableConstraint
    var_6 = python_code_.sqls_SqlNumberLiteral(value=var_5)
    assert isinstance(var_6, python_code_.sqls_SqlNumberLiteral)
    var_7 = "a;-<^O4h#zixs+"
    var_8 = python_code_.sqls_SqlParam(name=var_7)
    assert isinstance(var_8, python_code_.sqls_SqlParam)
    python_code_.sqls_EnumElement(name=var_7, text=var_7, sqls_EnumElement=var_5)
    var_49 = "_sqls_Trigger__sqls_Trigger104:sqls_InsertStatement75:_sqls_Trigger__sqls_Trigger104"
    var_50 = python_code_.sqls_SqlBinaryExpr(op=var_49)
    assert isinstance(var_50, python_code_.sqls_SqlBinaryExpr)
    var_55 = False
    var_56 = python_code_.sqls_OrderingTerm(asc=var_55, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_56, python_code_.sqls_OrderingTerm)


@pytest.mark.xfail(strict=True)
def test_49():
    var_3 = python_code_.sqls_TriggerUpdate()
    var_5 = python_code_.sqls_UniqueTableConstraint
    var_6 = python_code_.sqls_SqlNumberLiteral(value=var_5)
    assert isinstance(var_6, python_code_.sqls_SqlNumberLiteral)
    var_7 = "a;-<^O4h#zixs+"
    var_8 = python_code_.sqls_SqlParam(name=var_7)
    assert isinstance(var_8, python_code_.sqls_SqlParam)
    python_code_.sqls_EnumElement(name=var_7, text=var_7, sqls_EnumElement=var_5)
    var_13 = True
    var_14 = python_code_.sqls_Column(name=var_3, null=var_13, primaryKey=var_13)
    var_15 = python_code_.sqls_DeleteTable()
    var_16 = {var_14, var_14, var_14}
    var_17 = python_code_.sqls_Table(
        name=var_5, sqls_Table38=var_5, sqls_Table133=var_15, sqls_Table22=var_16
    )
    assert isinstance(var_17, python_code_.sqls_Table)
    python_code_.sqls_SqlMethod(
        array=var_6, name=var_5, sqls_SqlMethod37=var_17, sqls_SqlMethod131=var_8
    )


def test_50():
    var_37 = python_code_.sqls_SqlStringLiteral(value=1990.45)
    assert isinstance(var_37, python_code_.sqls_SqlStringLiteral)
    var_38 = 'if=I\x0bp"'
    var_43 = 2
    python_code_.sqls_SqlLibrary(database={"\x0bI*=:<n": True}, version=var_43)
    var_46 = python_code_.Type()
    var_50 = python_code_.sqls_SqlParam(name=853.63)
    assert isinstance(var_50, python_code_.sqls_SqlParam)
    python_code_.sqls_TableRef(
        alias=var_38, sqls_TableRef=var_46, sqls_TableRef64=var_37
    )


def test_51():
    var_22 = python_code_.sqls_SqlType()
    var_23 = -162
    var_24 = python_code_.sqls_SqlNumberLiteral(value=var_23)
    assert isinstance(var_24, python_code_.sqls_SqlNumberLiteral)
    var_26 = "_sqls_Trigger__sqls_Trigger104:sqls_InsertStatement75:_sqls_Trigger__sqls_Trigger104"
    var_27 = python_code_.sqls_SqlBinaryExpr(op=var_26)
    assert isinstance(var_27, python_code_.sqls_SqlBinaryExpr)
    var_34 = False
    var_35 = python_code_.sqls_OrderingTerm(asc=var_34, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_35, python_code_.sqls_OrderingTerm)
    var_38 = python_code_.sqls_SqlLibrary(database=var_26, version=var_22)
    python_code_.sqls_Tag(name=var_26, sqls_Tag=var_38)


def test_52():
    var_8 = python_code_.sqls_UniqueTableConstraint
    var_9 = python_code_.sqls_SqlNumberLiteral(value=var_8)
    assert isinstance(var_9, python_code_.sqls_SqlNumberLiteral)
    var_10 = "a;-<^O4h#zixs+"
    var_11 = python_code_.sqls_SqlParam(name=var_10)
    assert isinstance(var_11, python_code_.sqls_SqlParam)
    var_12 = python_code_.sqls_SqlType()
    python_code_.sqls_EnumElement(name=var_10, text=var_10, sqls_EnumElement=var_8)
    var_17 = "_sqls_Trigger__sqls_Trigger104:sqls_InsertStatement75:_sqls_Trigger__sqls_Trigger104"
    var_18 = python_code_.sqls_SqlBinaryExpr(op=var_17)
    assert isinstance(var_18, python_code_.sqls_SqlBinaryExpr)
    var_25 = False
    var_26 = python_code_.sqls_OrderingTerm(asc=var_25, desc=(), sqls_OrderingTerm=[])
    assert isinstance(var_26, python_code_.sqls_OrderingTerm)
    var_29 = python_code_.sqls_SqlLibrary(database=var_17, version=var_12)
    python_code_.sqls_Tag(name=var_17, sqls_Tag=var_29)


@pytest.mark.xfail(strict=True)
def test_53():
    var_1 = 'L\'1)}"loZ?"!('
    var_2 = bytes
    python_code_.sqls_Table(
        name=var_1,
        sqls_Table86=complex(1163.844, 1667.299368),
        sqls_Table133=var_2,
        sqls_Table19=b"/w\xc1\x9e\xeck\xd5",
        sqls_Table24=-4121,
    )


def test_54():
    var_0 = python_code_.TableConstraint()
    var_1 = python_code_.sqls_DeleteTable
    var_2 = python_code_.sqls_SqlExpr()
    var_3 = python_code_.sqls_Select(all=var_1, sqls_Select58=var_2)
    assert isinstance(var_3, python_code_.sqls_Select)
    var_8 = "sqls_Tablesqls_Type7_sqls_Column__sqls_Column29sqls_SqlMethod34"
    var_9 = python_code_.sqls_ResultColumn(name=var_8)
    var_13 = python_code_.sqls_Tag(
        name=("sqls_SqlExpr62", ":]\x0bp7 ZG", 3111.1), sqls_Tag35=var_9
    )
    var_14 = {var_13, var_13, var_13, var_13, var_13}
    var_15 = python_code_.sqls_Trigger(
        name=var_8,
        time=var_0,
        sqls_Trigger101=var_14,
        sqls_Trigger104=var_1,
        sqls_Trigger109=var_14,
        sqls_Trigger=var_14,
    )
    assert isinstance(var_15, python_code_.sqls_Trigger)
    var_20 = True
    var_21 = python_code_.sqls_OrderingTerm(asc=var_14, desc=var_20)
    var_26 = python_code_.sqls_SqlStringLiteral(value=var_3)
    assert isinstance(var_26, python_code_.sqls_SqlStringLiteral)
    python_code_.sqls_Trigger(
        name=var_21, time=None, sqls_Trigger101=var_14, sqls_Trigger106=var_1
    )
    var_31 = python_code_.sqls_ColumnRef()
    python_code_.sqls_TableRef(alias=var_8, sqls_TableRef126=var_31)
    var_33 = python_code_.sqls_SqlParam(name=var_8)
    assert isinstance(var_33, python_code_.sqls_SqlParam)
