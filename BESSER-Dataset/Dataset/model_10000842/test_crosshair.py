import datetime as _ch_datetime
from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator(0, '', '', '', 0, _ch_datetime.date(1, 1, 1), ''), 0, '', '', '\x00', 0, _ch_datetime.date(1, 1, 1), '') == None


from python_code import Farmer_produces

def test_Farmer_produces___init__():
    assert Farmer_produces.__init__(Farmer_produces(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import rating___review

def test_rating___review___init__():
    assert rating___review.__init__(rating___review(0, '', 0, '', '', ''), 0, '', 0, '', '\x00', '') == None

