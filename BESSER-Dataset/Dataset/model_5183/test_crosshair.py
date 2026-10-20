from python_code import TransitionQVT_A

def test_TransitionQVT_A___init__():
    assert TransitionQVT_A.__init__(TransitionQVT_A(0.0, '\x00\x00'), 0.0, '') == None


from python_code import TransitionQVT_B

def test_TransitionQVT_B___init__():
    assert TransitionQVT_B.__init__(TransitionQVT_B(''), '') == None


from python_code import TransitionQVT_C

def test_TransitionQVT_C___init__():
    assert TransitionQVT_C.__init__(TransitionQVT_C(''), '') == None

