from python_code import companies_company

def test_companies_company___init__():
    assert companies_company.__init__(companies_company('', companies_company=set()), '', companies_company=set()) == None


from python_code import companies_department_employees
from python_code import companies_department_manager
from python_code import companies_employee

def test_companies_employee___init__():
    assert companies_employee.__init__(companies_employee('', '', 0.0, '', companies_employee=companies_department_manager(), companies_employee12=companies_department_employees()), '', '', 0.0, '', companies_employee=companies_department_manager(), companies_employee12=companies_department_employees()) == None

