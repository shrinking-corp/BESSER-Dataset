from python_code import minuml1_ActionState

def test_minuml1_ActionState___init__():
    assert minuml1_ActionState.__init__(minuml1_ActionState(True), False) == None


from python_code import minuml1_BooleanExpression
from python_code import minuml1_Guard

def test_minuml1_BooleanExpression___init__():
    assert minuml1_BooleanExpression.__init__(minuml1_BooleanExpression('', '\x00', minuml1_BooleanExpression=minuml1_Guard()), '\x00\x00', '', minuml1_BooleanExpression=minuml1_Guard()) == None


from python_code import minuml1_ModelElement
from python_code import minuml1_ObjectFlowState
from python_code import minuml1_Partition

def test_minuml1_ModelElement___init__():
    assert minuml1_ModelElement.__init__(minuml1_ModelElement('', minuml1_ModelElement=minuml1_Partition(), minuml1_ModelElement11=minuml1_ObjectFlowState()), '', minuml1_ModelElement=minuml1_Partition(), minuml1_ModelElement11=minuml1_ObjectFlowState()) == None


from python_code import minuml1_Pseudostate

def test_minuml1_Pseudostate___init__():
    assert minuml1_Pseudostate.__init__(minuml1_Pseudostate(''), '') == None

