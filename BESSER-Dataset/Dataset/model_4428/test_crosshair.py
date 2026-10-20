from python_code import farrusco_Action

def test_farrusco_Action___init__():
    assert farrusco_Action.__init__(farrusco_Action(''), '') == None


from python_code import farrusco_AlterarEstado

def test_farrusco_AlterarEstado___init__():
    assert farrusco_AlterarEstado.__init__(farrusco_AlterarEstado(0, 0, 0), 0, 0, 0) == None


from python_code import farrusco_Behavior
from python_code import farrusco_Filho

def test_farrusco_Behavior___init__():
    assert farrusco_Behavior.__init__(farrusco_Behavior('', farrusco_Behavior=farrusco_Filho()), '', farrusco_Behavior=farrusco_Filho()) == None


from python_code import farrusco_Distancia

def test_farrusco_Distancia___init__():
    assert farrusco_Distancia.__init__(farrusco_Distancia(False, 0), False, 0) == None


from python_code import farrusco_Espera

def test_farrusco_Espera___init__():
    assert farrusco_Espera.__init__(farrusco_Espera(0), 0) == None


from python_code import farrusco_LED

def test_farrusco_LED___init__():
    assert farrusco_LED.__init__(farrusco_LED(True), False) == None


from python_code import farrusco_Motor

def test_farrusco_Motor___init__():
    assert farrusco_Motor.__init__(farrusco_Motor(0, 0), 0, 0) == None


from python_code import farrusco_Robot

def test_farrusco_Robot___init__():
    assert farrusco_Robot.__init__(farrusco_Robot('', farrusco_Robot=set(), farrusco_Robot2=set(), farrusco_Robot4=set()), '', farrusco_Robot=set(), farrusco_Robot2=set(), farrusco_Robot4=set()) == None


from python_code import farrusco_Servo

def test_farrusco_Servo___init__():
    assert farrusco_Servo.__init__(farrusco_Servo(0, 0, 0), 0, 0, 0) == None

