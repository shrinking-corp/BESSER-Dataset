from python_code import activitydiagram_Activity
from python_code import activitydiagram_ActivityEdge
from python_code import activitydiagram_ActivityNode
from python_code import activitydiagram_Token
from python_code import activitydiagram_Trace

def test_activitydiagram_ActivityNode___init__():
    assert activitydiagram_ActivityNode.__init__(activitydiagram_ActivityNode(False, ActivityNode=activitydiagram_Activity(), source=set(), target=set(), nodes=activitydiagram_Activity(), holder=set(), ActivityNode15=activitydiagram_ActivityEdge(), ActivityNode17=activitydiagram_ActivityEdge(), ActivityNode47=activitydiagram_Token(), activitydiagram_ActivityNode=activitydiagram_Trace()), True, ActivityNode=activitydiagram_Activity(), source=set(), target=set(), nodes=activitydiagram_Activity(), holder=set(), ActivityNode15=activitydiagram_ActivityEdge(), ActivityNode17=activitydiagram_ActivityEdge(), ActivityNode47=activitydiagram_Token(), activitydiagram_ActivityNode=activitydiagram_Trace()) == None


from python_code import activitydiagram_BooleanBinaryExpression
from python_code import activitydiagram_BooleanVariable

def test_activitydiagram_BooleanBinaryExpression___init__():
    assert activitydiagram_BooleanBinaryExpression.__init__(activitydiagram_BooleanBinaryExpression('', activitydiagram_BooleanBinaryExpression=activitydiagram_BooleanVariable(), activitydiagram_BooleanBinaryExpression42=activitydiagram_BooleanVariable()), '', activitydiagram_BooleanBinaryExpression=activitydiagram_BooleanVariable(), activitydiagram_BooleanBinaryExpression42=activitydiagram_BooleanVariable()) == None


from python_code import activitydiagram_BooleanUnaryExpression
from python_code import activitydiagram_BooleanVariable

def test_activitydiagram_BooleanUnaryExpression___init__():
    assert activitydiagram_BooleanUnaryExpression.__init__(activitydiagram_BooleanUnaryExpression('', activitydiagram_BooleanUnaryExpression=activitydiagram_BooleanVariable()), '', activitydiagram_BooleanUnaryExpression=activitydiagram_BooleanVariable()) == None


from python_code import activitydiagram_BooleanValue

def test_activitydiagram_BooleanValue___init__():
    assert activitydiagram_BooleanValue.__init__(activitydiagram_BooleanValue(True), False) == None


from python_code import activitydiagram_ForkedToken
from python_code import activitydiagram_Token

def test_activitydiagram_ForkedToken___init__():
    assert activitydiagram_ForkedToken.__init__(activitydiagram_ForkedToken(0, activitydiagram_ForkedToken=activitydiagram_Token()), 0, activitydiagram_ForkedToken=activitydiagram_Token()) == None


from python_code import activitydiagram_IntegerCalculationExpression
from python_code import activitydiagram_IntegerVariable

def test_activitydiagram_IntegerCalculationExpression___init__():
    assert activitydiagram_IntegerCalculationExpression.__init__(activitydiagram_IntegerCalculationExpression('', activitydiagram_IntegerCalculationExpression=activitydiagram_IntegerVariable()), '', activitydiagram_IntegerCalculationExpression=activitydiagram_IntegerVariable()) == None


from python_code import activitydiagram_BooleanVariable
from python_code import activitydiagram_IntegerComparisonExpression

def test_activitydiagram_IntegerComparisonExpression___init__():
    assert activitydiagram_IntegerComparisonExpression.__init__(activitydiagram_IntegerComparisonExpression('', activitydiagram_IntegerComparisonExpression=activitydiagram_BooleanVariable()), '', activitydiagram_IntegerComparisonExpression=activitydiagram_BooleanVariable()) == None


from python_code import activitydiagram_IntegerValue

def test_activitydiagram_IntegerValue___init__():
    assert activitydiagram_IntegerValue.__init__(activitydiagram_IntegerValue(0), 0) == None


from python_code import activitydiagram_NamedElement

def test_activitydiagram_NamedElement___init__():
    assert activitydiagram_NamedElement.__init__(activitydiagram_NamedElement(''), '') == None


from python_code import activitydiagram_Activity
from python_code import activitydiagram_InputValue
from python_code import activitydiagram_Value
from python_code import activitydiagram_Variable

def test_activitydiagram_Variable___init__():
    assert activitydiagram_Variable.__init__(activitydiagram_Variable('', activitydiagram_Variable=activitydiagram_Activity(), activitydiagram_Variable6=activitydiagram_Activity(), activitydiagram_Variable23=activitydiagram_Value(), activitydiagram_Variable25=activitydiagram_Value(), activitydiagram_Variable54=activitydiagram_InputValue()), '', activitydiagram_Variable=activitydiagram_Activity(), activitydiagram_Variable6=activitydiagram_Activity(), activitydiagram_Variable23=activitydiagram_Value(), activitydiagram_Variable25=activitydiagram_Value(), activitydiagram_Variable54=activitydiagram_InputValue()) == None

