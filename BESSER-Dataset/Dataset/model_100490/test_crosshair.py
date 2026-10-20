from python_code import UMLRealTimeStateMach_Pseudostate
from python_code import UMLRealTimeStateMach_RTPseudostate

def test_UMLRealTimeStateMach_RTPseudostate___init__():
    assert UMLRealTimeStateMach_RTPseudostate.__init__(UMLRealTimeStateMach_RTPseudostate(UMLRealTimeStateMach_RTPseudostate=UMLRealTimeStateMach_Pseudostate()), UMLRealTimeStateMach_RTPseudostate=UMLRealTimeStateMach_Pseudostate()) == None

def test_UMLRealTimeStateMach_RTPseudostate_RTstatemachinesdonotsupportconcurrencyorshallowhistory():
    assert UMLRealTimeStateMach_RTPseudostate.RTstatemachinesdonotsupportconcurrencyorshallowhistory(UMLRealTimeStateMach_RTPseudostate(UMLRealTimeStateMach_RTPseudostate=UMLRealTimeStateMach_Pseudostate()), '', '') == None


from python_code import UMLRealTimeStateMach_RTRegion
from python_code import UMLRealTimeStateMach_Region

def test_UMLRealTimeStateMach_RTRegion___init__():
    assert UMLRealTimeStateMach_RTRegion.__init__(UMLRealTimeStateMach_RTRegion(UMLRealTimeStateMach_RTRegion=UMLRealTimeStateMach_Region()), UMLRealTimeStateMach_RTRegion=UMLRealTimeStateMach_Region()) == None

def test_UMLRealTimeStateMach_RTRegion_RegionsinRTstatemachinescannothaveafinalstate():
    assert UMLRealTimeStateMach_RTRegion.RegionsinRTstatemachinescannothaveafinalstate(UMLRealTimeStateMach_RTRegion(UMLRealTimeStateMach_RTRegion=UMLRealTimeStateMach_Region()), '', '') == None


from python_code import UMLRealTimeStateMach_RTState
from python_code import UMLRealTimeStateMach_State

def test_UMLRealTimeStateMach_RTState___init__():
    assert UMLRealTimeStateMach_RTState.__init__(UMLRealTimeStateMach_RTState(UMLRealTimeStateMach_RTState=UMLRealTimeStateMach_State()), UMLRealTimeStateMach_RTState=UMLRealTimeStateMach_State()) == None

def test_UMLRealTimeStateMach_RTState_AcomposteRTstatehasexactlyoneregion():
    assert UMLRealTimeStateMach_RTState.AcomposteRTstatehasexactlyoneregion(UMLRealTimeStateMach_RTState(UMLRealTimeStateMach_RTState=UMLRealTimeStateMach_State()), '', '') == None

def test_UMLRealTimeStateMach_RTState_Constraint5():
    assert UMLRealTimeStateMach_RTState.Constraint5(UMLRealTimeStateMach_RTState(UMLRealTimeStateMach_RTState=UMLRealTimeStateMach_State()), '', '') == None

def test_UMLRealTimeStateMach_RTState_RTstatemachinescannothaveanydeferredtriggers():
    assert UMLRealTimeStateMach_RTState.RTstatemachinescannothaveanydeferredtriggers(UMLRealTimeStateMach_RTState(UMLRealTimeStateMach_RTState=UMLRealTimeStateMach_State()), '', '') == None

def test_UMLRealTimeStateMach_RTState_RTstatemachinesdonotsupportdoactivities():
    assert UMLRealTimeStateMach_RTState.RTstatemachinesdonotsupportdoactivities(UMLRealTimeStateMach_RTState(UMLRealTimeStateMach_RTState=UMLRealTimeStateMach_State()), '', '') == None

def test_UMLRealTimeStateMach_RTState_RTdoesnotsupportsubmachinestates():
    assert UMLRealTimeStateMach_RTState.RTdoesnotsupportsubmachinestates(UMLRealTimeStateMach_RTState(UMLRealTimeStateMach_RTState=UMLRealTimeStateMach_State()), '', '') == None


from python_code import UMLRealTimeStateMach_RTStateMachine
from python_code import UMLRealTimeStateMach_StateMachine

def test_UMLRealTimeStateMach_RTStateMachine___init__():
    assert UMLRealTimeStateMach_RTStateMachine.__init__(UMLRealTimeStateMach_RTStateMachine('', UMLRealTimeStateMach_RTStateMachine=UMLRealTimeStateMach_StateMachine()), '', UMLRealTimeStateMach_RTStateMachine=UMLRealTimeStateMach_StateMachine()) == None

def test_UMLRealTimeStateMach_RTStateMachine_RTstatemachinesdonothaveparametersorparametersets():
    assert UMLRealTimeStateMach_RTStateMachine.RTstatemachinesdonothaveparametersorparametersets(UMLRealTimeStateMach_RTStateMachine('', UMLRealTimeStateMach_RTStateMachine=UMLRealTimeStateMach_StateMachine()), 0, '\x00\x00') == None

def test_UMLRealTimeStateMach_RTStateMachine_RTstatemachinesmusthaveacontextanditmustbeaClass():
    assert UMLRealTimeStateMach_RTStateMachine.RTstatemachinesmusthaveacontextanditmustbeaClass(UMLRealTimeStateMach_RTStateMachine('', UMLRealTimeStateMach_RTStateMachine=UMLRealTimeStateMach_StateMachine()), 0, '\x00\x00') == None

def test_UMLRealTimeStateMach_RTStateMachine_AnRTstatemachineisneverreentrant():
    assert UMLRealTimeStateMach_RTStateMachine.AnRTstatemachineisneverreentrant(UMLRealTimeStateMach_RTStateMachine('', UMLRealTimeStateMach_RTStateMachine=UMLRealTimeStateMach_StateMachine()), 0, '\x00\x00') == None

def test_UMLRealTimeStateMach_RTStateMachine_Passivestatemachineareonlyallowedonpassivedataclasses():
    assert UMLRealTimeStateMach_RTStateMachine.Passivestatemachineareonlyallowedonpassivedataclasses(UMLRealTimeStateMach_RTStateMachine('', UMLRealTimeStateMach_RTStateMachine=UMLRealTimeStateMach_StateMachine()), 0, '\x00\x00') == None

def test_UMLRealTimeStateMach_RTStateMachine_AnRTstatemachinehasexactlyoneregion():
    assert UMLRealTimeStateMach_RTStateMachine.AnRTstatemachinehasexactlyoneregion(UMLRealTimeStateMach_RTStateMachine('', UMLRealTimeStateMach_RTStateMachine=UMLRealTimeStateMach_StateMachine()), 0, '\x00\x00') == None

