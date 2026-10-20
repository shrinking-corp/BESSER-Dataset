from python_code import entities_Import
from python_code import entities_Model

def test_entities_Import___init__():
    assert entities_Import.__init__(entities_Import('', entities_Import=entities_Model()), '', entities_Import=entities_Model()) == None


from python_code import entities_Entity
from python_code import entities_Property

def test_entities_Property___init__():
    assert entities_Property.__init__(entities_Property('', False, entities_Property=entities_Entity()), '', False, entities_Property=entities_Entity()) == None


from python_code import entities_Model
from python_code import entities_Type

def test_entities_Type___init__():
    assert entities_Type.__init__(entities_Type('', entities_Type=entities_Model()), '', entities_Type=entities_Model()) == None

