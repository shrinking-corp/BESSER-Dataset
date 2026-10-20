from python_code import RelationalDBContent_DataBase

def test_RelationalDBContent_DataBase___init__():
    assert RelationalDBContent_DataBase.__init__(RelationalDBContent_DataBase('', database=set()), '', database=set()) == None


from python_code import RelationalDBContent_NamedElement

def test_RelationalDBContent_NamedElement___init__():
    assert RelationalDBContent_NamedElement.__init__(RelationalDBContent_NamedElement(''), '') == None


from python_code import RelationalDBContent_TupleElement
from python_code import Tuple

def test_RelationalDBContent_TupleElement___init__():
    assert RelationalDBContent_TupleElement.__init__(RelationalDBContent_TupleElement('', elements=Tuple()), '', elements=Tuple()) == None

