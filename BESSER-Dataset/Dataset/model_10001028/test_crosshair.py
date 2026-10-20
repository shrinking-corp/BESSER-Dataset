from python_code import Native_App_CertificatesOfDepositAccount

def test_Native_App_CertificatesOfDepositAccount___init__():
    assert Native_App_CertificatesOfDepositAccount.__init__(Native_App_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import Native_App_CheckingAccount

def test_Native_App_CheckingAccount___init__():
    assert Native_App_CheckingAccount.__init__(Native_App_CheckingAccount(''), '') == None


from python_code import Native_App_SavingsAccount

def test_Native_App_SavingsAccount___init__():
    assert Native_App_SavingsAccount.__init__(Native_App_SavingsAccount(0.0), 0.0) == None

