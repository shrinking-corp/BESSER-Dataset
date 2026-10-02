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
    Enum,
    account_Account,
    account_AccountType,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
    annotations,
    date,
    datetime,
    time,
    transaction_DepositTransaction,
    transaction_Transaction,
    transaction_TransactionType,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
)


def test_0():
    var_0 = python_code_.account_Account(
        accountNo="'T4\nC", type=None, balance=-155.99, transactions0=set()
    )
    assert isinstance(var_0, python_code_.account_Account)


def test_1():
    var_0 = python_code_.account_Account(accountNo=1, type=None, balance=1090)
    assert isinstance(var_0, python_code_.account_Account)


def test_2():
    python_code_.transaction_Transaction(
        id=1128,
        type=b"=>\n\x0f\xaa\xf6-|\x92\xd7C",
        transactionTime=True,
        amount={1694.28},
    )


def test_3():
    var_0 = python_code_.transaction_Transaction(
        id=None, type=-743.04, transactionTime=(False,), amount=False, account1=-1234.06
    )
    assert isinstance(var_0, python_code_.transaction_Transaction)


def test_4():
    var_0 = python_code_.account_Account(
        accountNo=".= M*ImU_2b7~", type=None, balance=-901.81
    )
    assert isinstance(var_0, python_code_.account_Account)
    var_44 = python_code_.transaction_Transaction(
        id=-476, type=var_0, transactionTime=var_0, amount=262.05, account1=var_0
    )
    assert isinstance(var_44, python_code_.transaction_Transaction)


def test_5():
    python_code_.account_CertificatesOfDepositAccount(interestRate={}, timePeriod=858)


def test_6():
    python_code_.account_SavingsAccount(interestRate=True)


def test_7():
    python_code_.transaction_TransferTransaction(
        targetAccount=complex(1651.2398624, 1180.5011938), sourceAccount=None
    )


def test_8():
    var_52 = python_code_.transaction_Transaction(
        id=(-790, True),
        type=complex(2059.527, 1564.73186),
        transactionTime=set(),
        amount=None,
    )
    var_53 = {var_52}
    var_54 = python_code_.account_Account(
        accountNo=var_52, type=var_52, balance=var_52, transactions0=var_53
    )
    assert isinstance(var_54, python_code_.account_Account)


def test_9():
    var_0 = python_code_.account_Account(
        accountNo="account1", type=None, balance=810.75, transactions0=set()
    )
    assert isinstance(var_0, python_code_.account_Account)
    var_81 = python_code_.transaction_Transaction(
        id=1756, type=None, transactionTime=var_0, amount=-981.3, account1=var_0
    )
    assert isinstance(var_81, python_code_.transaction_Transaction)
    var_82 = {var_81, var_81, var_81, var_81, var_81}
    var_83 = python_code_.account_Account(
        accountNo=var_0, type=-2223.71, balance=2337.39, transactions0=var_82
    )
    python_code_.transaction_TransferTransaction(
        targetAccount=var_83, sourceAccount=None
    )


def test_10():
    var_0 = python_code_.account_Account(
        accountNo="transactions0", type=None, balance=-1103.9
    )
    assert isinstance(var_0, python_code_.account_Account)
    var_49 = -1834.58
    var_50 = sorted
    var_51 = python_code_.transaction_Transaction(
        id=var_50,
        type=var_50,
        transactionTime="transaction_Transaction",
        amount={"R={{zev \x0b4]B1~mT"},
        account1=(-934, -329, 612.55),
    )
    assert isinstance(var_51, python_code_.transaction_Transaction)
    var_52 = {var_51, var_51, var_51, var_51}
    var_53 = python_code_.account_Account(
        accountNo=var_0, type={}, balance=var_49, transactions0=var_52
    )
    assert isinstance(var_53, python_code_.account_Account)


def test_11():
    var_37 = python_code_.transaction_DepositTransaction()
    var_38 = 2934.72
    var_39 = python_code_.account_Account(
        accountNo=var_38, type=None, balance=var_38, transactions0=(False,)
    )
    assert isinstance(var_39, python_code_.account_Account)
    var_40 = python_code_.transaction_Transaction(
        id=None, type=var_37, transactionTime={False}, amount=var_38, account1=var_39
    )
    assert isinstance(var_40, python_code_.transaction_Transaction)


def test_12():
    var_30 = "a"
    var_31 = -1643
    var_32 = hash
    var_33 = set
    var_34 = python_code_.account_Account(
        accountNo=var_30, type=var_32, balance=var_33, transactions0=(2657.15,)
    )
    assert isinstance(var_34, python_code_.account_Account)
    var_35 = python_code_.transaction_Transaction(
        id=var_31, type=var_31, transactionTime=var_31, amount=var_30, account1=var_34
    )
    assert isinstance(var_35, python_code_.transaction_Transaction)
    var_36 = {var_35, var_35}
    var_37 = python_code_.account_Account(
        accountNo=var_30, type=var_30, balance=157.18, transactions0=var_36
    )
    assert isinstance(var_37, python_code_.account_Account)
    python_code_.transaction_TransferTransaction(
        targetAccount=var_34, sourceAccount=var_37
    )
