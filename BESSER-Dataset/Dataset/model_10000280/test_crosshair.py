from python_code import Authentication
from python_code import Database

def test_Authentication___init__():
    assert Authentication.__init__(Authentication('', '', '', True, 0, '', database7=Database()), '', '', '', False, 0, '', database7=Database()) == None


from python_code import LOGIN

def test_LOGIN___init__():
    assert LOGIN.__init__(LOGIN('', '\x00'), '\x00\x00', '') == None


from python_code import LoginAuthenticationProcessor

def test_LoginAuthenticationProcessor___init__():
    assert LoginAuthenticationProcessor.__init__(LoginAuthenticationProcessor('', '', False), '\x00', '', False) == None


from python_code import OPT_AuthenticationProcessor

def test_OPT_AuthenticationProcessor___init__():
    assert OPT_AuthenticationProcessor.__init__(OPT_AuthenticationProcessor('', False), '', False) == None


from python_code import RequestOTPAuthentication

def test_RequestOTPAuthentication___init__():
    assert RequestOTPAuthentication.__init__(RequestOTPAuthentication('', '\x00'), '\x00\x00', '') == None


from python_code import account_CertificatesOfDepositAccount

def test_account_CertificatesOfDepositAccount___init__():
    assert account_CertificatesOfDepositAccount.__init__(account_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import account_CheckingAccount

def test_account_CheckingAccount___init__():
    assert account_CheckingAccount.__init__(account_CheckingAccount(''), '') == None


from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None

