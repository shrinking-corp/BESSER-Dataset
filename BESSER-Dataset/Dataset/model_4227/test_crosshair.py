from python_code import company_Company
from python_code import company_Department

def test_company_Department___init__():
    assert company_Department.__init__(company_Department(0, 0, company_Department=company_Company(), company_Department2=set()), 0, 0, company_Department=company_Company(), company_Department2=set()) == None


from python_code import company_NamedElement

def test_company_NamedElement___init__():
    assert company_NamedElement.__init__(company_NamedElement(''), '') == None

