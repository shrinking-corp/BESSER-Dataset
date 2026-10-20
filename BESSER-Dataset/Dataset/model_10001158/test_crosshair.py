from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', 0, '', '', 0), '', 0, '', '', 0) == None


from python_code import Order

def test_Order___init__():
    assert Order.__init__(Order('\x00\x00', 0, '', ''), '', 0, '', '') == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', 0, '\x00\x00'), '', 0, '') == None


from python_code import Transaction

def test_Transaction___init__():
    assert Transaction.__init__(Transaction(0, 0, 0), 0, 0, 0) == None


from python_code import Warehouse

def test_Warehouse___init__():
    assert Warehouse.__init__(Warehouse('', '\x00'), '\x00\x00', '') == None

