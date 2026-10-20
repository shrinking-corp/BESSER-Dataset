from python_code import model_ConcreteTypeOne

def test_model_ConcreteTypeOne___init__():
    assert model_ConcreteTypeOne.__init__(model_ConcreteTypeOne(''), '') == None


from python_code import model_ConcreteTypeTwo

def test_model_ConcreteTypeTwo___init__():
    assert model_ConcreteTypeTwo.__init__(model_ConcreteTypeTwo(''), '') == None


import datetime as _ch_datetime
from python_code import model_ETypes

def test_model_ETypes___init__():
    assert model_ETypes.__init__(model_ETypes('', '', _ch_datetime.date(1, 1, 1), 0.0, '', '', '', '', '', False, '', 0, 0, '', float('nan'), '', ''), '', '', _ch_datetime.date(1, 1, 1), 0.0, '', '', '', '', '', True, '', 0, 0, '', 0.0, '', '') == None

