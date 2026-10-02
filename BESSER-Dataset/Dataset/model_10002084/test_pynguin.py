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
    Event,
    EventType,
    Registration,
    User,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_1 = python_code_.EventType(Type="4`H]`,QrS/f", EventTypeId=1626, events2=set())
    assert isinstance(var_1, python_code_.EventType)


def test_1():
    var_1 = python_code_.EventType(Type="jc!s#", EventTypeId=1771)
    assert isinstance(var_1, python_code_.EventType)


def test_2():
    var_18 = python_code_.User(
        UserId=-698,
        Email="user1",
        Login="]Z(Iwe\n J?i|>fL4\r+",
        Password="r@ ",
        PhoneNumber="events2",
        DateOfBirth="?.*;",
        registrations0={-1151.0},
    )
    assert isinstance(var_18, python_code_.User)


def test_3():
    var_18 = python_code_.User(
        UserId=-5696,
        Email="MN9R9.f-X?'S\ty#>",
        Login="/I\"<'1b0",
        Password="0>(ru",
        PhoneNumber="User_Event__registrations4_EventType__events2",
        DateOfBirth=" dwwTw%N7I}M",
    )
    assert isinstance(var_18, python_code_.User)


@pytest.mark.xfail(strict=True)
def test_4():
    var_20 = python_code_.EventType(
        Type="_Event__user7", EventTypeId=3, events2={"events6", 2, "GBL"}
    )
    assert isinstance(var_20, python_code_.EventType)
    var_21 = 154
    var_22 = "event5_User__events6"
    var_23 = lambda *args, **kwargs: "events2"
    var_24 = "_User__events6"
    var_25 = python_code_.Event(
        EventId=var_23,
        Address=var_21,
        CurrentNumberOfPlayers=2,
        MaxNumberOfPlayers=var_23,
        DateTime=var_24,
        Description=var_23,
        attribute=var_22,
        user7=set(),
    )
    assert isinstance(var_25, python_code_.Event)
    python_code_.User(
        UserId=var_21,
        Email=var_22,
        Login=var_23,
        Password=complex(-1490.272, 308.273339),
        PhoneNumber=var_22,
        DateOfBirth=var_20,
        events6=var_25,
    )


def test_5():
    var_15 = "%n*P%pT&b\rkXN"
    var_16 = python_code_.User(
        UserId=2258,
        Email=var_15,
        Login=var_15,
        Password=var_15,
        PhoneNumber=var_15,
        DateOfBirth=var_15,
        registrations0={-744.96, -2273.21},
        events6=var_15,
    )
    assert var_16.events6 == "%n*P%pT&b\rkXN"


def test_6():
    var_6 = "<&"
    var_10 = python_code_.Event(
        EventId=3,
        Address=var_6,
        CurrentNumberOfPlayers=-1436,
        MaxNumberOfPlayers=-487,
        DateTime=var_6,
        Description=var_6,
        attribute=var_6,
        event_type3=var_6,
        registrations4=set(),
    )
    assert isinstance(var_10, python_code_.Event)


def test_7():
    var_6 = "&"
    var_10 = python_code_.Event(
        EventId=2227,
        Address=var_6,
        CurrentNumberOfPlayers=1,
        MaxNumberOfPlayers=-2708,
        DateTime=var_6,
        Description=var_6,
        attribute=var_6,
    )
    assert isinstance(var_10, python_code_.Event)


@pytest.mark.xfail(strict=True)
def test_8():
    var_5 = 1204.0
    var_6 = "event_type3"
    var_7 = lambda *args, **kwargs: False
    var_8 = python_code_.Event(
        EventId=var_5,
        Address=var_6,
        CurrentNumberOfPlayers=complex(-816.8, -151.6342508),
        MaxNumberOfPlayers=var_7,
        DateTime=var_7,
        Description=var_7,
        attribute=var_7,
        event_type3=var_7,
        user7=b"\n\xb1\xbb\xb2\x87\x03\xb7",
    )
    assert isinstance(var_8, python_code_.Event)
    var_9 = -1674
    var_10 = {var_8, var_8, var_8, var_8, var_8}
    var_11 = python_code_.EventType(
        Type=b"\xa9\xa0Z", EventTypeId=var_9, events2=var_10
    )
    assert isinstance(var_11, python_code_.EventType)
    python_code_.User(
        UserId=var_11,
        Email=var_11,
        Login=var_7,
        Password=b"\x81\xa1\xb1n8\xd1\xbbdb`\x06\x83\xb6G#\x909\xe5",
        PhoneNumber=var_6,
        DateOfBirth=var_6,
        events6=var_8,
    )


