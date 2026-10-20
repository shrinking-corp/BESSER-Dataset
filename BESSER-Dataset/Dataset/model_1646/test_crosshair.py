from python_code import kwas_Leaf

def test_kwas_Leaf___init__():
    assert kwas_Leaf.__init__(kwas_Leaf(0), 0) == None


from python_code import kwas_Bin
from python_code import kwas_Top
from python_code import kwas_Tree

def test_kwas_Tree___init__():
    assert kwas_Tree.__init__(kwas_Tree('\x00\x00', '', 0, 0, kwas_Tree5=kwas_Bin(), kwas_Tree=kwas_Top(), kwas_Tree2=kwas_Bin()), '', '', 0, 0, kwas_Tree5=kwas_Bin(), kwas_Tree=kwas_Top(), kwas_Tree2=kwas_Bin()) == None

