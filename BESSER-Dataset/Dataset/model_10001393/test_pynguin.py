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
    Cart,
    Customer,
    ExerciseMachine,
    MediDevices,
    Medicine,
    Order,
    PaymentMethod,
    Person,
    Product,
    Registration,
    annotations,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = ""
    var_2 = float
    var_3 = "_Registration__admin11.person19._Product__mediDevices2"
    var_6 = -3519
    var_7 = python_code_.Cart(id=None, TotalBill=var_6)
    python_code_.PaymentMethod(
        paymentType=var_0, online=var_2, cashOnDelievery=var_3, cart9=var_7
    )


def test_1():
    var_2 = "qB5f=,"
    var_11 = "MediDevicesadin15"
    var_17 = python_code_.PaymentMethod(
        paymentType=var_11,
        online="product12-Admin-_Admin__product14",
        cashOnDelievery="&-\x0b",
        cart9=var_2,
    )
    assert isinstance(var_17, python_code_.PaymentMethod)


def test_2():
    var_0 = -1321
    var_12 = "_MediDevices__product3cartD6product3"
    var_13 = "E"
    var_19 = "MediDevicesadmin15"
    var_20 = python_code_.Medicine(
        id=var_0, name=var_19, formula=var_0, potency=var_13, product1=set()
    )
    assert isinstance(var_20, python_code_.Medicine)
    python_code_.PaymentMethod(
        paymentType=var_13, online=var_12, cashOnDelievery=var_12, cart9=None
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = lambda *args, **kwargs: "_Registration__admin11"
    var_2 = "BWa"
    var_6 = python_code_.ExerciseMachine(
        id=-5061.66, name=var_0, type=var_2, size=complex(732.00115, 1352.94)
    )
    python_code_.Product(
        pID=var_2,
        name=True,
        price=var_2,
        manufecturer={-4466.74},
        manufecturedDate=complex(-4438.00656, -627.543),
        expiry=938.57,
        color=b"\x95y\x96\x82\x94D\xa1q",
        exerciseMachine4=var_6,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_2 = "qB5f=,"
    var_11 = "MediDevicesadmin15"
    var_12 = python_code_.Person
    var_13 = python_code_.Product(
        pID=var_11,
        name=var_2,
        price=3,
        manufecturer=var_11,
        manufecturedDate=var_11,
        expiry="exerciseMachine4 PaymentMethod",
        color="\n\\@@G^0Ir\\b^Xm9n",
        medicine0=None,
        person13=None,
    )
    python_code_.MediDevices(
        id=b">\xae O\x9b*PHzvP", name=var_12, type=var_2, product3=var_13
    )


def test_5():
    var_2 = "ql5f=,"
    var_4 = python_code_.Person
    python_code_.MediDevices(id=var_4, name=b"W\xe9\xd5\xbe\xd0uO", type=var_2)


def test_6():
    var_8 = "!x^6Rx4(]/I`"
    var_9 = abs
    var_12 = python_code_.MediDevices(
        id=var_8, name="?@5;I+|", type="BP{zuo[*~[E2y]Yg", product3=var_9
    )
    assert isinstance(var_12, python_code_.MediDevices)


def test_7():
    var_0 = 2
    python_code_.Cart(id=-4238, TotalBill=var_0)


def test_8():
    var_7 = "bV2RT"
    var_10 = bool
    var_12 = python_code_.Order(
        id="/\\2`usRZda;*\rSqZ|\t",
        orderDate=var_7,
        quantity=var_10,
        orderStatus="",
        cart6=1656,
    )
    assert isinstance(var_12, python_code_.Order)
    var_13 = -3174
    var_14 = python_code_.Cart(id=var_12, TotalBill=var_13, paymentMethod8=var_13)
    assert isinstance(var_14, python_code_.Cart)
    var_15 = 1204
    python_code_.Medicine(id=var_15, name=var_10, formula=var_15, potency=None)


def test_9():
    var_20 = 1171
    var_22 = "USK@,q"
    python_code_.Medicine(
        id=var_20, name='{"n', formula=var_22, potency="_Product__medicine0"
    )


def test_10():
    var_2 = "ql5f=,"
    var_6 = python_code_.Admin(
        id=-2455,
        userName="X`uE *aRoj^]`kF~(a@",
        password="Admin:admin11:_Person__registration18",
        registration10=var_2,
    )
    assert isinstance(var_6, python_code_.Admin)


@pytest.mark.xfail(strict=True)
def test_11():
    var_2 = "ql5f=,"
    var_9 = "+5[n&;"
    var_14 = python_code_.Person
    var_17 = python_code_.Product(
        pID=var_9,
        name="]x>\x0cQ\\LPh%M F|z<W",
        price=3471,
        manufecturer=var_9,
        manufecturedDate=var_9,
        expiry="i/^jSWAw7BQ-",
        color=var_9,
        medicine0=var_2,
        exerciseMachine4=None,
        person13=None,
        admin15=var_14,
    )
    assert isinstance(var_17, python_code_.Product)
    python_code_.Admin(id={}, userName=set(), password=var_9, product14=var_17)


def test_12():
    var_2 = "qB5f=,"
    var_9 = python_code_.Product(
        pID=var_2,
        name="l`7i",
        price=2106,
        manufecturer=var_2,
        manufecturedDate=var_2,
        expiry="",
        color=var_2,
        person13=None,
        admin15=var_2,
    )
    assert isinstance(var_9, python_code_.Product)


def test_13():
    var_53 = "E"
    python_code_.Product(
        pID=var_53,
        name=var_53,
        price=3,
        manufecturer=var_53,
        manufecturedDate=var_53,
        expiry="exerciseMachine4 PaymentMethod",
        color="\n\\@@G^0Ir\\b^Xm9n",
        medicine0=None,
        person13=None,
    )


def test_14():
    var_0 = "registration10"
    var_1 = 2786
    var_2 = "ql5f=,"
    var_3 = "WGA"
    var_4 = python_code_.Person
    python_code_.Product(
        pID=var_0,
        name=var_0,
        price=var_1,
        manufecturer=var_0,
        manufecturedDate=var_2,
        expiry=var_3,
        color=var_4,
        mediDevices2=var_4,
    )
    var_6 = python_code_.Admin(
        id=-2455,
        userName="X`uE *aRoj^]`kF~(a@",
        password="Admin:admin11:_Person__registration18",
        registration10=var_2,
    )
    assert isinstance(var_6, python_code_.Admin)


@pytest.mark.xfail(strict=True)
def test_15():
    var_0 = lambda *args, **kwargs: "_Registration__admin11"
    var_1 = "mediDevices2,cart9,_Product__admin15"
    var_14 = "_Admin__registration10 admin11"
    var_15 = '"'
    var_16 = python_code_.Product(
        pID=var_1,
        name="Medicine _MediDevices__product3",
        price=-2020,
        manufecturer="_ExerciseMachine__product5-_MediDevices__product3-registration10-cart6",
        manufecturedDate="4>#}",
        expiry="o4zgb:&IAJ 2SN2$Dr1",
        color=var_1,
        person13=var_0,
        admin15=var_0,
    )
    python_code_.Person(
        Name=var_14,
        LastName=var_15,
        DOB=var_15,
        Address=4152.12,
        Phone=set(),
        Email=None,
        product12=var_16,
    )


@pytest.mark.xfail(strict=True)
def test_16():
    var_15 = 0
    var_16 = '_("ZPMUk2%'
    var_17 = repr
    var_18 = python_code_.ExerciseMachine(
        id=var_15, name=var_16, type=var_17, size=var_17
    )
    var_19 = 2141
    var_20 = "cart6"
    var_21 = python_code_.Registration(
        name=927.86,
        LastName=var_15,
        DOB=None,
        UserName=var_20,
        Password=b"\xbe\x93\x86\x14\x05\xca\x01\xe9\x96\xe6\xcbG\xfd\x8f}\x84\x1e\xc5",
        Address=var_16,
        Phone=b"T\x8b80\xccR<\xbd=\xb0zH\x1cQ\xbf\xc4\x81\xc2",
        Email=var_18,
    )
    python_code_.Person(
        Name=var_18,
        LastName=var_17,
        DOB=var_17,
        Address=var_16,
        Phone=var_19,
        Email=var_17,
        registration18=var_21,
    )


def test_17():
    var_0 = "n\\4"
    var_1 = "_ExerciseMachine__product5 _Cart__order7"
    var_2 = str
    python_code_.Registration(
        name=None,
        LastName=var_0,
        DOB=None,
        UserName=var_1,
        Password=None,
        Address=var_2,
        Phone=complex(-73.57, 2649.1011),
        Email=(-1622.35, -769.64, 837.98),
        person19=var_1,
        admin11=var_2,
    )
    var_4 = -605
    var_5 = bytes
    var_6 = 2
    var_7 = python_code_.ExerciseMachine(
        id=var_4, name=var_5, type=var_0, size=var_6, product5=()
    )
    assert isinstance(var_7, python_code_.ExerciseMachine)
    var_9 = "k7)RyN"
    python_code_.Person(
        Name=var_9,
        LastName={-369.36, ";X<]Ov=\\TD"},
        DOB=var_9,
        Address=var_1,
        Phone=var_2,
        Email=var_0,
        registration18=(),
    )


def test_18():
    var_0 = set
    var_1 = "js\\D5TkO\\"
    python_code_.ExerciseMachine(id=var_0, name=var_1, type=var_0, size=True)
    var_51 = -185
    var_54 = ""
    python_code_.Registration(
        name=var_1,
        LastName=var_0,
        DOB=var_0,
        UserName=var_54,
        Password=var_0,
        Address=complex(-4182.6648, 164.0),
        Phone=var_51,
        Email=var_54,
    )


def test_19():
    2


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = "^UN05"
    var_1 = lambda *args, **kwargs: []
    var_2 = 1402
    python_code_.Customer(id=True, userName=var_0, password=var_1)
    var_6 = python_code_.Cart(id=var_2, TotalBill=1)
    python_code_.Order(
        id=var_1, orderDate=var_0, quantity=var_2, orderStatus=set(), cart6=var_6
    )


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = "n\\4"
    var_1 = "_ExerciseMachine__product5 _Cart__order7"
    var_2 = str
    python_code_.Registration(
        name=None,
        LastName=var_0,
        DOB=None,
        UserName=var_1,
        Password=None,
        Address=var_2,
        Phone=complex(-73.57, 2649.1011),
        Email=(-1622.35, -769.64, 837.98),
        person19=var_1,
        admin11=var_2,
    )
    var_4 = -605
    var_5 = python_code_.PaymentMethod
    var_6 = 2
    var_7 = python_code_.ExerciseMachine(
        id=var_4, name=var_5, type=var_0, size=var_6, product5=()
    )
    assert isinstance(var_7, python_code_.ExerciseMachine)
    var_8 = "H)S3@&(7HLFo"
    var_9 = "k7)RyN"
    var_10 = python_code_.Person(
        Name=var_9,
        LastName={-369.36, ";X<]Ov=\\TD"},
        DOB=var_9,
        Address=var_1,
        Phone=var_2,
        Email=var_0,
        registration18=(),
    )
    python_code_.Registration(
        name=var_2,
        LastName=var_8,
        DOB=",nBl",
        UserName=var_7,
        Password=var_9,
        Address=var_9,
        Phone=var_6,
        Email=var_5,
        person19=var_10,
    )


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = ""
    var_1 = -154
    var_2 = complex
    var_3 = "\x0cMfV\n"
    var_4 = python_code_.Registration(
        name=var_0,
        LastName=var_0,
        DOB=var_2,
        UserName=var_0,
        Password=var_2,
        Address=var_2,
        Phone=[],
        Email=var_3,
        person19=var_0,
    )
    python_code_.Person(
        Name={808.48},
        LastName=var_0,
        DOB=True,
        Address=var_0,
        Phone=var_1,
        Email=b"\xb6\xaaA\xa9\x99\xfc\x90B\xb8\xcftC",
        registration18=var_4,
    )


def test_23():
    var_0 = -1334
    python_code_.Cart(id=True, TotalBill=var_0)
    var_7 = bytes
    var_8 = python_code_.Cart(
        id=var_7, TotalBill=complex(-151.0, 2086.249), order7=371.99
    )
    assert isinstance(var_8, python_code_.Cart)
    var_11 = "LA\x0c4)JB;/J\\B"
    var_12 = python_code_.Order(
        id={1627.35},
        orderDate=var_7,
        quantity={'"EJd$DS1VcQ$O)': 763},
        orderStatus=var_11,
        product17=(False, "\\kokqwzi\\T0&Gbj%", '"'),
    )
    assert isinstance(var_12, python_code_.Order)


def test_24():
    var_7 = "bV2RT"
    var_10 = int
    var_12 = python_code_.Order(
        id="/\\2`usRZda;*\rSqZ|\t",
        orderDate=var_7,
        quantity=var_10,
        orderStatus="",
        cart6=1656,
    )
    assert isinstance(var_12, python_code_.Order)


@pytest.mark.xfail(strict=True)
def test_25():
    var_0 = "^UN05"
    var_1 = lambda *args, **kwargs: []
    var_2 = 1402
    python_code_.Person(
        Name=var_0, LastName=var_1, DOB=True, Address=None, Phone=var_2, Email=b"6\xa5+"
    )
    python_code_.Customer(id=True, userName=var_0, password=var_1)
    var_5 = bytes
    var_6 = python_code_.Cart(
        id=var_5, TotalBill=complex(-151.0, 2086.249), order7=371.99
    )
    assert isinstance(var_6, python_code_.Cart)
    python_code_.Order(
        id=var_1, orderDate=var_0, quantity=var_2, orderStatus=set(), cart6=var_6
    )


def test_26():
    var_0 = -1334
    python_code_.Cart(id=True, TotalBill=var_0)
    var_8 = "47a#\x0bBq[XF("
    var_13 = "_Registration__admin11"
    var_14 = "_Admin__registration10_PaymentMethod__cart9"
    var_15 = python_code_.MediDevices
    python_code_.Person(
        Name=var_8,
        LastName=b"0\xe5\x12a\x9fd/\x9d\xc9\xf7",
        DOB=var_13,
        Address=var_14,
        Phone=var_8,
        Email=var_15,
        product12=var_14,
    )
    python_code_.MediDevices(id=var_8, name="_Cart__order7", type="GvvMp[ORV+ux_P)")


def test_27():
    var_2 = "5[n&;"
    var_7 = "aoK.kb"
    var_8 = python_code_.Product(
        pID='Qxq?(>h"[C;nW4@',
        name="IG$YX7]S",
        price=1671,
        manufecturer=var_7,
        manufecturedDate=">U~qe:7",
        expiry="/U",
        color="H^N-R@9?\r",
        person13=var_2,
        order16=var_7,
    )
    assert isinstance(var_8, python_code_.Product)


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = lambda *args, **kwargs: "_Registration__admin11"
    var_2 = "BWa"
    var_6 = "product3-exerciseMachine4-PaymentMethod-_ExerciseMachine__product5"
    var_7 = "X\n~"
    var_8 = "o"
    var_11 = 3
    var_12 = python_code_.Admin(id=var_6, userName=var_0, password=-61, product14=var_2)
    assert isinstance(var_12, python_code_.Admin)
    python_code_.Product(
        pID=1738.06,
        name={"registration10": False, "ozzP": False},
        price=var_11,
        manufecturer=var_8,
        manufecturedDate=var_7,
        expiry=complex(1527.0, -325.92489),
        color=var_6,
        medicine0="product3 _Order__cart6 PaymentMethod",
        mediDevices2=complex(916.11928, 5683.297),
        admin15=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = -1334
    var_1 = python_code_.Cart(id=var_0, TotalBill=var_0)
    var_2 = "+5[n&;"
    python_code_.Medicine(id=var_0, name=var_2, formula=var_1, potency=var_2)
    var_8 = "P/m%F-)O%~owCu^"
    var_9 = python_code_.PaymentMethod
    var_10 = '-\x0bYE|H\\_6NNSi\x0bXN"8'
    var_11 = "_Product__mediDevices2"
    var_12 = "\rTw"
    var_13 = python_code_.Product(
        pID=var_8,
        name=var_10,
        price=var_0,
        manufecturer=var_11,
        manufecturedDate=var_12,
        expiry={},
        color=complex(-1653.04746, -1561.97642),
        medicine0=852.61,
        mediDevices2=var_0,
    )
    assert isinstance(var_13, python_code_.Product)
    python_code_.Order(
        id=(),
        orderDate=var_8,
        quantity=var_0,
        orderStatus=var_9,
        cart6=var_2,
        product17=var_13,
    )


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = "=>5sc!"
    python_code_.Medicine(
        id=("medicine0 person19 _Person__product12 Person", -2795.61),
        name=-245.29,
        formula=var_0,
        potency=var_0,
    )
    var_2 = dict
    python_code_.Admin(id=var_2, userName=var_0, password=var_0)
    var_4 = -6652
    var_5 = " j]4\x0cAV"
    var_6 = python_code_.Medicine(
        id=var_4, name=var_5, formula=var_0, potency=var_2, product1=var_2
    )
    assert isinstance(var_6, python_code_.Medicine)
    var_11 = "%~,%"
    var_15 = -1
    var_16 = "Medicine,Product"
    var_17 = "tvpamj}"
    var_18 = 2
    var_19 = "WqUa1%:Z2Ko2u[\r"
    var_20 = python_code_.Product(
        pID=var_17,
        name=[-513.64, 2476.67],
        price=var_18,
        manufecturer=[
            "product17",
            "product5.paymentMethod8.cart9._Order__product17",
            1994.84,
        ],
        manufecturedDate=var_19,
        expiry=var_16,
        color=var_11,
        medicine0=var_2,
        admin15=complex(-462.1374, 2768.9),
        order16=False,
    )
    assert isinstance(var_20, python_code_.Product)
    python_code_.Order(
        id=(), orderDate=var_11, quantity=var_15, orderStatus=var_16, product17=var_20
    )


@pytest.mark.xfail(strict=True)
def test_31():
    var_2 = "ql5f=,"
    var_4 = python_code_.Person
    var_9 = "B[3<x"
    python_code_.Customer(id=b"\xb2>2@_\xb0\x0cR", userName=var_9, password=var_4)
    var_11 = -1
    var_12 = "Y|f]A"
    var_13 = "_PaymentMethod__cart9._Person__product12._Cart__paymentMethod8._Product__exerciseMachine4"
    var_14 = python_code_.Order(
        id=var_11, orderDate=var_12, quantity=var_4, orderStatus=var_13, cart6=var_13
    )
    assert isinstance(var_14, python_code_.Order)
    python_code_.Cart(id=[186, 2935], TotalBill=var_2, order7=var_14)


@pytest.mark.xfail(strict=True)
def test_32():
    var_0 = lambda *args, **kwargs: "_Registration__admin11"
    var_1 = "mediDevices2,cart9,_Product__admin15"
    var_2 = "BWa"
    var_3 = python_code_.Registration(
        name=var_1,
        LastName=1272,
        DOB=var_0,
        UserName=var_2,
        Password=var_0,
        Address=var_0,
        Phone=var_0,
        Email={False, '$e"\x0cQ\x0chV', False},
        person19=var_0,
    )
    var_4 = dict
    python_code_.Admin(
        id=var_0, userName=var_1, password=var_1, registration10=var_3, product14=var_4
    )


@pytest.mark.xfail(strict=True)
def test_33():
    var_6 = "_ExerciseMachine__product5,product3,product12,_PaymentMethod__cart9"
    var_7 = set
    python_code_.Registration(
        name=var_6,
        LastName=set(),
        DOB=None,
        UserName=var_7,
        Password=(-577.48, 1),
        Address=var_7,
        Phone=var_6,
        Email=None,
    )
    var_9 = "WUZ7E"
    var_11 = "_Admin__product14_Cart__paymentMethod8cart9"
    var_12 = 3144
    var_13 = "b1a&&\x0b26\\-y"
    var_14 = "product12order16_Product__mediDevices2"
    var_15 = "Iv\x0bE1h[Z*OXG5"
    var_16 = python_code_.Order(
        id=1889,
        orderDate="Product:exerciseMachine4",
        quantity=var_7,
        orderStatus=var_15,
    )
    python_code_.Product(
        pID={},
        name=var_11,
        price=var_12,
        manufecturer=var_9,
        manufecturedDate=var_13,
        expiry=var_14,
        color=var_14,
        mediDevices2=2941.55,
        exerciseMachine4=b'"k\xffj\xb3\xf0q1\x90~ \xcc',
        order16=var_16,
    )


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = -1334
    var_14 = python_code_.Person
    var_15 = "_MediDevices__product3cart6product3"
    var_16 = "E"
    var_17 = 919
    python_code_.Person(
        Name=var_15,
        LastName=var_16,
        DOB=var_0,
        Address=(-593, 2708.81, 2647.54),
        Phone=var_17,
        Email=var_16,
    )
    var_19 = python_code_.Person
    var_20 = python_code_.Product(
        pID=var_16,
        name=var_15,
        price=complex(-3257.6497, 1633.28243),
        manufecturer="\x0bgUK\r\\M70Ke}",
        manufecturedDate=var_19,
        expiry=var_14,
        color=-1185.07,
        mediDevices2=var_17,
        admin15=(3,),
    )
    assert isinstance(var_20, python_code_.Product)
    python_code_.MediDevices(
        id=b">\xae O\x9b*PHzvP", name=var_14, type=var_15, product3=var_20
    )


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = -1334
    var_1 = python_code_.Cart(id=var_0, TotalBill=var_0)
    var_2 = "+5[n&;"
    python_code_.Medicine(id=var_0, name=var_2, formula=var_1, potency=var_2)
    var_4 = 1171
    var_8 = "P/m%F-)O%~owCu^"
    var_15 = python_code_.Cart
    var_16 = -768
    var_17 = "<WWhNmo"
    var_18 = "lSwi7m9c*Z\rHT[;D}"
    var_19 = python_code_.Order(
        id=True, orderDate=var_15, quantity=var_15, orderStatus=var_8, product17=var_15
    )
    python_code_.Product(
        pID=var_8,
        name=var_4,
        price=var_16,
        manufecturer=set(),
        manufecturedDate=var_17,
        expiry=var_2,
        color=var_18,
        order16=var_19,
    )


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = "Cart"
    var_1 = lambda *args, **kwargs: True
    var_2 = 1710
    var_3 = python_code_.Registration(
        name="",
        LastName=var_0,
        DOB=var_0,
        UserName=var_1,
        Password=var_1,
        Address=var_0,
        Phone=var_2,
        Email=var_1,
    )
    var_4 = complex
    var_5 = "5mw3^YGH~:`oPH"
    var_6 = python_code_.ExerciseMachine(id=var_4, name=[True], type=var_5, size=var_2)
    var_7 = bool
    python_code_.MediDevices(id=var_7, name=var_3, type=var_5)
    var_9 = "OzN\x0cX"
    python_code_.Admin(id="yW%[aH$**x\tc\n2c,", userName=var_9, password=None)
    var_11 = "[-`N0VdC^-l(w.wO"
    python_code_.Medicine(
        id=var_1, name=var_11, formula=var_5, potency=complex(154.1, -294.30479)
    )
    var_16 = tuple
    var_17 = python_code_.Cart(
        id="E Q-\ry@a{%- x\r", TotalBill=var_9, paymentMethod8=var_16
    )
    assert isinstance(var_17, python_code_.Cart)
    python_code_.PaymentMethod(
        paymentType=var_7, online=var_9, cashOnDelievery=var_6, cart9=var_17
    )


@pytest.mark.xfail(strict=True)
def test_37():
    var_2 = "ql5f=,"
    var_4 = python_code_.Person
    var_10 = python_code_.Admin(
        id=-2455,
        userName="X`uE *aRoj^]`kF~(a@",
        password="Admin:admin11:_Person__registration18",
        registration10=var_2,
    )
    assert isinstance(var_10, python_code_.Admin)
    var_13 = 2379
    python_code_.Registration(
        name=var_10,
        LastName=b"\xe9\x85\xe4\xf0\xa4s\xc63\xdc\xb9|\x96",
        DOB=var_4,
        UserName=var_4,
        Password=var_10,
        Address=var_2,
        Phone=var_13,
        Email=var_2,
        person19={
            "qllFE7m0=!o-BA}hHj=": 1382.94,
            "/\\\x0c5D(z77VM_/6t": False,
            "_ExerciseMachine__product5": "product3",
        },
        admin11=var_10,
    )


@pytest.mark.xfail(strict=True)
def test_38():
    var_2 = "qUB5f=,"
    var_22 = ""
    var_24 = -1458
    var_25 = python_code_.Medicine(
        id=var_24,
        name="\rnw}lp,<^,\nKkC",
        formula=var_22,
        potency="\t9H\x0b$\nPoeHy|l1>d/?",
    )
    python_code_.Product(
        pID=var_2,
        name=var_2,
        price=var_24,
        manufecturer={56, -2392},
        manufecturedDate=5222,
        expiry=2032,
        color=var_22,
        medicine0=var_25,
        exerciseMachine4=var_24,
        order16=var_25,
    )


@pytest.mark.xfail(strict=True)
def test_39():
    var_2 = "qB5f=,"
    var_11 = ""
    var_13 = -1458
    var_14 = "-O\tR\n%3hm"
    var_15 = python_code_.Medicine(
        id=var_11,
        name=b"=\x95\x90\xde\xdf\x80\xb2Z\xe3\x8c\xb3",
        formula=var_13,
        potency=var_2,
        product1=var_13,
    )
    assert isinstance(var_15, python_code_.Medicine)
    python_code_.Product(
        pID=var_2,
        name=var_2,
        price=var_13,
        manufecturer={56, -2392},
        manufecturedDate=5222,
        expiry=2032,
        color=var_14,
        medicine0=var_15,
        exerciseMachine4=var_13,
        order16=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_40():
    var_0 = "product3._PaymentMethod__cart9.registration10"
    var_1 = python_code_.Admin(
        id={"_ExerciseMachine__product5.product12": -1428},
        userName=var_0,
        password=var_0,
    )
    var_2 = "_Product__mediDevices2"
    var_3 = "*ed<O\\K\t\x0c9!\n$DO?/\x0c/"
    var_4 = "37B@Y>7\x0c"
    var_5 = abs
    var_6 = "{ZlV2&fWqd"
    var_7 = "lV(z4'0w9<d?m*"
    var_8 = python_code_.Person(
        Name=var_5,
        LastName=var_6,
        DOB=var_7,
        Address=var_7,
        Phone=set(),
        Email=var_2,
        registration18=(),
        product12={},
    )
    python_code_.Product(
        pID=var_0,
        name=var_2,
        price=var_1,
        manufecturer=var_3,
        manufecturedDate=var_4,
        expiry=var_0,
        color=var_0,
        exerciseMachine4=var_2,
        person13=var_8,
        admin15=var_5,
    )
