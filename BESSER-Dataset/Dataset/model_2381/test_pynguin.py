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
    ActionGranularityType,
    ActionTimeType,
    Constraint,
    DataType,
    DistinctUserDefinedType,
    ENamedElement,
    Enum,
    ReferenceConstraint,
    ReferentialActionType,
    SQLObject,
    Table,
    TableConstraint,
    TypedElement,
    UniqueConstraint,
    UserDefinedType,
    abstractmethod,
    date,
    datetime,
    relational_Assertion,
    relational_BaseTable,
    relational_CheckConstraint,
    relational_Column,
    relational_Comment,
    relational_Constraint,
    relational_DataType,
    relational_DistinctUserDefinedType,
    relational_Domain,
    relational_ENamedElement,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_ReferenceConstraint,
    relational_SQLObject,
    relational_Schema,
    relational_Table,
    relational_TableConstraint,
    relational_Trigger,
    relational_TypedElement,
    relational_UniqueConstraint,
    relational_UserDefinedType,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_16 = python_code_.relational_TableConstraint()
    var_17 = 'O"jqG6'
    var_18 = "A\x0b\tp\t;GXB"
    var_19 = python_code_.relational_Domain(defaultValue=var_18, nullable=var_16)
    assert isinstance(var_19, python_code_.relational_Domain)
    python_code_.relational_CheckConstraint(
        searchCondition=var_17, relational_CheckConstraint=var_19
    )


def test_1():
    var_4 = python_code_.relational_Domain(
        defaultValue="uniqueConstraint,_relational_CheckConstraint__relational_CheckConstraint",
        nullable=True,
        relational_Domain49=None,
    )
    assert isinstance(var_4, python_code_.relational_Domain)


def test_2():
    var_1 = False
    var_2 = lambda *args, **kwargs: []
    var_3 = python_code_.relational_DataType()
    var_4 = python_code_.relational_Domain(
        defaultValue="RESTRICT",
        nullable=var_1,
        relational_Domain=var_2,
        relational_Domain49=var_3,
    )
    assert isinstance(var_4, python_code_.relational_Domain)


def test_3():
    var_10 = "relational_ReferenceConstraint"
    var_11 = python_code_.relational_DataType()
    var_12 = python_code_.relational_Domain(
        defaultValue=var_10, nullable=var_10, relational_Domain49=var_11
    )
    assert isinstance(var_12, python_code_.relational_Domain)


def test_4():
    var_12 = python_code_.relational_ForeignKey(
        onUpdate="qXI4T{i%uk", onDelete="}CQeAXgI|xC^8E>y0 *", foreignKey39=set()
    )
    assert isinstance(var_12, python_code_.relational_ForeignKey)


def test_5():
    var_12 = python_code_.relational_ForeignKey(
        onUpdate="_relational_SQLObject__sqlobject.referencedTable._relational_Trigger__triggersConstrainted",
        onDelete="_relational_Column__membersschema8Table26",
        referencingForeignKeys=None,
    )
    assert isinstance(var_12, python_code_.relational_ForeignKey)


def test_6():
    var_10 = "_relational_Trigger__triggers:relational_DataType:NO_ACTION:AFTER"
    var_11 = python_code_.relational_BaseTable()
    var_12 = python_code_.relational_ForeignKey(
        onUpdate=False,
        onDelete=var_10,
        ForeignKey=complex(-2791.0, 576.9),
        ForeignKey30=var_11,
        referencingForeignKeys=var_10,
    )
    assert isinstance(var_12, python_code_.relational_ForeignKey)


def test_7():
    var_17 = "O//2S&e"
    var_18 = python_code_.relational_ForeignKey(
        onUpdate=[True],
        onDelete=var_17,
        ForeignKey=var_17,
        referencingForeignKeys=None,
        foreignKey=1602,
    )
    assert isinstance(var_18, python_code_.relational_ForeignKey)


