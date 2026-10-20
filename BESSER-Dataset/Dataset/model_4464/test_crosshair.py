from python_code import robot_Echo

def test_robot_Echo___init__():
    assert robot_Echo.__init__(robot_Echo(''), '') == None


from python_code import robot_Movement

def test_robot_Movement___init__():
    assert robot_Movement.__init__(robot_Movement(0.0), 0.0) == None


from python_code import robot_Compare
from python_code import robot_Operator

def test_robot_Operator___init__():
    assert robot_Operator.__init__(robot_Operator('', robot_Operator=robot_Compare()), '', robot_Operator=robot_Compare()) == None


from python_code import robot_Sensor

def test_robot_Sensor___init__():
    assert robot_Sensor.__init__(robot_Sensor(''), '') == None


from python_code import robot_TBoolean

def test_robot_TBoolean___init__():
    assert robot_TBoolean.__init__(robot_TBoolean(''), '') == None


from python_code import robot_TFloat

def test_robot_TFloat___init__():
    assert robot_TFloat.__init__(robot_TFloat(''), '') == None


from python_code import robot_TInteger

def test_robot_TInteger___init__():
    assert robot_TInteger.__init__(robot_TInteger(''), '') == None


from python_code import robot_TString

def test_robot_TString___init__():
    assert robot_TString.__init__(robot_TString(''), '') == None


from python_code import robot_Values
from python_code import robot_Var

def test_robot_Var___init__():
    assert robot_Var.__init__(robot_Var('', robot_Var=robot_Values()), '', robot_Var=robot_Values()) == None


from python_code import robot_Variable

def test_robot_Variable___init__():
    assert robot_Variable.__init__(robot_Variable(''), '') == None

