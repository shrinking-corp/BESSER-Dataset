from python_code import employee_Company
from python_code import employee_Department

def test_employee_Department___init__():
    assert employee_Department.__init__(employee_Department(False, employee_Department=employee_Company(), employee_Department2=set()), False, employee_Department=employee_Company(), employee_Department2=set()) == None


from python_code import employee_NamedEntity

def test_employee_NamedEntity___init__():
    assert employee_NamedEntity.__init__(employee_NamedEntity(''), '') == None

