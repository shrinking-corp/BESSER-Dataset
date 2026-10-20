from python_code import statemachine_ExecuteCommand

def test_statemachine_ExecuteCommand___init__():
    assert statemachine_ExecuteCommand.__init__(statemachine_ExecuteCommand('', statemachine_ExecuteCommand=set()), '', statemachine_ExecuteCommand=set()) == None


from python_code import statemachine_Expression
from python_code import statemachine_SetCommand

def test_statemachine_SetCommand___init__():
    assert statemachine_SetCommand.__init__(statemachine_SetCommand('', statemachine_SetCommand=statemachine_Expression()), '', statemachine_SetCommand=statemachine_Expression()) == None


from python_code import statemachine_VerbatimExpression

def test_statemachine_VerbatimExpression___init__():
    assert statemachine_VerbatimExpression.__init__(statemachine_VerbatimExpression(''), '') == None

