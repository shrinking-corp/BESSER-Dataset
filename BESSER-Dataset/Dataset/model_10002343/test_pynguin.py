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
    Account,
    Customer,
    Item,
    Order,
    Shopping_Cart,
    annotations,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_1 = 2206.37
    var_2 = "8+&m3E!u9kV`<.8]"
    var_3 = 1923
    var_4 = python_code_.Account(Username=var_2, Password=var_3, post2="9L@v")
    assert isinstance(var_4, python_code_.Account)
    python_code_.Item(productId={450, 2, -19.5}, price=var_1, colour=var_2, user5=var_4)


def test_1():
    python_code_.Item(
        productId="orders7.myprofile0",
        price=-3034.45,
        colour="_Account__login4,_Shopping_Cart__orders7,Shopping_Cart",
    )


def test_2():
    var_0 = lambda *args, **kwargs: [-1, 254.58]
    python_code_.Item(
        productId="# '^V0LmK-yR", price=450.39, colour="(dpDq4\r5#Wu", user5=var_0
    )
    var_2 = abs
    var_3 = python_code_.Account(Username=b"\xa2`\x9e[\xbaf", Password=var_2)
    assert isinstance(var_3, python_code_.Account)
    var_5 = -295
    var_6 = python_code_.Order(quantity=var_5, price=[], user3=var_0)
    assert isinstance(var_6, python_code_.Order)


def test_3():
    var_0 = python_code_.Shopping_Cart(cartId="0(jb!\tC_zdx#lUa|P")
    assert isinstance(var_0, python_code_.Shopping_Cart)
    var_25 = python_code_.Item(
        productId="_Item__user5",
        price=-4453.25,
        colour="+T!o.\n-yVv8jWh-Z}yG",
        user5=var_0,
        Shopping_Cart_Login_19=var_0,
    )
    assert isinstance(var_25.user5, python_code_.Shopping_Cart)
    var_29 = {var_25, -2136.77}
    var_30 = python_code_.Shopping_Cart(
        cartId=complex(1271.43, -3731.1), Shopping_Cart_Login_08=var_29
    )
    assert isinstance(var_30, python_code_.Shopping_Cart)


def test_4():
    var_0 = python_code_.Shopping_Cart(cartId="0(jb!\tC_zdx#lUa|P")
    assert isinstance(var_0, python_code_.Shopping_Cart)
    var_25 = python_code_.Item(
        productId="_Item__user5",
        price=-4453.25,
        colour="+T!o.\n-yVv8jWh-Z}yG",
        user5=var_0,
        Shopping_Cart_Login_19=var_0,
    )
    assert isinstance(var_25.user5, python_code_.Shopping_Cart)


def test_5():
    var_25 = python_code_.Shopping_Cart(
        cartId="_Account__post2,friend6,_Order__friend6,Shopping_Cart_Login_08",
        Shopping_Cart_Login_08={True},
    )
    assert isinstance(var_25, python_code_.Shopping_Cart)


def test_6():
    var_11 = python_code_.Shopping_Cart(cartId="\\URBOg")
    assert isinstance(var_11, python_code_.Shopping_Cart)


def test_7():
    var_11 = python_code_.Shopping_Cart(cartId="\\URBOg")
    assert isinstance(var_11, python_code_.Shopping_Cart)
    var_13 = 0
    var_14 = python_code_.Order(
        quantity=var_13, price=None, friend6={var_11, -1, 1103.23}
    )
    assert isinstance(var_14, python_code_.Order)
    var_15 = lambda *args, **kwargs: "G^T?$9u\t'j(8iLt"
    var_16 = {var_11}
    python_code_.Order(quantity=var_15, price=False, friend6=var_16)


def test_8():
    var_51 = "usr3"
    var_58 = python_code_.Shopping_Cart(cartId=var_51, orders7=True)
    assert isinstance(var_58, python_code_.Shopping_Cart)


def test_9():
    var_25 = python_code_.Order(quantity=-2705, price=None, friend6=set(), user3=None)
    assert isinstance(var_25, python_code_.Order)


