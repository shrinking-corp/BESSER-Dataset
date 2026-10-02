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
    DefencePositionKind,
    Enum,
    ForwardPositionKind,
    HeightKind,
    HockeyleagueObject,
    Player,
    ShotKind,
    WeightKind,
    abstractmethod,
    date,
    datetime,
    hockeyleague_Arena,
    hockeyleague_Defence,
    hockeyleague_Forward,
    hockeyleague_Goalie,
    hockeyleague_GoalieStats,
    hockeyleague_HockeyleagueObject,
    hockeyleague_League,
    hockeyleague_Player,
    hockeyleague_PlayerStats,
    hockeyleague_Team,
    time,
)


def test_0():
    var_5 = -638
    python_code_.hockeyleague_GoalieStats(
        ties=-2034,
        emptyNetGoals=var_5,
        shutouts=var_5,
        goalsAgainst=-1484,
        saves=var_5,
        penaltyMinutes=var_5,
        goals=var_5,
        assists=var_5,
        points=var_5,
        year="_hockeyleague_PlayerStats__hockeyleague_PlayerStats2",
        gamesPlayedIn=var_5,
        minutesPlayedIn=var_5,
        goalsAgainstAverage=-505.03,
        wins=var_5,
        losses=-1692,
        hockeyleague_GoalieStats5=None,
    )


def test_1():
    var_5 = -638
    var_9 = python_code_.hockeyleague_GoalieStats(
        ties=var_5,
        emptyNetGoals=var_5,
        shutouts=var_5,
        goalsAgainst=2056,
        saves=-1697,
        penaltyMinutes=4385,
        goals=-209,
        assists=-231,
        points=var_5,
        year="left",
        gamesPlayedIn=var_5,
        minutesPlayedIn=-1,
        goalsAgainstAverage=1101.65,
        wins=var_5,
        losses=-1506,
        hockeyleague_GoalieStats5=var_5,
    )
    assert isinstance(var_9, python_code_.hockeyleague_GoalieStats)


def test_2():
    var_5 = -641
    var_13 = python_code_.hockeyleague_GoalieStats(
        ties=var_5,
        emptyNetGoals=-1865,
        shutouts=var_5,
        goalsAgainst=var_5,
        saves=var_5,
        penaltyMinutes=var_5,
        goals=var_5,
        assists=var_5,
        points=var_5,
        year="~ji()xZ<Y_;6A3",
        gamesPlayedIn=var_5,
        minutesPlayedIn=-895,
        goalsAgainstAverage=4193.32,
        wins=2721,
        losses=-933,
        hockeyleague_GoalieStats=var_5,
        hockeyleague_GoalieStats5=var_5,
    )
    assert isinstance(var_13, python_code_.hockeyleague_GoalieStats)


def test_3():
    var_4 = 38
    python_code_.hockeyleague_PlayerStats(
        year="7v[v\r3pVjdIG\x0c?",
        gamesPlayedIn=2982,
        goals=var_4,
        assists=var_4,
        points=-1128,
        plusMinus=2,
        penaltyMinutes=3066,
        powerPlayGoals=730,
        shortHandedGoals=207,
        gameWinningGoals=var_4,
        shots=var_4,
        shotPercentage=-346.52,
        hockeyleague_PlayerStats9=None,
    )


def test_4():
    var_7 = 317
    var_12 = python_code_.hockeyleague_PlayerStats(
        year="6>2",
        gamesPlayedIn=var_7,
        goals=var_7,
        assists=-1278,
        points=var_7,
        plusMinus=var_7,
        penaltyMinutes=-174,
        powerPlayGoals=var_7,
        shortHandedGoals=3,
        gameWinningGoals=var_7,
        shots=1,
        shotPercentage=206.04,
        hockeyleague_PlayerStats9=None,
        hockeyleague_PlayerStats2=var_7,
    )
    assert isinstance(var_12, python_code_.hockeyleague_PlayerStats)


