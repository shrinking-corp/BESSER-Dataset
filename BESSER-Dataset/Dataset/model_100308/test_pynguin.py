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
    Arc,
    ArcKind,
    Enum,
    Node,
    Node_dynamic,
    PNScenario,
    PNSimEvent,
    PNTrace,
    PetriNet,
    PetriNetEvent,
    Place,
    Transition,
    abstractmethod,
    date,
    datetime,
    petrinetsemantics_DDMMPetriNet_Arc,
    petrinetsemantics_DDMMPetriNet_Node,
    petrinetsemantics_DDMMPetriNet_PetriNet,
    petrinetsemantics_DDMMPetriNet_Place,
    petrinetsemantics_DDMMPetriNet_Transition,
    petrinetsemantics_EDMMPetriNet_FireTransitionEvent,
    petrinetsemantics_EDMMPetriNet_PetriNetEvent,
    petrinetsemantics_SDMMPetriNet_Node_dynamic,
    petrinetsemantics_SDMMPetriNet_PetriNet_dynamic,
    petrinetsemantics_SDMMPetriNet_Place_dynamic,
    petrinetsemantics_TM3PetriNet_PNScenario,
    petrinetsemantics_TM3PetriNet_PNSimEvent,
    petrinetsemantics_TM3PetriNet_PNTrace,
    time,
)


def test_0():
    var_20 = python_code_.petrinetsemantics_SDMMPetriNet_Place_dynamic(
        marking=1851, petrinetsemantics_SDMMPetriNet_Place_dynamic=None
    )
    assert isinstance(var_20, python_code_.petrinetsemantics_SDMMPetriNet_Place_dynamic)


def test_1():
    var_19 = python_code_.petrinetsemantics_SDMMPetriNet_Place_dynamic(
        marking=complex(-4103.553063, -449.0),
        petrinetsemantics_SDMMPetriNet_Place_dynamic=set(),
    )
    assert isinstance(var_19, python_code_.petrinetsemantics_SDMMPetriNet_Place_dynamic)


def test_2():
    python_code_.petrinetsemantics_DDMMPetriNet_Arc(
        kind=",A", weight=2647, incomings=None
    )


def test_3():
    var_1 = len
    var_10 = python_code_.petrinetsemantics_DDMMPetriNet_Arc(
        kind=2, weight=var_1, outgoings=[]
    )
    assert isinstance(var_10, python_code_.petrinetsemantics_DDMMPetriNet_Arc)


def test_4():
    var_19 = python_code_.petrinetsemantics_EDMMPetriNet_PetriNetEvent()
    python_code_.petrinetsemantics_DDMMPetriNet_Arc(
        kind="petrinetsemantics_DDMMPetriNet_Arc-read_arc-_petrinetsemantics_DDMMPetriNet_Arc__outgoings",
        weight=-3136,
        arcs=var_19,
    )


def test_5():
    var_19 = python_code_.petrinetsemantics_EDMMPetriNet_PetriNetEvent()
    python_code_.petrinetsemantics_DDMMPetriNet_Arc(
        kind="1/%5v+eO7\\+tX#", weight=var_19, incomings=var_19
    )


def test_6():
    var_7 = python_code_.petrinetsemantics_DDMMPetriNet_Node(
        name="l(Ve", source={"0[", 0, False}
    )
    assert isinstance(var_7, python_code_.petrinetsemantics_DDMMPetriNet_Node)


def test_7():
    var_7 = python_code_.petrinetsemantics_DDMMPetriNet_Node(name="r", target=set())
    assert isinstance(var_7, python_code_.petrinetsemantics_DDMMPetriNet_Node)


def test_8():
    var_34 = python_code_.petrinetsemantics_DDMMPetriNet_Node(
        name=(),
        nodes={
            "ya](uAP#U>({\r": False,
            "sG|{1_9kR:Gb": -1444.2,
            "_petrinetsemantics_DDMMPetriNet_Arc__outgoings": 1272,
        },
    )
    assert isinstance(var_34, python_code_.petrinetsemantics_DDMMPetriNet_Node)


def test_9():
    var_8 = python_code_.petrinetsemantics_DDMMPetriNet_PetriNet(
        name='BC4}O0*O]/"5J7', net={-817, 462.51}
    )
    assert isinstance(var_8, python_code_.petrinetsemantics_DDMMPetriNet_PetriNet)


def test_10():
    var_12 = python_code_.petrinetsemantics_DDMMPetriNet_PetriNet(name=315)
    assert isinstance(var_12, python_code_.petrinetsemantics_DDMMPetriNet_PetriNet)


def test_11():
    var_12 = python_code_.petrinetsemantics_DDMMPetriNet_PetriNet(
        name="petrinetsemantics_DDMMPetriNet_PetriNet Node9 petrinetsemantics_SDMMPetriNet_Node_dynamic",
        net2=set(),
    )
    assert isinstance(var_12, python_code_.petrinetsemantics_DDMMPetriNet_PetriNet)


def test_12():
    var_11 = python_code_.petrinetsemantics_EDMMPetriNet_FireTransitionEvent(
        time=598.44
    )
    assert isinstance(
        var_11, python_code_.petrinetsemantics_EDMMPetriNet_FireTransitionEvent
    )


def test_13():
    var_30 = python_code_.petrinetsemantics_EDMMPetriNet_FireTransitionEvent(
        time={},
        petrinetsemantics_EDMMPetriNet_FireTransitionEvent=complex(
            1600.754115, -1422.83
        ),
    )
    assert isinstance(
        var_30, python_code_.petrinetsemantics_EDMMPetriNet_FireTransitionEvent
    )


def test_14():
    python_code_.PNTrace()


def test_15():
    var_22 = python_code_.petrinetsemantics_DDMMPetriNet_Place(initialMarking=False)
    assert isinstance(var_22, python_code_.petrinetsemantics_DDMMPetriNet_Place)


def test_16():
    var_12 = python_code_.petrinetsemantics_DDMMPetriNet_Transition(
        min_time=(True, 3), max_time=complex(2401.122733, 693.57557)
    )
    assert isinstance(var_12, python_code_.petrinetsemantics_DDMMPetriNet_Transition)


def test_17():
    python_code_.petrinetsemantics_TM3PetriNet_PNSimEvent(
        internal=complex(1818.7426552, 1708.8748594), date=set(), name=None
    )
