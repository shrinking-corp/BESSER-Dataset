from python_code import rcl_BackwardAction

def test_rcl_BackwardAction___init__():
    assert rcl_BackwardAction.__init__(rcl_BackwardAction()) == None

def test_rcl_BackwardAction_eval():
    assert rcl_BackwardAction.eval(rcl_BackwardAction()) == None


from python_code import rcl_ForwardAction

def test_rcl_ForwardAction___init__():
    assert rcl_ForwardAction.__init__(rcl_ForwardAction()) == None

def test_rcl_ForwardAction_eval():
    assert rcl_ForwardAction.eval(rcl_ForwardAction()) == None


from python_code import rcl_HumidityQuery

def test_rcl_HumidityQuery___init__():
    assert rcl_HumidityQuery.__init__(rcl_HumidityQuery()) == None

def test_rcl_HumidityQuery_getIntValue():
    assert rcl_HumidityQuery.getIntValue(rcl_HumidityQuery()) == None


from python_code import rcl_LogAction

def test_rcl_LogAction___init__():
    assert rcl_LogAction.__init__(rcl_LogAction(''), '') == None

def test_rcl_LogAction_eval():
    assert rcl_LogAction.eval(rcl_LogAction('')) == None


from python_code import rcl_MessageQuery

def test_rcl_MessageQuery___init__():
    assert rcl_MessageQuery.__init__(rcl_MessageQuery()) == None

def test_rcl_MessageQuery_getStringValue():
    assert rcl_MessageQuery.getStringValue(rcl_MessageQuery()) == None


from python_code import rcl_ObstacleQuery

def test_rcl_ObstacleQuery___init__():
    assert rcl_ObstacleQuery.__init__(rcl_ObstacleQuery(True), False) == None

def test_rcl_ObstacleQuery_getBooleanValue():
    assert rcl_ObstacleQuery.getBooleanValue(rcl_ObstacleQuery(False)) == None


from python_code import rcl_SendAction

def test_rcl_SendAction___init__():
    assert rcl_SendAction.__init__(rcl_SendAction(''), '') == None

def test_rcl_SendAction_eval():
    assert rcl_SendAction.eval(rcl_SendAction('')) == None


from python_code import rcl_StopAction

def test_rcl_StopAction___init__():
    assert rcl_StopAction.__init__(rcl_StopAction()) == None

def test_rcl_StopAction_eval():
    assert rcl_StopAction.eval(rcl_StopAction()) == None


from python_code import rcl_TemperatureQuery

def test_rcl_TemperatureQuery___init__():
    assert rcl_TemperatureQuery.__init__(rcl_TemperatureQuery()) == None

def test_rcl_TemperatureQuery_getIntValue():
    assert rcl_TemperatureQuery.getIntValue(rcl_TemperatureQuery()) == None


from python_code import rcl_TurnAction

def test_rcl_TurnAction___init__():
    assert rcl_TurnAction.__init__(rcl_TurnAction()) == None

def test_rcl_TurnAction_eval():
    assert rcl_TurnAction.eval(rcl_TurnAction()) == None


from python_code import rcl_RoverValue
from python_code import rcl_VarAssignment

def test_rcl_VarAssignment___init__():
    assert rcl_VarAssignment.__init__(rcl_VarAssignment(True, rcl_VarAssignment=rcl_RoverValue()), False, rcl_VarAssignment=rcl_RoverValue()) == None

def test_rcl_VarAssignment_eval():
    assert rcl_VarAssignment.eval(rcl_VarAssignment(False, rcl_VarAssignment=rcl_RoverValue())) == None


from python_code import rcl_VarRef

def test_rcl_VarRef___init__():
    assert rcl_VarRef.__init__(rcl_VarRef(''), '') == None

def test_rcl_VarRef_eval():
    assert rcl_VarRef.eval(rcl_VarRef('')) == None

def test_rcl_VarRef_getBooleanValue():
    assert rcl_VarRef.getBooleanValue(rcl_VarRef('')) == None

def test_rcl_VarRef_getIntValue():
    assert rcl_VarRef.getIntValue(rcl_VarRef('')) == None

def test_rcl_VarRef_getStringValue():
    assert rcl_VarRef.getStringValue(rcl_VarRef('')) == None

