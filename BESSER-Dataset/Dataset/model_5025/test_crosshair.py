from python_code import model1_Address

def test_model1_Address___init__():
    assert model1_Address.__init__(model1_Address('', '', '\x00\x00'), '', '', '') == None


from python_code import model1_OrderAddress

def test_model1_OrderAddress___init__():
    assert model1_OrderAddress.__init__(model1_OrderAddress(True), False) == None


from python_code import model1_Company
from python_code import model1_Customer
from python_code import model1_ProductToOrder
from python_code import model1_SalesOrder

def test_model1_SalesOrder___init__():
    assert model1_SalesOrder.__init__(model1_SalesOrder(0, SalesOrder=model1_Customer(), model1_SalesOrder=model1_Company(), salesOrders=model1_Customer(), model1_SalesOrder31=model1_ProductToOrder()), 0, SalesOrder=model1_Customer(), model1_SalesOrder=model1_Company(), salesOrders=model1_Customer(), model1_SalesOrder31=model1_ProductToOrder()) == None

