from python_code import graph_Graph
from python_code import graph_Node

def test_graph_Node___init__():
    assert graph_Node.__init__(graph_Node('', graph_Node=graph_Graph()), '', graph_Node=graph_Graph()) == None

