from python_code import tfsm_plaink3_EvaluateGuard

def test_tfsm_plaink3_EvaluateGuard___init__():
    assert tfsm_plaink3_EvaluateGuard.__init__(tfsm_plaink3_EvaluateGuard(''), '') == None


from python_code import tfsm_plaink3_NamedElement

def test_tfsm_plaink3_NamedElement___init__():
    assert tfsm_plaink3_NamedElement.__init__(tfsm_plaink3_NamedElement(''), '') == None


from python_code import tfsm_plaink3_FSMClock
from python_code import tfsm_plaink3_TemporalGuard

def test_tfsm_plaink3_TemporalGuard___init__():
    assert tfsm_plaink3_TemporalGuard.__init__(tfsm_plaink3_TemporalGuard(0, tfsm_plaink3_TemporalGuard=tfsm_plaink3_FSMClock()), 0, tfsm_plaink3_TemporalGuard=tfsm_plaink3_FSMClock()) == None


from python_code import tfsm_plaink3_FSMEvent
from python_code import tfsm_plaink3_Guard
from python_code import tfsm_plaink3_State
from python_code import tfsm_plaink3_TFSM
from python_code import tfsm_plaink3_Transition

def test_tfsm_plaink3_Transition___init__():
    assert tfsm_plaink3_Transition.__init__(tfsm_plaink3_Transition('', tfsm_plaink3_Transition27=tfsm_plaink3_FSMEvent(), incomingTransitions=tfsm_plaink3_State(), tfsm_plaink3_Transition17=tfsm_plaink3_Guard(), tfsm_plaink3_Transition19=set(), tfsm_plaink3_Transition=tfsm_plaink3_TFSM(), Transition=tfsm_plaink3_State(), Transition11=tfsm_plaink3_State(), outgoingTransitions=tfsm_plaink3_State()), '', tfsm_plaink3_Transition27=tfsm_plaink3_FSMEvent(), incomingTransitions=tfsm_plaink3_State(), tfsm_plaink3_Transition17=tfsm_plaink3_Guard(), tfsm_plaink3_Transition19=set(), tfsm_plaink3_Transition=tfsm_plaink3_TFSM(), Transition=tfsm_plaink3_State(), Transition11=tfsm_plaink3_State(), outgoingTransitions=tfsm_plaink3_State()) == None

