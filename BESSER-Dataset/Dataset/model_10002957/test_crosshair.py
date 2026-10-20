from python_code import LocalDoctor

def test_LocalDoctor___init__():
    assert LocalDoctor.__init__(LocalDoctor(0), 0) == None


from python_code import Pharmaceutical

def test_Pharmaceutical___init__():
    assert Pharmaceutical.__init__(Pharmaceutical('\x00\x00', '', medication77=set()), '', '', medication77=set()) == None


import datetime as _ch_datetime
from python_code import Qualification

def test_Qualification___init__():
    assert Qualification.__init__(Qualification(_ch_datetime.date(1, 1, 1), '\x00', '\x00\x00'), _ch_datetime.date(1, 1, 1), '', '') == None


from python_code import Supplier

def test_Supplier___init__():
    assert Supplier.__init__(Supplier('', '', Supplier_Supply_052=set()), '', '', Supplier_Supply_052=set()) == None


import datetime as _ch_datetime
from python_code import WorkExperience

def test_WorkExperience___init__():
    assert WorkExperience.__init__(WorkExperience('', '\x00', _ch_datetime.date(1, 1, 3), _ch_datetime.date(1, 1, 1)), '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None

