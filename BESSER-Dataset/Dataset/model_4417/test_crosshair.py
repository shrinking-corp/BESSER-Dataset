from python_code import mindstorms_Choregraphy
from python_code import mindstorms_Reuse

def test_mindstorms_Choregraphy___init__():
    assert mindstorms_Choregraphy.__init__(mindstorms_Choregraphy('', mindstorms_Choregraphy=mindstorms_Reuse()), '', mindstorms_Choregraphy=mindstorms_Reuse()) == None


from python_code import mindstorms_ColorSensor

def test_mindstorms_ColorSensor___init__():
    assert mindstorms_ColorSensor.__init__(mindstorms_ColorSensor(''), '') == None


from python_code import mindstorms_Delay

def test_mindstorms_Delay___init__():
    assert mindstorms_Delay.__init__(mindstorms_Delay(0), 0) == None


from python_code import mindstorms_GoBackward

def test_mindstorms_GoBackward___init__():
    assert mindstorms_GoBackward.__init__(mindstorms_GoBackward(0, False), 0, False) == None


from python_code import mindstorms_GoForward

def test_mindstorms_GoForward___init__():
    assert mindstorms_GoForward.__init__(mindstorms_GoForward(0, False), 0, False) == None


from python_code import mindstorms_GoTo

def test_mindstorms_GoTo___init__():
    assert mindstorms_GoTo.__init__(mindstorms_GoTo(0, 0), 0, 0) == None


from python_code import mindstorms_Rotate

def test_mindstorms_Rotate___init__():
    assert mindstorms_Rotate.__init__(mindstorms_Rotate(0, False), 0, False) == None


from python_code import mindstorms_TouchSensor

def test_mindstorms_TouchSensor___init__():
    assert mindstorms_TouchSensor.__init__(mindstorms_TouchSensor(True), False) == None


from python_code import mindstorms_UltrasonicSensor

def test_mindstorms_UltrasonicSensor___init__():
    assert mindstorms_UltrasonicSensor.__init__(mindstorms_UltrasonicSensor('\x00', 0.0), '', 0.0) == None

