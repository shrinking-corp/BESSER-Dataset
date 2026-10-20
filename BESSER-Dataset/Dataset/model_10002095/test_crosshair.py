from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', b2=set(), r4=R()), '', b2=set(), r4=R()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