def test_8():
    var_9 = python_code_.relational_Column(
        nullable=False, defaultValue="SQLObject", length=2381, srid="8>[/,\nu\x0bn.a"
    )
    assert isinstance(var_9, python_code_.relational_Column)


def test_9():
    var_9 = python_code_.relational_Column(
        nullable=False, defaultValue="SQLObject", length=2381, srid="8>[/,\nu\x0bn.a"
    )
    assert isinstance(var_9, python_code_.relational_Column)
    var_10 = python_code_.relational_CheckConstraint(searchCondition=var_9)
    assert isinstance(var_10, python_code_.relational_CheckConstraint)
    var_11 = "_relational_ForeignKey__foreignKey,_relational_ForeignKey__foreignKey,_relational_ForeignKey__referencingForeignKeys"
    var_12 = (
        lambda *args, **kwargs: "relational_BaseTable-comments-_relational_Trigger__triggers-_relational_Trigger__Trigger22"
    )
    var_13 = python_code_.relational_ForeignKey(
        onUpdate={},
        onDelete=var_11,
        ForeignKey=417.45,
        ForeignKey30=var_12,
        foreignKey=var_9,
    )
    assert isinstance(var_13, python_code_.relational_ForeignKey)


def test_10():
    var_7 = python_code_.Constraint()
    var_10 = python_code_.relational_CheckConstraint(
        searchCondition="6IQ", relational_CheckConstraint=var_7
    )
    assert isinstance(var_10, python_code_.relational_CheckConstraint)
    var_17 = "*"
    var_18 = "BEFORE,relational_DataType"
    var_19 = "Dj%]\tg_Qwq`\tcC"
    var_21 = python_code_.relational_Column(
        nullable=False,
        defaultValue="_relational_ForeignKey__ForeignKey42,SET_NULL,relational_Column,schema6",
        length=878,
        srid=var_17,
        referencedMembers={var_19},
    )
    assert isinstance(var_21, python_code_.relational_Column)
    var_22 = python_code_.relational_ForeignKey(
        onUpdate=var_17,
        onDelete=var_18,
        ForeignKey=var_21,
        ForeignKey30="!Y_3r\rFmul8fm(4B'2",
    )
    assert isinstance(var_22, python_code_.relational_ForeignKey)
    var_24 = python_code_.relational_ENamedElement(name="")
    assert isinstance(var_24, python_code_.relational_ENamedElement)


def test_11():
    var_12 = python_code_.relational_Assertion(searchCondition="Rb~Uy!qh")
    assert isinstance(var_12, python_code_.relational_Assertion)


def test_12():
    var_12 = ";qTau1\t\nP\x0b\n<1"
    var_13 = python_code_.relational_Assertion(
        searchCondition=var_12, assertions="_relational_Trigger__Trigger22"
    )
    assert isinstance(var_13, python_code_.relational_Assertion)


def test_13():
    var_12 = python_code_.relational_ForeignKey(
        onUpdate="N,TI\x0c{i%|:Z6>fAwqm",
        onDelete="_relational_Domain__relational_Domain49",
        foreignKey=None,
    )
    assert isinstance(var_12, python_code_.relational_ForeignKey)
    var_18 = python_code_.relational_Schema()
    var_19 = python_code_.relational_Assertion(searchCondition=var_12, Assertion=var_18)
    assert isinstance(var_19, python_code_.relational_Assertion)


def test_14():
    var_8 = python_code_.relational_Schema()
    var_4 = python_code_.relational_Trigger(
        statementSQL='Y]c8"9',
        oldRow="Schema",
        newRow="TCIy,",
        oldTable='&OY{g-Y80\t"cCx>\nq',
        newTable="Comment_relational_ForeignKey__ForeignKey30",
        actionGranularity="relational_UniqueConstraint",
        updateType=False,
        insertType=True,
        deleteType=True,
        actionTime="relational_Table SET_DEFAULT CASCADE",
        condition="uF($`aX",
        triggers=var_8,
    )
    assert isinstance(var_4, python_code_.relational_Trigger)


