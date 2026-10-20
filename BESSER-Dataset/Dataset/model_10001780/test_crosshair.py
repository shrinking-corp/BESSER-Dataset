from python_code import Ticket

def test_Ticket___init__():
    assert Ticket.__init__(Ticket('\x00', '', '', 0, '', '', system1=set()), '', '', '', 0, '', '\x00', system1=set()) == None

