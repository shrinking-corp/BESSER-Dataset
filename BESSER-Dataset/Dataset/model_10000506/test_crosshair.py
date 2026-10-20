from python_code import Cancelorder

def test_Cancelorder___init__():
    assert Cancelorder.__init__(Cancelorder('', 0), '', 0) == None


from python_code import Customercare

def test_Customercare___init__():
    assert Customercare.__init__(Customercare(0, '', customer27=set(), seller32=set()), 0, '', customer27=set(), seller32=set()) == None


from python_code import Feedback

def test_Feedback___init__():
    assert Feedback.__init__(Feedback('', 0, 0), '\x00', 0, 0) == None


from python_code import Order

def test_Order___init__():
    assert Order.__init__(Order('', 0, '', pRODUCT24=set()), '', 0, '', pRODUCT24=set()) == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', 0, '', '', oRDER25=set(), warehouse30=set()), '', 0, '', '', oRDER25=set(), warehouse30=set()) == None


from python_code import Shipment

def test_Shipment___init__():
    assert Shipment.__init__(Shipment('', warehouse29=set()), '', warehouse29=set()) == None


from python_code import Transaction

def test_Transaction___init__():
    assert Transaction.__init__(Transaction(0), 0) == None


from python_code import sellers_warehouse

def test_sellers_warehouse___init__():
    assert sellers_warehouse.__init__(sellers_warehouse('', '', shipment28=set(), product31=set()), '', '', shipment28=set(), product31=set()) == None