def test_10():
    var_25 = python_code_.Order(quantity=-729, price=None, user3=None)
    assert isinstance(var_25, python_code_.Order)


def test_11():
    var_0 = -39.68
    var_9 = python_code_.Order(quantity=2, price=var_0, user3=var_0)
    assert isinstance(var_9, python_code_.Order)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.Customer
    var_1 = python_code_.Account(Username=var_0, Password=())
    assert isinstance(var_1, python_code_.Account)
    var_6 = "Shopping_Cart,_Accoun=__post2"
    python_code_.Customer(
        name=var_6, emailAddress=var_0, DOB=True, cellNo="5", Gender=var_6, user1=var_1
    )


def test_13():
    var_0 = python_code_.Shopping_Cart(cartId="0(jb!\tC_zdx#lUa|P")
    assert isinstance(var_0, python_code_.Shopping_Cart)
    var_25 = python_code_.Item(
        productId="_Item__user5",
        price=-4453.25,
        colour="+T!o.\n-yVv8jWh-Z}yG",
        user5=var_0,
        Shopping_Cart_Login_19=var_0,
    )
    assert isinstance(var_25.user5, python_code_.Shopping_Cart)
    var_29 = {var_25, -2136.77}
    var_30 = python_code_.Shopping_Cart(
        cartId=complex(1271.43, -3731.1), Shopping_Cart_Login_08=var_29
    )
    assert isinstance(var_30, python_code_.Shopping_Cart)
    var_31 = "user3"
    python_code_.Customer(
        name=var_31, emailAddress=var_25, DOB=var_25, cellNo=var_29, Gender=var_30
    )


def test_14():
    var_0 = lambda *args, **kwargs: [-1, 254.58]
    var_1 = python_code_.Item(
        productId=var_0, price=var_0, colour=var_0, Shopping_Cart_Login_19=var_0
    )
    var_2 = abs
    var_3 = python_code_.Account(Username=b"\xa2`\x9e[\xbaf", Password=var_2)
    assert isinstance(var_3, python_code_.Account)
    var_4 = python_code_.Item(
        productId="_Item__user5",
        price=8.38,
        colour="Shopping_Cart_Login_19-post2",
        user5=None,
    )
    var_5 = -295
    var_6 = python_code_.Order(quantity=var_5, price=[], user3=var_0)
    assert isinstance(var_6, python_code_.Order)
    var_7 = 'g"|y4*.!fr'
    var_10 = "N"
    python_code_.Customer(
        name=complex(1371.95, 632.0244),
        emailAddress=1123.58,
        DOB=var_7,
        cellNo="1'Nh!m?l*d{+*hN?oX",
        Gender=var_10,
        user1=var_6,
    )
    var_12 = {var_1, var_4, var_1, var_1}
    var_13 = python_code_.Shopping_Cart(
        cartId=[], orders7=var_6, Shopping_Cart_Login_08=var_12
    )
    assert isinstance(var_13, python_code_.Shopping_Cart)


def test_15():
    var_25 = python_code_.Account(
        Username='0%X\r",o\\cvwZMh', Password=-848, post2=set()
    )
    assert isinstance(var_25, python_code_.Account)


def test_16():
    var_25 = python_code_.Account(Username="_Account__post2", Password=78, login4=None)
    assert isinstance(var_25, python_code_.Account)


def test_17():
    var_27 = -1660
    var_28 = python_code_.Order(
        quantity=var_27, price=(), user3=[-775.05, True, 1877.31]
    )
    assert isinstance(var_28, python_code_.Order)
    var_29 = {var_28, var_28, var_28}
    var_30 = python_code_.Account(
        Username="FQ", Password=var_27, myprofile0="_Customer__user1", post2=var_29
    )
    assert isinstance(var_30, python_code_.Account)


def test_18():
    var_0 = str
    var_1 = python_code_.Account(Username=";2+6E", Password=var_0, login4=var_0)
    assert isinstance(var_1, python_code_.Account)


