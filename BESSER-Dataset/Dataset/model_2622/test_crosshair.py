from python_code import Dot_Graph
from python_code import Dot_GraphElement

def test_Dot_GraphElement___init__():
    assert Dot_GraphElement.__init__(Dot_GraphElement('', '\x00', GraphElement=Dot_Graph(), contents=Dot_Graph()), '\x00\x00', '', GraphElement=Dot_Graph(), contents=Dot_Graph()) == None


from python_code import Dot_NamedElement

def test_Dot_NamedElement___init__():
    assert Dot_NamedElement.__init__(Dot_NamedElement(''), '') == None


from python_code import Dot_DirectedArc
from python_code import Dot_Node

def test_Dot_Node___init__():
    assert Dot_Node.__init__(Dot_Node('', '\x00', Dot_Node=Dot_DirectedArc(), Dot_Node5=Dot_DirectedArc()), '\x00\x00', '', Dot_Node=Dot_DirectedArc(), Dot_Node5=Dot_DirectedArc()) == None

