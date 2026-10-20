import datetime as _ch_datetime
from python_code import model_ETypes

def test_model_ETypes___init__():
    assert model_ETypes.__init__(model_ETypes('', '', False, '', '', '', _ch_datetime.date(1, 1, 1), 0.0, 0.0, 0, '', '', '', ''), '', '', True, '', '', '', _ch_datetime.date(1, 1, 1), 0.0, 0.0, 0, '', '', '', '') == None

