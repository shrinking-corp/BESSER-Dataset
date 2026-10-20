from python_code import graph_Entry
from python_code import graph_Label

def test_graph_Entry___init__():
    assert graph_Entry.__init__(graph_Entry('', '\x00', Entry=graph_Label(), entries=graph_Label()), '\x00\x00', '', Entry=graph_Label(), entries=graph_Label()) == None


from python_code import graph_Edge
from python_code import graph_Graph
from python_code import graph_Vertex

def test_graph_Graph___init__():
    assert graph_Graph.__init__(graph_Graph(False, graph=set(), Graph=graph_Vertex(), Graph10=graph_Edge(), graph2=set()), False, graph=set(), Graph=graph_Vertex(), Graph10=graph_Edge(), graph2=set()) == None


from python_code import graph_GraphElement

def test_graph_GraphElement___init__():
    assert graph_GraphElement.__init__(graph_GraphElement(0), 0) == None


from python_code import graph_Named

def test_graph_Named___init__():
    assert graph_Named.__init__(graph_Named(''), '') == None


from python_code import graph_Typed

def test_graph_Typed___init__():
    assert graph_Typed.__init__(graph_Typed(''), '') == None

