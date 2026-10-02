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
    Access_Information,
    Admin,
    Attendance,
    Authentication,
    Course,
    Department,
    Employee_Interface,
    HOD,
    Student,
    Subject,
    Teacher,
    administrator,
    annotations,
    date,
    datetime,
    department,
    students,
    subject,
    time,
)


def test_0():
    var_0 = python_code_.Course(
        subjects__=None, duration="department5:Subject:Department", subject2=set()
    )
    assert isinstance(var_0, python_code_.Course)
    var_1 = python_code_.Subject(name="{X9_\x0c4qG'+\x0ceDK", course3=var_0)
    assert isinstance(var_1, python_code_.Subject)
    var_2 = "Subject"
    var_3 = {var_1, var_1}
    python_code_.Course(
        subjects__=var_1, duration=var_2, department1=var_1, subject2=var_3
    )


def test_1():
    python_code_.Subject(name=1911.29)


def test_2():
    var_0 = python_code_.Subject(
        name="course0 subject2 Department _Department__access_Information19",
        course3=[False, "HQ\\dn`#iK:?e"],
    )
    assert isinstance(var_0, python_code_.Subject)


def test_3():
    var_0 = python_code_.Course(
        subjects__=b".\xc5\x1d-]\xd1\xe9\x0c\xc3e\xff",
        duration={False, True},
        subject2=set(),
    )
    assert isinstance(var_0, python_code_.Course)


def test_4():
    var_0 = python_code_.Course(subjects__=None, duration="`}Xjql=pC")
    assert isinstance(var_0, python_code_.Course)


def test_5():
    var_39 = python_code_.Course(
        subjects__={187.67}, duration=complex(-1733.16478, -1458.6), department1=[]
    )
    assert isinstance(var_39, python_code_.Course)


def test_6():
    var_32 = python_code_.Department(
        course=None, students__=None, teachers__=None, hod=None, student4=set()
    )
    assert isinstance(var_32, python_code_.Department)


def test_7():
    var_32 = python_code_.Department(
        course=None, students__=None, teachers__=None, hod=None
    )
    assert isinstance(var_32, python_code_.Department)


def test_8():
    var_32 = python_code_.Department(
        course=None, students__=None, teachers__=None, hod=None, employee6=set()
    )
    assert isinstance(var_32, python_code_.Department)


def test_9():
    var_0 = python_code_.Employee_Interface()
    var_20 = python_code_.Department(
        course=None, students__=None, teachers__=var_0, hod=None, course0=None
    )
    assert isinstance(var_20, python_code_.Department)


def test_10():
    var_11 = python_code_.HOD()
    var_8 = python_code_.Department(
        course=[],
        students__=complex(-2112.28, 3105.2358),
        teachers__={"student9", -31.11, 'dU*r;.=">xrF0#*\x0bi'},
        hod=var_11,
        course0=b"|'\xe0\xe6>",
    )
    assert var_8.course0 == b"|'\xe0\xe6>"


def test_11():
    var_0 = python_code_.Employee_Interface()
    var_20 = python_code_.Department(
        course=var_0,
        students__=var_0,
        teachers__=None,
        hod=None,
        student4={var_0, -1860, var_0},
        access_Information19=var_0,
    )
    assert isinstance(var_20, python_code_.Department)


def test_12():
    python_code_.Student(Name=False, ID=1694.72)


def test_13():
    var_0 = python_code_.Course(subjects__=None, duration="k>d]3Oq_X4[h.lZV6")
    assert isinstance(var_0, python_code_.Course)
    python_code_.Student(Name=var_0, ID=var_0, admin13=var_0)


def test_14():
    var_18 = python_code_.Teacher()
    var_19 = set
    var_20 = python_code_.HOD()
    var_21 = python_code_.Access_Information()
    var_22 = python_code_.Department(
        course=var_18,
        students__=var_19,
        teachers__=var_19,
        hod=var_20,
        course0=["%~rJV\t'z~8", False],
        student4='b*{1GM":~f|sb6r',
        access_Information19=var_21,
    )
    assert var_22.course0 == ["%~rJV\t'z~8", False]
    var_23 = python_code_.Student(
        Name=var_18, ID={-963.6, True, -2221.82}, department5=var_22
    )
    assert isinstance(var_23, python_code_.Student)
    var_24 = {var_23}
    var_16 = python_code_.Department(
        course="department7",
        students__="O",
        teachers__=var_18,
        hod=var_18,
        student4=var_24,
    )
    assert isinstance(var_16, python_code_.Department)


def test_15():
    var_15 = lambda *args, **kwargs: "X"
    python_code_.Student(
        Name="|,`0JYrX~-6a6", ID="I)N'sp u\x0bwy\"", department5=var_15, admin13=var_15
    )


def test_16():
    var_0 = python_code_.Employee_Interface()
    python_code_.Student(
        Name=var_0, ID=complex(-3100.7613062, -2884.3), Having_Attendance8=var_0
    )


def test_17():
    python_code_.subject(subjectid="37/lO", subjectName="sgDZ")


def test_18():
    var_11 = lambda *args, **kwargs: "vk6"
    var_12 = python_code_.Department(
        course=var_11, students__=var_11, teachers__=1214, hod=var_11
    )
    assert isinstance(var_12, python_code_.Department)
    var_20 = "_Subject__course3"
    python_code_.department(id=var_20, name=var_20, director=var_11, address=b"\xbe")


