from python_code import operators_BooleanExp

def test_operators_BooleanExp___init__():
    assert operators_BooleanExp.__init__(operators_BooleanExp(''), '') == None


from python_code import operators_IntegerExp

def test_operators_IntegerExp___init__():
    assert operators_IntegerExp.__init__(operators_IntegerExp(''), '') == None


from python_code import operators_OperatorCallExp

def test_operators_OperatorCallExp___init__():
    assert operators_OperatorCallExp.__init__(operators_OperatorCallExp(''), '') == None


from python_code import operators_RealExp

def test_operators_RealExp___init__():
    assert operators_RealExp.__init__(operators_RealExp(''), '') == None


from python_code import operators_StringExp

def test_operators_StringExp___init__():
    assert operators_StringExp.__init__(operators_StringExp(''), '') == None

