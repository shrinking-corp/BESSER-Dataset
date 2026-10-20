from python_code import simplegraph_Edge
from python_code import simplegraph_Graph
from python_code import simplegraph_Node

def test_simplegraph_Node___init__():
    assert simplegraph_Node.__init__(simplegraph_Node('', source=set(), target=set(), Node=simplegraph_Edge(), Node6=simplegraph_Edge(), simplegraph_Node=simplegraph_Graph()), '', source=set(), target=set(), Node=simplegraph_Edge(), Node6=simplegraph_Edge(), simplegraph_Node=simplegraph_Graph()) == None

