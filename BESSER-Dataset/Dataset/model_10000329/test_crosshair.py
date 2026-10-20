from python_code import Bill
from python_code import Waiter

def test_Bill___init__():
    assert Bill.__init__(Bill(0, 0, 0, waiter7=Waiter()), 0, 0, 0, waiter7=Waiter()) == None


from python_code import Guest

def test_Guest___init__():
    assert Guest.__init__(Guest('', '', '\x00\x00'), '', '', '') == None


from python_code import Party

def test_Party___init__():
    assert Party.__init__(Party(0, 0, 0), 0, 0, 0) == None


from python_code import Staff

def test_Staff___init__():
    assert Staff.__init__(Staff('\x00\x00', '', '', ''), '', '', '', '') == None

