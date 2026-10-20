from python_code import activitydiagram_Activity
from python_code import activitydiagram_ActivityEdge
from python_code import activitydiagram_ActivityNode

def test_activitydiagram_ActivityNode___init__():
    assert activitydiagram_ActivityNode.__init__(activitydiagram_ActivityNode(True, ActivityNode=activitydiagram_Activity(), activitydiagram_ActivityNode=activitydiagram_ActivityEdge(), activitydiagram_ActivityNode10=activitydiagram_ActivityEdge(), nodes=activitydiagram_Activity()), False, ActivityNode=activitydiagram_Activity(), activitydiagram_ActivityNode=activitydiagram_ActivityEdge(), activitydiagram_ActivityNode10=activitydiagram_ActivityEdge(), nodes=activitydiagram_Activity()) == None


from python_code import activitydiagram_BooleanBinaryExpression
from python_code import activitydiagram_BooleanExpression

def test_activitydiagram_BooleanBinaryExpression___init__():
    assert activitydiagram_BooleanBinaryExpression.__init__(activitydiagram_BooleanBinaryExpression('', activitydiagram_BooleanBinaryExpression=activitydiagram_BooleanExpression(), activitydiagram_BooleanBinaryExpression64=activitydiagram_BooleanExpression()), '', activitydiagram_BooleanBinaryExpression=activitydiagram_BooleanExpression(), activitydiagram_BooleanBinaryExpression64=activitydiagram_BooleanExpression()) == None


from python_code import activitydiagram_BooleanExpression
from python_code import activitydiagram_BooleanUnaryExpression

def test_activitydiagram_BooleanUnaryExpression___init__():
    assert activitydiagram_BooleanUnaryExpression.__init__(activitydiagram_BooleanUnaryExpression('', activitydiagram_BooleanUnaryExpression=activitydiagram_BooleanExpression()), '', activitydiagram_BooleanUnaryExpression=activitydiagram_BooleanExpression()) == None


from python_code import activitydiagram_BooleanValue

def test_activitydiagram_BooleanValue___init__():
    assert activitydiagram_BooleanValue.__init__(activitydiagram_BooleanValue(True), False) == None


from python_code import activitydiagram_BooleanVariable
from python_code import activitydiagram_BooleanVariableAssignment
from python_code import activitydiagram_ControlFlow

def test_activitydiagram_BooleanVariable___init__():
    assert activitydiagram_BooleanVariable.__init__(activitydiagram_BooleanVariable(True, activitydiagram_BooleanVariable=activitydiagram_ControlFlow(), activitydiagram_BooleanVariable67=activitydiagram_BooleanVariableAssignment()), False, activitydiagram_BooleanVariable=activitydiagram_ControlFlow(), activitydiagram_BooleanVariable67=activitydiagram_BooleanVariableAssignment()) == None


from python_code import activitydiagram_IntegerBinaryExpression
from python_code import activitydiagram_IntegerExpression

def test_activitydiagram_IntegerBinaryExpression___init__():
    assert activitydiagram_IntegerBinaryExpression.__init__(activitydiagram_IntegerBinaryExpression('', activitydiagram_IntegerBinaryExpression=activitydiagram_IntegerExpression(), activitydiagram_IntegerBinaryExpression53=activitydiagram_IntegerExpression()), '', activitydiagram_IntegerBinaryExpression=activitydiagram_IntegerExpression(), activitydiagram_IntegerBinaryExpression53=activitydiagram_IntegerExpression()) == None


from python_code import activitydiagram_IntegerComparisonExpression
from python_code import activitydiagram_IntegerExpression

def test_activitydiagram_IntegerComparisonExpression___init__():
    assert activitydiagram_IntegerComparisonExpression.__init__(activitydiagram_IntegerComparisonExpression('', activitydiagram_IntegerComparisonExpression=activitydiagram_IntegerExpression(), activitydiagram_IntegerComparisonExpression58=activitydiagram_IntegerExpression()), '', activitydiagram_IntegerComparisonExpression=activitydiagram_IntegerExpression(), activitydiagram_IntegerComparisonExpression58=activitydiagram_IntegerExpression()) == None


from python_code import activitydiagram_IntegerValue

def test_activitydiagram_IntegerValue___init__():
    assert activitydiagram_IntegerValue.__init__(activitydiagram_IntegerValue(0), 0) == None


from python_code import activitydiagram_IntegerVariable
from python_code import activitydiagram_IntegerVariableAssignment

def test_activitydiagram_IntegerVariable___init__():
    assert activitydiagram_IntegerVariable.__init__(activitydiagram_IntegerVariable(0, activitydiagram_IntegerVariable=activitydiagram_IntegerVariableAssignment()), 0, activitydiagram_IntegerVariable=activitydiagram_IntegerVariableAssignment()) == None


from python_code import activitydiagram_NamedElement

def test_activitydiagram_NamedElement___init__():
    assert activitydiagram_NamedElement.__init__(activitydiagram_NamedElement(''), '') == None


from python_code import activitydiagram_Activity
from python_code import activitydiagram_Variable

def test_activitydiagram_Variable___init__():
    assert activitydiagram_Variable.__init__(activitydiagram_Variable('', activitydiagram_Variable=activitydiagram_Activity()), '', activitydiagram_Variable=activitydiagram_Activity()) == None

