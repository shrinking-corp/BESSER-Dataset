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
    Cart_Checkout,
    Cart_ShoppingCart,
    Customer_Account,
    Customer_Customer,
    Customer_Customer1,
    Customer_Payment,
    Customer_Payment1,
    Customer_User,
    GUI_Screen,
    Product_Item,
    Product_Item_Specification,
    Product_Item_Type,
    Shopping_Cart_Checkout,
    Shopping_Cart_ShoppingCart,
    annotations,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = python_code_.GUI_Screen
    var_1 = "Payment_Customer_11._GUI_Screen__GUI_Screen_ShoppingCart_024.GUI_Screen_Account_123.Customer_Customer"
    python_code_.Product_Item_Specification(
        quantity=var_0, price=var_0, id=var_0, ItemSpecs__={True, -3174}, Brand__=var_1
    )


def test_1():
    var_0 = "&]wGbs,"
    var_1 = True
    var_2 = lambda *args, **kwargs: [
        "GUI_Screen_Account_123",
        "_Shopping_Cart_ShoppingCart__ShoppingCart_Checkout_06",
    ]
    var_3 = python_code_.Customer_Payment1(PayBill__=var_0, Auth__=var_1, ID=var_2)
    assert isinstance(var_3, python_code_.Customer_Payment1)
    var_4 = 1998.07
    var_5 = -913
    var_6 = "b*@\r5D(g &"
    var_7 = python_code_.Product_Item(
        quantity=var_5,
        list__=var_4,
        id=b"U\x19Ms\x9d\xa8\x01*",
        OutofStock__=var_6,
        totalcost__=var_2,
        Item_ShoppingCart_020=None,
    )
    assert isinstance(var_7, python_code_.Product_Item)
    var_8 = python_code_.Product_Item_Specification(
        quantity=var_0,
        price=var_4,
        id=var_2,
        ItemSpecs__=var_0,
        Brand__=complex(405.69037, -3205.9),
        Item_Specification_Item_016=var_7,
    )
    assert isinstance(var_8, python_code_.Product_Item_Specification)


def test_2():
    var_0 = 0
    var_13 = "_Customer_Customer1__Payment_Customer_19"
    python_code_.Product_Item_Type(
        quantity=var_0,
        price=None,
        id=var_0,
        ItemType__=b"\xd2\x14\x1b\xf1x\tTC\x0c\xc9",
        Avail__=var_13,
    )


def test_3():
    var_0 = lambda *args, **kwargs: "GUI_Screen_Account_022Customer_Customer1"
    var_1 = "K,"
    var_2 = python_code_.Customer_Payment1(
        PayBill__=var_1, Auth__={False, True}, ID=(805, "ygNSGLLj>8R\r")
    )
    assert isinstance(var_2, python_code_.Customer_Payment1)
    var_3 = python_code_.Customer_Customer1(
        userId="v]B@e)",
        PaymentMet__=var_0,
        Account__=var_0,
        select__=var_1,
        Payment_Customer_19=var_2,
    )
    assert isinstance(var_3, python_code_.Customer_Customer1)
    var_4 = 1371.78
    var_5 = 131
    var_6 = python_code_.Product_Item(
        quantity=(), list__=var_4, id=var_5, OutofStock__=var_4, totalcost__=var_0
    )
    assert isinstance(var_6, python_code_.Product_Item)


def test_4():
    var_0 = lambda *args, **kwargs: True
    var_8 = 1998.07
    var_9 = 1132
    var_10 = "b*@\r5D(g &"
    var_11 = python_code_.Product_Item(
        quantity=var_9,
        list__=2464.54,
        id=var_9,
        OutofStock__=var_10,
        totalcost__=var_10,
        Item_Specification_Item_117={var_8, -1418.79, var_0},
        Item_Type_Item_119=set(),
    )
    assert isinstance(var_11, python_code_.Product_Item)


def test_5():
    var_0 = python_code_.GUI_Screen
    var_1 = "Payment_Customer_11._GUI_Screen__GUI_Screen_ShoppingCart_024.GUI_Screen_Account_123.Customer_Customer"
    var_3 = -1009.13
    var_5 = "8CjEh=F\nl;DzsZZ Ply"
    var_6 = "G?a7FYInFOR>"
    var_7 = python_code_.Customer_Customer(
        firstname=var_5,
        lastname=var_6,
        emailAddress=var_5,
        id=var_0,
        login=var_0,
        password=var_3,
        Message=["umH gV9C\n"],
    )
    var_8 = -1675
    var_9 = python_code_.Customer_Account(Login__=var_0, account__=var_6)
    var_10 = python_code_.Customer_Payment1(
        PayBill__={"pQ0X@^@lCJ3O", -1252.32, 3}, Auth__=[], ID=var_9
    )
    assert isinstance(var_10, python_code_.Customer_Payment1)
    var_11 = {var_10, var_10}
    var_12 = python_code_.Cart_Checkout(
        Paymentid=b"\xa3\xf2Wt\r\x1a\xb3\xc4\xc5\tM,\xff\x07Sn5",
        CheckoutID=var_8,
        billingMethod=var_1,
        CustomerID=None,
        PayBill__=var_1,
        ShoppingCart_Checkout_111=var_7,
        Checkout_Payment_014=var_11,
    )
    assert isinstance(var_12, python_code_.Cart_Checkout)


def test_6():
    var_0 = lambda *args, **kwargs: True
    var_1 = -732
    var_2 = "Customer_Customer"
    var_3 = python_code_.Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_1,
        billingMethod=var_2,
        CustomerID=var_2,
        PayBill__=var_2,
    )
    assert isinstance(var_3, python_code_.Cart_Checkout)


def test_7():
    var_0 = lambda *args, **kwargs: True
    var_1 = -777
    var_10 = python_code_.Cart_ShoppingCart(
        id=var_1,
        creationDate=var_0,
        CheckoutID=-1210,
        AddCart=var_1,
        RemoveOrder=-1076,
        UpdateOrder=1043,
        GetTotal__=2819.5,
    )
    assert isinstance(var_10, python_code_.Cart_ShoppingCart)


