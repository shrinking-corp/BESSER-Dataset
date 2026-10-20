import datetime as _ch_datetime
from python_code import Bookings

def test_Bookings___init__():
    assert Bookings.__init__(Bookings(0, '', '', 0, 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table5=set()), 0, '\x00', '', 0, 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table5=set()) == None


from python_code import Membership_Card

def test_Membership_Card___init__():
    assert Membership_Card.__init__(Membership_Card(0, 0, order0=set()), 0, 0, order0=set()) == None


from python_code import ViewOrder

def test_ViewOrder___init__():
    assert ViewOrder.__init__(ViewOrder(0, orderItem6=set()), 0, orderItem6=set()) == None

