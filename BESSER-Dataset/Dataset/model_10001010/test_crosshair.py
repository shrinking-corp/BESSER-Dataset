from python_code import Authenticate_staff

def test_Authenticate_staff___init__():
    assert Authenticate_staff.__init__(Authenticate_staff('', '', '\x00\x00'), '', '', '') == None


import datetime as _ch_datetime
from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee(0, '\x00', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), ''), 0, '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None

