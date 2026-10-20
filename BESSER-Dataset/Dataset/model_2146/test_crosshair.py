from python_code import graphdb_GraphElement
from python_code import graphdb_Property

def test_graphdb_Property___init__():
    assert graphdb_Property.__init__(graphdb_Property('', '\x00', Property=graphdb_GraphElement(), properties=graphdb_GraphElement()), '\x00\x00', '', Property=graphdb_GraphElement(), properties=graphdb_GraphElement()) == None

