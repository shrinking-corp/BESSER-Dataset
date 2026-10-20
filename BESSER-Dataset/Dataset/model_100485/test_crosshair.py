from python_code import model_INamedElement

def test_model_INamedElement___init__():
    assert model_INamedElement.__init__(model_INamedElement(''), '') == None


from python_code import model_state_State

def test_model_state_State___init__():
    assert model_state_State.__init__(model_state_State(False, model_state_State=set()), False, model_state_State=set()) == None

