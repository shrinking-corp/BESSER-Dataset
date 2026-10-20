import datetime as _ch_datetime
from python_code import Account

def test_Account___init__():
    assert Account.__init__(Account(0, _ch_datetime.date(1, 1, 2), ''), 0, _ch_datetime.date(1, 1, 2), '') == None


from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', 0, '', item2=set()), '', 0, '', item2=set()) == None

