from python_code import jPQL_AdditionExpression

def test_jPQL_AdditionExpression___init__():
    assert jPQL_AdditionExpression.__init__(jPQL_AdditionExpression(''), '') == None


from python_code import jPQL_BooleanLiteral

def test_jPQL_BooleanLiteral___init__():
    assert jPQL_BooleanLiteral.__init__(jPQL_BooleanLiteral(''), '') == None


from python_code import jPQL_ComparisonOperatorExpression

def test_jPQL_ComparisonOperatorExpression___init__():
    assert jPQL_ComparisonOperatorExpression.__init__(jPQL_ComparisonOperatorExpression(''), '') == None


from python_code import jPQL_Float
from python_code import jPQL_FloatLiteral

def test_jPQL_Float___init__():
    assert jPQL_Float.__init__(jPQL_Float(0, 0, jPQL_Float=jPQL_FloatLiteral()), 0, 0, jPQL_Float=jPQL_FloatLiteral()) == None


from python_code import jPQL_IntegerLiteral

def test_jPQL_IntegerLiteral___init__():
    assert jPQL_IntegerLiteral.__init__(jPQL_IntegerLiteral(0), 0) == None


from python_code import jPQL_LeftJoin

def test_jPQL_LeftJoin___init__():
    assert jPQL_LeftJoin.__init__(jPQL_LeftJoin(True), False) == None


from python_code import jPQL_MultiplicationExpression

def test_jPQL_MultiplicationExpression___init__():
    assert jPQL_MultiplicationExpression.__init__(jPQL_MultiplicationExpression(''), '') == None


from python_code import jPQL_NullLiteral

def test_jPQL_NullLiteral___init__():
    assert jPQL_NullLiteral.__init__(jPQL_NullLiteral(''), '') == None


from python_code import jPQL_ParameterExpression

def test_jPQL_ParameterExpression___init__():
    assert jPQL_ParameterExpression.__init__(jPQL_ParameterExpression('', 0), '', 0) == None


from python_code import jPQL_SelectClause
from python_code import jPQL_SelectStatement

def test_jPQL_SelectClause___init__():
    assert jPQL_SelectClause.__init__(jPQL_SelectClause(False, jPQL_SelectClause=jPQL_SelectStatement(), jPQL_SelectClause33=set()), False, jPQL_SelectClause=jPQL_SelectStatement(), jPQL_SelectClause33=set()) == None


from python_code import jPQL_SelectConstructorExpression

def test_jPQL_SelectConstructorExpression___init__():
    assert jPQL_SelectConstructorExpression.__init__(jPQL_SelectConstructorExpression('', jPQL_SelectConstructorExpression=set()), '', jPQL_SelectConstructorExpression=set()) == None


from python_code import jPQL_StringLiteral

def test_jPQL_StringLiteral___init__():
    assert jPQL_StringLiteral.__init__(jPQL_StringLiteral(''), '') == None

