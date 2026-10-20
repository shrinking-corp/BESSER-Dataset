import datetime as _ch_datetime
from python_code import Bookings

def test_Bookings___init__():
    assert Bookings.__init__(Bookings(0, '', '', 0, 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table5=set()), 0, '\x00', '', 0, 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table5=set()) == None


from python_code import Membership_Card

def test_Membership_Card___init__():
    assert Membership_Card.__init__(Membership_Card(0, 0, order0=set()), 0, 0, order0=set()) == None


from python_code import Table

def test_Table___init__():
    assert Table.__init__(Table(0, 0, order3=set(), bookedTables17=set()), 0, 0, order3=set(), bookedTables17=set()) == None


from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users(0, '', 0, order15=set()), 0, '', 0, order15=set()) == None

