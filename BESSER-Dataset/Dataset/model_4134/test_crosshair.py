from python_code import mathCompiler_External

def test_mathCompiler_External___init__():
    assert mathCompiler_External.__init__(mathCompiler_External(0, 0), 0, 0) == None


from python_code import mathCompiler_Expression
from python_code import mathCompiler_Let

def test_mathCompiler_Let___init__():
    assert mathCompiler_Let.__init__(mathCompiler_Let('', mathCompiler_Let=mathCompiler_Expression(), mathCompiler_Let26=mathCompiler_Expression()), '', mathCompiler_Let=mathCompiler_Expression(), mathCompiler_Let26=mathCompiler_Expression()) == None


from python_code import mathCompiler_Expression
from python_code import mathCompiler_Expressions
from python_code import mathCompiler_MathExp

def test_mathCompiler_MathExp___init__():
    assert mathCompiler_MathExp.__init__(mathCompiler_MathExp('', mathCompiler_MathExp=mathCompiler_Expressions(), mathCompiler_MathExp2=mathCompiler_Expression()), '', mathCompiler_MathExp=mathCompiler_Expressions(), mathCompiler_MathExp2=mathCompiler_Expression()) == None


from python_code import mathCompiler_Num

def test_mathCompiler_Num___init__():
    assert mathCompiler_Num.__init__(mathCompiler_Num(0), 0) == None


from python_code import mathCompiler_Var

def test_mathCompiler_Var___init__():
    assert mathCompiler_Var.__init__(mathCompiler_Var(''), '') == None

