from python_code import jPQL_BetweenExpression
from python_code import jPQL_Value
from python_code import jPQL_Variable

def test_jPQL_BetweenExpression___init__():
    assert jPQL_BetweenExpression.__init__(jPQL_BetweenExpression(True, jPQL_BetweenExpression=jPQL_Variable(), jPQL_BetweenExpression90=jPQL_Value(), jPQL_BetweenExpression93=jPQL_Value()), False, jPQL_BetweenExpression=jPQL_Variable(), jPQL_BetweenExpression90=jPQL_Value(), jPQL_BetweenExpression93=jPQL_Value()) == None


from python_code import jPQL_BooleanExpression

def test_jPQL_BooleanExpression___init__():
    assert jPQL_BooleanExpression.__init__(jPQL_BooleanExpression(True), False) == None


from python_code import jPQL_DateTimeExpression

def test_jPQL_DateTimeExpression___init__():
    assert jPQL_DateTimeExpression.__init__(jPQL_DateTimeExpression(''), '') == None


from python_code import jPQL_EmptyComparisonExpression
from python_code import jPQL_Variable

def test_jPQL_EmptyComparisonExpression___init__():
    assert jPQL_EmptyComparisonExpression.__init__(jPQL_EmptyComparisonExpression(True, jPQL_EmptyComparisonExpression=jPQL_Variable()), False, jPQL_EmptyComparisonExpression=jPQL_Variable()) == None


from python_code import jPQL_ExistsExpression
from python_code import jPQL_SelectStatement

def test_jPQL_ExistsExpression___init__():
    assert jPQL_ExistsExpression.__init__(jPQL_ExistsExpression(True, jPQL_ExistsExpression=jPQL_SelectStatement()), False, jPQL_ExistsExpression=jPQL_SelectStatement()) == None


from python_code import jPQL_Function

def test_jPQL_Function___init__():
    assert jPQL_Function.__init__(jPQL_Function('', jPQL_Function=set()), '', jPQL_Function=set()) == None


from python_code import jPQL_InExpression
from python_code import jPQL_Variable

def test_jPQL_InExpression___init__():
    assert jPQL_InExpression.__init__(jPQL_InExpression(True, jPQL_InExpression=jPQL_Variable()), False, jPQL_InExpression=jPQL_Variable()) == None


from python_code import jPQL_IntegerExpression

def test_jPQL_IntegerExpression___init__():
    assert jPQL_IntegerExpression.__init__(jPQL_IntegerExpression(0), 0) == None


from python_code import jPQL_LeftJoin

def test_jPQL_LeftJoin___init__():
    assert jPQL_LeftJoin.__init__(jPQL_LeftJoin(True), False) == None


from python_code import jPQL_LikeExpression
from python_code import jPQL_Variable

def test_jPQL_LikeExpression___init__():
    assert jPQL_LikeExpression.__init__(jPQL_LikeExpression(False, '\x00', jPQL_LikeExpression=jPQL_Variable()), False, '\x00', jPQL_LikeExpression=jPQL_Variable()) == None


from python_code import jPQL_NullComparisonExpression
from python_code import jPQL_Variable

def test_jPQL_NullComparisonExpression___init__():
    assert jPQL_NullComparisonExpression.__init__(jPQL_NullComparisonExpression(True, jPQL_NullComparisonExpression=jPQL_Variable()), False, jPQL_NullComparisonExpression=jPQL_Variable()) == None


from python_code import jPQL_NullExpression

def test_jPQL_NullExpression___init__():
    assert jPQL_NullExpression.__init__(jPQL_NullExpression(''), '') == None


from python_code import jPQL_ExpressionTerm
from python_code import jPQL_OperatorExpression
from python_code import jPQL_Variable

def test_jPQL_OperatorExpression___init__():
    assert jPQL_OperatorExpression.__init__(jPQL_OperatorExpression('', jPQL_OperatorExpression=jPQL_Variable(), jPQL_OperatorExpression61=jPQL_ExpressionTerm()), '', jPQL_OperatorExpression=jPQL_Variable(), jPQL_OperatorExpression61=jPQL_ExpressionTerm()) == None


from python_code import jPQL_OrderClause
from python_code import jPQL_SelectStatement

def test_jPQL_OrderClause___init__():
    assert jPQL_OrderClause.__init__(jPQL_OrderClause(False, False, jPQL_OrderClause=jPQL_SelectStatement(), jPQL_OrderClause11=set()), False, False, jPQL_OrderClause=jPQL_SelectStatement(), jPQL_OrderClause11=set()) == None


from python_code import jPQL_ParameterExpression

def test_jPQL_ParameterExpression___init__():
    assert jPQL_ParameterExpression.__init__(jPQL_ParameterExpression(''), '') == None


from python_code import jPQL_SelectClause
from python_code import jPQL_SelectFromClause

def test_jPQL_SelectClause___init__():
    assert jPQL_SelectClause.__init__(jPQL_SelectClause(False, jPQL_SelectClause=jPQL_SelectFromClause(), jPQL_SelectClause35=set()), False, jPQL_SelectClause=jPQL_SelectFromClause(), jPQL_SelectClause35=set()) == None


from python_code import jPQL_StringExpression

def test_jPQL_StringExpression___init__():
    assert jPQL_StringExpression.__init__(jPQL_StringExpression(''), '') == None

