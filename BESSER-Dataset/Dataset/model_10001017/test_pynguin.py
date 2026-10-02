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
    Enum,
    Login,
    NewClass,
    account_Account,
    account_AccountManager,
    account_AccountType,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
    annotations,
    customerpackage_Customer,
    date,
    datetime,
    time,
    transaction_Class,
    transaction_DepositTransaction,
    transaction_Transaction,
    transaction_TransactionType,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = "\x0caccount_Account__transactions2-_account_Account__transactions2-Login"
    var_77 = "transaction_Trasaction"
    var_78 = python_code_.customerpackage_Customer(
        name=var_77,
        dateOfBirth=var_0,
        address="transactions2.account1._account_Account__customer0",
        phoneNumber="S+\\\x0bK~K\n>",
        emailAddress=var_77,
    )
    assert isinstance(var_78, python_code_.customerpackage_Customer)
    python_code_.Login(
        username=var_77,
        password=var_77,
        securityQuestion=var_77,
        securityAnswer="~4+<dQF\t",
        lastLoginTime=var_77,
        customer5=var_78,
    )


def test_1():
    python_code_.Login(
        username={"txzAVIO\nXLh!,C !|\x0b", 3232.82},
        password=-557.33,
        securityQuestion={"w": "2@Q\x0bm~", "sZSZR;1N": -1273.39},
        securityAnswer=(),
        lastLoginTime=b":\x92\xabD\xaa\xc3o.\xc7\x01Z\x05\x86",
    )


def test_2():
    var_0 = "customer0 login4"
    var_1 = "_Login__customer5"
    var_2 = python_code_.account_SavingsAccount
    var_3 = python_code_.Login(
        username=var_0,
        password=var_1,
        securityQuestion=var_2,
        securityAnswer=var_2,
        lastLoginTime=var_1,
        customer5=set(),
    )
    assert isinstance(var_3, python_code_.Login)
    var_4 = 183.1
    var_5 = python_code_.account_Account(type=var_3, balance=var_4)
    assert isinstance(var_5, python_code_.account_Account)
    var_6 = python_code_.transaction_Transaction(
        id=var_0, type=None, amount=set(), account3=var_5
    )
    assert isinstance(var_6, python_code_.transaction_Transaction)
    var_7 = {var_6}
    python_code_.account_Account(type=var_1, balance=var_2, transactions2=var_7)
    var_10 = 3
    python_code_.account_CertificatesOfDepositAccount(
        interestRate={False, True}, timePeriod=var_10
    )


def test_3():
    var_82 = python_code_.customerpackage_Customer(
        name="S\x0b3LO",
        dateOfBirth=None,
        address=">qr/%gC!O",
        phoneNumber="transactions2._account_Account__transactions2",
        emailAddress="\rI*H[d{h+",
        account1={False},
        login4=None,
    )
    assert isinstance(var_82, python_code_.customerpackage_Customer)


def test_4():
    var_82 = python_code_.customerpackage_Customer(
        name='|]0K|gh"D\x0cG\x0c',
        dateOfBirth=None,
        address="?(\tdtTC p^9M!NO",
        phoneNumber="account_Account",
        emailAddress="_customerpackage_Customer__account1",
    )
    assert isinstance(var_82, python_code_.customerpackage_Customer)


def test_5():
    var_0 = "_hacc_unt_Accont__transactions2-_account_Account__transactions2-Login"
    var_74 = python_code_.customerpackage_Customer(
        name=var_0,
        dateOfBirth=var_0,
        address="'Q<]",
        phoneNumber="_account_Account__transactions2",
        emailAddress=")%TJ4Enz&2F+\\X>W",
        account1=set(),
        login4=var_0,
    )
    assert isinstance(var_74, python_code_.customerpackage_Customer)


def test_6():
    var_70 = python_code_.account_Account(
        type=None, balance=-517.22, transactions2={True, 0, -1}
    )
    assert isinstance(var_70, python_code_.account_Account)


def test_7():
    var_70 = python_code_.account_Account(type=None, balance=2935.44, customer0=None)
    assert isinstance(var_70, python_code_.account_Account)


