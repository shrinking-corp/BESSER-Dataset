from python_code import statesml_Event
from python_code import statesml_StateSystem
from python_code import statesml_Trigger

def test_statesml_Event___init__():
    assert statesml_Event.__init__(statesml_Event('', statesml_Event=statesml_StateSystem(), statesml_Event48=statesml_Trigger()), '', statesml_Event=statesml_StateSystem(), statesml_Event48=statesml_Trigger()) == None

