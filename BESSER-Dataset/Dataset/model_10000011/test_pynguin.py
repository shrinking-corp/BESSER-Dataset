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
    Camera_sensor,
    Event_Log,
    Home_Security,
    Light_Sensor,
    Lock_doors_sensors,
    Server,
    Temperature_sensor,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.Temperature_sensor(attribute="GO]GLW")


def test_1():
    var_13 = python_code_.Temperature_sensor(attribute=-1790.42, home_Security11=2185.7)
    assert isinstance(var_13, python_code_.Temperature_sensor)


def test_2():
    python_code_.Server(attribute="^~T5xlxe", home_Security1=None)


def test_3():
    var_33 = python_code_.Server(attribute=[], home_Security1="")
    assert isinstance(var_33, python_code_.Server)


def test_4():
    python_code_.Lock_doors_sensors(attribute="DP\\")


def test_5():
    var_48 = python_code_.Lock_doors_sensors(
        attribute={"_Lock_doors_sensors__home_Security9": -2606}, home_Security9=()
    )
    assert isinstance(var_48, python_code_.Lock_doors_sensors)


def test_6():
    python_code_.Light_Sensor(attribute="iRi!|7S?m")


def test_7():
    var_43 = python_code_.Light_Sensor(attribute="FHDI", home_Security7=())
    assert isinstance(var_43, python_code_.Light_Sensor)


def test_8():
    python_code_.Event_Log(attribute="=![7\x0c1oD/LPF*5)")


def test_9():
    var_15 = python_code_.Event_Log(attribute=(4773, False), home_Security5=-1932.63)
    assert isinstance(var_15, python_code_.Event_Log)


def test_10():
    var_12 = python_code_.Camera_sensor(
        Image_ID=-692.78,
        Video_ID=(False, True),
        home_Security3={"d(AM3\rg[DvcI": "_Server__home_Security1"},
    )
    assert isinstance(var_12, python_code_.Camera_sensor)


def test_11():
    python_code_.Camera_sensor(Image_ID=-2438, Video_ID=853)
