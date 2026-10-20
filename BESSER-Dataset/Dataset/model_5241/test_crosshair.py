from python_code import rhs_X

def test_rhs_X___init__():
    assert rhs_X.__init__(rhs_X('\x00', rhs_X=set()), '', rhs_X=set()) == None