def test_15():
    var_7 = True
    var_11 = "relational_UniqueConstraint"
    var_15 = python_code_.relational_Assertion(
        searchCondition=var_11, assertions={864, 2340.96}, Assertion=var_7
    )
    assert isinstance(var_15, python_code_.relational_Assertion)
    var_19 = python_code_.relational_Table()
    var_21 = python_code_.relational_Trigger(
        statementSQL="Wu?:w7F",
        oldRow=var_11,
        newRow=var_11,
        oldTable=var_11,
        newTable=var_11,
        actionGranularity="BaseTable36 STATEMENT _relational_Column__Column34",
        updateType=var_7,
        insertType=var_7,
        deleteType=True,
        actionTime="y)R&:`\rU0",
        condition="l3!#2KS.>c28",
        Trigger22=var_19,
        triggers13=var_19,
        Trigger20=None,
    )
    assert isinstance(var_21, python_code_.relational_Trigger)


def test_16():
    var_7 = True
    var_11 = "relational_UniqueConstraint"
    var_15 = python_code_.relational_Assertion(
        searchCondition=var_11, assertions={864, 2340.96}, Assertion=var_7
    )
    assert isinstance(var_15, python_code_.relational_Assertion)
    var_16 = lambda *args, **kwargs: [True]
    var_17 = python_code_.relational_Table()
    var_18 = python_code_.relational_Trigger(
        statementSQL=var_11,
        oldRow=4067.84,
        newRow=var_11,
        oldTable=var_11,
        newTable=var_16,
        actionGranularity=var_16,
        updateType="Table26_relational_ForeignKey__ForeignKeyROW",
        insertType={},
        deleteType=var_7,
        actionTime=[],
        condition=var_16,
        Trigger20=var_17,
    )
    assert isinstance(var_18, python_code_.relational_Trigger)


def test_17():
    var_6 = python_code_.relational_BaseTable()
    var_7 = python_code_.relational_SQLObject(
        description="AFTER", label="MxXY.\n=B", sqlobject=set(), SQLObject=var_6
    )
    assert isinstance(var_7, python_code_.relational_SQLObject)


def test_18():
    var_10 = python_code_.relational_SQLObject(
        description=-1, label=set(), SQLObject=[]
    )
    assert isinstance(var_10, python_code_.relational_SQLObject)


@pytest.mark.xfail(strict=True)
def test_19():
    var_4 = python_code_.relational_Domain(
        defaultValue="uniqueConstraint,_relational_CheckConstraint__relational_CheckConstraint",
        nullable=True,
        relational_Domain49=None,
    )
    assert isinstance(var_4, python_code_.relational_Domain)
    var_10 = "}Rj'ClQ(9"
    var_11 = python_code_.relational_Assertion
    var_12 = python_code_.relational_Comment(description=var_10)
    assert isinstance(var_12, python_code_.relational_Comment)
    python_code_.relational_SQLObject(
        description=var_10, label=var_11, SQLObject=var_12
    )


def test_20():
    var_7 = python_code_.relational_SQLObject(description="!", label="k_\n]H(A4e")
    assert isinstance(var_7, python_code_.relational_SQLObject)


def test_21():
    var_11 = python_code_.relational_Comment(description="F#JH'S\\F8G.iwN")
    assert isinstance(var_11, python_code_.relational_Comment)


def test_22():
    var_1 = False
    var_2 = lambda *args, **kwargs: []
    var_4 = python_code_.relational_Domain(defaultValue="comments", nullable=var_1)
    assert isinstance(var_4, python_code_.relational_Domain)
    var_9 = python_code_.relational_Comment(
        description="STATEMENT._relational_Trigger__Trigger22._relational_ForeignKey__ForeignKey30",
        Comment=var_2,
        comments=var_1,
    )
    assert isinstance(var_9, python_code_.relational_Comment)


def test_23():
    python_code_.relational_DataType()


