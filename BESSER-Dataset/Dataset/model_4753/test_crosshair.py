from python_code import fM_Node

def test_fM_Node___init__():
    assert fM_Node.__init__(fM_Node('\x00\x00', '', fM_Node=set()), '', '', fM_Node=set()) == None

