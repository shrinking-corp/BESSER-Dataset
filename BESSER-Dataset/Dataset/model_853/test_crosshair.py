from python_code import fsm_NamedElement

def test_fsm_NamedElement___init__():
    assert fsm_NamedElement.__init__(fsm_NamedElement(''), '') == None


from python_code import fsm_TimedTransition

def test_fsm_TimedTransition___init__():
    assert fsm_TimedTransition.__init__(fsm_TimedTransition(0), 0) == None

