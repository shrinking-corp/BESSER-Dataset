import datetime as _ch_datetime
from python_code import Attendance

def test_Attendance___init__():
    assert Attendance.__init__(Attendance(_ch_datetime.date(1, 1, 1), '', '\x00\x00', ''), _ch_datetime.date(1, 1, 1), '', '', '') == None


from python_code import Authenticate_staff

def test_Authenticate_staff___init__():
    assert Authenticate_staff.__init__(Authenticate_staff('', '', '\x00\x00'), '', '', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None


from python_code import Salary

def test_Salary___init__():
    assert Salary.__init__(Salary(0, 0.0, 0.0, 0.0, 0.0, ''), 0, 0.0, 0.0, 0.0, 0.0, '') == None

