from python_code import company_Company

def test_company_Company___init__():
    assert company_Company.__init__(company_Company('', company_Company=set()), '', company_Company=set()) == None


from python_code import company_TestClass

def test_company_TestClass___init__():
    assert company_TestClass.__init__(company_TestClass('\x00\x00', '', 0, 0), '', '', 0, 0) == None