def test_5():
    var_7 = 318
    var_12 = python_code_.hockeyleague_PlayerStats(
        year="_hockeyleague_PlayerStats__hockeyleague_PlayerStats _hockeyleague_PlayerStats__hockeyleague_PlayerStats2 hockeyleague_PlayerStats2",
        gamesPlayedIn=4888,
        goals=662,
        assists=var_7,
        points=-1541,
        plusMinus=var_7,
        penaltyMinutes=var_7,
        powerPlayGoals=1144,
        shortHandedGoals=-2861,
        gameWinningGoals=var_7,
        shots=var_7,
        shotPercentage=417.38,
        hockeyleague_PlayerStats9=var_7,
        hockeyleague_PlayerStats2=var_7,
    )
    assert isinstance(var_12, python_code_.hockeyleague_PlayerStats)


def test_6():
    var_4 = 38
    var_6 = python_code_.hockeyleague_PlayerStats(
        year="v<Nh~\\)$KS",
        gamesPlayedIn=var_4,
        goals=2,
        assists=-1,
        points=-2587,
        plusMinus=var_4,
        penaltyMinutes=var_4,
        powerPlayGoals=var_4,
        shortHandedGoals=687,
        gameWinningGoals=2,
        shots=405,
        shotPercentage=-282.58,
        hockeyleague_PlayerStats=var_4,
    )
    assert isinstance(var_6, python_code_.hockeyleague_PlayerStats)


def test_7():
    var_10 = python_code_.hockeyleague_Forward(
        position="I_dd%QAs#?]MJk", hockeyleague_Forward=set()
    )
    assert isinstance(var_10, python_code_.hockeyleague_Forward)


def test_8():
    var_10 = python_code_.hockeyleague_Forward(
        position="left_defence.left_wing._hockeyleague_PlayerStats__hockeyleague_PlayerStats2"
    )
    assert isinstance(var_10, python_code_.hockeyleague_Forward)


def test_9():
    var_3 = python_code_.hockeyleague_Defence(
        position=" xexls8rgR", hockeyleague_Defence=set(), hockeyleague_Defence16=None
    )
    assert isinstance(var_3, python_code_.hockeyleague_Defence)


def test_10():
    var_3 = python_code_.hockeyleague_Defence(position="right_wing")
    assert isinstance(var_3, python_code_.hockeyleague_Defence)


def test_11():
    var_15 = python_code_.hockeyleague_HockeyleagueObject
    var_7 = python_code_.hockeyleague_Defence(
        position=var_15, hockeyleague_Defence16=-1633.21
    )
    assert isinstance(var_7, python_code_.hockeyleague_Defence)


def test_12():
    var_1 = python_code_.hockeyleague_League(
        headoffice="|+", hockeyleague_League={-2155, 571}
    )
    assert isinstance(var_1, python_code_.hockeyleague_League)


def test_13():
    var_1 = python_code_.hockeyleague_League(
        headoffice="right_wing.left_wing.hockeyleague_Forward"
    )
    assert isinstance(var_1, python_code_.hockeyleague_League)


def test_14():
    var_12 = python_code_.hockeyleague_Arena(
        address="hockeyleague_Team", capacity=-2111, hockeyleague_Arena=None
    )
    assert isinstance(var_12, python_code_.hockeyleague_Arena)


def test_15():
    var_16 = python_code_.hockeyleague_Arena(
        address=b"cH\x07G\xccf8=}\x07\xaaW\xec[\xa4\xeb",
        capacity=b"~\x8a\xf3\xddR",
        hockeyleague_Arena=(),
    )
    assert isinstance(var_16, python_code_.hockeyleague_Arena)


def test_16():
    var_4 = python_code_.hockeyleague_HockeyleagueObject(name="#")
    assert isinstance(var_4, python_code_.hockeyleague_HockeyleagueObject)


def test_17():
    var_8 = "Y7\r,Q-I5D\n"
    var_13 = python_code_.WeightKind
    var_14 = -2799
    var_15 = -906
    var_16 = python_code_.hockeyleague_PlayerStats(
        year=var_8,
        gamesPlayedIn=var_14,
        goals=var_14,
        assists=var_15,
        points=2878,
        plusMinus=var_15,
        penaltyMinutes=var_14,
        powerPlayGoals=2,
        shortHandedGoals=var_15,
        gameWinningGoals=1373,
        shots=1393,
        shotPercentage=51.52,
        hockeyleague_PlayerStats9=var_13,
        hockeyleague_PlayerStats2=var_13,
    )
    var_17 = {var_16, var_16}
    var_18 = python_code_.hockeyleague_Forward(
        position=var_13, hockeyleague_Forward=var_17
    )
    assert isinstance(var_18, python_code_.hockeyleague_Forward)


