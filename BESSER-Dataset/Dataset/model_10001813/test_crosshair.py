from python_code import A

def test_A___init__():
    assert A.__init__(A(0, '\x00', b0=set()), 0, '', b0=set()) == None


from python_code import C

def test_C___init__():
    assert C.__init__(C(0, '\x00', b2=set()), 0, '', b2=set()) == None

