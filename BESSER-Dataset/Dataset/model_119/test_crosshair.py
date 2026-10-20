from python_code import dom_BinaryExpression
from python_code import dom_Expression

def test_dom_BinaryExpression___init__():
    assert dom_BinaryExpression.__init__(dom_BinaryExpression('', 0, dom_BinaryExpression=dom_Expression(), dom_BinaryExpression35=dom_Expression()), '', 0, dom_BinaryExpression=dom_Expression(), dom_BinaryExpression35=dom_Expression()) == None


from python_code import dom_BooleanLiteral

def test_dom_BooleanLiteral___init__():
    assert dom_BooleanLiteral.__init__(dom_BooleanLiteral(''), '') == None


from python_code import dom_BreakStatement
from python_code import dom_ContinueStatement
from python_code import dom_Label
from python_code import dom_LabeledStatement

def test_dom_Label___init__():
    assert dom_Label.__init__(dom_Label('', dom_Label=dom_ContinueStatement(), dom_Label84=dom_BreakStatement(), dom_Label102=dom_LabeledStatement()), '', dom_Label=dom_ContinueStatement(), dom_Label84=dom_BreakStatement(), dom_Label102=dom_LabeledStatement()) == None


from python_code import dom_Node

def test_dom_Node___init__():
    assert dom_Node.__init__(dom_Node(0, 0), 0, 0) == None


from python_code import dom_NumericLiteral

def test_dom_NumericLiteral___init__():
    assert dom_NumericLiteral.__init__(dom_NumericLiteral(''), '') == None


from python_code import dom_RegularExpressionLiteral

def test_dom_RegularExpressionLiteral___init__():
    assert dom_RegularExpressionLiteral.__init__(dom_RegularExpressionLiteral(''), '') == None


from python_code import dom_StringLiteral

def test_dom_StringLiteral___init__():
    assert dom_StringLiteral.__init__(dom_StringLiteral(''), '') == None


from python_code import dom_Expression
from python_code import dom_UnaryExpression

def test_dom_UnaryExpression___init__():
    assert dom_UnaryExpression.__init__(dom_UnaryExpression('', dom_UnaryExpression=dom_Expression()), '', dom_UnaryExpression=dom_Expression()) == None


from python_code import dom_XmlTextFragment

def test_dom_XmlTextFragment___init__():
    assert dom_XmlTextFragment.__init__(dom_XmlTextFragment(''), '') == None

