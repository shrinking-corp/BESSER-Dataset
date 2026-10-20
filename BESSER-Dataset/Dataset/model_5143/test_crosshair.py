from python_code import lhs_A

def test_lhs_A___init__():
    assert lhs_A.__init__(lhs_A('\x00', lhs_A=set()), '', lhs_A=set()) == None

