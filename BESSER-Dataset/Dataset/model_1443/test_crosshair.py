from python_code import simpleGraph_GraphElement

def test_simpleGraph_GraphElement___init__():
    assert simpleGraph_GraphElement.__init__(simpleGraph_GraphElement(0, False, simpleGraph_GraphElement=set()), 0, False, simpleGraph_GraphElement=set()) == None


from python_code import simpleGraph_Edge
from python_code import simpleGraph_Label
from python_code import simpleGraph_Node

def test_simpleGraph_Label___init__():
    assert simpleGraph_Label.__init__(simpleGraph_Label('', simpleGraph_Label=simpleGraph_Edge(), simpleGraph_Label16=simpleGraph_Node()), '', simpleGraph_Label=simpleGraph_Edge(), simpleGraph_Label16=simpleGraph_Node()) == None


from python_code import simpleGraph_Position

def test_simpleGraph_Position___init__():
    assert simpleGraph_Position.__init__(simpleGraph_Position(0, 0), 0, 0) == None

