from python_code import mathInterpreter_Num

def test_mathInterpreter_Num___init__():
    assert mathInterpreter_Num.__init__(mathInterpreter_Num(0), 0) == None


from python_code import mathInterpreter_Expression
from python_code import mathInterpreter_Solution
from python_code import mathInterpreter_Variable
from python_code import mathInterpreter_VariableRef

def test_mathInterpreter_Variable___init__():
    assert mathInterpreter_Variable.__init__(mathInterpreter_Variable('', mathInterpreter_Variable=mathInterpreter_Solution(), mathInterpreter_Variable4=mathInterpreter_Expression(), mathInterpreter_Variable18=mathInterpreter_VariableRef()), '', mathInterpreter_Variable=mathInterpreter_Solution(), mathInterpreter_Variable4=mathInterpreter_Expression(), mathInterpreter_Variable18=mathInterpreter_VariableRef()) == None

