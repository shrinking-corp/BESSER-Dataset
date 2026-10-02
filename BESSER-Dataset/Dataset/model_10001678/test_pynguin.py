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
    Grade,
    Note,
    Schedule,
    Student,
    Subject,
    Teacher,
    annotations,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_20 = "student8"
    var_21 = "&TUp|Lv{vA|"
    var_22 = ">+_!ZT,t$0.-"
    var_23 = "xg"
    var_24 = "N5f~SRBmfG@S?"
    var_25 = python_code_.Schedule()
    var_26 = python_code_.Student(
        phone=var_21, email=var_22, surname=var_23, name=var_24, schedule9=var_25
    )
    python_code_.Grade(name=var_20, students3=var_26)


def test_1():
    python_code_.Grade(name=None)


def test_2():
    var_6 = lambda *args, **kwargs: -2176
    python_code_.Grade(name=var_6, students3=var_6)
    python_code_.Student(
        phone="teacher0,_Student__subjects4,Grade",
        email=True,
        surname=var_6,
        name=complex(-1378.162824, 1920.0),
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = python_code_.Schedule()
    var_1 = "students3._Teacher__grades1"
    var_3 = python_code_.Teacher(name="TA]", surname=var_0, email=var_0, phone=var_1)
    var_5 = python_code_.Schedule()
    var_6 = lambda *args, **kwargs: -2176
    python_code_.Student(
        phone="teacher0,_Student__subjects4,Grade",
        email=True,
        surname=var_6,
        name=complex(-1378.162824, 1920.0),
    )
    python_code_.Grade(name=var_5, teacher0=var_3)


def test_4():
    var_0 = ""
    var_1 = bool
    python_code_.Teacher(
        name=var_0, surname=var_1, email=('7"W^q}', -1551), phone=var_0
    )
    var_8 = 'lenQ#4OIT_4rPj":(>'
    var_10 = python_code_.Student(
        phone="student5", email=var_0, surname="'|;\r", name="\\eW!56W", subjects4=var_8
    )
    assert isinstance(var_10, python_code_.Student)
    var_11 = python_code_.Grade
    var_15 = python_code_.Grade(name=var_11, teacher0=-224)
    assert isinstance(var_15, python_code_.Grade)


def test_5():
    var_21 = "\nI"
    var_22 = "students3:Grade:_Grade__teacher0:students3"
    var_13 = python_code_.Teacher(
        name=None, surname=var_21, email=var_22, phone=complex(-4152.461455, 393.774294)
    )
    python_code_.Student(
        phone=var_13,
        email="{|8tK,,y-y5\x0c{!",
        surname=var_13,
        name=var_13,
        subjects4=var_13,
        schedule9=var_13,
    )


def test_6():
    var_13 = "giRe2"
    var_17 = python_code_.Student(
        phone=var_13,
        email="{|8tK,,y-y5\x0c{!",
        surname=var_13,
        name=var_13,
        subjects4=var_13,
        schedule9=var_13,
    )
    assert isinstance(var_17, python_code_.Student)
    var_18 = "students3"
    python_code_.Teacher(
        name=var_13, surname=var_13, email=var_18, phone=var_18, grades1=var_17
    )
    var_20 = python_code_.Subject
    python_code_.Student(
        phone=var_20, email=False, surname=var_13, name=3149.92, schedule9=var_13
    )


def test_7():
    python_code_.Student(
        phone="\tz1`UvJ9q,", email="\x0bq~1v@^N+n", surname="student8", name="h+Ek9En"
    )


def test_8():
    var_13 = "gaRe2"
    var_15 = python_code_.Student(
        phone=var_13,
        email="{|8tK,,y-y5\x0c{!",
        surname=var_13,
        name=var_13,
        subjects4=var_13,
        schedule9=var_13,
    )
    assert isinstance(var_15, python_code_.Student)


def test_9():
    var_13 = "~oKt-/GHG"
    var_17 = python_code_.Student(
        phone=var_13,
        email="grades1,grades1,_Teacher__grades1",
        surname=var_13,
        name="ZnP>!{glB.JGzMJ'6",
        grade2=var_13,
    )
    assert isinstance(var_17, python_code_.Student)


def test_10():
    var_13 = "gaRde2"
    var_15 = python_code_.Student(
        phone=var_13,
        email=var_13,
        surname="_Student__schedule9 student5 grade2 Grade",
        name=";?_6_*0`DN",
        subjects4=var_13,
    )
    assert isinstance(var_15, python_code_.Student)


def test_11():
    python_code_.Schedule()


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.Schedule()
    var_1 = python_code_.Schedule()
    var_2 = "Schedule"
    python_code_.Student(phone=var_2, email=var_2, surname=var_2, name=var_1)
    var_6 = "_Student__grade2"
    var_7 = "*"
    var_8 = python_code_.Subject()
    var_9 = python_code_.Student(
        phone=var_0,
        email=var_6,
        surname=-74.7,
        name=var_7,
        subjects4=var_8,
        schedule9=complex(-262.256, 754.7726),
    )
    assert isinstance(var_9, python_code_.Student)
    var_15 = "grades1"
    var_16 = python_code_.Student(
        phone=var_1,
        email=var_2,
        surname=var_2,
        name=var_15,
        grade2=False,
        subjects4=var_7,
    )
    assert isinstance(var_16, python_code_.Student)
    python_code_.Grade(name=var_15, teacher0=-1131, students3=var_16)


@pytest.mark.xfail(strict=True)
def test_13():
    var_2 = lambda *args, **kwargs: 385
    var_3 = python_code_.Student(
        phone="&v)Yrt#`,I=", email=None, surname=var_2, name=var_2
    )
    var_4 = python_code_.Grade(name=b'\xab@~\x01\xd8\x10)\xa7\x96\x18"\xf6\x8a]1')
    var_6 = 'j5EXA"p'
    var_7 = python_code_.Grade(name=var_6, teacher0=var_3)
    var_10 = python_code_.Teacher(
        name=var_6, surname=(1618.44, 3463), email=var_4, phone=var_6
    )
    var_11 = python_code_.Subject()
    var_12 = python_code_.Subject()
    var_14 = "Grade"
    python_code_.Student(
        phone=var_4, email=var_10, surname=var_14, name=var_11, subjects4=var_12
    )
    var_18 = ""
    python_code_.Teacher(
        name=var_18,
        surname=complex(-2804.517, -4306.6592501),
        email=False,
        phone=var_2,
        grades1=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = python_code_.Subject()
    var_2 = "student8"
    var_3 = "PN\x0bH;m7T?2?'<"
    var_4 = python_code_.Schedule()
    var_5 = python_code_.Student(
        phone=var_2,
        email=var_2,
        surname=var_3,
        name=("35:9$;U7", -350, "}9P><D!5"),
        schedule9=var_4,
    )
    var_6 = python_code_.Schedule()
    var_7 = "\x0ce1Q\r>Fc(H\tkAS"
    var_8 = lambda *args, **kwargs: []
    var_9 = python_code_.Student(
        phone=var_7, email=var_7, surname=var_8, name=var_3, subjects4=1275
    )
    assert isinstance(var_9, python_code_.Student)
    var_10 = python_code_.Teacher(
        name=var_5, surname=set(), email=var_3, phone=var_7, grades1=var_8
    )
    var_13 = python_code_.Student(
        phone=var_6,
        email=var_2,
        surname=var_2,
        name=var_0,
        grade2=complex(735.3, 1618.28739),
    )
    assert isinstance(var_13, python_code_.Student)
    var_16 = "student5"
    python_code_.Grade(name=var_16)
    var_21 = ""
    python_code_.Grade(name=var_21, teacher0=var_10, students3=var_2)


@pytest.mark.xfail(strict=True)
def test_15():
    var_1 = "students3._Teache7r__grades1"
    var_18 = python_code_.Grade(name=1514, students3=var_1)
    assert isinstance(var_18, python_code_.Grade)
    var_21 = "\tP\r"
    var_22 = "grade2"
    python_code_.Student(
        phone=var_22, email=var_21, surname=var_22, name=var_21, grade2=var_18
    )
