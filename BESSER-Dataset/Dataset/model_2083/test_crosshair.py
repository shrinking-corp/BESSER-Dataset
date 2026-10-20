from python_code import UATMM_structure_KofN

def test_UATMM_structure_KofN___init__():
    assert UATMM_structure_KofN.__init__(UATMM_structure_KofN(0), 0) == None


from python_code import UATMM_structure_RDEP

def test_UATMM_structure_RDEP___init__():
    assert UATMM_structure_RDEP.__init__(UATMM_structure_RDEP(0.0), 0.0) == None


from python_code import UATMM_structure_AttackTree
from python_code import UATMM_structure_TreeMetaData

def test_UATMM_structure_TreeMetaData___init__():
    assert UATMM_structure_TreeMetaData.__init__(UATMM_structure_TreeMetaData('', '\x00', UATMM_structure_TreeMetaData=UATMM_structure_AttackTree()), '\x00\x00', '', UATMM_structure_TreeMetaData=UATMM_structure_AttackTree()) == None


from python_code import UATMM_structure_Weighted

def test_UATMM_structure_Weighted___init__():
    assert UATMM_structure_Weighted.__init__(UATMM_structure_Weighted(0.0, 0.0), 0.0, 0.0) == None

