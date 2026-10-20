from python_code import A

def test_A___init__():
    assert A.__init__(A(False, bs0=set()), False, bs0=set()) == None


from python_code import C

def test_C___init__():
    assert C.__init__(C(''), '') == None

