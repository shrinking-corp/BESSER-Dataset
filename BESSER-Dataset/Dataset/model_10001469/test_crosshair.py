from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import AA
from python_code import R

def test_AA___init__():
    assert AA.__init__(AA('', r5=R(), b6=set()), '', r5=R(), b6=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

