import datetime as _ch_datetime
from python_code import Places

def test_Places___init__():
    assert Places.__init__(Places(0, '', _ch_datetime.date(1, 1, 1), 0, '', '', '', ''), 0, '', _ch_datetime.date(1, 1, 1), 0, '', '', '', '') == None


import datetime as _ch_datetime
from python_code import Reviews

def test_Reviews___init__():
    assert Reviews.__init__(Reviews(0, 0, 0, _ch_datetime.date(1, 1, 1), '', 0), 0, 0, 0, _ch_datetime.date(1, 1, 1), '', 0) == None


import datetime as _ch_datetime
from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users(0, '\x00', 0, 0, _ch_datetime.date(1, 1, 1)), 0, '', 0, 0, _ch_datetime.date(1, 1, 1)) == None

