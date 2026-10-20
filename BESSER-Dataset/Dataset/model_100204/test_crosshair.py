from python_code import query_OrderByOrdinal

def test_query_OrderByOrdinal___init__():
    assert query_OrderByOrdinal.__init__(query_OrderByOrdinal(0), 0) == None


from python_code import query_Predicate

def test_query_Predicate___init__():
    assert query_Predicate.__init__(query_Predicate(False, False, '\x00\x00'), False, False, '') == None


from python_code import query_PredicateIn

def test_query_PredicateIn___init__():
    assert query_PredicateIn.__init__(query_PredicateIn(True), False) == None


from python_code import query_SQLQueryObject

def test_query_SQLQueryObject___init__():
    assert query_SQLQueryObject.__init__(query_SQLQueryObject()) == None

def test_query_SQLQueryObject_setSQL():
    assert query_SQLQueryObject.setSQL(query_SQLQueryObject(), '') == None

def test_query_SQLQueryObject_getSQL():
    assert query_SQLQueryObject.getSQL(query_SQLQueryObject()) == None


from python_code import query_SuperGroup
from python_code import query_SuperGroupElement

def test_query_SuperGroup___init__():
    assert query_SuperGroup.__init__(query_SuperGroup('', SuperGroup=query_SuperGroupElement(), superGroup=set()), '', SuperGroup=query_SuperGroupElement(), superGroup=set()) == None


from python_code import query_QuerySelectStatement
from python_code import query_UpdatabilityExpression
from python_code import query_UpdateOfColumn

def test_query_UpdatabilityExpression___init__():
    assert query_UpdatabilityExpression.__init__(query_UpdatabilityExpression('', UpdatabilityExpression=query_QuerySelectStatement(), updatabilityExpr=set(), UpdatabilityExpression413=query_UpdateOfColumn(), updatabilityExpr416=query_QuerySelectStatement()), '', UpdatabilityExpression=query_QuerySelectStatement(), updatabilityExpr=set(), UpdatabilityExpression413=query_UpdateOfColumn(), updatabilityExpr416=query_QuerySelectStatement()) == None


from python_code import query_ValueExpressionSimple

def test_query_ValueExpressionSimple___init__():
    assert query_ValueExpressionSimple.__init__(query_ValueExpressionSimple(''), '') == None

