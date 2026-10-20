from python_code import Costomer

def test_Costomer___init__():
    assert Costomer.__init__(Costomer('', 0, '', '', 0, ship_to1=set(), Costomer_Shipment_02=set()), '', 0, '', '', 0, ship_to1=set(), Costomer_Shipment_02=set()) == None


from python_code import CreditCard

def test_CreditCard___init__():
    assert CreditCard.__init__(CreditCard(0), 0) == None


import datetime as _ch_datetime
from python_code import Shipment

def test_Shipment___init__():
    assert Shipment.__init__(Shipment(0, _ch_datetime.date(1, 1, 1), '', '', has_shippment3=set()), 0, _ch_datetime.date(1, 1, 1), '', '', has_shippment3=set()) == None