def test_8():
    var_0 = python_code_.NewClass()
    var_1 = python_code_.account_Account
    var_2 = "3xS\x0b"
    var_3 = "T-/"
    var_4 = python_code_.customerpackage_Customer(
        name=var_2,
        dateOfBirth=var_3,
        address=var_0,
        phoneNumber=var_3,
        emailAddress=var_2,
    )
    assert isinstance(var_4, python_code_.customerpackage_Customer)
    var_5 = python_code_.account_Account(
        type=b"H\xe1\xa8\x04O\xd9\x10N\xf2\x96\xaa\xb2\xe6",
        balance=["transaction_Transaction", 1292],
        customer0=var_4,
    )
    assert isinstance(var_5, python_code_.account_Account)
    var_6 = {var_5, var_5, var_5, var_5, var_5}
    python_code_.customerpackage_Customer(
        name=(-1193.8, 1938.75),
        dateOfBirth=var_1,
        address=var_2,
        phoneNumber=var_1,
        emailAddress=var_3,
        account1=var_6,
    )
    var_8 = "8ID$MN5-NF"
    python_code_.account_AccountManager(attribute=var_8)


def test_9():
    var_0 = python_code_.account_AccountManager(attribute="customer5.customer5")
    var_6 = python_code_.account_Account(type=var_0, balance=-820.85, customer0=var_0)
    assert isinstance(var_6, python_code_.account_Account)


def test_10():
    var_7 = "/_lJVY"
    var_13 = -5380.41
    var_14 = -1974
    var_15 = python_code_.transaction_Transaction(id=var_14, type=1791, amount=None)
    var_16 = {var_15, var_15, var_15, var_15}
    var_17 = python_code_.account_Account(
        type=None, balance=var_13, transactions2=var_16
    )
    assert isinstance(var_17, python_code_.account_Account)
    var_18 = 1766.47
    var_19 = python_code_.account_Account(
        type="wn2", balance=var_18, transactions2=var_16
    )
    assert isinstance(var_19, python_code_.account_Account)
    var_20 = {var_17, var_17, var_17, var_19, var_19}
    var_21 = python_code_.customerpackage_Customer(
        name={},
        dateOfBirth=var_7,
        address=var_7,
        phoneNumber=var_7,
        emailAddress=var_7,
        account1=var_20,
    )
    assert isinstance(var_21, python_code_.customerpackage_Customer)


def test_11():
    python_code_.transaction_Transaction(id=-6, type=None, amount=-220.31)


def test_12():
    var_0 = set()
    var_1 = python_code_.account_Account(
        type=["|)!,4ww[C>M", -2512.57], balance=False, transactions2=var_0
    )
    assert isinstance(var_1, python_code_.account_Account)
    var_2 = python_code_.transaction_Transaction(
        id=("|]e@S", "account1", -817.21),
        type=None,
        amount={"_Login__customer5": "};\naGNCCjjj[2+Nu-r"},
        account3=var_1,
    )
    assert isinstance(var_2, python_code_.transaction_Transaction)


def test_13():
    python_code_.account_AccountManager(attribute="z-tSQg}?xi2\no8~p}")


def test_14():
    var_82 = python_code_.customerpackage_Customer(
        name="+JOX(QEaVGh9`\tWX\r",
        dateOfBirth=None,
        address="=h(3\rzOAvI",
        phoneNumber="_M.Ura",
        emailAddress="transactions2_customerpackage_Customer__account1",
    )
    assert isinstance(var_82, python_code_.customerpackage_Customer)
    var_85 = python_code_.account_Account(type=None, balance=set(), customer0=var_82)
    assert isinstance(var_85, python_code_.account_Account)


def test_15():
    var_75 = "transaction_Trasaction"
    var_77 = python_code_.account_Account(type=None, balance=-1543.86)
    assert isinstance(var_77, python_code_.account_Account)
    var_78 = {var_77}
    var_79 = python_code_.customerpackage_Customer(
        name="]I6j[g=\\nm!,!<|4$w",
        dateOfBirth=None,
        address=var_75,
        phoneNumber=var_75,
        emailAddress="Login,_Login__customer5,_customerpackage_Customer__login4,customer0",
        account1=var_78,
    )
    assert isinstance(var_79, python_code_.customerpackage_Customer)


def test_16():
    python_code_.account_CertificatesOfDepositAccount(
        interestRate=set(), timePeriod=False
    )


