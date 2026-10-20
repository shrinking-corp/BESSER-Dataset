from python_code import statemachine_Pseudostate
from python_code import statemachine_Region

def test_statemachine_Pseudostate___init__():
    assert statemachine_Pseudostate.__init__(statemachine_Pseudostate('', '\x00', statemachine_Pseudostate=statemachine_Region()), '\x00\x00', '', statemachine_Pseudostate=statemachine_Region()) == None


from python_code import statemachine_ComplexState
from python_code import statemachine_Region
from python_code import statemachine_State

def test_statemachine_State___init__():
    assert statemachine_State.__init__(statemachine_State('', statemachine_State=statemachine_ComplexState(), statemachine_State16=statemachine_Region()), '', statemachine_State=statemachine_ComplexState(), statemachine_State16=statemachine_Region()) == None


from python_code import statemachine_Statemachine

def test_statemachine_Statemachine___init__():
    assert statemachine_Statemachine.__init__(statemachine_Statemachine('', statemachine_Statemachine=set(), statemachine_Statemachine13=set()), '', statemachine_Statemachine=set(), statemachine_Statemachine13=set()) == None

