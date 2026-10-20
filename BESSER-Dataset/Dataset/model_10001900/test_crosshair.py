from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('\x00', r1=R(), b2=set()), '', r1=R(), b2=set()) == None


from python_code import A2
from python_code import R2

def test_A2___init__():
    assert A2.__init__(A2('', r5=R2(), b6=set()), '', r5=R2(), b6=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None


from python_code import Y2

def test_Y2___init__():
    assert Y2.__init__(Y2(''), '') == None

