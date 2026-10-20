from python_code import asso_FloatConstant

def test_asso_FloatConstant___init__():
    assert asso_FloatConstant.__init__(asso_FloatConstant(0.0), 0.0) == None


from python_code import asso_NegFloatConstant

def test_asso_NegFloatConstant___init__():
    assert asso_NegFloatConstant.__init__(asso_NegFloatConstant(0.0), 0.0) == None

