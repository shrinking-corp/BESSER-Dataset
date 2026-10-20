from python_code import CertificatesOfDepositAccount

def test_CertificatesOfDepositAccount___init__():
    assert CertificatesOfDepositAccount.__init__(CertificatesOfDepositAccount(0.0, 0), 0.0, 0) == None


from python_code import SavingsAccount

def test_SavingsAccount___init__():
    assert SavingsAccount.__init__(SavingsAccount(0.0), 0.0) == None