def test_24():
    var_8 = "SQLObjectrelational_ReferenceConst4aintrelational_ForeiganKey"
    var_13 = python_code_.relational_ForeignKey(
        onUpdate=var_8, onDelete="*w_5HBvsuo7sFTA\t"
    )
    assert isinstance(var_13, python_code_.relational_ForeignKey)
    var_15 = python_code_.relational_Column(
        nullable=False,
        defaultValue='cjEDvq"SrG',
        length=1988,
        srid="|OE~NZsO}3G|~",
        Column=None,
        referencedMembers={1, var_13},
    )
    assert isinstance(var_15, python_code_.relational_Column)


def test_25():
    var_9 = python_code_.relational_TypedElement
    var_23 = python_code_.relational_Schema()
    var_24 = python_code_.relational_Assertion(searchCondition=var_9, assertions=var_23)
    assert isinstance(var_24, python_code_.relational_Assertion)
    var_29 = python_code_.relational_ENamedElement(name="0`}WZx'wTyj~#6z")
    assert isinstance(var_29, python_code_.relational_ENamedElement)


@pytest.mark.xfail(strict=True)
def test_26():
    var_13 = "_relational_SQLObject__sqlobject"
    var_14 = lambda *args, **kwargs: 527
    var_19 = "wNhX<K%FJR"
    var_20 = python_code_.relational_SQLObject(
        description=var_13, label=var_19, SQLObject=var_14
    )
    assert isinstance(var_20, python_code_.relational_SQLObject)
    python_code_.relational_Comment(description=var_19, comments=var_20)


def test_27():
    var_4 = "i`sr_MErN uz$Nfx"
    var_2 = python_code_.relational_ForeignKey(
        onUpdate="referencedTable table relational_BaseTable _relational_ForeignKey__foreignKey",
        onDelete="_relational_CheckConstraint__relational_CheckConstraint",
        foreignKey=None,
        foreignKey39=set(),
        ForeignKey42=var_4,
    )
    assert isinstance(var_2, python_code_.relational_ForeignKey)


def test_28():
    var_11 = python_code_.relational_Comment(description="Zw/;Mc3zL8$K8q]")
    assert isinstance(var_11, python_code_.relational_Comment)
    var_12 = "O\x0b//2S&e"
    var_13 = python_code_.relational_ForeignKey(
        onUpdate="A%.)TO",
        onDelete="STW~A\n<*e",
        ForeignKey=var_12,
        referencingForeignKeys=var_12,
        foreignKey=None,
        ForeignKey42=None,
    )
    assert isinstance(var_13, python_code_.relational_ForeignKey)


def test_29():
    var_8 = "SQLObjectrelational_ReferenceConst4aintrelational_ForeiganKey"
    var_10 = python_code_.relational_Column(
        nullable=True,
        defaultValue=var_8,
        length=2829,
        srid="vB)Du@>\n-S][\x0bo",
        referencedMembers=set(),
        Column40=var_8,
    )
    assert isinstance(var_10, python_code_.relational_Column)


def test_30():
    var_12 = python_code_.relational_ForeignKey(
        onUpdate="MB50yY^4Gk1Zjk",
        onDelete="ROWINSTEADOF_relational_Trigger__triggers13",
        ForeignKey30=None,
        ForeignKey42=None,
    )
    assert isinstance(var_12, python_code_.relational_ForeignKey)
    var_20 = python_code_.relational_CheckConstraint(searchCondition=var_12)
    assert isinstance(var_20, python_code_.relational_CheckConstraint)
    var_21 = 2214
    var_22 = set()
    var_23 = python_code_.relational_Column(
        nullable=var_12,
        defaultValue=var_20,
        length=var_21,
        srid=var_12,
        members=var_22,
        referencedMembers=None,
        Column40=var_12,
    )
    assert isinstance(var_23, python_code_.relational_Column)