def test_18():
    var_7 = -5139
    var_11 = 471.89
    var_12 = python_code_.hockeyleague_PlayerStats(
        year="TCh+fGI8d\rX",
        gamesPlayedIn=var_7,
        goals=-1,
        assists=var_7,
        points=-572,
        plusMinus=var_7,
        penaltyMinutes=var_7,
        powerPlayGoals=var_7,
        shortHandedGoals=var_7,
        gameWinningGoals=1301,
        shots=-2504,
        shotPercentage=1554.58,
        hockeyleague_PlayerStats9=var_11,
    )
    assert isinstance(var_12, python_code_.hockeyleague_PlayerStats)
    var_14 = {var_12, var_12, var_12, var_12}
    var_15 = python_code_.hockeyleague_Team()
    var_16 = python_code_.hockeyleague_Defence(
        position=var_12, hockeyleague_Defence=var_14, hockeyleague_Defence16=var_15
    )
    assert isinstance(var_16, python_code_.hockeyleague_Defence)


def test_19():
    var_10 = python_code_.hockeyleague_Forward(
        position="I_dd%QAs#?]MJk", hockeyleague_Forward=set()
    )
    assert isinstance(var_10, python_code_.hockeyleague_Forward)
    var_12 = lambda *args, **kwargs: True
    var_13 = 204
    var_14 = python_code_.hockeyleague_Team()
    var_15 = python_code_.hockeyleague_PlayerStats(
        year=complex(-1556.849582, -1077.482527),
        gamesPlayedIn=var_12,
        goals=1165.94,
        assists=var_10,
        points=var_12,
        plusMinus=var_12,
        penaltyMinutes=var_13,
        powerPlayGoals=var_13,
        shortHandedGoals=var_13,
        gameWinningGoals=var_10,
        shots=var_13,
        shotPercentage=var_12,
        hockeyleague_PlayerStats9=var_14,
        hockeyleague_PlayerStats=[False],
        hockeyleague_PlayerStats2=var_10,
    )
    assert isinstance(var_15, python_code_.hockeyleague_PlayerStats)


def test_20():
    var_3 = python_code_.hockeyleague_Defence(position="right_wing")
    assert isinstance(var_3, python_code_.hockeyleague_Defence)
    var_10 = -2358
    var_11 = python_code_.HeightKind
    var_12 = 1
    var_13 = python_code_.hockeyleague_PlayerStats(
        year=-370.53,
        gamesPlayedIn=var_3,
        goals=-1425.43,
        assists=var_10,
        points=var_10,
        plusMinus=var_10,
        penaltyMinutes=var_10,
        powerPlayGoals=var_11,
        shortHandedGoals=var_12,
        gameWinningGoals=var_10,
        shots=var_10,
        shotPercentage=-1234.88,
        hockeyleague_PlayerStats=var_3,
        hockeyleague_PlayerStats2=complex(-255.0, 205.5310492),
    )
    assert isinstance(var_13, python_code_.hockeyleague_PlayerStats)


def test_21():
    var_1 = python_code_.hockeyleague_Goalie()
    var_2 = 3
    var_3 = -2206
    var_4 = 2691
    var_5 = python_code_.Player
    python_code_.hockeyleague_GoalieStats(
        ties=var_1,
        emptyNetGoals=var_2,
        shutouts=var_2,
        goalsAgainst=var_3,
        saves=complex(235.07, -683.630549),
        penaltyMinutes=var_2,
        goals=var_2,
        assists=var_2,
        points=var_3,
        year=3141,
        gamesPlayedIn=var_4,
        minutesPlayedIn=var_5,
        goalsAgainstAverage=var_5,
        wins=True,
        losses=var_1,
    )
    var_7 = "e\r@^`Mw.Th\r&ymBB\t\x0b\x0b"
    var_8 = python_code_.hockeyleague_Player(
        number=var_4,
        heightMesurement=var_3,
        heightValue=var_1,
        weightMesurement=var_7,
        weightValue=var_2,
        shot=var_3,
        birthdate=b"\xda\x9c\x86.z/\xfd!B\x02o\xcc4",
        birthplace=var_7,
    )
    assert isinstance(var_8, python_code_.hockeyleague_Player)


