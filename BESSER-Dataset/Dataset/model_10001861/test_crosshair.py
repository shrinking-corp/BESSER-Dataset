from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', b6=set(), r9=R()), '', b6=set(), r9=R()) == None


from python_code import A2
from python_code import B2

def test_A2___init__():
    assert A2.__init__(A2(0, c11=B2()), 0, c11=B2()) == None


from python_code import A21

def test_A21___init__():
    assert A21.__init__(A21(True), False) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

