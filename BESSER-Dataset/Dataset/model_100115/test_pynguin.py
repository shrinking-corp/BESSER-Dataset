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
    DataType,
    Enum,
    database_Column,
    database_Database,
    database_ForeignKey,
    database_Table,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = python_code_.database_Table(
        Name="", ColumnTable=set(), Table5=None, database_Table=None
    )
    assert isinstance(var_0, python_code_.database_Table)


def test_1():
    var_0 = python_code_.database_Table(
        Name="_database_ForeignKey__database_ForeignKey11", Table=None
    )
    assert isinstance(var_0, python_code_.database_Table)


@pytest.mark.xfail(strict=True)
def test_2():
    var_2 = python_code_.database_ForeignKey(
        Name="database_Database Float _database_ForeignKey__database_ForeignKey13",
        database_ForeignKey13=set(),
    )
    assert isinstance(var_2, python_code_.database_ForeignKey)
    python_code_.database_Table(
        Name="larZg?o",
        DbTable=None,
        Table5=None,
        database_Table=var_2,
        database_Table9=var_2,
    )


def test_3():
    var_4 = "#~(\x0b:"
    var_5 = int
    var_6 = "p?W5k?-6{\nB[R'j8:D"
    var_7 = python_code_.database_Table(
        Name=var_6, DbTable=var_4, Table5="qp#z", database_Table=var_5, Table=var_5
    )
    assert isinstance(var_7, python_code_.database_Table)


def test_4():
    var_0 = 3585
    var_5 = python_code_.database_Table(
        Name="3Ah", DbTable=var_0, database_Table9=var_0
    )
    assert var_5.database_Table9 == 3585


def test_5():
    var_13 = python_code_.database_ForeignKey(
        Name="database_Database Float _database_ForeignKey__database_ForeignKey13",
        database_ForeignKey13=set(),
    )
    assert isinstance(var_13, python_code_.database_ForeignKey)
    var_14 = bool
    var_15 = python_code_.database_Database()
    var_16 = python_code_.database_Table(
        Name=var_14, DbTable=var_15, Table5=(), Table=-2467
    )
    assert isinstance(var_16, python_code_.database_Table)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.database_Table(Name=True)
    assert isinstance(var_0, python_code_.database_Table)
    python_code_.database_ForeignKey(Name=1086.13, database_ForeignKey8=var_0)
    assert isinstance(var_0.database_Table9, python_code_.database_ForeignKey)


def test_7():
    var_0 = 3585
    var_5 = python_code_.database_Table(Name="IrKb%\\xHh;8", DbTable=None, Table=var_0)
    assert isinstance(var_5, python_code_.database_Table)


def test_8():
    var_2 = python_code_.database_ForeignKey(
        Name="database_Column14",
        database_ForeignKey=None,
        database_ForeignKey11=set(),
        DbFK=None,
        ForeignKey=None,
    )
    assert isinstance(var_2, python_code_.database_ForeignKey)


def test_9():
    var_2 = python_code_.database_ForeignKey(
        Name="database_Database Float _database_ForeignKey__database_ForeignKey13",
        database_ForeignKey13=set(),
    )
    assert isinstance(var_2, python_code_.database_ForeignKey)


def test_10():
    var_2 = python_code_.database_ForeignKey(Name="TxQ2f{ *\rsDcQ")
    assert isinstance(var_2, python_code_.database_ForeignKey)


def test_11():
    var_2 = str
    var_3 = python_code_.database_ForeignKey(
        Name="database_Database",
        database_ForeignKey8=None,
        database_ForeignKey13=set(),
        DbFK=var_2,
    )
    assert isinstance(var_3, python_code_.database_ForeignKey)


def test_12():
    var_0 = python_code_.database_Table(
        Name="", DbTable=None, Table5=None, database_Table9=None
    )
    assert isinstance(var_0, python_code_.database_Table)
    var_4 = python_code_.database_ForeignKey(
        Name=var_0, ForeignKey=complex(1268.2, -382.3655)
    )
    assert isinstance(var_4, python_code_.database_ForeignKey)


