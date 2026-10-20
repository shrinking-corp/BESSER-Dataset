import datetime as _ch_datetime
from python_code import Bookings

def test_Bookings___init__():
    assert Bookings.__init__(Bookings(0, '', '', 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table3=set()), 0, '', '', 0, _ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1), table3=set()) == None


import datetime as _ch_datetime
from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users(0, '', 0, _ch_datetime.date(1, 1, 1), order11=set()), 0, '', 0, _ch_datetime.date(1, 1, 1), order11=set()) == None

