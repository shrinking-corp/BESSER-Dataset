from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r3=R(), b4=set()), '', r3=R(), b4=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None


from python_code import tp2BMOexe3_A
from python_code import tp2BMOexe3_B

def test_tp2BMOexe3_A___init__():
    assert tp2BMOexe3_A.__init__(tp2BMOexe3_A(tp2BMOexe3_B(), 0, False, b7=tp2BMOexe3_B()), tp2BMOexe3_B(), 0, False, b7=tp2BMOexe3_B()) == None

