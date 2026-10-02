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
    Expr,
    ExprSimple,
    date,
    datetime,
    time,
    wh_Affect,
    wh_Command,
    wh_Commands,
    wh_Definition,
    wh_EObject,
    wh_Expr,
    wh_ExprSimple,
    wh_Exprs,
    wh_Input,
    wh_Nop,
    wh_Output,
    wh_Program,
    wh_Vars,
    wh_Wh,
    wh_cons,
)


def test_0():
    var_19 = python_code_.wh_Vars(vars=None, wh_Vars=499.24)
    assert isinstance(var_19, python_code_.wh_Vars)


def test_1():
    python_code_.wh_Vars(vars="Q^NN+cM0\x0c00Lb+U<")


def test_2():
    python_code_.wh_Output(vars='Af;J5+VN&]*"4`{]')


def test_3():
    var_23 = python_code_.wh_Output(vars={}, wh_Output='Jo"aGQ{O7\t')
    assert isinstance(var_23, python_code_.wh_Output)


def test_4():
    python_code_.wh_Input(vars={})


def test_5():
    var_25 = python_code_.wh_Input(
        vars=b"\xd4a*\x9e\xd7_q\xd0\x89\x04\xf5\xa8\xc3\xb2",
        wh_Input=b"H\x88~W \x13\x93\x93",
    )
    assert isinstance(var_25, python_code_.wh_Input)


def test_6():
    python_code_.wh_Program(name="KD~35\nGtI\tp-")


def test_7():
    var_28 = python_code_.wh_Program(name=(), wh_Program=[])
    assert isinstance(var_28, python_code_.wh_Program)


def test_8():
    var_28 = python_code_.wh_Program(name=[], wh_Program2=-3371.17)
    assert isinstance(var_28, python_code_.wh_Program)


def test_9():
    python_code_.wh_Commands()


def test_10():
    python_code_.wh_Nop(nop=187)


def test_11():
    var_1 = python_code_.wh_cons(list="p!U{`7_]WGWz $k\\hQl")
    assert isinstance(var_1, python_code_.wh_cons)
