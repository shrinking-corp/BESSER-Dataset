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
    rdbms_DocumentRoot,
    rdbms_EStringToStringMapEntry,
    rdbms_RDBMS,
    rdbms_column,
    rdbms_columns,
    rdbms_foreignKey,
    rdbms_foreignKeys,
    rdbms_hasForeignKeys,
    rdbms_key,
    rdbms_key2,
    rdbms_oID,
    rdbms_referencedColumns,
    rdbms_referencedKeys,
    rdbms_schema,
    rdbms_schemas,
    rdbms_table,
    rdbms_tables,
    time,
)


def test_0():
    var_2 = python_code_.rdbms_table(
        kind="_rdbms_DocumentRoot__rdbms_DocumentRoot40",
        name="_rdbms_key__rdbms_key57",
        oID="_rdbms_schema__rdbms_schema",
    )
    var_3 = python_code_.rdbms_referencedKeys
    var_4 = python_code_.rdbms_referencedColumns(
        group="rdbms_table84",
        rdbms_referencedColumns54=var_2,
        rdbms_referencedColumns62=set(),
        rdbms_referencedColumns=var_2,
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = {var_4, var_4}
    python_code_.rdbms_DocumentRoot(
        mixed=var_3,
        rdbms_DocumentRoot7=["V", True],
        rdbms_DocumentRoot20=set(),
        rdbms_DocumentRoot23=b"z\xd7\xce\xd6\xf3\x9d\xa5\x94\xd5\xcf-4\x81!)\x03.\xd7\xaa",
        rdbms_DocumentRoot31=var_5,
    )


def test_1():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_51 = {var_0}
    var_53 = python_code_.rdbms_referencedColumns(
        group=var_0, rdbms_referencedColumns=var_51
    )
    assert isinstance(var_53, python_code_.rdbms_referencedColumns)


def test_2():
    var_0 = "&(4HO!"
    var_12 = python_code_.rdbms_referencedKeys(group=var_0)
    var_13 = "_rdbms_referenceColumns__rdbms_referencedColumns"
    var_14 = python_code_.rdbms_referencedColumns(
        group=var_13, rdbms_referencedColumns62=var_0, rdbms_referencedColumns45=var_12
    )
    assert isinstance(var_14, python_code_.rdbms_referencedColumns)
    python_code_.rdbms_foreignKeys(group="HHHncy\\r<<{[\x0c#s\tcI")


@pytest.mark.xfail(strict=True)
def test_3():
    var_50 = "_rdbms_tables__rdbms_tables"
    var_51 = python_code_.rdbms_key(oID=".#O9uQb Dx", kind='P"\x0cr.1c', name=var_50)
    var_53 = "KNds|IY\\E QBo6B<"
    python_code_.rdbms_referencedColumns(group=var_53, rdbms_referencedColumns54=var_51)


def test_4():
    var_3 = python_code_.rdbms_referencedKeys
    var_4 = python_code_.rdbms_referencedColumns(
        group=var_3, rdbms_referencedColumns54=var_3
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    python_code_.rdbms_foreignKeys(
        group=var_3, rdbms_foreignKeys72=var_3, rdbms_foreignKeys=0
    )


def test_5():
    var_4 = python_code_.rdbms_referencedColumns(
        group="_rdbms_foreignKeys__rdbms_foreignKeys72"
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    python_code_.rdbms_foreignKeys(group="HHHncy\\r<<{[\x0c#s\tcI")


def test_6():
    var_78 = python_code_.rdbms_tables(group=[])
    assert isinstance(var_78, python_code_.rdbms_tables)


def test_7():
    var_31 = python_code_.rdbms_table
    var_35 = python_code_.rdbms_hasForeignKeys(group=var_31)
    var_38 = "rdbms_foreignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_39 = python_code_.rdbms_DocumentRoot(
        mixed=var_35, rdbms_DocumentRoot25=".u,l`X-H;;iP\n\n1q(9q"
    )
    var_40 = python_code_.rdbms_tables(group=var_38, rdbms_tables=var_39)
    assert isinstance(var_40, python_code_.rdbms_tables)


def test_8():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_54 = python_code_.rdbms_schema
    python_code_.rdbms_table(kind=var_0, name=var_54, oID=var_54)
    var_56 = python_code_.rdbms_schemas(group=599)
    assert isinstance(var_56, python_code_.rdbms_schemas)


def test_9():
    var_0 = "u&(4HO!"
    var_3 = python_code_.rdbms_schema(
        kind=var_0, name=var_0, oID="rdbms_foreignKey44", rdbms_schema75=None
    )
    var_13 = python_code_.rdbms_table(
        kind=[],
        name=var_0,
        oID=var_3,
        rdbms_table80={"rdbms_DocumentRoot13"},
        rdbms_table84=b"#\xcbH\x8b\xf7\x81\x8c\x8c#\r5\xe2\xe5",
    )
    assert isinstance(var_13, python_code_.rdbms_table)


@pytest.mark.xfail(strict=True)
def test_10():
    var_17 = python_code_.rdbms_table
    var_18 = "rdbms_foreignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_21 = python_code_.rdbms_table(kind=var_18, name=var_18, oID=var_17)
    python_code_.rdbms_columns(group=var_18, rdbms_columns78=var_21)


def test_11():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_1 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    var_2 = python_code_.rdbms_table(
        kind=var_1, name=var_1, oID=var_1, rdbms_table77=var_0, rdbms_table80=2
    )
    assert isinstance(var_2, python_code_.rdbms_table)
    var_3 = python_code_.rdbms_referencedKeys
    var_4 = python_code_.rdbms_referencedColumns(
        group=var_3, rdbms_referencedColumns54=var_3
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    python_code_.rdbms_oID(oID=var_3, rdbms_oID66=983.8)
    var_9 = "_rdbms_tables__rdbms_tables"
    python_code_.rdbms_key(
        oID={"@L[6*H!+H=8", True, '/1 ._CRXxPjs<1s"Q'}, kind=var_9, name=var_1
    )
    python_code_.rdbms_key(oID="G:)?Fg,Iu'", kind=None, name=var_4, rdbms_key57=var_3)


def test_12():
    var_0 = "u&(4HO!"
    var_1 = python_code_.rdbms_RDBMS()
    var_2 = python_code_.rdbms_referencedKeys
    var_3 = python_code_.rdbms_schema(
        kind=var_0,
        name="rdbms_RDBMS59_rdbms_DocumentRoot__rdbms_DocumentRoot27",
        oID="t\x0bU-JT?k",
        rdbms_schema=None,
    )
    var_4 = {var_3, var_3, var_3, var_3, var_3}
    var_5 = python_code_.rdbms_schemas(
        group=var_0, rdbms_schemas60=var_1, rdbms_schemas74=var_4
    )
    assert isinstance(var_5, python_code_.rdbms_schemas)
    python_code_.rdbms_foreignKey(
        refersTo=var_2,
        kind=var_3,
        name=-2400.25,
        oID=[True, 3410.7],
        owner=1292,
        rdbms_foreignKey48=var_3,
    )


def test_13():
    var_76 = tuple
    var_77 = python_code_.rdbms_schemas(group=var_76)
    assert isinstance(var_77, python_code_.rdbms_schemas)


def test_14():
    var_0 = "u&(4H=O!"
    var_22 = python_code_.rdbms_schemas(
        group="7\r@ja\t`q;", rdbms_schemas60=None, rdbms_schemas=var_0
    )
    assert isinstance(var_22, python_code_.rdbms_schemas)


def test_15():
    var_61 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    python_code_.rdbms_schema(
        kind="_rdbms_column__rdbms_column2",
        name=var_61,
        oID=var_61,
        rdbms_schema68=None,
        rdbms_schema71=var_61,
        rdbms_schema75=None,
        rdbms_schema=None,
    )


@pytest.mark.xfail(strict=True)
def test_16():
    var_24 = python_code_.rdbms_table
    var_25 = python_code_.rdbms_hasForeignKeys(group=var_24)
    var_26 = "rdbms_foreignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_27 = python_code_.rdbms_DocumentRoot(
        mixed=var_25, rdbms_DocumentRoot25=".u,l`X-H;;iP\n\n1q(9q"
    )
    var_28 = python_code_.rdbms_tables(group=var_26, rdbms_tables=var_27)
    assert isinstance(var_28, python_code_.rdbms_tables)
    var_29 = python_code_.rdbms_referencedKeys(
        group="%",
        rdbms_referencedKeys=None,
        rdbms_referencedKeys65={var_28, 1999, "2.JKY'fPUo,%DeX"},
    )
    python_code_.rdbms_oID(oID="\nF! ", rdbms_oID66=var_29, rdbms_oID=var_27)
    python_code_.rdbms_schema(
        kind=var_24, name=var_24, oID=var_24, rdbms_schema68=var_28
    )


def test_17():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_61 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    python_code_.rdbms_schema(
        kind=var_61,
        name="3\x0c1g@& \x0c%+,Do}s!{e",
        oID="hFEo/#",
        rdbms_schema75=None,
        rdbms_schema=var_0,
    )
    python_code_.rdbms_schema(kind="}w*\x0b+&>u~u;:", name=var_61, oID="rdbms_column4")


@pytest.mark.xfail(strict=True)
def test_18():
    var_13 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    var_14 = python_code_.rdbms_referencedKeys
    var_15 = python_code_.rdbms_referencedColumns(
        group=var_14, rdbms_referencedColumns54=var_14
    )
    assert isinstance(var_15, python_code_.rdbms_referencedColumns)
    var_16 = {var_15, var_15}
    var_17 = python_code_.rdbms_DocumentRoot(
        mixed=var_14,
        rdbms_DocumentRoot7=["V", True],
        rdbms_DocumentRoot20=set(),
        rdbms_DocumentRoot23=b"z\xd7\xce\xd6\xf3\x9d\xa5\x94\xd5\xcf-4\x81!)\x03.\xd7\xaa",
        rdbms_DocumentRoot31=var_16,
    )
    python_code_.rdbms_oID(oID=var_14, rdbms_oID66=983.8)
    var_19 = python_code_.rdbms_foreignKeys(
        group=var_14, rdbms_foreignKeys72=var_14, rdbms_foreignKeys=0
    )
    var_20 = "_rdbms_tables__rdbms_tables"
    python_code_.rdbms_key(
        oID={"@L[6*H!+H=8", True, '/1 ._CRXxPjs<1s"Q'}, kind=var_20, name=var_13
    )
    var_22 = "qF\nBU\x0cg=-@A-p?j~"
    var_23 = "KNds|IY\\E QBo6B<"
    var_24 = python_code_.rdbms_schemas(group=var_23, rdbms_schemas=var_17)
    assert isinstance(var_24, python_code_.rdbms_schemas)
    python_code_.rdbms_schema(
        kind=var_22,
        name=var_14,
        oID=var_23,
        rdbms_schema71=var_19,
        rdbms_schema75=var_24,
    )


def test_19():
    python_code_.rdbms_foreignKeys(group="HHHncy\\r<<{[\x0c#s\tcI")


def test_20():
    var_1 = "\tT_"
    python_code_.rdbms_foreignKey(
        refersTo=var_1, kind=var_1, name=var_1, oID=var_1, owner=var_1
    )


def test_21():
    var_3 = python_code_.rdbms_table
    var_4 = python_code_.rdbms_referencedColumns(
        group="_rdbms_foreignKeys__rdbms_foreignKeys72"
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_50 = ""
    var_51 = "o KH\\&p&"
    var_52 = python_code_.rdbms_foreignKeys(group=6048)
    var_53 = python_code_.rdbms_foreignKey(
        refersTo=var_3,
        kind=var_3,
        name=var_50,
        oID=var_50,
        owner=var_51,
        rdbms_foreignKey48=var_52,
    )
    assert isinstance(var_53, python_code_.rdbms_foreignKey)


def test_22():
    var_61 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    python_code_.rdbms_oID(oID=var_61)


def test_23():
    var_3 = python_code_.rdbms_referencedKeys
    var_4 = python_code_.rdbms_referencedColumns(
        group="Bb)", rdbms_referencedColumns45=None
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = {var_4, var_4}
    python_code_.rdbms_DocumentRoot(
        mixed=var_3,
        rdbms_DocumentRoot7=["V", True],
        rdbms_DocumentRoot20=set(),
        rdbms_DocumentRoot23=b"z\xd7\xce\xd6\xf3\x9d\xa5\x94\xd5\xcf-4\x81!)\x03.\xd7\xaa",
        rdbms_DocumentRoot31=var_5,
    )
    python_code_.rdbms_oID(oID=var_3, rdbms_oID66=983.8)


def test_24():
    var_0 = python_code_.rdbms_hasForeignKeys(
        group="rdbms_oID66", rdbms_hasForeignKeys=None
    )
    var_1 = sorted
    python_code_.rdbms_oID(oID=("'f", True), rdbms_oID63=var_0, rdbms_oID=var_1)


def test_25():
    var_1 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbm_DocumentRoot29"
    python_code_.rdbms_table(
        kind="_rdbms_DocumentRoot__rdbms_DocumentRoot40",
        name="_rdbms_key__rdbms_key57",
        oID="_rdbms_schema__rdbms_schema",
    )
    var_3 = python_code_.rdbms_referencedKeys
    var_4 = python_code_.rdbms_referencedColumns(
        group=var_1, rdbms_referencedColumns62={True, "\t{T\n2F"}
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = {var_4, var_4}
    var_6 = python_code_.rdbms_DocumentRoot(
        mixed=var_3,
        rdbms_DocumentRoot7=["V", True],
        rdbms_DocumentRoot20=set(),
        rdbms_DocumentRoot23=b"z\xd7\xce\xd6\xf3\x9d\xa5\x94\xd5\xcf-4\x81!)\x03.\xd7\xaa",
        rdbms_DocumentRoot31=var_5,
    )
    python_code_.rdbms_oID(oID="rdbms_key2", rdbms_oID51=var_6)
    var_54 = "rdbms_RDBMS-_rdbms_referencedColumns__rdbms_referencedColumns62-r-dbms_DocumentRoot"
    python_code_.rdbms_column(
        kind=var_1,
        name=var_1,
        oID=var_54,
        type=-1642,
        rdbms_column=(False, 770.37, True),
    )


def test_26():
    var_15 = "_rdbms_tables__rdbms_tables"
    var_23 = tuple
    python_code_.rdbms_key(oID=var_23, kind=var_15, name=var_15)


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = "g6|s-\nR-7;MNK+]UN"
    var_1 = "$,[?~76Y=A/Z"
    python_code_.rdbms_schema(kind=var_0, name=None, oID=var_1)
    var_3 = python_code_.rdbms_foreignKeys(group=var_0)
    var_4 = python_code_.rdbms_key2
    python_code_.rdbms_oID(oID=var_3, rdbms_oID=var_4)
    python_code_.rdbms_key(
        oID=var_4,
        kind=var_4,
        name=var_3,
        rdbms_key53=b"\xcde\xdc\xf4\xf9",
        rdbms_key=var_1,
    )
    var_7 = set()
    python_code_.rdbms_DocumentRoot(
        mixed=var_1,
        rdbms_DocumentRoot10=var_7,
        rdbms_DocumentRoot20=var_7,
        rdbms_DocumentRoot16=var_3,
        rdbms_DocumentRoot38=1076.55,
    )


def test_28():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_62 = "_rdbms_tables__rdbms_tables"
    python_code_.rdbms_key(oID=var_62, kind="bu?V", name=var_62, rdbms_key53=var_0)
    var_65 = python_code_.rdbms_tables(group="")
    assert isinstance(var_65, python_code_.rdbms_tables)


@pytest.mark.xfail(strict=True)
def test_29():
    var_50 = "rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot7"
    var_51 = "[YOx"
    var_52 = python_code_.rdbms_key2
    var_53 = python_code_.rdbms_hasForeignKeys(
        group=var_51, rdbms_hasForeignKeys=var_52
    )
    var_54 = "rdbms_RDBMS-_rdbms_referencedColumns__rdbms_referencedColumns62-rdbms_DocumentRoot"
    var_55 = python_code_.rdbms_column(
        kind=var_50,
        name=var_50,
        oID=var_54,
        type=-1642,
        rdbms_column=(False, 770.37, True),
    )
    var_56 = {var_55}
    var_57 = python_code_.rdbms_columns(group=var_53, rdbms_columns=var_56)
    assert isinstance(var_57, python_code_.rdbms_columns)
    var_58 = {var_57, var_57}
    python_code_.rdbms_DocumentRoot(
        mixed='H4FI\ni"pi', rdbms_DocumentRoot13=var_58, rdbms_DocumentRoot33=False
    )


def test_30():
    var_0 = "*+<W1UM7"
    python_code_.rdbms_columns(group=var_0)
    var_22 = python_code_.rdbms_tables(group=[])
    assert isinstance(var_22, python_code_.rdbms_tables)


def test_31():
    var_0 = python_code_.rdbms_key2()
    var_1 = len
    python_code_.rdbms_columns(group=var_1, rdbms_columns14=var_1)
    var_4 = "{BnT-qR"
    var_5 = list
    var_6 = python_code_.rdbms_key(oID=var_4, kind=var_5, name=var_4, rdbms_key57=var_0)
    var_7 = python_code_.rdbms_tables(group=[])
    assert isinstance(var_7, python_code_.rdbms_tables)
    python_code_.rdbms_oID(oID=var_4, rdbms_oID66=var_6, rdbms_oID=var_5)


def test_32():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_1 = "_rdbms_Documentoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbm_DocumentRoot29"
    var_4 = python_code_.rdbms_referencedColumns(
        group=var_1, rdbms_referencedColumns45=None
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = {var_4, var_4}
    python_code_.rdbms_DocumentRoot(
        mixed="_c%L_'15aBdlZuO'+h",
        rdbms_DocumentRoot=set(),
        rdbms_DocumentRoot25={False, var_0},
        rdbms_DocumentRoot13=set(),
        rdbms_DocumentRoot40=var_5,
        rdbms_DocumentRoot31=var_5,
    )


def test_33():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_51 = {"rdbms_column rdbms_foreignKeys47"}
    python_code_.rdbms_DocumentRoot(
        mixed="XIH[",
        rdbms_DocumentRoot25={"", True},
        rdbms_DocumentRoot16=var_51,
        rdbms_DocumentRoot38={var_0, var_0, False},
        rdbms_DocumentRoot42=var_51,
    )


def test_34():
    var_51 = {"rdbms_column rdbms_foreignKeys47"}
    python_code_.rdbms_DocumentRoot(
        mixed="V1\n:",
        rdbms_DocumentRoot7=var_51,
        rdbms_DocumentRoot25=var_51,
        rdbms_DocumentRoot31=set(),
    )


def test_35():
    var_0 = "I"
    var_31 = python_code_.rdbms_table
    python_code_.rdbms_hasForeignKeys(
        group=var_0, rdbms_hasForeignKeys50={-3604.11, var_31, 1193.45}
    )
    var_38 = "rdbms_DocumentRoot18 rdbms_foreignKeys47 _rdbms_columns__rdbms_columns"
    var_39 = python_code_.rdbms_DocumentRoot(
        mixed=var_38,
        rdbms_DocumentRoot7=set(),
        rdbms_DocumentRoot10=set(),
        rdbms_DocumentRoot23=set(),
        rdbms_DocumentRoot27=set(),
        rdbms_DocumentRoot16=set(),
        rdbms_DocumentRoot40=set(),
        rdbms_DocumentRoot29=set(),
    )
    var_40 = python_code_.rdbms_tables(group=var_38, rdbms_tables=var_39)
    assert isinstance(var_40, python_code_.rdbms_tables)


def test_36():
    var_31 = python_code_.rdbms_table
    var_35 = python_code_.rdbms_hasForeignKeys(group=var_31)
    python_code_.rdbms_DocumentRoot(
        mixed=var_35, rdbms_DocumentRoot25=".u,l`X-H;;iP\n\n1q(9q"
    )


def test_37():
    var_0 = "%"
    var_31 = python_code_.rdbms_table
    python_code_.rdbms_hasForeignKeys(group=var_31)
    var_38 = "rdbms_fore7ignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_39 = python_code_.rdbms_DocumentRoot(
        mixed=var_38,
        rdbms_DocumentRoot10={"wg%ZN`?Qi", True},
        rdbms_DocumentRoot20={-311, var_0},
        rdbms_DocumentRoot23={-1532, var_38, False},
        rdbms_DocumentRoot25=set(),
        rdbms_DocumentRoot36={False, 1263},
        rdbms_DocumentRoot38=set(),
        rdbms_DocumentRoot29={var_31, var_31, var_38},
        rdbms_DocumentRoot31=set(),
        rdbms_DocumentRoot33=set(),
    )
    python_code_.rdbms_referencedKeys(
        group=var_31, rdbms_referencedKeys=var_31, rdbms_referencedKeys34=var_39
    )


def test_38():
    var_4 = python_code_.rdbms_referencedColumns(
        group="n?1AWrdx", rdbms_referencedColumns=None
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    python_code_.rdbms_hasForeignKeys(group="3#[]P", rdbms_hasForeignKeys50={var_4})


def test_39():
    python_code_.rdbms_hasForeignKeys(group=(), rdbms_hasForeignKeys21={-624})


def test_40():
    python_code_.rdbms_hasForeignKeys(group="*St)iMNRyop")


@pytest.mark.xfail(strict=True)
def test_41():
    var_50 = "iA<Qllh7Q"
    var_52 = python_code_.rdbms_hasForeignKeys(group=var_50)
    python_code_.rdbms_column(
        kind="x%w\ngXWk8>ZPc9h", name=var_50, oID=var_50, type="", rdbms_column2=var_52
    )


def test_42():
    var_0 = ""
    var_31 = python_code_.rdbms_foreignKeys
    python_code_.rdbms_hasForeignKeys(
        group=var_0,
        rdbms_hasForeignKeys=var_31,
        rdbms_hasForeignKeys50={var_31, 1, 1098.0},
    )
    python_code_.rdbms_key(oID=var_31, kind=var_0, name=var_0)


def test_43():
    python_code_.rdbms_referencedKeys(group='D)H^)XT*U"aGO4\n]l')


@pytest.mark.xfail(strict=True)
def test_44():
    var_0 = python_code_.rdbms_key2()
    var_1 = "R\x0cs:n"
    python_code_.rdbms_key(
        oID=var_1,
        kind=var_0,
        name={"m"},
        rdbms_key53=var_0,
        rdbms_key=b'"\x13*\x91\xe9\x8b1\xb5',
    )
    var_3 = "rdbms_DocumentRoot13rdbms_DocumentRoot27"
    var_4 = "o]<zx"
    python_code_.rdbms_key(oID=var_3, kind=var_1, name=var_4)
    var_6 = "rdbms_DocumentRoot18 _rdbms_DocumentRoot__rdbms_DocumentRoot25 rdbms_columns rdbms_referencedColumns"
    var_7 = "jz$5[K&"
    var_8 = python_code_.rdbms_columns(group=[], rdbms_columns={})
    var_9 = python_code_.rdbms_column(
        kind=var_4,
        name=var_6,
        oID=var_6,
        type=var_7,
        rdbms_column2=var_1,
        rdbms_column11=set(),
        rdbms_column4=var_8,
    )
    assert isinstance(var_9, python_code_.rdbms_column)
    python_code_.rdbms_referencedKeys(group=var_4, rdbms_referencedKeys=var_9)


def test_45():
    var_53 = "[Y0Ox"
    var_56 = "rdbms_RDBMS-_rdbms_referencedColumns__rdbms_referencedColumns62-rdbms_DocumentRoot"
    python_code_.rdbms_column(
        kind=var_53,
        name=var_53,
        oID=var_56,
        type=-1642,
        rdbms_column=(False, 770.37, True),
    )


def test_46():
    var_53 = "rdbmK_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot7"
    var_57 = "$"
    python_code_.rdbms_column(
        kind=var_57,
        name="rdbms_column4.rdbms_referencedKeys65",
        oID=var_53,
        type=var_53,
    )


def test_47():
    var_13 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    var_26 = "_rdbms_foreignKeys__rdbms_foreignKeys72"
    var_48 = "_rdbms_tables__rdbms_tables,_rdbms_DocumentRoot__rdbms_DocumentRoot10"
    var_55 = python_code_.rdbms_columns(group=var_26)
    var_56 = python_code_.rdbms_column(
        kind=0, name=var_13, oID=(True,), type=var_48, rdbms_column4=var_55
    )
    assert isinstance(var_56, python_code_.rdbms_column)


def test_48():
    var_24 = python_code_.rdbms_foreignKey
    var_25 = python_code_.rdbms_hasForeignKeys(group=var_24)
    var_26 = "rdbms_foreignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_27 = python_code_.rdbms_DocumentRoot(
        mixed=var_25, rdbms_DocumentRoot25=".u,l`X-H;;iP\n\n1q(9q"
    )
    var_28 = python_code_.rdbms_tables(group=var_26, rdbms_tables=var_27)
    assert isinstance(var_28, python_code_.rdbms_tables)
    python_code_.rdbms_referencedKeys(
        group="%",
        rdbms_referencedKeys=None,
        rdbms_referencedKeys65={var_28, 1999, "2.JKY'fPUo,%DeX"},
    )
    var_32 = python_code_.rdbms_schemas(group=var_24)
    assert isinstance(var_32, python_code_.rdbms_schemas)
    var_33 = "?j>+#NQ&<hm\n;^e]/+"
    var_34 = "rdbms_DocumentRoot42 _rdbms_DocumentRoot__rdbms_DocumentRoot29"
    python_code_.rdbms_column(
        kind=var_33,
        name=var_34,
        oID=-3200.93,
        type=var_34,
        rdbms_column2=None,
        rdbms_column11=var_27,
    )


def test_49():
    var_0 = "rdbms_columns,_rdbms_columns__rdbms_columns"
    var_1 = python_code_.rdbms_referencedColumns(
        group=var_0, rdbms_referencedColumns=None
    )
    assert isinstance(var_1, python_code_.rdbms_referencedColumns)
    var_2 = python_code_.rdbms_oID(oID=var_0, rdbms_oID63=var_1)
    assert isinstance(var_2, python_code_.rdbms_oID)
    python_code_.rdbms_hasForeignKeys(group=None)


def test_50():
    var_1 = "rdbms_DocumentRoot31"
    var_2 = python_code_.rdbms_RDBMS
    var_3 = "rdbms_key281"
    var_4 = python_code_.rdbms_referencedColumns(group=var_3)
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = python_code_.rdbms_oID(oID=var_2, rdbms_oID63=var_4)
    assert isinstance(var_5, python_code_.rdbms_oID)
    var_6 = {var_5}
    python_code_.rdbms_hasForeignKeys(group=var_1, rdbms_hasForeignKeys50=var_6)
    var_77 = {var_4, var_4}
    var_78 = python_code_.rdbms_DocumentRoot(
        mixed=var_2,
        rdbms_DocumentRoot7=["V", True],
        rdbms_DocumentRoot20=set(),
        rdbms_DocumentRoot23=b"z\xd7\xce\xd6\xf3\x9d\xa5\x94\xd5\xcf-4\x81!)\x03.\xd7\xaa",
        rdbms_DocumentRoot31=var_77,
    )
    var_79 = python_code_.rdbms_tables(group=var_1, rdbms_tables=var_78)
    assert isinstance(var_79, python_code_.rdbms_tables)


def test_51():
    var_1 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    var_3 = python_code_.rdbms_referencedKeys
    var_4 = python_code_.rdbms_referencedColumns(
        group=var_3, rdbms_referencedColumns54=var_3
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = {var_4, var_4}
    var_6 = python_code_.rdbms_DocumentRoot(
        mixed=var_3,
        rdbms_DocumentRoot7=["V", True],
        rdbms_DocumentRoot20=set(),
        rdbms_DocumentRoot23=b"z\xd7\xce\xd6\xf3\x9d\xa5\x94\xd5\xcf-4\x81!)\x03.\xd7\xaa",
        rdbms_DocumentRoot31=var_5,
    )
    python_code_.rdbms_oID(oID=var_3, rdbms_oID66=983.8)
    python_code_.rdbms_foreignKeys(
        group=var_3, rdbms_foreignKeys72=var_3, rdbms_foreignKeys=0
    )
    var_9 = "_rdbms_tables__rdbms_tables"
    python_code_.rdbms_key(
        oID={"@L[6*H!+H=8", True, '/1 ._CRXxPjs<1s"Q'}, kind=var_9, name=var_1
    )
    var_12 = "KNds|IY\\E QBo6B<"
    var_13 = python_code_.rdbms_schemas(group=var_12, rdbms_schemas=var_6)
    assert isinstance(var_13, python_code_.rdbms_schemas)
    var_49 = "sOb$BQYPmX"
    var_50 = python_code_.rdbms_column(
        kind=var_49,
        name=var_12,
        oID=var_49,
        type="rdbms_foreignKey48",
        rdbms_column4=var_49,
    )
    python_code_.rdbms_schemas(group=var_3)
    var_51 = {var_50, var_50, var_50}
    var_52 = python_code_.rdbms_columns(
        group=var_4, rdbms_columns=var_51, rdbms_columns14=var_3
    )
    assert isinstance(var_52, python_code_.rdbms_columns)


@pytest.mark.xfail(strict=True)
def test_52():
    var_0 = "rdbms_columns,_rdbms_columns__rdbms_columns"
    var_1 = python_code_.rdbms_referencedColumns(
        group=var_0, rdbms_referencedColumns=None
    )
    assert isinstance(var_1, python_code_.rdbms_referencedColumns)
    var_2 = python_code_.rdbms_oID(oID=var_0, rdbms_oID63=var_1)
    assert isinstance(var_2, python_code_.rdbms_oID)
    var_3 = "so*xwZ_"
    var_4 = python_code_.rdbms_key
    python_code_.rdbms_schema(
        kind=var_3,
        name=var_1,
        oID=var_3,
        rdbms_schema68=True,
        rdbms_schema71=1394,
        rdbms_schema=var_4,
    )
    var_7 = "93l}B"
    var_8 = "rdbms_RDBMS"
    var_9 = python_code_.rdbms_hasForeignKeys(group=var_8)
    python_code_.rdbms_column(
        kind=var_3,
        name="rdbms_DocumentRoot42",
        oID=var_7,
        type={"94ub~wwh\x0c", 0, "2"},
        rdbms_column2=var_9,
    )


def test_53():
    var_0 = "*+<W1U?M7"
    python_code_.rdbms_referencedKeys(group=var_0, rdbms_referencedKeys34=False)
    var_2 = "rdbmK_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot7"
    var_3 = "NA<Qllh7Q"
    var_4 = python_code_.rdbms_key2
    python_code_.rdbms_hasForeignKeys(group=var_3, rdbms_hasForeignKeys=var_4)
    var_6 = "rdbms_RDBMS-_r\tdbms_referencedColumns__rdbms_referencedColumns62-rdbms_DocumentRoot"
    python_code_.rdbms_column(
        kind=var_6, name="rdbms_column4.rdbms_referencedKeys65", oID=var_2, type=var_0
    )


@pytest.mark.xfail(strict=True)
def test_54():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_1 = "G_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbm_DocumentRoot29"
    var_2 = python_code_.rdbms_table(
        kind="_rdbms_DocumentRoot__rdbms_DocumentRoot40",
        name="_rdbms_key__rdbms_key57",
        oID="_rdbms_schema__rdbms_schema",
    )
    var_58 = python_code_.rdbms_foreignKeys(group=complex(-822.880883, 609.3))
    python_code_.rdbms_column(
        kind=var_1,
        name=var_1,
        oID=(),
        type=var_1,
        rdbms_column2=(),
        rdbms_column11=var_1,
    )
    python_code_.rdbms_DocumentRoot(
        mixed=var_58,
        rdbms_DocumentRoot10=var_2,
        rdbms_DocumentRoot18=var_0,
        rdbms_DocumentRoot42=var_1,
        rdbms_DocumentRoot33=(),
    )


def test_55():
    var_24 = python_code_.rdbms_table
    var_25 = python_code_.rdbms_hasForeignKeys(group=var_24)
    var_26 = "rdbms_foreignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_27 = python_code_.rdbms_DocumentRoot(
        mixed=var_25, rdbms_DocumentRoot25=".u,l`X-H;;iP\n\n1q(9q"
    )
    var_28 = python_code_.rdbms_tables(group=var_26, rdbms_tables83=set())
    assert isinstance(var_28, python_code_.rdbms_tables)
    var_29 = python_code_.rdbms_referencedKeys(
        group="%",
        rdbms_referencedKeys=None,
        rdbms_referencedKeys65={var_28, 1999, "2.JKY'fPUo,%DeX"},
    )
    python_code_.rdbms_oID(oID="\nF! ", rdbms_oID66=var_29, rdbms_oID=var_27)


@pytest.mark.xfail(strict=True)
def test_56():
    var_0 = str
    var_4 = "s\x0b=]|l&`#;&}~AJM#n"
    var_9 = "?"
    python_code_.rdbms_schema(
        kind={}, name=None, oID=var_4, rdbms_schema71={"D$+)&": 2855}
    )
    var_10 = complex
    python_code_.rdbms_schema(kind=var_9, name=-125, oID=var_10, rdbms_schema75=3210.53)
    var_18 = "_rdbms_table__rdbms_table77"
    var_19 = "w.0gvG~6q2p[f=@r%p5"
    python_code_.rdbms_key(oID=var_9, kind=var_18, name=var_19)
    var_22 = "lq9uC Dy"
    python_code_.rdbms_foreignKey(
        refersTo=var_0, kind=var_22, name=var_4, oID=var_10, owner=2834
    )
    python_code_.rdbms_columns(group=var_10, rdbms_columns=var_0)


def test_57():
    var_31 = python_code_.rdbms_table
    var_44 = "_rdbms_DocumentRoot__rdbms_DocumentRoot29,_rdbms_DocumentRoot__rdbms_DocumentRoot25,_rdbms_hasForeignKeys__rdbms_hasForeignKeys21,_rdbms_columns__rdbms_columns14"
    var_45 = "~"
    var_46 = "rdbms_foreignKeys,_rdbms_oID__rdbms_oID51,rdbms_hasForeignKeys21,rdbms_foreignKey48"
    python_code_.rdbms_foreignKey(
        refersTo=var_44,
        kind=var_44,
        name=(2254,),
        oID=var_45,
        owner=var_46,
        rdbms_foreignKey=(),
        rdbms_foreignKey48=var_31,
        rdbms_foreignKey44=complex(1922.44, -1585.485029),
    )


def test_58():
    var_0 = "*+<W1UM7"
    python_code_.rdbms_schema(
        kind=var_0, name=var_0, oID="f", rdbms_schema75=None, rdbms_schema=None
    )
    var_25 = python_code_.rdbms_RDBMS()
    var_26 = "`"
    var_27 = python_code_.rdbms_key2()
    python_code_.rdbms_key(oID=var_25, kind=True, name=var_26, rdbms_key57=var_27)


def test_59():
    var_0 = "*+<W1U? M7"
    var_13 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_Do4umentRoot__rdbms_DocumentRoot29"
    var_14 = python_code_.rdbms_referencedKeys
    var_15 = python_code_.rdbms_referencedColumns(
        group=var_14, rdbms_referencedColumns54=var_14
    )
    assert isinstance(var_15, python_code_.rdbms_referencedColumns)
    python_code_.rdbms_oID(oID=var_13, rdbms_oID51=None)
    python_code_.rdbms_foreignKeys(
        group=var_0,
        rdbms_foreignKeys72=var_0,
        rdbms_foreignKeys=None,
        rdbms_foreignKeys47={var_0, 1498.53},
    )


def test_60():
    var_61 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    var_62 = python_code_.rdbms_table
    var_67 = "rdbms_foreignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_70 = "_rdbms_oID__rdbms_oID63,rdbms_DocumentRoot16"
    python_code_.rdbms_foreignKey(
        refersTo=var_70,
        kind=var_61,
        name=var_67,
        oID=var_62,
        owner=var_70,
        rdbms_foreignKey44=-1630,
    )


@pytest.mark.xfail(strict=True)
def test_61():
    var_31 = python_code_.rdbms_table
    var_44 = "_rdbms_DocumentRoot__rdbms_DocumentRoot29,_rdbms_DocumentRoot__rdbms_DocumentRoot25,_rdbms_hasForeignKeys__rdbms_hasForeignKeys21,_rdbms_columns__rdbms_columns14"
    var_45 = "~"
    var_46 = "rdbms_foreignKeys,_rdbms_oID__rdbms_oID51,rdbms_hasForeignKeys21,rdbms_foreignKey48"
    python_code_.rdbms_foreignKey(
        refersTo=var_44,
        kind=var_44,
        name=(2254,),
        oID=var_45,
        owner=var_46,
        rdbms_foreignKey=(),
        rdbms_foreignKey48=var_31,
        rdbms_foreignKey44=complex(1922.44, -1585.485029),
    )
    var_48 = "xgu6!_L2"
    python_code_.rdbms_DocumentRoot(
        mixed=var_48,
        rdbms_DocumentRoot7=(),
        rdbms_DocumentRoot18={
            "": 188.7,
            "_rdbms_DocumentRoot__rdbms_DocumentRoot40": -1282.7,
            "Vegl6wE": True,
        },
        rdbms_DocumentRoot42=3434.62,
        rdbms_DocumentRoot33=var_31,
    )


def test_62():
    var_1 = "rdbms_DocumentRoot31"
    var_2 = python_code_.rdbms_RDBMS
    var_3 = "rdbms_key281"
    var_4 = python_code_.rdbms_referencedColumns(group=var_3)
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = python_code_.rdbms_oID(oID=var_2, rdbms_oID63=var_4)
    assert isinstance(var_5, python_code_.rdbms_oID)
    var_6 = {var_5}
    var_7 = python_code_.rdbms_hasForeignKeys(group=var_1, rdbms_hasForeignKeys50=var_6)
    var_70 = "rdbms_foreignKeys47,rdbms_hasForeignKeys,_rdbms_tables__rdbms_tables69,_rdbms_DocumentRoot__rdbms_DocumentRoot31"
    var_71 = python_code_.rdbms_DocumentRoot(
        mixed=var_1,
        rdbms_DocumentRoot7=var_6,
        rdbms_DocumentRoot23=set(),
        rdbms_DocumentRoot27=var_6,
        rdbms_DocumentRoot36={var_7, 1326.98, var_2},
        rdbms_DocumentRoot38={131, -5653.49, -1},
        rdbms_DocumentRoot33=set(),
    )
    var_72 = python_code_.rdbms_tables(group=var_70, rdbms_tables=var_71)
    assert isinstance(var_72, python_code_.rdbms_tables)
    var_73 = python_code_.rdbms_referencedKeys(
        group="%",
        rdbms_referencedKeys=None,
        rdbms_referencedKeys65={var_72, 1999, "2.JKY'fPUo,%DeX"},
    )
    python_code_.rdbms_oID(oID="\nF! ", rdbms_oID66=var_73, rdbms_oID=var_71)
    var_75 = python_code_.rdbms_RDBMS()
    var_76 = python_code_.rdbms_schemas(group=var_3, rdbms_schemas60=var_75)
    assert isinstance(var_76, python_code_.rdbms_schemas)


def test_63():
    var_0 = "&(4HO!"
    var_12 = python_code_.rdbms_referencedKeys(group=var_0)
    var_13 = "_rdbms_referenceColumns__rdbms_referencedColumns"
    var_14 = python_code_.rdbms_referencedColumns(
        group=var_13, rdbms_referencedColumns62=var_0, rdbms_referencedColumns45=var_12
    )
    assert isinstance(var_14, python_code_.rdbms_referencedColumns)
    var_15 = lambda *args, **kwargs: []
    var_16 = set()
    var_17 = python_code_.rdbms_DocumentRoot(
        mixed=var_15,
        rdbms_DocumentRoot={-780.94, False, 1193},
        rdbms_DocumentRoot38=b"s88\\0\xa0,\xda\xae\x82\x1c\xb8v\xd1\x10",
        rdbms_DocumentRoot33=var_16,
    )
    python_code_.rdbms_foreignKeys(group="HHHncy\\r<<{[\x0c#s\tcI")
    python_code_.rdbms_hasForeignKeys(group=var_0, rdbms_hasForeignKeys21=var_17)


@pytest.mark.xfail(strict=True)
def test_64():
    var_3 = python_code_.rdbms_referencedKeys
    var_7 = python_code_.rdbms_oID(oID=var_3, rdbms_oID66=983.8)
    python_code_.rdbms_foreignKeys(
        group=var_3, rdbms_foreignKeys72=var_3, rdbms_foreignKeys=0
    )
    var_11 = "qF\nBU\x0cg=-@A-p?j~"
    python_code_.rdbms_oID(oID=var_3)
    var_52 = python_code_.rdbms_RDBMS()
    var_55 = "rdbms_DocumentRoot18"
    python_code_.rdbms_columns(group=var_55, rdbms_columns14=var_52)
    var_58 = "_rdbms_DocumentRoot__rdbms_DocumentRoot23 _rdbms_DocumentRoot__rdbms_DocumentRoot31 _rdbms_columns__rdbms_columns14"
    var_59 = python_code_.rdbms_hasForeignKeys(group=var_11)
    var_60 = {var_59, var_59, var_59, var_59}
    python_code_.rdbms_DocumentRoot(
        mixed=var_58,
        rdbms_DocumentRoot={},
        rdbms_DocumentRoot20=var_60,
        rdbms_DocumentRoot16=var_60,
        rdbms_DocumentRoot18=var_60,
        rdbms_DocumentRoot36=var_3,
        rdbms_DocumentRoot42=var_11,
        rdbms_DocumentRoot29=var_7,
        rdbms_DocumentRoot33=var_60,
    )


def test_65():
    var_0 = "&(4HO!"
    var_12 = python_code_.rdbms_referencedKeys(group=var_0)
    var_13 = "_rdbms_referenceColumns__rdbms_referencedColumns"
    var_14 = python_code_.rdbms_referencedColumns(
        group=var_13, rdbms_referencedColumns62=var_0, rdbms_referencedColumns45=var_12
    )
    assert isinstance(var_14, python_code_.rdbms_referencedColumns)
    var_16 = set()
    var_17 = python_code_.rdbms_DocumentRoot(
        mixed=var_0,
        rdbms_DocumentRoot7=set(),
        rdbms_DocumentRoot10={1232.67},
        rdbms_DocumentRoot27=var_16,
        rdbms_DocumentRoot38=var_16,
        rdbms_DocumentRoot29=var_16,
    )
    python_code_.rdbms_referencedKeys(
        group="rdbms_referencedKeys65._rdbms_DocumentRoot__rdbms_DocumentRoot38._rdbms_table__rdbms_table80",
        rdbms_referencedKeys34=var_17,
    )
    var_24 = '5?\r}":]9O+UU'
    var_25 = python_code_.rdbms_referencedKeys(
        group=var_13, rdbms_referencedKeys65=var_16
    )
    var_30 = "h;jWC/F?o"
    var_31 = python_code_.rdbms_schemas(group=var_30, rdbms_schemas60=var_13)
    assert isinstance(var_31, python_code_.rdbms_schemas)
    var_26 = python_code_.rdbms_oID(oID=var_24, rdbms_oID66=var_25, rdbms_oID63=var_14)
    assert isinstance(var_26, python_code_.rdbms_oID)
    python_code_.rdbms_oID(oID=var_0)


@pytest.mark.xfail(strict=True)
def test_66():
    var_1 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbm_DocumentRoot29"
    var_2 = python_code_.rdbms_table(
        kind="_rdbms_DocumentRoot__rdbms_DocumentRoot40",
        name="_rdbms_key__rdbms_key57",
        oID="_rdbms_schema__rdbms_schema",
    )
    var_3 = python_code_.rdbms_RDBMS
    var_4 = python_code_.rdbms_referencedColumns(
        group="rdbms_table84",
        rdbms_referencedColumns54=var_2,
        rdbms_referencedColumns62=set(),
        rdbms_referencedColumns=var_2,
    )
    assert isinstance(var_4, python_code_.rdbms_referencedColumns)
    var_5 = {var_4, var_4}
    python_code_.rdbms_DocumentRoot(
        mixed="HM%H_yo", rdbms_DocumentRoot=set(), rdbms_DocumentRoot10=set()
    )
    python_code_.rdbms_oID(oID=var_3, rdbms_oID66=983.8)
    var_54 = "rdbms_RDBMS-_rdbms_referencedColumns__rdbms_referencedColumns62-r-dbms_DocumentRoot"
    var_55 = python_code_.rdbms_column(
        kind=var_1,
        name=var_1,
        oID=var_54,
        type=-1642,
        rdbms_column=(False, 770.37, True),
    )
    var_57 = set()
    var_58 = python_code_.rdbms_tables(group=var_57)
    assert isinstance(var_58, python_code_.rdbms_tables)
    var_59 = python_code_.rdbms_tables(
        group=var_54, rdbms_tables69=var_3, rdbms_tables83=var_5, rdbms_tables=-2202
    )
    assert isinstance(var_59, python_code_.rdbms_tables)
    var_60 = {var_58, var_58, var_58, var_59, var_58}
    python_code_.rdbms_DocumentRoot(
        mixed=complex(537.961, 549.37814),
        rdbms_DocumentRoot=var_57,
        rdbms_DocumentRoot7={True},
        rdbms_DocumentRoot10=b"e\xa7\x95\xa9\xf6!,\x1eu\x85R\x97",
        rdbms_DocumentRoot13=True,
        rdbms_DocumentRoot18=var_55,
        rdbms_DocumentRoot36=True,
        rdbms_DocumentRoot42=var_60,
    )


@pytest.mark.xfail(strict=True)
def test_67():
    var_1 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbm_DocumentRoot29"
    var_3 = python_code_.rdbms_RDBMS
    python_code_.rdbms_DocumentRoot(
        mixed="HM%H_yo", rdbms_DocumentRoot=set(), rdbms_DocumentRoot10=set()
    )
    python_code_.rdbms_oID(oID=var_3, rdbms_oID66=983.8)
    var_54 = "rdbms_RDBMS-_rdbms_referencedColumns__rdbms_referencedColumns62-r-dbms_DocumentRoot"
    python_code_.rdbms_column(
        kind="QhxP\t3a3NDTR5JHzp ", name=var_54, oID=var_54, type=var_54
    )
    var_56 = set()
    var_58 = python_code_.rdbms_tables(group=var_1)
    assert isinstance(var_58, python_code_.rdbms_tables)
    var_62 = python_code_.rdbms_columns(
        group=var_54,
        rdbms_columns78={
            "]%u/a/F": "_rdbms_foreignKeys__rdbms_foreignKeys47,rdbms_schema,rdbms_referencedColumns54,rdbms_foreignKeys72",
            "IO": 1156.29,
            "rdbms_oID": -390,
        },
    )
    python_code_.rdbms_table(
        kind=var_56, name=var_1, oID=var_54, rdbms_table77=var_62, rdbms_table84=var_58
    )


@pytest.mark.xfail(strict=True)
def test_68():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_61 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    var_63 = python_code_.rdbms_schema(
        kind=var_61,
        name="3\x0c1g@& \x0c%+,Do}s!{e",
        oID="hFEo/#",
        rdbms_schema75=None,
        rdbms_schema=var_0,
    )
    var_71 = python_code_.rdbms_schema(
        kind="VW'EcNw!.{nMU}1>Il!", name=var_61, oID="%+f`V~dD|+0", rdbms_schema=var_61
    )
    var_72 = {var_63, -958.94, 0}
    var_75 = "rdbms_RDBMS-_rdbms_referencedColumns__rdbms_referencedColumns62-r-dbms_DocumentRoot"
    python_code_.rdbms_column(
        kind=var_61,
        name=var_61,
        oID=var_75,
        type=-1642,
        rdbms_column=(False, 770.37, True),
    )
    var_77 = set()
    var_78 = "\twP3"
    var_79 = python_code_.rdbms_schemas
    var_80 = python_code_.rdbms_key(oID=var_71, kind=var_78, name=var_79)
    var_81 = python_code_.rdbms_key2()
    var_82 = python_code_.rdbms_key(
        oID=var_75, kind=complex(2022.5081, 2042.24), name=var_79, rdbms_key57=var_81
    )
    var_83 = {var_80, var_80, var_80, var_82, var_80}
    python_code_.rdbms_DocumentRoot(
        mixed=var_78,
        rdbms_DocumentRoot=var_77,
        rdbms_DocumentRoot10=var_72,
        rdbms_DocumentRoot23=var_83,
        rdbms_DocumentRoot16=var_72,
        rdbms_DocumentRoot42=var_79,
    )


@pytest.mark.xfail(strict=True)
def test_69():
    var_1 = "\tT_"
    var_4 = python_code_.rdbms_hasForeignKeys(group=var_1)
    var_5 = bool
    var_6 = python_code_.rdbms_tables(group=var_1)
    assert isinstance(var_6, python_code_.rdbms_tables)
    var_7 = python_code_.rdbms_table(
        kind=var_4, name=var_5, oID=var_1, rdbms_table84=var_6
    )
    assert isinstance(var_7, python_code_.rdbms_table)
    var_8 = {var_4, var_4}
    python_code_.rdbms_DocumentRoot(
        mixed=var_6,
        rdbms_DocumentRoot7=var_5,
        rdbms_DocumentRoot20=var_8,
        rdbms_DocumentRoot25=var_8,
        rdbms_DocumentRoot27=var_1,
        rdbms_DocumentRoot18=var_5,
        rdbms_DocumentRoot38=var_8,
    )


def test_70():
    var_0 = python_code_.rdbms_EStringToStringMapEntry()
    var_61 = "_rdbms_DocumentRoot__rdbms_DocumentRoot20,rdbms_DocumentRoot10,rdbms_columns,_rdbms_DocumentRoot__rdbms_DocumentRoot29"
    python_code_.rdbms_schema(
        kind=var_61,
        name="3\x0c1g@& \x0c%+,Do}s!{e",
        oID="hFEo/#",
        rdbms_schema75=None,
        rdbms_schema=var_0,
    )
    python_code_.rdbms_table(
        kind="(bMI7v~Yj/\rU!@c\rR",
        name=var_61,
        oID=var_61,
        rdbms_table80=var_0,
        rdbms_table84=None,
        rdbms_table=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_71():
    var_2 = "rdbms_foreignKey44:rdbms_DocumentRoot16"
    var_3 = "rdbms_schemas74,rdbms_DocumentRoot10"
    var_4 = "WY'*P*"
    var_5 = python_code_.rdbms_hasForeignKeys(group=var_4, rdbms_hasForeignKeys=b"A6ge")
    python_code_.rdbms_column(
        kind={True}, name=var_2, oID=set(), type=var_3, rdbms_column2=var_5
    )


@pytest.mark.xfail(strict=True)
def test_72():
    var_1 = "M9Mofn+"
    python_code_.rdbms_hasForeignKeys(group=var_1)
    var_3 = python_code_.rdbms_EStringToStringMapEntry()
    var_4 = "\tSe{.\nG7y"
    var_5 = {var_3}
    var_6 = len
    var_7 = python_code_.rdbms_referencedKeys(group=var_6, rdbms_referencedKeys65=var_5)
    var_8 = {var_7, var_7, var_7}
    var_9 = python_code_.rdbms_DocumentRoot(
        mixed=6025,
        rdbms_DocumentRoot=var_5,
        rdbms_DocumentRoot7=var_5,
        rdbms_DocumentRoot40=var_5,
        rdbms_DocumentRoot33=var_8,
    )
    python_code_.rdbms_foreignKeys(group=var_4, rdbms_foreignKeys=var_9)
    var_11 = "_rdbms_table__rdbms_table84"
    var_12 = python_code_.rdbms_column(kind=var_9, name=var_11, oID=var_4, type=None)
    python_code_.rdbms_hasForeignKeys(
        group=var_4, rdbms_hasForeignKeys=var_12, rdbms_hasForeignKeys21=var_9
    )
