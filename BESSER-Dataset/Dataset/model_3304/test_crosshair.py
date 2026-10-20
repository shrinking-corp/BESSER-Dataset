import datetime as _ch_datetime
from python_code import model_STEMTime

def test_model_STEMTime___init__():
    assert model_STEMTime.__init__(model_STEMTime(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None

def test_model_STEMTime_addIncrement():
    assert model_STEMTime.addIncrement(model_STEMTime(_ch_datetime.date(1, 1, 2)), 0) == None

def test_model_STEMTime_hashCode():
    assert model_STEMTime.hashCode(model_STEMTime(_ch_datetime.date(1, 1, 2))) == None

def test_model_STEMTime_equals():
    assert model_STEMTime.equals(model_STEMTime(_ch_datetime.date(1, 1, 2)), 0) == None