def test_19():
    var_0 = python_code_.Course(subjects__=0, duration=set())
    assert isinstance(var_0, python_code_.Course)
    var_4 = "Admin-student4-_Subject__course3-Department"
    python_code_.students(
        name=var_4,
        gender=var_4,
        birthdate=b"\x8a\x9bB\xb5\x0c]*",
        address=var_4,
        id=var_0,
    )


def test_20():
    var_0 = python_code_.Course(
        subjects__=None, duration="department5:Subject:Department", subject2=set()
    )
    assert isinstance(var_0, python_code_.Course)
    var_1 = python_code_.Subject(name="{X9_\x0c4qG'+\x0ceDK", course3=var_0)
    assert isinstance(var_1, python_code_.Subject)


def test_21():
    var_0 = python_code_.Course(
        subjects__=None, duration="G.o i+m\rjyy", department1=None, subject2=set()
    )
    assert isinstance(var_0, python_code_.Course)
    var_2 = "_Course__subject2"
    var_3 = lambda *args, **kwargs: -3032
    python_code_.subject(subjectid=var_2, subjectName=var_3)
    var_5 = "wn}Y7D7"
    var_6 = python_code_.HOD()
    var_7 = python_code_.Access_Information()
    var_8 = python_code_.Department(
        course=var_0,
        students__=b"\x13~u\x88",
        teachers__=b";\x8eW\xd33",
        hod=var_6,
        access_Information19=var_7,
    )
    assert isinstance(var_8, python_code_.Department)
    var_9 = python_code_.Student(Name=var_3, ID=(2602, -1496.76), department5=var_8)
    assert isinstance(var_9, python_code_.Student)
    var_10 = {var_9, var_9, var_9, var_9, var_9}
    var_11 = python_code_.Department(
        course=var_2,
        students__=var_5,
        teachers__=var_3,
        hod=var_6,
        course0=-1401.91,
        student4=var_10,
    )
    assert var_11.course0 == pytest.approx(-1401.91, abs=0.01, rel=0.01)
    var_15 = python_code_.Department(
        course=var_2,
        students__=None,
        teachers__=var_2,
        hod=None,
        employee6={var_2, -1665, var_2},
    )
    assert isinstance(var_15, python_code_.Department)


@pytest.mark.xfail(strict=True)
def test_22():
    var_1 = "A6lW/~[."
    var_2 = python_code_.HOD()
    var_3 = tuple
    var_4 = python_code_.Access_Information()
    var_5 = python_code_.Student(
        Name=var_3, ID=1260.62, department5=var_1, Having_Attendance8=var_4
    )
    assert isinstance(var_5, python_code_.Student)
    var_6 = {var_5, var_5, var_5, var_5}
    var_7 = python_code_.Department(
        course=var_1, students__=var_1, teachers__=set(), hod=var_2, student4=var_6
    )
    assert isinstance(var_7, python_code_.Department)
    python_code_.Course(subjects__=(), duration=var_1, department1=var_7)


@pytest.mark.xfail(strict=True)
def test_23():
    var_8 = python_code_.Student(
        Name="\nO,6}",
        ID="subject2 Employee_Interface Access_Information _Department__student4",
        Having_Attendance8=None,
    )
    var_9 = "q.:"
    var_10 = python_code_.Course(subjects__=var_8, duration=var_9, department1=-1.42)
    assert isinstance(var_10, python_code_.Course)
    python_code_.Department(
        course=var_8,
        students__=var_8,
        teachers__=complex(-1202.3, -439.7766),
        hod=complex(4132.0, 324.62475),
        course0=var_10,
        student4=var_9,
    )


def test_24():
    var_0 = b"\x19\x1bDV5\x04\x97R\x82"
    var_11 = python_code_.Subject(name="{X9_\x0c4qG'+\x0ceDK", course3=var_0)
    assert isinstance(var_11, python_code_.Subject)
    var_12 = "Sujec"
    var_13 = {var_11, var_11, var_0}
    var_14 = python_code_.Course(
        subjects__=var_11, duration=var_12, department1=var_11, subject2=var_13
    )
    assert isinstance(var_14, python_code_.Course)


@pytest.mark.xfail(strict=True)
def test_25():
    var_11 = python_code_.Subject(name="y19;ZZ,<My}&.aKVL7&")
    var_12 = "E3\x0bQ"
    var_13 = python_code_.Student(Name=var_12, ID=577.8)
    var_14 = python_code_.Teacher()
    var_15 = python_code_.HOD()
    var_16 = hash
    var_17 = python_code_.Access_Information()
    var_18 = python_code_.Department(
        course=var_11,
        students__=var_13,
        teachers__=var_14,
        hod=var_15,
        course0=var_16,
        access_Information19=var_17,
    )
    assert isinstance(var_18, python_code_.Department)
    python_code_.Course(subjects__=var_11, duration=var_12, department1=var_18)
    assert isinstance(var_18.course0, python_code_.Course)


def test_26():
    var_4 = list
    var_6 = python_code_.Teacher()
    var_7 = '?Vj["rP9'
    var_8 = python_code_.Course(
        subjects__=var_4, duration=var_7, subject2=b"\x1e\xf9\xc8k"
    )
    assert isinstance(var_8, python_code_.Course)
    var_9 = python_code_.Subject(name=var_6, course3=var_8)
    assert isinstance(var_9, python_code_.Subject)
