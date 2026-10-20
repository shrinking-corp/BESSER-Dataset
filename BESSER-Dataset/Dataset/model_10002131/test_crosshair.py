from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee('\x00\x00', '', '', ''), '', '', '', '') == None

