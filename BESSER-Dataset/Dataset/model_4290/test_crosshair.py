from python_code import model_ExtraBall

def test_model_ExtraBall___init__():
    assert model_ExtraBall.__init__(model_ExtraBall('', '\x00'), '\x00\x00', '') == None


import datetime as _ch_datetime
from python_code import model_Game

def test_model_Game___init__():
    assert model_Game.__init__(model_Game('', _ch_datetime.date(1, 1, 1), model_Game=set(), model_Game2=set()), '', _ch_datetime.date(1, 1, 1), model_Game=set(), model_Game2=set()) == None

