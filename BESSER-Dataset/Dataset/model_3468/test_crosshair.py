from python_code import coCoMM_HardLimitCC
from python_code import coCoMM_HardLimitCCExpression

def test_coCoMM_HardLimitCCExpression___init__():
    assert coCoMM_HardLimitCCExpression.__init__(coCoMM_HardLimitCCExpression('', '\x00', coCoMM_HardLimitCCExpression=coCoMM_HardLimitCC()), '\x00\x00', '', coCoMM_HardLimitCCExpression=coCoMM_HardLimitCC()) == None

