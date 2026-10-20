from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A2
from python_code import R

def test_A2___init__():
    assert A2.__init__(A2('', r5=R(), b6=set()), '', r5=R(), b6=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

