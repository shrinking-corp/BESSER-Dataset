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
    NamedElement,
    NetElement,
    abstractmethod,
    date,
    datetime,
    pn_NamedElement,
    pn_Net,
    pn_NetElement,
    pn_Place,
    pn_Transition,
    time,
)


def test_0():
    var_16 = python_code_.pn_Place(
        noOfTokens=1643, srcP2T={382.79}, trgT2P={True, "e\tr=i`3[$gl", 862.27}
    )
    assert isinstance(var_16, python_code_.pn_Place)


def test_1():
    var_16 = python_code_.pn_Place(noOfTokens=0, Place4=None)
    assert isinstance(var_16, python_code_.pn_Place)


def test_2():
    var_19 = python_code_.pn_Place(
        noOfTokens={}, Place=("pn_NetElement,_pn_Net__Net,pn_Transition,elements",)
    )
    assert isinstance(var_19, python_code_.pn_Place)


def test_3():
    var_20 = python_code_.pn_Place(
        noOfTokens={"a4k\x0c,!#OVg]lo": "\x0b}:", "elements": -1265.25}, Place4=set()
    )
    assert isinstance(var_20, python_code_.pn_Place)


def test_4():
    var_15 = python_code_.pn_Net(incrementalID="elements", net=set())
    assert isinstance(var_15, python_code_.pn_Net)


def test_5():
    var_15 = python_code_.pn_Net(incrementalID="\tq+\\\x0bc")
    assert isinstance(var_15, python_code_.pn_Net)


def test_6():
    var_16 = python_code_.pn_Net(incrementalID=set(), net=(), Net=[])
    assert isinstance(var_16, python_code_.pn_Net)


def test_7():
    var_15 = python_code_.pn_NamedElement(
        name={"10Way+!go\t`:]q>": 2, "^:kIOve": True, "_pn_Place__trgT2P": True}
    )
    assert isinstance(var_15, python_code_.pn_NamedElement)


def test_8():
    python_code_.pn_Transition()
