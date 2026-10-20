from python_code import dependencies_Equivalence
from python_code import dependencies_Graph

def test_dependencies_Graph___init__():
    assert dependencies_Graph.__init__(dependencies_Graph('', dependencies_Graph=set(), dependencies_Graph2=dependencies_Equivalence()), '', dependencies_Graph=set(), dependencies_Graph2=dependencies_Equivalence()) == None


from python_code import dependencies_NamedElement

def test_dependencies_NamedElement___init__():
    assert dependencies_NamedElement.__init__(dependencies_NamedElement(''), '') == None

