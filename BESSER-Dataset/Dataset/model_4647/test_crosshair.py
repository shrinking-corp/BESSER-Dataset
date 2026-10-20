from python_code import notation_Bounds
from python_code import notation_Node

def test_notation_Bounds___init__():
    assert notation_Bounds.__init__(notation_Bounds(0, 0, notation_Bounds=notation_Node()), 0, 0, notation_Bounds=notation_Node()) == None


from python_code import notation_Diagram

def test_notation_Diagram___init__():
    assert notation_Diagram.__init__(notation_Diagram('', notation_Diagram=set()), '', notation_Diagram=set()) == None


from python_code import notation_Location

def test_notation_Location___init__():
    assert notation_Location.__init__(notation_Location(0, 0), 0, 0) == None


from python_code import notation_MindMapNode

def test_notation_MindMapNode___init__():
    assert notation_MindMapNode.__init__(notation_MindMapNode(False, False, 0), False, False, 0) == None


from python_code import notation_NotationElement

def test_notation_NotationElement___init__():
    assert notation_NotationElement.__init__(notation_NotationElement('', '\x00'), '\x00\x00', '') == None


from python_code import notation_Note

def test_notation_Note___init__():
    assert notation_Note.__init__(notation_Note(''), '') == None


from python_code import notation_EObject
from python_code import notation_Edge
from python_code import notation_View

def test_notation_View___init__():
    assert notation_View.__init__(notation_View('', '', notation_View=set(), notation_View2=notation_EObject(), View=notation_Edge(), View10=notation_Edge(), source=set(), target=set()), '', '', notation_View=set(), notation_View2=notation_EObject(), View=notation_Edge(), View10=notation_Edge(), source=set(), target=set()) == None

def test_notation_View_getAllChildren():
    assert notation_View.getAllChildren(notation_View('\x00\x00', '', notation_View=set(), notation_View2=notation_EObject(), View=notation_Edge(), View10=notation_Edge(), source=set(), target=set())) == None