def test_13():
    var_1 = "database_ForeignKey11"
    var_2 = python_code_.database_Column
    var_3 = python_code_.database_Column(
        Name=(), Type=var_1, IsPrimaryKey=var_2, database_Column=set()
    )
    assert isinstance(var_3, python_code_.database_Column)
    var_4 = {var_3, var_3, var_3}
    var_5 = python_code_.database_ForeignKey(
        Name="7",
        database_ForeignKey=var_3,
        database_ForeignKey11=var_4,
        ForeignKey=var_4,
    )
    assert isinstance(var_5, python_code_.database_ForeignKey)


def test_14():
    var_2 = str
    var_3 = python_code_.database_ForeignKey(
        Name="FpdtMUVw~#p[T",
        database_ForeignKey=None,
        database_ForeignKey8=var_2,
        ForeignKey=var_2,
    )
    assert isinstance(var_3, python_code_.database_ForeignKey)


def test_15():
    python_code_.database_Column(
        Name=complex(-4316.0, 1460.154),
        Type="Date.Table5._database_ForeignKey__database_ForeignKey13._database_ForeignKey__DbFK",
        IsPrimaryKey=set(),
    )


def test_16():
    python_code_.DataType.Float


@pytest.mark.xfail(strict=True)
def test_17():
    var_1 = "'kj]7:|T"
    var_2 = bool
    var_3 = python_code_.database_ForeignKey(
        Name=var_2, database_ForeignKey=[], ForeignKey=True
    )
    assert isinstance(var_3, python_code_.database_ForeignKey)
    python_code_.database_Table(Name=var_1, DbTable=var_2, database_Table=var_3)


@pytest.mark.xfail(strict=True)
def test_18():
    var_6 = dict
    var_9 = "Table5"
    var_10 = "/q|3j2(q1V\nvLY*=-"
    var_11 = python_code_.database_Column(
        Name=var_9, Type=var_10, IsPrimaryKey=var_10, TableColumn=var_6
    )
    assert isinstance(var_11, python_code_.database_Column)
    python_code_.database_Table(Name=var_6, Table5=var_11, database_Table=(635.54,))


def test_19():
    var_2 = python_code_.database_ForeignKey(
        Name="database_Database Float _database_ForeignKey__database_ForeignKey13",
        database_ForeignKey13=set(),
    )
    assert isinstance(var_2, python_code_.database_ForeignKey)
    python_code_.database_Column(
        Name=b"MU+\x82\xabP<\x0es\x7f\xcf\xe2\xe0",
        Type=var_2,
        IsPrimaryKey=[],
        TableColumn=var_2,
    )


def test_20():
    var_0 = python_code_.database_Table(
        Name="", ColumnTable=set(), Table5=None, database_Table=None
    )
    assert isinstance(var_0, python_code_.database_Table)
    var_4 = list
    var_5 = python_code_.database_Column(
        Name=[219], Type=var_4, IsPrimaryKey=var_4, Column=var_0
    )
    assert isinstance(var_5, python_code_.database_Column)


def test_21():
    var_0 = python_code_.database_Table(Name="4g\t\x0bOk\x0c3n!_|cKs")
    assert isinstance(var_0, python_code_.database_Table)
    var_17 = 'g\\]w1"?&.UEV\n*!F\t$N'
    var_18 = python_code_.database_Column(
        Name=var_17,
        Type=2051.97,
        IsPrimaryKey=624,
        Column=var_0,
        database_Column=113,
        database_Column14=var_0,
    )
    assert isinstance(var_18, python_code_.database_Column)


def test_22():
    var_2 = python_code_.database_ForeignKey(
        Name="bf:U\nz>X",
        database_ForeignKey=None,
        database_ForeignKey8=None,
        database_ForeignKey11={205},
        DbFK=None,
        ForeignKey=None,
    )
    assert isinstance(var_2, python_code_.database_ForeignKey)
    var_14 = False
    var_15 = python_code_.database_Column(
        Name=set(),
        Type=var_2,
        IsPrimaryKey=var_14,
        Column=[],
        database_Column=var_2,
        database_Column14={"me;R<e%": False, ".<oh2?F1]qxcZN.9uy": -1095},
    )
    assert isinstance(var_15, python_code_.database_Column)


