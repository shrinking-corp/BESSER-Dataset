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
    admin,
    annotations,
    cash,
    credit_card,
    customer,
    date,
    datetime,
    flights,
    payement,
    ticket,
    time,
)


def test_0():
    var_14 = python_code_.flights(
        number=3465,
        time=361,
        name="customer5",
        dest="]5`Jwe=]] ",
        depart='vQ[d<u sv".~;{',
        customer7={False, ".{w'ID-", -3949.69},
    )
    assert isinstance(var_14, python_code_.flights)


def test_1():
    var_14 = python_code_.flights(
        number=997,
        time=542,
        name="_flights__customer7:payement1:_flights__admin9:_customer__flights6",
        dest="\x0b&N/fiep:Ao8^",
        depart="YV}||<-k1M'vP",
        admin9=None,
    )
    assert isinstance(var_14, python_code_.flights)


def test_2():
    var_1 = -13
    var_14 = python_code_.flights(
        number=-615,
        time=var_1,
        name="9Iu*#-mS",
        dest="admin _flights__admin9 _flights__customer7 ticket",
        depart="'MJp_4\n+lM}M",
        admin9=var_1,
    )
    assert isinstance(var_14, python_code_.flights)


def test_3():
    var_14 = python_code_.admin(
        username="customer0.flights6.payement",
        pwd="customer5",
        name_of_flight="app ZB=UKYJ]=VCx3QN",
        type="customer7-_ticket__customer3",
        seats=920,
        cost=-569,
        customer5={True, False},
        flights8={1206, 705, 1312.44},
    )
    assert isinstance(var_14, python_code_.admin)


def test_4():
    var_14 = python_code_.admin(
        username="G",
        pwd="_admin__customer5",
        name_of_flight="_ticket__customer3.customer3._customer__admin4.payement",
        type="y .1\x0b hbL-LI",
        seats=0,
        cost=-603,
    )
    assert isinstance(var_14, python_code_.admin)


def test_5():
    var_6 = python_code_.ticket(
        tiketno_=3,
        source="Z\\2\\?2A)pUR7S",
        dest=">+}B}a?%a",
        custid=1645,
        attribute=",/aDW}qa53 W=t^#",
        customer3=set(),
    )
    assert isinstance(var_6, python_code_.ticket)


def test_6():
    var_6 = python_code_.ticket(
        tiketno_=-1579,
        source="_payement__customer0",
        dest="ticket,_customer__ticket2",
        custid=0,
        attribute="customer7,_customer__flights6,_flights__customer7",
    )
    assert isinstance(var_6, python_code_.ticket)


@pytest.mark.xfail(strict=True)
def test_7():
    var_14 = python_code_.admin(
        username="flights8",
        pwd="fR{}f'6*B3%tpO+",
        name_of_flight="l}8E\rRlfK~5yYpHH ",
        type="#7C",
        seats=626,
        cost=-2215,
    )
    assert isinstance(var_14, python_code_.admin)
    var_18 = "}"
    var_19 = python_code_.customer(
        name=var_18,
        address=set(),
        age=var_14,
        source=None,
        payement1=None,
        admin4=var_14,
    )
    assert isinstance(var_19, python_code_.customer)
    python_code_.payement(
        customer_info={},
        pay_amt=complex(-2375.5637465, 321.2),
        transc_id=var_14,
        pay_date=var_14,
        paymethod=var_18,
        customer0=var_19,
    )


def test_8():
    var_0 = "#HF`Bz.q!%9mb"
    var_1 = 2
    var_2 = "uT8!o4M4"
    python_code_.payement(
        customer_info=var_0,
        pay_amt=("_payement__customer0", True, -1357.25),
        transc_id=True,
        pay_date=var_1,
        paymethod=var_2,
    )


def test_9():
    python_code_.customer(name=[], address=(), age=False, source=())


