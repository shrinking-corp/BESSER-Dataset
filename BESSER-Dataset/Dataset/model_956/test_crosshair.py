from python_code import graph_Edge
from python_code import graph_Graph
from python_code import graph_Node

def test_graph_Node___init__():
    assert graph_Node.__init__(graph_Node('', graph_Node=graph_Graph(), source=set(), target=set(), Node=graph_Edge(), Node6=graph_Edge()), '', graph_Node=graph_Graph(), source=set(), target=set(), Node=graph_Edge(), Node6=graph_Edge()) == None

