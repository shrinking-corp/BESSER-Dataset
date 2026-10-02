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
    Begin_Game_UseCase,
    Change_Deck__Image_Changes__UseCase,
    Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase,
    MemoryGame_Card,
    MemoryGame_Deck,
    Player_Actor,
    Quit_UseCase,
    Shuffle_Deck__Restart_Game__UseCase,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_4 = python_code_.MemoryGame_Deck(
        id=-2595, image=",n|!X2 &Ks~)y\x0b", cards=None, card0=set()
    )
    assert isinstance(var_4, python_code_.MemoryGame_Deck)


def test_1():
    var_4 = python_code_.MemoryGame_Deck(id=0, image="mYlB8`@", cards=None)
    assert isinstance(var_4, python_code_.MemoryGame_Deck)


def test_2():
    var_4 = python_code_.MemoryGame_Deck(id=2326, image=":';^5\rUs", cards=None)
    assert isinstance(var_4, python_code_.MemoryGame_Deck)
    var_9 = 2
    var_11 = python_code_.MemoryGame_Card(
        position=var_9,
        id=-3717,
        image="In9a}_,ry\t(\nu",
        isShowing=True,
        deck=None,
        deck1=var_4,
    )
    assert isinstance(var_11.deck1, python_code_.MemoryGame_Deck)
    var_12 = "<P4Jm;"
    var_13 = {var_11, var_11}
    python_code_.MemoryGame_Deck(id={}, image=var_12, cards=var_12, card0=var_13)


def test_3():
    python_code_.MemoryGame_Card(
        position=1758, id=2, image="&?Io\\:qqqCMUs", isShowing=True, deck=None
    )


def test_4():
    var_4 = python_code_.MemoryGame_Deck(id=-2030, image="|4p", cards=None)
    assert isinstance(var_4, python_code_.MemoryGame_Deck)
    var_54 = python_code_.MemoryGame_Card(
        position=-211, id=-82, image='\\m5"E', isShowing=True, deck=None, deck1=var_4
    )
    assert isinstance(var_54.deck1, python_code_.MemoryGame_Deck)


def test_5():
    python_code_.Player_Actor()


def test_6():
    var_12 = python_code_.Begin_Game_UseCase()
    var_13 = -594
    var_14 = float
    var_15 = python_code_.MemoryGame_Card(
        position=var_12,
        id=var_13,
        image='}|YI\x0cd\twcgu"-s"rY-',
        isShowing=var_14,
        deck=var_14,
    )
    var_16 = {var_15}
    var_17 = python_code_.MemoryGame_Deck(
        id=var_13, image=var_13, cards=var_15, card0=var_16
    )
    assert isinstance(var_15.deck1, python_code_.MemoryGame_Deck)
    assert isinstance(var_17, python_code_.MemoryGame_Deck)


def test_7():
    var_4 = False
    var_12 = 30
    var_13 = python_code_.MemoryGame_Card(
        position=var_12,
        id=-3717,
        image="In9a}_,ry\t(\nu",
        isShowing=True,
        deck=None,
        deck1=var_4,
    )
    assert isinstance(var_13, python_code_.MemoryGame_Card)
    var_17 = "<P4Jm;5"
    var_18 = {var_13, var_13}
    var_19 = python_code_.MemoryGame_Deck(
        id={}, image=var_17, cards=var_17, card0=var_18
    )
    assert isinstance(var_13.deck1, python_code_.MemoryGame_Deck)
    assert isinstance(var_19, python_code_.MemoryGame_Deck)


def test_8():
    var_53 = 1865
    var_54 = list
    var_55 = python_code_.MemoryGame_Deck(id=var_54, image=var_53, cards=var_54)
    assert isinstance(var_55, python_code_.MemoryGame_Deck)
    var_56 = python_code_.MemoryGame_Card(
        position=set(),
        id=var_53,
        image=None,
        isShowing={"MemoryGame_Card:deck1:deck1": 365, "deck1,deck1": False},
        deck=var_55,
        deck1=2373.43,
    )
    assert var_56.deck1 == pytest.approx(2373.43, abs=0.01, rel=0.01)


def test_9():
    var_50 = python_code_.Quit_UseCase()
    var_51 = True
    var_52 = bytes
    var_53 = "_MemoryGame_Card__deck1,card0,_MemoryGame_Deck__card0,MemoryGame_Card"
    var_54 = python_code_.MemoryGame_Deck(
        id=var_52, image=var_53, cards=var_52, card0=var_53
    )
    assert isinstance(var_54, python_code_.MemoryGame_Deck)
    var_55 = python_code_.MemoryGame_Card(
        position=complex(-610.36495, 3547.9483062),
        id=var_50,
        image=var_50,
        isShowing=var_51,
        deck=var_52,
        deck1=var_54,
    )
    assert isinstance(var_55.deck1, python_code_.MemoryGame_Deck)


def test_10():
    var_0 = python_code_.Shuffle_Deck__Restart_Game__UseCase()
    var_1 = python_code_.Player_Actor()
    var_3 = ">o;`nP\x0bOo\rTP9A2\x0b,"
    var_4 = False
    var_5 = "59"
    var_6 = -644
    var_7 = 1
    var_8 = python_code_.MemoryGame_Card(
        position=var_6,
        id=var_7,
        image=("Hxi&U2E:)!-E9XfNe<",),
        isShowing=var_7,
        deck=var_0,
    )
    var_9 = python_code_.MemoryGame_Deck(id=var_4, image=var_5, cards=var_8, card0={})
    assert isinstance(var_9, python_code_.MemoryGame_Deck)
    var_11 = -1025
    var_12 = True
    var_13 = python_code_.MemoryGame_Card(
        position=var_4,
        id=var_11,
        image=var_3,
        isShowing=var_12,
        deck=var_1,
        deck1=var_9,
    )
    assert isinstance(var_13, python_code_.MemoryGame_Card)
    var_14 = {var_8, var_8, var_13}
    var_15 = python_code_.MemoryGame_Deck(id=0, image=var_3, cards=var_8, card0=var_14)
    assert isinstance(var_8.deck1, python_code_.MemoryGame_Deck)
    assert isinstance(var_15, python_code_.MemoryGame_Deck)
    var_31 = "3"
    python_code_.MemoryGame_Deck(id=var_15, image=var_31, cards=3942.21)
