#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    abstractmethod,
    annotations,
    classes_Card,
    classes_Hand,
    combinations_Brelan,
    combinations_Carre,
    combinations_Combination,
    combinations_Couleur,
    combinations_DoublePaire,
    combinations_Full,
    combinations_Paire,
    combinations_PlusHauteCarte,
    combinations_QuinteFlush,
    combinations_Suite,
    date,
    datetime,
    int,
    time,
    utils_Parser,
)


def test_0():
    var_72 = python_code_.combinations_Combination(
        name="KEhL]~2/NNZS`+f2Y=", value=None, cards0={False, 799.17, -3899}
    )
    assert isinstance(var_72, python_code_.combinations_Combination)


def test_1():
    var_72 = python_code_.combinations_Combination(
        name="MMs{\tJ \nk:AP\tS6", value=None
    )
    assert isinstance(var_72, python_code_.combinations_Combination)


def test_2():
    python_code_.classes_Card(name=3238, value=(-375.99, -276.45))


def test_3():
    var_129 = python_code_.classes_Card(
        name=(),
        value={"classes_Card": "liPlwA*- bhw h*"},
        hand1=[476.48],
        hand3=complex(-939.0, -1235.7),
    )
    assert var_129.hand1 == [476.48]


def test_4():
    python_code_.int()


def test_5():
    python_code_.combinations_QuinteFlush(start=[-1511, True, "classes_Card"])


def test_6():
    python_code_.combinations_Carre(quartet=None)


def test_7():
    python_code_.combinations_Full(paire=(), triplet={True})


def test_8():
    python_code_.combinations_Suite(start=None)


def test_9():
    python_code_.combinations_Brelan(triplet=b"\xc0<<\xe2q2\x8b\xce\x92*\xa28\xf6\x02")


def test_10():
    python_code_.combinations_DoublePaire(strongPaire=None, weakPaire=None)


def test_11():
    python_code_.combinations_Paire(paire=1854)


def test_12():
    var_74 = python_code_.combinations_Combination(
        name="_classes_Card__hand3", value=None
    )
    assert isinstance(var_74, python_code_.combinations_Combination)
    var_85 = python_code_.classes_Card(name=1423.45, value=var_74, hand1=var_74)
    assert isinstance(var_85.hand1, python_code_.combinations_Combination)


def test_13():
    var_101 = python_code_.classes_Card(name="classes_Hand", value=None, hand1=None)
    var_104 = python_code_.combinations_Combination(
        name="classes_Card.combinations_Combination.hand1",
        value=None,
        cards0={2, 136, var_101},
    )
    assert isinstance(var_101.hand1, python_code_.combinations_Combination)
    assert isinstance(var_104, python_code_.combinations_Combination)


def test_14():
    var_72 = list
    var_73 = "_combinations_Combination__cards0_classes_Card__hand3combinations_Combination_classes_Card__hand1"
    var_74 = python_code_.classes_Card(name=var_73, value=var_72, hand1=var_73)
    assert isinstance(var_74, python_code_.classes_Card)
    var_75 = {var_74, True}
    var_76 = python_code_.combinations_Combination(
        name={"hand2cards0hand2": ",$=ctC", "|AaAQzmxC!u": -43},
        value=var_72,
        cards0=var_75,
    )
    assert isinstance(var_74.hand1, python_code_.combinations_Combination)
    assert isinstance(var_76, python_code_.combinations_Combination)


def test_15():
    var_74 = python_code_.combinations_Combination(name="X@}t{xF)oI|bQBT<", value=None)
    assert isinstance(var_74, python_code_.combinations_Combination)
    var_85 = "classes_Hand_classes_Card__hand3_combinations_Combination__cards0hand2"
    var_86 = python_code_.classes_Card(
        name=complex(976.0, -531.0), value={-1223.36, 3403.84, 1869}, hand1=var_74
    )
    assert isinstance(var_86.hand1, python_code_.combinations_Combination)
    var_87 = {var_86}
    python_code_.combinations_Combination(name=var_85, value=var_74, cards0=var_87)


def test_16():
    var_134 = "1etQ}NpQ\to6(nV2"
    var_135 = python_code_.int()
    var_136 = python_code_.combinations_Combination(
        name=var_134, value=var_135, cards0=var_134
    )
    assert isinstance(var_136, python_code_.combinations_Combination)
    var_137 = python_code_.classes_Card(name=None, value=False, hand1=var_136)
    assert isinstance(var_137.hand1, python_code_.combinations_Combination)
    python_code_.combinations_Carre(quartet=var_137)


def test_17():
    var_0 = "7|`qvqQJJ!/"
    var_1 = python_code_.int()
    var_2 = python_code_.combinations_Combination
    var_3 = python_code_.classes_Card(name=[], value=var_0, hand1=var_2)
    assert isinstance(var_3, python_code_.classes_Card)
    var_4 = {var_3, var_3, var_3}
    var_5 = python_code_.combinations_Combination(name=var_0, value=var_1, cards0=var_4)
    assert isinstance(var_3.hand1, python_code_.combinations_Combination)
    assert isinstance(var_5, python_code_.combinations_Combination)
    python_code_.combinations_Suite(start=var_2)
    var_9 = python_code_.combinations_PlusHauteCarte()
    python_code_.combinations_QuinteFlush(start=var_3)
    python_code_.combinations_Carre(quartet=complex(2088.517, -1770.212))
    python_code_.combinations_Paire(
        paire="_classes_Card__hand3.classes_Card.cards0.hand1"
    )
    python_code_.combinations_Full(paire=var_2, triplet=var_2)
    var_16 = python_code_.classes_Hand()
    python_code_.combinations_DoublePaire(strongPaire=674.24, weakPaire=var_3)
    python_code_.classes_Card(
        name=complex(-3038.973, -2275.8), value={318.84, 401, -3306.49}, hand3=var_16
    )
    python_code_.combinations_Brelan(triplet=var_9)
