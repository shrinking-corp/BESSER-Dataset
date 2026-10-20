import datetime as _ch_datetime
from python_code import Bookings

def test_Bookings___init__():
    assert Bookings.__init__(Bookings(0, '', '', 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), table5=set()), 0, '', '', 0, _ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1), table5=set()) == None


from python_code import Menu

def test_Menu___init__():
    assert Menu.__init__(Menu('', '', 0.0, 0, orderItem7=set()), '', '', 0.0, 0, orderItem7=set()) == None


from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users(0, '', 0, order13=set()), 0, '', 0, order13=set()) == None

