from python_code import DOT_Anchor
from python_code import DOT_Compartment

def test_DOT_Anchor___init__():
    assert DOT_Anchor.__init__(DOT_Anchor('', Anchor=DOT_Compartment(), anchor=DOT_Compartment()), '', Anchor=DOT_Compartment(), anchor=DOT_Compartment()) == None

from python_code import DOT_GraphElement
from python_code import DOT_Label

def test_DOT_GraphElement___init__():
    assert DOT_GraphElement.__init__(DOT_GraphElement('', '', '\x00\x00', GraphElement=DOT_Label(), element=DOT_Label()), '', '', '', GraphElement=DOT_Label(), element=DOT_Label()) == None

from python_code import DOT_Node
from python_code import DOT_NodeShape

def test_DOT_Node___init__():
    assert DOT_Node.__init__(DOT_Node(False, '', 0, 0, 0, DOT_Node=DOT_NodeShape()), True, '', 0, 0, 0, DOT_Node=DOT_NodeShape()) == None

from python_code import DOT_PolygonNodeShape

def test_DOT_PolygonNodeShape___init__():
    assert DOT_PolygonNodeShape.__init__(DOT_PolygonNodeShape(0, 0, 0, False, 0), 0, 0, 0, False, 0) == None

from python_code import DOT_Shape

def test_DOT_Shape___init__():
    assert DOT_Shape.__init__(DOT_Shape(0, 0, 0), 0, 0, 0) == None

from python_code import DOT_SimpleCompartment

def test_DOT_SimpleCompartment___init__():
    assert DOT_SimpleCompartment.__init__(DOT_SimpleCompartment(''), '') == None

from python_code import DOT_SimpleLabel

def test_DOT_SimpleLabel___init__():
    assert DOT_SimpleLabel.__init__(DOT_SimpleLabel(''), '') == None

from python_code import DOT_Nodelike
from python_code import DOT_SubGraph

def test_DOT_SubGraph___init__():
    assert DOT_SubGraph.__init__(DOT_SubGraph('', owner=set(), SubGraph=DOT_Nodelike()), '', owner=set(), SubGraph=DOT_Nodelike()) == None
