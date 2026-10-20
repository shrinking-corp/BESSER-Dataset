from python_code import entities_Package
from python_code import entities_PackagedType

def test_entities_PackagedType___init__():
    assert entities_PackagedType.__init__(entities_PackagedType('', entities_PackagedType=entities_Package()), '', entities_PackagedType=entities_Package()) == None


from python_code import entities_Entity
from python_code import entities_Property
from python_code import entities_Type

def test_entities_Property___init__():
    assert entities_Property.__init__(entities_Property('', False, entities_Property9=entities_Entity(), entities_Property=entities_Type()), '', False, entities_Property9=entities_Entity(), entities_Property=entities_Type()) == None

