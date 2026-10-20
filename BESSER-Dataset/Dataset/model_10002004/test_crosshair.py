from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import R
from python_code import X

def test_X___init__():
    assert X.__init__(X('', r5=R(), w6=set()), '', r5=R(), w6=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

