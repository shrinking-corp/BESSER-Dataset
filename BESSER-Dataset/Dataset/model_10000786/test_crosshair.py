from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import Department

def test_Department___init__():
    assert Department.__init__(Department(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Student

def test_Student___init__():
    assert Student.__init__(Student(0.0, 0, '', ''), 0.0, 0, '', '') == None

