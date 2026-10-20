from python_code import arduino_BinaryBooleanExpression

def test_arduino_BinaryBooleanExpression___init__():
    assert arduino_BinaryBooleanExpression.__init__(arduino_BinaryBooleanExpression(''), '') == None


from python_code import arduino_BinaryIntegerExpression

def test_arduino_BinaryIntegerExpression___init__():
    assert arduino_BinaryIntegerExpression.__init__(arduino_BinaryIntegerExpression(''), '') == None


from python_code import arduino_BooleanConstant

def test_arduino_BooleanConstant___init__():
    assert arduino_BooleanConstant.__init__(arduino_BooleanConstant(True), False) == None


from python_code import arduino_BooleanVariable
from python_code import arduino_BooleanVariableRef

def test_arduino_BooleanVariable___init__():
    assert arduino_BooleanVariable.__init__(arduino_BooleanVariable(True, arduino_BooleanVariable=arduino_BooleanVariableRef()), False, arduino_BooleanVariable=arduino_BooleanVariableRef()) == None


from python_code import arduino_Delay

def test_arduino_Delay___init__():
    assert arduino_Delay.__init__(arduino_Delay('', 0), '', 0) == None


from python_code import arduino_IntegerConstant

def test_arduino_IntegerConstant___init__():
    assert arduino_IntegerConstant.__init__(arduino_IntegerConstant(0), 0) == None


from python_code import arduino_IntegerVariable
from python_code import arduino_IntegerVariableRef

def test_arduino_IntegerVariable___init__():
    assert arduino_IntegerVariable.__init__(arduino_IntegerVariable(0, arduino_IntegerVariable=arduino_IntegerVariableRef()), 0, arduino_IntegerVariable=arduino_IntegerVariableRef()) == None


from python_code import arduino_LED

def test_arduino_LED___init__():
    assert arduino_LED.__init__(arduino_LED(''), '') == None


from python_code import arduino_NamedElement

def test_arduino_NamedElement___init__():
    assert arduino_NamedElement.__init__(arduino_NamedElement(''), '') == None


from python_code import arduino_Repeat

def test_arduino_Repeat___init__():
    assert arduino_Repeat.__init__(arduino_Repeat(0), 0) == None


from python_code import arduino_UnaryBooleanExpression

def test_arduino_UnaryBooleanExpression___init__():
    assert arduino_UnaryBooleanExpression.__init__(arduino_UnaryBooleanExpression(''), '') == None


from python_code import arduino_UnaryIntegerExpression

def test_arduino_UnaryIntegerExpression___init__():
    assert arduino_UnaryIntegerExpression.__init__(arduino_UnaryIntegerExpression(''), '') == None


from python_code import arduino_Pin
from python_code import arduino_WaitFor

def test_arduino_WaitFor___init__():
    assert arduino_WaitFor.__init__(arduino_WaitFor('', arduino_WaitFor=arduino_Pin()), '', arduino_WaitFor=arduino_Pin()) == None

