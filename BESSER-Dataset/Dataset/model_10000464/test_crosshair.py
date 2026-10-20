import datetime as _ch_datetime
from python_code import Bookings

def test_Bookings___init__():
    assert Bookings.__init__(Bookings(0, '', '', 0, 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table5=set()), 0, '\x00', '', 0, 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table5=set()) == None


from python_code import Membership_Card

def test_Membership_Card___init__():
    assert Membership_Card.__init__(Membership_Card(0, 0, order0=set()), 0, 0, order0=set()) == None


from python_code import Menu

def test_Menu___init__():
    assert Menu.__init__(Menu('', '', 0.0, 0, orderItem7=set()), '', '', 0.0, 0, orderItem7=set()) == None


from python_code import Table

def test_Table___init__():
    assert Table.__init__(Table(0, 0, bookedTables15=set(), order3=set()), 0, 0, bookedTables15=set(), order3=set()) == None

