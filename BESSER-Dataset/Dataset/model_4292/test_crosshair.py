from python_code import expression_BooleanExpression

def test_expression_BooleanExpression___init__():
    assert expression_BooleanExpression.__init__(expression_BooleanExpression(''), '') == None


from python_code import expression_NegativeIntExpression

def test_expression_NegativeIntExpression___init__():
    assert expression_NegativeIntExpression.__init__(expression_NegativeIntExpression('', '\x00'), '\x00\x00', '') == None


from python_code import expression_StringExpression

def test_expression_StringExpression___init__():
    assert expression_StringExpression.__init__(expression_StringExpression(''), '') == None

