from python_code import sample_Type
from python_code import sample_TypeMap

def test_sample_Type___init__():
    assert sample_Type.__init__(sample_Type('', sample_Type=sample_TypeMap()), '', sample_Type=sample_TypeMap()) == None


from python_code import sample_TypeMap
from python_code import sample_Value

def test_sample_Value___init__():
    assert sample_Value.__init__(sample_Value(0, sample_Value=sample_TypeMap()), 0, sample_Value=sample_TypeMap()) == None

