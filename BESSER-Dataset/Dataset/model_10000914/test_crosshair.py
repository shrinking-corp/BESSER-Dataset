from python_code import Class

def test_Class___init__():
    assert Class.__init__(Class('', '\x00'), '\x00\x00', '') == None


import datetime as _ch_datetime
from python_code import Cliente

def test_Cliente___init__():
    assert Cliente.__init__(Cliente(0, '', 0, 0, 0, 0, 0, '', _ch_datetime.date(1, 1, 1)), 0, '', 0, 0, 0, 0, 0, '', _ch_datetime.date(1, 1, 1)) == None


from python_code import Direccion

def test_Direccion___init__():
    assert Direccion.__init__(Direccion(0, 0, '\x00', 0, '', '', '', 0, '', ''), 0, 0, '\x00', 0, '', '', '', 0, '', '') == None


from python_code import Login1

def test_Login1___init__():
    assert Login1.__init__(Login1('', '\x00'), '\x00\x00', '') == None


from python_code import Personas

def test_Personas___init__():
    assert Personas.__init__(Personas(0, '', '', '', '', ''), 0, '', '', '', '\x00', '') == None


from python_code import account_CertificatesOfDepositAccount

def test_account_CertificatesOfDepositAccount___init__():
    assert account_CertificatesOfDepositAccount.__init__(account_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import account_CheckingAccount

def test_account_CheckingAccount___init__():
    assert account_CheckingAccount.__init__(account_CheckingAccount(''), '') == None


from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None


from python_code import gerente

def test_gerente___init__():
    assert gerente.__init__(gerente(0, '', '', 0, 0), 0, '', '', 0, 0) == None

