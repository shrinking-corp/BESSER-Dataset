from python_code import Array
from python_code import Value

def test_Array___init__():
    assert Array.__init__(Array(Value('')), Value('')) == None


from python_code import Bool

def test_Bool___init__():
    assert Bool.__init__(Bool(True), False) == None


from python_code import Documents
from python_code import Json
from python_code import Value

def test_Documents___init__():
    assert Documents.__init__(Documents('\x00\x00', Json(Value('')), '', 0), '', Json(Value('')), '', 0) == None


from python_code import Json
from python_code import Value

def test_Json___init__():
    assert Json.__init__(Json(Value('')), Value('')) == None


from python_code import MapService

def test_MapService___init__():
    assert MapService.__init__(MapService(0.0, '', ''), 0.0, '', '') == None


from python_code import Number

def test_Number___init__():
    assert Number.__init__(Number(0), 0) == None


from python_code import Value

def test_Value___init__():
    assert Value.__init__(Value(''), '') == None

