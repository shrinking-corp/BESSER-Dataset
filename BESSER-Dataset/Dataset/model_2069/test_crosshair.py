from python_code import Simpletree_File
from python_code import Simpletree_TreeElement

def test_Simpletree_TreeElement___init__():
    assert Simpletree_TreeElement.__init__(Simpletree_TreeElement(0, '\x00', Simpletree_TreeElement=Simpletree_File()), 0, '\x00', Simpletree_TreeElement=Simpletree_File()) == None

