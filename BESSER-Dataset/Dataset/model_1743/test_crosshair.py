from python_code import model_ETypes

def test_model_ETypes___init__():
    assert model_ETypes.__init__(model_ETypes('', '', False, '', '', '', datetime.date(1, 1, 1), 0.0, 0.0, 0, '', '', '', ''), '', '', True, '', '', '', datetime.date(1, 1, 1), 0.0, 0.0, 0, '', '', '', '') == None