def test_23():
    var_2 = python_code_.database_ForeignKey(
        Name="E&L6&", database_ForeignKey8=None, DbFK=None
    )
    assert isinstance(var_2, python_code_.database_ForeignKey)
    var_13 = "]F"
    var_14 = python_code_.database_Column(
        Name=-1285.63, Type=var_13, IsPrimaryKey=var_13, database_Column=var_2
    )
    assert isinstance(var_14, python_code_.database_Column)


def test_24():
    var_2 = python_code_.database_ForeignKey(
        Name="database_Column14._database_Table__Table5", database_ForeignKey=None
    )
    assert isinstance(var_2, python_code_.database_ForeignKey)
    var_13 = b"\x05\xef\xb2\xa1\x99b\x0e\xbdC\xee\xa4\xe4\x83n\x1d\xbf\x8d\xb6"
    var_14 = python_code_.database_Column(
        Name=("Database16", "#+lmH5,&o\tG{6~"),
        Type=var_13,
        IsPrimaryKey={"7}_0/`d$": -2660, "DbTableRoot": "DbFkRoot"},
        database_Column=var_2,
        database_Column14=var_2,
    )
    assert isinstance(var_14, python_code_.database_Column)


def test_25():
    var_0 = python_code_.database_Table(Name="-d:w(4+tqlo$i6n#", Table5=None)
    assert isinstance(var_0, python_code_.database_Table)
    var_8 = python_code_.database_Table
    var_9 = python_code_.database_Column(
        Name=var_8, Type=var_8, IsPrimaryKey=set(), Column=var_8
    )
    assert isinstance(var_9, python_code_.database_Column)


def test_26():
    var_0 = "database_Table9"
    var_1 = "database_ForeignKey11"
    var_2 = python_code_.database_ForeignKey
    var_3 = python_code_.database_Column(
        Name=(), Type=var_1, IsPrimaryKey=var_2, database_Column=set()
    )
    assert isinstance(var_3, python_code_.database_Column)
    var_4 = {var_3, var_3, var_3}
    var_5 = python_code_.database_ForeignKey(Name=var_0, database_ForeignKey11=var_4)
    assert isinstance(var_5, python_code_.database_ForeignKey)


def test_27():
    var_4 = "#~(\x0b:"
    var_5 = int
    var_6 = "p?W5k?-6{\nB[R'j8:D"
    var_7 = python_code_.database_Table(
        Name=var_6, DbTable=var_4, Table5="qp#z", database_Table=var_5, Table=var_5
    )
    assert isinstance(var_7, python_code_.database_Table)
    var_8 = python_code_.database_Column(
        Name=var_4, Type=set(), IsPrimaryKey=var_5, Column=var_7
    )
    assert isinstance(var_8, python_code_.database_Column)
    var_9 = python_code_.database_Database()
    var_10 = python_code_.database_Column(
        Name=var_6, Type=var_8, IsPrimaryKey=(1, 2976.76), TableColumn=var_9
    )
    var_11 = {var_8, var_8, var_8, var_8, var_10}
    python_code_.database_Table(
        Name=set(), DbTable=var_9, ColumnTable=var_11, Table=b"|\nw\xd5\xba\xe0\xa5|}M"
    )


def test_28():
    var_2 = python_code_.database_Database
    var_4 = "\x0c"
    var_5 = python_code_.database_ForeignKey(
        Name=var_2, database_ForeignKey13=(), DbFK=var_4, ForeignKey=var_4
    )
    assert isinstance(var_5, python_code_.database_ForeignKey)
    var_7 = python_code_.database_Column(
        Name="!gx\n*HD", Type="T%&@o,'0V", IsPrimaryKey=True, database_Column=None
    )
    var_8 = {var_7, var_7, var_7, var_7, 3410.12}
    var_9 = python_code_.database_Table(
        Name={
            True,
            "_database_Column__database_Column14:_database_ForeignKey__ForeignKey:database_ForeignKey13",
        },
        ColumnTable=var_8,
        Table5=var_2,
    )
    assert isinstance(var_9, python_code_.database_Table)


