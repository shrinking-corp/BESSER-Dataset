from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('', '\x00'), '\x00\x00', '') == None


from python_code import Book

def test_Book___init__():
    assert Book.__init__(Book('\x00\x00', '', '', 0), '', '', '', 0) == None


from python_code import Car

def test_Car___init__():
    assert Car.__init__(Car('', '', '', 0, 0, 0, 0), '', '\x00', '', 0, 0, 0, 0) == None

