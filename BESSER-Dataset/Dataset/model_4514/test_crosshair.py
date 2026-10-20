from python_code import majordomo_BooleanSensor
from python_code import majordomo_BooleanSensorStatement

def test_majordomo_BooleanSensor___init__():
    assert majordomo_BooleanSensor.__init__(majordomo_BooleanSensor(majordomo_BooleanSensor=majordomo_BooleanSensorStatement()), majordomo_BooleanSensor=majordomo_BooleanSensorStatement()) == None

def test_majordomo_BooleanSensor_getValue():
    assert majordomo_BooleanSensor.getValue(majordomo_BooleanSensor(majordomo_BooleanSensor=majordomo_BooleanSensorStatement())) == None


from python_code import majordomo_CompareOperation
from python_code import majordomo_ValueExpression

def test_majordomo_CompareOperation___init__():
    assert majordomo_CompareOperation.__init__(majordomo_CompareOperation('', majordomo_CompareOperation=majordomo_ValueExpression(), majordomo_CompareOperation25=majordomo_ValueExpression()), '', majordomo_CompareOperation=majordomo_ValueExpression(), majordomo_CompareOperation25=majordomo_ValueExpression()) == None


from python_code import majordomo_ConstantValue

def test_majordomo_ConstantValue___init__():
    assert majordomo_ConstantValue.__init__(majordomo_ConstantValue(0.0), 0.0) == None


from python_code import majordomo_Extension

def test_majordomo_Extension___init__():
    assert majordomo_Extension.__init__(majordomo_Extension(''), '') == None


from python_code import majordomo_FloatSensor
from python_code import majordomo_SensorValue

def test_majordomo_FloatSensor___init__():
    assert majordomo_FloatSensor.__init__(majordomo_FloatSensor(majordomo_FloatSensor=majordomo_SensorValue()), majordomo_FloatSensor=majordomo_SensorValue()) == None

def test_majordomo_FloatSensor_getValue():
    assert majordomo_FloatSensor.getValue(majordomo_FloatSensor(majordomo_FloatSensor=majordomo_SensorValue())) == None


from python_code import majordomo_House
from python_code import majordomo_Majordomo
from python_code import majordomo_Program

def test_majordomo_Majordomo___init__():
    assert majordomo_Majordomo.__init__(majordomo_Majordomo('\x00', majordomo_Majordomo=majordomo_House(), majordomo_Majordomo2=set(), majordomo_Majordomo4=majordomo_Program()), '', majordomo_Majordomo=majordomo_House(), majordomo_Majordomo2=set(), majordomo_Majordomo4=majordomo_Program()) == None


from python_code import majordomo_ActionSetReference
from python_code import majordomo_PreparedActionSet
from python_code import majordomo_Program

def test_majordomo_PreparedActionSet___init__():
    assert majordomo_PreparedActionSet.__init__(majordomo_PreparedActionSet('', PreparedActionSet=majordomo_Program(), preparedActionSets=majordomo_Program(), majordomo_PreparedActionSet=set(), majordomo_PreparedActionSet48=majordomo_ActionSetReference()), '', PreparedActionSet=majordomo_Program(), preparedActionSets=majordomo_Program(), majordomo_PreparedActionSet=set(), majordomo_PreparedActionSet48=majordomo_ActionSetReference()) == None


from python_code import majordomo_PreparedStatement
from python_code import majordomo_Program
from python_code import majordomo_Statement
from python_code import majordomo_StatementReference

def test_majordomo_PreparedStatement___init__():
    assert majordomo_PreparedStatement.__init__(majordomo_PreparedStatement('', preparedStatements=majordomo_Program(), majordomo_PreparedStatement41=majordomo_Statement(), majordomo_PreparedStatement=majordomo_StatementReference(), PreparedStatement=majordomo_Program()), '', preparedStatements=majordomo_Program(), majordomo_PreparedStatement41=majordomo_Statement(), majordomo_PreparedStatement=majordomo_StatementReference(), PreparedStatement=majordomo_Program()) == None


from python_code import majordomo_PreparedValue
from python_code import majordomo_Program
from python_code import majordomo_ValueExpression
from python_code import majordomo_ValueReference

def test_majordomo_PreparedValue___init__():
    assert majordomo_PreparedValue.__init__(majordomo_PreparedValue('', PreparedValue=majordomo_Program(), constants=majordomo_Program(), majordomo_PreparedValue=majordomo_ValueExpression(), majordomo_PreparedValue54=majordomo_ValueReference()), '', PreparedValue=majordomo_Program(), constants=majordomo_Program(), majordomo_PreparedValue=majordomo_ValueExpression(), majordomo_PreparedValue54=majordomo_ValueReference()) == None

