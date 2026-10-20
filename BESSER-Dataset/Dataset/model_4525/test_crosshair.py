from python_code import model_ContinuosAction

def test_model_ContinuosAction___init__():
    assert model_ContinuosAction.__init__(model_ContinuosAction(0.0), 0.0) == None


from python_code import model_Move

def test_model_Move___init__():
    assert model_Move.__init__(model_Move(''), '') == None


from python_code import model_RandomAction

def test_model_RandomAction___init__():
    assert model_RandomAction.__init__(model_RandomAction(True), False) == None


from python_code import model_Turn

def test_model_Turn___init__():
    assert model_Turn.__init__(model_Turn(0.0, '\x00\x00'), 0.0, '') == None