def test_17():
    python_code_.account_SavingsAccount(
        InterestRate=b"\x87\x1a\x15\xfb\xdc\x13\xe8\x88\x06^{\xa4\xc1\x89\xeb\x986"
    )


def test_18():
    python_code_.transaction_TransferTransaction(targetAccount=None, sourceAccount=None)


def test_19():
    var_0 = python_code_.account_AccountManager(attribute=False)
    var_1 = -1113
    var_2 = 565.92
    var_3 = python_code_.transaction_Transaction(id=var_1, type=None, amount=var_2)
    var_4 = {var_3, var_3, var_3, var_3, var_3}
    var_5 = python_code_.account_Account(type=var_0, balance=var_0, transactions2=var_4)
    assert isinstance(var_5, python_code_.account_Account)


def test_20():
    var_0 = -2931
    var_1 = python_code_.transaction_Transaction(
        id=var_0,
        type={-375.7, "\rPgxhC|Y6p2", "_account_Account__transactions2.account3.Login"},
        amount={"Erw": -2360, "Fu": False, "_account_Account__customer0": 2282.13},
    )
    var_2 = "_account_Account__transactions2_Login__customer5customer0"
    var_3 = python_code_.account_AccountManager(attribute=var_2)
    var_6 = "login4"
    var_7 = "/_lJVY"
    var_8 = python_code_.account_Account(type=var_3, balance=set())
    assert isinstance(var_8, python_code_.account_Account)
    var_9 = python_code_.account_Account(type=None, balance=var_0, customer0=var_7)
    assert isinstance(var_9, python_code_.account_Account)
    var_10 = {var_8, var_9}
    var_11 = python_code_.customerpackage_Customer(
        name=var_6,
        dateOfBirth=complex(740.46237, 1291.0),
        address=var_7,
        phoneNumber=var_1,
        emailAddress=complex(-3420.68313, -2667.233582),
        account1=var_10,
    )
    assert isinstance(var_11, python_code_.customerpackage_Customer)


def test_21():
    var_0 = "_account_Account__transactions2-_account_Account__transactions2-Login"
    var_1 = python_code_.transaction_Transaction
    var_2 = python_code_.customerpackage_Customer(
        name=var_0,
        dateOfBirth=(),
        address=var_0,
        phoneNumber=var_1,
        emailAddress=var_1,
        login4=var_1,
    )
    assert isinstance(var_2, python_code_.customerpackage_Customer)
    var_3 = python_code_.transaction_Transaction(
        id=-1, type=var_0, amount=478.56, account3=var_2
    )
    var_4 = {var_3, var_3}
    var_5 = python_code_.account_Account(
        type=set(), balance=-802.41, customer0=var_2, transactions2=var_4
    )
    assert isinstance(var_5, python_code_.account_Account)


def test_22():
    var_70 = python_code_.account_Account(type=None, balance=-1490.89)
    assert isinstance(var_70, python_code_.account_Account)
    var_71 = 723
    var_72 = 1042.08
    var_73 = python_code_.transaction_Transaction(
        id=var_71, type={}, amount=var_72, account3={}
    )
    assert isinstance(var_73, python_code_.transaction_Transaction)


def test_23():
    var_1 = "7*v3\\u=PXa^;\rFrk=nh"
    var_2 = python_code_.account_AccountManager(attribute=var_1)
    var_3 = python_code_.transaction_DepositTransaction()
    var_4 = -1913
    var_5 = 3041.28
    var_6 = python_code_.transaction_Transaction(id=var_4, type=None, amount=var_5)
    var_7 = 2260.51
    var_8 = python_code_.account_Account(
        type=4085.46, balance=var_7, transactions2=var_1
    )
    assert isinstance(var_8, python_code_.account_Account)
    var_9 = python_code_.transaction_Transaction(
        id=var_4, type=var_1, amount=var_3, account3=var_8
    )
    assert isinstance(var_9, python_code_.transaction_Transaction)
    var_10 = {var_6, var_6, var_9, var_6}
    var_11 = python_code_.account_Account(
        type=var_2, balance=3226, transactions2=var_10
    )
    assert isinstance(var_11, python_code_.account_Account)


