from python_code import testmerge_A
from python_code import testmerge_B

def test_testmerge_B___init__():
    assert testmerge_B.__init__(testmerge_B('', B=testmerge_A(), toB=testmerge_A()), '', B=testmerge_A(), toB=testmerge_A()) == None

def test_testmerge_B_getA():
    assert testmerge_B.getA(testmerge_B('', B=testmerge_A(), toB=testmerge_A()), 0) == None

