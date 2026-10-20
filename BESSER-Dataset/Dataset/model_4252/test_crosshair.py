from python_code import employeeDsl_Employee
from python_code import employeeDsl_EmployeeContainer

def test_employeeDsl_Employee___init__():
    assert employeeDsl_Employee.__init__(employeeDsl_Employee(0, '', 0, employeeDsl_Employee=employeeDsl_EmployeeContainer()), 0, '', 0, employeeDsl_Employee=employeeDsl_EmployeeContainer()) == None

