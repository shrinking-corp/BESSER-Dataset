from python_code import farrusco_AlterarEstado

def test_farrusco_AlterarEstado___init__():
    assert farrusco_AlterarEstado.__init__(farrusco_AlterarEstado('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import farrusco_Bumpers

def test_farrusco_Bumpers___init__():
    assert farrusco_Bumpers.__init__(farrusco_Bumpers('', '\x00'), '\x00\x00', '') == None


from python_code import farrusco_Distancia

def test_farrusco_Distancia___init__():
    assert farrusco_Distancia.__init__(farrusco_Distancia(0, '', '\x00\x00'), 0, '', '') == None


from python_code import farrusco_Espera

def test_farrusco_Espera___init__():
    assert farrusco_Espera.__init__(farrusco_Espera('', 0), '', 0) == None


from python_code import farrusco_LED

def test_farrusco_LED___init__():
    assert farrusco_LED.__init__(farrusco_LED('', '\x00'), '\x00\x00', '') == None


from python_code import farrusco_Motor

def test_farrusco_Motor___init__():
    assert farrusco_Motor.__init__(farrusco_Motor('', 0, 0), '\x00', 0, 0) == None


from python_code import farrusco_Paralelo

def test_farrusco_Paralelo___init__():
    assert farrusco_Paralelo.__init__(farrusco_Paralelo(''), '') == None


from python_code import farrusco_Prioridade

def test_farrusco_Prioridade___init__():
    assert farrusco_Prioridade.__init__(farrusco_Prioridade(''), '') == None


from python_code import farrusco_Robot

def test_farrusco_Robot___init__():
    assert farrusco_Robot.__init__(farrusco_Robot('', farrusco_Robot=set(), farrusco_Robot2=set(), farrusco_Robot4=set()), '', farrusco_Robot=set(), farrusco_Robot2=set(), farrusco_Robot4=set()) == None


from python_code import farrusco_Sequencial

def test_farrusco_Sequencial___init__():
    assert farrusco_Sequencial.__init__(farrusco_Sequencial(''), '') == None


from python_code import farrusco_Servo

def test_farrusco_Servo___init__():
    assert farrusco_Servo.__init__(farrusco_Servo('\x00\x00', 0, 0, 0), '', 0, 0, 0) == None

