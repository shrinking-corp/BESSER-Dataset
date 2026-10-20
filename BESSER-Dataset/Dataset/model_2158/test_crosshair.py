from python_code import pcg_Edge
from python_code import pcg_Graph
from python_code import pcg_Vertex

def test_pcg_Edge___init__():
    assert pcg_Edge.__init__(pcg_Edge('', pcg_Edge=pcg_Graph(), pcg_Edge6=pcg_Vertex(), pcg_Edge9=pcg_Vertex()), '', pcg_Edge=pcg_Graph(), pcg_Edge6=pcg_Vertex(), pcg_Edge9=pcg_Vertex()) == None


from python_code import pcg_Resource
from python_code import pcg_Vertex

def test_pcg_Resource___init__():
    assert pcg_Resource.__init__(pcg_Resource('', '\x00', pcg_Resource=pcg_Vertex()), '\x00\x00', '', pcg_Resource=pcg_Vertex()) == None

