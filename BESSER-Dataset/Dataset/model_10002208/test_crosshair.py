from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import C

def test_C___init__():
    assert C.__init__(C(0, False, b3=set()), 0, False, b3=set()) == None


from python_code import C1

def test_C1___init__():
    assert C1.__init__(C1(0, False), 0, False) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