def test_19():
    var_0 = python_code_.Shopping_Cart(cartId="$83", orders7=None)
    assert isinstance(var_0, python_code_.Shopping_Cart)
    var_20 = 0
    var_21 = python_code_.Order(
        quantity=var_20, price=None, friend6={var_0, -1, 1103.23}
    )
    assert isinstance(var_21, python_code_.Order)


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = "Ck{n}\t=1MkP"
    var_1 = -925.2
    var_2 = python_code_.Customer(
        name=var_0,
        emailAddress=var_0,
        DOB=var_0,
        cellNo=var_1,
        Gender=var_1,
        user1=var_0,
    )
    assert isinstance(var_2, python_code_.Customer)
    var_3 = "myprofile0"
    var_4 = lambda *args, **kwargs: []
    var_5 = python_code_.Item(productId=var_0, price=var_1, colour=var_3, user5=var_4)
    var_6 = "user1"
    var_7 = python_code_.Shopping_Cart(cartId=var_6, orders7={"xyt9[~U/x@qh6.Jk": 143})
    assert isinstance(var_7, python_code_.Shopping_Cart)
    var_8 = {var_7, var_7}
    var_9 = python_code_.Order(quantity=True, price=var_4, friend6=var_8)
    assert isinstance(var_9, python_code_.Order)
    var_10 = -2479
    python_code_.Account(Username=None, Password=var_10, login4=var_5)
    assert isinstance(var_5.user5, python_code_.Account)


def test_21():
    var_0 = lambda *args, **kwargs: [-1, 254.58]
    python_code_.Item(
        productId=var_0, price=var_0, colour=var_0, Shopping_Cart_Login_19=var_0
    )


def test_22():
    var_0 = lambda *args, **kwargs: [-1, 254.58]
    var_1 = python_code_.Item(
        productId=var_0, price=var_0, colour=var_0, Shopping_Cart_Login_19=var_0
    )
    var_51 = tuple
    var_58 = "user1"
    var_59 = python_code_.Shopping_Cart(
        cartId=var_58, orders7=var_1, Shopping_Cart_Login_08={-1278.58, var_58}
    )
    assert isinstance(var_59, python_code_.Shopping_Cart)
    var_60 = {var_59, var_59}
    var_61 = python_code_.Order(quantity=True, price=var_0, friend6=var_60)
    assert isinstance(var_61, python_code_.Order)
    var_63 = -295
    var_73 = "pU]x7R\nd"
    python_code_.Customer(
        name=var_73, emailAddress=var_73, DOB=var_51, cellNo=var_73, Gender=var_73
    )
    var_77 = python_code_.Order(quantity=var_60, price=var_61, user3=var_63)
    assert isinstance(var_77, python_code_.Order)


def test_23():
    var_0 = -852.24
    var_1 = ""
    var_2 = python_code_.Item(productId=set(), price=var_0, colour=var_1)
    var_3 = python_code_.Order(quantity={}, price=var_2)
    assert isinstance(var_3, python_code_.Order)
    var_4 = "|F!nOC"
    python_code_.Customer(
        name=-658.53, emailAddress=var_1, DOB=var_4, cellNo=var_0, Gender=var_1
    )
    var_8 = -288
    var_9 = python_code_.Account(
        Username=complex(1282.347, -187.2), Password=var_8, login4=[]
    )
    assert isinstance(var_9, python_code_.Account)


def test_24():
    var_21 = sorted
    var_22 = "user3"
    var_23 = 1
    var_24 = 1202
    var_25 = 681.19
    var_26 = python_code_.Item(
        productId=complex(256.3931728, -1900.8),
        price=var_25,
        colour=var_22,
        Shopping_Cart_Login_19=var_22,
    )
    assert isinstance(var_26, python_code_.Item)
    var_27 = python_code_.Order(
        quantity=var_24,
        price=var_26,
        friend6={
            '?UQL-@"': "user1-Shopping_Cart-_Account__post2",
            "&\x0clxS3ix0TN|U": True,
        },
    )
    assert isinstance(var_27, python_code_.Order)
    var_28 = {var_27, var_27, var_27, var_27}
    var_29 = python_code_.Account(Username=var_22, Password=var_23, post2=var_28)
    assert isinstance(var_29, python_code_.Account)
    var_30 = python_code_.Account(Username=var_22, Password=var_21, post2=var_28)
    assert isinstance(var_30, python_code_.Account)
    var_31 = python_code_.Account(
        Username=["_Account__myprofile0,Item,login4,Shopping_Cart_Login_08"],
        Password="orders7",
        login4=var_21,
    )
    assert isinstance(var_31, python_code_.Account)


