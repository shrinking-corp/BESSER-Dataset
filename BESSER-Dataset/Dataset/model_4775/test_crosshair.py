from python_code import types_Branch
from python_code import types_Case

def test_types_Case___init__():
    assert types_Case.__init__(types_Case('', types_Case=types_Branch()), '', types_Case=types_Branch()) == None


from python_code import types_Collection

def test_types_Collection___init__():
    assert types_Collection.__init__(types_Collection(''), '') == None


from python_code import types_Enum

def test_types_Enum___init__():
    assert types_Enum.__init__(types_Enum('', '\x00'), '\x00\x00', '') == None


from python_code import types_Struct

def test_types_Struct___init__():
    assert types_Struct.__init__(types_Struct('', False, types_Struct=set(), types_Struct14=set()), '', True, types_Struct=set(), types_Struct14=set()) == None


from python_code import types_Type
from python_code import types_Typedef

def test_types_Typedef___init__():
    assert types_Typedef.__init__(types_Typedef('', types_Typedef=types_Type()), '', types_Typedef=types_Type()) == None

