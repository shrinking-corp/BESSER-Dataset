from python_code import expression_BooleanLiteral

def test_expression_BooleanLiteral___init__():
    assert expression_BooleanLiteral.__init__(expression_BooleanLiteral(True), False) == None


from python_code import expression_IntegerLiteral

def test_expression_IntegerLiteral___init__():
    assert expression_IntegerLiteral.__init__(expression_IntegerLiteral(0), 0) == None


from python_code import expression_PredicateBooleanOperator

def test_expression_PredicateBooleanOperator___init__():
    assert expression_PredicateBooleanOperator.__init__(expression_PredicateBooleanOperator('\x00', expression_PredicateBooleanOperator=set()), '', expression_PredicateBooleanOperator=set()) == None


from python_code import expression_StringLiteral

def test_expression_StringLiteral___init__():
    assert expression_StringLiteral.__init__(expression_StringLiteral(''), '') == None


from python_code import expression_TimeLiteral

def test_expression_TimeLiteral___init__():
    assert expression_TimeLiteral.__init__(expression_TimeLiteral(''), '') == None

