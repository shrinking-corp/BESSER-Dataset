from python_code import petrinet_Arc
from python_code import petrinet_Node
from python_code import petrinet_Petrinet

def test_petrinet_Node___init__():
    assert petrinet_Node.__init__(petrinet_Node('', petrinet_Node=petrinet_Petrinet(), Node8=petrinet_Arc(), target=set(), source=set(), Node=petrinet_Arc()), '', petrinet_Node=petrinet_Petrinet(), Node8=petrinet_Arc(), target=set(), source=set(), Node=petrinet_Arc()) == None


from python_code import petrinet_Place

def test_petrinet_Place___init__():
    assert petrinet_Place.__init__(petrinet_Place(0), 0) == None