def test_31():
    var_4 = "i`sr_MErN uz$Nfx"
    var_2 = python_code_.relational_ForeignKey(
        onUpdate="referencedTable table relational_BaseTable _relational_ForeignKey__foreignKey",
        onDelete="_relational_CheckConstraint__relational_CheckConstraint",
        foreignKey=None,
        foreignKey39=set(),
        ForeignKey42=var_4,
    )
    assert isinstance(var_2, python_code_.relational_ForeignKey)
    var_6 = python_code_.relational_TableConstraint()
    var_9 = "l|v7qVAb$>+#"
    var_10 = python_code_.relational_UniqueConstraint()
    var_11 = True
    var_12 = int
    var_13 = python_code_.relational_Column(
        nullable=var_11,
        defaultValue=var_12,
        length=var_12,
        srid=var_4,
        members=(),
        Column40=var_6,
    )
    assert isinstance(var_13, python_code_.relational_Column)
    var_14 = {var_13}
    var_15 = python_code_.relational_ForeignKey(
        onUpdate=var_4,
        onDelete=var_9,
        ForeignKey="0\\}:j.!lv&|D?\nH=b\t",
        foreignKey=var_10,
        foreignKey39=var_14,
        ForeignKey42=var_12,
    )
    assert isinstance(var_15, python_code_.relational_ForeignKey)


def test_32():
    var_6 = True
    var_10 = "INSTEADOF:BaseTable36:referencedTable"
    var_11 = "+#WM;HleW"
    var_12 = "O[B]"
    var_14 = python_code_.relational_Trigger(
        statementSQL="\r6gOg(",
        oldRow=var_11,
        newRow="",
        oldTable="-b8WQ'EOeG",
        newTable="_relational_Column__columns-_relational_Column__Column40-SET_NULL-schema6",
        actionGranularity=var_12,
        updateType=var_6,
        insertType=False,
        deleteType=False,
        actionTime="A\t'\\nMr;'NO_nx=O1,)",
        condition="r<PW&|h*m^7N",
        triggers13=var_10,
        triggersConstrainted=set(),
        Trigger20=None,
    )
    assert isinstance(var_14, python_code_.relational_Trigger)


def test_33():
    var_12 = python_code_.relational_ForeignKey(
        onUpdate="table24 _relational_Trigger__Trigger20 comments",
        onDelete="o -[U&c6CMG9",
        referencingForeignKeys=None,
        foreignKey=None,
        ForeignKey42=None,
    )
    assert isinstance(var_12, python_code_.relational_ForeignKey)
    var_19 = "5AG"
    var_20 = "_relational_Assertion__Assertion"
    var_21 = False
    var_22 = lambda *args, **kwargs: -243
    var_23 = python_code_.relational_Table()
    var_24 = python_code_.relational_Schema()
    var_25 = python_code_.relational_Trigger(
        statementSQL=var_19,
        oldRow=var_19,
        newRow=var_20,
        oldTable=var_20,
        newTable=var_12,
        actionGranularity={"VI5e9M!sp'-Z}": "z81lXLMy|]ip"},
        updateType=var_21,
        insertType=var_19,
        deleteType=var_20,
        actionTime=var_22,
        condition=var_22,
        Trigger22=var_23,
        Trigger=var_24,
    )
    assert isinstance(var_25, python_code_.relational_Trigger)


def test_34():
    var_10 = True
    var_11 = "SQLObjectrelational_ReferenceConstraintrelational_ForeignKey"
    var_12 = python_code_.relational_Column(
        nullable=var_10,
        defaultValue=var_11,
        length=var_10,
        srid=var_10,
        Column34=var_10,
    )
    assert isinstance(var_12, python_code_.relational_Column)


def test_35():
    var_9 = python_code_.relational_Column(
        nullable=False,
        defaultValue="_relational_Comment__comments",
        length=-22,
        srid="",
        Column=None,
        referencedMembers={False, True, True},
        Column40=None,
    )
    assert isinstance(var_9, python_code_.relational_Column)


def test_36():
    var_8 = "SQLObjectrelational_RefereneConst4aintrelational_ForeiganKey"
    var_12 = python_code_.relational_Column(
        nullable=True,
        defaultValue="_relational_Column__Column34,_relational_Comment__Comment",
        length=-732,
        srid="_relational_SQLObject__SQLObject",
        Column=var_8,
    )
    assert isinstance(var_12, python_code_.relational_Column)


