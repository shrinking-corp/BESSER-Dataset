from python_code import Primitives_Back
from python_code import Primitives_Expression
from python_code import Primitives_Forward
from python_code import Primitives_Left
from python_code import Primitives_Right

def test_Primitives_Expression___init__():
    assert Primitives_Expression.__init__(Primitives_Expression(Primitives_Expression3=Primitives_Back(), Primitives_Expression5=Primitives_Left(), Primitives_Expression7=Primitives_Right(), Primitives_Expression=Primitives_Forward()), Primitives_Expression3=Primitives_Back(), Primitives_Expression5=Primitives_Left(), Primitives_Expression7=Primitives_Right(), Primitives_Expression=Primitives_Forward()) == None

def test_Primitives_Expression_eval():
    assert Primitives_Expression.eval(Primitives_Expression(Primitives_Expression3=Primitives_Back(), Primitives_Expression5=Primitives_Left(), Primitives_Expression7=Primitives_Right(), Primitives_Expression=Primitives_Forward()), '') == None

