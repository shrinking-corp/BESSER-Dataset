from python_code import activitydiagram_AcceptEventAction
from python_code import activitydiagram_SignalEvent

def test_activitydiagram_AcceptEventAction___init__():
    assert activitydiagram_AcceptEventAction.__init__(activitydiagram_AcceptEventAction(activitydiagram_AcceptEventAction=activitydiagram_SignalEvent()), activitydiagram_AcceptEventAction=activitydiagram_SignalEvent()) == None

def test_activitydiagram_AcceptEventAction_execute():
    assert activitydiagram_AcceptEventAction.execute(activitydiagram_AcceptEventAction(activitydiagram_AcceptEventAction=activitydiagram_SignalEvent())) == None


from python_code import activitydiagram_ActivityFinalNode

def test_activitydiagram_ActivityFinalNode___init__():
    assert activitydiagram_ActivityFinalNode.__init__(activitydiagram_ActivityFinalNode()) == None

def test_activitydiagram_ActivityFinalNode_execute():
    assert activitydiagram_ActivityFinalNode.execute(activitydiagram_ActivityFinalNode()) == None


from python_code import activitydiagram_BooleanBinaryExpression
from python_code import activitydiagram_BooleanVariable

def test_activitydiagram_BooleanBinaryExpression___init__():
    assert activitydiagram_BooleanBinaryExpression.__init__(activitydiagram_BooleanBinaryExpression('', activitydiagram_BooleanBinaryExpression=activitydiagram_BooleanVariable(), activitydiagram_BooleanBinaryExpression44=activitydiagram_BooleanVariable()), '', activitydiagram_BooleanBinaryExpression=activitydiagram_BooleanVariable(), activitydiagram_BooleanBinaryExpression44=activitydiagram_BooleanVariable()) == None


from python_code import activitydiagram_BooleanUnaryExpression
from python_code import activitydiagram_BooleanVariable

def test_activitydiagram_BooleanUnaryExpression___init__():
    assert activitydiagram_BooleanUnaryExpression.__init__(activitydiagram_BooleanUnaryExpression('', activitydiagram_BooleanUnaryExpression=activitydiagram_BooleanVariable()), '', activitydiagram_BooleanUnaryExpression=activitydiagram_BooleanVariable()) == None


from python_code import activitydiagram_BooleanValue

def test_activitydiagram_BooleanValue___init__():
    assert activitydiagram_BooleanValue.__init__(activitydiagram_BooleanValue(True), False) == None


from python_code import activitydiagram_DecisionNode

def test_activitydiagram_DecisionNode___init__():
    assert activitydiagram_DecisionNode.__init__(activitydiagram_DecisionNode()) == None

def test_activitydiagram_DecisionNode_execute():
    assert activitydiagram_DecisionNode.execute(activitydiagram_DecisionNode()) == None


from python_code import activitydiagram_ForkNode

def test_activitydiagram_ForkNode___init__():
    assert activitydiagram_ForkNode.__init__(activitydiagram_ForkNode()) == None

def test_activitydiagram_ForkNode_execute():
    assert activitydiagram_ForkNode.execute(activitydiagram_ForkNode()) == None


from python_code import activitydiagram_ForkedToken
from python_code import activitydiagram_Token

def test_activitydiagram_ForkedToken___init__():
    assert activitydiagram_ForkedToken.__init__(activitydiagram_ForkedToken(0, activitydiagram_ForkedToken=activitydiagram_Token()), 0, activitydiagram_ForkedToken=activitydiagram_Token()) == None


from python_code import activitydiagram_InitialNode

def test_activitydiagram_InitialNode___init__():
    assert activitydiagram_InitialNode.__init__(activitydiagram_InitialNode()) == None

def test_activitydiagram_InitialNode_execute():
    assert activitydiagram_InitialNode.execute(activitydiagram_InitialNode()) == None


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


from python_code import activitydiagram_JoinNode

def test_activitydiagram_JoinNode___init__():
    assert activitydiagram_JoinNode.__init__(activitydiagram_JoinNode()) == None

def test_activitydiagram_JoinNode_execute():
    assert activitydiagram_JoinNode.execute(activitydiagram_JoinNode()) == None


from python_code import activitydiagram_MergeNode

def test_activitydiagram_MergeNode___init__():
    assert activitydiagram_MergeNode.__init__(activitydiagram_MergeNode()) == None

def test_activitydiagram_MergeNode_execute():
    assert activitydiagram_MergeNode.execute(activitydiagram_MergeNode()) == None


from python_code import activitydiagram_NamedElement

def test_activitydiagram_NamedElement___init__():
    assert activitydiagram_NamedElement.__init__(activitydiagram_NamedElement(''), '') == None


from python_code import activitydiagram_OpaqueAction

def test_activitydiagram_OpaqueAction___init__():
    assert activitydiagram_OpaqueAction.__init__(activitydiagram_OpaqueAction(activitydiagram_OpaqueAction=set()), activitydiagram_OpaqueAction=set()) == None

def test_activitydiagram_OpaqueAction_execute():
    assert activitydiagram_OpaqueAction.execute(activitydiagram_OpaqueAction(activitydiagram_OpaqueAction=set())) == None


from python_code import activitydiagram_SendSignalAction
from python_code import activitydiagram_Signal

def test_activitydiagram_SendSignalAction___init__():
    assert activitydiagram_SendSignalAction.__init__(activitydiagram_SendSignalAction(activitydiagram_SendSignalAction=activitydiagram_Signal()), activitydiagram_SendSignalAction=activitydiagram_Signal()) == None

def test_activitydiagram_SendSignalAction_execute():
    assert activitydiagram_SendSignalAction.execute(activitydiagram_SendSignalAction(activitydiagram_SendSignalAction=activitydiagram_Signal())) == None