def test_8():
    var_23 = "k,"
    var_24 = python_code_.Customer_Payment1(
        PayBill__=var_23,
        Auth__=False,
        ID=var_23,
        Payment_Customer_08=set(),
        Checkout_Payment_115=None,
    )
    assert isinstance(var_24, python_code_.Customer_Payment1)


def test_9():
    var_23 = "K,"
    var_24 = python_code_.Customer_Payment1(
        PayBill__=var_23, Auth__={False, True}, ID=(805, "ygNSGLLj>8R\r")
    )
    assert isinstance(var_24, python_code_.Customer_Payment1)


def test_10():
    var_17 = "_Cart_ShoppingCart__ShoppingCart_Checkout_0~10.ShoppingCart_Customer_113"
    var_21 = -1009.13
    var_22 = "A`AL\\K"
    var_23 = 26
    var_25 = python_code_.Customer_Payment1(
        PayBill__=var_17, Auth__=True, ID=var_23, Checkout_Payment_115=var_21
    )
    assert isinstance(var_25, python_code_.Customer_Payment1)
    var_26 = 1
    var_27 = python_code_.Product_Item(
        quantity=var_26,
        list__=var_21,
        id=var_23,
        OutofStock__={True, 1, 649.25},
        totalcost__=True,
        Item_Specification_Item_117=var_22,
    )
    assert isinstance(var_27, python_code_.Product_Item)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = 0
    var_1 = 238
    var_2 = python_code_.Shopping_Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_1,
        billingMethod=(),
        CustomerID=(False, -1368.51),
        Checkout__=complex(1642.1401, -1372.055),
    )
    assert isinstance(var_2, python_code_.Shopping_Cart_Checkout)
    var_3 = 538
    var_4 = "_Product_Item__Item_ShoppingCart_020"
    var_5 = python_code_.GUI_Screen(
        id=var_3,
        Message=var_0,
        Exit__=False,
        Error__=var_4,
        DisplayList__=var_0,
        GUI_Screen_Account_022={"ZVtrq`Mspz!\t": 3405.06},
    )
    python_code_.Customer_Account(
        Login__=var_2,
        account__="Shopping_Cart_ShoppingCart,Item_Type_Item_119",
        GUI_Screen_Account_123=var_5,
    )


def test_12():
    var_0 = repr
    var_1 = python_code_.Shopping_Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_0,
        billingMethod={
            "]Bo#": False,
            "Customer_Payment._Product_Item__GUI_Screen_Item_127.GUI_Screen_Account_022._Customer_Payment1__Payment_Customer_08": -1677,
        },
        CustomerID=var_0,
        Checkout__=var_0,
    )
    assert isinstance(var_1, python_code_.Shopping_Cart_Checkout)
    var_2 = python_code_.Customer_Account(
        Login__=var_0, account__=b"\x0e\x19\xa7i\xcdCP\xf7_\x06}\xdfK\x0cC"
    )
    var_3 = -2602.97
    var_4 = "Item_ShoppingCart_121"
    var_5 = 465
    var_6 = -827
    var_7 = python_code_.Cart_Checkout(
        Paymentid=var_5,
        CheckoutID=var_6,
        billingMethod=complex(94.2830444, -252.8691),
        CustomerID=(-1661, True, -2198.25),
        PayBill__=var_2,
        ShoppingCart_Checkout_111=var_0,
    )
    assert isinstance(var_7, python_code_.Cart_Checkout)
    var_8 = python_code_.Customer_Payment1(
        PayBill__=var_4, Auth__=-1880, ID=var_2, Checkout_Payment_115=var_7
    )
    assert isinstance(var_8, python_code_.Customer_Payment1)
    var_9 = python_code_.Customer_Customer1(
        userId=var_0,
        PaymentMet__=var_3,
        Account__=var_4,
        select__=var_0,
        Payment_Customer_19=var_8,
    )
    assert isinstance(var_9, python_code_.Customer_Customer1)
    var_10 = {var_9, var_9, var_9, var_9, var_9}
    python_code_.Customer_Payment1(
        PayBill__=var_1,
        Auth__={
            "g`qL(yE(R]": -2439.6,
            "Product_Item_Type": 1,
            "_Product_Item_Type__Item_Type_Item_018": False,
        },
        ID=var_2,
        Payment_Customer_08=var_10,
    )
    var_12 = "[QJ<14m2&QN hp"
    var_13 = "_Cart_ShoppingCart__ShoppingCart_Checkout_010:_Customer_Customer1__ShoppingCart_Customer_113:Payment_Customer_08"
    python_code_.Customer_Customer(
        firstname=var_2,
        lastname=var_4,
        emailAddress=complex(194.428, 2030.5625828),
        id=var_6,
        login=var_5,
        password=var_12,
        Message=var_13,
    )


def test_13():
    var_1 = "K,"
    var_2 = python_code_.Customer_Payment1(
        PayBill__=var_1, Auth__={False, True}, ID=(805, "ygNSGLLj>8R\r")
    )
    assert isinstance(var_2, python_code_.Customer_Payment1)
    var_3 = python_code_.Customer_Customer1(
        userId=var_1,
        PaymentMet__=426.19,
        Account__="ShoppingCart_Checkout_06",
        select__=var_1,
        Payment_Customer_19=var_2,
        ShoppingCart_Customer_113=None,
    )
    assert isinstance(var_3, python_code_.Customer_Customer1)


def test_14():
    var_26 = "Customer_Customer1Item_ShoppingCrt_121Item_Specification_Item_016Item_ShoppingCart_020"
    var_35 = python_code_.Customer_User(Addresschange__={}, userid__=var_26)
    var_36 = 1560.49
    var_37 = abs
    python_code_.Customer_Customer1(
        userId=var_35,
        PaymentMet__=var_36,
        Account__=var_26,
        select__={604.04},
        ShoppingCart_Customer_113=var_37,
    )


def test_15():
    var_0 = repr
    var_1 = python_code_.Shopping_Cart_Checkout(
        Paymentid=-813,
        CheckoutID=-1,
        billingMethod=")fSeZv2,",
        CustomerID="V\x0bn(M9o12",
        Checkout__=316.87,
        Payment_Checkout_15={"Item_ShoppingCart_020", var_0, var_0},
        ShoppingCart_Checkout_17=None,
    )
    assert isinstance(var_1, python_code_.Shopping_Cart_Checkout)