def test_9():
    var_6 = "&"
    var_10 = python_code_.Event(
        EventId=87,
        Address=var_6,
        CurrentNumberOfPlayers=-4770,
        MaxNumberOfPlayers=1,
        DateTime=var_6,
        Description='Z= ^"I7Pa*MW',
        attribute="user1",
        event_type3=var_6,
    )
    assert isinstance(var_10, python_code_.Event)


def test_10():
    var_6 = "&"
    var_10 = python_code_.Event(
        EventId=989,
        Address=var_6,
        CurrentNumberOfPlayers=40,
        MaxNumberOfPlayers=68,
        DateTime=var_6,
        Description="\\qH?,XpRl3;T&qc",
        attribute="}hRh]^}&@Q}h\r<0Q",
        user7=var_6,
    )
    assert isinstance(var_10, python_code_.Event)


def test_11():
    var_0 = python_code_.EventType(Type="^d4DQ *G\\%n8Oz", EventTypeId=-1221)
    assert isinstance(var_0, python_code_.EventType)
    var_7 = 3
    var_8 = "#[F1\x0b(sTUY4u7"
    var_9 = python_code_.Event(
        EventId=var_7,
        Address=var_8,
        CurrentNumberOfPlayers=var_7,
        MaxNumberOfPlayers=var_7,
        DateTime=(),
        Description=var_8,
        attribute=set(),
        event_type3=var_0,
        registrations4={468.57, 1769, 3024},
    )
    assert isinstance(var_9, python_code_.Event)


def test_12():
    var_6 = -2347
    var_7 = "user1:User"
    var_8 = python_code_.Event(
        EventId=var_6,
        Address=var_7,
        CurrentNumberOfPlayers=113,
        MaxNumberOfPlayers=-2081,
        DateTime="user7",
        Description=var_7,
        attribute=var_7,
        event_type3=None,
        registrations4=set(),
    )
    assert isinstance(var_8, python_code_.Event)
    var_9 = {var_8}
    var_10 = python_code_.EventType(Type=var_6, EventTypeId=var_7, events2=var_9)
    assert isinstance(var_10, python_code_.EventType)


@pytest.mark.xfail(strict=True)
def test_13():
    var_18 = python_code_.User(
        UserId=-1528,
        Email="M>^(x2_C)o<3,i",
        Login="Registration events2 event_type3",
        Password="_\x0c^1WuW@jU08|p",
        PhoneNumber="Registration:_User__events6",
        DateOfBirth="user7",
    )
    assert isinstance(var_18, python_code_.User)
    var_23 = "Qf%D6KH"
    var_24 = 3
    var_25 = python_code_.EventType(Type=var_23, EventTypeId=var_24)
    assert isinstance(var_25, python_code_.EventType)
    python_code_.Event(
        EventId=var_24,
        Address=var_23,
        CurrentNumberOfPlayers=var_24,
        MaxNumberOfPlayers={-2078},
        DateTime=var_18,
        Description=(True,),
        attribute=None,
        user7=var_18,
    )
    assert isinstance(var_18.events6, python_code_.Event)


@pytest.mark.xfail(strict=True)
def test_14():
    var_24 = -2502
    var_25 = "\r/\n)<hu"
    var_26 = lambda *args, **kwargs: False
    var_27 = python_code_.EventType(Type=var_26, EventTypeId=var_26)
    assert isinstance(var_27, python_code_.EventType)
    var_20 = python_code_.Event(
        EventId=var_24,
        Address=var_24,
        CurrentNumberOfPlayers={False, 0},
        MaxNumberOfPlayers=var_24,
        DateTime=var_25,
        Description=var_25,
        attribute=var_25,
        event_type3=var_27,
    )
    assert isinstance(var_20, python_code_.Event)
    var_28 = "g8\n"
    var_29 = "XT4c/"
    var_30 = "dy\r0LM\n?RM6A$ll?V,L"
    var_31 = python_code_.Registration()
    var_32 = {var_31}
    var_33 = "Registration-events2-_User__registrations0"
    var_34 = "\\%L SA9J~LzLPO\nV\x0b^I"
    var_35 = "] CX&cdwPOTJ*TX*R?"
    var_36 = python_code_.User(
        UserId=[False, "D%L,", True],
        Email=var_33,
        Login=var_34,
        Password=var_35,
        PhoneNumber=var_26,
        DateOfBirth=var_20,
        events6=-1305,
    )
    assert var_36.events6 == -1305
    python_code_.Event(
        EventId=var_25,
        Address=[],
        CurrentNumberOfPlayers=var_27,
        MaxNumberOfPlayers=var_26,
        DateTime=var_28,
        Description=var_29,
        attribute=var_30,
        registrations4=var_32,
        user7=var_36,
    )


