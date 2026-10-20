from python_code import statemachine_NamedElement

def test_statemachine_NamedElement___init__():
    assert statemachine_NamedElement.__init__(statemachine_NamedElement(''), '') == None


from python_code import statemachine_AbstractState
from python_code import statemachine_StateMachineDescription
from python_code import statemachine_Transition

def test_statemachine_Transition___init__():
    assert statemachine_Transition.__init__(statemachine_Transition('', outcomingTransitions=statemachine_AbstractState(), incomingTransitions=statemachine_AbstractState(), statemachine_Transition=statemachine_StateMachineDescription(), Transition=statemachine_AbstractState(), Transition6=statemachine_AbstractState()), '', outcomingTransitions=statemachine_AbstractState(), incomingTransitions=statemachine_AbstractState(), statemachine_Transition=statemachine_StateMachineDescription(), Transition=statemachine_AbstractState(), Transition6=statemachine_AbstractState()) == None

