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
    Account,
    Administrator,
    Comment,
    IAcc_Interface,
    Project,
    User,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_22 = python_code_.User(Id=-874, project4={-1})
    assert isinstance(var_22, python_code_.User)


def test_1():
    var_22 = python_code_.User(Id=1618, account7=None)
    assert isinstance(var_22, python_code_.User)


def test_2():
    var_22 = python_code_.User(Id=-1066, comment2=set())
    assert isinstance(var_22, python_code_.User)


@pytest.mark.xfail(strict=True)
def test_3():
    var_1 = set
    var_2 = "comment2 _Comment__user3 _User__account7"
    var_4 = python_code_.User(Id=-2744, comment2=set())
    assert isinstance(var_4, python_code_.User)
    python_code_.Account(UserName=var_1, Info=var_2, user6=var_4)


def test_4():
    var_3 = -1515
    var_4 = python_code_.User(Id=-1576, account7=var_3)
    assert isinstance(var_4, python_code_.User)


def test_5():
    python_code_.Account(
        UserName="account7._Project__user5._Administrator__comment0.Administrator",
        Info="{~>T}",
        user6=None,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_3 = "}\t7T0o#O7;>4"
    var_4 = -3875
    var_5 = python_code_.Administrator(Id=var_4)
    assert isinstance(var_5, python_code_.Administrator)
    python_code_.Account(UserName=var_3, Info=var_3, administrator8=var_5)


def test_7():
    var_31 = python_code_.Account(UserName=None, Info=False, administrator8=1580.54)
    assert var_31.administrator8 == pytest.approx(1580.54, abs=0.01, rel=0.01)


def test_8():
    python_code_.Comment(
        Id=2167,
        Creator=None,
        Title="",
        Body="account9",
        CreationDate="User",
        user3=None,
    )


def test_9():
    var_19 = python_code_.Comment(
        Id=4718,
        Creator=None,
        Title="T",
        Body='KNe]OMja57U"',
        CreationDate="2~V\\IQD 3a9U.MP6#",
        user3=None,
    )
    var_20 = {var_19}
    var_21 = python_code_.Administrator(Id=None, comment0=var_20)
    assert isinstance(var_21, python_code_.Administrator)


def test_10():
    var_25 = python_code_.User(Id=2509)
    assert isinstance(var_25, python_code_.User)
    var_27 = "X@"
    var_29 = python_code_.Comment(
        Id=var_25,
        Creator=var_25,
        Title=var_27,
        Body=var_25,
        CreationDate=var_27,
        user3=var_25,
    )
    assert isinstance(var_29, python_code_.Comment)


def test_11():
    var_17 = python_code_.Administrator(Id=290, comment0={2993.66, True})
    assert isinstance(var_17, python_code_.Administrator)


def test_12():
    var_17 = python_code_.Administrator(Id=587)
    assert isinstance(var_17, python_code_.Administrator)


def test_13():
    var_18 = python_code_.Administrator(Id=23.34, account9=())
    assert isinstance(var_18, python_code_.Administrator)


def test_14():
    var_17 = python_code_.Administrator(Id=675, comment0={-238.86, 447})
    assert isinstance(var_17, python_code_.Administrator)
    var_20 = "t\x0b~;~QlV"
    var_21 = -2514
    var_22 = python_code_.User(Id=var_21)
    assert isinstance(var_22, python_code_.User)
    var_23 = python_code_.Project(
        Id=complex(-2172.0, -3276.0),
        Title={},
        Info=var_20,
        Access=var_17,
        State=var_20,
        user5=var_22,
    )
    assert isinstance(var_23, python_code_.Project)
    var_24 = {var_23, var_23, var_23, var_23, var_20}
    var_25 = python_code_.User(Id=var_17, project4=var_24)
    assert isinstance(var_25, python_code_.User)


def test_15():
    var_25 = python_code_.User(Id=-1933, account7=None)
    assert isinstance(var_25, python_code_.User)
    var_32 = python_code_.Project(
        Id=591,
        Title="_Project__user5_User__comment2comment0",
        Info="AdministratorUserUser",
        Access="*W'ev\x0c8FLQ-YT",
        State='; 8IXDBt"kE=&u\\1\x0b^\t',
        user5=var_25,
    )
    assert isinstance(var_32, python_code_.Project)


def test_16():
    var_22 = python_code_.User(Id=-874, project4={-1})
    assert isinstance(var_22, python_code_.User)
    var_23 = 2
    python_code_.Project(
        Id=var_23,
        Title=b"\xae\xb0\x0b\xdfn\x94\xdd\xef\xf6\xa5E\xbdcm",
        Info=var_22,
        Access=[True, False, -1],
        State=var_23,
    )
    var_25 = "administrator1_User__project4"
    var_26 = python_code_.Project(
        Id=130,
        Title=(),
        Info=var_25,
        Access=var_25,
        State=b"S\xe6\xd0.\x12<a",
        user5=var_22,
    )
    assert isinstance(var_26, python_code_.Project)


def test_17():
    python_code_.IAcc_Interface()


def test_18():
    var_11 = tuple
    var_12 = python_code_.Comment(
        Id=(),
        Creator={"\nv8t\\ 8>qVre#ZXD%@-": False},
        Title={},
        Body=(),
        CreationDate=var_11,
        user3=True,
    )
    assert isinstance(var_12, python_code_.Comment)
    var_13 = {var_12, var_12}
    var_14 = python_code_.Administrator(Id=None, comment0=var_13)
    assert isinstance(var_14, python_code_.Administrator)
    var_15 = python_code_.User(Id=var_14, comment2=var_13)
    assert isinstance(var_15, python_code_.User)


@pytest.mark.xfail(strict=True)
def test_19():
    var_7 = "dr\\\x0b4ZlJVS/\x0be-h"
    python_code_.Project(
        Id=[
            "zOQ5<96KJaSAak[",
            "administrator1",
            "account9Projectaccount9administrator8",
        ],
        Title=var_7,
        Info=var_7,
        Access=var_7,
        State=var_7,
    )
    var_9 = python_code_.User(Id=-3807, account7=var_7)
    assert isinstance(var_9, python_code_.User)
    var_10 = "dr\\\x0b^ZlJVS/\x0be-h"
    var_11 = "]~9CM4z@r;<'fc`rP|]"
    var_13 = python_code_.Administrator(Id=var_11)
    assert isinstance(var_13, python_code_.Administrator)
    python_code_.Account(
        UserName=var_11,
        Info=var_10,
        user6=var_9,
        administrator8={-1479.21, -2279.38, 276.87},
    )


def test_20():
    var_0 = python_code_.IAcc_Interface()
    var_2 = "comment2 _Comment__user3 _User__account7"
    var_3 = python_code_.Account(
        UserName="_Account__administrator8", Info=var_2, user6=var_0
    )
    assert isinstance(var_3.user6, python_code_.IAcc_Interface)
    var_4 = python_code_.User(Id=-2744, comment2=set())
    assert isinstance(var_4, python_code_.User)


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = -195
    var_1 = lambda *args, **kwargs: []
    python_code_.Project(
        Id=var_0,
        Title=b"\xed\x1as=C\xcb\x1cP\xee\xe13$\xc3!>6\xb5y",
        Info=var_0,
        Access=var_1,
        State=var_1,
    )
    var_4 = -1
    var_5 = python_code_.User(Id=var_1)
    assert isinstance(var_5, python_code_.User)
    var_6 = "_User__account7,_User__account7,_Comment__administrator1"
    var_7 = python_code_.Comment(
        Id=var_4, Creator=var_5, Title=var_5, Body=var_6, CreationDate=var_6
    )
    var_8 = {var_7, var_7}
    var_9 = python_code_.User(Id=var_6, comment2=var_8)
    assert isinstance(var_9, python_code_.User)
    var_12 = python_code_.Administrator(Id=(), account9=var_1, comment0=var_8)
    assert isinstance(var_12, python_code_.Administrator)
    var_13 = float
    var_14 = python_code_.Account(
        UserName=var_9, Info=var_13, administrator8={-4440, "user6"}
    )
    assert isinstance(var_14, python_code_.Account)
    python_code_.Administrator(Id=var_4, account9=var_14)
    assert isinstance(var_14.administrator8, python_code_.Administrator)


def test_22():
    var_22 = python_code_.User(Id=0, project4=set())
    assert isinstance(var_22, python_code_.User)
    var_23 = float
    var_24 = python_code_.Administrator(Id=var_23)
    assert isinstance(var_24, python_code_.Administrator)
    var_25 = 1
    var_26 = "AccountUser_User__comment2"
    var_27 = python_code_.Comment(
        Id=var_25,
        Creator=var_22,
        Title=var_26,
        Body="f1o",
        CreationDate=var_26,
        administrator1=var_22,
        user3=var_22,
    )
    assert isinstance(var_27, python_code_.Comment)


def test_23():
    var_17 = python_code_.Administrator(Id=587)
    assert isinstance(var_17, python_code_.Administrator)
    var_18 = tuple
    var_19 = python_code_.Comment(
        Id=(),
        Creator={"\nv8t\\ 8>qVre#ZXD%@-": False},
        Title={},
        Body=(),
        CreationDate=var_18,
        user3=True,
    )
    assert isinstance(var_19, python_code_.Comment)


def test_24():
    var_3 = lambda *args, **kwargs: "_Account__user6"
    var_6 = 2889
    var_7 = python_code_.Administrator(Id=var_6)
    assert isinstance(var_7, python_code_.Administrator)
    var_9 = "<gj75>^P"
    var_10 = -437
    var_11 = python_code_.Project(
        Id=False, Title=None, Info=var_9, Access=var_7, State=var_7, user5=set()
    )
    assert isinstance(var_11, python_code_.Project)
    var_12 = {var_11}
    var_13 = python_code_.User(Id=var_10, project4=var_12, comment2=var_12)
    assert isinstance(var_13, python_code_.User)
    var_14 = python_code_.Project(
        Id=var_3, Title={}, Info=2761, Access=var_3, State=var_9, user5=var_13
    )
    assert isinstance(var_14, python_code_.Project)


def test_25():
    var_3 = -1521
    var_4 = python_code_.User(Id=var_3)
    assert isinstance(var_4, python_code_.User)
    var_5 = '\n"]fo\x0bo5v>(:8x8'
    var_6 = python_code_.Project(
        Id=b">jN\x05\xf9\x85m\x11\xfe\x039\x14?\xc6\xba\xdcP\x92\xe8",
        Title=var_4,
        Info=[],
        Access=b"x\x9d\xba\xfd\x05\xd8\xe0P{`QM\xc0+\xcd\x0e",
        State=var_5,
        user5=var_5,
    )
    assert isinstance(var_6, python_code_.Project)


def test_26():
    var_19 = python_code_.Comment(
        Id=1242,
        Creator=None,
        Title="yJ2H96PY ^ZYr)+{3by",
        Body="]hi8}0=L;FxW\nGY",
        CreationDate="y4JwW%(wpvNj",
        user3=None,
    )
    var_20 = {var_19, var_19, var_19}
    var_22 = python_code_.Administrator(Id=None, comment0=var_20)
    assert isinstance(var_22, python_code_.Administrator)
    var_23 = python_code_.Administrator(Id=None, comment0=var_20)
    assert isinstance(var_23, python_code_.Administrator)


def test_27():
    var_17 = python_code_.Administrator(Id=-3410)
    assert isinstance(var_17, python_code_.Administrator)
    var_18 = 206
    var_19 = lambda *args, **kwargs: [
        True,
        1352.87,
        "_Project__user5:Comment:_Project__user5:Account",
    ]
    var_20 = "_User__project4"
    var_21 = python_code_.Comment(
        Id=var_18,
        Creator=[],
        Title=var_17,
        Body=var_19,
        CreationDate=var_20,
        administrator1=("&\n<xUE lN?o{>$$i", -3409.05, -1),
    )
    assert isinstance(var_21, python_code_.Comment)
    var_22 = {var_21, var_21, var_21, var_21}
    var_23 = python_code_.User(Id=var_18, comment2=var_22)
    assert isinstance(var_23, python_code_.User)
    var_24 = "Project.user3._Comment__administrator1.account9"
    python_code_.Project(
        Id=var_19, Title=2799, Info=var_19, Access=var_20, State=var_24
    )
    var_26 = python_code_.Administrator(Id=var_18, comment0=var_22)
    assert isinstance(var_26, python_code_.Administrator)


def test_28():
    var_19 = python_code_.Comment(
        Id=1816,
        Creator=None,
        Title="Account",
        Body="e[PN4%m\x0b=vm\x0c",
        CreationDate="account7",
    )
    var_24 = {var_19, var_19}
    var_25 = python_code_.Administrator(Id=None, comment0=var_24)
    assert isinstance(var_25, python_code_.Administrator)
    var_26 = python_code_.User(Id=var_25, comment2=var_24)
    assert isinstance(var_26, python_code_.User)
    var_27 = 119
    var_28 = python_code_.User(Id=var_27, comment2=var_24)
    assert isinstance(var_28, python_code_.User)


@pytest.mark.xfail(strict=True)
def test_29():
    var_17 = python_code_.Administrator(Id=-3410)
    assert isinstance(var_17, python_code_.Administrator)
    var_19 = lambda *args, **kwargs: "hH/L7i#"
    var_23 = "administrator8"
    var_24 = python_code_.Account(
        UserName=var_23,
        Info=("User:_Comment__administrator1:_Account__administrator8",),
        user6=var_19,
    )
    python_code_.User(Id=var_17, account7=var_24)
    assert isinstance(var_24.user6, python_code_.User)


def test_30():
    var_17 = python_code_.Administrator(Id=-1608)
    assert isinstance(var_17, python_code_.Administrator)
    var_18 = "+z%R+b{=P\n[s~"
    var_19 = python_code_.Account(
        UserName=var_17,
        Info=var_18,
        administrator8={"comment0": -1738, "u\t\x0bU.Gq": -1344},
    )
    assert var_19.administrator8 == {"comment0": -1738, "u\t\x0bU.Gq": -1344}
    var_20 = 1
    var_21 = python_code_.User(Id=var_20, comment2=var_18)
    assert isinstance(var_21, python_code_.User)
    var_22 = tuple
    var_23 = python_code_.Comment(
        Id=433.9,
        Creator=var_21,
        Title=var_18,
        Body=var_22,
        CreationDate=var_22,
        user3=var_21,
    )
    assert isinstance(var_23, python_code_.Comment)


@pytest.mark.xfail(strict=True)
def test_31():
    var_19 = -2454
    var_20 = tuple
    var_21 = python_code_.User(Id=var_19, project4=[])
    assert isinstance(var_21, python_code_.User)
    var_22 = python_code_.Project(
        Id=var_19, Title=var_20, Info=var_19, Access=var_20, State=var_20, user5=var_21
    )
    assert isinstance(var_22, python_code_.Project)
    var_23 = "n\njFJEgaW5~$b74^Hu"
    var_24 = python_code_.Account(UserName=(), Info=var_23)
    python_code_.Administrator(Id=var_22, account9=var_24)
    assert isinstance(var_24.administrator8, python_code_.Administrator)


@pytest.mark.xfail(strict=True)
def test_32():
    var_22 = python_code_.User(
        Id=1950,
        project4={-326, True, "administrator1_Administrator__comment0administrator1"},
    )
    assert isinstance(var_22, python_code_.User)
    var_23 = -1787
    var_24 = lambda *args, **kwargs: "q-A4)2uov.a3qF"
    var_25 = python_code_.Administrator(Id=var_23, account9=var_24)
    assert isinstance(var_25, python_code_.Administrator)
    var_26 = "_User__comment2"
    python_code_.Project(
        Id=var_23, Title=var_26, Info=var_22, Access=var_26, State=var_24
    )
    python_code_.Account(UserName=var_26, Info=var_24, administrator8=var_25)


def test_33():
    var_25 = python_code_.User(Id=4069)
    assert isinstance(var_25, python_code_.User)
    var_31 = "6@\\"
    var_32 = "_Comment__user3"
    var_33 = python_code_.Administrator(Id=var_32, comment0=var_32)
    assert isinstance(var_33, python_code_.Administrator)
    var_34 = python_code_.Comment(
        Id="administrator1",
        Creator=var_25,
        Title=var_31,
        Body=var_32,
        CreationDate=var_31,
        administrator1=var_33,
    )
    assert isinstance(var_34, python_code_.Comment)
    var_35 = int
    var_36 = "0\x0c7gTc=uEE"
    python_code_.Project(
        Id=var_35, Title=var_33, Info=var_36, Access=var_25, State=var_36
    )
