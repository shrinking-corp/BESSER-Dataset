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
    Contexte,
    JArray,
    JBool,
    JMember,
    JNull,
    JNum,
    JObject,
    JStr,
    JValueJSONPrintVisitor,
    JValueVisitor_Interface,
    JValue_Interface,
    Protraction,
    Retraction,
    State_Interface,
    Wait,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_30 = python_code_.JArray(value="\x0b)yz|", value4=set())
    assert isinstance(var_30, python_code_.JArray)


def test_1():
    var_30 = python_code_.JArray(value="JObject._JMember__JObject_JMember_11.jMember3")
    assert isinstance(var_30, python_code_.JArray)


def test_2():
    python_code_.JMember(nom="4HL\x0bE]-8", jValue2=None)


def test_3():
    var_34 = python_code_.JMember(nom=91.12, jValue2=())
    assert isinstance(var_34, python_code_.JMember)


def test_4():
    var_34 = python_code_.JMember(nom=(), JObject_JMember_11='M@Z[TBO"#hl/!')
    assert isinstance(var_34, python_code_.JMember)


def test_5():
    python_code_.JNull(value=-569)


def test_6():
    python_code_.JStr(value="^nB`V9URa.q_rAM5hs")


def test_7():
    python_code_.JNum(value=-457)


def test_8():
    python_code_.JBool(value=False)
