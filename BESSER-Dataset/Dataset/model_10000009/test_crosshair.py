from python_code import CreateUserAction
from python_code import Employee_Actor

def test_CreateUserAction___init__():
    assert CreateUserAction.__init__(CreateUserAction(Employee_Actor()), Employee_Actor()) == None


from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee('', '', 0, '', '', 0, ''), '', '\x00', 0, '', '', 0, '') == None


import datetime as _ch_datetime
from python_code import LeaveApplication

def test_LeaveApplication___init__():
    assert LeaveApplication.__init__(LeaveApplication('', '', '', '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)), '', '', '', '', '', _ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1)) == None


import datetime as _ch_datetime
from python_code import LeaveHistoryQuery

def test_LeaveHistoryQuery___init__():
    assert LeaveHistoryQuery.__init__(LeaveHistoryQuery(_ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1)), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None


from python_code import Employee_Actor
from python_code import LoginAction

def test_LoginAction___init__():
    assert LoginAction.__init__(LoginAction(Employee_Actor()), Employee_Actor()) == None


from python_code import Employee_Actor
from python_code import Query

def test_Query___init__():
    assert Query.__init__(Query('', Employee_Actor()), '', Employee_Actor()) == None


import datetime as _ch_datetime
from python_code import LeaveApplication
from python_code import Request

def test_Request___init__():
    assert Request.__init__(Request('', LeaveApplication('', '', '', '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1))), '', LeaveApplication('', '\x00', '', '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1))) == None