def test_10():
    var_4 = "`RK3>jQPV"
    var_8 = python_code_.flights(
        number=2188,
        time=-1923,
        name='\\mF"^B.$scQ;-\tC_',
        dest="arXo~\r`;mtS~m",
        depart='nxJy\t}VZ_(yvw-"N',
    )
    assert isinstance(var_8, python_code_.flights)
    var_9 = python_code_.customer(
        name=var_4, address="", age=75, source=var_4, flights6=var_8
    )
    assert isinstance(var_9, python_code_.customer)


def test_11():
    var_3 = abs
    var_4 = "F.nd"
    var_6 = python_code_.ticket(
        tiketno_=-2235,
        source="\n\\jveFdO$\x0c+c0xQ",
        dest="AKC\x0bn(YZn%iQi0",
        custid=87,
        attribute="customer7._admin__flights8.customer5",
    )
    assert isinstance(var_6, python_code_.ticket)
    var_7 = python_code_.customer(
        name=var_3,
        address=var_4,
        age={"customer3._ticket__customer3.payement": False},
        source=var_3,
        payement1=1869.34,
        ticket2=var_6,
    )
    assert isinstance(var_7, python_code_.customer)


def test_12():
    var_3 = abs
    var_13 = 2708
    var_14 = b"T"
    var_15 = -208
    var_16 = python_code_.admin(
        username=";te 3{&NqiiM(X;",
        pwd="?}t@_3j\x0b5NF>cd=J/",
        name_of_flight=var_13,
        type="_flights__customer7._ticket__customer3._payement__customer0._flights__customer7",
        seats=1711,
        cost=var_15,
    )
    assert isinstance(var_16, python_code_.admin)
    var_17 = python_code_.customer(
        name=var_3,
        address=var_13,
        age=var_3,
        source=var_14,
        payement1=var_3,
        ticket2=var_14,
        admin4=var_16,
    )
    assert isinstance(var_17, python_code_.customer)
    var_18 = {var_17, var_17}
    python_code_.admin(
        username=var_13,
        pwd="z",
        name_of_flight=var_13,
        type=(),
        seats=b"}\xf6\x8c\x0fR\x07Y\xc8\xd33\xa8m\xe2\x06D",
        cost=complex(-3982.5, 1908.6543889),
        customer5=var_18,
    )


def test_13():
    var_18 = "flights6ticket2_customer__flights6payement"
    var_19 = "c_"
    var_20 = repr
    var_21 = python_code_.admin(
        username=var_20,
        pwd=set(),
        name_of_flight=set(),
        type=-3001,
        seats=var_20,
        cost=var_18,
    )
    assert isinstance(var_21, python_code_.admin)
    var_14 = python_code_.customer(
        name=var_18,
        address=complex(116.9, -2109.68),
        age=b"3\xc4\xed)\xa7",
        source=var_19,
        admin4=var_21,
    )
    assert isinstance(var_14, python_code_.customer)


def test_14():
    python_code_.credit_card()


def test_15():
    var_1 = -54
    var_11 = python_code_.admin(
        username="D",
        pwd="Y'qK,Lm5p*@ `n1M:nS",
        name_of_flight="_ticket__customer3",
        type='v`T8~|"|V#d<i6,f$iD',
        seats=var_1,
        cost=var_1,
        flights8=set(),
    )
    assert isinstance(var_11, python_code_.admin)
    var_12 = "MK,7s:E"
    var_13 = lambda *args, **kwargs: False
    var_14 = python_code_.flights(
        number=var_1,
        time=var_11,
        name=var_12,
        dest=var_13,
        depart=var_13,
        admin9=var_11,
    )
    assert isinstance(var_14, python_code_.flights)


def test_16():
    var_0 = "_customer__flights6_customer__ticket2"
    var_1 = -1168
    var_2 = python_code_.customer(name=var_0, address=1, age=var_1, source=var_1)
    var_3 = object
    var_4 = {var_2}
    var_5 = python_code_.admin(
        username=var_0,
        pwd=var_0,
        name_of_flight=None,
        type=None,
        seats=b"\x86\x8fw#B\x7f",
        cost=var_3,
        customer5=var_4,
    )
    assert isinstance(var_5, python_code_.admin)


