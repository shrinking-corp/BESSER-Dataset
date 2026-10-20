from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', r9=R(), b10=set()), '', r9=R(), b10=set()) == None


from python_code import A2

def test_A2___init__():
    assert A2.__init__(A2(''), '') == None


from python_code import B2

def test_B2___init__():
    assert B2.__init__(B2(0, c5=set()), 0, c5=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

