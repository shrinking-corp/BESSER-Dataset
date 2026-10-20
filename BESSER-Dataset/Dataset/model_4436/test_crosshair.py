from python_code import dsl_ColorSensor

def test_dsl_ColorSensor___init__():
    assert dsl_ColorSensor.__init__(dsl_ColorSensor(''), '') == None


from python_code import dsl_Ignorables

def test_dsl_Ignorables___init__():
    assert dsl_Ignorables.__init__(dsl_Ignorables(''), '') == None


from python_code import dsl_Mission
from python_code import dsl_SensorType
from python_code import dsl_Task

def test_dsl_Task___init__():
    assert dsl_Task.__init__(dsl_Task('', False, '\x00\x00', dsl_Task=dsl_Mission(), dsl_Task2=dsl_SensorType()), '', False, '', dsl_Task=dsl_Mission(), dsl_Task2=dsl_SensorType()) == None


from python_code import dsl_TouchSensor

def test_dsl_TouchSensor___init__():
    assert dsl_TouchSensor.__init__(dsl_TouchSensor(''), '') == None


from python_code import dsl_UltrasonicSensor

def test_dsl_UltrasonicSensor___init__():
    assert dsl_UltrasonicSensor.__init__(dsl_UltrasonicSensor('', '\x00'), '\x00\x00', '') == None

