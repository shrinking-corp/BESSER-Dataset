from python_code import Class
from python_code import Model
from python_code import Persistence

def test_Model___init__():
    assert Model.__init__(Model('\x00', '', '', '', False, '', '', '', False, '', '\x00', class3=Class(), _dataAccess6=Persistence()), '', '', '', '', False, '', '', '', False, '', '', class3=Class(), _dataAccess6=Persistence()) == None


from python_code import Class
from python_code import SaveGameWidget

def test_SaveGameWidget___init__():
    assert SaveGameWidget.__init__(SaveGameWidget('', '', '\x00\x00', class5=Class()), '', '', '', class5=Class()) == None

