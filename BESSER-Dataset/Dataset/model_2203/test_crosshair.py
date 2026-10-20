from python_code import MMTree_Leaf

def test_MMTree_Leaf___init__():
    assert MMTree_Leaf.__init__(MMTree_Leaf(''), '') == None


from python_code import MMTree_Node
from python_code import MMTree_TreeElement

def test_MMTree_TreeElement___init__():
    assert MMTree_TreeElement.__init__(MMTree_TreeElement('', MMTree_TreeElement=MMTree_Node()), '', MMTree_TreeElement=MMTree_Node()) == None

