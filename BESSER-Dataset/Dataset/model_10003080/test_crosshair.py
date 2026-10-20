from python_code import Error_code

def test_Error_code___init__():
    assert Error_code.__init__(Error_code('', '', '\x00\x00'), '', '', '') == None


from python_code import History

def test_History___init__():
    assert History.__init__(History('', '\x00'), '\x00\x00', '') == None


import datetime as _ch_datetime
from python_code import Scanner

def test_Scanner___init__():
    assert Scanner.__init__(Scanner(0, '', '\x00', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), 0.0), 0, '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), 0.0) == None

