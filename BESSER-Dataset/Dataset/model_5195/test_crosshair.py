from python_code import a_C

def test_a_C___init__():
    assert a_C.__init__(a_C(''), '') == None

def test_a_C_o():
    assert a_C.o(a_C(''), 0) == None

