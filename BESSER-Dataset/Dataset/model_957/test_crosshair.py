from python_code import graph_Edge
from python_code import graph_Node
from python_code import graph_NodeType

def test_graph_Node___init__():
    assert graph_Node.__init__(graph_Node('', target=set(), source=set(), graph_Node=graph_NodeType(), Node=graph_Edge(), Node6=graph_Edge()), '', target=set(), source=set(), graph_Node=graph_NodeType(), Node=graph_Edge(), Node6=graph_Edge()) == None

