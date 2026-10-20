from python_code import farmbot_modeling_BooleanExpression
from python_code import farmbot_modeling_If

def test_farmbot_modeling_BooleanExpression___init__():
    assert farmbot_modeling_BooleanExpression.__init__(farmbot_modeling_BooleanExpression(0, '', 0, farmbot_modeling_BooleanExpression=farmbot_modeling_If()), 0, '', 0, farmbot_modeling_BooleanExpression=farmbot_modeling_If()) == None


from python_code import farmbot_modeling_ExecuteSequence
from python_code import farmbot_modeling_If

def test_farmbot_modeling_ExecuteSequence___init__():
    assert farmbot_modeling_ExecuteSequence.__init__(farmbot_modeling_ExecuteSequence(0, farmbot_modeling_ExecuteSequence=farmbot_modeling_If(), farmbot_modeling_ExecuteSequence7=farmbot_modeling_If()), 0, farmbot_modeling_ExecuteSequence=farmbot_modeling_If(), farmbot_modeling_ExecuteSequence7=farmbot_modeling_If()) == None


from python_code import farmbot_modeling_FindHome

def test_farmbot_modeling_FindHome___init__():
    assert farmbot_modeling_FindHome.__init__(farmbot_modeling_FindHome(''), '') == None


from python_code import farmbot_modeling_Move

def test_farmbot_modeling_Move___init__():
    assert farmbot_modeling_Move.__init__(farmbot_modeling_Move(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import farmbot_modeling_RunFarmware

def test_farmbot_modeling_RunFarmware___init__():
    assert farmbot_modeling_RunFarmware.__init__(farmbot_modeling_RunFarmware(''), '') == None


from python_code import farmbot_modeling_Schedule

def test_farmbot_modeling_Schedule___init__():
    assert farmbot_modeling_Schedule.__init__(farmbot_modeling_Schedule(0, '', '', False, '', '', ''), 0, '\x00', '', False, '', '', '') == None


from python_code import farmbot_modeling_SendMessage

def test_farmbot_modeling_SendMessage___init__():
    assert farmbot_modeling_SendMessage.__init__(farmbot_modeling_SendMessage('', '\x00'), '\x00\x00', '') == None


from python_code import farmbot_modeling_Sequence

def test_farmbot_modeling_Sequence___init__():
    assert farmbot_modeling_Sequence.__init__(farmbot_modeling_Sequence('', farmbot_modeling_Sequence=set()), '', farmbot_modeling_Sequence=set()) == None


from python_code import farmbot_modeling_TurnOff

def test_farmbot_modeling_TurnOff___init__():
    assert farmbot_modeling_TurnOff.__init__(farmbot_modeling_TurnOff(0), 0) == None


from python_code import farmbot_modeling_TurnOnAnalog

def test_farmbot_modeling_TurnOnAnalog___init__():
    assert farmbot_modeling_TurnOnAnalog.__init__(farmbot_modeling_TurnOnAnalog(0, 0), 0, 0) == None


from python_code import farmbot_modeling_TurnOnDigital

def test_farmbot_modeling_TurnOnDigital___init__():
    assert farmbot_modeling_TurnOnDigital.__init__(farmbot_modeling_TurnOnDigital(0), 0) == None


from python_code import farmbot_modeling_Wait

def test_farmbot_modeling_Wait___init__():
    assert farmbot_modeling_Wait.__init__(farmbot_modeling_Wait(0.0), 0.0) == None

