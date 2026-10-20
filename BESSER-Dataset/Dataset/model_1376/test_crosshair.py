from python_code import statemachine_Command
from python_code import statemachine_State
from python_code import statemachine_Statemachine

def test_statemachine_Command___init__():
    assert statemachine_Command.__init__(statemachine_Command('', statemachine_Command10=statemachine_State(), statemachine_Command=statemachine_Statemachine()), '', statemachine_Command10=statemachine_State(), statemachine_Command=statemachine_Statemachine()) == None


from python_code import statemachine_Event
from python_code import statemachine_Statemachine
from python_code import statemachine_Transition

def test_statemachine_Event___init__():
    assert statemachine_Event.__init__(statemachine_Event('', statemachine_Event15=statemachine_Transition(), statemachine_Event=statemachine_Statemachine(), statemachine_Event3=statemachine_Statemachine()), '', statemachine_Event15=statemachine_Transition(), statemachine_Event=statemachine_Statemachine(), statemachine_Event3=statemachine_Statemachine()) == None


from python_code import statemachine_NamedElement

def test_statemachine_NamedElement___init__():
    assert statemachine_NamedElement.__init__(statemachine_NamedElement('', '\x00'), '\x00\x00', '') == None

