from python_code import finitestatemachines_NamedElement

def test_finitestatemachines_NamedElement___init__():
    assert finitestatemachines_NamedElement.__init__(finitestatemachines_NamedElement(''), '') == None


from python_code import finitestatemachines_TimedTransition

def test_finitestatemachines_TimedTransition___init__():
    assert finitestatemachines_TimedTransition.__init__(finitestatemachines_TimedTransition(0), 0) == None