def test_17():
    var_0 = python_code_.admin
    var_15 = "payement1.admin.customer"
    var_18 = python_code_.flights(
        number=-4035, time=1011, name=var_15, dest=var_15, depart=var_15, admin9=var_0
    )
    assert isinstance(var_18, python_code_.flights)


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = 'rOB_k ,?~E8i"r .A'
    var_1 = "_customer__payement1-_admin__customer5-_admin__flights8"
    var_2 = complex
    var_3 = -3757
    var_4 = 0
    var_5 = python_code_.payement(
        customer_info=var_0,
        pay_amt={179, 382.22, -1},
        transc_id=var_3,
        pay_date=var_4,
        paymethod=var_2,
        customer0=var_2,
    )
    assert isinstance(var_5, python_code_.payement)
    python_code_.customer(
        name=var_0, address=var_1, age=var_0, source=var_2, payement1=var_5
    )


def test_19():
    var_14 = python_code_.admin(
        username='A;"e^Be^>',
        pwd="_customer__flights6",
        name_of_flight="",
        type="r",
        seats=-3258,
        cost=-779,
        customer5={"Nh2m0nX!Jm"},
    )
    assert isinstance(var_14, python_code_.admin)
    var_17 = "oHt$Vm=H"
    var_18 = "flights8:_customer__admin4"
    var_19 = "_customer__payement1:ticket2"
    var_20 = python_code_.customer(
        name=var_17,
        address=var_18,
        age="M&LVtq0",
        source=var_19,
        admin4=var_14,
        flights6=var_18,
    )
    assert isinstance(var_20, python_code_.customer)


def test_20():
    var_0 = "KR=|UTLHBO"
    var_1 = sorted
    var_2 = "admin9,flights6"
    var_3 = "Kb^u~8CX^i8#gsLHov"
    var_4 = -2923
    var_5 = python_code_.admin(
        username="_payement__customer0",
        pwd=var_2,
        name_of_flight="\\G|i8?",
        type=var_3,
        seats=2,
        cost=var_4,
        flights8=set(),
    )
    assert isinstance(var_5, python_code_.admin)
    var_6 = python_code_.customer(
        name=var_1,
        address=var_2,
        age=var_1,
        source=var_3,
        payement1=var_1,
        ticket2=var_0,
        admin4=var_5,
    )
    assert isinstance(var_6, python_code_.customer)


@pytest.mark.xfail(strict=True)
def test_21():
    var_21 = (
        lambda *args, **kwargs: "payement,_customer__payement1,_admin__customer5,flights"
    )
    var_22 = "lK7Z bQk)XT1V(zd'"
    var_23 = "o6[[VxH"
    var_24 = 1580
    var_25 = python_code_.admin(
        username=var_22,
        pwd=var_21,
        name_of_flight=var_22,
        type=var_23,
        seats=var_24,
        cost=True,
    )
    assert isinstance(var_25, python_code_.admin)
    var_26 = -326
    var_27 = "_admin__flights8,admin"
    var_28 = ")"
    var_29 = 3507
    var_30 = python_code_.customer(
        name=var_23,
        address=var_21,
        age=var_29,
        source=var_21,
        payement1=var_21,
        admin4=var_25,
    )
    assert isinstance(var_30, python_code_.customer)
    var_31 = "'X3b5g"
    var_32 = "_ticket__customer3 _payement__customer0"
    var_33 = "VjFq$iZ\x0cvr0\r"
    var_34 = python_code_.flights(
        number=("&QV~fF/9M",), time=var_21, name=var_25, dest=var_23, depart=var_33
    )
    assert isinstance(var_34, python_code_.flights)
    var_35 = {var_34, var_34}
    var_36 = python_code_.admin(
        username=var_26,
        pwd=var_21,
        name_of_flight=var_23,
        type=var_32,
        seats=var_26,
        cost=var_29,
        flights8=var_35,
    )
    assert isinstance(var_36, python_code_.admin)
    var_37 = python_code_.customer(
        name=var_27,
        address=var_28,
        age=var_21,
        source=var_31,
        ticket2=(),
        admin4=var_36,
    )
    assert isinstance(var_37, python_code_.customer)
    var_38 = {var_30, var_30, var_30, var_37, var_30}
    var_39 = python_code_.ticket(
        tiketno_=var_26,
        source=(-631.02,),
        dest=var_28,
        custid=(),
        attribute=var_23,
        customer3=var_38,
    )
    assert isinstance(var_39, python_code_.ticket)
    python_code_.customer(
        name=var_22, address=var_27, age=var_24, source=var_21, ticket2=var_39
    )
    python_code_.payement(
        customer_info=2,
        pay_amt=var_26,
        transc_id=var_26,
        pay_date=[-5165.79, True],
        paymethod={-912, False},
        customer0=var_30,
    )


