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
    RDBMS_Column,
    RDBMS_FKey,
    RDBMS_PKey,
    RDBMS_Scheme,
    RDBMS_Table,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.RDBMS_Column(name="SF]4,vZ)m}Vc4y,;E\t(")


def test_1():
    var_48 = python_code_.RDBMS_Column(name=None, RDBMS_Column=False)
    assert isinstance(var_48, python_code_.RDBMS_Column)


@pytest.mark.xfail(strict=True)
def test_2():
    var_33 = 'oT<.",'
    var_46 = python_code_.RDBMS_Table(
        name=var_33, table={True, var_33}, RDBMS_Table=None
    )
    assert isinstance(var_46, python_code_.RDBMS_Table)
    python_code_.RDBMS_Column(name=var_33, columns=var_46)
    assert isinstance(var_46.RDBMS_ecoreTable7, python_code_.RDBMS_Column)


def test_3():
    var_47 = python_code_.RDBMS_Column(
        name=[],
        columns={
            'JJuYjrhp*+MPfy+Qg]"': "I,wHa)j-A84\x0bwK",
            "v>;y73qg6~K": "tables,_RDBMS_Scheme__RDBMS_ecoreScheme,RDBMS_ecoreTable7,_RDBMS_Table__RDBMS_Table",
            "z\\+s\t/I%g@K/#\tt": 2212.07,
        },
    )
    assert isinstance(var_47, python_code_.RDBMS_Column)


def test_4():
    var_51 = python_code_.RDBMS_Column(name=False, RDBMS_Column16=-1527)
    assert isinstance(var_51, python_code_.RDBMS_Column)


def test_5():
    var_33 = 'oT<S",'
    var_44 = python_code_.RDBMS_Column(
        name=var_33, RDBMS_ecoreColumn=var_33, columns=var_33, RDBMS_Column=None
    )
    assert isinstance(var_44, python_code_.RDBMS_Column)


def test_6():
    var_43 = python_code_.RDBMS_Table(
        name="_}jL&&4sA){}G`Zl", table={-2292.51}, tables=None
    )
    assert isinstance(var_43, python_code_.RDBMS_Table)


def test_7():
    var_43 = python_code_.RDBMS_Table(
        name="G", RDBMS_ecoreTable=None, tables=None, RDBMS_ecoreTable7=None
    )
    assert isinstance(var_43, python_code_.RDBMS_Table)


def test_8():
    var_47 = python_code_.RDBMS_PKey()
    var_48 = python_code_.RDBMS_Table(
        name=b"\xf6\xd3eRX\xd2wh\xf3\x8eAY\xf7",
        tables={"&3:\nK~Fz:h\r<!": -1671.79},
        RDBMS_Table=var_47,
    )
    assert var_48.tables == {"&3:\nK~Fz:h\r<!": -1671.79}


def test_9():
    var_16 = "4j`9\tBj"
    var_17 = python_code_.RDBMS_Table(name=var_16, RDBMS_ecoreTable=var_16)
    assert isinstance(var_17, python_code_.RDBMS_Table)


def test_10():
    var_45 = python_code_.RDBMS_Scheme(
        name="RDBMS_ecoreScheme.RDBMS_Table.RDBMS_ecoreFKey.RDBMS_PKey",
        RDBMS_ecoreScheme=None,
    )
    assert isinstance(var_45, python_code_.RDBMS_Scheme)
    var_47 = python_code_.RDBMS_Table(
        name="4/FX%iweD4vE'k*\t ",
        RDBMS_ecoreTable=var_45,
        table={var_45, "", var_45},
        RDBMS_ecoreTable7=var_45,
    )
    assert isinstance(var_47.RDBMS_ecoreTable7, python_code_.RDBMS_Scheme)


def test_11():
    var_50 = python_code_.RDBMS_Scheme(name={False, "4-CE7"})
    assert isinstance(var_50, python_code_.RDBMS_Scheme)


def test_12():
    var_50 = python_code_.RDBMS_Scheme(
        name="_RDBMS_Column__RDBMS_Column",
        scheme={-2553.89, True, True},
        scheme2=set(),
        RDBMS_ecoreScheme13=None,
    )
    assert isinstance(var_50, python_code_.RDBMS_Scheme)


def test_13():
    var_33 = 'oT<S",'
    var_45 = python_code_.RDBMS_Scheme(
        name=var_33, scheme=set(), scheme2={var_33}, RDBMS_ecoreScheme13=var_33
    )
    assert isinstance(var_45, python_code_.RDBMS_Scheme)


def test_14():
    var_27 = lambda *args, **kwargs: []
    var_28 = python_code_.RDBMS_Scheme(
        name="7UXSu&4\\|\\+L(q3%o5K", scheme={var_27}, RDBMS_ecoreScheme=var_27
    )
    assert isinstance(var_28, python_code_.RDBMS_Scheme)


