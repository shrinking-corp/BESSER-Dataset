from python_code import ClassA

def test_ClassA___init__():
    assert ClassA.__init__(ClassA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


import datetime as _ch_datetime
from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None

