import datetime as _ch_datetime
from python_code import Login2

def test_Login2___init__():
    assert Login2.__init__(Login2('\x00\x00', '', '', '', _ch_datetime.date(1, 1, 1)), '', '', '', '', _ch_datetime.date(1, 1, 1)) == None


from python_code import account_CertificatesOfDepositAccount

def test_account_CertificatesOfDepositAccount___init__():
    assert account_CertificatesOfDepositAccount.__init__(account_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import account_CheckingAccount

def test_account_CheckingAccount___init__():
    assert account_CheckingAccount.__init__(account_CheckingAccount(''), '') == None


from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None

