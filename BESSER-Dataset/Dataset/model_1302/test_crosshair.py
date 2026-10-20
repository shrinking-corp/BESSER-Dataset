from python_code import stateMachine_IDElement

def test_stateMachine_IDElement___init__():
    assert stateMachine_IDElement.__init__(stateMachine_IDElement(''), '') == None


from python_code import stateMachine_State
from python_code import stateMachine_StateMachine
from python_code import stateMachine_Transition

def test_stateMachine_State___init__():
    assert stateMachine_State.__init__(stateMachine_State('', source=set(), target=set(), State=stateMachine_Transition(), State10=stateMachine_Transition(), stateMachine_State=stateMachine_StateMachine()), '', source=set(), target=set(), State=stateMachine_Transition(), State10=stateMachine_Transition(), stateMachine_State=stateMachine_StateMachine()) == None

