from python_code import Tescher

def test_Tescher___init__():
    assert Tescher.__init__(Tescher(0, '', '', student6=set(), courses8=set()), 0, '', '', student6=set(), courses8=set()) == None


from python_code import account_CertificatesOfDepositAccount

def test_account_CertificatesOfDepositAccount___init__():
    assert account_CertificatesOfDepositAccount.__init__(account_CertificatesOfDepositAccount(0, 0.0), 0, 0.0) == None


from python_code import account_CheckingAccount

def test_account_CheckingAccount___init__():
    assert account_CheckingAccount.__init__(account_CheckingAccount(''), '') == None


from python_code import account_SavingsAccount

def test_account_SavingsAccount___init__():
    assert account_SavingsAccount.__init__(account_SavingsAccount(0.0), 0.0) == None


from python_code import courses

def test_courses___init__():
    assert courses.__init__(courses('', 0, tescher9=set(), student10=set()), '', 0, tescher9=set(), student10=set()) == None

