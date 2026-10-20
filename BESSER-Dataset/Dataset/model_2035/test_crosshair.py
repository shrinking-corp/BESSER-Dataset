from python_code import dsl_Event
from python_code import dsl_Statemachine
from python_code import dsl_Transition

def test_dsl_Event___init__():
    assert dsl_Event.__init__(dsl_Event('', '\x00', dsl_Event21=dsl_Transition(), dsl_Event=dsl_Statemachine(), dsl_Event3=dsl_Statemachine()), '\x00\x00', '', dsl_Event21=dsl_Transition(), dsl_Event=dsl_Statemachine(), dsl_Event3=dsl_Statemachine()) == None

