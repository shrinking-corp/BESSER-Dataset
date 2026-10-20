from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', r5=R(), b6=set()), '', r5=R(), b6=set()) == None


from python_code import A2
from python_code import R2

def test_A2___init__():
    assert A2.__init__(A2('', r11=R2(), b12=set()), '', r11=R2(), b12=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None


from python_code import Y2

def test_Y2___init__():
    assert Y2.__init__(Y2(''), '') == None

