from python_code import tsm_NamedElement

def test_tsm_NamedElement___init__():
    assert tsm_NamedElement.__init__(tsm_NamedElement(''), '') == None


from python_code import tsm_TimeEvent
from python_code import tsm_Transition

def test_tsm_TimeEvent___init__():
    assert tsm_TimeEvent.__init__(tsm_TimeEvent(0, tsm_TimeEvent=tsm_Transition()), 0, tsm_TimeEvent=tsm_Transition()) == None