def test_15():
    var_0 = python_code_.RDBMS_FKey()
    var_1 = "g%*"
    var_13 = python_code_.RDBMS_Column(name=var_1, RDBMS_Column16=var_0)
    var_17 = python_code_.RDBMS_Scheme(
        name=var_1, RDBMS_ecoreScheme13=b"\xf8_xD\x82,t\xe7-OV\xbeP\x14\x9c\xce"
    )
    assert isinstance(var_17, python_code_.RDBMS_Scheme)
    var_17.remTable(RDBMS_n=var_13)
    var_19 = var_13.setTable(RDBMS_n="_RDBMS_Table__tables RDBMS_FKey keys")
    var_20 = python_code_.RDBMS_Table(name=set(), RDBMS_ecoreTable=var_17, table=var_19)
    assert isinstance(var_20, python_code_.RDBMS_Table)
    var_20.remColumn(RDBMS_n=[])


def test_16():
    var_0 = python_code_.RDBMS_FKey()
    var_1 = "g%8"
    var_13 = python_code_.RDBMS_Column(name=var_1, RDBMS_Column16=var_0)
    var_13.setName(RDBMS_n=895.15)


def test_17():
    python_code_.RDBMS_FKey()


def test_18():
    var_43 = python_code_.RDBMS_Table(name="E{:Eu]")
    assert isinstance(var_43, python_code_.RDBMS_Table)
    var_46 = python_code_.RDBMS_Column(name=var_43, RDBMS_ecoreColumn=var_43)
    assert isinstance(var_46, python_code_.RDBMS_Column)


def test_19():
    var_51 = python_code_.RDBMS_Column(
        name="\\G^7#nKu$i]", RDBMS_Column=None, RDBMS_Column16=None
    )
    var_56 = ""
    var_57 = abs
    var_58 = python_code_.RDBMS_Column(name=var_56, columns=var_57, RDBMS_Column=set())
    assert isinstance(var_58, python_code_.RDBMS_Column)
    var_59 = python_code_.RDBMS_Table(
        name=var_56, table={812, var_51}, RDBMS_ecoreTable7=None
    )
    assert isinstance(var_59, python_code_.RDBMS_Table)
    var_59.setName(RDBMS_n=-4308)


@pytest.mark.xfail(strict=True)
def test_20():
    var_48 = lambda *args, **kwargs: False
    var_49 = python_code_.RDBMS_Table(name=var_48)
    assert isinstance(var_49, python_code_.RDBMS_Table)
    var_50 = var_49.remColumn(RDBMS_n=var_48)
    var_51 = python_code_.RDBMS_Scheme(name={}, scheme2=var_50)
    assert isinstance(var_51, python_code_.RDBMS_Scheme)
    python_code_.RDBMS_Column(
        name={"DEv(Y{nT\\7\x0cJAS)14", True, False}, columns=var_49
    )
    assert isinstance(var_49.RDBMS_ecoreTable7, python_code_.RDBMS_Column)


def test_21():
    var_0 = lambda *args, **kwargs: -1
    var_1 = python_code_.RDBMS_Table(
        name="{;K[g;>sub2\x0co4", table=set(), tables=None, RDBMS_ecoreTable7=var_0
    )
    assert isinstance(var_1, python_code_.RDBMS_Table)
    var_40 = "@T2XMh&"
    var_41 = python_code_.RDBMS_Column(name=var_40, columns=var_0)
    var_41.setName(RDBMS_n=895.15)
    var_1.addColumn(RDBMS_n=set())


def test_22():
    var_45 = python_code_.RDBMS_Scheme(
        name="RDBMS_FKey11-_RDBMS_Table__tables-_RDBMS_Table__RDBMS_ecoreTable",
        scheme={-1753, 263},
    )
    assert isinstance(var_45, python_code_.RDBMS_Scheme)
    var_47 = python_code_.RDBMS_Table(name="4GgoYU", RDBMS_ecoreTable=var_45)
    assert isinstance(var_47, python_code_.RDBMS_Table)


def test_23():
    var_0 = lambda *args, **kwargs: -1
    var_1 = python_code_.RDBMS_Table(name=var_0, RDBMS_ecoreTable7=[3804.95])
    assert var_1.RDBMS_ecoreTable7 == [3804.95]
    var_2 = python_code_.RDBMS_Column(name=var_0, RDBMS_ecoreColumn=var_1)
    assert isinstance(var_2, python_code_.RDBMS_Column)
    var_3 = var_2.setName(RDBMS_n=var_1)
    var_4 = python_code_.RDBMS_Scheme(name=var_0, scheme=var_3)
    assert isinstance(var_4, python_code_.RDBMS_Scheme)
    var_4.addTable(RDBMS_n=var_1)
    var_6 = "RDBMS_Column:RDBMS_Scheme"
    python_code_.RDBMS_Column(name=var_6, RDBMS_Column=var_2)
    var_1.setName(RDBMS_n=var_0)
    var_4.remTable(RDBMS_n=var_4)