def test_22():
    var_0 = "?Ob"
    var_1 = 3876
    var_2 = "@rcrWo[]6\x0c|7G\r9J"
    var_3 = python_code_.hockeyleague_Player(
        number="_hockeyleague_League__hockeyleague_League._hockeyleague_GoalieStats__hockeyleague_GoalieStats.hockeyleague_PlayerStats.inches",
        heightMesurement=var_0,
        heightValue=3808,
        weightMesurement={",", "left_wing"},
        weightValue=var_1,
        shot=var_1,
        birthdate=var_2,
        birthplace=var_0,
    )
    assert isinstance(var_3, python_code_.hockeyleague_Player)
    var_4 = -2532
    var_5 = -3191
    var_6 = float
    var_10 = python_code_.hockeyleague_HockeyleagueObject(name=None)
    assert isinstance(var_10, python_code_.hockeyleague_HockeyleagueObject)
    var_11 = python_code_.hockeyleague_Team()
    var_12 = python_code_.HeightKind.inches
    var_14 = 928
    var_15 = 1
    var_16 = -367.35
    var_17 = "_hockeyleague_PlayerStats__hockeyleague_PlayerStats left_defence"
    var_18 = python_code_.hockeyleague_Forward(
        position=var_17, hockeyleague_Forward=var_0
    )
    assert isinstance(var_18, python_code_.hockeyleague_Forward)
    var_19 = python_code_.hockeyleague_PlayerStats(
        year=var_4,
        gamesPlayedIn=var_11,
        goals=var_12,
        assists=var_5,
        points=-488,
        plusMinus=var_14,
        penaltyMinutes=var_15,
        powerPlayGoals=var_12,
        shortHandedGoals=var_6,
        gameWinningGoals=var_6,
        shots=var_11,
        shotPercentage=var_16,
        hockeyleague_PlayerStats9=var_11,
        hockeyleague_PlayerStats2=var_18,
    )
    assert isinstance(var_19, python_code_.hockeyleague_PlayerStats)
    var_24 = 2
    var_25 = 3
    python_code_.hockeyleague_PlayerStats(
        year=3390.14,
        gamesPlayedIn=var_24,
        goals=var_1,
        assists=var_15,
        points=var_6,
        plusMinus=var_14,
        penaltyMinutes=var_6,
        powerPlayGoals=var_25,
        shortHandedGoals=var_14,
        gameWinningGoals=var_14,
        shots=var_6,
        shotPercentage=var_17,
        hockeyleague_PlayerStats=None,
    )
    var_33 = "dG%nk*kZE6e#"
    var_34 = python_code_.hockeyleague_League(headoffice=var_33)
    assert isinstance(var_34, python_code_.hockeyleague_League)


def test_23():
    var_8 = "Y7,Q-I5D\n"
    var_10 = python_code_.hockeyleague_Forward(
        position=var_8, hockeyleague_Forward13=var_8
    )
    assert isinstance(var_10, python_code_.hockeyleague_Forward)


def test_24():
    var_0 = python_code_.Player()
    var_1 = 2136
    var_2 = python_code_.ShotKind
    var_3 = python_code_.hockeyleague_PlayerStats(
        year=778.08,
        gamesPlayedIn=var_0,
        goals=var_1,
        assists=-783,
        points=var_1,
        plusMinus=var_0,
        penaltyMinutes=var_1,
        powerPlayGoals=var_2,
        shortHandedGoals=var_0,
        gameWinningGoals=var_1,
        shots=var_1,
        shotPercentage=complex(398.39703, 2369.5571),
        hockeyleague_PlayerStats=var_0,
    )
    var_4 = {var_3, var_3}
    var_5 = python_code_.hockeyleague_Defence(
        position=complex(-1682.0, -2959.36),
        hockeyleague_Defence=var_4,
        hockeyleague_Defence16=var_2,
    )
    assert isinstance(var_5, python_code_.hockeyleague_Defence)
    var_6 = "_hockeyleague_PlayerStats__hockeyleague_PlayerStats2hockeyleague_Goalie_hockeyleague_PlayerStats__hockeyleague_PlayerStats9hockeyleague_Goalie"
    var_7 = "z+Eg4*"
    var_8 = python_code_.hockeyleague_Player(
        number=var_1,
        heightMesurement=-3085.86,
        heightValue=var_2,
        weightMesurement=var_2,
        weightValue=var_1,
        shot=var_6,
        birthdate=var_7,
        birthplace=complex(-3230.9879204, 2100.0),
    )
    assert isinstance(var_8, python_code_.hockeyleague_Player)


