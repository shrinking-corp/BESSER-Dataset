import datetime as _ch_datetime
from python_code import family_Family
from python_code import family_Person

def test_family_Person___init__():
    assert family_Person.__init__(family_Person('', '\x00', _ch_datetime.date(1, 1, 3), family_Person=family_Family()), '', '', _ch_datetime.date(1, 1, 1), family_Person=family_Family()) == None

