from python_code import Conta_CertificatesOfDepositAccount

def test_Conta_CertificatesOfDepositAccount___init__():
    assert Conta_CertificatesOfDepositAccount.__init__(Conta_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import Conta_CheckingAccount

def test_Conta_CheckingAccount___init__():
    assert Conta_CheckingAccount.__init__(Conta_CheckingAccount(''), '') == None


from python_code import Conta_SavingsAccount

def test_Conta_SavingsAccount___init__():
    assert Conta_SavingsAccount.__init__(Conta_SavingsAccount(0.0), 0.0) == None

