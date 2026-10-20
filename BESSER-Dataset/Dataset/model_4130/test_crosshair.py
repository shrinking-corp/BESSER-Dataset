from python_code import mathinterpreter_External

def test_mathinterpreter_External___init__():
    assert mathinterpreter_External.__init__(mathinterpreter_External('', mathinterpreter_External=set()), '', mathinterpreter_External=set()) == None


from python_code import mathinterpreter_MathExpression
from python_code import mathinterpreter_Model
from python_code import mathinterpreter_PMExpression

def test_mathinterpreter_MathExpression___init__():
    assert mathinterpreter_MathExpression.__init__(mathinterpreter_MathExpression('', mathinterpreter_MathExpression=mathinterpreter_Model(), mathinterpreter_MathExpression2=mathinterpreter_PMExpression()), '', mathinterpreter_MathExpression=mathinterpreter_Model(), mathinterpreter_MathExpression2=mathinterpreter_PMExpression()) == None


from python_code import mathinterpreter_Number

def test_mathinterpreter_Number___init__():
    assert mathinterpreter_Number.__init__(mathinterpreter_Number(0), 0) == None


from python_code import mathinterpreter_DefineExpr
from python_code import mathinterpreter_PMExpression
from python_code import mathinterpreter_Variable

def test_mathinterpreter_Variable___init__():
    assert mathinterpreter_Variable.__init__(mathinterpreter_Variable('', mathinterpreter_Variable=mathinterpreter_DefineExpr(), mathinterpreter_Variable5=mathinterpreter_PMExpression()), '', mathinterpreter_Variable=mathinterpreter_DefineExpr(), mathinterpreter_Variable5=mathinterpreter_PMExpression()) == None


from python_code import mathinterpreter_VariableName

def test_mathinterpreter_VariableName___init__():
    assert mathinterpreter_VariableName.__init__(mathinterpreter_VariableName(''), '') == None

