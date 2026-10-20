from python_code import noop_AsmStatement

def test_noop_AsmStatement___init__():
    assert noop_AsmStatement.__init__(noop_AsmStatement('', noop_AsmStatement=set()), '', noop_AsmStatement=set()) == None


from python_code import noop_AssignmentExpression
from python_code import noop_Expression

def test_noop_AssignmentExpression___init__():
    assert noop_AssignmentExpression.__init__(noop_AssignmentExpression('', noop_AssignmentExpression69=noop_Expression(), noop_AssignmentExpression=noop_Expression()), '', noop_AssignmentExpression69=noop_Expression(), noop_AssignmentExpression=noop_Expression()) == None


from python_code import noop_BoolLiteral

def test_noop_BoolLiteral___init__():
    assert noop_BoolLiteral.__init__(noop_BoolLiteral(True), False) == None


from python_code import noop_BreakStatement

def test_noop_BreakStatement___init__():
    assert noop_BreakStatement.__init__(noop_BreakStatement(''), '') == None


from python_code import noop_ByteLiteral

def test_noop_ByteLiteral___init__():
    assert noop_ByteLiteral.__init__(noop_ByteLiteral(''), '') == None


from python_code import noop_ContinueStatement

def test_noop_ContinueStatement___init__():
    assert noop_ContinueStatement.__init__(noop_ContinueStatement(''), '') == None


from python_code import noop_Block
from python_code import noop_Expression
from python_code import noop_ForStatement

def test_noop_ForStatement___init__():
    assert noop_ForStatement.__init__(noop_ForStatement('', noop_ForStatement=set(), noop_ForStatement39=set(), noop_ForStatement42=noop_Expression(), noop_ForStatement45=set(), noop_ForStatement48=noop_Block()), '', noop_ForStatement=set(), noop_ForStatement39=set(), noop_ForStatement42=noop_Expression(), noop_ForStatement45=set(), noop_ForStatement48=noop_Block()) == None


from python_code import noop_Block
from python_code import noop_ForeverStatement

def test_noop_ForeverStatement___init__():
    assert noop_ForeverStatement.__init__(noop_ForeverStatement('', noop_ForeverStatement=noop_Block()), '', noop_ForeverStatement=noop_Block()) == None


from python_code import noop_Expression
from python_code import noop_ReturnStatement

def test_noop_ReturnStatement___init__():
    assert noop_ReturnStatement.__init__(noop_ReturnStatement('', noop_ReturnStatement=noop_Expression()), '', noop_ReturnStatement=noop_Expression()) == None


from python_code import noop_StringLiteral

def test_noop_StringLiteral___init__():
    assert noop_StringLiteral.__init__(noop_StringLiteral(''), '') == None