def test_29():
    var_2 = str
    var_3 = python_code_.database_ForeignKey(
        Name="FpdtMUVw~#p[T",
        database_ForeignKey=None,
        database_ForeignKey8=var_2,
        ForeignKey=var_2,
    )
    assert isinstance(var_3, python_code_.database_ForeignKey)
    var_4 = "Database16-_dataCbase_ForeignKey__database_ForeignKey"
    var_5 = python_code_.database_Column(
        Name=var_2, Type=var_4, IsPrimaryKey=True, database_Column14=var_3
    )
    assert isinstance(var_5, python_code_.database_Column)
    var_6 = {var_5, var_5, var_5, var_4}
    var_7 = python_code_.database_ForeignKey(Name=var_2, database_ForeignKey13=var_6)
    assert isinstance(var_7, python_code_.database_ForeignKey)


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = 2514.409597936202
    var_4 = bool
    var_5 = "_database_ForeignKey__DbFK:DbFkRoot:Float"
    var_6 = python_code_.database_ForeignKey(
        Name=var_5,
        database_ForeignKey=complex(-2056.4601, 2350.39),
        database_ForeignKey8=var_0,
        database_ForeignKey13=(-440.21, "[x|8e", 3521.91),
        DbFK=None,
    )
    assert isinstance(var_6, python_code_.database_ForeignKey)
    var_7 = python_code_.database_Column(
        Name=var_4,
        Type=None,
        IsPrimaryKey=var_4,
        Column=var_4,
        database_Column=var_0,
        database_Column14=var_6,
    )
    assert isinstance(var_7, python_code_.database_Column)
    python_code_.database_Table(Name=var_5, ColumnTable=var_4)


@pytest.mark.xfail(strict=True)
def test_31():
    var_5 = int
    var_6 = "p?W5k?-6{\nB[R'j8:D"
    var_13 = python_code_.database_ForeignKey(Name=var_6, database_ForeignKey8=var_5)
    assert isinstance(var_13, python_code_.database_ForeignKey)
    var_14 = "_database_Table__DbTable"
    python_code_.database_Table(
        Name=var_14, Table5=True, database_Table=var_5, database_Table9=var_13
    )


def test_32():
    var_2 = complex
    var_4 = lambda *args, **kwargs: []
    var_5 = python_code_.database_Database()
    var_6 = python_code_.database_ForeignKey(Name=True)
    assert isinstance(var_6, python_code_.database_ForeignKey)
    var_7 = python_code_.database_Column(
        Name=var_4, Type=var_5, IsPrimaryKey=var_4, database_Column=var_6
    )
    assert isinstance(var_7, python_code_.database_Column)
    var_8 = {var_7}
    python_code_.database_ForeignKey(Name=var_2, database_ForeignKey11=var_8)


@pytest.mark.xfail(strict=True)
def test_33():
    var_4 = "#~(\x0b:"
    var_5 = int
    var_6 = "p?W5k?-6{\nB[R'j8:D"
    var_7 = python_code_.database_Table(
        Name=var_6, DbTable=var_4, Table5="qp#z", database_Table=var_5, Table=var_5
    )
    assert isinstance(var_7, python_code_.database_Table)
    var_8 = python_code_.database_Column(
        Name=var_4, Type=set(), IsPrimaryKey=var_5, Column=var_7
    )
    assert isinstance(var_8, python_code_.database_Column)
    var_9 = python_code_.database_Database()
    python_code_.database_Column(
        Name=var_6, Type=var_8, IsPrimaryKey=(1, 2976.76), TableColumn=var_9
    )
    python_code_.database_Column(
        Name="us/8tBB",
        Type=var_6,
        IsPrimaryKey=[],
        Column=var_5,
        TableColumn=var_7,
        database_Column=var_7,
        database_Column14=var_6,
    )


