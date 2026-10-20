from python_code import Ticket

def test_Ticket___init__():
    assert Ticket.__init__(Ticket(''), '') == None


from python_code import Vehicle_Interface
from python_code import spot

def test_spot___init__():
    assert spot.__init__(spot(0, '\x00', Vehicle_Interface()), 0, '\x00', Vehicle_Interface()) == None

