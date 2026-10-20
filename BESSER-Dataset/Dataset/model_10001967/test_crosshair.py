from python_code import Dispatch_drown

def test_Dispatch_drown___init__():
    assert Dispatch_drown.__init__(Dispatch_drown('', '\x00'), '\x00\x00', '') == None


from python_code import Motion_Sensor

def test_Motion_Sensor___init__():
    assert Motion_Sensor.__init__(Motion_Sensor(''), '') == None