def test_24():
    var_13 = "_RDBMS_Scheme__RDBMS_ecoreScheme"
    var_14 = python_code_.RDBMS_Scheme(name=var_13)
    assert isinstance(var_14, python_code_.RDBMS_Scheme)
    var_14.setName(RDBMS_n=())


@pytest.mark.xfail(strict=True)
def test_25():
    var_43 = python_code_.RDBMS_Table(name="\n\tY-\nlY/k{j?u_Z", RDBMS_Table=None)
    assert isinstance(var_43, python_code_.RDBMS_Table)
    python_code_.RDBMS_Column(
        name=")lG9;n7|*ybv", RDBMS_ecoreColumn=var_43, columns=var_43
    )
    assert isinstance(var_43.RDBMS_ecoreTable7, python_code_.RDBMS_Column)


@pytest.mark.xfail(strict=True)
def test_26():
    var_21 = "g4d2"
    var_23 = python_code_.RDBMS_Scheme(name=var_21, RDBMS_ecoreScheme=[])
    assert isinstance(var_23, python_code_.RDBMS_Scheme)
    python_code_.RDBMS_Table(name=var_21, tables=var_23)


@pytest.mark.xfail(strict=True)
def test_27():
    var_25 = python_code_.RDBMS_PKey()
    var_26 = python_code_.RDBMS_Table(
        name=b"\xf6\xd3eRX\xd2wh\xf3\x8eAY\xf7",
        tables={"&3:\nK~Fz:h\r<!": -1671.79},
        RDBMS_Table=var_25,
    )
    assert isinstance(var_26, python_code_.RDBMS_Table)
    var_27 = "\rz+H 1.\r[\nZ9%I%t/"
    python_code_.RDBMS_Scheme(name=var_27, RDBMS_ecoreScheme=var_26)
    assert isinstance(var_26.tables, python_code_.RDBMS_Scheme)


@pytest.mark.xfail(strict=True)
def test_28():
    var_1 = "_RDBMS_Table__tables:_RDBMS_Scheme__RDBMS_ecoreScheme"
    var_2 = "92HCb4C4"
    var_3 = python_code_.RDBMS_Scheme(name=var_2, scheme=var_1)
    assert isinstance(var_3, python_code_.RDBMS_Scheme)
    var_4 = 'n"!L{'
    var_5 = bytes
    var_6 = python_code_.RDBMS_Column(name=var_4, columns=var_5)
    assert isinstance(var_6, python_code_.RDBMS_Column)
    python_code_.RDBMS_Table(
        name=var_1, RDBMS_ecoreTable=var_3, table={}, RDBMS_ecoreTable7=var_6
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_50 = "RDBMS_ecoreTable7"
    var_51 = dict
    var_52 = python_code_.RDBMS_Table(name=var_50, RDBMS_ecoreTable7=var_51)
    assert isinstance(var_52, python_code_.RDBMS_Table)
    var_53 = python_code_.RDBMS_FKey()
    python_code_.RDBMS_Column(name=1124.47, columns=var_52, RDBMS_Column=var_53)
    assert isinstance(var_52.RDBMS_ecoreTable7, python_code_.RDBMS_Column)


def test_30():
    var_50 = python_code_.RDBMS_Scheme(name="n", RDBMS_ecoreScheme13=None)
    assert isinstance(var_50, python_code_.RDBMS_Scheme)
    var_51 = int
    var_52 = python_code_.RDBMS_Table(
        name=var_50,
        table="RDBMS_FKey:_RDBMS_Scheme__scheme:RDBMS_FKey11:_RDBMS_Table__tables",
        RDBMS_Table=var_51,
    )
    assert isinstance(var_52, python_code_.RDBMS_Table)
    var_53 = python_code_.RDBMS_Column(
        name=b"\xd3Ku`\x05\xc4\xe9\xa8\xf95", RDBMS_ecoreColumn=var_52
    )
    assert isinstance(var_53, python_code_.RDBMS_Column)
    var_50.setName(RDBMS_n=[])


@pytest.mark.xfail(strict=True)
def test_31():
    python_code_.RDBMS_Column(name="$A>\x0cJ\x0cqOfQOFi#XD@TT", RDBMS_Column=None)
    var_50 = "RDBMS_FKey"
    python_code_.RDBMS_Scheme(
        name=var_50,
        RDBMS_ecoreScheme={3628.35, 64.36, -394.09},
        RDBMS_ecoreScheme13={
            "RE%{/Lk=TFb\x0bpB@%D$": True,
            "2kQb3tW[]?f?(]]\t+]A": -663,
            "_RDBMS_Scheme__scheme2": "OAjU(xvE",
        },
    )
