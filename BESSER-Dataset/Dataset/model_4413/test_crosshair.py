from python_code import arduino_BinaryExpression
from python_code import arduino_Expression

def test_arduino_BinaryExpression___init__():
    assert arduino_BinaryExpression.__init__(arduino_BinaryExpression('', arduino_BinaryExpression=arduino_Expression(), arduino_BinaryExpression29=arduino_Expression()), '', arduino_BinaryExpression=arduino_Expression(), arduino_BinaryExpression29=arduino_Expression()) == None


from python_code import arduino_Constant
from python_code import arduino_WaitFor

def test_arduino_Constant___init__():
    assert arduino_Constant.__init__(arduino_Constant(0, arduino_Constant=arduino_WaitFor()), 0, arduino_Constant=arduino_WaitFor()) == None


from python_code import arduino_Delay

def test_arduino_Delay___init__():
    assert arduino_Delay.__init__(arduino_Delay(0), 0) == None


from python_code import arduino_NamedElement

def test_arduino_NamedElement___init__():
    assert arduino_NamedElement.__init__(arduino_NamedElement(''), '') == None


from python_code import arduino_Expression
from python_code import arduino_UnaryExpression

def test_arduino_UnaryExpression___init__():
    assert arduino_UnaryExpression.__init__(arduino_UnaryExpression('', arduino_UnaryExpression=arduino_Expression()), '', arduino_UnaryExpression=arduino_Expression()) == None

