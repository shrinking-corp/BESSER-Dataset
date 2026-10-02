from python_code import account_AccountManager

def test_account_AccountManager___init__():
    assert account_AccountManager.__init__(account_AccountManager(''), '') == None

from python_code import account_CertificatesOfDepositAccount

def test_account_CertificatesOfDepositAccount___init__():
    assert account_CertificatesOfDepositAccount.__init__(account_CertificatesOfDepositAccount(0.0, 0), 0.0, 0) == None

from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None
