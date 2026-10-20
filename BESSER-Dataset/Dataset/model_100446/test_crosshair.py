from python_code import states_Module

def test_states_Module___init__():
    assert states_Module.__init__(states_Module('', states_Module=set()), '', states_Module=set()) == None


from python_code import states_SimpleState

def test_states_SimpleState___init__():
    assert states_SimpleState.__init__(states_SimpleState(0), 0) == None

