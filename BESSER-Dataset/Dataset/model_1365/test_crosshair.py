from python_code import statemachine_OpaqueBehavior

def test_statemachine_OpaqueBehavior___init__():
    assert statemachine_OpaqueBehavior.__init__(statemachine_OpaqueBehavior('', '\x00'), '\x00\x00', '') == None


from python_code import statemachine_PseudoState

def test_statemachine_PseudoState___init__():
    assert statemachine_PseudoState.__init__(statemachine_PseudoState(''), '') == None

