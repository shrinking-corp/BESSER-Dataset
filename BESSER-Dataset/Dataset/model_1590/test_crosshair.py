from python_code import petrinet_Arc
from python_code import petrinet_Node
from python_code import petrinet_PNGraph

def test_petrinet_Arc___init__():
    assert petrinet_Arc.__init__(petrinet_Arc('', petrinet_Arc=petrinet_PNGraph(), petrinet_Arc6=petrinet_Node(), petrinet_Arc8=petrinet_Node()), '', petrinet_Arc=petrinet_PNGraph(), petrinet_Arc6=petrinet_Node(), petrinet_Arc8=petrinet_Node()) == None


from python_code import petrinet_PNGraph
from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place('', '\x00', petrinet_Place=petrinet_PNGraph()), '\x00\x00', '', petrinet_Place=petrinet_PNGraph()) == None


from python_code import petrinet_PNGraph
from python_code import petrinet_Transition

def test_petrinet_Transition___init__():
    assert petrinet_Transition.__init__(petrinet_Transition('', petrinet_Transition=petrinet_PNGraph()), '', petrinet_Transition=petrinet_PNGraph()) == None