def test_22():
    var_1 = 2
    var_7 = repr
    var_8 = "iTY~Iy"
    var_9 = python_code_.customer(
        name=var_7,
        address=b"\x8dq+\xb9\xd0\xda\xfd\xaa\xc4",
        age=var_1,
        source=var_8,
        payement1=False,
        admin4=var_8,
    )
    assert isinstance(var_9, python_code_.customer)


def test_23():
    var_4 = "Jii-"
    var_9 = -1
    var_10 = -4808
    var_11 = python_code_.flights(
        number=var_9, time=var_10, name=var_4, dest=var_4, depart=var_4, admin9={}
    )
    assert isinstance(var_11, python_code_.flights)
    var_12 = {var_11}
    var_13 = python_code_.admin(
        username=var_4,
        pwd=var_4,
        name_of_flight=b"\xabs(\x102\xe5\xa4",
        type=[5234, -887, "_admin__customer5.customer0"],
        seats=set(),
        cost=var_4,
        customer5={"flights", False},
        flights8=var_12,
    )
    assert isinstance(var_13, python_code_.admin)


def test_24():
    var_4 = "`RK3>QPV"
    var_8 = python_code_.flights(
        number=2188,
        time=-1923,
        name='\\mF"^B.$scQ;-\tC_',
        dest="arXo~\r`;mtS~m",
        depart='nxJy\t}VZ_(yvw-"N',
    )
    assert isinstance(var_8, python_code_.flights)
    var_9 = python_code_.customer(
        name=var_4, address="", age=75, source=var_4, flights6=var_8
    )
    assert isinstance(var_9, python_code_.customer)
    var_10 = 3338
    var_11 = {var_9, var_9, var_9, var_9, 1376}
    var_12 = python_code_.flights(
        number=var_10,
        time=var_10,
        name="EhsI\x0cpJF\\5Vo~9",
        dest=var_4,
        depart="_payement__customer0:payement:_flights__admin9:_customer__flights6",
        customer7=var_11,
        admin9=None,
    )
    assert isinstance(var_12, python_code_.flights)


def test_25():
    var_3 = abs
    var_4 = "F.nd"
    var_6 = python_code_.ticket(
        tiketno_=-2235,
        source="\n\\jveFdO$\x0c+c0xQ",
        dest="AKC\x0bn(YZn%iQi0",
        custid=87,
        attribute="customer7._admin__flights8.customer5",
    )
    assert isinstance(var_6, python_code_.ticket)
    var_7 = python_code_.customer(
        name=var_3,
        address=var_4,
        age={"customer3._ticket__customer3.payement": False},
        source=var_3,
        payement1=1869.34,
        ticket2=var_6,
    )
    assert isinstance(var_7, python_code_.customer)
    var_8 = 1
    var_9 = {var_7, var_7, var_7}
    python_code_.ticket(
        tiketno_=var_6,
        source=var_4,
        dest=var_7,
        custid=var_8,
        attribute=var_7,
        customer3=var_9,
    )
    var_11 = -732
    python_code_.payement(
        customer_info='Vj`O"g(',
        pay_amt=var_9,
        transc_id=var_11,
        pay_date=complex(675.1802071, 1256.8877311),
        paymethod=var_4,
    )


