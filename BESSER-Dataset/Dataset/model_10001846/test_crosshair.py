from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', b0=set(), r3=R()), '', b0=set(), r3=R()) == None


from python_code import A12
from python_code import R2

def test_A12___init__():
    assert A12.__init__(A12('', b6=set(), r9=R2()), '', b6=set(), r9=R2()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None


from python_code import Y2

def test_Y2___init__():
    assert Y2.__init__(Y2(''), '') == None

