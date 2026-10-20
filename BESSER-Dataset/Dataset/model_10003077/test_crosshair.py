from python_code import Bank

def test_Bank___init__():
    assert Bank.__init__(Bank('\x00\x00', '', branch0=set()), '', '', branch0=set()) == None


from python_code import Employee
from python_code import Manager

def test_Employee___init__():
    assert Employee.__init__(Employee(0, 0, manager8=Manager()), 0, 0, manager8=Manager()) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '', '', '', ''), 0, '', '', '', '') == None

