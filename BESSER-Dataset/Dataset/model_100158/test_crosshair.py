from python_code import mql_BetweenExpression
from python_code import mql_Value
from python_code import mql_Variable

def test_mql_BetweenExpression___init__():
    assert mql_BetweenExpression.__init__(mql_BetweenExpression(True, mql_BetweenExpression=mql_Variable(), mql_BetweenExpression95=mql_Value(), mql_BetweenExpression98=mql_Value()), False, mql_BetweenExpression=mql_Variable(), mql_BetweenExpression95=mql_Value(), mql_BetweenExpression98=mql_Value()) == None


from python_code import mql_BooleanExpression

def test_mql_BooleanExpression___init__():
    assert mql_BooleanExpression.__init__(mql_BooleanExpression(True), False) == None


from python_code import mql_DateTimeExpression

def test_mql_DateTimeExpression___init__():
    assert mql_DateTimeExpression.__init__(mql_DateTimeExpression(''), '') == None


from python_code import mql_EmptyComparisonExpression
from python_code import mql_Variable

def test_mql_EmptyComparisonExpression___init__():
    assert mql_EmptyComparisonExpression.__init__(mql_EmptyComparisonExpression(True, mql_EmptyComparisonExpression=mql_Variable()), False, mql_EmptyComparisonExpression=mql_Variable()) == None


from python_code import mql_ExistsExpression
from python_code import mql_SelectStatement

def test_mql_ExistsExpression___init__():
    assert mql_ExistsExpression.__init__(mql_ExistsExpression(True, mql_ExistsExpression=mql_SelectStatement()), False, mql_ExistsExpression=mql_SelectStatement()) == None


from python_code import mql_FromClass

def test_mql_FromClass___init__():
    assert mql_FromClass.__init__(mql_FromClass('', mql_FromClass=set()), '', mql_FromClass=set()) == None


from python_code import mql_Function

def test_mql_Function___init__():
    assert mql_Function.__init__(mql_Function('', mql_Function=set()), '', mql_Function=set()) == None


from python_code import mql_Import
from python_code import mql_QueryModule

def test_mql_Import___init__():
    assert mql_Import.__init__(mql_Import('', mql_Import=mql_QueryModule()), '', mql_Import=mql_QueryModule()) == None


from python_code import mql_InExpression
from python_code import mql_Variable

def test_mql_InExpression___init__():
    assert mql_InExpression.__init__(mql_InExpression(True, mql_InExpression=mql_Variable()), False, mql_InExpression=mql_Variable()) == None


from python_code import mql_IntegerExpression

def test_mql_IntegerExpression___init__():
    assert mql_IntegerExpression.__init__(mql_IntegerExpression(0), 0) == None


from python_code import mql_LeftJoin

def test_mql_LeftJoin___init__():
    assert mql_LeftJoin.__init__(mql_LeftJoin(True), False) == None


from python_code import mql_LikeExpression
from python_code import mql_Variable

def test_mql_LikeExpression___init__():
    assert mql_LikeExpression.__init__(mql_LikeExpression(False, '\x00', mql_LikeExpression=mql_Variable()), False, '\x00', mql_LikeExpression=mql_Variable()) == None


from python_code import mql_MQuery
from python_code import mql_NamedQuery
from python_code import mql_QueryModule

def test_mql_NamedQuery___init__():
    assert mql_NamedQuery.__init__(mql_NamedQuery('', mql_NamedQuery=mql_QueryModule(), mql_NamedQuery6=mql_MQuery()), '', mql_NamedQuery=mql_QueryModule(), mql_NamedQuery6=mql_MQuery()) == None


from python_code import mql_NullComparisonExpression
from python_code import mql_Variable

def test_mql_NullComparisonExpression___init__():
    assert mql_NullComparisonExpression.__init__(mql_NullComparisonExpression(True, mql_NullComparisonExpression=mql_Variable()), False, mql_NullComparisonExpression=mql_Variable()) == None


from python_code import mql_NullExpression

def test_mql_NullExpression___init__():
    assert mql_NullExpression.__init__(mql_NullExpression(''), '') == None


from python_code import mql_ExpressionTerm
from python_code import mql_OperatorExpression
from python_code import mql_Variable

def test_mql_OperatorExpression___init__():
    assert mql_OperatorExpression.__init__(mql_OperatorExpression('', mql_OperatorExpression=mql_Variable(), mql_OperatorExpression66=mql_ExpressionTerm()), '', mql_OperatorExpression=mql_Variable(), mql_OperatorExpression66=mql_ExpressionTerm()) == None


from python_code import mql_OrderClause
from python_code import mql_SelectStatement

def test_mql_OrderClause___init__():
    assert mql_OrderClause.__init__(mql_OrderClause(False, False, mql_OrderClause18=set(), mql_OrderClause=mql_SelectStatement()), False, False, mql_OrderClause18=set(), mql_OrderClause=mql_SelectStatement()) == None


from python_code import mql_ParameterExpression

def test_mql_ParameterExpression___init__():
    assert mql_ParameterExpression.__init__(mql_ParameterExpression(''), '') == None


from python_code import mql_SelectClause
from python_code import mql_SelectFromClause

def test_mql_SelectClause___init__():
    assert mql_SelectClause.__init__(mql_SelectClause(False, mql_SelectClause=mql_SelectFromClause(), mql_SelectClause42=set()), False, mql_SelectClause=mql_SelectFromClause(), mql_SelectClause42=set()) == None


from python_code import mql_StringExpression

def test_mql_StringExpression___init__():
    assert mql_StringExpression.__init__(mql_StringExpression(''), '') == None

