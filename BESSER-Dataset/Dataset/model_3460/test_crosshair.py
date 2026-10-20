from python_code import coCoMM_HardLimitDR
from python_code import coCoMM_HardLimitDRExpression

def test_coCoMM_HardLimitDRExpression___init__():
    assert coCoMM_HardLimitDRExpression.__init__(coCoMM_HardLimitDRExpression('', '\x00', coCoMM_HardLimitDRExpression=coCoMM_HardLimitDR()), '\x00\x00', '', coCoMM_HardLimitDRExpression=coCoMM_HardLimitDR()) == None


import datetime as _ch_datetime
from python_code import coCoMM_CoCo
from python_code import coCoMM_Project

def test_coCoMM_Project___init__():
    assert coCoMM_Project.__init__(coCoMM_Project('', _ch_datetime.date(1, 1, 1), False, coCoMM_Project=coCoMM_CoCo(), coCoMM_Project54=set(), coCoMM_Project57=set()), '', _ch_datetime.date(1, 1, 1), False, coCoMM_Project=coCoMM_CoCo(), coCoMM_Project54=set(), coCoMM_Project57=set()) == None

