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
    RModelElement,
    SimpleRDBMS_Column,
    SimpleRDBMS_ForeignKey,
    SimpleRDBMS_Key,
    SimpleRDBMS_RModelElement,
    SimpleRDBMS_Schema,
    SimpleRDBMS_Table,
    date,
    datetime,
    time,
)


def test_0():
    var_6 = python_code_.SimpleRDBMS_Column(
        type="P9[x\rCObgdGn(#\tRc",
        Column=None,
        column8=set(),
        Column19=None,
        Column14=None,
    )
    assert isinstance(var_6, python_code_.SimpleRDBMS_Column)


def test_1():
    var_6 = python_code_.SimpleRDBMS_Column(
        type="SimpleRDBMS_Table _SimpleRDBMS_Column__column11 owner owner",
        Column19=None,
    )
    assert isinstance(var_6, python_code_.SimpleRDBMS_Column)


def test_2():
    var_6 = python_code_.SimpleRDBMS_Column(
        type="SimpleRDBMS_Key._key.Table._SimpleRDBMS_Column__column", column11={True}
    )
    assert isinstance(var_6, python_code_.SimpleRDBMS_Column)


def test_3():
    var_30 = python_code_.SimpleRDBMS_Column(type=[], Column19=-3462)
    assert isinstance(var_30, python_code_.SimpleRDBMS_Column)


def test_4():
    var_11 = python_code_.SimpleRDBMS_Column(type=b'|"\xc5\x91\xd0', Column14=[])
    assert isinstance(var_11, python_code_.SimpleRDBMS_Column)


def test_5():
    var_10 = python_code_.SimpleRDBMS_Column(
        type=b"<\xe4\xae\x15\x1e\x82@F7\xc7\x82\xe3\x94X\xc6=#\xbb",
        Column=(),
        column8=b"\xaank",
        Column14=None,
    )
    assert isinstance(var_10, python_code_.SimpleRDBMS_Column)


def test_6():
    var_48 = python_code_.SimpleRDBMS_Column(type=None, column=(2122, 1, 1116.34))
    assert isinstance(var_48, python_code_.SimpleRDBMS_Column)


def test_7():
    python_code_.SimpleRDBMS_RModelElement(
        kind=-1687, name={',Pkv7s"5\\q$H}+@a', False}
    )


def test_8():
    python_code_.SimpleRDBMS_Table()
