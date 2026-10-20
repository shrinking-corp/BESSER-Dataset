from python_code import eol_expression_BooleanExpression

def test_eol_expression_BooleanExpression___init__():
    assert eol_expression_BooleanExpression.__init__(eol_expression_BooleanExpression(True), False) == None


from python_code import eol_expression_IntegerExpression

def test_eol_expression_IntegerExpression___init__():
    assert eol_expression_IntegerExpression.__init__(eol_expression_IntegerExpression(0), 0) == None


from python_code import eol_expression_RealExpression

def test_eol_expression_RealExpression___init__():
    assert eol_expression_RealExpression.__init__(eol_expression_RealExpression(0.0), 0.0) == None


from python_code import eol_expression_StringExpression

def test_eol_expression_StringExpression___init__():
    assert eol_expression_StringExpression.__init__(eol_expression_StringExpression(''), '') == None

