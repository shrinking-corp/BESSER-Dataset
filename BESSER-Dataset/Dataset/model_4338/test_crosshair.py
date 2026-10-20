from python_code import ast_Number

def test_ast_Number___init__():
    assert ast_Number.__init__(ast_Number(0), 0) == None


from python_code import ast_Variable

def test_ast_Variable___init__():
    assert ast_Variable.__init__(ast_Variable(''), '') == None

