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
from python_code import A, b_A, b_B, b_C, date, datetime, time


def test_0():
    var_0 = python_code_.b_B(y=True, b_B0=None, b_B3={-304, -3459, -1})
    assert isinstance(var_0, python_code_.b_B)


def test_1():
    var_0 = python_code_.b_B(y={" $M|q/^f": 57.02})
    assert isinstance(var_0, python_code_.b_B)


@pytest.mark.xfail(strict=True)
def test_2():
    var_2 = True
    var_10 = python_code_.b_A
    var_11 = python_code_.b_B(y=var_2, b_B0=var_10)
    assert isinstance(var_11, python_code_.b_B)
    var_12 = python_code_.b_A(x=" i-yo\x0bbVNqmc#\\?")
    var_13 = var_12.bar()
    python_code_.b_B(y=var_10, b_B=var_11, b_B0=var_11, b_B3=var_13)


def test_3():
    var_12 = python_code_.b_B(y=None, b_B0=4729)
    assert isinstance(var_12, python_code_.b_B)


def test_4():
    var_10 = python_code_.b_B(y={}, b_B=set())
    assert var_10.b_B == set()


def test_5():
    python_code_.b_A(x="_b_A__b_A_b_B__b_B3b_A")


def test_6():
    var_9 = "_b_B__b_B0-b_B3"
    var_10 = python_code_.b_B(y={}, b_B=set())
    assert var_10.b_B == set()
    var_11 = python_code_.b_A(x=var_9, b_A=var_10)
    assert isinstance(var_11.b_A, python_code_.b_B)


def test_7():
    True


def test_8():
    var_0 = ""
    var_1 = python_code_.b_A(x=var_0)
    var_1.bar()


def test_9():
    var_14 = python_code_.b_C(z={652.44, "b_B3,_b_B__b_B,_b_A__b_A"})
    assert isinstance(var_14, python_code_.b_C)


@pytest.mark.xfail(strict=True)
def test_10():
    var_12 = python_code_.b_B(y=True, b_B=None)
    assert isinstance(var_12, python_code_.b_B)
    python_code_.b_B(y=False, b_B0=var_12, b_B3=set())
    assert isinstance(var_12.b_B, python_code_.b_B)


@pytest.mark.xfail(strict=True)
def test_11():
    var_1 = python_code_.A()
    var_10 = "b_B0.b_B0._b_B__b_B0"
    var_11 = python_code_.b_A(x=var_10, b_A=var_1)
    assert isinstance(var_11.b_A, python_code_.A)
    var_12 = True
    var_13 = True
    var_14 = var_11.bar()
    var_15 = python_code_.b_B(y=var_13, b_B3=var_14)
    assert isinstance(var_15, python_code_.b_B)
    python_code_.b_B(y=var_12, b_B0=var_15)
    assert isinstance(var_15.b_B, python_code_.b_B)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.b_C(z=3541.94)
    assert isinstance(var_0, python_code_.b_C)
    var_1 = False
    var_2 = False
    var_3 = python_code_.b_B(y=var_2, b_B=var_1)
    assert var_3.b_B is False
    python_code_.b_B(y=var_1, b_B0=var_3)
