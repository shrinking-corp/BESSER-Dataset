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
    Comparable_BlackjackHand__Interface,
    Enum,
    Iterable_Card__Interface,
    abstractmethod,
    annotations,
    blackjack_BlackjackGame,
    blackjack_BlackjackHand,
    blackjack_Card,
    blackjack_CardSet,
    blackjack_DealerBot,
    blackjack_Deck,
    blackjack_DeckShuffledListener_Interface,
    blackjack_ExampleInstrumentedTest,
    blackjack_ExampleUnitTest,
    blackjack_GameState,
    blackjack_MainActivity,
    blackjack_Suit,
    blackjack_Value,
    date,
    datetime,
    genmymodelreverse_C1,
    genmymodelreverse_C11,
    genmymodelreverse_C12,
    genmymodelreverse_android_support_v7_app_AppCompatActivity,
    genmymodelreverse_java_lang_Comparable_Interface,
    genmymodelreverse_java_lang_Iterable_Interface,
    genmymodelreverse_java_util_Iterator_Interface,
    time,
)


def test_0():
    python_code_.blackjack_Card(
        suit=None, value=None, MAX_VALUE_OF_ACE=-71, BLACKJACK_VALUE=1004, cardset6=None
    )


def test_1():
    python_code_.blackjack_BlackjackGame(
        MAX_HITS=-479,
        MAX_CARDS_PULLED=-2169,
        gstate=None,
        hitButton="blackjackgame12",
        stayButton="cards7",
        gameResultTextView="ma'",
        playersHandTextView="r|a=",
        dealersHandTextView="Eid^jDuE;*$:",
        playerHandValueTextView="5GND\\(6yT%|}h/iP]o",
        dealersHandValueTextView="hAz68\t/",
        theDeck11=None,
        dealerBot13=None,
    )


def test_2():
    var_12 = "ZC"
    var_13 = python_code_.blackjack_BlackjackGame(
        MAX_HITS=493,
        MAX_CARDS_PULLED=0,
        gstate=var_12,
        hitButton=var_12,
        stayButton="\nC]{o/)W;k.KDs",
        gameResultTextView=var_12,
        playersHandTextView=var_12,
        dealersHandTextView=var_12,
        playerHandValueTextView="I\x0bbhy5N6a.Vn0\x0b^",
        dealersHandValueTextView=var_12,
        playerHand3=None,
        theDeck11=var_12,
        dealerBot13=var_12,
    )
    assert isinstance(var_13, python_code_.blackjack_BlackjackGame)


def test_3():
    python_code_.genmymodelreverse_java_util_Iterator_Interface()


def test_4():
    var_32 = python_code_.blackjack_Card(
        suit=[2516.87, True, -1674.26],
        value={699, "hHN"},
        MAX_VALUE_OF_ACE=1253,
        BLACKJACK_VALUE=-1259.01,
        cardset6=complex(2593.4109467, 1244.585372),
    )
    assert isinstance(var_32, python_code_.blackjack_Card)


def test_5():
    var_12 = python_code_.blackjack_BlackjackHand()
    python_code_.blackjack_BlackjackGame(
        MAX_HITS=3999,
        MAX_CARDS_PULLED=-4064,
        gstate=None,
        hitButton="wx>XUo\\1@l#<(;b",
        stayButton='"us>+-Oj#X3',
        gameResultTextView="_blackjack_BlackjackGame__theDeck11-_blackjack_BlackjackGame__dealerBot13-blackjack_CardSet-blackjack_Deck",
        playersHandTextView="blackjackgame12 blackjack_BlackjackHand blackjackgame2",
        dealersHandTextView="blackjack_DeckShuffledListener_Interface",
        playerHandValueTextView="|M`",
        dealersHandValueTextView="'*bZkZ\x0bKAqv[uo|}\r\x0b",
        deckShuffledListener9=var_12,
        dealerBot13=var_12,
    )


def test_6():
    var_10 = "EZCN"
    var_12 = python_code_.blackjack_BlackjackGame(
        MAX_HITS=2,
        MAX_CARDS_PULLED=1081,
        gstate=var_10,
        hitButton=var_10,
        stayButton=var_10,
        gameResultTextView="IqY\r",
        playersHandTextView="_blackjack_Card__cardset6-_blackjack_BlackjackGame__dealerBot13",
        dealersHandTextView=var_10,
        playerHandValueTextView="{kN~<;tfR8M/j(B;C%",
        dealersHandValueTextView="&r,\n|zw\tP?8kH-%SBV ",
        playerHand3=var_10,
    )
    assert isinstance(var_12, python_code_.blackjack_BlackjackGame)


def test_7():
    var_13 = python_code_.blackjack_BlackjackGame(
        MAX_HITS=None,
        MAX_CARDS_PULLED=True,
        gstate=None,
        hitButton=2,
        stayButton=[],
        gameResultTextView=[],
        playersHandTextView=True,
        dealersHandTextView=True,
        playerHandValueTextView=b"\x97\xc1\xa1]\t",
        dealersHandValueTextView={"cards7", -225, False},
        theDeck11=False,
    )
    assert isinstance(var_13, python_code_.blackjack_BlackjackGame)
