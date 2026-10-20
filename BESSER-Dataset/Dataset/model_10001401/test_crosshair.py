from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r5=R(), b2=set()), '', r5=R(), b2=set()) == None


from python_code import A2
from python_code import R2

def test_A2___init__():
    assert A2.__init__(A2('', b8=set(), r11=R2()), '', b8=set(), r11=R2()) == None


from python_code import C

def test_C___init__():
    assert C.__init__(C(0, False, b1=set()), 0, False, b1=set()) == None


from python_code import C4

def test_C4___init__():
    assert C4.__init__(C4(0, False, b7=set()), 0, False, b7=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None


from python_code import Y2

def test_Y2___init__():
    assert Y2.__init__(Y2(''), '') == None

