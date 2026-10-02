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
    Edge,
    NamedElement,
    NetElement,
    abstractmethod,
    date,
    datetime,
    pnw_Edge,
    pnw_NamedElement,
    pnw_Net,
    pnw_NetElement,
    pnw_PTEdge,
    pnw_Place,
    pnw_TPEdge,
    pnw_Transition,
    time,
)


def test_0():
    var_60 = python_code_.pnw_Place(
        noOfTokens=-244, fromPlace={True}, toPlace={-1706.08, "", -3381}, Place=None
    )
    assert isinstance(var_60, python_code_.pnw_Place)


def test_1():
    var_60 = python_code_.pnw_Place(noOfTokens=1118, toPlace=set(), Place11=None)
    assert isinstance(var_60, python_code_.pnw_Place)


def test_2():
    var_60 = python_code_.pnw_Place(noOfTokens=-1, Place=None)
    assert isinstance(var_60, python_code_.pnw_Place)


def test_3():
    var_65 = python_code_.pnw_Place(
        noOfTokens=(), fromPlace=[4637.82, 224], Place="elements"
    )
    assert isinstance(var_65, python_code_.pnw_Place)


def test_4():
    var_70 = python_code_.pnw_Place(
        noOfTokens={"K0GD;", 1051.25, 2812},
        Place="FJzO%1U,*OesW",
        Place11=b'"\xea\x9e\x9e\xa8m\xc0T\xc7[\xe1\xd7\xf5',
    )
    assert isinstance(var_70, python_code_.pnw_Place)


def test_5():
    var_2 = python_code_.pnw_Net(incrementalID="inTPEdges", net=set())
    assert isinstance(var_2, python_code_.pnw_Net)


def test_6():
    var_2 = python_code_.pnw_Net(incrementalID="1\x0b", Net=None)
    assert isinstance(var_2, python_code_.pnw_Net)


def test_7():
    var_61 = python_code_.pnw_Net(
        incrementalID=486.02, net=b"\xb6\x9a\x01\x8f\xda\x9e\xc0", Net=()
    )
    assert isinstance(var_61, python_code_.pnw_Net)


def test_8():
    python_code_.pnw_Transition()


def test_9():
    var_0 = python_code_.pnw_Edge(weight=-385)
    assert isinstance(var_0, python_code_.pnw_Edge)


def test_10():
    var_61 = python_code_.pnw_NamedElement(name={"\tJ\\g#Z": False})
    assert isinstance(var_61, python_code_.pnw_NamedElement)
