from python_code import myDsl_Expression
from python_code import myDsl_Let

def test_myDsl_Let___init__():
    assert myDsl_Let.__init__(myDsl_Let('', myDsl_Let26=myDsl_Expression(), myDsl_Let=myDsl_Expression()), '', myDsl_Let26=myDsl_Expression(), myDsl_Let=myDsl_Expression()) == None


from python_code import myDsl_Expression
from python_code import myDsl_MathExp

def test_myDsl_MathExp___init__():
    assert myDsl_MathExp.__init__(myDsl_MathExp('', myDsl_MathExp=myDsl_Expression()), '', myDsl_MathExp=myDsl_Expression()) == None


from python_code import myDsl_Method

def test_myDsl_Method___init__():
    assert myDsl_Method.__init__(myDsl_Method('\x00', myDsl_Method=set()), '', myDsl_Method=set()) == None


from python_code import myDsl_Num

def test_myDsl_Num___init__():
    assert myDsl_Num.__init__(myDsl_Num(0), 0) == None


from python_code import myDsl_Var

def test_myDsl_Var___init__():
    assert myDsl_Var.__init__(myDsl_Var(''), '') == None

