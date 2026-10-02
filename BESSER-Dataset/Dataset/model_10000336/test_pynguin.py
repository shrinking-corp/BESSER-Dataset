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
    Autenticavel,
    Banco,
    CRUD,
    Class,
    Cofre,
    ContaBancaria,
    Conta_Conjunta,
    Conta_Corrente,
    Conta_Normal,
    Conta_Poupan_a,
    Deposito,
    Emprestimo,
    Enum,
    Enumeration,
    FixedAccount,
    IAutenticavel,
    Remover_Conta,
    SalvarConta,
    SistemaInterno,
    Transferencia,
    annotations,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_53 = "Luq^KNDgr'CBd\x0ck="
    var_54 = python_code_.ContaBancaria(
        NumeroConta=-493,
        NomeConta="u\r0gm(i{8PI",
        Saldo=237.16,
        bank1=var_53,
        autenticavel5=var_53,
    )
    assert isinstance(var_54, python_code_.ContaBancaria)
    python_code_.Autenticavel(Autenticar=var_53, Senha="", contaBancaria4=var_54)


def test_1():
    python_code_.Autenticavel(Autenticar='\n}xoK"Jo"4', Senha="_IAutenticavel__i2")


def test_2():
    var_55 = "c?_F,oa\nD?j)S8\n9U?e"
    var_56 = -1791.73
    var_58 = python_code_.Autenticavel(
        Autenticar="_IAutenticavel__i2",
        Senha="bank1,_ContaBancaria__bank1",
        contaBancaria4=var_55,
    )
    assert isinstance(var_58, python_code_.Autenticavel)
    var_59 = 295.87
    python_code_.Deposito(Valor=var_56, Nome="bxwR vRtqzdd==-D")
    var_61 = list
    var_62 = python_code_.Banco(NomeBanco=var_61)
    assert isinstance(var_62, python_code_.Banco)
    python_code_.FixedAccount(chequeBookNo=var_59)
    python_code_.Conta_Normal(id=-313)


def test_3():
    python_code_.IAutenticavel(Autenticar="2%Qo^")


def test_4():
    python_code_.IAutenticavel(Autenticar=b"\xbf")


def test_5():
    python_code_.ContaBancaria(
        NumeroConta=2446, NomeConta="\rRX.0_7+9LW4'*B\r/\x0b", Saldo=329.45
    )


def test_6():
    var_53 = "Luq^KNDngr'CBd\x0ck="
    var_88 = python_code_.ContaBancaria(
        NumeroConta=-493,
        NomeConta="u\r0gm(i{8PI",
        Saldo=237.16,
        bank1=var_53,
        autenticavel5=var_53,
    )
    assert isinstance(var_88, python_code_.ContaBancaria)
    python_code_.CRUD(Adicionar_Conta=var_53, Remover_Conta=var_53)


def test_7():
    var_54 = python_code_.Banco(
        NomeBanco='0Ta"RU(0VQ6Ci~', bankAccount0={"ZVm\\fFKjbcps?}:C", True}
    )
    assert isinstance(var_54, python_code_.Banco)


def test_8():
    var_54 = python_code_.Banco(NomeBanco="7q\ns)")
    assert isinstance(var_54, python_code_.Banco)


def test_9():
    python_code_.FixedAccount(chequeBookNo="ND [u5F$GYjAuea")


def test_10():
    python_code_.Deposito(Valor=False, Nome=(-193, -2445.5))


@pytest.mark.xfail(strict=True)
def test_11():
    var_57 = ",yY?AT[Y_\x0c)eYX1t&H"
    var_58 = python_code_.IAutenticavel(
        Autenticar=var_57, i2=complex(-616.8417313, 931.0)
    )
    assert isinstance(var_58, python_code_.IAutenticavel)
    var_60 = "2(',\x0b2*r67\x0bF\\+A"
    python_code_.Transferencia(Nome=var_60, Valor=var_57)
    python_code_.IAutenticavel(Autenticar=var_60, i3=var_58)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = hash
    var_1 = -794.01
    var_2 = python_code_.ContaBancaria(
        NumeroConta=-198, NomeConta="x@K\\Ko", Saldo=var_1
    )
    var_3 = python_code_.Class()
    var_4 = python_code_.IAutenticavel(
        Autenticar=[1277.78, -5445.65, True], i2=var_3, i3=b"\xe73\x18\xcb"
    )
    assert isinstance(var_4, python_code_.IAutenticavel)
    python_code_.Cofre(Dinheiro_Armazenado=var_2, Emprestimo_Total=var_0)
    python_code_.IAutenticavel(Autenticar="_ContaBancaria__autenticavel5", i2=var_4)
    assert isinstance(var_4.i3, python_code_.IAutenticavel)


def test_13():
    python_code_.Emprestimo(Valor=2258.0)


def test_14():
    python_code_.Conta_Normal(id=87)


def test_15():
    python_code_.Conta_Conjunta(id=860)