def test_16():
    var_1 = "Payment_Customer_11._GUI_Screen__GUI_Screen_ShopfingCart_024.GUI_Screen_Account_123.Customer_Customer"
    var_5 = python_code_.Shopping_Cart_Checkout(
        Paymentid=-366,
        CheckoutID=-3153,
        billingMethod=var_1,
        CustomerID=var_1,
        Checkout__=225.99,
    )
    assert isinstance(var_5, python_code_.Shopping_Cart_Checkout)


def test_17():
    var_9 = "_Customer_Qustomer1__Payment_Customer_19"
    var_18 = 2008.2442277415023
    var_21 = -1549
    var_22 = -222
    var_23 = python_code_.Cart_ShoppingCart(
        id=1,
        creationDate=var_18,
        CheckoutID=var_21,
        AddCart=var_22,
        RemoveOrder=complex(-2021.0, -2613.8553),
        UpdateOrder=var_22,
        GetTotal__=var_18,
        ShoppingCart_Checkout_010={True},
        ShoppingCart_Customer_012=set(),
        GUI_Screen_ShoppingCart_125={},
    )
    assert isinstance(var_23, python_code_.Cart_ShoppingCart)
    var_24 = 1051
    var_25 = python_code_.GUI_Screen
    var_26 = -1975
    var_27 = -1540
    var_28 = set()
    var_29 = python_code_.Shopping_Cart_ShoppingCart(
        id=var_26,
        creationDate=var_26,
        CheckoutID=b"\xc9A\x7f\x08Pr\xee\\\x10\xa7US\x1b\xe1",
        AddOrder=var_27,
        RemoveOrder=[],
        UpdateOrder={""},
        GetTotal__=var_18,
        ShoppingCart_Checkout_06=var_28,
    )
    var_30 = python_code_.Shopping_Cart_Checkout(
        Paymentid=None,
        CheckoutID=var_24,
        billingMethod=var_25,
        CustomerID=var_9,
        Checkout__=var_18,
        ShoppingCart_Checkout_17=var_29,
    )
    assert isinstance(var_30, python_code_.Shopping_Cart_Checkout)


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = "&]wGbs,"
    var_29 = -1222
    var_30 = tuple
    python_code_.Shopping_Cart_ShoppingCart(
        id=var_0,
        creationDate=2,
        CheckoutID=var_29,
        AddOrder=var_30,
        RemoveOrder=[],
        UpdateOrder="#$-mi{ {Du*c+cG",
        GetTotal__=(True,),
        ShoppingCart_Checkout_06=var_30,
    )


def test_19():
    var_5 = 4358
    var_6 = 780
    var_7 = -908.2721128566218
    python_code_.Shopping_Cart_ShoppingCart(
        id=var_6,
        creationDate=None,
        CheckoutID=2,
        AddOrder=var_6,
        RemoveOrder=var_6,
        UpdateOrder=var_6,
        GetTotal__=var_7,
        Customer_ShoppingCart_13=var_5,
    )


def test_20():
    var_0 = len
    python_code_.Customer_User(Addresschange__=None, userid__=var_0)
    var_5 = 2208
    var_6 = 789
    var_7 = -899.23
    var_8 = python_code_.Shopping_Cart_ShoppingCart(
        id=1109,
        creationDate=None,
        CheckoutID=var_5,
        AddOrder=var_6,
        RemoveOrder=1972,
        UpdateOrder=var_6,
        GetTotal__=var_7,
    )
    var_10 = -639
    var_51 = "Customer_Customer"
    var_53 = -4646.897416138177
    var_54 = -876
    var_55 = python_code_.Product_Item(
        quantity=(),
        list__=var_0,
        id=b"\xf5p{\x8e\x93Da\x9c\x14",
        OutofStock__=var_51,
        totalcost__=b"I\x1e\x9e\x89\xf6",
        Item_ShoppingCart_020=var_0,
        GUI_Screen_Item_127=False,
    )
    assert isinstance(var_55, python_code_.Product_Item)
    var_56 = "is"
    var_57 = set()
    var_58 = python_code_.Product_Item(
        quantity=var_10,
        list__=var_53,
        id=var_0,
        OutofStock__=var_51,
        totalcost__=var_56,
        Item_Specification_Item_117=var_57,
    )
    var_59 = {var_55, var_58, var_55}
    var_60 = python_code_.Cart_ShoppingCart(
        id=var_5,
        creationDate=var_0,
        CheckoutID=var_54,
        AddCart=b"\xa3b",
        RemoveOrder=var_6,
        UpdateOrder=var_5,
        GetTotal__=var_8,
        Item_ShoppingCart_121=var_59,
    )
    assert isinstance(var_60, python_code_.Cart_ShoppingCart)


def test_21():
    var_0 = lambda *args, **kwargs: True
    var_1 = 1608
    var_11 = -4601
    var_12 = "Ufz2+Pae.ZEU^lQ"
    python_code_.Customer_Payment(
        Paymentid=var_11,
        login=var_11,
        ApplPay=var_1,
        CustomerId=var_12,
        PayPal=var_0,
        Payment__=var_0,
        Payment_Checkout_04=var_12,
    )


def test_22():
    var_1 = True
    var_9 = "_Customer_Customer1__Payment_Customer_19"
    var_10 = -1009.13
    var_14 = "ShoppingCart_Checkout_111"
    python_code_.Customer_Payment(
        Paymentid=var_1,
        login=var_14,
        ApplPay=var_9,
        CustomerId=var_9,
        PayPal=var_9,
        Payment__=var_10,
    )


def test_23():
    var_0 = lambda *args, **kwargs: True
    var_1 = -732
    var_2 = "Customer_Customer"
    var_3 = python_code_.Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_1,
        billingMethod=var_2,
        CustomerID=var_2,
        PayBill__=var_2,
    )
    assert isinstance(var_3, python_code_.Cart_Checkout)
    var_12 = 2938
    var_13 = "Customer_ShoppingCart_02"
    var_14 = -113.5
    python_code_.Customer_Payment(
        Paymentid=var_12,
        login=var_13,
        ApplPay=True,
        CustomerId=var_2,
        PayPal=var_1,
        Payment__=var_14,
        Payment_Customer_00={},
    )


