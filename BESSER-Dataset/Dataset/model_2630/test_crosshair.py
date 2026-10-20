from python_code import nodesAndEdges_ColoredNode

def test_nodesAndEdges_ColoredNode___init__():
    assert nodesAndEdges_ColoredNode.__init__(nodesAndEdges_ColoredNode(''), '') == None

def test_nodesAndEdges_ColoredNode_toString():
    assert nodesAndEdges_ColoredNode.toString(nodesAndEdges_ColoredNode('')) == None


from python_code import nodesAndEdges_Edge

def test_nodesAndEdges_Edge___init__():
    assert nodesAndEdges_Edge.__init__(nodesAndEdges_Edge('', '\x00'), '\x00\x00', '') == None

def test_nodesAndEdges_Edge_toString():
    assert nodesAndEdges_Edge.toString(nodesAndEdges_Edge('', '')) == None


from python_code import nodesAndEdges_Node

def test_nodesAndEdges_Node___init__():
    assert nodesAndEdges_Node.__init__(nodesAndEdges_Node(''), '') == None


from python_code import nodesAndEdges_ShapedNode

def test_nodesAndEdges_ShapedNode___init__():
    assert nodesAndEdges_ShapedNode.__init__(nodesAndEdges_ShapedNode(0.0, '\x00\x00'), 0.0, '') == None

def test_nodesAndEdges_ShapedNode_toString():
    assert nodesAndEdges_ShapedNode.toString(nodesAndEdges_ShapedNode(0.0, '\x00')) == None

