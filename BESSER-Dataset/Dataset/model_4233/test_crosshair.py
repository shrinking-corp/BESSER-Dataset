from python_code import employee_Department
from python_code import employee_Employee

def test_employee_Employee___init__():
    assert employee_Employee.__init__(employee_Employee(0, employee_Employee=employee_Department()), 0, employee_Employee=employee_Department()) == None


from python_code import employee_NamedEntity

def test_employee_NamedEntity___init__():
    assert employee_NamedEntity.__init__(employee_NamedEntity('', 0), '', 0) == None