def test_26():
    var_14 = python_code_.flights(
        number=2,
        time=-1703,
        name='Do3?giw9uT"/W:\x0br\x0c~',
        dest="jw pYVlN[uER|/h0",
        depart="tROk`[Z>j5\\E\\G?Iz",
    )
    assert isinstance(var_14, python_code_.flights)
    var_16 = bool
    var_17 = "nuGkA;}Zu;NT^-n~RG<"
    var_18 = -1249
    var_19 = "d\x0c>+P')uB@"
    var_20 = "\\]s3Z"
    var_21 = "admin"
    var_22 = python_code_.customer(
        name=var_21,
        address=var_19,
        age=var_18,
        source=var_20,
        payement1=None,
        ticket2=var_16,
    )
    assert isinstance(var_22, python_code_.customer)
    var_23 = {var_22}
    var_24 = python_code_.ticket(
        tiketno_={-2087.43, 2336.19, -1126.63},
        source=var_16,
        dest=var_19,
        custid=3124.16,
        attribute=var_20,
        customer3=var_23,
    )
    assert isinstance(var_24, python_code_.ticket)
    var_25 = python_code_.customer(
        name=var_16, address=var_17, age=var_18, source=var_19, ticket2=var_24
    )
    assert isinstance(var_25, python_code_.customer)
    var_26 = python_code_.credit_card
    var_27 = python_code_.ticket(
        tiketno_=var_18,
        source=var_26,
        dest=var_26,
        custid=var_23,
        attribute=var_19,
        customer3=var_23,
    )
    assert isinstance(var_27, python_code_.ticket)


def test_27():
    var_17 = "flights\\,ticket2,_flights__customer7"
    var_18 = lambda *args, **kwargs: []
    var_19 = python_code_.ticket(
        tiketno_=(False, True),
        source=var_17,
        dest=var_17,
        custid=var_18,
        attribute=var_17,
    )
    assert isinstance(var_19, python_code_.ticket)
    var_20 = "yv"
    var_21 = "eLp'[%*X"
    var_22 = python_code_.ticket(
        tiketno_=complex(-4142.604, -2389.5969),
        source=var_20,
        dest=var_19,
        custid={},
        attribute=var_21,
    )
    var_24 = ""
    var_25 = 1399
    var_26 = 3
    var_27 = python_code_.customer(
        name=var_22, address=var_20, age=var_26, source=var_24, admin4=None
    )
    var_28 = python_code_.customer(
        name=var_21,
        address=var_20,
        age=var_18,
        source={},
        payement1=var_20,
        admin4=var_18,
    )
    assert isinstance(var_28, python_code_.customer)
    var_29 = {var_27, var_27, var_28}
    var_30 = python_code_.admin(
        username=var_24,
        pwd=var_18,
        name_of_flight=var_22,
        type=-3020,
        seats=var_18,
        cost=var_25,
        customer5=var_29,
    )
    assert isinstance(var_30, python_code_.admin)


def test_28():
    var_0 = "KR=|UTLHBO"
    var_47 = lambda *args, **kwargs: []
    var_48 = 1865
    var_49 = "3pVowE4>"
    var_50 = abs
    var_51 = python_code_.customer(
        name=var_47,
        address=var_0,
        age=complex(1654.8321, -1101.195),
        source=var_49,
        admin4=var_50,
    )
    assert isinstance(var_51, python_code_.customer)
    var_52 = ",g\x0cOhtlC#G"
    var_53 = ">gjD7E]y'/"
    var_54 = python_code_.admin(
        username=var_47,
        pwd=b"w\xbb\x1c\xd8Z\xdc;\x85\x88\xac\x89M$R\xdb\xf5\xda:a",
        name_of_flight=var_53,
        type=var_50,
        seats=None,
        cost=complex(128.3373, -1554.47),
    )
    assert isinstance(var_54, python_code_.admin)
    var_55 = python_code_.customer(
        name=var_52,
        address=var_52,
        age=b"\xe8w\xcf\x88(",
        source=var_52,
        admin4=var_54,
        flights6=var_47,
    )
    assert isinstance(var_55, python_code_.customer)
    var_56 = {var_51, var_51, var_51, var_55}
    var_57 = python_code_.flights(
        number=None, time=var_48, name=529.8, dest=var_0, depart=var_0, customer7=var_56
    )
    assert isinstance(var_57, python_code_.flights)
    var_58 = {var_57}
    var_59 = python_code_.admin(
        username=var_0,
        pwd=[],
        name_of_flight=var_47,
        type=[],
        seats=1393,
        cost=b"\x94\xd8y",
        flights8=var_58,
    )
    assert isinstance(var_59, python_code_.admin)


