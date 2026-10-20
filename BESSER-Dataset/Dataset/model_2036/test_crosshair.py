from python_code import eMFProject_Event
from python_code import eMFProject_Statemachine
from python_code import eMFProject_Transition

def test_eMFProject_Event___init__():
    assert eMFProject_Event.__init__(eMFProject_Event('', '\x00', eMFProject_Event15=eMFProject_Transition(), eMFProject_Event=eMFProject_Statemachine(), eMFProject_Event3=eMFProject_Statemachine()), '\x00\x00', '', eMFProject_Event15=eMFProject_Transition(), eMFProject_Event=eMFProject_Statemachine(), eMFProject_Event3=eMFProject_Statemachine()) == None


from python_code import eMFProject_State
from python_code import eMFProject_Statemachine
from python_code import eMFProject_Transition

def test_eMFProject_State___init__():
    assert eMFProject_State.__init__(eMFProject_State('', eMFProject_State9=set(), eMFProject_State12=set(), eMFProject_State18=eMFProject_Transition(), eMFProject_State=eMFProject_Statemachine()), '', eMFProject_State9=set(), eMFProject_State12=set(), eMFProject_State18=eMFProject_Transition(), eMFProject_State=eMFProject_Statemachine()) == None

