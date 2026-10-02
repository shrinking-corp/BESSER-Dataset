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
    AnswerdBuilder,
    Answers,
    Choices,
    ConcreteOtherAnswers,
    ConcreteRightAnswers,
    Enum,
    MCRightAnswer,
    MultipleChoicesAnswers,
    NuRightAnswer,
    NumericAnswers,
    OtherAnswer,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.AnswerdBuilder(login="customer0", password="~b)>[ac", state=None)


@pytest.mark.xfail(strict=True)
def test_1():
    var_8 = python_code_.MultipleChoicesAnswers
    var_9 = python_code_.ConcreteOtherAnswers(
        billingAddress="g_Qggs=M",
        open=None,
        closed=None,
        isClosed=True,
        customer3=var_8,
    )
    var_16 = "7W"
    python_code_.AnswerdBuilder(
        login=var_16, password=var_16, state=var_9, customer0=False, account2=var_9
    )


def test_2():
    python_code_.ConcreteOtherAnswers(
        billingAddress="fF\nL", open=None, closed=None, isClosed=True
    )


def test_3():
    python_code_.ConcreteRightAnswers(
        address={
            "_ConcreteRightAnswers__webUser1:_AnswerdBuilder__customer0:customer0:webUser1": -474.27,
            'F>9|1Teu"\tl3': True,
        },
        phone=None,
        email=b"\xb0\x0c$\xfeU\xd5\x10\xd6\xa4\x8f\x95B\x94",
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_1 = "ConcreteOtherAnswers:_AnswerdBuilder__~ccount2:_AnswerdBuilder__account2:_AnswerdBuilder__account2"
    var_6 = python_code_.ConcreteRightAnswers(
        address=var_1, phone=-3239.12, email=var_1
    )
    var_7 = "_ConcreteRightAnswers__webUser1 _ConcreteOtherAnswers__customer3 _ConcreteRightAnswers__webUser1 customer3"
    var_8 = python_code_.NuRightAnswer
    python_code_.ConcreteOtherAnswers(
        billingAddress=var_7, open=('"6(',), closed=var_8, isClosed=None
    )
    python_code_.Choices(creationDate=None)
    var_11 = "AnswerdBuilder:ConcreteOtherAnswers"
    python_code_.NumericAnswers(name=-1010, description=var_11)
    python_code_.AnswerdBuilder(
        login=var_8, password=var_11, state=var_1, customer0=var_6, account2=None
    )


def test_5():
    python_code_.NumericAnswers(
        name=b"<\xa7\xce\xd2\xa7\xa7\xe9\x1a\xd3", description=True
    )


def test_6():
    python_code_.Choices(creationDate=None)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.AnswerdBuilder(
        login=4133, password=-3866, state=-674.67, customer0=(1097.78, ']RviD5L"-Qug')
    )
    assert isinstance(var_0, python_code_.AnswerdBuilder)
    var_1 = bool
    python_code_.Choices(creationDate=var_1)
    var_38 = ""
    var_39 = "customer0,customer0,webUser1"
    var_40 = python_code_.ConcreteRightAnswers(
        address=var_39, phone=None, email=var_38, webUser1=3
    )
    assert isinstance(var_40, python_code_.ConcreteRightAnswers)
    python_code_.ConcreteRightAnswers(
        address=var_39, phone=var_38, email="AOCE", webUser1=var_0
    )


def test_8():
    python_code_.MultipleChoicesAnswers(
        number=[True, -2565.68],
        ordered=set(),
        shipped=None,
        shipTo=-138.76,
        total=b"~\xf5*\x9b\xa8&\xf2-\x8c\x15\x83R",
        status=None,
    )


def test_9():
    python_code_.Answers(paidDate=None, total=-1015.56, details=").huJ1kc\tO+a}\x0by\\")


def test_10():
    python_code_.MCRightAnswer(quantity=2838, price=-2771.03)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = python_code_.AnswerdBuilder(
        login=4133, password=-3866, state=-674.67, customer0=(1097.78, ']RviD5L"-Qug')
    )
    assert isinstance(var_0, python_code_.AnswerdBuilder)
    var_38 = ""
    var_39 = "customer0,customer0,webUser1"
    var_40 = python_code_.ConcreteRightAnswers(
        address=var_39, phone=None, email=var_38, webUser1=3
    )
    assert isinstance(var_40, python_code_.ConcreteRightAnswers)
    python_code_.AnswerdBuilder(
        login=var_38, password=True, state=var_38, customer0=var_40
    )


def test_12():
    var_0 = python_code_.AnswerdBuilder(
        login="\x0c`h1mB,?o9v",
        password="_AnswerdBuilder__account2",
        state=None,
        customer0=None,
        account2=None,
    )
    var_42 = python_code_.Choices
    var_43 = python_code_.AnswerdBuilder(
        login=var_0,
        password=var_42,
        state=b"\xa8\xf5\xc5\xc9\r\x00\xac\xd1\xd7b\x10\xed7\x1dv\xa2\xed",
        account2=-594.18,
    )
    assert isinstance(var_43, python_code_.AnswerdBuilder)


def test_13():
    var_8 = python_code_.MultipleChoicesAnswers
    python_code_.ConcreteOtherAnswers(
        billingAddress="g_Qggs=M",
        open=None,
        closed=None,
        isClosed=True,
        customer3=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = python_code_.AnswerdBuilder(
        login="_ConcreteRightAnswers__webUser1",
        password="'WAg]\"3\rAD\x0b.Z\\+q=\x0c",
        state=None,
        customer0=None,
    )
    python_code_.ConcreteOtherAnswers(
        billingAddress=complex(149.9018703, 1391.4883),
        open=-1413,
        closed=2646.9,
        isClosed=var_0,
        customer3=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_15():
    var_43 = 2123.1986548744717
    var_45 = "R+"
    var_47 = python_code_.ConcreteOtherAnswers(
        billingAddress=var_45,
        open=var_45,
        closed=var_45,
        isClosed=False,
        customer3=var_43,
    )
    assert isinstance(var_47, python_code_.ConcreteOtherAnswers)
    python_code_.AnswerdBuilder(
        login=var_45,
        password=b"M\xe5\x0f\xb8'\x84\x1a\xde\x02\x8e\xdd:V\x96q",
        state=None,
        account2=var_47,
    )
