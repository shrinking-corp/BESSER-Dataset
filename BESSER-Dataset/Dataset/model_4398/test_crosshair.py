from python_code import raspirover_Angle

def test_raspirover_Angle___init__():
    assert raspirover_Angle.__init__(raspirover_Angle()) == None

def test_raspirover_Angle_toRad():
    assert raspirover_Angle.toRad(raspirover_Angle()) == None

def test_raspirover_Angle_print():
    assert raspirover_Angle.print(raspirover_Angle()) == None


from python_code import raspirover_AngleUnit

def test_raspirover_AngleUnit___init__():
    assert raspirover_AngleUnit.__init__(raspirover_AngleUnit()) == None

def test_raspirover_AngleUnit_toRad():
    assert raspirover_AngleUnit.toRad(raspirover_AngleUnit(), '') == None


from python_code import raspirover_BackwardAction

def test_raspirover_BackwardAction___init__():
    assert raspirover_BackwardAction.__init__(raspirover_BackwardAction()) == None

def test_raspirover_BackwardAction_eval():
    assert raspirover_BackwardAction.eval(raspirover_BackwardAction()) == None


from python_code import raspirover_Block
from python_code import raspirover_Sketch

def test_raspirover_Block___init__():
    assert raspirover_Block.__init__(raspirover_Block(raspirover_Block=raspirover_Sketch(), raspirover_Block14=set()), raspirover_Block=raspirover_Sketch(), raspirover_Block14=set()) == None

def test_raspirover_Block_execute():
    assert raspirover_Block.execute(raspirover_Block(raspirover_Block=raspirover_Sketch(), raspirover_Block14=set())) == None


from python_code import raspirover_Centimeter

def test_raspirover_Centimeter___init__():
    assert raspirover_Centimeter.__init__(raspirover_Centimeter()) == None

def test_raspirover_Centimeter_getSymbol():
    assert raspirover_Centimeter.getSymbol(raspirover_Centimeter()) == None

def test_raspirover_Centimeter_toCm():
    assert raspirover_Centimeter.toCm(raspirover_Centimeter(), '') == None


from python_code import raspirover_Degree

def test_raspirover_Degree___init__():
    assert raspirover_Degree.__init__(raspirover_Degree()) == None

def test_raspirover_Degree_toRad():
    assert raspirover_Degree.toRad(raspirover_Degree(), '') == None

def test_raspirover_Degree_getSymbol():
    assert raspirover_Degree.getSymbol(raspirover_Degree()) == None


from python_code import raspirover_Foot

def test_raspirover_Foot___init__():
    assert raspirover_Foot.__init__(raspirover_Foot()) == None

def test_raspirover_Foot_toCm():
    assert raspirover_Foot.toCm(raspirover_Foot(), '') == None

def test_raspirover_Foot_getSymbol():
    assert raspirover_Foot.getSymbol(raspirover_Foot()) == None


from python_code import raspirover_ForwardAction

def test_raspirover_ForwardAction___init__():
    assert raspirover_ForwardAction.__init__(raspirover_ForwardAction()) == None

def test_raspirover_ForwardAction_eval():
    assert raspirover_ForwardAction.eval(raspirover_ForwardAction()) == None


from python_code import raspirover_Gradian

def test_raspirover_Gradian___init__():
    assert raspirover_Gradian.__init__(raspirover_Gradian()) == None

def test_raspirover_Gradian_getSymbol():
    assert raspirover_Gradian.getSymbol(raspirover_Gradian()) == None

def test_raspirover_Gradian_toRad():
    assert raspirover_Gradian.toRad(raspirover_Gradian(), '') == None


from python_code import raspirover_HumidityQuery

def test_raspirover_HumidityQuery___init__():
    assert raspirover_HumidityQuery.__init__(raspirover_HumidityQuery()) == None

def test_raspirover_HumidityQuery_getIntValue():
    assert raspirover_HumidityQuery.getIntValue(raspirover_HumidityQuery()) == None


from python_code import raspirover_Inch

def test_raspirover_Inch___init__():
    assert raspirover_Inch.__init__(raspirover_Inch()) == None

def test_raspirover_Inch_toCm():
    assert raspirover_Inch.toCm(raspirover_Inch(), '') == None

def test_raspirover_Inch_getSymbol():
    assert raspirover_Inch.getSymbol(raspirover_Inch()) == None


from python_code import raspirover_Length

def test_raspirover_Length___init__():
    assert raspirover_Length.__init__(raspirover_Length()) == None

def test_raspirover_Length_toCm():
    assert raspirover_Length.toCm(raspirover_Length()) == None

def test_raspirover_Length_print():
    assert raspirover_Length.print(raspirover_Length()) == None


from python_code import raspirover_LengthUnit

def test_raspirover_LengthUnit___init__():
    assert raspirover_LengthUnit.__init__(raspirover_LengthUnit()) == None

def test_raspirover_LengthUnit_toCm():
    assert raspirover_LengthUnit.toCm(raspirover_LengthUnit(), '') == None


from python_code import raspirover_LogAction

def test_raspirover_LogAction___init__():
    assert raspirover_LogAction.__init__(raspirover_LogAction(''), '') == None

def test_raspirover_LogAction_eval():
    assert raspirover_LogAction.eval(raspirover_LogAction('')) == None


from python_code import raspirover_MessageQuery

def test_raspirover_MessageQuery___init__():
    assert raspirover_MessageQuery.__init__(raspirover_MessageQuery()) == None

