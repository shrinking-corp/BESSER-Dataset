import datetime as _ch_datetime
from python_code import Order

def test_Order___init__():
    assert Order.__init__(Order(0, _ch_datetime.date(1, 1, 1), '', float('inf'), '', items6=set()), 0, _ch_datetime.date(1, 1, 2), '', 0.0, '', items6=set()) == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('\x00\x00', '', lineItems4=set()), '', '', lineItems4=set()) == None

