from python_code import projectDsl_Employee
from python_code import projectDsl_Employees

def test_projectDsl_Employee___init__():
    assert projectDsl_Employee.__init__(projectDsl_Employee('', 0, 0, projectDsl_Employee=projectDsl_Employees()), '\x00', 0, 0, projectDsl_Employee=projectDsl_Employees()) == None

