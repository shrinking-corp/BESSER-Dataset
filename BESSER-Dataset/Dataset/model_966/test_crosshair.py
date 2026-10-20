from python_code import simplegraph_Element
from python_code import simplegraph_Graph

def test_simplegraph_Graph___init__():
    assert simplegraph_Graph.__init__(simplegraph_Graph('', Graph=simplegraph_Element(), graph=set()), '', Graph=simplegraph_Element(), graph=set()) == None


from python_code import simplegraph_Edge
from python_code import simplegraph_Node

def test_simplegraph_Node___init__():
    assert simplegraph_Node.__init__(simplegraph_Node('', target=set(), source=set(), Node=simplegraph_Edge(), Node5=simplegraph_Edge()), '', target=set(), source=set(), Node=simplegraph_Edge(), Node5=simplegraph_Edge()) == None

