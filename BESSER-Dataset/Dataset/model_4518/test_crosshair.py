from python_code import Logo_Back
from python_code import Logo_Expression
from python_code import Logo_Forward
from python_code import Logo_Left
from python_code import Logo_Right

def test_Logo_Expression___init__():
    assert Logo_Expression.__init__(Logo_Expression(Logo_Expression=Logo_Back(), Logo_Expression3=Logo_Forward(), Logo_Expression5=Logo_Left(), Logo_Expression7=Logo_Right()), Logo_Expression=Logo_Back(), Logo_Expression3=Logo_Forward(), Logo_Expression5=Logo_Left(), Logo_Expression7=Logo_Right()) == None

def test_Logo_Expression_eval():
    assert Logo_Expression.eval(Logo_Expression(Logo_Expression=Logo_Back(), Logo_Expression3=Logo_Forward(), Logo_Expression5=Logo_Left(), Logo_Expression7=Logo_Right()), '') == None

