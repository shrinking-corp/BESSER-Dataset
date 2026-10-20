from python_code import AdminController
from python_code import processQuery

def test_AdminController___init__():
    assert AdminController.__init__(AdminController(0, '', 0, processQuery7=processQuery()), 0, '', 0, processQuery7=processQuery()) == None


from python_code import BookingController
from python_code import processQuery

def test_BookingController___init__():
    assert BookingController.__init__(BookingController(0, '', '', '', '', '', processQuery9=processQuery(), is_reserved_by3=set()), 0, '', '', '', '', '', processQuery9=processQuery(), is_reserved_by3=set()) == None


from python_code import Login
from python_code import processQuery

def test_Login___init__():
    assert Login.__init__(Login(0, 0, processQuery12=processQuery()), 0, 0, processQuery12=processQuery()) == None


from python_code import Membership_Card

def test_Membership_Card___init__():
    assert Membership_Card.__init__(Membership_Card(0, 0, order5=set()), 0, 0, order5=set()) == None

