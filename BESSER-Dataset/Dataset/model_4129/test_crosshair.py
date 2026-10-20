from python_code import mathinterpreter_Number

def test_mathinterpreter_Number___init__():
    assert mathinterpreter_Number.__init__(mathinterpreter_Number(0), 0) == None


from python_code import mathinterpreter_DefineExpr
from python_code import mathinterpreter_PMExpression
from python_code import mathinterpreter_Variable
from python_code import mathinterpreter_VariableDefinition

def test_mathinterpreter_Variable___init__():
    assert mathinterpreter_Variable.__init__(mathinterpreter_Variable('', mathinterpreter_Variable=mathinterpreter_VariableDefinition(), mathinterpreter_Variable4=mathinterpreter_DefineExpr(), mathinterpreter_Variable9=mathinterpreter_PMExpression()), '', mathinterpreter_Variable=mathinterpreter_VariableDefinition(), mathinterpreter_Variable4=mathinterpreter_DefineExpr(), mathinterpreter_Variable9=mathinterpreter_PMExpression()) == None


from python_code import mathinterpreter_VariableName

def test_mathinterpreter_VariableName___init__():
    assert mathinterpreter_VariableName.__init__(mathinterpreter_VariableName(''), '') == None

