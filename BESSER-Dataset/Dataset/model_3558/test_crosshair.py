from python_code import xs_AndExpression
from python_code import xs_Expression

def test_xs_AndExpression___init__():
    assert xs_AndExpression.__init__(xs_AndExpression('', xs_AndExpression=xs_Expression(), xs_AndExpression72=xs_Expression()), '', xs_AndExpression=xs_Expression(), xs_AndExpression72=xs_Expression()) == None


from python_code import xs_ComparisonExpression
from python_code import xs_Expression

def test_xs_ComparisonExpression___init__():
    assert xs_ComparisonExpression.__init__(xs_ComparisonExpression('', xs_ComparisonExpression82=xs_Expression(), xs_ComparisonExpression=xs_Expression()), '', xs_ComparisonExpression82=xs_Expression(), xs_ComparisonExpression=xs_Expression()) == None


from python_code import xs_EqualsExpression
from python_code import xs_Expression

def test_xs_EqualsExpression___init__():
    assert xs_EqualsExpression.__init__(xs_EqualsExpression('', xs_EqualsExpression=xs_Expression(), xs_EqualsExpression77=xs_Expression()), '', xs_EqualsExpression=xs_Expression(), xs_EqualsExpression77=xs_Expression()) == None


from python_code import xs_Expression
from python_code import xs_Factor

def test_xs_Factor___init__():
    assert xs_Factor.__init__(xs_Factor('', xs_Factor=xs_Expression(), xs_Factor92=xs_Expression()), '', xs_Factor=xs_Expression(), xs_Factor92=xs_Expression()) == None


from python_code import xs_Expression
from python_code import xs_ForStatement
from python_code import xs_ForVarDeclaration
from python_code import xs_Statement

def test_xs_ForStatement___init__():
    assert xs_ForStatement.__init__(xs_ForStatement('', xs_ForStatement=xs_ForVarDeclaration(), xs_ForStatement44=xs_Expression(), xs_ForStatement47=xs_Statement()), '', xs_ForStatement=xs_ForVarDeclaration(), xs_ForStatement44=xs_Expression(), xs_ForStatement47=xs_Statement()) == None


from python_code import xs_Block
from python_code import xs_Call
from python_code import xs_FunctionDeclaration
from python_code import xs_Type

def test_xs_FunctionDeclaration___init__():
    assert xs_FunctionDeclaration.__init__(xs_FunctionDeclaration('\x00\x00', False, xs_FunctionDeclaration=xs_Type(), xs_FunctionDeclaration10=set(), xs_FunctionDeclaration13=xs_Block(), xs_FunctionDeclaration95=xs_Call()), '', True, xs_FunctionDeclaration=xs_Type(), xs_FunctionDeclaration10=set(), xs_FunctionDeclaration13=xs_Block(), xs_FunctionDeclaration95=xs_Call()) == None


from python_code import xs_GlobalVarDeclaration
from python_code import xs_Type

def test_xs_GlobalVarDeclaration___init__():
    assert xs_GlobalVarDeclaration.__init__(xs_GlobalVarDeclaration(False, False, xs_GlobalVarDeclaration=xs_Type()), False, False, xs_GlobalVarDeclaration=xs_Type()) == None


from python_code import xs_IncludeDeclaration

def test_xs_IncludeDeclaration___init__():
    assert xs_IncludeDeclaration.__init__(xs_IncludeDeclaration(''), '') == None


from python_code import xs_LiteralBool

def test_xs_LiteralBool___init__():
    assert xs_LiteralBool.__init__(xs_LiteralBool(True), False) == None


from python_code import xs_LiteralFloat

def test_xs_LiteralFloat___init__():
    assert xs_LiteralFloat.__init__(xs_LiteralFloat(0.0), 0.0) == None


from python_code import xs_LiteralInt

def test_xs_LiteralInt___init__():
    assert xs_LiteralInt.__init__(xs_LiteralInt(0), 0) == None


from python_code import xs_LiteralString

def test_xs_LiteralString___init__():
    assert xs_LiteralString.__init__(xs_LiteralString(''), '') == None


from python_code import xs_Expression
from python_code import xs_OrExpression

def test_xs_OrExpression___init__():
    assert xs_OrExpression.__init__(xs_OrExpression('', xs_OrExpression=xs_Expression(), xs_OrExpression67=xs_Expression()), '', xs_OrExpression=xs_Expression(), xs_OrExpression67=xs_Expression()) == None


from python_code import xs_Block
from python_code import xs_RuleDeclaration

def test_xs_RuleDeclaration___init__():
    assert xs_RuleDeclaration.__init__(xs_RuleDeclaration('', False, False, False, '', 0, 0, 0, xs_RuleDeclaration=xs_Block()), '', False, False, False, '', 0, 0, 0, xs_RuleDeclaration=xs_Block()) == None


from python_code import xs_Expression
from python_code import xs_Term

def test_xs_Term___init__():
    assert xs_Term.__init__(xs_Term('', xs_Term=xs_Expression(), xs_Term87=xs_Expression()), '', xs_Term=xs_Expression(), xs_Term87=xs_Expression()) == None

