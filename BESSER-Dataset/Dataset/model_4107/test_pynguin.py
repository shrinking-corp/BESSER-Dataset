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
    ABC,
    AbstractState,
    Enum,
    NamedElement,
    PseudostateKind,
    abstractmethod,
    compositestates_AbstractState,
    compositestates_NamedElement,
    compositestates_Pseudostate,
    compositestates_Region,
    compositestates_State,
    compositestates_Transition,
    date,
    datetime,
    time,
)


def test_0():
    var_8 = python_code_.compositestates_State(State=None)
    assert isinstance(var_8, python_code_.compositestates_State)


@pytest.mark.xfail(strict=True)
def test_1():
    var_8 = python_code_.compositestates_State(State=None)
    assert isinstance(var_8, python_code_.compositestates_State)
    var_9 = python_code_.compositestates_State()
    python_code_.compositestates_Region(Region=var_8, ownedRegions=var_9)


def test_2():
    var_16 = python_code_.compositestates_State(
        ownerState=None, State=complex(256.73, 1745.3343)
    )
    assert isinstance(var_16, python_code_.compositestates_State)


def test_3():
    var_1 = python_code_.compositestates_Region(
        ownerRegion={False, 1340.48, "_compositestates_Region__ownerRegion"}
    )
    assert isinstance(var_1, python_code_.compositestates_Region)


def test_4():
    var_1 = python_code_.compositestates_Region()
    assert var_1.ownedRegions is None


def test_5():
    var_11 = python_code_.compositestates_Region(Region7=set())
    assert isinstance(var_11, python_code_.compositestates_Region)


def test_6():
    var_12 = python_code_.compositestates_Region(Region=-2191)
    assert isinstance(var_12, python_code_.compositestates_Region)


def test_7():
    var_0 = python_code_.compositestates_State()
    assert isinstance(var_0, python_code_.compositestates_State)
    var_1 = python_code_.compositestates_State
    var_0.evalState(compositestates_context=var_1)


def test_8():
    var_3 = python_code_.compositestates_NamedElement(name=-492.62)
    assert isinstance(var_3, python_code_.compositestates_NamedElement)


def test_9():
    var_5 = python_code_.compositestates_Pseudostate(kind="W$!")
    assert isinstance(var_5, python_code_.compositestates_Pseudostate)


def test_10():
    var_32 = python_code_.compositestates_Region(
        Region7=(-1, True, -2498), ownerRegion=(-1265,)
    )
    assert isinstance(var_32, python_code_.compositestates_Region)
    var_32.initRegion(compositestates_context=var_32)


@pytest.mark.xfail(strict=True)
def test_11():
    var_11 = python_code_.compositestates_Region(
        Region7=None, ownerRegion={False}, ownedRegions=None
    )
    assert isinstance(var_11, python_code_.compositestates_Region)
    python_code_.compositestates_State(ownerState={var_11, var_11}, State=var_11)
    assert isinstance(var_11.ownedRegions, python_code_.compositestates_State)


@pytest.mark.xfail(strict=True)
def test_12():
    var_8 = python_code_.compositestates_State(ownerState=set())
    assert isinstance(var_8, python_code_.compositestates_State)
    var_9 = "r$w"
    var_10 = python_code_.compositestates_Pseudostate(kind=var_9)
    assert isinstance(var_10, python_code_.compositestates_Pseudostate)
    var_11 = python_code_.AbstractState
    var_12 = python_code_.compositestates_Region(
        Region=complex(4341.6, -2221.6), Region7="~", ownedRegions=var_11
    )
    assert isinstance(var_12, python_code_.compositestates_Region)
    var_13 = var_12.initRegion(compositestates_context=var_10)
    var_14 = python_code_.compositestates_Region(
        Region=var_8, Region7=var_11, ownerRegion=var_13
    )
    assert isinstance(var_14, python_code_.compositestates_Region)
    python_code_.compositestates_State(State=var_12)
    assert isinstance(var_12.ownedRegions, python_code_.compositestates_State)


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = python_code_.compositestates_State(ownerState=None, State=set())
    assert isinstance(var_0, python_code_.compositestates_State)
    var_0.evalState(compositestates_context=None)
    python_code_.compositestates_Region(Region=None, ownedRegions=var_0)


def test_14():
    var_8 = python_code_.compositestates_State(ownerState=set())
    assert isinstance(var_8, python_code_.compositestates_State)


def test_15():
    var_1 = python_code_.compositestates_Region(ownerRegion=set())
    assert isinstance(var_1, python_code_.compositestates_Region)
    var_3 = python_code_.compositestates_State(
        ownerState={var_1, var_1, "n!PHy\rT)5}T$?k"}
    )
    assert isinstance(var_3, python_code_.compositestates_State)


def test_16():
    var_1 = python_code_.compositestates_Region(ownerRegion=set())
    assert isinstance(var_1, python_code_.compositestates_Region)
    var_3 = python_code_.compositestates_State(
        ownerState={var_1, var_1, "n!PHy\rT)5}T$?k"}
    )
    assert isinstance(var_3, python_code_.compositestates_State)
    python_code_.compositestates_State(ownerState={var_1, var_1, "n!PHy\rT)5}T$?k"})


def test_17():
    var_17 = python_code_.compositestates_State
    var_18 = python_code_.compositestates_Region(Region=var_17, Region7=var_17)
    assert isinstance(var_18, python_code_.compositestates_Region)


def test_18():
    var_17 = tuple
    var_18 = python_code_.compositestates_Region(Region=var_17, Region7=var_17)
    assert isinstance(var_18, python_code_.compositestates_Region)
    var_26 = python_code_.compositestates_State(
        ownerState={var_18, var_18, "n!PHy\rT)5}T$?k"}
    )
    assert isinstance(var_26, python_code_.compositestates_State)


def test_19():
    var_17 = python_code_.compositestates_State
    var_18 = python_code_.compositestates_Region(Region=var_17, Region7=var_17)
    assert isinstance(var_18, python_code_.compositestates_Region)
    var_26 = python_code_.compositestates_State(
        ownerState={var_18, var_18, "n!PHy\rT)5}T$?k"}
    )
    assert isinstance(var_26, python_code_.compositestates_State)