def test_16():
    var_0 = -549.56
    python_code_.Emprestimo(Valor=var_0)
    var_2 = python_code_.Remover_Conta()
    python_code_.Deposito(
        Valor=var_2, Nome=b"\xad\xc7\xe0S5\xbf\x87\xcaH%\x97\xd4\xe2\x11,"
    )
    var_11 = 2004.99
    var_13 = python_code_.Autenticavel
    python_code_.Conta_Poupan_a(Nome=var_2, CPF=var_13, Senha=var_11)


@pytest.mark.xfail(strict=True)
def test_17():
    var_1 = -794.01
    var_2 = python_code_.ContaBancaria(
        NumeroConta=-198, NomeConta="x@K\\Ko", Saldo=var_1
    )
    var_29 = python_code_.Cofre(Dinheiro_Armazenado=var_1, Emprestimo_Total=var_1)
    var_30 = python_code_.IAutenticavel(
        Autenticar="_Autenticavel__contaBancaria4:_IAutenticavel__i3",
        i2=var_29,
        i3=None,
    )
    var_32 = "_I[Autenticavel__i2"
    python_code_.Conta_Corrente(
        Nome="_ContaBancaria__autenticavel5,ContaBancaria,bank1",
        CPF=2,
        Senha=var_1,
        Taxa_de_Movimenta__o=1602.0,
    )
    python_code_.Autenticavel(Autenticar=var_32, Senha=var_30, contaBancaria4=var_2)


def test_18():
    python_code_.SistemaInterno(Entrar=None, _attr=None, _attr1='.Qf\x0blY"P;((&L,,')


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = 5817.79
    var_1 = python_code_.Emprestimo(Valor=var_0)
    var_2 = 75
    var_3 = python_code_.Conta_Normal(id=var_2)
    var_4 = "bankAccount0._IAutenticavel__i2._ContaBancaria__autenticavel5._Autenticavel__contaBancaria4"
    var_5 = python_code_.Banco(NomeBanco=var_4)
    assert isinstance(var_5, python_code_.Banco)
    var_7 = python_code_.Conta_Normal(id=())
    var_8 = python_code_.Transferencia(Nome=var_3, Valor=var_0)
    python_code_.Conta_Conjunta(id=var_8)
    python_code_.CRUD(Adicionar_Conta=var_4, Remover_Conta=var_7)
    var_11 = -467.55
    python_code_.Cofre(Dinheiro_Armazenado=var_11, Emprestimo_Total={-1160, 1118, True})
    var_13 = 2613.0
    var_14 = "=J$_=Shh@"
    python_code_.Deposito(Valor=var_13, Nome=var_14)
    var_16 = python_code_.Banco(NomeBanco=set())
    var_18 = python_code_.IAutenticavel(Autenticar=None)
    python_code_.SistemaInterno(Entrar=var_18, _attr=var_16, _attr1=-1)
    var_20 = "+d <\n"
    var_21 = python_code_.Conta_Corrente
    python_code_.Conta_Poupan_a(Nome=var_20, CPF=var_21, Senha=-3884.79)
    var_23 = python_code_.Autenticavel(
        Autenticar=complex(2528.5116163, 3099.120528), Senha=[]
    )
    python_code_.FixedAccount(chequeBookNo=var_20)
    var_27 = True
    python_code_.SalvarConta(interestRate=var_1, noticeGiven=var_27)
    python_code_.ContaBancaria(
        NumeroConta=var_21,
        NomeConta=var_14,
        Saldo=b'\xc0\x10\x94\xba\xf6\x19)\xfazN\x9e\xed"J\x85',
        autenticavel5=var_23,
    )


def test_20():
    var_53 = "Luq^KNDgr'CBd\x0ck="
    var_97 = python_code_.ContaBancaria(
        NumeroConta=0, NomeConta="MsOtgv>1KJf", Saldo=3297.76
    )
    var_98 = {var_97, var_97, var_97, var_97, var_97, "#vX&GN*  XRzX"}
    var_101 = python_code_.Banco(NomeBanco=var_53, bankAccount0=var_98)
    assert isinstance(var_101, python_code_.Banco)


def test_21():
    var_14 = python_code_.Conta_Normal
    var_16 = 1
    var_17 = python_code_.ContaBancaria(
        NumeroConta=-3525, NomeConta="contaBancaria4", Saldo=-4723.69, bank1=var_16
    )
    assert isinstance(var_17, python_code_.ContaBancaria)
    var_20 = {var_17, var_17, var_17}
    var_19 = python_code_.Banco(NomeBanco=var_14, bankAccount0=var_20)
    assert isinstance(var_19, python_code_.Banco)


def test_22():
    var_53 = "Luq^KNDgr'CBd\x0ck="
    var_97 = python_code_.ContaBancaria(
        NumeroConta=0, NomeConta="MsOtgv>1KJf", Saldo=3297.76
    )
    var_98 = {var_97, var_97, var_97, var_97, var_97, "#vX&GN*  XRzX"}
    var_99 = python_code_.Banco(NomeBanco=var_53, bankAccount0=var_98)
    assert isinstance(var_99, python_code_.Banco)
    python_code_.Conta_Normal(id=475)
    var_101 = python_code_.Banco(NomeBanco=var_53, bankAccount0=var_98)
    assert isinstance(var_101, python_code_.Banco)
