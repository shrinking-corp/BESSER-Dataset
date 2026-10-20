from python_code import urml_BoolLiteral

def test_urml_BoolLiteral___init__():
    assert urml_BoolLiteral.__init__(urml_BoolLiteral(True), False) == None


from python_code import urml_Identifiable
from python_code import urml_Identifier

def test_urml_Identifiable___init__():
    assert urml_Identifiable.__init__(urml_Identifiable(False, False, '\x00\x00', urml_Identifiable=urml_Identifier()), False, False, '', urml_Identifiable=urml_Identifier()) == None


from python_code import urml_IntLiteral

def test_urml_IntLiteral___init__():
    assert urml_IntLiteral.__init__(urml_IntLiteral(0), 0) == None


from python_code import urml_ConcatenateExpression
from python_code import urml_Expression
from python_code import urml_LogStatement
from python_code import urml_StringExpression

def test_urml_StringExpression___init__():
    assert urml_StringExpression.__init__(urml_StringExpression('', urml_StringExpression157=urml_Expression(), urml_StringExpression=urml_LogStatement(), urml_StringExpression168=urml_ConcatenateExpression(), urml_StringExpression171=urml_ConcatenateExpression()), '', urml_StringExpression157=urml_Expression(), urml_StringExpression=urml_LogStatement(), urml_StringExpression168=urml_ConcatenateExpression(), urml_StringExpression171=urml_ConcatenateExpression()) == None


from python_code import urml_Expression
from python_code import urml_LocalVar
from python_code import urml_Variable

def test_urml_Variable___init__():
    assert urml_Variable.__init__(urml_Variable(True, urml_Variable=urml_LocalVar(), urml_Variable121=urml_Expression()), False, urml_Variable=urml_LocalVar(), urml_Variable121=urml_Expression()) == None

