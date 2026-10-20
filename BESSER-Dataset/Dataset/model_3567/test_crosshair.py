from python_code import expressions_BooleanValue

def test_expressions_BooleanValue___init__():
    assert expressions_BooleanValue.__init__(expressions_BooleanValue(True), False) == None


from python_code import expressions_NumberValue

def test_expressions_NumberValue___init__():
    assert expressions_NumberValue.__init__(expressions_NumberValue(''), '') == None


from python_code import expressions_StringValue

def test_expressions_StringValue___init__():
    assert expressions_StringValue.__init__(expressions_StringValue(''), '') == None


from python_code import expressions_Variable

def test_expressions_Variable___init__():
    assert expressions_Variable.__init__(expressions_Variable(''), '') == None

