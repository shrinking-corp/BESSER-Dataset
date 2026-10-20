from python_code import diagraph_DCompartmentEdge

def test_diagraph_DCompartmentEdge___init__():
    assert diagraph_DCompartmentEdge.__init__(diagraph_DCompartmentEdge('', 0), '', 0) == None


from python_code import diagraph_DLabeledElement
from python_code import diagraph_EClass

def test_diagraph_DLabeledElement___init__():
    assert diagraph_DLabeledElement.__init__(diagraph_DLabeledElement('\x00\x00', '', diagraph_DLabeledElement=diagraph_EClass(), diagraph_DLabeledElement14=set()), '', '', diagraph_DLabeledElement=diagraph_EClass(), diagraph_DLabeledElement14=set()) == None


from python_code import diagraph_DLineEdge

def test_diagraph_DLineEdge___init__():
    assert diagraph_DLineEdge.__init__(diagraph_DLineEdge(''), '') == None

