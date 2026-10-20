from python_code import stateMachine_Event
from python_code import stateMachine_Events
from python_code import stateMachine_Transition

def test_stateMachine_Event___init__():
    assert stateMachine_Event.__init__(stateMachine_Event('', stateMachine_Event=stateMachine_Events(), stateMachine_Event18=stateMachine_Transition()), '', stateMachine_Event=stateMachine_Events(), stateMachine_Event18=stateMachine_Transition()) == None


from python_code import stateMachine_State
from python_code import stateMachine_States
from python_code import stateMachine_Transition

def test_stateMachine_State___init__():
    assert stateMachine_State.__init__(stateMachine_State('', stateMachine_State=stateMachine_States(), stateMachine_State13=stateMachine_States(), stateMachine_State23=stateMachine_Transition(), stateMachine_State15=set()), '', stateMachine_State=stateMachine_States(), stateMachine_State13=stateMachine_States(), stateMachine_State23=stateMachine_Transition(), stateMachine_State15=set()) == None


from python_code import stateMachine_Events
from python_code import stateMachine_StateMachine
from python_code import stateMachine_States
from python_code import stateMachine_Variables

def test_stateMachine_StateMachine___init__():
    assert stateMachine_StateMachine.__init__(stateMachine_StateMachine('', stateMachine_StateMachine=stateMachine_Variables(), stateMachine_StateMachine2=stateMachine_Events(), stateMachine_StateMachine4=stateMachine_States()), '', stateMachine_StateMachine=stateMachine_Variables(), stateMachine_StateMachine2=stateMachine_Events(), stateMachine_StateMachine4=stateMachine_States()) == None