def test_25():
    var_0 = "Ck{n}\t=1MkP"
    python_code_.Customer(
        name=var_0,
        emailAddress="Shopping_Cart_Login_08",
        DOB="Qmo",
        cellNo=-6018.47,
        Gender=var_0,
    )
    var_51 = "//*/l#m%-%J|5S/LH>"
    var_53 = lambda *args, **kwargs: [
        "_Shopping_Cart__orders7.Shopping_Cart.Customer",
        926,
    ]
    var_55 = "user3"
    var_56 = 1
    var_57 = 1202
    var_58 = 681.19
    var_59 = python_code_.Item(
        productId=complex(256.3931728, -1900.8),
        price=var_58,
        colour=var_51,
        Shopping_Cart_Login_19=var_0,
    )
    assert isinstance(var_59, python_code_.Item)
    var_60 = python_code_.Order(
        quantity=var_57,
        price=var_59,
        friend6={
            '?UQL-@"': "user1-Shopping_Cart-_Account__post2",
            "&\x0clxS3ix0TN|U": True,
        },
    )
    assert isinstance(var_60, python_code_.Order)
    var_61 = {var_60, var_60, var_60, var_60}
    var_62 = python_code_.Account(Username=var_55, Password=var_56, post2=var_61)
    assert isinstance(var_62, python_code_.Account)
    var_64 = python_code_.Account(Username=(True,), Password=var_57, login4={})
    assert isinstance(var_64, python_code_.Account)
    var_65 = python_code_.Shopping_Cart(cartId=var_53, orders7=var_60)
    assert isinstance(var_65, python_code_.Shopping_Cart)


@pytest.mark.xfail(strict=True)
def test_26():
    var_0 = -39.68
    var_3 = lambda *args, **kwargs: -3385
    var_4 = -142.45
    var_5 = "orders7"
    var_6 = python_code_.Shopping_Cart(cartId=var_5)
    assert isinstance(var_6, python_code_.Shopping_Cart)
    var_7 = python_code_.Item(
        productId=["wvCK"], price=var_4, colour=var_0, Shopping_Cart_Login_19=var_6
    )
    assert isinstance(var_7, python_code_.Item)
    var_8 = 2
    var_9 = "P|k=4*Y@R/\r,fL:/(^"
    var_10 = python_code_.Customer(
        name="`WHJ'f>\ty",
        emailAddress="CJ`@EW<?sY",
        DOB=var_9,
        cellNo=set(),
        Gender=var_3,
        user1=var_3,
    )
    python_code_.Account(Username=var_5, Password=var_8, myprofile0=var_10, post2=var_4)


@pytest.mark.xfail(strict=True)
def test_27():
    var_3 = lambda *args, **kwargs: -3385
    var_5 = "orders7"
    var_6 = python_code_.Shopping_Cart(cartId=var_5)
    assert isinstance(var_6, python_code_.Shopping_Cart)
    var_8 = "login4,Shopping_Cart_Login_08,Order,post2"
    var_10 = "user3"
    var_11 = python_code_.Account(
        Username=var_8, Password=var_8, myprofile0={'"T&\x0bB`/mn\n#': False}
    )
    assert isinstance(var_11, python_code_.Account)
    python_code_.Customer(
        name=var_5,
        emailAddress=var_3,
        DOB=-2832.74,
        cellNo=var_6,
        Gender=var_10,
        user1=var_11,
    )