def test_25():
    var_12 = python_code_.hockeyleague_Team()
    var_16 = "uoazu<B>)iy"
    var_59 = -719
    var_60 = 36
    var_61 = python_code_.hockeyleague_PlayerStats(
        year=var_16,
        gamesPlayedIn=var_59,
        goals=var_60,
        assists=var_59,
        points=-2083,
        plusMinus=2,
        penaltyMinutes=2,
        powerPlayGoals=-2315,
        shortHandedGoals=var_60,
        gameWinningGoals=298,
        shots=var_60,
        shotPercentage=629.2,
        hockeyleague_PlayerStats9=var_12,
        hockeyleague_PlayerStats=None,
    )
    var_62 = {var_61, var_61, var_61}
    var_63 = python_code_.hockeyleague_Defence(
        position=var_16, hockeyleague_Defence16=None
    )
    assert isinstance(var_63, python_code_.hockeyleague_Defence)
    var_67 = python_code_.hockeyleague_Defence(
        position=var_16, hockeyleague_Defence=var_62, hockeyleague_Defence16=None
    )
    assert isinstance(var_67, python_code_.hockeyleague_Defence)
    var_69 = python_code_.hockeyleague_Defence(
        position=var_16, hockeyleague_Defence=var_62
    )
    assert isinstance(var_69, python_code_.hockeyleague_Defence)


def test_26():
    var_8 = "Y7\r,Q-I5`D\n"
    var_13 = python_code_.hockeyleague_Arena
    var_15 = -906
    var_16 = python_code_.hockeyleague_PlayerStats(
        year=var_8,
        gamesPlayedIn=1706,
        goals=-252,
        assists=4592,
        points=var_15,
        plusMinus=var_15,
        penaltyMinutes=1,
        powerPlayGoals=var_15,
        shortHandedGoals=var_15,
        gameWinningGoals=2,
        shots=var_15,
        shotPercentage=1124.58,
    )
    var_17 = {var_16, var_16}
    var_18 = python_code_.hockeyleague_Forward(
        position=var_13, hockeyleague_Forward=var_17
    )
    assert isinstance(var_18, python_code_.hockeyleague_Forward)
    var_19 = "kilograms:_hockeyleague_PlayerStats__hockeyleague_PlayerStats2:right_wing"
    var_20 = python_code_.hockeyleague_Forward(
        position=var_19, hockeyleague_Forward=var_17
    )
    assert isinstance(var_20, python_code_.hockeyleague_Forward)


def test_27():
    var_1 = python_code_.hockeyleague_League(
        headoffice="|+", hockeyleague_League={-2155, 571}
    )
    assert isinstance(var_1, python_code_.hockeyleague_League)
    var_5 = "^qS3:\n.[lDy"
    var_6 = 1476
    var_7 = 1207
    var_8 = lambda *args, **kwargs: 2
    var_9 = python_code_.hockeyleague_Defence(
        position=var_8, hockeyleague_Defence=b"o-\xa5(\x89\xd3\xf3\xe5\x1c'\xbb_\xb0"
    )
    assert isinstance(var_9, python_code_.hockeyleague_Defence)
    var_10 = python_code_.hockeyleague_PlayerStats(
        year=var_5,
        gamesPlayedIn=complex(1341.28578, -2040.73),
        goals=var_6,
        assists=var_6,
        points=var_1,
        plusMinus=False,
        penaltyMinutes=var_6,
        powerPlayGoals=True,
        shortHandedGoals={"": 2555.1},
        gameWinningGoals=var_7,
        shots=var_6,
        shotPercentage=(-1234,),
        hockeyleague_PlayerStats=var_9,
    )
    assert isinstance(var_10, python_code_.hockeyleague_PlayerStats)
