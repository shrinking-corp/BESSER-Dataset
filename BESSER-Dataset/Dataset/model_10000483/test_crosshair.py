import datetime as _ch_datetime
from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person('', '\x00'), '\x00\x00', '') == None

