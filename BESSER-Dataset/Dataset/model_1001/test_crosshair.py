from python_code import GraphML_Data

def test_GraphML_Data___init__():
    assert GraphML_Data.__init__(GraphML_Data('', '\x00'), '\x00\x00', '') == None


from python_code import Graph
from python_code import GraphML_Element

def test_GraphML_Element___init__():
    assert GraphML_Element.__init__(GraphML_Element('', GraphML_Element=set(), contents=Graph()), '', GraphML_Element=set(), contents=Graph()) == None


from python_code import GraphML_LocatedElement

def test_GraphML_LocatedElement___init__():
    assert GraphML_LocatedElement.__init__(GraphML_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import GraphML_Port

def test_GraphML_Port___init__():
    assert GraphML_Port.__init__(GraphML_Port(''), '') == None

