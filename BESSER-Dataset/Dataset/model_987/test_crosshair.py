from python_code import qVTcDataDependencyGraph_ClassNode

def test_qVTcDataDependencyGraph_ClassNode___init__():
    assert qVTcDataDependencyGraph_ClassNode.__init__(qVTcDataDependencyGraph_ClassNode('', '\x00'), '\x00\x00', '') == None


from python_code import qVTcDataDependencyGraph_ContainmentEdge

def test_qVTcDataDependencyGraph_ContainmentEdge___init__():
    assert qVTcDataDependencyGraph_ContainmentEdge.__init__(qVTcDataDependencyGraph_ContainmentEdge(''), '') == None


from python_code import qVTcDataDependencyGraph_DependencyEdge

def test_qVTcDataDependencyGraph_DependencyEdge___init__():
    assert qVTcDataDependencyGraph_DependencyEdge.__init__(qVTcDataDependencyGraph_DependencyEdge(False, False, '\x00\x00'), False, False, '') == None


from python_code import qVTcDataDependencyGraph_Element
from python_code import qVTcDataDependencyGraph_Graph

def test_qVTcDataDependencyGraph_Graph___init__():
    assert qVTcDataDependencyGraph_Graph.__init__(qVTcDataDependencyGraph_Graph('', Graph=qVTcDataDependencyGraph_Element(), graph=set()), '', Graph=qVTcDataDependencyGraph_Element(), graph=set()) == None


from python_code import qVTcDataDependencyGraph_EObject
from python_code import qVTcDataDependencyGraph_Edge
from python_code import qVTcDataDependencyGraph_Node

def test_qVTcDataDependencyGraph_Node___init__():
    assert qVTcDataDependencyGraph_Node.__init__(qVTcDataDependencyGraph_Node('', target=set(), source=set(), qVTcDataDependencyGraph_Node=qVTcDataDependencyGraph_EObject(), Node=qVTcDataDependencyGraph_Edge(), Node6=qVTcDataDependencyGraph_Edge()), '', target=set(), source=set(), qVTcDataDependencyGraph_Node=qVTcDataDependencyGraph_EObject(), Node=qVTcDataDependencyGraph_Edge(), Node6=qVTcDataDependencyGraph_Edge()) == None

