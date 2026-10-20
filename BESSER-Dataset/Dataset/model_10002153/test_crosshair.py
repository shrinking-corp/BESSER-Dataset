from python_code import CurrentAccount

def test_CurrentAccount___init__():
    assert CurrentAccount.__init__(CurrentAccount('', 0, 0), '\x00', 0, 0) == None


from python_code import Loan_Account

def test_Loan_Account___init__():
    assert Loan_Account.__init__(Loan_Account('\x00\x00', 0, 0, ''), '', 0, 0, '') == None

