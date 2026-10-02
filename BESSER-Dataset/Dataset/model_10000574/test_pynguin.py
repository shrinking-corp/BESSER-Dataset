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
    Admin_Actor,
    AjoutProduit_UseCase,
    Customer,
    Enum,
    LineItem,
    MyActor_Actor,
    MyClass2,
    Order,
    Payment,
    Product,
    ShoppinCart,
    WebUser,
    Webuser_Actor,
    annotations,
    date,
    datetime,
    mypackage2_OrderStatus,
    mypackage_UserState,
    time,
)


def test_0():
    var_9 = python_code_.Product(
        name="~|c", description="hy:*RtrEAH\\k~S0k]B", item12={387.21}
    )
    assert isinstance(var_9, python_code_.Product)


def test_1():
    var_9 = python_code_.Product(name="Productorder2", description="&N&1b1&")
    assert isinstance(var_9, python_code_.Product)


def test_2():
    var_17 = python_code_.LineItem(
        quantity=-2873,
        price=-5013.32,
        product13=None,
        lineitem15={"order2", 1765, True},
    )
    assert isinstance(var_17, python_code_.LineItem)


def test_3():
    var_17 = python_code_.LineItem(quantity=-653, price=2435.85)
    assert isinstance(var_17, python_code_.LineItem)


def test_4():
    var_17 = python_code_.Admin_Actor()
    var_24 = -2344.5449600620504
    var_25 = python_code_.LineItem(
        quantity=-388, price=var_24, product13=var_17, sc19=var_17
    )
    assert isinstance(var_25, python_code_.LineItem)


def test_5():
    var_12 = python_code_.Payment
    var_21 = python_code_.LineItem(
        quantity=-1899, price=-1553.52, product13=None, sc19=var_12
    )
    assert isinstance(var_21, python_code_.LineItem)


def test_6():
    var_18 = python_code_.WebUser(
        login=True, password=[], state={False, "7"}, customer6=()
    )
    assert isinstance(var_18, python_code_.WebUser)


@pytest.mark.xfail(strict=True)
def test_7():
    var_11 = 0
    var_13 = lambda *args, **kwargs: "d\nzE"
    var_14 = python_code_.Customer(
        address=complex(-166.689, 2919.857414), phone={}, email=var_13
    )
    python_code_.WebUser(login=var_13, password=var_11, state=None, customer6=var_14)


@pytest.mark.xfail(strict=True)
def test_8():
    var_18 = python_code_.Order(
        number=-1438,
        ordered=None,
        shipped=True,
        shipTo="_ShoppinCart__items18",
        total=-45.77,
        status=None,
        account5=None,
    )
    assert isinstance(var_18, python_code_.Order)
    var_19 = python_code_.Webuser_Actor()
    var_20 = python_code_.ShoppinCart(creationDate=var_19, webuser8=[])
    assert isinstance(var_20, python_code_.ShoppinCart)
    python_code_.WebUser(login=1080.88, password=[], state=var_18, shoppincart9=var_20)


def test_9():
    var_12 = "items18,_LineItem__sc19,items18,account17"
    var_13 = python_code_.WebUser(
        login=1222.59, password=var_12, state=-4059, shoppincart9=[1316.01]
    )
    assert isinstance(var_13, python_code_.WebUser)
    var_14 = 1275.1
    var_15 = -1
    var_19 = python_code_.Order(
        number=var_15,
        ordered=None,
        shipped=False,
        shipTo="_Account__payment0items14webuser7",
        total=var_14,
        status=var_14,
        account5=None,
    )
    assert isinstance(var_19, python_code_.Order)
    var_20 = python_code_.Payment(
        paidDate=var_12, total=var_14, details=var_12, order2=var_19
    )
    assert isinstance(var_20, python_code_.Payment)


def test_10():
    var_8 = python_code_.Webuser_Actor()
    var_11 = python_code_.Account(
        billingAddress="webuser7",
        open=None,
        closed=var_8,
        isClosed=False,
        payment0={False, var_8, -2976.24},
    )
    assert isinstance(var_11, python_code_.Account)


def test_11():
    var_11 = python_code_.Account(
        billingAddress='`xW[jt,I]1it"x',
        open=None,
        closed=None,
        isClosed=False,
        order4={4903.6},
        customer11=None,
    )
    assert isinstance(var_11, python_code_.Account)


