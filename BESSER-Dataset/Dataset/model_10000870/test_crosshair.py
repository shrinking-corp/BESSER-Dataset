from python_code import Airport

def test_Airport___init__():
    assert Airport.__init__(Airport('', '', '', routes7=set()), '', '', '', routes7=set()) == None


from python_code import Customers
from python_code import Reservation

def test_Customers___init__():
    assert Customers.__init__(Customers('\x00\x00', '', '', '', reservation0=Reservation()), '', '', '', '', reservation0=Reservation()) == None


from python_code import Plane

def test_Plane___init__():
    assert Plane.__init__(Plane('', '', 0, flight4=set(), seats13=set()), '', '', 0, flight4=set(), seats13=set()) == None


from python_code import Routes

def test_Routes___init__():
    assert Routes.__init__(Routes('', '', '', airport6=set(), flight9=set()), '', '', '', airport6=set(), flight9=set()) == None


from python_code import Seats

def test_Seats___init__():
    assert Seats.__init__(Seats(0, False, plane12=set()), 0, False, plane12=set()) == None


from python_code import Ticket

def test_Ticket___init__():
    assert Ticket.__init__(Ticket('', '', '', '', '', flight11=set()), '', '', '', '\x00', '', flight11=set()) == None

