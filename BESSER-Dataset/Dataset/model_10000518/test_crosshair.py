from python_code import Medeina
from python_code import User

def test_Medeina___init__():
    assert Medeina.__init__(Medeina('', User('', '\x00\x00')), '', User('', '')) == None


from python_code import Organization

def test_Organization___init__():
    assert Organization.__init__(Organization(''), '') == None


import datetime as _ch_datetime
from python_code import Pet

def test_Pet___init__():
    assert Pet.__init__(Pet('', '', '', '', '', '', '', '', False, '', _ch_datetime.date(1, 1, 1), 0, '', ''), '', '', '', '', '', '', '', '', False, '', _ch_datetime.date(1, 1, 1), 0, '\x00', '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '\x00'), '\x00\x00', '') == None

