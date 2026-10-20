import datetime as _ch_datetime
from python_code import shop_ChequePayment

def test_shop_ChequePayment___init__():
    assert shop_ChequePayment.__init__(shop_ChequePayment(True, _ch_datetime.date(1, 1, 1)), False, _ch_datetime.date(1, 1, 2)) == None


import datetime as _ch_datetime
from python_code import shop_Person

def test_shop_Person___init__():
    assert shop_Person.__init__(shop_Person('', '', _ch_datetime.date(1, 1, 1), '', '', ''), '', '', _ch_datetime.date(1, 1, 1), '', '', '') == None

def test_shop_Person_getDisplayName():
    assert shop_Person.getDisplayName(shop_Person('\x00', '\x00\x00', _ch_datetime.date(1, 1, 1), '', '', '')) == None


import datetime as _ch_datetime
from python_code import shop_Valuable

def test_shop_Valuable___init__():
    assert shop_Valuable.__init__(shop_Valuable(_ch_datetime.date(1, 1, 1), 0.0), _ch_datetime.date(1, 1, 1), 0.0) == None

