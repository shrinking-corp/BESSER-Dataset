from python_code import martinfowlerdsl_AbstractEvent
from python_code import martinfowlerdsl_StateMachine

def test_martinfowlerdsl_AbstractEvent___init__():
    assert martinfowlerdsl_AbstractEvent.__init__(martinfowlerdsl_AbstractEvent('', '\x00', martinfowlerdsl_AbstractEvent=martinfowlerdsl_StateMachine()), '\x00\x00', '', martinfowlerdsl_AbstractEvent=martinfowlerdsl_StateMachine()) == None


from python_code import martinfowlerdsl_Event
from python_code import martinfowlerdsl_Transition

def test_martinfowlerdsl_Event___init__():
    assert martinfowlerdsl_Event.__init__(martinfowlerdsl_Event(True, martinfowlerdsl_Event=martinfowlerdsl_Transition()), False, martinfowlerdsl_Event=martinfowlerdsl_Transition()) == None


from python_code import martinfowlerdsl_State
from python_code import martinfowlerdsl_StateMachine
from python_code import martinfowlerdsl_Transition

def test_martinfowlerdsl_State___init__():
    assert martinfowlerdsl_State.__init__(martinfowlerdsl_State('', martinfowlerdsl_State=martinfowlerdsl_StateMachine(), martinfowlerdsl_State3=martinfowlerdsl_StateMachine(), martinfowlerdsl_State7=set(), source=set(), State=martinfowlerdsl_Transition(), martinfowlerdsl_State11=martinfowlerdsl_Transition()), '', martinfowlerdsl_State=martinfowlerdsl_StateMachine(), martinfowlerdsl_State3=martinfowlerdsl_StateMachine(), martinfowlerdsl_State7=set(), source=set(), State=martinfowlerdsl_Transition(), martinfowlerdsl_State11=martinfowlerdsl_Transition()) == None

