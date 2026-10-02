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
    Card___Abstract__,
    Deck,
    FortuneTeller,
    TarotCard___Card,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = python_code_.Card___Abstract__(_id=True)
    python_code_.FortuneTeller(_tarotDeck=var_0)
    var_2 = lambda *args, **kwargs: "Card___Abstract__,deck0"
    python_code_.TarotCard___Card(_id=var_0, _fileName=var_2, _fortunes=var_2)
    var_4 = "[r"
    python_code_.Deck(_deck=var_4)


def test_1():
    python_code_.Card___Abstract__(_id=-2047)


def test_2():
    var_8 = 0
    var_9 = "I1sn2/Xs6j^"
    python_code_.Card___Abstract__(_id=var_9)
    python_code_.FortuneTeller(_tarotDeck=var_8)
    var_14 = "_Card___Abstract____deck0"
    python_code_.Deck(_deck=var_14)


def test_3():
    python_code_.FortuneTeller(_tarotDeck=set())


def test_4():
    var_0 = "_FortuneTeller__deck2_Deck__card___Abstract__1_Deck__card___Abstract__1"
    var_1 = python_code_.Deck(_deck=var_0)
    var_2 = "FortuneTeller"
    var_4 = python_code_.FortuneTeller(_tarotDeck=var_1, deck2="(yT)R6")
    assert isinstance(var_4, python_code_.FortuneTeller)
    var_5 = python_code_.FortuneTeller(_tarotDeck=var_1)
    var_6 = 2665
    python_code_.TarotCard___Card(_id=var_6, _fileName=var_5, _fortunes=var_0)
    python_code_.Card___Abstract__(_id=var_2)


def test_5():
    python_code_.Deck(_deck="_Card___Abstract____deck0")


def test_6():
    var_23 = python_code_.Deck(_deck=(), card___Abstract__1=b"\xc1\xa4\xbe/\x9aq#`-L")
    assert isinstance(var_23, python_code_.Deck)


def test_7():
    python_code_.TarotCard___Card(
        _id=-3084, _fileName="qzQV[\n6:HrB|0(J.RF.", _fortunes="5|I$Yp4bQB\\Z+F\x0c"
    )


def test_8():
    python_code_.Card___Abstract__(_id=-1688, deck0=None)


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.Deck(
        _deck=set(),
        fortuneTeller3=b"\xab:L\xf5[\x8a\x81:\xc6\xb0\xe4_v\xca\xa1\xd3s\xfc\xfa",
    )
    assert (
        var_0.fortuneTeller3
        == b"\xab:L\xf5[\x8a\x81:\xc6\xb0\xe4_v\xca\xa1\xd3s\xfc\xfa"
    )
    var_1 = "1Ao"
    var_2 = python_code_.TarotCard___Card(
        _id="sgnT\x0cCT*Drsi2]I", _fileName=var_0, _fortunes=var_1
    )
    var_3 = python_code_.Deck(_deck=var_2, card___Abstract__1=var_1)
    assert isinstance(var_3, python_code_.Deck)
    var_5 = list
    python_code_.FortuneTeller(_tarotDeck=var_0)
    var_17 = -899
    var_19 = python_code_.Card___Abstract__(_id=var_17, deck0=False)
    assert isinstance(var_19, python_code_.Card___Abstract__)
    python_code_.Deck(_deck=var_5, card___Abstract__1=var_19)
    assert isinstance(var_19.deck0, python_code_.Deck)


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = bool
    python_code_.TarotCard___Card(_id=True, _fileName=var_0, _fortunes=var_0)
    var_2 = "\r;C%vVTB5\td"
    var_3 = python_code_.Deck(_deck=var_2, fortuneTeller3=var_0)
    assert isinstance(var_3, python_code_.Deck)
    python_code_.FortuneTeller(_tarotDeck=var_3, deck2=var_3)
    assert isinstance(var_3.fortuneTeller3, python_code_.FortuneTeller)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = 561
    var_1 = python_code_.Deck(
        _deck=False, card___Abstract__1=complex(-3026.141, 220.371)
    )
    assert isinstance(var_1, python_code_.Deck)
    python_code_.Card___Abstract__(_id=var_0, deck0=var_1)


def test_12():
    python_code_.Card___Abstract__(_id=2030)
    var_6 = python_code_.Card___Abstract__
    var_8 = 0
    python_code_.FortuneTeller(_tarotDeck=var_8)
    var_14 = "_Card___Abstract____deck0"
    var_15 = python_code_.Deck(_deck=var_14)
    python_code_.FortuneTeller(_tarotDeck=var_15, deck2=var_6)
