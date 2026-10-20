from python_code import types_EObject
from python_code import types_EnumType

def test_types_EnumType___init__():
    assert types_EnumType.__init__(types_EnumType('', types_EnumType=types_EObject()), '', types_EnumType=types_EObject()) == None

