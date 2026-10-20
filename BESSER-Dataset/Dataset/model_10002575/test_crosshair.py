from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import Chess

def test_Chess___init__():
    assert Chess.__init__(Chess(0.0, 0, '', '', ''), 0.0, 0, '', '', '\x00') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None

