from python_code import GraphMM_Edge
from python_code import GraphMM_Node

def test_GraphMM_Node___init__():
    assert GraphMM_Node.__init__(GraphMM_Node('', '', 0.0, GraphMM_Node=GraphMM_Edge(), GraphMM_Node3=GraphMM_Edge()), '', '', 0.0, GraphMM_Node=GraphMM_Edge(), GraphMM_Node3=GraphMM_Edge()) == None

