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
    Admin,
    Customer,
    Login,
    ShoppingCart,
    annotations,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_32 = "<9nv=jCP&zX"
    var_33 = python_code_.Customer(
        name=var_32,
        email="d?QEE3Q",
        sem='MK`0"!"Iw/K',
        branch="Z[K|",
        password=var_32,
        phone=-524,
    )
    python_code_.Admin(email=var_32, password=var_32)
    var_37 = 0
    python_code_.ShoppingCart(
        cartID=var_37,
        productID=var_37,
        quantity=var_37,
        dateAdded="Customer",
        Customer_ShoppingCart_11=var_33,
    )


def test_1():
    python_code_.ShoppingCart(
        cartID=[], productID=(449.33,), quantity=None, dateAdded={}
    )


def test_2():
    python_code_.Login(
        email="_ShoppingCart__Customer_ShoppingCart_11ShoppingCart", password="m"
    )


def test_3():
    python_code_.Admin(email="7|!$", password="Customer")


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.Login(email=(), password=complex(-701.163, -921.43))
    var_1 = 1054
    var_2 = python_code_.ShoppingCart(
        cartID=set(),
        productID=var_0,
        quantity=var_1,
        dateAdded=complex(1074.90179, -1265.0),
    )
    var_3 = "A}t>NF"
    var_4 = python_code_.Admin(email=var_2, password=var_3)
    var_5 = bool
    var_6 = "H0:g?b!(\x0bg.Af4Nk4}3"
    python_code_.ShoppingCart(
        cartID=var_1,
        productID=var_4,
        quantity=var_5,
        dateAdded=var_6,
        Customer_ShoppingCart_11=var_4,
    )
    var_10 = -2031
    var_12 = 1402
    var_13 = "_ShoppingCart__Customer_ShoppingCart_11"
    var_14 = python_code_.Customer(
        name=var_4,
        email=var_10,
        sem=var_3,
        branch=var_13,
        password=3386,
        phone=-2501.95,
    )
    python_code_.ShoppingCart(
        cartID=var_12,
        productID=["-n75HQ)Z3C'", True, "cd0W/K[O<{|8$naI\n@"],
        quantity=var_4,
        dateAdded=var_13,
        Customer_ShoppingCart_11=var_14,
    )
    assert isinstance(var_14.Customer_ShoppingCart_00, python_code_.ShoppingCart)


@pytest.mark.xfail(strict=True)
def test_5():
    var_7 = hash
    var_8 = "iz"
    var_9 = 473
    var_11 = "_ShoppingCart__Customer_ShoppingCart_11"
    var_12 = "lS0GLU GzrUPiLb17"
    var_13 = "Qgw\tyJ2A>O[wcc"
    var_14 = 1016
    var_15 = python_code_.Customer(
        name="Customer",
        email=var_12,
        sem="R:0=L~]YE%C%1PLHh;",
        branch=var_13,
        password="_ShoppingCart__Customer_ShoppingCart_11",
        phone=var_14,
        Customer_ShoppingCart_00=var_11,
    )
    assert isinstance(var_15, python_code_.Customer)
    python_code_.ShoppingCart(
        cartID=var_7,
        productID=var_8,
        quantity=var_9,
        dateAdded=var_8,
        Customer_ShoppingCart_11=var_15,
    )
    assert isinstance(var_15.Customer_ShoppingCart_00, python_code_.ShoppingCart)


def test_6():
    var_0 = -424
    var_1 = python_code_.ShoppingCart(
        cartID={},
        productID="RR|",
        quantity=var_0,
        dateAdded=var_0,
        Customer_ShoppingCart_11={
            "\x0bO_ rFoY'It,#/7.Di?": 1,
            "#": "@v$\x0cpY(y+",
            "Customer_ShoppingCart_00": -616.53,
        },
    )
    assert isinstance(var_1, python_code_.ShoppingCart)
    var_2 = "+1Kp_Y"
    var_3 = "_Customer__Customer_ShoppingCart_00:ShoppingCart"
    var_4 = python_code_.Login(email=var_2, password=var_3)
    var_5 = lambda *args, **kwargs: []
    var_6 = -306
    python_code_.Customer(
        name=var_5, email=var_4, sem=var_5, branch=var_3, password=var_4, phone=var_6
    )
