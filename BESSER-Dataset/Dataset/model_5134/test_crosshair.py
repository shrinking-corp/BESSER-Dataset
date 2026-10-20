from python_code import TestMerge_A
from python_code import TestMerge_B

def test_TestMerge_A___init__():
    assert TestMerge_A.__init__(TestMerge_A('', TestMerge_A=TestMerge_B()), '', TestMerge_A=TestMerge_B()) == None

