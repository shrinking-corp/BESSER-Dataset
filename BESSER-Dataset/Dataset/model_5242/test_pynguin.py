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
    Car,
    Color,
    Enum,
    date,
    datetime,
    genericsGoCrazy_Car,
    genericsGoCrazy_Comp,
    genericsGoCrazy_MyClass,
    genericsGoCrazy_MySubClass,
    genericsGoCrazy_OtherClass,
    genericsGoCrazy_SubCar,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_4 = python_code_.Car()
    var_7 = "Xh"
    var_8 = python_code_.genericsGoCrazy_Car
    var_9 = python_code_.genericsGoCrazy_Car(
        name=var_7,
        fullName=b"\x84\xa9r3\x10\x93\xb64\xdeZv\xcb\xa9F\xa6\xb1\x16\xe7J",
        doors=var_8,
        color=var_8,
        genericsGoCrazy_Car0=(),
    )
    assert isinstance(var_9, python_code_.genericsGoCrazy_Car)
    python_code_.genericsGoCrazy_Car(
        name=var_4,
        fullName=var_7,
        doors=var_8,
        color="d",
        genericsGoCrazy_Car=var_9,
        genericsGoCrazy_Car0=var_9,
    )
    assert isinstance(var_9.genericsGoCrazy_Car0, python_code_.genericsGoCrazy_Car)


def test_1():
    python_code_.genericsGoCrazy_Car(
        name=b"\xaf-\xd5\x10\x06\xfd6\x04\xffAZ\x8d\xde\xc7Z\xb8\xf0t\x9c",
        fullName=False,
        doors=("6{Np<KHU+T3TM8", True, "i:"),
        color=complex(1683.2872, -1142.452727),
    )


def test_2():
    var_38 = python_code_.genericsGoCrazy_Car(
        name=False,
        fullName=False,
        doors=[],
        color=".6}*73\n1",
        genericsGoCrazy_Car=738.06,
    )
    assert isinstance(var_38, python_code_.genericsGoCrazy_Car)


def test_3():
    var_0 = sorted
    var_1 = "\n9qT"
    var_2 = python_code_.genericsGoCrazy_MyClass(
        a1=var_0, a2=var_0, a3=var_0, theEObject=var_1, aMap=var_1
    )
    var_2.bar(
        genericsGoCrazy_ts=None,
        genericsGoCrazy_aT=var_1,
        genericsGoCrazy_aF=("m\t\\\t'", True, True),
    )
    var_4 = "QJH"
    var_5 = python_code_.genericsGoCrazy_Car(
        name=var_4, fullName=var_1, doors=var_0, color=var_0
    )
    var_5.superFoo(genericsGoCrazy_key=-299.33)
    var_7 = python_code_.genericsGoCrazy_Comp()
    var_9 = "(bDD\\<(^kP4<uAL["
    var_10 = "genericsGoCrazy_Car.genericsGoCrazy_Car0.BLUE._genericsGoCrazy_Car__genericsGoCrazy_Car"
    var_11 = python_code_.genericsGoCrazy_Car(
        name=None, fullName=var_9, doors=var_4, color=var_10
    )
    var_11.enhancedFoo(genericsGoCrazy_aT=var_7, genericsGoCrazy_aInt=())


def test_4():
    python_code_.Car()


def test_5():
    var_2 = "C\\=]7"
    var_3 = 'yhN$Aod4pA\\B%"(A'
    var_4 = bool
    var_5 = "~U"
    var_6 = python_code_.genericsGoCrazy_MyClass(
        a1=var_2, a2=True, a3=var_3, theEObject=var_4, aMap=var_5
    )
    var_7 = "\\"
    var_8 = python_code_.genericsGoCrazy_Car(
        name=var_3, fullName=var_5, doors=var_7, color=var_2
    )
    var_8.foo(genericsGoCrazy_a=var_3)
    var_6.bar(
        genericsGoCrazy_ts=("$BJF\n\nG*o7\t[NDu66", 2691.4),
        genericsGoCrazy_aT=var_4,
        genericsGoCrazy_aF=var_3,
    )
    var_8.enhancedFoo(genericsGoCrazy_aT=var_8, genericsGoCrazy_aInt=None)


def test_6():
    python_code_.genericsGoCrazy_MyClass(
        a1="genericsGoCrazy_Car",
        a2="#W-G",
        a3="=^+\x0c5\t_",
        theEObject="+1<\x0b3",
        aMap="_",
    )


def test_7():
    var_0 = "genericsGoCrazy_Car0,genericsGoCrazy_Car0,_genericsGoCrazy_Car__genericsGoCrazy_Car,BLUE"
    var_1 = "h@Ww+TZ-"
    var_2 = "BLUE.BLUE.BLUE.genericsGoCrazy_Car"
    var_3 = python_code_.genericsGoCrazy_MyClass(
        a1=var_0, a2=var_1, a3=None, theEObject=var_0, aMap=var_2
    )
    var_3.bar(
        genericsGoCrazy_ts=var_3, genericsGoCrazy_aT=var_0, genericsGoCrazy_aF=None
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_4 = python_code_.Car()
    var_15 = "uHV<=@\x0b?1S\r>IE)g0J"
    var_16 = "BLUE _genericsGoCrazy_Car__genericsGoCrazy_Car0"
    var_17 = python_code_.genericsGoCrazy_Car(
        name=var_4,
        fullName=var_16,
        doors=True,
        color=var_16,
        genericsGoCrazy_Car=var_15,
    )
    assert isinstance(var_17, python_code_.genericsGoCrazy_Car)
    python_code_.genericsGoCrazy_Car(
        name={"Q\nf&z", 5964.13},
        fullName=var_15,
        doors=var_15,
        color=var_15,
        genericsGoCrazy_Car0=var_17,
    )
