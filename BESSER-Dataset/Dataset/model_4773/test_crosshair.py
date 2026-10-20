from python_code import types_ArrayType

def test_types_ArrayType___init__():
    assert types_ArrayType.__init__(types_ArrayType(0), 0) == None


from python_code import types_EObject
from python_code import types_Operation
from python_code import types_ServiceType
from python_code import types_TypeReference

def test_types_Operation___init__():
    assert types_Operation.__init__(types_Operation('\x00', types_Operation=types_ServiceType(), types_Operation16=types_TypeReference(), types_Operation19=set(), types_Operation22=types_EObject()), '', types_Operation=types_ServiceType(), types_Operation16=types_TypeReference(), types_Operation19=set(), types_Operation22=types_EObject()) == None


from python_code import types_Type
from python_code import types_TypeReference

def test_types_Type___init__():
    assert types_Type.__init__(types_Type('', types_Type=types_TypeReference()), '', types_Type=types_TypeReference()) == None

