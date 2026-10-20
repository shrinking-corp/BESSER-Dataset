from python_code import types_ArrayType
from python_code import types_Type

def test_types_ArrayType___init__():
    assert types_ArrayType.__init__(types_ArrayType(0, types_ArrayType=types_Type()), 0, types_ArrayType=types_Type()) == None


from python_code import types_EnumerationType
from python_code import types_Enumerator

def test_types_Enumerator___init__():
    assert types_Enumerator.__init__(types_Enumerator('', Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()), '', Enumerator=types_EnumerationType(), enumerator=types_EnumerationType()) == None


from python_code import types_Type
from python_code import types_TypeConstraint

def test_types_TypeConstraint___init__():
    assert types_TypeConstraint.__init__(types_TypeConstraint('', types_TypeConstraint=types_Type()), '', types_TypeConstraint=types_Type()) == None

