from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(0, order14=set()), 0, order14=set()) == None


from python_code import Inventory

def test_Inventory___init__():
    assert Inventory.__init__(Inventory(0, 0, float('inf'), store2=set(), items8=set()), 0, 0, 0.0, store2=set(), items8=set()) == None


from python_code import Vendor

def test_Vendor___init__():
    assert Vendor.__init__(Vendor(0, 0, '', purchaseOrder4=set()), 0, 0, '', purchaseOrder4=set()) == None

