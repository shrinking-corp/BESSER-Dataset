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
    AbstractState,
    Enum,
    NamedElement,
    PseudostateKind,
    State,
    Statement,
    abstractmethod,
    date,
    datetime,
    fsmcore_AbstractState,
    fsmcore_Conditional,
    fsmcore_Constraint,
    fsmcore_FinalState,
    fsmcore_Loop,
    fsmcore_NamedElement,
    fsmcore_Program,
    fsmcore_Pseudostate,
    fsmcore_Region,
    fsmcore_State,
    fsmcore_StateMachine,
    fsmcore_Statement,
    fsmcore_Transition,
    fsmcore_Trigger,
    fsmcore_VarDecl,
    time,
)


def test_0():
    var_8 = python_code_.fsmcore_Statement(fsmcore_Statement=None)
    assert isinstance(var_8, python_code_.fsmcore_Statement)


def test_1():
    var_17 = python_code_.fsmcore_Statement(fsmcore_Statement=-1206.19)
    assert isinstance(var_17, python_code_.fsmcore_Statement)


def test_2():
    python_code_.fsmcore_Constraint()


def test_3():
    var_16 = python_code_.fsmcore_Constraint(fsmcore_Constraint=b"\x9d\xab \xe2")
    assert isinstance(var_16, python_code_.fsmcore_Constraint)


def test_4():
    python_code_.fsmcore_Trigger(expression=True)


def test_5():
    var_18 = python_code_.fsmcore_Trigger(
        expression=1524.52, fsmcore_Trigger="jN3\x0bVFK3{0Q;="
    )
    assert isinstance(var_18, python_code_.fsmcore_Trigger)


def test_6():
    var_6 = python_code_.fsmcore_Program(
        fsmcore_Program14=None, fsmcore_Program24=set()
    )
    assert isinstance(var_6, python_code_.fsmcore_Program)


def test_7():
    var_6 = python_code_.fsmcore_Program(fsmcore_Program=None, fsmcore_Program11=None)
    assert isinstance(var_6, python_code_.fsmcore_Program)


def test_8():
    var_31 = python_code_.fsmcore_Program(fsmcore_Program11=())
    assert isinstance(var_31, python_code_.fsmcore_Program)


def test_9():
    var_10 = python_code_.fsmcore_Program(fsmcore_Program14=-3877)
    assert isinstance(var_10, python_code_.fsmcore_Program)


def test_10():
    python_code_.fsmcore_Region()


def test_11():
    var_18 = python_code_.fsmcore_Trigger(
        expression=1524.52, fsmcore_Trigger="jN3\x0bVFK3{0Q;="
    )
    assert isinstance(var_18, python_code_.fsmcore_Trigger)
    var_22 = python_code_.fsmcore_Statement()
    var_22.eval(fsmcore_context=())


def test_12():
    python_code_.fsmcore_NamedElement(
        name="_fsmcore_Program__fsmcore_Program14,_fsmcore_Program__fsmcore_Program24,_fsmcore_Statement__fsmcore_Statement,_fsmcore_Constraint__fsmcore_Constraint"
    )


def test_13():
    var_8 = python_code_.fsmcore_Constraint(
        fsmcore_Constraint={1032.68, 1419.49, 38.28}
    )
    assert isinstance(var_8, python_code_.fsmcore_Constraint)
    var_8.evalConstraint(fsmcore_context=var_8)


def test_14():
    var_11 = python_code_.fsmcore_Program(fsmcore_Program=None, fsmcore_Program11=None)
    assert isinstance(var_11, python_code_.fsmcore_Program)
    var_12 = python_code_.fsmcore_Statement(fsmcore_Statement=var_11)
    assert isinstance(var_12, python_code_.fsmcore_Statement)


def test_15():
    python_code_.fsmcore_Trigger(expression=True, fsmcore_Trigger=None)
    var_19 = python_code_.fsmcore_Program(fsmcore_Program11={})
    assert isinstance(var_19, python_code_.fsmcore_Program)
    var_19.eval(fsmcore_context=[])


def test_16():
    var_17 = python_code_.fsmcore_Pseudostate(kind="J\x0bcX\\\tdqa3")
    assert isinstance(var_17, python_code_.fsmcore_Pseudostate)


def test_17():
    var_17 = python_code_.fsmcore_Program(fsmcore_Program=[False, 1587.32])
    assert isinstance(var_17, python_code_.fsmcore_Program)


def test_18():
    var_8 = python_code_.fsmcore_Statement()
    var_9 = python_code_.fsmcore_Program(
        fsmcore_Program=None, fsmcore_Program14=var_8, fsmcore_Program24={var_8, False}
    )
    assert isinstance(var_9, python_code_.fsmcore_Program)


def test_19():
    var_21 = python_code_.fsmcore_State()
    var_22 = python_code_.fsmcore_Program(
        fsmcore_Program=var_21,
        fsmcore_Program11=var_21,
        fsmcore_Program14=var_21,
        fsmcore_Program24=(False, "@cO)%q", "3 X1Ehw"),
    )
    assert isinstance(var_22, python_code_.fsmcore_Program)
    var_23 = python_code_.fsmcore_Statement(fsmcore_Statement=var_22)
    assert isinstance(var_23, python_code_.fsmcore_Statement)
    var_24 = var_23.eval(fsmcore_context=var_23)
    var_25 = python_code_.fsmcore_Program(fsmcore_Program24=var_24)
    assert isinstance(var_25, python_code_.fsmcore_Program)
    var_22.eval(fsmcore_context=var_22)
