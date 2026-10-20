from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator('', '\x00'), '\x00\x00', '') == None


from python_code import CheckStatus

def test_CheckStatus___init__():
    assert CheckStatus.__init__(CheckStatus(''), '') == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import DBDetails

def test_DBDetails___init__():
    assert DBDetails.__init__(DBDetails(False, False), False, False) == None


from python_code import D_B_details

def test_D_B_details___init__():
    assert D_B_details.__init__(D_B_details('', '\x00'), '\x00\x00', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None


from python_code import Logout

def test_Logout___init__():
    assert Logout.__init__(Logout(0), 0) == None


import datetime as _ch_datetime
from python_code import MonitorComplaint

def test_MonitorComplaint___init__():
    assert MonitorComplaint.__init__(MonitorComplaint('', _ch_datetime.date(1, 1, 2), ''), '\x00\x00', _ch_datetime.date(1, 1, 1), '') == None


from python_code import RegisterComplaint

def test_RegisterComplaint___init__():
    assert RegisterComplaint.__init__(RegisterComplaint('', '\x00'), '\x00\x00', '') == None


from python_code import UpdateStatus

def test_UpdateStatus___init__():
    assert UpdateStatus.__init__(UpdateStatus(True), False) == None


from python_code import administrator

def test_administrator___init__():
    assert administrator.__init__(administrator('', '\x00'), '\x00\x00', '') == None


from python_code import check_status

def test_check_status___init__():
    assert check_status.__init__(check_status(''), '') == None


from python_code import customer

def test_customer___init__():
    assert customer.__init__(customer('\x00\x00', 0, '', ''), '', 0, '', '') == None


from python_code import login

def test_login___init__():
    assert login.__init__(login('', '\x00'), '\x00\x00', '') == None


from python_code import logout

def test_logout___init__():
    assert logout.__init__(logout(''), '') == None


from python_code import monitor_complaint

def test_monitor_complaint___init__():
    assert monitor_complaint.__init__(monitor_complaint(0, '', '\x00\x00'), 0, '', '') == None


from python_code import register_complaint

def test_register_complaint___init__():
    assert register_complaint.__init__(register_complaint('', '\x00'), '\x00\x00', '') == None


from python_code import update_status

def test_update_status___init__():
    assert update_status.__init__(update_status(''), '') == None