def test_24():
    var_0 = "J1KaS?y"
    var_1 = lambda *args, **kwargs: []
    var_2 = "_Cart_ShoppingCart__ShoppingCart_Checkout_010.ShoppingCart_Customer_113"
    var_3 = "Checkout_Payment_014-GUI_Screen"
    var_4 = "z[kE8$9^%(<Z[n>QM"
    var_5 = "k|#N^`q>g9{Aq\x0c:"
    python_code_.Customer_Customer(
        firstname=var_0,
        lastname=var_1,
        emailAddress=var_2,
        id={
            "_Cart_ShoppingCart__ShoppingCart_Customer_012:Customer_Payment:_Product_Item__Item_Specification_Item_117:_Customer_Customer__Payment_Customer_11": 2761.61,
            "_Customer_Payment1__Checkout_Payment_115,_Customer_Payment__Payment_Checkout_04": -4051.77,
        },
        login=var_3,
        password=var_4,
        Message=var_5,
    )


def test_25():
    var_26 = "Customer_Customer1Item_ShoppingCrt_121Item_Specification_Item_016Item_ShoppingCart_020"
    var_33 = 385.68
    var_35 = python_code_.Customer_User(Addresschange__={}, userid__=var_26)
    var_36 = 1560.49
    var_37 = abs
    python_code_.Customer_Customer1(
        userId=var_35,
        PaymentMet__=var_36,
        Account__=var_26,
        select__={604.04},
        ShoppingCart_Customer_113=var_37,
    )
    var_39 = "x!^o/YW+R]:"
    python_code_.Customer_Customer(
        firstname=(1840, "fbsT:JQ{\x0cbtf2^\rFa#j", -1537.36),
        lastname=var_39,
        emailAddress=var_37,
        id=var_33,
        login=[],
        password=var_26,
        Message=var_35,
        Payment_Customer_11=False,
    )


def test_26():
    var_0 = 0
    var_13 = "_Customer_Customer1__Payment_Customer_19"
    var_14 = python_code_.Product_Item_Type(
        quantity=var_0,
        price=None,
        id=var_0,
        ItemType__=b"\xd2\x14\x1b\xf1x\tTC\x0c\xc9",
        Avail__=var_13,
    )
    python_code_.GUI_Screen(
        id=var_0,
        Message=None,
        Exit__=-1920.74,
        Error__=var_13,
        DisplayList__=var_14,
        GUI_Screen_ShoppingCart_024=-2039.34,
    )


def test_27():
    var_17 = "_Cart_ShoppingCart__ShoppingCart_Checkout_0~10.ShoppingCart_Customer_113"
    var_33 = 131
    python_code_.GUI_Screen(
        id=var_33, Message=var_17, Exit__=var_33, Error__=var_17, DisplayList__=var_17
    )


def test_28():
    python_code_.Customer_User(
        Addresschange__="m7KpZ,0Rm0>K", userid__="Customer_Payment"
    )


def test_29():
    var_0 = lambda *args, **kwargs: True
    var_11 = -777
    var_12 = "Customer_Cust}omer"
    var_13 = python_code_.Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_11,
        billingMethod=var_12,
        CustomerID=var_12,
        PayBill__=var_12,
    )
    assert isinstance(var_13, python_code_.Cart_Checkout)
    var_15 = python_code_.Customer_Customer1(
        userId=var_11,
        PaymentMet__=var_0,
        Account__=var_0,
        select__=var_11,
        ShoppingCart_Customer_113={-3489},
    )
    var_16 = {var_15}
    var_17 = python_code_.Customer_Payment1(
        PayBill__=1978,
        Auth__=var_11,
        ID=-1738.18,
        Payment_Customer_08=var_16,
        Checkout_Payment_115=var_13,
    )
    assert isinstance(var_17, python_code_.Customer_Payment1)


def test_30():
    var_0 = lambda *args, **kwargs: True
    var_1 = -777
    var_8 = 1998.07
    var_9 = 1132
    var_10 = "b*@\r5D(g &"
    var_11 = python_code_.Product_Item(
        quantity=var_9,
        list__=2464.54,
        id=var_9,
        OutofStock__=var_10,
        totalcost__=var_10,
        Item_Specification_Item_117={var_8, -1418.79, var_0},
        Item_Type_Item_119=set(),
    )
    assert isinstance(var_11, python_code_.Product_Item)
    var_12 = python_code_.Product_Item_Specification(
        quantity=var_1,
        price=var_8,
        id=-3350,
        ItemSpecs__=",iJ",
        Brand__="_Product_Item__GUI_Screen_Item_127",
    )
    var_13 = 245
    var_14 = -1455
    var_15 = 1
    var_16 = "^Do$`':TqM2'q4>"
    var_17 = python_code_.Shopping_Cart_Checkout(
        Paymentid=var_15,
        CheckoutID=set(),
        billingMethod=var_0,
        CustomerID=var_16,
        Checkout__=(1015.28,),
    )
    assert isinstance(var_17, python_code_.Shopping_Cart_Checkout)
    var_18 = python_code_.Customer_Payment(
        Paymentid=var_13,
        login=var_10,
        ApplPay=var_14,
        CustomerId=var_0,
        PayPal=var_15,
        Payment__=var_12,
        Payment_Checkout_04=var_17,
    )
    assert isinstance(var_18, python_code_.Customer_Payment)


