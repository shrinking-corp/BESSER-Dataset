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
    Lekar,
    Pregled,
    Zdravstveni_karton,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_40 = -2516
    var_41 = python_code_.Pregled(
        BrPregled=var_40,
        DatumP="_Zdravstveni_karton__pregled2 _Pregled__lekar1 _Pregled__lekar1 Pregled",
        zdravstveni_karton3=(3508.56,),
    )
    assert var_41.zdravstveni_karton3 == (3508.56,)
    python_code_.Zdravstveni_karton(BrKart=None)


def test_1():
    python_code_.Zdravstveni_karton(BrKart=-2182)


def test_2():
    var_74 = python_code_.Zdravstveni_karton(
        BrKart={"_Zdravstveni_karton__pregled2": -961, "_": True}, pregled2={}
    )
    assert isinstance(var_74, python_code_.Zdravstveni_karton)


def test_3():
    var_46 = python_code_.Pregled(BrPregled=3, DatumP="LekarPregled", lekar1=set())
    assert isinstance(var_46, python_code_.Pregled)


def test_4():
    var_46 = python_code_.Pregled(
        BrPregled=1099, DatumP="wlT(*\"2\x0b^=`=*|;{O'", zdravstveni_karton3=None
    )
    assert isinstance(var_46, python_code_.Pregled)


def test_5():
    var_40 = -2523
    var_41 = python_code_.Pregled(BrPregled=var_40, DatumP="F^Fg4##oY~2mTBlJ;")
    assert isinstance(var_41, python_code_.Pregled)


def test_6():
    var_40 = -2516
    var_41 = python_code_.Pregled(
        BrPregled=var_40,
        DatumP="_Zdravstveni_karton__pregled2 _Pregled__lekar1 _Pregled__lekar1 Pregled",
        zdravstveni_karton3=(3508.56,),
    )
    assert var_41.zdravstveni_karton3 == (3508.56,)
    python_code_.Zdravstveni_karton(BrKart=None)


def test_7():
    var_46 = python_code_.Pregled(BrPregled=-2159, DatumP="U")
    assert isinstance(var_46, python_code_.Pregled)
    var_86 = python_code_.Lekar(
        Zaposleni_ID="Pregled:Lekar:_Pregled__zdravstveni_karton3",
        ImeZap="k\r_F*",
        PrzZap="pregled0-zdravstveni_karton3-pregled0",
        AdrZap="6~(",
        BrTelZap="b",
        Fakultet=">:%6g.r#+`CQE%4\r/TP",
        DatZavSk="rIFO4$6?HV sI",
        RadStaz=-2421,
        pregled0=var_46,
    )
    assert isinstance(var_86, python_code_.Lekar)
    var_87 = "Pregled"
    var_88 = {var_86}
    python_code_.Pregled(
        BrPregled=complex(-256.228073, 1605.0), DatumP=var_87, lekar1=var_88
    )


def test_8():
    python_code_.Lekar(
        Zaposleni_ID="\x0bp3a-q=2;FC'K/#-aua",
        ImeZap='SM+"Z\x0cC%u;s;',
        PrzZap="Pregled lekar1",
        AdrZap="-od.!8SK",
        BrTelZap="\x0cSc",
        Fakultet="~<U!(Ya",
        DatZavSk="Yk",
        RadStaz=-767,
    )


def test_9():
    var_46 = python_code_.Pregled(
        BrPregled=91,
        DatumP="\x0c/aY8#g:R8Zw:oY$^0",
        lekar1={False, "s\x0bD+B_:Uxrx^x$b~)", "pregled2"},
    )
    assert isinstance(var_46, python_code_.Pregled)
    var_81 = python_code_.Lekar(
        Zaposleni_ID=var_46,
        ImeZap="@tO?L'\\dO[h+$,\n",
        PrzZap=b"}\xa7r:\x05\xbeq\x17\x9fp\xaf\xff)",
        AdrZap="s9@\t2Z;w(h@T;",
        BrTelZap=var_46,
        Fakultet=var_46,
        DatZavSk=var_46,
        RadStaz=(3,),
        pregled0=var_46,
    )
    assert isinstance(var_81, python_code_.Lekar)


@pytest.mark.xfail(strict=True)
def test_10():
    var_46 = python_code_.Pregled(BrPregled=-3424, DatumP="LxEe;.")
    assert isinstance(var_46, python_code_.Pregled)
    var_81 = python_code_.Lekar(
        Zaposleni_ID=var_46,
        ImeZap="@tO?L'\\dO[h+$,\n",
        PrzZap=b"}\xa7r:\x05\xbeq\x17\x9fp\xaf\xff)",
        AdrZap="s9@\t2Z;w(h@T;",
        BrTelZap=var_46,
        Fakultet=var_46,
        DatZavSk=var_46,
        RadStaz=(3,),
        pregled0=var_46,
    )
    assert isinstance(var_81, python_code_.Lekar)
    python_code_.Zdravstveni_karton(BrKart=-1222, pregled2=var_46)
    assert isinstance(var_46.zdravstveni_karton3, python_code_.Zdravstveni_karton)


@pytest.mark.xfail(strict=True)
def test_11():
    var_8 = -2516
    var_9 = python_code_.Pregled(
        BrPregled=var_8,
        DatumP="_Zdravstveni_karton__pregled2 _Pregled__lekar1 _Pregled__lekar1 Pregled",
        zdravstveni_karton3=(3508.56,),
    )
    assert var_9.zdravstveni_karton3 == (3508.56,)
    python_code_.Zdravstveni_karton(BrKart=-150, pregled2=var_9)


