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
    BaseRole,
    ChatMessage,
    Enum,
    Enumeration,
    Enumeration2,
    Game,
    Guardian,
    NightAction,
    Player,
    Role,
    Room,
    Seer,
    State,
    SysMessage,
    Villager,
    Wolf,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_28 = python_code_.Player(
        role="Kq{&7@]O_/+lIvxYlc",
        isAlive=False,
        votes=1,
        vote_for=None,
        night_target=None,
    )
    assert isinstance(var_28, python_code_.Player)
    var_98 = 1408
    var_99 = python_code_.Game(turn_state=var_98, player0=var_28)
    assert isinstance(var_99, python_code_.Game)
    var_100 = {var_99}
    python_code_.Player(
        role=var_28,
        isAlive=False,
        votes=var_98,
        vote_for=var_28,
        night_target=var_28,
        game1=var_100,
    )


def test_1():
    python_code_.Game(turn_state=None, player0=None)


def test_2():
    var_30 = python_code_.Game(turn_state=None, player0=-1386)
    assert isinstance(var_30, python_code_.Game)


def test_3():
    var_28 = python_code_.Player(
        role="N~/XEg",
        isAlive=True,
        votes=0,
        vote_for=None,
        night_target=None,
        game1=set(),
    )
    assert isinstance(var_28, python_code_.Player)


def test_4():
    var_28 = python_code_.Player(
        role="JeRM\x0c{kKrZu\r3Imp0p",
        isAlive=False,
        votes=-3368,
        vote_for=None,
        night_target=None,
    )
    assert isinstance(var_28, python_code_.Player)


def test_5():
    var_7 = "D:\nqw|{ZFp|-z2,"
    var_9 = False
    var_18 = python_code_.Game(turn_state=None)
    var_19 = {var_18, var_18, var_18, var_18, var_9}
    var_20 = python_code_.Player(
        role=var_7,
        isAlive=var_9,
        votes="IH,X",
        vote_for=var_9,
        night_target=[],
        game1=var_19,
    )
    assert isinstance(var_20, python_code_.Player)


def test_6():
    var_28 = python_code_.Player(
        role="(Px",
        isAlive=True,
        votes=-1,
        vote_for=None,
        night_target=None,
        game1=set(),
    )
    assert isinstance(var_28, python_code_.Player)
    var_35 = python_code_.Game(turn_state=var_28, player0=var_28)
    assert isinstance(var_35, python_code_.Game)


def test_7():
    python_code_.BaseRole(role=None, appear_as=None, night_action=None, wins_with=None)


def test_8():
    var_28 = python_code_.Player(
        role="player0", isAlive=False, votes=1193, vote_for=None, night_target=None
    )
    assert isinstance(var_28, python_code_.Player)
    var_30 = 3
    var_31 = lambda *args, **kwargs: True
    var_32 = python_code_.Game(turn_state=None, player0=var_31)
    var_33 = {var_32, var_32, var_32, var_32}
    var_34 = python_code_.Player(
        role=var_28,
        isAlive={True, True},
        votes=var_30,
        vote_for=var_30,
        night_target={False, True},
        game1=var_33,
    )
    assert isinstance(var_34, python_code_.Player)


def test_9():
    var_6 = True
    python_code_.BaseRole(
        role=var_6, appear_as=var_6, night_action=var_6, wins_with=var_6
    )
    var_18 = python_code_.Player
    python_code_.Game(turn_state=var_18)
    var_21 = python_code_.Game(turn_state={}, player0=var_18)
    assert isinstance(var_21, python_code_.Game)


def test_10():
    var_74 = -2159
    var_76 = False
    var_77 = "pJoFN;"
    var_78 = bytes
    var_79 = False
    var_80 = 2840
    var_81 = python_code_.Player(
        role=-2660.13,
        isAlive=var_79,
        votes=var_80,
        vote_for=var_76,
        night_target=var_78,
    )
    assert isinstance(var_81, python_code_.Player)
    var_82 = python_code_.Player(
        role=var_78,
        isAlive=var_76,
        votes=var_74,
        vote_for=var_81,
        night_target=var_78,
        game1=var_77,
    )
    assert isinstance(var_82, python_code_.Player)
    var_83 = python_code_.Game(turn_state=None, player0=var_82)
    assert isinstance(var_83, python_code_.Game)
    var_84 = {var_83, var_83}
    var_85 = python_code_.Player(
        role=var_77,
        isAlive=var_78,
        votes=b"\xfd{\xa14",
        vote_for=var_76,
        night_target=var_81,
        game1=var_84,
    )
    assert isinstance(var_85, python_code_.Player)
