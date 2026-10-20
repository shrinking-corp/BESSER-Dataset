from python_code import SimpleTree_File
from python_code import SimpleTree_TreeElement

def test_SimpleTree_TreeElement___init__():
    assert SimpleTree_TreeElement.__init__(SimpleTree_TreeElement(0, '\x00', SimpleTree_TreeElement=SimpleTree_File()), 0, '\x00', SimpleTree_TreeElement=SimpleTree_File()) == None

