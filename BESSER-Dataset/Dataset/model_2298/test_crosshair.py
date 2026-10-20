import datetime as _ch_datetime
from python_code import Persons_Person
from python_code import Persons_PersonRegister

def test_Persons_Person___init__():
    assert Persons_Person.__init__(Persons_Person('', _ch_datetime.date(1, 1, 1), Person=Persons_PersonRegister(), persons=Persons_PersonRegister()), '', _ch_datetime.date(1, 1, 2), Person=Persons_PersonRegister(), persons=Persons_PersonRegister()) == None

