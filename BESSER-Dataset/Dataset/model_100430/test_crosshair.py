from python_code import statemachine_Action
from python_code import statemachine_NormalState

def test_statemachine_Action___init__():
    assert statemachine_Action.__init__(statemachine_Action('', '\x00', statemachine_Action=statemachine_NormalState()), '\x00\x00', '', statemachine_Action=statemachine_NormalState()) == None

from python_code import statemachine_StateMachine

def test_statemachine_StateMachine___init__():
    assert statemachine_StateMachine.__init__(statemachine_StateMachine(statemachine_StateMachine2=set(), statemachine_StateMachine=set()), statemachine_StateMachine2=set(), statemachine_StateMachine=set()) == None

def test_statemachine_StateMachine_printReachable():
    assert statemachine_StateMachine.printReachable(statemachine_StateMachine(statemachine_StateMachine2=set(), statemachine_StateMachine=set())) == None
