from python_code import d3ql_BooleanLiteral

def test_d3ql_BooleanLiteral___init__():
    assert d3ql_BooleanLiteral.__init__(d3ql_BooleanLiteral(''), '') == None


from python_code import d3ql_FunctionCall

def test_d3ql_FunctionCall___init__():
    assert d3ql_FunctionCall.__init__(d3ql_FunctionCall('', d3ql_FunctionCall=set()), '', d3ql_FunctionCall=set()) == None


from python_code import d3ql_IntegerLiteral

def test_d3ql_IntegerLiteral___init__():
    assert d3ql_IntegerLiteral.__init__(d3ql_IntegerLiteral(0), 0) == None


from python_code import d3ql_Named
from python_code import d3ql_PathExpression

def test_d3ql_Named___init__():
    assert d3ql_Named.__init__(d3ql_Named('', d3ql_Named=d3ql_PathExpression()), '', d3ql_Named=d3ql_PathExpression()) == None


from python_code import d3ql_PathElement
from python_code import d3ql_PathExpression

def test_d3ql_PathElement___init__():
    assert d3ql_PathElement.__init__(d3ql_PathElement('', d3ql_PathElement=d3ql_PathExpression()), '', d3ql_PathElement=d3ql_PathExpression()) == None


from python_code import d3ql_StringLiteral

def test_d3ql_StringLiteral___init__():
    assert d3ql_StringLiteral.__init__(d3ql_StringLiteral(''), '') == None

