from python_code import fowlerdsl_Event
from python_code import fowlerdsl_Statemachine
from python_code import fowlerdsl_Transition

def test_fowlerdsl_Event___init__():
    assert fowlerdsl_Event.__init__(fowlerdsl_Event(False, '', '\x00\x00', fowlerdsl_Event=fowlerdsl_Statemachine(), fowlerdsl_Event12=fowlerdsl_Transition()), False, '', '', fowlerdsl_Event=fowlerdsl_Statemachine(), fowlerdsl_Event12=fowlerdsl_Transition()) == None


from python_code import fowlerdsl_State
from python_code import fowlerdsl_Statemachine
from python_code import fowlerdsl_Transition

def test_fowlerdsl_State___init__():
    assert fowlerdsl_State.__init__(fowlerdsl_State('', fowlerdsl_State=fowlerdsl_Statemachine(), fowlerdsl_State6=set(), fowlerdsl_State9=set(), fowlerdsl_State15=fowlerdsl_Transition()), '', fowlerdsl_State=fowlerdsl_Statemachine(), fowlerdsl_State6=set(), fowlerdsl_State9=set(), fowlerdsl_State15=fowlerdsl_Transition()) == None