def test_24():
    var_0 = "customer0 login4"
    var_1 = "_Login__customer5"
    var_2 = python_code_.account_SavingsAccount
    var_3 = python_code_.Login(
        username=var_0,
        password=var_1,
        securityQuestion=var_2,
        securityAnswer=var_2,
        lastLoginTime=var_1,
        customer5=set(),
    )
    assert isinstance(var_3, python_code_.Login)
    var_4 = 183.11
    var_5 = python_code_.account_Account(type=var_3, balance=var_4)
    assert isinstance(var_5, python_code_.account_Account)
    var_6 = python_code_.transaction_Transaction(
        id=var_0, type=None, amount=set(), account3=var_5
    )
    assert isinstance(var_6, python_code_.transaction_Transaction)
    var_7 = {var_6}
    python_code_.account_Account(type=var_1, balance=var_2, transactions2=var_7)
    var_10 = 3
    python_code_.account_CertificatesOfDepositAccount(
        interestRate={False, True}, timePeriod=var_10
    )


@pytest.mark.xfail(strict=True)
def test_25():
    var_1 = python_code_.transaction_DepositTransaction()
    var_3 = 586
    python_code_.transaction_Transaction(
        id=var_3, type=None, amount=(True, "customerpackage_Customercustomer0customer0")
    )
    var_6 = -1437.78
    var_7 = "login4"
    var_8 = python_code_.customerpackage_Customer(
        name=var_7,
        dateOfBirth=True,
        address=var_7,
        phoneNumber=var_7,
        emailAddress=var_3,
        login4=1886,
    )
    assert isinstance(var_8, python_code_.customerpackage_Customer)
    var_9 = python_code_.account_Account(
        type=var_1, balance=var_6, customer0=var_8, transactions2=b"h"
    )
    assert isinstance(var_9, python_code_.account_Account)
    python_code_.account_SavingsAccount(InterestRate=var_6)
    var_11 = python_code_.NewClass()
    var_12 = float
    var_13 = python_code_.account_Account(type=[], balance=var_12)
    assert isinstance(var_13, python_code_.account_Account)
    var_14 = python_code_.account_Account(type=var_11, balance=var_6, customer0=var_12)
    assert isinstance(var_14, python_code_.account_Account)
    python_code_.account_AccountManager(attribute=var_7)
    var_28 = 3550.5
    var_30 = "_B"
    var_31 = "m1\x0b4&\tl5Hp"
    python_code_.Login(
        username=var_30,
        password={},
        securityQuestion=var_31,
        securityAnswer=var_12,
        lastLoginTime=var_28,
        customer5=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_26():
    var_0 = -3472
    python_code_.transaction_Transaction(id=var_0, type=None, amount=False)
    var_5 = ""
    var_6 = ";DgK;zQD>Z;8#"
    var_7 = "poSD\\f\t73\\/E\\[Aj"
    var_8 = "customer0"
    var_9 = (
        "_account_Account__transactions2-customer0-_transaction_Transaction__account3"
    )
    var_10 = abs
    var_11 = python_code_.Login(
        username=var_6,
        password=var_7,
        securityQuestion=var_8,
        securityAnswer=var_9,
        lastLoginTime=var_10,
        customer5=var_8,
    )
    assert isinstance(var_11, python_code_.Login)
    python_code_.customerpackage_Customer(
        name=var_5,
        dateOfBirth=[],
        address=var_5,
        phoneNumber=" ",
        emailAddress=var_5,
        login4=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = python_code_.transaction_Class()
    var_1 = python_code_.account_Account
    python_code_.Login(
        username=True,
        password=var_1,
        securityQuestion={
            "_transaction_Transaction__account3-Login-_account_Account__transactions2-transactions2",
            1071.31,
        },
        securityAnswer=True,
        lastLoginTime=var_1,
    )
    var_3 = len
    var_4 = "o{dUgP5lAc7~KTO"
    var_5 = "Q{(v kIOv+m\\pm\\"
    var_6 = sorted
    var_7 = python_code_.customerpackage_Customer(
        name=var_4,
        dateOfBirth=var_0,
        address=var_5,
        phoneNumber=var_6,
        emailAddress=var_6,
        account1={},
    )
    assert isinstance(var_7, python_code_.customerpackage_Customer)
    python_code_.account_Account(
        type=var_1, balance=var_3, customer0=var_7, transactions2=var_7
    )
