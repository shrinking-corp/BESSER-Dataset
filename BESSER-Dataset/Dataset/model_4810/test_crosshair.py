from python_code import model_Param

def test_model_Param___init__():
    assert model_Param.__init__(model_Param('', '\x00'), '\x00\x00', '') == None