@pytest.mark.xfail(strict=True)
def test_15():
    var_18 = python_code_.User(
        UserId=3,
        Email="events6",
        Login="user7-events6",
        Password="Q\r9",
        PhoneNumber="eJ,",
        DateOfBirth="0",
    )
    assert isinstance(var_18, python_code_.User)
    var_20 = -750
    var_21 = python_code_.EventType
    python_code_.Event(
        EventId=var_20,
        Address=[],
        CurrentNumberOfPlayers={},
        MaxNumberOfPlayers=var_20,
        DateTime={
            "Registration": -2216,
            "events2": "_EventType__events2",
            "events6,_EventType__events2": 2,
        },
        Description=(),
        attribute=var_18,
        event_type3=var_21,
        registrations4=var_18,
        user7=var_18,
    )


def test_16():
    var_1 = python_code_.EventType(Type="9P", EventTypeId=603, events2={3947, -2487.12})
    assert isinstance(var_1, python_code_.EventType)
    var_5 = "EVAxiLwi"
    var_6 = 1592
    var_7 = -2345
    var_8 = python_code_.Event(
        EventId=var_6,
        Address={True, "\tJ"},
        CurrentNumberOfPlayers=var_7,
        MaxNumberOfPlayers=var_7,
        DateTime=(),
        Description=var_5,
        attribute=var_1,
    )
    assert isinstance(var_8, python_code_.Event)
    var_9 = lambda *args, **kwargs: 1264
    var_10 = "sH4A"
    var_11 = "_User__registrations0_User__events6events2"
    var_12 = python_code_.EventType(Type=var_11, EventTypeId=var_7)
    var_13 = python_code_.Event(
        EventId=True,
        Address=var_9,
        CurrentNumberOfPlayers=var_7,
        MaxNumberOfPlayers=var_6,
        DateTime=var_8,
        Description=var_10,
        attribute=var_5,
        event_type3=var_12,
    )
    assert isinstance(var_13, python_code_.Event)
    var_14 = {var_8, var_8, var_13, var_13}
    python_code_.EventType(Type=var_5, EventTypeId=var_6, events2=var_14)


def test_17():
    var_0 = python_code_.EventType(Type=1285.03, EventTypeId=2647)
    assert isinstance(var_0, python_code_.EventType)
    var_1 = python_code_.Registration()
    var_2 = "K"
    var_3 = 2
    var_4 = python_code_.EventType(
        Type=var_2, EventTypeId=var_3, events2=("events6", "event5")
    )
    assert isinstance(var_4, python_code_.EventType)
    var_5 = "Ky* 4 "
    var_6 = python_code_.EventType
    var_7 = 'g"'
    var_8 = set()
    var_9 = python_code_.User(
        UserId=1243.61,
        Email=var_5,
        Login=var_2,
        Password=var_6,
        PhoneNumber=var_7,
        DateOfBirth=False,
        registrations0=var_8,
    )
    assert isinstance(var_9, python_code_.User)
    var_11 = "5s78E6lSC'deXtYhE"
    var_12 = "9"
    var_13 = python_code_.Event(
        EventId=("D]XI)}oy", True),
        Address=var_11,
        CurrentNumberOfPlayers=var_3,
        MaxNumberOfPlayers=complex(-893.5864518, 2044.4714),
        DateTime=var_2,
        Description=var_12,
        attribute=var_2,
        user7=2725.11,
    )
    assert isinstance(var_13, python_code_.Event)
    var_14 = -1892
    var_15 = "Xj%"
    var_16 = python_code_.Event(
        EventId=var_3,
        Address=var_0,
        CurrentNumberOfPlayers=var_2,
        MaxNumberOfPlayers=var_14,
        DateTime=var_11,
        Description=var_15,
        attribute=var_1,
        event_type3=var_6,
        user7=var_11,
    )
    assert isinstance(var_16, python_code_.Event)
    var_17 = {var_13, var_16, var_16, var_13}
    var_18 = python_code_.EventType(Type=var_7, EventTypeId=None, events2=var_17)
    assert isinstance(var_18, python_code_.EventType)
    var_26 = 5181
    var_27 = "z'qRVMdwY~"
    python_code_.Event(
        EventId=var_26,
        Address=var_6,
        CurrentNumberOfPlayers=var_6,
        MaxNumberOfPlayers=(1340.85, "eD(\t", 3),
        DateTime=var_11,
        Description=set(),
        attribute=var_27,
        registrations4=var_17,
    )
