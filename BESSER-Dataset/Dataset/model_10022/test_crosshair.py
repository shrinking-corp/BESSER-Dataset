from python_code import qvtcorebase_AbstractMapping

def test_qvtcorebase_AbstractMapping___init__():
    assert qvtcorebase_AbstractMapping.__init__(qvtcorebase_AbstractMapping()) == None

def test_qvtcorebase_AbstractMapping_getRefinement():
    assert qvtcorebase_AbstractMapping.getRefinement(qvtcorebase_AbstractMapping()) == None

def test_qvtcorebase_AbstractMapping_getContext():
    assert qvtcorebase_AbstractMapping.getContext(qvtcorebase_AbstractMapping()) == None


from python_code import qvtcorebase_Area
from python_code import qvtcorebase_BottomPattern
from python_code import qvtcorebase_GuardPattern

def test_qvtcorebase_Area___init__():
    assert qvtcorebase_Area.__init__(qvtcorebase_Area(area=qvtcorebase_GuardPattern(), area2=qvtcorebase_BottomPattern(), Area=qvtcorebase_BottomPattern(), Area17=qvtcorebase_GuardPattern()), area=qvtcorebase_GuardPattern(), area2=qvtcorebase_BottomPattern(), Area=qvtcorebase_BottomPattern(), Area17=qvtcorebase_GuardPattern()) == None

def test_qvtcorebase_Area_getAllVariables():
    assert qvtcorebase_Area.getAllVariables(qvtcorebase_Area(area=qvtcorebase_GuardPattern(), area2=qvtcorebase_BottomPattern(), Area=qvtcorebase_BottomPattern(), Area17=qvtcorebase_GuardPattern())) == None


from python_code import qvtcorebase_Assignment
from python_code import qvtcorebase_BottomPattern
from python_code import qvtcorebase_OCLExpression

def test_qvtcorebase_Assignment___init__():
    assert qvtcorebase_Assignment.__init__(qvtcorebase_Assignment('', assignment=qvtcorebase_BottomPattern(), qvtcorebase_Assignment=qvtcorebase_OCLExpression(), Assignment=qvtcorebase_BottomPattern()), '', assignment=qvtcorebase_BottomPattern(), qvtcorebase_Assignment=qvtcorebase_OCLExpression(), Assignment=qvtcorebase_BottomPattern()) == None


from python_code import qvtcorebase_CorePattern

def test_qvtcorebase_CorePattern___init__():
    assert qvtcorebase_CorePattern.__init__(qvtcorebase_CorePattern(qvtcorebase_CorePattern=set()), qvtcorebase_CorePattern=set()) == None

def test_qvtcorebase_CorePattern_getAllVariables():
    assert qvtcorebase_CorePattern.getAllVariables(qvtcorebase_CorePattern(qvtcorebase_CorePattern=set())) == None

def test_qvtcorebase_CorePattern_getArea():
    assert qvtcorebase_CorePattern.getArea(qvtcorebase_CorePattern(qvtcorebase_CorePattern=set())) == None


from python_code import qvtcorebase_BottomPattern
from python_code import qvtcorebase_EnforcementOperation
from python_code import qvtcorebase_OperationCallExp

def test_qvtcorebase_EnforcementOperation___init__():
    assert qvtcorebase_EnforcementOperation.__init__(qvtcorebase_EnforcementOperation('', EnforcementOperation=qvtcorebase_BottomPattern(), enforcementOperation=qvtcorebase_BottomPattern(), qvtcorebase_EnforcementOperation=qvtcorebase_OperationCallExp()), '', EnforcementOperation=qvtcorebase_BottomPattern(), enforcementOperation=qvtcorebase_BottomPattern(), qvtcorebase_EnforcementOperation=qvtcorebase_OperationCallExp()) == None

