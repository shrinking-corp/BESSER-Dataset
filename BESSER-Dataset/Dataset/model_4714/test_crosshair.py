from python_code import flowgraph_Item

def test_flowgraph_Item___init__():
    assert flowgraph_Item.__init__(flowgraph_Item('', 0), '', 0) == None


from python_code import flowgraph_SimpleStmt

def test_flowgraph_SimpleStmt___init__():
    assert flowgraph_SimpleStmt.__init__(flowgraph_SimpleStmt('', '', '\x00\x00'), '', '', '') == None

