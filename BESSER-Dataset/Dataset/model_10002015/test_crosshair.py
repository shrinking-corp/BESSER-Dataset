from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', '', '\x00\x00'), '', '', '') == None


from python_code import Employee
from python_code import _10_7_1992

def test_Employee___init__():
    assert Employee.__init__(Employee('', '', '\x00', '', '', '', _10_7_1992(), '', '', '', ''), '', '', '\x00', '', '', '', _10_7_1992(), '', '', '', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None