@pytest.mark.xfail(strict=True)
def test_31():
    var_0 = 3
    var_1 = python_code_.Customer_Payment1
    var_2 = -1776
    var_3 = 1448.22
    var_4 = "t\x0cY\\30VNa&4"
    var_5 = -2537
    var_6 = python_code_.Customer_Payment(
        Paymentid=True,
        login=var_2,
        ApplPay=var_0,
        CustomerId=var_0,
        PayPal=var_5,
        Payment__=var_2,
        Payment_Customer_00={"Product_Item_Specification"},
    )
    var_7 = {var_6, var_6}
    var_8 = python_code_.Shopping_Cart_Checkout(
        Paymentid=var_3,
        CheckoutID=2138.92,
        billingMethod=var_2,
        CustomerID=var_4,
        Checkout__=var_1,
        Payment_Checkout_15=var_7,
    )
    assert isinstance(var_8, python_code_.Shopping_Cart_Checkout)
    var_9 = {var_8, var_8, var_8, var_8, var_8}
    var_10 = python_code_.Shopping_Cart_ShoppingCart(
        id=var_0,
        creationDate=var_1,
        CheckoutID=var_2,
        AddOrder=var_1,
        RemoveOrder=1491.21,
        UpdateOrder=var_2,
        GetTotal__=var_3,
        ShoppingCart_Checkout_06=var_9,
    )
    assert isinstance(var_10, python_code_.Shopping_Cart_ShoppingCart)
    var_11 = -1162.79
    var_12 = "d>"
    python_code_.Product_Item_Type(
        quantity=var_9, price=var_11, id=var_8, ItemType__=var_12, Avail__=var_8
    )
    var_14 = "ShoppingCart_Customer_012"
    var_15 = "_Customer_Customer1__ShoppingCart_Customer_113"
    python_code_.Customer_Customer(
        firstname=None,
        lastname=var_14,
        emailAddress={},
        id=(False,),
        login=None,
        password=var_15,
        Message=var_1,
        Payment_Customer_11=var_0,
    )
    var_17 = "TuH5\n+!='|]\r%;[P\x0bA"
    python_code_.Customer_Account(Login__=var_17, account__=var_0)
    var_19 = 571.31
    python_code_.Product_Item(
        quantity=var_11,
        list__=var_19,
        id=var_15,
        OutofStock__=var_15,
        totalcost__={},
        Item_Type_Item_119=complex(4927.0, -3917.0),
        Item_ShoppingCart_020=-2499.88,
    )


@pytest.mark.xfail(strict=True)
def test_32():
    var_0 = "_Cart_ShoppingCart__ShoppingCart_Customer_012"
    var_1 = 144
    var_2 = python_code_.Customer_Payment(
        Paymentid=var_0,
        login=var_0,
        ApplPay=var_1,
        CustomerId="\\B2R0",
        PayPal={-2894.86, True},
        Payment__=-1979.03,
    )
    var_3 = {var_2, var_2, var_2, var_2, var_2}
    var_4 = python_code_.Shopping_Cart_Checkout(
        Paymentid=set(),
        CheckoutID=1717.37,
        billingMethod={},
        CustomerID=var_0,
        Checkout__=var_0,
        Payment_Checkout_15=var_3,
    )
    assert isinstance(var_4, python_code_.Shopping_Cart_Checkout)
    var_7 = "zb{]ja^ufDh&4W5"
    python_code_.Customer_Customer(
        firstname=var_2,
        lastname={False},
        emailAddress=var_0,
        id=-279.12,
        login=var_7,
        password=True,
        Message=var_0,
        Payment_Customer_11=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_33():
    var_0 = 2477.36
    var_1 = 1
    var_2 = int
    var_3 = python_code_.Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_1,
        billingMethod=var_2,
        CustomerID=complex(-2068.2, 1034.0),
        PayBill__=var_2,
    )
    assert isinstance(var_3, python_code_.Cart_Checkout)
    var_5 = "dTNG6n["
    var_6 = "^YpSV:CP%"
    var_7 = "zKhs4p|!D#r$un\nMQ"
    var_8 = python_code_.Customer_Account(
        Login__=var_6, account__=var_7, GUI_Screen_Account_123=var_2
    )
    python_code_.GUI_Screen(
        id=var_2,
        Message=var_5,
        Exit__=[-1, 2],
        Error__=None,
        DisplayList__=var_1,
        GUI_Screen_Account_022=var_8,
    )


def test_34():
    var_26 = "Customer_Customer1Item_ShoppingCart_121Item_Specification_Item_016Item_ShoppingCart_020"
    var_28 = "_Customer_Customer1__Payment_Customer_19"
    var_32 = -4522
    var_33 = 385.68
    var_34 = python_code_.Product_Item_Type(
        quantity=var_32,
        price=var_33,
        id=-383,
        ItemType__=var_26,
        Avail__=var_26,
        Item_Type_Item_018=var_28,
    )
    assert isinstance(var_34, python_code_.Product_Item_Type)


def test_35():
    var_0 = 0
    var_1 = "Customer_Cu1stomer1Item_ShoppingCart_121Item_Specification_Item_016Item_ShoppingCart_020"
    var_2 = float
    var_3 = "_Customer_Customer1__Payment_Customer_19"
    var_4 = python_code_.Product_Item_Type(
        quantity=var_0,
        price=None,
        id=var_0,
        ItemType__=b"\xd2\x14\x1b\xf1x\tTC\x0c\xc9",
        Avail__=var_3,
    )
    var_5 = {var_4, var_4, var_4, var_4, var_4}
    var_6 = python_code_.Product_Item(
        quantity=var_0,
        list__=(),
        id=var_0,
        OutofStock__=var_1,
        totalcost__=var_2,
        Item_Type_Item_119=var_5,
        GUI_Screen_Item_127=(),
    )
    assert isinstance(var_6, python_code_.Product_Item)
    python_code_.Product_Item_Specification(
        quantity=var_2, price=var_2, id=var_2, ItemSpecs__={True, -3174}, Brand__=var_3
    )


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = lambda *args, **kwargs: True
    var_2 = "Customer_Customer"
    var_9 = -4632.62
    var_11 = -4601
    var_15 = 2633
    var_16 = ""
    var_17 = python_code_.Customer_Customer1(
        userId=var_2, PaymentMet__=True, Account__=var_16, select__=True
    )
    python_code_.Cart_ShoppingCart(
        id=var_11,
        creationDate=None,
        CheckoutID=var_15,
        AddCart=var_15,
        RemoveOrder=var_0,
        UpdateOrder=var_0,
        GetTotal__=var_9,
        ShoppingCart_Checkout_010={"^p"},
        ShoppingCart_Customer_012=var_17,
        GUI_Screen_ShoppingCart_125=complex(-25.08184, -3764.0),
    )


