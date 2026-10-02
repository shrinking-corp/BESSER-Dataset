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
    Named,
    Person,
    abstractmethod,
    date,
    datetime,
    school_Named,
    school_Person,
    school_School,
    school_SchoolModel,
    school_SchoolStatistics,
    school_Student,
    school_Teacher,
    time,
)


def test_0():
    var_2 = python_code_.school_Student(
        registrationNum=-1, school_Student={True, 3251.17, False}
    )
    assert isinstance(var_2, python_code_.school_Student)


def test_1():
    var_2 = python_code_.school_Student(registrationNum=3479)
    assert isinstance(var_2, python_code_.school_Student)


@pytest.mark.xfail(strict=True)
def test_2():
    var_6 = python_code_.school_SchoolStatistics(
        studentsNumber=(),
        teachersNumber=("IFb", False, "+/`\\9svtZ\nP'PS"),
        studentsWithNoTeacher=[";\x0ck+5?+Xk6%\\v,=i", "$!\x0cn<mu\nj?e"],
    )
    python_code_.school_School(school_School2=var_6)


def test_3():
    python_code_.school_SchoolStatistics(
        studentsNumber=(),
        teachersNumber=("IFb", False, "+/`\\9svtZ\nP'PS"),
        studentsWithNoTeacher=[";\x0ck+5?+Xk6%\\v,=i", "$!\x0cn<mu\nj?e"],
    )


def test_4():
    var_9 = python_code_.school_SchoolStatistics(
        studentsNumber=[],
        teachersNumber={},
        studentsWithNoTeacher={},
        school_SchoolStatistics=[],
    )
    assert isinstance(var_9, python_code_.school_SchoolStatistics)


def test_5():
    var_3 = python_code_.school_School(school_School4=set(), school_School=None)
    assert isinstance(var_3, python_code_.school_School)


def test_6():
    var_3 = python_code_.school_School(school_School=None)
    assert isinstance(var_3, python_code_.school_School)


def test_7():
    var_2 = python_code_.school_SchoolModel()
    var_3 = python_code_.school_School(school_School2=var_2)
    assert isinstance(var_3.school_School2, python_code_.school_SchoolModel)
    var_3.getTeachers()


def test_8():
    var_3 = python_code_.school_School(
        school_School=b"k\x1b\xa0\xf7\x13\xd3\x9f\x02@l\x01\xb0\xd6"
    )
    assert isinstance(var_3, python_code_.school_School)


def test_9():
    python_code_.school_Teacher()


def test_10():
    var_4 = python_code_.school_Named(name=complex(-87.52, -1333.42))
    assert isinstance(var_4, python_code_.school_Named)


def test_11():
    var_3 = python_code_.school_School(school_School2=None, school_School=None)
    assert isinstance(var_3, python_code_.school_School)
    var_3.getStudents()


def test_12():
    var_9 = python_code_.school_School(school_School4={2073.22}, school_School=[])
    assert isinstance(var_9, python_code_.school_School)
    var_9.getTeachers()


@pytest.mark.xfail(strict=True)
def test_13():
    var_2 = python_code_.school_Student(registrationNum=1)
    assert isinstance(var_2, python_code_.school_Student)
    var_3 = python_code_.school_School()
    assert isinstance(var_3, python_code_.school_School)
    python_code_.school_SchoolStatistics(
        studentsNumber=set(),
        teachersNumber=var_2,
        studentsWithNoTeacher=var_2,
        school_SchoolStatistics=var_3,
    )
    assert isinstance(var_3.school_School2, python_code_.school_SchoolStatistics)
