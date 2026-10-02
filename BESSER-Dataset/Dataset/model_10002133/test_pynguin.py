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
    AllowType,
    ApprovalType,
    CrudType,
    Enum,
    Enumeration,
    Event,
    Group,
    Organization,
    Panel,
    Permission,
    Resource,
    ResourceType,
    ScopeType,
    User,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    "a/n"


def test_1():
    python_code_.Permission(
        Id=[55.51, True], Name=False, Crud=(), Allow=None, Scope=None
    )


def test_2():
    python_code_.Resource(
        Id=1,
        Name="tM3o[h_",
        Description="`,BR6:;i'\r\"k*]Sc",
        NumberAvailable=-1,
        Type=None,
        Private=True,
    )


def test_3():
    var_0 = "b&];mhJ9=5..D^'"
    var_1 = lambda *args, **kwargs: False
    var_2 = -3098
    var_3 = False
    var_4 = python_code_.Resource(
        Id=var_2,
        Name=var_0,
        Description=var_0,
        NumberAvailable=var_2,
        Type=b"\xa1",
        Private=var_3,
    )
    var_5 = -1794
    var_6 = "_4n_\\n<+VPc.TfV"
    var_7 = 'WE"\x0b@-oN'
    var_8 = python_code_.User(
        UserName=var_0,
        UserHash=var_5,
        UserNameFull=complex(3438.14, 3485.0887051),
        EmailAddress=var_6,
        Password=var_7,
        Id=var_1,
        FirstName=var_7,
        LastName=None,
    )
    python_code_.Panel(
        Id=(False, "63r", False),
        Name=var_0,
        Submitter=var_0,
        Description=var_0,
        Scheduled=b'VIMv"\x8b\xb9\x03L\xc1\xd9\xd1\x13',
        Length=True,
        PreBufferTime=-1609,
        PostBufferTime=[613.29],
        Approval=var_1,
        Resources=var_4,
        Private=var_3,
        Panelists=var_8,
    )


def test_4():
    var_0 = -881
    var_1 = lambda *args, **kwargs: False
    python_code_.Resource(
        Id=var_0,
        Name=var_0,
        Description=var_0,
        NumberAvailable=var_1,
        Type=None,
        Private=var_1,
    )
    var_3 = "a-O"
    var_4 = -3215
    var_5 = "cDr5@="
    var_6 = python_code_.User(
        UserName=var_1,
        UserHash=var_0,
        UserNameFull=var_1,
        EmailAddress=complex(-744.32, -1457.6),
        Password=var_3,
        Id=var_5,
        FirstName=var_5,
        LastName=var_1,
    )
    var_7 = -410
    var_8 = 's$"\\<6nZ&.?Ha# '
    var_9 = python_code_.Permission(
        Id=var_7, Name=var_8, Crud={}, Allow=var_3, Scope=var_4
    )
    var_10 = python_code_.Group(
        Id=var_4,
        Name=var_5,
        Users=var_6,
        Permissions=var_9,
        Scope=var_3,
        ScopeId=(False,),
    )
    var_11 = -2007
    var_12 = python_code_.ApprovalType
    var_13 = python_code_.Event(
        Id=var_11,
        Name=var_1,
        Description=var_8,
        Date=var_12,
        Panels=var_11,
        Resources=[],
        Groups=var_1,
    )
    python_code_.Organization(
        Id=var_0,
        Name=[],
        Description=set(),
        Url=var_3,
        Groups=var_10,
        Events=var_13,
        Owners=var_6,
    )


def test_5():
    python_code_.Group(
        Id=complex(-1096.48771, 2886.6),
        Name=None,
        Users=b"\xe4\xb8\x97\x0b\x82k7\xe4,V\x9e\x08",
        Permissions=False,
        Scope=None,
        ScopeId=b"\xd2\x08\xcfF\xf5y\x07\xc4\xd0\xbe\xd7\x97",
    )
