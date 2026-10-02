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
from python_code import date, datetime, testpackage_Group, testpackage_User, time


def test_0():
    var_36 = python_code_.testpackage_Group(
        name="_testpackage_Group__testpackage_Group", testpackage_Group=set()
    )
    assert isinstance(var_36, python_code_.testpackage_Group)


def test_1():
    var_36 = python_code_.testpackage_Group(
        name="_testpackage_Group__testpackage_Group"
    )
    assert isinstance(var_36, python_code_.testpackage_Group)


def test_2():
    var_53 = python_code_.testpackage_User(
        name=620.68, password=set(), testpackage_User=True
    )
    assert isinstance(var_53, python_code_.testpackage_User)


def test_3():
    python_code_.testpackage_User(
        name=complex(2426.34036, -3858.9742284), password=2519
    )


def test_4():
    var_58 = python_code_.testpackage_Group(name="2.")
    assert isinstance(var_58, python_code_.testpackage_Group)
    var_61 = python_code_.testpackage_User(
        name="4",
        password="_testpackage_User__testpackage_User-_testpackage_Group__testpackage_Group-testpackage_User",
        testpackage_User=var_58,
    )
    assert isinstance(var_61, python_code_.testpackage_User)


def test_5():
    var_36 = python_code_.testpackage_Group(
        name="testpackage_User-_testpackage_Group__testpackage_Group-testpackage_User-testpackage_Group",
        testpackage_Group={"_testpackage_Group__testpackage_Group"},
    )
    assert isinstance(var_36, python_code_.testpackage_Group)
    var_36.isMember(testpackage_user={True})


def test_6():
    var_48 = python_code_.testpackage_Group(name=set(), testpackage_Group={})
    assert isinstance(var_48, python_code_.testpackage_Group)
    var_46 = python_code_.testpackage_User(
        name=[], password=True, testpackage_User=var_48
    )
    assert isinstance(var_46, python_code_.testpackage_User)


def test_7():
    var_6 = "Fae-<aJ"
    var_7 = python_code_.testpackage_Group(name=var_6)
    assert isinstance(var_7, python_code_.testpackage_Group)
    var_35 = python_code_.testpackage_User(
        name=var_6, password=var_6, testpackage_User=var_7
    )
    assert isinstance(var_35, python_code_.testpackage_User)
    var_36 = python_code_.testpackage_Group(
        name="testpackage_User", testpackage_Group={-660.57, var_35, var_6}
    )
    assert isinstance(var_36, python_code_.testpackage_Group)


def test_8():
    var_6 = "Dc*3:t["
    var_59 = python_code_.testpackage_User(name=var_6, password=var_6)
    var_60 = python_code_.testpackage_Group(
        name="testpackage_User", testpackage_Group={-660.57, var_59, var_6}
    )
    assert isinstance(var_60, python_code_.testpackage_Group)


def test_9():
    var_6 = "I3\\)1Y\x0b1I5khFlt8}W>"
    var_66 = b"-\x94\x93\x92*\xc4\x0bmg\xb6\xecN\xd61\x1f\x04\xa9\xfe\x01"
    var_67 = python_code_.testpackage_User(
        name=var_6, password='?\x0b|e4~B%"$', testpackage_User=var_66
    )
    assert isinstance(var_67, python_code_.testpackage_User)
    var_68 = python_code_.testpackage_Group(
        name="testpackage_User", testpackage_Group={-660.57, var_67, var_6}
    )
    assert isinstance(var_68, python_code_.testpackage_Group)
