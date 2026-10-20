from python_code import tfsm_NamedElement

def test_tfsm_NamedElement___init__():
    assert tfsm_NamedElement.__init__(tfsm_NamedElement(''), '') == None


from python_code import tfsm_FSMClock
from python_code import tfsm_TemporalGuard

def test_tfsm_TemporalGuard___init__():
    assert tfsm_TemporalGuard.__init__(tfsm_TemporalGuard(0, tfsm_TemporalGuard=tfsm_FSMClock()), 0, tfsm_TemporalGuard=tfsm_FSMClock()) == None

