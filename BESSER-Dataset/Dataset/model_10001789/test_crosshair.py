from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A4
from python_code import R

def test_A4___init__():
    assert A4.__init__(A4('', r7=R(), b8=set()), '', r7=R(), b8=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

