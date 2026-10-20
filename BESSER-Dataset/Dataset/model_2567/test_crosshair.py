from python_code import dsl_Event
from python_code import dsl_StateMachine
from python_code import dsl_Transition

def test_dsl_Event___init__():
    assert dsl_Event.__init__(dsl_Event('', dsl_Event=dsl_StateMachine(), dsl_Event10=dsl_Transition()), '', dsl_Event=dsl_StateMachine(), dsl_Event10=dsl_Transition()) == None


from python_code import dsl_State
from python_code import dsl_StateMachine
from python_code import dsl_Transition

def test_dsl_State___init__():
    assert dsl_State.__init__(dsl_State('', dsl_State=dsl_StateMachine(), dsl_State5=dsl_StateMachine(), dsl_State7=set(), dsl_State13=dsl_Transition()), '', dsl_State=dsl_StateMachine(), dsl_State5=dsl_StateMachine(), dsl_State7=set(), dsl_State13=dsl_Transition()) == None

