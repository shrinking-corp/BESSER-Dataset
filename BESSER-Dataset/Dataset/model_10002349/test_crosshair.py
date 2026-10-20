from python_code import Medical_Record_CertificatesOfDepositAccount

def test_Medical_Record_CertificatesOfDepositAccount___init__():
    assert Medical_Record_CertificatesOfDepositAccount.__init__(Medical_Record_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import Medical_Record_CheckingAccount

def test_Medical_Record_CheckingAccount___init__():
    assert Medical_Record_CheckingAccount.__init__(Medical_Record_CheckingAccount(''), '') == None


from python_code import Medical_Record_SavingsAccount

def test_Medical_Record_SavingsAccount___init__():
    assert Medical_Record_SavingsAccount.__init__(Medical_Record_SavingsAccount(0.0), 0.0) == None

