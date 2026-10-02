from python_code import grapho_GraphElement
from python_code import grapho_GraphO

def test_grapho_GraphElement___init__():
    assert grapho_GraphElement.__init__(grapho_GraphElement('', grapho_GraphElement=grapho_GraphO()), '', grapho_GraphElement=grapho_GraphO()) == None

from python_code import grapho_GraphOEditor

def test_grapho_GraphOEditor___init__():
    assert grapho_GraphOEditor.__init__(grapho_GraphOEditor()) == None

def test_grapho_GraphOEditor_addEdge():
    assert grapho_GraphOEditor.addEdge(grapho_GraphOEditor()) == None

def test_grapho_GraphOEditor_addNode():
    assert grapho_GraphOEditor.addNode(grapho_GraphOEditor()) == None
