from python_code import jpql_BetweenExpression
from python_code import jpql_Value
from python_code import jpql_Variable

def test_jpql_BetweenExpression___init__():
    assert jpql_BetweenExpression.__init__(jpql_BetweenExpression(True, jpql_BetweenExpression=jpql_Variable(), jpql_BetweenExpression95=jpql_Value(), jpql_BetweenExpression98=jpql_Value()), False, jpql_BetweenExpression=jpql_Variable(), jpql_BetweenExpression95=jpql_Value(), jpql_BetweenExpression98=jpql_Value()) == None


from python_code import jpql_BooleanExpression

def test_jpql_BooleanExpression___init__():
    assert jpql_BooleanExpression.__init__(jpql_BooleanExpression(True), False) == None


from python_code import jpql_DateTimeExpression

def test_jpql_DateTimeExpression___init__():
    assert jpql_DateTimeExpression.__init__(jpql_DateTimeExpression(''), '') == None


from python_code import jpql_EmptyComparisonExpression
from python_code import jpql_Variable

def test_jpql_EmptyComparisonExpression___init__():
    assert jpql_EmptyComparisonExpression.__init__(jpql_EmptyComparisonExpression(True, jpql_EmptyComparisonExpression=jpql_Variable()), False, jpql_EmptyComparisonExpression=jpql_Variable()) == None


from python_code import jpql_ExistsExpression
from python_code import jpql_SelectStatement

def test_jpql_ExistsExpression___init__():
    assert jpql_ExistsExpression.__init__(jpql_ExistsExpression(True, jpql_ExistsExpression=jpql_SelectStatement()), False, jpql_ExistsExpression=jpql_SelectStatement()) == None


from python_code import jpql_FromClass

def test_jpql_FromClass___init__():
    assert jpql_FromClass.__init__(jpql_FromClass('', jpql_FromClass=set()), '', jpql_FromClass=set()) == None


from python_code import jpql_Function

def test_jpql_Function___init__():
    assert jpql_Function.__init__(jpql_Function('', jpql_Function=set()), '', jpql_Function=set()) == None


from python_code import jpql_Import
from python_code import jpql_QueryModule

def test_jpql_Import___init__():
    assert jpql_Import.__init__(jpql_Import('', jpql_Import=jpql_QueryModule()), '', jpql_Import=jpql_QueryModule()) == None


from python_code import jpql_InExpression
from python_code import jpql_Variable

def test_jpql_InExpression___init__():
    assert jpql_InExpression.__init__(jpql_InExpression(True, jpql_InExpression=jpql_Variable()), False, jpql_InExpression=jpql_Variable()) == None


from python_code import jpql_IntegerExpression

def test_jpql_IntegerExpression___init__():
    assert jpql_IntegerExpression.__init__(jpql_IntegerExpression(0), 0) == None


from python_code import jpql_LeftJoin

def test_jpql_LeftJoin___init__():
    assert jpql_LeftJoin.__init__(jpql_LeftJoin(True), False) == None


from python_code import jpql_LikeExpression
from python_code import jpql_Variable

def test_jpql_LikeExpression___init__():
    assert jpql_LikeExpression.__init__(jpql_LikeExpression(False, '\x00', jpql_LikeExpression=jpql_Variable()), False, '\x00', jpql_LikeExpression=jpql_Variable()) == None


from python_code import jpql_JPQLQuery
from python_code import jpql_NamedQuery
from python_code import jpql_QueryModule

def test_jpql_NamedQuery___init__():
    assert jpql_NamedQuery.__init__(jpql_NamedQuery('', jpql_NamedQuery=jpql_QueryModule(), jpql_NamedQuery6=jpql_JPQLQuery()), '', jpql_NamedQuery=jpql_QueryModule(), jpql_NamedQuery6=jpql_JPQLQuery()) == None


from python_code import jpql_NullComparisonExpression
from python_code import jpql_Variable

def test_jpql_NullComparisonExpression___init__():
    assert jpql_NullComparisonExpression.__init__(jpql_NullComparisonExpression(True, jpql_NullComparisonExpression=jpql_Variable()), False, jpql_NullComparisonExpression=jpql_Variable()) == None


from python_code import jpql_NullExpression

def test_jpql_NullExpression___init__():
    assert jpql_NullExpression.__init__(jpql_NullExpression(''), '') == None


from python_code import jpql_ExpressionTerm
from python_code import jpql_OperatorExpression
from python_code import jpql_Variable

def test_jpql_OperatorExpression___init__():
    assert jpql_OperatorExpression.__init__(jpql_OperatorExpression('', jpql_OperatorExpression=jpql_Variable(), jpql_OperatorExpression66=jpql_ExpressionTerm()), '', jpql_OperatorExpression=jpql_Variable(), jpql_OperatorExpression66=jpql_ExpressionTerm()) == None


from python_code import jpql_OrderClause
from python_code import jpql_SelectStatement

def test_jpql_OrderClause___init__():
    assert jpql_OrderClause.__init__(jpql_OrderClause(False, False, jpql_OrderClause18=set(), jpql_OrderClause=jpql_SelectStatement()), False, False, jpql_OrderClause18=set(), jpql_OrderClause=jpql_SelectStatement()) == None


from python_code import jpql_ParameterExpression

def test_jpql_ParameterExpression___init__():
    assert jpql_ParameterExpression.__init__(jpql_ParameterExpression(''), '') == None


from python_code import jpql_SelectClause
from python_code import jpql_SelectFromClause

def test_jpql_SelectClause___init__():
    assert jpql_SelectClause.__init__(jpql_SelectClause(False, jpql_SelectClause=jpql_SelectFromClause(), jpql_SelectClause42=set()), False, jpql_SelectClause=jpql_SelectFromClause(), jpql_SelectClause42=set()) == None


from python_code import jpql_SelectConstructorExpression

def test_jpql_SelectConstructorExpression___init__():
    assert jpql_SelectConstructorExpression.__init__(jpql_SelectConstructorExpression('', jpql_SelectConstructorExpression=set()), '', jpql_SelectConstructorExpression=set()) == None


from python_code import jpql_StringExpression

def test_jpql_StringExpression___init__():
    assert jpql_StringExpression.__init__(jpql_StringExpression(''), '') == None

