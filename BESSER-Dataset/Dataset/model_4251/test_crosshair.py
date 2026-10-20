from python_code import Employees_Employee
from python_code import Employees_EmployeeContainer

def test_Employees_Employee___init__():
    assert Employees_Employee.__init__(Employees_Employee('', 0, 0, Employees_Employee=Employees_EmployeeContainer()), '\x00', 0, 0, Employees_Employee=Employees_EmployeeContainer()) == None

