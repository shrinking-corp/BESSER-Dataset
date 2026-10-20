from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r1=R(), b2=set()), '', r1=R(), b2=set()) == None


from python_code import T

def test_T___init__():
    assert T.__init__(T(''), '') == None