@pytest.mark.xfail(strict=True)
def test_37():
    var_0 = repr
    var_1 = python_code_.Shopping_Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_0,
        billingMethod={
            "]Bo#": False,
            "Customer_Payment._Product_Item__GUI_Screen_Item_127.GUI_Screen_Account_022._Customer_Payment1__Payment_Customer_08": -1677,
        },
        CustomerID=var_0,
        Checkout__=var_0,
    )
    assert isinstance(var_1, python_code_.Shopping_Cart_Checkout)
    var_17 = 538
    var_18 = "_Product_Item__Item_ShoppingCart_020"
    var_21 = 650
    var_22 = -3469.33
    var_23 = "Item_Specification_Item_016-Payment_Customer_19-Customer_Payment-Product_Item_Type"
    var_24 = python_code_.Customer_Customer(
        firstname=var_18,
        lastname=var_18,
        emailAddress=var_18,
        id=None,
        login="_Cart_Checkout__ShoppingCart_Checkout_111:_Product_Item__Item_ShoppingCart_020:_GUI_Screen__GUI_Screen_Item_026",
        password="YO:v[QLsD'jSbT)XILT",
        Message=var_23,
        Customer_ShoppingCart_02=var_0,
    )
    python_code_.Shopping_Cart_ShoppingCart(
        id={},
        creationDate=b"\x19\xe7n\x9a\xe0\xcc\x83Y\xff\xa6=\xda\x0c",
        CheckoutID=var_17,
        AddOrder=var_21,
        RemoveOrder=var_0,
        UpdateOrder=var_17,
        GetTotal__=var_22,
        Customer_ShoppingCart_13=var_24,
    )


def test_38():
    var_32 = -4632.62
    var_33 = -1549
    var_34 = -222
    var_35 = python_code_.Cart_ShoppingCart(
        id=1,
        creationDate=var_32,
        CheckoutID=var_33,
        AddCart=var_34,
        RemoveOrder=complex(-2021.0, -2613.8553),
        UpdateOrder=var_34,
        GetTotal__=var_32,
        ShoppingCart_Checkout_010={True},
        ShoppingCart_Customer_012=set(),
        GUI_Screen_ShoppingCart_125={},
    )
    assert isinstance(var_35, python_code_.Cart_ShoppingCart)


def test_39():
    var_0 = "&]wGbs,"
    var_10 = "Customer_Customer"
    var_12 = 2179
    var_13 = hash
    var_14 = python_code_.Customer_User(
        Addresschange__=var_13,
        userid__={"E,~ToxvJ<xx#&": "N", "ShoppingCart_Checkout_010": -337.22},
    )
    var_15 = -1398
    var_16 = python_code_.Product_Item_Type(
        quantity=var_15, price=-3454.65, id=var_12, ItemType__=var_14, Avail__=var_0
    )
    var_17 = 1946.12
    var_18 = python_code_.Product_Item(
        quantity=complex(-670.0888075, 2123.712),
        list__=var_17,
        id=var_15,
        OutofStock__=var_0,
        totalcost__=var_10,
    )
    assert isinstance(var_18, python_code_.Product_Item)
    var_19 = 933
    var_20 = 2633
    var_21 = {var_18, var_18, var_18, var_18}
    var_22 = python_code_.Cart_ShoppingCart(
        id=var_19,
        creationDate=None,
        CheckoutID=var_16,
        AddCart=var_14,
        RemoveOrder=var_20,
        UpdateOrder=var_15,
        GetTotal__=var_17,
        Item_ShoppingCart_121=var_21,
    )
    assert isinstance(var_22, python_code_.Cart_ShoppingCart)


