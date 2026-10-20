from python_code import dot_Attribute
from python_code import dot_DirectedEdge
from python_code import dot_UnDirectedEdge

def test_dot_Attribute___init__():
    assert dot_Attribute.__init__(dot_Attribute(0, dot_Attribute=dot_UnDirectedEdge(), dot_Attribute18=dot_DirectedEdge()), 0, dot_Attribute=dot_UnDirectedEdge(), dot_Attribute18=dot_DirectedEdge()) == None


from python_code import dot_Graph
from python_code import dot_GraphModel

def test_dot_Graph___init__():
    assert dot_Graph.__init__(dot_Graph('', dot_Graph=dot_GraphModel()), '', dot_Graph=dot_GraphModel()) == None


from python_code import dot_DirectedEdge
from python_code import dot_Node
from python_code import dot_UnDirectedEdge

def test_dot_Node___init__():
    assert dot_Node.__init__(dot_Node('', dot_Node=dot_UnDirectedEdge(), dot_Node7=dot_UnDirectedEdge(), dot_Node12=dot_DirectedEdge(), dot_Node15=dot_DirectedEdge()), '', dot_Node=dot_UnDirectedEdge(), dot_Node7=dot_UnDirectedEdge(), dot_Node12=dot_DirectedEdge(), dot_Node15=dot_DirectedEdge()) == None

