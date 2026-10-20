from python_code import Inventory

def test_Inventory___init__():
    assert Inventory.__init__(Inventory('\x00', 0.0), '', 0.0) == None


from python_code import InventoryType

def test_InventoryType___init__():
    assert InventoryType.__init__(InventoryType(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product(0.0, 0, '', ''), 0.0, 0, '', '') == None

