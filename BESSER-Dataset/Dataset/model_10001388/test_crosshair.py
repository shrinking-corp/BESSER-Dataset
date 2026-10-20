from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', 0), '', 0) == None


from python_code import Loan

def test_Loan___init__():
    assert Loan.__init__(Loan(0, '', '', 0, '', ''), 0, '', '', 0, '\x00', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', 0), '', 0) == None


from python_code import payslip

def test_payslip___init__():
    assert payslip.__init__(payslip(0, '\x00'), 0, '\x00') == None

