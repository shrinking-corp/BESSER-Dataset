from python_code import actions_GetRealTimeAction

def test_actions_GetRealTimeAction___init__():
    assert actions_GetRealTimeAction.__init__(actions_GetRealTimeAction(''), '') == None


from python_code import actions_ThrowAction

def test_actions_ThrowAction___init__():
    assert actions_ThrowAction.__init__(actions_ThrowAction(''), '') == None


from python_code import ITimeConsumer
from python_code import actions_TimeAction

def test_actions_TimeAction___init__():
    assert actions_TimeAction.__init__(actions_TimeAction(0, actions_TimeAction=ITimeConsumer()), 0, actions_TimeAction=ITimeConsumer()) == None


from python_code import ILogicFunction
from python_code import actions_PreGenerationAction
from python_code import actions_TimedConditionAction

def test_actions_TimedConditionAction___init__():
    assert actions_TimedConditionAction.__init__(actions_TimedConditionAction(0, actions_TimedConditionAction=actions_PreGenerationAction(), actions_TimedConditionAction10=ILogicFunction()), 0, actions_TimedConditionAction=actions_PreGenerationAction(), actions_TimedConditionAction10=ILogicFunction()) == None

