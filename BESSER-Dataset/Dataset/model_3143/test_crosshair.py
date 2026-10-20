from python_code import USE_CollectionType
from python_code import USE_Type

def test_USE_CollectionType___init__():
    assert USE_CollectionType.__init__(USE_CollectionType('', USE_CollectionType=USE_Type()), '', USE_CollectionType=USE_Type()) == None


from python_code import USE_SimpleType

def test_USE_SimpleType___init__():
    assert USE_SimpleType.__init__(USE_SimpleType(''), '') == None

