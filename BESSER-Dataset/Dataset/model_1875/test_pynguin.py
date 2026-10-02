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
    Annotatable,
    Collection,
    ProbLogStatement,
    ProbabilityMeasure,
    Proposition,
    Referable,
    Statement,
    abstractmethod,
    date,
    datetime,
    problog_Annotatable,
    problog_AnnotatedReferable,
    problog_Atom,
    problog_Cheat,
    problog_Collection,
    problog_Comment,
    problog_Evidence,
    problog_ImportLibrary,
    problog_LHS,
    problog_PLList,
    problog_PLTuple,
    problog_ProbLogProgram,
    problog_ProbLogStatement,
    problog_ProbabilityFraction,
    problog_ProbabilityLiteral,
    problog_ProbabilityMeasure,
    problog_Proposition,
    problog_Query,
    problog_RHS,
    problog_Referable,
    problog_Rule,
    problog_Statement,
    problog_Term,
    problog_TermInstance,
    problog_Variable,
    time,
)


def test_0():
    python_code_.problog_Term(
        name="problog_ProbLogProgram-_problog_Term__problog_Term",
        arguments=2447,
        problog_Term=None,
    )


def test_1():
    var_2 = -548
    var_3 = python_code_.problog_Term(
        name=">qQAPE\x0bw0`V\nHBYa5\r4", arguments=var_2, problog_Term16=var_2
    )
    assert isinstance(var_3, python_code_.problog_Term)


def test_2():
    var_74 = -4578.44467215375
    var_75 = python_code_.problog_Term(
        name=var_74, arguments=var_74, problog_Term=var_74
    )
    assert isinstance(var_75, python_code_.problog_Term)


def test_3():
    python_code_.problog_TermInstance()


def test_4():
    var_105 = python_code_.problog_ProbabilityFraction(nominator=1022, denominator=-483)
    assert isinstance(var_105, python_code_.problog_ProbabilityFraction)


def test_5():
    var_80 = python_code_.problog_ProbabilityLiteral(value=756.96)
    assert isinstance(var_80, python_code_.problog_ProbabilityLiteral)


def test_6():
    var_95 = python_code_.problog_Variable(
        name="_problog_Term__problog_Term _problog_Term__problog_Term16"
    )
    assert isinstance(var_95, python_code_.problog_Variable)


def test_7():
    var_88 = python_code_.problog_Atom(name=[])
    assert isinstance(var_88, python_code_.problog_Atom)


def test_8():
    var_89 = python_code_.problog_Evidence(value=58)
    assert isinstance(var_89, python_code_.problog_Evidence)


def test_9():
    var_79 = python_code_.problog_ImportLibrary(name=(False, 3572.5))
    assert isinstance(var_79, python_code_.problog_ImportLibrary)


def test_10():
    var_1 = python_code_.problog_Cheat(
        contents="_problog_Term__problog_Term.problog_TermInstance"
    )
    assert isinstance(var_1, python_code_.problog_Cheat)


def test_11():
    var_1 = python_code_.problog_Comment(text=",1\\f`5R(")
    assert isinstance(var_1, python_code_.problog_Comment)
