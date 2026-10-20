from python_code import model_Container
from python_code import model_Content

def test_model_Content___init__():
    assert model_Content.__init__(model_Content('', '\x00', model_Content=model_Container()), '\x00\x00', '', model_Content=model_Container()) == None


from python_code import model_TableContentWithValidation

def test_model_TableContentWithValidation___init__():
    assert model_TableContentWithValidation.__init__(model_TableContentWithValidation('', 0), '', 0) == None


from python_code import model_TableContentWithoutValidation

def test_model_TableContentWithoutValidation___init__():
    assert model_TableContentWithoutValidation.__init__(model_TableContentWithoutValidation('', 0), '', 0) == None