@pytest.mark.xfail(strict=True)
def test_40():
    var_0 = -8
    var_1 = "Customer_Customer1Item_ShoppingCart_121Item_Specification_Item_016Item_ShoppingCart_020"
    var_2 = float
    var_3 = "_Customer_Customer1__Payment_Customer_19"
    var_13 = 538
    var_14 = "_Product_Item__Item_ShoppingCart_020"
    var_16 = -3469.33
    var_18 = python_code_.Product_Item_Type(
        quantity=(-643.97,),
        price=var_16,
        id=var_13,
        ItemType__=var_14,
        Avail__=var_1,
        Item_Type_Item_018=b'\xd17\xb1\x0ev\xf9\xb4\xd4\x05\x00\xc8\xa6-\xbd"\xbc\xca',
    )
    assert isinstance(var_18, python_code_.Product_Item_Type)
    var_19 = "Payment_Customer_08-Item_Type_Item_119"
    var_20 = "_Cart_ShoppingCart__ShoppingCart_Checkout_010Customer_Payment"
    var_21 = "Item_Specification_Item_117:Item_Type_Item_119:_GUI_Screen__GUI_Screen_Item_026"
    var_22 = -2907
    var_23 = -598
    var_24 = 2913.28
    var_25 = python_code_.Shopping_Cart_ShoppingCart(
        id=b"\x04\x17\xc1\xe4?n\xac",
        creationDate=complex(-1454.92, 2535.0),
        CheckoutID=var_2,
        AddOrder=var_22,
        RemoveOrder=var_22,
        UpdateOrder=var_23,
        GetTotal__=var_24,
        Customer_ShoppingCart_13=var_19,
    )
    python_code_.Customer_Customer(
        firstname=var_19,
        lastname=var_20,
        emailAddress=var_18,
        id=var_0,
        login=var_21,
        password=var_3,
        Message=var_20,
        Customer_ShoppingCart_02=var_25,
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_0 = lambda *args, **kwargs: "GUI_Screen_Account_022Customer_Customer1"
    var_9 = -793
    var_10 = "Customr_Customer"
    var_11 = python_code_.Cart_Checkout(
        Paymentid=var_0,
        CheckoutID=var_9,
        billingMethod=var_10,
        CustomerID=var_10,
        PayBill__=var_10,
    )
    assert isinstance(var_11, python_code_.Cart_Checkout)
    var_12 = -2328
    var_13 = "&F3lu[9Yr4?"
    var_15 = python_code_.Customer_Payment(
        Paymentid=2013,
        login="Payment_Checkout_04 _Customer_Payment__Payment_Customer_00",
        ApplPay=var_9,
        CustomerId="ShoppingCart_Checkout_111",
        PayPal=var_12,
        Payment__=-922.26,
        Payment_Checkout_04=var_11,
    )
    python_code_.Customer_Customer(
        firstname=-2102.45,
        lastname=var_0,
        emailAddress=var_13,
        id={"_Shopping_Cart_ShoppingCart__Customer_ShoppingCart_13": "'/YvG%X\x0cLLv"},
        login=var_0,
        password=var_10,
        Message=(
            3,
            "GUI_Screen_ShoppingCart_024:Item_Specification_Item_117:Checkout_Payment_014",
            -1158.27,
        ),
        Payment_Customer_11=var_15,
    )


def test_42():
    var_17 = "_Cart_Shopping>Cart__ShoppingCart_Checkout_0~10.ShoppingCart_Customer_113"
    var_18 = 2008.2442277415023
    var_19 = -929
    var_20 = python_code_.Product_Item_Specification(
        quantity=-94,
        price=var_18,
        id=var_19,
        ItemSpecs__=var_17,
        Brand__="Payment_Customer_08.Item_Specification_Item_016._Customer_Payment__Payment_Checkout_04",
        Item_Specification_Item_016=var_18,
    )
    assert isinstance(var_20, python_code_.Product_Item_Specification)


def test_43():
    var_12 = -1009.13
    var_13 = "A`ATL\\K"
    var_14 = "ShoppingCart_Checkout_111"
    python_code_.GUI_Screen(
        id={"'\"", "UkvEY`85E:b=l"},
        Message=var_14,
        Exit__=var_12,
        Error__=var_13,
        DisplayList__="_Cart_ShoppingCart__ShoppingCart_Customer_012",
        GUI_Screen_ShoppingCart_024=var_12,
        GUI_Screen_Item_026=b"\xcb\xc7\x03\x87\x04\x10\x98\xb0-\xc7\x83T\xdd^",
    )


@pytest.mark.xfail(strict=True)
def test_44():
    var_0 = lambda *args, **kwargs: True
    var_8 = "Payment_Customer_11._GUI_Screen__GUI_Screen_ShoppingCart_024.GUI_Screen_Account_123.Customer_Customer"
    var_10 = -805.13
    var_11 = "INlRm("
    var_12 = "_Customer_Payment__Payment_Checkout_04,Payment_Customer_11,Customer_Payment,Cart_Checkout"
    var_13 = 3
    var_14 = python_code_.Product_Item(
        quantity=var_13,
        list__=var_10,
        id=var_13,
        OutofStock__=var_8,
        totalcost__=var_0,
        Item_ShoppingCart_020=var_11,
        GUI_Screen_Item_127=1937.85,
    )
    assert isinstance(var_14, python_code_.Product_Item)
    python_code_.GUI_Screen(
        id=var_8,
        Message=var_11,
        Exit__=var_12,
        Error__=var_8,
        DisplayList__=var_13,
        GUI_Screen_Item_026=var_14,
    )


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = python_code_.Customer_Customer1
    var_1 = '0MU\rd<"\x0bW8`'
    var_2 = python_code_.Product_Item_Type(
        quantity=None, price=var_0, id=var_0, ItemType__=var_1, Avail__=var_0
    )
    var_3 = 4058.27
    var_4 = python_code_.Product_Item_Specification(
        quantity=var_0, price=var_3, id=var_1, ItemSpecs__=var_2, Brand__=var_1
    )
    python_code_.Customer_User(
        Addresschange__=complex(-1396.915, 303.536), userid__=None
    )
    var_6 = 1275.94
    var_7 = "xW{>@q_n"
    var_8 = python_code_.Product_Item_Specification(
        quantity=complex(594.238975, 5013.9),
        price=var_6,
        id=var_0,
        ItemSpecs__=var_3,
        Brand__=var_7,
    )
    var_9 = 2316.2
    var_10 = 121
    var_11 = "u%X"
    var_12 = python_code_.Product_Item_Specification(
        quantity=var_7, price=var_9, id=var_10, ItemSpecs__=var_6, Brand__=var_11
    )
    var_13 = {var_8, var_4, var_12, var_4}
    var_14 = lambda *args, **kwargs: 58
    var_15 = -5151.65
    var_16 = python_code_.Cart_ShoppingCart(
        id=b"\x87\xe2\x1e\x16\xb0\xfa\x97\xb6\xa2",
        creationDate=var_0,
        CheckoutID=var_0,
        AddCart=var_0,
        RemoveOrder=var_14,
        UpdateOrder=var_2,
        GetTotal__=var_15,
        ShoppingCart_Checkout_010={},
        ShoppingCart_Customer_012=var_3,
    )
    assert isinstance(var_16, python_code_.Cart_ShoppingCart)
    var_17 = python_code_.Product_Item(
        quantity=2224.78,
        list__=var_6,
        id=None,
        OutofStock__=var_1,
        totalcost__=var_1,
        Item_Specification_Item_117=var_13,
        Item_Type_Item_119=var_1,
        Item_ShoppingCart_020=var_16,
    )
    assert isinstance(var_17, python_code_.Product_Item)
    var_19 = "'S8ag3"
    var_20 = "st~fU"
    var_21 = python_code_.GUI_Screen(
        id=True,
        Message=b"\xbf\xdc\xf8Mi\x92}\xcc\xa1\x7f\xe2",
        Exit__="Py@St_;",
        Error__={},
        DisplayList__=var_10,
    )
    python_code_.Customer_Account(
        Login__=var_20, account__=var_19, GUI_Screen_Account_123=var_21
    )


def test_46():
    var_24 = "[QJ<14m2&QN hp"
    var_25 = -4522
    var_26 = 385.68
    var_27 = python_code_.Product_Item_Type(
        quantity=var_25, price=var_26, id=var_25, ItemType__=3, Avail__=var_26
    )
    var_28 = ".(p)T,\\]=xi"
    var_29 = -1132.66
    python_code_.Customer_Customer1(
        userId=var_28,
        PaymentMet__=var_29,
        Account__=(-1, 1591),
        select__={
            0,
            "Product_Item:ShoppingCart_Customer_113:_GUI_Screen__GUI_Screen_ShoppingCart_024:Customer_Payment",
        },
    )
    var_31 = python_code_.Customer_User
    var_32 = "h|k<^;W0uxs"
    python_code_.Customer_Customer(
        firstname=var_31,
        lastname=var_27,
        emailAddress="Q`yWVLy",
        id=var_25,
        login=var_26,
        password=var_24,
        Message=var_32,
    )
    var_34 = 2032.87
    var_35 = python_code_.Shopping_Cart_Checkout(
        Paymentid=var_25,
        CheckoutID=var_31,
        billingMethod=var_27,
        CustomerID=var_31,
        Checkout__=var_34,
    )
    assert isinstance(var_35, python_code_.Shopping_Cart_Checkout)
    var_36 = "GUI_Screen_Item_127"
    python_code_.Shopping_Cart_Checkout(
        Paymentid={"}^O.D", -649, "u=@%g4"},
        CheckoutID=(),
        billingMethod=var_36,
        CustomerID=var_25,
        Checkout__={
            "Item_ShoppingCart_020": "pe;n{",
            "Shopping_Cart_ShoppingCart_Customer_Payment__Payment_Customer_00Item_Type_Item_018": False,
        },
        ShoppingCart_Checkout_17=complex(2095.421, -5257.3143),
    )
    var_38 = 1
    var_39 = -1637
    python_code_.Customer_Payment(
        Paymentid=var_38,
        login=var_31,
        ApplPay=var_39,
        CustomerId=var_24,
        PayPal=var_31,
        Payment__=var_35,
        Payment_Customer_00=var_32,
    )


@pytest.mark.xfail(strict=True)
def test_47():
    var_6 = 780
    var_7 = -908.2721128566218
    var_63 = 2667
    var_64 = "Q%IkPh"
    var_65 = python_code_.Product_Item_Specification(
        quantity=var_6,
        price=var_7,
        id=complex(952.33678, 2573.9),
        ItemSpecs__=1604,
        Brand__=var_64,
    )
    var_66 = python_code_.Cart_Checkout
    var_67 = 2
    var_68 = 2694.19
    var_69 = python_code_.Cart_ShoppingCart(
        id=var_66,
        creationDate=var_65,
        CheckoutID=var_67,
        AddCart=var_66,
        RemoveOrder=var_6,
        UpdateOrder=b"\xd7g\xee\x7f\xd9\xa6g\x90\x07\x89W\xa0\xa2\x9b",
        GetTotal__=var_68,
        Item_ShoppingCart_121=[2972.23, True],
    )
    assert isinstance(var_69, python_code_.Cart_ShoppingCart)
    var_70 = "_GUI_Screen__GUI_Screen_Account_022.Item_ShoppingCart_121._Product_Item_Specification__Item_Specification_Item_016.ShoppingCart_Customer_012"
    var_71 = python_code_.Product_Item(
        quantity="iYl@|P?%_L?a.`GaXe",
        list__=set(),
        id=var_67,
        OutofStock__={False, False},
        totalcost__=var_70,
    )
    assert isinstance(var_71, python_code_.Product_Item)
    python_code_.GUI_Screen(
        id=(),
        Message=-2379,
        Exit__=var_66,
        Error__=set(),
        DisplayList__=var_63,
        GUI_Screen_ShoppingCart_024=var_69,
        GUI_Screen_Item_026=var_71,
    )


@pytest.mark.xfail(strict=True)
def test_48():
    var_0 = 248
    var_1 = "r(jw_*>_C~FG]H`;u"
    var_2 = python_code_.GUI_Screen(
        id=var_0,
        Message=set(),
        Exit__=var_1,
        Error__={},
        DisplayList__=var_1,
        GUI_Screen_Account_022=[],
    )
    var_3 = bool
    python_code_.Customer_Customer1(
        userId=False,
        PaymentMet__=2002.41,
        Account__=var_3,
        select__=None,
        Payment_Customer_19=b"\x8e",
        ShoppingCart_Customer_113=var_3,
    )
    python_code_.Customer_Account(
        Login__=var_1, account__={}, GUI_Screen_Account_123=var_2
    )


def test_49():
    var_0 = ""
    var_1 = "3*Ze'I)qK0Z"
    var_2 = bytes
    var_3 = -1571
    var_4 = python_code_.Customer_Customer(
        firstname=var_0,
        lastname=var_1,
        emailAddress=var_2,
        id=var_3,
        login=var_0,
        password=var_1,
        Message=var_0,
    )
    var_5 = python_code_.Customer_Payment(
        Paymentid=var_2,
        login=[-3913.66],
        ApplPay={},
        CustomerId=var_4,
        PayPal=var_2,
        Payment__=var_0,
        Payment_Checkout_04=(False,),
    )
    var_6 = -1
    var_7 = python_code_.Customer_Payment(
        Paymentid=var_6,
        login=set(),
        ApplPay="",
        CustomerId=b"\xacZ\xbf\xba\x88\x12\xa80l\xc6;\x89\xf9\xca\x92\xb6\x86\x03",
        PayPal=var_6,
        Payment__=None,
    )
    var_8 = {var_5, var_7, var_5, var_7, var_7}
    var_9 = python_code_.Shopping_Cart_Checkout(
        Paymentid=complex(-2958.281933, 3223.517),
        CheckoutID=var_3,
        billingMethod=var_2,
        CustomerID=var_3,
        Checkout__=var_4,
        Payment_Checkout_15=var_8,
    )
    assert isinstance(var_9, python_code_.Shopping_Cart_Checkout)
    var_10 = "_GUI_Screen__GUI_Screen_Item_026-Payment_Customer_19"
    python_code_.GUI_Screen(
        id=var_6,
        Message=var_1,
        Exit__=var_10,
        Error__=var_10,
        DisplayList__=var_2,
        GUI_Screen_ShoppingCart_024=var_2,
        GUI_Screen_Item_026=var_2,
    )
    var_12 = lambda *args, **kwargs: [151.31, -2352]
    var_13 = 2356
    var_14 = python_code_.Cart_Checkout(
        Paymentid=var_2,
        CheckoutID=var_13,
        billingMethod=var_0,
        CustomerID=var_7,
        PayBill__="&i8*%8`",
        ShoppingCart_Checkout_111=var_8,
    )
    assert isinstance(var_14, python_code_.Cart_Checkout)
    var_15 = python_code_.Customer_Payment1(
        PayBill__=var_4, Auth__=var_4, ID=var_12, Checkout_Payment_115=var_14
    )
    assert isinstance(var_15, python_code_.Customer_Payment1)
