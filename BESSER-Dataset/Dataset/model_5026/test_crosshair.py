from python_code import company_Addressable

def test_company_Addressable___init__():
    assert company_Addressable.__init__(company_Addressable('', '', '\x00\x00'), '', '', '') == None


from python_code import company_Company
from python_code import company_Customer
from python_code import company_SalesOrder

def test_company_SalesOrder___init__():
    assert company_SalesOrder.__init__(company_SalesOrder(0, SalesOrder=company_Customer(), company_SalesOrder=company_Company(), salesOrders=company_Customer()), 0, SalesOrder=company_Customer(), company_SalesOrder=company_Company(), salesOrders=company_Customer()) == None