def test_12():
    var_9 = python_code_.Product(
        name="~|c", description="hy:*RtrEAH\\k~S0k]B", item12={387.21}
    )
    assert isinstance(var_9, python_code_.Product)
    var_10 = python_code_.ShoppinCart(creationDate=-300.27, webuser8=var_9)
    assert isinstance(var_10, python_code_.ShoppinCart)


def test_13():
    var_10 = repr
    var_11 = python_code_.ShoppinCart(creationDate=var_10)
    assert isinstance(var_11, python_code_.ShoppinCart)


def test_14():
    python_code_.Payment(paidDate=-2428.68, total="x?]p;", details=None)


def test_15():
    var_0 = "5k:Xmo[|"
    var_2 = python_code_.Payment(
        paidDate=var_0,
        total=b"\xf9\x05\xc8\xe4\x87Zxp\x84l\x85\xce\xc8\xa3",
        details=var_0,
        account1=[991.34, 3],
    )
    assert isinstance(var_2, python_code_.Payment)


def test_16():
    python_code_.Customer(address="60V2GYuF", phone="Customer", email="{\npN~")


def test_17():
    var_3 = lambda *args, **kwargs: "~,b?_&^vb;=GUVo@-q?"
    var_4 = "]78vM8]5 R"
    var_5 = python_code_.Customer(address=var_3, phone=var_4, email=var_4, acc10=b"}%")
    assert isinstance(var_5, python_code_.Customer)


def test_18():
    python_code_.MyClass2(attribute="webuser7")


def test_19():
    var_9 = python_code_.Product(
        name="TW", description="_Payment__order2", item12={True}
    )
    assert isinstance(var_9, python_code_.Product)
    var_11 = 0
    var_12 = python_code_.LineItem(quantity=var_11, price=var_9, product13=var_9)
    assert isinstance(var_12, python_code_.LineItem)


@pytest.mark.xfail(strict=True)
def test_20():
    var_12 = python_code_.Product(
        name="iaLt=\x0c{:",
        description="_Customer__webuser7,Account,account5,_Customer__acc10",
    )
    assert isinstance(var_12, python_code_.Product)
    var_13 = 3
    var_14 = python_code_.ShoppinCart(creationDate=var_12, account17=var_13)
    assert isinstance(var_14, python_code_.ShoppinCart)
    var_15 = python_code_.ShoppinCart
    python_code_.LineItem(quantity=var_13, price=var_12, sc19=var_14, lineitem15=var_15)


def test_21():
    var_18 = python_code_.Order(
        number=-1438,
        ordered=None,
        shipped=True,
        shipTo="_ShoppinCart__items18",
        total=-45.77,
        status=None,
        account5=None,
    )
    assert isinstance(var_18, python_code_.Order)


def test_22():
    var_16 = python_code_.Product(name="\r7q.zwKQY?,=vK", description='YpS"iZ[V')
    assert isinstance(var_16, python_code_.Product)
    var_17 = list
    var_18 = python_code_.Order(
        number=2615,
        ordered=var_17,
        shipped=True,
        shipTo="webuser8",
        total=-2628.17,
        status=var_17,
        order3={-1446.01},
        account5=var_17,
        items14=set(),
    )
    assert isinstance(var_18, python_code_.Order)


def test_23():
    var_12 = "items18,_LineItem__sc19,items18,account17"
    var_13 = python_code_.WebUser(
        login=1222.59, password=var_12, state=-4059, shoppincart9=[1316.01]
    )
    assert isinstance(var_13, python_code_.WebUser)
    var_14 = 1275.06
    var_15 = -1
    var_19 = python_code_.Order(
        number=var_15,
        ordered=None,
        shipped=False,
        shipTo="_Account__payment0items14webuser7",
        total=var_14,
        status=var_14,
        account5=None,
    )
    assert isinstance(var_19, python_code_.Order)
    var_20 = python_code_.Payment(
        paidDate=var_12, total=var_14, details=var_12, order2=var_19
    )
    assert isinstance(var_20, python_code_.Payment)


