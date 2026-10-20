from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', '', '\x00\x00'), '', '', '') == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', '\x00'), '\x00\x00', '') == None


import datetime as _ch_datetime
from python_code import ShoppingCart

def test_ShoppingCart___init__():
    assert ShoppingCart.__init__(ShoppingCart(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None