def test_raspirover_MessageQuery_getStringValue():
    assert raspirover_MessageQuery.getStringValue(raspirover_MessageQuery()) == None


from python_code import raspirover_Meter

def test_raspirover_Meter___init__():
    assert raspirover_Meter.__init__(raspirover_Meter()) == None

def test_raspirover_Meter_toCm():
    assert raspirover_Meter.toCm(raspirover_Meter(), '') == None

def test_raspirover_Meter_getSymbol():
    assert raspirover_Meter.getSymbol(raspirover_Meter()) == None


from python_code import raspirover_Millimeter

def test_raspirover_Millimeter___init__():
    assert raspirover_Millimeter.__init__(raspirover_Millimeter()) == None

def test_raspirover_Millimeter_toCm():
    assert raspirover_Millimeter.toCm(raspirover_Millimeter(), '') == None

def test_raspirover_Millimeter_getSymbol():
    assert raspirover_Millimeter.getSymbol(raspirover_Millimeter()) == None


from python_code import raspirover_NamedElement

def test_raspirover_NamedElement___init__():
    assert raspirover_NamedElement.__init__(raspirover_NamedElement(''), '') == None


from python_code import raspirover_ObstacleQuery

def test_raspirover_ObstacleQuery___init__():
    assert raspirover_ObstacleQuery.__init__(raspirover_ObstacleQuery(True), False) == None

def test_raspirover_ObstacleQuery_getBooleanValue():
    assert raspirover_ObstacleQuery.getBooleanValue(raspirover_ObstacleQuery(False)) == None


from python_code import raspirover_Action
from python_code import raspirover_Pin

def test_raspirover_Pin___init__():
    assert raspirover_Pin.__init__(raspirover_Pin(0, raspirover_Pin=raspirover_Action()), 0, raspirover_Pin=raspirover_Action()) == None


from python_code import raspirover_Radian

def test_raspirover_Radian___init__():
    assert raspirover_Radian.__init__(raspirover_Radian()) == None

def test_raspirover_Radian_toRad():
    assert raspirover_Radian.toRad(raspirover_Radian(), '') == None

def test_raspirover_Radian_getSymbol():
    assert raspirover_Radian.getSymbol(raspirover_Radian()) == None


from python_code import raspirover_SendAction

def test_raspirover_SendAction___init__():
    assert raspirover_SendAction.__init__(raspirover_SendAction(''), '') == None

def test_raspirover_SendAction_eval():
    assert raspirover_SendAction.eval(raspirover_SendAction('')) == None


from python_code import raspirover_StopAction

def test_raspirover_StopAction___init__():
    assert raspirover_StopAction.__init__(raspirover_StopAction()) == None

def test_raspirover_StopAction_eval():
    assert raspirover_StopAction.eval(raspirover_StopAction()) == None


from python_code import raspirover_TemperatureQuery

def test_raspirover_TemperatureQuery___init__():
    assert raspirover_TemperatureQuery.__init__(raspirover_TemperatureQuery()) == None

def test_raspirover_TemperatureQuery_getIntValue():
    assert raspirover_TemperatureQuery.getIntValue(raspirover_TemperatureQuery()) == None


from python_code import raspirover_Turn

def test_raspirover_Turn___init__():
    assert raspirover_Turn.__init__(raspirover_Turn()) == None

def test_raspirover_Turn_getSymbol():
    assert raspirover_Turn.getSymbol(raspirover_Turn()) == None

def test_raspirover_Turn_toRad():
    assert raspirover_Turn.toRad(raspirover_Turn(), '') == None


from python_code import raspirover_TurnAction

def test_raspirover_TurnAction___init__():
    assert raspirover_TurnAction.__init__(raspirover_TurnAction()) == None

def test_raspirover_TurnAction_eval():
    assert raspirover_TurnAction.eval(raspirover_TurnAction()) == None


from python_code import raspirover_RoverValue
from python_code import raspirover_VarAssignment

def test_raspirover_VarAssignment___init__():
    assert raspirover_VarAssignment.__init__(raspirover_VarAssignment(True, raspirover_VarAssignment=raspirover_RoverValue()), False, raspirover_VarAssignment=raspirover_RoverValue()) == None

def test_raspirover_VarAssignment_eval():
    assert raspirover_VarAssignment.eval(raspirover_VarAssignment(False, raspirover_VarAssignment=raspirover_RoverValue())) == None


from python_code import raspirover_VarRef

def test_raspirover_VarRef___init__():
    assert raspirover_VarRef.__init__(raspirover_VarRef(0.0), 0.0) == None

def test_raspirover_VarRef_eval():
    assert raspirover_VarRef.eval(raspirover_VarRef(0.0)) == None

def test_raspirover_VarRef_getIntValue():
    assert raspirover_VarRef.getIntValue(raspirover_VarRef(0.0)) == None

def test_raspirover_VarRef_getStringValue():
    assert raspirover_VarRef.getStringValue(raspirover_VarRef(0.0)) == None

def test_raspirover_VarRef_getBooleanValue():
    assert raspirover_VarRef.getBooleanValue(raspirover_VarRef(0.0)) == None


from python_code import raspirover_Yard

def test_raspirover_Yard___init__():
    assert raspirover_Yard.__init__(raspirover_Yard()) == None

def test_raspirover_Yard_getSymbol():
    assert raspirover_Yard.getSymbol(raspirover_Yard()) == None

def test_raspirover_Yard_toCm():
    assert raspirover_Yard.toCm(raspirover_Yard(), '') == None

