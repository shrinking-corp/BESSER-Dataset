from python_code import types_BooleanLiteral

def test_types_BooleanLiteral___init__():
    assert types_BooleanLiteral.__init__(types_BooleanLiteral(True), False) == None


from python_code import types_CharLiteral

def test_types_CharLiteral___init__():
    assert types_CharLiteral.__init__(types_CharLiteral(''), '') == None


from python_code import types_CollectionType
from python_code import types_TypeReference

def test_types_CollectionType___init__():
    assert types_CollectionType.__init__(types_CollectionType(0, types_CollectionType=types_TypeReference()), 0, types_CollectionType=types_TypeReference()) == None


from python_code import types_EntityType

def test_types_EntityType___init__():
    assert types_EntityType.__init__(types_EntityType('', types_EntityType=set()), '', types_EntityType=set()) == None


from python_code import types_EnumerationLiteral
from python_code import types_EnumerationType

def test_types_EnumerationLiteral___init__():
    assert types_EnumerationLiteral.__init__(types_EnumerationLiteral('', types_EnumerationLiteral=types_EnumerationType()), '', types_EnumerationLiteral=types_EnumerationType()) == None


from python_code import types_MapType
from python_code import types_TypeReference

def test_types_MapType___init__():
    assert types_MapType.__init__(types_MapType(0, types_MapType=types_TypeReference(), types_MapType7=types_TypeReference()), 0, types_MapType=types_TypeReference(), types_MapType7=types_TypeReference()) == None


from python_code import types_Model

def test_types_Model___init__():
    assert types_Model.__init__(types_Model('', types_Model=set(), types_Model2=set()), '', types_Model=set(), types_Model2=set()) == None


from python_code import types_NamedType
from python_code import types_TypeReference

def test_types_NamedType___init__():
    assert types_NamedType.__init__(types_NamedType('', types_NamedType=types_TypeReference()), '', types_NamedType=types_TypeReference()) == None


from python_code import types_NumberLiteral

def test_types_NumberLiteral___init__():
    assert types_NumberLiteral.__init__(types_NumberLiteral(''), '') == None


from python_code import types_StringLiteral

def test_types_StringLiteral___init__():
    assert types_StringLiteral.__init__(types_StringLiteral(''), '') == None

