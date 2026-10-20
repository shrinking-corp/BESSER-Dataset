from python_code import Appraisal

def test_Appraisal___init__():
    assert Appraisal.__init__(Appraisal('', '\x00'), '\x00\x00', '') == None


from python_code import Routing_Configuration_Settings

def test_Routing_Configuration_Settings___init__():
    assert Routing_Configuration_Settings.__init__(Routing_Configuration_Settings('', '\x00'), '\x00\x00', '') == None


from python_code import account_CertificatesOfDepositAccount

def test_account_CertificatesOfDepositAccount___init__():
    assert account_CertificatesOfDepositAccount.__init__(account_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import account_CheckingAccount

def test_account_CheckingAccount___init__():
    assert account_CheckingAccount.__init__(account_CheckingAccount(''), '') == None


from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None