def test_24():
    var_2 = -2339
    var_3 = -2342.93
    var_4 = python_code_.LineItem(quantity=var_2, price=var_3)
    assert isinstance(var_4, python_code_.LineItem)
    var_5 = 2044.53
    var_6 = python_code_.Product(
        name=var_5, description=complex(-110.72097, 1497.0), item12="Order"
    )
    assert isinstance(var_6, python_code_.Product)
    var_7 = python_code_.LineItem(quantity=var_2, price=var_5, product13=var_6)
    assert isinstance(var_7, python_code_.LineItem)


def test_25():
    var_0 = sorted
    var_1 = 1343.87
    python_code_.Payment(paidDate=var_0, total=var_1, details=var_1)
    var_3 = 2490
    var_4 = -691.65
    var_5 = python_code_.LineItem(quantity=var_3, price=var_4)
    assert isinstance(var_5, python_code_.LineItem)
    var_6 = "account17"
    var_7 = python_code_.Customer(
        address=True, phone=var_1, email=var_6, webuser7=var_1
    )
    assert isinstance(var_7, python_code_.Customer)
    var_12 = True
    var_13 = {var_5, var_5, var_5, var_5}
    var_14 = python_code_.Order(
        number=var_0,
        ordered=var_0,
        shipped=var_12,
        shipTo=var_6,
        total=complex(-4092.0, -323.226),
        status=var_3,
        items14=var_13,
    )
    assert isinstance(var_14, python_code_.Order)


def test_26():
    var_8 = "]78vM8]5 R"
    var_9 = python_code_.Customer(
        address="\r<6\rS/imJ4D",
        phone="product13",
        email="z]<a&@\tay}U.Wh}!{xq",
        webuser7=var_8,
    )
    assert isinstance(var_9, python_code_.Customer)


