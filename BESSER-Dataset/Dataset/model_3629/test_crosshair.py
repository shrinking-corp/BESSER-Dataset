from python_code import stateChart_PseudoState

def test_stateChart_PseudoState___init__():
    assert stateChart_PseudoState.__init__(stateChart_PseudoState(''), '') == None


from python_code import stateChart_State

def test_stateChart_State___init__():
    assert stateChart_State.__init__(stateChart_State('', '', '\x00\x00'), '', '', '') == None

