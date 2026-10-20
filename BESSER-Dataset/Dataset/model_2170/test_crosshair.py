from python_code import dgf_DContainment

def test_dgf_DContainment___init__():
    assert dgf_DContainment.__init__(dgf_DContainment(''), '') == None


from python_code import dgf_DGraphElement
from python_code import dgf_Graph

def test_dgf_DGraphElement___init__():
    assert dgf_DGraphElement.__init__(dgf_DGraphElement('', dgf_DGraphElement=dgf_Graph()), '', dgf_DGraphElement=dgf_Graph()) == None


from python_code import dgf_DContainedElement
from python_code import dgf_DNode
from python_code import dgf_DVertex

def test_dgf_DNode___init__():
    assert dgf_DNode.__init__(dgf_DNode('', dgf_DNode9=dgf_DContainedElement(), dgf_DNode=dgf_DVertex(), dgf_DNode3=dgf_DVertex(), dgf_DNode5=set()), '', dgf_DNode9=dgf_DContainedElement(), dgf_DNode=dgf_DVertex(), dgf_DNode3=dgf_DVertex(), dgf_DNode5=set()) == None


from python_code import dgf_DReference

def test_dgf_DReference___init__():
    assert dgf_DReference.__init__(dgf_DReference(True), False) == None