@pytest.mark.xfail(strict=True)
def test_34():
    var_4 = lambda *args, **kwargs: []
    var_5 = python_code_.database_Database()
    var_6 = python_code_.database_ForeignKey(Name=True)
    assert isinstance(var_6, python_code_.database_ForeignKey)
    var_7 = python_code_.database_Column(
        Name=var_4, Type=var_5, IsPrimaryKey=var_4, database_Column=var_6
    )
    assert isinstance(var_7, python_code_.database_Column)
    var_8 = set()
    var_9 = python_code_.database_ForeignKey(
        Name="?Y", database_ForeignKey11={var_6, "c!x5KyU }|{x"}, ForeignKey=var_5
    )
    assert isinstance(var_9, python_code_.database_ForeignKey)
    var_13 = "[QA"
    var_14 = python_code_.database_Table(
        Name=var_13,
        ColumnTable="database_Column,_database_Table__Table,_database_Column__TableColumn",
        database_Table9=var_8,
        Table=var_9,
    )
    assert isinstance(var_14, python_code_.database_Table)
    python_code_.database_ForeignKey(
        Name=var_4,
        database_ForeignKey8=var_14,
        database_ForeignKey11=var_13,
        DbFK=var_5,
    )
    assert isinstance(var_14.database_Table9, python_code_.database_ForeignKey)


def test_35():
    var_15 = "Database16"
    var_16 = python_code_.database_ForeignKey
    var_17 = python_code_.database_Table(Name=")|O\n&Y<q%", database_Table9=[])
    assert var_17.database_Table9 == []
    var_18 = python_code_.database_Column(
        Name=var_15, Type=var_16, IsPrimaryKey=None, Column=var_17
    )
    assert isinstance(var_18, python_code_.database_Column)
    var_19 = "SeZE1[[4_Hl9BCyc"
    var_20 = False
    var_21 = python_code_.database_Column(
        Name=var_16,
        Type=var_19,
        IsPrimaryKey=var_20,
        Column="Os7..*Y8!<(O16\\",
        database_Column=None,
        database_Column14="'[1`yWk;V",
    )
    assert isinstance(var_21, python_code_.database_Column)
    var_22 = {var_18, var_21}
    python_code_.database_Table(Name=var_15, ColumnTable=var_22)


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = "database_Table9"
    var_1 = "database_ForeignKey11"
    var_2 = python_code_.database_ForeignKey
    var_3 = python_code_.database_Column(
        Name="rP%E6}%nf YLm",
        Type=var_1,
        IsPrimaryKey=True,
        database_Column=var_1,
        database_Column14=var_0,
    )
    assert isinstance(var_3, python_code_.database_Column)
    var_6 = "0;P."
    var_7 = {var_3, var_3}
    var_8 = python_code_.database_ForeignKey(
        Name=var_6, database_ForeignKey=var_2, database_ForeignKey13=var_7, DbFK=var_6
    )
    assert isinstance(var_8, python_code_.database_ForeignKey)
    var_9 = "Float"
    python_code_.database_ForeignKey(
        Name=var_9, database_ForeignKey13=var_2, DbFK=var_0
    )


@pytest.mark.xfail(strict=True)
def test_37():
    var_2 = 70.03
    var_13 = python_code_.database_Table(
        Name="IEPm\x0cFz84$@P|\nX9@0", DbTable=None, database_Table9=None
    )
    assert isinstance(var_13, python_code_.database_Table)
    var_14 = lambda *args, **kwargs: True
    var_15 = python_code_.database_ForeignKey(
        Name=var_14,
        database_ForeignKey=complex(-1900.39011, -4042.12845),
        database_ForeignKey8=var_14,
        database_ForeignKey11=[],
    )
    assert isinstance(var_15, python_code_.database_ForeignKey)
    var_16 = python_code_.database_Column(
        Name=set(),
        Type=var_13,
        IsPrimaryKey=var_2,
        Column=var_14,
        TableColumn=complex(2225.0491632, 1667.0),
        database_Column=var_15,
    )
    assert isinstance(var_16, python_code_.database_Column)
    var_17 = "TableColumn:_database_ForeignKey__ForeignKey:_database_ForeignKey__database_ForeignKey8"
    var_18 = False
    var_19 = python_code_.database_Column(
        Name=var_2, Type=var_17, IsPrimaryKey=var_18, database_Column14=var_13
    )
    var_20 = {var_16, var_19, var_19}
    var_21 = list
    python_code_.database_ForeignKey(
        Name=var_14, database_ForeignKey11=var_20, database_ForeignKey13=var_21
    )
