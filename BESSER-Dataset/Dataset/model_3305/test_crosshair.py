from python_code import graphgenerators_GraphGenerator

def test_graphgenerators_GraphGenerator___init__():
    assert graphgenerators_GraphGenerator.__init__(graphgenerators_GraphGenerator()) == None

def test_graphgenerators_GraphGenerator_getGraph():
    assert graphgenerators_GraphGenerator.getGraph(graphgenerators_GraphGenerator()) == None


from python_code import graphgenerators_LatticeGraphGenerator

def test_graphgenerators_LatticeGraphGenerator___init__():
    assert graphgenerators_LatticeGraphGenerator.__init__(graphgenerators_LatticeGraphGenerator(False, False, False), False, False, False) == None


from python_code import graphgenerators_MigrationEdgeGraphGenerator

def test_graphgenerators_MigrationEdgeGraphGenerator___init__():
    assert graphgenerators_MigrationEdgeGraphGenerator.__init__(graphgenerators_MigrationEdgeGraphGenerator('\x00', 0.0, ''), '', 0.0, '') == None


from python_code import graphgenerators_PajekNetGraphGenerator

def test_graphgenerators_PajekNetGraphGenerator___init__():
    assert graphgenerators_PajekNetGraphGenerator.__init__(graphgenerators_PajekNetGraphGenerator('', 0.0, 0, 0), '', 0.0, 0, 0) == None


from python_code import graphgenerators_PlateCarreeGlobeGraphGenerator

def test_graphgenerators_PlateCarreeGlobeGraphGenerator___init__():
    assert graphgenerators_PlateCarreeGlobeGraphGenerator.__init__(graphgenerators_PlateCarreeGlobeGraphGenerator(0, 0.0), 0, 0.0) == None


from python_code import graphgenerators_SquareLatticeGraphGenerator

def test_graphgenerators_SquareLatticeGraphGenerator___init__():
    assert graphgenerators_SquareLatticeGraphGenerator.__init__(graphgenerators_SquareLatticeGraphGenerator(0, 0, 0.0), 0, 0, 0.0) == None

