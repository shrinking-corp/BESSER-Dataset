from python_code import test1_ConceptA
from python_code import test1_ConceptC

def test_test1_ConceptC___init__():
    assert test1_ConceptC.__init__(test1_ConceptC(0, False, test1_ConceptC=test1_ConceptA()), 0, False, test1_ConceptC=test1_ConceptA()) == None

