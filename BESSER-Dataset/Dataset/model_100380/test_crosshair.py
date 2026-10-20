from python_code import myDsl_Event
from python_code import myDsl_Statemachine
from python_code import myDsl_Transition

def test_myDsl_Event___init__():
    assert myDsl_Event.__init__(myDsl_Event(False, '\x00', myDsl_Event=myDsl_Statemachine(), myDsl_Event13=myDsl_Transition()), False, '\x00', myDsl_Event=myDsl_Statemachine(), myDsl_Event13=myDsl_Transition()) == None


from python_code import myDsl_JvmTypeReference
from python_code import myDsl_Service
from python_code import myDsl_Statemachine

def test_myDsl_Service___init__():
    assert myDsl_Service.__init__(myDsl_Service('', myDsl_Service=myDsl_Statemachine(), myDsl_Service6=myDsl_JvmTypeReference()), '', myDsl_Service=myDsl_Statemachine(), myDsl_Service6=myDsl_JvmTypeReference()) == None


from python_code import myDsl_State
from python_code import myDsl_Statemachine
from python_code import myDsl_Transition
from python_code import myDsl_XExpression

def test_myDsl_State___init__():
    assert myDsl_State.__init__(myDsl_State('', myDsl_State8=myDsl_XExpression(), myDsl_State10=set(), myDsl_State=myDsl_Statemachine(), myDsl_State16=myDsl_Transition()), '', myDsl_State8=myDsl_XExpression(), myDsl_State10=set(), myDsl_State=myDsl_Statemachine(), myDsl_State16=myDsl_Transition()) == None

