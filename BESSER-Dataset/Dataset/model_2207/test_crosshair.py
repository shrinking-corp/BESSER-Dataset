from python_code import filetree_FileTree
from python_code import filetree_User

def test_filetree_User___init__():
    assert filetree_User.__init__(filetree_User('\x00\x00', '', '', '', filetree_User=filetree_FileTree()), '', '', '', '', filetree_User=filetree_FileTree()) == None

