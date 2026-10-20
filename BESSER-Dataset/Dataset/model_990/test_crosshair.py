from python_code import notation_AbsoluteBendPoint

def test_notation_AbsoluteBendPoint___init__():
    assert notation_AbsoluteBendPoint.__init__(notation_AbsoluteBendPoint(0, 0), 0, 0) == None


from python_code import notation_Anchor
from python_code import notation_Edge

def test_notation_Anchor___init__():
    assert notation_Anchor.__init__(notation_Anchor(0, 0, notation_Anchor=notation_Edge(), notation_Anchor13=notation_Edge()), 0, 0, notation_Anchor=notation_Edge(), notation_Anchor13=notation_Edge()) == None


from python_code import notation_DiagramElement
from python_code import notation_EObject

def test_notation_DiagramElement___init__():
    assert notation_DiagramElement.__init__(notation_DiagramElement(False, False, notation_DiagramElement=notation_EObject()), False, False, notation_DiagramElement=notation_EObject()) == None


from python_code import notation_Edge
from python_code import notation_HierarchicalNode
from python_code import notation_Node

def test_notation_Node___init__():
    assert notation_Node.__init__(notation_Node(0, 0, 0, 0, source=set(), target=set(), nodes=notation_HierarchicalNode(), Node=notation_Edge(), Node7=notation_Edge(), Node16=notation_HierarchicalNode()), 0, 0, 0, 0, source=set(), target=set(), nodes=notation_HierarchicalNode(), Node=notation_Edge(), Node7=notation_Edge(), Node16=notation_HierarchicalNode()) == None


from python_code import notation_RelativeBendPoint

def test_notation_RelativeBendPoint___init__():
    assert notation_RelativeBendPoint.__init__(notation_RelativeBendPoint(0, 0, 0, 0), 0, 0, 0, 0) == None

