from python_code import statemachine_Action
from python_code import statemachine_NormalState
from python_code import statemachine_Statement

def test_statemachine_Action___init__():
    assert statemachine_Action.__init__(statemachine_Action('', statemachine_Action=statemachine_Statement(), statemachine_Action20=statemachine_NormalState()), '', statemachine_Action=statemachine_Statement(), statemachine_Action20=statemachine_NormalState()) == None


from python_code import statemachine_StateMachine

def test_statemachine_StateMachine___init__():
    assert statemachine_StateMachine.__init__(statemachine_StateMachine(statemachine_StateMachine=set(), statemachine_StateMachine2=set()), statemachine_StateMachine=set(), statemachine_StateMachine2=set()) == None

def test_statemachine_StateMachine_printReachable():
    assert statemachine_StateMachine.printReachable(statemachine_StateMachine(statemachine_StateMachine=set(), statemachine_StateMachine2=set())) == None

