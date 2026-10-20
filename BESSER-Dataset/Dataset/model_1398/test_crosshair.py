from python_code import model_State

def test_model_State___init__():
    assert model_State.__init__(model_State()) == None

def test_model_State_onEnter():
    assert model_State.onEnter(model_State()) == None

def test_model_State_onExit():
    assert model_State.onExit(model_State()) == None

