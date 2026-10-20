from python_code import restbehavior_Constant
from python_code import restbehavior_DataType

def test_restbehavior_Constant___init__():
    assert restbehavior_Constant.__init__(restbehavior_Constant('', restbehavior_Constant=restbehavior_DataType()), '', restbehavior_Constant=restbehavior_DataType()) == None


from python_code import restbehavior_InternalMessage
from python_code import restbehavior_MessageAction

def test_restbehavior_InternalMessage___init__():
    assert restbehavior_InternalMessage.__init__(restbehavior_InternalMessage('', restbehavior_InternalMessage=restbehavior_MessageAction()), '', restbehavior_InternalMessage=restbehavior_MessageAction()) == None


from python_code import restbehavior_DataType
from python_code import restbehavior_OpType

def test_restbehavior_OpType___init__():
    assert restbehavior_OpType.__init__(restbehavior_OpType('', restbehavior_OpType=restbehavior_DataType()), '', restbehavior_OpType=restbehavior_DataType()) == None


from python_code import restbehavior_BehaviorSpecification
from python_code import restbehavior_State
from python_code import restbehavior_Transition

def test_restbehavior_State___init__():
    assert restbehavior_State.__init__(restbehavior_State('', restbehavior_State15=set(), restbehavior_State20=restbehavior_Transition(), restbehavior_State=restbehavior_BehaviorSpecification(), restbehavior_State10=restbehavior_BehaviorSpecification(), restbehavior_State13=set()), '', restbehavior_State15=set(), restbehavior_State20=restbehavior_Transition(), restbehavior_State=restbehavior_BehaviorSpecification(), restbehavior_State10=restbehavior_BehaviorSpecification(), restbehavior_State13=set()) == None


from python_code import restbehavior_ReturnAction
from python_code import restbehavior_StatusCode

def test_restbehavior_StatusCode___init__():
    assert restbehavior_StatusCode.__init__(restbehavior_StatusCode(0, restbehavior_StatusCode=restbehavior_ReturnAction()), 0, restbehavior_StatusCode=restbehavior_ReturnAction()) == None