def test_12():
    var_101 = "lekar1"
    var_102 = float
    var_46 = python_code_.Lekar(
        Zaposleni_ID=complex(-3605.21379, 492.8),
        ImeZap=var_101,
        PrzZap=complex(727.9117322, 2837.0),
        AdrZap=var_102,
        BrTelZap=var_101,
        Fakultet=var_102,
        DatZavSk=-1951.25,
        RadStaz=var_102,
    )
    var_100 = python_code_.Lekar(
        Zaposleni_ID='pWW/dTF1"',
        ImeZap="CNkc<xTC|pj",
        PrzZap="~Vg%SWnk",
        AdrZap="\\r*-",
        BrTelZap="pregled0.Zdravstveni_karton._Lekar__pregled0._Pregled__zdravstveni_karton3",
        Fakultet="\x0cmGbv!9z}Z#",
        DatZavSk="pregled2",
        RadStaz=59,
        pregled0=var_46,
    )
    var_103 = {var_100, var_46, var_100}
    var_104 = python_code_.Pregled(BrPregled=var_100, DatumP=var_46, lekar1=var_103)
    assert isinstance(var_104, python_code_.Pregled)


def test_13():
    var_46 = {3196, "0_@Yy2.i6kY", -1590}
    var_94 = python_code_.Lekar(
        Zaposleni_ID="_Pregled__zdravstveni_karton3",
        ImeZap=",",
        PrzZap="pregled2:_Lekar__pregled0",
        AdrZap="L\t4Nw]RND.\\LtWr",
        BrTelZap="&j:xu2bC7 ^\x0c!8E",
        Fakultet="6z{1OXT ",
        DatZavSk="_$V;\n>E2lMlM-\\tTzt",
        RadStaz=-280,
        pregled0=var_46,
    )
    assert isinstance(var_94, python_code_.Lekar)


def test_14():
    var_46 = python_code_.Pregled(
        BrPregled=0, DatumP="Pregled", lekar1=set(), zdravstveni_karton3=None
    )
    assert isinstance(var_46, python_code_.Pregled)
    var_69 = ""
    var_70 = python_code_.Lekar(
        Zaposleni_ID="H\x0b-@'/)\rr\t}y>\x0b/",
        ImeZap=var_69,
        PrzZap="pregled2",
        AdrZap=var_69,
        BrTelZap="=",
        Fakultet=var_69,
        DatZavSk="hE",
        RadStaz=-1,
        pregled0=var_46,
    )
    assert isinstance(var_70, python_code_.Lekar)
    var_71 = "lekar1"
    var_72 = python_code_.Pregled
    var_73 = -2129
    var_74 = "pregled0:Pregled"
    var_75 = python_code_.Pregled(BrPregled=var_73, DatumP=var_74, lekar1=var_74)
    assert isinstance(var_75, python_code_.Pregled)
    var_76 = python_code_.Lekar(
        Zaposleni_ID=complex(2099.430146, -3328.5464),
        ImeZap=[False],
        PrzZap=var_71,
        AdrZap=var_71,
        BrTelZap=var_72,
        Fakultet=var_72,
        DatZavSk=None,
        RadStaz=2,
        pregled0=var_75,
    )
    assert isinstance(var_76, python_code_.Lekar)


def test_15():
    var_3 = -1152
    var_4 = python_code_.Zdravstveni_karton(BrKart=var_3, pregled2=-319.99)
    assert isinstance(var_4, python_code_.Zdravstveni_karton)
    var_8 = -1151
    var_9 = python_code_.Pregled(BrPregled=var_8, DatumP={})
    assert isinstance(var_9, python_code_.Pregled)


@pytest.mark.xfail(strict=True)
def test_16():
    var_47 = hash
    var_48 = "lekar1"
    var_50 = "\x0c[pTOX2Ougoy`oW|"
    var_51 = "Zdravstveni_karton-pregled0"
    var_52 = 23
    var_53 = python_code_.Pregled(BrPregled=var_51, DatumP=[], lekar1=())
    assert isinstance(var_53, python_code_.Pregled)
    var_54 = python_code_.Lekar(
        Zaposleni_ID=var_50,
        ImeZap=var_48,
        PrzZap=var_50,
        AdrZap=var_47,
        BrTelZap=var_48,
        Fakultet=var_51,
        DatZavSk=var_50,
        RadStaz=var_52,
        pregled0=var_53,
    )
    assert isinstance(var_54, python_code_.Lekar)
    var_55 = 3
    var_56 = python_code_.Zdravstveni_karton(BrKart=var_55, pregled2=var_53)
    assert isinstance(var_53.zdravstveni_karton3, python_code_.Zdravstveni_karton)
    var_57 = 367
    var_58 = list
    var_59 = "U&B\n1Mvlnp\r'Eq"
    var_60 = python_code_.Lekar(
        Zaposleni_ID=var_50,
        ImeZap=var_51,
        PrzZap=var_50,
        AdrZap=var_51,
        BrTelZap=var_48,
        Fakultet=var_58,
        DatZavSk=var_59,
        RadStaz=None,
    )
    var_61 = {var_60, var_54, var_60, var_60, var_60}
    python_code_.Pregled(
        BrPregled=var_57, DatumP=var_58, lekar1=var_61, zdravstveni_karton3=var_56
    )