def test_37():
    var_9 = python_code_.relational_Column(
        nullable=False,
        defaultValue="A&q|/x77hT}%\na)hwgT",
        length=1408,
        srid="o;}1~x.Fw]xXYW08",
        Column=None,
        members={-3691.07, 2288.68, False},
    )
    assert isinstance(var_9, python_code_.relational_Column)


def test_38():
    var_8 = "SQLObjectrelational_ReferenceConst4aintrelational_ForeiganKey"
    var_11 = python_code_.relational_Column(
        nullable=True, defaultValue=var_8, length=-601, srid=var_8, columns=var_8
    )
    assert isinstance(var_11, python_code_.relational_Column)


def test_39():
    var_0 = python_code_.TableConstraint()
    var_18 = "SQLObjectrelational_ReferenceConstraintrelational_ForeignKey"
    var_19 = python_code_.relational_Column(
        nullable=True,
        defaultValue=var_18,
        length=-1,
        srid="uniqueConstraint._relational_Domain__relational_Domain49",
        Column=None,
    )
    assert isinstance(var_19, python_code_.relational_Column)
    var_21 = python_code_.relational_Comment(
        description=complex(-3835.2182989, -1377.337464)
    )
    assert isinstance(var_21, python_code_.relational_Comment)
    var_22 = {var_21}
    var_23 = python_code_.relational_SQLObject(
        description=var_0, label=[-979.14, False], sqlobject=var_22
    )
    assert isinstance(var_23, python_code_.relational_SQLObject)


@pytest.mark.xfail(strict=True)
def test_40():
    var_3 = python_code_.relational_PrimaryKey()
    var_4 = "foreignKey39:_relational_Domain__relational_Domain"
    var_5 = python_code_.relational_Comment(
        description=var_4, Comment=[], comments=b"\xbf\x17"
    )
    assert isinstance(var_5, python_code_.relational_Comment)
    var_6 = python_code_.relational_Comment(
        description=var_4,
        Comment=var_3,
        comments={"7_RK\\)P": True, 'NC"\n]PRwlp': "EdC[r-\nL-*~)rQO"},
    )
    var_7 = {var_5, var_5, var_5, var_5, var_6}
    python_code_.relational_SQLObject(
        description=(-4333.88, 1641.06), label=var_4, sqlobject=var_7, SQLObject=var_5
    )


def test_41():
    var_2 = python_code_.DataType()
    var_3 = python_code_.relational_Schema()
    var_4 = python_code_.relational_BaseTable()
    var_6 = python_code_.ActionGranularityType.STATEMENT
    var_7 = ""
    var_8 = lambda *args, **kwargs: -1
    var_9 = python_code_.relational_Domain(
        defaultValue=var_7, nullable=var_3, relational_Domain49=var_8
    )
    assert isinstance(var_9, python_code_.relational_Domain)
    var_10 = python_code_.relational_CheckConstraint(
        searchCondition=var_7, relational_CheckConstraint=var_3
    )
    assert isinstance(var_10, python_code_.relational_CheckConstraint)
    var_14 = "/,SNy\\PF=!V6b;f4\x0cZ"
    var_15 = "e(~rca|jb{`-Kh#6s"
    var_16 = False
    var_17 = "Column40 Table26 _relational_Assertion__assertions"
    var_18 = python_code_.relational_Trigger(
        statementSQL=var_7,
        oldRow=var_6,
        newRow=var_14,
        oldTable=var_15,
        newTable=var_14,
        actionGranularity=var_15,
        updateType=var_9,
        insertType=var_16,
        deleteType=var_7,
        actionTime=var_17,
        condition=var_2,
        Trigger22=var_8,
    )
    assert isinstance(var_18, python_code_.relational_Trigger)
    var_20 = python_code_.relational_SQLObject(description=var_7, label=var_17)
    assert isinstance(var_20, python_code_.relational_SQLObject)
    var_22 = python_code_.relational_ForeignKey(
        onUpdate=var_8, onDelete=var_9, ForeignKey42=var_18
    )
    assert isinstance(var_22, python_code_.relational_ForeignKey)
    var_28 = python_code_.relational_ReferenceConstraint()
    var_32 = "_relational_Comment__comments:relational_SQLObject"
    var_33 = "xdV5)=:6qCnG4=\r"
    var_34 = python_code_.relational_Column(
        nullable=var_16,
        defaultValue=b"!/#\xa7\xd40\xf2\xe6\xdeu",
        length=complex(-2243.3, -259.0),
        srid=var_33,
        Column=complex(-1765.65, 2379.568),
        columns=set(),
        Column40=var_22,
        Column34=var_28,
    )
    assert isinstance(var_34, python_code_.relational_Column)
    var_35 = {var_34, var_34}
    python_code_.relational_ForeignKey(
        onUpdate=[-1832.35], onDelete=var_32, ForeignKey30=var_4, foreignKey39=var_35
    )


