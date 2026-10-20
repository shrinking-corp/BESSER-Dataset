from python_code import A

def test_A___init__():
    assert A.__init__(A('', b2=set()), '', b2=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', b4=set(), r7=R()), '', b4=set(), r7=R()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

