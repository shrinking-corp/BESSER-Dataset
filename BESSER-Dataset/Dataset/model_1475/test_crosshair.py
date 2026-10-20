from python_code import Graph_Graph
from python_code import Graph_GraphElement

def test_Graph_GraphElement___init__():
    assert Graph_GraphElement.__init__(Graph_GraphElement('', '\x00', GraphElement=Graph_Graph(), contents=Graph_Graph()), '\x00\x00', '', GraphElement=Graph_Graph(), contents=Graph_Graph()) == None


from python_code import Graph_NamedElement

def test_Graph_NamedElement___init__():
    assert Graph_NamedElement.__init__(Graph_NamedElement(''), '') == None

