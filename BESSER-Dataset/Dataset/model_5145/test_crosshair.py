from python_code import testmerge_A3
from python_code import testmerge_B3

def test_testmerge_B3___init__():
    assert testmerge_B3.__init__(testmerge_B3(B3=testmerge_A3(), toB3=testmerge_A3()), B3=testmerge_A3(), toB3=testmerge_A3()) == None

def test_testmerge_B3_getA():
    assert testmerge_B3.getA(testmerge_B3(B3=testmerge_A3(), toB3=testmerge_A3()), '') == None

