from python_code import ardlers_NumberLiteral

def test_ardlers_NumberLiteral___init__():
    assert ardlers_NumberLiteral.__init__(ardlers_NumberLiteral('', 0), '', 0) == None


from python_code import ardlers_Map
from python_code import ardlers_Range

def test_ardlers_Range___init__():
    assert ardlers_Range.__init__(ardlers_Range(0.0, 0.0, ardlers_Range=ardlers_Map(), ardlers_Range52=ardlers_Map()), 0.0, 0.0, ardlers_Range=ardlers_Map(), ardlers_Range52=ardlers_Map()) == None


from python_code import ardlers_Smoothing

def test_ardlers_Smoothing___init__():
    assert ardlers_Smoothing.__init__(ardlers_Smoothing(0.0), 0.0) == None


from python_code import ardlers_State

def test_ardlers_State___init__():
    assert ardlers_State.__init__(ardlers_State(''), '') == None

