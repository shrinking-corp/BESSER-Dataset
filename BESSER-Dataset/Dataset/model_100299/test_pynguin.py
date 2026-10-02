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
    Arc,
    Attribute,
    Label,
    PetriNetType,
    Place,
    StructuredLabel,
    date,
    datetime,
    petrinet_Animation,
    petrinet_AnimationLabel,
    petrinet_Arc,
    petrinet_ExtendedPetriNet,
    petrinet_GeometryLabel,
    petrinet_Identity,
    petrinet_InputPlace,
    petrinet_Place,
    petrinet_Token,
    time,
)


def test_0():
    var_8 = python_code_.petrinet_Identity(
        text="_petrinet_Identity__petrinet_Identity_petrinet_InputPlace__petrinet_InputPlace_petrinet_Token__petrinet_Tokenpetrinet_Place6",
        petrinet_Identity=None,
    )
    assert isinstance(var_8, python_code_.petrinet_Identity)


def test_1():
    var_14 = python_code_.petrinet_Identity(text=-221.18, petrinet_Identity=[])
    assert isinstance(var_14, python_code_.petrinet_Identity)


def test_2():
    var_13 = python_code_.petrinet_InputPlace(text=False)
    assert isinstance(var_13, python_code_.petrinet_InputPlace)


def test_3():
    var_28 = python_code_.petrinet_InputPlace(text=False, petrinet_InputPlace={})
    assert isinstance(var_28, python_code_.petrinet_InputPlace)


def test_4():
    var_0 = python_code_.petrinet_Token(text=())
    assert isinstance(var_0, python_code_.petrinet_Token)


def test_5():
    var_19 = python_code_.petrinet_Token(
        text=complex(-1950.1, -1593.2797111), petrinet_Token=[]
    )
    assert isinstance(var_19, python_code_.petrinet_Token)


def test_6():
    var_9 = python_code_.petrinet_GeometryLabel(
        text=".4zMja3ETK1;\x0bg", petrinet_GeometryLabel=None
    )
    assert isinstance(var_9, python_code_.petrinet_GeometryLabel)


def test_7():
    var_21 = python_code_.petrinet_GeometryLabel(
        text="[!c#;XC&WV", petrinet_GeometryLabel=()
    )
    assert isinstance(var_21, python_code_.petrinet_GeometryLabel)


def test_8():
    python_code_.petrinet_AnimationLabel()