def test_42():
    var_1 = python_code_.relational_DataType()
    var_4 = python_code_.relational_DistinctUserDefinedType()
    var_9 = python_code_.UniqueConstraint()
    var_10 = "R*%bV/-'bwdi:t"
    var_11 = python_code_.relational_SQLObject(description=var_10, label=("1L3eOo?U",))
    assert isinstance(var_11, python_code_.relational_SQLObject)
    var_13 = "s}'o@j-{"
    var_14 = False
    var_15 = 'Ar."B\trPhEQpe'
    var_16 = python_code_.relational_TypedElement
    var_17 = -2452
    var_18 = python_code_.relational_Column(
        nullable=var_16, defaultValue=var_16, length=var_17, srid=566, columns=var_1
    )
    assert isinstance(var_18, python_code_.relational_Column)
    var_19 = {var_18, var_18}
    var_20 = python_code_.relational_PrimaryKey()
    var_21 = python_code_.relational_ForeignKey(
        onUpdate=var_16, onDelete=var_15, ForeignKey=var_16
    )
    assert isinstance(var_21, python_code_.relational_ForeignKey)
    var_22 = {var_20, var_21, var_20}
    var_23 = python_code_.relational_ReferenceConstraint()
    var_24 = python_code_.relational_Column(
        nullable=var_14,
        defaultValue=var_4,
        length=var_1,
        srid=var_9,
        referencedMembers=var_22,
        Column34=var_23,
    )
    assert isinstance(var_24, python_code_.relational_Column)
    var_25 = python_code_.relational_ForeignKey(
        onUpdate=var_13, onDelete=(), ForeignKey=var_18, foreignKey39=var_19
    )
    assert isinstance(var_25, python_code_.relational_ForeignKey)
    var_30 = "Ox\"\x0b-U4kvyZ~<C3'd"
    var_31 = "Dn?NuLo"
    var_32 = python_code_.relational_Trigger(
        statementSQL=var_30,
        oldRow=[],
        newRow=var_13,
        oldTable=var_13,
        newTable=(-192,),
        actionGranularity=var_31,
        updateType=var_16,
        insertType=var_14,
        deleteType=var_14,
        actionTime=var_16,
        condition=var_16,
        Trigger22=0,
        triggers=-1938.51,
    )
    assert isinstance(var_32, python_code_.relational_Trigger)
    var_45 = python_code_.relational_ForeignKey(
        onUpdate=var_31, onDelete=var_15, referencingForeignKeys=(-2607.64,)
    )
    assert isinstance(var_45, python_code_.relational_ForeignKey)
    var_46 = python_code_.relational_Column(
        nullable=var_15,
        defaultValue=var_15,
        length=var_24,
        srid=var_30,
        referencedMembers=var_15,
        Column40=var_45,
        Column34="k_ ",
    )
    assert isinstance(var_46, python_code_.relational_Column)
