from python_code import graph_Edge

def test_graph_Edge___init__():
    assert graph_Edge.__init__(graph_Edge(True), False) == None

def test_graph_Edge_update():
    assert graph_Edge.update(graph_Edge(False), 0, '\x00\x00', '') == None


from python_code import graph_Graph

def test_graph_Graph___init__():
    assert graph_Graph.__init__(graph_Graph('', '\x00'), '\x00\x00', '') == None

def test_graph_Graph_addNamedAdjacent():
    assert graph_Graph.addNamedAdjacent(graph_Graph('', ''), '', '', '', '', '') == None

def test_graph_Graph_addAdjacent():
    assert graph_Graph.addAdjacent(graph_Graph('', ''), '', '', '', '') == None

def test_graph_Graph_addVertex():
    assert graph_Graph.addVertex(graph_Graph('', ''), '') == None

def test_graph_Graph_addEdge():
    assert graph_Graph.addEdge(graph_Graph('', ''), '') == None


from python_code import graph_GraphElement

def test_graph_GraphElement___init__():
    assert graph_GraphElement.__init__(graph_GraphElement(''), '') == None


from python_code import graph_Vertex

def test_graph_Vertex___init__():
    assert graph_Vertex.__init__(graph_Vertex(True), False) == None

def test_graph_Vertex_getIncomingEdgeFrom():
    assert graph_Vertex.getIncomingEdgeFrom(graph_Vertex(False), 0) == None

def test_graph_Vertex_hasForIncomingAdjacent():
    assert graph_Vertex.hasForIncomingAdjacent(graph_Vertex(False), 0) == None

def test_graph_Vertex_hasForAdjacent():
    assert graph_Vertex.hasForAdjacent(graph_Vertex(False), 0) == None

def test_graph_Vertex_getOutgoingEdgeTo():
    assert graph_Vertex.getOutgoingEdgeTo(graph_Vertex(False), 0) == None

def test_graph_Vertex_hasForOutgoingAdjacent():
    assert graph_Vertex.hasForOutgoingAdjacent(graph_Vertex(False), 0) == None

def test_graph_Vertex_getEdgeTo():
    assert graph_Vertex.getEdgeTo(graph_Vertex(False), 0) == None