def test_27():
    var_8 = python_code_.Webuser_Actor()
    var_11 = python_code_.Account(
        billingAddress="", open=None, closed=None, isClosed=False, cart16=var_8
    )
    assert isinstance(var_11, python_code_.Account)


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = python_code_.Customer(
        address="_ShoppinCart__account17 _WebUser__customer6 customer6",
        phone="Y",
        email="_WebUser__customer6",
        webuser7=None,
    )
    var_2 = python_code_.Account(
        billingAddress="",
        open=var_0,
        closed=var_0,
        isClosed=True,
        payment0=set(),
        cart16=var_0,
    )
    assert isinstance(var_2, python_code_.Account)
    python_code_.Customer(
        address="|M,G48ap*",
        phone="\tow",
        email="_LineItem__sc19 Account order4",
        acc10=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_57 = lambda *args, **kwargs: "Payment"
    var_58 = lambda *args, **kwargs: False
    var_59 = python_code_.Account(
        billingAddress=var_57,
        open=True,
        closed=var_57,
        isClosed=var_58,
        customer11=var_57,
    )
    assert isinstance(var_59, python_code_.Account)
    python_code_.ShoppinCart(creationDate=b")\x926%\xd84r", account17=var_59)


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = python_code_.AjoutProduit_UseCase()
    var_1 = 0
    var_2 = python_code_.Product(name=var_1, description=var_0)
    assert isinstance(var_2, python_code_.Product)
    var_3 = python_code_.LineItem(
        quantity=var_1,
        price=b"a\xc6\xef5\xb0",
        product13=var_2,
        lineitem15={"gQbG~*=q": False, "/Cn": True, "Fh\nvo!Me`": ""},
    )
    assert isinstance(var_3, python_code_.LineItem)
    var_4 = python_code_.Admin_Actor()
    python_code_.MyClass2(attribute=var_4)
    var_70 = lambda *args, **kwargs: "~,b?_&^vb;=GUVo@-q?"
    var_72 = "FQuQ\t*.\r2U.&K. ZtU"
    var_73 = "EE?\t.5^ZUgZs.e"
    var_74 = True
    var_75 = python_code_.Account(
        billingAddress=var_1, open=[], closed=var_0, isClosed=var_74, customer11=var_70
    )
    assert isinstance(var_75, python_code_.Account)
    python_code_.Customer(address=var_70, phone=var_72, email=var_73, acc10=var_75)


def test_31():
    var_14 = python_code_.ShoppinCart(
        creationDate=None, account17=None, items18={False, 2696.33}
    )
    assert isinstance(var_14, python_code_.ShoppinCart)


def test_32():
    var_10 = python_code_.Webuser_Actor()
    var_12 = python_code_.Webuser_Actor()
    var_13 = True
    var_14 = "-\\s(=<LiI\x0b_UeF"
    var_15 = python_code_.MyClass2(attribute=var_14)
    var_16 = 456.07
    var_17 = python_code_.Payment(
        paidDate=False, total=var_15, details=var_14, account1=var_12, order2=var_13
    )
    assert isinstance(var_17, python_code_.Payment)
    var_18 = {var_17, var_17, var_17}
    var_19 = python_code_.Order(
        number=-1,
        ordered=var_12,
        shipped='7J["4',
        shipTo=var_12,
        total=var_16,
        status=None,
        order3=var_18,
        account5=var_10,
    )
    assert isinstance(var_19, python_code_.Order)


def test_33():
    var_12 = bytes
    var_18 = -1338
    var_19 = True
    var_20 = python_code_.Order(
        number=var_18,
        ordered=True,
        shipped=var_19,
        shipTo=False,
        total=var_18,
        status=False,
    )
    assert isinstance(var_20, python_code_.Order)
    var_13 = python_code_.Payment(
        paidDate=var_12, total=847.5, details=var_12, order2=var_20
    )
    assert isinstance(var_13, python_code_.Payment)


def test_34():
    var_8 = python_code_.Webuser_Actor()
    var_12 = python_code_.ShoppinCart(
        creationDate='Pddks`mvk;n|\\)1DL"L', account17=var_8
    )
    assert isinstance(var_12, python_code_.ShoppinCart)


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = "account17.customer11._Account__order4.account5"
    var_2 = "R0MyoD-![u7("
    var_3 = python_code_.Customer(
        address=var_2, phone=var_2, email=False, webuser7=-3631
    )
    assert isinstance(var_3, python_code_.Customer)
    python_code_.WebUser(login=var_0, password=var_0, state=None, customer6=var_3)


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = "?v"
    var_14 = "M<q"
    var_15 = python_code_.AjoutProduit_UseCase
    python_code_.Payment(paidDate=var_15, total=var_15, details=False)
    var_16 = 1328
    var_17 = python_code_.LineItem(quantity=var_16, price=var_16)
    assert isinstance(var_17, python_code_.LineItem)
    var_18 = {var_17, var_17, var_17, var_17}
    var_19 = python_code_.ShoppinCart(creationDate=var_15, items18=var_18)
    assert isinstance(var_19, python_code_.ShoppinCart)
    python_code_.WebUser(login=var_0, password=var_14, state=None, shoppincart9=var_19)


def test_37():
    var_0 = "50kEmo[|"
    var_5 = dict
    var_47 = True
    var_48 = 737.9966135766044
    var_50 = python_code_.Order(
        number=var_47,
        ordered=var_0,
        shipped=True,
        shipTo="W!GnV1FN\x0bI)0w'v}",
        total=var_48,
        status=None,
        items14=set(),
    )
    assert isinstance(var_50, python_code_.Order)
    var_51 = -38.43
    var_52 = {var_50, var_50, var_50}
    var_53 = python_code_.LineItem(quantity=var_5, price=var_51, lineitem15=var_52)
    assert isinstance(var_53, python_code_.LineItem)


@pytest.mark.xfail(strict=True)
def test_38():
    var_13 = lambda *args, **kwargs: 3237
    var_26 = True
    var_27 = python_code_.ShoppinCart
    var_30 = python_code_.Account(
        billingAddress="\t^bR,)nUdwzU|B\no\\",
        open=None,
        closed=var_27,
        isClosed=var_26,
        payment0=set(),
        customer11=var_13,
    )
    assert isinstance(var_30, python_code_.Account)
    python_code_.Order(
        number=var_13,
        ordered=None,
        shipped=var_26,
        shipTo=complex(-1163.0, 329.0),
        total=var_27,
        status=("GDsu22T}A1[", 0, -3568.36),
        account5=var_30,
        items14=-1280.6,
    )


@pytest.mark.xfail(strict=True)
def test_39():
    var_12 = 2413.63
    var_13 = lambda *args, **kwargs: 3237
    var_14 = True
    var_16 = "_Customer__acc10o,_WebUser__shoppincart9,sc19"
    var_17 = False
    var_18 = python_code_.Account(
        billingAddress=var_16,
        open=var_16,
        closed=var_14,
        isClosed=var_17,
        customer11=var_13,
    )
    assert isinstance(var_18, python_code_.Account)
    var_19 = python_code_.Order(
        number=var_14,
        ordered=None,
        shipped=True,
        shipTo="customer6",
        total=var_12,
        status=None,
        account5=var_18,
    )
    assert isinstance(var_19, python_code_.Order)
    var_20 = {var_19}
    var_21 = python_code_.Customer(
        address=var_13,
        phone=var_16,
        email="`Gd/",
        acc10=b"q\xe7\x8a\xbaY2\x14\xef\x8b\xbdx\xa8b\x02\xb5k\xe0B\xc9",
    )
    assert isinstance(var_21, python_code_.Customer)
    python_code_.Account(
        billingAddress=var_13,
        open=None,
        closed=var_17,
        isClosed={},
        order4=var_20,
        customer11=var_21,
        cart16=var_16,
    )


def test_40():
    var_3 = 0
    var_4 = python_code_.LineItem(quantity=var_3, price=var_3)
    assert isinstance(var_4, python_code_.LineItem)
    var_5 = python_code_.LineItem(quantity=var_4, price=[])
    var_7 = "iHv-P$yAIe"
    var_8 = {var_5, var_5, var_5, var_4, var_4}
    var_9 = python_code_.Product(name=var_7, description=[], item12=var_8)
    assert isinstance(var_9, python_code_.Product)
    var_10 = "Account"
    python_code_.Product(name=-3872, description=var_10)
    var_12 = list
    python_code_.MyClass2(attribute=var_12)


@pytest.mark.xfail(strict=True)
def test_41():
    var_0 = "8j#-##hES"
    var_1 = python_code_.WebUser(
        login=1473.48, password=var_0, state=None, shoppincart9=0
    )
    assert isinstance(var_1, python_code_.WebUser)
    python_code_.ShoppinCart(
        creationDate=complex(465.535, -4255.323425), webuser8=var_1
    )


def test_42():
    var_17 = python_code_.LineItem(quantity=0, price=-450.01, lineitem15=set())
    assert isinstance(var_17, python_code_.LineItem)
    var_19 = "r\x0ctM3_BM"
    var_20 = "7_"
    var_22 = python_code_.Product(name=var_17, description=None)
    assert isinstance(var_22, python_code_.Product)
    var_23 = 2479.77
    var_24 = set()
    var_25 = python_code_.Account(
        billingAddress=var_20, open=var_19, closed=[], isClosed=651, payment0=var_24
    )
    assert isinstance(var_25, python_code_.Account)
    var_26 = python_code_.Payment(
        paidDate=var_17, total=var_23, details=var_22, account1=var_25
    )
    assert isinstance(var_26, python_code_.Payment)


@pytest.mark.xfail(strict=True)
def test_43():
    var_8 = python_code_.Webuser_Actor()
    var_12 = -602.52
    var_13 = lambda *args, **kwargs: 3237
    var_14 = True
    var_15 = python_code_.ShoppinCart
    var_16 = "_Customer__acc10o,_WebUser__shoppincart9,sc19"
    var_17 = True
    var_18 = python_code_.Account(
        billingAddress=var_16,
        open=var_16,
        closed=var_14,
        isClosed=var_17,
        customer11=var_13,
    )
    assert isinstance(var_18, python_code_.Account)
    var_19 = python_code_.Order(
        number=var_14,
        ordered=None,
        shipped=True,
        shipTo="customer6",
        total=var_12,
        status=None,
        account5=var_18,
    )
    assert isinstance(var_19, python_code_.Order)
    var_20 = {var_19, True}
    var_21 = python_code_.MyActor_Actor()
    var_24 = python_code_.Account(
        billingAddress=var_13,
        open=None,
        closed=var_17,
        isClosed={},
        order4=var_20,
        customer11=var_21,
        cart16=var_16,
    )
    assert isinstance(var_24, python_code_.Account)
    var_27 = "Q'1"
    python_code_.WebUser(
        login=var_27, password="ShoppinCart _WebUser__customer6 Payment", state=var_8
    )
    python_code_.Customer(address=var_16, phone=var_13, email=var_15)
    python_code_.ShoppinCart(creationDate=var_13, account17=var_24)
