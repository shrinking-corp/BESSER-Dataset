from python_code import dsl_TouchSensor

def test_dsl_TouchSensor___init__():
    assert dsl_TouchSensor.__init__(dsl_TouchSensor(''), '') == None


from python_code import dsl_UltrasonicSensor

def test_dsl_UltrasonicSensor___init__():
    assert dsl_UltrasonicSensor.__init__(dsl_UltrasonicSensor('', '\x00'), '\x00\x00', '') == None