def test_29():
    var_0 = "_flights__admin9"
    python_code_.customer(
        name=var_0, address=var_0, age=var_0, source=(1249.77, ":", 361)
    )
    var_3 = -2857
    var_4 = 3
    var_5 = "flights8_payement__customer0_flights__admin9flights"
    var_6 = python_code_.payement(
        customer_info=var_0,
        pay_amt=None,
        transc_id=var_3,
        pay_date=var_4,
        paymethod=var_5,
    )
    var_7 = list
    var_8 = 3974
    var_9 = python_code_.admin(
        username=var_4,
        pwd=-2000.06,
        name_of_flight=var_7,
        type=var_7,
        seats=var_8,
        cost=var_0,
    )
    assert isinstance(var_9, python_code_.admin)
    var_12 = '$"1MXnX\nIV \x0c`vZXI'
    var_13 = "e\r[0\rY6k3{?E\\r\r~5"
    var_14 = "D"
    var_15 = "8iiGbHP`&Fy$V"
    var_16 = python_code_.flights(
        number=var_6,
        time=var_8,
        name=var_13,
        dest=var_14,
        depart=var_15,
        customer7=var_13,
    )
    assert isinstance(var_16, python_code_.flights)
    var_17 = python_code_.customer(
        name=var_12, address=var_5, age=var_4, source=var_12, flights6=var_16
    )
    assert isinstance(var_17, python_code_.customer)
    var_18 = "payement:customer3"
    var_19 = python_code_.ticket(
        tiketno_=None,
        source=var_7,
        dest=var_18,
        custid=var_7,
        attribute=var_5,
        customer3=[0, -125],
    )
    assert isinstance(var_19, python_code_.ticket)


def test_30():
    var_0 = python_code_.admin
    var_4 = "Jii-"
    var_5 = "_customer__admin4"
    var_6 = python_code_.flights(
        number=-4035, time=1011, name=var_4, dest=var_4, depart=var_5, admin9=var_0
    )
    assert isinstance(var_6, python_code_.flights)
    var_7 = python_code_.customer(
        name={-1912, "8\t v`0Uc\x0ce-^", "%?\rvmnzG?\n ER;:\rw"},
        address=var_4,
        age=set(),
        source=var_4,
        flights6=var_6,
    )
    assert isinstance(var_7, python_code_.customer)
    var_9 = ".)$5<*:6\"'-#j"
    var_10 = 1877
    var_11 = {var_6, var_6, var_6, var_6, var_6}
    var_12 = python_code_.admin(
        username=var_0,
        pwd=var_9,
        name_of_flight=complex(-841.68, -1890.4),
        type=var_4,
        seats={
            "S;<J#EkEY\r1i'": "Lt AGOtskf\nugM",
            "_flights__customer7-_admin__customer5-customer": "R",
            "mrP<xg~VE+=4": 3275,
        },
        cost=var_10,
        flights8=var_11,
    )
    assert isinstance(var_12, python_code_.admin)


