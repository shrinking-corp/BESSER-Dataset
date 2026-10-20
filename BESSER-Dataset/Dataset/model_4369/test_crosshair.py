from python_code import klangexpr_BooleanLiteral

def test_klangexpr_BooleanLiteral___init__():
    assert klangexpr_BooleanLiteral.__init__(klangexpr_BooleanLiteral(True), False) == None


from python_code import klangexpr_DoubleLiteral

def test_klangexpr_DoubleLiteral___init__():
    assert klangexpr_DoubleLiteral.__init__(klangexpr_DoubleLiteral(0.0), 0.0) == None


from python_code import klangexpr_FunctionCall

def test_klangexpr_FunctionCall___init__():
    assert klangexpr_FunctionCall.__init__(klangexpr_FunctionCall('', klangexpr_FunctionCall=set()), '', klangexpr_FunctionCall=set()) == None


from python_code import klangexpr_IntegerLiteral

def test_klangexpr_IntegerLiteral___init__():
    assert klangexpr_IntegerLiteral.__init__(klangexpr_IntegerLiteral(0), 0) == None


from python_code import klangexpr_SendMessage

def test_klangexpr_SendMessage___init__():
    assert klangexpr_SendMessage.__init__(klangexpr_SendMessage(''), '') == None


from python_code import klangexpr_StringLiteral

def test_klangexpr_StringLiteral___init__():
    assert klangexpr_StringLiteral.__init__(klangexpr_StringLiteral(''), '') == None


from python_code import klangexpr_Expression
from python_code import klangexpr_VariableAssignment

def test_klangexpr_VariableAssignment___init__():
    assert klangexpr_VariableAssignment.__init__(klangexpr_VariableAssignment('', klangexpr_VariableAssignment=klangexpr_Expression()), '', klangexpr_VariableAssignment=klangexpr_Expression()) == None


from python_code import klangexpr_VariableReference

def test_klangexpr_VariableReference___init__():
    assert klangexpr_VariableReference.__init__(klangexpr_VariableReference(''), '') == None

