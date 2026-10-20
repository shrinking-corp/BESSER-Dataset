from python_code import tfsm_EvaluateGuard

def test_tfsm_EvaluateGuard___init__():
    assert tfsm_EvaluateGuard.__init__(tfsm_EvaluateGuard(''), '') == None


from python_code import tfsm_NamedElement

def test_tfsm_NamedElement___init__():
    assert tfsm_NamedElement.__init__(tfsm_NamedElement(''), '') == None


from python_code import tfsm_FSMEvent
from python_code import tfsm_Guard
from python_code import tfsm_State
from python_code import tfsm_TFSM
from python_code import tfsm_Transition

def test_tfsm_Transition___init__():
    assert tfsm_Transition.__init__(tfsm_Transition('', Transition11=tfsm_State(), outgoingTransitions=tfsm_State(), incomingTransitions=tfsm_State(), tfsm_Transition17=tfsm_Guard(), tfsm_Transition19=set(), tfsm_Transition=tfsm_TFSM(), Transition=tfsm_State(), tfsm_Transition27=tfsm_FSMEvent()), '', Transition11=tfsm_State(), outgoingTransitions=tfsm_State(), incomingTransitions=tfsm_State(), tfsm_Transition17=tfsm_Guard(), tfsm_Transition19=set(), tfsm_Transition=tfsm_TFSM(), Transition=tfsm_State(), tfsm_Transition27=tfsm_FSMEvent()) == None

