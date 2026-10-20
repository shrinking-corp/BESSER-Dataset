from python_code import logo_Parameter

def test_logo_Parameter___init__():
    assert logo_Parameter.__init__(logo_Parameter(''), '') == None


from python_code import logo_Symbol

def test_logo_Symbol___init__():
    assert logo_Symbol.__init__(logo_Symbol(''), '') == None


from python_code import logo_constant_BoolValue

def test_logo_constant_BoolValue___init__():
    assert logo_constant_BoolValue.__init__(logo_constant_BoolValue(True), False) == None


from python_code import logo_constant_IntValue

def test_logo_constant_IntValue___init__():
    assert logo_constant_IntValue.__init__(logo_constant_IntValue(0), 0) == None


from python_code import logo_expression_VariableRead

def test_logo_expression_VariableRead___init__():
    assert logo_expression_VariableRead.__init__(logo_expression_VariableRead(''), '') == None


from python_code import logo_statement_ProcedureDefinition

def test_logo_statement_ProcedureDefinition___init__():
    assert logo_statement_ProcedureDefinition.__init__(logo_statement_ProcedureDefinition('', logo_statement_ProcedureDefinition=set(), logo_statement_ProcedureDefinition8=set()), '', logo_statement_ProcedureDefinition=set(), logo_statement_ProcedureDefinition8=set()) == None


from python_code import logo_value_BoolValue

def test_logo_value_BoolValue___init__():
    assert logo_value_BoolValue.__init__(logo_value_BoolValue(True), False) == None


from python_code import logo_value_IntValue

def test_logo_value_IntValue___init__():
    assert logo_value_IntValue.__init__(logo_value_IntValue(0), 0) == None