def test_31():
    var_0 = 137
    var_1 = "g"
    var_2 = "_customer__admin4-_flights__admin9"
    var_3 = "e\x0b!+xXG<\t3"
    var_4 = python_code_.customer(
        name=var_0,
        address=var_3,
        age=var_0,
        source=var_3,
        payement1={"%F$hmi}><]ddA'XX^"},
    )
    assert isinstance(var_4, python_code_.customer)
    var_5 = "X6zdLRKZDv;9\x0b"
    var_6 = python_code_.cash
    var_7 = python_code_.customer(
        name=var_2,
        address=var_5,
        age=complex(352.3238, 1801.0984158),
        source=var_5,
        admin4=var_6,
    )
    var_8 = {var_4, var_4, var_7, var_4, var_7}
    var_9 = python_code_.admin(
        username=var_1,
        pwd=var_2,
        name_of_flight=var_1,
        type=var_2,
        seats=3141.7,
        cost=var_1,
        customer5=var_8,
        flights8=var_8,
    )
    assert isinstance(var_9, python_code_.admin)
    var_10 = python_code_.flights(
        number=var_0, time=var_0, name=var_1, dest=var_1, depart=var_2, admin9=var_9
    )
    assert isinstance(var_10, python_code_.flights)
    var_12 = python_code_.customer(
        name=var_2, address=var_0, age=var_1, source=var_2, payement1={}, admin4=var_9
    )
    var_13 = set
    var_14 = "{^PePTJ)Lq!]([RE$"
    var_15 = "m"
    var_16 = -2744
    var_17 = -2385
    python_code_.admin(
        username=var_13,
        pwd=var_9,
        name_of_flight=var_14,
        type=var_15,
        seats=var_16,
        cost=var_17,
        flights8=var_8,
    )
    var_19 = ":x4u?)RR+iCXD?qP"
    var_20 = python_code_.flights(
        number=var_14,
        time=var_12,
        name=var_3,
        dest=var_13,
        depart=var_19,
        customer7=var_8,
    )
    assert isinstance(var_20, python_code_.flights)


def test_32():
    var_3 = abs
    var_4 = "`UK3>QPV"
    var_8 = python_code_.flights(
        number=-13, time=688, name=var_4, dest=var_4, depart="r%^aMZc8]P>o+'"
    )
    assert isinstance(var_8, python_code_.flights)
    var_9 = python_code_.customer(
        name=var_4, address="", age=75, source=var_4, flights6=var_8
    )
    assert isinstance(var_9, python_code_.customer)
    var_10 = 3338
    var_11 = {var_9, var_9, var_9, 1376}
    var_12 = python_code_.flights(
        number=var_10,
        time=var_10,
        name="EhsI\x0cpJF\\5Vo~9",
        dest=var_4,
        depart="_payement__customer0:payement:_flights__admin9:_customer__flights6",
        customer7=var_11,
        admin9=None,
    )
    assert isinstance(var_12, python_code_.flights)
    var_13 = -2953
    var_14 = "admin9customer0_customer__flights6flights"
    var_15 = python_code_.customer(
        name="", address=[], age=var_13, source=var_14, payement1=None, ticket2=-2624.55
    )
    assert isinstance(var_15, python_code_.customer)
    var_19 = "_admin__customer5:_customer__ticket2:customer3:payement1"
    var_20 = 1364
    var_21 = 0
    var_22 = python_code_.ticket(
        tiketno_=(),
        source=var_3,
        dest=var_19,
        custid=var_21,
        attribute=var_19,
        customer3="_customer__payement1-admin4",
    )
    assert isinstance(var_22, python_code_.ticket)
    var_23 = "customer3:_customer__flights6:_customer__ticket2:admin"
    var_24 = "\x0bS?wkE\n!G"
    var_25 = python_code_.admin(
        username=var_3,
        pwd=var_23,
        name_of_flight=var_3,
        type=var_24,
        seats=var_20,
        cost=var_20,
    )
    assert isinstance(var_25, python_code_.admin)
    var_26 = python_code_.customer(
        name=var_19,
        address=None,
        age=var_20,
        source=var_8,
        ticket2=var_22,
        admin4=var_25,
    )
    assert isinstance(var_26, python_code_.customer)
